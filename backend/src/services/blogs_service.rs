use crate::models::{
    CloudPlatformRecipe, EngineeringBlog, FreeApiProvider, ZeroGpuGuide,
};
use crate::services::diagram_service::DiagramService;

pub fn get_zero_gpu_guide() -> ZeroGpuGuide {
    ZeroGpuGuide {
        title: "Zero-GPU Cloud Compute Survival Guide 2026".to_string(),
        urdu_subtitle: "Bina local GPU ke Google Colab, Kaggle Dual-T4, Google One Pro 1000 Units aur Free SOTA APIs ka mukammal blueprint".to_string(),
        description: "Agar aapke pas local GPU nahi hai to pareshan hone ki bilkul zaroorat nahi! 2026 mein Google Colab Free T4, Kaggle 30 hours/week Dual T4 (30GB VRAM), Google One Pro 1000 Compute Units, aur Free SOTA API providers (Groq, Cerebras, Google AI Studio) ke zariye aap production model training aur deployment 100% free kar sakte hain.".to_string(),
        colab_free_t4: CloudPlatformRecipe {
            platform: "Google Colab Free Tier (Nvidia T4 15GB VRAM)".to_string(),
            vram: "15 GB GDDR6".to_string(),
            weekly_quota: "Approx 12-16 hours per session (resets daily)".to_string(),
            cost: "$0.00 (100% Free)".to_string(),
            setup_instructions_urdu: "Google Colab mein Notebook kholein, Runtime menu par ja kar 'Change runtime type' select karein aur 'T4 GPU' choose karein. Session khatam hone par hamesha runtime unassign zaroor karein taake aapka cooldown trigger na ho.".to_string(),
            setup_snippet: "!pip install -q torch transformers datasets accelerate bitsandbytes peft trl unsloth\nimport torch\nprint('Device:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU')".to_string(),
            saver_script: Some("from google.colab import runtime\n# Job mukammal hote hi automatically session terminate karein taake compute waste na ho:\nruntime.unassign()".to_string()),
        },
        kaggle_dual_t4: CloudPlatformRecipe {
            platform: "Kaggle Notebooks (Dual Nvidia T4 2x15GB = 30GB VRAM)".to_string(),
            vram: "30 GB Combined VRAM (2x T4 GPUs)".to_string(),
            weekly_quota: "30 Hours per week (resets every Saturday)".to_string(),
            cost: "$0.00 (100% Free phone-verified account)".to_string(),
            setup_instructions_urdu: "Kaggle settings panel mein 'Accelerator' -> 'GPU T4 x 2' select karein. Dual T4 ke sath aap PyTorch DDP ya Hugging Face Accelerate ke zariye 14B models ko bhi asaani se fine-tune kar sakte hain.".to_string(),
            setup_snippet: "!accelerate config default\nimport torch\nprint('Available GPUs:', torch.cuda.device_count())".to_string(),
            saver_script: Some("import os\n# Auto-commit notebook or save model weights to Kaggle Dataset before quota ends\nos.system('kaggle datasets version -p ./weights -m \"Auto save checkpoint\"')".to_string()),
        },
        google_one_compute_units_saver: CloudPlatformRecipe {
            platform: "Google One Pro / Colab Pro (100 - 1000 Compute Units Optimizer)".to_string(),
            vram: "Nvidia A100 (40GB/80GB) ya L4 (24GB)".to_string(),
            weekly_quota: "100 to 1000 Compute Units (paid / Google One AI Premium bundle)".to_string(),
            cost: "Google One AI Premium bundle ($19.99/mo with 2TB storage) or standalone".to_string(),
            setup_instructions_urdu: "A100 GPU 1.3 to 2.5 compute units fi-ghanta consume karta hai. Agar training ke baad notebook open reh gayi to raat bhar mein 50+ units zaya ho jayenge! Hamesha Python try-finally block mein `runtime.unassign()` lagayein.".to_string(),
            setup_snippet: "# Run heavy 70B LoRA or Unsloth GRPO on A100 GPU\n!pip install -q \"unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git\"".to_string(),
            saver_script: Some("try:\n    # Training running...\n    pass\nfinally:\n    from google.colab import runtime\n    print('Training finished or failed. Disconnecting runtime to save compute units!')\n    runtime.unassign()".to_string()),
        },
        free_api_providers: vec![
            FreeApiProvider {
                name: "Groq Cloud Free Tier".to_string(),
                free_tier_limits: "30 requests/min, 14,400 requests/day, 6,000 tokens/min".to_string(),
                speed: "300 - 500 tokens/sec".to_string(),
                best_for: "Ultra-low latency LLM inference, Llama 3.3 70B, real-time agent tool loops".to_string(),
                endpoint_url: "https://api.groq.com/openai/v1/chat/completions".to_string(),
                sample_curl: "curl -X POST https://api.groq.com/openai/v1/chat/completions -H \"Authorization: Bearer $GROQ_API_KEY\" -H \"Content-Type: application/json\" -d '{\"model\": \"llama-3.3-70b-versatile\", \"messages\": [{\"role\": \"user\", \"content\": \"Assalam-o-Alaikum!\"}]}'".to_string(),
            },
            FreeApiProvider {
                name: "Google AI Studio (Gemini 2.0 Flash / Pro)".to_string(),
                free_tier_limits: "15 requests/min, 1,500 requests/day, 1M token context window".to_string(),
                speed: "150 - 200 tokens/sec".to_string(),
                best_for: "Massive context analysis (books, PDFs, video), multimodal vision, complex reasoning".to_string(),
                endpoint_url: "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent".to_string(),
                sample_curl: "curl \"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=$GEMINI_API_KEY\" -H 'Content-Type: application/json' -d '{\"contents\": [{\"parts\": [{\"text\": \"Roman Urdu mein AI samjhao.\"}]}]}'".to_string(),
            },
            FreeApiProvider {
                name: "Cerebras Inference Free Tier".to_string(),
                free_tier_limits: "30 requests/min, 1M tokens/day".to_string(),
                speed: "1,800+ tokens/sec (World's Fastest Inference)".to_string(),
                best_for: "Instant speculative decoding, synthetic data generation, high-frequency agent thoughts".to_string(),
                endpoint_url: "https://api.cerebras.ai/v1/chat/completions".to_string(),
                sample_curl: "curl -X POST https://api.cerebras.ai/v1/chat/completions -H \"Authorization: Bearer $CEREBRAS_API_KEY\" -H \"Content-Type: application/json\" -d '{\"model\": \"llama3.1-8b\", \"messages\": [{\"role\": \"user\", \"content\": \"Fast reasoning test\"}]}'".to_string(),
            },
        ],
    }
}

pub fn get_engineering_blogs() -> Vec<EngineeringBlog> {
    let raw_blogs = vec![
        (
            1,
            "zero-gpu-survival-guide-2026",
            "Zero-GPU Survival Guide 2026: Google Colab, Kaggle 30h Dual-T4 & Google One Pro 1000 Compute Units Mastery",
            "Cloud & Compute",
            12,
            "Bina kisi local GPU ke production-grade models fine-tune karein aur Google One Pro compute units ko auto-disconnect script se 100% bachaayein.",
            r#"Agar aapke pas RTX 4090 ya Mac M3 Max nahi hai, to pareshan hone ki bilkul zaroorat nahi! 2026 mein modern AI engineering hardware-poor engineers ke liye pehle se kahin zyada accessible hai.

### 1. The Reality of Hardware Hierarchy
- **Google Colab Free T4 (15GB GDDR6)**: Fast prototyping, inference, and QLoRA on 7B/8B models.
- **Kaggle Dual-T4 (30GB Combined VRAM)**: 30 hours per week free! PyTorch DDP aur Accelerate ke zariye 14B models comfortably fine-tune ho sakte hain.
- **Google One Pro (100-1000 Compute Units)**: Agar aapke pas Google One 2TB AI Premium plan hai to aapko monthly 100 se 1000 compute units milte hain. Is se aap Nvidia A100 (40GB/80GB) ya L4 GPUs run kar sakte hain.

### 2. The Dreaded 'Forgot to Disconnect' Disaster
A100 GPU 2.5 compute units per hour consume karta hai. Agar raat ko model train karne laga kar so gaye aur notebook chal rahi to subah tak 60 units zaya! Iska hal `runtime.unassign()` hai.

### 3. Step-by-Step Survival Recipe
Hamesha apne Python script ko `try...finally` block mein wrap karein taake job pass ho ya fail, runtime foran shutdown ho jaye!"#,
            Some(r#"# Google Colab Auto-Disconnect & Saver Script
import time
import torch

try:
    print(f"CUDA Device: {torch.cuda.get_device_name(0)}")
    print("Training Unsloth 4-bit LoRA adapter...")
    # Your training loop here
    time.sleep(2)
    print("Training successfully finished & weights pushed to HuggingFace Hub!")
except Exception as e:
    print(f"Error during training: {e}")
finally:
    # Google One Pro / Colab Pro 1000 Compute Units Saver:
    try:
        from google.colab import runtime
        print("Disconnecting runtime to save your precious compute units!")
        runtime.unassign()
    except ImportError:
        print("Not running in Google Colab environment.")
"#),
            Some("Google Colab Free T4 (15GB VRAM) ya Kaggle Dual-T4 (30h/week). Cost: $0.00. Unassign script prevents compute burn."),
            r#"@preset midnight
@animate flow
flow LR: Zero-GPU Cloud Compute Strategy 2026
dev[Local Laptop // 0-VRAM] ~purple -> choose{Workload Type?}*
choose ->|Rapid Prototyping| colab[Google Colab Free T4 // 15GB VRAM] ~info
choose ->|Heavy Fine-Tuning| kaggle[Kaggle Dual T4 // 30GB VRAM, 30h/wk] ~teal
choose ->|Long Jobs & A100| gpro[Google One Pro // 1000 Compute Units]* ~ok
choose ->|High Speed Inference| freeapi[Groq & Gemini Flash Free Tier // 300+ tps] ~purple
colab -> saver[Auto-Disconnect Saver // runtime.unassign()]* $bolt ~ok
gpro -> saver"#,
            "midnight",
            "flow",
        ),
        (
            2,
            "why-85-percent-fail-ai",
            "Why 85% Fail AI Courses (And How Top-Down + First-Principles Makes You Unstoppable)",
            "Learning Strategy",
            8,
            "85% log AI seekhte waqt calculus ke jhanjhat mein phas kar drop out kar jate hain; top-down methodology pehle din working system deploy karwati hai.",
            r#"Aksar university courses aur online tutorials students ko pehle 6 mahine calculus, matrix proofs, aur dry probability padhate hain. Nateeja? Student 4 hafton baad demotivate ho kar chor deta hai kyunki usne koi working cheez nahi banayi hoti.

### 1. Top-Down Learning (The fast.ai & Karpathy Way)
- **Day 1**: Working LLM pipeline, semantic search, ya computer vision model run karein.
- **Week 2**: Uske components ko inspect karein — embedding kya hai? Tokenizer kahan fail hota hai?
- **Week 3-4**: First-principles depth mein jayein — self-attention ka QK^T matrix multiplication khud NumPy mein likhein.

### 2. Active Recall & The 70:20:10 Rule
70% waqt code likhne aur real-world projects banane mein, 20% code review aur debugging mein, aur sirf 10% passive video lecture dekhne mein lagayein."#,
            Some(r#"# Top-Down Example: Day 1 Working Inference Pipeline
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
result = classifier("Shipping working AI code on Day 1 is 10x better than passive theory!")
print("Classification:", result)
"#),
            Some("Local CPU / Google Colab Free Tier. Cost: $0.00. Zero GPU required for inference."),
            r#"@preset midnight
@animate pulse
flow LR: Top-Down vs Bottom-Up AI Mastery
trap[Bottom-Up Trap // 6 Months Calculus Paralysis] ~muted -> fail[85% Drop Out // Zero Shipped Projects]* ~danger
sol[Top-Down Mastery // Ship Working System Day 1] ~purple -> peel[Peel Layers First-Principles // Math as Needed]* ~teal
peel -> build[Build PyTorch From Scratch] ~info
build -> prod[15% Top AI Engineers // Shipped Portfolio] ~ok"#,
            "midnight",
            "pulse",
        ),
        (
            3,
            "tensors-memory-strides",
            "Tensors & Memory Strides Under the Hood: Zero-Copy Layouts & SIMD",
            "Low-Level AI",
            10,
            "Tensor asal mein RAM ka aik flat 1D buffer hota hai; strides aur storage offsets samajh kar zero-copy high performance code likhein.",
            r#"PyTorch ya NumPy mein jab aap `tensor.transpose(0, 1)` karte hain to kya data memory mein move hota hai? Bilkul nahi! Yeh zero-copy operation hai jo sirf metadata strides ko update karta hai.

### 1. Strides Ka Concept
Strides yeh batate hain ke agle row ya column par jane ke liye memory mein kitne elements aage koodna (stride) hai. Aik (3, 4) float32 tensor ka default row-major stride (4, 1) hota hai.

### 2. The `.contiguous()` Trap
Jab tensor non-contiguous ho jata hai (jaise transpose ke baad), aur aap `.view()` call karte hain, to PyTorch error deta hai! Aapko `.contiguous()` call karna padta hai jo naya buffer allocate karta hai. Is overhead se bachna high-scale production systems ke liye zaroori hai."#,
            Some(r#"import torch

# 2D Tensor shape (3, 4)
x = torch.arange(12, dtype=torch.float32).reshape(3, 4)
print("Original Shape:", x.shape, "Strides:", x.stride())
print("Is Contiguous:", x.is_contiguous())

# Transpose is ZERO-COPY!
t = x.t()
print("Transposed Shape:", t.shape, "Strides:", t.stride())
print("Is Contiguous:", t.is_contiguous())
"#),
            Some("Pure Python / NumPy / PyTorch CPU. Zero VRAM. Execution time: <10ms."),
            r#"@preset midnight
@animate wave
arch LR: Tensor Memory Layout & Strides Under the Hood
logical[2D Matrix 3x4 // Shape & Dtype] ~purple -> strides[Strides 4,1 // Byte Steps]* ~info
strides -> ram[(1D Flat Contiguous Buffer in RAM/VRAM)] $db ~teal
ram -> op{Transpose / Reshape}*
op ->|Zero-Copy View| view[New Metadata Strides 1,4 // 0-Copy] ~ok
op ->|Non-Contiguous .contiguous()| clone[Deep Memory Copy // Allocation Penalty] ~danger"#,
            "midnight",
            "wave",
        ),
        (
            4,
            "the-illustrated-transformer",
            "The Illustrated Transformer & Scaled Dot-Product Attention (sqrt{d_k} Math Intuitively)",
            "Deep Learning",
            15,
            "Scaled Dot-Product Attention ka QK^T matrix math, sqrt{d_k} scaling ki mathematical waja, aur causal masking ki visual explanation.",
            r#"Transformer architecture 2017 mein introduce hua aur aaj tak sabhi SOTA LLMs (GPT-4o, Claude 3.5, Llama 3, DeepSeek) ki bunyad hai. Lekin attention mechanism asal mein karta kya hai?

### 1. Query, Key, aur Value Ka Mental Model
- **Query (Q)**: 'Main kya dhoond raha hoon?'
- **Key (K)**: 'Mere pas kya information moojood hai?'
- **Value (V)**: 'Meri actual content details kya hain?'
Jab Q aur K ka dot product lete hain to correlation score nikalta hai.

### 2. sqrt{d_k} Se Divide Kyun Karte Hain?
Agar dimension d_k bara ho (maslan 64 ya 128), to dot products ka variance bara ho jata hai. Softmax function bare numbers par saturate ho jata hai aur gradients zero ho jate hain (vanishing gradients). sqrt{d_k} se divide karne se variance wapis 1 par rehti hai!"#,
            Some(r#"import torch
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
print("Output shape:", out.shape, "Attention sum:", weights.sum(dim=-1))
"#),
            Some("Runs locally on CPU or Colab Free T4 in 5ms. Memory: <50MB RAM."),
            r#"@preset midnight
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
out -> proj[Linear Output Projection Wo] ~ok"#,
            "midnight",
            "wave",
        ),
        (
            5,
            "kv-cache-paged-attention",
            "KV-Cache & PagedAttention (vLLM): Breaking the GPU Memory Wall",
            "Inference & Systems",
            11,
            "LLM generation ke waqt KV Cache VRAM kyun bhar deta hai aur vLLM ka PagedAttention virtual memory paging ke zariye 80% waste kaise khatam karta hai.",
            r#"Autoregressive LLM inference mein har naya token generate karne ke liye purane tokens ke Key aur Value tensors dobara compute nahi kiye jate — unhe VRAM mein cache kiya jata hai jise **KV-Cache** kehte hain.

### 1. Naive Allocation Ka Nuqsan
Traditional systems har request ke liye max sequence length (maslan 4,096 tokens) ka contiguous VRAM block pehle se book kar lete the. Agar user ne sirf 100 tokens generate kiye to baqi 97% memory zaya (internal fragmentation)! Nateeja: GPU sirf 2 ya 3 concurrent requests handle kar sakti thi.

### 2. PagedAttention Ka Inqilab (vLLM)
Operating Systems ke Virtual Memory Paging concept ko adopt karte hue, PagedAttention KV-cache ko chote non-contiguous blocks (e.g. 16 tokens per block) mein divide karta hai. Is se GPU memory utilization 20% se seedha 96% par chali jati hai aur throughput 4x-10x barh jati hai!"#,
            Some(r#"def kv_cache_size_gb(num_layers, hidden_size, seq_len, batch_size, bytes_per_elem=2):
    bytes_total = 2 * num_layers * hidden_size * bytes_per_elem * seq_len * batch_size
    return bytes_total / (1024 ** 3)

vram_for_100_users_4k = kv_cache_size_gb(32, 4096, 4096, 100)
print(f"KV Cache for 100 users @ 4k tokens: {vram_for_100_users_4k:.2f} GB VRAM!")
"#),
            Some("Deploy on RunPod / Colab Pro L4 / local vLLM. Zero-VRAM estimation script runs on CPU."),
            r#"@preset midnight
@animate flow
flow LR: KV-Cache & PagedAttention Memory Architecture
prompt[Prompt Tokens] ~purple -> prefill[Prefill Phase // Parallel Compute]* $cpu ~info
prefill -> init_kv[Initial K & V Tensors] ~teal
gen[Autoregressive Decode Step] ->|New Single Token| append[Append New K, V Vector]
append -> vmem{Standard Allocation?}*
vmem ->|Naive Contiguous Alloc| frag[60-80% VRAM Waste & Memory Fragmentation] ~danger
vmem ->|PagedAttention vLLM| table[Virtual Page Table // Non-Contiguous Blocks]* ~ok
table -> vram[(VRAM Physical Blocks // 96% Memory Utilization)] $db ~ok"#,
            "midnight",
            "flow",
        ),
        (
            6,
            "vector-search-vs-hybrid-rag",
            "Pure Vector Search vs Hybrid RAG (BM25 + pgvector + RRF + ColPali Vision RAG)",
            "Information Retrieval",
            14,
            "Kyun sirf vector cosine similarity real enterprise RAG mein fail hoti hai aur BM25 keyword search + pgvector + RRF + ColPali se zero hallucination kaise hasil karein.",
            r#"Standard RAG tutorials mein log sirf `text-embedding-3-small` use kar ke vector search karte hain. Lekin jab client pooche: 'Invoice number #PK-9821 ka total bill kitna tha?', to vector search fail ho jata hai kyunki invoice number ka koi semantic meaning nahi hota!

### 1. Hybrid Search (Dense + Sparse)
- **Sparse (BM25 / Full-Text)**: Exact part numbers, invoice IDs, acronyms, aur names pakadta hai.
- **Dense (pgvector HNSW)**: Conceptual similarity aur fuzzy semantics pakadta hai.

### 2. Reciprocal Rank Fusion (RRF)
Dono lists ko bina score normalization ke merge karne ke liye RRF formula use hota hai:
`RRF_Score(d) = sum(1 / (k + rank(d)))` jahan `k = 60`.

### 3. ColPali (Vision-Language RAG 2026)
Complex multi-column PDFs, tables, aur Pakistani Urdu cheques ke liye text extract karne ke bajaye pooray page ka screenshot embed kiya jata hai via ColPali late-interaction!"#,
            Some(r#"def rrf_merge(bm25_ranks, vector_ranks, k=60):
    scores = {}
    for rank, doc_id in enumerate(bm25_ranks):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
    for rank, doc_id in enumerate(vector_ranks):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)

bm25 = ["doc_invoice_9821", "doc_receipt_12", "doc_legal_contract"]
vector = ["doc_legal_contract", "doc_invoice_9821", "doc_tax_return"]
ranked = rrf_merge(bm25, vector)
print("Top Fused Document:", ranked[0])
"#),
            Some("PostgreSQL with pgvector + Supabase free tier. Embeddings via Groq / Gemini Flash API."),
            r#"@preset midnight
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
rerank -> topk[Top-K High-Precision Context] ~ok"#,
            "midnight",
            "flow",
        ),
        (
            7,
            "mcp-and-smolagents",
            "Anthropic MCP & Hugging Face smolagents: Why Code Agents Beat Brittle Chains",
            "Agentic AI",
            13,
            "JSON-based tool calling aur LangChain chains kyun toot-ti hain; Anthropic Model Context Protocol aur executable Python CodeAgents ka jadeed tareeqa.",
            r#"2024 tak log brittle JSON chains aur LangChain use kar rahe the. Thori si schema change hoti thi aur agent crash ho jata tha! 2026 ka gold standard **Code Agents** aur **Model Context Protocol (MCP)** hai.

### 1. CodeAgent Advantage (Hugging Face smolagents)
Agent se JSON nikalne ke bajaye us se seedha Python code likhwayein. Code sandbox mein run hota hai, loop chala sakta hai, conditions check kar sakta hai, aur 3x kam LLM calls mein kaam khatam karta hai.

### 2. Anthropic Model Context Protocol (MCP)
MCP aik open standard protocol hai jo LLMs ko enterprise data sources (Postgres, GitHub, Slack, local filesystem) se connect karta hai securely via standardized JSON-RPC."#,
            Some(r#"from smolagents import CodeAgent, HfApiModel, tool

@tool
def get_crypto_price_pkr(coin: str) -> str:
    """Fetches real-time crypto price in PKR.
    Args:
        coin: Symbol like BTC or ETH
    """
    return f"{coin} price is currently PKR 27,850,000"

agent = CodeAgent(tools=[get_crypto_price_pkr], model=HfApiModel())
print("CodeAgent initialized with MCP tool support.")
"#),
            Some("Groq Free API (Llama 3.3 70B) ya Cerebras Free API. Local CPU sandbox. $0.00 Cost."),
            r#"@preset midnight
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
self_heal ->|Success| deliverable((Final Validated Deliverable)) ~ok"#,
            "midnight",
            "pulse",
        ),
        (
            8,
            "unsloth-4bit-qlora",
            "Unsloth 4-Bit QLoRA Math: Fine-Tuning 8B Models on a Free 15GB Colab T4",
            "Model Training",
            12,
            "Unsloth custom OpenAI Triton kernels ke zariye VRAM 80% kaise bachaata hai aur free Colab T4 par Llama 3 8B model 5x tezi se kaise train hota hai.",
            r#"Standard Hugging Face PEFT mein 8B model fine-tune karne ke liye kam az kam 24GB VRAM (RTX 3090/4090) zaroori hoti hai. Lekin Unsloth ne game badal diya!

### 1. Manual Backprop in Triton
Unsloth ne PyTorch ke autograd ko bypass kar ke manually written OpenAI Triton kernels banaye. Is se Cross-Entropy loss aur RoPE embeddings ka memory footprint 80% kam ho jata hai.

### 2. NF4 Quantization + LoRA Rank r=16
Base model ke weights 4-bit NormalFloat (NF4) mein freeze rehte hain, jabke sirf choti low-rank matrices A aur B train hoti hain. Free Colab T4 GPU (15GB VRAM) par batch size 4 ke sath training makhan ki tarah chalti hai!"#,
            Some(r#"from unsloth import FastLanguageModel

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
print("Model ready for ultra-fast training on Free Google Colab T4!")
"#),
            Some("Google Colab Free Tier (T4 GPU 15GB). Training time: ~20 mins on 1k samples. Cost: $0.00."),
            r#"@preset midnight
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
out -> loss[Cross-Entropy Loss] -> unsloth[Unsloth Fast Triton Kernels // 5x Speed, 80% Less VRAM]* ~ok"#,
            "midnight",
            "glow",
        ),
        (
            9,
            "deepseek-r1-and-grpo",
            "DeepSeek-R1 & GRPO: How Reasoning Models Learn to <think> Without a Critic Model",
            "Reinforcement Learning",
            16,
            "DeepSeek-R1 ne PPO ke baray Critic model ko khatam kar ke Group Relative Policy Optimization (GRPO) ke zariye reasoning models kaise banaye.",
            r#"DeepSeek-R1 ne OpenAI o1 ko challenge kar ke puri dunya ko hairaan kar diya. Unka sab se bara breakthrough kya tha? **GRPO (Group Relative Policy Optimization)**.

### 1. Traditional PPO Ka Masla
Traditional RLHF (PPO) mein policy model ke barabar ka aik doosra 'Critic / Value Model' VRAM mein rakhna padta tha. 70B model ke sath 70B critic model run karne ke liye 8x H100 GPUs chahiye the!

### 2. GRPO Ka Simple Magic
GRPO mein koi critic model nahi hota! Model aik prompt ke liye 4 se 8 mukhtalif jawab generate karta hai. Phir deterministic rules (maslan: kya compiler ne code pass kiya? kya math answer theek hai?) se har answer ko reward milta hai. Phir is group ka mean aur standard deviation nikaal kar advantage calculate hota hai!

### 3. Emergence of <think> Tokens
Model ko kisi ne explicitly nahi sikhaya ke <think> likho. Jab correct answer par reward mila to model ne khud ba khud lambi chain-of-thought aur self-correction strategy evolve kar li!"#,
            Some(r#"import numpy as np

def compute_grpo_advantages(rewards: list[float], epsilon=1e-6) -> np.ndarray:
    r = np.array(rewards)
    mean_r = np.mean(r)
    std_r = np.std(r) + epsilon
    advantages = (r - mean_r) / std_r
    return advantages

rewards = [1.0, 0.0, -0.5, 1.0]
adv = compute_grpo_advantages(rewards)
print("GRPO Group Advantages:", adv)
"#),
            Some("Kaggle Dual-T4 (30h/week) or Colab Pro with Unsloth GRPO trainer. $0.00 cost."),
            r#"@preset midnight
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
ppo -> trained[Reasoning Master Model // DeepSeek-R1 style] ~purple"#,
            "midnight",
            "wave",
        ),
        (
            10,
            "learner-to-3k-ai-engineer",
            "From Learner to $3k+ AI Engineer: Packaging AI Microservices with Supabase & Rust",
            "Career & Architecture",
            9,
            "Pakistan aur remote market mein $3k-$5k/month kamane wale AI Engineer kaise banain; portfolio projects, Rust microservices, aur Supabase architecture.",
            r#"Sirf Jupyter Notebook run karna aapko AI engineer nahi banata. Clients notebook nahi khareedte — clients **reliable, fast, production-ready APIs** chahte hain jo sub-50ms latency mein unke business problems solve karein.

### 1. The $3k/mo Tech Stack
- **Backend**: Rust Axum (10x faster than FastAPI, zero memory leaks, sub-10ms overhead).
- **Database**: Supabase PostgreSQL with `pgvector`, Row Level Security (RLS), aur Supabase Auth.
- **Inference Router**: Groq / Gemini Flash for 90% cheap queries + DeepSeek-R1 / Claude for hard reasoning.
- **Frontend**: Svelte 5 / SvelteKit (clean, light, Claude-style UI).

### 2. Upwork & Direct Client Strategy
Kabhi 'I will do AI' ka generic proposal na bhejein. Har proposal ke sath aik working loom video ya interactive URL bhejein (jaise aapka Capstone project). Client ko dikhayein ke aapne unka problem pehle hi solve kar rakha hai!"#,
            Some(r#"use axum::{routing::post, Json, Router};
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
}
"#),
            Some("Deploy to Fly.io free tier or Railway + Supabase Free PostgreSQL. $0.00 startup cost."),
            r#"@preset midnight
@animate flow
flow LR: $3,000/mo AI Engineer Production Architecture
client[Global Upwork / Enterprise Clients] $user ~purple -> gateway[Rust Axum Gateway // <10ms Auth & Rate Limit]* ~ok
gateway -> cache[(Redis / Memory Semantic Cache)] $bolt ~teal
gateway -> supa[(Supabase Auth, pgvector & Realtime DB)] $db ~info
gateway -> llm_pool{Inference Router}*
llm_pool ->|Cheap / Fast| groq[Groq Llama 3 // 300 tps] ~teal
llm_pool ->|Reasoning| deepseek[DeepSeek-R1 / Claude 3.5 Sonnet] ~purple
gateway -> mon[Telemetry & Billing // OpenTelemetry + Stripe] $chart ~ok
mon -> profit((High-Margin $3k-10k/mo AI SaaS Service)) ~ok"#,
            "midnight",
            "flow",
        ),
    ];

    raw_blogs
        .into_iter()
        .map(|(id, slug, title, category, reading_time, summary, content, code, recipe, script, preset, anim)| {
            let svg = DiagramService::render_script_to_svg(script, Some(preset), Some(anim)).ok();
            EngineeringBlog {
                id,
                slug: slug.to_string(),
                title: title.to_string(),
                category: category.to_string(),
                reading_time_minutes: reading_time,
                summary_roman_urdu: summary.to_string(),
                content_roman_urdu: content.to_string(),
                code_snippet: code.map(|s| s.to_string()),
                compute_recipe: recipe.map(|s| s.to_string()),
                diagram_script: script.to_string(),
                diagram_preset: preset.to_string(),
                diagram_animation: anim.to_string(),
                diagram_svg: svg,
                order_index: id,
            }
        })
        .collect()
}
