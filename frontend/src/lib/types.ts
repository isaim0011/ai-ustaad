// TypeScript Definitions for AI Ustaad Platform
// Includes Phase, Module, Lesson, Practice Checkpoint and Hugging Face Sub-Projects

export interface HfSubproject {
	module_number: number;
	module_slug: string;
	project_title: string;
	project_slug: string;
	hf_model: string;
	hf_model_url: string;
	hf_dataset: string;
	hf_dataset_url: string;
	colab_url: string;
	colab_notebook_url?: string;
	kaggle_url: string;
	kaggle_notebook_url?: string;
	hardware_requirement: string;
	estimated_runtime_seconds: string;
	key_learning_takeaway: string;
	starter_code: string;
	runnable_starter_code?: string;
	gradio_code: string;
	gradio_demo_code?: string;
}

export interface PracticeProject {
	title: string;
	humorous_badge?: string;
	description_roman_urdu?: string;
	colab_url: string;
	xp_reward: number;
	checklist: string[];
	hf_subproject?: HfSubproject;
}

export interface PracticeCheckpoint {
	title: string;
	urdu_title?: string;
	description?: string;
	colab_url: string;
	checklist: string[];
	xp_reward?: number;
	badge_name?: string;
	hf_subproject?: HfSubproject;
}

export interface ZeroGpuRecipe {
	platform: string;
	vram_required: string;
	estimated_cost: string;
	compute_units_tip: string;
	one_click_command: string;
	unassign_code?: string;
}

export interface LessonData {
	id: string;
	module_id: string;
	lesson_code: string;
	slug: string;
	title: string;
	duration_minutes: number;
	lesson_type: string;
	roman_urdu_content: string;
	english_summary: string;
	code_example: string;
	xp_reward: number;
	order_index: number;
	diagram_script?: string;
	diagram_type?: string;
	resources?: { title: string; url: string }[];
}

export interface ModuleData {
	id: string;
	phase_id?: string;
	module_number: number;
	slug: string;
	title: string;
	weeks_range: string;
	estimated_hours: number;
	real_world_deliverable: string;
	badge_slug?: string;
	order_index: number;
	diagram_script?: string;
	diagram_preset?: string;
	diagram_animation?: string;
	zero_gpu_recipe?: ZeroGpuRecipe;
	practice_project?: PracticeProject;
	practice_checkpoint?: PracticeCheckpoint;
	learning_outcomes?: string[];
	practical_tasks?: string[];
	lessons?: LessonData[];
}

export interface PhaseData {
	id: string;
	phase_number: number;
	slug: string;
	title: string;
	weeks_range: string;
	level: string;
	description: string;
	order_index: number;
	modules: ModuleData[];
}
