use axum::{
    extract::{Path, State},
    Json,
};
use crate::{
    auth::AuthenticatedUser,
    db::AppState,
    error::AppError,
    models::{
        ProgressCompleteRequest, ProgressCompleteResponse, QuizResult, QuizSubmission, UserProfile,
    },
};

pub async fn get_progress(
    user: AuthenticatedUser,
    State(state): State<AppState>,
) -> Json<UserProfile> {
    let profile = state.get_user_profile(&user.user_id).await;
    Json(profile)
}

pub async fn complete_lesson(
    user: AuthenticatedUser,
    State(state): State<AppState>,
    Json(req): Json<ProgressCompleteRequest>,
) -> Result<Json<ProgressCompleteResponse>, AppError> {
    let res = state.complete_lesson(&user.user_id, &req.lesson_slug).await?;
    Ok(Json(res))
}

pub async fn submit_quiz(
    user: AuthenticatedUser,
    Path(module_slug): Path<String>,
    State(state): State<AppState>,
    Json(req): Json<QuizSubmission>,
) -> Result<Json<QuizResult>, AppError> {
    let res = state.submit_quiz(&user.user_id, &module_slug, &req.answers).await?;
    Ok(Json(res))
}
