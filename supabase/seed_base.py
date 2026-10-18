import os
import json

def esc(val):
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

def get_base_sql():
    lines = []
    lines.append("-- ==============================================================================")
    lines.append("-- AI USTAAD PLATFORM: 002_seed_syllabus.sql")
    lines.append("-- Complete 20-Week Roman Urdu AI Engineering Curriculum (Zero Se Hero Tak)")
    lines.append("-- 5 Phases, 14 Modules, 3 Tracks, 11 Badges, 84 Lessons, 70 Quiz Questions & 8 Challenges")
    lines.append("-- Official Portal: https://ai-ustaad.pages.dev")
    lines.append("-- ==============================================================================\n")

    # 1. Badges
    lines.append("-- 1. GAMIFICATION BADGES")
    badges = [
        ("pehla-prompt", "Pehla Prompt", "Safar Ka Aaghaz", "Completed your very first lesson on AI Ustaad!", "🚀", 50, {"type": "lesson_count", "threshold": 1}),
        ("prompt-rookie", "Prompt Rookie", "Prompts Ka Ustaad", "Mastered zero-shot, few-shot, CoT and prompt engineering patterns.", "🎯", 100, {"type": "module_complete", "module_slug": "prompt-engineering-and-llm-mental-models"}),
        ("ml-practitioner", "ML Practitioner", "Data Se Model Tak", "Mastered classical machine learning, feature pipelines, and metrics.", "📊", 150, {"type": "module_complete", "module_slug": "classical-machine-learning"}),
        ("transformer-expert", "Transformer Expert", "Attention Is All You Need", "Built multi-head attention and transformer blocks from raw tensors.", "🧠", 200, {"type": "module_complete", "module_slug": "attention-and-transformers-under-the-hood"}),
        ("app-builder", "App Builder", "Full-Stack AI Creator", "Shipped production-grade AI applications and streaming APIs.", "⚡", 250, {"type": "module_complete", "module_slug": "building-ai-applications-and-apis"}),
        ("rag-master", "RAG Master", "Context & Retrieval Wizard", "Architected advanced hybrid RAG pipelines with ColPali and reranking.", "🔍", 300, {"type": "module_complete", "module_slug": "vector-databases-and-modern-rag"}),
        ("agent-architect", "Agent Architect", "Autonomous Systems Master", "Created autonomous multi-agent swarms with Anthropic MCP and smolagents.", "🤖", 350, {"type": "module_complete", "module_slug": "autonomous-agents-and-tool-use"}),
        ("finetuning-pro", "Fine-tuning Pro", "LoRA & Unsloth Wizard", "Fine-tuned open-source models with Unsloth and DeepSeek-R1 GRPO.", "🔥", 400, {"type": "module_complete", "module_slug": "fine-tuning-and-model-adaptation"}),
        ("production-ready", "Production Ready", "0 to 1 Million Requests", "Deployed low-latency LLM microservices with vLLM, Docker and Rust.", "🛡️", 450, {"type": "module_complete", "module_slug": "production-ai-engineering-mlops"}),
        ("ai-graduate", "AI Graduate", "Hero Ban Gaye!", "Successfully completed the entire AI Ustaad curriculum and Capstone project.", "🎓", 1000, {"type": "module_complete", "module_slug": "enterprise-capstone-and-career-launch"}),
        ("top-performer", "Top Performer", "90%+ Quiz Score Champion", "Achieved 90% or higher score on a module quiz.", "👑", 200, {"type": "quiz_score", "min_score": 90}),
    ]

    for b in badges:
        slug, title, urdu, desc, icon, xp, crit = b
        lines.append(f"""insert into public.badges (slug, title, roman_urdu_subtitle, description, icon, xp_bonus, unlock_criteria)
values ({esc(slug)}, {esc(title)}, {esc(urdu)}, {esc(desc)}, {esc(icon)}, {xp}, {esc(crit)})
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
    course_title = "AI Ustaad — AI Mastery: Zero Se Production Tak"
    course_sub = "Pakistan aur South Asia Ka Pehla Complete, Production-Grade Roman Urdu AI Engineering Curriculum (ai-ustaad.pages.dev)"
    course_desc = "20 hafton ka mukammal safar: Python aur linear algebra ki bunyad se le kar Deep Learning, Transformers, Modern RAG, Autonomous Multi-Agent Systems, DeepSeek-R1 GRPO, Anthropic MCP, aur Production MLOps tak (ai-ustaad.pages.dev)."
    design_principles = [
        "Zero Hand-Waving: Math & Tensors first-principles se samjhein",
        "Roman Urdu Intuition + Global English Standards",
        "2026 SOTA First: DeepSeek-R1 GRPO, Anthropic MCP, ColPali, Unsloth",
        "Code in Production: Rust, PyTorch, vLLM, Docker",
        "Interactive Animated Diagrams (DiagramKit) har concept ke liye"
    ]
    zero_gpu_guide = {
        "title": "Zero-GPU Cloud Compute Survival Guide 2026",
        "urdu_subtitle": "Bina local GPU ke Google Colab, Kaggle Dual-T4, Google One Pro 1000 Units aur Free SOTA APIs ka blueprint",
        "description": "Agar aapke pas local GPU nahi hai to pareshan hone ki bilkul zaroorat nahi! Colab Free T4, Kaggle 30h/wk Dual T4, Google One Pro compute units aur Free SOTA API providers ke zariye 100% free model training karein.",
        "colab_free_t4": {
            "platform": "Google Colab Free Tier (Nvidia T4 15GB VRAM)",
            "vram": "15 GB GDDR6",
            "weekly_quota": "Approx 12-16 hours per session (resets daily)",
            "cost": "$0.00 (100% Free)",
            "setup_instructions_urdu": "Runtime type -> T4 GPU select karein. Training ke baad runtime unassign zaroor karein.",
            "setup_snippet": "!pip install -q torch transformers datasets accelerate bitsandbytes peft trl unsloth",
            "saver_script": "from google.colab import runtime\nruntime.unassign()"
        },
        "kaggle_dual_t4": {
            "platform": "Kaggle Notebooks (Dual Nvidia T4 2x15GB = 30GB VRAM)",
            "vram": "30 GB Combined VRAM",
            "weekly_quota": "30 Hours per week",
            "cost": "$0.00 (100% Free phone-verified account)",
            "setup_instructions_urdu": "Accelerator -> GPU T4 x 2 select karein. 14B models PyTorch DDP se train karein.",
            "setup_snippet": "!accelerate config default",
            "saver_script": "import os\nos.system('kaggle datasets version -p ./weights -m \"Auto save\"')"
        },
        "google_one_compute_units_saver": {
            "platform": "Google One Pro / Colab Pro (100 - 1000 Compute Units Optimizer)",
            "vram": "Nvidia A100 (40GB/80GB) ya L4 (24GB)",
            "weekly_quota": "100 to 1000 Compute Units",
            "cost": "Google One AI Premium bundle ($19.99/mo) or standalone",
            "setup_instructions_urdu": "Hamesha Python try-finally block mein runtime.unassign() lagayein taake raat bhar compute units burn na hon.",
            "setup_snippet": "# Run heavy 70B LoRA or Unsloth GRPO on A100 GPU",
            "saver_script": "try:\n    pass\nfinally:\n    from google.colab import runtime\n    runtime.unassign()"
        },
        "free_api_providers": [
            {
                "name": "Groq Cloud Free Tier",
                "free_tier_limits": "30 requests/min, 14,400 requests/day, 6,000 tokens/min",
                "speed": "300 - 500 tokens/sec",
                "best_for": "Ultra-low latency LLM inference, Llama 3.3 70B, real-time agent tool loops",
                "endpoint_url": "https://api.groq.com/openai/v1/chat/completions",
                "sample_curl": "curl -X POST https://api.groq.com/openai/v1/chat/completions ..."
            },
            {
                "name": "Google AI Studio (Gemini 2.0 Flash / Pro)",
                "free_tier_limits": "15 requests/min, 1,500 requests/day, 1M token context window",
                "speed": "150 - 200 tokens/sec",
                "best_for": "Massive context analysis (books, PDFs, video), multimodal vision, complex reasoning",
                "endpoint_url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
                "sample_curl": "curl \"https://generativelanguage.googleapis.com/...\""
            },
            {
                "name": "Cerebras Inference Free Tier",
                "free_tier_limits": "30 requests/min, 1M tokens/day",
                "speed": "1,800+ tokens/sec (World's Fastest Inference)",
                "best_for": "Instant speculative decoding, synthetic data generation, high-frequency agent thoughts",
                "endpoint_url": "https://api.cerebras.ai/v1/chat/completions",
                "sample_curl": "curl -X POST https://api.cerebras.ai/v1/chat/completions ..."
            }
        ]
    }

    lines.append(f"""insert into public.courses (slug, title, subtitle, description, language, total_weeks, level, design_principles, zero_gpu_guide, is_published)
values (
  {esc(course_slug)},
  {esc(course_title)},
  {esc(course_sub)},
  {esc(course_desc)},
  'roman-urdu',
  20,
  'Zero to Hero (Beginner to Production)',
  {esc(design_principles)},
  {esc(zero_gpu_guide)},
  true
)
on conflict (slug) do update set
  title = excluded.title,
  subtitle = excluded.subtitle,
  description = excluded.description,
  design_principles = excluded.design_principles,
  zero_gpu_guide = excluded.zero_gpu_guide;\n""")

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
select id, {num}, {esc(slug)}, {esc(title)}, {esc(weeks)}, {esc(lvl)}, {esc(desc)}, {esc(dkit)}, {num}
from public.courses where slug = {esc(course_slug)}
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
select id, {esc(code)}, {esc(slug)}, {esc(title)}, {esc(desc)}, {esc(topics)}, {esc(dkit)}
from public.courses where slug = {esc(course_slug)}
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
values ({num}, {esc(title)}, {esc(urdu)}, {esc(xp)}, true)
on conflict (week_number) do update set
  title = excluded.title,
  description_roman_urdu = excluded.description_roman_urdu,
  xp_reward = excluded.xp_reward;\n""")

    return lines
