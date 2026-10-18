use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DiagramRenderRequest {
    pub script: String,
    #[serde(default)]
    pub preset: Option<String>,
    #[serde(default)]
    pub mode: Option<String>,
    #[serde(default)]
    pub animate: Option<String>,
    #[serde(default)]
    pub speed: Option<f32>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DiagramIssueModel {
    pub code: String,
    pub message: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DiagramRenderResponse {
    pub svg: String,
    pub width: f32,
    pub height: f32,
    pub valid: bool,
    pub issues: Vec<DiagramIssueModel>,
    pub lint: Vec<String>,
    pub kind: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GalleryDiagram {
    pub id: String,
    pub title: String,
    pub urdu_title: String,
    pub category: String,
    pub script: String,
    pub svg: String,
    pub description: String,
}
