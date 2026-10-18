import os
import json

def escape_sql(val):
    if val is None:
        return "NULL"
    if isinstance(val, bool):
        return "TRUE" if val else "FALSE"
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, (dict, list)):
        s = json.dumps(val)
        return "'" + s.replace("'", "''") + "'::jsonb"
    return "'" + str(val).replace("'", "''") + "'"

def main():
    out_dir = r"C:\Users\Bimo\.gemini\antigravity\scratch\ai-mastery-platform\supabase\migrations"
    out_file = os.path.join(out_dir, "002_seed_syllabus.sql")
    os.makedirs(out_dir, exist_ok=True)
    
    lines = []
    lines.append("-- ==============================================================================")
    lines.append("-- AI MASTERY PLATFORM: 002_seed_syllabus.sql")
    lines.append("-- Complete 20-Week Roman Urdu AI Engineering Curriculum (Zero Se Hero Tak)")
    lines.append("-- 5 Phases, 14 Modules, 3 Tracks, 11 Badges, 44 Lessons, Quizzes & Challenges")
    lines.append("-- ==============================================================================\n")

    # 1. Badges
    lines.append("-- 1. GAMIFICATION BADGES")
    badges = [
        ("pehla-prompt", "Pehla Prompt", "Safar Ka Aaghaz", "Completed your very first lesson on AI Mastery!", "", 50, {"type": "lesson_count", "threshold": 1}),
        ("prompt-rookie", "Prompt Rookie", "Prompts Ka Ustaad", "Mastered zero-shot, few-shot, CoT and prompt engineering patterns.", "", 100, {"type": "module_complete", "module_slug": "prompt-engineering-and-llm-mental-models"}),
        ("ml-practitioner", "ML Practitioner", "Data Se Model Tak", "Mastered classical machine learning, feature pipelines, and metrics.", "", 150, {"type": "module_complete", "module_slug": "classical-machine-learning"}),
        ("transformer-expert", "Transformer Expert", "Attention Is All You Need", "Built multi-head attention and transformer blocks from raw tensors.", "", 200, {"type": "module_complete", "module_slug": "attention-and-transformers-under-the-hood"}),
        ("app-builder", "App Builder", "Full-Stack AI Creator", "Shipped production-grade AI applications and streaming APIs.", "⚡", 250, {"type": "module_complete", "module_slug": "building-ai-applications-and-apis"}),
        ("rag-master", "RAG Master", "Context & Retrieval Wizard", "Architected advanced hybrid RAG pipelines with ColPali and reranking.", "", 300, {"type": "module_complete", "module_slug": "vector-databases-and-modern-rag"}),
        ("agent-architect", "Agent Architect", "Autonomous Systems Master", "Created autonomous multi-agent swarms with Anthropic MCP and smolagents.", "", 350, {"type": "module_complete", "module_slug": "autonomous-agents-and-tool-use"}),
        ("finetuning-pro", "Fine-tuning Pro", "LoRA & Unsloth Wizard", "Fine-tuned open-source models with Unsloth and DeepSeek-R1 GRPO.", "", 400, {"type": "module_complete", "module_slug": "fine-tuning-and-model-adaptation"}),
        ("production-ready", "Production Ready", "0 to 1 Million Requests", "Deployed low-latency LLM microservices with vLLM, Docker and Rust.", "️", 450, {"type": "module_complete", "module_slug": "production-ai-engineering-mlops"}),
        ("ai-graduate", "AI Graduate", "Hero Ban Gaye!", "Successfully completed the entire AI Mastery curriculum and Capstone project.", "", 1000, {"type": "module_complete", "module_slug": "enterprise-capstone-and-career-launch"}),
        ("top-performer", "Top Performer", "90%+ Quiz Score Champion", "Achieved 90% or higher score on a module quiz.", "", 200, {"type": "quiz_score", "min_score": 90}),
    ]

    for b in badges:
        slug, title, urdu, desc, icon, xp, crit = b
        lines.append(f"""insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ({escape_sql(slug)}, {escape_sql(title)}, {escape_sql(urdu)}, {escape_sql(desc)}, {escape_sql(icon)}, {xp}, {escape_sql(crit)})
on conflict (slug) do update set
  title = excluded.title,
  roman_urdu_subtitle = excluded.roman_urdu_subtitle,
  description = excluded.description,
  icon = excluded.icon,
  xp_bonus = excluded.xp_bonus,
  unlock_criteria = excluded.unlock_criteria;\n""")

    # 2. Course
    lines.append("\n-- 2. COURSE")
    course_slug = "ai-mastery-zero-to-production"
    course_title = "AI Mastery - Zero to Production (AI Zero Se Hero Tak)"
    course_sub = "Pakistan aur South Asia Ka Pehla Complete, Production-Grade Roman Urdu AI Engineering Curriculum"
    course_desc = "20 hafton ka mukammal safar: Python aur linear algebra ki bunyad se le kar Deep Learning, Transformers, Modern RAG, Autonomous Multi-Agent Systems, DeepSeek-R1 GRPO, Anthropic MCP, aur Production MLOps tak."
    design_principles = [
        "Zero Hand-Waving: Math & Tensors first-principles se samjhein",
        "Roman Urdu Intuition + Global English Standards",
        "2026 SOTA First: DeepSeek-R1 GRPO, Anthropic MCP, ColPali, Unsloth",
        "Code in Production: Rust, PyTorch, vLLM, Docker",
        "Interactive Animated Diagrams (DiagramKit) har concept ke liye"
    ]
    lines.append(f"""insert into public.courses (slug, title, subtitle, description, language, total_weeks, level, design_principles, is_published)
values (
  {escape_sql(course_slug)},
  {escape_sql(course_title)},
  {escape_sql(course_sub)},
  {escape_sql(course_desc)},
  'roman-urdu',
  20,
  'Zero to Hero (Beginner to Production)',
  {escape_sql(design_principles)},
  true
)
on conflict (slug) do update set
  title = excluded.title,
  subtitle = excluded.subtitle,
  description = excluded.description,
  design_principles = excluded.design_principles;\n""")

    # 3. Phases
    lines.append("\n-- 3. PHASES (5 PHASES)")
    phases = [
        (1, "phase-1-foundations", "Phase 1: Foundations & Python Mastery", "Weeks 1-4", "Beginner",
         "Python fundamentals, NumPy tensors, Vector math, Prompt Engineering aur LLM mental models.",
         """@preset midnight
@animate flow
flow LR: Phase 1 Foundations
  py[Python 3.12 & NumPy] $python -> math[Linear Algebra & Calculus] $brain
  math -> prompt[Prompt Engineering & LLMs] $terminal
  prompt -> first_app[Pehla AI Prototype] $cube *"""),

        (2, "phase-2-core-ml-deeplearning", "Phase 2: Core ML & Deep Learning", "Weeks 5-8", "Intermediate",
         "Scikit-learn se Gradient Descent, PyTorch neural networks, Backpropagation, aur Transformer Attention mechanism.",
         """@preset midnight
@animate pulse
flow LR: Phase 2 Core ML to Deep Learning
  ml[Classical ML & Trees] $database -> torch[PyTorch Tensors & Autograd] $cpu
  torch -> mlp[Neural Networks MLP] $layers
  mlp -> attn[Attention & Transformers] $brain *"""),

        (3, "phase-3-modern-genai-stack", "Phase 3: Modern GenAI Stack & RAG", "Weeks 9-12", "Advanced",
         "Embeddings, Vector Databases, Advanced RAG (Hybrid Search, Re-ranking, ColPali), aur Multi-Agent Systems with Anthropic MCP & smolagents.",
         """@preset midnight
@animate flow
flow LR: Phase 3 Modern GenAI Stack
  apis[Streaming LLM APIs] $server -> rag[Advanced RAG & ColPali] $database
  rag -> mcp[Anthropic MCP Tools] $code
  mcp -> agents[Autonomous Multi-Agent Swarms] $brain *"""),

        (4, "phase-4-production-mlops", "Phase 4: Fine-Tuning & Production MLOps", "Weeks 13-16", "Expert",
         "LoRA/QLoRA with Unsloth, DeepSeek-R1 GRPO reasoning, Quantization (GGUF/AWQ), High-throughput inference with vLLM aur Rust Axum microservices.",
         """@preset midnight
@animate flow
flow LR: Phase 4 Fine-Tuning & Production MLOps
  unsloth[Unsloth LoRA & QLoRA] $cpu -> grpo[DeepSeek-R1 GRPO RL] $brain
  grpo -> vllm[vLLM PagedAttention] $server
  vllm -> rust[Rust Axum Microservice] $lock *"""),

        (5, "phase-5-specialization-capstone", "Phase 5: Specialization & Enterprise Capstone", "Weeks 17-20", "Mastery",
         "Three specialized tracks (AI Developers, AI Business/Product, AI Research), end-to-end multi-tenant enterprise AI system with auth, evaluation, telemetry & global deployment.",
         """@preset midnight
@animate pulse
arch LR: Phase 5 Specialization & Capstone
  tracks[Specialization Tracks A / B / C] $terminal -> capstone[Multi-Tenant Enterprise AI] $server *
  capstone -> eval[Ragas & Guardrails] $lock
  capstone -> cloud[Global Cloud & Portfolio] $cloud""")
    ]

    for p in phases:
        num, slug, title, weeks, lvl, desc, dkit = p
        lines.append(f"""insert into public.phases (course_id, phase_number, slug, title, weeks_range, level, description, diagram_script, order_index)
select id, {num}, {escape_sql(slug)}, {escape_sql(title)}, {escape_sql(weeks)}, {escape_sql(lvl)}, {escape_sql(desc)}, {escape_sql(dkit)}, {num}
from public.courses where slug = {escape_sql(course_slug)}
on conflict (slug) do update set
  phase_number = excluded.phase_number,
  title = excluded.title,
  weeks_range = excluded.weeks_range,
  level = excluded.level,
  description = excluded.description,
  diagram_script = excluded.diagram_script,
  order_index = excluded.order_index;\n""")

    # 4. Specialization Tracks
    lines.append("\n-- 4. SPECIALIZATION TRACKS")
    tracks = [
        ("TRACK-A", "track-a-developers", "Track A: AI for Software Developers",
         "Full-stack AI systems, high-concurrency Rust backends, streaming UI with Svelte/React, WebSocket agents, custom tool integration (MCP), and production deployment.",
         ["High-Scale Rust & Go AI Microservices", "Custom MCP Tools & Plugin Engineering", "Streaming WebSocket & SSE Architectures", "vLLM & TensorRT-LLM Infrastructure", "Real-Time Agent Swarms"],
         """@preset midnight
@animate flow
flow LR: Track A: Software Developer Pathway
  fe[Svelte 5 / Next.js Client] $browser -> gw[Rust Axum Gateway] $server *
  gw -> mcp[Anthropic MCP Tools] $code
  gw -> vllm[vLLM Inference Engine] $cpu
  group Production Stack: gw mcp vllm"""),

        ("TRACK-B", "track-b-business-product", "Track B: AI for Business & Product Leaders",
         "AI product strategy, unit economics of tokens, enterprise security/compliance, multi-agent workflow orchestration, AI transformation roadmaps, and ROI measurement.",
         ["AI Product Market Fit & UX Design", "Token Cost Economics & ROI Modeling", "Enterprise Security, SOC2 & Compliance", "Workflow Automation with n8n & LangGraph", "AI Transformation Strategy"],
         """@preset midnight
@animate pulse
arch LR: Track B: Business & Product Strategy
  roi[Token Unit Economics] $dollar -> flow[Workflow Automation] $terminal
  flow -> sec[SOC2 & Data Security] $lock *
  sec -> scale[Enterprise AI Transformation] $chart"""),

        ("TRACK-C", "track-c-research-architecture", "Track C: AI Research & Architecture",
         "Cutting-edge architectures, reasoning model pre-training & RL (GRPO, PPO), attention variants (MQA, GQA, Linear Attention), state space models (Mamba), and ColPali visual embeddings.",
         ["Reasoning Models & GRPO Dynamics", "State Space Models (Mamba & Jamba)", "Multi-Vector Vision-Language Retrieval (ColPali)", "Synthetic Data & Self-Play Generation", "Custom Attention Kernels with FlashAttention-3"],
         """@preset midnight
@animate flow
layers: Track C: AI Research Deep Dive
  layer 4: Group Relative Policy Optimization (GRPO)
  layer 3: State Space Models (Mamba / SSMs)
  layer 2: Multi-Vector Vision Retrieval (ColPali)
  layer 1: FlashAttention-3 & Custom Triton Kernels""")
    ]

    for t in tracks:
        code, slug, title, desc, topics, dkit = t
        lines.append(f"""insert into public.specialization_tracks (course_id, track_code, slug, title, description, topics, diagram_script)
select id, {escape_sql(code)}, {escape_sql(slug)}, {escape_sql(title)}, {escape_sql(desc)}, {escape_sql(topics)}, {escape_sql(dkit)}
from public.courses where slug = {escape_sql(course_slug)}
on conflict (slug) do update set
  title = excluded.title,
  description = excluded.description,
  topics = excluded.topics,
  diagram_script = excluded.diagram_script;\n""")

    # 5. Weekly Challenges
    lines.append("\n-- 5. WEEKLY CHALLENGES")
    challenges = [
        (1, "NumPy Vectorization Challenge", "Ek pure Python nested loop matrix multiplier ko NumPy vectorized broadcasting mein convert karein aur 50x speedup demonstrate karein.", 50),
        (2, "Few-Shot Chain of Thought Engineering", "Ek complex mathematical word problem solver prompt design karein jo consistent JSON format mein final step-by-step reasoning return kare.", 50),
        (3, "Gradient Boosting Churn Predictor", "Customer churn dataset par XGBoost train karein aur F1 score 0.85 se ooper achieve karein.", 75),
        (4, "PyTorch Micrograd From Scratch", "PyTorch autograd use kiye baghair ek 2-layer neural network ka manual backprop forward/backward pass likhein.", 100),
        (5, "ColPali Multi-Vector Search", "Ek 10-page financial PDF report ko ColPali use karte hue index karein aur tables se accurate numbers retrieve karein.", 120),
        (6, "Anthropic MCP Tool Server", "Ek custom SQLite aur Weather API MCP tool server banayein jo Claude Desktop ke sath smoothly interact kare.", 150),
        (7, "Unsloth 4-bit Fine-Tuning", "LLaMA-3-8B model ko Roman Urdu Q&A dataset par Unsloth se fine-tune karein aur GGUF export karein.", 200),
        (8, "End-to-End Enterprise System", "Complete multi-tenant AI system deploy karein with auth, telemetry, and sub-100ms streaming responses.", 300)
    ]
    for c in challenges:
        num, title, urdu, xp = c
        lines.append(f"""insert into public.weekly_challenges (week_number, title, description_roman_urdu, xp_reward, is_active)
values ({num}, {escape_sql(title)}, {escape_sql(urdu)}, {xp}, true)
on conflict (week_number) do update set
  title = excluded.title,
  description_roman_urdu = excluded.description_roman_urdu,
  xp_reward = excluded.xp_reward;\n""")

    return lines, out_file

if __name__ == "__main__":
    pass
