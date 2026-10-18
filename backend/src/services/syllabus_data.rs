use crate::models::{
    BadgeDefinition, CodeSnippet, CourseOverview, DesignPrinciple, EngineeringBlog, Lesson, Module,
    Phase, PhaseSummary, PracticeCheckpoint, ProjectBrief, Quiz, QuizQuestion, ResourceLink,
    SpecializationTrack, WeeklyChallenge, ZeroGpuGuide, ZeroGpuRecipe,
};
use crate::services::blogs_service::{get_engineering_blogs, get_zero_gpu_guide};
use crate::services::diagram_service::DiagramService;

pub struct SyllabusStore {
    pub course: CourseOverview,
    pub phases: Vec<Phase>,
    pub challenges: Vec<WeeklyChallenge>,
    pub blogs: Vec<EngineeringBlog>,
    pub zero_gpu_guide: ZeroGpuGuide,
}

impl SyllabusStore {
    pub fn new() -> Self {
        let (phases, badges, tracks, design_principles, challenges) = build_syllabus();
        let blogs = get_engineering_blogs();
        let zero_gpu_guide = get_zero_gpu_guide();

        let total_phases = phases.len() as u32;
        let mut total_modules = 0;
        let mut total_lessons = 0;

        let phase_summaries = phases
            .iter()
            .map(|p| {
                total_modules += p.modules.len() as u32;
                let l_count: usize = p.modules.iter().map(|m| m.lessons.len()).sum();
                total_lessons += l_count as u32;
                PhaseSummary {
                    id: p.id,
                    slug: p.slug.clone(),
                    title: p.title.clone(),
                    urdu_title: p.urdu_title.clone(),
                    week_range: p.week_range.clone(),
                    module_count: p.modules.len(),
                    lesson_count: l_count,
                }
            })
            .collect();

        let course = CourseOverview {
            title: "AI Mastery: Zero to Production".to_string(),
            subtitle: "20 Hafton Mein Zero Se AI Engineer Tak (Roman Urdu + Code)".to_string(),
            description: "Pakistan aur South Asia ke engineers ke liye pehla rigorous, production-grade AI curriculum. Har concept Roman Urdu ki aasan aur dilchasp zubaan mein, hands-on PyTorch, SOTA Transformers, RAG, Autonomous Agents, aur MLOps ke sath!".to_string(),
            language: "Roman Urdu + Technical English".to_string(),
            total_weeks: 20,
            total_phases,
            total_modules,
            total_lessons,
            total_hours: 160,
            design_principles,
            tracks,
            badges,
            phases: phase_summaries,
            zero_gpu_guide: Some(zero_gpu_guide.clone()),
        };

        Self {
            course,
            phases,
            challenges,
            blogs,
            zero_gpu_guide,
        }
    }

    pub fn get_module(&self, slug: &str) -> Option<&Module> {
        for phase in &self.phases {
            if let Some(m) = phase.modules.iter().find(|m| {
                m.slug == slug
                    || (m.slug == "python-mastery" && slug == "python-for-ai-and-fast-math")
                    || (m.slug == "math-vectors-tensors" && slug == "prompt-engineering-and-llm-mental-models")
                    || (m.slug == "classical-ml" && slug == "classical-machine-learning")
                    || (m.slug == "deep-learning-pytorch" && slug == "deep-learning-and-pytorch-foundations")
                    || (m.slug == "nlp-transformers" && slug == "attention-and-transformers-under-the-hood")
                    || (m.slug == "llm-prompt-engineering" && slug == "building-ai-applications-and-apis")
                    || (m.slug == "vector-databases" && slug == "vector-databases-and-modern-rag")
                    || (m.slug == "production-rag" && slug == "autonomous-agents-and-tool-use")
                    || (m.slug == "llm-fine-tuning" && slug == "fine-tuning-and-model-adaptation")
                    || (m.slug == "autonomous-agents" && slug == "ai-safety-evals-and-guardrails")
                    || (m.slug == "multimodal-ai" && slug == "production-ai-engineering-mlops")
                    || (m.slug == "mlops-deployment" && slug == "multimodal-ai-and-vision")
                    || (m.slug == "capstone-production" && slug == "enterprise-capstone-and-career-launch")
            }) {
                return Some(m);
            }
        }
        None
    }

    pub fn get_lesson(&self, slug: &str) -> Option<(&Module, &Lesson)> {
        for phase in &self.phases {
            for module in &phase.modules {
                if let Some(l) = module.lessons.iter().find(|l| l.slug == slug) {
                    return Some((module, l));
                }
            }
        }
        None
    }

    pub fn get_all_modules(&self) -> Vec<&Module> {
        self.phases.iter().flat_map(|p| p.modules.iter()).collect()
    }

    pub fn get_blogs(&self) -> &[EngineeringBlog] {
        &self.blogs
    }

    pub fn get_blog(&self, slug: &str) -> Option<&EngineeringBlog> {
        self.blogs.iter().find(|b| b.slug == slug)
    }

    pub fn get_cloud_guide(&self) -> &ZeroGpuGuide {
        &self.zero_gpu_guide
    }
}

fn build_syllabus() -> (
    Vec<Phase>,
    Vec<BadgeDefinition>,
    Vec<SpecializationTrack>,
    Vec<DesignPrinciple>,
    Vec<WeeklyChallenge>,
) {
    let design_principles = vec![
        DesignPrinciple {
            title: "70:20:10 Active Mastery".to_string(),
            urdu_title: "70% Hands-on Code, 20% Peer Review, 10% Deep Theory".to_string(),
            description: "Sirf video dekhne se koi engineer nahi banta. 70% waqt real code aur projects mein guzrega.".to_string(),
            icon: "bolt".to_string(),
        },
        DesignPrinciple {
            title: "Production-First Mindset".to_string(),
            urdu_title: "Jupyter Se Bahar, Production Mein Shamil".to_string(),
            description: "Jupyter notebooks se aagay barh kar async services, Docker, GPU inference aur vector DBs seekhein.".to_string(),
            icon: "server".to_string(),
        },
        DesignPrinciple {
            title: "Mathematical Intuition".to_string(),
            urdu_title: "Maths Ka Darr Khatam, Geometric Intuition Qaim".to_string(),
            description: "Tensors, gradients, aur attention matrices ko geometrically samjhein bina ratta lagaye.".to_string(),
            icon: "cpu".to_string(),
        },
        DesignPrinciple {
            title: "Zero Hallucination Engineering".to_string(),
            urdu_title: "Reliable, Tested aur Guardrailed AI Systems".to_string(),
            description: "Evaluation benchmarks, LLM-as-a-judge, aur strict schemas ke sath 100% resilient apps banana.".to_string(),
            icon: "shield".to_string(),
        },
    ];

    let tracks = vec![
        SpecializationTrack {
            id: "genai-llm-systems".to_string(),
            title: "Generative AI & LLM Systems Engineer".to_string(),
            urdu_title: "Generative AI Aur LLM Systems Specialist".to_string(),
            description: "Advanced RAG, Fine-Tuning (PEFT/LoRA), vLLM deployment aur structured outputs mein maharat.".to_string(),
            focus_modules: vec!["nlp-transformers".to_string(), "vector-databases".to_string(), "production-rag".to_string(), "llm-fine-tuning".to_string()],
            target_role: "Senior AI Engineer / LLM Solutions Architect".to_string(),
        },
        SpecializationTrack {
            id: "autonomous-agents".to_string(),
            title: "Autonomous AI Agent Architect".to_string(),
            urdu_title: "Autonomous AI Agents Ka Architect".to_string(),
            description: "ReAct patterns, LangGraph cyclic workflows, multi-agent systems aur tool orchestration.".to_string(),
            focus_modules: vec!["llm-prompt-engineering".to_string(), "autonomous-agents".to_string(), "multimodal-ai".to_string()],
            target_role: "AI Agent Architect / Automation Specialist".to_string(),
        },
        SpecializationTrack {
            id: "mlops-platform".to_string(),
            title: "Production MLOps & Platform Engineer".to_string(),
            urdu_title: "MLOps Aur High-Scale GPU Serving Engineer".to_string(),
            description: "vLLM, TensorRT-LLM, model registries, automated CI/CD, Kubernetes GPU orchestration aur telemetry.".to_string(),
            focus_modules: vec!["deep-learning-pytorch".to_string(), "mlops-deployment".to_string(), "capstone-production".to_string()],
            target_role: "MLOps Engineer / AI Infrastructure Lead".to_string(),
        },
    ];

    let badges = vec![
        BadgeDefinition {
            id: "chai-munshi".to_string(),
            title: "Chai Wala Munshi".to_string(),
            urdu_title: "Python Zero Se Hero".to_string(),
            description: "Completed Module 0: Python Zero Se Hero and solved the Chai Shop billing checkpoint!".to_string(),
            icon: "☕".to_string(),
            xp_requirement: 250,
            module_requirement: Some("python-zero-se-hero".to_string()),
        },
        BadgeDefinition {
            id: "python-ninja".to_string(),
            title: "Python Ka Ustaad".to_string(),
            urdu_title: "Python Ninja (Async & Performance)".to_string(),
            description: "Awarded after completing Module 1: Python Mastery for AI Engineers with high distinction.".to_string(),
            icon: "🐍".to_string(),
            xp_requirement: 500,
            module_requirement: Some("python-mastery".to_string()),
        },
        BadgeDefinition {
            id: "math-tensor-lord".to_string(),
            title: "Matrix & Tensor Badshah".to_string(),
            urdu_title: "Tensors & Vector Geometry Expert".to_string(),
            description: "Awarded after completing Module 2: Mathematics, Vectors & Tensors.".to_string(),
            icon: "📐".to_string(),
            xp_requirement: 1000,
            module_requirement: Some("math-vectors-tensors".to_string()),
        },
        BadgeDefinition {
            id: "pytorch-pioneer".to_string(),
            title: "PyTorch Ka Hero".to_string(),
            urdu_title: "Deep Learning & Autograd Master".to_string(),
            description: "Awarded after training neural networks from scratch in PyTorch (Module 4).".to_string(),
            icon: "🔥".to_string(),
            xp_requirement: 2000,
            module_requirement: Some("deep-learning-pytorch".to_string()),
        },
        BadgeDefinition {
            id: "transformer-titan".to_string(),
            title: "Attention Is All You Need".to_string(),
            urdu_title: "Multi-Head Attention & Transformer Builder".to_string(),
            description: "Awarded after coding a Mini-GPT decoder from scratch (Module 6).".to_string(),
            icon: "⚡".to_string(),
            xp_requirement: 3000,
            module_requirement: Some("nlp-transformers".to_string()),
        },
        BadgeDefinition {
            id: "rag-architect".to_string(),
            title: "RAG Mastermind".to_string(),
            urdu_title: "Zero Hallucination Hybrid RAG Architect".to_string(),
            description: "Awarded after building enterprise hybrid search with re-ranking (Module 9).".to_string(),
            icon: "🔍".to_string(),
            xp_requirement: 4500,
            module_requirement: Some("production-rag".to_string()),
        },
        BadgeDefinition {
            id: "lora-fine-tuner".to_string(),
            title: "Fine-Tuning Champion".to_string(),
            urdu_title: "PEFT & QLoRA Specialist".to_string(),
            description: "Awarded after fine-tuning an 8B LLM on custom domain data (Module 10).".to_string(),
            icon: "🎯".to_string(),
            xp_requirement: 6000,
            module_requirement: Some("llm-fine-tuning".to_string()),
        },
        BadgeDefinition {
            id: "agentic-wizard".to_string(),
            title: "Autonomous Agent Operator".to_string(),
            urdu_title: "ReAct & LangGraph Architect".to_string(),
            description: "Awarded after building self-correcting multi-agent graphs (Module 11).".to_string(),
            icon: "🤖".to_string(),
            xp_requirement: 7500,
            module_requirement: Some("autonomous-agents".to_string()),
        },
        BadgeDefinition {
            id: "mlops-commander".to_string(),
            title: "Production Deployment Guru".to_string(),
            urdu_title: "vLLM, TensorRT & Kubernetes Serving Pro".to_string(),
            description: "Awarded after deploying high-throughput LLM gateway (Module 13).".to_string(),
            icon: "🚀".to_string(),
            xp_requirement: 9000,
            module_requirement: Some("mlops-deployment".to_string()),
        },
        BadgeDefinition {
            id: "streak-fire-7".to_string(),
            title: "7-Day Streak Warrior".to_string(),
            urdu_title: "Lagaataar 7 Din Ka Champion".to_string(),
            description: "Completed lessons for 7 consecutive days without breaking streak.".to_string(),
            icon: "🔥".to_string(),
            xp_requirement: 1500,
            module_requirement: None,
        },
        BadgeDefinition {
            id: "ai-master-graduate".to_string(),
            title: "AI Mastery Grandmaster".to_string(),
            urdu_title: "AI Engineer Grandmaster (All 14 Modules Complete)".to_string(),
            description: "Successfully completed the entire 20-week curriculum and defended Capstone!".to_string(),
            icon: "🏆".to_string(),
            xp_requirement: 12000,
            module_requirement: Some("capstone-production".to_string()),
        },
    ];

    let challenges = vec![
        WeeklyChallenge {
            id: "week-1-challenge".to_string(),
            week: 1,
            title: "High-Throughput Log Sanitizer".to_string(),
            urdu_title: "10 Million Lines Log Parser (Async + Polars)".to_string(),
            description_urdu: "Python generators aur Polars use karke 10 million log lines ko process karein aur anomalous embeddings filter karein.".to_string(),
            xp_reward: 250,
            badge_reward: None,
        },
        WeeklyChallenge {
            id: "week-6-challenge".to_string(),
            week: 6,
            title: "Scaled Dot-Product Attention from Scratch".to_string(),
            urdu_title: "Raw PyTorch Tensors Se Attention Mechanism Banaein".to_string(),
            description_urdu: "Bina kisi high-level library ke Q, K, V matrices ka dot product aur causal masking implement karein.".to_string(),
            xp_reward: 400,
            badge_reward: Some("transformer-titan".to_string()),
        },
        WeeklyChallenge {
            id: "week-13-challenge".to_string(),
            week: 13,
            title: "Zero-Latency Hybrid RAG Benchmark".to_string(),
            urdu_title: "Hybrid Search (Dense + BM25) Under 50ms".to_string(),
            description_urdu: "pgvector HNSW index aur BM25 ko Reciprocal Rank Fusion se combine karke sub-50ms latency achieve karein.".to_string(),
            xp_reward: 500,
            badge_reward: Some("rag-architect".to_string()),
        },
    ];

    let phases = vec![
        build_phase_1(),
        build_phase_2(),
        build_phase_3(),
        build_phase_4(),
        build_phase_5(),
    ];

    (phases, badges, tracks, design_principles, challenges)
}

// Helper to pre-render or assign SVG
fn render_svg_or_fallback(script: &str) -> Option<String> {
    DiagramService::render_script_to_svg(script, Some("midnight"), Some("flow")).ok()
}


fn get_checkpoint(mod_num: usize) -> PracticeCheckpoint {
    match mod_num {
        0 => PracticeCheckpoint {
            title: "Chai Shop Billing & Khata Management Engine".to_string(),
            urdu_title: "Chai Dhaba Billing & Munshi CLI".to_string(),
            description: "Dhabay aur chai shop ke liye real-time terminal billing tool. Har customer ka order (Doodh Patti, Elaichi Chai, Paratha), tax, discount calculate kare aur JSON khata file mein daily report append kare!".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod0_chai_billing".to_string(),
            checklist: vec![
                "@dataclass for MenuItem & OrderBill with auto-validation".to_string(),
                "Interactive while loop CLI with clean input sanitization".to_string(),
                "JSON persistence for daily transactions khata".to_string(),
                "Discount & sales tax automated calculation".to_string(),
                "Summary report generator showing top-selling item & profit".to_string(),
            ],
            xp_reward: 100,
            badge_name: "chai-munshi".to_string(),
        },
        1 => PracticeCheckpoint {
            title: "Biryani vs Pulao Sentiment & Price Vectorizer".to_string(),
            urdu_title: "Biryani vs Pulao Sentiment Analyzer".to_string(),
            description: "Karahi, Biryani aur Pulao ke 50,000 food reviews ko pure Python vs NumPy vectorized arrays se analyze karein. Cosine similarity se find karein ke kiske reviews mein sab se zyada 'Lazeez' aur 'Mirchi' ka vector overlap hai!".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod1_biryani_sentiment".to_string(),
            checklist: vec![
                "NumPy SIMD vectorized dot product implementation".to_string(),
                "Zero-copy broadcasting array operations".to_string(),
                "Cosine similarity calculator without SciPy".to_string(),
                "50x speedup benchmark vs Python nested loops".to_string(),
            ],
            xp_reward: 150,
            badge_name: "biryani-analyst".to_string(),
        },
        2 => PracticeCheckpoint {
            title: "Rishta Matcher & Bio Compatibility Algorithm".to_string(),
            urdu_title: "Rishta Matcher Vector Distance Calculator".to_string(),
            description: "Candidate ke CV/Bio aur Mother-in-Law (Saas) ki strict 15-point demand list ke darmiyan high-dimensional embeddings calculate karein. Prompt engineering se 'Red Flags' identify karein aur automated humorous compatibility score generate karein!".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod2_rishta_matcher".to_string(),
            checklist: vec![
                "Few-Shot Chain of Thought prompt engineering".to_string(),
                "Structured JSON output validation with Pydantic".to_string(),
                "Negative constraints & Hallucination mitigation rules".to_string(),
                "Automated compatibility score generation (0-100%)".to_string(),
            ],
            xp_reward: 150,
            badge_name: "rishta-whisperer".to_string(),
        },
        3 => PracticeCheckpoint {
            title: "PSL/IPL Match Outcome & Cricketer Performance Predictor".to_string(),
            urdu_title: "Cricketer Performance & Match Winner Predictor".to_string(),
            description: "Historical T20 pitch report, dew factor, strike rate, aur player matchups par LightGBM & XGBoost classifier train karein. Match ke 16th over mein live winning probability estimate karein!".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod3_cricket_predictor".to_string(),
            checklist: vec![
                "Data leakage prevention with temporal split".to_string(),
                "Feature engineering (Strike rate in death overs, economy against spin)".to_string(),
                "Hyperparameter tuning with Optuna".to_string(),
                "Precision-Recall & ROC-AUC evaluation".to_string(),
            ],
            xp_reward: 150,
            badge_name: "toss-ka-badshah".to_string(),
        },
        4 => PracticeCheckpoint {
            title: "Desi Meme Classifier & Sarcastic Roast Bot".to_string(),
            urdu_title: "Meme Classifier & Roast Engine".to_string(),
            description: "PyTorch se custom convolutional/MLP neural network train karein jo viral memes ko detect kare (e.g. 'Sarfaraz Dhoka Nahi Dega' vs 'Disappointed Pakistani Fan') aur instant humorous roast dialogue generate kare.".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod4_meme_roast_bot".to_string(),
            checklist: vec![
                "Custom PyTorch Dataset & DataLoader".to_string(),
                "CrossEntropyLoss with AdamW & CosineAnnealing".to_string(),
                "Mixed Precision (AMP) training on Free Colab T4".to_string(),
                "Model checkpointing and inference visualizer".to_string(),
            ],
            xp_reward: 200,
            badge_name: "meme-roaster".to_string(),
        },
        5 => PracticeCheckpoint {
            title: "Mirza Ghalib vs Allama Iqbal Urdu Poetry Rhyme Engine".to_string(),
            urdu_title: "Ghalib vs Iqbal Poetry Mini-GPT".to_string(),
            description: "Raw PyTorch tensors se multi-head self-attention transformer likhein jo classic Urdu ghazals ke meter aur qafiya (rhyme) ko seekh kar naye humorous shair complete kare!".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod5_ghalib_gpt".to_string(),
            checklist: vec![
                "Custom Causal Self-Attention mask".to_string(),
                "Rotary Position Embeddings (RoPE)".to_string(),
                "Byte-Pair Encoding (BPE) tokenizer integration".to_string(),
                "Next-token generation with temperature & top-p sampling".to_string(),
            ],
            xp_reward: 200,
            badge_name: "shayar-e-ai".to_string(),
        },
        6 => PracticeCheckpoint {
            title: "Ami Ka WhatsApp Auto-Responder Bot".to_string(),
            urdu_title: "Ami Ka WhatsApp Reply Bot".to_string(),
            description: "'Beta kahan ho?', 'Roti khayi?', aur 'Dahi le aana' jese WhatsApp messages ke liye production-ready FastAPI streaming server banayein with Server-Sent Events (SSE) and token-rate streaming.".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod6_ami_reply_bot".to_string(),
            checklist: vec![
                "FastAPI async route with StreamingResponse".to_string(),
                "Pydantic V2 request & response schemas".to_string(),
                "In-memory token-bucket rate limiter".to_string(),
                "CORS & Bearer token authorization middleware".to_string(),
            ],
            xp_reward: 200,
            badge_name: "farmanbardar-beta".to_string(),
        },
        7 => PracticeCheckpoint {
            title: "Grandma's Secret Biryani Recipe RAG Engine".to_string(),
            urdu_title: "Nani Amma Biryani Recipe RAG Search".to_string(),
            description: "Scanned handwritten recipe notes aur secret spices PDF documents ko PostgreSQL pgvector hybrid search (BM25 + Dense) se index karein. Query: 'Agar namak tez ho jaye to kya karein?' -> exact potaato trick cite kare!".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod7_secret_biryani_rag".to_string(),
            checklist: vec![
                "pgvector HNSW index creation in PostgreSQL".to_string(),
                "Reciprocal Rank Fusion (RRF) for Hybrid search".to_string(),
                "Cross-Encoder re-ranking with FlashRank".to_string(),
                "Strict source citation grounding prompt".to_string(),
            ],
            xp_reward: 250,
            badge_name: "bawarchi-rag".to_string(),
        },
        8 => PracticeCheckpoint {
            title: "Aggressive Salary Negotiation AI Agent Swarm".to_string(),
            urdu_title: "Salary Negotiation Multi-Agent Swarm".to_string(),
            description: "Anthropic Model Context Protocol (MCP) aur smolagents use karte hue 3 agents ka swarm banayein (Analyst, Market Researcher, Hardball Negotiator) jo remote USD salary packages par counter-offers draft kare!".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod8_salary_negotiator".to_string(),
            checklist: vec![
                "Custom MCP tool server (Tax Calculator, Glassdoor scraper)".to_string(),
                "ReAct planning & execution loop".to_string(),
                "Human-in-the-loop approval checkpoint".to_string(),
                "Multi-turn counter-offer generation".to_string(),
            ],
            xp_reward: 250,
            badge_name: "dollar-earner".to_string(),
        },
        9 => PracticeCheckpoint {
            title: "Roman Urdu Sarcasm & Roast Fine-Tuning Engine".to_string(),
            urdu_title: "Roman Urdu Sarcasm Detector (Unsloth QLoRA)".to_string(),
            description: "Free Google Colab T4 par Unsloth 4-bit QLoRA use karke Llama 3.2 3B ya Gemma 2 2B ko fine-tune karein. Model pehchane ke 'Bohot aala bhai!' tareef hai ya taana!".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod9_urdu_sarcasm".to_string(),
            checklist: vec![
                "Unsloth 4-bit FastLanguageModel setup".to_string(),
                "ChatML dataset packing with assistant masking".to_string(),
                "LoRA rank 16 / alpha 32 configuration".to_string(),
                "GGUF Q4_K_M quant export for local inference".to_string(),
            ],
            xp_reward: 300,
            badge_name: "taana-master".to_string(),
        },
        10 => PracticeCheckpoint {
            title: "Phuppo-Proof Family Group Content Guardrail Firewall".to_string(),
            urdu_title: "Family Group PII & Jailbreak Firewall".to_string(),
            description: "Family WhatsApp groups mein fake news, toxic rishta gossip aur PII leaks ko rokne ke liye NeMo Guardrails + Microsoft Presidio firewall deploy karein jo toxic messages ko polite Roman Urdu mein rewrite kare.".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod10_family_firewall".to_string(),
            checklist: vec![
                "Presidio PII anonymizer (phone, CNIC, address)".to_string(),
                "Semantic jailbreak detection rail".to_string(),
                "Ragas faithfulness evaluation metric".to_string(),
                "Automated GitHub Actions CI eval runner".to_string(),
            ],
            xp_reward: 300,
            badge_name: "sulah-joo".to_string(),
        },
        11 => PracticeCheckpoint {
            title: "Sub-50ms High-Scale AI Microservice Gateway".to_string(),
            urdu_title: "Sub-50ms Rust Axum LLM Gateway".to_string(),
            description: "Rust Axum mein high-throughput proxy gateway banayein jo Groq, Cerebras aur vLLM clusters ke darmiyan round-robin load balance kare with automated failover aur sub-50ms latency.".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod11_rust_gateway".to_string(),
            checklist: vec![
                "Rust Axum async route handlers".to_string(),
                "Token-bucket rate limiter per API key".to_string(),
                "Multi-provider health check & circuit breaker".to_string(),
                "OpenTelemetry distributed tracing".to_string(),
            ],
            xp_reward: 350,
            badge_name: "rocket-engineer".to_string(),
        },
        12 => PracticeCheckpoint {
            title: "Handwritten Doctor Prescription & Urdu Audio Transcriber".to_string(),
            urdu_title: "Doctor Prescription OCR & Audio Transcriber".to_string(),
            description: "Doctor ki tehrir (handwritten bad handwriting) aur tez bolay gaye Urdu audio notes ko Whisper Large v3 + Vision LLM se parse karke structured medicine dosage JSON generate karein.".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod12_doctor_ocr".to_string(),
            checklist: vec![
                "Whisper audio chunking & transcription".to_string(),
                "Vision LLM multimodal prompt with dosage schema".to_string(),
                "Pydantic JSON schema strict enforcement".to_string(),
                "Medicine interaction warning system".to_string(),
            ],
            xp_reward: 350,
            badge_name: "hakeem-ai".to_string(),
        },
        13 => PracticeCheckpoint {
            title: "100% Offline Exam Crammer Chatbot".to_string(),
            urdu_title: "Offline WebGPU Exam Crammer".to_string(),
            description: "Transformers.js + WebGPU ke zariye student ke browser mein Llama-3.2-1B-Instruct model 100% offline run karein taake bina internet / load-shedding ke exam revision ki ja sake.".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod13_offline_crammer".to_string(),
            checklist: vec![
                "WebGPU device initialization in JavaScript".to_string(),
                "ONNX / Transformers.js quantized model loading".to_string(),
                "Zero-server edge inference loop".to_string(),
                "Local browser IndexedDB chat persistence".to_string(),
            ],
            xp_reward: 400,
            badge_name: "bijli-proof".to_string(),
        },
        14 => PracticeCheckpoint {
            title: "Global AI Micro-SaaS Capstone Defense".to_string(),
            urdu_title: "Commercial AI SaaS Capstone Launch".to_string(),
            description: "Supabase Auth, PostgreSQL RLS, Stripe billing aur Cloudflare Pages deployment ke sath ek commercial AI SaaS banayein aur live internet par launch karein!".to_string(),
            colab_url: "https://colab.research.google.com/drive/1ai_ustaad_mod14_capstone_defense".to_string(),
            checklist: vec![
                "Multi-tenant Supabase schema with RLS".to_string(),
                "Stripe webhook payment integration".to_string(),
                "Production deployment on Cloudflare Pages".to_string(),
                "Live 60-second video demo & GitHub repository".to_string(),
            ],
            xp_reward: 500,
            badge_name: "unicorn-founder".to_string(),
        },
        _ => panic!("Invalid module number"),
    }
}

fn build_phase_1() -> Phase {

    let m0_script = r#"@preset midnight
@animate flow
flow LR: Python Zero Se Hero Learning Journey
  syntax[0.1 Syntax & Mental Model] $code -> struct[0.2 Lists, Dicts & Tuples] $db
  struct -> func[0.3 Functions & *args] $code
  func -> oop[0.4 OOP & @dataclass] $cube
  oop -> io[0.5 File I/O & JSON APIs] $cloud
  io -> np[0.6 NumPy & Pandas Intro] $cpu *"#;

    let m0 = Module {
        id: 0,
        phase_id: 1,
        slug: "python-zero-se-hero".to_string(),
        week: 0,
        title: "Python Zero Se Hero (Prerequisite Track)".to_string(),
        urdu_title: "Pehle Python, Phir AI — Zero Se Hero Tak".to_string(),
        description: "Python ki bunyadi syntax, dynamic typing mental model, data structures, functions, OOP, file handling, aur NumPy/Pandas ka practical aaghaz.".to_string(),
        diagram_script: m0_script.to_string(),
        diagram_svg: render_svg_or_fallback(m0_script),
        lessons: vec![
            Lesson {
                id: 1,
                module_slug: "python-zero-se-hero".to_string(),
                slug: "python-mental-model-syntax".to_string(),
                title: "Python Mental Model, Setup & Fast Syntax".to_string(),
                urdu_title: "Python Ka Mental Model, Interpreter Aur Basic Syntax".to_string(),
                duration_mins: 30,
                xp_reward: 50,
                explanation_urdu: "Python ek interpreted bytecode language hai jo CPython VM par execute hoti hai. Variables memory labels hote hain. Dynamic typing, conditionals aur modern match-case patterns seekhein.".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "Python 3.12 Type Hints & Pattern Matching".to_string(),
                    code: r#"model_name: str = "llama-3.2"
active_users: int = 1500

match model_name:
    case "llama-3.2" | "gemma-2":
        print("Edge inference ready!")
    case _:
        print("Standard cloud model")"#.to_string(),
                    explanation: "Pattern matching se complex if/else chains simplify hoti hain.".to_string(),
                }),
                diagram_script: Some(r#"@preset midnight
@animate flow
flow LR: CPython Execution
  src[code.py] -> comp[CPython Compiler] -> pyc[.pyc Bytecode] -> vm[Virtual Machine]*"#.to_string()),
                diagram_svg: render_svg_or_fallback(r#"@preset midnight
@animate flow
flow LR: CPython Execution
  src[code.py] -> comp[CPython Compiler] -> pyc[.pyc Bytecode] -> vm[Virtual Machine]*"#),
                key_takeaways: vec![
                    "Python source code pehle .pyc bytecode mein translate hota hai.".to_string(),
                    "Type hints run-time par crash nahi karte lekin validation mein madad dete hain.".to_string(),
                ],
                resources: vec![
                    ResourceLink { title: "Python 3.12 Official Tutorial".to_string(), url: "https://docs.python.org/3/tutorial/".to_string(), resource_type: "Docs".to_string() }
                ],
            },
            Lesson {
                id: 2,
                module_slug: "python-zero-se-hero".to_string(),
                slug: "python-data-structures-deep-dive".to_string(),
                title: "Data Structures Deep-Dive: Lists, Tuples, Sets, Dicts".to_string(),
                urdu_title: "Lists, Tuples, Sets, Dictionaries Aur Comprehensions".to_string(),
                duration_mins: 35,
                xp_reward: 50,
                explanation_urdu: "Lists dynamic arrays hain, Tuples immutable hain, Sets hash tables hain O(1) lookup ke sath, aur Dictionaries key-value mapping hain. Comprehensions se code tez aur compact banta hai.".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "Comprehensions & O(1) Hash Sets".to_string(),
                    code: r#"menu = {"chai": 60, "paratha": 120, "samosa": 40}
taxed = {k: round(v * 1.16, 2) for k, v in menu.items()}
unique_categories = {"beverage", "food", "snack"}
print(f"Taxed menu: {taxed}")"#.to_string(),
                    explanation: "Set lookups O(1) constant time mein execute hote hain.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec![
                    "Search by key/value ke liye Set aur Dict Hashing O(1) time leti hai.".to_string(),
                ],
                resources: vec![],
            },
            Lesson {
                id: 3,
                module_slug: "python-zero-se-hero".to_string(),
                slug: "python-functions-scope-closures".to_string(),
                title: "Functions, Scope, Closures & *args/**kwargs".to_string(),
                urdu_title: "Functions, Scope Rules (LEGB), Aur Observability Decorators".to_string(),
                duration_mins: 30,
                xp_reward: 50,
                explanation_urdu: "Functions first-class citizens hain. Variable resolution LEGB rule follow karta hai. *args arbitrary tuple leta hai aur **kwargs named dictionary. Decorators telemetry ke liye ahem hain.".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "Benchmark Decorator & Parameter Dispatching".to_string(),
                    code: r#"def benchmark(fn):
    def wrapper(*args, **kwargs):
        print(f"Running {fn.__name__}...")
        return fn(*args, **kwargs)
    return wrapper

@benchmark
def order_chai(name: str, *extras, **metadata):
    print(f"Chai for {name}, extras: {extras}")"#.to_string(),
                    explanation: "Decorators original function code ko modify kiye baghair monitoring add karte hain.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec![
                    "LEGB: Local -> Enclosing -> Global -> Built-in scope hierarchy.".to_string(),
                ],
                resources: vec![],
            },
            Lesson {
                id: 4,
                module_slug: "python-zero-se-hero".to_string(),
                slug: "python-oop-classes-dataclasses".to_string(),
                title: "Object-Oriented Programming (OOP) for AI: Classes & @dataclass".to_string(),
                urdu_title: "OOP, Dunder Methods Aur Modern @dataclass(slots=True)".to_string(),
                duration_mins: 40,
                xp_reward: 75,
                explanation_urdu: "Class blueprint hai aur Object instance hai. Dunder methods (__call__, __len__, __repr__) Python ke core protocols implement karte hain. @dataclass(slots=True) memory overhead khatam karta hai.".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "High-Performance Memory Efficient Dataclass".to_string(),
                    code: r#"from dataclasses import dataclass

@dataclass(slots=True)
class ChaiOrder:
    table_id: int
    items: list[str]
    total_rs: float

order = ChaiOrder(table_id=5, items=["Doodh Patti", "Paratha"], total_rs=180.0)
print(order)"#.to_string(),
                    explanation: "slots=True instance ke liye __dict__ heap overhead avoid karta hai.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec![
                    "PyTorch models nn.Module class par based hote hain.".to_string(),
                ],
                resources: vec![],
            },
            Lesson {
                id: 5,
                module_slug: "python-zero-se-hero".to_string(),
                slug: "python-files-json-apis".to_string(),
                title: "File Handling, JSON, Parquet & REST API Requests".to_string(),
                urdu_title: "Disk File I/O, JSONL Streaming Aur Web REST APIs".to_string(),
                duration_mins: 35,
                xp_reward: 75,
                explanation_urdu: "Context managers (with statement) file leaks rokte hain. JSONL LLM datasets ka universal format hai. REST API calling with retry logic and error handling.".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "JSONL File Streaming for AI Datasets".to_string(),
                    code: r#"import json

records = [{"prompt": "Suno!", "response": "Ji farmayein"}]
with open("dataset.jsonl", "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r) + "\n")"#.to_string(),
                    explanation: "JSONL streaming memory mein puray dataset ko load kiye baghair iterate karta hai.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec![
                    "with open(...) hamesha use karein taake file descriptors leak na hon.".to_string(),
                ],
                resources: vec![],
            },
            Lesson {
                id: 6,
                module_slug: "python-zero-se-hero".to_string(),
                slug: "python-numpy-pandas-foundations".to_string(),
                title: "NumPy & Pandas Foundations: Vectors, Matrices & Tabular Data".to_string(),
                urdu_title: "NumPy NDArray, Vector Math Aur Pandas Tabular Analysis".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Python lists se NumPy C-contiguous arrays tak ka safar! Vectorized dot products, array slicing, aur Pandas DataFrame groupby aggregations for AI pipelines.".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "NumPy Vectorized Calculations & Pandas DataFrame".to_string(),
                    code: r#"import numpy as np
import pandas as pd

prices = np.array([60, 120, 50])
quantities = np.array([5, 2, 4])
revenue = np.dot(prices, quantities)
print(f"Vectorized Total Revenue: Rs {revenue}")"#.to_string(),
                    explanation: "np.dot C-level SIMD instructions use karta hai.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec![
                    "NumPy arrays contiguous memory block use karte hain.".to_string(),
                    "Pandas DataFrames tabular data cleaning ke liye golden standard hain.".to_string(),
                ],
                resources: vec![
                    ResourceLink { title: "NumPy Docs".to_string(), url: "https://numpy.org/doc/stable/".to_string(), resource_type: "Docs".to_string() },
                    ResourceLink { title: "Pandas User Guide".to_string(), url: "https://pandas.pydata.org/docs/".to_string(), resource_type: "Guide".to_string() }
                ],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-0".to_string(),
            module_slug: "python-zero-se-hero".to_string(),
            title: "Module 0: Python Foundations Quiz".to_string(),
            passing_score: 70,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "Which Python data types are mutable?".to_string(),
                    urdu_question: "Python mein kaun si data types mutable (in-place modifiable) hoti hain?".to_string(),
                    options: vec![
                        "Lists, Dictionaries, and Sets".to_string(),
                        "Tuples, Strings, and Integers".to_string(),
                        "All primitive types".to_string(),
                        "None of the above".to_string(),
                    ],
                    correct_index: 0,
                    explanation_urdu: "Lists, Dicts aur Sets mutable hain jabke Tuples aur Strings immutable hain.".to_string(),
                },
                QuizQuestion {
                    id: 2,
                    question: "What is the primary benefit of @dataclass(slots=True)?".to_string(),
                    urdu_question: "Classes mein @dataclass(slots=True) use karne ka sab se bara faida kya hai?".to_string(),
                    options: vec![
                        "Eliminates dynamic __dict__ overhead and improves memory and attribute lookup speed".to_string(),
                        "Automatically compiles Python into Rust".to_string(),
                        "Runs code on GPU".to_string(),
                        "Disables all class methods".to_string(),
                    ],
                    correct_index: 0,
                    explanation_urdu: "slots=True dynamic dictionary allocate karne ke bajaye fixed-size C array use karta hai.".to_string(),
                },
                QuizQuestion {
                    id: 3,
                    question: "What is the time complexity of searching a key in a Python dict or set?".to_string(),
                    urdu_question: "Python dictionary ya set mein key dhoondne ka time complexity kya hota hai?".to_string(),
                    options: vec![
                        "O(1) average constant time via Hash Table".to_string(),
                        "O(N) linear time scan".to_string(),
                        "O(N^2) quadratic time".to_string(),
                        "O(log N) binary search".to_string(),
                    ],
                    correct_index: 0,
                    explanation_urdu: "Dicts aur Sets Hash Tables par base karte hain is liye inka lookup average O(1) hota hai.".to_string(),
                },
                QuizQuestion {
                    id: 4,
                    question: "How do *args and **kwargs collect incoming function parameters?".to_string(),
                    urdu_question: "Functions mein *args aur **kwargs parameters ko kis format mein collect karte hain?".to_string(),
                    options: vec![
                        "*args as a Tuple, **kwargs as a Dictionary".to_string(),
                        "*args as a List, **kwargs as a Set".to_string(),
                        "Both as JSON strings".to_string(),
                        "Both as pure floats".to_string(),
                    ],
                    correct_index: 0,
                    explanation_urdu: "*args positional arguments ko tuple aur **kwargs keyword arguments ko dictionary banata hai.".to_string(),
                },
                QuizQuestion {
                    id: 5,
                    question: "What is the key difference between json.dump() and json.dumps()?".to_string(),
                    urdu_question: "json.dumps() aur json.dump() mein bunyadi farq kya hai?".to_string(),
                    options: vec![
                        "json.dumps() returns a string; json.dump() writes directly to an open file stream".to_string(),
                        "json.dumps() connects to SQL database".to_string(),
                        "json.dump() only works on NumPy arrays".to_string(),
                        "There is no difference".to_string(),
                    ],
                    correct_index: 0,
                    explanation_urdu: "dumps ka 's' String ke liye hai jabke dump() file stream mein write karta hai.".to_string(),
                },
            ],
        },
        resources: vec![
            ResourceLink { title: "Python Official Docs".to_string(), url: "https://docs.python.org/3/".to_string(), resource_type: "Docs".to_string() },
        ],
        project: Some(ProjectBrief {
            title: "Chai Dhaba Billing & Khata Management Engine".to_string(),
            description: "Build an interactive CLI khata management tool for a local chai shop with @dataclass items, automated tax calculation, and persistent JSONL disk storage.".to_string(),
            deliverables: vec![
                "Python CLI with interactive order loop".to_string(),
                "@dataclass models with slots=True".to_string(),
                "JSONL daily khata persistence and summary metrics".to_string(),
            ],
            evaluation_criteria: vec![
                "Zero crashes on invalid user input".to_string(),
                "Accurate profit margin calculations".to_string(),
            ],
            real_world_deliverable: Some("Chai Dhaba Billing Engine & Khata Management CLI".to_string()),
            zero_gpu_recipe: None,
        }),
        real_world_deliverable: Some("Chai Dhaba Billing Engine & Khata Management CLI".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Local CPU / Google Colab Free Tier".to_string(),
            vram_required: "0 GB (Any CPU / Laptop)".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "Pure Python logic runs 100% locally on any basic laptop or Colab CPU without requiring GPU compute.".to_string(),
            one_click_command: "python -m pip install tabulate rich && python chai_billing.py".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(0)),
    };

    let m1_script = r#"@preset midnight
@animate flow
flow LR: Python Data Pipeline Architecture | Clean Architecture & Ingestion
csv[Raw Data / CSV] ~muted -> ingest[Ingestion Pipeline // Pydantic Validation]* ~info
ingest -> clean[Data Sanitization // Vectorized NumPy] ~teal
clean -> model[ML Features Matrix] ~purple
model -> store[(Feature Store)] $db ~ok"#;

    let m1 = Module {
        id: 1,
        phase_id: 1,
        slug: "python-mastery".to_string(),
        week: 1,
        title: "Python Mastery for AI Engineers".to_string(),
        urdu_title: "AI Engineers Ke Liye Modern Python Mastery".to_string(),
        description: "Python 3.12+ features, typing, async I/O, memory optimization, NumPy vectorization, aur production-grade data pipelines.".to_string(),
        diagram_script: m1_script.to_string(),
        diagram_svg: render_svg_or_fallback(m1_script),
        lessons: vec![
            Lesson {
                id: 101,
                module_slug: "python-mastery".to_string(),
                slug: "python-deep-dive".to_string(),
                title: "Modern Python 3.12+, Typing & Dataclasses".to_string(),
                urdu_title: "Python 3.12+ Ki Nayi Features, Strict Typing Aur Dataclasses".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "So guys, dekhein: AI pipelines mein runtime par data ka type mismatch sab se bara bug hota hai. Python 3.12 mein strict typing aur `@dataclass(slots=True)` use karne se memory 20% kam use hoti hai aur attribute lookups 1.5x fast ho jate hain!".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "High-Performance Data Class with Slots".to_string(),
                    code: r#"from dataclasses import dataclass
from typing import List, Optional

@dataclass(slots=True)
class EmbeddingRecord:
    id: str
    vector: List[float]
    metadata: dict
    score: Optional[float] = None

record = EmbeddingRecord(id="doc_1", vector=[0.12, -0.45], metadata={"source": "urdu_book"})
print(record)"#.to_string(),
                    explanation: "`slots=True` use karne se Python har instance ke liye `__dict__` nahi banata, balke C-level struct jaisa compact memory layout use karta hai.".to_string(),
                }),
                diagram_script: Some(r#"@preset midnight
@animate pulse
arch LR: Dataclass Memory Layout
obj[Instance Object] -> s[Slots: Direct C Pointers]* ~teal
dict[Standard __dict__] ~danger -> o[Dynamic Heap Overhead] ~muted"#.to_string()),
                diagram_svg: render_svg_or_fallback(r#"@preset midnight
@animate pulse
arch LR: Dataclass Memory Layout
obj[Instance Object] -> s[Slots: Direct C Pointers]* ~teal
dict[Standard __dict__] ~danger -> o[Dynamic Heap Overhead] ~muted"#),
                key_takeaways: vec![
                    "`slots=True` se memory usage significantly decrease hoti hai.".to_string(),
                    "Strict typing AI models ke inputs aur outputs ko validate karne ke liye laazmi hai.".to_string(),
                ],
                resources: vec![
                    ResourceLink { title: "Python 3.12 Official Docs".to_string(), url: "https://docs.python.org/3.12/".to_string(), resource_type: "Official Docs".to_string() }
                ],
            },
            Lesson {
                id: 102,
                module_slug: "python-mastery".to_string(),
                slug: "python-memory-concurrency".to_string(),
                title: "GIL, Memory Profiling & AsyncIO for AI APIs".to_string(),
                urdu_title: "Python GIL, Memory Profiling Aur AsyncIO LLM Calls".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Jab hum 1000 documents ko LLM API se embed karwate hain to sequential code bohot slow hota hai. AsyncIO aur `httpx.AsyncClient` use karke hum concurrent requests bhejte hain jo 10x fast execution deti hain.".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "Concurrent Async Embedding Requests".to_string(),
                    code: r#"import asyncio
import httpx

async def fetch_embedding(client, text: str):
    response = await client.post("http://localhost:8000/embed", json={"text": text})
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        texts = [f"Urdu document chunk {i}" for i in range(50)]
        tasks = [fetch_embedding(client, t) for t in texts]
        results = await asyncio.gather(*tasks)
        print(f"Fetched {len(results)} embeddings concurrently!")

if __name__ == "__main__":
    asyncio.run(main())"#.to_string(),
                    explanation: "`asyncio.gather` I/O wait time ko overlap karta hai, jiss se network latency waste nahi hoti.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec![
                    "I/O-bound tasks (jaise API calls ya DB queries) ke liye AsyncIO best hai.".to_string(),
                    "CPU-bound tasks (tensor operations) ke liye multiprocessing ya native C/Rust extensions zaroori hain.".to_string(),
                ],
                resources: vec![],
            },
            Lesson {
                id: 103,
                module_slug: "python-mastery".to_string(),
                slug: "numpy-vectorization".to_string(),
                title: "NumPy Vectorization & Matrix Broadcasting".to_string(),
                urdu_title: "NumPy Vectorization Aur SIMD Broadcasting Ka Jadoo".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Dekhein: Python loops bohot slow hain kyunke har step par dynamic type checking hoti hai. NumPy C-level contiguous memory arrays use karta hai aur CPU ki SIMD instructions ko activate karta hai. 100x speedup guarantee!".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "Vectorized Cosine Similarity in NumPy".to_string(),
                    code: r#"import numpy as np

# 10,000 document vectors (dim 128)
docs = np.random.randn(10000, 128)
query = np.random.randn(128)

# Vectorized Cosine Similarity without any Python loop!
dot_products = np.dot(docs, query)
norms = np.linalg.norm(docs, axis=1) * np.linalg.norm(query)
similarities = dot_products / norms

top_idx = np.argmax(similarities)
print(f"Top matching document index: {top_idx}, score: {similarities[top_idx]:.4f}")"#.to_string(),
                    explanation: "`np.dot(docs, query)` 10,000 vectors ke dot products milliseconds mein calculate karta hai.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec![
                    "Loops se bachein; hamesha broadcasting aur vectorized operations use karein.".to_string(),
                ],
                resources: vec![],
            },
            Lesson {
                id: 104,
                module_slug: "python-mastery".to_string(),
                slug: "pandas-data-wrangling".to_string(),
                title: "High-Performance Data Wrangling (Polars & Arrow)".to_string(),
                urdu_title: "High-Speed Data Wrangling: Polars Aur Apache Arrow".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Bari AI datasets (jaise 50GB web text) par Pandas memory overflow kar deta hai. Modern AI engineers Polars use karte hain jo Rust mein likha gaya hai aur multi-threaded lazy execution support karta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Lazy evaluation se unnecessary computations skip ho jati hain.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 105,
                module_slug: "python-mastery".to_string(),
                slug: "python-clean-architecture".to_string(),
                title: "Clean Architecture, Type Safety & Pytest for ML".to_string(),
                urdu_title: "AI Systems Ke Liye Clean Architecture Aur Pytest Suite".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Spaghetti code models ko production mein crash kar deta hai. Separation of concerns seekhein: Data Access Layer, Model Inference Layer, aur API Controller Layer ko alag rakhein.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Unit tests aur deterministic mocks ML deployment ke liye zaroori hain.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 106,
                module_slug: "python-mastery".to_string(),
                slug: "module-1-capstone".to_string(),
                title: "Module 1 Capstone: Enterprise Ingestion Engine".to_string(),
                urdu_title: "Capstone Project: Production Ingestion & Sanitization Engine".to_string(),
                duration_mins: 60,
                xp_reward: 200,
                explanation_urdu: "Is project mein aap ek multi-threaded pipeline banayenge jo raw unstructured texts ko parse karegi, regex aur token filters lagaye gi, aur validated Parquet files generate karegi.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Production data pipeline complete!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-1".to_string(),
            module_slug: "python-mastery".to_string(),
            title: "Python Mastery & Performance Evaluation".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "Why should you use @dataclass(slots=True) in AI data processing pipelines?".to_string(),
                    urdu_question: "AI data pipelines mein @dataclass(slots=True) kyun use karni chahiye?".to_string(),
                    options: vec![
                        "It makes the class run on GPU automatically".to_string(),
                        "It eliminates the __dict__ overhead and optimizes memory layout".to_string(),
                        "It turns all variables into PyTorch tensors".to_string(),
                        "It converts Python into C++ code directly".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Bilkul sahi! `slots=True` instances ke liye heap dictionary overhead eliminate karta hai aur direct attribute pointers allocate karta hai.".to_string(),
                },
                QuizQuestion {
                    id: 2,
                    question: "When processing 5,000 asynchronous LLM API calls, which approach gives the best throughput?".to_string(),
                    urdu_question: "5,000 async LLM API calls bhejte waqt sab se behtareen throughput kis se milegi?".to_string(),
                    options: vec![
                        "A standard for-loop with requests.post()".to_string(),
                        "AsyncIO with httpx.AsyncClient and asyncio.gather() or TaskGroup".to_string(),
                        "multiprocessing with 5,000 separate Python processes".to_string(),
                        "Thread sleep for 100ms after each request".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Zabardast! AsyncIO I/O-bound wait time ko overlap karta hai jiss se hazaron network calls concurrently process hoti hain bina process overhead ke.".to_string(),
                },
                QuizQuestion {
                    id: 3,
                    question: "Why is NumPy matrix multiplication faster than nested Python for-loops?".to_string(),
                    urdu_question: "NumPy matrix multiplication Python loops se 100x tez kyun hoti hai?".to_string(),
                    options: vec![
                        "Because Python ignores math errors in NumPy".to_string(),
                        "Because NumPy uses contiguous memory buffers and compiled SIMD BLAS routines".to_string(),
                        "Because NumPy converts numbers to strings".to_string(),
                        "Because NumPy runs in the browser".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Sahi jawab! NumPy contiguous C arrays aur hardware SIMD vector instructions (AVX-512) use karta hai.".to_string(),
                },
            ],
        },
        resources: vec![
            ResourceLink { title: "Python Speed Optimization Guide".to_string(), url: "https://wiki.python.org/moin/PythonSpeed".to_string(), resource_type: "Docs".to_string() },
            ResourceLink { title: "Polars User Guide".to_string(), url: "https://docs.pola.rs/user-guide/".to_string(), resource_type: "Guide".to_string() },
        ],
        project: Some(ProjectBrief {
            title: "Async Multi-Source Data Ingestion Engine".to_string(),
            description: "Build a production-grade async data pipeline that extracts text from multiple sources, cleans it, and outputs validated Arrow tables.".to_string(),
            deliverables: vec![
                "Python CLI with async data extractor".to_string(),
                "Pydantic validation schemas with slots".to_string(),
                "Pytest test suite with >90% coverage".to_string(),
            ],
            evaluation_criteria: vec![
                "Zero memory leaks on 1GB text batch".to_string(),
                "Full type annotations passing mypy --strict".to_string(),
            ],
            real_world_deliverable: Some("500k E-Commerce Order Sanitizer & Parquet Data Pipeline".to_string()),
            zero_gpu_recipe: None,
        }),
        real_world_deliverable: Some("500k E-Commerce Order Sanitizer & Parquet Data Pipeline".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Local CPU / Google Colab Free Tier".to_string(),
            vram_required: "0 GB (CPU)".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "NumPy AVX-512 vectorization runs blazing fast on standard Colab CPU without burning any GPU compute units.".to_string(),
            one_click_command: "python -m pip install numpy polars pyarrow pydantic && python main.py".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(1)),
    };

    let m2_script = r#"@preset midnight
@animate pulse
layers: Tensor Dimensionality & Memory Hierarchy | CPU to GPU Strided Memory
Rank-4 Tensor // Batch x Channels x Height x Width (B x C x H x W)*
Rank-3 Tensor // Sequence Length x Batch x Hidden Dim (S x B x D)
Rank-2 Matrix // Weight Transformation (d_in x d_out)
Rank-1 Vector // Feature Vector (Embedding Dimension d)
Rank-0 Scalar // Loss Value / Learning Rate"#;

    let m2 = Module {
        id: 2,
        phase_id: 1,
        slug: "math-vectors-tensors".to_string(),
        week: 3,
        title: "Mathematics, Vectors & Tensors".to_string(),
        urdu_title: "AI Ka Math: Vectors, Matrices Aur Tensors Ki Geometric Samajh".to_string(),
        description: "Linear Algebra, Vector Spaces, Dot Product, Matrix Transformations, Multivariable Calculus, Gradients, aur Tensor Strides.".to_string(),
        diagram_script: m2_script.to_string(),
        diagram_svg: render_svg_or_fallback(m2_script),
        lessons: vec![
            Lesson {
                id: 201,
                module_slug: "math-vectors-tensors".to_string(),
                slug: "linear-algebra-intuition".to_string(),
                title: "Vector Spaces, Dot Products & Cosine Similarity".to_string(),
                urdu_title: "Vector Spaces, Dot Product Aur Cosine Similarity Ka Geometric Intuition".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Dekhein guys: Dot product asal mein projection hai! Jab do vectors ek hi direction mein point karte hain to unka dot product maximum hota hai. LLMs aur Vector Databases isi principle par semantic search karti hain.".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "Manual Dot Product Calculation".to_string(),
                    code: r#"def manual_dot_product(u, v):
    assert len(u) == len(v), "Vectors must have same dimension!"
    return sum(a * b for a, b in zip(u, v))

v1 = [1.0, 2.0, 3.0]
v2 = [4.0, -1.0, 2.0]
print("Dot product:", manual_dot_product(v1, v2))"#.to_string(),
                    explanation: "Yeh fundamental operation hai jo har neural network layer aur attention head mein chalta hai.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec![
                    "Dot product angle aur magnitude dono ko measure karta hai.".to_string(),
                    "Cosine similarity magnitude ko normalize karke sirf direction compare karti hai.".to_string(),
                ],
                resources: vec![],
            },
            Lesson {
                id: 202,
                module_slug: "math-vectors-tensors".to_string(),
                slug: "matrix-transformations".to_string(),
                title: "Matrices as Linear Transformations & Eigenvalues".to_string(),
                urdu_title: "Matrices As Linear Transformations Aur Eigenvalues".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Matrix koi boring table nahi hai, balke space ko stretch, rotate, aur shear karne ka function hai. Har neural network layer asal mein input space ko naye space mein transform kar rahi hoti hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Linear transformation origin ko fix rakhti hai aur grid lines ko parallel rakhti hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 203,
                module_slug: "math-vectors-tensors".to_string(),
                slug: "calculus-gradient-descent".to_string(),
                title: "Multivariable Calculus, Gradients & Jacobians".to_string(),
                urdu_title: "Multivariable Calculus, Gradient Vector Aur Steepest Descent".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Gradient vector hamesha us direction mein point karta hai jahan function sab se tezi se barh raha ho. Training ke doran hum minus gradient (-nabla L) ki taraf chalte hain taake loss minimum ho sake.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Gradient descent loss surface par descend karne ka algorithm hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 204,
                module_slug: "math-vectors-tensors".to_string(),
                slug: "probability-distributions".to_string(),
                title: "Probability Distributions, Bayes & Cross-Entropy".to_string(),
                urdu_title: "Probability Distributions, Bayes Theorem Aur Cross-Entropy Loss".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Cross-Entropy measure karta hai ke model ki predicted probability distribution true distribution se kitni mukhtalif hai. LLMs har next token par isi loss ko minimize karte hain.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Cross-entropy loss surprise (information entropy) ko quantify karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 205,
                module_slug: "math-vectors-tensors".to_string(),
                slug: "tensor-operations-gpu".to_string(),
                title: "Tensor Strides, Shapes & GPU Memory Contiguity".to_string(),
                urdu_title: "Tensor Strides, GPU Memory Layout Aur Contiguous Views".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "GPU par tensor transpose karne se data copy nahi hota, sirf strides change hote hain. Lekin jab tak aap `.contiguous()` call na karein, CUDA kernels optimize nahi ho saktin!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Strides samajhna high-speed PyTorch aur CUDA optimization ke liye laazmi hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 206,
                module_slug: "math-vectors-tensors".to_string(),
                slug: "module-2-capstone".to_string(),
                title: "Module 2 Capstone: Pure Python Tensor Engine".to_string(),
                urdu_title: "Capstone: Raw Python & NumPy Se Vector Math Engine Banana".to_string(),
                duration_mins: 60,
                xp_reward: 200,
                explanation_urdu: "Is capstone mein aap ek micro Tensor class likhenge jo matrix multiplication, broadcasting, aur numerical gradient checking perform karegi.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Mathematical foundation solidified!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-2".to_string(),
            module_slug: "math-vectors-tensors".to_string(),
            title: "Vectors & Tensor Geometry Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "If two non-zero vectors have a dot product of zero, what is the geometric relationship between them?".to_string(),
                    urdu_question: "Agar do non-zero vectors ka dot product zero ho, to unka aapas mein geometric relation kya hai?".to_string(),
                    options: vec![
                        "They are parallel and point in the same direction".to_string(),
                        "They are orthogonal (perpendicular / 90 degrees)".to_string(),
                        "They have the exact same length".to_string(),
                        "One of the vectors is negative".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Bilkul durust! Dot product = ||u|| ||v|| cos(theta). Jab angle 90 degree ho to cos(90)=0 hota hai, matlab vectors orthogonal hain.".to_string(),
                },
                QuizQuestion {
                    id: 2,
                    question: "In neural network optimization, what direction does the negative gradient (-∇L) point towards?".to_string(),
                    urdu_question: "Neural network training mein negative gradient (-∇L) kis taraf point karta hai?".to_string(),
                    options: vec![
                        "Towards the steepest ascent of loss".to_string(),
                        "Towards the steepest descent (maximum decrease of loss)".to_string(),
                        "Towards a random weight initialization".to_string(),
                        "Towards zero learning rate".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Sahi jawab! Negative gradient hamesha steepest descent ki taraf le jata hai taake loss jaldi se jaldi minimize ho sake.".to_string(),
                },
            ],
        },
        resources: vec![
            ResourceLink { title: "3Blue1Brown Essence of Linear Algebra".to_string(), url: "https://www.3blue1brown.com/topics/linear-algebra".to_string(), resource_type: "Video Series".to_string() },
        ],
        project: None,
        real_world_deliverable: Some("Pure-NumPy Semantic Resume-Job Matcher & Cosine Similarity Engine".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Local CPU / Google Colab Free Tier".to_string(),
            vram_required: "0 GB (CPU)".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "Pure NumPy tensor calculations require 0 VRAM; run on any 4GB RAM laptop or Colab CPU.".to_string(),
            one_click_command: "python resume_matcher.py --top-k 5".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(2)),
    };

    Phase {
        id: 1,
        slug: "phase-1-foundations".to_string(),
        title: "Phase 1: Foundations of AI Engineering".to_string(),
        urdu_title: "Phase 1: AI Engineering Ki Bunyadi Maharat (Python & Tensors)".to_string(),
        week_range: "Weeks 1-4".to_string(),
        description: "Modern Python 3.12+, AsyncIO, memory profiling, NumPy vectorization, linear algebra intuition, gradients aur tensor memory layouts.".to_string(),
        outcome: "Aap raw Python aur NumPy se high-performance vector math operations aur data ingestion pipelines build karne ke qabil ho jayenge.".to_string(),
        modules: vec![m0, m1, m2],
    }
}

fn build_phase_2() -> Phase {
    let m3_script = r#"@preset midnight
@animate flow
flow LR: Classical Machine Learning Pipeline | Feature Engineering to Evaluation
raw[(Raw Features)] $db ~muted -> split{Train / Test Split}
split ->|80%| train[Training Set] ~info
split ->|20%| test[Holdout Test Set] ~teal
train -> pipe[Pipeline: Scaler + PCA + Model]* ~purple
pipe -> eval[Cross Validation // ROC-AUC & F1] ~teal
eval -> metric{Score >= Threshold?}
metric ->|Yes| deploy[Register Model] ~ok
metric ->|No| train"#;

    let m3 = Module {
        id: 3,
        phase_id: 2,
        slug: "classical-ml".to_string(),
        week: 5,
        title: "Classical Machine Learning & Scikit-Learn".to_string(),
        urdu_title: "Classical Machine Learning Aur Production Scikit-Learn".to_string(),
        description: "Supervised & Unsupervised learning, Gradient Boosted Trees (XGBoost/LightGBM), hyperparameter tuning, model validation aur metrics.".to_string(),
        diagram_script: m3_script.to_string(),
        diagram_svg: render_svg_or_fallback(m3_script),
        lessons: vec![
            Lesson {
                id: 301,
                module_slug: "classical-ml".to_string(),
                slug: "supervised-learning-core".to_string(),
                title: "Supervised Learning Core: Linear & Logistic Regression".to_string(),
                urdu_title: "Supervised Learning: Linear Aur Logistic Regression with L1/L2".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "So guys, dekhein: Har complex model se pehle baseline banana zaroori hai. Ridge (L2) weights ko shrink karta hai, jabke Lasso (L1) feature selection karke irrelevant weights ko bilkul zero kar deta hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Hamesha pehle simple baseline model train karein.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 302,
                module_slug: "classical-ml".to_string(),
                slug: "tree-models-ensembles".to_string(),
                title: "Decision Trees, Random Forests & XGBoost / LightGBM".to_string(),
                urdu_title: "Ensemble Models: Random Forests Aur High-Speed XGBoost".to_string(),
                duration_mins: 55,
                xp_reward: 100,
                explanation_urdu: "Tabular data par deep learning se zyada XGBoost aur LightGBM jeet-tay hain! Gradient Boosting har aglay tree ko pichlay trees ke errors par train karta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Gradient boosting residuals par iteratively train karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 303,
                module_slug: "classical-ml".to_string(),
                slug: "unsupervised-learning-clustering".to_string(),
                title: "Dimensionality Reduction & Clustering (PCA, t-SNE, K-Means)".to_string(),
                urdu_title: "Unsupervised Learning: PCA Dimensionality Reduction Aur K-Means".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Jab aapke paas 1000-dimensional embeddings hoon to unhe visualize kaise karein? PCA maximum variance ke axes dhoondta hai aur data ko 2D ya 3D mein project karta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["PCA linear projection hai jabke t-SNE non-linear neighborhood preserve karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 304,
                module_slug: "classical-ml".to_string(),
                slug: "model-validation-metrics".to_string(),
                title: "Rigorous Evaluation: Precision, Recall, F1 & ROC-AUC".to_string(),
                urdu_title: "Model Validation: Precision, Recall, F1 Score Aur ROC-AUC".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Imbalanced dataset mein sirf accuracy dekhna bewakoofi hai! Fraud detection mein agar 99% data non-fraud ho to 99% accuracy useless hai; wahan Recall aur Precision-Recall AUC dekhi jati hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Class imbalance mein F1-score aur Precision-Recall curves use karein.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 305,
                module_slug: "classical-ml".to_string(),
                slug: "feature-engineering-pipelines".to_string(),
                title: "Leakage-Free Feature Engineering & Sklearn Pipelines".to_string(),
                urdu_title: "Data Leakage Se Bachne Ke Liye Sklearn Pipelines Ka Istemaal".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Agar aapne test set ko scaler fit karne se pehle include kar liya to data leakage ho jayegi. Sklearn Pipeline ensure karti hai ke transformers sirf train data par fit hoon!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Pipeline fit_transform train par aur transform test par chalati hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 306,
                module_slug: "classical-ml".to_string(),
                slug: "module-3-capstone".to_string(),
                title: "Module 3 Capstone: Production Predictive ML Service".to_string(),
                urdu_title: "Capstone: End-to-End Tabular ML Model with Model Registry".to_string(),
                duration_mins: 60,
                xp_reward: 200,
                explanation_urdu: "Is project mein aap customer churn ka prediction model train karke MLflow registry mein log karenge aur serialized artifacts export karenge.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["End-to-end Classical ML system deployed.".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-3".to_string(),
            module_slug: "classical-ml".to_string(),
            title: "Classical ML & Model Evaluation Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "Why is accuracy a misleading metric for highly imbalanced datasets (e.g. 99% negative, 1% positive)?".to_string(),
                    urdu_question: "Imbalanced datasets par accuracy misleading kyun hoti hai?".to_string(),
                    options: vec![
                        "Because accuracy cannot be calculated on computers".to_string(),
                        "A naive model predicting 'negative' for all samples gets 99% accuracy while detecting zero positives".to_string(),
                        "Because accuracy only works for regression problems".to_string(),
                        "Because accuracy requires GPU acceleration".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Bilkul sahi! Agar 99% transactions normal hain to dummy model jo sab ko normal bolay ga wo bhi 99% accurate kehlayega, jabke saray fraud miss ho jayenge!".to_string(),
                },
            ],
        },
        resources: vec![],
        project: None,
        real_world_deliverable: Some("Upwork Client Churn & High-Value Lead Scoring Production Web Service".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Local CPU / Google Colab Free Tier".to_string(),
            vram_required: "0 GB (CPU)".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "Scikit-Learn and LightGBM train 100k rows in <15 seconds on Colab dual-core CPU.".to_string(),
            one_click_command: "pip install scikit-learn lightgbm fastapi && uvicorn app:app --port 8000".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(3)),
    };

    let m4_script = r#"@preset midnight
@animate wave
arch LR: Deep Learning Forward & Backward Pass | Computational Graph in PyTorch
x[Input Tensor x] ~purple -> lin1[Linear Layer // W1 . x + b1]
lin1 -> act[Activation // ReLU / GELU] ~info
act -> lin2[Linear Layer 2 // W2 . a + b2]
lin2 -> loss[Loss Computation // CrossEntropy]* ~danger
loss ==>|Autograd Backward| g2[Gradient dL/dW2] ~teal
g2 ==> g1[Gradient dL/dW1] ~teal
g1 ==> opt[AdamW Weight Update // W = W - lr x g]* ~ok"#;

    let m4 = Module {
        id: 4,
        phase_id: 2,
        slug: "deep-learning-pytorch".to_string(),
        week: 7,
        title: "Deep Learning Foundations & PyTorch from Scratch".to_string(),
        urdu_title: "Deep Learning Ki Bunyad Aur PyTorch Ka Mukammal Safar".to_string(),
        description: "Multi-layer Perceptrons, computational graphs, Autograd, custom training loops, optimizers (SGD, AdamW), aur GPU training best practices.".to_string(),
        diagram_script: m4_script.to_string(),
        diagram_svg: render_svg_or_fallback(m4_script),
        lessons: vec![
            Lesson {
                id: 401,
                module_slug: "deep-learning-pytorch".to_string(),
                slug: "perceptron-neural-nets".to_string(),
                title: "Perceptrons & Non-Linear Activation Functions (GELU, SwiGLU)".to_string(),
                urdu_title: "Perceptrons Aur Modern Non-Linear Activations (ReLU, GELU, SwiGLU)".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Agar neural network mein activation function na ho to 100 layers bhi ek single linear layer ban jati hain! Non-linearity network ko complex functions approximate karne ki taaqat deti hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Non-linearities jaise GELU aur SwiGLU modern LLMs mein standard hain.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 402,
                module_slug: "deep-learning-pytorch".to_string(),
                slug: "backprop-computational-graphs".to_string(),
                title: "Backpropagation & Dynamic Graphs with PyTorch Autograd".to_string(),
                urdu_title: "Computational Graphs Aur PyTorch Autograd Ka Dynamic Jadoo".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Jab aap `loss.backward()` call karte hain to PyTorch forward pass ke dauran banaye gaye graph par chain rule apply karke har leaf parameter ka `.grad` calculate kar leta hai.".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "PyTorch Autograd in Action".to_string(),
                    code: r#"import torch

# Create leaf tensor with gradient tracking
x = torch.tensor(3.0, requires_grad=True)
y = 2 * (x ** 2) + 5 * x - 1

# Backward pass applies chain rule
y.backward()

# dy/dx = 4*x + 5 = 4*(3) + 5 = 17.0
print(f"Gradient at x=3: {x.grad.item():.1f}")"#.to_string(),
                    explanation: "PyTorch automatically calculates exact analytical gradients without any numerical finite differences.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Autograd dynamic computational graphs maintain karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 403,
                module_slug: "deep-learning-pytorch".to_string(),
                slug: "loss-functions-optimizers".to_string(),
                title: "Loss Functions & Optimizers: AdamW vs SGD with Momentum".to_string(),
                urdu_title: "Loss Functions Aur Optimizers: AdamW Ka Decoupled Weight Decay".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "AdamW modern deep learning ka gold standard optimizer hai kyunke yeh adaptive learning rates aur decoupled weight decay ko combine karta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["AdamW L2 regularization ko gradient update se decouple karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 404,
                module_slug: "deep-learning-pytorch".to_string(),
                slug: "training-loop-engineering".to_string(),
                title: "Production Training Loops: Mixed Precision (AMP) & Checkpointing".to_string(),
                urdu_title: "Resilient PyTorch Training Loops: Mixed Precision (fp16/bf16) & AMP".to_string(),
                duration_mins: 55,
                xp_reward: 100,
                explanation_urdu: "`torch.cuda.amp.autocast()` use karne se matrix multiplications 16-bit precision par hoti hain, jiss se GPU memory aadhi aur training speed 2x ho jati hai bina accuracy lose kiye!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["AMP (Automatic Mixed Precision) GPU training speed aur memory dono optimize karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 405,
                module_slug: "deep-learning-pytorch".to_string(),
                slug: "regularization-batchnorm".to_string(),
                title: "Modern Regularization: LayerNorm, RMSNorm & Cosine Schedulers".to_string(),
                urdu_title: "Modern Regularization: BatchNorm vs LayerNorm vs RMSNorm".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Transformers mein BatchNorm fail ho jata hai kyunke sequence lengths dynamic hoti hain. Isliye LayerNorm aur RMSNorm use hote hain jo sequence dimension ke across normalize karte hain.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["RMSNorm LayerNorm se 10% fast hai kyunke mean shift skip karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 406,
                module_slug: "deep-learning-pytorch".to_string(),
                slug: "module-4-capstone".to_string(),
                title: "Module 4 Capstone: Custom Neural Engine from Raw Tensors".to_string(),
                urdu_title: "Capstone: Custom Neural Network Engine Built with Raw Tensors".to_string(),
                duration_mins: 60,
                xp_reward: 200,
                explanation_urdu: "Aap bina `nn.Module` ke raw tensors par custom forward pass, autograd hooks, aur AdamW step likhenge.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Deep learning fundamentals mastered!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-4".to_string(),
            module_slug: "deep-learning-pytorch".to_string(),
            title: "PyTorch & Deep Learning Core Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "Why is AdamW preferred over standard Adam for training modern deep neural networks?".to_string(),
                    urdu_question: "Modern neural networks train karne ke liye AdamW standard Adam se behtar kyun hai?".to_string(),
                    options: vec![
                        "AdamW is written in Rust".to_string(),
                        "AdamW correctly decouples weight decay from the gradient-based momentum update".to_string(),
                        "AdamW does not require a learning rate".to_string(),
                        "AdamW only works on CPUs".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Loshchilov & Hutter (2017) ne prove kiya ke standard Adam L2 regularization ko adaptive gradients ke sath mix karke weight decay distort kar deta tha; AdamW isay properly decouple karta hai.".to_string(),
                },
            ],
        },
        resources: vec![
            ResourceLink { title: "PyTorch Official Tutorials".to_string(), url: "https://pytorch.org/tutorials/".to_string(), resource_type: "Tutorials".to_string() }
        ],
        project: None,
        real_world_deliverable: Some("PyTorch Neural Financial Fraud Classifier & TensorBoard Telemetry".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Google Colab Free T4 (15GB VRAM)".to_string(),
            vram_required: "1.5 GB VRAM".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "Colab Free T4 handles 50,000 parameter PyTorch MLP in under 2 minutes. Call runtime.unassign() once finished.".to_string(),
            one_click_command: "!python train_fraud_detector.py --epochs 20 --device cuda".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(4)),
    };

    Phase {
        id: 2,
        slug: "phase-2-machine-learning".to_string(),
        title: "Phase 2: Machine Learning & Deep Learning Foundations".to_string(),
        urdu_title: "Phase 2: Modern Machine Learning Aur Deep Learning PyTorch".to_string(),
        week_range: "Weeks 5-8".to_string(),
        description: "Scikit-Learn, ensemble methods (XGBoost), model validation, PyTorch Autograd, custom training loops, optimizers aur mixed precision GPU execution.".to_string(),
        outcome: "Aap kisi bhi dataset par classical ML models aur deep neural networks ko scratch se train aur evaluate kar sakenge.".to_string(),
        modules: vec![m3, m4],
    }
}

fn build_phase_3() -> Phase {
    let m5_script = r#"@preset midnight
@animate ripple
flow LR: Vision Transformer (ViT) Architecture | Patches to Predictions
img[Input Image // 224x224x3] $file ~purple -> patch[Patch Extraction // 16x16 Patches]* ~info
patch -> proj[Linear Projection + Position Embeddings] ~teal
proj -> enc[Transformer Encoder Blocks x 12]* ~purple
enc -> cls[CLS Token Output] ~teal
cls -> mlp[MLP Classification Head] ~ok
mlp -> pred((Predicted Class)) ~ok"#;

    let m5 = Module {
        id: 5,
        phase_id: 3,
        slug: "computer-vision".to_string(),
        week: 9,
        title: "Computer Vision & Modern Visual Models".to_string(),
        urdu_title: "Modern Computer Vision: Convolutions Se Vision Transformers (ViT) Tak".to_string(),
        description: "2D Convolutions, ResNet residual bottlenecks, Vision Transformers (ViT), object detection (YOLO), aur data augmentations.".to_string(),
        diagram_script: m5_script.to_string(),
        diagram_svg: render_svg_or_fallback(m5_script),
        lessons: vec![
            Lesson {
                id: 501,
                module_slug: "computer-vision".to_string(),
                slug: "convolutions-feature-maps".to_string(),
                title: "2D Convolutions, Kernels, Padding & Stride Mechanics".to_string(),
                urdu_title: "2D Convolutions, Feature Maps Aur Receptive Field".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Convolutional filters image ke over slide karte hain aur edges, textures aur patterns extract karte hain. Weight sharing ki wajah se parameters MLP ke muqablay hazaron guna kam ho jate hain!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Convolutions spatial translation invariance provide karti hain.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 502,
                module_slug: "computer-vision".to_string(),
                slug: "classic-modern-cnns".to_string(),
                title: "ResNet Residual Skips & Modern ConvNeXt Architecture".to_string(),
                urdu_title: "Vanishing Gradients Ka Hal: ResNet Residual Connections".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "He et al. ne skip connections introduce keen `F(x) + x`. Agar deeper layers koi naya pattern na bhi seekhein to identity mapping pass ho jati hai, jiss se 152 layers ka network bhi train ho jata hai bina vanishing gradients ke!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Residual connections gradients ko uninterrupted flow hone deti hain.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 503,
                module_slug: "computer-vision".to_string(),
                slug: "vision-transformers-vit".to_string(),
                title: "Vision Transformers (ViT): Patches Are All You Need".to_string(),
                urdu_title: "Vision Transformers (ViT): Images Ko Tokens Samajh Kar Process Karna".to_string(),
                duration_mins: 55,
                xp_reward: 100,
                explanation_urdu: "ViT image ko 16x16 pixel patches mein kaat-ta hai aur har patch ko ek word token ki tarah embed karta hai! Phir standard transformer encoder global attention apply karta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["ViT global context captured karta hai bina receptive field restriction ke.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 504,
                module_slug: "computer-vision".to_string(),
                slug: "object-detection-segmentation".to_string(),
                title: "Object Detection (YOLO) & Semantic Segmentation".to_string(),
                urdu_title: "Real-Time Object Detection: YOLO Architecture & Bounding Boxes".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Classification sirf 'kya hai' batati hai, jabke Object Detection 'kahan hai' bhi batati hai. YOLO single forward pass mein bounding boxes aur class probabilities predict karta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Single-shot detectors sub-10ms real-time inference dete hain.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 505,
                module_slug: "computer-vision".to_string(),
                slug: "data-augmentation-transfer".to_string(),
                title: "Transfer Learning & Albumentations for Production CV".to_string(),
                urdu_title: "Transfer Learning Aur Albumentations Se Model Accuracy Barhana".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Pretrained weights (jaise ImageNet) se fine-tuning karne par choti datasets par bhi 95%+ accuracy hasil ho jati hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Transfer learning data scarcity ko solve karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 506,
                module_slug: "computer-vision".to_string(),
                slug: "module-5-capstone".to_string(),
                title: "Module 5 Capstone: Real-Time Defect Detection System".to_string(),
                urdu_title: "Capstone: Production Visual Inspection & Defect Detection".to_string(),
                duration_mins: 60,
                xp_reward: 200,
                explanation_urdu: "Aap ek ViT/YOLO pipeline deploy karenge jo live industrial camera feeds se defective parts ko classify aur localize karegi.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Computer vision system production ready!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-5".to_string(),
            module_slug: "computer-vision".to_string(),
            title: "Computer Vision & Transformers Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "How does a Vision Transformer (ViT) represent a 2D image as input to the standard Transformer Encoder?".to_string(),
                    urdu_question: "Vision Transformer (ViT) 2D image ko input tokens mein kaise convert karta hai?".to_string(),
                    options: vec![
                        "It runs 50 layers of convolutions first".to_string(),
                        "It flattens the image patches (e.g. 16x16) into a sequence of linear embeddings plus positional encodings".to_string(),
                        "It converts the image into an audio waveform".to_string(),
                        "It reads the file metadata only".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "ViT image ko 16x16 grid patches mein divide karke har patch ko linear projection matrix se token embedding vector mein map karta hai.".to_string(),
                },
            ],
        },
        resources: vec![],
        project: None,
        real_world_deliverable: Some("Urdu Handwritten Cheque OCR & Mobile Receipt Vision Scanner".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Google Colab Free T4 (15GB VRAM)".to_string(),
            vram_required: "4 GB VRAM".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "Use mixed precision torch.cuda.amp.autocast() to train ResNet-50 with 2x batch size on free T4.".to_string(),
            one_click_command: "!python train_cheque_ocr.py --arch resnet50 --fp16".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(5)),
    };

    let m6_script = r#"@preset midnight
@animate wave
arch LR: Modern Transformer Decoder Architecture | Generative Pre-training
tok[Token IDs] $code ~purple -> emb[Token + RoPE Rotary Embeddings] ~info
emb -> mha[Causal Multi-Head Attention // Scaled Dot-Product]* ~purple
mha -> norm1[RMSNorm & Residual Add] ~teal
norm1 -> ffn[SwiGLU Feed-Forward Network]* ~info
ffn -> norm2[RMSNorm & Residual Add] ~teal
norm2 -> head[Linear LM Head] ~teal
head -> sm[Softmax Next Token Probabilities]* ~ok"#;

    let m6 = Module {
        id: 6,
        phase_id: 3,
        slug: "nlp-transformers".to_string(),
        week: 10,
        title: "NLP & Modern Transformers".to_string(),
        urdu_title: "NLP Ki Duniya Aur Modern Transformer Architecture (Attention Is All You Need)".to_string(),
        description: "Tokenization (BPE), Scaled Dot-Product Attention, Multi-Head Attention, Rotary Positional Embeddings (RoPE), SwiGLU, aur Decoder-only LLM pre-training.".to_string(),
        diagram_script: m6_script.to_string(),
        diagram_svg: render_svg_or_fallback(m6_script),
        lessons: vec![
            Lesson {
                id: 601,
                module_slug: "nlp-transformers".to_string(),
                slug: "tokenization-bpe".to_string(),
                title: "Tokenization Deep Dive: Byte-Pair Encoding (BPE) & Tiktoken".to_string(),
                urdu_title: "Tokenization Deep Dive: BPE, WordPiece Aur Tiktoken Ka Tariqa-e-Kaar".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "LLMs text ko words ya characters mein nahi parhtay, balke subword tokens mein parhtay hain. BPE most frequent byte pairs ko merge karke fixed vocabulary banata hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["BPE out-of-vocabulary words ko subwords mein split kar deta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 602,
                module_slug: "nlp-transformers".to_string(),
                slug: "word-embeddings-sequence".to_string(),
                title: "Embeddings Evolution: From Word2Vec to Contextual Vectors".to_string(),
                urdu_title: "Word Embeddings Ka Safar: Static Vectors Se Contextual Representations Tak".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Word2Vec mein 'bank' (river bank vs money bank) ka ek hi vector hota tha. Transformer contextual embeddings generate karta hai jahan token ka vector uske surrounding words par depend karta hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Contextual embeddings polysemy (ek lafz ke muta'addid maani) solve karti hain.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 603,
                module_slug: "nlp-transformers".to_string(),
                slug: "self-attention-math".to_string(),
                title: "Scaled Dot-Product Attention: The Exact Mathematics".to_string(),
                urdu_title: "Scaled Dot-Product Attention: Formula Aur Dimensions Ka Detailed Math".to_string(),
                duration_mins: 55,
                xp_reward: 150,
                explanation_urdu: "`Attention(Q,K,V) = softmax((Q . K^T) / sqrt(d_k)) . V`. Square root of d_k se divide karna is liye zaroori hai kyunke high dimensions mein dot product bohot bara ho jata hai aur softmax gradients vanish ho jate hain!".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "PyTorch Causal Attention with Mask".to_string(),
                    code: r#"import torch
import torch.nn.functional as F

def causal_self_attention(Q, K, V):
    # Q, K, V shape: [B, H, S, d_k]
    d_k = Q.size(-1)
    seq_len = Q.size(-2)
    
    # 1. Scaled dot product
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    
    # 2. Lower-triangular causal mask so tokens cannot look into the future!
    mask = torch.tril(torch.ones(seq_len, seq_len, device=Q.device))
    scores = scores.masked_fill(mask == 0, float('-inf'))
    
    # 3. Softmax & matmul with V
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, V)"#.to_string(),
                    explanation: "Yeh causal self-attention implementation GPT family ke generative decoding ka core engine hai.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Causal mask future tokens ko mask karta hai taake generation autoregressive rahay.".to_string()],
                resources: vec![
                    ResourceLink { title: "Attention Is All You Need (Vaswani et al.)".to_string(), url: "https://arxiv.org/abs/1706.03762".to_string(), resource_type: "Paper".to_string() }
                ],
            },
            Lesson {
                id: 604,
                module_slug: "nlp-transformers".to_string(),
                slug: "multi-head-attention-arch".to_string(),
                title: "Multi-Head Attention & Rotary Positional Embeddings (RoPE)".to_string(),
                urdu_title: "Multi-Head Attention Aur Modern RoPE (Rotary Embeddings)".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Single head sirf ek tarah ka relation dekh sakta hai. 32 heads har head ko alag feature (syntax, grammar, entities, coreference) par focus karne ki azadi dete hain. RoPE relative positions ko complex plane mein rotate karke represent karta hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["RoPE relative positional information maintain karta hai long context windows mein.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 605,
                module_slug: "nlp-transformers".to_string(),
                slug: "encoder-decoder-paradigms".to_string(),
                title: "Architectural Paradigms: BERT vs GPT vs T5".to_string(),
                urdu_title: "Architectural Paradigms: Encoder-Only vs Decoder-Only vs Seq2Seq".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "BERT bidirectional encoder hai (classification ke liye best), GPT causal decoder hai (generation ke liye best). Aaj kal ke almost saray modern LLMs (Llama, Claude, GPT-4) decoder-only hain.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Decoder-only models scale better on autoregressive next-token prediction.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 606,
                module_slug: "nlp-transformers".to_string(),
                slug: "module-6-capstone".to_string(),
                title: "Module 6 Capstone: Build a Mini-GPT from Scratch in PyTorch".to_string(),
                urdu_title: "Capstone: Mini-GPT Decoder Scratch Se PyTorch Mein Banaein".to_string(),
                duration_mins: 75,
                xp_reward: 250,
                explanation_urdu: "Is grand capstone mein aap Andrej Karpathy ke nanoGPT style mein complete Decoder-only transformer block likhenge aur choti text dataset par train karke novel sentences generate karenge!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Full autoregressive LLM built and verified!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-6".to_string(),
            module_slug: "nlp-transformers".to_string(),
            title: "Transformers & Attention Mechanism Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "In scaled dot-product attention, why do we scale by dividing by sqrt(d_k)?".to_string(),
                    urdu_question: "Scaled dot-product attention mein sqrt(d_k) se divide kyun kiya jata hai?".to_string(),
                    options: vec![
                        "To prevent large magnitude dot products from pushing softmax into extremely small gradient regions".to_string(),
                        "To convert the attention scores into integer values".to_string(),
                        "To save GPU memory during the backward pass".to_string(),
                        "Because of Python floating point limitations".to_string(),
                    ],
                    correct_index: 0,
                    explanation_urdu: "Bilkul sahi! Jab d_k bara hota hai to dot product ka variance d_k ho jata hai, jiss se softmax outputs 0 ya 1 ho jati hain aur gradients vanish ho jate hain.".to_string(),
                },
                QuizQuestion {
                    id: 2,
                    question: "Why do autoregressive models like GPT use a causal attention mask?".to_string(),
                    urdu_question: "GPT jaisay generative models causal attention mask kyun use karte hain?".to_string(),
                    options: vec![
                        "To hide confidential data from the model".to_string(),
                        "To prevent tokens from attending to future tokens during next-token prediction".to_string(),
                        "To reduce the number of heads in the multi-head attention".to_string(),
                        "To compress the weights of the feedforward network".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Zabardast! Causal mask ensure karta hai ke position i par baitha token sirf i aur us se pehle ke tokens ko dekh sake, aagay ke nahi.".to_string(),
                },
            ],
        },
        resources: vec![
            ResourceLink { title: "The Illustrated Transformer by Jay Alammar".to_string(), url: "https://jalammar.github.io/illustrated-transformer/".to_string(), resource_type: "Visual Guide".to_string() }
        ],
        project: None,
        real_world_deliverable: Some("Roman Urdu BPE Tokenizer & FastText Semantic Sentiment Classifier".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Local CPU / Google Colab Free Tier".to_string(),
            vram_required: "0.5 GB VRAM / CPU".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "BPE vocabulary training on 50MB Roman Urdu text completes in 40s on standard CPU.".to_string(),
            one_click_command: "python train_bpe.py --input urdu_corpus.txt --vocab-size 32000".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(6)),
    };

    Phase {
        id: 3,
        slug: "phase-3-transformers-nlp".to_string(),
        title: "Phase 3: Transformers, NLP & Visual Architectures".to_string(),
        urdu_title: "Phase 3: Modern Transformers, NLP Aur Vision Models".to_string(),
        week_range: "Weeks 9-10".to_string(),
        description: "Vision Transformers (ViT), object detection, Byte-Pair Encoding, Scaled Dot-Product Attention, Multi-Head Attention, RoPE aur Mini-GPT decoder implementation.".to_string(),
        outcome: "Aap SOTA Transformer architecture ko mathematical depth aur PyTorch implementation ke sath mukammal master kar lenge.".to_string(),
        modules: vec![m5, m6],
    }
}

fn build_phase_4() -> Phase {
    let m7_script = r#"@preset midnight
@animate glow
seq: Enterprise LLM Structured Output Flow
u: Client Application
p: System Prompt & Schema*
m: LLM Engine
v: JSON Schema Validator
u -> p: Send User Query
p -> m: Inject Few-Shot CoT & JSON Schema
m --> v: Stream Candidate Tokens
v -> v: Validate against Pydantic Spec
v --> u: Guaranteed Valid Typed Response"#;

    let m7 = Module {
        id: 7,
        phase_id: 4,
        slug: "llm-prompt-engineering".to_string(),
        week: 11,
        title: "LLM Architecture & Prompt Engineering".to_string(),
        urdu_title: "LLMs Ki Architecture Aur Production Prompt Engineering".to_string(),
        description: "Modern SOTA LLMs, Chain-of-Thought, ReAct prompting, Structured JSON Outputs with Instructor/Pydantic, KV Caching, aur LLM-as-a-Judge evaluation.".to_string(),
        diagram_script: m7_script.to_string(),
        diagram_svg: render_svg_or_fallback(m7_script),
        lessons: vec![
            Lesson {
                id: 701,
                module_slug: "llm-prompt-engineering".to_string(),
                slug: "modern-llm-landscapes".to_string(),
                title: "Modern LLM Landscape: Open Weights vs Frontier Models".to_string(),
                urdu_title: "Modern LLMs Ka Maidan: Llama 3, Claude 3.5 Sonnet, DeepSeek & Mistral".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Frontier proprietary models (Claude 3.5 Sonnet) reasoning mein lead karte hain jabke Open-weights models (Llama 3.3 70B, DeepSeek V3) local deployment aur privacy ke liye best hain.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Har use case ke hisab se model size aur latency trade-off evaluate karein.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 702,
                module_slug: "llm-prompt-engineering".to_string(),
                slug: "prompt-patterns-cot".to_string(),
                title: "Chain-of-Thought (CoT), Few-Shot & In-Context Learning".to_string(),
                urdu_title: "Reasoning Boost: Chain-of-Thought (CoT) Aur Few-Shot Prompt Patterns".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Jab aap model ko bolte hain 'Think step by step before answering', to model intermediate tokens generate karta hai jo aglay reasoning steps ke liye computation buffer ban jate hain!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["CoT prompt intermediate computational scratchpad provide karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 703,
                module_slug: "llm-prompt-engineering".to_string(),
                slug: "structured-json-outputs".to_string(),
                title: "Guaranteed Structured Outputs with JSON Schema & Instructor".to_string(),
                urdu_title: "Production Structured Outputs: Pydantic Aur Instructor Ka Istemaal".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Production systems mein unstructured text parse karna suicide hai! Instructor library Pydantic schemas enforce karti hai aur token level par invalid JSON syntax generate hone hi nahi deti.".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "Pydantic Structured Output with Instructor".to_string(),
                    code: r#"from pydantic import BaseModel, Field
from typing import List

class ExtractedEntities(BaseModel):
    people: List[str] = Field(description="Names of people mentioned")
    organizations: List[str] = Field(description="Companies or institutions")
    sentiment: str = Field(description="Overall sentiment: Positive, Neutral, Negative")

# Guaranteed typed schema directly from LLM API"#.to_string(),
                    explanation: "Pydantic model LLM output ko runtime par validate karke 100% typed Python object deta hai.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Grammar-based sampling ensures zero schema violation.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 704,
                module_slug: "llm-prompt-engineering".to_string(),
                slug: "context-window-kv-cache".to_string(),
                title: "KV Cache Mechanics & Long Context Windows".to_string(),
                urdu_title: "KV Cache Ki Working: In-Memory Key-Value Reuse".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Autoregressive generation mein har naye token par pichlay saray tokens ka K aur V dobara calculate nahi hota, balke GPU VRAM mein KV Cache ki soorat mein store rehta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["KV Cache generation speed ko O(N^2) se O(N) laata hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 705,
                module_slug: "llm-prompt-engineering".to_string(),
                slug: "evaluation-benchmarking".to_string(),
                title: "LLM Evaluation & Benchmarking: LLM-as-a-Judge".to_string(),
                urdu_title: "Automated Evaluation: LLM-as-a-Judge Aur Ragas Framework".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Insaan hazaron responses manually check nahi kar sakte. Ek powerful frontier model (jaise Claude 3.5 Sonnet) ko structured rubric de kar candidate outputs ko grade karwaya jata hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Clear scoring rubrics prompt judge model ko deterministic banati hain.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 706,
                module_slug: "llm-prompt-engineering".to_string(),
                slug: "module-7-capstone".to_string(),
                title: "Module 7 Capstone: Enterprise Prompt Optimization Suite".to_string(),
                urdu_title: "Capstone: Automated Prompt Tuning & Regression Testing Engine".to_string(),
                duration_mins: 60,
                xp_reward: 200,
                explanation_urdu: "Aap ek CI/CD pipeline banayenge jo har prompt change par 100 benchmark queries par automated eval run karegi aur regression report degi.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Prompt engineering operationalized!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-7".to_string(),
            module_slug: "llm-prompt-engineering".to_string(),
            title: "Prompt Engineering & Structured Output Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "What is the primary function of the KV Cache during autoregressive text generation?".to_string(),
                    urdu_question: "Text generation ke dauran KV Cache ka asal maqsad kya hai?".to_string(),
                    options: vec![
                        "To translate words into Urdu",
                        "To store past Keys and Values in VRAM so they don't need recomputation on every new token",
                        "To compress the weights of the model onto disk",
                        "To connect to the database",
                    ].into_iter().map(|s| s.to_string()).collect(),
                    correct_index: 1,
                    explanation_urdu: "Sahi! KV cache pichlay tokens ke computed Key aur Value vectors ko save rakhta hai taake har naye token par sirf naya vector compute ho.".to_string(),
                },
            ],
        },
        resources: vec![],
        project: None,
        real_world_deliverable: Some("Roman Urdu Mini-GPT Decoder & Interactive Attention Weight Heatmap".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Google Colab Free T4 (15GB VRAM)".to_string(),
            vram_required: "6 GB VRAM".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "Enable FlashAttention-2 or PyTorch SDPA (scaled_dot_product_attention) for 3x memory reduction.".to_string(),
            one_click_command: "!python train_mini_gpt.py --seq-len 512 --batch-size 16".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(7)),
    };

    let m8_script = r#"@preset midnight
@animate flow
flow LR: Vector Database Semantic Search & HNSW Indexing
doc[Document Chunk] $file ~purple -> emb[Embedding Model // bge-m3]* $ai
emb -> vec[Dense Vector // 1024-dim] ~teal
vec -> hnsw[(HNSW Vector Index // pgvector / Qdrant)]* $db ~info
query[User Query] $user ~purple -> q_emb[Query Embedding] $ai
q_emb -> sim{Approximate Nearest Neighbor (ANN)}
hnsw -> sim
sim -> res[Top-K Nearest Document Chunks] ~ok"#;

    let m8 = Module {
        id: 8,
        phase_id: 4,
        slug: "vector-databases".to_string(),
        week: 12,
        title: "Embeddings, Vector Databases & Semantic Search".to_string(),
        urdu_title: "Embeddings, Vector Databases Aur Semantic Search Ki Architecture".to_string(),
        description: "Dense Embeddings (bge-m3), Distance Metrics, HNSW vs IVF indexing, pgvector in PostgreSQL, Qdrant, aur high-throughput vector retrieval.".to_string(),
        diagram_script: m8_script.to_string(),
        diagram_svg: render_svg_or_fallback(m8_script),
        lessons: vec![
            Lesson {
                id: 801,
                module_slug: "vector-databases".to_string(),
                slug: "embedding-models-geometry".to_string(),
                title: "SOTA Embedding Models & High-Dimensional Geometry".to_string(),
                urdu_title: "Modern Embedding Models (bge-m3, text-embedding-3) Aur High-Dim Space".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "1536-dimensional space mein 'Curse of Dimensionality' activate ho jati hai: saray points lagbhag barabar doori par mehsoos hotay hain. Isliye normalized cosine similarity use ki jati hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Unit norm embeddings par dot product exact cosine similarity ke barabar hota hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 802,
                module_slug: "vector-databases".to_string(),
                slug: "distance-metrics-similarity".to_string(),
                title: "Distance Metrics: Cosine vs Inner Product vs Euclidean (L2)".to_string(),
                urdu_title: "Distance Metrics Ka Muqabla: Cosine vs Dot Product vs Euclidean L2".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Agar aapki embeddings already unit-normalized hoon to Inner Product (dot product) calculate karna Euclidean distance se 3x fast hota hai kyunke square root calculate nahi karna parta!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Normalized vectors par Inner Product fastest distance metric hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 803,
                module_slug: "vector-databases".to_string(),
                slug: "vector-indexing-hnsw".to_string(),
                title: "HNSW (Hierarchical Navigable Small World) Graph Indexing".to_string(),
                urdu_title: "ANN Search Ka King: HNSW Graph Indexing Kaise Kaam Karti Hai".to_string(),
                duration_mins: 55,
                xp_reward: 150,
                explanation_urdu: "Linear scan (exhaustive search) O(N) slow hai. HNSW skip-list jaisa multi-layer proximity graph banata hai jo O(log N) time mein nearest neighbors tak pohnch jata hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["HNSW graph logarithmic retrieval time aur >98% recall provide karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 804,
                module_slug: "vector-databases".to_string(),
                slug: "pgvector-postgresql".to_string(),
                title: "Native Vector Search with PostgreSQL & pgvector".to_string(),
                urdu_title: "PostgreSQL Mein Vector Search: pgvector Extension Aur HNSW Indexes".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Naya vector DB seekhne se pehle dekhein: PostgreSQL mein `CREATE EXTENSION vector;` chala kar standard relational data aur embeddings ko ek hi table mein store aur join kiya ja sakta hai!".to_string(),
                code_snippet: Some(CodeSnippet {
                    language: "sql".to_string(),
                    title: "pgvector HNSW Index Creation in SQL".to_string(),
                    code: r#"CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE document_embeddings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content TEXT NOT NULL,
    embedding vector(1536) NOT NULL
);

-- Build high-speed HNSW index with Cosine distance
CREATE INDEX ON document_embeddings 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- Query top-5 most similar chunks
SELECT content, 1 - (embedding <=> '[0.012, -0.045, ...]') AS similarity
FROM document_embeddings
ORDER BY embedding <=> '[0.012, -0.045, ...]'
LIMIT 5;"#.to_string(),
                    explanation: "`<=>` cosine distance operator hai aur HNSW index sub-millisecond query search deta hai.".to_string(),
                }),
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["pgvector relational queries aur vector search ko seamless integrate karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 805,
                module_slug: "vector-databases".to_string(),
                slug: "specialized-vector-dbs".to_string(),
                title: "Specialized Vector DBs: Qdrant vs Milvus vs Pinecone".to_string(),
                urdu_title: "Standalone Vector Databases: Qdrant (Rust) Aur Milvus Ka Muqabla".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Jab billions of vectors aur heavy real-time filtering ho to Qdrant (Rust-based) ya Milvus use hote hain jo memory-mapped payload filtering provide karte hain.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Qdrant payload index vectors ke sath boolean metadata filters accelerate karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 806,
                module_slug: "vector-databases".to_string(),
                slug: "module-8-capstone".to_string(),
                title: "Module 8 Capstone: Multi-Tenant Vector Search Service".to_string(),
                urdu_title: "Capstone: High-Performance Multi-Tenant Semantic Search Engine".to_string(),
                duration_mins: 60,
                xp_reward: 200,
                explanation_urdu: "Is capstone mein aap ek API banayenge jo different organization IDs ke mutabiq isolated vector search execute karegi.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Multi-tenant vector search deployed!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-8".to_string(),
            module_slug: "vector-databases".to_string(),
            title: "Vector Databases & HNSW Indexing Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "What is the time complexity of searching nearest neighbors in an HNSW graph index?".to_string(),
                    urdu_question: "HNSW graph index mein nearest neighbor search ki time complexity kya hoti hai?".to_string(),
                    options: vec![
                        "O(N) linear time".to_string(),
                        "O(log N) logarithmic time".to_string(),
                        "O(N^2) quadratic time".to_string(),
                        "O(1) constant time".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Sahi jawab! HNSW multi-layered skip-list architecture use karta hai jo O(log N) time complexity deta hai.".to_string(),
                },
            ],
        },
        resources: vec![],
        project: None,
        real_world_deliverable: Some("Pakistani Legal Contract & Bank Statement Hybrid RAG (pgvector + BM25 + ColPali)".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Supabase Free Tier (pgvector) + Groq / Gemini Flash Free Tier".to_string(),
            vram_required: "0 GB (Hosted Cloud API & Supabase)".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "Generate text-embedding-3 or BGE embeddings via serverless endpoints, store in free Supabase PostgreSQL.".to_string(),
            one_click_command: "cargo run --bin hybrid_rag_ingest -- --pdf sample_contract.pdf".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(8)),
    };

    Phase {
        id: 4,
        slug: "phase-4-prompt-and-vectors".to_string(),
        title: "Phase 4: LLM Architecture, Prompting & Vector Databases".to_string(),
        urdu_title: "Phase 4: LLM Prompt Engineering Aur Vector Databases".to_string(),
        week_range: "Weeks 11-12".to_string(),
        description: "Frontier LLM prompting, Structured Outputs with Pydantic/Instructor, KV Caching, SOTA Embeddings, HNSW indexing, aur pgvector in PostgreSQL.".to_string(),
        outcome: "Aap 100% reliable structured LLM outputs generate karne aur enterprise vector search architectures khari karne ke mahir ban jayenge.".to_string(),
        modules: vec![m7, m8],
    }
}

fn build_phase_5() -> Phase {
    let m9_script = r#"@preset midnight
@animate flow
arch LR: Production Hybrid RAG Architecture | Zero Hallucination Retrieval
q[User Query] $user ~purple -> embed[Embedding Model // text-embedding-3]* $ai
q -> bm25[BM25 Keyword Search] ~teal
embed -> vdb[(Vector Database // pgvector / Qdrant)] $db ~info
vdb ->|Dense Retrieval| rrf[Hybrid Fusion & Re-Ranker // Cohere Rerank v3]* $bolt
bm25 ->|Sparse Retrieval| rrf
rrf -> ctx[Top-K Context Chunks] ~teal
ctx -> prompt[System Prompt + Context Builder]
q --> prompt
prompt -> llm[[LLM Generator // Claude / GPT-4o / Llama 3]] $ai ~purple
llm -> out((Grounded Answer + Citations)) ~ok
group Retrieval: vdb bm25 rrf"#;

    let m9 = Module {
        id: 9,
        phase_id: 5,
        slug: "production-rag".to_string(),
        week: 13,
        title: "Production RAG Architectures".to_string(),
        urdu_title: "Production RAG: Hybrid Search, Re-Ranking Aur Zero Hallucination".to_string(),
        description: "Document parsing, Semantic chunking, Hybrid Search (Dense + BM25), Reciprocal Rank Fusion (RRF), Cross-Encoder Re-ranking, HyDE, aur GraphRAG.".to_string(),
        diagram_script: m9_script.to_string(),
        diagram_svg: render_svg_or_fallback(m9_script),
        lessons: vec![
            Lesson {
                id: 901,
                module_slug: "production-rag".to_string(),
                slug: "chunking-preprocessing".to_string(),
                title: "Advanced Document Parsing & Semantic Chunking".to_string(),
                urdu_title: "Document Parsing: Unstructured/Docling Aur Semantic Chunking".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Fixed-character chunking lafzon ko beech mein se kaat deti hai. Semantic chunking sentence similarity check karti hai aur jab topic change hota hai tab chunk split karti hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Semantic chunking chunk boundaries par context preserve karti hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 902,
                module_slug: "production-rag".to_string(),
                slug: "hybrid-search-rrf".to_string(),
                title: "Hybrid Search: Dense Vectors + Sparse BM25 with RRF".to_string(),
                urdu_title: "Hybrid Search: Dense Semantic Vectors Aur Sparse BM25 Keyword Search".to_string(),
                duration_mins: 55,
                xp_reward: 150,
                explanation_urdu: "Dense vector search acronyms aur exact part numbers (jaise 'SKU-9821') par fail ho jati hai! Hybrid search BM25 exact matching aur vector semantic matching ko RRF se merge karti hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Hybrid search dense + sparse dono ke benefits combine karti hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 903,
                module_slug: "production-rag".to_string(),
                slug: "cross-encoder-reranking".to_string(),
                title: "Cross-Encoder Re-ranking (Cohere & FlashRank)".to_string(),
                urdu_title: "Cross-Encoder Re-ranking: Chunks Ki Asal Relevance Verify Karna".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Bi-encoders fast hotay hain lekin query aur document ko alag encode karte hain. Cross-encoder query aur chunk ko ek sath padh kar cross-attention calculate karta hai, jiss se top-3 chunks 100% relevant hotay hain!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Re-ranking retrieval quality ko 20-30% boost karti hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 904,
                module_slug: "production-rag".to_string(),
                slug: "query-transformation-hyde".to_string(),
                title: "Query Transformations: HyDE, Multi-Query & Step-Back".to_string(),
                urdu_title: "Query Transformations: Hypothetical Document Embeddings (HyDE)".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "User ka sawal chota aur vague hota hai. HyDE model se kehta hai ke pehle ek hypothetical jawab likhay, aur us jawab ki embedding se chunks dhoonday! Retrieval accuracy skyrocket ho jati hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["HyDE query-to-document space mismatch ko bridge karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 905,
                module_slug: "production-rag".to_string(),
                slug: "advanced-rag-patterns".to_string(),
                title: "Self-RAG, Corrective RAG (CRAG) & GraphRAG".to_string(),
                urdu_title: "Advanced RAG: Self-RAG, Corrective RAG Aur Knowledge Graph RAG".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Agar retrieved chunks ghalat hoon to? Corrective RAG pehle relevance check karta hai; agar irrelevant hoon to web search par fallback karta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Self-reflective loops hallucination ko production mein prevent karte hain.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 906,
                module_slug: "production-rag".to_string(),
                slug: "module-9-capstone".to_string(),
                title: "Module 9 Capstone: Enterprise Zero-Hallucination RAG".to_string(),
                urdu_title: "Capstone: Production Enterprise RAG with Verifiable Citations".to_string(),
                duration_mins: 65,
                xp_reward: 200,
                explanation_urdu: "Aap ek end-to-end RAG system ship karenge jo financial reports parse karega aur har claim ke sath exact page number aur snippet citation dega.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Production enterprise RAG live!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-9".to_string(),
            module_slug: "production-rag".to_string(),
            title: "Production RAG Architectures Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "Why does Hybrid Search (Dense + Sparse BM25) outperform pure Dense Vector search?".to_string(),
                    urdu_question: "Hybrid Search (Dense + BM25) akeli vector search se behtar kyun hoti hai?".to_string(),
                    options: vec![
                        "Because BM25 uses neural network transformers".to_string(),
                        "Because BM25 captures exact keywords and identifiers that vector models often miss".to_string(),
                        "Because BM25 reduces GPU electricity consumption".to_string(),
                        "Because BM25 translates languages".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Dense vectors semantic meaning samajhte hain lekin exact part numbers, IDs, aur rare terms ko blur kar dete hain; BM25 exact match karta hai.".to_string(),
                },
            ],
        },
        resources: vec![],
        project: None,
        real_world_deliverable: Some("Unsloth 4-bit QLoRA & DeepSeek-R1 GRPO Fine-Tuning on Free Colab T4".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Google Colab Free T4 (15GB VRAM) / Kaggle Dual-T4 (30h/wk)".to_string(),
            vram_required: "7.5 GB VRAM (Llama 3 8B 4-bit)".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "Unsloth Triton kernels allow 4-bit QLoRA fine-tuning on a 15GB T4. Wrap script in try/finally runtime.unassign()!".to_string(),
            one_click_command: "!pip install 'unsloth[colab-new]' && python train_qlora.py".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(9)),
    };

    let m10_script = r#"@preset midnight
@animate glow
arch LR: LoRA Matrix Decomposition | Low-Rank Adaptation (PEFT)
x[Input Activation x // dim d] ~purple -> w0[Frozen Base Weights W0 // d x k]* ~muted
x -> a[LoRA Matrix A // d x r, Gaussian Init] ~info
a -> b[LoRA Matrix B // r x k, Zero Init]* ~teal
w0 -> add((+))
b -> scale[Scaling // alpha / r] -> add
add -> y[Output Activation y // dim k] ~ok"#;

    let m10 = Module {
        id: 10,
        phase_id: 5,
        slug: "llm-fine-tuning".to_string(),
        week: 14,
        title: "Fine-Tuning LLMs (PEFT, LoRA & QLoRA)".to_string(),
        urdu_title: "LLM Fine-Tuning: PEFT, LoRA, QLoRA Aur DPO Alignment".to_string(),
        description: "Fine-tuning vs Prompting trade-offs, Instruction dataset curation, LoRA low-rank decomposition math, QLoRA NF4 quantization, aur Direct Preference Optimization (DPO).".to_string(),
        diagram_script: m10_script.to_string(),
        diagram_svg: render_svg_or_fallback(m10_script),
        lessons: vec![
            Lesson {
                id: 1001,
                module_slug: "llm-fine-tuning".to_string(),
                slug: "fine-tuning-vs-rag".to_string(),
                title: "When to Fine-Tune vs When to use RAG".to_string(),
                urdu_title: "Faisla Kaise Karein: Fine-Tuning Kab Karni Hai Aur RAG Kab Use Karna Hai".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Rule of thumb: Nayi facts aur information sikhane ke liye RAG use karein. Model ka tone, style, specific format, ya reasoning behaviour badalne ke liye Fine-Tuning use karein!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["RAG is for knowledge retrieval; Fine-tuning is for behavioral adaptation.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1002,
                module_slug: "llm-fine-tuning".to_string(),
                slug: "dataset-curation-formatting".to_string(),
                title: "Instruction Dataset Curation & ChatML Formatting".to_string(),
                urdu_title: "Instruction Datasets: Quality Filtering Aur ChatML Format".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Quality > Quantity! 1,000 clean, human-verified instruction pairs 100,000 noisy samples se behtar model produce karte hain. Tokenizer ke chat template ko hamesha follow karein.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Clean data formatting prevents training divergence.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1003,
                module_slug: "llm-fine-tuning".to_string(),
                slug: "peft-lora-deep-dive".to_string(),
                title: "LoRA Mathematics: Low-Rank Matrix Decomposition".to_string(),
                urdu_title: "LoRA Ka Mathematical Deep Dive: Low-Rank Matrix Decomposition".to_string(),
                duration_mins: 55,
                xp_reward: 150,
                explanation_urdu: "`W = W0 + (alpha/r) * (B x A)`. Matrix A random Gaussian se initialize hoti hai aur Matrix B zero se. Is se training ke pehle step par output bilkul base model jaisi rehti hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["LoRA rank r=16 99% accuracy retain karti hai with 0.1% parameters.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1004,
                module_slug: "llm-fine-tuning".to_string(),
                slug: "qlora-quantization-bitsandbytes".to_string(),
                title: "QLoRA: 4-Bit NormalFloat (NF4) & Double Quantization".to_string(),
                urdu_title: "QLoRA: 4-Bit NormalFloat Quantization Aur Single GPU Fine-Tuning".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "QLoRA base model ko 4-bit NormalFloat (NF4) par compress karta hai aur gradients 16-bit LoRA adapters mein flow karate hain. Ek 16GB consumer GPU par 8B model fine-tune ho jata hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["QLoRA enables high-quality fine-tuning on consumer hardware.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1005,
                module_slug: "llm-fine-tuning".to_string(),
                slug: "dpo-rlhf-alignment".to_string(),
                title: "Alignment & Preference Tuning: DPO vs RLHF".to_string(),
                urdu_title: "Model Alignment: Direct Preference Optimization (DPO)".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "RLHF bohot unstable hota tha kyunke us mein separate reward model train karna parta tha. DPO direct cross-entropy style loss se model ko human preferred responses ki taraf align karta hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["DPO simplifies preference optimization without complex RL loops.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1006,
                module_slug: "llm-fine-tuning".to_string(),
                slug: "module-10-capstone".to_string(),
                title: "Module 10 Capstone: Fine-Tune & Export Custom Domain LLM".to_string(),
                urdu_title: "Capstone: Domain-Specific Llama 3 Fine-Tune Aur Weights Merge Karna".to_string(),
                duration_mins: 70,
                xp_reward: 200,
                explanation_urdu: "Aap Roman Urdu medical advice ya legal assistant data par LoRA train karenge aur adapters ko base model mein merge karke GGUF/vLLM format mein export karenge.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Custom fine-tuned LLM ready for serving!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-10".to_string(),
            module_slug: "llm-fine-tuning".to_string(),
            title: "LoRA & PEFT Fine-Tuning Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "In LoRA, how is the adapter matrix B initialized at the start of training?".to_string(),
                    urdu_question: "LoRA training ke aaghaz par Matrix B ko kis tarah initialize kiya jata hai?".to_string(),
                    options: vec![
                        "With random large integers".to_string(),
                        "With all zeros, ensuring Delta W is zero initially so output matches the base model".to_string(),
                        "With an identity matrix".to_string(),
                        "With the weights of the input embeddings".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Matrix B ko zero initialize karne se initial Delta W = B x A = 0 hota hai, jiss se training shuru hote hi model random outputs nahi deta.".to_string(),
                },
            ],
        },
        resources: vec![],
        project: None,
        real_world_deliverable: Some("Autonomous Freelance Upwork Job Scraper & Proposal Generator with Anthropic MCP & smolagents".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Groq Free Tier (Llama 3.3 70B @ 350 tok/s) / Local CPU Sandbox".to_string(),
            vram_required: "0 GB (Cloud LLM API)".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "smolagents executes Python tools locally on CPU while querying Groq API at 350 tokens/sec for free.".to_string(),
            one_click_command: "python upwork_agent.py --query 'Rust Backend Engineer'".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(10)),
    };

    let m11_script = r#"@preset midnight
@animate pulse
flow TB: Autonomous AI Agent ReAct Loop | Reasoning + Acting Cycle
user[User Goal / Task] $user ~purple -> thought[1. Thought // Reasoning & Plan]* $ai
thought -> action[2. Action // Select Tool & Args] ~info
action -> exec[3. Tool Execution // Search, DB, API, Python] $gear ~teal
exec -> obs[4. Observation // Raw Tool Result] ~teal
obs -> reflect{Goal Achieved?}*
reflect ->|No - Need more info| thought
reflect ->|Yes - Completed| final((5. Final Answer & Deliverable)) ~ok"#;

    let m11 = Module {
        id: 11,
        phase_id: 5,
        slug: "autonomous-agents".to_string(),
        week: 15,
        title: "Autonomous AI Agents (ReAct, LangGraph & Tools)".to_string(),
        urdu_title: "Autonomous AI Agents: ReAct Loops, Tool Calling Aur LangGraph".to_string(),
        description: "ReAct patterns, Native function calling specs, error recovery, cyclic workflows with LangGraph, multi-agent collaboration, aur human-in-the-loop approval.".to_string(),
        diagram_script: m11_script.to_string(),
        diagram_svg: render_svg_or_fallback(m11_script),
        lessons: vec![
            Lesson {
                id: 1101,
                module_slug: "autonomous-agents".to_string(),
                slug: "agentic-architecture-patterns".to_string(),
                title: "Agentic Architecture: Memory, Tools, Planning & Execution".to_string(),
                urdu_title: "AI Agent Ka Brain: Memory, Tool Use, Planning Aur Reflection".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "AI Agent sirf sawal ka jawab nahi deta, balke complex goals ko sub-tasks mein split karta hai, tools call karta hai, aur errors aane par khud ko self-correct karta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Autonomous agents interact with real-world environments through tools.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1102,
                module_slug: "autonomous-agents".to_string(),
                slug: "function-calling-specs".to_string(),
                title: "Function & Tool Calling Specifications (OpenAPI & JSON Schema)".to_string(),
                urdu_title: "Function Calling: Tools Define Karna Aur Arguments Validate Karna".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Model tool ka code run nahi karta; model sirf JSON arguments produce karta hai. Aapka application server tool ko securely execute karke output model ko observation ke tor par return karta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Strict JSON schemas prevent invalid tool invocations.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1103,
                module_slug: "autonomous-agents".to_string(),
                slug: "react-loops-self-correction".to_string(),
                title: "ReAct Loops & Deterministic Error Recovery".to_string(),
                urdu_title: "ReAct Loop: Thought, Action, Observation Aur Self-Correction".to_string(),
                duration_mins: 55,
                xp_reward: 150,
                explanation_urdu: "Agar tool call error de (e.g. 404 Not Found), to ReAct agent crash nahi hota balke observation read karke alternative parameters ya alternative tool try karta hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Self-healing retry logic robust agents ki pehchan hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1104,
                module_slug: "autonomous-agents".to_string(),
                slug: "graph-based-workflows".to_string(),
                title: "Stateful Cyclic Graphs with LangGraph".to_string(),
                urdu_title: "LangGraph: Cyclic State Machines Aur Checkpointed Memory".to_string(),
                duration_mins: 55,
                xp_reward: 150,
                explanation_urdu: "Chains linear hoti hain; real agents ko loops aur cycles chahiye hotay hain! LangGraph state ko graph nodes aur conditional edges ke zariye persist karta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["LangGraph state persistence aur cycles support karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1105,
                module_slug: "autonomous-agents".to_string(),
                slug: "multi-agent-collaboration".to_string(),
                title: "Multi-Agent Systems: Supervisor, Worker & Critique".to_string(),
                urdu_title: "Multi-Agent Architecture: Supervisor, Worker Aur Critique Patterns".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Ek hi prompt mein sab kuch daalne ke bajaye specialised agents banayein: Coder Agent code likhega, Reviewer Agent critique karega, aur Test Agent verify karega.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Role specialization multi-agent accuracy ko double kar deti hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1106,
                module_slug: "autonomous-agents".to_string(),
                slug: "module-11-capstone".to_string(),
                title: "Module 11 Capstone: Autonomous Code Bug-Fixing Agent".to_string(),
                urdu_title: "Capstone: Autonomous Bug-Fixing & Testing Agent".to_string(),
                duration_mins: 70,
                xp_reward: 200,
                explanation_urdu: "Aap ek agent banayenge jo GitHub issue read karega, repository mein failing test run karega, code patch likhega, test dobara chala kar verify karega aur PR generate karega!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Autonomous coding agent shipped!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-11".to_string(),
            module_slug: "autonomous-agents".to_string(),
            title: "Autonomous Agents & Tool Calling Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "What are the four core phases of the ReAct agent loop?".to_string(),
                    urdu_question: "ReAct agent loop ke 4 bunyadi steps kon se hain?".to_string(),
                    options: vec![
                        "Compile, Run, Debug, Release".to_string(),
                        "Thought (Reasoning), Action (Tool Call), Observation (Result), and Reflection (Evaluation)".to_string(),
                        "Vectorize, Index, Search, Retrieve".to_string(),
                        "Tokenize, Embed, Transpose, Softmax".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "ReAct (Yao et al.) Thought -> Action -> Observation -> Reflection loop par mabni hai.".to_string(),
                },
            ],
        },
        resources: vec![],
        project: None,
        real_world_deliverable: Some("Sub-50ms Rust Axum High-Scale AI Gateway with Semantic Caching & Rate Limiting".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Local Docker / Fly.io Free Tier / Render".to_string(),
            vram_required: "0 GB (CPU Gateway)".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "Compiled Rust Axum binary consumes only 12MB RAM and handles 25,000 req/sec on a single vCPU.".to_string(),
            one_click_command: "cargo run --release".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(11)),
    };

    let m12_script = r#"@preset midnight
@animate ripple
arch LR: Vision-Language Multimodal Architecture | Cross-Attention & Alignment
img[Image Input] $file ~purple -> vis[Vision Encoder // SigLIP / CLIP] ~teal
vis -> proj[Multimodal Projection Adapter // MLP]* ~info
text[Prompt Text] $code ~purple -> tok[Text Tokenizer & Embeddings] ~teal
proj -> fusion((Cross-Modal Concatenation))
tok -> fusion
fusion -> llm[[Multimodal LLM Backbone // Llama 3.2 Vision]]* $ai ~purple
llm -> out((Visual Reasoning & OCR Answer)) ~ok"#;

    let m12 = Module {
        id: 12,
        phase_id: 5,
        slug: "multimodal-ai".to_string(),
        week: 16,
        title: "Multimodal AI & Vision-Language Models".to_string(),
        urdu_title: "Multimodal AI: Vision-Language Models (VLMs), Speech & Video".to_string(),
        description: "Vision Encoders (SigLIP), Multimodal Projection Adapters, LLaVA, Whisper speech recognition, video frame reasoning, aur visual agents.".to_string(),
        diagram_script: m12_script.to_string(),
        diagram_svg: render_svg_or_fallback(m12_script),
        lessons: vec![
            Lesson {
                id: 1201,
                module_slug: "multimodal-ai".to_string(),
                slug: "multimodal-architectures".to_string(),
                title: "Vision Encoders (SigLIP/CLIP) & Projector Layers".to_string(),
                urdu_title: "Vision Encoders Aur Multimodal Projectors: Images Ko Text Space Mein Map Karna".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "VLM mein image encoder (SigLIP) ke visual tokens ko ek chota 2-layer MLP projector LLM ki text embedding dimension mein convert kar deta hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Projectors cross-modal representations align karte hain.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1202,
                module_slug: "multimodal-ai".to_string(),
                slug: "vision-language-models".to_string(),
                title: "SOTA VLMs for Complex Document OCR & Visual Reasoning".to_string(),
                urdu_title: "SOTA VLMs: Complex Invoices, Tables Aur Charts Ka Visual Extraction".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Traditional OCR spatial structure loose kar deta hai. Modern VLMs visual layout samajh kar nested tables aur graphs ko exact markdown mein extract karte hain.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Spatial reasoning layout-heavy documents ke liye critical hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1203,
                module_slug: "multimodal-ai".to_string(),
                slug: "audio-speech-models".to_string(),
                title: "Speech AI: Whisper ASR, Voice Activity & Real-Time Audio".to_string(),
                urdu_title: "Voice AI: Whisper Speech-to-Text Aur Voice Activity Detection (VAD)".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Real-time voice bots mein VAD (Voice Activity Detection) 100ms mein detect karti hai ke user ne bolna band kiya hai ya nahi, taake natural turn-taking ho sake.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Sub-500ms voice pipeline VAD + streaming LLM + TTS par depend karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1204,
                module_slug: "multimodal-ai".to_string(),
                slug: "video-understanding".to_string(),
                title: "Video Intelligence: Frame Sampling & Temporal Attention".to_string(),
                urdu_title: "Video AI: Dynamic Frame Extraction Aur Temporal Understanding".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Video ke har frame ko process karna expensive hota hai. Keyframe extraction (1 frame per second) se 90% compute bacha kar video events trace kiye ja sakte hain.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Keyframe sampling video tokens ko context limits ke andar rakhta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1205,
                module_slug: "multimodal-ai".to_string(),
                slug: "multimodal-agentic-flows".to_string(),
                title: "Multimodal Agentic Workflows & Visual UI Operators".to_string(),
                urdu_title: "Visual AI Agents: Computer Use Aur Screen Understanding".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Visual agents screen ke screenshots dekh kar mouse clicks aur keyboard input execute karte hain taake legacy desktop software automate ho sake.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Coordinate grounding visual agent interactions ko enable karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1206,
                module_slug: "multimodal-ai".to_string(),
                slug: "module-12-capstone".to_string(),
                title: "Module 12 Capstone: Multimodal Document & Video Intelligence Engine".to_string(),
                urdu_title: "Capstone: Production Multimodal Ingestion & Search Assistant".to_string(),
                duration_mins: 65,
                xp_reward: 200,
                explanation_urdu: "Aap ek system build karenge jo videos aur PDF diagrams ko ingest karke cross-modal question answering provide karega.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Multimodal intelligence engine deployed!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-12".to_string(),
            module_slug: "multimodal-ai".to_string(),
            title: "Multimodal AI & Vision-Language Models Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "What is the purpose of the projection adapter (e.g. MLP) between a vision encoder and an LLM backbone?".to_string(),
                    urdu_question: "Vision encoder aur LLM ke darmiyan projection adapter ka kya kaam hota hai?".to_string(),
                    options: vec![
                        "To compress the image to JPEG format".to_string(),
                        "To project visual patch embeddings into the same vector space and dimension as the LLM's text token embeddings".to_string(),
                        "To play sound effects".to_string(),
                        "To detect faces only".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Projector visual vectors ko language model ke text embedding space mein align karta hai taake LLM visual patches ko tokens ki tarah process kar sake.".to_string(),
                },
            ],
        },
        resources: vec![],
        project: None,
        real_world_deliverable: Some("Voice WhatsApp Voice-Note Transcriber (Whisper) & Urdu Invoice Scanner (ColPali)".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Google Colab Free T4 (15GB VRAM)".to_string(),
            vram_required: "5 GB VRAM".to_string(),
            estimated_cost: "$0.00 Free".to_string(),
            compute_units_tip: "Use faster-whisper with INT8 quantization on Colab T4 for 4x real-time audio transcription.".to_string(),
            one_click_command: "!pip install faster-whisper && python transcribe.py voice_note.ogg".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(12)),
    };

    let m13_script = r#"@preset midnight
@animate flow
flow LR: Modern MLOps & LLMOps Lifecycle | Zero to Production Pipeline
git[[Code & Config // Git]] $github ~purple -> ci[CI/CD & Lint] ~info
data[(Curated Datasets & Prompts)] $db ~teal -> train[Distributed Training / PEFT] $cpu ~teal
train -> eval{Evaluation Suite // ROUGE, BLEU, LLM-as-Judge}*
eval ->|Pass| reg[(Model Registry // MLflow / W&B)] $db ~ok
eval ->|Fail| train
reg -> deploy[Kubernetes / vLLM Serving // Fast Inference] $docker ~info
deploy -> mon[Telemetry & Drift Monitoring // Prometheus + Tracing] $chart ~purple
mon -->|Data Drift Feedback| data"#;

    let m13 = Module {
        id: 13,
        phase_id: 5,
        slug: "mlops-deployment".to_string(),
        week: 17,
        title: "MLOps, Model Serving & Deployment".to_string(),
        urdu_title: "MLOps & LLMOps: vLLM High-Throughput Serving Aur Fast Inference".to_string(),
        description: "vLLM, PagedAttention, TensorRT-LLM, Quantization (AWQ/GGUF), Production LLM Gateway, OpenTelemetry observability, aur Kubernetes GPU orchestration.".to_string(),
        diagram_script: m13_script.to_string(),
        diagram_svg: render_svg_or_fallback(m13_script),
        lessons: vec![
            Lesson {
                id: 1301,
                module_slug: "mlops-deployment".to_string(),
                slug: "inference-engines-vllm".to_string(),
                title: "vLLM & PagedAttention: 10x Inference Throughput".to_string(),
                urdu_title: "vLLM Aur PagedAttention: OS Paging Se GPU VRAM Fragmentation Khatam Karna".to_string(),
                duration_mins: 55,
                xp_reward: 150,
                explanation_urdu: "Standard serving mein 60-80% VRAM memory fragmentation ki wajah se waste ho jati thi. vLLM OS ke virtual memory paging concept ko use karta hai aur continuous batching se throughput 10x barha deta hai!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Continuous batching aur PagedAttention modern serving ke cornerstones hain.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1302,
                module_slug: "mlops-deployment".to_string(),
                slug: "quantization-runtime".to_string(),
                title: "Model Quantization: AWQ, GPTQ & GGUF Runtime".to_string(),
                urdu_title: "Quantization: AWQ, GPTQ Aur GGUF (llama.cpp) Runtime Optimization".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "AWQ (Activation-aware Weight Quantization) sirf un 1% salient weights ko high precision rakhta hai jo activations ko dictate karte hain; baqi 99% weights 4-bit par chale jate hain bina quality drop ke!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["AWQ maintains perplexity while reducing memory footprint by 75%.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1303,
                module_slug: "mlops-deployment".to_string(),
                slug: "api-gateway-rate-limiting".to_string(),
                title: "Building Production LLM Gateways with Token Streaming".to_string(),
                urdu_title: "Production LLM Gateway: Fast Token Streaming Aur Rate Limiting".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "User ko pehla token 200ms mein milna chahiye (Time To First Token - TTFT). Server-Sent Events (SSE) streaming se instant response feel hoti hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Low TTFT (Time to First Token) user experience ko dramatic boost deta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1304,
                module_slug: "mlops-deployment".to_string(),
                slug: "observability-tracing".to_string(),
                title: "LLMOps Observability: Tracing, Latency & Cost Tracking".to_string(),
                urdu_title: "LLMOps Observability: OpenTelemetry, Langfuse Aur Token Cost Monitoring".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Bina tracing ke aap andhay hain! Har LLM call ka token count, prompt latency, cache hit ratio, aur exact cost dollar mein track honi chahiye.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Granular tracing prevents billing surprises and identifies bottlenecks.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1305,
                module_slug: "mlops-deployment".to_string(),
                slug: "kubernetes-gpu-orchestration".to_string(),
                title: "Kubernetes GPU Orchestration & Auto-Scaling".to_string(),
                urdu_title: "Kubernetes Par GPU Pods Deploy Karna Aur Autoscaling (HPA)".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Traffic aane par automatic GPU pods scale karna aur idle hone par scale-to-zero karna hazaron dollars ki cloud savings deta hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["KEDA event-driven autoscaling GPU workloads optimize karta hai.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1306,
                module_slug: "mlops-deployment".to_string(),
                slug: "module-13-capstone".to_string(),
                title: "Module 13 Capstone: High-Throughput LLM Gateway Service".to_string(),
                urdu_title: "Capstone: Production vLLM Gateway with Prometheus Metrics".to_string(),
                duration_mins: 65,
                xp_reward: 200,
                explanation_urdu: "Aap ek Rust/Python gateway deploy karenge jo multi-model routing, token streaming, aur live telemetry provide karegi.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Production LLM Gateway live in production!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-13".to_string(),
            module_slug: "mlops-deployment".to_string(),
            title: "MLOps & Model Serving Quiz".to_string(),
            passing_score: 75,
            xp_reward: 150,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "How does PagedAttention in vLLM prevent GPU VRAM memory fragmentation?".to_string(),
                    urdu_question: "vLLM ka PagedAttention GPU memory fragmentation ko kaise khatam karta hai?".to_string(),
                    options: vec![
                        "By running everything on CPU instead".to_string(),
                        "By allocating non-contiguous physical memory blocks for KV caches, similar to virtual memory paging in operating systems".to_string(),
                        "By rounding all model weights to integers".to_string(),
                        "By clearing memory after every character".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "PagedAttention operating system ke virtual memory paging algorithm ko adapt karke non-contiguous blocks allocate karta hai, jiss se memory waste 4% se kam reh jati hai.".to_string(),
                },
            ],
        },
        resources: vec![],
        project: None,
        real_world_deliverable: Some("100% Offline In-Browser WebGPU Chatbot & GGUF Ollama Desktop Assistant".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Local Client Browser (WebGPU) / Ollama Local CPU".to_string(),
            vram_required: "0 GB Cloud VRAM (Client-side hardware)".to_string(),
            estimated_cost: "$0.00 Free (Zero Server Infrastructure Cost)".to_string(),
            compute_units_tip: "WebLLM compiles Llama 3 8B directly into WebGPU shaders, running 100% inside student browser.".to_string(),
            one_click_command: "ollama run llama3.2:3b".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(13)),
    };

    let m14_script = r#"@preset midnight
@animate glow
arch LR: Enterprise Production AI Architecture | Multi-Tier Defense & Routing
client[Web & Mobile Clients] $browser ~purple -> gate[API Gateway & Rate Limiter] $server ~info
gate -> guard[Guardrails // NeMo / Prompt Injection Shield]* ~danger
guard -> route{Semantic Cache & Smart Router}
route ->|Cache Hit| fast[Cached Response // <10ms] ~ok
route ->|Simple Task| small[Small Fast LLM // Llama 3 8B] ~teal
route ->|Complex Task| deep[Large Reasoning LLM // Claude 3.5 Sonnet]* ~purple
small -> mon[Telemetry & Tracing // OpenTelemetry] $chart ~info
deep -> mon
fast -> mon
mon -> resp((User Response with SLA)) ~ok"#;

    let m14 = Module {
        id: 14,
        phase_id: 5,
        slug: "capstone-production".to_string(),
        week: 19,
        title: "Capstone Architecture & Production AI Systems".to_string(),
        urdu_title: "Grand Capstone: Enterprise Autonomous AI System Architecture".to_string(),
        description: "Enterprise system design, Prompt injection defense, Semantic caching, Cost-latency optimization, Continuous automated evals, aur final Capstone defense.".to_string(),
        diagram_script: m14_script.to_string(),
        diagram_svg: render_svg_or_fallback(m14_script),
        lessons: vec![
            Lesson {
                id: 1401,
                module_slug: "capstone-production".to_string(),
                slug: "enterprise-system-design".to_string(),
                title: "Enterprise AI System Design: Multi-Tier Architecture & SLAs".to_string(),
                urdu_title: "Enterprise System Design: High Availability Aur 99.9% Uptime Architecture".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Production AI systems mein graceful degradation zaroori hai. Agar primary model down ho to auto-fallback secondary open-source model par switch hona chahiye.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Fallback strategies ensure zero downtime for end users.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1402,
                module_slug: "capstone-production".to_string(),
                slug: "security-guardrails".to_string(),
                title: "Security & Guardrails: Prompt Injection Defense (NeMo Guardrails)".to_string(),
                urdu_title: "AI Security: Prompt Injection Defense Aur PII Data Masking".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Malicious users system prompt leak karne ya jailbreak karne ki koshish karte hain. NeMo Guardrails input ko sanitize karti hai aur output par PII data mask karti hai.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Multi-layer guardrails secure sensitive enterprise data.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1403,
                module_slug: "capstone-production".to_string(),
                slug: "cost-latency-tradeoffs".to_string(),
                title: "Cost & Latency Optimization: Semantic Caching & Model Cascades".to_string(),
                urdu_title: "Cost Optimization: Semantic Caching (GPTCache) Aur Model Cascades".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Agar 30% queries semantically similar hoon to vector cache se <10ms mein zero-cost answer deliver ho jata hai! Choti queries Llama 3 8B solve karta hai aur complex reasoning Claude 3.5 Sonnet.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Semantic caching cuts API bills by 30-50%.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1404,
                module_slug: "capstone-production".to_string(),
                slug: "ci-cd-evaluation-automation".to_string(),
                title: "Continuous Evaluation & Regression Testing in CI/CD".to_string(),
                urdu_title: "CI/CD Evals: GitHub Actions Mein Automated LLM Benchmarks".to_string(),
                duration_mins: 50,
                xp_reward: 100,
                explanation_urdu: "Code badalne par unit tests run hotay hain; isi tarah AI prompt ya model version badalne par 500-question automated benchmark run hona chahiye before merging to main!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["Automated evaluation gates prevent silent degradation.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1405,
                module_slug: "capstone-production".to_string(),
                slug: "portfolio-presentation".to_string(),
                title: "Portfolio Packaging & Open Source Release Strategy".to_string(),
                urdu_title: "Portfolio Packaging: Open-Source Release Aur Technical Writing".to_string(),
                duration_mins: 45,
                xp_reward: 100,
                explanation_urdu: "Apne capstone ko standard software jaisa package karein: Clean README, DiagramKit architectural diagrams, Dockerfile, benchmark comparisons, aur live interactive demo.".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["A polished live demo attracts global recruiters and clients.".to_string()],
                resources: vec![],
            },
            Lesson {
                id: 1406,
                module_slug: "capstone-production".to_string(),
                slug: "final-capstone-defense".to_string(),
                title: "Grand Capstone Defense & AI Mastery Graduation".to_string(),
                urdu_title: "Grand Capstone Defense: Autonomous Enterprise System Release".to_string(),
                duration_mins: 90,
                xp_reward: 500,
                explanation_urdu: "Mubarak ho! Aapne poora 20 hafton ka safar mukammal kar liya hai. Ab aap apna final autonomous system defend karenge aur AI Mastery Grandmaster certificate unlock karenge!".to_string(),
                code_snippet: None,
                diagram_script: None,
                diagram_svg: None,
                key_takeaways: vec!["AI Mastery Certified Production Engineer!".to_string()],
                resources: vec![],
            },
        ],
        quiz: Quiz {
            id: "quiz-module-14".to_string(),
            module_slug: "capstone-production".to_string(),
            title: "Production Architecture & Capstone Defense Quiz".to_string(),
            passing_score: 75,
            xp_reward: 200,
            questions: vec![
                QuizQuestion {
                    id: 1,
                    question: "How does semantic caching differ from standard exact-match HTTP caching?".to_string(),
                    urdu_question: "Semantic caching aam exact-match HTTP caching se mukhtalif kyun hai?".to_string(),
                    options: vec![
                        "Semantic caching only works with MySQL".to_string(),
                        "Semantic caching compares query embedding vectors, returning cached answers for semantically equivalent questions even if phrased differently".to_string(),
                        "Semantic caching deletes data every minute".to_string(),
                        "Semantic caching requires manual human approval".to_string(),
                    ],
                    correct_index: 1,
                    explanation_urdu: "Exact match caching fail ho jati hai agar wording thori badal jaye; semantic caching embedding similarity use karti hai aur matching meaning par cached response de deti hai.".to_string(),
                },
            ],
        },
        resources: vec![],
        project: Some(ProjectBrief {
            title: "Enterprise Autonomous AI Intelligence Platform".to_string(),
            description: "Design, build, and deploy an end-to-end production AI system incorporating Hybrid RAG, Fine-Tuned Adapters, Multi-Agent workflows, and vLLM serving with live telemetry.".to_string(),
            deliverables: vec![
                "Fully functional multi-agent backend in Rust/Python".to_string(),
                "Interactive DiagramKit live architecture viewer".to_string(),
                "Automated eval suite with >95% accuracy score".to_string(),
                "Docker container and Kubernetes deployment manifest".to_string(),
            ],
            evaluation_criteria: vec![
                "Sub-50ms retrieval latency".to_string(),
                "Zero unhandled exceptions or hallucinations on benchmark test cases".to_string(),
                "Comprehensive documentation and architectural diagrams".to_string(),
            ],
            real_world_deliverable: Some("Production Multi-Tenant AI Micro-SaaS on Supabase + Rust Axum + Cloudflare".to_string()),
            zero_gpu_recipe: None,
        }),
        real_world_deliverable: Some("Production Multi-Tenant AI Micro-SaaS on Supabase + Rust Axum + Cloudflare".to_string()),
        zero_gpu_recipe: Some(ZeroGpuRecipe {
            platform: "Supabase Free Tier + Cloudflare Pages + Fly.io / Groq".to_string(),
            vram_required: "0 GB Dedicated Server VRAM".to_string(),
            estimated_cost: "$0.00 Free Forever Tier".to_string(),
            compute_units_tip: "Deploy frontend on Cloudflare Pages (free unlimited bandwidth), database on Supabase, backend on Fly.io free tier.".to_string(),
            one_click_command: "git push origin main".to_string(),
        }),
        practice_checkpoint: Some(get_checkpoint(14)),
    };

    Phase {
        id: 5,
        slug: "phase-5-production-and-capstone".to_string(),
        title: "Phase 5: Production RAG, Fine-Tuning & Grand Capstone".to_string(),
        urdu_title: "Phase 5: Production RAG, Autonomous Agents, MLOps Aur Grand Capstone".to_string(),
        week_range: "Weeks 13-20".to_string(),
        description: "Hybrid RAG, Cross-Encoder Re-ranking, PEFT/LoRA fine-tuning, ReAct autonomous agents, Multimodal Vision-Language systems, vLLM serving, aur Grand Capstone Defense.".to_string(),
        outcome: "Aap kisi bhi enterprise scale par end-to-end generative AI systems, autonomous agents aur high-scale GPU pipelines design aur deploy karne ke qabil ban jayenge.".to_string(),
        modules: vec![m9, m10, m11, m12, m13, m14],
    }
}
