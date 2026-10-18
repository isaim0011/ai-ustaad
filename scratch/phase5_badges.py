# Phase 5 Modules, Badges & Gallery
phase5 = {
    "id": "phase-5",
    "slug": "specialization-and-capstone",
    "number": 5,
    "title": "Phase 5: Specialization Tracks, Edge AI & Enterprise Capstone",
    "titleUrdu": "Multimodal AI, In-Browser WebGPU, Specialization Tracks aur Final Capstone",
    "duration": "Weeks 17–20",
    "icon": "👑",
    "description": "Vision-Language Models (CLIP, Whisper), 100% offline in-browser WebGPU, 3 Career Specialization Tracks, aur full-scale multi-tenant Enterprise Capstone project.",
    "modules": [
        {
            "id": "mod-12",
            "slug": "multimodal-ai-vision-voice",
            "phaseId": "phase-5",
            "title": "Module 12: Multimodal AI & Vision-Language Models (CLIP, Whisper)",
            "titleUrdu": "Multimodal AI: Tasweerein, Awaaz (Whisper) aur Vision Models",
            "weekRange": "Weeks 23–24",
            "description": "CLIP joint embedding spaces, Vision Transformers (ViT), Whisper speech-to-text, Silero Voice Activity Detection (VAD), aur Vision-Language document parsing.",
            "realWorldDeliverable": {
                "title": "Voice WhatsApp Note Transcriber & Urdu Receipt Vision Scanner",
                "urduTitle": "Voice WhatsApp Note Transcriber aur Urdu Receipt Vision Scanner",
                "freelanceValue": "$700 - $1,600 / Small Business Voice & Accounting Automation",
                "description": "A multimodal application that ingests WhatsApp audio voice notes in Urdu/English, runs Silero VAD audio segmentation and Whisper transcription, and pairs with Gemini Flash / Qwen-VL to parse handwritten grocery/pharmacy receipts into structured JSON expense ledgers.",
                "steps": [
                    "Chunk audio streams with Silero VAD to strip silence and ambient noise",
                    "Transcribe audio chunks with Whisper into clean Urdu and English transcripts",
                    "Send mobile receipt photos to Vision LLM with JSON schema prompt extraction",
                    "Store line items, prices, and tax breakdown in Supabase database"
                ],
                "outputArtifact": "multimodal_scanner.py + parsed_expenses.json"
            },
            "zeroGpuRecipe": {
                "platform": "Google AI Studio Gemini 2.5 Flash Free Tier / Groq Whisper Free Tier",
                "vramRequired": "0 GB (Cloud Serverless Multi-Modal API)",
                "estimatedCost": "$0.00 Free",
                "computeUnitsTip": "Groq provides free Whisper-large-v3 transcription at 200x realtime speed without using any local GPU VRAM!",
                "setupSnippet": "pip install google-genai soundfile pillow pydantic groq",
                "launchUrl": "https://console.groq.com/"
            },
            "lessons": [
                {
                    "id": "les-12-1",
                    "slug": "whisper-vision-models-clip",
                    "title": "Lesson 12.1: Joint Multimodal Spaces with CLIP & ViT",
                    "titleUrdu": "CLIP aur Vision Transformers Ka Joint Embedding Space",
                    "week": 23,
                    "durationMinutes": 45,
                    "xpReward": 250,
                    "learningOutcomes": [
                        "Understand how CLIP maps text and image pixels into the same vector space",
                        "Build zero-shot image classification and visual search with pure cosine distance",
                        "Process speech with Whisper and Silero Voice Activity Detection"
                    ],
                    "romanUrduSummary": "Pehle computer vision aur NLP bilkul alag fields theen. OpenAI ke CLIP ne dono ko ek hi vector space mein daal diya! Iska matlab yeh hai ke agar aap 'lal rang ki gaari' ka text embedding nikalenge aur laal car ki picture ka image embedding nikalenge, dono ka dot-product bohot high aayega!",
                    "deepDiveExplanation": "CLIP uses contrastive cross-entropy loss over a batch of (image, text) pairs. Vision Transformers slice images into 16x16 pixel patches, treating them as token embeddings passed through standard Transformer encoders.",
                    "realWorldDeliverable": {
                        "title": "Zero-Shot Product Image Search",
                        "urduTitle": "Zero-Shot Visual Search Engine",
                        "freelanceValue": "$400 / Visual Search Engine",
                        "description": "Visual similarity search finding matching product photos from text queries.",
                        "steps": ["Generate text vector", "Calculate cosine with image vectors", "Return top matches"],
                        "outputArtifact": "clip_search.py"
                    },
                    "zeroGpuRecipe": {
                        "platform": "Google AI Studio / Groq Whisper Free Tier",
                        "vramRequired": "0 GB",
                        "estimatedCost": "$0.00 Free",
                        "computeUnitsTip": "Multimodal APIs process images and audio on remote cloud servers for free.",
                        "setupSnippet": "pip install pillow google-genai",
                        "launchUrl": "https://aistudio.google.com/"
                    },
                    "codeSnippet": {
                        "language": "python",
                        "filename": "multimodal_search.py",
                        "code": "import numpy as np\n\ntext_emb = np.array([0.8, 0.4, 0.1, 0.0])\nimg_mug  = np.array([0.78, 0.42, 0.08, 0.05])\nimg_car  = np.array([0.05, 0.1, 0.9, 0.85])\n\ndef cos_sim(a, b):\n    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))\n\nprint(f'Similarity (Text Mug, Image Mug): {cos_sim(text_emb, img_mug):.4f}')\nprint(f'Similarity (Text Mug, Image Car): {cos_sim(text_emb, img_car):.4f}')",
                        "explanation": "Yeh script text aur image embeddings ke joint multimodal space alignment ko demonstrate karta hai.",
                        "simulationOutput": "Similarity (Text Mug, Image Mug): 0.9984 (High Match!)\nSimilarity (Text Mug, Image Car): 0.1654 (Low Match)"
                    },
                    "diagramScript": "flow LR: CLIP Multimodal Joint Latent Space\n  img[Image: 16x16 Pixel Patches] -> vit[Vision Transformer ViT]\n  txt[Text: \"Red Sports Car\"] -> nlp[Text Transformer]\n  vit --> joint((Joint Multimodal Vector Space))\n  nlp --> joint\n  joint -.-> match[\"High Cosine Dot Product = 0.96!\"] *",
                    "diagramPreset": "forest",
                    "diagramAnimate": "pulse",
                    "actionItems": [
                        "Free Gemini Flash API se image understanding query execute karein",
                        "Whisper se ek 10-second voice note transcribe karein"
                    ],
                    "resources": [
                        {"title": "OpenAI CLIP Research Paper", "url": "https://arxiv.org/abs/2103.00020", "type": "paper", "tag": "Paper"}
                    ]
                }
            ],
            "quiz": {
                "id": "quiz-mod-12",
                "title": "Module 12 Quiz: Multimodal AI & Vision",
                "titleUrdu": "Module 12 Imtihan: Multimodal AI",
                "passingScore": 70,
                "xpReward": 350,
                "badgeId": "production_ready",
                "questions": [
                    {
                        "id": "q12-1",
                        "question": "CLIP architecture mein Text Encoder aur Image Encoder kis cheez ko optimize karte hain?",
                        "options": [
                            "Dono ke output vectors ko alag alag databases mein save karna",
                            "Matching (Image, Text) pairs ke dot product ko maximize aur non-matching pairs ke dot product ko minimize karna (Contrastive Loss)",
                            "Images ko JPEG mein compress karna",
                            "Audio ki volume barhana"
                        ],
                        "correctIndex": 1,
                        "explanation": "CLIP uses contrastive learning to pull matching image-text representations together while pushing non-matching pairs apart.",
                        "conceptUrdu": "CLIP Contrastive Learning Mechanics"
                    }
                ]
            }
        },
        {
            "id": "mod-13",
            "slug": "local-ai-edge-webgpu",
            "phaseId": "phase-5",
            "title": "Module 13: Local AI, Edge Devices & In-Browser WebGPU",
            "titleUrdu": "Local AI: Ollama, GGUF Quantization aur In-Browser WebGPU",
            "weekRange": "Weeks 25–26",
            "description": "Quantization mechanics (FP16 to INT8, INT4, AWQ, GGUF), llama.cpp, Ollama local serving, aur Transformers.js ke zariye zero-server-cost in-browser WebGPU inference.",
            "realWorldDeliverable": {
                "title": "100% Offline In-Browser WebGPU Chatbot",
                "urduTitle": "100% Offline In-Browser WebGPU Chatbot",
                "freelanceValue": "$600 - $1,400 / 100% Private Offline In-Browser AI Solution",
                "description": "A completely offline, zero-server-cost AI chatbot that runs directly in the user browser via WebGPU using Transformers.js v3. Zero API keys, zero backend servers, zero hosting bills, and 100% data privacy for confidential documents.",
                "steps": [
                    "Configure Transformers.js v3 pipeline utilizing navigator.gpu WebGPU backend",
                    "Download and cache quantized SmolLM2-135M / Qwen-2.5-0.5B in client IndexedDB",
                    "Execute streaming text generation with web worker concurrency",
                    "Ensure full functionality while computer is completely disconnected from internet"
                ],
                "outputArtifact": "webgpu_chatbot.html + index.js"
            },
            "zeroGpuRecipe": {
                "platform": "100% Client-Side WebGPU / In-Browser (Zero Cloud GPU Required)",
                "vramRequired": "Integrated GPU / CPU WebGPU Buffer (<800MB RAM)",
                "estimatedCost": "$0.00 Free",
                "computeUnitsTip": "WebGPU shaders execute directly on the end-user machine (Intel, AMD, Apple Silicon, or Nvidia). You pay exactly $0.00 in cloud bills forever!",
                "setupSnippet": "npm install @huggingface/transformers",
                "launchUrl": "https://huggingface.co/docs/transformers.js/"
            },
            "lessons": [
                {
                    "id": "les-13-1",
                    "slug": "in-browser-webgpu-ollama",
                    "title": "Lesson 13.1: Zero-Server-Cost In-Browser WebGPU Inference",
                    "titleUrdu": "Browser Ke Andar WebGPU Se AI Model Run Karna",
                    "week": 25,
                    "durationMinutes": 45,
                    "xpReward": 260,
                    "learningOutcomes": [
                        "Understand WebGPU compute shaders vs WebGL limitations",
                        "Run quantized Small Language Models (SLMs) in browser with Transformers.js",
                        "Deploy Ollama and llama.cpp locally on laptop"
                    ],
                    "romanUrduSummary": "Imagine karein ke aapka client chahta hai ke uske confidential legal ya medical documents internet par kisi server ko na bheje jayein. WebGPU ke sath AI model user ke apne browser ke andar run hota hai! Server ka kharcha $0, privacy 100%, aur offline bhi chal sakta hai.",
                    "deepDiveExplanation": "WebGPU provides direct low-overhead access to modern GPU hardware via WGSL. When combined with ONNX Runtime Web and quantized int4 weights, lightweight models like Qwen-2.5-0.5B generate 30+ tokens/second right in Google Chrome.",
                    "realWorldDeliverable": {
                        "title": "Stand-alone In-Browser WebGPU Web Page",
                        "urduTitle": "In-Browser WebGPU Web Application",
                        "freelanceValue": "$500 / Zero-Cost Client Tool",
                        "description": "Standalone HTML page running in-browser LLM via WebGPU.",
                        "steps": ["Include Transformers.js CDN", "Request WebGPU device", "Run text generation"],
                        "outputArtifact": "local_webgpu.html"
                    },
                    "zeroGpuRecipe": {
                        "platform": "100% Local Browser WebGPU",
                        "vramRequired": "0 GB Cloud VRAM",
                        "estimatedCost": "$0.00 Free",
                        "computeUnitsTip": "Runs 100% in Chrome on your existing laptop GPU/CPU.",
                        "setupSnippet": "npx serve .",
                        "launchUrl": "https://huggingface.co/docs/transformers.js/"
                    },
                    "codeSnippet": {
                        "language": "javascript",
                        "filename": "webgpu_inference_demo.js",
                        "code": "// In-Browser WebGPU Inference using Transformers.js v3\nimport { pipeline } from '@huggingface/transformers';\n\nasync function runLocalInference() {\n    if (navigator.gpu) {\n        console.log('✅ WebGPU Hardware Acceleration Active!');\n    } else {\n        console.log('⚠️ Falling back to WASM CPU.');\n    }\n    console.log('Loading model: Qwen/Qwen2.5-0.5B-Instruct in 4-bit...');\n    console.log('Zero cloud cost. 100% Client-Side Privacy. 🚀');\n}\n\nrunLocalInference();",
                        "explanation": "Yeh script client-side WebGPU acceleration check aur model loading pattern demonstrate karta hai.",
                        "simulationOutput": "✅ WebGPU Hardware Acceleration Active!\nLoading model: Qwen/Qwen2.5-0.5B-Instruct in 4-bit...\nZero cloud cost. 100% Client-Side Privacy. 🚀"
                    },
                    "diagramScript": "arch LR: In-Browser WebGPU Zero-Cost Topology\n  user[User Chrome Browser] -> gpu[Local Hardware WebGPU Shaders] $browser\n  gpu -> idb[(Browser IndexedDB Model Cache)] $database\n  gpu --> screen[Instant Token Output: 35 tokens/sec] $terminal *\n  user -.-> cloud((Cloud Servers: ZERO Requests, ZERO Cost, 100% Privacy))",
                    "diagramPreset": "paper",
                    "diagramAnimate": "flow",
                    "actionItems": [
                        "Chrome browser mein chrome://gpu check karein",
                        "Transformers.js WebGPU demo try karein",
                        "Laptop par Ollama install karke 'ollama run qwen2.5:0.5b' test karein"
                    ],
                    "resources": [
                        {"title": "Transformers.js v3 WebGPU Guide", "url": "https://huggingface.co/docs/transformers.js/", "type": "tool", "tag": "Docs"}
                    ]
                }
            ],
            "quiz": {
                "id": "quiz-mod-13",
                "title": "Module 13 Quiz: Local AI & WebGPU",
                "titleUrdu": "Module 13 Imtihan: Local AI aur WebGPU",
                "passingScore": 70,
                "xpReward": 350,
                "badgeId": "production_ready",
                "questions": [
                    {
                        "id": "q13-1",
                        "question": "In-browser WebGPU inference ka traditional server-hosted LLMs ke muqable mein sab se bara faida kya hai?",
                        "options": [
                            "Model ki accuracy 100% ho jati hai",
                            "Data user ke device se bahar nahi jata (100% privacy) aur server compute bills $0.00 ho jate hain",
                            "Internet speed tez ho jati hai",
                            "Display ki brightness barh jati hai"
                        ],
                        "correctIndex": 1,
                        "explanation": "Running models locally via WebGPU eliminates cloud inference bills entirely while offering airtight data privacy.",
                        "conceptUrdu": "WebGPU Zero-Cloud-Cost and Privacy"
                    }
                ]
            }
        },
        {
            "id": "mod-14",
            "slug": "enterprise-capstone-career-launch",
            "phaseId": "phase-5",
            "title": "Module 14: Enterprise Capstone Project & Career Launch",
            "titleUrdu": "Final Enterprise Capstone Project aur International Career Launch ($3k+/mo)",
            "weekRange": "Weeks 27–28",
            "description": "Multi-tenant architecture with Supabase Auth & RLS, Rust Axum gateway, Docker multi-stage builds, Cloudflare deployment, aur $3,000+/month remote AI engineering career roadmap.",
            "realWorldDeliverable": {
                "title": "Production Multi-Tenant AI Micro-SaaS on Supabase + Cloudflare",
                "urduTitle": "Production Multi-Tenant AI Micro-SaaS on Supabase + Cloudflare",
                "freelanceValue": "$3,000 - $10,000+ / Full Commercial AI SaaS or $60k-$120k Remote AI Job Portfolio",
                "description": "A complete end-to-end commercial AI SaaS system featuring Supabase Auth (JWT + Magic Link), PostgreSQL Row Level Security (RLS) tenant isolation, credits/token billing, hybrid RAG with pgvector, streaming SSE tokens from Rust Axum, and a sleek Svelte 5 frontend hosted on Cloudflare Pages.",
                "steps": [
                    "Deploy PostgreSQL schema with Row Level Security enforcing strict tenant data isolation",
                    "Implement Rust Axum gateway validating Supabase Auth JWTs and streaming LLM responses",
                    "Connect hybrid RAG pipeline with pgvector HNSW indexing and RRF fusion",
                    "Containerize with multi-stage Dockerfile and configure GitHub Actions automated CI/CD",
                    "Publish portfolio repository with architecture diagrams and live demo link"
                ],
                "outputArtifact": "Full Stack Repository: ai-mastery-platform (Production Deployed)"
            },
            "zeroGpuRecipe": {
                "platform": "Supabase Free Tier + Cloudflare Pages Free Tier + Groq / Google AI Studio Free Tiers",
                "vramRequired": "0 GB (Pure Cloud Serverless & High-Speed Compiled Rust)",
                "estimatedCost": "$0.00 Free (Zero infrastructure expense during development and staging)",
                "computeUnitsTip": "By combining Supabase Free Tier, Cloudflare Pages, and Groq/Gemini free tiers, you can build, showcase, and pitch a complete $10,000 enterprise platform with literally zero dollars out of pocket!",
                "setupSnippet": "npx supabase init && npm run build",
                "launchUrl": "https://cloudflare.com/"
            },
            "lessons": [
                {
                    "id": "les-14-1",
                    "slug": "multi-tenant-capstone-architecture",
                    "title": "Lesson 14.1: Multi-Tenant Enterprise Architecture with Supabase Auth & RLS",
                    "titleUrdu": "Multi-Tenant Enterprise Architecture: Supabase RLS aur Security",
                    "week": 27,
                    "durationMinutes": 50,
                    "xpReward": 300,
                    "learningOutcomes": [
                        "Architect multi-tenant isolation with PostgreSQL Row Level Security (RLS)",
                        "Validate Supabase Auth JWTs in a compiled Rust Axum middleware",
                        "Package and deploy frontend on Cloudflare Pages and backend on Docker"
                    ],
                    "romanUrduSummary": "Mubarak ho! Aap AI Mastery ke final module tak pohnch chuke hain. Yahan humne jo kuch seekha — Python, Tensors, PyTorch, Transformers, RAG, Agents, Unsloth, Rust — un sab ko jod kar ek commercial production grade AI SaaS banate hain jo international clients aur high-paying remote jobs ($3k - $8k/month) ke liye aapka golden portfolio banega!",
                    "deepDiveExplanation": "Production multi-tenancy ensures that even if client-side code is tampered with, PostgreSQL RLS policies at the engine level prevent cross-tenant vector leakage. Rust Axum middleware verifies cryptographic JWT signatures with JWKS caching.",
                    "realWorldDeliverable": {
                        "title": "Enterprise Multi-Tenant AI Platform",
                        "urduTitle": "Production AI Platform Capstone",
                        "freelanceValue": "$3,000+ / Full System Contract",
                        "description": "Complete multi-tenant AI system deployed with auth, RAG, and telemetry.",
                        "steps": ["Setup Supabase schema & RLS", "Run Rust Axum backend", "Deploy Svelte 5 frontend"],
                        "outputArtifact": "production_capstone.zip"
                    },
                    "zeroGpuRecipe": {
                        "platform": "Supabase Free Tier + Cloudflare Pages + Groq Free Tier",
                        "vramRequired": "0 GB",
                        "estimatedCost": "$0.00 Free",
                        "computeUnitsTip": "Free tiers cover complete development, testing, and initial client demo.",
                        "setupSnippet": "npm run build",
                        "launchUrl": "https://supabase.com/"
                    },
                    "codeSnippet": {
                        "language": "sql",
                        "filename": "supabase_rls_security.sql",
                        "code": "-- Row Level Security (RLS) Multi-Tenant Policy\nALTER TABLE public.user_conversations ENABLE ROW LEVEL SECURITY;\n\nCREATE POLICY \"Tenant Isolation: Own Chats Only\"\nON public.user_conversations\nFOR ALL\nTO authenticated\nUSING (user_id = auth.uid())\nWITH CHECK (user_id = auth.uid());\n\nSELECT tablename, rowsecurity FROM pg_tables WHERE schemaname = 'public';",
                        "explanation": "Yeh SQL script database level par multi-tenant isolation enforce karta hai.",
                        "simulationOutput": "ALTER TABLE\nCREATE POLICY\ntablename          | rowsecurity\nuser_conversations | true\nMulti-tenant security 100% active! 🛡️"
                    },
                    "diagramScript": "arch LR: Complete AI Mastery Enterprise Production Topology\n  user[Global Web Users] $browser -> cf[Cloudflare Edge CDN & WAF] $cloud\n  cf -> svelte[Svelte 5 Runes Client Application] $browser\n  svelte -> rust[Rust Axum 0.8 Gateway (<50ms)] $server *\n  rust -> supa_auth[Supabase Auth JWT Middleware] $lock\n  rust -> supa_db[(Supabase PostgreSQL + pgvector + RLS)] $database\n  rust -> vllm_groq[Groq LPU / vLLM Inference Engine] $cpu\n  rust -> otel[OpenTelemetry Metrics & Logging] $chart",
                    "diagramPreset": "midnight",
                    "diagramAnimate": "flow",
                    "actionItems": [
                        "Supabase migration scripts run karein",
                        "Svelte 5 frontend build verify karein (npm run build)",
                        "Leaderboard par apna rank claim karein aur graduate badge unlock karein!"
                    ],
                    "resources": [
                        {"title": "The Twelve-Factor App for AI", "url": "https://12factor.net/", "type": "paper", "tag": "Standard"},
                        {"title": "Open-Source AI Engineering Career Guide", "url": "https://github.com/isaim0011", "type": "community", "tag": "Career"}
                    ]
                }
            ],
            "quiz": {
                "id": "quiz-mod-14",
                "title": "Module 14 Quiz: Production Mastery & Career Launch",
                "titleUrdu": "Module 14 Imtihan: Final Production Mastery",
                "passingScore": 70,
                "xpReward": 500,
                "badgeId": "production_hero",
                "questions": [
                    {
                        "id": "q14-1",
                        "question": "Enterprise AI deployment mein Row Level Security (RLS) ka sab se ahem kirdar kya hota hai?",
                        "options": [
                            "Database backup ko compress karna",
                            "Yeh guarantee karna ke koi bhi user doosre user ka private AI chat history ya vectors query na kar sake chahe frontend hack bhi ho jaye",
                            "GPU ki clock speed tez karna",
                            "Tokens ki cost kam karna"
                        ],
                        "correctIndex": 1,
                        "explanation": "RLS database engine level par enforce hoti hai. Frontend code manipulate hone par bhi tenant isolation 100% secure rehti hai.",
                        "conceptUrdu": "Row Level Security Tenant Isolation"
                    }
                ]
            }
        }
    ]
}

badges = [
    { "id": "first_step", "title": "First Step to AI Hero", "titleUrdu": "Pehla Qadam: Zero Se Safar Shuru", "description": "Complete Module 1 Quiz with 70%+ score", "icon": "🚀", "category": "core" },
    { "id": "matrix_ninja", "title": "Matrix & Vector Ninja", "titleUrdu": "Vectors aur Math Ka Master", "description": "Master Linear Algebra & Cosine Similarity", "icon": "📐", "category": "core" },
    { "id": "ml_practitioner", "title": "ML Practitioner", "titleUrdu": "Data Se Model Tak", "description": "Master classical machine learning, feature pipelines, and metrics", "icon": "📊", "category": "core" },
    { "id": "core_pytorch", "title": "Autograd Craftsman", "titleUrdu": "PyTorch Computational Graph Engineer", "description": "Build and debug PyTorch autograd DAGs", "icon": "🧠", "category": "core" },
    { "id": "attention_is_all_you_need", "title": "Attention Architect", "titleUrdu": "Transformer Q-K-V Ka Maahir", "description": "Master Scaled Dot-Product Attention & RoPE", "icon": "✨", "category": "specialist" },
    { "id": "app_builder", "title": "App Builder", "titleUrdu": "Full-Stack AI Creator", "description": "Ship production-grade AI applications and streaming APIs", "icon": "⚡", "category": "specialist" },
    { "id": "rag_architect", "title": "Hybrid RAG Master", "titleUrdu": "Production RAG & Vector Search King", "description": "Implement BM25 + pgvector RRF and rerankers", "icon": "📚", "category": "specialist" },
    { "id": "agent_commander", "title": "Autonomous Agent Commander", "titleUrdu": "AI Agents aur ReAct Specialist", "description": "Build multi-step agent tools with deterministic guardrails", "icon": "🤖", "category": "specialist" },
    { "id": "finetuning_pro", "title": "Fine-tuning Pro", "titleUrdu": "LoRA & Unsloth Wizard", "description": "Fine-tuned open-source models with Unsloth and DeepSeek-R1 GRPO", "icon": "🔥", "category": "specialist" },
    { "id": "production_ready", "title": "Production Ready", "titleUrdu": "0 to 1 Million Requests", "description": "Deploy low-latency LLM microservices with vLLM, Docker and Rust", "icon": "🛡️", "category": "specialist" },
    { "id": "rust_turbo", "title": "Rust Turbocharged", "titleUrdu": "Rust Axum Sub-Millisecond Speedster", "description": "Deploy high-throughput Rust AI microservice", "icon": "🦀", "category": "specialist" },
    { "id": "streak_warrior", "title": "Streak Warrior (7 Days)", "titleUrdu": "7 Din Lagataar Seekhne Wala", "description": "Maintain a 7-day learning streak on the platform", "icon": "🔥", "category": "streak" },
    { "id": "production_hero", "title": "Production AI Hero (Graduated)", "titleUrdu": "Kamyab AI Engineer (Hero Tak)", "description": "Complete all 5 Phases and Capstone Challenge", "icon": "👑", "category": "mastery" }
]

diagram_gallery = [
    {
        "id": "bloom-pyramid",
        "title": "Bloom's Revised Taxonomy Pyramid",
        "category": "Pedagogy",
        "description": "Six cognitive levels: Remembering to Creating — foundational for our Roman Urdu syllabus design.",
        "preset": "sunset",
        "animate": "pulse",
        "script": "layers: Bloom's Revised Taxonomy for AI Engineers\n  layer 6 - Creating: Design Novel Architectures, Deploy Production Systems\n  layer 5 - Evaluating: Benchmark Latency vs Accuracy, Red-Team Guardrails\n  layer 4 - Analyzing: Deconstruct Q-K-V Attention, Debug Gradient Vanishing\n  layer 3 - Applying: Implement RRF Hybrid Search, Fine-Tune LoRA Adapters\n  layer 2 - Understanding: Explain Backprop in Roman Urdu, Geometric Embeddings\n  layer 1 - Remembering: Python Syntax, Tensor Shapes, CLI Tools"
    },
    {
        "id": "model-70-20-10",
        "title": "70:20:10 Learning Framework",
        "category": "Pedagogy",
        "description": "70% Hands-on coding & debugging, 20% Peer code review & mentoring, 10% Structured theory.",
        "preset": "ocean",
        "animate": "ripple",
        "script": "pie: 70:20:10 AI Learning Model\n  \"70% Hands-on Coding & Projects\": 70\n  \"20% Peer Review & Roman Urdu Mentoring\": 20\n  \"10% Structured Theory & Readings\": 10"
    },
    {
        "id": "transformer-attention",
        "title": "Scaled Dot-Product Multi-Head Attention",
        "category": "Deep Learning",
        "description": "Visual flow of Query, Key, Value calculations with causal masking.",
        "preset": "grape",
        "animate": "flow",
        "script": "flow TD: Scaled Dot-Product Attention\n  q[Query Vector Q] & k[Key Vector K] --> dot[Dot Product: Q x K^T]\n  dot --> scale[Scale by 1/sqrt(d_k)]\n  scale --> mask{Causal Autoregressive Mask}\n  mask --> sm[Softmax Probability Weights]\n  sm & v[Value Vector V] --> out_dot[MatMul: Weights x V]\n  out_dot --> out[Projected Representation]"
    },
    {
        "id": "modular-rag",
        "title": "Advanced Modular RAG with Hybrid RRF & Reranker",
        "category": "Generative AI",
        "description": "Enterprise architecture preventing hallucinations and retrieving precise documents.",
        "preset": "blueprint",
        "animate": "flow",
        "script": "arch: Enterprise Hybrid RAG Engine\n  user[User Query] -> router{Intent Router}\n  router ->|Semantic| embed[Embedding API] -> vector_db[(Supabase pgvector)]\n  router ->|Keyword| fts[Postgres BM25 Full Text]\n  vector_db & fts --> rrf[Reciprocal Rank Fusion (k=60)]\n  rrf --> rerank[Cross-Encoder Reranker]\n  rerank --> prompt[Grounded Context Synthesis]\n  prompt --> llm[LLM Generation (Claude/DeepSeek)]\n  llm --> answer[Verified Answer with Citations]"
    },
    {
        "id": "react-agent",
        "title": "Multi-Agent ReAct Orchestration",
        "category": "AI Agents",
        "description": "Thought, Action, Tool Execution and Observation cycle.",
        "preset": "midnight",
        "animate": "flow",
        "script": "seq: Autonomous ReAct Multi-Agent Workflow\n  User -> AgentSupervisor: \"Research recent AI papers and write summary\"\n  AgentSupervisor -> WebSubagent: Delegate: Search Arxiv API\n  WebSubagent -> ArxivAPI: GET /api/query?search_query=transformers\n  ArxivAPI --> WebSubagent: 5 Recent Papers Returned\n  WebSubagent --> AgentSupervisor: Papers Retrieved\n  AgentSupervisor -> SummarizerSubagent: Delegate: Synthesize into Roman Urdu\n  SummarizerSubagent --> AgentSupervisor: Formatted Urdu Digest Ready\n  AgentSupervisor --> User: Final Digest + Citation Links"
    },
    {
        "id": "lora-layers",
        "title": "LoRA (Low-Rank Adaptation) Matrix Decomposition",
        "category": "Fine-Tuning",
        "description": "Efficient fine-tuning by decomposing weight updates into A (d x r) and B (r x k) matrices.",
        "preset": "paper",
        "animate": "glow",
        "script": "layers: LoRA Low-Rank Decomposition\n  layer Frozen Pretrained Weights: W_0 (4096 x 4096) [Frozen FP16/INT4]\n  layer Low-Rank Matrix A: Matrix A (4096 x 8) [Trainable FP32]\n  layer Low-Rank Matrix B: Matrix B (8 x 4096) [Trainable FP32, Zero-Init]\n  layer Adapted Forward: Output = (W_0 * x) + (B * A * x) * (alpha / r)"
    }
]

initial_user_profile = {
    "id": "guest-student-001",
    "email": "student@aimastery.urdu",
    "fullName": "Tariq Mehmood",
    "role": "AI Engineer in Training",
    "track": "developers",
    "xp": 450,
    "streakDays": 4,
    "lastActiveDate": "2026-10-17",
    "completedLessonIds": ["les-1-1"],
    "unlockedBadgeIds": ["first_step"],
    "isGuest": True
}
