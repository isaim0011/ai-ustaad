use axum::{extract::State, Json};
use crate::{
    db::AppState,
    error::AppError,
    models::{DiagramRenderRequest, DiagramRenderResponse, GalleryDiagram},
    services::DiagramService,
};

pub async fn render_diagram(
    State(_state): State<AppState>,
    Json(req): Json<DiagramRenderRequest>,
) -> Result<Json<DiagramRenderResponse>, AppError> {
    let res = DiagramService::render(&req)?;
    Ok(Json(res))
}

pub async fn get_gallery(
    State(_state): State<AppState>,
) -> Json<Vec<GalleryDiagram>> {
    let gallery = DiagramService::get_gallery();
    Json(gallery)
}
