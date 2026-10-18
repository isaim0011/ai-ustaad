use axum::{extract::State, Json};
use serde_json::{json, Value};
use crate::db::AppState;

pub async fn health_check(State(state): State<AppState>) -> Json<Value> {
    let db_connected = state.pool.is_some();
    Json(json!({
        "status": "ok",
        "service": "ai-mastery-backend",
        "version": "0.1.0",
        "database_connected": db_connected,
        "total_modules": state.syllabus.course.total_modules,
        "total_lessons": state.syllabus.course.total_lessons,
        "diagramkit_native": true,
        "timestamp": chrono::Utc::now().to_rfc3339()
    }))
}
