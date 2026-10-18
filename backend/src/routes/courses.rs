use axum::{
    extract::{Path, State},
    Json,
};
use serde_json::{json, Value};
use crate::{
    db::AppState,
    error::AppError,
    models::{CourseOverview, EngineeringBlog, Lesson, Module, Phase, ZeroGpuGuide},
};

pub async fn get_course(State(state): State<AppState>) -> Json<CourseOverview> {
    Json(state.syllabus.course.clone())
}

pub async fn get_phases(State(state): State<AppState>) -> Json<Vec<Phase>> {
    Json(state.syllabus.phases.clone())
}

pub async fn get_modules(State(state): State<AppState>) -> Json<Value> {
    let modules = state.syllabus.get_all_modules();
    let summaries: Vec<Value> = modules
        .iter()
        .map(|m| {
            json!({
                "id": m.id,
                "phase_id": m.phase_id,
                "slug": m.slug,
                "week": m.week,
                "title": m.title,
                "urdu_title": m.urdu_title,
                "description": m.description,
                "lesson_count": m.lessons.len(),
                "diagram_script": m.diagram_script,
                "real_world_deliverable": m.real_world_deliverable,
                "zero_gpu_recipe": m.zero_gpu_recipe,
                "practice_checkpoint": m.practice_checkpoint,
            })
        })
        .collect();

    Json(json!(summaries))
}

pub async fn get_module_by_slug(
    Path(slug): Path<String>,
    State(state): State<AppState>,
) -> Result<Json<Module>, AppError> {
    let module = state
        .syllabus
        .get_module(&slug)
        .ok_or_else(|| AppError::NotFound(format!("Module `{slug}` not found")))?;

    Ok(Json(module.clone()))
}

pub async fn get_lesson_by_slug(
    Path(slug): Path<String>,
    State(state): State<AppState>,
) -> Result<Json<Lesson>, AppError> {
    let (_module, lesson) = state
        .syllabus
        .get_lesson(&slug)
        .ok_or_else(|| AppError::NotFound(format!("Lesson `{slug}` not found")))?;

    Ok(Json(lesson.clone()))
}

pub async fn get_blogs(State(state): State<AppState>) -> Json<Vec<EngineeringBlog>> {
    Json(state.syllabus.get_blogs().to_vec())
}

pub async fn get_blog_by_slug(
    Path(slug): Path<String>,
    State(state): State<AppState>,
) -> Result<Json<EngineeringBlog>, AppError> {
    let blog = state
        .syllabus
        .get_blog(&slug)
        .ok_or_else(|| AppError::NotFound(format!("Blog `{slug}` not found")))?;

    Ok(Json(blog.clone()))
}

pub async fn get_cloud_guide(State(state): State<AppState>) -> Json<ZeroGpuGuide> {
    Json(state.syllabus.get_cloud_guide().clone())
}

