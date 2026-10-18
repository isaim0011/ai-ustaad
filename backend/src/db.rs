use std::{collections::HashMap, str::FromStr, sync::Arc};
use tokio::sync::RwLock;
use sqlx::postgres::{PgConnectOptions, PgPoolOptions};
use sqlx::PgPool;

use crate::{
    config::Config,
    error::AppError,
    models::{
        ProgressCompleteResponse, QuizAnswerFeedback, QuizResult, UserProfile,
    },
    services::SyllabusStore,
};

#[derive(Clone)]
pub struct AppState {
    pub pool: Option<PgPool>,
    pub config: Arc<Config>,
    pub syllabus: Arc<SyllabusStore>,
    pub memory_users: Arc<RwLock<HashMap<String, UserProfile>>>,
}

impl AppState {
    pub async fn new(config: Arc<Config>) -> Self {
        let pool = if let Some(ref db_url) = config.database_url {
            tracing::info!("Connecting to PostgreSQL database: {}", db_url);
            match PgConnectOptions::from_str(db_url) {
                Ok(mut opts) => {
                    // Critical for Supabase Supavisor transaction pooler (port 6543)
                    opts = opts.statement_cache_capacity(0);
                    match PgPoolOptions::new()
                        .max_connections(10)
                        .connect_with(opts)
                        .await
                    {
                        Ok(p) => {
                            tracing::info!("Successfully connected to PostgreSQL / Supabase!");
                            Some(p)
                        }
                        Err(e) => {
                            tracing::warn!("Could not connect to PostgreSQL: {e}. Falling back to high-speed in-memory store.");
                            None
                        }
                    }
                }
                Err(e) => {
                    tracing::warn!("Invalid DATABASE_URL format: {e}. Falling back to in-memory store.");
                    None
                }
            }
        } else {
            tracing::info!("No DATABASE_URL configured. Running with in-memory dynamic state + standalone demo store.");
            None
        };

        let syllabus = Arc::new(SyllabusStore::new());
        let mut initial_users = HashMap::new();
        initial_users.insert("guest-user".to_string(), UserProfile::default());

        Self {
            pool,
            config,
            syllabus,
            memory_users: Arc::new(RwLock::new(initial_users)),
        }
    }

    pub async fn get_user_profile(&self, user_id: &str) -> UserProfile {
        let mut lock = self.memory_users.write().await;
        lock.entry(user_id.to_string())
            .or_insert_with(|| UserProfile {
                user_id: user_id.to_string(),
                username: "AI Student".to_string(),
                email: None,
                total_xp: 0,
                current_level: 1,
                current_streak: 1,
                longest_streak: 1,
                completed_lessons: Vec::new(),
                completed_modules: Vec::new(),
                unlocked_badges: Vec::new(),
                quiz_scores: HashMap::new(),
                last_active_date: Some(chrono::Utc::now().format("%Y-%m-%d").to_string()),
            })
            .clone()
    }

    pub async fn complete_lesson(
        &self,
        user_id: &str,
        lesson_slug: &str,
    ) -> Result<ProgressCompleteResponse, AppError> {
        let (module, lesson) = self
            .syllabus
            .get_lesson(lesson_slug)
            .ok_or_else(|| AppError::NotFound(format!("Lesson `{lesson_slug}` not found")))?;

        let mut lock = self.memory_users.write().await;
        let profile = lock.entry(user_id.to_string()).or_insert_with(UserProfile::default);

        let already_completed = profile.completed_lessons.contains(&lesson_slug.to_string());
        let mut xp_awarded = 0;
        let mut newly_unlocked_badges = Vec::new();

        if !already_completed {
            profile.completed_lessons.push(lesson_slug.to_string());
            xp_awarded = lesson.xp_reward;
            profile.total_xp += xp_awarded;
            profile.current_level = 1 + (profile.total_xp / 500);

            // Check if all lessons of the module are completed
            let module_all_done = module
                .lessons
                .iter()
                .all(|l| profile.completed_lessons.contains(&l.slug));
            if module_all_done && !profile.completed_modules.contains(&module.slug) {
                profile.completed_modules.push(module.slug.clone());
            }

            // Check badge unlocks
            for badge in &self.syllabus.course.badges {
                if profile.unlocked_badges.contains(&badge.id) {
                    continue;
                }

                let xp_ok = profile.total_xp >= badge.xp_requirement;
                let module_ok = match &badge.module_requirement {
                    Some(req_module) => profile.completed_modules.contains(req_module),
                    None => true,
                };

                if xp_ok && module_ok {
                    profile.unlocked_badges.push(badge.id.clone());
                    newly_unlocked_badges.push(badge.clone());
                }
            }
        }

        let total_xp = profile.total_xp;
        let current_level = profile.current_level;
        let current_streak = profile.current_streak;

        let message_urdu = if already_completed {
            "Aap pehle hi yeh lesson complete kar chuke hain! XP pehle se add ho chuki hai.".to_string()
        } else {
            format!("Mubarak ho! Aapne `{}` complete kar liya aur {} XP hasil ki!", lesson.urdu_title, xp_awarded)
        };

        Ok(ProgressCompleteResponse {
            success: true,
            xp_awarded,
            total_xp,
            current_level,
            current_streak,
            unlocked_badges: newly_unlocked_badges,
            message_urdu,
        })
    }

    pub async fn submit_quiz(
        &self,
        user_id: &str,
        module_slug: &str,
        answers: &[usize],
    ) -> Result<QuizResult, AppError> {
        let module = self
            .syllabus
            .get_module(module_slug)
            .ok_or_else(|| AppError::NotFound(format!("Module `{module_slug}` not found")))?;

        let quiz = &module.quiz;
        let mut correct_count = 0;
        let mut feedback = Vec::new();

        for (i, q) in quiz.questions.iter().enumerate() {
            let selected = answers.get(i).copied().unwrap_or(999);
            let is_correct = selected == q.correct_index;
            if is_correct {
                correct_count += 1;
            }
            feedback.push(QuizAnswerFeedback {
                question_id: q.id,
                correct: is_correct,
                selected_index: selected,
                correct_index: q.correct_index,
                explanation_urdu: q.explanation_urdu.clone(),
            });
        }

        let total_questions = quiz.questions.len().max(1);
        let score_percent = ((correct_count * 100) / total_questions) as u32;
        let passed = score_percent >= quiz.passing_score;

        let mut xp_awarded = 0;
        let mut new_badges = Vec::new();

        if passed {
            let mut lock = self.memory_users.write().await;
            let profile = lock.entry(user_id.to_string()).or_insert_with(UserProfile::default);

            let prev_score = profile.quiz_scores.get(module_slug).copied().unwrap_or(0);
            if prev_score < quiz.passing_score {
                xp_awarded = quiz.xp_reward;
                profile.total_xp += xp_awarded;
                profile.current_level = 1 + (profile.total_xp / 500);
            }

            profile.quiz_scores.insert(module_slug.to_string(), score_percent);

            // Check badges that require this module
            for badge in &self.syllabus.course.badges {
                if profile.unlocked_badges.contains(&badge.id) {
                    continue;
                }
                if let Some(ref req_mod) = badge.module_requirement {
                    if req_mod == module_slug && profile.total_xp >= badge.xp_requirement {
                        profile.unlocked_badges.push(badge.id.clone());
                        new_badges.push(badge.clone());
                    }
                }
            }
        }

        Ok(QuizResult {
            score_percent,
            passed,
            xp_awarded,
            new_badges,
            detailed_feedback: feedback,
        })
    }
}
