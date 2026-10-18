-- ==============================================================================
-- AI USTAAD PLATFORM: 002_seed_syllabus.sql
-- Complete 20-Week Roman Urdu AI Engineering Curriculum (Zero Se Hero Tak)
-- 5 Phases, 14 Modules, 3 Tracks, 11 Badges, 84 Lessons, 70 Quiz Questions & 8 Challenges
-- Official Portal: https://ai-ustaad.pages.dev
-- ==============================================================================

-- 1. GAMIFICATION BADGES
insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('chai-munshi', 'Chai Wala Munshi', 'Python Zero Se Hero', 'Completed Module 0: Python Zero Se Hero and solved the Chai Shop billing checkpoint!', '☕', 100, '{"type": "module_complete", "module_slug": "python-zero-se-hero"}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;

insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('pehla-prompt', 'Pehla Prompt', 'Safar Ka Aaghaz', 'Completed your very first lesson on AI Ustaad!', '🚀', 50, '{"type": "lesson_count", "threshold": 1}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;

insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('prompt-rookie', 'Prompt Rookie', 'Prompts Ka Ustaad', 'Mastered zero-shot, few-shot, CoT and prompt engineering patterns.', '🎯', 100, '{"type": "module_complete", "module_slug": "prompt-engineering-and-llm-mental-models"}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;

insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('ml-practitioner', 'ML Practitioner', 'Data Se Model Tak', 'Mastered classical machine learning, feature pipelines, and metrics.', '📊', 150, '{"type": "module_complete", "module_slug": "classical-machine-learning"}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;

insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('transformer-expert', 'Transformer Expert', 'Attention Is All You Need', 'Built multi-head attention and transformer blocks from raw tensors.', '🧠', 200, '{"type": "module_complete", "module_slug": "attention-and-transformers-under-the-hood"}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;

insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('app-builder', 'App Builder', 'Full-Stack AI Creator', 'Shipped production-grade AI applications and streaming APIs.', '⚡', 250, '{"type": "module_complete", "module_slug": "building-ai-applications-and-apis"}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;

insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('rag-master', 'RAG Master', 'Context & Retrieval Wizard', 'Architected advanced hybrid RAG pipelines with ColPali and reranking.', '🔍', 300, '{"type": "module_complete", "module_slug": "vector-databases-and-modern-rag"}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;

insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('agent-architect', 'Agent Architect', 'Autonomous Systems Master', 'Created autonomous multi-agent swarms with Anthropic MCP and smolagents.', '🤖', 350, '{"type": "module_complete", "module_slug": "autonomous-agents-and-tool-use"}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;

insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('finetuning-pro', 'Fine-tuning Pro', 'LoRA & Unsloth Wizard', 'Fine-tuned open-source models with Unsloth and DeepSeek-R1 GRPO.', '🔥', 400, '{"type": "module_complete", "module_slug": "fine-tuning-and-model-adaptation"}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;

insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('production-ready', 'Production Ready', '0 to 1 Million Requests', 'Deployed low-latency LLM microservices with vLLM, Docker and Rust.', '🛡️', 450, '{"type": "module_complete", "module_slug": "production-ai-engineering-mlops"}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;

insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('ai-graduate', 'AI Graduate', 'Hero Ban Gaye!', 'Successfully completed the entire AI Ustaad curriculum and Capstone project.', '🎓', 1000, '{"type": "module_complete", "module_slug": "enterprise-capstone-and-career-launch"}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;

insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ('top-performer', 'Top Performer', '90%+ Quiz Score Champion', 'Achieved 90% or higher score on a module quiz.', '👑', 200, '{"type": "quiz_score", "min_score": 90}'::jsonb)
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;


-- 2. COURSE
insert into public.courses (slug, title, subtitle, description, language, total_weeks, level, design_principles, zero_gpu_guide, is_published)
values (
  'ai-mastery-zero-to-production',
  'AI Ustaad — AI Mastery: Zero Se Production Tak',
  'Pakistan aur South Asia Ka Pehla Complete, Production-Grade Roman Urdu AI Engineering Curriculum (ai-ustaad.pages.dev)',
  '20 hafton ka mukammal safar: Python aur linear algebra ki bunyad se le kar Deep Learning, Transformers, Modern RAG, Autonomous Multi-Agent Systems, DeepSeek-R1 GRPO, Anthropic MCP, aur Production MLOps tak (ai-ustaad.pages.dev).',
  'roman-urdu',
  20,
  'Zero to Hero (Beginner to Production)',
  '["Zero Hand-Waving: Math & Tensors first-principles se samjhein", "Roman Urdu Intuition + Global English Standards", "2026 SOTA First: DeepSeek-R1 GRPO, Anthropic MCP, ColPali, Unsloth", "Code in Production: Rust, PyTorch, vLLM, Docker", "Interactive Animated Diagrams (DiagramKit) har concept ke liye"]'::jsonb,
  '{"title": "Zero-GPU Cloud Compute Survival Guide 2026", "urdu_subtitle": "Bina local GPU ke Google Colab, Kaggle Dual-T4, Google One Pro 1000 Units aur Free SOTA APIs ka blueprint", "description": "Agar aapke pas local GPU nahi hai to pareshan hone ki bilkul zaroorat nahi! Colab Free T4, Kaggle 30h/wk Dual T4, Google One Pro compute units aur Free SOTA API providers ke zariye 100% free model training karein.", "colab_free_t4": {"platform": "Google Colab Free Tier (Nvidia T4 15GB VRAM)", "vram": "15 GB GDDR6", "weekly_quota": "Approx 12-16 hours per session (resets daily)", "cost": "$0.00 (100% Free)", "setup_instructions_urdu": "Runtime type -> T4 GPU select karein. Training ke baad runtime unassign zaroor karein.", "setup_snippet": "!pip install -q torch transformers datasets accelerate bitsandbytes peft trl unsloth", "saver_script": "from google.colab import runtime\nruntime.unassign()"}, "kaggle_dual_t4": {"platform": "Kaggle Notebooks (Dual Nvidia T4 2x15GB = 30GB VRAM)", "vram": "30 GB Combined VRAM", "weekly_quota": "30 Hours per week", "cost": "$0.00 (100% Free phone-verified account)", "setup_instructions_urdu": "Accelerator -> GPU T4 x 2 select karein. 14B models PyTorch DDP se train karein.", "setup_snippet": "!accelerate config default", "saver_script": "import os\nos.system(''kaggle datasets version -p ./weights -m \"Auto save\"'')"}, "google_one_compute_units_saver": {"platform": "Google One Pro / Colab Pro (100 - 1000 Compute Units Optimizer)", "vram": "Nvidia A100 (40GB/80GB) ya L4 (24GB)", "weekly_quota": "100 to 1000 Compute Units", "cost": "Google One AI Premium bundle ($19.99/mo) or standalone", "setup_instructions_urdu": "Hamesha Python try-finally block mein runtime.unassign() lagayein taake raat bhar compute units burn na hon.", "setup_snippet": "# Run heavy 70B LoRA or Unsloth GRPO on A100 GPU", "saver_script": "try:\n    pass\nfinally:\n    from google.colab import runtime\n    runtime.unassign()"}, "free_api_providers": [{"name": "Groq Cloud Free Tier", "free_tier_limits": "30 requests/min, 14,400 requests/day, 6,000 tokens/min", "speed": "300 - 500 tokens/sec", "best_for": "Ultra-low latency LLM inference, Llama 3.3 70B, real-time agent tool loops", "endpoint_url": "https://api.groq.com/openai/v1/chat/completions", "sample_curl": "curl -X POST https://api.groq.com/openai/v1/chat/completions ..."}, {"name": "Google AI Studio (Gemini 2.0 Flash / Pro)", "free_tier_limits": "15 requests/min, 1,500 requests/day, 1M token context window", "speed": "150 - 200 tokens/sec", "best_for": "Massive context analysis (books, PDFs, video), multimodal vision, complex reasoning", "endpoint_url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent", "sample_curl": "curl \"https://generativelanguage.googleapis.com/...\""}, {"name": "Cerebras Inference Free Tier", "free_tier_limits": "30 requests/min, 1M tokens/day", "speed": "1,800+ tokens/sec (World''s Fastest Inference)", "best_for": "Instant speculative decoding, synthetic data generation, high-frequency agent thoughts", "endpoint_url": "https://api.cerebras.ai/v1/chat/completions", "sample_curl": "curl -X POST https://api.cerebras.ai/v1/chat/completions ..."}]}'::jsonb,
  true
)
on conflict (slug) do update set
  title = excluded.title,
  subtitle = excluded.subtitle,
  description = excluded.description,
  design_principles = excluded.design_principles,
  zero_gpu_guide = excluded.zero_gpu_guide;


-- 3. PHASES (6 PHASES: PREREQUISITE + 5 AI PHASES)
insert into public.phases (course_id, phase_number, slug, title, weeks_range, level, description, diagram_script, order_index)
select id, 0, 'phase-0-python-prerequisite', 'Prerequisite Track: Python Zero Se Hero', 'Weeks 0', 'Absolute Beginner', 'Naye hain aur Python nahi aati? Pehle Python Zero Se Hero complete karein, phir AI Mastery shuru karein! Variables, Loops, OOP, JSON, APIs aur NumPy foundations.', '@preset midnight
@animate flow
flow LR: Python Zero Se Hero Pipeline
  p1[0.1: Variables & Logic] $terminal -> p2[0.2: Functions & Types] ~info $code
  p2 -> p3[0.3: Lists & Dicts] ~purple $database
  p3 -> p4[0.4: OOP & Dataclass] ~teal $brain
  p4 -> p5[0.5: Files, JSON & APIs] ~warn $server
  p5 -> p6[0.6: NumPy & Fast Math]* ~ok $cpu', 0
from public.courses where slug = 'ai-mastery-zero-to-production'
on conflict (slug) do update set
  phase_number = excluded.phase_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  level = excluded.level,
  description = excluded.description,
  diagram_script = excluded.diagram_script,
  order_index = excluded.order_index;

insert into public.phases (course_id, phase_number, slug, title, weeks_range, level, description, diagram_script, order_index)
select id, 1, 'phase-1-foundations', 'Phase 1: Foundations & Python Mastery', 'Weeks 1-4', 'Beginner', 'Pehle Python (Module 0: Python Zero Se Hero), phir NumPy tensors, Vector math, Prompt Engineering aur LLM mental models.', '@preset midnight
@animate flow
flow LR: Phase 1 Foundations
  py0[Module 0: Python Zero Se Hero] $python -> py[Module 1: NumPy & Fast Math] $cpu
  py -> prompt[Module 2: Prompt Engineering & LLMs] $terminal
  prompt -> first_app[Pehla AI Prototype] $cube *', 1
from public.courses where slug = 'ai-mastery-zero-to-production'
on conflict (slug) do update set
  phase_number = excluded.phase_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  level = excluded.level,
  description = excluded.description,
  diagram_script = excluded.diagram_script,
  order_index = excluded.order_index;

insert into public.phases (course_id, phase_number, slug, title, weeks_range, level, description, diagram_script, order_index)
select id, 2, 'phase-2-core-ml-deeplearning', 'Phase 2: Core ML & Deep Learning', 'Weeks 5-8', 'Intermediate', 'Scikit-learn se Gradient Descent, PyTorch neural networks, Backpropagation, aur Transformer Attention mechanism.', '@preset midnight
@animate pulse
flow LR: Phase 2 Core ML to Deep Learning
  ml[Classical ML & Trees] $database -> torch[PyTorch Tensors & Autograd] $cpu
  torch -> mlp[Neural Networks MLP] $layers
  mlp -> attn[Attention & Transformers] $brain *', 2
from public.courses where slug = 'ai-mastery-zero-to-production'
on conflict (slug) do update set
  phase_number = excluded.phase_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  level = excluded.level,
  description = excluded.description,
  diagram_script = excluded.diagram_script,
  order_index = excluded.order_index;

insert into public.phases (course_id, phase_number, slug, title, weeks_range, level, description, diagram_script, order_index)
select id, 3, 'phase-3-modern-genai-stack', 'Phase 3: Modern GenAI Stack & RAG', 'Weeks 9-12', 'Advanced', 'Embeddings, Vector Databases, Advanced RAG (Hybrid Search, Re-ranking, ColPali), aur Multi-Agent Systems with Anthropic MCP & smolagents.', '@preset midnight
@animate flow
flow LR: Phase 3 Modern GenAI Stack
  apis[Streaming LLM APIs] $server -> rag[Advanced RAG & ColPali] $database
  rag -> mcp[Anthropic MCP Tools] $code
  mcp -> agents[Autonomous Multi-Agent Swarms] $brain *', 3
from public.courses where slug = 'ai-mastery-zero-to-production'
on conflict (slug) do update set
  phase_number = excluded.phase_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  level = excluded.level,
  description = excluded.description,
  diagram_script = excluded.diagram_script,
  order_index = excluded.order_index;

insert into public.phases (course_id, phase_number, slug, title, weeks_range, level, description, diagram_script, order_index)
select id, 4, 'phase-4-production-mlops', 'Phase 4: Fine-Tuning & Production MLOps', 'Weeks 13-16', 'Expert', 'LoRA/QLoRA with Unsloth, DeepSeek-R1 GRPO reasoning, Quantization (GGUF/AWQ), High-throughput inference with vLLM aur Rust Axum microservices.', '@preset midnight
@animate flow
flow LR: Phase 4 Fine-Tuning & Production MLOps
  unsloth[Unsloth LoRA & QLoRA] $cpu -> grpo[DeepSeek-R1 GRPO RL] $brain
  grpo -> vllm[vLLM PagedAttention] $server
  vllm -> rust[Rust Axum Microservice] $lock *', 4
from public.courses where slug = 'ai-mastery-zero-to-production'
on conflict (slug) do update set
  phase_number = excluded.phase_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  level = excluded.level,
  description = excluded.description,
  diagram_script = excluded.diagram_script,
  order_index = excluded.order_index;

insert into public.phases (course_id, phase_number, slug, title, weeks_range, level, description, diagram_script, order_index)
select id, 5, 'phase-5-specialization-capstone', 'Phase 5: Specialization & Enterprise Capstone', 'Weeks 17-20', 'Mastery', 'Three specialized tracks (AI Developers, AI Business/Product, AI Research), end-to-end multi-tenant enterprise AI system with auth, evaluation, telemetry & global deployment.', '@preset midnight
@animate pulse
arch LR: Phase 5 Specialization & Capstone
  tracks[Specialization Tracks A / B / C] $terminal -> capstone[Multi-Tenant Enterprise AI] $server *
  capstone -> eval[Ragas & Guardrails] $lock
  capstone -> cloud[Global Cloud & Portfolio] $cloud', 5
from public.courses where slug = 'ai-mastery-zero-to-production'
on conflict (slug) do update set
  phase_number = excluded.phase_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  level = excluded.level,
  description = excluded.description,
  diagram_script = excluded.diagram_script,
  order_index = excluded.order_index;


-- 4. SPECIALIZATION TRACKS
insert into public.specialization_tracks (course_id, track_code, slug, title, description, topics, diagram_script)
select id, 'TRACK-A', 'track-a-developers', 'Track A: AI for Software Developers', 'Full-stack AI systems, high-concurrency Rust backends, streaming UI with Svelte/React, WebSocket agents, custom tool integration (MCP), and production deployment.', '["High-Scale Rust & Go AI Microservices", "Custom MCP Tools & Plugin Engineering", "Streaming WebSocket & SSE Architectures", "vLLM & TensorRT-LLM Infrastructure", "Real-Time Agent Swarms"]'::jsonb, '@preset midnight
@animate flow
flow LR: Track A: Software Developer Pathway
  fe[Svelte 5 / Next.js Client] $browser -> gw[Rust Axum Gateway] $server *
  gw -> mcp[Anthropic MCP Tools] $code
  gw -> vllm[vLLM Inference Engine] $cpu
  group Production Stack: gw mcp vllm'
from public.courses where slug = 'ai-mastery-zero-to-production'
on conflict (slug) do update set
  title = excluded.title,
  description = excluded.description,
  topics = excluded.topics,
  diagram_script = excluded.diagram_script;

insert into public.specialization_tracks (course_id, track_code, slug, title, description, topics, diagram_script)
select id, 'TRACK-B', 'track-b-business-product', 'Track B: AI for Business & Product Leaders', 'AI product strategy, unit economics of tokens, enterprise security/compliance, multi-agent workflow orchestration, AI transformation roadmaps, and ROI measurement.', '["AI Product Market Fit & UX Design", "Token Cost Economics & ROI Modeling", "Enterprise Security, SOC2 & Compliance", "Workflow Automation with n8n & LangGraph", "AI Transformation Strategy"]'::jsonb, '@preset midnight
@animate pulse
arch LR: Track B: Business & Product Strategy
  roi[Token Unit Economics] $dollar -> flow[Workflow Automation] $terminal
  flow -> sec[SOC2 & Data Security] $lock *
  sec -> scale[Enterprise AI Transformation] $chart'
from public.courses where slug = 'ai-mastery-zero-to-production'
on conflict (slug) do update set
  title = excluded.title,
  description = excluded.description,
  topics = excluded.topics,
  diagram_script = excluded.diagram_script;

insert into public.specialization_tracks (course_id, track_code, slug, title, description, topics, diagram_script)
select id, 'TRACK-C', 'track-c-research-architecture', 'Track C: AI Research & Architecture', 'Cutting-edge architectures, reasoning model pre-training & RL (GRPO, PPO), attention variants (MQA, GQA, Linear Attention), state space models (Mamba), and ColPali visual embeddings.', '["Reasoning Models & GRPO Dynamics", "State Space Models (Mamba & Jamba)", "Multi-Vector Vision-Language Retrieval (ColPali)", "Synthetic Data & Self-Play Generation", "Custom Attention Kernels with FlashAttention-3"]'::jsonb, '@preset midnight
@animate flow
layers: Track C: AI Research Deep Dive
  layer 4: Group Relative Policy Optimization (GRPO)
  layer 3: State Space Models (Mamba / SSMs)
  layer 2: Multi-Vector Vision Retrieval (ColPali)
  layer 1: FlashAttention-3 & Custom Triton Kernels'
from public.courses where slug = 'ai-mastery-zero-to-production'
on conflict (slug) do update set
  title = excluded.title,
  description = excluded.description,
  topics = excluded.topics,
  diagram_script = excluded.diagram_script;


-- 5. WEEKLY CHALLENGES
insert into public.weekly_challenges (week_number, title, description_roman_urdu, xp_reward, is_active)
values (1, 'NumPy Vectorization Challenge', 'Ek pure Python nested loop matrix multiplier ko NumPy vectorized broadcasting mein convert karein aur 50x speedup demonstrate karein.', 50, true)
on conflict (week_number) do update set
  title = excluded.title,
  description_roman_urdu = excluded.description_roman_urdu,
  xp_reward = excluded.xp_reward;

insert into public.weekly_challenges (week_number, title, description_roman_urdu, xp_reward, is_active)
values (2, 'Few-Shot Chain of Thought Engineering', 'Ek complex mathematical word problem solver prompt design karein jo consistent JSON format mein final step-by-step reasoning return kare.', 50, true)
on conflict (week_number) do update set
  title = excluded.title,
  description_roman_urdu = excluded.description_roman_urdu,
  xp_reward = excluded.xp_reward;

insert into public.weekly_challenges (week_number, title, description_roman_urdu, xp_reward, is_active)
values (3, 'Gradient Boosting Churn Predictor', 'Customer churn dataset par XGBoost train karein aur F1 score 0.85 se ooper achieve karein.', 75, true)
on conflict (week_number) do update set
  title = excluded.title,
  description_roman_urdu = excluded.description_roman_urdu,
  xp_reward = excluded.xp_reward;

insert into public.weekly_challenges (week_number, title, description_roman_urdu, xp_reward, is_active)
values (4, 'PyTorch Micrograd From Scratch', 'PyTorch autograd use kiye baghair ek 2-layer neural network ka manual backprop forward/backward pass likhein.', 100, true)
on conflict (week_number) do update set
  title = excluded.title,
  description_roman_urdu = excluded.description_roman_urdu,
  xp_reward = excluded.xp_reward;

insert into public.weekly_challenges (week_number, title, description_roman_urdu, xp_reward, is_active)
values (5, 'ColPali Multi-Vector Search', 'Ek 10-page financial PDF report ko ColPali use karte hue index karein aur tables se accurate numbers retrieve karein.', 120, true)
on conflict (week_number) do update set
  title = excluded.title,
  description_roman_urdu = excluded.description_roman_urdu,
  xp_reward = excluded.xp_reward;

insert into public.weekly_challenges (week_number, title, description_roman_urdu, xp_reward, is_active)
values (6, 'Anthropic MCP Tool Server', 'Ek custom SQLite aur Weather API MCP tool server banayein jo Claude Desktop ke sath smoothly interact kare.', 150, true)
on conflict (week_number) do update set
  title = excluded.title,
  description_roman_urdu = excluded.description_roman_urdu,
  xp_reward = excluded.xp_reward;

insert into public.weekly_challenges (week_number, title, description_roman_urdu, xp_reward, is_active)
values (7, 'Unsloth 4-bit Fine-Tuning', 'LLaMA-3-8B model ko Roman Urdu Q&A dataset par Unsloth se fine-tune karein aur GGUF export karein.', 200, true)
on conflict (week_number) do update set
  title = excluded.title,
  description_roman_urdu = excluded.description_roman_urdu,
  xp_reward = excluded.xp_reward;

insert into public.weekly_challenges (week_number, title, description_roman_urdu, xp_reward, is_active)
values (8, 'End-to-End Enterprise System', 'Complete multi-tenant AI system deploy karein with auth, telemetry, and sub-100ms streaming responses.', 300, true)
on conflict (week_number) do update set
  title = excluded.title,
  description_roman_urdu = excluded.description_roman_urdu,
  xp_reward = excluded.xp_reward;


-- 0. SCHEMA UPGRADES
alter table public.modules add column if not exists practice_checkpoint jsonb default '{}'::jsonb;


-- 6. MODULES (ALL 15 MODULES: MODULE 0 TO 14)
insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  0,
  'python-zero-se-hero',
  'Module 0: Python Zero Se Hero (Prerequisite Track: Pehle Python, Phir AI)',
  'Prerequisite / Week 0',
  12,
  '["Python interpreter, REPL, aur dynamic typing mental model", "Core data structures: Lists, Tuples, Sets, Dictionaries aur List Comprehensions", "Clean modular functions: Scope, Closures, *args, **kwargs aur Lambdas", "Object-Oriented Programming (OOP) for AI: Classes, Inheritance, Dunder Methods aur @dataclass", "File I/O, JSON serialization, exception handling aur REST API calls with requests", "NumPy vector basics aur Pandas DataFrame tabular manipulation for AI data ingestion"]'::jsonb,
  '["Chai Dhaba Billing CLI script with @dataclass & JSON storage likhein", "Nested dictionary se customer orders ka structured JSON report generate karein", "Pure Python list comprehension se complex data filter aur transform karein", "Custom class banayein with __repr__, __len__, aur custom property methods", "Public REST API se JSON data fetch karke Pandas DataFrame mein load karein"]'::jsonb,
  '[{"title": "Python 3.12 Official Tutorial", "url": "https://docs.python.org/3/tutorial/"}, {"title": "Automate the Boring Stuff with Python", "url": "https://automatetheboringstuff.com/"}, {"title": "Google Colab Python Beginner Guide", "url": "https://colab.research.google.com/"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Python Zero Se Hero Learning Journey
  syntax[0.1 Syntax & Mental Model] $code -> struct[0.2 Lists, Dicts & Tuples] $database
  struct -> func[0.3 Functions & *args] $terminal
  func -> oop[0.4 OOP & @dataclass] $box
  oop -> io[0.5 File I/O & JSON APIs] $cloud
  io -> np[0.6 NumPy & Pandas Intro] $cpu *',
  'midnight',
  'flow',
  'chai-munshi',
  'Chai Dhaba Billing Engine & Khata Management CLI',
  '{"platform": "Local Terminal / Google Colab Free Tier", "vram_required": "0 GB (Any CPU / Laptop)", "estimated_cost": "$0.00 Free", "compute_units_tip": "Pure Python logic runs 100% locally on any basic laptop or Colab CPU without requiring GPU compute.", "one_click_command": "python -m pip install tabulate rich && python chai_billing.py"}'::jsonb,
  '{"title": "Chai Shop Billing & Khata Management Engine", "urdu_title": "Chai Dhaba Billing & Munshi CLI", "description": "Dhabay aur chai shop ke liye real-time terminal billing tool. Har customer ka order (Doodh Patti, Elaichi Chai, Paratha), tax, discount calculate kare aur JSON khata file mein daily report append kare!", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod0_chai_billing", "checklist": ["@dataclass for MenuItem & OrderBill with auto-validation", "Interactive while loop CLI with clean input sanitization", "JSON persistence for daily transactions khata", "Discount & sales tax automated calculation", "Summary report generator showing top-selling item & profit"], "xp_reward": 100, "badge_name": "chai-munshi"}'::jsonb,
  0
from public.phases p
where p.slug = 'phase-1-foundations'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  1,
  'python-for-ai-and-fast-math',
  'Module 1: Python for AI & Fast Math (NumPy, Linear Algebra)',
  'Weeks 1-2',
  14,
  '["Python lists vs contiguous C-aligned NumPy memory layout ka farq", "High-performance vectorized operations aur SIMD parallelism", "Vector spaces, Dot products, projections aur Cosine similarity", "Calculus fundamentals: Gradients, partial derivatives, aur Loss surfaces", "Python 3.12 GIL, memory profiling, and AsyncIO event loops for AI pipelines", "High-throughput tabular wrangling with Polars & Apache Arrow"]'::jsonb,
  '["Pure Python nested loop ko NumPy vectorized broadcasting mein convert karein", "Cosine similarity function zero external libraries ke sath implement karein", "Gradient descent optimization loop for linear regression likhein", "tracemalloc aur AsyncIO se parallel batch LLM requests profile karein", "500k record dataset ko Polars lazy streaming pipeline se sanitize karein"]'::jsonb,
  '[{"title": "NumPy Illustrated Guide", "url": "https://numpy.org/doc/stable/"}, {"title": "3Blue1Brown Linear Algebra Series", "url": "https://www.3blue1brown.com/topics/linear-algebra"}, {"title": "Polars Official User Guide", "url": "https://docs.pola.rs/"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 1 Fast Math & Vector Pipeline
  py_list[Python List Overhead] $code -> numpy_arr[Contiguous C NumPy Array] $cpu
  numpy_arr -> simd[SIMD Vectorized Dot Product] $terminal
  simd -> loss[Loss Surface & Gradient Descent] $brain *',
  'midnight',
  'flow',
  'pehla-prompt',
  '500k E-Commerce Order Sanitizer & Parquet Data Pipeline',
  '{"platform": "Local CPU / Google Colab Free Tier", "vram_required": "0 GB (CPU)", "estimated_cost": "$0.00 Free", "compute_units_tip": "NumPy AVX-512 vectorization runs blazing fast on standard Colab CPU without burning any GPU compute units.", "one_click_command": "python -m pip install numpy polars pyarrow pydantic && python main.py"}'::jsonb,
  '{"title": "Biryani vs Pulao Sentiment & Price Vectorizer", "urdu_title": "Biryani vs Pulao Sentiment Analyzer", "description": "Karahi, Biryani aur Pulao ke 50,000 food reviews ko pure Python vs NumPy vectorized arrays se analyze karein. Cosine similarity se find karein ke kiske reviews mein sab se zyada ''Lazeez'' aur ''Mirchi'' ka vector overlap hai!", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod1_biryani_sentiment", "checklist": ["NumPy SIMD vectorized dot product implementation", "Zero-copy broadcasting array operations", "Cosine similarity calculator without SciPy", "50x speedup benchmark vs Python nested loops"], "xp_reward": 150, "badge_name": "biryani-analyst"}'::jsonb,
  1
from public.phases p
where p.slug = 'phase-1-foundations'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  2,
  'prompt-engineering-and-llm-mental-models',
  'Module 2: Prompt Engineering & LLM Mental Models',
  'Weeks 3-4',
  12,
  '["Next-Token Prediction mechanism aur Sampling parameters (Temperature, Top-P, Repetition Penalty)", "System vs User vs Assistant messages ka role aur prompt injection risks", "Few-Shot prompting, Chain of Thought (CoT), aur Least-to-Most decomposition", "Structured Outputs guarantee karna (JSON Schema, Pydantic, Instructor)", "KV Cache mechanics aur context window token budget economics", "Automated LLM evaluation aur LLM-as-a-Judge benchmarking"]'::jsonb,
  '["Ek complex reasoning puzzle ke liye Zero-Shot vs CoT prompt ka comparative test run karein", "Strict Pydantic JSON schema ke sath financial extraction prompt enforce karein", "Prompt injection jailbreak attack design karein aur uske khilaf system defense implement karein", "KV Cache context budget simulator likhein jo long-document chats ki cost calculate kare", "Enterprise prompt benchmark suite build karein jo 50 test cases par accuracy score kare"]'::jsonb,
  '[{"title": "OpenAI Prompt Engineering Guide", "url": "https://platform.openai.com/docs/guides/prompt-engineering"}, {"title": "Anthropic Interactive Prompt Tutorial", "url": "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 2 Prompt Mental Model
  user_prompt[Raw User Prompt] $terminal -> system_ctx[System Context & Schema] $code
  system_ctx -> cot[Chain-of-Thought Scratchpad] $brain
  cot -> json_out[Validated JSON Structure] $server *',
  'midnight',
  'flow',
  'prompt-rookie',
  'Multi-Step Medical Triage Prompt Pipeline with JSON Schemas',
  '{"platform": "Groq Cloud / Google AI Studio Free Tier", "vram_required": "0 GB (API-Based)", "estimated_cost": "$0.00 Free Tier", "compute_units_tip": "Groq Cloud free tier provides 30 req/min for LLaMA-3.3-70B; Gemini 2.0 Flash provides 1,500 req/day with zero credit card.", "one_click_command": "curl https://api.groq.com/openai/v1/models -H \"Authorization: Bearer $GROQ_API_KEY\""}'::jsonb,
  '{"title": "Rishta Matcher & Bio Compatibility Algorithm", "urdu_title": "Rishta Matcher Vector Distance Calculator", "description": "Candidate ke CV/Bio aur Mother-in-Law (Saas) ki strict 15-point demand list ke darmiyan high-dimensional embeddings calculate karein. Prompt engineering se ''Red Flags'' identify karein aur automated humorous compatibility score generate karein!", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod2_rishta_matcher", "checklist": ["Few-Shot Chain of Thought prompt engineering", "Structured JSON output validation with Pydantic", "Negative constraints & Hallucination mitigation rules", "Automated compatibility score generation (0-100%)"], "xp_reward": 150, "badge_name": "rishta-whisperer"}'::jsonb,
  2
from public.phases p
where p.slug = 'phase-1-foundations'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  3,
  'classical-machine-learning',
  'Module 3: Classical Machine Learning & Feature Engineering',
  'Weeks 5-6',
  14,
  '["Supervised learning taxonomy: Linear, Logistic, Trees, Ensembles", "Gradient Boosting mechanics (XGBoost, LightGBM, CatBoost)", "Dimensionality reduction: PCA, t-SNE, and K-Means clustering", "Model evaluation: Precision, Recall, F1-Score, ROC-AUC, and calibration", "Data leakage prevention and production Sklearn ColumnTransformer pipelines", "Deploying tabular models with low latency SLAs"]'::jsonb,
  '["Clean cross-validation pipeline implement karein with zero data leakage", "Custom Random Forest vs XGBoost benchmark run karein on imbalanced data", "PCA dimensionality reduction se 50 features ko 3 visual components mein compress karein", "Threshold tuning se F1-score optimize karein on credit fraud dataset", "Production ML Churn microservice export karein via ONNX/Joblib"]'::jsonb,
  '[{"title": "Scikit-Learn Documentation", "url": "https://scikit-learn.org/stable/"}, {"title": "XGBoost Production Architecture", "url": "https://xgboost.readthedocs.io/en/stable/"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 3 Classical ML Pipeline
  raw_data[Raw Mixed Tabular Data] $database -> pipe[Leakage-Free Sklearn Pipeline] $layers
  pipe -> trees[XGBoost Gradient Boosted Trees] $cpu
  trees -> eval_metrics[Precision / Recall / F1 Matrix] $chart
  eval_metrics -> onnx[Low-Latency ONNX Model] $server *',
  'midnight',
  'flow',
  'ml-practitioner',
  'Production Customer Churn ML Service (XGBoost + Fast Scikit-Pipeline)',
  '{"platform": "Local CPU / Colab Free Tier", "vram_required": "0 GB (CPU-Optimized)", "estimated_cost": "$0.00 Free", "compute_units_tip": "Classical ML (XGBoost, LightGBM, Scikit-learn) runs with multi-threaded CPU OpenMP; no GPU compute units required.", "one_click_command": "pip install scikit-learn xgboost lightgbm polars optuna && python train.py"}'::jsonb,
  '{"title": "PSL/IPL Match Outcome & Cricketer Performance Predictor", "urdu_title": "Cricketer Performance & Match Winner Predictor", "description": "Historical T20 pitch report, dew factor, strike rate, aur player matchups par LightGBM & XGBoost classifier train karein. Match ke 16th over mein live winning probability estimate karein!", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod3_cricket_predictor", "checklist": ["Data leakage prevention with temporal split", "Feature engineering (Strike rate in death overs, economy against spin)", "Hyperparameter tuning with Optuna", "Precision-Recall & ROC-AUC evaluation"], "xp_reward": 150, "badge_name": "toss-ka-badshah"}'::jsonb,
  3
from public.phases p
where p.slug = 'phase-2-core-ml-deeplearning'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  4,
  'deep-learning-and-pytorch-foundations',
  'Module 4: Deep Learning & PyTorch Foundations',
  'Weeks 7-8',
  16,
  '["PyTorch Tensors, memory layout (strides, contiguity), aur GPU acceleration", "Dynamic computational graphs aur Autograd backward pass mechanics", "Neural network forward pass, non-linear activations (GELU, SwiGLU), aur loss functions", "Production training loops: Automatic Mixed Precision (AMP), gradient scaling, and gradient clipping", "Normalization & Regularization: LayerNorm, RMSNorm, and Cosine Annealing learning rate schedules", "Building a micrograd-style reverse-mode autodiff engine from raw tensors"]'::jsonb,
  '["Manual tensor strides aur memory contiguity inspect karein", "PyTorch autograd use kiye baghair manual 2-layer backpropagation pass likhein", "SwiGLU activation module define karein aur standard ReLU se performance compare karein", "torch.cuda.amp.autocast aur GradScaler ke sath memory 50% reduce karein", "Custom Micrograd Autograd engine build karein jo non-linear decision boundary train kare"]'::jsonb,
  '[{"title": "PyTorch Official Deep Learning Tutorials", "url": "https://pytorch.org/tutorials/"}, {"title": "Andrej Karpathy: Micrograd Video Series", "url": "https://www.youtube.com/watch?v=VMj-3S1tku0"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 4 PyTorch Deep Learning Graph
  tensors[PyTorch Tensors on CUDA GPU] $database -> autograd[Dynamic Autograd Graph] $brain
  autograd -> forward[Forward Pass & SwiGLU Activations] $layers
  forward -> amp[Mixed Precision AMP & GradScaler] $cpu
  amp -> opt[AdamW Parameter Update] $server *',
  'midnight',
  'flow',
  'transformer-expert',
  'Mini-Autograd Deep Learning Engine & Multi-GPU Training Loop',
  '{"platform": "Google Colab Free Tier (Nvidia T4 15GB VRAM)", "vram_required": "2 GB VRAM", "estimated_cost": "$0.00 Free", "compute_units_tip": "PyTorch MLP and CNN training loops take less than 2 minutes on Colab T4 GPU; zero compute credits required.", "one_click_command": "python -c \"import torch; print(torch.cuda.is_available())\""}'::jsonb,
  '{"title": "Desi Meme Classifier & Sarcastic Roast Bot", "urdu_title": "Meme Classifier & Roast Engine", "description": "PyTorch se custom convolutional/MLP neural network train karein jo viral memes ko detect kare (e.g. ''Sarfaraz Dhoka Nahi Dega'' vs ''Disappointed Pakistani Fan'') aur instant humorous roast dialogue generate kare.", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod4_meme_roast_bot", "checklist": ["Custom PyTorch Dataset & DataLoader", "CrossEntropyLoss with AdamW & CosineAnnealing", "Mixed Precision (AMP) training on Free Colab T4", "Model checkpointing and inference visualizer"], "xp_reward": 200, "badge_name": "meme-roaster"}'::jsonb,
  4
from public.phases p
where p.slug = 'phase-2-core-ml-deeplearning'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  5,
  'attention-and-transformers-under-the-hood',
  'Module 5: Attention & Transformers Under the Hood',
  'Weeks 8-9',
  18,
  '["Scaled Dot-Product Attention: Query, Key, Value matrix mechanics", "Multi-Head Attention (MHA) projections and latent subspace alignment", "Tokenization deep dive: Byte-Pair Encoding (BPE) & Tiktoken", "Rotary Position Embeddings (RoPE) vs Sinusoidal encodings", "Architectural taxonomy: BERT vs GPT vs T5 paradigms", "Building, training, and autoregressively sampling from a Mini-GPT in pure PyTorch"]'::jsonb,
  '["Raw PyTorch tensors ke sath Scaled Dot-Product Attention implement karein", "Causal lower-triangular attention mask implement karein to prevent looking ahead", "Byte-Pair Encoding merge table zero libraries ke sath build karein", "RoPE 2D complex plane rotation function implement karein", "Complete Mini-GPT causal language model construct karein and sample generations"]'::jsonb,
  '[{"title": "Attention Is All You Need Paper", "url": "https://arxiv.org/abs/1706.03762"}, {"title": "The Illustrated Transformer", "url": "https://jalammar.github.io/illustrated-transformer/"}]'::jsonb,
  '@preset midnight
@animate pulse
arch LR: Full Transformer Block Pipeline
  in_tok[Input Token Embeddings] $terminal -> norm1[LayerNorm 1] $cpu
  norm1 -> mha[Multi-Head Attention] $brain
  mha -> add1[Residual Add] $layers
  in_tok -> add1
  add1 -> norm2[LayerNorm 2] $cpu
  norm2 -> ffn[Feed-Forward Network (GELU)] $cube
  ffn -> add2[Residual Add] $layers *
  add1 -> add2',
  'midnight',
  'pulse',
  'transformer-expert',
  'Mini-GPT Decoder-Only Language Model Trained on Urdu Poetry',
  '{"platform": "Google Colab Free Tier (T4 GPU)", "vram_required": "4 GB VRAM", "estimated_cost": "$0.00 Free", "compute_units_tip": "A 6-layer Mini-GPT trains on Colab Free T4 GPU in 12 minutes on Shakespeare/Urdu corpus without paid compute units.", "one_click_command": "pip install torch tiktoken datasets && python train_gpt.py"}'::jsonb,
  '{"title": "Mirza Ghalib vs Allama Iqbal Urdu Poetry Rhyme Engine", "urdu_title": "Ghalib vs Iqbal Poetry Mini-GPT", "description": "Raw PyTorch tensors se multi-head self-attention transformer likhein jo classic Urdu ghazals ke meter aur qafiya (rhyme) ko seekh kar naye humorous shair complete kare!", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod5_ghalib_gpt", "checklist": ["Custom Causal Self-Attention mask", "Rotary Position Embeddings (RoPE)", "Byte-Pair Encoding (BPE) tokenizer integration", "Next-token generation with temperature & top-p sampling"], "xp_reward": 200, "badge_name": "shayar-e-ai"}'::jsonb,
  5
from public.phases p
where p.slug = 'phase-2-core-ml-deeplearning'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  6,
  'building-ai-applications-and-apis',
  'Module 6: Building AI Applications & Modern APIs',
  'Weeks 11-12',
  14,
  '["Real-time token streaming via Server-Sent Events (SSE) aur HTTP/2", "Full-stack AI architectures: Frontend state, Svelte 5 Runes aur abort controllers", "Asynchronous background worker queues with FastAPI and Redis", "Token cost optimization: Semantic Caching via Redis & vector cosine thresholds", "Real-time bidirectional AI streaming via WebSockets and connection pooling", "Resilient enterprise streaming gateway with circuit breakers and fallback providers"]'::jsonb,
  '["FastAPI SSE token streaming endpoint implement karein", "Svelte 5 client-side streaming reader with cancel button build karein", "Redis vector semantic cache wrapper design karein for 80% token savings", "Bidirectional WebSocket streaming server implement karein with ping/pong heartbeats", "Production multi-provider failover AI Gateway build karein"]'::jsonb,
  '[{"title": "FastAPI Streaming Responses", "url": "https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse"}, {"title": "Svelte 5 Runes Overview", "url": "https://svelte.dev/docs/svelte/overview"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 6 Modern Streaming AI Stack
  user[User Browser Svelte 5] $browser -> sse_req[HTTP/2 SSE Request] $terminal
  sse_req -> gateway[Axum / FastAPI Gateway] $server
  gateway -> cache[Redis Semantic Cache] $database
  gateway -> llm[LLM Async Streaming Engine] $cpu
  llm -> user: Chunked Token Stream *',
  'midnight',
  'flow',
  'app-builder',
  'WhatsApp/Web AI Customer Support Bot with SSE Streaming & Fallback',
  '{"platform": "Local CPU / Fly.io Free Tier / Render", "vram_required": "0 GB (CPU)", "estimated_cost": "$0.00 Free", "compute_units_tip": "Host async FastAPI or Rust Axum server on free tier connected to Groq API.", "one_click_command": "uvicorn main:app --workers 4"}'::jsonb,
  '{"title": "Ami Ka WhatsApp Auto-Responder Bot", "urdu_title": "Ami Ka WhatsApp Reply Bot", "description": "''Beta kahan ho?'', ''Roti khayi?'', aur ''Dahi le aana'' jese WhatsApp messages ke liye production-ready FastAPI streaming server banayein with Server-Sent Events (SSE) and token-rate streaming.", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod6_ami_reply_bot", "checklist": ["FastAPI async route with StreamingResponse", "Pydantic V2 request & response schemas", "In-memory token-bucket rate limiter", "CORS & Bearer token authorization middleware"], "xp_reward": 200, "badge_name": "farmanbardar-beta"}'::jsonb,
  6
from public.phases p
where p.slug = 'phase-3-modern-genai-stack'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  7,
  'vector-databases-and-modern-rag',
  'Module 7: Vector Databases & Modern RAG Architecture (ColPali)',
  'Weeks 13-14',
  16,
  '["Embedding models geometry, Cosine vs Inner Product vs Euclidean metrics", "Approximate Nearest Neighbor (ANN) indexing: HNSW, IVFFlat, aur PQ", "Advanced Hybrid Search: Dense vectors + Sparse BM25 via Reciprocal Rank Fusion (RRF)", "Document parsing and semantic chunking strategies", "Query transformations: HyDE (Hypothetical Document Embeddings) and Multi-Query", "2026 SOTA: ColPali Vision-Language Multi-Vector RAG without OCR text errors"]'::jsonb,
  '["PostgreSQL pgvector extension enable karein aur HNSW vector index build karein", "BM25 sparse search aur dense embeddings ka hybrid fusion algorithm likhein", "Semantic document chunker implement karein based on embedding cosine similarity", "Cross-Encoder Re-ranker (FlashRank / Cohere) se top-k chunks re-order karein", "ColPali multi-vector late interaction scoring implement karein on complex PDF tables"]'::jsonb,
  '[{"title": "pgvector GitHub Repository", "url": "https://github.com/pgvector/pgvector"}, {"title": "ColPali SOTA Paper", "url": "https://arxiv.org/abs/2407.01449"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 7 Modern RAG Pipeline
  doc[Complex PDF Document with Tables] $terminal -> colpali[ColPali Vision Multi-Vector Embeddings] $brain
  query[User Natural Query] $code -> hybrid[Hybrid HNSW + BM25 Search] $database
  hybrid -> rerank[Cross-Encoder Re-Ranker] $server
  rerank -> llm[LLM with Grounded Citations] $cpu *',
  'midnight',
  'flow',
  'rag-master',
  'Multimodal PDF/Report RAG with ColPali Multi-Vector Search & Reranking',
  '{"platform": "Colab T4 / Supabase pgvector / Qdrant Cloud Free", "vram_required": "0 GB - 4 GB (ColPali)", "estimated_cost": "$0.00 Free Tier", "compute_units_tip": "Supabase pgvector and Qdrant free tier provide 1M vectors for free. Run ColPali indexing on Colab T4.", "one_click_command": "docker run -p 6333:6333 qdrant/qdrant"}'::jsonb,
  '{"title": "Grandma''s Secret Biryani Recipe RAG Engine", "urdu_title": "Nani Amma Biryani Recipe RAG Search", "description": "Scanned handwritten recipe notes aur secret spices PDF documents ko PostgreSQL pgvector hybrid search (BM25 + Dense) se index karein. Query: ''Agar namak tez ho jaye to kya karein?'' -> exact potaato trick cite kare!", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod7_secret_biryani_rag", "checklist": ["pgvector HNSW index creation in PostgreSQL", "Reciprocal Rank Fusion (RRF) for Hybrid search", "Cross-Encoder re-ranking with FlashRank", "Strict source citation grounding prompt"], "xp_reward": 250, "badge_name": "bawarchi-rag"}'::jsonb,
  7
from public.phases p
where p.slug = 'phase-3-modern-genai-stack'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  8,
  'autonomous-agents-and-tool-use',
  'Module 8: Autonomous Agents, MCP & Tool Use (Anthropic MCP, smolagents)',
  'Weeks 15-16',
  16,
  '["The ReAct Pattern: Reasoning + Acting cyclic execution loops", "2026 Industry Standard: Anthropic Model Context Protocol (MCP) Client & Server Architecture", "HuggingFace smolagents: Code-First Agents vs JSON-Action agents", "Function and tool calling specifications with OpenAPI and JSON Schemas", "Stateful cyclic multi-agent graphs with LangGraph and memory checkpoints", "Multi-agent collaboration patterns: Supervisor, Worker, and Critique"]'::jsonb,
  '["Custom SQLite database query tool implement karein with strict schema validation", "Anthropic MCP server create karein jo local system diagnostics provide kare", "smolagents sandboxed Python interpreter agent build karein", "LangGraph state machine graph construct karein with human-in-the-loop review", "Autonomous Multi-Agent Bug Fixing swarm build karein"]'::jsonb,
  '[{"title": "Anthropic Model Context Protocol (MCP)", "url": "https://modelcontextprotocol.io/"}, {"title": "HuggingFace smolagents Documentation", "url": "https://huggingface.co/docs/smolagents/"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 8 Agentic Architecture
  user[User High-Level Task] $terminal -> planner[ReAct Supervisor Agent] $brain
  planner -> mcp[Anthropic MCP Server Tools] $code
  mcp -> env[Sandboxed Execution Environment] $server
  env -> obs[Observation & Self-Correction] $database
  obs -> planner: Cyclic Thought Loop *',
  'midnight',
  'flow',
  'agent-architect',
  'Autonomous Multi-Agent Swarm with Anthropic MCP & Sandboxed Code Execution',
  '{"platform": "Local CPU / Groq Cloud / Gemini API Free Tier", "vram_required": "0 GB (Tool Use APIs)", "estimated_cost": "$0.00 Free Tier", "compute_units_tip": "Agent reasoning loops run on cloud API free tier (Groq / Gemini 2.0 Flash) with zero GPU cost.", "one_click_command": "pip install mcp smolagents langgraph langchain-core && python agent.py"}'::jsonb,
  '{"title": "Aggressive Salary Negotiation AI Agent Swarm", "urdu_title": "Salary Negotiation Multi-Agent Swarm", "description": "Anthropic Model Context Protocol (MCP) aur smolagents use karte hue 3 agents ka swarm banayein (Analyst, Market Researcher, Hardball Negotiator) jo remote USD salary packages par counter-offers draft kare!", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod8_salary_negotiator", "checklist": ["Custom MCP tool server (Tax Calculator, Glassdoor scraper)", "ReAct planning & execution loop", "Human-in-the-loop approval checkpoint", "Multi-turn counter-offer generation"], "xp_reward": 250, "badge_name": "dollar-earner"}'::jsonb,
  8
from public.phases p
where p.slug = 'phase-3-modern-genai-stack'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  9,
  'fine-tuning-and-model-adaptation',
  'Module 9: Fine-Tuning & Model Adaptation',
  'Weeks 13-14',
  16,
  '["PEFT, LoRA aur QLoRA mathematics: Low-Rank decomposition, rank r, scaling factor alpha aur target projection matrices", "High-quality dataset curation: ChatML formatting, multi-turn packing aur token masking", "Fast fine-tuning with Unsloth: Triton hand-written kernels aur 2x-5x training speedups", "Preference alignment: Direct Preference Optimization (DPO) aur ORPO bina separate reward model ke", "DeepSeek-R1 style Group Relative Policy Optimization (GRPO): Self-play reasoning training", "Production export: Adapter merging, 16-bit float reconstruction aur GGUF / AWQ quantization"]'::jsonb,
  '["LoRA low-rank decomposition PyTorch custom layer se implement karein", "Instruction-tuning dataset ko ChatML format mein clean aur tokenize karein with padding masks", "Unsloth use karte hue Llama 3 / Mistral model ko 4-bit QLoRA se fine-tune karein Colab T4 par", "DPO trainer setup karein chosen vs rejected preference pairs par", "GRPO rule-based reward function likhein jo mathematical step-by-step reasoning reward kare", "LoRA weights ko base model mein merge karke vLLM aur llama.cpp GGUF format mein export karein"]'::jsonb,
  '[{"title": "LoRA: Low-Rank Adaptation Paper", "url": "https://arxiv.org/abs/2106.09685"}, {"title": "Unsloth Documentation & Notebooks", "url": "https://github.com/unslothai/unsloth"}, {"title": "DeepSeek-R1 Technical Report & GRPO", "url": "https://arxiv.org/abs/2501.12948"}, {"title": "Hugging Face TRL (Transformer Reinforcement Learning)", "url": "https://huggingface.co/docs/trl/index"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 9 Fine-Tuning Pipeline
  raw_data[Domain Dataset ChatML] $database -> unsloth[Unsloth Fast QLoRA] $cpu
  unsloth -> dpo[DPO / GRPO Alignment] $brain
  dpo -> merge[LoRA Weights Merge] $server
  merge -> gguf[vLLM / GGUF Export] $terminal *',
  'midnight',
  'flow',
  'finetuning-pro',
  'Fine-Tuned Domain Reasoning LLM with Unsloth LoRA & DeepSeek-R1 GRPO',
  '{"platform": "Google Colab Free Tier (T4 15GB) / Kaggle Dual T4", "vram_required": "6-12 GB (Unsloth 4-bit QLoRA)", "estimated_cost": "$0.00 Free", "compute_units_tip": "Unsloth 4-bit memory optimizations enable training 8B parameter models on a single free T4 GPU without OOM.", "one_click_command": "pip install unsloth \"xformers<0.0.27\" trl peft"}'::jsonb,
  '{"title": "Roman Urdu Sarcasm & Roast Fine-Tuning Engine", "urdu_title": "Roman Urdu Sarcasm Detector (Unsloth QLoRA)", "description": "Free Google Colab T4 par Unsloth 4-bit QLoRA use karke Llama 3.2 3B ya Gemma 2 2B ko fine-tune karein. Model pehchane ke ''Bohot aala bhai!'' tareef hai ya taana!", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod9_urdu_sarcasm", "checklist": ["Unsloth 4-bit FastLanguageModel setup", "ChatML dataset packing with assistant masking", "LoRA rank 16 / alpha 32 configuration", "GGUF Q4_K_M quant export for local inference"], "xp_reward": 300, "badge_name": "taana-master"}'::jsonb,
  9
from public.phases p
where p.slug = 'phase-4-production-mlops'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  10,
  'ai-safety-evals-and-guardrails',
  'Module 10: AI Safety, Evals & Guardrails',
  'Weeks 14-15',
  14,
  '["Systematic LLM evaluation metrics: The Ragas Triad (Faithfulness, Answer Relevance, Context Precision)", "Programmable runtime guardrails using NeMo Guardrails aur Colang 2.0", "Automated PII detection aur irreversible data anonymization with Microsoft Presidio", "Hallucination detection engines and groundedness score thresholds using TruLens", "Automated CI/CD evaluation test gates and regression prevention with DeepEval", "Multi-layer enterprise safety architecture: Input rails, dialog rails aur output rails"]'::jsonb,
  '["Ragas evaluation pipeline build karein jo RAG responses ko 0-1 scale par mathematically score kare", "NeMo Guardrails flow define karein jo competitor mentions aur prompt injection block kare", "Presidio pipeline configure karein jo CNIC, credit card aur phone numbers redact kare", "TruLens Feedback Functions setup karein for groundedness and toxic sentiment detection", "GitHub Actions workflow likhein jo PR merge hone se pehle DeepEval evaluation suite run kare"]'::jsonb,
  '[{"title": "Ragas: Automated Evaluation for RAG", "url": "https://docs.ragas.io/en/stable/"}, {"title": "NeMo Guardrails Documentation", "url": "https://docs.nvidia.com/nemo/guardrails/latest/index.html"}, {"title": "Microsoft Presidio PII Protection", "url": "https://microsoft.github.io/presidio/"}, {"title": "DeepEval LLM Evaluation Framework", "url": "https://docs.confident-ai.com/"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 10 Enterprise Safety Architecture
  user_input[User Prompt] $browser -> presidio[Presidio PII Redactor] $lock
  presidio -> nemo_in[NeMo Input Guardrail] $shield
  nemo_in -> llm[LLM / RAG Engine] $cpu
  llm -> nemo_out[NeMo Output Rail & Hallucination Check] $shield
  nemo_out -> sanitized[Sanitized Safe Output] $server *',
  'midnight',
  'flow',
  'production-ready',
  'Enterprise Safety Firewall & Multi-Layer Guardrail Gateway with PII Redaction',
  '{"platform": "Local CPU / Render / Fly.io Free Tier", "vram_required": "0 GB (CPU)", "estimated_cost": "$0.00 Free", "compute_units_tip": "Microsoft Presidio, NeMo Guardrails, and Ragas evaluation runs efficiently on multi-core standard CPUs.", "one_click_command": "pip install presidio-analyzer presidio-anonymizer ragas nemoguardrails deepeval"}'::jsonb,
  '{"title": "Phuppo-Proof Family Group Content Guardrail Firewall", "urdu_title": "Family Group PII & Jailbreak Firewall", "description": "Family WhatsApp groups mein fake news, toxic rishta gossip aur PII leaks ko rokne ke liye NeMo Guardrails + Microsoft Presidio firewall deploy karein jo toxic messages ko polite Roman Urdu mein rewrite kare.", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod10_family_firewall", "checklist": ["Presidio PII anonymizer (phone, CNIC, address)", "Semantic jailbreak detection rail", "Ragas faithfulness evaluation metric", "Automated GitHub Actions CI eval runner"], "xp_reward": 300, "badge_name": "sulah-joo"}'::jsonb,
  10
from public.phases p
where p.slug = 'phase-4-production-mlops'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  11,
  'production-ai-engineering-mlops',
  'Module 11: Production AI Engineering & MLOps',
  'Weeks 15-16',
  16,
  '["High-throughput inference architecture: vLLM PagedAttention, Continuous Batching aur KV Cache memory management", "Advanced model quantization formats: AWQ, GPTQ, NF4 aur FP8 KV Cache compression", "Ultra-low latency reverse proxies in Rust Axum with asynchronous SSE streaming", "Comprehensive LLM observability: Distributed tracing with OpenTelemetry, Prometheus aur Langfuse", "Scalable containerized deployment on Kubernetes using KServe, Ray Serve aur Horizontal Pod Autoscalers (HPA)", "Enterprise production resiliency: Multi-provider circuit breakers, fallback routing aur token budget quotas"]'::jsonb,
  '["vLLM engine run karein with PagedAttention and continuous batching benchmark", "AWQ quantized model deploy karein 4x memory savings ke sath", "Rust Axum streaming LLM gateway build karein capable of 10,000+ concurrent requests", "OpenTelemetry spans aur Langfuse tracing dashboard integrate karein", "Kubernetes deployment manifest configure karein with GPU resource limits and KServe autoscaler"]'::jsonb,
  '[{"title": "vLLM: Easy, Fast, and Cheap LLM Serving", "url": "https://docs.vllm.ai/en/latest/"}, {"title": "PagedAttention Research Paper (Woosuk Kwon et al.)", "url": "https://arxiv.org/abs/2309.06180"}, {"title": "Rust Axum Web Framework", "url": "https://github.com/tokio-rs/axum"}, {"title": "Langfuse Open Source LLM Engineering Platform", "url": "https://langfuse.com/"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 11 Production Serving Architecture
  client[Concurrent Clients] $browser -> rust_gw[Rust Axum Gateway] $server *
  rust_gw -> otel[OpenTelemetry / Langfuse Tracing] $chart
  rust_gw -> vllm[vLLM PagedAttention Cluster] $cpu
  vllm -> gpu_cache[Paged KV Cache Blocks] $database
  vllm -> k8s[Kubernetes KServe Autoscaler] $cloud',
  'midnight',
  'flow',
  'production-ready',
  'High-Throughput vLLM & Rust Axum LLM Gateway with Kubernetes KServe Autoscaling',
  '{"platform": "Fly.io / Render Free Tier / Local CPU", "vram_required": "0 GB (Gateway) / 16 GB+ (vLLM Production Host)", "estimated_cost": "$0.00 (Development & Proxy Gateway)", "compute_units_tip": "Develop and test high-concurrency Rust Axum reverse proxy locally on CPU connected to free Groq/Cerebras endpoints.", "one_click_command": "cargo run --release"}'::jsonb,
  '{"title": "Sub-50ms High-Scale AI Microservice Gateway", "urdu_title": "Sub-50ms Rust Axum LLM Gateway", "description": "Rust Axum mein high-throughput proxy gateway banayein jo Groq, Cerebras aur vLLM clusters ke darmiyan round-robin load balance kare with automated failover aur sub-50ms latency.", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod11_rust_gateway", "checklist": ["Rust Axum async route handlers", "Token-bucket rate limiter per API key", "Multi-provider health check & circuit breaker", "OpenTelemetry distributed tracing"], "xp_reward": 350, "badge_name": "rocket-engineer"}'::jsonb,
  11
from public.phases p
where p.slug = 'phase-4-production-mlops'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  12,
  'multimodal-ai-and-vision',
  'Module 12: Multimodal AI & Vision',
  'Weeks 17-18',
  16,
  '["Foundations of Vision-Language Models (VLMs): CLIP contrastive learning aur joint embedding spaces", "Vision Encoders & Cross-Attention Projectors: SigLIP, Linear projection vs MLP projection aur LLaVA architecture", "Document & Invoice OCR Intelligence: Visual table extraction, bounding boxes aur key-value parsing", "Audio & Speech AI: Whisper acoustic features, Mel-spectrograms, CTC loss aur audio-LLM tokenization", "Video understanding: Keyframe sampling, temporal attention mechanisms aur video question answering", "End-to-end multimodal agent pipelines integrating images, diagrams, audio transcripts aur text"]'::jsonb,
  '["CLIP zero-shot image classification aur visual search engine implement karein", "Florence-2 / Moondream VLM use karke invoices aur receipts se structured JSON extract karein", "Whisper model se Roman Urdu audio speech ko stream aur transcribe karein", "OpenCV video frame extraction pipeline build karein for temporal video search", "Multimodal RAG pipeline design karein jo PDF ke diagrams aur tables ko visually retrieve kare"]'::jsonb,
  '[{"title": "OpenAI CLIP: Learning Transferable Visual Models", "url": "https://arxiv.org/abs/2103.00020"}, {"title": "LLaVA: Visual Instruction Tuning", "url": "https://llava-vl.github.io/"}, {"title": "Google SigLIP: Sigmoid Loss for Language Image Pre-Training", "url": "https://arxiv.org/abs/2303.15343"}, {"title": "OpenAI Whisper Speech Recognition", "url": "https://github.com/openai/whisper"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 12 Multimodal Architecture
  img[Visual Input: Image / Video Frame] $browser -> vis_enc[Vision Encoder: SigLIP / ViT] $cpu
  vis_enc -> proj[Linear / MLP Projector] $layers
  audio[Audio Input: Speech WAV] $terminal -> whisper[Whisper Encoder] $cpu
  proj & whisper -> llm[Multimodal LLM Backbone] $brain *
  llm -> out[Structured Visual Analysis & Grounding] $server',
  'midnight',
  'flow',
  'ai-graduate',
  'Multimodal Document & Video Intelligence Engine with Visual Grounding',
  '{"platform": "Google AI Studio (Gemini 2.0 Flash) / Colab Free T4", "vram_required": "0 GB (via Gemini API) / 8 GB (Local Moondream / Florence-2)", "estimated_cost": "$0.00 Free", "compute_units_tip": "Gemini 2.0 Flash on Google AI Studio provides 1,500 free multimodal requests per day with 1M context for video, audio and image processing.", "one_click_command": "pip install google-genai pillow opencv-python transformers"}'::jsonb,
  '{"title": "Handwritten Doctor Prescription & Urdu Audio Transcriber", "urdu_title": "Doctor Prescription OCR & Audio Transcriber", "description": "Doctor ki tehrir (handwritten bad handwriting) aur tez bolay gaye Urdu audio notes ko Whisper Large v3 + Vision LLM se parse karke structured medicine dosage JSON generate karein.", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod12_doctor_ocr", "checklist": ["Whisper audio chunking & transcription", "Vision LLM multimodal prompt with dosage schema", "Pydantic JSON schema strict enforcement", "Medicine interaction warning system"], "xp_reward": 350, "badge_name": "hakeem-ai"}'::jsonb,
  12
from public.phases p
where p.slug = 'phase-5-specialization-capstone'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  13,
  'local-ai-and-edge-devices',
  'Module 13: Local AI & Edge Devices',
  'Weeks 18-19',
  14,
  '["C++ Inference optimization: llama.cpp architecture, GGUF binary quantization formats aur CPU vectorization", "Ollama deep dive: Custom Modelfiles, system prompt templating, REST API automation aur memory swapping", "Hardware acceleration: Apple Silicon Metal Performance Shaders (MPS), Vulkan cross-platform aur AMD ROCm", "In-browser AI execution: WebGPU, Wasm (WebAssembly) aur Transformers.js for zero-server latency", "Embedded Edge AI: Nvidia Jetson Orin Nano, Raspberry Pi 5 NPU aur INT4 embedded model deployment", "100% privacy-preserving offline AI architectures for confidential healthcare, legal aur field operations"]'::jsonb,
  '["llama.cpp build karein local machine par with native AVX-512 / Metal flags", "Custom Ollama Modelfile create karein Roman Urdu personality aur parameter constraints ke sath", "In-browser sentiment classifier aur chat client deploy karein using WebGPU & Transformers.js", "Raspberry Pi / Jetson benchmark run karein measuring tokens per second and thermal throttling", "Complete offline RAG pipeline build karein using local ChromaDB and Ollama embeddings"]'::jsonb,
  '[{"title": "llama.cpp GitHub Repository", "url": "https://github.com/ggerganov/llama.cpp"}, {"title": "Ollama Documentation & Modelfiles", "url": "https://github.com/ollama/ollama/blob/main/docs/modelfile.md"}, {"title": "Transformers.js In-Browser AI", "url": "https://huggingface.co/docs/transformers.js/index"}, {"title": "WebGPU W3C Specification", "url": "https://www.w3.org/TR/webgpu/"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 13 Local AI Execution Stack
  hardware[Consumer CPU / Apple M-Chip / NPU] $cpu -> backend[llama.cpp / Vulkan / Metal] $layers
  backend -> gguf[Quantized GGUF Q4_K_M Weights] $database
  backend -> ollama[Ollama Local REST Daemon] $server *
  ollama -> app[Private Offline Application] $browser',
  'midnight',
  'flow',
  'production-ready',
  '100% Offline Autonomous Edge AI Assistant with Voice & Local RAG',
  '{"platform": "Local Consumer Laptop (Mac M-series / Intel / AMD) / Raspberry Pi", "vram_required": "0 GB GPU (Runs 100% on CPU RAM with AVX-512 / Metal)", "estimated_cost": "$0.00 Free", "compute_units_tip": "llama.cpp and Ollama run 3B and 8B quantized GGUF models directly on standard consumer CPU RAM with zero cloud dependency.", "one_click_command": "ollama run llama3.2:3b"}'::jsonb,
  '{"title": "100% Offline Exam Crammer Chatbot", "urdu_title": "Offline WebGPU Exam Crammer", "description": "Transformers.js + WebGPU ke zariye student ke browser mein Llama-3.2-1B-Instruct model 100% offline run karein taake bina internet / load-shedding ke exam revision ki ja sake.", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod13_offline_crammer", "checklist": ["WebGPU device initialization in JavaScript", "ONNX / Transformers.js quantized model loading", "Zero-server edge inference loop", "Local browser IndexedDB chat persistence"], "xp_reward": 400, "badge_name": "bijli-proof"}'::jsonb,
  13
from public.phases p
where p.slug = 'phase-5-specialization-capstone'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;

insert into public.modules (
  phase_id, module_number, slug, title, weeks_range, estimated_hours,
  learning_outcomes, practical_tasks, resources, diagram_script,
  diagram_preset, diagram_animation, badge_slug, real_world_deliverable, zero_gpu_recipe, practice_checkpoint, order_index
)
select
  p.id,
  14,
  'enterprise-capstone-and-career-launch',
  'Module 14: Enterprise Capstone & Career Launch',
  'Weeks 19-20',
  20,
  '["Enterprise multi-tenant architecture: Row-Level Security (RLS), vector workspace isolation aur compliance audit trails", "High availability & resilience engineering: Circuit breakers, exponential jitter backoff aur multi-cloud fallback", "Monetization & cost governance: Token metering, user rate limits aur Stripe usage-based billing integration", "Production packaging & release: Multi-stage Docker builds, Helm charts aur semantic versioning CI/CD pipelines", "AI engineering career positioning: Technical architecture whitepapers, GitHub portfolio stardom aur live demos", "Grand Capstone Defense: Live presentation, technical peer review aur graduation from the AI Ustaad curriculum"]'::jsonb,
  '["Supabase Postgres Row-Level Security policies configure karein multi-tenant vector partitioning ke liye", "Stripe metered billing webhook listener implement karein tracking input and output tokens", "Multi-stage Dockerfile optimize karein reducing production image size from 4GB to under 200MB", "Interactive live portfolio project showcase deploy karein on Cloudflare Pages / Fly.io", "Grand Capstone live defense conduct karein with comprehensive system architecture documentation"]'::jsonb,
  '[{"title": "Supabase Row Level Security Deep Dive", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security"}, {"title": "Stripe Usage-Based Metered Billing", "url": "https://stripe.com/docs/billing/subscriptions/usage-based"}, {"title": "Docker Multi-Stage Builds Guide", "url": "https://docs.docker.com/build/building/multi-stage/"}, {"title": "System Design for Enterprise AI Applications", "url": "https://github.com/donnemartin/system-design-primer"}]'::jsonb,
  '@preset midnight
@animate flow
flow LR: Module 14 Enterprise Architecture
  client[Cloudflare Pages Frontend] $browser -> gw[Multi-Tenant Gateway] $server *
  gw -> rls[Supabase Postgres RLS & Vector Partition] $database
  gw -> billing[Stripe Token Metering] $dollar
  gw -> cluster[Resilient LLM Inference Cluster] $cpu
  gw -> audit[Immutable Audit Log] $lock',
  'midnight',
  'flow',
  'ai-graduate',
  'Multi-Tenant Enterprise AI Platform with Auth, Billing, Observability & Live Defense',
  '{"platform": "Fly.io / Render / Cloudflare Pages / Supabase Free Tier", "vram_required": "0 GB (Cloud Serverless / Microservices Architecture)", "estimated_cost": "$0.00 Free Tier", "compute_units_tip": "Deploy multi-tenant frontend on Cloudflare Pages, backend on Render, and Postgres/pgvector on Supabase completely within free tier limits.", "one_click_command": "docker compose up -d"}'::jsonb,
  '{"title": "Global AI Micro-SaaS Capstone Defense", "urdu_title": "Commercial AI SaaS Capstone Launch", "description": "Supabase Auth, PostgreSQL RLS, Stripe billing aur Cloudflare Pages deployment ke sath ek commercial AI SaaS banayein aur live internet par launch karein!", "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod14_capstone_defense", "checklist": ["Multi-tenant Supabase schema with RLS", "Stripe webhook payment integration", "Production deployment on Cloudflare Pages", "Live 60-second video demo & GitHub repository"], "xp_reward": 500, "badge_name": "unicorn-founder"}'::jsonb,
  14
from public.phases p
where p.slug = 'phase-5-specialization-capstone'
on conflict (slug) do update set
  module_number = excluded.module_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  estimated_hours = excluded.estimated_hours,
  learning_outcomes = excluded.learning_outcomes,
  practical_tasks = excluded.practical_tasks,
  resources = excluded.resources,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  badge_slug = excluded.badge_slug,
  real_world_deliverable = excluded.real_world_deliverable,
  zero_gpu_recipe = excluded.zero_gpu_recipe,
  practice_checkpoint = excluded.practice_checkpoint,
  order_index = excluded.order_index;


-- 7. LESSONS (DETAILED LESSONS FOR EVERY MODULE)
delete from public.lessons;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '0.1',
  'python-mental-model-syntax',
  'Python Mental Model, Setup & Fast Syntax (Interpreter, Variables & Conditionals)',
  30,
  'theory_and_code',
  'Khush-Aamdeed! Yeh hamara **Python Zero Se Hero** track hai jo un doston ke liye design kiya gaya hai jinhon ne pehle kabhi coding nahi ki ya Python ka basic syntax refresh karna chahte hain.

### 1. Python Ka Mental Model: Yeh Kaise Kaam Karta Hai?
C++ ya Rust ke bar-aks, jahan code pehle machine code mein compile hota hai, Python ek **interpreted bytecode** language hai. Jab aap `python main.py` likhte hain, to:
1. Python parser aapke code ko syntax tree mein convert karta hai.
2. CPython compiler isay `.pyc` bytecode mein translate karta hai.
3. CPython Virtual Machine (VM) is bytecode ko line-by-line execute karti hai.

### 2. Variables & Dynamic Typing
Python mein variables sirf ek pointer/label hote hain jo memory mein kisi object ki taraf point karte hain:
```python
x = 42          # x points to integer object 42
x = "AI Ustaad" # Ab wahi x string object ki taraf point kar raha hai
```
Isay **Dynamic Typing** kehte hain. AI pipelines mein clean code ke liye hum modern Python 3.12 **Type Hints** use karte hain:
```python
model_name: str = "llama-3.2"
batch_size: int = 32
learning_rate: float = 0.001
is_training: bool = True
```

### 3. Conditionals & Modern Match-Case
Python 3.10+ mein modern structural pattern matching introduce hui jo complex if/else chains ko clean banati hai:
```python
def route_model(task: str) -> str:
    match task:
        case "chat" | "reasoning":
            return "deepseek-r1"
        case "vision":
            return "siglip-clip"
        case _:
            return "llama-3.2-3b"
```',
  'Understand Python''s CPython bytecode VM architecture, dynamic typing, type annotations, truthy/falsy evaluation, and modern Python 3.10+ match-case syntax.',
  '# Python Foundations: Mental Model & Fast Syntax
import sys

# 1. Type annotations & Variables
app_name: str = "AI Ustaad Dhaba Billing"
version: float = 1.0
active_tables: int = 12

print(f"[{app_name} v{version}] Python Interpreter: {sys.version.split()[0]}")

# 2. Modern Walrus Operator (:=) for in-line evaluation
while (user_input := input("Item code daalein (ya ''exit'' likhein): ").strip().lower()) != ''exit'':
    # 3. Match-Case Pattern Matching
    match user_input:
        case "c1" | "chai":
            price = 60
            print(f"Doodh Patti Selected! Price: Rs {price}")
        case "p1" | "paratha":
            price = 120
            print(f"Lachha Paratha Selected! Price: Rs {price}")
        case _:
            print("Invalid code! Try ''c1'' ya ''p1''.")
    break',
  '@preset midnight
@animate flow
flow LR: Python Bytecode Virtual Machine Loop
  src[Python Source .py] $code -> comp[CPython Bytecode Compiler] $cpu
  comp -> pyc[.pyc Bytecode Instructions] $database
  pyc -> vm[CPython Execution Loop] $server
  vm -> out[Console Output / State] $terminal *',
  'flow',
  '[{"title": "Python 3.12 Official Tutorial", "url": "https://docs.python.org/3/tutorial/"}]'::jsonb,
  15,
  1
from public.modules m
where m.slug = 'python-zero-se-hero'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '0.2',
  'python-data-structures-deep-dive',
  'Data Structures Deep-Dive: Lists, Tuples, Sets, Dictionaries & Comprehensions',
  35,
  'theory_and_code',
  'AI Engineering mein data ko sahi structure mein rakhna sab se zaroori skill hai. Chaliye Python ke 4 bunyadi data structures ko first-principles se samjhein:

### 1. Lists: Dynamic Arrays (Order Preserved, Mutable)
Python ki `list` C-array of pointers hoti hai. Jab list bharti hai, Python automatically 1.125x capacity over-allocate kar leta hai taake har append par realloc na karna paray.
* Lookup by index: $O(1)$ fast!
* Append at end: $O(1)$ amortized fast!
* Search by value (`x in my_list`): $O(N)$ slow!

### 2. Tuples: Immutable Arrays
Tuples list jese hote hain lekin banne ke baad badal nahi sakte (`immutable`). Iska faida:
1. Memory overhead 30% kam hota hai.
2. Dictionary ke keys ban sakte hain kyunke inka hash constant rehta hai.

### 3. Sets: Unordered Unique Hash Tables
Sets duplicate values ko allow nahi karte aur Hash Table par chalte hain.
* Search (`x in my_set`): $O(1)$ instant!
* AI vocabulary tokens deduplicate karne ke liye perfect!

### 4. Dictionaries: Key-Value Hash Maps
Python 3.7+ mein Dictionaries insertion order preserve karti hain.
```python
customer_orders = {
    "order_101": {"item": "Doodh Patti", "qty": 2, "price": 60},
    "order_102": {"item": "Karak Chai", "qty": 1, "price": 50}
}
```

### 5. Comprehensions: Fast Pythonic Transformations
Loop likhne ke bajaye single-line vectorized syntax:
```python
prices = [60, 120, 50, 40]
discounted = [p * 0.9 for p in prices if p > 50]
```',
  'Deep dive into Python built-in collections: memory mechanics, algorithmic time complexity, hash tables, sets for token deduplication, and idiomatic comprehensions.',
  '# Data Structures & Comprehensions
import time

# 1. List vs Set Lookup Benchmark
dataset_size = 100_000
raw_tokens = [f"token_{i}" for i in range(dataset_size)]
token_set = set(raw_tokens)

target = "token_99999"

# Measure List scan O(N)
t0 = time.perf_counter()
found_in_list = target in raw_tokens
t_list = time.perf_counter() - t0

# Measure Set hash lookup O(1)
t0 = time.perf_counter()
found_in_set = target in token_set
t_set = time.perf_counter() - t0

print(f"List Lookup O(N): {t_list*1000:.4f} ms")
print(f"Set Lookup O(1):  {t_set*1000:.4f} ms")
print(f"Speedup: {t_list / max(t_set, 1e-9):.1f}x tez!")

# 2. Dictionary Comprehension for Chai Menu
menu = {"chai": 60, "paratha": 120, "bun_kabab": 150}
taxed_menu = {item: round(price * 1.16, 2) for item, price in menu.items()}
print("Menu with 16% GST:", taxed_menu)',
  '@preset midnight
@animate pulse
flow LR: Data Structure Lookup Performance
  list_scan[List Linear Scan O(N)] $code -> mem_slow[Sequential Pointer Chasing] $alert
  set_hash[Set / Dict Hash Lookup O(1)] $database -> mem_fast[Direct Hash Bucket Jump] $ok *',
  'flow',
  '[{"title": "Python Time Complexity Documentation", "url": "https://wiki.python.org/moin/TimeComplexity"}]'::jsonb,
  20,
  2
from public.modules m
where m.slug = 'python-zero-se-hero'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '0.3',
  'python-functions-scope-closures',
  'Functions, Scope, Closures, *args/**kwargs & Lambda Functions',
  30,
  'theory_and_code',
  'AI applications mein har model pipeline, inference engine, aur data cleaner modular functions par depend karta hai.

### 1. Functions Are First-Class Citizens
Python mein function koi alag makhlooq nahi hai, balki ek standard object hai! Iska matlab:
* Aap function ko variable mein assign kar sakte hain.
* Function ko doosre function ke andar argument ke taur par pass kar sakte hain (Callbacks).
* Function se naya function return kar sakte hain (Higher-Order Functions & Closures).

### 2. Variable Scope: LEGB Rule
Python variable ko dhoondte waqt 4 darjaat check karta hai:
1. **L (Local):** Function ke andar define kiya gaya variable.
2. **E (Enclosing):** Nested function ke parent function ka scope.
3. **G (Global):** File / Module level ka scope.
4. **B (Built-in):** Python ke apne functions jese `print`, `len`, `range`.

### 3. *args aur **kwargs: Flexible Parameter Dispatching
Jab aapko pehle se pata na ho ke function mein kitne arguments aayenge (jese AI model inference parameters):
* `*args`: Saare positional arguments ko **Tuple** bana kar accept karta hai.
* `**kwargs`: Saare named keyword arguments ko **Dictionary** bana kar accept karta hai.

### 4. Function Decorators: Logging & Telemetry
Decorator ek aisa function hota hai jo kisi doosre function ke gird wrapper bana kar uski behavior ko extend karta hai bina original code ko chhere:
```python
def log_execution(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__}...")
        return fn(*args, **kwargs)
    return wrapper
```',
  'Master first-class functions, the LEGB scope hierarchy, variable arguments dispatching with *args/**kwargs, closures, and observability decorators.',
  'import time
from functools import wraps

# 1. Production Decorator: Telemetry & Benchmark
def benchmark(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = fn(*args, **kwargs)
        duration = time.perf_counter() - t0
        print(f"[Benchmark] {fn.__name__} executed in {duration*1000:.3f} ms")
        return result
    return wrapper

# 2. Flexible Function with *args and **kwargs
@benchmark
def calculate_chai_bill(base_price: float, *extras, discount_pct: float = 0.0, **metadata):
    total = base_price + sum(extras)
    total -= total * (discount_pct / 100.0)
    print(f"Order for {metadata.get(''customer'', ''Guest'')} at Table {metadata.get(''table'', ''Counter'')}")
    return total

bill = calculate_chai_bill(60.0, 20.0, 15.0, discount_pct=10.0, customer="Aslam Bhai", table=4)
print(f"Final Bill Amount: Rs {bill:.2f}")',
  '@preset midnight
@animate wave
flow LR: LEGB Scope Resolution Flow
  l[Local Scope: Inside Function] $code -> e[Enclosing Scope: Parent Def] $box
  e -> g[Global Scope: Module Level] $terminal
  g -> b[Built-in Scope: Python Core] $database *',
  'flow',
  '[{"title": "Real Python: Python Decorators Guide", "url": "https://realpython.com/primer-on-python-decorators/"}]'::jsonb,
  20,
  3
from public.modules m
where m.slug = 'python-zero-se-hero'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '0.4',
  'python-oop-classes-dataclasses',
  'Object-Oriented Programming (OOP) for AI: Classes, Methods & @dataclass',
  40,
  'theory_and_code',
  'PyTorch ka `nn.Module`, Hugging Face ke models, aur LangChain ke components sab Object-Oriented Programming (OOP) par bane hain! Agar aapko classes ki samajh nahi to AI code samajhna namumkin ho jata hai.

### 1. Class Aur Object Ka Falsafa
* **Class:** Blue-print ya Naqsha (jese Ghar ka blue-print).
* **Object / Instance:** Us naqshe par bana hua haqeeqi ghar jo memory mein space leta hai.
* `__init__`: Constructor jo object bante hi execute hota hai.
* `self`: Current instance ka pointer.

### 2. Dunder (Double Underscore) Magic Methods
Python ki asli taqat dunder methods mein hai:
* `__repr__`: Developer-friendly string representation.
* `__len__`: `len(my_object)` call hone par kya return ho.
* `__getitem__`: `my_object[0]` array indexing support karne ke liye (jese PyTorch Dataset).
* `__call__`: Object ko function ki tarah execute karne ke liye `model(input_tensors)`.

### 3. Modern @dataclass(slots=True)
Traditional Python classes mein har instance ke sath ek dynamic dictionary `__dict__` jurti hai jo bohot memory leti hai.
Python 3.10+ mein `@dataclass(slots=True)` use karne se:
1. `__init__`, `__repr__`, aur `__eq__` khud ba khud generate ho jate hain.
2. Memory 25% kam use hoti hai.
3. Attribute lookup 20% fast ho jata hai.',
  'Understand classes, inheritance, dunder protocols (__call__, __len__, __getitem__), and memory-optimized modern @dataclass with slots.',
  'from dataclasses import dataclass, field
from typing import List

# Modern Python 3.12 @dataclass with slots
@dataclass(slots=True)
class MenuItem:
    name: str
    price: float
    category: str = "beverage"

@dataclass(slots=True)
class DhabaOrder:
    order_id: int
    customer_name: str
    items: List[MenuItem] = field(default_factory=list)

    def add_item(self, item: MenuItem):
        self.items.append(item)

    @property
    def total_bill(self) -> float:
        return sum(item.price for item in self.items)

    def __repr__(self) -> str:
        return f"<Order #{self.order_id}: {self.customer_name} ({len(self.items)} items) -> Rs {self.total_bill}>"

# Create Order
order = DhabaOrder(order_id=1, customer_name="Hamza")
order.add_item(MenuItem("Doodh Patti", 60.0))
order.add_item(MenuItem("Samosa", 40.0, category="snack"))
order.add_item(MenuItem("Special Elaichi Chai", 80.0))

print(order)
print(f"Total payable: Rs {order.total_bill:.2f}")',
  '@preset midnight
@animate flow
flow LR: OOP Class Memory Optimization
  standard[Standard Python Class] $code -> dict_mem[Instance __dict__ Dynamic Heap] $alert
  dataclass_slot[@dataclass slots=True] $database -> fixed_struct[C-Aligned Fixed Offset Struct] $ok *',
  'flow',
  '[{"title": "Python Dataclasses Documentation", "url": "https://docs.python.org/3/library/dataclasses.html"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'python-zero-se-hero'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '0.5',
  'python-files-json-apis',
  'File Handling, JSON, Parquet & REST API Requests for Data Harvesting',
  35,
  'theory_and_code',
  'AI models bina clean data ke bekaar hain. Is sabaq mein hum seekhein ge ke kaise disk se files read/write ki jati hain, JSON format handle hota hai, aur internet APIs se data harvest kiya jata hai.

### 1. Context Managers: Resource Leaks Ko Khatam Karein
File open karke close karna bhool jana sab se bara memory leak hai. Python ka `with` statement ensure karta hai ke file hamesha band ho chahe koi error hi kyun na aaye:
```python
with open("khata.json", "w", encoding="utf-8") as f:
    f.write(data)
```

### 2. JSON & JSONL: LLM Ka Universal Language
* **JSON:** Single document ya object ke liye perfect.
* **JSONL (JSON Lines):** Har line par ek alag JSON object hota hai. LLM fine-tuning datasets (Unsloth, OpenAI, Anthropic) 100% JSONL format use karte hain kyunke isay pura memory mein load kiye baghair stream kiya ja sakta hai!

### 3. REST API Requests With Error Handling
Internet se data fetch karte waqt hamesha network errors aur API rate limits (429 Too Many Requests) ka khayal rakhna parta hai:
```python
try:
    response = requests.get(api_url, timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")
```',
  'Learn file stream safety with context managers, JSON/JSONL serialization for LLM datasets, robust try/except error handling, and REST API harvesting.',
  'import json
import tempfile
import os

# 1. JSON Persistence (Dhaba Khata File)
khata_data = [
    {"bill_id": 101, "customer": "Bimo", "items": ["Special Chai", "Paratha"], "total": 180},
    {"bill_id": 102, "customer": "Ali", "items": ["Doodh Patti"], "total": 60}
]

with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".jsonl") as tmp:
    # Write as JSON Lines (JSONL) - SOTA AI Dataset standard
    for record in khata_data:
        tmp.write(json.dumps(record) + "\n")
    tmp_path = tmp.name

print(f"JSONL Saved to temp file: {tmp_path}")

# Read line-by-line streaming (Zero memory spike)
print("\nStreaming records from disk:")
with open(tmp_path, "r", encoding="utf-8") as f:
    for line in f:
        record = json.loads(line.strip())
        print(f"Bill #{record[''bill_id'']} -> {record[''customer'']}: Rs {record[''total'']}")

os.remove(tmp_path)',
  '@preset midnight
@animate flow
flow LR: Data Harvesting & JSONL Storage
  remote_api[Web REST API] $cloud -> parser[HTTP Client & JSON Parser] $terminal
  parser -> validator[Schema Validation] $code
  validator -> jsonl_disk[(Streaming JSONL On Disk)] $database *',
  'flow',
  '[{"title": "Python JSON Documentation", "url": "https://docs.python.org/3/library/json.html"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'python-zero-se-hero'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '0.6',
  'python-numpy-pandas-foundations',
  'NumPy & Pandas Foundations: Vectors, Matrices & Fast Tabular Manipulation',
  45,
  'theory_and_code',
  'Mubarak ho! Aapne pure Python ke tamam zaroori pillars master kar liye hain. Ab hum qadam rakh rahe hain **Numerical & Tabular Python** mein jo AI Engineering ka gateway hai!

### 1. NumPy: High-Performance Numerical Arrays
Python list mein har number ek generic pointer hota hai. Jabke NumPy `ndarray` memory mein ek contiguous binary block hota hai.
* 1D Array = **Vector** (e.g. word embeddings ya feature list)
* 2D Array = **Matrix** (e.g. tabular dataset ya image pixels)
* 3D+ Array = **Tensor** (e.g. batch of transformer attention weights)

NumPy broadcasting se aap bina loop lagaye poore array ko multiply kar sakte hain:
```python
import numpy as np
salaries = np.array([45000, 60000, 85000, 120000])
with_bonus = salaries * 1.15 # Vectorized 15% increase in 1 CPU cycle!
```

### 2. Pandas: Data Analysis & Feature Wrangling
Pandas tabular datasets (CSVs, Excel, SQL queries) ke liye Python ka sab se powerful tool hai:
* `DataFrame`: Row aur Column table structure.
* Filtering: `df[df[''sales''] > 1000]`
* Groupby: `df.groupby(''city'')[''revenue''].mean()`

Yeh foundation aapko Module 1: Python for AI & Fast Math ke liye 100% tayar kar deti hai!',
  'The bridge from pure Python to AI Engineering: NumPy n-dimensional arrays, vector broadcasting, Boolean indexing, and Pandas DataFrame data wrangling.',
  'import numpy as np
import pandas as pd

# 1. NumPy Vectorized Operations
prices = np.array([60, 120, 50, 40, 80], dtype=np.float32)
quantities = np.array([10, 4, 15, 8, 6], dtype=np.float32)

# Vectorized Dot Product (Total Revenue)
total_revenue = np.dot(prices, quantities)
print(f"NumPy Vectorized Total Revenue: Rs {total_revenue:.2f}")

# 2. Pandas DataFrame Manipulation
sales_records = {
    "item": ["Doodh Patti", "Lachha Paratha", "Elaichi Chai", "Samosa", "Bun Kabab"],
    "category": ["Chai", "Food", "Chai", "Snack", "Food"],
    "unit_price": [60, 120, 80, 40, 150],
    "units_sold": [120, 45, 60, 80, 35]
}

df = pd.DataFrame(sales_records)
df["total_sales"] = df["unit_price"] * df["units_sold"]

print("\n--- Dhaba Sales DataFrame ---")
print(df[["item", "category", "total_sales"]])

print("\nCategory Wise Revenue Summary:")
summary = df.groupby("category")["total_sales"].sum()
print(summary)',
  '@preset midnight
@animate pulse
flow LR: The AI Engineering Transition Bridge
  py_syntax[Module 0: Python Core Syntax] $code -> np_vec[Module 0.6: NumPy Vectors] $cpu
  np_vec -> pd_df[Module 0.6: Pandas DataFrames] $database
  pd_df -> ai_math[Module 1: High-Performance Tensors & Fast Math] $brain *',
  'flow',
  '[{"title": "NumPy Quickstart", "url": "https://numpy.org/doc/stable/user/quickstart.html"}, {"title": "Pandas 10-Minute Guide", "url": "https://pandas.pydata.org/docs/user_guide/10min.html"}]'::jsonb,
  30,
  6
from public.modules m
where m.slug = 'python-zero-se-hero'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '1.1',
  'python-vectors-tensors',
  'Python Data Structures Se NumPy Tensors Tak',
  25,
  'theory_and_code',
  'So guys, aaj hum AI Engineering ka sab se pehla aur ahem qadam utha rahe hain! Aksar log samajhte hain ke AI koi jaadu hai, lekin dar-haqeeqat modern AI model ek bohot bara mathematical function hai jo numbers (Tensors) input leta hai aur numbers return karta hai.

Python mein standard `list` dynamic hoti hai — iska matlab yeh hai ke memory mein har element ka pointer alag jagah store hota hai (pointer chasing). Jab aap 1 million numbers par Python ka `for` loop chalate hain to CPU cache misses ki wajah se program bohot slow ho jata hai.

Iske bar-aks **NumPy Arrays** C-contiguous memory blocks use karte hain. Iska faida yeh hota hai ke modern CPUs ke SIMD (Single Instruction Multiple Data) registers ek hi clock cycle mein 4 se 8 numbers ko parallel process kar sakte hain! Yeh wahi concept hai jo aage chal kar GPU acceleration ka bunyadi pillar banta hai.',
  'Understand CPU memory locality, cache hierarchy, and why NumPy vectorized operations deliver 50x-100x speedups over pure Python loops.',
  'import time
import numpy as np

# 1. Pure Python Loop
size = 5_000_000
list_a = list(range(size))
list_b = list(range(size))

start = time.perf_counter()
py_result = [a * b for a, b in zip(list_a, list_b)]
py_time = time.perf_counter() - start

# 2. NumPy Vectorized Operation (SIMD)
np_a = np.arange(size, dtype=np.float32)
np_b = np.arange(size, dtype=np.float32)

start = time.perf_counter()
np_result = np_a * np_b
np_time = time.perf_counter() - start

print(f"Python Loop Time: {py_time:.4f}s")
print(f"NumPy Vector Time: {np_time:.4f}s")
print(f"Speedup: {py_time / np_time:.1f}x tez!")',
  '@preset midnight
@animate flow
flow LR: Vectorized Memory Layout
  mem_py[Python List: Scattered Pointers] $code -> cpu[CPU Cache Misses] $server
  mem_np[NumPy: Contiguous 32-bit Float Block] $database -> simd[CPU SIMD 8-lane Parallel] $cpu *',
  'flow',
  '[{"title": "NumPy Array Memory Layout", "url": "https://numpy.org/doc/stable/reference/arrays.ndarray.html"}]'::jsonb,
  15,
  1
from public.modules m
where m.slug = 'python-for-ai-and-fast-math'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '1.2',
  'linear-algebra-intuition',
  'Linear Algebra Intuition: Dot Products, Projections & Embeddings',
  30,
  'theory_and_code',
  'So guys, jab hum kisi word ya document ko AI ke hawaley karte hain, to computer text ko direct nahi samajhta. Hum har word ya text chunk ko ek **High-Dimensional Vector (Embedding)** mein convert karte hain (jaise 1536 ya 3072 numbers ka vector).

Lekin do vectors kitne similar hain yeh kaise pata chale ga? Yahan kaam aata hai **Dot Product** aur **Cosine Similarity**!
Dot product ka geometrical formula hai:
$u \cdot v = |u| |v| \cos(\theta)$

Agar dono vectors ek hi direction mein point kar rahe hain to $\cos(0) = 1$ (100% semantic similarity). Agar dono aapas mein perpendicular (90 degrees) hain to $\cos(90) = 0$ (koi similarity nahi). Yahi formula poori RAG (Retrieval-Augmented Generation) aur Vector Search ki bunyad hai!',
  'Explore geometric intuition of vector spaces, dot products, projections, and cosine similarity underlying vector search and RAG.',
  'import numpy as np

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    # u . v / (||u|| * ||v||)
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
    return float(dot_product / (norm_v1 * norm_v2))

# Real Embedding Simulation
king = np.array([0.91, 0.12, 0.85], dtype=np.float32)
queen = np.array([0.89, 0.15, 0.82], dtype=np.float32)
apple = np.array([0.11, 0.95, -0.42], dtype=np.float32)

print(f"Similarity (King, Queen): {cosine_similarity(king, queen):.4f}") # High
print(f"Similarity (King, Apple): {cosine_similarity(king, apple):.4f}") # Low',
  '@preset midnight
@animate pulse
arch LR: Embedding Vector Angle
  vec_a[Vector A: King] $terminal -> dot[Dot Product u . v] $brain
  vec_b[Vector B: Queen] $terminal -> dot
  dot -> norm[Norm Normalization ||u|| ||v||] $layers
  norm -> sim[Cosine Similarity: 0.98 Close] $chart *',
  'arch',
  '[{"title": "Cosine Similarity Mathematics", "url": "https://en.wikipedia.org/wiki/Cosine_similarity"}]'::jsonb,
  20,
  2
from public.modules m
where m.slug = 'python-for-ai-and-fast-math'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '1.3',
  'calculus-gradient-descent',
  'Calculus & Gradient Descent: Cost Function Ko Zero Karna',
  35,
  'theory_and_code',
  'So guys, ab sawal yeh paida hota hai ke AI Model "Seekhta" kaise hai?
Jawab hai: **Calculus aur Gradient Descent**!

Har neural network mein lakhoon ya arabon parameters hote hain (weights aur biases). Shuru mein yeh weights bilkul random hote hain, to model ghalat predictions deta hai. Hum ek **Loss Function** (jaise Mean Squared Error ya Cross Entropy) calculate karte hain jo batata hai ke model kitni bari ghalti kar raha hai.

Gradient dar-haqeeqat multi-variable derivative hota hai:
$\nabla L = \left[ \frac{\partial L}{\partial w_1}, \frac{\partial L}{\partial w_2}, \dots \right]$
Yeh vector batata hai ke "kis direction mein chalne se loss sab se tez barhega".
Is liye hum loss kam karne ke liye gradient ke **opposite (negative)** direction mein chalte hain:
$w = w - \eta \cdot \nabla L$
Jahan $\eta$ (eta) learning rate hai!',
  'Understand multivariable calculus, partial derivatives, loss surfaces, and parameter updates via gradient descent.',
  'import numpy as np

# Synthetic Dataset: y = 3x + 2 + noise
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1) * 0.1

# Initialize Weight and Bias randomly
w = np.random.randn(1, 1)
b = np.zeros((1, 1))
learning_rate = 0.05
epochs = 200

# Training Loop: Gradient Descent from scratch
for epoch in range(epochs):
    # 1. Forward Pass: y_hat = Xw + b
    y_pred = X.dot(w) + b
    loss = np.mean((y_pred - y) ** 2)
    
    # 2. Compute Gradients: dL/dw and dL/db
    N = len(X)
    dw = (2 / N) * X.T.dot(y_pred - y)
    db = (2 / N) * np.sum(y_pred - y)
    
    # 3. Update Parameters
    w -= learning_rate * dw
    b -= learning_rate * db
    
    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch+1:03d} | Loss: {loss:.4f} | w: {w[0,0]:.3f} | b: {b[0,0]:.3f}")

print(f"Final Learned Equation: y = {w[0,0]:.2f}x + {b[0,0]:.2f} (Target was ~ 3.00x + 4.00)")',
  '@preset midnight
@animate flow
flow LR: Gradient Descent Step
  weights[Current Weights w] $database -> fwd[Forward Prediction Xw + b] $cpu
  fwd -> loss[Loss Surface L(w)] $chart
  loss -> grad[Gradient dL/dw] $brain
  grad -> update[Weight Update: w - eta*grad] $terminal *
  update -> weights',
  'flow',
  '[{"title": "Calculus for Deep Learning", "url": "https://ml-cheatsheet.readthedocs.io/en/latest/gradient_descent.html"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'python-for-ai-and-fast-math'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '1.4',
  'memory-profiling-gil-async',
  'Python 3.12 GIL, Memory Profiling & AsyncIO for AI Pipelines',
  35,
  'theory_and_code',
  'So guys, jab hum production AI applications banate hain, to sab se bara bottleneck Python ka **GIL (Global Interpreter Lock)** aur memory leaks bante hain!

Aksar log sochte hain ke Python mein multi-threading se sab kuch fast ho jayega, lekin CPU-bound tasks (jaise tensor math) mein GIL sirf ek CPU core use karne deta hai. Jabke I/O-bound tasks (jaise remote LLM API calls, vector search queries, document streaming) ke liye **AsyncIO** sab se best solution hai. Ek single async event loop par aap thousands of concurrent LLM streams serve kar sakte hain!

Sath hi, Python 3.12 mein strict typing aur `@dataclass(slots=True)` use karne se memory 20% kam use hoti hai kyunke Python per-instance `__dict__` allocate nahi karta, balke C-struct jaisa fixed memory block banata hai. Is lesson mein hum `tracemalloc` se memory profiling aur `asyncio.gather` se concurrent streaming master karenge.',
  'Master Python GIL constraints, memory profiling with tracemalloc, dataclass slots memory savings, and AsyncIO event loops for high-throughput AI API calls.',
  'import asyncio
import tracemalloc
import time
from dataclasses import dataclass

@dataclass(slots=True)
class PromptTask:
    task_id: int
    prompt: str
    temperature: float

async def simulate_llm_stream(task: PromptTask) -> dict:
    await asyncio.sleep(0.05)
    return {
        "task_id": task.task_id,
        "tokens": len(task.prompt.split()) * 4,
        "status": "completed"
    }

async def run_batch():
    tracemalloc.start()
    tasks = [PromptTask(i, f"Roman Urdu AI prompt number {i}", 0.7) for i in range(500)]
    
    start_time = time.perf_counter()
    results = await asyncio.gather(*(simulate_llm_stream(t) for t in tasks))
    elapsed = time.perf_counter() - start_time
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Processed {len(results)} LLM calls in {elapsed:.3f}s via AsyncIO!")
    print(f"Peak RAM used: {peak / 1024:.2f} KB (slots=True efficiency)")

asyncio.run(run_batch())',
  '@preset midnight
@animate flow
flow LR: AsyncIO High-Concurrency LLM Streamer
  event_loop[AsyncIO Single Event Loop] $server -> req1[Async LLM Stream 1] $cloud
  event_loop -> req2[Async LLM Stream 2] $cloud
  event_loop -> req3[Async LLM Stream 3] $cloud
  req1 -> collector[Token Accumulator] $database
  req2 -> collector
  req3 -> collector *',
  'flow',
  '[{"title": "Python AsyncIO Documentation", "url": "https://docs.python.org/3/library/asyncio.html"}, {"title": "Python Dataclasses Slots", "url": "https://docs.python.org/3/library/dataclasses.html"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'python-for-ai-and-fast-math'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '1.5',
  'polars-arrow-data-wrangling',
  'High-Performance Data Wrangling with Polars & Apache Arrow',
  35,
  'theory_and_code',
  'So guys, classical AI tutorials mein sab Pandas sikhate hain, lekin 2026 production AI pipelines mein Pandas outdated ho chuka hai! Pandas single-threaded hai aur har operation par data ki nayi copy banata hai (RAM explosion).

Modern standard hai **Polars** jo Rust mein likha gaya hai aur **Apache Arrow** columnar memory format par chalta hai. Polars ke 3 baray faiday hain:
1. **Multi-threaded Execution**: CPU ke tamam cores ko parallel use karta hai.
2. **Lazy Evaluation (`lazy()`)**: Aapke filters aur transformations ko pehle analyze karke optimal query execution plan banata hai (Predicate Pushdown).
3. **Zero-Copy Arrow Memory**: Parquet files ko direct RAM mein stream karta hai bina kisi overhead ke.',
  'Leverage Polars and Apache Arrow for zero-copy memory layouts, multi-threaded SIMD parallel query execution, and streaming data pipelines.',
  'import polars as pl
import numpy as np

# Create synthetic 100k e-commerce records
n_records = 100_000
df = pl.DataFrame({
    "order_id": np.arange(n_records),
    "customer_region": np.random.choice(["Karachi", "Lahore", "Islamabad", "Peshawar"], n_records),
    "order_amount": np.random.uniform(500, 15000, n_records),
    "is_returned": np.random.choice([True, False], n_records, p=[0.12, 0.88])
})

query = (
    df.lazy()
    .filter(pl.col("is_returned") == False)
    .group_by("customer_region")
    .agg([
        pl.count().alias("total_delivered_orders"),
        pl.col("order_amount").sum().round(2).alias("total_revenue"),
        pl.col("order_amount").mean().round(2).alias("avg_order_value")
    ])
    .sort("total_revenue", descending=True)
)

result = query.collect()
print("Polars Aggregation Results:")
print(result)',
  '@preset midnight
@animate pulse
arch LR: Polars Apache Arrow Columnar Engine
  raw[Raw Parquet Ingestion] $database -> arrow[Apache Arrow Columnar Layout] $cube
  arrow -> rust_engine[Rust Multi-Threaded Query Optimizer] $cpu *
  rust_engine -> pred[Predicate Pushdown & SIMD Filtering] $layers
  pred -> out[Sanitized Clean Batch] $terminal',
  'arch',
  '[{"title": "Polars Documentation", "url": "https://docs.pola.rs/"}, {"title": "Apache Arrow Specification", "url": "https://arrow.apache.org/"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'python-for-ai-and-fast-math'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '1.6',
  'module-1-capstone-ingestion',
  'Module 1 Capstone: 500k Record Enterprise Ingestion & Sanitization Engine',
  50,
  'project',
  'So guys, mubarak ho! Aapne Module 1 ke tamam foundational concepts (NumPy, Linear Algebra, Calculus, Memory Profiling aur Polars) mukammal kar liye hain. Ab waqt hai aapke **Pehle Real-World Production Capstone** ka!

Is capstone mein aap ek end-to-end Enterprise Ingestion Pipeline implement karenge jo 500,000 raw customer feedback comments ko stream karegi:
1. Dirty text sanitization (HTML removal, unicode normalization, Urdu/English mixed character cleaning).
2. Data validation with strict typed schema.
3. Fast token length distribution calculation via Polars.
4. Exporting to partitioned Parquet chunks jo aglay modules mein Embedding generation ke liye 100% ready honge!',
  'Build an end-to-end multi-threaded data ingestion and sanitization pipeline processing 500k records into embedding-ready Parquet partitions.',
  'import polars as pl
import re

def clean_urdu_english_text(raw_text: str) -> str:
    clean = re.sub(r''<.*?>'', '''', raw_text)
    clean = re.sub(r''http\S+'', '''', clean)
    clean = re.sub(r''\s+'', '' '', clean).strip()
    return clean

raw_batch = pl.DataFrame({
    "id": [101, 102, 103, 104],
    "comment": [
        "<b>Bohot zabardast product hai!</b> 100% recommend: https://shop.com/p1",
        "Delivery bohot late thi... <br> lekin customer support accha tha.",
        "Quality bilkul bakwas hai, refund chahiye!",
        "AI course ne meri coding style transform kar di! Highly recommended."
    ]
})

sanitized_batch = raw_batch.with_columns(
    pl.col("comment").map_elements(clean_urdu_english_text, return_dtype=pl.Utf8).alias("clean_comment")
).with_columns(
    pl.col("clean_comment").str.len_chars().alias("char_count")
)

print("Capstone Sanitized Data:")
print(sanitized_batch)',
  '@preset midnight
@animate flow
flow LR: Enterprise Ingestion Pipeline
  raw[Raw Webhook Stream (500k Records)] $cloud -> validator[Pydantic Type Validator] $code
  validator -> polars_sink[Polars Streaming Sink] $database
  polars_sink -> parquet_store[Embedding-Ready Parquet Chunks] $server *',
  'flow',
  '[{"title": "Data Pipeline Best Practices", "url": "https://docs.pola.rs/user-guide/concepts/streaming/"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'python-for-ai-and-fast-math'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '2.1',
  'how-llms-work',
  'LLMs Kaise Kaam Karte Hain: Next Token Prediction & Context Window',
  30,
  'theory_and_code',
  'So guys, Large Language Models (LLMs) ke baare mein sab se ahem mental model yeh hai: **LLM koi database ya conscious mind nahi hai; yeh ek statistical next-token prediction engine hai!**

Jab aap model ko prompt dete hain, to model us text ko **Tokens** (sub-words) mein break karta hai. Phir har step par model apni vocabulary mein se aglay token ki probability distribution calculate karta hai.
Maslan agar sentence hai: "Pakistan ka qaumi khel ___ hai", to model `hockey` ko 92%, `cricket` ko 6%, aur `football` ko 1% probability assign karega.

Yahan 3 critical sampling parameters kaam aate hain:
1. **Temperature ($T$)**: Logits ko divide karta hai. $T=0$ ka matlab Greedy Search (hamesha highest probability token choose karo). $T=1.0$ creative outputs deta hai.
2. **Top-P (Nucleus Sampling)**: Sirf un tokens ko consider karta hai jinki cumulative probability $P$ tak pohnchti hai.
3. **Context Window**: Model ki memory limit jahan tak wo pichle tokens dekh sakta hai.',
  'Understand next-token autoregressive generation, logits, temperature scaling, top-p nucleus sampling, and context window economics.',
  'import numpy as np

# Simulate Vocabulary Logits for Next Token Prediction
vocab = ["cricket", "hockey", "football", "biryani", "code"]
logits = np.array([2.1, 4.8, 1.2, -1.5, 0.5])

def softmax_with_temp(logits: np.ndarray, temperature: float = 1.0) -> np.ndarray:
    scaled = logits / max(temperature, 1e-5)
    exp_scaled = np.exp(scaled - np.max(scaled)) # numerical stability
    return exp_scaled / np.sum(exp_scaled)

print("--- Temperature 0.1 (Greedy / Deterministic) ---")
probs_low = softmax_with_temp(logits, temperature=0.1)
for word, p in zip(vocab, probs_low):
    print(f"  {word:10s}: {p*100:.2f}%")

print("
--- Temperature 1.2 (Creative / Random Exploration) ---")
probs_high = softmax_with_temp(logits, temperature=1.2)
for word, p in zip(vocab, probs_high):
    print(f"  {word:10s}: {p*100:.2f}%")',
  '@preset midnight
@animate flow
flow LR: Next Token Prediction Pipeline
  input_text[Prompt Text] $terminal -> tokenize[BPE Tokenizer] $code
  tokenize -> transformer[Decoder Transformer] $brain
  transformer -> logits[Vocabulary Logits Vector] $layers
  logits -> softmax[Softmax + Temperature] $cpu
  softmax -> next_tok[Selected Next Token] $cube *',
  'flow',
  '[{"title": "What Are Large Language Models?", "url": "https://www.youtube.com/watch?v=zjkBMFhNj_g"}]'::jsonb,
  20,
  1
from public.modules m
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '2.2',
  'prompt-patterns-cot',
  'Prompt Engineering Patterns: Zero-Shot, Few-Shot & Chain-of-Thought',
  35,
  'theory_and_code',
  'So guys, agar aap LLM se mushkil mathematical ya logical sawaal poochein to direct Zero-Shot prompt aksar fail ho jata hai. Kyun?
Kyunke LLM agla token bina kisi "rough work" ke foran generate karne ki koshish karta hai!

Yahan do powerful techniques aati hain:
1. **Few-Shot Prompting**: Model ko 2 se 3 solved examples provide karein taake wo pattern aur format samajh jaye.
2. **Chain-of-Thought (CoT)**: Model ko majboor karein ke wo final answer se pehle step-by-step reasoning likhay: *"Let''s think step by step"*.

Jab model intermediate tokens generate karta hai, to wo tokens aglay step ke context mein add ho jate hain — is tarah model ko extra computational capacity milti hai! DeepSeek-R1 aur OpenAI o1 isi fundamental principle ko reinforcement learning se scale karte hain.',
  'Master In-Context Learning: Zero-Shot vs Few-Shot prompt templates, Chain-of-Thought scratchpads, and least-to-most task decomposition.',
  '# Demonstration of Chain-of-Thought (CoT) Prompt Pattern

direct_zero_shot_prompt = (
    "Q: Ek dukaan par 12 dahi bhallay hain. 4 log aaye aur har ek ne 2 plate khaye.\n"
    "Dukaan walay ne 5 naye banaye. Dukaan par kitne dahi bhallay bache?\nAnswer:"
)

chain_of_thought_prompt = (
    "Sawaal: Ek dukaan par 12 dahi bhallay hain. 4 log aaye aur har ek ne 2 plate khaye.\n"
    "Dukaan walay ne 5 naye banaye. Dukaan par kitne dahi bhallay bache?\n\n"
    "Aap step-by-step sochein:\n"
    "1. Shuru mein total dahi bhallay = 12\n"
    "2. 4 logo ne 2, 2 plate khaye: 4 * 2 = 8 khaye gaye.\n"
    "3. Baqi bache: 12 - 8 = 4.\n"
    "4. Dukaan walay ne 5 naye banaye: 4 + 5 = 9.\n\n"
    "Jawab: 9 dahi bhallay baqi hain."
)

print("CoT Pattern ready for LLM submission. Model accuracy increases from 35% to 85%!")',
  '@preset midnight
@animate pulse
arch LR: CoT Reasoning Scratchpad
  prompt[Raw Multi-Step Question] $terminal -> cot[Step-by-Step Scratchpad Tokens] $brain
  cot -> intermediate[Intermediate Computation Storage] $database
  intermediate -> final[High-Confidence Final Solution] $server *',
  'arch',
  '[{"title": "Chain-of-Thought Paper (Wei et al.)", "url": "https://arxiv.org/abs/2201.11903"}]'::jsonb,
  25,
  2
from public.modules m
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '2.3',
  'structured-outputs-json',
  'Structured Outputs & Function Calling Foundations',
  35,
  'theory_and_code',
  'So guys, jab hum production mein software banate hain, to hum LLM se conversational text nahi balke **Strict JSON** chahte hain jo hamaray backend database ya API mein direct save ho sakay.

Agar aap sirf prompt mein likhein *"Please return valid JSON"*, to 100 mein se 5 dafa LLM extra markdown (```json ... ```) ya missing commas ke sath output dega aur aapka backend crash ho jayega!

Iska production solution hai **Grammar-Based Constrained Decoding / JSON Schema**.
Modern inference engines (jaise Groq, OpenAI, Gemini) LLM ke output logits par regex/grammar mask lagate hain — yaani agar agla token valid JSON bracket ya key nahi hai to model us token ko generate kar hi nahi sakta!',
  'Enforce 100% deterministic JSON schemas and constrained grammar decoding using Pydantic models for reliable backend integration.',
  'import json
from pydantic import BaseModel, Field
from typing import List

# 1. Define Strict Pydantic Schema
class ProductExtraction(BaseModel):
    product_name: str = Field(description="Name of the product in Urdu/English")
    price_pkr: float = Field(description="Price converted to Pakistani Rupees")
    category: str = Field(description="Category e.g. Electronics, Grocery")
    tags: List[str] = Field(default_factory=list)

# 2. Extract JSON Schema for LLM API Spec
schema = ProductExtraction.model_json_schema()
print("Generated OpenAI/Groq Compatible JSON Schema:")
print(json.dumps(schema, indent=2))

# 3. Simulated Validated Response from Model
sample_llm_output = ''{"product_name": "Pakistani Basmati Rice 5kg", "price_pkr": 1850.0, "category": "Grocery", "tags": ["premium", "rice"]}''
parsed_obj = ProductExtraction.model_validate_json(sample_llm_output)
print(f"\nParsed Object Verified: {parsed_obj.product_name} -> PKR {parsed_obj.price_pkr}")',
  '@preset midnight
@animate flow
flow LR: Constrained JSON Decoding
  llm_logits[Model Raw Logits] $brain -> grammar[Grammar / JSON Schema Mask] $code
  grammar -> filter[Invalid Tokens Logit = -inf] $layers
  filter -> json_token[Only Valid JSON Token Allowed] $server *',
  'flow',
  '[{"title": "OpenAI Structured Outputs Guide", "url": "https://platform.openai.com/docs/guides/structured-outputs"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '2.4',
  'kv-cache-context-mechanics',
  'KV Cache Architecture & Long Context Window Mechanics',
  40,
  'theory_and_code',
  'So guys, jab aap ChatGPT ya kisi LLM se baat karte hain, to kya aapne socha hai ke pehla token aane mein waqt lagta hai (Time to First Token - TTFT), lekin uske baad tokens tezi se stream hote hain?

Iska raaz hai **KV Cache (Key-Value Cache)**!
Self-attention mein har token ko pichle tamam tokens ke Key ($K$) aur Value ($V$) vectors ke sath multiply hona hota hai. Agar hum har naye token par poori chat history ko dubara compute karein, to generation $O(N^2)$ ho jayegi aur bohot slow ho jayegi.

Is liye modern inference engines pichle sabhi tokens ke $K$ aur $V$ tensors ko GPU VRAM mein cache kar letay hain. Naya token sirf apna Query ($Q$) vector calculate karta hai aur direct cached $K$ aur $V$ se multiply ho jata hai.
Lekin iska nuqsan yeh hai ke long chats mein KV Cache memory bohot barh jati hai:
$$\text{KV Cache Size} = 2 \times \text{layers} \times \text{heads} \times d_k \times \text{seq\_len} \times \text{precision bytes}$$
Is lesson mein hum KV cache ki memory math aur context window optimization ko first-principles se samjhein ge.',
  'Understand autoregressive generation memory-bandwidth bottlenecks, KV cache mathematical formulation, and GPU VRAM scaling across sequence lengths.',
  'def calculate_kv_cache_ram(
    num_layers: int,
    num_kv_heads: int,
    head_dim: int,
    seq_len: int,
    precision_bytes: int = 2 # FP16/BF16
) -> float:
    # 2 for Key and Value
    bytes_per_token = 2 * num_layers * num_kv_heads * head_dim * precision_bytes
    total_bytes = bytes_per_token * seq_len
    return total_bytes / (1024 ** 3) # in Gigabytes (GB)

# Llama-3-8B specs: 32 layers, 8 KV heads (Grouped Query Attention), head_dim 128
llama3_8b_kv_16k = calculate_kv_cache_ram(32, 8, 128, 16_384, precision_bytes=2)
llama3_8b_kv_128k = calculate_kv_cache_ram(32, 8, 128, 131_072, precision_bytes=2)

print(f"Llama 3 8B KV Cache at 16k context: {llama3_8b_kv_16k:.2f} GB RAM")
print(f"Llama 3 8B KV Cache at 128k context: {llama3_8b_kv_128k:.2f} GB RAM (Massive VRAM consumption!)")',
  '@preset midnight
@animate flow
flow LR: Autoregressive KV Cache Engine
  new_token[New Input Token] $terminal -> q_proj[Query Projection Q] $cpu
  kv_cache[Cached Prior K & V Tensors] $database -> attn_compute[Scaled Dot-Product Attention] $brain *
  q_proj -> attn_compute
  attn_compute -> next_tok[Generated Next Token] $terminal',
  'flow',
  '[{"title": "Transformers KV Cache Explained", "url": "https://kipp.ly/transformer-inference-survey/"}]'::jsonb,
  30,
  4
from public.modules m
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '2.5',
  'llm-evals-judge-benchmarks',
  'LLM Evaluation & Benchmarking: Automated LLM-as-a-Judge',
  35,
  'theory_and_code',
  'So guys, jab hum production mein prompt ya model update karte hain, to hum kaise check karein ke naya prompt pichle se behtar hai?
Purane metrics jaise BLEU ya ROUGE generative AI mein fail ho jate hain kyunke ek hi baat ko 10 mukhtalif tareeqon se kaha ja sakta hai.

Modern standard hai **LLM-as-a-Judge**!
Hum ek powerful reasoning model (jaise Claude 3.5 Sonnet ya GPT-4o) ko ek clear evaluation rubric dete hain jismein wo candidate output ko 4 dimensions par 1 se 5 score karta hai:
1. **Faithfulness**: Kya answer sirf context par mabni hai ya hallucination hai?
2. **Relevance**: Kya sawal ka seedha jawab diya gaya?
3. **Completeness**: Kya koi zaroori step miss to nahi hua?
4. **Tone & Formatting**: Kya output requested JSON ya conversational style ke mutabiq hai?',
  'Implement automated LLM evaluation pipelines using LLM-as-a-Judge, scoring rubrics, and systematic regression testing.',
  'import json

judge_rubric = (
    "You are an expert AI evaluator. Rate the assistant answer from 1 to 5 based on:\n"
    "1. Faithfulness (no hallucinations)\n"
    "2. Helpfulness and clarity in Roman Urdu\n"
    ''Return valid JSON with: {"faithfulness_score": int, "helpfulness_score": int, "critique": str}''
)

def simulate_llm_judge(question: str, context: str, answer: str) -> dict:
    # Simulated Judge Evaluation
    return {
        "question": question,
        "faithfulness_score": 5,
        "helpfulness_score": 5,
        "critique": "Answer accurately explains PyTorch autograd in clear conversational Roman Urdu with zero hallucination."
    }

eval_result = simulate_llm_judge(
    question="Autograd kaise kaam karta hai?",
    context="PyTorch autograd builds dynamic computational graphs during forward pass.",
    answer="So guys, PyTorch autograd forward pass ke dauran computational graph banata hai aur backward() par gradients calculate karta hai."
)
print("LLM-as-a-Judge Evaluation Output:")
print(json.dumps(eval_result, indent=2))',
  '@preset midnight
@animate pulse
arch LR: Automated LLM Evaluation Pipeline
  gen_answer[Candidate Model Answer] $code -> judge[Judge LLM Rubric Evaluation] $brain
  gold_ref[Ground Truth Reference] $database -> judge
  judge -> metrics[Faithfulness & Relevance Scores] $server *',
  'arch',
  '[{"title": "Judging LLM-as-a-Judge with MT-Bench", "url": "https://arxiv.org/abs/2306.05685"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '2.6',
  'module-2-capstone-prompt-optimizer',
  'Module 2 Capstone: Enterprise Prompt Optimization & Regression Suite',
  50,
  'project',
  'So guys, Module 2 ke Capstone mein aap ek **Automated Prompt Optimization & Regression Testing Suite** banayenge!

Enterprise mein jab product manager prompt change karta hai to aksar 20% puraane edge cases break ho jate hain (silent regression). Aapka capstone:
1. 3 mukhtalif system prompt variants (Direct, Few-Shot, Chain-of-Thought) ko 10 synthetic test cases par run karega.
2. Output ko Pydantic schema validation se verify karega.
3. Automated LLM judge ke zariye har variant ko score karega.
4. Winning prompt select karega jo highest accuracy aur lowest token cost deliver kare!',
  'Build an automated prompt optimization and regression testing suite comparing prompt variants across benchmarks to find Pareto-optimal prompts.',
  '# Module 2 Capstone: Automated Prompt Benchmark Runner
test_cases = [
    {"input": "Mera order #9921 abhi tak nahi mila, refund karein!", "expected_intent": "refund"},
    {"input": "Aapki shop par Basmati rice ka rate kya hai?", "expected_intent": "inquiry"},
    {"input": "Bohot buri service thi, packaging phati hui thi.", "expected_intent": "complaint"}
]

prompt_variants = {
    "variant_a_direct": "Classify customer message intent as: refund, inquiry, complaint.",
    "variant_b_cot": "Analyze user sentiment, identify core issue, then classify intent: refund, inquiry, complaint."
}

def evaluate_variant(name: str, template: str) -> float:
    # Simulate scoring across benchmark
    accuracy = 0.90 if "cot" in name else 0.70
    print(f"Evaluated {name}: Accuracy = {accuracy*100:.1f}%")
    return accuracy

scores = {name: evaluate_variant(name, tmpl) for name, tmpl in prompt_variants.items()}
winning_prompt = max(scores, key=scores.get)
print(f"\nWinning Production Prompt: {winning_prompt} with {scores[winning_prompt]*100}% accuracy!")',
  '@preset midnight
@animate flow
flow LR: Automated Prompt Tuning Pipeline
  base_prompt[Base System Prompt] $code -> variations[Mutation Engine (CoT / Roles)] $cube
  variations -> test_suite[Golden Test Suite (50 Cases)] $database
  test_suite -> eval_judge[Evaluation Judge LLM] $brain
  eval_judge -> winner[Pareto-Optimal Production Prompt] $terminal *',
  'flow',
  '[{"title": "DSPy: Automated Prompt Optimization", "url": "https://github.com/stanfordnlp/dspy"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '3.1',
  'supervised-learning-pipeline',
  'Supervised Learning Pipeline: Preprocessing Se Validation Tak',
  35,
  'theory_and_code',
  'So guys, jab hum Machine Learning ki dunya mein qadam rakhte hain to pehla sabq yeh hai: **GIGO (Garbage In, Garbage Out)**!
Dunya ka sab se bara model bhi bekar ثابت hoga agar aapka data preprocessing aur validation pipeline kharab hai.

ML pipeline ke 4 bunyadi steps hote hain:
1. **Feature Engineering**: Categorical variables ko One-Hot ya Target Encoding karna, aur continuous features ko scale karna (`StandardScaler`).
2. **Train/Validation/Test Split**: Kabhi bhi test data par scaler fit na karein (Data Leakage)!
3. **Cross-Validation**: 5-Fold Stratified CV se model ki stability measure karna.
4. **Evaluation Metrics**: Class imbalance mein Accuracy dhoka deti hai; wahan Precision, Recall aur F1-Score dekhna parta hai.',
  'Build leakage-free supervised learning pipelines with Scikit-learn: preprocessing, stratified cross-validation, and robust metrics.',
  'import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 1. Generate Synthetic Imbalanced Dataset
X, y = make_classification(n_samples=1000, n_features=10, weights=[0.85, 0.15], random_state=42)

# 2. Train-Test Split (Holdout set)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# 3. Leakage-Free Pipeline: Scaler fits ONLY on training folds!
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(class_weight="balanced"))
])

# 4. Stratified 5-Fold Cross Validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring="f1")

print(f"5-Fold CV F1-Scores: {scores.round(3)}")
print(f"Mean F1: {scores.mean():.3f} (+/- {scores.std():.3f})")',
  '@preset midnight
@animate flow
flow LR: Leakage-Free ML Pipeline
  raw_train[Raw Training Data] $database -> scaler[StandardScaler Fit & Transform] $layers
  scaler -> train_model[Model Training] $brain
  raw_test[Raw Test Data] $database -> scaler_test[Apply Pre-Fit Scaler Only] $layers
  scaler_test -> eval[F1 & ROC-AUC Evaluation] $chart *',
  'flow',
  '[{"title": "Scikit-Learn Common Pitfalls", "url": "https://scikit-learn.org/stable/common_pitfalls.html"}]'::jsonb,
  20,
  1
from public.modules m
where m.slug = 'classical-machine-learning'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '3.2',
  'tree-models-gradient-boosting',
  'Decision Trees Se XGBoost & LightGBM Tak',
  40,
  'theory_and_code',
  'So guys, tabular data (tables, databases, CSVs) par deep learning aksar fail ho jati hai ya bohot slow hoti hai. Dunya ke 90% Kaggle competitions aur production tabular tasks mein **Gradient Boosted Decision Trees (GBDT)** jeet-te hain!

Safar shuru hota hai ek single **Decision Tree** se jo if-else rules banata hai (Gini Impurity ya Entropy ke mutabiq). Lekin ek akela tree bohot jaldi overfit ho jata hai.
Phir aata hai **Random Forest (Bagging)**: Yeh hazaron trees parallel train karta hai aur unka average nikalta hai (Variance reduction).

Aur aakhir mein aata hai **Gradient Boosting (XGBoost / LightGBM)**:
Yeh trees ko sequential train karta hai. Pehla tree prediction karta hai; doosra tree pehle tree ke **Residuals (Errors)** ko predict karta hai; teesra tree doosre ke errors ko theek karta hai! Is tarah har naya tree model ki ghaltiyon ko khatam karta chala jata hai.',
  'Master ensemble learning: Bagging vs Boosting, tree splitting criteria, and training XGBoost models on tabular data.',
  'import numpy as np
import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Synthetic Customer Churn Dataset
X, y = make_classification(n_samples=2000, n_features=15, n_informative=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train Production XGBoost Classifier
model = xgb.XGBClassifier(
    n_estimators=100,
    learning_rate=0.08,
    max_depth=4,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="logloss",
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("XGBoost Production Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Retained", "Churned"]))',
  '@preset midnight
@animate pulse
arch LR: Gradient Boosting Tree Sequence
  data[Input Features X] $database -> tree1[Tree 1: Initial Prediction] $cpu
  tree1 -> res1[Residual Error 1] $chart
  res1 -> tree2[Tree 2: Fit on Residual 1] $cpu
  tree2 -> res2[Residual Error 2] $chart
  res2 -> tree3[Tree 3: Minimize Remaining Loss] $cpu *
  tree1 -> final[Ensemble Sum: y_hat = t1 + eta*t2 + eta*t3] $server
  tree2 -> final
  tree3 -> final',
  'arch',
  '[{"title": "XGBoost Original Paper", "url": "https://arxiv.org/abs/1603.02754"}]'::jsonb,
  25,
  2
from public.modules m
where m.slug = 'classical-machine-learning'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '3.3',
  'unsupervised-learning-clustering',
  'Dimensionality Reduction & Clustering: PCA, t-SNE & K-Means',
  35,
  'theory_and_code',
  'So guys, real-world AI pipelines mein aksar hamare paas labels (ground truth) nahi hote. Misal ke taur par, 100,000 unlabelled customer interactions ya 1536-dimensional embeddings. Yahan kaam aati hai **Unsupervised Learning**!

Do ahem techniques hain:
1. **Dimensionality Reduction (PCA & t-SNE)**: 1536-dimensional embedding vectors ko 2D ya 3D mein project karna taake hum human eyes se clusters dekh sakein. PCA linear covariance eigenvectors nikalta hai, jabke t-SNE local neighborhood probabilities ko preserve karta hai.
2. **K-Means Clustering**: Data points ko $K$ groups mein divide karna by minimizing distance from cluster centroids. Yeh customer segmentation aur vector database query routing ke liye foundation banta hai!',
  'Apply unsupervised dimensionality reduction (PCA, t-SNE) and centroid clustering (K-Means) for embedding visualization and customer segmentation.',
  'import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Simulate 500 embedding vectors in 64 dimensions
np.random.seed(42)
embeddings = np.random.randn(500, 64)

# 1. Dimensionality Reduction: Compress from 64D to 3D via PCA
pca = PCA(n_components=3)
reduced_embeddings = pca.fit_transform(embeddings)
print(f"Explained Variance Ratio (3 components): {pca.explained_variance_ratio_.sum():.2%}")

# 2. Cluster into 4 Customer Archetypes
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(reduced_embeddings)

print(f"Cluster Distribution: {np.bincount(cluster_labels)}")',
  '@preset midnight
@animate flow
flow LR: Unsupervised Embedding Clustering
  high_dim[High-Dim Embedding Space (1536-D)] $database -> pca[PCA Covariance Matrix Eigenvectors] $brain
  pca -> low_dim[Low-Dim 2D Space] $layers
  low_dim -> kmeans[K-Means Centroid Assignment] $cube *',
  'flow',
  '[{"title": "PCA Comprehensive Guide", "url": "https://scikit-learn.org/stable/modules/decomposition.html#pca"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'classical-machine-learning'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '3.4',
  'model-evaluation-metrics',
  'Rigorous Model Evaluation: Precision, Recall, F1 & ROC-AUC',
  35,
  'theory_and_code',
  'So guys, sochiye: ek bank mein 99.9% transactions legitimate hoti hain aur sirf 0.1% fraudulent. Agar koi bewaqoof model hamesha keh de "Sab kuch normal hai", to uski Accuracy 99.9% hogi! Lekin bank tabah ho jayega kyunke 100% fraud miss ho gaya!

Is liye professional AI engineers **Accuracy Trap** se bach kar yeh metrics use karte hain:
- **Precision**: Jo model ne Fraud kaha, us mein se kitne waqai Fraud thay? (False Positives minimize karna).
- **Recall**: Total Fraud transactions mein se model ne kitne pakray? (False Negatives minimize karna).
- **F1-Score**: Precision aur Recall ka Harmonic Mean: $2 \cdot \frac{P \times R}{P + R}$.
- **ROC-AUC**: Mukhtalif thresholds par model ki discrimination power measure karna.',
  'Understand confusion matrix mechanics, Precision-Recall tradeoffs, ROC-AUC curves, and optimal decision threshold selection.',
  'import numpy as np
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, roc_auc_score

# True labels vs Model probabilities
y_true = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1])
y_probs = np.array([0.05, 0.12, 0.20, 0.35, 0.45, 0.48, 0.55, 0.60, 0.85, 0.92])

# Threshold Tuning: Default 0.5 vs Conservative 0.4
for threshold in [0.5, 0.4]:
    y_pred = (y_probs >= threshold).astype(int)
    cm = confusion_matrix(y_true, y_pred)
    p, r, f1, _ = precision_recall_fscore_support(y_true, y_pred, average="binary")
    print(f"Threshold: {threshold} | Precision: {p:.2f} | Recall: {r:.2f} | F1: {f1:.2f}")

auc = roc_auc_score(y_true, y_probs)
print(f"ROC-AUC Score: {auc:.3f}")',
  '@preset midnight
@animate pulse
arch LR: Evaluation Metrics Framework
  predictions[Model Probability Output] $code -> conf_matrix[Confusion Matrix: TP, FP, TN, FN] $database
  conf_matrix -> prec_rec[Precision-Recall Curve] $chart
  conf_matrix -> f1_opt[F1-Score Optimal Threshold] $terminal *',
  'arch',
  '[{"title": "Precision and Recall Explained", "url": "https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'classical-machine-learning'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '3.5',
  'feature-engineering-pipelines',
  'Leakage-Free Feature Engineering & Sklearn Pipelines',
  35,
  'theory_and_code',
  'So guys, jab raw data tabular database se aata hai, to usmein mixed types hoti hain: numerical (income, age), categorical (city, gender), aur missing values (`NaN`).

Agar aap train aur test data ko ikattha impute ya scale kar lein, to test set ki information model mein leak ho jati hai. Model training par 99% score karta hai lekin production mein ja kar crash kar jata hai!

Iska production solution hai **Scikit-learn `ColumnTransformer` aur `Pipeline`**.
Yeh transforms ko ek atomic executable DAG banata hai jo training ke waqt parameters fit karta hai aur production mein new incoming records par sirf deterministic transform chalata hai.',
  'Construct robust end-to-end ColumnTransformers and Pipeline workflows handling missing values, scaling, and categorical encoding without data leakage.',
  'import numpy as np
import polars as pl
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge

# Mixed Feature Dataset
X = np.array([
    [25.0, "Karachi", 50000.0],
    [np.nan, "Lahore", 85000.0],
    [38.0, "Islamabad", 120000.0],
    [45.0, "Karachi", np.nan]
], dtype=object)
y = np.array([120.0, 190.0, 280.0, 210.0])

num_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

preprocessor = ColumnTransformer(transformers=[
    ("num", num_pipe, [0, 2]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), [1])
])

full_model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", Ridge(alpha=1.0))
])

full_model.fit(X, y)
print("Pipeline trained successfully with zero leakage!")',
  '@preset midnight
@animate flow
flow LR: Leakage-Free Sklearn Pipeline
  raw_feat[Raw Mixed Tabular Features] $database -> col_trans[ColumnTransformer (Numeric + Categorical)] $layers
  col_trans -> scaler[StandardScaler (Fit only on Train)] $cpu
  scaler -> model[Predictive Model Classifier] $brain *',
  'flow',
  '[{"title": "Sklearn Pipeline Composite Estimators", "url": "https://scikit-learn.org/stable/modules/compose.html"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'classical-machine-learning'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '3.6',
  'module-3-capstone-ml-service',
  'Module 3 Capstone: Production Customer Churn Predictive ML Service',
  55,
  'project',
  'So guys, Module 3 ke Capstone mein aap ek real-world **Customer Churn Prediction Service** build karenge jo SaaS aur Fintech companies ki backbone hoti hai!

Is capstone mein aap:
1. Imbalanced customer usage features ko load karenge.
2. Leakage-free Sklearn pipeline + XGBoost model train karenge.
3. Optuna se hyperparameter tuning (learning rate, tree depth, subsample) execute karenge.
4. Model ko serialized binary (`.joblib` ya `.onnx`) mein export karke FastAPI endpoint ke through sub-10ms inference benchmark verify karenge!',
  'Ship an end-to-end production ML microservice: dataset preprocessing, Optuna hyperparameter optimization, model export, and real-time inference.',
  'import xgboost as xgb
import joblib
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# 1. Train Capstone Churn Model
X, y = make_classification(n_samples=5000, n_features=12, weights=[0.8, 0.2], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = xgb.XGBClassifier(n_estimators=80, max_depth=3, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# 2. Export Model Artifact
joblib.dump(model, "churn_model.joblib")
print("Model saved to churn_model.joblib")

# 3. Simulated Fast Inference API Handler
loaded_model = joblib.load("churn_model.joblib")
new_customer_features = np.random.randn(1, 12)
churn_prob = loaded_model.predict_proba(new_customer_features)[0, 1]
print(f"Customer Churn Risk: {churn_prob*100:.1f}% -> {''Urgent Retention Intervention'' if churn_prob > 0.5 else ''Healthy Customer''}")',
  '@preset midnight
@animate flow
flow LR: Production ML Churn Microservice
  user_event[Real-Time User Feature Vector] $terminal -> fast_api[FastAPI Prediction Endpoint] $server
  fast_api -> onnx_model[ONNX Runtime Low-Latency Model] $brain
  onnx_model -> churn_score[Churn Risk Score + Interventions] $database *',
  'flow',
  '[{"title": "XGBoost Production Serving", "url": "https://xgboost.readthedocs.io/en/stable/tutorials/saving_model.html"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'classical-machine-learning'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '4.1',
  'pytorch-tensors-autograd',
  'PyTorch Tensors, GPU Acceleration & Autograd',
  35,
  'theory_and_code',
  'So guys, welcome to PyTorch! Dunya ke 95% AI research papers aur frontier labs (OpenAI, Meta, Anthropic) PyTorch use karti hain.

PyTorch ke 2 baray superpowers hain:
1. **GPU Acceleration**: NumPy arrays sirf CPU par chalte hain. PyTorch Tensors ko aap ek simple command `.to(''cuda'')` se Nvidia GPU VRAM mein bhej sakte hain jahan hazaron CUDA cores parallel calculations karte hain.
2. **Autograd (Automatic Differentiation)**: PyTorch aapke har mathematical operation ka computational graph background mein record karta rehta hai. Jab aap `loss.backward()` call karte hain to Chain Rule of Calculus automatically execute hota hai aur har parameter ka gradient calculate ho jata hai!',
  'Understand PyTorch GPU device memory allocation, CUDA acceleration, dynamic computation graphs, and the autograd backward engine.',
  'import torch

# 1. Check Device Availability
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using Compute Device: {device}")

# 2. Create Leaf Tensors with Gradient Tracking
x = torch.tensor([2.0, 3.0], requires_grad=True, device=device)
w = torch.tensor([1.5, -2.5], requires_grad=True, device=device)
b = torch.tensor(1.0, requires_grad=True, device=device)

# 3. Dynamic Forward Pass: y = w * x + b
y = w * x + b
loss = y.sum() ** 2

# 4. Backward Pass (Calculus Chain Rule automatically calculated!)
loss.backward()

print("Computation Graph Executed:")
print(f"Loss Value: {loss.item():.4f}")
print(f"dL/dw Gradient: {w.grad}")
print(f"dL/dx Gradient: {x.grad}")
print(f"dL/db Gradient: {b.grad}")',
  '@preset midnight
@animate flow
flow LR: PyTorch Autograd Graph
  w[Weight w] $database -> mul[Multiply Node (*)] $cpu
  x[Input x] $terminal -> mul
  mul -> add[Addition Node (+)] $cpu
  b[Bias b] $database -> add
  add -> loss[Loss Node] $chart *
  loss -. backward gradient stream .-> w',
  'flow',
  '[{"title": "PyTorch Autograd Mechanics", "url": "https://pytorch.org/docs/stable/notes/autograd.html"}]'::jsonb,
  25,
  1
from public.modules m
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '4.2',
  'building-mlp-neural-net',
  'Multi-Layer Perceptron (MLP) From Scratch in PyTorch',
  40,
  'theory_and_code',
  'So guys, ek single linear layer sirf seedhi lines (linear boundaries) draw kar sakti hai. Real-world problems (jaise text, images, complex churn) non-linear hoti hain.

Non-linearity introduce karne ke liye hum do linear layers ke darmian **Activation Function** lagate hain (jaise ReLU, GELU, ya SwiGLU). Is combination ko **Multi-Layer Perceptron (MLP)** kehte hain!

Har training step ke 5 muqaddas arkaan hote hain:
1. `optimizer.zero_grad()`: Pichle step ke gradients zero karna (warna PyTorch unhe accumulate kar deta hai).
2. `outputs = model(inputs)`: Forward pass.
3. `loss = criterion(outputs, targets)`: Ghalati calculate karna.
4. `loss.backward()`: Gradients calculate karna via backpropagation.
5. `optimizer.step()`: Weights ko gradient ki direction mein update karna.',
  'Construct modular neural networks using torch.nn.Module, non-linear activations, loss functions, and the canonical 5-step training loop.',
  'import torch
import torch.nn as nn
import torch.optim as optim

# 1. Define MLP Architecture
class DeepMLP(nn.Module):
    def __init__(self, in_features: int, hidden_dim: int, out_features: int):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(in_features, hidden_dim),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, out_features)
        )
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)

# 2. Instantiate Model, Loss & Optimizer
model = DeepMLP(in_features=8, hidden_dim=32, out_features=1)
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.AdamW(model.parameters(), lr=0.01, weight_decay=1e-4)

# 3. Canonical Training Step
dummy_x = torch.randn(16, 8) # Batch 16, Features 8
dummy_y = torch.randint(0, 2, (16, 1)).float()

for epoch in range(10):
    optimizer.zero_grad()
    preds = model(dummy_x)
    loss = criterion(preds, dummy_y)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1:02d} | Loss: {loss.item():.4f}")',
  '@preset midnight
@animate pulse
arch LR: MLP Feed-Forward Architecture
  in_layer[Input Vector (Dim 8)] $terminal -> l1[Linear Layer 1 (Dim 32)] $layers
  l1 -> gelu[GELU Non-Linearity] $brain
  gelu -> l2[Linear Layer 2 (Dim 32)] $layers
  l2 -> out[Output Logits (Dim 1)] $server *',
  'arch',
  '[{"title": "PyTorch Neural Networks Tutorial", "url": "https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html"}]'::jsonb,
  30,
  2
from public.modules m
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '4.3',
  'activation-functions-loss-optimizers',
  'Modern Activations (GELU, SwiGLU) & Optimizers: AdamW vs SGD',
  35,
  'theory_and_code',
  'So guys, purani textbooks mein Sigmoid aur Tanh sikhaye jaate thay jinki wajah se gradients vanish ho jate thay ($dL/dw \approx 0$). Phir ReLU aya jisne deep learning ko revolutionize kiya, lekin ReLU mein negative values par gradient permanent zero ho jata hai ("Dying ReLU problem").

2026 SOTA LLMs (jaise LLaMA 3, Gemma 2, DeepSeek) use karte hain **SwiGLU (Swish Gated Linear Unit)**:
$$\text{SwiGLU}(x) = (x W_1) \otimes \text{Swish}(x W_2)$$
Yeh gating mechanism model ko expressive power deta hai.

Sath hi, optimizer dunya mein **AdamW** standard hai. Classic Adam mein L2 regularization ghalat tareeqe se gradient ke sath mix ho jati thi; AdamW weight decay ko decoupled rakhta hai jis se generalization bohot behtar hoti hai.',
  'Explore modern neural network components: vanishing gradients, GELU vs SwiGLU gating mechanisms, and decoupled weight decay in AdamW.',
  'import torch
import torch.nn as nn
import torch.nn.functional as F

class SwiGLU(nn.Module):
    def __init__(self, in_features: int, hidden_dim: int):
        super().__init__()
        self.w_gate = nn.Linear(in_features, hidden_dim, bias=False)
        self.w_up = nn.Linear(in_features, hidden_dim, bias=False)
        self.w_down = nn.Linear(hidden_dim, in_features, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Swish(x * W_gate) * (x * W_up)
        return self.w_down(F.silu(self.w_gate(x)) * self.w_up(x))

layer = SwiGLU(in_features=128, hidden_dim=256)
x = torch.randn(4, 128)
output = layer(x)
print("SwiGLU Layer Output Shape:", output.shape)',
  '@preset midnight
@animate pulse
arch LR: SwiGLU Gating Mechanism
  input_x[Input Activation Vector x] $terminal -> gate[Linear Gate W_gate] $layers
  input_x -> up[Linear Up W_up] $layers
  gate -> silu[SiLU / Swish Activation] $brain
  silu -> elem_mul[Elementwise Gated Multiply] $cube *
  up -> elem_mul
  elem_mul -> down[Linear Down Projection W_down] $server',
  'arch',
  '[{"title": "GLU Variants Paper (Noam Shazeer)", "url": "https://arxiv.org/abs/2002.05202"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '4.4',
  'training-loop-amp-checkpointing',
  'Production Training Loops: Mixed Precision (AMP) & Checkpointing',
  40,
  'theory_and_code',
  'So guys, agar aap standard 32-bit float (FP32) par training chalayein to GPU VRAM bohot jaldi full ho jati hai aur training slow hoti hai. Modern GPUs (Nvidia Tensor Cores) FP16 aur BF16 (Bfloat16) ko 3x se 5x tezi se execute karte hain!

Lekin FP16 mein chotay gradients underflow (0.0000...) ho jate hain.
Iska solution hai **Automatic Mixed Precision (AMP) aur `GradScaler`**:
1. Forward pass ko automatically FP16/BF16 mein cast karo (Memory 50% bachayein).
2. Loss ko calculate karke ek scale factor se multiply karo taake gradients underflow na hon.
3. Gradients unscale karke master FP32 weights ko update karo.
4. Sath hi `torch.nn.utils.clip_grad_norm_` se exploding gradients ko rokain!',
  'Master production training performance with PyTorch Automatic Mixed Precision (AMP), GradScaler, gradient clipping, and state dict checkpointing.',
  'import torch
import torch.nn as nn

device = "cuda" if torch.cuda.is_available() else "cpu"
model = nn.Sequential(nn.Linear(512, 1024), nn.GELU(), nn.Linear(1024, 10)).to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
scaler = torch.cuda.amp.GradScaler(enabled=(device == "cuda"))

# Simulated AMP Training Step
inputs = torch.randn(64, 512, device=device)
targets = torch.randint(0, 10, (64,), device=device)
criterion = nn.CrossEntropyLoss()

optimizer.zero_grad()
# Autocast runs forward pass in FP16/BF16
with torch.cuda.amp.autocast(enabled=(device == "cuda")):
    outputs = model(inputs)
    loss = criterion(outputs, targets)

# Scaler handles backprop without underflow
scaler.scale(loss).backward()
scaler.unscale_(optimizer)
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0) # Prevent exploding grads
scaler.step(optimizer)
scaler.update()

print("AMP Training Step Completed! VRAM footprint minimized.")',
  '@preset midnight
@animate flow
flow LR: Automatic Mixed Precision (AMP) Flow
  fp32[Master FP32 Weights] $database -> cast[Autocast to FP16 / BF16] $layers
  cast -> forward[Forward Pass & Loss] $brain
  forward -> scaler[GradScaler Loss Scaling] $chart
  scaler -> backward[Backward Pass (No Underflow)] $cpu *
  backward -> update[Unscale & Optimizer Step] $server',
  'flow',
  '[{"title": "PyTorch AMP Documentation", "url": "https://pytorch.org/docs/stable/amp.html"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '4.5',
  'normalization-regularization-schedulers',
  'Modern Regularization: LayerNorm, RMSNorm & Cosine Schedulers',
  35,
  'theory_and_code',
  'So guys, jab neural networks bohot deep ho jate hain (50 ya 100 layers), to unke activations ki scale har layer ke baad fluctuate karti hai (Internal Covariate Shift).

Is problem ko solve karne ke liye hum **Normalization** use karte hain:
- **LayerNorm**: Har sample ke features ka mean zero aur variance one karta hai: $\frac{x - \mu}{\sigma} \gamma + \beta$.
- **RMSNorm**: Modern LLMs (LLaMA, Mistral) mein mean subtraction skip kar di jati hai, sirf root-mean-square se normalize kiya jata hai ($40\%$ faster GPU execution!).

Sath hi, model ko start mein high learning rate dena training destabilize kar sakta hai. Is liye hum **Warmup + Cosine Annealing Learning Rate Scheduler** lagate hain jo pehle smooth start karta hai aur baad mein learning rate ko zero ki taraf decay karta hai.',
  'Understand feature normalization evolution (BatchNorm to LayerNorm to RMSNorm) and learning rate scheduling with cosine decay and warmup.',
  'import torch
import torch.nn as nn

class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # RMS = sqrt(mean(x^2))
        rms = torch.sqrt(torch.mean(x ** 2, dim=-1, keepdim=True) + self.eps)
        return (x / rms) * self.weight

# Verify RMSNorm on batch of vectors
norm = RMSNorm(dim=64)
sample = torch.randn(2, 10, 64) * 5.0 # High variance activations
normalized = norm(sample)
print("Input std:", sample.std().item())
print("RMSNorm output std:", normalized.std().item())',
  '@preset midnight
@animate flow
flow LR: RMSNorm & Learning Rate Schedule
  in_acts[Hidden Activations] $layers -> rmsnorm[RMSNorm (No Mean Centering)] $cpu
  rmsnorm -> residual[Residual Connection] $cube
  scheduler[Cosine Annealing LR Warmup] $terminal -> opt_step[Optimizer Step] $brain *',
  'flow',
  '[{"title": "RMSNorm Paper", "url": "https://arxiv.org/abs/1910.07467"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '4.6',
  'module-4-capstone-neural-engine',
  'Module 4 Capstone: Custom Neural Engine from Raw Tensors',
  55,
  'project',
  'So guys, congratulations! Aapne Deep Learning ke tamam mathematical aur implementation foundations samajh liye hain. Ab waqt hai **Ultimate First-Principles Test** ka!

Is capstone mein aap Andrej Karpathy ke micrograd jaisa ek **Custom Autograd Engine** implement karenge using raw Python scalar/tensor nodes:
1. Ek `Value` class banayein jo scalar numbers hold kare aur computation graph trace kare.
2. `__add__` aur `__mul__` ke local derivatives register karein.
3. Topological Sort algorithm se reverse execution graph order nikaalein.
4. Ek 2-layer Neural Net train karke non-linear decision boundary par loss zero karein!',
  'Construct a complete reverse-mode automatic differentiation engine from scratch and train a neural network without any PyTorch autograd magic.',
  '# Module 4 Capstone: Custom Micrograd-style Autodiff Node
class Value:
    def __init__(self, data, _children=()):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(_children)

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other))
        def _backward():
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad
        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other))
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)
        self.grad = 1.0
        for node in reversed(topo):
            node._backward()

a = Value(3.0)
b = Value(-2.0)
c = a * b + Value(10.0)
c.backward()
print(f"Computed c: {c.data} | dc/da gradient: {a.grad} (Expected -2.0) | dc/db: {b.grad} (Expected 3.0)")',
  '@preset midnight
@animate flow
flow LR: Custom Autograd Engine Graph
  node_a[Leaf Node A (Weight)] $code -> mul[Multiply Op] $cpu
  node_b[Leaf Node B (Input)] $code -> mul
  mul -> add[Add Op (Bias)] $layers
  add -> loss[Loss Value] $brain
  loss -> topo_back[Reverse Topological Backward Pass] $terminal *',
  'flow',
  '[{"title": "Andrej Karpathy micrograd repo", "url": "https://github.com/karpathy/micrograd"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '5.1',
  'self-attention-math',
  'Self-Attention Mechanism: Q, K, V Matrices Ka Khel',
  40,
  'theory_and_code',
  'So guys, modern AI ki tareekh ka sab se bara milestone 2017 ka paper tha: *"Attention Is All You Need"*. Isne RNNs aur LSTMs ko hamesha ke liye khatam kar diya!

RNNs sequential thay — word by word process karte thay, jis ki wajah se GPU parallelization na-mumkin thi.
Transformer ka dil hai **Scaled Dot-Product Attention**:
$$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$$

Is formula ko aasan zubaan mein samjhein:
1. **Query ($Q$)**: "Main kya dhoond raha hoon?" (Maslan word "bank" pooche ga: "kya main river bank hoon ya financial bank?")
2. **Key ($K$)**: "Mere pas kya information hai?" Har token apni pehchan announce karta hai.
3. **Value ($V$)**: Asal semantic content jo doosre tokens ko pass hona hai.
4. **$\sqrt{d_k}$ se divide kyun karte hain?**: Jab dimension $d_k$ bara hota hai to dot product bohot bara ho jata hai, jis se Softmax ke gradients vanish ho jate hain. Scale karne se variance 1 rehti hai!',
  'Master the mathematical formulation of Scaled Dot-Product Attention: Query, Key, Value projections, dot products, scaling factor, and softmax weights.',
  'import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor, mask: torch.Tensor = None):
    d_k = Q.size(-1)
    # 1. MatMul Q and K^T -> (Batch, Heads, Seq_Q, Seq_K)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    
    # 2. Apply Causal Mask if provided (to prevent looking at future tokens)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float(''-inf''))
        
    # 3. Softmax along last dimension -> Attention Weights
    attn_weights = F.softmax(scores, dim=-1)
    
    # 4. Multiply with Value matrix V
    output = torch.matmul(attn_weights, V)
    return output, attn_weights

# Demonstration: Sequence of 3 tokens, Embedding Dim 4
Q = torch.randn(1, 1, 3, 4)
K = torch.randn(1, 1, 3, 4)
V = torch.randn(1, 1, 3, 4)

out, weights = scaled_dot_product_attention(Q, K, V)
print("Attention Output Shape:", out.shape)
print("Attention Weights Matrix:\n", weights[0, 0].detach().numpy().round(3))',
  '@preset midnight
@animate flow
flow LR: Scaled Dot-Product Attention
  q[Query Matrix Q] $terminal -> matmul[MatMul Q * K^T] $cpu
  k[Key Matrix K] $terminal -> matmul
  matmul -> scale[Scale 1 / sqrt(d_k)] $layers
  scale -> softmax[Softmax Normalization] $brain
  softmax -> v_mul[MatMul with Value V] $cube *
  v[Value Matrix V] $terminal -> v_mul',
  'flow',
  '[{"title": "Vaswani et al. (Attention Is All You Need)", "url": "https://arxiv.org/abs/1706.03762"}]'::jsonb,
  30,
  1
from public.modules m
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '5.2',
  'multihead-attention-blocks',
  'Multi-Head Attention & Transformer Block Architecture',
  40,
  'theory_and_code',
  'So guys, single attention head sirf ek qism ka relationship capture kar sakta hai (maslan verb aur subject ka connection). Lekin real language mein hazaron patterns hote hain: rhyming, sentiment, factual references, etc.

Is liye hum embedding ko multiple heads (jaise 8, 16, ya 32 heads) mein split karte hain. Har head alag latent subspace mein attend karta hai.
Phir sabhi heads ke outputs ko concatenate karke ek projection layer se pass kiya jata hai.

Iske sath hi Transformer Block mein do cheezein hoti hain:
1. **Residual Connections (Skip Connections)**: Gradient vanishing se bachne ke liye input ko direct output mein add kiya jata hai: $x + \text{Sublayer}(x)$.
2. **RMSNorm / LayerNorm**: Activations ki scale ko stable rakhne ke liye.',
  'Construct complete Transformer blocks combining multi-head attention projections, residual additions, RMSNorm, and Feed-Forward Networks.',
  'import torch
import torch.nn as nn

class TransformerBlock(nn.Module):
    def __init__(self, embed_dim: int, num_heads: int, mlp_dim: int):
        super().__init__()
        self.norm1 = nn.LayerNorm(embed_dim)
        self.attn = nn.MultiheadAttention(embed_dim, num_heads, batch_first=True)
        self.norm2 = nn.LayerNorm(embed_dim)
        self.mlp = nn.Sequential(
            nn.Linear(embed_dim, mlp_dim),
            nn.GELU(),
            nn.Linear(mlp_dim, embed_dim)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        norm_x = self.norm1(x)
        attn_out, _ = self.attn(norm_x, norm_x, norm_x)
        x = x + attn_out
        x = x + self.mlp(self.norm2(x))
        return x

block = TransformerBlock(embed_dim=64, num_heads=4, mlp_dim=256)
tokens = torch.randn(2, 10, 64)
out = block(tokens)
print("Transformer Block Output Shape:", out.shape)',
  '@preset midnight
@animate pulse
arch LR: Full Transformer Block Pipeline
  in_tok[Input Token Embeddings] $terminal -> norm1[LayerNorm 1] $cpu
  norm1 -> mha[Multi-Head Attention] $brain
  mha -> add1[Residual Add] $layers
  in_tok -> add1
  add1 -> norm2[LayerNorm 2] $cpu
  norm2 -> ffn[Feed-Forward Network (GELU)] $cube
  ffn -> add2[Residual Add] $layers *
  add1 -> add2',
  'arch',
  '[{"title": "Transformers Architecture Deep Dive", "url": "https://huggingface.co/docs/transformers/index"}]'::jsonb,
  30,
  2
from public.modules m
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '5.3',
  'tokenization-bpe-tiktoken',
  'Tokenization Deep Dive: Byte-Pair Encoding (BPE) & Tiktoken',
  35,
  'theory_and_code',
  'So guys, agar aap text ko character-by-character feed karein to sequence length 10x barh jati hai (O(N^2) attention collapse). Agar word-by-word karein to vocabulary mein lakhoon words chahiye hotay hain aur out-of-vocabulary (OOV) words fail ho jate hain.

Iska universal solution hai **Byte-Pair Encoding (BPE)**:
Shuru mein har character ek token hota hai. Phir training dataset mein jo do tokens sab se zyada ek sath aate hain (highest frequency pair), unko merge karke ek naya single token bana diya jata hai.
Maslan: ''u'' + ''r'' -> ''ur'', ''ur'' + ''du'' -> ''urdu''.

OpenAI ka `tiktoken` Rust mein implement kiya gaya hai aur per second 1 million tokens tokenize kar sakta hai!',
  'Understand subword tokenization mechanics, the Byte-Pair Encoding (BPE) iterative merge algorithm, vocabulary construction, and tiktoken.',
  'from collections import Counter

# Mini BPE Algorithm Demonstration
corpus = ["low", "lower", "newest", "widest"]

def get_stats(vocab):
    pairs = Counter()
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[symbols[i], symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, v_in):
    v_out = {}
    bigram = '' ''.join(pair)
    replacement = ''''.join(pair)
    for word in v_in:
        w_out = word.replace(bigram, replacement)
        v_out[w_out] = v_in[word]
    return v_out

vocab = {''l o w </w>'': 5, ''l o w e r </w>'': 2, ''n e w e s t </w>'': 6, ''w i d e s t </w>'': 3}
for i in range(5):
    pairs = get_stats(vocab)
    if not pairs: break
    best_pair = pairs.most_common(1)[0][0]
    vocab = merge_vocab(best_pair, vocab)
    print(f"BPE Merge Step {i+1}: Best Pair {best_pair}")',
  '@preset midnight
@animate flow
flow LR: Byte-Pair Encoding (BPE) Pipeline
  raw_text[Raw Text Stream] $terminal -> utf8_bytes[UTF-8 Byte Split] $code
  utf8_bytes -> pair_count[Pair Frequency Counter] $cpu
  pair_count -> merge_table[Iterative Merge Rules] $database
  merge_table -> token_ids[Compressed Token IDs] $brain *',
  'flow',
  '[{"title": "OpenAI Tiktoken Repo", "url": "https://github.com/openai/tiktoken"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '5.4',
  'rotary-embeddings-rope-pos',
  'Rotary Position Embeddings (RoPE) & Context Length Scaling',
  35,
  'theory_and_code',
  'So guys, Self-Attention inherently permutation-invariant hoti hai — yaani agar aap sentence ke words ko aage peeche kar dein to dot product ka answer same rehta hai! Is liye model ko position batana lazmi hota hai.

Vaswani 2017 ne Sinusoidal positional encodings use kiye jo absolute positions thay. Lekin absolute position se model kabhi bhi train-length se lambe documents extrapolate nahi kar pata tha.

Modern LLMs (Llama 3, DeepSeek, Mistral) **RoPE (Rotary Position Embedding)** use karte hain:
Query aur Key vectors ko 2D complex plane mein rotation angle se multiply kiya jata hai: $R_{\theta, m} q$.
Iska jadoo yeh hai ke dot product lene par absolute positions cancel ho jati hain aur sirf **Relative Distance ($m - n$)** bachta hai:
$$\langle R_m q, R_n k \rangle = g(q, k, m - n)$$
Isi mathematical beauty ki wajah se context window 4k se 128k tokens tak scale hoti hai!',
  'Understand why self-attention requires positional encodings and how Rotary Position Embeddings (RoPE) rotate Q and K in complex 2D planes.',
  'import torch

def apply_rotary_pos_emb(x: torch.Tensor, seq_len: int):
    # Dim must be even for 2D complex pairs
    dim = x.size(-1)
    inv_freq = 1.0 / (10000 ** (torch.arange(0, dim, 2).float() / dim))
    t = torch.arange(seq_len, dtype=torch.float32)
    freqs = torch.outer(t, inv_freq)
    
    # cos and sin embeddings
    cos = freqs.cos().repeat_interleave(2, dim=-1)
    sin = freqs.sin().repeat_interleave(2, dim=-1)
    
    # Rotate 2D pairs: [-x2, x1, -x4, x3, ...]
    x_rotated = torch.stack([-x[..., 1::2], x[..., 0::2]], dim=-1).flatten(-2)
    return (x * cos) + (x_rotated * sin)

q = torch.randn(1, 4, 16) # Batch 1, Seq 4, Dim 16
q_rope = apply_rotary_pos_emb(q, seq_len=4)
print("RoPE Successfully Applied. Output Shape:", q_rope.shape)',
  '@preset midnight
@animate pulse
arch LR: Rotary Position Embedding (RoPE)
  query_vec[Query Vector Q] $layers -> rotate_q[2D Complex Rotation Matrix R_m] $brain
  key_vec[Key Vector K] $layers -> rotate_k[2D Complex Rotation Matrix R_n] $brain
  rotate_q -> dot_prod[Dot Product (Preserves Relative m-n)] $cube *
  rotate_k -> dot_prod',
  'arch',
  '[{"title": "RoFormer: Enhanced Transformer with Rotary Position Embedding", "url": "https://arxiv.org/abs/2104.09864"}]'::jsonb,
  30,
  4
from public.modules m
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '5.5',
  'encoder-decoder-paradigms',
  'Architectural Paradigms: BERT vs GPT vs T5',
  35,
  'theory_and_code',
  'So guys, Transformers ki dunya mein teen mukhtalif architectural families aayi hain:
1. **Encoder-Only (BERT)**: Ismein koi mask nahi hota, har token aage aur peeche tamam tokens ko dekh sakta hai (Bidirectional). Best for Classification aur Embedding generation.
2. **Decoder-Only (GPT, Llama, DeepSeek)**: Ismein **Causal Lower-Triangular Mask** hota hai. Token sirf pichle tokens dekh sakta hai, mustaqbil ke tokens nahi dekh sakta. Best for Autoregressive Generation.
3. **Encoder-Decoder (T5, BART)**: Ismein do blocks hote hain jo Cross-Attention se connect hote hain. Best for Translation aur Summarization.

2026 mein dunya **Decoder-Only** par kyun mutafiq ho gayi?
Kyunke Decoder-Only models simple hote hain, KV Cache implement karna aasan hota hai, aur scaling laws (Compute vs Loss) sab se predictable follow karte hain!',
  'Compare the 3 major transformer paradigms: Encoder-Only (BERT), Decoder-Only (GPT), and Encoder-Decoder (T5), and understand why Decoder-Only won.',
  'import torch

# Demonstrate Causal Mask vs Bidirectional Mask
seq_len = 4
causal_mask = torch.tril(torch.ones(seq_len, seq_len))
print("Causal Mask (Decoder-Only GPT): Token can only see past tokens:")
print(causal_mask.numpy())

bidirectional_mask = torch.ones(seq_len, seq_len)
print("\nBidirectional Mask (Encoder-Only BERT): Token sees all tokens:")
print(bidirectional_mask.numpy())',
  '@preset midnight
@animate flow
flow LR: Transformer Architectural Taxonomy
  bert[Encoder-Only (BERT): Bidirectional] $brain -> tasks1[Classification & Embeddings] $layers
  gpt[Decoder-Only (GPT/Llama): Causal Mask] $server -> tasks2[Autoregressive Text Generation] $terminal *
  t5[Encoder-Decoder (T5): Cross-Attention] $cube -> tasks3[Seq2Seq Translation & Summary] $database',
  'flow',
  '[{"title": "Illustrated GPT-2", "url": "https://jalammar.github.io/illustrated-gpt2/"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '5.6',
  'module-5-capstone-minigpt',
  'Module 5 Capstone: Build a Complete Mini-GPT from Scratch in PyTorch',
  60,
  'project',
  'So guys, this is IT! Module 5 ka Grand Capstone: **Ek Mukammal Decoder-Only Mini-GPT Model from Scratch in PyTorch**!

Aap tamam seekhi hui cheezon ko ek single executable script mein integrate karenge:
1. Token Embedding Layer + Positional Embedding Layer.
2. N Multi-Head Causal Self-Attention Blocks with Residual Connections & LayerNorm.
3. Final Projection LM Head jo vocabulary logits return kare.
4. An Autoregressive `generate()` loop jo greedy sampling se text continue kare!

Yeh script run karte hi aap official taur par Transformer Engineer ban jayenge!',
  'Construct and train a complete, runnable Mini-GPT causal autoregressive language model in pure PyTorch and generate text from a prompt.',
  'import torch
import torch.nn as nn
import torch.nn.functional as F

class MiniGPT(nn.Module):
    def __init__(self, vocab_size=1000, embed_dim=64, num_heads=4, num_layers=2, max_len=64):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab_size, embed_dim)
        self.pos_emb = nn.Embedding(max_len, embed_dim)
        
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim, nhead=num_heads, dim_feedforward=embed_dim*4, 
            batch_first=True, activation="gelu"
        )
        self.blocks = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.ln_f = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, vocab_size, bias=False)
        self.max_len = max_len

    def forward(self, idx):
        B, T = idx.shape
        pos = torch.arange(0, T, device=idx.device)
        x = self.tok_emb(idx) + self.pos_emb(pos)
        
        # Causal mask for autoregressive generation
        mask = nn.Transformer.generate_square_subsequent_mask(T, device=idx.device)
        x = self.blocks(x, mask=mask, is_causal=True)
        logits = self.head(self.ln_f(x))
        return logits

    @torch.no_grad()
    def generate(self, idx, max_new_tokens=10):
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -self.max_len:]
            logits = self(idx_cond)
            next_token = torch.argmax(logits[:, -1, :], dim=-1, keepdim=True)
            idx = torch.cat((idx, next_token), dim=1)
        return idx

model = MiniGPT(vocab_size=200, embed_dim=32, num_heads=2, num_layers=2)
prompt = torch.tensor([[10, 24, 55]]) # 3 input tokens
generated = model.generate(prompt, max_new_tokens=5)
print("Mini-GPT Generated Token IDs:", generated.tolist())',
  '@preset midnight
@animate flow
flow LR: Complete Mini-GPT Architecture
  in_indices[Token Indices (B, T)] $terminal -> tok_emb[Token + Pos Embeddings] $layers
  tok_emb -> tf_blocks[N x Causal Transformer Blocks] $brain
  tf_blocks -> ln_f[Final LayerNorm] $cpu
  ln_f -> lm_head[Linear LM Head (Vocab Size)] $server
  lm_head -> logits[Next Token Logits & Sampling] $cube *',
  'flow',
  '[{"title": "NanoGPT by Andrej Karpathy", "url": "https://github.com/karpathy/nanoGPT"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '6.1',
  'streaming-llm-apis',
  'Streaming LLM APIs: Server-Sent Events (SSE) & Async Iterators',
  30,
  'theory_and_code',
  'So guys, jab user LLM se 500 words ka response mangta hai, to agar aap poora response complete hone tak intezar karein to user ko 5 se 10 seconds tak blank screen dekhni paregi! Yeh terrible User Experience (UX) hai.

Iska industry standard solution **Server-Sent Events (SSE)** hai (`Content-Type: text/event-stream`). Server HTTP connection open rakhta hai aur jaise hi LLM ek naya token generate karta hai, server use foran client ko push kar deta hai:
`data: {"token": "Pakistan"}\n\n`

Client-side par JavaScript ka `ReadableStream` aur `TextDecoder` har token ko instant UI mein append karte hain.',
  'Architect low-latency streaming endpoints utilizing HTTP/2 Server-Sent Events (SSE) and asynchronous token iterators.',
  'import asyncio
from typing import AsyncGenerator
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

async def mock_token_generator(prompt: str) -> AsyncGenerator[str, None]:
    words = f"Salam! Aapne poocha: ''{prompt}''. Hum real-time token streaming seekh rahe hain!".split()
    for word in words:
        await asyncio.sleep(0.08)
        yield f"data: {word} \n\n"
    yield "data: [DONE]\n\n"

@app.get("/api/chat/stream")
async def chat_stream(prompt: str):
    return StreamingResponse(
        mock_token_generator(prompt),
        media_type="text/event-stream"
    )',
  '@preset midnight
seq: Real-Time SSE Token Streaming
  client[Svelte 5 Client] -> server[FastAPI / Axum Gateway]: GET /api/chat/stream
  server -> llm[LLM Provider]: Stream Completion
  llm -> server: Token: ''Salam''
  server -> client: data: ''Salam''
  llm -> server: Token: ''Pakistan''
  server -> client: data: ''Pakistan'' *
  server -> client: data: [DONE]',
  'seq',
  '[{"title": "MDN Server-Sent Events", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events"}]'::jsonb,
  20,
  1
from public.modules m
where m.slug = 'building-ai-applications-and-apis'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '6.2',
  'fullstack-ai-architecture',
  'Full-Stack AI Architecture: State & Token Management',
  35,
  'theory_and_code',
  'So guys, ek professional AI frontend mein teen cheezein lazmi honi chahiye:
1. **AbortController**: Agar user response ke beech mein ''Stop Generating'' dabaye to foran HTTP stream abort ho jaye taake token waste na hon.
2. **Optimistic Updates**: User ka message foran screen par show ho bina network latency ka wait kiye.
3. **Token Accounting**: Har message ke input tokens aur output tokens count karke database mein log karna taake billing aur rate limits track ho sakein.',
  'Manage client-side chat state, optimistic UI rendering, AbortController request cancellation, and database token accounting.',
  '// Svelte 5 / TypeScript Stream Reader with AbortController
let abortController = null;

async function sendMessage(promptText) {
    if (abortController) abortController.abort();
    abortController = new AbortController();

    try {
        const response = await fetch(`/api/chat/stream?prompt=${encodeURIComponent(promptText)}`, {
            signal: abortController.signal
        });
        
        const reader = response.body?.getReader();
        const decoder = new TextDecoder();
        
        while (reader) {
            const { value, done } = await reader.read();
            if (done) break;
            const chunk = decoder.decode(value);
            console.log("Stream Chunk:", chunk);
        }
    } catch (err) {
        if (err.name === ''AbortError'') console.log(''Generation aborted by user.'');
    }
}',
  '@preset midnight
@animate flow
flow LR: Abortable Stream Lifecycle
  user[User Clicks Stop] $browser -> abort[AbortController.abort()] $terminal
  abort -> stream[ReadableStream Closed] $code
  stream -> server[Server Halts LLM Inference] $server *',
  'flow',
  '[{"title": "Web Fetch API Streams", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Streams_API"}]'::jsonb,
  25,
  2
from public.modules m
where m.slug = 'building-ai-applications-and-apis'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '6.3',
  'fastapi-async-worker-queues',
  'Production Async AI Gateways with FastAPI & Redis Task Queues',
  35,
  'theory_and_code',
  'So guys, jab aapke AI platform par 500 users aik sath heavy requests bhejte hain (jaise document extraction ya image embedding), to seedha FastAPI worker par run karne se poora server block ho jata hai!

Iska production pattern hai **Async Background Worker Queue (Celery / ARQ + Redis)**:
1. FastAPI request receive karta hai, ek unique `job_id` generate karta hai, aur foran `202 Accepted` return kar deta hai (sub-10ms response).
2. Background Redis Queue mein job enqueue hoti hai.
3. Dedicated GPU/CPU worker process job utha kar execute karta hai aur status database mein update karta hai.
4. Client polling ya WebSocket ke zariye progress bar update karta hai.',
  'Decouple synchronous HTTP request handlers from long-running AI compute tasks using FastAPI, Redis queues, and background worker pools.',
  'import asyncio
import uuid
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()
job_store = {}

def heavy_ai_document_processing(job_id: str, document_text: str):
    job_store[job_id] = {"status": "processing", "progress": 0.2}
    import time; time.sleep(1)
    job_store[job_id] = {"status": "completed", "chunks": 42, "embedding_dim": 1536}

@app.post("/api/documents/ingest")
async def ingest_document(doc_text: str, bg_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    job_store[job_id] = {"status": "queued"}
    bg_tasks.add_task(heavy_ai_document_processing, job_id, doc_text)
    return {"job_id": job_id, "status": "queued"}

@app.get("/api/documents/status/{job_id}")
async def get_status(job_id: str):
    return job_store.get(job_id, {"status": "not_found"})',
  '@preset midnight
@animate flow
flow LR: Async Worker Queue Architecture
  client[Client HTTP Ingest] $browser -> api[FastAPI Gateway] $server
  api -> queue[Redis Job Queue] $database
  api -> client: 202 Accepted {job_id} *
  queue -> worker[Background AI Worker Process] $cpu
  worker -> db[PostgreSQL Result Cache] $database',
  'flow',
  '[{"title": "FastAPI Background Tasks", "url": "https://fastapi.tiangolo.com/tutorial/background-tasks/"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'building-ai-applications-and-apis'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '6.4',
  'semantic-caching-redis-gptcache',
  'Semantic Caching with Redis & Vector Similarity for 80% Cost Reduction',
  40,
  'theory_and_code',
  'So guys, agar ek user pooche *"Pakistan ka capital kya hai?"* aur 5 minute baad doosra user pooche *"What is the capital city of Pakistan?"*, to traditional exact-match caching (jaise standard Redis key-value) fail ho jayegi kyunke strings mukhtalif hain!

Dono dafa LLM API ko call karne se aapke paise aur latency waste honge.
Iska solution hai **Semantic Caching (GPTCache / Redis Vector Search)**:
1. Incoming prompt ka vector embedding banayein.
2. Redis vector index mein search karein: agar pichle kisi query se Cosine Similarity > 0.95 hai, to LLM ko call kiye baghair pichla answer return kar dein!
3. Is se enterprise AI bills **70% se 80% reduce** ho jate hain aur response time 1.5s se gir kar **15 milliseconds** par aa jata hai!',
  'Implement semantic vector caching using Redis and embedding similarity thresholds to serve repetitive LLM queries in under 20ms.',
  'import numpy as np

class InMemorySemanticCache:
    def __init__(self, similarity_threshold: float = 0.92):
        self.threshold = similarity_threshold
        self.entries = []

    def get(self, query_emb: np.ndarray):
        for emb, answer in self.entries:
            sim = np.dot(query_emb, emb) / (np.linalg.norm(query_emb) * np.linalg.norm(emb))
            if sim >= self.threshold:
                return answer, sim
        return None, 0.0

    def set(self, query_emb: np.ndarray, answer: str):
        self.entries.append((query_emb, answer))

cache = InMemorySemanticCache(similarity_threshold=0.90)
q1_emb = np.array([0.95, 0.10, -0.05])
cache.set(q1_emb, "Islamabad is the capital city of Pakistan.")

q2_emb = np.array([0.93, 0.12, -0.04])
cached_ans, sim = cache.get(q2_emb)

if cached_ans:
    print(f"CACHE HIT! Similarity: {sim:.3f}")
    print(f"Answer: {cached_ans} (Saved 100% LLM token cost!)")',
  '@preset midnight
@animate pulse
arch LR: Semantic Caching Flow
  prompt[User Query Prompt] $terminal -> emb[Embedding Model (bge-small)] $brain
  emb -> cache_lookup[Redis Vector Index Search] $database
  cache_lookup -> hit{Similarity >= 0.95?} $code
  hit -- YES --> fast_out[Instant Cache Return (15ms)] $server *
  hit -- NO --> llm_call[Call Frontier LLM ($$$)] $cloud',
  'arch',
  '[{"title": "GPTCache Architecture", "url": "https://github.com/zilliztech/GPTCache"}]'::jsonb,
  30,
  4
from public.modules m
where m.slug = 'building-ai-applications-and-apis'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '6.5',
  'websockets-realtime-ai-streams',
  'Real-Time Bidirectional AI Streams with WebSockets',
  35,
  'theory_and_code',
  'So guys, Server-Sent Events (SSE) sirf unidirectional hote hain (Server se Client). Lekin modern agentic applications (jaise voice bots, real-time typing corrections, interactive AI canvas) mein **Bidirectional Communication** chahiye hoti hai jahan client aur server aapas mein continuous messages exchange kar sakein.

Yahan kaam aata hai **WebSockets (`ws://` aur `wss://`)**:
Ek single TCP connection establish hota hai jo full-duplex communication provide karta hai. Client user ka keystroke ya audio chunk bhejta rehta hai, aur server simultaneously tokens aur UI widget states push karta rehta hai.
Is lesson mein hum FastAPI WebSockets aur heartbeat ping/pong connection resilience ko master karenge.',
  'Build full-duplex, low-latency bidirectional AI applications using WebSockets, structured event framing, and heartbeat keep-alives.',
  'from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio

app = FastAPI()

@app.websocket("/ws/agent")
async def websocket_ai_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_json({"type": "status", "msg": "Agent thinking..."})
            await asyncio.sleep(0.1)
            for tok in ["Autonomous", "Agent", "Online!"]:
                await websocket.send_json({"type": "token", "content": tok})
                await asyncio.sleep(0.05)
            await websocket.send_json({"type": "done"})
    except WebSocketDisconnect:
        print("Client gracefully disconnected.")',
  '@preset midnight
seq: Bidirectional WebSocket AI Flow
  client[Web Browser / React Client] -> server[FastAPI WebSocket]: WS Handshake (101 Switching Protocols)
  client -> server: {"action": "user_input", "text": "Plan my flight"}
  server -> client: {"type": "status", "state": "Invoking Booking Tool"}
  server -> client: {"type": "token", "val": "Found 3 flights..."} *
  client -> server: {"action": "confirm", "flight_id": "PK301"}',
  'seq',
  '[{"title": "FastAPI WebSockets Guide", "url": "https://fastapi.tiangolo.com/advanced/websockets/"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'building-ai-applications-and-apis'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '6.6',
  'module-6-capstone-ai-gateway',
  'Module 6 Capstone: Enterprise Resilient Streaming AI Gateway Service',
  55,
  'project',
  'So guys, Module 6 ke Grand Capstone mein aap ek **Production-Grade Resilient AI Gateway** banayenge jo enterprise applications ko serve karega!

Real world mein agar Groq down ho jaye to aapki company ka customer support bot band nahi hona chahiye. Aapka gateway:
1. Multi-provider fallback cascade implement karega (Groq -> Cerebras -> Gemini Flash).
2. Semantic Cache layer check karega (Redis vector similarity).
3. Token-Bucket Rate Limiter lagaye ga taake koi spammer API budget burn na kare.
4. Server-Sent Events (SSE) ke through sub-100ms streaming ensure karega!',
  'Ship a production-grade AI gateway service featuring multi-provider failover cascades, semantic caching, token-bucket rate limiting, and SSE streaming.',
  'import asyncio
from typing import AsyncGenerator

async def provider_groq(prompt: str):
    for t in ["Groq", "Ultra-Fast", "Stream", "Output"]:
        yield t
        await asyncio.sleep(0.02)

async def provider_fallback(prompt: str):
    for t in ["Fallback", "Gemini", "Backup", "Stream"]:
        yield t
        await asyncio.sleep(0.05)

async def resilient_gateway_stream(prompt: str) -> AsyncGenerator[str, None]:
    try:
        async for token in provider_groq(prompt):
            yield token
    except Exception as e:
        print(f"Primary provider failed: {e}. Switching to fallback cascade!")
        async for token in provider_fallback(prompt):
            yield token

async def test_gateway():
    print("Testing Enterprise Gateway Streaming:")
    async for tok in resilient_gateway_stream("Hello AI Ustaad"):
        print(f"Token: {tok}")

asyncio.run(test_gateway())',
  '@preset midnight
@animate flow
flow LR: Resilient AI Gateway Cascade
  req[User Streaming Request] $terminal -> rate[Token-Bucket Rate Limiter] $code
  rate -> cache[Redis Semantic Cache] $database
  cache -> primary[Primary Provider (Groq 400 tok/s)] $server
  primary -. Circuit Breaker Failure .-> fallback[Fallback Provider (Gemini / Cerebras)] $cloud *
  primary -> sse_out[SSE Client Stream] $browser
  fallback -> sse_out',
  'flow',
  '[{"title": "OpenAI Compatible Gateways", "url": "https://github.com/BerriAI/litellm"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'building-ai-applications-and-apis'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '7.1',
  'embeddings-vector-indexes',
  'Vector Embeddings & Indexing: HNSW, IVFFlat & pgvector',
  35,
  'theory_and_code',
  'So guys, agar aapke database mein 1 million documents ke embeddings hain, to har query par 1 million dot products calculate karna ($O(N)$ brute-force) bohot slow ho jayega.

Isliye hum **Approximate Nearest Neighbor (ANN)** indexing use karte hain:
1. **IVFFlat (Inverted File Flat)**: Space ko Voronoi cells mein divide karta hai. Query aane par sirf sab se qareebi cell ke points check hote hain.
2. **HNSW (Hierarchical Navigable Small World)**: Graph-based indexing hai jo skip-lists ki tarah multi-layer graph banati hai. Yeh fastest search speed ($O(\log N)$) aur 98%+ recall deti hai!

PostgreSQL mein `pgvector` extension HNSW index natively support karti hai.',
  'Understand vector embeddings geometry, ANN search indexing algorithms (IVFFlat vs HNSW), and pgvector execution.',
  '-- PostgreSQL pgvector Schema and HNSW Index Creation
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE document_embeddings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content TEXT NOT NULL,
    metadata JSONB,
    embedding vector(1536)
);

CREATE INDEX ON document_embeddings 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

SELECT id, content, 1 - (embedding <=> ''[0.12, -0.45, ...]''::vector) AS similarity
FROM document_embeddings
ORDER BY embedding <=> ''[0.12, -0.45, ...]''::vector
LIMIT 5;',
  '@preset midnight
@animate pulse
arch LR: HNSW Hierarchical Navigation
  layer2[Layer 2: Sparse Long-Jump Highway] $layers -> layer1[Layer 1: Medium-Density Clusters] $layers
  layer1 -> layer0[Layer 0: Dense Full-Vector Graph] $database *
  query[Query Vector] $terminal -> layer2',
  'arch',
  '[{"title": "Pinecone HNSW Guide", "url": "https://www.pinecone.io/learn/series/faiss/hnsw/"}]'::jsonb,
  25,
  1
from public.modules m
where m.slug = 'vector-databases-and-modern-rag'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '7.2',
  'advanced-rag-reranking',
  'Advanced RAG: Hybrid Search & Cross-Encoder Re-Ranking',
  40,
  'theory_and_code',
  'So guys, standard RAG aksar production mein fail ho jata hai kyunke:
- Dense Vector Search exact keywords (jaise part numbers, CNIC, phone numbers, exact error codes) miss kar deta hai.
- Keyword Search (BM25) semantic meaning miss kar deta hai.

Iska production solution hai **Hybrid Search with Reciprocal Rank Fusion (RRF)**:
$$\text{RRF Score}(d) = \frac{1}{60 + \text{Rank}_{\text{Dense}}(d)} + \frac{1}{60 + \text{Rank}_{\text{BM25}}(d)}$$

Uske baad hum top-20 results ko ek **Cross-Encoder Re-Ranker** (jaise Cohere Re-rank ya FlashRank) se pass karte hain jo query aur document chunk ko ikattha cross-attend karta hai aur sab se relevant top-3 chunks extract karta hai.',
  'Implement production Hybrid Search combining dense semantic embeddings with sparse BM25, fused via RRF and Cross-Encoder re-ranking.',
  'import numpy as np

def reciprocal_rank_fusion(dense_ranks: dict, sparse_ranks: dict, k: int = 60) -> dict:
    all_doc_ids = set(dense_ranks.keys()).union(sparse_ranks.keys())
    rrf_scores = {}
    for doc_id in all_doc_ids:
        r_dense = dense_ranks.get(doc_id, 1000)
        r_sparse = sparse_ranks.get(doc_id, 1000)
        score = (1.0 / (k + r_dense)) + (1.0 / (k + r_sparse))
        rrf_scores[doc_id] = score
    return dict(sorted(rrf_scores.items(), key=lambda item: item[1], reverse=True))

dense_results = {"doc_urdu_poetry": 1, "doc_pak_history": 2, "doc_tax_law": 3}
sparse_results = {"doc_tax_law": 1, "doc_urdu_poetry": 3, "doc_corporate": 2}

fused = reciprocal_rank_fusion(dense_results, sparse_results)
print("Hybrid RRF Ranked Chunks:")
for doc, score in fused.items():
    print(f"  {doc:18s}: RRF Score = {score:.4f}")',
  '@preset midnight
@animate flow
flow LR: Hybrid RAG Pipeline
  query[User Query] $terminal -> dense[Dense HNSW Search] $brain
  query -> sparse[Sparse BM25 Search] $code
  dense -> rrf[Reciprocal Rank Fusion] $layers
  sparse -> rrf
  rrf -> rerank[Cross-Encoder Reranker] $server
  rerank -> final[Top-3 Pristine Context Chunks] $cube *',
  'flow',
  '[{"title": "Cohere Rerank Documentation", "url": "https://docs.cohere.com/docs/reranking"}]'::jsonb,
  30,
  2
from public.modules m
where m.slug = 'vector-databases-and-modern-rag'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '7.3',
  'colpali-visual-rag',
  '2026 SOTA: ColPali Vision-Language Multi-Vector RAG',
  45,
  'theory_and_code',
  'So guys, traditional RAG ka sab se bara dard **PDF Parsing & OCR** hai. Jab PDF mein complex tables, charts, diagrams, ya Urdu Nastaliq font hota hai to OCR tool (Tesseract/PyPDF) kachra text generate karta hai.

2024-2026 ka sab se bara breakthrough hai **ColPali (ColBERT + PaliGemma)**!
ColPali text extraction nahi karta. Yeh PDF ke har page ka ek visual screenshot leta hai aur Vision-Language Model se har page ke liye multiple patch-level vectors generate karta hai.

Query ke waqt **Late Interaction (MaxSim)** algorithm use hota hai:
$$\text{Score}(Q, D) = \sum_{q \in Q} \max_{d \in D} (q \cdot d)$$
Query ka har word page ke exact visual table cell ya chart bar se match karta hai! Zero OCR errors!',
  'Understand ColPali multi-vector retrieval, visual document indexing directly from page images, and Late Interaction (MaxSim) operator mechanics.',
  'import torch

def late_interaction_maxsim(query_token_embeddings: torch.Tensor, doc_patch_embeddings: torch.Tensor) -> float:
    sim_matrix = torch.matmul(query_token_embeddings, doc_patch_embeddings.T)
    max_per_query = torch.max(sim_matrix, dim=-1).values
    score = torch.sum(max_per_query).item()
    return score

Q = torch.randn(4, 128)
D = torch.randn(16, 128)
Q = Q / torch.norm(Q, dim=-1, keepdim=True)
D = D / torch.norm(D, dim=-1, keepdim=True)

score = late_interaction_maxsim(Q, D)
print(f"ColPali Late Interaction MaxSim Score: {score:.3f}")',
  '@preset midnight
@animate flow
flow LR: ColPali Multi-Vector Late Interaction
  pdf_page[PDF Page Screenshot] $terminal -> vlm[PaliGemma Vision Encoder] $brain
  vlm -> patches[Page Patch Vectors (1024 Multi-Vectors)] $database
  q_text[Query: ''Q3 EBITDA margin''] $code -> q_vecs[Query Token Vectors] $layers
  patches -> maxsim[MaxSim Late Interaction Sum-Max] $cpu *
  q_vecs -> maxsim',
  'flow',
  '[{"title": "ColPali GitHub Repository", "url": "https://github.com/illuin-tech/colpali"}]'::jsonb,
  35,
  3
from public.modules m
where m.slug = 'vector-databases-and-modern-rag'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '7.4',
  'document-chunking-hierarchical',
  'Advanced Document Parsing & Semantic Chunking',
  35,
  'theory_and_code',
  'So guys, agar aap document ko bilkul andha-dhund fixed 500 characters par split kar dein, to sentence beech mein kat jayega aur context destroy ho jayega!

Isliye modern RAG mein teen advanced chunking strategies use hoti hain:
1. **Recursive Character Chunking**: Paragraphs (`\n\n`), phir sentences (`\n`), phir spaces par split karta hai taake natural boundaries preserve hon.
2. **Semantic Chunking**: Har sentence ka embedding banata hai aur jahan do consecutive sentences ki Cosine Similarity achanak drop ho (Topic Shift), wahan naya chunk shuru karta hai.
3. **Parent-Document (Hierarchical) Retrieval**: Chotay 200-token chunks par search karta hai, lekin LLM ko poora parent paragraph (800 tokens) pass karta hai taake context complete rahay!',
  'Master recursive chunking, semantic similarity boundary detection, and parent-document hierarchical chunk retrieval.',
  'import numpy as np

def semantic_chunking(sentences: list, embeddings: list, threshold: float = 0.75):
    chunks = []
    current_chunk = [sentences[0]]
    
    for i in range(len(sentences) - 1):
        v1, v2 = embeddings[i], embeddings[i+1]
        sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        
        if sim < threshold:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentences[i+1]]
        else:
            current_chunk.append(sentences[i+1])
            
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

sample_sents = [
    "PyTorch is a popular deep learning library.",
    "It provides dynamic computational graphs and autograd.",
    "Pakistan celebrated its cricket victory yesterday.",
    "The fans in Lahore celebrated on the streets."
]
emb_data = [np.array([1.0, 0.1]), np.array([0.9, 0.2]), np.array([0.1, 0.9]), np.array([0.2, 0.85])]

chunks = semantic_chunking(sample_sents, emb_data)
print(f"Created {len(chunks)} Semantic Chunks cleanly separated by topic:")
for idx, c in enumerate(chunks):
    print(f"Chunk {idx+1}: {c}")',
  '@preset midnight
@animate flow
flow LR: Semantic Chunking Workflow
  raw_doc[Continuous Raw Document Text] $database -> sents[Sentence Segmenter] $code
  sents -> sim_calc[Consecutive Embedding Cosine Drop] $brain
  sim_calc -> split[Topic-Boundary Split] $layers
  split -> parent_child[Parent Document Hierarchical Store] $server *',
  'flow',
  '[{"title": "LangChain Semantic Chunking", "url": "https://python.langchain.com/docs/how_to/semantic_chunker/"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'vector-databases-and-modern-rag'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '7.5',
  'query-transformation-hyde-multi',
  'Query Transformations: HyDE, Multi-Query & Step-Back',
  35,
  'theory_and_code',
  'So guys, user ka original query aksar chota, ambiguous, ya incomplete hota hai (maslan: *"loan documents"*). Agar aap seedha is query ka embedding banayein to database se acche chunks nahi milenge.

Yahan kaam aati hain **Query Transformations**:
1. **HyDE (Hypothetical Document Embeddings)**: LLM se pehle ek farzi (hypothetical) ideal answer generate karwayein. Phir us generated answer ka embedding banayein! Document-to-document similarity hamesha query-to-document se 10x behtar hoti hai!
2. **Multi-Query**: LLM se ek query ke 3 mukhtalif synonyms generate karwayein aur parallel vector search karein.
3. **Step-Back Prompting**: Specific sawal se pehle broad foundational concept retrieve karna.',
  'Supercharge retrieval recall using query expansion strategies: Hypothetical Document Embeddings (HyDE), multi-query generation, and step-back abstractions.',
  'def generate_hyde_prompt(user_query: str) -> str:
    return (
        "Please write a short hypothetical paragraph answering this question accurately.\n"
        "Do not worry about specific facts, focus on domain vocabulary and scientific concepts.\n"
        f"Question: {user_query}\nHypothetical Answer:"
    )

query = "PyTorch AMP memory leak fix"
hypothetical_answer = (
    "When training with PyTorch Automatic Mixed Precision (AMP), ensure you call "
    "scaler.unscale_ before clipping gradients and invoke scaler.update(). Avoid storing tensors "
    "with attached computation graphs in history lists."
)

print("Original User Query:", query)
print("\nGenerated HyDE Passage (Matches doc space perfectly):")
print(hypothetical_answer)',
  '@preset midnight
@animate pulse
arch LR: HyDE Query Transformation
  raw_q[Short User Query] $terminal -> llm_gen[LLM Generates Hypothetical Doc] $brain
  llm_gen -> hyde_doc[Hypothetical Target Answer] $code
  hyde_doc -> vector_search[Doc-to-Doc High-Precision Search] $database *',
  'arch',
  '[{"title": "HyDE Research Paper", "url": "https://arxiv.org/abs/2212.10496"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'vector-databases-and-modern-rag'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '7.6',
  'module-7-capstone-enterprise-rag',
  'Module 7 Capstone: Zero-Hallucination Enterprise RAG with Source Verification',
  60,
  'project',
  'So guys, Module 7 ka Grand Capstone aapko real-world Enterprise AI architect banayega!

Is capstone mein aap ek **Zero-Hallucination Production RAG System** build karenge:
1. Multi-page financial report PDF ko parse aur semantic chunks mein split karna.
2. PostgreSQL `pgvector` HNSW index + BM25 sparse search se Hybrid Search run karna.
3. Cross-Encoder reranker se top-3 chunks prioritize karna.
4. LLM prompt mein strict citation rules lagana (e.g. `[Doc 1, Page 4]`).
5. Automated faithfulness check karna: agar answer context se substantiate na ho to model explicit *"I cannot answer based on the provided documents"* return kare!',
  'Ship an end-to-end enterprise RAG pipeline featuring hybrid HNSW+BM25 search, Cross-Encoder reranking, grounded citation generation, and hallucination guardrails.',
  'def generate_grounded_rag_prompt(query: str, retrieved_chunks: list) -> str:
    context_str = ""
    for idx, c in enumerate(retrieved_chunks):
        context_str += f"[Source {idx+1} | Page {c[''page'']}]: {c[''text'']}\n"
        
    prompt = (
        f"Context Information:\n{context_str}\n"
        "Task: Answer the user question strictly using the provided sources.\n"
        "Every factual claim must cite its source e.g. [Source 1, Page 2].\n"
        "If the context does not contain the answer, reply: ''Information not found in verified documents.''\n\n"
        f"Question: {query}\nGrounded Answer:"
    )
    return prompt

mock_chunks = [
    {"page": 4, "text": "Net revenue for Q3 2025 reached PKR 45.2 Billion, an increase of 18% YoY."},
    {"page": 7, "text": "Operating expenses were reduced by 6% due to automated AI workflows."}
]

rag_prompt = generate_grounded_rag_prompt("What was the Q3 2025 revenue?", mock_chunks)
print("Production Grounded Prompt:")
print(rag_prompt)',
  '@preset midnight
@animate flow
flow LR: Enterprise Zero-Hallucination RAG
  query[User Natural Query] $terminal -> hybrid[Hybrid HNSW + BM25 Search] $database
  hybrid -> rerank[Cross-Encoder Reranker] $server
  rerank -> context[Top-3 Verified Context Chunks] $layers
  context -> llm[LLM with Citation Grounding] $brain
  llm -> verifier[Faithfulness Verifier] $code
  verifier -> out[Guaranteed Grounded Output with Citations] $terminal *',
  'flow',
  '[{"title": "Ragas: Automated Evaluation of RAG", "url": "https://docs.ragas.io/"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'vector-databases-and-modern-rag'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '8.1',
  'react-agent-architecture',
  'ReAct Pattern: Reasoning + Acting Ka Mukammal Framework',
  35,
  'theory_and_code',
  'So guys, jab hum LLM ko tools (APIs, Database, Calculator) dete hain to wo sirf text generator nahi rehta, balke ek **Autonomous Agent** ban jata hai!

Sab se famous pattern hai **ReAct (Reasoning + Acting)**:
1. **Thought**: Model sochta hai ke agla qadam kya hona chahiye: *"Mujhe pehle customer ka order number dhoondna hai."*
2. **Action**: Model specific tool call karta hai with exact parameters: `lookup_order(order_id=9821)`.
3. **Observation**: Environment tool ka result wapis LLM ko bhejta hai: `Order status: Shipped, Tracking: TCS102`.
4. **Reflection**: Model observation dekh kar agla step decide karta hai ya final user response generate karta hai.

Agar tool koi error de to model **Self-Correction** karta hai aur doosra tareeqa azmata hai!',
  'Implement the ReAct paradigm: alternating between Reasoning thoughts, Action tool executions, and Observations with autonomous error correction.',
  'import json

def tool_database_lookup(user_id: int) -> dict:
    db = {101: {"name": "Ahmed", "tier": "Gold", "balance": 15000}}
    return db.get(user_id, {"error": "User not found"})

class ReActAgentLoop:
    def __init__(self):
        self.tools = {"database_lookup": tool_database_lookup}

    def execute_step(self, action_name: str, **kwargs):
        if action_name in self.tools:
            return self.tools[action_name](**kwargs)
        return {"error": "Unknown tool"}

agent = ReActAgentLoop()
action = "database_lookup"
args = {"user_id": 101}
observation = agent.execute_step(action, **args)
print("Tool Execution Observation:", json.dumps(observation))',
  '@preset midnight
@animate flow
flow LR: ReAct Autonomous Agent Loop
  thought[Thought: Model Reasons] $brain -> action[Action: Tool Call Generated] $code
  action -> env[Environment Executes Tool] $server
  env -> obs[Observation: Raw Tool Result] $database
  obs -> thought: Loop until Task Solved *
  thought -> final_ans[Final Resolved Answer] $terminal',
  'flow',
  '[{"title": "ReAct Research Paper (Yao et al.)", "url": "https://arxiv.org/abs/2210.03629"}]'::jsonb,
  25,
  1
from public.modules m
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '8.2',
  'anthropic-mcp-deepdive',
  '2026 Standard: Anthropic Model Context Protocol (MCP) Deep Dive',
  45,
  'theory_and_code',
  'So guys, pehle har company apna custom tool format likhti thi (LangChain tools alag, OpenAI functions alag, AutoGen alag). Is fragmented dunya ko khatam karne ke liye Anthropic ne **Model Context Protocol (MCP)** launch kiya jo 2026 ka universal USB-C standard ban chuka hai!

MCP Architecture ke 3 arkaan hain:
1. **MCP Host**: Application jismein LLM chal raha hai (jaise Claude Desktop, Antigravity IDE, ya aapka backend).
2. **MCP Client**: Jo host ke andar server se connection banata hai.
3. **MCP Server**: Lightweight microservice jo tools, prompts, aur resources expose karti hai via JSON-RPC 2.0 (stdio ya SSE transport).

Ek dafa aapne MCP server likh diya, wo kisi bhi AI client mein bina modification plug-and-play chalega!',
  'Master the Model Context Protocol (MCP): Host, Client, and Server architecture communicating via JSON-RPC 2.0 stdio/SSE transports.',
  'import json

def handle_mcp_request(json_rpc_str: str) -> str:
    req = json.loads(json_rpc_str)
    req_id = req.get("id")
    method = req.get("method")
    
    if method == "tools/list":
        return json.dumps({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "get_system_metrics",
                        "description": "Returns CPU and RAM statistics",
                        "inputSchema": {"type": "object", "properties": {}}
                    }
                ]
            }
        })
    return json.dumps({"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}})

sample_rpc = ''{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}''
response = handle_mcp_request(sample_rpc)
print("MCP Server Response:\n", response)',
  '@preset midnight
@animate pulse
arch LR: Anthropic MCP Architecture
  host[MCP Host (AI Platform)] $browser -> client[MCP Client Engine] $terminal
  client -> transport[JSON-RPC 2.0 via stdio / SSE] $layers
  transport -> server[MCP Server (Local Tools / DB / APIs)] $server *',
  'arch',
  '[{"title": "Official MCP Documentation", "url": "https://modelcontextprotocol.io/"}]'::jsonb,
  30,
  2
from public.modules m
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '8.3',
  'smolagents-code-agents',
  'HuggingFace smolagents: Code-First Agents & Sandboxing',
  40,
  'theory_and_code',
  'So guys, traditional agents har step par JSON tool calls generate karte hain:
`{"action": "add", "args": {"a": 5, "b": 10}}`
Agar aapko 100 calculations karni hon to 100 round-trips lagte hain jo bohot slow aur mehanga hota hai!

HuggingFace ne **smolagents** ke zariye **Code-First Agents** introduce kiye!
Model actions ko JSON mein nahi balke seedha **Python Code Block** mein likhta hai:
```python
results = [math.sqrt(x) for x in range(100)]
final_sum = sum(results)
print(final_sum)
```
Yeh code ek secure sandboxed AST interpreter mein execute hota hai. 1 single LLM call mein complex loops, data transformation, aur multi-tool logic execute ho jata hai!',
  'Explore HuggingFace smolagents: replacing clunky multi-turn JSON tool schemas with direct sandboxed Python code synthesis.',
  'import math

class SandboxedPythonAgent:
    def __init__(self):
        self.safe_globals = {"math": math, "sum": sum, "range": range, "print": print}

    def execute_agent_code(self, code_str: str):
        try:
            local_vars = {}
            exec(code_str, self.safe_globals, local_vars)
            return {"status": "success", "locals": local_vars}
        except Exception as e:
            return {"status": "error", "error_msg": str(e)}

agent = SandboxedPythonAgent()
generated_code = (
    "values = [math.factorial(n) for n in range(1, 6)]\n"
    "total = sum(values)"
)
res = agent.execute_agent_code(generated_code)
print("Sandboxed Code Execution Result:", res[''locals''][''total''])',
  '@preset midnight
@animate flow
flow LR: Code-First smolagents Execution
  prompt[User Data Analytics Request] $terminal -> llm[LLM Synthesizes Python Code] $brain
  llm -> ast_check[Sandboxed AST Security Inspection] $code
  ast_check -> py_exec[Python Local Interpreter Execution] $cpu *
  py_exec -> final_res[Instant Mathematical Result] $server',
  'flow',
  '[{"title": "HuggingFace smolagents Blog", "url": "https://huggingface.co/blog/smolagents"}]'::jsonb,
  30,
  3
from public.modules m
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '8.4',
  'function-calling-json-schemas',
  'Function Calling Specifications & Runtime Schema Validation',
  35,
  'theory_and_code',
  'So guys, jab LLM kisi tool ko call karta hai to aksar numbers ko string bana deta hai (`"50"` instead of `50`) ya required keys miss kar deta hai.

Iska production solution hai **Runtime Schema Validation via Pydantic & OpenAPI**.
Hum tool ki exact specification define karte hain:
- Tool name
- Clear description (jo model ko batati hai ke kab call karna hai)
- Pydantic parameters with type annotations aur default values.

Agar LLM ghalat arguments return kare to validator foran error trap karta hai aur model ko auto-correction prompt bhejta hai: *"Validation failed: age must be an integer >= 18"*. Model agle turn par theek argument generate karta hai!',
  'Define robust function specifications using OpenAPI schemas and Pydantic models with automated schema validation and correction loops.',
  'from pydantic import BaseModel, Field, ValidationError

class WeatherToolArgs(BaseModel):
    city: str = Field(description="Name of the city, e.g. Lahore, Karachi")
    days: int = Field(ge=1, le=7, description="Forecast days between 1 and 7")

def execute_validated_tool(raw_args: dict):
    try:
        validated = WeatherToolArgs(**raw_args)
        return {"status": "success", "result": f"Weather in {validated.city} for {validated.days} days: Sunny 28C"}
    except ValidationError as e:
        return {"status": "schema_error", "details": e.errors()}

bad_input = {"city": "Islamabad", "days": 10}
print("Validation Error Trap:", execute_validated_tool(bad_input))

good_input = {"city": "Islamabad", "days": 3}
print("Valid Tool Execution:", execute_validated_tool(good_input))',
  '@preset midnight
@animate flow
flow LR: Function Calling Validation Loop
  llm_call[LLM Tool Call Arguments] $brain -> pydantic[Pydantic Runtime Schema Check] $code
  pydantic -- Valid --> exec[Execute Python Tool Function] $server *
  pydantic -- Invalid --> retry[Error Context Feedback to LLM] $terminal
  retry -> llm_call',
  'flow',
  '[{"title": "OpenAI Function Calling Guide", "url": "https://platform.openai.com/docs/guides/function-calling"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '8.5',
  'langgraph-cyclic-workflows',
  'Stateful Multi-Agent Cyclic Graphs with LangGraph',
  40,
  'theory_and_code',
  'So guys, puraane agent frameworks (jaise original LangChain chains) Linear DAGs (Directed Acyclic Graphs) thay — yaani data sirf aage move kar sakta tha, pichle step par wapis nahi aa sakta tha!

Lekin real-world problem solving **Cyclic (Chakkar wali)** hoti hai:
Codegen -> Run Tests -> Error Found -> Wapis Codegen par jao -> Dubara test karo!

Iske liye 2026 mein **LangGraph** industry standard ban chuka hai.
LangGraph mein:
1. **State**: Ek shared dictionary jo tamam agents read/write karte hain.
2. **Nodes**: Python functions ya AI agents (Researcher, Coder, Reviewer).
3. **Edges & Conditional Edges**: Jo decide karte hain ke agla node kon sa chalay ga based on current state!
4. **Human-in-the-Loop**: Execution ko pause karke human approval ka wait karna.',
  'Architect stateful, cyclic agent workflows using LangGraph state machines, conditional edges, and human-in-the-loop checkpoints.',
  'from typing import TypedDict

class AgentState(TypedDict):
    code: str
    test_passed: bool
    iterations: int

def coder_node(state: AgentState) -> AgentState:
    print(f"Coder: Writing code attempt {state[''iterations''] + 1}...")
    state[''code''] = "def add(a, b): return a + b"
    state[''iterations''] += 1
    return state

def tester_node(state: AgentState) -> AgentState:
    print("Tester: Running pytest suite...")
    state[''test_passed''] = (state[''iterations''] >= 2)
    return state

def should_continue(state: AgentState) -> str:
    if state[''test_passed''] or state[''iterations''] >= 3:
        return "END"
    return "coder_node"

state = {"code": "", "test_passed": False, "iterations": 0}
while True:
    state = coder_node(state)
    state = tester_node(state)
    next_step = should_continue(state)
    if next_step == "END":
        print(f"Workflow Finished! Final Code: {state[''code'']}, Passed: {state[''test_passed'']}")
        break',
  '@preset midnight
@animate flow
flow LR: LangGraph Cyclic State Machine
  coder[Coder Agent Node] $code -> tester[Tester Validation Node] $server
  tester -> cond{Tests Passed?} $terminal
  cond -- NO --> coder
  cond -- YES --> end_node[Production Artifact Ready] $cube *',
  'flow',
  '[{"title": "LangGraph Official Documentation", "url": "https://langchain-ai.github.io/langgraph/"}]'::jsonb,
  30,
  5
from public.modules m
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '8.6',
  'module-8-capstone-autonomous-swarm',
  'Module 8 Capstone: Autonomous Multi-Agent Software Engineering Swarm',
  60,
  'project',
  'So guys, Module 8 ka Grand Capstone aapko **Autonomous Swarm Engineer** banayega!

Is capstone mein aap ek **Multi-Agent Software Development Swarm** implement karenge jismein 3 specialized agents aapas mein collaborate karte hain:
1. **Supervisor Agent**: User ki feature request ko decompose karta hai aur sub-tasks assign karta hai.
2. **Coder Agent**: Anthropic MCP server ke zariye file read/write tools execute karke code files create karta hai.
3. **Critic & Security Agent**: Code ko audit karta hai (SQL injection check, type errors) aur passing verdict deta hai.

Swarm ek cyclic loop mein chalega jab tak security audit 100% pass na ho jaye!',
  'Construct an autonomous multi-agent swarm with Supervisor, Worker, and Critic roles utilizing MCP tools and self-correcting feedback loops.',
  'class MultiAgentSwarm:
    def __init__(self):
        self.history = []

    def run_swarm(self, user_objective: str):
        print(f"=== Supervisor: Planning tasks for: ''{user_objective}'' ===")
        task = "Build sanitized SQL query builder"
        
        print("=== Coder Agent: Generating Python implementation ===")
        code = "def safe_query(user_id: int): return f''SELECT * FROM users WHERE id = {int(user_id)}''"
        
        print("=== Security Critic Agent: Auditing for SQL Injection ===")
        audit_passed = "int(" in code
        print(f"Security Audit Result: {''PASS'' if audit_passed else ''FAIL''}")
        
        return {"task": task, "code": code, "audit_status": "APPROVED"}

swarm = MultiAgentSwarm()
result = swarm.run_swarm("Create user query function")
print("\nSwarm Final Production Deliverable:", result)',
  '@preset midnight
@animate flow
flow LR: Multi-Agent Software Swarm
  user[User Feature Request] $terminal -> supervisor[Supervisor Planner Agent] $brain
  supervisor -> coder[Coder Agent (MCP File Tools)] $code
  coder -> critic[Security & Quality Critic Agent] $server
  critic -- Feedback & Bug Fixes --> coder
  critic -- Approved --> release[Production Git PR] $cube *',
  'flow',
  '[{"title": "Multi-Agent Systems Patterns", "url": "https://arxiv.org/abs/2308.08155"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '9.1',
  'peft-lora-qlora-foundations',
  'PEFT, LoRA & QLoRA Foundations: Low-Rank Adapters & Mathematics',
  35,
  'theory_and_code',
  'So guys, jab hum kisi 8 Billion parameter model (jaise Llama-3-8B) ko poora fine-tune karne ki koshish karte hain (Full Fine-Tuning), to humein har parameter ke gradients aur Adam optimizer states (first aur second moments) store karne parte hain. Ek 8B model 16-bit floating point mein 16GB VRAM leta hai, lekin training ke waqt 60GB se 80GB VRAM mangta hai! Yeh normal developers ke budget se bahar hai.

Iska revolutionary solution **PEFT (Parameter-Efficient Fine-Tuning)** aur khusoosan **LoRA (Low-Rank Adaptation)** hai. LoRA ka fundamental insight yeh hai: model ke weight updates matrix Delta W ka intrinsic rank bohot chota (low-rank) hota hai!

Original frozen weights W (dimension d x k) ko freeze rakha jata hai, aur side par do bohot choti matrices add ki jati hain:
`Delta W = B * A`
Jahan:
- `A` matrix ka dimension `r x k` hota hai (Gaussian initialization)
- `B` matrix ka dimension `d x r` hota hai (zeros se initialize)
- `r` rank parameter hai (aam tor par 8, 16, ya 32).

Forward pass ban jata hai:
`h = W * x + (alpha / r) * (B * A * x)`

Yahan `alpha` ek scaling constant hai (jaise 16 ya 32). Agar d=4096 aur r=16 ho, to parameters 4096 x 4096 = 16,777,216 se gir kar sirf 2 x 4096 x 16 = 131,072 reh jate hain—**99.2% parameter reduction!**

**QLoRA (Quantized LoRA)** is se bhi ek qadam aage jata hai: Base model ke frozen weights ko **NF4 (NormalFloat 4-bit)** format mein compress karta hai with Double Quantization aur Paged Optimizers, jis se aap 8B model ko sirf 6GB VRAM wale GPU par train kar sakte hain!',
  'Understand Low-Rank Adaptation (LoRA) and QLoRA mathematics, parameter-efficient weight decomposition (BA), rank selection, and NF4 quantization.',
  'import torch
import torch.nn as nn

class LoRALinear(nn.Module):
    """First-principles implementation of a LoRA Linear Layer."""
    def __init__(self, in_features: int, out_features: int, rank: int = 16, alpha: float = 32.0):
        super().__init__()
        # Frozen base weight matrix
        self.base_weight = nn.Parameter(torch.randn(out_features, in_features), requires_grad=False)
        self.rank = rank
        self.scaling = alpha / rank
        
        # Trainable low-rank decomposition matrices
        # Matrix A initialized with normal distribution
        self.lora_A = nn.Parameter(torch.randn(rank, in_features) * (1.0 / rank))
        # Matrix B initialized to zero so training starts with zero delta
        self.lora_B = nn.Parameter(torch.zeros(out_features, rank))
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Base forward pass (frozen)
        base_out = torch.matmul(x, self.base_weight.t())
        # LoRA forward pass: (x @ A.T) @ B.T * scaling
        lora_out = torch.matmul(torch.matmul(x, self.lora_A.t()), self.lora_B.t()) * self.scaling
        return base_out + lora_out

# Test layer dimensions
layer = LoRALinear(in_features=4096, out_features=4096, rank=16)
x = torch.randn(2, 4096)
output = layer(x)
print("Output shape:", output.shape)
trainable_params = sum(p.numel() for p in layer.parameters() if p.requires_grad)
frozen_params = sum(p.numel() for p in layer.parameters() if not p.requires_grad)
print(f"Trainable (LoRA): {trainable_params:,} | Frozen: {frozen_params:,}")',
  '@preset midnight
@animate flow
flow LR: LoRA Low-Rank Forward Pass
  input[Input Vector x] $terminal -> base[Frozen Base Weight W d x k] $database
  input -> lora_a[LoRA Matrix A r x k] $cpu
  lora_a -> lora_b[LoRA Matrix B d x r] $cpu
  lora_b -> scale[Scaling Alpha / r] $layers
  base -> add[Element-wise Sum (+)] $code
  scale -> add
  add -> output[Output Activation h] $server *',
  'flow',
  '[{"title": "Hugging Face PEFT Library", "url": "https://huggingface.co/docs/peft/index"}, {"title": "QLoRA: Efficient Finetuning of Quantized LLMs", "url": "https://arxiv.org/abs/2305.14314"}]'::jsonb,
  25,
  1
from public.modules m
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '9.2',
  'dataset-curation-chatml-packing',
  'Dataset Curation & ChatML Formatting: Tokenization Packing & Masks',
  35,
  'theory_and_code',
  'So guys, fine-tuning mein "Garbage In, Garbage Out" ka qanoon 100% sach hai! Agar aap 10,000 low-quality samples train karenge to model confuse ho jayega, lekin agar aap 1,000 pristine, carefully structured examples train karenge to model domain master ban jayega.

Modern fine-tuning ka industry standard format **ChatML** ya standard roles format hai (`system`, `user`, `assistant`). Har conversation ko specific special tokens mein wrap kiya jata hai:
`<|im_start|>system\nAap AI Ustaad ke medical assistant hain.<|im_end|>\n<|im_start|>user\nSirf sar dard hai.<|im_end|>\n<|im_start|>assistant\n...<|im_end|>`

Training ke waqt do critical techniques use hoti hain:
1. **Loss Masking (Prompt Masking)**: Model ko user ke prompt aur system prompt predict karne par penalize nahi kiya jata! Loss sirf aur sirf assistant ke response tokens par calculate hoti hai. PyTorch mein non-target tokens ka label `-100` set kiya jata hai (CrossEntropyLoss default ignore_index).
2. **Sample Packing (Sequence Packing)**: Agar aapka max context length 2048 hai aur aapke conversations 200-300 tokens ke hain, to padding tokens (`<pad>`) add karne se 70% GPU compute waste hota hai! Packing technique mein multiple conversations ko ek single 2048 sequence mein pack kar diya jata hai using attention masking.',
  'Structure training datasets into standardized ChatML format, apply loss masking with -100 labels on prompt tokens, and utilize sequence packing to eliminate wasted padding compute.',
  'from typing import List, Dict
import json

def format_chatml_example(system_prompt: str, conversations: List[Dict[str, str]]) -> str:
    """Converts structured multi-turn conversation into ChatML formatted string."""
    formatted = f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
    for turn in conversations:
        role = turn["role"] # ''user'' or ''assistant''
        content = turn["content"]
        formatted += f"<|im_start|>{role}\n{content}<|im_end|>\n"
    return formatted

# Example dataset record
record = {
    "system": "Aap AI Ustaad ke expert Python aur AI mentor hain jo Roman Urdu mein samjhate hain.",
    "conversations": [
        {"role": "user", "content": "PyTorch mein requires_grad=True ka kya maqsad hai?"},
        {"role": "assistant", "content": "So guys, jab aap requires_grad=True set karte hain, to PyTorch autograd engine ko batata hai ke is tensor par hone wale tamam mathematical operations ka computation graph track kare taake backward() call par gradients calculate ho sakein."}
    ]
}

chatml_text = format_chatml_example(record["system"], record["conversations"])
print(chatml_text)',
  '@preset midnight
@animate flow
flow LR: Sequence Packing in Context Window
  s1[Sample 1: 300 Tokens] $terminal -> pack[Packed 2048 Tensor] $cpu
  s2[Sample 2: 500 Tokens] $terminal -> pack
  s3[Sample 3: 800 Tokens] $terminal -> pack
  pack -> mask[Block-Diagonal Attention Mask] $database
  mask -> loss[Target Loss Masking: Only Assistant Labels] $brain *',
  'flow',
  '[{"title": "Hugging Face Chat Template Documentation", "url": "https://huggingface.co/docs/transformers/main/en/chat_templating"}, {"title": "OpenAI ChatML Specification", "url": "https://github.com/openai/openai-python/blob/main/chatml.md"}]'::jsonb,
  25,
  2
from public.modules m
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '9.3',
  'unsloth-fast-finetuning',
  'Fast 4-bit Fine-Tuning with Unsloth: Triton Kernels & FlashAttention',
  40,
  'theory_and_code',
  'So guys, standard Hugging Face PEFT library se jab aap LoRA train karte hain to Python overhead aur unoptimized PyTorch autograd kernels ki wajah se training slow hoti hai aur VRAM spikes aate hain.

**Unsloth** ek open-source framework hai jo fine-tuning ko **2x se 5x fast** karta hai aur VRAM usage ko **70% reduce** karta hai!
Unsloth yeh miracle kaise karta hai?
1. **Manual Triton GPU Kernels**: RoPE (Rotary Position Embeddings), Cross-Entropy Loss, aur MLP Activations (SwiGLU) ke liye PyTorch C++ kernels ki jagah custom OpenAI Triton kernels likhe gaye hain jo memory reads/writes minimize karte hain.
2. **Gradient Checkpointing Optimization**: Backward pass ke doran intermediate activations ko intelligently discard aur recompute karta hai bina VRAM explode kiye.
3. **Native 4-bit Quantization**: BitsAndBytes ke muqable mein zero accuracy loss ke sath direct 4-bit linear projection kernels provide karta hai.

Iska sab se bara faida: Aap Google Colab ke 100% free T4 GPU (15GB VRAM) par **Llama 3.1 8B**, **Mistral 7B**, ya **Phi-4** ko aasaani se fine-tune kar sakte hain!',
  'Leverage Unsloth''s hand-written OpenAI Triton kernels and optimized backpropagation to achieve 5x faster fine-tuning on free-tier consumer GPUs with 70% less VRAM.',
  '# Unsloth Fast Fine-Tuning Recipe (Runs seamlessly on Colab T4)
from unsloth import FastLanguageModel
import torch
from trl import SFTTrainer
from transformers import TrainingArguments

max_seq_length = 2048
dtype = None # Auto detection (Float16 for T4, Bfloat16 for Ampere+)
load_in_4bit = True # 4-bit QLoRA

# 1. Load Model & Tokenizer with Unsloth optimizations
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Meta-Llama-3.1-8B-Instruct",
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
)

# 2. Add LoRA Adapters to Attention & MLP projection matrices
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0, # Unsloth supports 0 dropout for optimized kernels
    bias="none",
    use_gradient_checkpointing="unsloth",
    random_state=3407,
)

print("Model successfully patched with Unsloth Triton kernels!")',
  '@preset midnight
@animate pulse
arch LR: Unsloth Memory Architecture
  gpu_ram[15GB T4 VRAM] $database -> q4[NF4 Base Model 5.5GB] $layers
  gpu_ram -> lora[LoRA Adapters 0.2GB] $cpu
  gpu_ram -> triton[Custom Triton Kernels 2.5GB] $server *
  gpu_ram -> free[Free Headroom 6.8GB] $chart',
  'arch',
  '[{"title": "Unsloth GitHub Repository", "url": "https://github.com/unslothai/unsloth"}, {"title": "OpenAI Triton Programming Guide", "url": "https://triton-lang.org/main/index.html"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '9.4',
  'dpo-orpo-alignment',
  'Preference Alignment: Direct Preference Optimization (DPO) & ORPO',
  35,
  'theory_and_code',
  'So guys, SFT (Supervised Fine-Tuning) se model text generate karna seekh jata hai, lekin model ko user ki preferences ke mutabiq align karna (helpful, harmless, accurate banana) SFT se mushkil hota hai.

Pehle iske liye **RLHF (Reinforcement Learning from Human Feedback)** use hota tha:
1. Ek alag **Reward Model** train kiya jata tha.
2. PPO (Proximal Policy Optimization) algorithm se policy update ki jati thi.
Lekin PPO bohot unstable tha, 4 models aik sath memory mein load karne parte the (Actor, Critic, Reference, Reward Model), aur training crash ho jati thi!

2023 mein Stanford researchers ne **DPO (Direct Preference Optimization)** introduce kiya.
DPO ka mathematical breakthrough: **Reward model ki zaroorat hi khatam kar di!**
DPO seedha policy model ki probabilities aur reference model ki probabilities ka ratio lekar closed-form mathematical derivation se loss compute karta hai:
`L_DPO = - E [ log sigma ( beta * log( pi(y_w | x) / pi_ref(y_w | x) ) - beta * log( pi(y_l | x) / pi_ref(y_l | x) ) ) ]`

Jahan:
- `y_w` = Chosen (winning/behtar) response
- `y_l` = Rejected (losing/kharab) response
- `beta` = KL divergence penalty scaling factor (aam tor par 0.1)

Model chosen response ki probability ko barhata hai aur rejected response ki probability ko exponentially drop karta hai!',
  'Master Direct Preference Optimization (DPO) and ORPO to align LLMs directly on pairwise chosen vs rejected completions without unstable reward models or PPO.',
  'from trl import DPOTrainer, DPOConfig
from datasets import Dataset

# Sample preference alignment dataset
preference_data = {
    "prompt": [
        "Python mein memory leak kaise debug karein?",
    ],
    "chosen": [
        "Memory leaks debug karne ke liye `tracemalloc` standard library use karein, snapshots compare karein aur circular references check karein objgraph ke sath.",
    ],
    "rejected": [
        "Memory leak koi masla nahi hota, bas computer restart kar dein ya RAM barha lein.",
    ]
}

dataset = Dataset.from_dict(preference_data)

dpo_config = DPOConfig(
    beta=0.1, # KL penalty strength
    learning_rate=5e-6,
    batch_size=2,
    gradient_accumulation_steps=4,
    max_prompt_length=512,
    max_length=1024,
    output_dir="./dpo_aligned_model"
)

print("DPO Configuration ready for preference alignment!")',
  '@preset midnight
@animate flow
flow LR: Direct Preference Optimization (DPO)
  prompt[User Prompt x] $terminal -> model[Policy Model pi_theta] $cpu
  prompt -> ref[Frozen Ref Model pi_ref] $database
  model -> log_ratio[Log Probability Ratio Win vs Loss] $brain
  ref -> log_ratio
  log_ratio -> loss[DPO Loss: Boost y_w & Suppress y_l] $layers *',
  'flow',
  '[{"title": "Direct Preference Optimization Paper (Rafailov et al.)", "url": "https://arxiv.org/abs/2305.18290"}, {"title": "TRL DPOTrainer Documentation", "url": "https://huggingface.co/docs/trl/dpo_trainer"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '9.5',
  'deepseek-r1-grpo-training',
  'DeepSeek-R1 GRPO: Reasoning Chains & Value-Model-Free RL',
  40,
  'theory_and_code',
  'So guys, January 2025 mein DeepSeek ne AI ki duniya ko hila kar rakh diya jab unhone **DeepSeek-R1** release kiya, jo OpenAI ke o1 ke barabar mathematical reasoning karta hai lekin 10x kam cost par!

DeepSeek-R1 ki sab se bari technical innovation **GRPO (Group Relative Policy Optimization)** hai.
PPO mein ek bara "Critic" ya "Value Model" chahiye hota hai jo har token ka value predict karta hai. GRPO ne Critic ko **mukammal tor par delete** kar diya!

GRPO kaise kaam karta hai?
1. Har prompt `q` ke liye, current model `G` different responses generate karta hai (jaise G=4 ya G=8 candidate reasoning chains).
2. Har response ko ek deterministic rule-based reward function score karta hai (maslan: kya final answer bracket `<answer>...</answer>` mein durust hai? Kya reasoning steps valid hain?). Scores: `r_1, r_2, ..., r_G`.
3. In `G` scores ka mean aur standard deviation compute kiya jata hai:
   `A_i = (r_i - mean(r)) / std(r)`
   Ise **Group Relative Advantage** kehte hain!
4. Agar kisi response ka score group ke average se behtar hai, to model us reasoning trajectory ko reinforce karta hai; agar group se bura hai to suppress karta hai!

Nateeja? Model bina kisi human supervision ke khud se long "Chain of Thought" (Aha! moments, self-correction, verification) develop kar leta hai!',
  'Understand DeepSeek-R1''s Group Relative Policy Optimization (GRPO), eliminating the PPO Critic model by computing group relative advantages across sampled candidate reasoning trajectories.',
  'import torch
from typing import List

def compute_grpo_advantages(rewards: List[float], epsilon: float = 1e-8) -> torch.Tensor:
    """Calculates Group Relative Advantage across G sampled completions (DeepSeek-R1 style)."""
    r = torch.tensor(rewards, dtype=torch.float32)
    mean = r.mean()
    std = r.std(unbiased=False)
    # Normalized relative advantage within the sampled group
    advantages = (r - mean) / (std + epsilon)
    return advantages

# Example: 4 sampled outputs for a math problem
# Output 1 got correct answer (1.0), Output 2 partial (0.5), Output 3 wrong (0.0), Output 4 wrong (0.0)
rewards = [1.0, 0.5, 0.0, 0.0]
advantages = compute_grpo_advantages(rewards)

for i, (rew, adv) in enumerate(zip(rewards, advantages)):
    status = "REINFORCE (+)" if adv > 0 else "PENALIZE (-)"
    print(f"Sample {i+1}: Reward = {rew:.2f} | Advantage = {adv.item():+.3f} -> {status}")',
  '@preset midnight
@animate flow
flow LR: DeepSeek-R1 GRPO Architecture
  prompt[Math / Logic Prompt q] $terminal -> gen[Generate G=4 Reasoning Chains] $cpu
  gen -> r1[Trajectory 1: Score 1.0] $code
  gen -> r2[Trajectory 2: Score 0.5] $code
  gen -> r3[Trajectory 3: Score 0.0] $code
  gen -> r4[Trajectory 4: Score 0.0] $code
  r1 & r2 & r3 & r4 -> grpo[GRPO Advantage: (r - mean) / std] $brain *
  grpo -> update[Policy Gradient Update with KL Bound] $server',
  'flow',
  '[{"title": "DeepSeek-R1: Incentivizing Reasoning Capability via RL", "url": "https://arxiv.org/abs/2501.12948"}, {"title": "Hugging Face TRL GRPOTrainer", "url": "https://huggingface.co/docs/trl/main/en/grpo_trainer"}]'::jsonb,
  30,
  5
from public.modules m
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '9.6',
  'capstone-fine-tune-domain-model',
  'Module 9 Capstone: Fine-Tune Domain LLM, Adapter Merge & GGUF Export',
  50,
  'project',
  'So guys, mubarak ho! Aap Module 9 ke Capstone project par pohanch chuke hain. Is capstone mein aap ek specialized domain-specific reasoning model train karenge aur use production inference ke liye packaging karenge!

Aapka Capstone Mission:
1. **Dataset Preparation**: Ek specialized domain (jaise Urdu/English Medical Triage ya Legal Contract Analysis) ka 1,000+ samples ka ChatML dataset curate aur validate karein.
2. **Unsloth QLoRA Training**: Llama 3.1 8B ko Unsloth mein 4-bit load karke LoRA rank r=16, alpha=32 par 3 epochs train karein. Training loss curve observe karein aur evaluate karein ke loss converge ho rahi hai.
3. **Weight Merging**: LoRA adapters ko base 16-bit model weights mein merge karein (`model.merge_and_unload()`).
4. **Quantization & Export**:
   - Model ko 16-bit safetensors format mein save karein vLLM high-throughput serving ke liye.
   - Model ko **GGUF Q4_K_M** aur **Q8_0** format mein quantize karein taake laptop ya edge device par offline run ho sake!
5. **Validation Benchmark**: Base model vs fine-tuned model ke answers compare karein aur domain accuracy gain document karein.',
  'Execute the Module 9 Capstone: fine-tune a domain model with Unsloth, merge LoRA adapters into base weights, and export to GGUF and safetensors formats for production serving.',
  '# Capstone LoRA Merge & GGUF Export Script
from unsloth import FastLanguageModel

# 1. Load trained model with adapters
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="./lora_model",
    max_seq_length=2048,
    load_in_4bit=False, # Load in 16-bit for clean weight merging
)

# 2. Save merged 16-bit model for vLLM production serving
print("Merging LoRA adapters into base weights...")
model.save_pretrained_merged("finetuned_domain_model_16bit", tokenizer, save_method="merged_16bit")
print("16-bit model saved for vLLM deployment!")

# 3. Export directly to GGUF format for local llama.cpp / Ollama execution
print("Exporting to GGUF Q4_K_M...")
model.save_pretrained_gguf("finetuned_domain_model_gguf", tokenizer, quantization_method="q4_k_m")
print("GGUF export complete! Ready for local and serverless deployment.")',
  '@preset midnight
@animate flow
flow LR: Capstone Fine-Tuning & Export Lifecycle
  dataset[Domain Dataset ChatML] $database -> train[Unsloth 4-bit LoRA Training] $cpu
  train -> eval[Validation & Loss Convergence] $chart
  eval -> merge[Merge Adapters to Base 16-bit] $server *
  merge -> vllm[vLLM High-Throughput SafeTensors] $cloud
  merge -> gguf[Local Edge GGUF Q4_K_M] $terminal',
  'flow',
  '[{"title": "Unsloth Saving & Exporting Guide", "url": "https://docs.unsloth.ai/basics/saving-and-exporting"}, {"title": "llama.cpp GGUF Quantization Formats", "url": "https://github.com/ggerganov/llama.cpp"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '10.1',
  'ragas-triad-llm-evals',
  'LLM Evaluation Frameworks: The Ragas Triad (Faithfulness & Relevance)',
  35,
  'theory_and_code',
  'So guys, jab aap production mein LLM ya RAG application deploy karte hain, to aap manual "vibe check" (kuch queries type karke dekhna) par bharosa nahi kar sakte! Production engineering ka asool hai: **"If you cannot measure it, you cannot improve it."**

RAG systems ko evaluate karne ka gold standard **Ragas Triad** hai:
1. **Faithfulness (Haqeeqat-Pasandi)**: Kya generated answer mukammal tor par retrieved context par mabni hai ya model ne bahar se jhoot bola hai? High faithfulness = Zero Hallucination!
2. **Answer Relevance**: Kya model ka answer user ke ahem sawaal ka direct jawab deta hai ya idhar udhar ki ghuma-phira kar baatein karta hai?
3. **Context Precision & Recall**: Kya vector database ne exact relevant chunks retrieve kiye the ya kachra context bheja tha?

Ragas framework LLM-as-a-judge paradigm use karta hai jahan ek high-reasoning model (jaise Claude 3.5 ya GPT-4o) structured prompts se har dimension par 0.0 se 1.0 ke darmiyan mathematical score assign karta hai.',
  'Implement quantitative RAG evaluation using the Ragas Triad to calculate mathematical metrics for Faithfulness, Answer Relevance, and Context Precision.',
  'from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevance, context_precision
from datasets import Dataset

# Sample evaluation dataset representing RAG pipeline test run
data_samples = {
    "question": ["AI Ustaad ka primary mission kya hai?"],
    "contexts": [["AI Ustaad Pakistan aur South Asia ka pehla zero-to-hero Roman Urdu AI Engineering curriculum hai jo production-grade skills sikhata hai."]],
    "answer": ["AI Ustaad ka maqsad Pakistan mein Roman Urdu ke zariye production-grade AI engineering sikhana hai."],
    "ground_truth": ["AI Ustaad Pakistan ka premier Roman Urdu AI platform hai."]
}

dataset = Dataset.from_dict(data_samples)

# Evaluate using the Ragas Triad metrics
results = evaluate(
    dataset=dataset,
    metrics=[faithfulness, answer_relevance, context_precision]
)

print("Ragas Evaluation Scores:")
print(f"Faithfulness: {results[''faithfulness'']:.3f}")
print(f"Answer Relevance: {results[''answer_relevance'']:.3f}")
print(f"Context Precision: {results[''context_precision'']:.3f}")',
  '@preset midnight
@animate flow
flow LR: The Ragas Evaluation Triad
  query[User Query] $terminal -> ctx[Retrieved Context] $database
  ctx -> ans[Generated Answer] $cpu
  ctx & ans -> f_score[Faithfulness Metric: Context -> Answer Grounding] $brain
  query & ans -> r_score[Answer Relevance Metric: Query -> Answer Match] $brain
  query & ctx -> p_score[Context Precision: Query -> Context Quality] $brain *',
  'flow',
  '[{"title": "Ragas Metrics Deep Dive", "url": "https://docs.ragas.io/en/stable/concepts/metrics/index.html"}, {"title": "Evaluating RAG Applications with TruLens", "url": "https://www.trulens.org/"}]'::jsonb,
  25,
  1
from public.modules m
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '10.2',
  'nemo-guardrails-semantic-rails',
  'Guardrails Architecture: NeMo Guardrails & Colang 2.0',
  35,
  'theory_and_code',
  'So guys, enterprise applications mein aap LLM ko khula nahi chhor sakte ke wo kisi competitor ki tareef kare, vulgar language generate kare, ya jailbreak prompts ("Ignore all previous instructions") ka shikar ban jaye!

NVIDIA ka **NeMo Guardrails** industry ka sab se powerful programmable guardrails system hai jo **Colang** language use karta hai.
NeMo teen levels par rails apply karta hai:
1. **Input Rails**: User ke prompt ko LLM tak pohanchne se pehle intercept karta hai. Agar prompt injection ya toxic intent detect ho, to LLM execute hi nahi hota!
2. **Dialog Rails**: Conversation ke flow ko guide karta hai taake bot hamesha defined business path par rahe.
3. **Output Rails**: LLM ke generated answer ko check karta hai. Agar model hallucinate kare ya sensitive confidential information leak kare, to response ko block karke safe fallback message bhejta hai.',
  'Deploy programmable guardrails with NVIDIA NeMo Guardrails and Colang 2.0 to enforce topical boundaries, prevent jailbreaks, and sanitize outputs.',
  '# config.co (Colang 2.0 Guardrails Definition)
''''''
define user ask about competitors
  "Does your platform use CompetitorX?"
  "Why is CompetitorY better than you?"

define bot refuse competitor discussion
  "AI Ustaad hamara flagship platform hai. Hum competitors par tabsira nahi karte, balki apne curriculum ki quality aur production results par focus karte hain."

define flow handle competitors
  user ask about competitors
  bot refuse competitor discussion

define user attempt jailbreak
  "Ignore all previous instructions"
  "DAN mode enabled"

define bot refuse jailbreak
  "Maaf kijiye, security policies ke teht yeh request process nahi ki ja sakti."

define flow handle jailbreak
  user attempt jailbreak
  bot refuse jailbreak
''''''

print("Colang 2.0 safety rails defined successfully!")',
  '@preset midnight
@animate flow
flow LR: NeMo Guardrails Interception Pipeline
  prompt[User Request] $terminal -> in_rail[Input Rail: Jailbreak Check] $shield
  in_rail -- Passed --> llm[Core LLM Engine] $cpu
  in_rail -- Flagged --> block[Predefined Safe Refusal] $lock
  llm -> out_rail[Output Rail: Fact & Policy Check] $shield
  out_rail -- Safe --> client[User Response] $server *
  out_rail -- Violates --> fallback[Safe Fallback Message] $lock',
  'flow',
  '[{"title": "NVIDIA NeMo Guardrails GitHub", "url": "https://github.com/NVIDIA/NeMo-Guardrails"}, {"title": "Colang Language Guide", "url": "https://docs.nvidia.com/nemo/guardrails/latest/colang_language_guide.html"}]'::jsonb,
  25,
  2
from public.modules m
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '10.3',
  'pii-redaction-presidio',
  'Enterprise Data Sanitization: Microsoft Presidio & PII Redaction',
  35,
  'theory_and_code',
  'So guys, agar aapka user chat mein apna CNIC number (Pakistan National ID), credit card details, phone number, ya private address enter kare, aur aap use direct external cloud LLM (OpenAI/Anthropic) ko bhej dein, to yeh **GDPR**, **HIPAA**, aur local data privacy laws ki shadeed violation hai!

Microsoft ka **Presidio** industry-standard PII (Personally Identifiable Information) detection aur anonymization engine hai.
Presidio do components par mushtamil hota hai:
1. **Presidio Analyzer**: Named Entity Recognition (NER spaCy models), regular expressions, aur mathematical checksums (jaise Luhn algorithm for credit cards) se PII entities detect karta hai.
2. **Presidio Anonymizer**: Detect hone wali entities ko mask karta hai (jaise `<PHONE_NUMBER>`, `<CNIC>`, ya sha-256 hash se replace karna).

Jab LLM response generate kar leta hai, to aap **Deanonymizer** ke zariye original values restore kar sakte hain, ya LLM ko hamesha sanitized data par hi operate karne dete hain.',
  'Sanitize and anonymize sensitive PII (CNIC, credit cards, emails, phone numbers) before cloud transmission using Microsoft Presidio Analyzer and Anonymizer.',
  'from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine

# 1. Initialize Presidio Engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# 2. Add custom Pakistani CNIC Recognizer (Format: 42101-1234567-1)
cnic_pattern = Pattern(name="pakistani_cnic_pattern", regex=r"\b\d{5}-\d{7}-\d{1}\b", score=0.95)
cnic_recognizer = PatternRecognizer(supported_entity="PAK_CNIC", patterns=[cnic_pattern])
analyzer.registry.add_recognizer(cnic_recognizer)

# 3. Analyze raw incoming text
raw_text = "Salam, mera naam Ahmad hai, CNIC 42101-1234567-1 aur email ahmad@example.com hai."
results = analyzer.analyze(text=raw_text, entities=["PAK_CNIC", "EMAIL_ADDRESS", "PERSON"], language="en")

# 4. Anonymize sensitive entities
anonymized_result = anonymizer.anonymize(text=raw_text, analyzer_results=results)

print("Original:", raw_text)
print("Sanitized for LLM:", anonymized_result.text)',
  '@preset midnight
@animate flow
flow LR: Presidio PII Redaction Architecture
  user_raw[Raw Text with PII] $terminal -> analyzer[Presidio Analyzer: NER & Regex] $database
  analyzer -> entities[Detected Entities: CNIC, Email, Phone] $layers
  entities -> anon[Presidio Anonymizer: Mask / Hash] $lock *
  anon -> clean_text[Clean Redacted Text] $server
  clean_text -> cloud_llm[External Cloud LLM Provider] $cloud',
  'flow',
  '[{"title": "Microsoft Presidio Documentation", "url": "https://microsoft.github.io/presidio/"}, {"title": "Presidio PatternRecognizer Guide", "url": "https://microsoft.github.io/presidio/analyzer/customizing_nlp_models/"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '10.4',
  'hallucination-detection-trulens',
  'Real-Time Hallucination Detection & Groundedness with TruLens',
  35,
  'theory_and_code',
  'So guys, RAG system mein sab se khatarnak cheez "Confident Hallucination" hoti hai—jahan model aisi baat pooray yaqeen ke sath likhta hai jo retrieved documents mein mojood hi nahi hoti!

Is challenge ko real-time production inference ke doran pakadne ke liye **TruLens** aur **Groundedness Verification** algorithms use kiye jate hain.
Groundedness verification ka mechanism yeh hai:
1. Model ke generated response ko atomic claims ya sentences mein split kiya jata hai (Sentence Tokenization).
2. Har claim ke liye retrieved context ke sath NLI (Natural Language Inference) entailment score calculate kiya jata hai:
   - **Entailment**: Claim context se logically sabit hota hai (Score 1.0)
   - **Neutral**: Context mein is claim ka zikr nahi hai (Score 0.5)
   - **Contradiction**: Claim context ke khilaf hai (Score 0.0)
3. Agar average Groundedness score defined threshold (maslan 0.80) se kam aye, to response ko foran suppress karke verified disclaimer ke sath fallback serve kiya jata hai!',
  'Deconstruct LLM responses into atomic propositional claims to compute real-time Natural Language Inference (NLI) Groundedness scores with TruLens.',
  'from typing import List, Dict

def verify_groundedness_claims(claims: List[str], context: str) -> Dict[str, any]:
    """Mock NLI Groundedness evaluator verifying claims against retrieved context."""
    verified_claims = []
    hallucinated_claims = []
    
    for claim in claims:
        # In production: Cross-Encoder NLI model (deberta-v3) computes entailment probability
        # Simplified token overlap heuristic for demonstration:
        words = [w.lower() for w in claim.split() if len(w) > 3]
        match_count = sum(1 for w in words if w in context.lower())
        overlap_ratio = match_count / max(len(words), 1)
        
        if overlap_ratio >= 0.6:
            verified_claims.append(claim)
        else:
            hallucinated_claims.append(claim)
            
    score = len(verified_claims) / max(len(claims), 1)
    return {
        "groundedness_score": score,
        "is_safe": score >= 0.75,
        "verified": verified_claims,
        "hallucinated": hallucinated_claims
    }

ctx = "AI Ustaad platform par 14 modules hain aur yeh Roman Urdu mein parhaya jata hai."
claims = [
    "AI Ustaad platform par 14 modules hain.",
    "AI Ustaad har student ko free Tesla car deta hai."
]

audit = verify_groundedness_claims(claims, ctx)
print(f"Groundedness Score: {audit[''groundedness_score'']:.2f} | Safe to deliver: {audit[''is_safe'']}")
print(f"Hallucinated flags: {audit[''hallucinated'']}")',
  '@preset midnight
@animate flow
flow LR: Real-Time Groundedness Verification
  resp[Generated LLM Response] $terminal -> split[Sentence / Claim Splitter] $layers
  split -> c1[Claim 1: 14 Modules] $code
  split -> c2[Claim 2: Free Tesla] $code
  c1 & c2 -> nli[NLI Entailment vs Context] $brain
  nli -> score[Groundedness Score: 0.50] $chart *
  score -- Below 0.80 --> block[Block & Alert User: High Hallucination Risk] $lock',
  'flow',
  '[{"title": "TruLens Groundedness Evaluation", "url": "https://www.trulens.org/trulens_eval/groundedness/"}, {"title": "Hugging Face DeBERTa NLI Model", "url": "https://huggingface.co/cross-encoder/nli-deberta-v3-base"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '10.5',
  'automated-eval-cicd-deepeval',
  'Automated CI/CD Evaluation Gates & Regression Testing with DeepEval',
  35,
  'theory_and_code',
  'So guys, jab software development mein hum naya code likhte hain to unit tests (pytest / jest) chala kar check karte hain ke purana feature break to nahi hua. Lekin AI engineering mein jab aap prompt change karte hain, embedding model update karte hain, ya chunking size badalte hain, to aapko kaise pata chalega ke overall accuracy improve hui ya degrade?

Iska solution **Automated CI/CD Evaluation Gates** hai using **DeepEval**!
Har Pull Request (PR) par GitHub Actions workflow trigger hota hai:
1. Predefined "Golden Test Dataset" (maslan 100 hard real-world questions with verified answers) run hota hai.
2. DeepEval har test case par G-Eval metrics (Hallucination Metric, Answer Relevance Metric, Bias Metric) evaluate karta hai.
3. Agar average score benchmark threshold (maslan 0.85) se drop ho jaye, to **CI build fail ho jati hai aur PR merge block ho jata hai!**

Is se aapki production app silent quality regression se hamesha mehfooz rehti hai.',
  'Configure continuous integration evaluation pipelines with DeepEval and GitHub Actions to enforce strict test gates and prevent accuracy regressions before deployment.',
  '# test_rag_quality.py (DeepEval Pytest Suite)
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric

def test_rag_faithfulness():
    # Construct test case from current staging pipeline
    test_case = LLMTestCase(
        input="Pakistan ka capital shehar konsa hai?",
        actual_output="Pakistan ka dar-ul-hukumat Islamabad hai.",
        context=["Islamabad Pakistan ka official capital shehar hai."]
    )
    
    # Define metrics with strict production thresholds
    relevancy_metric = AnswerRelevancyMetric(threshold=0.8)
    hallucination_metric = HallucinationMetric(threshold=0.2) # Max 20% hallucination allowed
    
    # Assert will fail pytest if thresholds are violated
    assert_test(test_case, [relevancy_metric, hallucination_metric])

print("DeepEval CI/CD test case validated for automated pipeline execution!")',
  '@preset midnight
@animate flow
flow LR: GitHub Actions AI Evaluation Gate
  git_push[Git Push / PR] $terminal -> gh_action[GitHub Actions Runner] $server
  gh_action -> run_suite[DeepEval Golden Test Suite: 100 Cases] $database
  run_suite -> metrics[Compute Aggregate Scores] $chart
  metrics -- Score >= 0.85 --> pass[Green Gate: Auto-Merge Allowed] $server *
  metrics -- Score < 0.85 --> fail[Red Gate: PR Blocked & Slack Alert] $lock',
  'flow',
  '[{"title": "DeepEval GitHub Actions CI/CD Integration", "url": "https://docs.confident-ai.com/docs/integrations-github-actions"}, {"title": "Continuous Integration for LLM Applications", "url": "https://martinfowler.com/articles/cd4ml.html"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '10.6',
  'capstone-enterprise-safety-firewall',
  'Module 10 Capstone: Enterprise Safety Firewall & Multi-Layer Gateway',
  50,
  'project',
  'So guys, congratulations! Aap Module 10 ke Capstone par pohanch chuke hain. Is capstone mein aap ek complete, production-grade **Enterprise AI Safety Firewall** build karenge jo raw user prompts aur LLM responses ke beech bulletproof shield ka kaam karega!

Aapka Capstone Architecture:
1. **Presidio PII Interceptor**: Incoming prompt se Pakistani CNIC, Credit Card, Email aur Phone numbers ko detect aur redact karega.
2. **NeMo Topical & Jailbreak Rails**: Jailbreak attempts ("DAN mode", "Ignore instructions") aur competitor comparisons ko instant block karega.
3. **NLI Groundedness Checker**: LLM ke generated answer ke har sentence ko context ke sath cross-check karega; agar groundedness score < 0.80 ho to disclaimer inject karega.
4. **Structured Audit Logging**: Har request ka safety status, redacted fields count, aur evaluation scores structured JSON format mein log karega for compliance.
5. **FastAPI Firewall Gateway**: In tamam layers ko ek high-performance async API endpoint mein package karein.',
  'Architect and deploy the Module 10 Capstone: a multi-layered Enterprise AI Safety Firewall integrating Presidio PII redaction, NeMo Guardrails, and NLI Groundedness checks.',
  'import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="AI Ustaad Enterprise Safety Gateway")

class PromptRequest(BaseModel):
    query: str
    user_id: str

class SafeResponse(BaseModel):
    is_safe: bool
    sanitized_query: str
    response: str
    safety_flags: List[str]

@app.post("/api/v1/secure-chat", response_model=SafeResponse)
async def secure_chat_endpoint(req: PromptRequest):
    flags = []
    
    # 1. Jailbreak Check
    jailbreak_keywords = ["ignore previous", "dan mode", "jailbreak"]
    if any(k in req.query.lower() for k in jailbreak_keywords):
        flags.append("JAILBREAK_ATTEMPT")
        return SafeResponse(
            is_safe=False,
            sanitized_query=req.query,
            response="Security Policy Violation: Prompt injection patterns detected.",
            safety_flags=flags
        )
        
    # 2. PII Sanitization (Mock Presidio)
    sanitized = req.query
    if "@" in sanitized:
        sanitized = "[REDACTED_EMAIL]"
        flags.append("PII_EMAIL_REDACTED")
        
    # 3. Process Safe Query
    simulated_answer = f"Safe response generated for query: {sanitized}"
    
    return SafeResponse(
        is_safe=True,
        sanitized_query=sanitized,
        response=simulated_answer,
        safety_flags=flags
    )',
  '@preset midnight
@animate pulse
arch LR: Capstone Enterprise Safety Gateway
  user[User Request] $browser -> pii[Layer 1: Presidio PII Sanitizer] $lock
  pii -> rails[Layer 2: NeMo Jailbreak & Topical Rail] $shield
  rails -> llm[Layer 3: Core LLM Inference Engine] $cpu
  llm -> nli[Layer 4: Real-Time Groundedness Checker] $brain *
  nli -> audit[Layer 5: Structured JSON Audit Log] $database
  nli -> safe_user[Sanitized Verified Response] $server',
  'arch',
  '[{"title": "OWASP Top 10 for Large Language Models", "url": "https://owasp.org/www-project-top-10-for-large-language-model-applications/"}, {"title": "Enterprise AI Security Best Practices", "url": "https://nv-nemo.github.io/guardrails/"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '11.1',
  'vllm-paged-attention-mechanics',
  'High-Throughput LLM Inference: vLLM Architecture & PagedAttention',
  35,
  'theory_and_code',
  'So guys, jab aap production mein LLM serve karte hain, to sab se bara bottleneck GPU compute nahi balki **GPU Memory (VRAM)** hoti hai, khusoosan **KV Cache (Key-Value Cache)**!

Traditional inference systems mein har incoming request ke liye memory pehle se reserve (pre-allocate) ki jati thi max_context_length (jaise 4096 tokens) ke hisab se. Nateeja?
- **Internal Fragmentation**: Agar request sirf 100 tokens generate kare, to baqi 3996 tokens ki VRAM bilkul waste ho jati thi!
- **External Fragmentation**: Memory contiguous na hone ki wajah se VRAM hote hue bhi nayi requests reject ho jati theen. 60% se 80% VRAM waste hoti thi!

UC Berkeley ke researchers ne **PagedAttention** introduce kiya (jo vLLM ka dil hai), jo operating system ke **Virtual Memory Paging** concept se inspired hai:
1. KV Cache ko contiguous memory mein rakhne ki bajaye fixed-size **Pages / Blocks** (jaise 16 ya 32 tokens per block) mein divide kiya jata hai.
2. GPU VRAM mein ek **Block Table** maintain hoti hai jo logical token positions ko physical non-contiguous GPU blocks se map karti hai.
3. Jab naya token generate hota hai, to sirf ek chota physical block allocate hota hai—zero memory waste!
4. **Continuous Batching (Iteration-Level Scheduling)**: Nayi requests ko purani batch ke khatam hone ka intezar nahi karna parta; har token step par nayi requests batch mein enter aur exit ho sakti hain!

Nateeja? vLLM standard Hugging Face ke muqable mein **10x se 24x zyada throughput** deliver karta hai!',
  'Master vLLM''s PagedAttention virtual memory architecture and continuous batching to eliminate KV-cache fragmentation and achieve 20x higher inference throughput.',
  '# vLLM High-Throughput Serving Script
from vllm import LLM, SamplingParams

# 1. Define Sampling Parameters
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.9,
    max_tokens=256
)

# 2. Initialize vLLM Engine with PagedAttention
# gpu_memory_utilization: Reserve 90% of GPU VRAM for model & Paged KV cache
llm = LLM(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    tensor_parallel_size=1, # Number of GPUs
    gpu_memory_utilization=0.90,
    max_model_len=4096,
    trust_remote_code=True
)

prompts = [
    "Python mein async generators kaise kaam karte hain?",
    "Explain PagedAttention in three concise sentences.",
    "Database indexing ke primary trade-offs kya hain?"
]

# Continuous batching processes all prompts concurrently
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"\nPrompt: {prompt}\nResponse: {generated_text.strip()}")',
  '@preset midnight
@animate flow
flow LR: PagedAttention Virtual Memory Mapping
  logical[Logical Tokens: [0..15] [16..31]] $terminal -> table[vLLM Block Table] $server
  table -> p1[Physical Block 7 in VRAM] $database
  table -> p2[Physical Block 12 in VRAM] $database
  p1 & p2 -> attn[Non-Contiguous Paged Attention Kernel] $cpu *
  attn -> stream[Continuous Batching Output Stream] $chart',
  'flow',
  '[{"title": "vLLM Documentation", "url": "https://docs.vllm.ai/"}, {"title": "PagedAttention Paper", "url": "https://arxiv.org/abs/2309.06180"}]'::jsonb,
  25,
  1
from public.modules m
where m.slug = 'production-ai-engineering-mlops'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '11.2',
  'model-quantization-awq-gptq',
  'Model Quantization Deep Dive: AWQ, GPTQ & KV Cache Compression',
  35,
  'theory_and_code',
  'So guys, model quantization ka matlab hai weights aur activations ki numeric precision ko kam karna (jaise 16-bit Float se 4-bit ya 8-bit Integer mein convert karna) taake memory 75% kam ho jaye aur bandwidth 4x fast ho jaye!

Lekin agar aap naadani mein tamam weights ko round off kar dein, to model ki reasoning collapse ho jati hai.
Modern quantization do clever techniques use karti hai:
1. **AWQ (Activation-aware Weight Quantization)**:
   AWQ ka fundamental insight yeh hai: **Tamam weights barabar ahem nahi hote!** Sirf 1% weights aise hote hain jin par activation magnitudes bohot bare hote hain (Salient Weights). AWQ in 1% salient weights ko identify karke unhe mathematically protect karta hai aur baqi 99% weights ko 4-bit quantize kar deta hai. Nateeja? Zero perplexity loss!
2. **GPTQ (Generalized Post-Training Quantization)**:
   Second-order Taylor expansion (Hessian matrix) use karke layer-by-layer quantization errors ko compensate karta hai.
3. **KV Cache FP8 / INT8 Quantization**:
   Sirf model weights hi nahi, balki lambi conversations ke KV Cache ko bhi 16-bit float ki jagah FP8 mein compress kiya jata hai, jis se context length double ho jati hai bina extra VRAM ke!',
  'Understand AWQ (Activation-aware Weight Quantization), GPTQ, and FP8 KV-cache compression to run large models in 75% less VRAM without perplexity degradation.',
  '# Deploying AWQ 4-Bit Model with vLLM
from vllm import LLM, SamplingParams

# Serving quantized AWQ model directly on consumer/cloud GPU
# Notice: quantization="awq" flag instructs vLLM to use optimized GEMM W4A16 kernels
llm = LLM(
    model="TheBloke/Llama-2-7B-Chat-AWQ",
    quantization="awq",
    dtype="float16",
    max_model_len=4096
)

sampling_params = SamplingParams(temperature=0.7, max_tokens=150)
outputs = llm.generate(["What is the primary benefit of AWQ quantization?"], sampling_params)
print(outputs[0].outputs[0].text)',
  '@preset midnight
@animate flow
flow LR: AWQ Activation-Aware Quantization
  weights[FP16 Weights 14GB] $database -> inspect[Activation Magnitude Profiler] $cpu
  inspect -> salient[Top 1% Salient Weights: Protect High Precision] $shield
  inspect -> normal[99% Normal Weights: Quantize to 4-bit INT4] $layers
  salient & normal -> pack[AWQ Compressed Model 3.8GB] $server *
  pack -> vram[Fits in 8GB VRAM GPU with Zero Perplexity Loss] $terminal',
  'flow',
  '[{"title": "AWQ: Activation-aware Weight Quantization Paper", "url": "https://arxiv.org/abs/2306.00978"}, {"title": "AutoAWQ GitHub Repository", "url": "https://github.com/casper-hansen/AutoAWQ"}]'::jsonb,
  25,
  2
from public.modules m
where m.slug = 'production-ai-engineering-mlops'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '11.3',
  'rust-axum-llm-gateway',
  'High-Concurrency LLM Reverse Proxy & Gateway in Rust Axum',
  40,
  'theory_and_code',
  'So guys, jab aapke platform par hazaron concurrent users token streaming requests bhej rahe hon, to Python ka asyncio runtime (uvicorn/gunicorn) Global Interpreter Lock (GIL) aur memory overhead ki wajah se bottleneck ban jata hai.

Iska high-performance solution **Rust** aur **Axum** (built on Tokio asynchronous runtime) hai!
Kyun Rust?
- **Zero-Cost Abstractions**: Rust mein koi garbage collector nahi hota; memory compile-time par deterministic hoti hai.
- **Fearless Concurrency**: Tokio multi-threaded work-stealing threadpool hazaron concurrent SSE connections ko minimal CPU aur sirf kuch megabytes RAM mein handle kar leta hai!
- **Channel Streaming**: Rust ke `tokio::sync::mpsc` channels ke zariye backend vLLM se aane wale token streams direct client HTTP response stream mein pipe ho jate hain bina intermediate allocation ke.

Is lesson mein hum ek production Rust Axum gateway banayenge jo token rate limiting, authentication, aur SSE streaming proxying provide karega.',
  'Architect an ultra-high concurrency LLM streaming gateway in Rust Axum leveraging the Tokio async runtime for sub-millisecond connection handling.',
  '// Rust Axum LLM Streaming Reverse Proxy (src/main.rs)
use axum::{
    routing::get,
    response::sse::{Event, KeepAlive, Sse},
    Router,
};
use futures::stream::{self, Stream};
use std::{convert::Infallible, time::Duration};
use tokio_stream::StreamExt as _;

async fn stream_tokens() -> Sse<impl Stream<Item = Result<Event, Infallible>>> {
    let words = vec!["Salam!", "Yeh", "Rust", "Axum", "high-throughput", "streaming", "gateway", "hai."];
    
    let stream = stream::iter(words).map(|word| {
        Ok(Event::default().data(word))
    }).throttle(Duration::from_millis(50));

    Sse::new(stream).keep_alive(KeepAlive::default())
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/v1/stream", get(stream_tokens));
    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();
    println!("Rust Axum Gateway listening on http://0.0.0.0:8080");
    axum::serve(listener, app).await.unwrap();
}',
  '@preset midnight
@animate flow
flow LR: Rust Axum Concurrent Gateway
  clients[10,000+ Concurrent HTTP Connections] $browser -> tokio[Tokio Work-Stealing Runtime] $cpu
  tokio -> axum[Rust Axum Router & Rate Limiter] $server *
  axum -> pool[Reqwest HTTP/2 Connection Pool] $network
  pool -> vllm[Backend vLLM Cluster] $database
  vllm -> clients: Zero-Copy Chunked SSE Streams',
  'flow',
  '[{"title": "Axum Web Framework Docs", "url": "https://docs.rs/axum/latest/axum/"}, {"title": "Tokio Asynchronous Runtime", "url": "https://tokio.rs/"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'production-ai-engineering-mlops'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '11.4',
  'opentelemetry-langfuse-observability',
  'Production LLM Observability: OpenTelemetry, Tracing & Langfuse',
  35,
  'theory_and_code',
  'So guys, jab ek user ki request aati hai aur wo agentic loop, vector retrieval, reranking, aur LLM call se guzarti hai, to agar response mein 4 seconds lag gaye ya galat answer aya, to aap kaise diagnose karenge ke masla kahan tha?
- Kya vector database slow tha?
- Kya prompt tokens bohot lambe the?
- Kya tool execution fail hui?

Iska jawab **Distributed Tracing & LLM Observability** hai using **OpenTelemetry** aur **Langfuse**!
1. **Traces & Spans**: Har request ko ek unique `trace_id` milta hai. Har internal operation (embedding generation, DB query, LLM completion) ek child `span` banata hai jisme exact latency (milliseconds), input/output tokens, aur cost track hoti hai.
2. **Token & Cost Accounting**: Har LLM provider ke input aur output tokens calculate karke exact dollar cost per user track ki jati hai.
3. **Session Replays**: User feedback (thumbs up / thumbs down) ko trace se link karke debugging dashboard mein dekha ja sakta hai.',
  'Instrument production AI pipelines with OpenTelemetry spans and Langfuse tracing to monitor latency bottlenecks, token unit economics, and end-to-end execution graphs.',
  'from langfuse import Langfuse
import time

# Initialize Langfuse client
langfuse = Langfuse()

def run_observed_rag_pipeline(user_query: str, user_id: str):
    # 1. Create root trace for user session
    trace = langfuse.trace(
        name="chat_interaction",
        user_id=user_id,
        input={"query": user_query}
    )
    
    # 2. Span: Vector Database Retrieval
    retrieval_span = trace.span(name="vector_retrieval", input=user_query)
    time.sleep(0.04) # Simulate DB latency
    retrieved_docs = ["Doc 1: AI Ustaad curriculum overview"]
    retrieval_span.end(output={"docs_count": len(retrieved_docs)})
    
    # 3. Generation: LLM Call with token metrics
    generation = trace.generation(
        name="llama_completion",
        model="meta-llama/llama-3.1-8b-instruct",
        input=[{"role": "user", "content": user_query}],
        output="Salam! AI Ustaad mein 14 modules hain.",
        usage={"input": 45, "output": 18, "total": 63}
    )
    
    trace.update(output="Salam! AI Ustaad mein 14 modules hain.")
    print("Trace successfully exported to Langfuse dashboard!")

run_observed_rag_pipeline("AI Ustaad mein kitne modules hain?", "student_user_101")',
  '@preset midnight
@animate flow
flow LR: OpenTelemetry Distributed Trace
  trace[Trace: User Chat Request] $terminal -> span_retrieval[Span: Hybrid Search 42ms] $database
  trace -> span_rerank[Span: FlashRank Reranker 18ms] $cpu
  trace -> span_llm[Generation: vLLM Stream 320ms] $server *
  span_llm -> metrics[Export to Langfuse & Prometheus: Tokens, Latency, Cost] $chart',
  'flow',
  '[{"title": "Langfuse Open Source LLM Observability", "url": "https://langfuse.com/docs"}, {"title": "OpenTelemetry Python SDK", "url": "https://opentelemetry.io/docs/languages/python/"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'production-ai-engineering-mlops'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '11.5',
  'kubernetes-kserve-ray-autoscaling',
  'Enterprise Cluster Serving: Kubernetes, KServe, Ray & Autoscaling',
  35,
  'theory_and_code',
  'So guys, enterprise scale par jab traffic subah 100 requests/sec se barh kar shaam ko 50,000 requests/sec ho jaye, to aap ek single GPU server par nahi reh sakte! Aapko dynamic horizontal cluster autoscaling chahiye.

Modern AI infrastructure **Kubernetes (K8s)** par build hoti hai using two dominant technologies:
1. **KServe / vLLM Operator**:
   KServe Kubernetes par serverless AI serving provide karta hai. Yeh standard CPU/Memory metrics ki bajaye **Queue Depth (vLLM Waiting Requests)** aur **KV Cache Usage** par autoscaling (HPA / KEDA) trigger karta hai! Agar waiting queue > 10 ho jaye, to foran naye GPU pods spin up ho jate hain.
2. **Ray Serve**:
   Distributed Python execution framework jo multi-node model parallelism (Tensor Parallelism across 8x H100 GPUs) aur dynamic request routing handle karta hai.

Is lesson mein hum production Kubernetes manifests (Deployment, Service, KEDA ScaledObject) configure karenge jo zero-downtime rolling updates provide karte hain.',
  'Deploy distributed LLM inference clusters on Kubernetes with KServe and Ray Serve, configuring KEDA autoscaling driven by real-time vLLM queue-depth metrics.',
  '# k8s-vllm-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-inference-deployment
  labels:
    app: vllm-engine
spec:
  replicas: 2
  selector:
    matchLabels:
      app: vllm-engine
  template:
    metadata:
      labels:
        app: vllm-engine
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:latest
        args: ["--model", "meta-llama/Meta-Llama-3.1-8B-Instruct", "--gpu-memory-utilization", "0.9"]
        resources:
          limits:
            nvidia.com/gpu: 1
            memory: 32Gi
            cpu: "8"
        ports:
        - containerPort: 8000
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 60
          periodSeconds: 10',
  '@preset midnight
@animate pulse
arch LR: Kubernetes KServe Cluster Autoscaling
  ingress[Cloud Ingress / Load Balancer] $network -> keda[KEDA Autoscaler Controller] $server
  keda -> metric[vLLM Waiting Requests Metric] $chart
  ingress -> pod1[GPU Pod 1: vLLM Replica] $cpu
  ingress -> pod2[GPU Pod 2: vLLM Replica] $cpu
  metric -- Queue > 15 --> pod3[Scale Out: GPU Pod 3] $cloud *',
  'arch',
  '[{"title": "KServe: Cloud-Native Model Serving", "url": "https://kserve.github.io/website/"}, {"title": "KEDA: Kubernetes Event-Driven Autoscaling", "url": "https://keda.sh/"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'production-ai-engineering-mlops'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '11.6',
  'capstone-high-throughput-cluster',
  'Module 11 Capstone: Production High-Throughput Serving Cluster (99.9% SLA)',
  50,
  'project',
  'So guys, congratulations! Aap Phase 4 ke final Capstone project par pohanch chuke hain. Is capstone mein aap ek high-scale, resilient **Production AI Serving Cluster** architecture assemble karenge jo 99.9% uptime SLA ensure karega!

Aapka Capstone Architecture:
1. **Rust Axum Gateway Layer**: Front-facing API jo token authentication, rate limiting (sliding window), aur client SSE streaming handle karegi.
2. **Multi-Provider Fallback Circuit Breaker**: Primary vLLM cluster par requests send karega; agar local cluster busy ya down ho (latency > 2s ya 5xx errors), to automatically external failover provider (jaise Groq ya Cerebras) par seamless switch karega!
3. **Telemetry & Metrics Exporter**: Prometheus `/metrics` endpoint expose karega jo Token Latency P95/P99, Active Connections, aur Cache Hit Ratios track karega.
4. **Docker Compose & K8s Packaging**: Poore stack (Axum Proxy + vLLM + Redis Cache + Prometheus) ko containerize karein with automated health checks.
5. **Stress Test Verification**: Locust ya k6 se 500 concurrent virtual users ka load test chala kar verify karein ke zero dropped requests hon!',
  'Build and verify the Module 11 Capstone: an enterprise-grade high-throughput serving cluster with Rust Axum gateway, dynamic fallback circuit breakers, and Prometheus telemetry.',
  '# Prometheus Metric Exporter for LLM Serving Cluster (Python/Rust Middleware)
from prometheus_client import Counter, Histogram, generate_latest
from fastapi import FastAPI, Response

app = FastAPI()

# 1. Prometheus Metrics Definitions
REQUEST_COUNT = Counter(''llm_requests_total'', ''Total incoming LLM inference requests'', [''model'', ''status''])
LATENCY_HISTOGRAM = Histogram(''llm_token_latency_seconds'', ''Token generation latency in seconds'', [''model''])

@app.get("/api/chat")
async def chat_handler(model: str = "llama-3.1-8b"):
    REQUEST_COUNT.labels(model=model, status="success").inc()
    with LATENCY_HISTOGRAM.labels(model=model).time():
        # Simulated inference
        pass
    return {"status": "ok", "message": "Cluster operational"}

@app.get("/metrics")
async def metrics_endpoint():
    """Exposes standard Prometheus scrape endpoint."""
    return Response(content=generate_latest(), media_type="text/plain")',
  '@preset midnight
@animate flow
flow LR: High-Throughput Cluster with Circuit Breaker
  traffic[High Concurrency User Traffic] $browser -> gateway[Rust Axum Gateway & Rate Limiter] $server *
  gateway -> cb[Circuit Breaker & Fallback Manager] $shield
  cb -- Normal Healthy --> vllm_cluster[Primary vLLM K8s Cluster] $cpu
  cb -- High Latency / 5xx Error --> groq[Failover Fast Cloud Groq API] $cloud
  gateway -> prometheus[Prometheus & Grafana Telemetry] $chart',
  'flow',
  '[{"title": "Designing Data-Intensive Applications: Reliability", "url": "https://dataintensive.net/"}, {"title": "Prometheus Monitoring System", "url": "https://prometheus.io/docs/introduction/overview/"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'production-ai-engineering-mlops'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '12.1',
  'vision-language-foundations-clip',
  'Foundations of Vision-Language Models: CLIP & Contrastive Learning',
  35,
  'theory_and_code',
  'So guys, 2021 se pehle Computer Vision aur NLP do bilkul alag alag jaziray (islands) the! Computer Vision models (ResNet, EfficientNet) 1,000 fixed ImageNet classes predict karte the, jabke NLP models text par kaam karte the.

OpenAI ke **CLIP (Contrastive Language-Image Pre-training)** ne in dono dunyaon ko hamesha ke liye mila diya!
CLIP ka core concept bohot khubsurat hai: **Contrastive Learning in a Shared Joint Embedding Space**.
CLIP kaise train hota hai?
1. 400 Million (Image, Text Caption) pairs internet se liye gaye.
2. Image ko ek **Vision Encoder** (ViT ya ResNet) se pass karke vector $I_i$ banaya jata hai ($d=512$).
3. Text caption ko ek **Text Encoder** (Transformer) se pass karke vector $T_j$ banaya jata ($d=512$).
4. Ek batch mein $N$ images aur $N$ texts hote hain ($N \times N$ similarity matrix).
5. Loss function (InfoNCE / Symmetric Cross Entropy) ka target yeh hota hai ke diagonal elements ($I_i \cdot T_i$) ki cosine similarity maximum ho (close to 1), aur non-diagonal elements ($I_i \cdot T_j$) ki similarity 0 ke qareeb ho!

Iska jadu: CLIP bina kisi training ke **Zero-Shot Classifier** ban jata hai! Aap prompt likhein "A photo of a Lahori samosa" aur CLIP lakhon images mein se samosa dhoond kar nikal lega!',
  'Understand OpenAI CLIP''s contrastive learning objective (InfoNCE), dual-encoder architecture, shared vector embedding space, and zero-shot visual classification.',
  'import torch
import torch.nn.functional as F

def clip_contrastive_loss(image_embeddings: torch.Tensor, text_embeddings: torch.Tensor, temperature: float = 0.07):
    """Calculates symmetric CLIP contrastive InfoNCE loss across a batch of N pairs."""
    # 1. Normalize embeddings to unit hypersphere
    image_norm = F.normalize(image_embeddings, p=2, dim=-1)
    text_norm = F.normalize(text_embeddings, p=2, dim=-1)
    
    # 2. Compute cosine similarity matrix (N x N) scaled by temperature
    logits = torch.matmul(image_norm, text_norm.t()) / temperature
    
    # 3. Ground truth targets: Diagonal elements (i == j)
    labels = torch.arange(len(image_embeddings), device=image_embeddings.device)
    
    # 4. Symmetric cross-entropy loss (Image-to-Text and Text-to-Image)
    loss_img = F.cross_entropy(logits, labels)
    loss_txt = F.cross_entropy(logits.t(), labels)
    return (loss_img + loss_txt) / 2.0

# Batch of 4 images and 4 matching text captions
img_vecs = torch.randn(4, 512)
txt_vecs = torch.randn(4, 512)
loss = clip_contrastive_loss(img_vecs, txt_vecs)
print(f"Computed CLIP Contrastive Loss: {loss.item():.4f}")',
  '@preset midnight
@animate flow
flow LR: CLIP Joint Contrastive Embedding Space
  img[Image Input] $browser -> img_enc[Vision Encoder ViT] $cpu
  txt[Text Caption] $terminal -> txt_enc[Text Encoder Transformer] $cpu
  img_enc -> img_vec[Normalized Image Vector I] $layers
  txt_enc -> txt_vec[Normalized Text Vector T] $layers
  img_vec & txt_vec -> mat[N x N Cosine Similarity Matrix] $database *
  mat -> loss[InfoNCE Loss: Maximize Diagonal Matches] $brain',
  'flow',
  '[{"title": "CLIP Paper (Radford et al., 2021)", "url": "https://arxiv.org/abs/2103.00020"}, {"title": "OpenCLIP Implementation", "url": "https://github.com/mlfoundations/open_clip"}]'::jsonb,
  25,
  1
from public.modules m
where m.slug = 'multimodal-ai-and-vision'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '12.2',
  'cross-attention-projectors-siglip',
  'Vision Encoders & Projectors: SigLIP & Modern VLM Architecture',
  35,
  'theory_and_code',
  'So guys, modern Vision-Language Models (jaise LLaVA, Qwen2-VL, aur Gemini) CLIP ke dual encoders se aage nikal chuke hain. Wo images ko sirf classify nahi karte balki images ke baare mein insani rawani ke sath guftagu karte hain!

Modern VLM ka architecture teen ahem hisson par mushtamil hota hai:
1. **Vision Encoder (SigLIP / ViT)**:
   Google ka **SigLIP (Sigmoid Loss for Language Image Pre-training)** standard Softmax ki jagah simple pairwise sigmoid loss use karta hai, jis se batch size normalization ki zaroorat khatam ho jati hai aur vision features bohot rich bante hain.
2. **Cross-Modal Projector**:
   Vision encoder image ko 16x16 patches mein tod kar har patch ka vector banata hai (maslan 576 tokens, har token dimension 1024). Lekin LLM ka input dimension 4096 hota hai!
   Is mismatch ko bridge karne ke liye ek **Projector** (2-layer MLP with GELU activation) use hota hai jo image tokens ko LLM ke text embedding space mein translate karta hai!
3. **Autoregressive LLM Backbone**:
   LLM ke liye image tokens bilkul aam text tokens ki tarah ban jate hain! System prompt + Image Tokens + User Query ek single sequence mein concatenate ho kar LLM ke attention blocks se guzar kar answer generate karte hain.',
  'Architect modern Vision-Language Models (VLMs) utilizing SigLIP vision backbones and MLP cross-modal projectors to map 2D image patch tokens directly into LLM embedding space.',
  'import torch
import torch.nn as nn

class VisionProjector(nn.Module):
    """2-Layer MLP Cross-Modal Projector (LLaVA-1.5 Style)."""
    def __init__(self, vision_dim: int = 1024, llm_dim: int = 4096):
        super().__init__()
        self.linear1 = nn.Linear(vision_dim, llm_dim)
        self.act = nn.GELU()
        self.linear2 = nn.Linear(llm_dim, llm_dim)
        
    def forward(self, visual_tokens: torch.Tensor) -> torch.Tensor:
        # Input shape: [batch, num_patches (e.g. 576), vision_dim]
        # Output shape: [batch, num_patches, llm_dim]
        return self.linear2(self.act(self.linear1(visual_tokens)))

# Simulate 576 image patch tokens coming from SigLIP ViT-SO400M
projector = VisionProjector(vision_dim=1024, llm_dim=4096)
raw_patches = torch.randn(1, 576, 1024)
projected_tokens = projector(raw_patches)

print(f"Raw visual patch tokens: {raw_patches.shape}")
print(f"Projected tokens ready for LLM attention: {projected_tokens.shape}")',
  '@preset midnight
@animate flow
flow LR: Modern VLM (LLaVA) Architecture
  image[Input Image 336x336] $browser -> vit[SigLIP ViT Vision Encoder] $cpu
  vit -> patches[576 Visual Patch Tokens 1024-d] $layers
  patches -> mlp[2-Layer MLP Projector] $server *
  mlp -> llm_tokens[Visual Tokens in 4096-d LLM Space] $database
  prompt[User Prompt: ''Describe chart''] $terminal -> tokenizer[Text Tokenizer] $code
  tokenizer & llm_tokens -> llm[LLM Backbone Llama / Mistral] $brain
  llm -> output[Text Response Stream] $terminal',
  'flow',
  '[{"title": "SigLIP Research Paper", "url": "https://arxiv.org/abs/2303.15343"}, {"title": "LLaVA Architecture Overview", "url": "https://github.com/haotian-liu/LLaVA"}]'::jsonb,
  25,
  2
from public.modules m
where m.slug = 'multimodal-ai-and-vision'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '12.3',
  'document-invoice-ocr-donut',
  'Document & Invoice Intelligence: Visual OCR & Structured Extraction',
  35,
  'theory_and_code',
  'So guys, real-world enterprise applications mein sab se aam problem PDFs, scanned receipts, utility bills, aur complex tabular financial invoices ko parse karna hota hai.

Purana tarika kya tha?
1. Pehle Tesseract OCR se ganda text extract karo (jisme columns aur layout mess up ho jate the).
2. Phir mushkil Regex likho jo har invoice format ke change hone par phat jata tha!

Modern AI approach **OCR-free Visual Document Intelligence** hai (jaise Microsoft Florence-2, Donut, aur Gemini 2.0 Flash):
- Model direct image ke pixels ko dekhta hai.
- Yeh spatial relationships ko samajhta hai (maslan: "Total Amount" ke theek samne ya neechay likha hua number hi total hai chahe koi divider line na ho).
- Direct **Pydantic Structured JSON** output produce karta hai jisme invoice number, line items, tax rate, aur total amounts verified format mein milte hain.',
  'Extract structured data from complex invoices, receipts, and tabular PDFs using end-to-end Visual Document Models without brittle OCR preprocessing.',
  'from pydantic import BaseModel, Field
from typing import List

# 1. Define Strict Pydantic Schema for Invoice Extraction
class LineItem(BaseModel):
    description: str = Field(description="Item name or service rendered")
    quantity: int = Field(description="Quantity purchased")
    unit_price: float = Field(description="Price per unit in PKR or USD")
    total_price: float = Field(description="Total price for this line item")

class InvoiceData(BaseModel):
    invoice_number: str
    vendor_name: str
    issue_date: str
    line_items: List[LineItem]
    subtotal: float
    tax_amount: float
    total_due: float

# In production: Pass image bytes + schema to Gemini 2.0 Flash or Florence-2
sample_extracted = InvoiceData(
    invoice_number="INV-2026-0042",
    vendor_name="Systems Limited Lahore",
    issue_date="2026-10-15",
    line_items=[
        LineItem(description="Cloud GPU Hosting T4", quantity=10, unit_price=1200.0, total_price=12000.0),
        LineItem(description="LLM Inference Setup", quantity=1, unit_price=25000.0, total_price=25000.0)
    ],
    subtotal=37000.0,
    tax_amount=5920.0,
    total_due=42920.0
)

print(sample_extracted.model_dump_json(indent=2))',
  '@preset midnight
@animate flow
flow LR: Document Visual Intelligence Pipeline
  pdf[Scanned PDF / Receipt Image] $browser -> vlm[Visual Document Model Florence-2 / Gemini] $cpu
  vlm -> visual_layout[Spatial Layout & Table Understanding] $layers
  visual_layout -> schema[Pydantic JSON Validation Engine] $lock *
  schema -> clean_json[Structured Validated Invoice JSON] $server',
  'flow',
  '[{"title": "Donut: Document Understanding Transformer", "url": "https://arxiv.org/abs/2111.15664"}, {"title": "Microsoft Florence-2 Vision Foundation Model", "url": "https://huggingface.co/microsoft/Florence-2-large"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'multimodal-ai-and-vision'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '12.4',
  'whisper-speech-audio-llms',
  'Audio & Speech Processing: OpenAI Whisper & Audio-LLM Integrations',
  35,
  'theory_and_code',
  'So guys, audio speech processing mein raw waveform (16,000 samples per second) ko direct neural network mein feed karna bohot inefficient hota hai.

OpenAI ka **Whisper** standard audio pipeline follow karta hai:
1. **Log-Mel Spectrogram**: Audio ko 25-millisecond windows (with 10ms hop length) mein divide karke Fourier Transform (FFT) apply kiya jata hai, aur frequencies ko human ear ki sensitivity (Mel scale, 80 ya 128 channels) par map kiya jata hai.
2. **Audio Encoder**: 2D Mel-spectrogram ko convolutional layers aur Transformer blocks se process karke acoustic representations banata hai.
3. **Autoregressive Text Decoder**: Multi-lingual text tokens predict karta hai with timestamp tokens (`<|0.00|>`, `<|2.40|>`) jo word-level alignments provide karte hain.

Whisper Roman Urdu aur Pakistani accents par bohot shandaar kaam karta hai jab aap initial prompt parameter mein thora context pass karein!',
  'Understand speech-to-text processing using OpenAI Whisper, Log-Mel spectrogram feature extraction, and timestamp alignment tokens for audio-LLM architectures.',
  'import numpy as np

def compute_mock_mel_spectrogram(audio_signal: np.ndarray, num_mel_bins: int = 80) -> np.ndarray:
    """Conceptual representation of transforming 1D audio waveform into 2D Mel Spectrogram."""
    # Window framing: 25ms window, 10ms hop
    hop_length = 160 # 10ms at 16kHz
    num_frames = len(audio_signal) // hop_length
    
    # 2D feature matrix: [Frequency Channels, Time Frames]
    mel_spectrogram = np.random.randn(num_mel_bins, num_frames)
    return mel_spectrogram

# 2 seconds of 16kHz audio waveform
audio = np.random.randn(32000)
mel = compute_mock_mel_spectrogram(audio)

print(f"Input Raw Audio Samples: {len(audio):,}")
print(f"Generated Mel-Spectrogram shape: {mel.shape} (80 mel bins x {mel.shape[1]} time frames)")',
  '@preset midnight
@animate flow
flow LR: Whisper Speech Processing Flow
  raw_wav[1D Audio Waveform 16kHz] $terminal -> stft[Short-Time Fourier Transform FFT] $cpu
  stft -> mel[80-Channel Log-Mel Spectrogram] $layers
  mel -> enc[Whisper Audio Encoder ViT] $server *
  enc -> dec[Autoregressive Decoder + Timestamp Tokens] $brain
  dec -> urdu_txt[Transcribed Roman Urdu Text with Timestamps] $terminal',
  'flow',
  '[{"title": "OpenAI Whisper Paper", "url": "https://arxiv.org/abs/2212.04356"}, {"title": "Hugging Face Whisper Fine-Tuning Guide", "url": "https://huggingface.co/blog/fine-tune-whisper"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'multimodal-ai-and-vision'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '12.5',
  'video-understanding-temporal-attention',
  'Video AI & Temporal Understanding: Keyframe Sampling & Dynamic Attention',
  35,
  'theory_and_code',
  'So guys, video dar-asal static images ka sequence hota hai jo waqt (time dimension) ke sath badalta hai. Agar ek 10 minute ki video 30 frames per second (fps) par ho, to total 18,000 frames bante hain! Agar har frame ko VLM mein bhejenge to context window explode ho jayegi aur hazaron dollars burn honge.

Modern Video AI do intelligent sampling strategies use karti hai:
1. **Scene Change & Keyframe Extraction**: OpenCV ya ffmpeg ke zariye sirf wo frames extract kiye jate hain jahan camera angle ya screen content badalta hai (Color Histogram Differences / Optical Flow thresholding). Aam tor par 1 fps ya 0.5 fps sample rate 95% information retain karti hai.
2. **Temporal Attention**: Video tokens ko 3D grid $(T, H, W)$ mein treat kiya jata hai. Model spatial attention (frame ke andar cheezein) aur temporal attention (frame $t_1$ se $t_2$ ke darmiyan action ka sequence) ko aapas mein correlate karta hai.

Is technique se aap 1-hour lambi lecture videos ya CCTV footage ko digest karke exact second par event dhoond sakte hain!',
  'Process long-form video intelligence using OpenCV keyframe sampling, scene detection, and temporal cross-attention to analyze events across time.',
  'import cv2
import numpy as np

def extract_uniform_keyframes(video_path: str, max_frames: int = 8) -> list:
    """Extracts uniformly spaced keyframes from a video file for VLM processing."""
    # Mocking video frame extraction logic
    total_frames = 1800 # 60 seconds at 30fps
    frame_indices = np.linspace(0, total_frames - 1, max_frames, dtype=int)
    
    extracted_frames = []
    for idx in frame_indices:
        timestamp_sec = idx / 30.0
        # In production: cap.set(cv2.CAP_PROP_POS_FRAMES, idx); ret, frame = cap.read()
        extracted_frames.append({"frame_idx": int(idx), "timestamp_sec": round(timestamp_sec, 2)})
        
    return extracted_frames

frames = extract_uniform_keyframes("lecture_ai_ustaad.mp4", max_frames=6)
for f in frames:
    print(f"Extracted Frame at {f[''timestamp_sec'']}s (Index: {f[''frame_idx'']})")',
  '@preset midnight
@animate flow
flow LR: Video Temporal Sampling Pipeline
  video[Raw Video Stream 30 FPS] $browser -> sampler[Uniform / Scene-Change Sampler] $cpu
  sampler -> frames[Keyframes: 1 FPS (e.g. 10 frames)] $layers
  frames -> temporal_attn[Temporal & Spatial Cross-Attention] $brain *
  temporal_attn -> qa_engine[Timestamp-Grounded Video Q&A] $server',
  'flow',
  '[{"title": "Google VideoPrism Foundation Model", "url": "https://arxiv.org/abs/2402.13217"}, {"title": "OpenCV Video Processing in Python", "url": "https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'multimodal-ai-and-vision'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '12.6',
  'capstone-multimodal-intelligence-engine',
  'Module 12 Capstone: Multimodal Document & Video Intelligence Engine',
  50,
  'project',
  'So guys, congratulations! Aap Module 12 ke Capstone project par pohanch chuke hain. Is capstone mein aap ek unified **Multimodal Intelligence Engine** develop karenge jo text, complex visual documents (diagrams/tables), aur audio recordings teeno ko ek sath ingest aur analyze karega!

Aapka Capstone Architecture:
1. **Visual Document Parser**: Complex technical PDF reports se tables aur flowcharts visually crop karke multimodal embeddings generate karega.
2. **Audio Transcription Layer**: Voice queries ya meeting recordings ko Whisper ke zariye timestamped text mein convert karega.
3. **Cross-Modal Retrieval**: User text ya image prompt bhej sakta hai ("Find me the quarterly revenue chart in this 50-page PDF") aur engine exact visual page crop return karega.
4. **Structured JSON Synthesizer**: Final answer visual grounding (bounding box coordinates) aur verified citations ke sath return karega.
5. **Interactive UI**: Svelte 5 ya Streamlit interface jahan user PDF upload kare, audio record kare, aur live streaming answers visual highlights ke sath dekhe!',
  'Assemble the Module 12 Capstone: a production Multimodal Document and Video Intelligence Engine combining visual table extraction, Whisper audio transcription, and cross-modal retrieval.',
  '# Capstone Multimodal Engine Integration Pipeline
from typing import Dict, Any

class MultimodalIntelligenceEngine:
    def __init__(self):
        print("Multimodal Engine initialized: Vision + Audio + LLM active.")
        
    def process_query(self, text_query: str, visual_asset: str = None, audio_asset: str = None) -> Dict[str, Any]:
        result = {
            "query": text_query,
            "modalities_analyzed": ["text"],
            "findings": []
        }
        
        if visual_asset:
            result["modalities_analyzed"].append("vision")
            result["findings"].append({
                "type": "chart_analysis",
                "extracted_data": {"Q3_Growth": "+24%", "Total_Users": "1.2M"},
                "confidence": 0.96
            })
            
        if audio_asset:
            result["modalities_analyzed"].append("audio")
            result["findings"].append({
                "type": "audio_transcript",
                "speaker": "Mentor",
                "snippet": "AI Ustaad production curriculum graduation complete."
            })
            
        return result

engine = MultimodalIntelligenceEngine()
output = engine.process_query(
    text_query="Summarize financial chart and verified voice note.",
    visual_asset="balance_sheet.png",
    audio_asset="meeting_note.wav"
)
print("Multimodal Engine Output:", output)',
  '@preset midnight
@animate pulse
arch LR: Capstone Multimodal Engine Architecture
  user_inputs[Text + Image PDF + Audio WAV] $browser -> ingest[Multi-Modal Ingestion Gateway] $server
  ingest -> doc_vlm[Visual Document Parser] $layers
  ingest -> audio_whisper[Whisper Speech Engine] $cpu
  doc_vlm & audio_whisper -> fusion[Cross-Modal Context Fusion] $database *
  fusion -> vlm_core[Multimodal Foundation LLM] $brain
  vlm_core -> grounded_out[Visual Grounded Response + Bounding Boxes] $terminal',
  'arch',
  '[{"title": "Gemini Multimodal Ingestion Docs", "url": "https://ai.google.dev/gemini-api/docs/multimodal"}, {"title": "Multimodal Retrieval Augmented Generation (M-RAG)", "url": "https://arxiv.org/abs/2410.08182"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'multimodal-ai-and-vision'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '13.1',
  'llama-cpp-gguf-cpu-optimization',
  'Running AI Locally: llama.cpp, GGUF Formats & CPU Optimization',
  35,
  'theory_and_code',
  'So guys, agar aapke pas koi mehnga Nvidia GPU nahi hai, sirf ek normal 16GB RAM wala laptop hai, to kya aap Llama 3 ya DeepSeek run kar sakte hain? **100% YES!**

Georgi Gerganov ka **llama.cpp** software engineering ki dunya ka masterclass project hai! Yeh pure C/C++ mein likha gaya hai with zero external dependencies.
Iske ahem features:
1. **GGUF (GPT-Generated Unified Format)**:
   Model ke tamam tensors, metadata, tokenizer vocabulary, aur hyper-parameters ek single binary file mein store hote hain. GGUF memory-mapped (`mmap`) hota hai, yaani file load hote hi instant execute hona shuru ho jati hai bina poori RAM occupy kiye!
2. **K-Quants (Q4_K_M, Q5_K_M)**:
   Uniform quantization ki bajaye different tensor layers ko different bit-widths assign karta hai (critical attention layers ko 5-bit ya 6-bit aur baqi weights ko 4-bit) taake minimal RAM mein maximum intelligence mile.
3. **SIMD CPU Vectorization**:
   Modern Intel/AMD CPUs ke AVX2, AVX-512, aur ARM NEON instructions ko direct assembly level par target karta hai, jis se CPU par 15 se 30 tokens/second ki smooth speed milti hai!',
  'Understand Georgi Gerganov''s llama.cpp C/C++ architecture, the unified GGUF binary format, mmap memory management, and AVX-512/ARM NEON vectorization.',
  '# Compiling and Running llama.cpp with Hardware Acceleration
# On Linux / Windows (MSVC or MinGW) with AVX2:
# cmake -B build -DGGML_AVX2=ON && cmake --build build --config Release

# Running Quantized Llama 3.2 3B locally on CPU:
# ./build/bin/llama-cli \
#     -m ./models/Llama-3.2-3B-Instruct-Q4_K_M.gguf \
#     -p "Salam! AI Ustaad par local inference kaise fast hota hai?" \
#     -n 256 \
#     --threads 8 \
#     --temp 0.7

print("llama.cpp CLI configuration verified for low-latency CPU execution!")',
  '@preset midnight
@animate flow
flow LR: llama.cpp Architecture & Memory Mapping
  gguf_file[GGUF Binary File on Disk] $database -> mmap[OS mmap Zero-Copy Virtual Memory] $server
  mmap -> cpu_cores[Multi-Core CPU Threads with AVX-512] $cpu *
  cpu_cores -> simd[SIMD Vectorized Dot Product Kernels] $layers
  simd -> token_stream[Instant Token Stream Output] $terminal',
  'flow',
  '[{"title": "llama.cpp GitHub Repository", "url": "https://github.com/ggerganov/llama.cpp"}, {"title": "GGUF File Format Specification", "url": "https://github.com/ggerganov/ggml/blob/master/docs/gguf.md"}]'::jsonb,
  25,
  1
from public.modules m
where m.slug = 'local-ai-and-edge-devices'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '13.2',
  'ollama-modelfiles-rest-orchestration',
  'Ollama Deep Dive: Custom Modelfiles, Swapping & REST APIs',
  35,
  'theory_and_code',
  'So guys, jabke llama.cpp raw engine hai, **Ollama** ne local AI ko Docker ki tarah aasan aur elegant bana diya hai!

Ollama background mein ek lightweight daemon run karta hai jo localhost port 11434 par OpenAI-compatible REST API expose karta hai.
Ahem capabilities:
1. **The Modelfile**:
   Dockerfiles ki tarah aap custom `Modelfile` likh sakte hain:
   ```dockerfile
   FROM llama3.2:3b
   PARAMETER temperature 0.2
   PARAMETER stop "<|eot_id|>"
   SYSTEM """Aap AI Ustaad ke strict enterprise mentor hain."""
   ```
2. **Dynamic Model Swapping**:
   Ollama automatically models ko VRAM/RAM mein swap in aur swap out karta hai. Jab request aati hai to model load hota hai, aur 5 minute idle rehne par memory release ho jati hai.
3. **Local Embedding API**:
   `/api/embeddings` endpoint se aap bina kisi third-party cost ke local text vectors generate kar sakte hain.',
  'Configure and automate local LLM workflows with Ollama, author custom Modelfiles with system templates, and orchestrate REST API inference.',
  'import requests
import json

def query_local_ollama(prompt: str, model: str = "llama3.2:3b") -> str:
    """Calls local Ollama daemon streaming REST endpoint on localhost:11434."""
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 128
        }
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        data = response.json()
        return data.get("response", "")
    except requests.exceptions.ConnectionError:
        return "Ollama daemon not running. Start with ''ollama serve''."

# Example execution
answer = query_local_ollama("AI Ustaad ka vision kya hai?")
print("Ollama Response:", answer)',
  '@preset midnight
@animate flow
flow LR: Ollama Local Daemon Architecture
  client[Desktop / Web App] $browser -> rest[HTTP REST API localhost:11434] $network
  rest -> daemon[Ollama Background Daemon] $server *
  daemon -> modelfile[Modelfile Config & Template] $code
  daemon -> engine[Embedded llama.cpp Runner] $cpu
  engine -> weights[Cached GGUF Weights in ~/.ollama] $database',
  'flow',
  '[{"title": "Ollama Official Documentation", "url": "https://ollama.com/"}, {"title": "Ollama API Specification", "url": "https://github.com/ollama/ollama/blob/main/docs/api.md"}]'::jsonb,
  25,
  2
from public.modules m
where m.slug = 'local-ai-and-edge-devices'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '13.3',
  'hardware-acceleration-metal-vulkan',
  'Edge Hardware Acceleration: Apple Metal (MPS), Vulkan & ROCm',
  35,
  'theory_and_code',
  'So guys, local inference ko CPU se 10x tez karne ke liye humein edge hardware accelerators (Integrated GPUs aur NPUs) ka faida uthana parta hai.

Teen primary acceleration backends industry standard hain:
1. **Apple Silicon Metal (MPS)**:
   M1, M2, M3, M4 chips par **Unified Memory Architecture (UMA)** hoti hai! CPU aur GPU ek hi high-bandwidth memory pool (100 GB/s se 800 GB/s) share karte hain. Koi PCIe transfer latency nahi hoti! Metal Performance Shaders use karke 70B parameter models Mac Studio par smoothly run hote hain.
2. **Vulkan Cross-Platform**:
   Vulkan ek low-level, high-performance graphics & compute API hai jo har platform (Windows, Linux, Android, Intel iGPU, AMD APU) par GPU compute enable karti hai bina proprietary CUDA drivers ke.
3. **AMD ROCm**:
   AMD Radeon graphics cards par open-source PyTorch aur vLLM execution enable karta hai.',
  'Leverage native hardware acceleration frameworks including Apple Metal Performance Shaders (MPS), cross-platform Vulkan compute, and AMD ROCm for local inference.',
  'import torch

def detect_local_accelerator() -> str:
    """Detects and returns optimal hardware acceleration device for PyTorch inference."""
    if torch.cuda.is_available():
        device_name = torch.cuda.get_device_name(0)
        return f"CUDA Acceleration Active: {device_name}"
    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "Apple Metal Performance Shaders (MPS) Unified Memory Active"
    else:
        num_threads = torch.get_num_threads()
        return f"CPU AVX Vectorized Fallback ({num_threads} threads active)"

status = detect_local_accelerator()
print("Local Hardware Diagnostic:", status)',
  '@preset midnight
@animate pulse
arch LR: Hardware Acceleration Tiers
  app[Inference Engine] $server -> dispatch[Hardware Dispatcher] $layers
  dispatch -- Apple Silicon --> mps[Apple Metal Unified RAM] $cpu *
  dispatch -- Nvidia Hardware --> cuda[CUDA Tensor Cores] $gpu
  dispatch -- AMD / Intel iGPU --> vulkan[Vulkan Compute Pipeline] $chip
  dispatch -- Fallback --> avx[Multi-Core CPU AVX-512] $database',
  'arch',
  '[{"title": "Apple Metal Performance Shaders Docs", "url": "https://developer.apple.com/metal/"}, {"title": "Vulkan Compute Documentation", "url": "https://www.vulkan.org/"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'local-ai-and-edge-devices'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '13.4',
  'in-browser-ai-webgpu',
  'In-Browser Client AI: WebGPU & Transformers.js',
  35,
  'theory_and_code',
  'So guys, socho agar aap ek aisi AI web application banayein jisme aapko backend server ka **ek rupiya bhi na dena pare**, aur user ka data user ke browser se **ek inch bhi bahar na jaye**!

Yeh futuristic architecture ab **WebGPU** aur **Transformers.js (v3)** ke sath 100% possible hai!
WebGPU browser ka modern low-level graphics aur compute standard hai jo WebGL ke muqable mein direct GPU compute shaders execute karta hai.
Iska mechanism:
1. Browser user ke local GPU (Intel, Nvidia, ya Apple M-chip) se direct WebAssembly (Wasm) aur WebGPU interface establish karta hai.
2. ONNX Runtime Web model weights (jaise Phi-3.5-mini, Whisper, ya BGE-embeddings) ko user ke browser cache (IndexedDB) mein download aur cache karta hai.
3. Generation, embedding retrieval, aur sentiment classification poori tarah client-side JavaScript mein execute hoti hai!

Zero server costs, zero API rate limits, aur 100% airtight data privacy!',
  'Run deep learning transformers directly inside client web browsers using WebGPU, ONNX Runtime Web, and Transformers.js with zero server infrastructure costs.',
  '// In-Browser AI with Transformers.js and WebGPU (Client-side JavaScript)
// <script type="module">
// import { pipeline } from ''https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.0.0'';

async function initBrowserAI() {
    console.log("Initializing in-browser text classification on WebGPU...");
    
    // In production web client:
    // const classifier = await pipeline(''sentiment-analysis'', ''Xenova/distilbert-base-uncased-finetuned-sst-2-english'', {
    //     device: ''webgpu''
    // });
    // const output = await classifier(''AI Ustaad makes local edge AI incredibly practical!'');
    // console.log("WebGPU Result:", output);
    
    return { status: "WebGPU pipeline ready", device: "client-side GPU" };
}

initBrowserAI().then(console.log);',
  '@preset midnight
@animate flow
flow LR: In-Browser WebGPU Execution Flow
  browser[User Browser Tab] $browser -> idb[IndexedDB Cached ONNX Weights] $database
  browser -> webgpu[WebGPU Compute Shader API] $cpu *
  webgpu -> gpu[Local Client GPU Hardware] $chip
  gpu -> dom[Direct DOM UI Update: Zero Network Latency] $terminal',
  'flow',
  '[{"title": "Transformers.js Documentation", "url": "https://huggingface.co/docs/transformers.js/index"}, {"title": "WebGPU Fundamentals", "url": "https://webgpufundamentals.org/"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'local-ai-and-edge-devices'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '13.5',
  'edge-ai-jetson-raspberry-pi',
  'Edge AI on Embedded Hardware: Nvidia Jetson & Raspberry Pi NPUs',
  35,
  'theory_and_code',
  'So guys, jab hum AI ko internet se door kisi factory floor, drone, smart camera, ya agricultural farm mein deploy karte hain jahan 4G/WiFi ka nam-o-nishan nahi hota, to humein **Embedded Edge AI** hardware chahiye hota hai.

Do leading embedded computing platforms:
1. **Nvidia Jetson Orin Nano (40-67 TOPS AI Performance)**:
   Jetson ek credit-card size computer hai jisme 1024-core Nvidia Ampere GPU aur Tensor Cores mojood hote hain. Yeh 7-15 Watts power consume karta hai aur 4-bit quantized 7B models ko real-time 20+ tokens/sec par run kar sakta hai!
2. **Raspberry Pi 5 + Raspberry Pi AI Kit (Hailo-8L NPU)**:
   13 TOPS ka dedicated Neural Processing Unit (NPU) jo vision models (YOLOv8, Pose Estimation) ko sirf 2-3 Watts power par 30+ FPS video streams par execute karta hai!

Key challenge: **Thermal Management & Power Throttling**. Edge devices par fan profiles, dynamic voltage scaling, aur model batch size ko tune karna lazmi hota hai taake chip overheat ho kar restart na ho.',
  'Deploy compact quantized models on embedded hardware such as Nvidia Jetson Orin and Raspberry Pi 5 NPUs with strict power, memory, and thermal constraints.',
  '# Monitoring Embedded Jetson Thermals & NPU Power (Python Edge Daemon)
import subprocess
import time

def read_jetson_telemetry() -> dict:
    """Reads Tegrastats or thermal zone on Nvidia Jetson embedded device."""
    try:
        with open("/sys/devices/virtual/thermal/thermal_zone0/temp", "r") as f:
            temp_milli = int(f.read().strip())
            celsius = temp_milli / 1000.0
    except FileNotFoundError:
        celsius = 45.2 # Simulated baseline temperature
        
    return {
        "cpu_temp_celsius": celsius,
        "is_throttled": celsius > 80.0,
        "power_mode": "15W_6CORE_BALANCED"
    }

telemetry = read_jetson_telemetry()
print(f"Edge Device Temperature: {telemetry[''cpu_temp_celsius'']} C | Throttled: {telemetry[''is_throttled'']}")',
  '@preset midnight
@animate flow
flow LR: Embedded Edge AI Pipeline
  sensor[CCTV Camera / Microphone Sensor] $browser -> npu[Hailo-8L NPU / Jetson Orin Tensor Cores] $chip *
  npu -> int4_engine[Quantized INT4 Inference 10W Power] $cpu
  int4_engine -> action[Local GPIO Relay Trigger / Alert] $server
  int4_engine -> log[Local SQLite Storage: 100% Offline] $database',
  'flow',
  '[{"title": "Nvidia Jetson Orin Developer Documentation", "url": "https://developer.nvidia.com/embedded/jetson-orin"}, {"title": "Raspberry Pi AI Kit Overview", "url": "https://www.raspberrypi.com/documentation/accessories/ai-kit.html"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'local-ai-and-edge-devices'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '13.6',
  'capstone-offline-edge-assistant',
  'Module 13 Capstone: 100% Offline Autonomous Edge AI Assistant',
  50,
  'project',
  'So guys, congratulations! Aap Module 13 ke Capstone project par pohanch chuke hain. Is capstone mein aap ek mukammal **100% Offline Autonomous Edge AI Assistant** build karenge jo airplane mode par bhi voice commands sunega, local documents search karega, aur Roman Urdu mein jawab dega!

Aapka Capstone Architecture:
1. **Local Speech-to-Text**: Whisper.cpp ya faster-whisper local CPU par audio stream ko text mein convert karega.
2. **Local Vector Knowledge Base**: ChromaDB ya SQLite-vec local disk par chalegi with sentence-transformers embeddings (all-MiniLM-L6-v2 ya BGE-small).
3. **Local LLM Engine**: Ollama ya llama.cpp ke zariye Llama 3.2 3B (Q4_K_M) local RAM par execute hoga.
4. **Local Text-to-Speech (TTS)**: Piper TTS ya Kokoro local audio synthesizer ke zariye instant voice playback provide karega.
5. **Zero-Network Audit**: Wireshark ya network disconnect karke prove karein ke system bina internet ke 100% functional rehta hai!',
  'Architect and deploy the Module 13 Capstone: a 100% offline, privacy-first Edge AI Assistant combining whisper.cpp speech recognition, local SQLite-vec RAG, and quantized Ollama inference.',
  '# Capstone Offline Assistant Coordinator
class OfflineEdgeAssistant:
    def __init__(self):
        self.device = "Local CPU / Edge Accelerator"
        print("Offline Assistant online: Network connectivity = 0 (Airtight Privacy)")
        
    def execute_voice_turn(self, audio_input_bytes: bytes) -> dict:
        # 1. Local STT (Whisper.cpp)
        transcribed_text = "AI Ustaad platform ke offline safety protocols kya hain?"
        
        # 2. Local Vector Search (SQLite-vec)
        retrieved_snippet = "Offline protocols require zero cloud telemetry and local disk encryption."
        
        # 3. Local LLM Reasoning (llama.cpp)
        answer = "So guys, offline safety protocols ke teht tamam embeddings local SQLite file mein store hoti hain aur koi network packet bahar nahi jata."
        
        return {
            "query": transcribed_text,
            "context": retrieved_snippet,
            "response": answer,
            "offline_verified": True
        }

assistant = OfflineEdgeAssistant()
result = assistant.execute_voice_turn(b"mock_audio_bytes")
print("Offline Assistant Turn Result:", result)',
  '@preset midnight
@animate pulse
arch LR: Capstone Offline Edge Assistant
  mic[Local USB Microphone] $browser -> whisper_cpp[Local Whisper.cpp STT] $cpu
  whisper_cpp -> query[Transcribed Query] $terminal
  query -> local_rag[Local SQLite-vec Database] $database
  query & local_rag -> llama_runner[llama.cpp / Ollama Engine] $server *
  llama_runner -> piper_tts[Local Piper TTS Synthesizer] $chip
  piper_tts -> speaker[Local Audio Speaker Output] $terminal',
  'arch',
  '[{"title": "Whisper.cpp High-Performance C++ Port", "url": "https://github.com/ggerganov/whisper.cpp"}, {"title": "Piper Local Fast Neural TTS", "url": "https://github.com/rhasspy/piper"}]'::jsonb,
  50,
  6
from public.modules m
where m.slug = 'local-ai-and-edge-devices'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '14.1',
  'enterprise-multi-tenant-architecture',
  'Enterprise System Design: Multi-Tenant RLS, Vector Partitioning & Audit',
  35,
  'theory_and_code',
  'So guys, jab aap ek B2B SaaS AI product build karte hain jahan Company A (Bank) aur Company B (Hospital) dono aapka platform use kar rahe hain, to agar Company A ke user ko Company B ke confidential documents ka jawab ghalti se bhi mil gaya, to aapki company par millions dollars ka lawsuit ho sakta hai!

Enterprise Multi-Tenancy ke teen pillars hote hain:
1. **Row-Level Security (RLS)**:
   Database level par har query par automatically `WHERE tenant_id = auth.jwt()->>''tenant_id''` enforce hota hai. Chahe backend application code mein developer `WHERE` clause bhool bhi jaye, database engine kisi doosre tenant ka data return hi nahi kar sakta!
2. **Vector Space Partitioning**:
   pgvector mein har vector index mein `metadata->>''tenant_id''` par HNSW / IVFFlat partial indexes banaye jate hain taake similarity search sirf tenant ke apne documents ke darmiyan execute ho.
3. **Immutable Audit Trails**:
   Har prompt, response, model version, aur data access event ko append-only audit table mein log kiya jata hai for SOC2 and ISO-27001 compliance.',
  'Architect airtight multi-tenant enterprise AI platforms utilizing Supabase Row-Level Security (RLS), partition-isolated vector indexes, and immutable audit logs.',
  '-- Enterprise Multi-Tenant RLS & pgvector Partitioning (PostgreSQL)
-- 1. Enable RLS on vector documents table
ALTER TABLE public.document_embeddings ENABLE ROW LEVEL SECURITY;

-- 2. Strict Tenant Isolation Policy based on JWT claims
CREATE POLICY tenant_isolation_policy ON public.document_embeddings
    FOR ALL
    USING (tenant_id = (current_setting(''request.jwt.claims'', true)::jsonb ->> ''tenant_id'')::uuid)
    WITH CHECK (tenant_id = (current_setting(''request.jwt.claims'', true)::jsonb ->> ''tenant_id'')::uuid);

-- 3. Filtered HNSW Vector Index for blazing-fast isolated search
CREATE INDEX idx_tenant_hnsw_vectors ON public.document_embeddings 
USING hnsw (embedding vector_cosine_ops)
WHERE is_active = true;',
  '@preset midnight
@animate flow
flow LR: Enterprise Multi-Tenant Isolation
  req_a[Tenant A User (Bank)] $browser -> auth[JWT Auth & Tenant Context] $lock
  req_b[Tenant B User (Hospital)] $browser -> auth
  auth -> rls[Postgres Row-Level Security Engine] $server *
  rls -- Partition A --> data_a[Tenant A Isolated Vectors] $database
  rls -- Partition B --> data_b[Tenant B Isolated Vectors] $database',
  'flow',
  '[{"title": "PostgreSQL Row-Level Security Guide", "url": "https://www.postgresql.org/docs/current/ddl-rowsecurity.html"}, {"title": "Multi-Tenancy in Vector Databases", "url": "https://supabase.com/docs/guides/ai"}]'::jsonb,
  25,
  1
from public.modules m
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '14.2',
  'high-availability-circuit-breakers',
  'High Availability & Resilience: Circuit Breakers & Multi-Cloud Fallback',
  35,
  'theory_and_code',
  'So guys, enterprise engineering ka qanoon hai: **"Everything fails, all the time."**
OpenAI ka API down ho sakta hai, Anthropic par rate limit lag sakti hai, ya aapka primary cloud provider network outage face kar sakta hai. Agar aapki system in failures ko gracefully handle nahi karti to aapka 99.9% uptime SLA break ho jayega.

Iska solution **Circuit Breaker Pattern** aur **Multi-Cloud Dynamic Routing** hai:
1. **Three Circuit States**:
   - **CLOSED (Normal)**: Tamam requests primary model provider (jaise vLLM / OpenAI) ko jati hain.
   - **OPEN (Tripped)**: Agar pichli 10 requests mein se 5 fail hon ya latency 3s se zyada ho, to circuit foran OPEN ho jata hai aur primary provider par requests bhejna band ho jata hai!
   - **HALF-OPEN (Recovery)**: Kuch seconds baad circuit kuch probe requests primary ko bhej kar check karta hai; agar pass hon to CLOSED ho jata hai.
2. **Exponential Jitter Backoff**:
   Retry karte waqt uniform delay ki bajaye randomized exponential backoff (`delay = min(max_delay, base * 2^attempt) + random_jitter`) use kiya jata hai taake cascading "thundering herd" problem na bane.',
  'Implement enterprise reliability patterns including Circuit Breakers (Closed/Open/Half-Open), exponential jitter backoff, and automatic multi-cloud provider failover.',
  'import time
import random
from enum import Enum

class CircuitState(Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

class ResilientAIGateway:
    def __init__(self, failure_threshold: int = 3, recovery_time_sec: float = 10.0):
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.recovery_time = recovery_time_sec
        self.last_failure_time = 0
        
    def call_ai_service(self, prompt: str) -> str:
        current_time = time.time()
        
        # Check if OPEN circuit can transition to HALF_OPEN
        if self.state == CircuitState.OPEN:
            if current_time - self.last_failure_time > self.recovery_time:
                self.state = CircuitState.HALF_OPEN
            else:
                # Instant Failover to Secondary Provider (e.g. Groq / Cloudflare)
                return f"[FAILOVER_PROVIDER] Handled via secondary provider: {prompt[:30]}..."
                
        try:
            # Simulate primary call
            return f"[PRIMARY_PROVIDER] Successful response: {prompt[:30]}..."
        except Exception:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
            return "[FAILOVER_PROVIDER] Handled via secondary provider fallback."

gateway = ResilientAIGateway()
print("Circuit Breaker Gateway Status:", gateway.state.value)',
  '@preset midnight
@animate flow
flow LR: Circuit Breaker State Transition
  closed[CLOSED: Normal Traffic] $server -- Failures > Threshold --> open_state[OPEN: Route to Fallover Provider] $shield
  open_state -- Recovery Timeout --> half_open[HALF-OPEN: Test Canary Probe] $layers
  half_open -- Canary Success --> closed *
  half_open -- Canary Fails --> open_state',
  'flow',
  '[{"title": "Martin Fowler: Circuit Breaker Pattern", "url": "https://martinfowler.com/bliki/CircuitBreaker.html"}, {"title": "AWS Architecture Center: Exponential Backoff And Jitter", "url": "https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/"}]'::jsonb,
  25,
  2
from public.modules m
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '14.3',
  'token-metering-stripe-billing',
  'Monetization & Governance: Token Metering & Stripe Usage-Based Billing',
  35,
  'theory_and_code',
  'So guys, agar aapka user bohot lambi videos ya 100-page ke documents summarize karwata hai aur aap us se fixed $10/month charge kar rahe hain, to aapki company kuch hi hafton mein bankrupt ho jayegi!

Modern AI companies ka business model **Usage-Based (Metered) Billing** hota hai:
1. **Accurate Token Metering**:
   Har API response ke baad input tokens aur output tokens ko extract karke Redis TimeSeries ya Postgres mein asynchronously log kiya jata hai.
2. **Stripe Metering API Integration**:
   Stripe ke **Billing Meters** feature ko har ghante customer ka aggregated token count report kiya jata hai (`stripe.billing.meter_events.create`).
3. **Hard & Soft Quotas**:
   Jab customer apne monthly budget (jaise $50) ke 80% par pohanchta hai to automated email notification trigger hoti hai (Soft Limit); 100% par non-critical requests block ho jati hain (Hard Limit) taake runaway bill shocks se bacha ja sake.',
  'Implement precise token metering pipelines and integrate Stripe Usage-Based Billing meters to monetize AI applications sustainably with budget quotas.',
  'import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_mock_key")

def report_token_usage_to_stripe(customer_id: str, input_tokens: int, output_tokens: int):
    """Reports consumed AI tokens to Stripe Usage-Based Billing Meter."""
    total_tokens = input_tokens + output_tokens
    
    # In production with live Stripe API:
    # stripe.billing.MeterEvent.create(
    #     event_name="ai_tokens_consumed",
    #     payload={
    #         "value": str(total_tokens),
    #         "stripe_customer_id": customer_id
    #     }
    # )
    
    cost_estimate_usd = (input_tokens * 0.00000015) + (output_tokens * 0.0000006)
    return {
        "customer_id": customer_id,
        "total_tokens": total_tokens,
        "cost_estimate_usd": round(cost_estimate_usd, 6),
        "status": "reported_to_stripe"
    }

usage = report_token_usage_to_stripe("cus_PK10294", input_tokens=1540, output_tokens=420)
print("Stripe Metering Event:", usage)',
  '@preset midnight
@animate flow
flow LR: Token Metering & Stripe Billing Architecture
  gateway[AI Gateway Response] $server -> counter[Async Token Counter Worker] $cpu
  counter -> db[PostgreSQL Token Ledger] $database
  counter -> stripe[Stripe Billing Meter API] $dollar *
  stripe -> invoice[Monthly Usage-Based End Customer Invoice] $chart',
  'flow',
  '[{"title": "Stripe Usage-Based Metered Billing Docs", "url": "https://stripe.com/docs/billing/subscriptions/usage-based"}, {"title": "Managing LLM Costs & Quotas", "url": "https://www.datadoghq.com/blog/llm-cost-management/"}]'::jsonb,
  25,
  3
from public.modules m
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '14.4',
  'packaging-open-source-helm-docker',
  'Packaging & Distribution: Multi-Stage Docker & Helm Charts',
  35,
  'theory_and_code',
  'So guys, jab aapka AI system local machine par chal raha hota hai to "It works on my machine!" kehna kafi nahi hota. Production deployment ke liye containerization aur automated packaging lazmi hai.

1. **Multi-Stage Docker Builds**:
   PyTorch aur CUDA libraries bohot bari hoti hain (single image 6GB se 10GB ki ban jati hai!).
   Multi-stage build mein pehla stage (Builder) dependencies compile karta hai, aur final stage (Runtime) sirf zaroori compiled artifacts copy karta hai. Nateeja? Container image size **70% chota** ho jata hai, attack surface reduce hoti hai, aur deploy speed 4x fast hoti hai!
2. **Kubernetes Helm Charts**:
   Poore platform (Frontend, Backend, Redis, Vector DB, KEDA Autoscaler) ko ek single configurable Helm chart package (`values.yaml`) mein define kiya jata hai taake enterprise client ek command `helm install ai-ustaad ./chart` se poora stack deploy kar sake!',
  'Package enterprise AI microservices with multi-stage Docker builds to slash container footprint and define declarative Kubernetes Helm charts for one-click deployment.',
  '# Multi-Stage Dockerfile for High-Performance AI Gateway
# Stage 1: Build stage with compiler toolchain
FROM rust:1.80-slim as builder
WORKDIR /app
COPY Cargo.toml Cargo.lock ./
COPY src ./src
RUN cargo build --release

# Stage 2: Minimal Distroless / Debian Runtime
FROM debian:bookworm-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/target/release/ai_gateway /app/ai_gateway

EXPOSE 8080
USER 1001
CMD ["/app/ai_gateway"]',
  '@preset midnight
@animate flow
flow LR: Multi-Stage Docker Optimization
  heavy[Stage 1: Heavy Build Environment 3.5GB (Compilers + SDKs)] $layers -> compile[Compile Binary] $cpu
  compile -> light[Stage 2: Slim Runtime Environment 95MB (Zero Bloat)] $server *
  light -> registry[Deploy to Docker Hub / Cloudflare] $cloud',
  'flow',
  '[{"title": "Docker Multi-Stage Builds Documentation", "url": "https://docs.docker.com/build/building/multi-stage/"}, {"title": "Helm: The Kubernetes Package Manager", "url": "https://helm.sh/docs/"}]'::jsonb,
  25,
  4
from public.modules m
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '14.5',
  'ai-career-portfolio-stardom',
  'AI Career Launch: Viral Demos, Technical Whitepapers & GitHub Stardom',
  35,
  'theory_and_code',
  'So guys, aapne 20 hafton mein duniya ke sab se advanced AI concepts seekh liye hain. Lekin agar duniya ko aapke kaam ka pata hi nahi chalega to aapko top global AI companies (San Francisco, London, Dubai) se remote offers kaise milenge?

Aapko apna **Proof of Work** show karna hai:
1. **The Viral 60-Second Video Demo**:
   Log lambe text nahi parhte! Twitter (X) aur LinkedIn par apne Capstone ka ek 60-second crisp screen recording post karein jisme real-time token streaming, diagram visual grounding, aur speed demonstrate ho rahi ho.
2. **The Architecture Whitepaper**:
   Apne GitHub repo ke README mein clear DiagramKit architecture diagrams, benchmark graphs (Latency P99, Throughput comparison), aur design trade-offs document karein.
3. **Open-Source Contribution Blueprint**:
   Popular AI repos (vLLM, Unsloth, Langfuse, LiteLLM) mein bug fixes aur documentation PRs submit karein. Yeh GitHub profile ko global recruiters ki nazar mein golden bana deta hai!',
  'Position your AI Engineering profile globally with high-impact 60-second video demos, rigorous technical architecture READMEs, and open-source contributions.',
  '# GitHub Repository README Blueprint for Top AI Projects
# # Enterprise Multimodal RAG with ColPali & vLLM
# 
# [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# [![Docker Pulls](https://img.shields.io/badge/docker-ready-blue.svg)](https://hub.docker.com/)
# 
# ## 🚀 Architecture Overview
# Built with Rust Axum, vLLM PagedAttention, and Supabase pgvector.
# 
# ## 📊 Benchmarks
# - **Throughput**: 450 tokens/sec on single Nvidia L4
# - **P99 Latency**: 42ms TTFT (Time to First Token)
# - **Test Coverage**: 94% with DeepEval CI gates
# 
# ## 🛠️ Quickstart
# ```bash
# docker compose up -d
# curl -N http://localhost:8080/v1/chat/stream -d ''{"prompt": "Hello"}''
# ```

print("README template validated for high-impact developer branding!")',
  '@preset midnight
@animate flow
flow LR: AI Engineering Career Funnel
  repo[GitHub Open Source Repository] $code -> demo[60s X / LinkedIn Video Demo] $browser
  demo -> whitepaper[Technical Architecture Whitepaper] $database
  whitepaper -> interview[Global Remote Interview Offers ($100k-$180k)] $server *',
  'flow',
  '[{"title": "How to Build a World-Class Developer Portfolio", "url": "https://github.com/readme/guides"}, {"title": "Open Source Contribution Guide", "url": "https://opensource.guide/how-to-contribute/"}]'::jsonb,
  25,
  5
from public.modules m
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;

insert into public.lessons (
  module_id, lesson_code, slug, title, duration_minutes,
  lesson_type, roman_urdu_content, english_summary, code_example,
  diagram_script, diagram_type, resources, xp_reward, order_index
)
select
  m.id,
  '14.6',
  'grand-capstone-defense-graduation',
  'Grand Capstone Defense: Enterprise AI Platform Graduation',
  60,
  'project',
  'So guys, TAMAM AI USTAAD FELLOWS KO MUBARAK HO! Aap curriculum ke aakhri aur sab se azeem marhalay par pohanch chuke hain: **The Grand Capstone Defense & Graduation**!

Aapne Python aur tensors ki pehli line se le kar Transformers, Deep Learning, Modern Hybrid RAG, Autonomous Multi-Agent Swarms, LoRA fine-tuning, DeepSeek-R1 GRPO, vLLM PagedAttention, aur Multi-Tenant Cloud Architecture tak ka 20-hafton ka safar tay kiya hai.

Aapka Final Graduation Criteria:
1. **Live Production Deployment**: Ek live public URL (jaise `https://your-capstone.pages.dev`) jahan platform active aur testable ho.
2. **Complete Full-Stack Architecture**:
   - Modern Svelte 5 / Next.js UI with real-time SSE token streaming.
   - Rust Axum ya FastAPI resilient gateway with rate-limiting.
   - Supabase Postgres with pgvector, Row-Level Security (RLS) aur audit logs.
   - NeMo Guardrails aur Presidio safety filters.
   - Distributed telemetry dashboard (Langfuse / Prometheus).
3. **Defense Presentation**: 10-minute video presentation jisme aap architecture decisions, latency trade-offs, aur edge case handling explain karein.

Jab aap yeh defense submit karenge to aapko **Official AI Ustaad Graduate Badge (🎓)** aur Certificate of Engineering Mastery se nawaza jayega!',
  'Deliver your Grand Capstone Defense: demonstrate a live multi-tenant enterprise AI system with streaming UI, Rust gateway, RLS vector storage, and safety guardrails to graduate.',
  '# Final AI Ustaad Platform Graduation Verification Script
def verify_graduation_readiness(checklist: dict) -> bool:
    print("AI USTAAD — ENGINEERING MASTERY GRADUATION AUDIT")
    print("=" * 55)
    all_passed = True
    for requirement, status in checklist.items():
        symbol = "✅" if status else "❌"
        print(f"{symbol} {requirement}")
        if not status:
            all_passed = False
            
    print("=" * 55)
    if all_passed:
        print("CONGRATULATIONS! You have mastered the complete AI curriculum.")
        print("Awarded: [AI Graduate Badge 🎓] | Status: PRODUCTION READY")
    else:
        print("Please resolve missing items before final graduation defense.")
    return all_passed

audit = {
    "Live Production Endpoint Deployed": True,
    "Multi-Tenant RLS & Vector Partitioning": True,
    "Real-Time SSE Streaming Gateway Active": True,
    "Enterprise Safety Rails & PII Redaction": True,
    "OpenTelemetry Distributed Tracing Configured": True,
    "Automated CI/CD Evaluation Tests Passing": True
}

verify_graduation_readiness(audit)',
  '@preset midnight
@animate pulse
arch LR: The Complete AI Ustaad Full-Stack Universe
  learner[Zero: Eager Student] $terminal -> p1[Phase 1: Foundations] $code
  p1 -> p2[Phase 2: Core ML & Deep Learning] $layers
  p2 -> p3[Phase 3: Modern GenAI & RAG] $database
  p3 -> p4[Phase 4: Fine-Tuning & MLOps] $cpu
  p4 -> p5[Phase 5: Specialization & Enterprise] $server *
  p5 -> hero[Hero: Production AI Engineer 🎓] $cloud',
  'arch',
  '[{"title": "AI Ustaad Official Platform", "url": "https://ai-ustaad.pages.dev"}, {"title": "Global AI Engineering Community", "url": "https://github.com"}]'::jsonb,
  100,
  6
from public.modules m
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (slug) do update set
  lesson_code = excluded.lesson_code,
  title = excluded.title,
  duration_minutes = excluded.duration_minutes,
  lesson_type = excluded.lesson_type,
  roman_urdu_content = excluded.roman_urdu_content,
  english_summary = excluded.english_summary,
  code_example = excluded.code_example,
  diagram_script = excluded.diagram_script,
  diagram_type = excluded.diagram_type,
  resources = excluded.resources,
  xp_reward = excluded.xp_reward,
  order_index = excluded.order_index;


-- 8. QUIZZES & QUESTIONS
delete from public.quiz_questions;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 0 Quiz: Python Foundations & Data Structures', 70, 25
from public.modules m
where m.slug = 'python-zero-se-hero'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'Python mein Mutable aur Immutable data types mein bunyadi farq kya hota hai?',
  '["Lists aur Dictionaries mutable hain jabke Tuples aur Strings immutable hain", "Tamam Python data types mutable hoti hain", "Numbers mutable hote hain lekin Lists immutable", "Python mein types compile-time par fix ho jati hain"]'::jsonb,
  0,
  'Python mein Lists, Sets aur Dictionaries mutable hain (unhe in-place modify kiya ja sakta hai), jabke Tuples, Integers, Floats aur Strings immutable hain (unhe in-place modify nahi kiya ja sakta, naya object banta hai).'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'python-zero-se-hero'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Classes mein `@dataclass(slots=True)` use karne ka sab se bara faida kya hota hai?',
  '["Yeh dynamic `__dict__` overhead ko eliminate karke memory 20-30% save karta hai aur attribute lookup fast karta hai", "Yeh class ko automatic PyTorch model bana deta hai", "Yeh Python code ko Rust mein convert kar deta hai", "Is se class mein methods add nahi kiye ja sakte"]'::jsonb,
  0,
  '`slots=True` define karne se Python instance ke liye dictionary allocate karne ke bajaye fixed-size C array use karta hai, jisse memory usage kam hoti hai aur attribute access tez hota hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'python-zero-se-hero'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'Expression `[x**2 for x in [1, 2, 3, 4] if x % 2 == 0]` ka final result kya hoga?',
  '["[4, 16]", "[1, 9]", "[1, 4, 9, 16]", "[2, 4]"]'::jsonb,
  0,
  'Yeh list comprehension sirf even numbers (2 aur 4) ko filter karti hai (`if x % 2 == 0`) aur unka square (2**2 = 4, 4**2 = 16) generate karti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'python-zero-se-hero'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'Functions mein `*args` aur `**kwargs` ka kya maqsad hota hai?',
  '["`*args` positional arguments ko tuple mein aur `**kwargs` keyword arguments ko dictionary mein collect karta hai", "`*args` sirf float numbers accept karta hai", "`**kwargs` function ko asynchronous worker bana deta hai", "Dono reserved keywords hain jo execute nahi ho sakte"]'::jsonb,
  0,
  '`*args` (non-keyword arguments) ko tuple ke taur par aur `**kwargs` (keyword arguments) ko key-value pairs wali dictionary ke taur par function ke andar pass karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'python-zero-se-hero'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'JSON serialization ke waqt `json.dumps()` aur `json.dump()` mein kya farq hai?',
  '["`json.dumps()` Python data ko string mein convert karta hai jabke `json.dump()` file handle mein write karta hai", "`json.dumps()` database mein query execute karta hai", "`json.dump()` sirf lists ke liye valid hai", "Dono bilkul same function ke alias hain"]'::jsonb,
  0,
  '`dumps` ka ''s'' String ke liye hai (serializes object to a JSON formatted str), jabke `dump()` pehla argument data aur doosra argument open file stream leta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'python-zero-se-hero'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 1 Quiz: Python & Linear Algebra Check', 70, 25
from public.modules m
where m.slug = 'python-for-ai-and-fast-math'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'NumPy mein Vectorized operations pure Python loops ke muqable mein kyun 50x se 100x tez hote hain?',
  '["NumPy ke arrays C-contiguous memory blocks mein hote hain aur CPU SIMD instructions use karte hain", "Python loops memory use nahi karte", "NumPy hamesha GPU par run hota hai chahe CUDA na ho", "NumPy code string format mein execute hota hai"]'::jsonb,
  0,
  'NumPy ke arrays C-contiguous memory blocks mein hote hain aur modern CPU SIMD (Single Instruction Multiple Data) registers ka faida uthate hain, jabke Python loops mein har element generic object hota hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'python-for-ai-and-fast-math'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Agar do vectors u aur v ka Dot Product 0 ho, to iska geometrical matlab kya hai?',
  '["Dono vectors bilkul identical hain", "Dono vectors aapas mein 90 degree (orthogonal/perpendicular) hain", "Dono vectors opposite directions mein hain", "Dono vectors ki length zero hai"]'::jsonb,
  1,
  'Dot product formula u . v = |u| |v| cos(theta) hota hai. Jab angle 90 degree hota hai to cos(90) = 0, yaani dono vectors ek doosre se bilkul unrelated (orthogonal) hain.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'python-for-ai-and-fast-math'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'Gradient Descent optimization mein Learning Rate parameter bohot zyada bara (high) rakhne se kya nuqsan ho sakta hai?',
  '["Training foran 1 step mein complete ho jayegi", "Model loss surface ke minimum ko overshoot kar dega aur loss diverge ho jayega", "GPU memory full ho jayegi", "Code syntax error de dega"]'::jsonb,
  1,
  'Bohot bara learning rate rakhne se parameters itni bari jump lagate hain ke wo minimum valley ko cross karke doosri taraf nikal jate hain aur loss function diverge (infinity ki taraf) ho jata hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'python-for-ai-and-fast-math'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'Matrix Multiplication A @ B execute hone ke liye konsi mathematical shart lazmi hai?',
  '["Dono matrices ka shape bilkul identical hona chahiye", "Matrix A ke columns ki tadaad Matrix B ki rows ki tadaad ke barabar honi chahiye", "Dono matrices square matrices honi chahiye", "Matrix A ke elements positive hone chahiye"]'::jsonb,
  1,
  'Agar Matrix A ka dimension (m x k) ho, to Matrix B ka dimension lazmi (k x n) hona chahiye, taake inner dimension k match kare aur result (m x n) bane.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'python-for-ai-and-fast-math'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Eigenvalues aur Eigenvectors ka geometrical matlab kya hota hai?',
  '["Transformation ke baad vector ki direction change nahi hoti, sirf scale (stretch ya shrink) hota hai", "Vector hamesha 180 degree flip ho jata hai", "Vector ki length hamesha zero ho jati hai", "Matrix determinant zero ho jata hai"]'::jsonb,
  0,
  'A * v = lambda * v formula ke mutabiq, eigenvector v par matrix A multiply karne se uski direction wahi rehti hai, sirf magnitude eigenvalue lambda se scale hota hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'python-for-ai-and-fast-math'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 2 Quiz: Prompt Engineering & LLM Architecture', 70, 25
from public.modules m
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'LLM generation ke waqt Temperature parameter ko 0.0 par set karne ka kya asar hota hai?',
  '["Model bilkul random answers dega", "Model hamesha highest probability wala token select karega (Greedy search/deterministic output)", "Model ka context window 0 ho jayega", "Model internet se live data fetch karega"]'::jsonb,
  1,
  'Temperature 0.0 softmax distribution ko sharpest kar deta hai jis se model hamesha sab se high probability token pick karta hai, deterministic aur consistent ban jata hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Chain-of-Thought (CoT) prompting complex reasoning tasks mein direct prompting se behtar kyun perform karti hai?',
  '["CoT prompt model ko tokens generate karne ka waqt deta hai jisse intermediate computational steps execute hote hain", "CoT se model ki training dubara shuru ho jati hai", "CoT prompt sirf English mein kaam karta hai", "CoT prompt token limit ko double kar deta hai"]'::jsonb,
  0,
  'LLM ka computational budget directly generated tokens par depend karta hai. CoT model ko intermediate reasoning tokens generate karne par majboor karta hai jo final answer ke liye computation provide karte hain.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'System Prompt aur User Prompt mein Bunyadi farq kya hota hai?',
  '["System prompt developer define karta hai jo model ka persona aur safety rules set karta hai, jabke user prompt end-user ki query hoti hai", "System prompt sirf database mein save hota hai", "System prompt hamesha user prompt ke baad execute hota hai", "Dono bilkul aik jaisi cheez hain koi farq nahi"]'::jsonb,
  0,
  'System prompt model ko guiding instructions, persona, constraints aur guardrails provide karta hai, jabke user prompt run-time query hoti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'Few-Shot Prompting mein kya technique use ki jati hai?',
  '["Model ko prompt ke andar hi 2 se 5 concrete input-output examples provide ki jati hain", "Model ko fine-tune kiya jata hai", "Prompt ko 5 dafa repeat kiya jata hai", "Model ke weights change kiye jate hain"]'::jsonb,
  0,
  'Few-shot prompting mein prompt ke context ke andar hi real examples di jati hain taake model pattern, output format aur style ko in-context learn kar sake.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Agar LLM Context Window limit (jaise 8k ya 32k tokens) exhaust ho jaye to kya hota hai?',
  '["Pehle wale conversation tokens truncate ho jate hain aur model unhe bhool jata hai", "Server physically restart ho jata hai", "API automatically temperature barha deti hai", "Output hamesha blank aata hai"]'::jsonb,
  0,
  'Context window exceed hone par shuru ke tokens attention mechanism se bahar nikal jate hain jis se model pehle di gayi context details bhool jata hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'prompt-engineering-and-llm-mental-models'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 3 Quiz: Classical ML & Scikit-Learn', 70, 25
from public.modules m
where m.slug = 'classical-machine-learning'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'Machine Learning model mein Overfitting ka sab se bara symptom kya hota hai?',
  '["Training data par bohot high accuracy (e.g. 99%) lekin Test/Validation data par bohot kharab accuracy", "Model training hi na ho", "Training data aur Test data dono par 50% accuracy", "Model ka file size bohot chota ho jana"]'::jsonb,
  0,
  'Overfitting tab hoti hai jab model training data ke noise ko ratta laga leta hai, jis se unseen test data par generalization fail ho jati hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'classical-machine-learning'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Random Forest algorithm kis ensemble technique par mabni hota hai?',
  '["Bagging (Bootstrap Aggregating) of multiple Decision Trees", "Single Linear Regression", "Deep Convolutional Neural Network", "K-Means Clustering"]'::jsonb,
  0,
  'Random Forest multiple decision trees ko data ke random subsets (bootstrap) par train karta hai aur unki predictions ka average ya majority vote leta hai (Bagging).'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'classical-machine-learning'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'L1 Regularization (Lasso) aur L2 Regularization (Ridge) mein sab se ahem farq kya hai?',
  '["L1 regularization non-important feature weights ko exactly ZERO kar deti hai (feature selection)", "L2 regularization weights ko zero karti hai", "L1 sirf classification mein use hoti hai", "L2 mein training fast hoti hai"]'::jsonb,
  0,
  'L1 penalty |w| gradients ko zero par push karti hai jis se sparse weights bante hain aur feature selection ho jati hai, jabke L2 penalty w^2 weights ko chota karti hai lekin zero nahi karti.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'classical-machine-learning'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'Medical Diagnosis jaise sensitive tasks mein Precision vs Recall mein se kis metric ko prioritize kiya jata hai?',
  '["Recall ko, taake koi bhi bimaar mareez miss na ho (False Negatives minimize hon)", "Precision ko, taake healthy mareez ko test na karna pare", "Sirf Accuracy ko", "Sirf training time ko"]'::jsonb,
  0,
  'Medical diagnosis mein False Negative khatarnak hota hai (bimaar ko healthy keh dena), is liye High Recall lazmi hoti hai taake tamam actual positive cases catch hon.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'classical-machine-learning'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Distance-based algorithms (jaise KNN aur SVM) mein Feature Scaling (StandardScaler) kyun zaroori hoti hai?',
  '["Taake bare scale wale features (jaise Salary 100,000) chote scale wale features (jaise Age 25) ko Euclidean distance mein overpower na karein", "Data ko encrypt karne ke liye", "Python errors prevent karne ke liye", "Dataset ka size chota karne ke liye"]'::jsonb,
  0,
  'Euclidean distance direct numerical values par depend karti hai. Agar features normalize na hon to bara magnitude wala feature distance metric ko mukammal dominate kar leta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'classical-machine-learning'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 4 Quiz: PyTorch Tensors & Neural Networks', 70, 25
from public.modules m
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'Neural Networks mein Activation Functions (jaise ReLU, GELU) add karna kyun lazmi hai?',
  '["Non-linearity introduce karne ke liye, warna kitni bhi layers hon network ek simple linear regression ban kar reh jata hai", "Memory consumption kam karne ke liye", "Weights ko initialize karne ke liye", "Data ko shuffle karne ke liye"]'::jsonb,
  0,
  'Agar non-linear activations na hon to W2 * (W1 * x) = (W2 * W1) * x = W_combined * x ban jata hai, yaani 100 layers bhi ek single linear transformation ban jati hain.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'PyTorch training loop mein `optimizer.zero_grad()` call karna kyun zaroori hota hai?',
  '["Kyunke PyTorch by default gradients ko accumulate (add) karta hai, is liye har naye batch se pehle purane gradients clear karna lazmi hai", "Weights ko reset karne ke liye", "Learning rate ko zero karne ke liye", "Loss function ko initialize karne ke liye"]'::jsonb,
  0,
  'PyTorch mein `.backward()` previous gradients mein naye gradients add karta hai. Agar `.zero_grad()` na karein to multiple batches ke gradients jama ho kar weights ko corrupt kar denge.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'PyTorch mein `loss.backward()` method ka asal function kya hota hai?',
  '["Autograd computation graph ke zariye chain rule apply karke tamam trainable parameters ke gradients compute karna", "Loss ki value print karna", "Model ko save karna", "Weights ko update karna"]'::jsonb,
  0,
  '`.backward()` reverse-mode automatic differentiation (backpropagation) execute karta hai aur har parameter ke `.grad` attribute mein gradient store karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'Deep Sigmoid networks mein Vanishing Gradient Problem kyun paida hoti hai?',
  '["Sigmoid derivative ka maximum value sirf 0.25 hota hai, deep layers mein multiply hote hote gradients zero ke qareeb pohanch jate hain", "Sigmoid memory leak karta hai", "Weights negative ho jate hain", "Learning rate zero ho jati hai"]'::jsonb,
  0,
  'Sigmoid derivative hamesha 0 aur 0.25 ke darmiyan hota hai. 10 layers mein 0.25^10 = 0.00000095 ban jata hai, jis se initial layers ke weights train hona band ho jate hain.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Training ke doran `Dropout` layer neural network mein kya function perform karti hai?',
  '["Randomly neurons ki activations ko zero kar deti hai taake neurons ek doosre par co-dependent na hon aur overfitting reduce ho", "Corrupt data rows ko drop karti hai", "Memory release karti hai", "Model ki speed 2x karti hai"]'::jsonb,
  0,
  'Dropout regularizer hai jo training ke waqt randomly (e.g. 20% ya 50% probability par) neurons deactivate karta hai, jis se network robust representations seekhta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'deep-learning-and-pytorch-foundations'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 5 Quiz: Attention & Transformers Mechanics', 70, 30
from public.modules m
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'Self-Attention formula Softmax(Q * K^T / sqrt(d_k)) * V mein sqrt(d_k) se divide kyun kiya jata hai?',
  '["Taake dot product magnitude bohot bara na ho jis se softmax gradients vanish ho jate hain", "Computation speed ko double karne ke liye", "Token length ko truncate karne ke liye", "Matrix ko invertible banane ke liye"]'::jsonb,
  0,
  'Jab dimension d_k bara hota hai to dot product ka variance bara ho jata hai, jis se softmax outputs 0 ya 1 ke bohot qareeb ho jate hain aur gradients vanish ho jate hain. sqrt(d_k) scaling variance ko 1 rakhti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Multi-Head Attention ka single attention head ke muqable mein kya faida hota hai?',
  '["Model aik sath mukhtalif representation subspaces aur positions se information ko attend kar sakta hai (e.g. syntax, semantics, grammar)", "Parameters 50% kam ho jate hain", "Model ki inference latency zero ho jati hai", "Transformers ko positional embeddings ki zaroorat nahi rehti"]'::jsonb,
  0,
  'Multi-head attention multiple independent projections use karta hai, jisse model ek head se subject-verb agreement aur doosre head se pronoun-reference track kar sakta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'Transformer models mein Positional Encoding add karna kyun lazmi hota hai?',
  '["Kyunke Self-Attention mechanism permutation-invariant hota hai; bina positional encoding ke sentence mein lafzon ki tarteeb (order) lost ho jati hai", "Model ke weights ko normalize karne ke liye", "Context window barhane ke liye", "Tokenization speed barhane ke liye"]'::jsonb,
  0,
  'Self-attention operations sets ki tarah order-independent hote hain. ''Billi ne sher ko dekha'' aur ''Sher ne billi ko dekha'' attention ke liye identical honge jab tak positional encoding add na ho.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'Decoder-only models (jaise GPT aur Llama) mein Causal Attention Masking ka kya role hota hai?',
  '["Future tokens ko -infinity mask kar deta hai taake model next token predict karte waqt aane wale tokens ko ''cheat'' na kar sake", "Prompt tokens ko delete kar deta hai", "Gradients ko clip karta hai", "Temperature ko scale karta hai"]'::jsonb,
  0,
  'Autoregressive models mein causal mask upper triangular matrix ko -inf kar deta hai taake softmax ke baad future positions ki attention weight 0 ho.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'LLM generation ke doran KV Cache (Key-Value Cache) use karne ka primary benefit kya hai?',
  '["Pehle generate hone wale tokens ke Key aur Value tensors ko memory mein save rakhta hai taake har naye token par poora context dubara compute na karna pare", "Model ka file size chota kar deta hai", "Training time 10x fast kar deta hai", "Accuracy ko 100% kar deta hai"]'::jsonb,
  0,
  'KV cache bina use kiye N tokens generate karne mein O(N^2) computation lagti hai; KV cache save karne se har naye token par sirf naye token ka KV compute hota hai O(N).'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'attention-and-transformers-under-the-hood'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 6 Quiz: AI APIs & Streaming Architecture', 70, 25
from public.modules m
where m.slug = 'building-ai-applications-and-apis'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'Server-Sent Events (SSE) streaming API endpoints ke liye konsa HTTP Content-Type header lazmi hota hai?',
  '["text/event-stream", "application/json", "multipart/form-data", "application/octet-stream"]'::jsonb,
  0,
  'SSE ke liye `Content-Type: text/event-stream` header lazmi hota hai jo browser client ko batata hai ke HTTP connection open rahega aur data chunks push honge.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'building-ai-applications-and-apis'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Client-side frontend mein AbortController use karne ka sab se bara faida kya hai?',
  '["Jab user ''Stop Generating'' click kare to active HTTP token stream foran abort ho jata hai jis se server aur token resources waste nahi hote", "Network speed double ho jati hai", "Response JSON format mein convert ho jata hai", "Tokens automatically encrypt ho jate hain"]'::jsonb,
  0,
  'AbortController ke `.abort()` signal se in-flight fetch request cancel ho jati hai aur backend stream generator close ho kar compute bacha leta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'building-ai-applications-and-apis'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'AI APIs mein Semantic Caching ka kya maqsad hota hai?',
  '["Agar naya prompt purane cached prompt ke bohot qareeb ho (high cosine similarity) to direct cache se answer return karna bina LLM API call kiye", "Images ko compress karna", "SQL queries ko optimize karna", "User passwords encrypt karna"]'::jsonb,
  0,
  'Semantic cache vector embeddings compare karta hai. ''Pakistan ka capital?'' aur ''Capital of Pakistan?'' par exact string match fail ho jata hai lekin vector cache 0.96 similarity par hit de kar $0 cost par instant answer serve karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'building-ai-applications-and-apis'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'WebSockets aur Server-Sent Events (SSE) mein bunyadi farq kya hai?',
  '["WebSockets full-duplex bidirectional (both ways) hote hain jabke SSE unidirectional (server-to-client) lightweight HTTP/2 stream hota hai", "SSE sirf mobile par chalta hai", "WebSockets JSON support nahi karte", "Dono bilkul identical hain"]'::jsonb,
  0,
  'Text generation streams ke liye SSE behtareen hai kyunke simple HTTP connection use karta hai, jabke complex bidirectional audio/video ya tool chat ke liye WebSockets zaroori hote hain.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'building-ai-applications-and-apis'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Sliding-Window Token Bucket rate limiter API gateway mein kya serve karta hai?',
  '["API ko traffic bursts aur abuse se bachata hai taake downstream LLM quotas exhaust na hon aur fairness maintain rahe", "Prompts ko translate karta hai", "Responses ko grammar check karta hai", "Token size double karta hai"]'::jsonb,
  0,
  'Token bucket rate limiting clients ko defined quota per minute assign karta hai aur DDoS ya excessive script requests ko 429 Too Many Requests status ke sath block karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'building-ai-applications-and-apis'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 7 Quiz: Vector Search & Hybrid RAG', 70, 30
from public.modules m
where m.slug = 'vector-databases-and-modern-rag'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'Hybrid Search mein Dense Retrieval aur Sparse Retrieval ko combine karne ka kya faida hota hai?',
  '["Dense embeddings conceptual meaning capture karti hain jabke Sparse BM25 exact keywords, part numbers aur names match karta hai", "Database ki RAM usage zero ho jati hai", "Chunks ki zaroorat khatam ho jati hai", "Accuracy hamesha 100% ho jati hai"]'::jsonb,
  0,
  'Sirf vector search exact serial numbers (e.g. ''ERR_404_B'') par confuse ho sakti hai. Hybrid search Dense + BM25 ko Reciprocal Rank Fusion (RRF) se combine karke best of both worlds deti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'vector-databases-and-modern-rag'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Cross-Encoder Re-ranker Bi-Encoder ke muqable mein behtar retrieval accuracy kyun deta hai?',
  '["Cross-encoder query aur document tokens ko aik sath full self-attention se compare karta hai", "Cross-encoder 100x fast hota hai", "Cross-encoder vectors store nahi karta", "Cross-encoder memory use nahi karta"]'::jsonb,
  0,
  'Bi-encoders query aur doc ko alag alag embed karte hain (fast candidate retrieval). Cross-encoder top 20 candidates ko query ke sath concatenate karke deep cross-attention se score karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'vector-databases-and-modern-rag'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'Vector databases mein HNSW (Hierarchical Navigable Small World) index ka primary trade-off kya hai?',
  '["Bohot fast sub-millisecond approximate nearest neighbor search milti hai lekin index building time aur RAM consumption zyada hoti hai", "HNSW sirf 100 vectors store kar sakta hai", "HNSW GPU ke baghair nahi chalta", "HNSW mein vectors delete nahi ho sakte"]'::jsonb,
  0,
  'HNSW multi-layer graph structure maintain karta hai jo O(log N) search latency provide karta hai lekin extra graph memory (RAM) demand karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'vector-databases-and-modern-rag'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'ColPali retrieval architecture traditional text OCR chunking ke muqable mein kyun superior hai?',
  '["ColPali PDF pages ki images ko direct multi-vector Vision-Language representations mein index karta hai bina text extract kiye", "ColPali sirf plain text documents read karta hai", "ColPali vector database use nahi karta", "ColPali training time zero karta hai"]'::jsonb,
  0,
  'Complex PDFs mein tables, charts aur layouts OCR mein mess up ho jate hain. ColPali visual embeddings se tables aur graphs ko as-is visually retrieve kar leta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'vector-databases-and-modern-rag'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Text Chunking ke doran Chunks ke darmiyan Chunk Overlap (e.g. 50 tokens) rakhna kyun zaroori hota hai?',
  '["Taake sentences ke darmiyan context split na ho aur boundary ke ahem information pieces lost na hon", "Tokens count kam karne ke liye", "File format maintain karne ke liye", "Speed barhane ke liye"]'::jsonb,
  0,
  'Agar chunk boundary kisi zaroori sentence ke beech mein split ho jaye to dono chunks adhooray ho jate hain. Overlap boundary context ko preserve rakhta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'vector-databases-and-modern-rag'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 8 Quiz: Agents, MCP & Tool Use', 70, 30
from public.modules m
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'ReAct (Reasoning + Acting) Agent framework ka core execution loop kya hota hai?',
  '["Thought -> Action -> Action Input -> Observation -> Next Thought", "Prompt -> Generate -> Exit", "Input -> Database Query -> Output", "Compile -> Run -> Debug"]'::jsonb,
  0,
  'ReAct pattern mein agent pehle sochta hai (Thought), action decide karke tool call karta hai (Action), external world se result leta hai (Observation), aur phir agla step plan karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Anthropic Model Context Protocol (MCP) ka primary maqsad kya hai?',
  '["AI models ko standardized open protocol ke zariye local files, tools, aur databases se connect karna", "Naya transformer model train karna", "CSS styles design karna", "Python package manage karna"]'::jsonb,
  0,
  'MCP ek open universal protocol hai (like USB-C for AI) jo AI models ko tools, prompts aur resources securely expose karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'Multi-Agent Systems mein Supervisor / Router Pattern ka kya function hota hai?',
  '["Ek coordinator agent user intent analyze karke specialized sub-agents (Coder, Researcher, Critic) ko kaam delegate karta hai", "System crash prevent karta hai", "Database backup leta hai", "Token price calculate karta hai"]'::jsonb,
  0,
  'Supervisor pattern divide-and-conquer strategy use karta hai jahan main orchestrator sub-tasks create karta hai aur specialized agents unhe parallel execute karte hain.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'Tool Use mein Function Calling ke waqt JSON Schema validation kyun critical hoti hai?',
  '["Taake LLM se aane wale arguments ka type aur structure verify ho sake aur runtime code execution crashes prevent hon", "Internet traffic kam karne ke liye", "Model ko fast tokenize karne ke liye", "Python syntax highlight karne ke liye"]'::jsonb,
  0,
  'LLM kabhi kabhi invalid keys ya wrong data types generate kar sakta hai. Pydantic / JSON schema validate karke hallucinated parameters ko block karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Autonomous Agent mein Short-Term Memory aur Long-Term Memory mein kya farq hota hai?',
  '["Short-term memory current context window scratchpad mein hoti hai, jabke long-term memory external vector database mein persist hoti hai", "Short-term memory RAM mein hoti hai, long-term memory GPU mein", "Dono identical hoti hain", "Short-term memory expire nahi hoti"]'::jsonb,
  0,
  'Short-term memory current task execution context hoti hai jo session ke baad khatam ho sakti hai; long-term memory previous sessions ka persistent knowledge base hoti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'autonomous-agents-and-tool-use'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 9 Quiz: LoRA, Unsloth & DeepSeek-R1 GRPO', 70, 30
from public.modules m
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'LoRA (Low-Rank Adaptation) mein rank parameter ''r'' (e.g. r=16) ka kya role hota hai?',
  '["Yeh low-rank decomposition matrices A aur B ke inner dimension ko control karta hai, jitna chota r utne kam trainable parameters", "Yeh learning rate ko control karta hai", "Yeh model ke total layers count ko barhata hai", "Yeh GPU temperature ko fix karta hai"]'::jsonb,
  0,
  'LoRA mein Delta W = B * A hota hai jahan A ka shape (r x d_in) aur B ka (d_out x r) hota hai. Rank r matrix compression ka bottleneck dimension hota hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'QLoRA mein NF4 (NormalFloat 4-bit) quantization format standard INT4 se behtar kyun hai?',
  '["Normally distributed weights ke liye mathematically optimal quantile representation provide karta hai with near-zero accuracy loss", "NF4 file size ko double kar deta hai", "NF4 sirf AMD cards par chalta hai", "NF4 training data ko encrypt karta hai"]'::jsonb,
  0,
  'Pre-trained neural network weights zero-mean normal distribution follow karte hain. NF4 quantization bins information theory ke mutabiq zero-loss mapping ensure karte hain.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'SFT (Supervised Fine-Tuning) dataset training ke waqt Loss Masking (-100 label) kyun lagai jati hai?',
  '["Taake loss sirf assistant ke generated response tokens par calculate ho, system aur user prompt tokens par model train na ho", "System prompt ko hide karne ke liye", "Dataset se corrupt characters delete karne ke liye", "GPU memory full hone se bachane ke liye"]'::jsonb,
  0,
  'Model ko user prompt memorize karne par penalize nahi karna chahiye. PyTorch CrossEntropyLoss label -100 ko ignore karta hai, so loss sirf assistant tokens par banti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'Direct Preference Optimization (DPO) traditional PPO RLHF se superior kyun mana jata hai?',
  '["DPO ko separate Reward Model aur complex reinforcement learning loop ki zaroorat nahi hoti, direct policy probabilities se loss compute hoti hai", "DPO sirf 10 parameters train karta hai", "DPO bina GPU ke train hota hai", "DPO training time 10x slow kar deta hai"]'::jsonb,
  0,
  'DPO reward function ko mathematically substitute karke direct reference vs active policy log-likelihood ratios se train karta hai, jis se training crash-proof ban jati hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'DeepSeek-R1 ke GRPO (Group Relative Policy Optimization) mein Critic Model ki jagah kya cheez use hoti hai?',
  '["Har prompt ke multiple sampled completions ka group mean aur standard deviation lekar normalized relative advantage calculate kiya jata hai", "Ek bara 70B model judge banta hai", "Human annotators live scoring karte hain", "Zero reward assign kiya jata hai"]'::jsonb,
  0,
  'GRPO Critic value-network ko eliminate karta hai. Group ke G candidate outputs ke rule-based rewards ka (r - mean) / std compute karke relative advantage derive hota hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'fine-tuning-and-model-adaptation'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 10 Quiz: AI Evals & Safety Guardrails', 70, 30
from public.modules m
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'Ragas evaluation framework mein Faithfulness metric kis cheez ko mathematically measure karta hai?',
  '["Generated answer ke claims kitne accurately retrieved context documents par grounded hain (Zero Hallucination check)", "Answer kitna lamba hai", "User prompt ki grammar check karna", "API call ki latency measure karna"]'::jsonb,
  0,
  'Faithfulness score = (Number of claims in answer supported by context) / (Total claims in answer). 1.0 ka matlab zero hallucination hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'NeMo Guardrails mein Input Rails kis point par execute hoti hain?',
  '["User query ko intercept karti hain aur LLM tak pohanchne se pehle jailbreaks aur malicious patterns block karti hain", "LLM ke answer generate hone ke baad", "Database save hone ke baad", "Client browser band hone par"]'::jsonb,
  0,
  'Input rails gateway par pehli defense hoti hain jo adversarial prompt injections ko LLM inference se pehle hi drop kar deti hain, saving cost and securing the system.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'Microsoft Presidio enterprise AI pipelines mein kya critical role ada karta hai?',
  '["Personally Identifiable Information (PII) jaise CNIC, phone numbers, credit cards ko detect aur anonymize/mask karta hai", "SQL queries generate karta hai", "Images create karta hai", "Model fine-tune karta hai"]'::jsonb,
  0,
  'Presidio sensitive personal details ko cloud LLM par bhejne se pehle replace karta hai (e.g. `<PAK_CNIC>`), ensuring GDPR and regulatory compliance.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'TruLens Groundedness evaluation kis Natural Language Inference (NLI) technique par kaam karta hai?',
  '["Answer ke har sentence ko atomic claims mein split karke context ke sath entailment vs contradiction probability score karta hai", "Word count ratio check karta hai", "Alphabetical sorting karta hai", "Cosine similarity calculate karta hai"]'::jsonb,
  0,
  'TruLens NLI models (jaise DeBERTa) ke zariye check karta hai ke source text se answer logically entail (sabik) hota hai ya neutral/contradictory hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Automated CI/CD Evaluation Gates (DeepEval) software repository mein kyun lagaye jate hain?',
  '["Taake agar naye prompt ya model change se accuracy ya safety benchmarks threshold se drop hon to PR merge automatically block ho jaye", "Docker images delete karne ke liye", "Developer ki salary deduct karne ke liye", "Tests ko skip karne ke liye"]'::jsonb,
  0,
  'DeepEval automated evaluation gates silent quality regressions ko production mein release hone se rokti hain by failing GitHub Actions workflows.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'ai-safety-evals-and-guardrails'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 11 Quiz: vLLM, MLOps & High-Throughput Serving', 70, 30
from public.modules m
where m.slug = 'production-ai-engineering-mlops'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'vLLM serving engine ka PagedAttention algorithm traditional serving se kyun 10x-20x zyada throughput deliver karta hai?',
  '["KV Cache ko contiguous memory mein rakhne ki bajaye non-contiguous virtual memory blocks mein page karta hai, eliminating memory waste and fragmentation", "Model weights ko delete kar deta hai", "Gradients ko zero kar deta hai", "Sirf CPU par run hota hai"]'::jsonb,
  0,
  'PagedAttention operating system ke virtual memory paging concept ko use karta hai. Har request ke liye dynamic blocks allocate hote hain jis se zero VRAM waste hoti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'production-ai-engineering-mlops'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Continuous Batching (Iteration-Level Scheduling) ka static batching ke muqable mein kya faida hai?',
  '["Nayi incoming requests ko purani batch ke mukammal hone ka wait nahi karna parta; har token step par requests dynamically join aur leave kar sakti hain", "Requests hamesha 1 by 1 process hoti hain", "Batch size fixed 1 ho jati hai", "Latency 10x barh jati hai"]'::jsonb,
  0,
  'Static batching mein fast requests ko slow requests ke finish hone ka wait karna parta tha. Continuous batching token-level scheduling se GPU utilization 95%+ rakhti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'production-ai-engineering-mlops'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'AWQ (Activation-aware Weight Quantization) ka fundamental technical insight kya hai?',
  '["Sirf top 1% salient weights jin par activation magnitudes bohot bare hote hain unhe high-precision protect karna aur baqi 99% weights ko 4-bit quantize karna", "Tamam weights ko random round off kar dena", "Weights ko text format mein convert karna", "Attention layers ko delete kar dena"]'::jsonb,
  0,
  'AWQ activations ko observe karke ahem weights identify karta hai aur unhe mathematically scale karke protect karta hai, preserving reasoning accuracy.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'production-ai-engineering-mlops'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'Production LLM Streaming Gateways ke liye Rust Axum framework kyun choose kiya jata hai?',
  '["Tokio async runtime ke zariye bina garbage collector pause ke 10,000+ concurrent SSE streams ko ultra-low CPU aur minimal RAM mein handle kar sakta hai", "Rust mein code likhna Python se simple hota hai", "Rust sirf GPUs par chalta hai", "Rust automatic database banata hai"]'::jsonb,
  0,
  'Rust compile-time memory safety, zero-cost abstractions aur Tokio multi-threaded work-stealing scheduler high-concurrency streaming gateways ke liye industry benchmark hain.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'production-ai-engineering-mlops'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Kubernetes par LLM inference clusters ko autoscale karte waqt KEDA autoscaler kis primary metric par scale out karta hai?',
  '["vLLM Waiting Requests Queue Depth aur KV Cache Usage metrics par", "Standard CPU percentage par", "Disk storage usage par", "Current clock time par"]'::jsonb,
  0,
  'LLMs compute-bound aur memory-bound hote hain. GPU HPA autoscaling waiting queue depth par karni chahiye taake users ko latency spikes na milein.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'production-ai-engineering-mlops'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 12 Quiz: Multimodal AI & Vision-Language Models', 70, 30
from public.modules m
where m.slug = 'multimodal-ai-and-vision'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'OpenAI CLIP training mein InfoNCE Contrastive Loss ka primary objective kya hota hai?',
  '["Matching (Image, Text) pairs ki cosine similarity ko matrix diagonal par maximize karna aur non-matching pairs ko zero ke qareeb push karna", "Images ko 1000 classes mein classify karna", "Images se background remove karna", "Audio signals ko text mein convert karna"]'::jsonb,
  0,
  'CLIP symmetric cross-entropy loss use karta hai jo shared embedding space mein positive image-text pairs ko aapas mein khinchti hai aur negative pairs ko dur karti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'multimodal-ai-and-vision'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Modern VLMs (jaise LLaVA) mein Cross-Modal Projector (MLP) ka kya role hota hai?',
  '["Vision Encoder ke patch tokens ko LLM ke text embedding space (e.g. 1024-d to 4096-d) mein translate aur project karna", "Image ka resolution 4k karna", "Text prompt ko image mein badalna", "Camera focus adjust karna"]'::jsonb,
  0,
  'Projector visual patch features ko LLM ke native token representations mein convert karta hai taake LLM ke attention layers unhe text tokens ki tarah seamlessly process kar sakein.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'multimodal-ai-and-vision'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'Visual Document Models (jaise Florence-2 aur Donut) classical OCR pipelines ke muqable mein kyun behtar hain?',
  '["Direct visual pixels se spatial tables, forms aur layout structure ko Pydantic JSON mein parse karte hain bina brittle text-OCR preprocessing ke", "Bohat zyada CPU memory use karte hain", "Sirf English text read kar sakte hain", "Files ko PDF mein convert karte hain"]'::jsonb,
  0,
  'OCR-free visual document intelligence complex visual layout, dividing lines aur relative positioning ko visually samajh kar high-accuracy structured JSON generate karti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'multimodal-ai-and-vision'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'OpenAI Whisper speech recognition architecture mein raw audio signal ko pehle kis representation mein convert kiya jata hai?',
  '["80-Channel Log-Mel Spectrogram (2D frequency-time representation)", "MP3 compressed audio stream", "Binary bitstream", "RGB pixel matrix"]'::jsonb,
  0,
  'Audio wave ko Short-Time Fourier Transform (STFT) ke zariye human hearing sensitivity (Mel scale) par map kiya jata hai jo 2D Log-Mel spectrogram banata hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'multimodal-ai-and-vision'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Long-form Video Understanding mein Uniform Keyframe Sampling (e.g. 1 frame per second) ka kya faida hai?',
  '["Context window token consumption aur compute costs ko 95% reduce karta hai jabke primary temporal actions aur visual transitions retain rehte hain", "Video ko slow-motion kar deta hai", "Video ka audio mute kar deta hai", "Video ko delete kar deta hai"]'::jsonb,
  0,
  'Har frame bhejenge to 30fps par hazaron redundant frames context window exhaust kar denge. Keyframe sampling critical state changes capture karti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'multimodal-ai-and-vision'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 13 Quiz: Local LLMs, Ollama & Edge Optimization', 70, 30
from public.modules m
where m.slug = 'local-ai-and-edge-devices'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'llama.cpp mein GGUF binary format ka sab se bara faida kya hai?',
  '["Single unified binary file jo OS mmap (memory mapping) ke zariye zero-copy instant load hoti hai aur CPU RAM par direct execute hoti hai", "GGUF sirf Python mein execute hota hai", "GGUF model ko uncompressed rakhta hai", "GGUF file size ko 10x bara kar deta hai"]'::jsonb,
  0,
  'GGUF metadata, vocabulary aur tensors ko single file mein pack karta hai jo memory-mapped I/O ke sath bina initial RAM loading lag ke instant token streaming provide karti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'local-ai-and-edge-devices'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Ollama Modelfile mein persistent persona aur guardrail instructions define karne ke liye konsi command use hoti hai?',
  '["SYSTEM \"\"\"...\"\"\"", "FROM base_model", "PARAMETER temperature 0.7", "TEMPLATE {{ .Prompt }}"]'::jsonb,
  0,
  'Modelfile mein `SYSTEM` command base model ke har conversation session ke liye permanent system prompt aur behavior boundaries enforce karti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'local-ai-and-edge-devices'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'Apple Silicon (M1/M2/M3/M4) chips par LLM inference itni tez kyun hoti hai?',
  '["Unified Memory Architecture (UMA) ki wajah se CPU aur GPU ek hi high-bandwidth memory pool (100GB/s se 800GB/s) zero-copy share karte hain", "Apple devices par models train nahi hote", "Apple chips internet use nahi karte", "Apple chips mein cache memory nahi hoti"]'::jsonb,
  0,
  'Traditional PCs mein PCIe bus par VRAM transfer latency hoti hai. Apple Unified Memory mein weights direct RAM mein rehte hain aur Metal GPU instantly access karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'local-ai-and-edge-devices'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'WebGPU aur Transformers.js ke zariye In-Browser AI chalane ka sab se bara business benefit kya hai?',
  '["Zero backend server compute cost aur 100% airtight data privacy kyunke model direct user ke client browser mein execute hota hai", "Browser ka tab crash ho jata hai", "Client ko Python install karna parta hai", "Internet traffic 10x barh jati hai"]'::jsonb,
  0,
  'Client-side WebGPU execution se SaaS company ko cloud GPU bills pay nahi karne parte aur user ka sensitive data kabhi browser se bahar nahi jata.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'local-ai-and-edge-devices'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Embedded edge hardware (jaise Nvidia Jetson ya Raspberry Pi) par AI deploy karte waqt sab se ahem challenge kya hota hai?',
  '["Strict power limits (e.g. 10W-15W budget) aur thermal throttling management taake device overheat ho kar crash na ho", "Python versions ka match na hona", "Monitor screen ka chota hona", "Keyboard attach na hona"]'::jsonb,
  0,
  'Edge devices cooling aur power limited environments mein operate karte hain. Quantized models aur controlled inference frequencies thermal shutdowns prevent karti hain.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'local-ai-and-edge-devices'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quizzes (module_id, title, passing_score_pct, xp_reward)
select m.id, 'Module 14 Quiz: Enterprise Architecture & Career Capstone', 70, 50
from public.modules m
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (module_id) do update set
  title = excluded.title,
  passing_score_pct = excluded.passing_score_pct,
  xp_reward = excluded.xp_reward;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  1,
  'Enterprise multi-tenant systems mein PostgreSQL Row-Level Security (RLS) kya security guarantee provide karta hai?',
  '["Database engine level par data isolate karta hai; agar application code mein WHERE clause miss bhi ho jaye to tenant kabhi doosre tenant ka data nahi dekh sakta", "Database password encrypt karta hai", "SQL injection ko allow karta hai", "Backups automatically delete karta hai"]'::jsonb,
  0,
  'RLS policies database kernel level par har query par automatically `tenant_id = auth.jwt()->>''tenant_id''` inject karti hain, preventing cross-tenant data leaks.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  2,
  'Circuit Breaker pattern mein jab state ''OPEN'' ho jaye to gateway ka kya behavior hota hai?',
  '["Failing primary provider ko mazeed requests bhejna band kar deta hai aur foran secondary failover provider par traffic route karta hai", "Tamam user requests ko drop kar deta hai", "Server ko reboot kar deta hai", "Database delete kar deta hai"]'::jsonb,
  0,
  'OPEN circuit failing downstream service ko recover hone ka waqt deta hai aur instant failover ke zariye user requests ko 99.9% uptime ke sath serve karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  3,
  'Stripe Usage-Based Metered Billing integrate karne ka primary workflow kya hota hai?',
  '["Har successful inference turn ke input aur output tokens count karke Stripe Meter Events API ko asynchronously report karna", "User se har prompt par credit card CVV mangna", "Monthly fixed bill generate karna bina usage track kiye", "Stripe webhooks ko block karna"]'::jsonb,
  0,
  'Usage-based billing token consumption ke exact events Stripe billing meter ko bhejti hai jo month end par accurate consumption invoice generate karta hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  4,
  'Production packaging mein Multi-Stage Docker builds use karne ka kya faida hota hai?',
  '["Heavy compilers aur build tools ko pehle stage mein chhor kar final image mein sirf lightweight compiled runtime binaries copy karna, reducing image size by 70%+", "Docker image size 10GB bara kar dena", "Deployment speed ko slow kar dena", "Kubernetes ko bypass karna"]'::jsonb,
  0,
  'Multi-stage builds production containers ko minimal, secure aur fast banati hain. Attack surface minimize hoti hai aur deployment seconds mein execute hoti hai.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;

insert into public.quiz_questions (
  quiz_id, question_number, question_roman_urdu, options, correct_option_index, explanation_roman_urdu
)
select
  qz.id,
  5,
  'Global AI Engineering roles ($100k-$180k) secure karne ke liye sab se authentic proof-of-work kya hota hai?',
  '["Live deployed public application URL, clear architectural diagrams, benchmark latency graphs aur open-source GitHub code", "Sirf resume par buzzwords likhna", "Certificates ki photos upload karna bina kisi working project ke", "Theory questions yaad karna"]'::jsonb,
  0,
  'Global elite engineering teams working software, reproducible benchmarks aur clean system design ko dekhti hain. Live production projects are the ultimate unfair advantage.'
from public.quizzes qz
join public.modules m on m.id = qz.module_id
where m.slug = 'enterprise-capstone-and-career-launch'
on conflict (quiz_id, question_number) do update set
  question_roman_urdu = excluded.question_roman_urdu,
  options = excluded.options,
  correct_option_index = excluded.correct_option_index,
  explanation_roman_urdu = excluded.explanation_roman_urdu;


-- 9. ENGINEERING DEEP-DIVE BLOGS (10 SUB-PAGES)
insert into public.engineering_blogs (
  slug, title, category, reading_time_minutes, summary_roman_urdu,
  content_roman_urdu, code_snippet, compute_recipe, diagram_script,
  diagram_preset, diagram_animation, order_index
)
values (
  'zero-gpu-survival-guide-2026',
  'Zero-GPU Survival Guide 2026: Google Colab, Kaggle 30h Dual-T4 & Google One Pro 1000 Compute Units Mastery',
  'Cloud & Compute',
  12,
  'Bina kisi local GPU ke production-grade models fine-tune karein aur Google One Pro compute units ko auto-disconnect script se 100% bachaayein.',
  'Agar aapke pas RTX 4090 ya Mac M3 Max nahi hai, to pareshan hone ki bilkul zaroorat nahi! 2026 mein modern AI engineering hardware-poor engineers ke liye pehle se kahin zyada accessible hai.

### 1. The Reality of Hardware Hierarchy
- **Google Colab Free T4 (15GB GDDR6)**: Fast prototyping, inference, and QLoRA on 7B/8B models.
- **Kaggle Dual-T4 (30GB Combined VRAM)**: 30 hours per week free! PyTorch DDP aur Accelerate ke zariye 14B models comfortably fine-tune ho sakte hain.
- **Google One Pro (100-1000 Compute Units)**: Agar aapke pas Google One 2TB AI Premium plan hai to aapko monthly 100 se 1000 compute units milte hain. Is se aap Nvidia A100 (40GB/80GB) ya L4 GPUs run kar sakte hain.

### 2. The Dreaded ''Forgot to Disconnect'' Disaster
A100 GPU 2.5 compute units per hour consume karta hai. Agar raat ko model train karne laga kar so gaye aur notebook chal rahi to subah tak 60 units zaya! Iska hal `runtime.unassign()` hai.

### 3. Step-by-Step Survival Recipe
Hamesha apne Python script ko `try...finally` block mein wrap karein taake job pass ho ya fail, runtime foran shutdown ho jaye!',
  '# Google Colab Auto-Disconnect & Saver Script
import time
import torch

try:
    print(f"CUDA Device: {torch.cuda.get_device_name(0)}")
    print("Training Unsloth 4-bit LoRA adapter...")
    time.sleep(2)
    print("Training successfully finished & weights pushed to HuggingFace Hub!")
except Exception as e:
    print(f"Error during training: {e}")
finally:
    try:
        from google.colab import runtime
        print("Disconnecting runtime to save your precious compute units!")
        runtime.unassign()
    except ImportError:
        print("Not running in Google Colab environment.")',
  'Google Colab Free T4 (15GB VRAM) ya Kaggle Dual-T4 (30h/week). Cost: $0.00. Unassign script prevents compute burn.',
  '@preset midnight
@animate flow
flow LR: Zero-GPU Cloud Compute Strategy 2026
dev[Local Laptop // 0-VRAM] ~purple -> choose{Workload Type?}*
choose ->|Rapid Prototyping| colab[Google Colab Free T4 // 15GB VRAM] ~info
choose ->|Heavy Fine-Tuning| kaggle[Kaggle Dual T4 // 30GB VRAM, 30h/wk] ~teal
choose ->|Long Jobs & A100| gpro[Google One Pro // 1000 Compute Units]* ~ok
choose ->|High Speed Inference| freeapi[Groq & Gemini Flash Free Tier // 300+ tps] ~purple
colab -> saver[Auto-Disconnect Saver // runtime.unassign()]* $bolt ~ok
gpro -> saver',
  'midnight',
  'flow',
  1
)
on conflict (slug) do update set
  title = excluded.title,
  category = excluded.category,
  reading_time_minutes = excluded.reading_time_minutes,
  summary_roman_urdu = excluded.summary_roman_urdu,
  content_roman_urdu = excluded.content_roman_urdu,
  code_snippet = excluded.code_snippet,
  compute_recipe = excluded.compute_recipe,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  order_index = excluded.order_index;

insert into public.engineering_blogs (
  slug, title, category, reading_time_minutes, summary_roman_urdu,
  content_roman_urdu, code_snippet, compute_recipe, diagram_script,
  diagram_preset, diagram_animation, order_index
)
values (
  'why-85-percent-fail-ai',
  'Why 85% Fail AI Courses (And How Top-Down + First-Principles Makes You Unstoppable)',
  'Learning Strategy',
  8,
  '85% log AI seekhte waqt calculus ke jhanjhat mein phas kar drop out kar jate hain; top-down methodology pehle din working system deploy karwati hai.',
  'Aksar university courses aur online tutorials students ko pehle 6 mahine calculus, matrix proofs, aur dry probability padhate hain. Nateeja? Student 4 hafton baad demotivate ho kar chor deta hai kyunki usne koi working cheez nahi banayi hoti.

### 1. Top-Down Learning (The fast.ai & Karpathy Way)
- **Day 1**: Working LLM pipeline, semantic search, ya computer vision model run karein.
- **Week 2**: Uske components ko inspect karein — embedding kya hai? Tokenizer kahan fail hota hai?
- **Week 3-4**: First-principles depth mein jayein — self-attention ka QK^T matrix multiplication khud NumPy mein likhein.

### 2. Active Recall & The 70:20:10 Rule
70% waqt code likhne aur real-world projects banane mein, 20% code review aur debugging mein, aur sirf 10% passive video lecture dekhne mein lagayein.',
  'from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
result = classifier("Shipping working AI code on Day 1 is 10x better than passive theory!")
print("Classification:", result)',
  'Local CPU / Google Colab Free Tier. Cost: $0.00. Zero GPU required for inference.',
  '@preset midnight
@animate pulse
flow LR: Top-Down vs Bottom-Up AI Mastery
trap[Bottom-Up Trap // 6 Months Calculus Paralysis] ~muted -> fail[85% Drop Out // Zero Shipped Projects]* ~danger
sol[Top-Down Mastery // Ship Working System Day 1] ~purple -> peel[Peel Layers First-Principles // Math as Needed]* ~teal
peel -> build[Build PyTorch From Scratch] ~info
build -> prod[15% Top AI Engineers // Shipped Portfolio] ~ok',
  'midnight',
  'pulse',
  2
)
on conflict (slug) do update set
  title = excluded.title,
  category = excluded.category,
  reading_time_minutes = excluded.reading_time_minutes,
  summary_roman_urdu = excluded.summary_roman_urdu,
  content_roman_urdu = excluded.content_roman_urdu,
  code_snippet = excluded.code_snippet,
  compute_recipe = excluded.compute_recipe,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  order_index = excluded.order_index;

insert into public.engineering_blogs (
  slug, title, category, reading_time_minutes, summary_roman_urdu,
  content_roman_urdu, code_snippet, compute_recipe, diagram_script,
  diagram_preset, diagram_animation, order_index
)
values (
  'tensors-memory-strides',
  'Tensors & Memory Strides Under the Hood: Zero-Copy Layouts & SIMD',
  'Low-Level AI',
  10,
  'Tensor asal mein RAM ka aik flat 1D buffer hota hai; strides aur storage offsets samajh kar zero-copy high performance code likhein.',
  'PyTorch ya NumPy mein jab aap `tensor.transpose(0, 1)` karte hain to kya data memory mein move hota hai? Bilkul nahi! Yeh zero-copy operation hai jo sirf metadata strides ko update karta hai.

### 1. Strides Ka Concept
Strides yeh batate hain ke agle row ya column par jane ke liye memory mein kitne elements aage koodna (stride) hai. Aik (3, 4) float32 tensor ka default row-major stride (4, 1) hota hai.

### 2. The `.contiguous()` Trap
Jab tensor non-contiguous ho jata hai (jaise transpose ke baad), aur aap `.view()` call karte hain, to PyTorch error deta hai! Aapko `.contiguous()` call karna padta hai jo naya buffer allocate karta hai. Is overhead se bachna high-scale production systems ke liye zaroori hai.',
  'import torch

x = torch.arange(12, dtype=torch.float32).reshape(3, 4)
print("Original Shape:", x.shape, "Strides:", x.stride())
print("Is Contiguous:", x.is_contiguous())

t = x.t()
print("Transposed Shape:", t.shape, "Strides:", t.stride())
print("Is Contiguous:", t.is_contiguous())',
  'Pure Python / NumPy / PyTorch CPU. Zero VRAM. Execution time: <10ms.',
  '@preset midnight
@animate wave
arch LR: Tensor Memory Layout & Strides Under the Hood
logical[2D Matrix 3x4 // Shape & Dtype] ~purple -> strides[Strides 4,1 // Byte Steps]* ~info
strides -> ram[(1D Flat Contiguous Buffer in RAM/VRAM)] $db ~teal
ram -> op{Transpose / Reshape}*
op ->|Zero-Copy View| view[New Metadata Strides 1,4 // 0-Copy] ~ok
op ->|Non-Contiguous .contiguous()| clone[Deep Memory Copy // Allocation Penalty] ~danger',
  'midnight',
  'wave',
  3
)
on conflict (slug) do update set
  title = excluded.title,
  category = excluded.category,
  reading_time_minutes = excluded.reading_time_minutes,
  summary_roman_urdu = excluded.summary_roman_urdu,
  content_roman_urdu = excluded.content_roman_urdu,
  code_snippet = excluded.code_snippet,
  compute_recipe = excluded.compute_recipe,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  order_index = excluded.order_index;

insert into public.engineering_blogs (
  slug, title, category, reading_time_minutes, summary_roman_urdu,
  content_roman_urdu, code_snippet, compute_recipe, diagram_script,
  diagram_preset, diagram_animation, order_index
)
values (
  'the-illustrated-transformer',
  'The Illustrated Transformer & Scaled Dot-Product Attention (sqrt{d_k} Math Intuitively)',
  'Deep Learning',
  15,
  'Scaled Dot-Product Attention ka QK^T matrix math, sqrt{d_k} scaling ki mathematical waja, aur causal masking ki visual explanation.',
  'Transformer architecture 2017 mein introduce hua aur aaj tak sabhi SOTA LLMs (GPT-4o, Claude 3.5, Llama 3, DeepSeek) ki bunyad hai. Lekin attention mechanism asal mein karta kya hai?

### 1. Query, Key, aur Value Ka Mental Model
- **Query (Q)**: ''Main kya dhoond raha hoon?''
- **Key (K)**: ''Mere pas kya information moojood hai?''
- **Value (V)**: ''Meri actual content details kya hain?''
Jab Q aur K ka dot product lete hain to correlation score nikalta hai.

### 2. sqrt{d_k} Se Divide Kyun Karte Hain?
Agar dimension d_k bara ho (maslan 64 ya 128), to dot products ka variance bara ho jata hai. Softmax function bare numbers par saturate ho jata hai aur gradients zero ho jate hain (vanishing gradients). sqrt{d_k} se divide karne se variance wapis 1 par rehti hai!',
  'import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q, K, V, mask=None):
    d_k = Q.size(-1)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    attention_weights = F.softmax(scores, dim=-1)
    return torch.matmul(attention_weights, V), attention_weights

q = torch.randn(1, 1, 4, 64)
k = torch.randn(1, 1, 4, 64)
v = torch.randn(1, 1, 4, 64)
out, weights = scaled_dot_product_attention(q, k, v)
print("Output shape:", out.shape, "Attention sum:", weights.sum(dim=-1))',
  'Runs locally on CPU or Colab Free T4 in 5ms. Memory: <50MB RAM.',
  '@preset midnight
@animate wave
arch LR: Scaled Dot-Product Self-Attention
tok[Token Embeddings X] ~purple -> qkv[Linear Projections // Wq, Wk, Wv]
qkv -> q[Queries Q] ~info
qkv -> k[Keys K] ~teal
qkv -> v[Values V] ~teal
q -> matmul((Q x K^T))
k -> matmul
matmul -> scale[Scale 1 / sqrt d_k // Prevent Vanishing Gradients]*
scale -> mask[Causal Masking // Upper Triangle -inf]
mask -> sm[Softmax // Attention Heatmap Probabilities]* ~purple
sm -> out((Softmax x V))
v -> out
out -> proj[Linear Output Projection Wo] ~ok',
  'midnight',
  'wave',
  4
)
on conflict (slug) do update set
  title = excluded.title,
  category = excluded.category,
  reading_time_minutes = excluded.reading_time_minutes,
  summary_roman_urdu = excluded.summary_roman_urdu,
  content_roman_urdu = excluded.content_roman_urdu,
  code_snippet = excluded.code_snippet,
  compute_recipe = excluded.compute_recipe,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  order_index = excluded.order_index;

insert into public.engineering_blogs (
  slug, title, category, reading_time_minutes, summary_roman_urdu,
  content_roman_urdu, code_snippet, compute_recipe, diagram_script,
  diagram_preset, diagram_animation, order_index
)
values (
  'kv-cache-paged-attention',
  'KV-Cache & PagedAttention (vLLM): Breaking the GPU Memory Wall',
  'Inference & Systems',
  11,
  'LLM generation ke waqt KV Cache VRAM kyun bhar deta hai aur vLLM ka PagedAttention virtual memory paging ke zariye 80% waste kaise khatam karta hai.',
  'Autoregressive LLM inference mein har naya token generate karne ke liye purane tokens ke Key aur Value tensors dobara compute nahi kiye jate — unhe VRAM mein cache kiya jata hai jise **KV-Cache** kehte hain.

### 1. Naive Allocation Ka Nuqsan
Traditional systems har request ke liye max sequence length (maslan 4,096 tokens) ka contiguous VRAM block pehle se book kar lete the. Agar user ne sirf 100 tokens generate kiye to baqi 97% memory zaya (internal fragmentation)! Nateeja: GPU sirf 2 ya 3 concurrent requests handle kar sakti thi.

### 2. PagedAttention Ka Inqilab (vLLM)
Operating Systems ke Virtual Memory Paging concept ko adopt karte hue, PagedAttention KV-cache ko chote non-contiguous blocks (e.g. 16 tokens per block) mein divide karta hai. Is se GPU memory utilization 20% se seedha 96% par chali jati hai aur throughput 4x-10x barh jati hai!',
  'def kv_cache_size_gb(num_layers, hidden_size, seq_len, batch_size, bytes_per_elem=2):
    bytes_total = 2 * num_layers * hidden_size * bytes_per_elem * seq_len * batch_size
    return bytes_total / (1024 ** 3)

vram_for_100_users_4k = kv_cache_size_gb(32, 4096, 4096, 100)
print(f"KV Cache for 100 users @ 4k tokens: {vram_for_100_users_4k:.2f} GB VRAM!")',
  'Deploy on RunPod / Colab Pro L4 / local vLLM. Zero-VRAM estimation script runs on CPU.',
  '@preset midnight
@animate flow
flow LR: KV-Cache & PagedAttention Memory Architecture
prompt[Prompt Tokens] ~purple -> prefill[Prefill Phase // Parallel Compute]* $cpu ~info
prefill -> init_kv[Initial K & V Tensors] ~teal
gen[Autoregressive Decode Step] ->|New Single Token| append[Append New K, V Vector]
append -> vmem{Standard Allocation?}*
vmem ->|Naive Contiguous Alloc| frag[60-80% VRAM Waste & Memory Fragmentation] ~danger
vmem ->|PagedAttention vLLM| table[Virtual Page Table // Non-Contiguous Blocks]* ~ok
table -> vram[(VRAM Physical Blocks // 96% Memory Utilization)] $db ~ok',
  'midnight',
  'flow',
  5
)
on conflict (slug) do update set
  title = excluded.title,
  category = excluded.category,
  reading_time_minutes = excluded.reading_time_minutes,
  summary_roman_urdu = excluded.summary_roman_urdu,
  content_roman_urdu = excluded.content_roman_urdu,
  code_snippet = excluded.code_snippet,
  compute_recipe = excluded.compute_recipe,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  order_index = excluded.order_index;

insert into public.engineering_blogs (
  slug, title, category, reading_time_minutes, summary_roman_urdu,
  content_roman_urdu, code_snippet, compute_recipe, diagram_script,
  diagram_preset, diagram_animation, order_index
)
values (
  'vector-search-vs-hybrid-rag',
  'Pure Vector Search vs Hybrid RAG (BM25 + pgvector + RRF + ColPali Vision RAG)',
  'Information Retrieval',
  14,
  'Kyun sirf vector cosine similarity real enterprise RAG mein fail hoti hai aur BM25 keyword search + pgvector + RRF + ColPali se zero hallucination kaise hasil karein.',
  'Standard RAG tutorials mein log sirf `text-embedding-3-small` use kar ke vector search karte hain. Lekin jab client pooche: ''Invoice number #PK-9821 ka total bill kitna tha?'', to vector search fail ho jata hai kyunki invoice number ka koi semantic meaning nahi hota!

### 1. Hybrid Search (Dense + Sparse)
- **Sparse (BM25 / Full-Text)**: Exact part numbers, invoice IDs, acronyms, aur names pakadta hai.
- **Dense (pgvector HNSW)**: Conceptual similarity aur fuzzy semantics pakadta hai.

### 2. Reciprocal Rank Fusion (RRF)
Dono lists ko bina score normalization ke merge karne ke liye RRF formula use hota hai:
`RRF_Score(d) = sum(1 / (k + rank(d)))` jahan `k = 60`.

### 3. ColPali (Vision-Language RAG 2026)
Complex multi-column PDFs, tables, aur Pakistani Urdu cheques ke liye text extract karne ke bajaye pooray page ka screenshot embed kiya jata hai via ColPali late-interaction!',
  'def rrf_merge(bm25_ranks, vector_ranks, k=60):
    scores = {}
    for rank, doc_id in enumerate(bm25_ranks):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
    for rank, doc_id in enumerate(vector_ranks):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)

bm25 = ["doc_invoice_9821", "doc_receipt_12", "doc_legal_contract"]
vector = ["doc_legal_contract", "doc_invoice_9821", "doc_tax_return"]
ranked = rrf_merge(bm25, vector)
print("Top Fused Document:", ranked[0])',
  'PostgreSQL with pgvector + Supabase free tier. Embeddings via Groq / Gemini Flash API.',
  '@preset midnight
@animate flow
arch LR: Production Hybrid RAG & ColPali Pipeline
query[User Question] $user ~purple -> dense[Dense Embedder // text-embedding-3] ~info
query -> sparse[Sparse Lexical // BM25 Tokenizer] ~teal
query -> vision[Multi-Vector ColPali // Page Image Embeds]* ~purple
dense -> vdb[(pgvector HNSW Index)] $db ~info
sparse -> sdb[(Inverted Index / BM25)] $db ~teal
vision -> cvdb[(ColPali Late Interaction Index)] $db ~purple
vdb -> rrf[Reciprocal Rank Fusion RRF]* $bolt
sdb -> rrf
cvdb -> rrf
rrf -> rerank[Cross-Encoder Re-Ranker // Cohere v3] ~ok
rerank -> topk[Top-K High-Precision Context] ~ok',
  'midnight',
  'flow',
  6
)
on conflict (slug) do update set
  title = excluded.title,
  category = excluded.category,
  reading_time_minutes = excluded.reading_time_minutes,
  summary_roman_urdu = excluded.summary_roman_urdu,
  content_roman_urdu = excluded.content_roman_urdu,
  code_snippet = excluded.code_snippet,
  compute_recipe = excluded.compute_recipe,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  order_index = excluded.order_index;

insert into public.engineering_blogs (
  slug, title, category, reading_time_minutes, summary_roman_urdu,
  content_roman_urdu, code_snippet, compute_recipe, diagram_script,
  diagram_preset, diagram_animation, order_index
)
values (
  'mcp-and-smolagents',
  'Anthropic MCP & Hugging Face smolagents: Why Code Agents Beat Brittle Chains',
  'Agentic AI',
  13,
  'JSON-based tool calling aur LangChain chains kyun toot-ti hain; Anthropic Model Context Protocol aur executable Python CodeAgents ka jadeed tareeqa.',
  '2024 tak log brittle JSON chains aur LangChain use kar rahe the. Thori si schema change hoti thi aur agent crash ho jata tha! 2026 ka gold standard **Code Agents** aur **Model Context Protocol (MCP)** hai.

### 1. CodeAgent Advantage (Hugging Face smolagents)
Agent se JSON nikalne ke bajaye us se seedha Python code likhwayein. Code sandbox mein run hota hai, loop chala sakta hai, conditions check kar sakta hai, aur 3x kam LLM calls mein kaam khatam karta hai.

### 2. Anthropic Model Context Protocol (MCP)
MCP aik open standard protocol hai jo LLMs ko enterprise data sources (Postgres, GitHub, Slack, local filesystem) se connect karta hai securely via standardized JSON-RPC.',
  'from smolagents import CodeAgent, HfApiModel, tool

@tool
def get_crypto_price_pkr(coin: str) -> str:
    """Fetches real-time crypto price in PKR.
    Args:
        coin: Symbol like BTC or ETH
    """
    return f"{coin} price is currently PKR 27,850,000"

agent = CodeAgent(tools=[get_crypto_price_pkr], model=HfApiModel())
print("CodeAgent initialized with MCP tool support.")',
  'Groq Free API (Llama 3.3 70B) ya Cerebras Free API. Local CPU sandbox. $0.00 Cost.',
  '@preset midnight
@animate pulse
flow TB: Modern CodeAgent & Model Context Protocol MCP
user[User Goal / Intent] $user ~purple -> planner[smolagents CodeAgent Planner]* $ai ~purple
planner -> act[Generate Pure Python Executable Code] ~info
act -> mcp[Anthropic MCP Host Gateway // JSON-RPC]* $gear ~teal
mcp -> t1[Postgres MCP Server] $db ~teal
mcp -> t2[GitHub MCP Server] $github ~teal
mcp -> t3[Filesystem MCP Server] $gear ~teal
t1 -> obs[Tool Outputs & DataFrames] ~ok
t2 -> obs
t3 -> obs
obs -> interp[Secure Sandboxed Python Interpreter] ~info
interp -> self_heal{Exception / Error?}*
self_heal ->|Traceback detected| planner
self_heal ->|Success| deliverable((Final Validated Deliverable)) ~ok',
  'midnight',
  'pulse',
  7
)
on conflict (slug) do update set
  title = excluded.title,
  category = excluded.category,
  reading_time_minutes = excluded.reading_time_minutes,
  summary_roman_urdu = excluded.summary_roman_urdu,
  content_roman_urdu = excluded.content_roman_urdu,
  code_snippet = excluded.code_snippet,
  compute_recipe = excluded.compute_recipe,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  order_index = excluded.order_index;

insert into public.engineering_blogs (
  slug, title, category, reading_time_minutes, summary_roman_urdu,
  content_roman_urdu, code_snippet, compute_recipe, diagram_script,
  diagram_preset, diagram_animation, order_index
)
values (
  'unsloth-4bit-qlora',
  'Unsloth 4-Bit QLoRA Math: Fine-Tuning 8B Models on a Free 15GB Colab T4',
  'Model Training',
  12,
  'Unsloth custom OpenAI Triton kernels ke zariye VRAM 80% kaise bachaata hai aur free Colab T4 par Llama 3 8B model 5x tezi se kaise train hota hai.',
  'Standard Hugging Face PEFT mein 8B model fine-tune karne ke liye kam az kam 24GB VRAM (RTX 3090/4090) zaroori hoti hai. Lekin Unsloth ne game badal diya!

### 1. Manual Backprop in Triton
Unsloth ne PyTorch ke autograd ko bypass kar ke manually written OpenAI Triton kernels banaye. Is se Cross-Entropy loss aur RoPE embeddings ka memory footprint 80% kam ho jata hai.

### 2. NF4 Quantization + LoRA Rank r=16
Base model ke weights 4-bit NormalFloat (NF4) mein freeze rehte hain, jabke sirf choti low-rank matrices A aur B train hoti hain. Free Colab T4 GPU (15GB VRAM) par batch size 4 ke sath training makhan ki tarah chalti hai!',
  'from unsloth import FastLanguageModel

max_seq_length = 2048
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/llama-3-8b-bnb-4bit",
    max_seq_length=max_seq_length,
    load_in_4bit=True,
)

model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
)
print("Model ready for ultra-fast training on Free Google Colab T4!")',
  'Google Colab Free Tier (T4 GPU 15GB). Training time: ~20 mins on 1k samples. Cost: $0.00.',
  '@preset midnight
@animate glow
arch LR: Unsloth 4-bit QLoRA Parameter-Efficient Fine-Tuning
act[Input Tensor X // 16-bit Float] ~purple -> base[Base LLM Weights W0 // 4-bit NF4 Quantized]* ~muted
act -> lora_a[LoRA Matrix A // 16-bit, rank r=16] ~info
lora_a -> lora_b[LoRA Matrix B // 16-bit, rank r=16]* ~teal
lora_b -> scale[alpha / r Scaling] ~teal
base -> dequant[De-Quantize to 16-bit on the fly] ~info
dequant -> sum((+))
scale -> sum
sum -> out[Forward Activation Y] ~ok
out -> loss[Cross-Entropy Loss] -> unsloth[Unsloth Fast Triton Kernels // 5x Speed, 80% Less VRAM]* ~ok',
  'midnight',
  'glow',
  8
)
on conflict (slug) do update set
  title = excluded.title,
  category = excluded.category,
  reading_time_minutes = excluded.reading_time_minutes,
  summary_roman_urdu = excluded.summary_roman_urdu,
  content_roman_urdu = excluded.content_roman_urdu,
  code_snippet = excluded.code_snippet,
  compute_recipe = excluded.compute_recipe,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  order_index = excluded.order_index;

insert into public.engineering_blogs (
  slug, title, category, reading_time_minutes, summary_roman_urdu,
  content_roman_urdu, code_snippet, compute_recipe, diagram_script,
  diagram_preset, diagram_animation, order_index
)
values (
  'deepseek-r1-and-grpo',
  'DeepSeek-R1 & GRPO: How Reasoning Models Learn to <think> Without a Critic Model',
  'Reinforcement Learning',
  16,
  'DeepSeek-R1 ne PPO ke baray Critic model ko khatam kar ke Group Relative Policy Optimization (GRPO) ke zariye reasoning models kaise banaye.',
  'DeepSeek-R1 ne OpenAI o1 ko challenge kar ke puri dunya ko hairaan kar diya. Unka sab se bara breakthrough kya tha? **GRPO (Group Relative Policy Optimization)**.

### 1. Traditional PPO Ka Masla
Traditional RLHF (PPO) mein policy model ke barabar ka aik doosra ''Critic / Value Model'' VRAM mein rakhna padta tha. 70B model ke sath 70B critic model run karne ke liye 8x H100 GPUs chahiye the!

### 2. GRPO Ka Simple Magic
GRPO mein koi critic model nahi hota! Model aik prompt ke liye 4 se 8 mukhtalif jawab generate karta hai. Phir deterministic rules (maslan: kya compiler ne code pass kiya? kya math answer theek hai?) se har answer ko reward milta hai. Phir is group ka mean aur standard deviation nikaal kar advantage calculate hota hai!

### 3. Emergence of <think> Tokens
Model ko kisi ne explicitly nahi sikhaya ke <think> likho. Jab correct answer par reward mila to model ne khud ba khud lambi chain-of-thought aur self-correction strategy evolve kar li!',
  'import numpy as np

def compute_grpo_advantages(rewards: list[float], epsilon=1e-6) -> np.ndarray:
    r = np.array(rewards)
    mean_r = np.mean(r)
    std_r = np.std(r) + epsilon
    advantages = (r - mean_r) / std_r
    return advantages

rewards = [1.0, 0.0, -0.5, 1.0]
adv = compute_grpo_advantages(rewards)
print("GRPO Group Advantages:", adv)',
  'Kaggle Dual-T4 (30h/week) or Colab Pro with Unsloth GRPO trainer. $0.00 cost.',
  '@preset midnight
@animate wave
flow LR: DeepSeek-R1 Group Relative Policy Optimization GRPO
prompt[Math / Coding Prompt q] ~purple -> policy[Old Policy LLM pi_theta_old]* $ai ~purple
policy -> g1[Completion o1 // with think trace] ~info
policy -> g2[Completion o2 // with think trace] ~info
policy -> g3[Completion o3 // with think trace] ~info
policy -> g4[Completion o4 // with think trace] ~info
g1 -> reward[Deterministic Rule Reward // Accuracy + Format Check]* $bolt ~teal
g2 -> reward
g3 -> reward
g4 -> reward
reward -> norm[Group Normalization // Advantage A = r - mean / std]* ~ok
norm -> ppo[GRPO Objective Update // No Critic Value Model Needed!]* ~ok
ppo -> trained[Reasoning Master Model // DeepSeek-R1 style] ~purple',
  'midnight',
  'wave',
  9
)
on conflict (slug) do update set
  title = excluded.title,
  category = excluded.category,
  reading_time_minutes = excluded.reading_time_minutes,
  summary_roman_urdu = excluded.summary_roman_urdu,
  content_roman_urdu = excluded.content_roman_urdu,
  code_snippet = excluded.code_snippet,
  compute_recipe = excluded.compute_recipe,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  order_index = excluded.order_index;

insert into public.engineering_blogs (
  slug, title, category, reading_time_minutes, summary_roman_urdu,
  content_roman_urdu, code_snippet, compute_recipe, diagram_script,
  diagram_preset, diagram_animation, order_index
)
values (
  'learner-to-3k-ai-engineer',
  'From Learner to $3k+ AI Engineer: Packaging AI Microservices with Supabase & Rust',
  'Career & Architecture',
  9,
  'Pakistan aur remote market mein $3k-$5k/month kamane wale AI Engineer kaise banain; portfolio projects, Rust microservices, aur Supabase architecture.',
  'Sirf Jupyter Notebook run karna aapko AI engineer nahi banata. Clients notebook nahi khareedte — clients **reliable, fast, production-ready APIs** chahte hain jo sub-50ms latency mein unke business problems solve karein.

### 1. The $3k/mo Tech Stack
- **Backend**: Rust Axum (10x faster than FastAPI, zero memory leaks, sub-10ms overhead).
- **Database**: Supabase PostgreSQL with `pgvector`, Row Level Security (RLS), aur Supabase Auth.
- **Inference Router**: Groq / Gemini Flash for 90% cheap queries + DeepSeek-R1 / Claude for hard reasoning.
- **Frontend**: Svelte 5 / SvelteKit (clean, light, Claude-style UI).

### 2. Upwork & Direct Client Strategy
Kabhi ''I will do AI'' ka generic proposal na bhejein. Har proposal ke sath aik working loom video ya interactive URL bhejein (jaise aapka Capstone project). Client ko dikhayein ke aapne unka problem pehle hi solve kar rakha hai!',
  'use axum::{routing::post, Json, Router};
use serde::{Deserialize, Serialize};

#[derive(Deserialize)]
struct ClientQuery { prompt: String }

#[derive(Serialize)]
struct AiResponse { answer: String, latency_ms: u64 }

async fn handle_ai(Json(payload): Json<ClientQuery>) -> Json<AiResponse> {
    Json(AiResponse {
        answer: format!("Production processed: {}", payload.prompt),
        latency_ms: 8,
    })
}',
  'Deploy to Fly.io free tier or Railway + Supabase Free PostgreSQL. $0.00 startup cost.',
  '@preset midnight
@animate flow
flow LR: $3,000/mo AI Engineer Production Architecture
client[Global Upwork / Enterprise Clients] $user ~purple -> gateway[Rust Axum Gateway // <10ms Auth & Rate Limit]* ~ok
gateway -> cache[(Redis / Memory Semantic Cache)] $bolt ~teal
gateway -> supa[(Supabase Auth, pgvector & Realtime DB)] $db ~info
gateway -> llm_pool{Inference Router}*
llm_pool ->|Cheap / Fast| groq[Groq Llama 3 // 300 tps] ~teal
llm_pool ->|Reasoning| deepseek[DeepSeek-R1 / Claude 3.5 Sonnet] ~purple
gateway -> mon[Telemetry & Billing // OpenTelemetry + Stripe] $chart ~ok
mon -> profit((High-Margin $3k-10k/mo AI SaaS Service)) ~ok',
  'midnight',
  'flow',
  10
)
on conflict (slug) do update set
  title = excluded.title,
  category = excluded.category,
  reading_time_minutes = excluded.reading_time_minutes,
  summary_roman_urdu = excluded.summary_roman_urdu,
  content_roman_urdu = excluded.content_roman_urdu,
  code_snippet = excluded.code_snippet,
  compute_recipe = excluded.compute_recipe,
  diagram_script = excluded.diagram_script,
  diagram_preset = excluded.diagram_preset,
  diagram_animation = excluded.diagram_animation,
  order_index = excluded.order_index;
