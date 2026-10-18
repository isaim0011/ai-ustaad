pub mod courses;
pub mod diagrams;
pub mod health;
pub mod mentor;
pub mod progress;

use axum::{
    routing::{get, post},
    Router,
};
use crate::db::AppState;

pub fn create_router(state: AppState) -> Router {
    Router::new()
        .route("/api/health", get(health::health_check))
        .route("/api/course", get(courses::get_course))
        .route("/api/phases", get(phases_handler))
        .route("/api/modules", get(courses::get_modules))
        .route("/api/modules/{slug}", get(courses::get_module_by_slug))
        .route("/api/lessons/{slug}", get(courses::get_lesson_by_slug))
        .route("/api/blogs", get(courses::get_blogs))
        .route("/api/blogs/{slug}", get(courses::get_blog_by_slug))
        .route("/api/cloud-guide", get(courses::get_cloud_guide))
        .route("/api/diagrams/render", post(diagrams::render_diagram))
        .route("/api/diagrams/gallery", get(diagrams::get_gallery))
        .route("/api/progress", get(progress::get_progress))
        .route("/api/progress/complete", post(progress::complete_lesson))
        .route("/api/quizzes/{module_slug}/submit", post(progress::submit_quiz))
        .route("/api/ai/mentor", post(mentor::ask_mentor))
        .with_state(state)
}

async fn phases_handler(
    state: axum::extract::State<AppState>,
) -> axum::Json<Vec<crate::models::Phase>> {
    courses::get_phases(state).await
}
