use crate::{
    error::AppError,
    models::{DiagramIssueModel, DiagramRenderRequest, DiagramRenderResponse, GalleryDiagram},
};
use dkit_diagram::{RenderOptions, ThemeMode};

pub struct DiagramService;

impl DiagramService {
    pub fn render(req: &DiagramRenderRequest) -> Result<DiagramRenderResponse, AppError> {
        let script = req.script.trim();
        if script.is_empty() {
            return Err(AppError::BadRequest("DiagramKit script cannot be empty".to_string()));
        }

        // Compile script into DiagramKit AST spec
        let diagram = dkit_api::compile(script)
            .map_err(|e| AppError::DiagramError(format!("Script compilation error: {e}")))?;

        // Build render options
        let mut opts = RenderOptions::default();

        if let Some(preset) = &req.preset {
            opts.style.preset = Some(preset.clone());
        }

        if let Some(mode_str) = &req.mode {
            if let Some(m) = ThemeMode::parse(mode_str) {
                opts.style.mode = Some(m);
            }
        }

        if let Some(anim) = &req.animate {
            opts.style.animate = Some(anim.clone());
        }

        if let Some(speed) = req.speed {
            opts.style.speed = Some(speed);
        }

        // Render into animated, self-contained SVG with geometry verification
        let output = dkit_diagram::render(&diagram, &opts)
            .map_err(|e| AppError::DiagramError(format!("Rendering failed: {e}")))?;

        let valid = output.report.ok();
        let issues = output
            .report
            .issues
            .into_iter()
            .map(|i| DiagramIssueModel {
                code: i.code.to_string(),
                message: i.message,
            })
            .collect();

        Ok(DiagramRenderResponse {
            svg: output.svg,
            width: output.width,
            height: output.height,
            valid,
            issues,
            lint: output.lint,
            kind: output.kind.to_string(),
        })
    }

    pub fn render_script_to_svg(script: &str, preset: Option<&str>, animate: Option<&str>) -> Result<String, AppError> {
        let req = DiagramRenderRequest {
            script: script.to_string(),
            preset: preset.map(|s| s.to_string()).or_else(|| Some("midnight".to_string())),
            mode: Some("dark".to_string()),
            animate: animate.map(|s| s.to_string()).or_else(|| Some("flow".to_string())),
            speed: Some(1.0),
        };
        let res = Self::render(&req)?;
        Ok(res.svg)
    }

    pub fn get_gallery() -> Vec<GalleryDiagram> {
        let gallery_specs = vec![
            (
                "transformer-attention",
                "Transformer Multi-Head Attention",
                "Transformer Ka Multi-Head Attention Architecture",
                "Deep Learning & NLP",
                r#"@preset midnight
@animate wave
arch LR: Multi-Head Self Attention | Core building block of Modern LLMs
x[Input Embeddings] ~purple -> qkv[Linear Projections // Q, K, V]
qkv -> q[Queries Q] ~info
qkv -> k[Keys K] ~teal
qkv -> v[Values V] ~teal
q -> dot((Q . K^T))
k -> dot
dot -> scale[Scale & Mask // sqrt d_k] -> soft[Softmax // Attention Weights]*
soft -> prod((Attention x V))
v -> prod
prod -> out[Linear Out] ~ok -> res((Residual Add & Norm)) ~purple"#,
                "Detailed architecture of the scaled dot-product multi-head attention mechanism used in modern LLMs.",
            ),
            (
                "rag-pipeline",
                "Production Hybrid RAG Architecture",
                "Production Hybrid RAG Pipeline (Dense + Sparse)",
                "Generative AI & LLMs",
                r#"@preset midnight
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
group Retrieval: vdb bm25 rrf"#,
                "Complete enterprise retrieval-augmented generation pipeline with hybrid retrieval (vector + BM25) and re-ranking.",
            ),
            (
                "react-agent-loop",
                "Autonomous AI Agent ReAct Loop",
                "Autonomous AI Agent Ka ReAct Cycle (Thought - Action - Observation)",
                "Autonomous Agents",
                r#"@preset midnight
@animate pulse
flow TB: Autonomous AI Agent ReAct Loop | Reasoning + Acting Cycle
user[User Goal / Task] $user ~purple -> thought[1. Thought // Reasoning & Plan]* $ai
thought -> action[2. Action // Select Tool & Args] ~info
action -> exec[3. Tool Execution // Search, DB, API, Python] $gear ~teal
exec -> obs[4. Observation // Raw Tool Result] ~teal
obs -> reflect{Goal Achieved?}*
reflect ->|No - Need more info| thought
reflect ->|Yes - Completed| final((5. Final Answer & Deliverable)) ~ok"#,
                "The ReAct loop: how modern reasoning agents decide on tool calls, observe results, and self-correct.",
            ),
            (
                "lora-matrix-decomposition",
                "LoRA Parameter-Efficient Fine-Tuning",
                "LoRA Low-Rank Adaptation (A x B Decomposition)",
                "Model Fine-Tuning",
                r#"@preset midnight
@animate glow
arch LR: LoRA Matrix Decomposition | Low-Rank Adaptation (PEFT)
x[Input Activation x // dim d] ~purple -> w0[Frozen Base Weights W0 // d x k]* ~muted
x -> a[LoRA Matrix A // d x r, Gaussian Init] ~info
a -> b[LoRA Matrix B // r x k, Zero Init]* ~teal
w0 -> add((+))
b -> scale[Scaling // alpha / r] -> add
add -> y[Output Activation y // dim k] ~ok"#,
                "Mathematical low-rank adapter decomposition allowing fine-tuning of 70B models on commodity GPUs.",
            ),
            (
                "mlops-pipeline",
                "Full-Lifecycle MLOps & LLMOps",
                "Production MLOps Pipeline: Training Se Deployment Tak",
                "MLOps & Platform Engineering",
                r#"@preset midnight
@animate flow
flow LR: Modern MLOps & LLMOps Lifecycle | Zero to Production Pipeline
git[[Code & Config // Git]] $github ~purple -> ci[CI/CD & Lint] ~info
data[(Curated Datasets & Prompts)] $db ~teal -> train[Distributed Training / PEFT] $cpu ~teal
train -> eval{Evaluation Suite // ROUGE, BLEU, LLM-as-Judge}*
eval ->|Pass| reg[(Model Registry // MLflow / W&B)] $db ~ok
eval ->|Fail| train
reg -> deploy[Kubernetes / vLLM Serving // Fast Inference] $docker ~info
deploy -> mon[Telemetry & Drift Monitoring // Prometheus + Tracing] $chart ~purple
mon -->|Data Drift Feedback| data"#,
                "End-to-end continuous training, automated evaluation gates, model registry, and containerized serving.",
            ),
            (
                "blooms-taxonomy-pyramid",
                "Bloom's Learning Taxonomy for AI",
                "AI Engineers Ka Learning Pyramid (Theory Se Creation Tak)",
                "Pedagogy & Curriculum",
                r#"@preset midnight
@animate glow
pyramid: AI Mastery Bloom's Taxonomy | Hierarchy of Learning & Engineering
Create // Ship End-to-End Production AI Systems & Custom Architectures*
Evaluate // Benchmark, LLM-as-a-Judge, Red-Teaming & Cost-Latency Tradeoffs
Analyze // Error Profiling, Embedding Geometries & Tensor Bottlenecks
Apply // Implement PyTorch Modules, LoRA Fine-Tuning & Multi-Agent Graphs
Understand // Intuition behind Attention, Backprop, Loss Landscapes & RAG
Remember // Python Syntax, Vector Math, PyTorch APIs & Model Terminology"#,
                "Structured pedagogical framework used in this course to transition from rote memory to shipping novel systems.",
            ),
            (
                "learning-methodology-pie",
                "70:20:10 Hands-on Learning Model",
                "70:20:10 Practical Learning Methodology",
                "Pedagogy & Curriculum",
                r#"@preset midnight
pie: 70:20:10 AI Mastery Learning Model | Active Mastery Framework
Hands-on Code & Capstone Projects = 70*
Peer Code Reviews & Community Hackathons = 20
Deep Dive Theory & Architectural Lectures = 10"#,
                "Distribution of effort: 70% active coding and building, 20% collaboration and code review, 10% theory.",
            ),
            (
                "gantt-roadmap",
                "20-Week Master AI Engineering Roadmap",
                "20 Hafton Ka Complete Roadmap (Zero Se Production)",
                "Roadmap & Phases",
                r#"@preset midnight
gantt: 20-Week Master AI Engineering Roadmap | 5 Phases to Production
section Phase 1 Foundations
Python Mastery & OOP | 2026-01-05 | 2w
Vectors, Tensors & Linear Algebra | after Python Mastery & OOP | 2w
section Phase 2 Machine Learning
Classical ML & Scikit-Learn | after Vectors, Tensors & Linear Algebra | 2w
Deep Learning & PyTorch from Scratch | after Classical ML & Scikit-Learn | 2w*
section Phase 3 Transformers & RAG
Computer Vision & Modern NLP | after Deep Learning & PyTorch from Scratch | 2w
Transformers & Multi-Head Attention | after Computer Vision & Modern NLP | 2w*
Production RAG & Vector DBs | after Transformers & Multi-Head Attention | 2w
section Phase 4 Agents & Fine-Tuning
PEFT, LoRA & QLoRA Fine-Tuning | after Production RAG & Vector DBs | 2w
Autonomous AI Agents & Tool Calling | after PEFT, LoRA & QLoRA Fine-Tuning | 2w*
Multimodal Vision-Language Systems | after Autonomous AI Agents & Tool Calling | 1w
section Phase 5 Production MLOps
vLLM Serving, TensorRT & MLOps | after Multimodal Vision-Language Systems | 2w
Real-World Capstone System | after vLLM Serving, TensorRT & MLOps | 2w*
milestone AI Mastery Certified Engineer | after Real-World Capstone System"#,
                "The complete 20-week progressive timeline mapped across all 5 phases and milestones.",
            ),
        ];

        gallery_specs
            .into_iter()
            .map(|(id, title, urdu_title, category, script, desc)| {
                let svg = Self::render_script_to_svg(script, Some("midnight"), Some("flow"))
                    .unwrap_or_else(|_| "<svg><text>Error rendering diagram</text></svg>".to_string());
                GalleryDiagram {
                    id: id.to_string(),
                    title: title.to_string(),
                    urdu_title: urdu_title.to_string(),
                    category: category.to_string(),
                    script: script.to_string(),
                    svg,
                    description: desc.to_string(),
                }
            })
            .collect()
    }
}
