use serde::{Deserialize, Serialize};
use super::gamification::{BadgeDefinition, Quiz};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DesignPrinciple {
    pub title: String,
    pub urdu_title: String,
    pub description: String,
    pub icon: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SpecializationTrack {
    pub id: String,
    pub title: String,
    pub urdu_title: String,
    pub description: String,
    pub focus_modules: Vec<String>,
    pub target_role: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ResourceLink {
    pub title: String,
    pub url: String,
    pub resource_type: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CodeSnippet {
    pub language: String,
    pub title: String,
    pub code: String,
    pub explanation: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ZeroGpuRecipe {
    pub platform: String,
    pub vram_required: String,
    pub estimated_cost: String,
    pub compute_units_tip: String,
    pub one_click_command: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CloudPlatformRecipe {
    pub platform: String,
    pub vram: String,
    pub weekly_quota: String,
    pub cost: String,
    pub setup_instructions_urdu: String,
    pub setup_snippet: String,
    pub saver_script: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FreeApiProvider {
    pub name: String,
    pub free_tier_limits: String,
    pub speed: String,
    pub best_for: String,
    pub endpoint_url: String,
    pub sample_curl: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ZeroGpuGuide {
    pub title: String,
    pub urdu_subtitle: String,
    pub description: String,
    pub colab_free_t4: CloudPlatformRecipe,
    pub kaggle_dual_t4: CloudPlatformRecipe,
    pub google_one_compute_units_saver: CloudPlatformRecipe,
    pub free_api_providers: Vec<FreeApiProvider>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EngineeringBlog {
    pub id: u32,
    pub slug: String,
    pub title: String,
    pub category: String,
    pub reading_time_minutes: u32,
    pub summary_roman_urdu: String,
    pub content_roman_urdu: String,
    pub code_snippet: Option<String>,
    pub compute_recipe: Option<String>,
    pub diagram_script: String,
    pub diagram_preset: String,
    pub diagram_animation: String,
    pub diagram_svg: Option<String>,
    pub order_index: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ProjectBrief {
    pub title: String,
    pub description: String,
    pub deliverables: Vec<String>,
    pub evaluation_criteria: Vec<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub real_world_deliverable: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub zero_gpu_recipe: Option<ZeroGpuRecipe>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Lesson {
    pub id: u32,
    pub module_slug: String,
    pub slug: String,
    pub title: String,
    pub urdu_title: String,
    pub duration_mins: u32,
    pub xp_reward: u32,
    pub explanation_urdu: String,
    pub code_snippet: Option<CodeSnippet>,
    pub diagram_script: Option<String>,
    pub diagram_svg: Option<String>,
    pub key_takeaways: Vec<String>,
    pub resources: Vec<ResourceLink>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Module {
    pub id: u32,
    pub phase_id: u32,
    pub slug: String,
    pub week: u32,
    pub title: String,
    pub urdu_title: String,
    pub description: String,
    pub diagram_script: String,
    pub diagram_svg: Option<String>,
    pub lessons: Vec<Lesson>,
    pub quiz: Quiz,
    pub resources: Vec<ResourceLink>,
    pub project: Option<ProjectBrief>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub real_world_deliverable: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub zero_gpu_recipe: Option<ZeroGpuRecipe>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub practice_checkpoint: Option<PracticeCheckpoint>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PracticeCheckpoint {
    pub title: String,
    pub urdu_title: String,
    pub description: String,
    pub colab_url: String,
    pub checklist: Vec<String>,
    pub xp_reward: u32,
    pub badge_name: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PhaseSummary {
    pub id: u32,
    pub slug: String,
    pub title: String,
    pub urdu_title: String,
    pub week_range: String,
    pub module_count: usize,
    pub lesson_count: usize,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Phase {
    pub id: u32,
    pub slug: String,
    pub title: String,
    pub urdu_title: String,
    pub week_range: String,
    pub description: String,
    pub outcome: String,
    pub modules: Vec<Module>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CourseOverview {
    pub title: String,
    pub subtitle: String,
    pub description: String,
    pub language: String,
    pub total_weeks: u32,
    pub total_phases: u32,
    pub total_modules: u32,
    pub total_lessons: u32,
    pub total_hours: u32,
    pub design_principles: Vec<DesignPrinciple>,
    pub tracks: Vec<SpecializationTrack>,
    pub badges: Vec<BadgeDefinition>,
    pub phases: Vec<PhaseSummary>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub zero_gpu_guide: Option<ZeroGpuGuide>,
}
