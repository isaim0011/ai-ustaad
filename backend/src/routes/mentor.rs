use axum::{extract::State, Json};
use crate::{
    db::AppState,
    error::AppError,
    services::mentor_service::{MentorChatRequest, MentorChatResponse, MentorService},
};

pub async fn ask_mentor(
    State(_state): State<AppState>,
    Json(req): Json<MentorChatRequest>,
) -> Result<Json<MentorChatResponse>, AppError> {
    let res = MentorService::answer(&req)?;
    Ok(Json(res))
}
