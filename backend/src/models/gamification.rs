use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BadgeDefinition {
    pub id: String,
    pub title: String,
    pub urdu_title: String,
    pub description: String,
    pub icon: String,
    pub xp_requirement: u32,
    pub module_requirement: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct QuizQuestion {
    pub id: u32,
    pub question: String,
    pub urdu_question: String,
    pub options: Vec<String>,
    pub correct_index: usize,
    pub explanation_urdu: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Quiz {
    pub id: String,
    pub module_slug: String,
    pub title: String,
    pub questions: Vec<QuizQuestion>,
    pub passing_score: u32,
    pub xp_reward: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct QuizSubmission {
    pub answers: Vec<usize>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct QuizAnswerFeedback {
    pub question_id: u32,
    pub correct: bool,
    pub selected_index: usize,
    pub correct_index: usize,
    pub explanation_urdu: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct QuizResult {
    pub score_percent: u32,
    pub passed: bool,
    pub xp_awarded: u32,
    pub new_badges: Vec<BadgeDefinition>,
    pub detailed_feedback: Vec<QuizAnswerFeedback>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct UserProfile {
    pub user_id: String,
    pub username: String,
    pub email: Option<String>,
    pub total_xp: u32,
    pub current_level: u32,
    pub current_streak: u32,
    pub longest_streak: u32,
    pub completed_lessons: Vec<String>,
    pub completed_modules: Vec<String>,
    pub unlocked_badges: Vec<String>,
    pub quiz_scores: HashMap<String, u32>,
    pub last_active_date: Option<String>,
}

impl Default for UserProfile {
    fn default() -> Self {
        Self {
            user_id: "guest-user".to_string(),
            username: "AI Explorer".to_string(),
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
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ProgressCompleteRequest {
    pub lesson_slug: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ProgressCompleteResponse {
    pub success: bool,
    pub xp_awarded: u32,
    pub total_xp: u32,
    pub current_level: u32,
    pub current_streak: u32,
    pub unlocked_badges: Vec<BadgeDefinition>,
    pub message_urdu: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct WeeklyChallenge {
    pub id: String,
    pub week: u32,
    pub title: String,
    pub urdu_title: String,
    pub description_urdu: String,
    pub xp_reward: u32,
    pub badge_reward: Option<String>,
}
