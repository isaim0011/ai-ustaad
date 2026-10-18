import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';

interface MentorResponse {
	reply_urdu: string;
	code_snippet?: {
		language: string;
		title: string;
		code: string;
	} | null;
	diagram_script?: string | null;
	suggested_followups: string[];
}

// Built-in Roman Urdu AI Ustaad Knowledge Engine covering all 14 curriculum modules
const KNOWLEDGE_BASE: Array<{
	keywords: string[];
	match: (text: string) => boolean;
	generate: () => MentorResponse;
}> = [
	// 1. Transformers & Self-Attention
	{
		keywords: ['attention', 'transformer', 'multi-head', 'scaled dot', 'qkv', 'query', 'key', 'value', 'kv cache'],
		match: (t) => t.includes('attention') || t.includes('transformer') || t.includes('qkv') || t.includes('kv cache'),
		generate: () => ({
			reply_urdu: `Transformer ka sab se bunyadi aur inqilabi building block **Scaled Dot-Product Attention** hai! 

Iska formula hai:
$$\\text{Attention}(Q, K, V) = \\text{softmax}\\left(\\frac{Q K^T}{\\sqrt{d_k}}\\right) V$$

### Roman Urdu Intuition:
1. **Query ($Q$)**: Har token doosray tokens se poochta hai: *"Mere context ke liye tumhare paas kya information hai?"*
2. **Key ($K$)**: Har token apni identity broadcast karta hai: *"Mere paas ye topics aur syntactic features hain."*
3. **Dot-Product ($Q K^T$)**: Dono vectors ka dot product nikal kar correlation score banaya jata hai.
4. **Scale by $\\sqrt{d_k}$**: Agar dimension barh jaye to dot product bohot bada ho jata hai aur softmax gradients saturate ho kar zero ho jate hain (vanishing gradient). Is liye $\\sqrt{d_k}$ se divide karna lazmi hai!
5. **Softmax**: Scores ko 0 se 1 ki probability distribution mein convert karta hai.
6. **Value ($V$)**: Probability weights ke mutabiq actual feature vectors aggregate ho kar agle layer ko milte hain.`,
			code_snippet: {
				language: 'python',
				title: 'PyTorch Scaled Dot-Product Attention Implementation',
				code: `import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor, mask: torch.Tensor = None):
    """
    Q, K, V shape: [batch_size, num_heads, seq_len, d_k]
    """
    d_k = Q.size(-1)
    
    # 1. Compute raw affinity scores: (Q @ K^T) / sqrt(d_k)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    
    # 2. Apply causal mask if autoregressive (decoder)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))
        
    # 3. Softmax over last dimension to get attention probabilities
    attn_weights = F.softmax(scores, dim=-1)
    
    # 4. Context vectors by weighted sum of values: attn @ V
    output = torch.matmul(attn_weights, V)
    return output, attn_weights

# Quick Zero-GPU Test:
B, H, S, D = 2, 8, 16, 64
q = torch.randn(B, H, S, D)
k = torch.randn(B, H, S, D)
v = torch.randn(B, H, S, D)
out, weights = scaled_dot_product_attention(q, k, v)
print(f"Output shape: {out.shape}")  # [2, 8, 16, 64]`
			},
			diagram_script: `@preset midnight
@animate flow
arch LR: Scaled Dot-Product Attention Architecture
  q[Query Matrix Q] ~info -> dot((MatMul Q.K^T))
  k[Key Matrix K] ~teal -> dot
  dot -> scale[Scale 1/sqrt(d_k)] -> mask[Causal Mask] -> soft[Softmax Layer] ~purple*
  v[Value Matrix V] ~ok -> out_mult((MatMul Weights.V))
  soft -> out_mult -> out[Attended Context Output]* $brain`,
			suggested_followups: [
				'Multi-Head Attention mein heads split karne ka kya mathematical faida hai?',
				'KV Cache inference ke waqt memory aur speed ko kaise 10x improve karta hai?',
				'RoPE (Rotary Position Embedding) Transformer mein kaise kaam karta hai?'
			]
		})
	},

	// 2. Modern RAG & ColPali & pgvector
	{
		keywords: ['rag', 'vector', 'retrieval', 'colpali', 'bm25', 'rerank', 'hybrid', 'embedding', 'chunking'],
		match: (t) => t.includes('rag') || t.includes('retrieval') || t.includes('colpali') || t.includes('bm25') || t.includes('rerank') || t.includes('vector'),
		generate: () => ({
			reply_urdu: `Modern 2026 RAG architecture mein purana "naive chunking + cosine similarity" system reject ho chuka hai! 

### Production RAG ke 4 Pillars:
1. **Hybrid Retrieval (Dense + Sparse)**:
   - **Dense (pgvector / Qdrant)**: High-dimensional embeddings (e.g. BGE-M3 / OpenAI text-3) semantic concept samajhte hain.
   - **Sparse (BM25 / SPLADE)**: Exact keyword matching karta hai (part numbers, technical terms, error codes).
2. **Reciprocal Rank Fusion (RRF)**:
   - Dono search engines ke ranks ko combine karta hai: $RRF(d) = \\sum \\frac{1}{60 + r(d)}$.
3. **Cross-Encoder Re-Ranking**:
   - Bi-encoders sirf independently match karte hain. Re-ranker (Cohere ya BGE-Reranker-Large) pure question aur chunk ko aik saath dekh kar top-5 final context select karta hai.
4. **ColPali (Vision-Language Retrieval)**:
   - PDFs ko extract karne ki bajaye page images ko seedha Multi-Vector ColBERT style mein index karta hai! Tables aur charts 100% preserve rehte hain.`,
			code_snippet: {
				language: 'python',
				title: 'Production Hybrid Search + Reciprocal Rank Fusion (RRF)',
				code: `def reciprocal_rank_fusion(dense_results, sparse_results, k=60):
    """
    Combines dense semantic and BM25 sparse results using RRF.
    """
    rrf_scores = {}
    
    # Process Dense Search ranks
    for rank, doc_id in enumerate(dense_results):
        if doc_id not in rrf_scores:
            rrf_scores[doc_id] = 0.0
        rrf_scores[doc_id] += 1.0 / (k + rank + 1)
        
    # Process BM25 Sparse ranks
    for rank, doc_id in enumerate(sparse_results):
        if doc_id not in rrf_scores:
            rrf_scores[doc_id] = 0.0
        rrf_scores[doc_id] += 1.0 / (k + rank + 1)
        
    # Sort documents by descending RRF score
    sorted_docs = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_docs

# Example usage
dense_top = ["doc_A", "doc_B", "doc_C"]
sparse_top = ["doc_B", "doc_D", "doc_A"]
blended = reciprocal_rank_fusion(dense_top, sparse_top)
print("Hybrid Reranked order:", blended)`
			},
			diagram_script: `@preset midnight
@animate pulse
arch LR: 2026 Hybrid RAG Pipeline
  query[User Query] $terminal -> dense[pgvector Dense Search] $database
  query -> sparse[BM25 Keyword Search] $filter
  dense -> rrf[Reciprocal Rank Fusion RRF] ~purple
  sparse -> rrf
  rrf -> rerank[BGE Cross-Encoder Reranker] ~teal
  rerank -> llm[LLM Context Generation]* ~ok $brain`,
			suggested_followups: [
				'ColPali vision-based retrieval naive OCR se behtar kyun hai?',
				'Supabase PostgreSQL mein HNSW index kaise banate hain?',
				'Context window stuffing ke bajaye Re-ranking se latency kaise ghati hai?'
			]
		})
	},

	// 3. LoRA, QLoRA, Fine-Tuning & Unsloth
	{
		keywords: ['lora', 'qlora', 'fine-tuning', 'finetuning', 'unsloth', 'peft', 'rank', 'sft'],
		match: (t) => t.includes('lora') || t.includes('qlora') || t.includes('tuning') || t.includes('unsloth') || t.includes('peft'),
		generate: () => ({
			reply_urdu: `**LoRA (Low-Rank Adaptation)** aur **QLoRA** ne model fine-tuning ki dunya badal di hai! 

### Asal Magic Kya Hai?
Aik 8-Billion parameter model ka weight matrix $W_0 \\in \\mathbb{R}^{d \\times k}$ hota hai.
Puri model ko train karne ke bajaye, hum $W_0$ ko **freeze** kar dete hain aur do bohot chote low-rank matrices add karte hain:
$$\\Delta W = B \\times A$$
Jahan $A \\in \\mathbb{R}^{r \\times k}$ aur $B \\in \\mathbb{R}^{d \\times r}$ (jahan $r \\ll d$, aam tor par $r = 16$ ya $32$).

### QLoRA (Dettmers et al.):
1. Base model ko **NF4 (4-bit NormalFloat)** precision mein quantize kiya jata hai.
2. Gradients sirf 16-bit LoRA adapters ($A$ aur $B$) ke through pass hote hain.
3. Google Colab ke free **15GB T4 GPU** par 8B Llama-3 ya Mistral araam se train ho jati hai!
4. **Unsloth**: Custom OpenAI Triton kernels use karke training ko 2x tez aur 70% kam VRAM mein chala deta hai.`,
			code_snippet: {
				language: 'python',
				title: 'Unsloth Fast QLoRA Setup on Free Google Colab',
				code: `from unsloth import FastLanguageModel
import torch

max_seq_length = 2048
dtype = None # Auto detects Float16 or Bfloat16
load_in_4bit = True # 4bit QLoRA quantisation

# 1. Load Pretrained SOTA 4-bit model
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Llama-3.2-3B-Instruct",
    max_seq_length = max_seq_length,
    load_in_4bit = load_in_4bit,
)

# 2. Add LoRA Adapters (only trains 0.1% parameters!)
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Rank
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
)

print("LoRA Model configured successfully on Free T4 GPU!")`
			},
			diagram_script: `@preset midnight
@animate wave
arch LR: LoRA Rank Decomposition Workflow
  x[Input Hidden States x] -> w0[Frozen Base Weights W0 // 4-bit NF4] ~default
  x -> lora_a[LoRA Matrix A // d x r] ~purple
  lora_a -> lora_b[LoRA Matrix B // r x k] ~teal
  w0 -> sum((Add Residual))
  lora_b -> sum
  sum -> out[Adapted Output y = W0*x + B*A*x]* ~ok $cpu`,
			suggested_followups: [
				'LoRA Rank r=16 aur r=64 mein kya farq hai aur kab barhana chahiye?',
				'Unsloth Triton kernels PyTorch ke standard autograd se 2x tez kyun hain?',
				'Trained LoRA adapters ko base model ke sath merge kaise karte hain?'
			]
		})
	},

	// 4. DeepSeek-R1, Reasoning & GRPO
	{
		keywords: ['deepseek', 'grpo', 'reasoning', 'rl', 'reinforcement', 'ppo', 'reward', 'r1'],
		match: (t) => t.includes('deepseek') || t.includes('grpo') || t.includes('reasoning') || t.includes('ppo') || t.includes('r1'),
		generate: () => ({
			reply_urdu: `**DeepSeek-R1** aur **GRPO (Group Relative Policy Optimization)** ne 2026 mein reasoning models ka naya inqilab paida kar diya hai! 

### Purana PPO vs DeepSeek GRPO:
- **PPO (Proximal Policy Optimization)** mein aik bara **Critic Model (Value Model)** train karna parta tha jo memory aur compute ka bohot bara hissa kha jata tha.
- **GRPO ka Kamaal**: DeepSeek ne Critic Model ko bilkul khatam kar diya!
- Model har question ke liye multiple candidate outputs ($G$ outputs) ka group generate karti hai.
- Group ke andar har sample ka reward calculate kiya jata hai, aur baseline group ka **mean aur standard deviation** ban jata hai:
$$A_i = \\frac{R_i - \\text{mean}(\\{R\\})}{\\text{std}(\\{R\\})}$$
- Is tarah model ko pata chalta hai group mein konsa reasoning step sab se behtar tha! Zero extra critic network!`,
			code_snippet: {
				language: 'python',
				title: 'GRPO Group Advantage Computation in PyTorch',
				code: `import torch

def compute_grpo_advantage(rewards: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    """
    rewards shape: [batch_size, group_size]
    Each prompt has a group of generated responses with raw reward scores.
    """
    # 1. Compute mean across the group
    mean_reward = rewards.mean(dim=-1, keepdim=True)
    
    # 2. Compute std across the group
    std_reward = rewards.std(dim=-1, keepdim=True)
    
    # 3. Normalized Group Advantage without any Critic model!
    advantages = (rewards - mean_reward) / (std_reward + eps)
    return advantages

# Example: 1 prompt with group of 4 candidate outputs
sample_rewards = torch.tensor([[0.2, 0.8, 0.9, 0.1]])
adv = compute_grpo_advantage(sample_rewards)
print("Normalized Group Advantages:", adv)`
			},
			diagram_script: `@preset midnight
@animate flow
arch LR: DeepSeek-R1 GRPO Optimization
  prompt[User Prompt] -> llm[Policy LLM] $brain
  llm -> g1[Candidate 1: Think -> Ans] ~info
  llm -> g2[Candidate 2: Think -> Ans] ~teal
  llm -> g3[Candidate 3: Think -> Ans] ~warn
  g1 -> rew[Reward Scoring Function]
  g2 -> rew
  g3 -> rew
  rew -> norm[Group Normalization: (R - mean)/std] ~purple
  norm -> grad[Policy Gradient Update (No Critic!)]* ~ok $cpu`,
			suggested_followups: [
				'DeepSeek-R1 mein <think> token aur chain-of-thought self-verification kaise emerge hoti hai?',
				'Rule-based verification (Math & Code) reward models se ziyada reliable kyun hai?',
				'Google Colab par GRPO fine-tuning kaise run ki ja sakti hai?'
			]
		})
	},

	// 5. Autonomous Agents, Anthropic MCP & smolagents
	{
		keywords: ['agent', 'mcp', 'smolagent', 'tool', 'function calling', 'swarm', 'protocol'],
		match: (t) => t.includes('agent') || t.includes('mcp') || t.includes('smolagent') || t.includes('tool'),
		generate: () => ({
			reply_urdu: `**Autonomous Agents** aur **Model Context Protocol (MCP)** 2026 ke enterprise application development ki reedh ki haddi hain! 

### 1. Model Context Protocol (MCP):
- Anthropic ka open standard jo LLMs ko databases, local tools, files, aur APIs se connect karta hai.
- Client-Server architecture: Agent aik MCP Client hota hai, jabke database ya web search tool MCP Server hota hai jo JSON-RPC over stdin/SSE par chalta hai.

### 2. CodeAgents (smolagents by HuggingFace):
- Purane ReAct agents JSON string format mein tool calls bhejte the jo slow aur parsing errors ka shikar the.
- 2026 SOTA trend **CodeAgent** hai: LLM seedha executable Python code likhta hai jo tools ko functions ki tarah call karta hai! Is se multi-step logic 10x tezi se chalta hai.`,
			code_snippet: {
				language: 'python',
				title: 'HuggingFace smolagents CodeAgent with Custom Tools',
				code: `from smolagents import CodeAgent, HfApiModel, tool

@tool
def calculate_system_latency(num_tokens: int, tps: float) -> str:
    """Calculates total streaming latency given tokens and tokens per second.
    Args:
        num_tokens: Total tokens generated.
        tps: Generation speed in tokens per second.
    """
    seconds = num_tokens / tps
    return f"Total latency: {seconds:.2f}s"

# Initialize CodeAgent
agent = CodeAgent(
    tools=[calculate_system_latency],
    model=HfApiModel()
)

# The agent writes real python code to solve the objective!
# response = agent.run("Calculate latency for 500 tokens at 45 tokens per second")`
			},
			diagram_script: `@preset midnight
@animate flow
arch LR: MCP Autonomous Multi-Agent Swarm
  user[User Instruction] $terminal -> orchestrator[Orchestrator Agent] $brain
  orchestrator -> client[MCP Client Host] ~purple
  client -> s1[MCP Server: PostgreSQL pgvector] $database
  client -> s2[MCP Server: GitHub CI/CD] $layers
  client -> s3[MCP Server: Python Code Sandbox] $terminal
  s1 -> synth[Agent State Synthesizer] ~teal
  s2 -> synth
  s3 -> synth
  synth -> orchestrator -> response[Verified Solution Delivery]* ~ok`,
			suggested_followups: [
				'MCP JSON-RPC standard aur classic OpenAI Function Calling mein kya farq hai?',
				'Multi-agent debate swarms hallucination rate ko kaise kam karte hain?',
				'CodeAgent sandbox execution mein security guardrails kaise lagate hain?'
			]
		})
	},

	// 6. Rust Axum & High-Performance Gateways
	{
		keywords: ['rust', 'axum', 'backend', 'gateway', 'vllm', 'performance', 'actix'],
		match: (t) => t.includes('rust') || t.includes('axum') || t.includes('gateway') || t.includes('vllm'),
		generate: () => ({
			reply_urdu: `AI Systems mein Python training ke liye behtareen hai, lekin **Production Gateways aur High-Throughput Serving** ke liye **Rust (Axum)** industry ka gold standard hai! 

### Rust Axum Kyun Chunte Hain?
1. **Zero Garbage Collection Pauses**: Python FastAPI mein heavy concurrency par GC latency spikes aate hain. Rust mein deterministic sub-millisecond latency milti hai.
2. **Memory Safety without Cost**: Compile-time ownership model ensure karta hai ke zero data races hon.
3. **vLLM / Triton Streaming Gateway**: SSE (Server-Sent Events) aur WebSocket streaming ko thousands of concurrent users par bina memory bloat ke serve karta hai.`,
			code_snippet: {
				language: 'rust',
				title: 'Rust Axum 0.8 Production High-Performance Gateway',
				code: `use axum::{routing::post, Json, Router};
use serde::{Deserialize, Serialize};
use std::net::SocketAddr;

#[derive(Deserialize)]
struct InferenceRequest {
    prompt: String,
    temperature: Option<f32>,
}

#[derive(Serialize)]
struct InferenceResponse {
    status: &'static str,
    latency_ms: f64,
}

async fn handle_inference(Json(payload): Json<InferenceRequest>) -> Json<InferenceResponse> {
    // Ultra-low latency routing to vLLM engine
    Json(InferenceResponse {
        status: "routed_to_engine",
        latency_ms: 0.42,
    })
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/api/inference", post(handle_inference));
    let addr = SocketAddr::from(([0, 0, 0, 0], 8080));
    println!("AI Gateway listening on http://{}", addr);
    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}`
			},
			diagram_script: `@preset midnight
@animate flow
arch LR: Rust Axum AI Gateway Architecture
  client[Client Web / Mobile] -> axum[Rust Axum 0.8 Gateway] ~purple $server
  axum -> rate[Token Bucket Rate Limiter] $filter
  rate -> pool[Async Worker Pool Tokio] ~teal
  pool -> vllm[vLLM Inference Engine] $cpu
  vllm -> axum -> stream[SSE Streaming Response]* ~ok $terminal`,
			suggested_followups: [
				'Axum 0.8 mein Tower middleware se rate-limiting kaise karte hain?',
				'Python FastAPI aur Rust Axum mein p99 latency ka kya farq hota hai?',
				'vLLM ke Continuous Batching algorithm ko Rust gateway ke sath kaise integrate karein?'
			]
		})
	},

	// 7. Free Zero-GPU Compute Recipes (Colab, Kaggle)
	{
		keywords: ['colab', 'free', 'gpu', 'kaggle', 'zero-gpu', 'compute', 't4'],
		match: (t) => t.includes('colab') || t.includes('free') || t.includes('kaggle') || t.includes('zero-gpu') || t.includes('compute'),
		generate: () => ({
			reply_urdu: `AI Engineering seekhne ke liye \$3000 ka gaming laptop ya RTX 4090 GPU khareedne ki **bilkul zaroorat nahi hai**! 

### AI Mastery Zero-GPU Cloud Strategy:
1. **Google Colab Free Tier**:
   - Free 15GB VRAM Nvidia T4 GPU rozana milta hai.
   - Unsloth QLoRA aur 4-bit quantization ke sath Llama-3-8B 100% free train ho sakti hai.
2. **Kaggle Notebooks**:
   - Har hafte **30 hours** ka free **Dual Nvidia T4 GPU (30GB total VRAM)** milta hai!
   - Batch size 4x barha kar distributed data parallel (DDP) test kiya ja sakta hai.
3. **HuggingFace Inference API & Groq**:
   - Groq par Llama-3.3-70B 300+ tokens/sec ki speed se free API tier par milti hai.
   - Local CPU par sirf code logic likhein, compute cloud se free uthayein!`,
			code_snippet: {
				language: 'python',
				title: 'Google Colab Hardware Accelerator Verification Script',
				code: `import torch

def verify_zero_gpu_cloud():
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)
        print(f" Free Cloud GPU Active: {gpu_name}")
        print(f" Available VRAM: {vram_gb:.2f} GB")
        print(" Zero-GPU AI Engineering Ready!")
    else:
        print("Running in CPU mode. Enable GPU via: Runtime > Change runtime type > T4 GPU")

verify_zero_gpu_cloud()`
			},
			diagram_script: `@preset midnight
@animate flow
arch LR: Zero-GPU Cloud Pipeline
  local[Local Laptop: Thin Client] $terminal -> colab[Google Colab: Free 15GB T4 GPU] ~teal $cpu
  local -> kaggle[Kaggle: 30h/week Dual-T4 30GB VRAM] ~purple $server
  local -> groq[Groq LPU: 300 tps Free API] ~ok $brain
  colab -> weights[Save LoRA Weights to HuggingFace Hub]* $database`,
			suggested_followups: [
				'Google Colab session disconnect hone se bachane ka reliable tareeqa kya hai?',
				'Kaggle par Dual-T4 par Distributed Training kaise chalate hain?',
				'Google One Pro cloud compute credits ko AI experimentation mein kaise utilize karein?'
			]
		})
	}
];

// Fallback generator for general Roman Urdu AI questions
function generateGeneralReply(query: string): MentorResponse {
	return {
		reply_urdu: `Bohot behtareen sawal hai: **"${query}"**! 

AI Mastery curriculum ke mutabiq har concept ko first-principles math aur production-grade implementation se samjhna zaroori hai.

### Key Conceptual Takeaways:
1. **Mathematical Underpinnings**: Har deep learning model tensors, loss functions, aur gradient updates par mushtamil hota hai.
2. **Production Scalability**: Sirf local prototype banana kafi nahi — streaming latency, GPU memory footprint, aur continuous evaluation dekhna lazmi hai.
3. **Zero-GPU Efficiency**: Modern optimization tools (Unsloth, 4-bit NF4 quantization, vLLM continuous batching) expensive hardware dependency khatam kar dete hain.

Aap mazeed specific details ke liye neechay diye gaye follow-up options par click kar sakte hain!`,
		code_snippet: {
			language: 'python',
			title: 'AI Engineering First-Principles Tensor Pipeline',
			code: `import torch

# Verifying tensor compute gradient propagation
x = torch.tensor([2.0, 3.0], requires_grad=True)
y = (x ** 2).sum()
y.backward()

print("Computed Gradients d(y)/d(x):", x.grad)
# Expected: [4.0, 6.0]`
		},
		diagram_script: `@preset midnight
@animate flow
arch LR: First-Principles AI Architecture
  concept[Mathematical Intuition] -> code[Production Code] ~teal $terminal
  code -> eval[Evaluation & Tracing] ~purple $filter
  eval -> deploy[Edge & Cloud Deployment]* ~ok $server`,
		suggested_followups: [
			'Transformer ka Self-Attention formula aur intuition samjhao',
			'Modern RAG mein ColPali aur BM25 re-ranking ka kya role hai?',
			'Google Colab Free GPU par bina paise diye LoRA fine-tuning kaise karein?'
		]
	};
}

const SYSTEM_PROMPT = `You are "AI Ustaad", the premier Roman Urdu AI Engineering Mentor for the AI Mastery platform (ai-ustaad.pages.dev).

ROLE AND SCOPE:
You answer ONLY questions strictly related to the 15 curriculum modules of AI Mastery:
1. Module 00: Python Foundations (variables, control flow, functions, OOP, data structures, file handling)
2. Module 01: Python for AI & Fast Math (NumPy, vectorization, matrix algebra, broadcasting)
3. Module 02: PyTorch from Scratch (tensors, autograd, computational graphs, Dataset & DataLoader)
4. Module 03: Neural Networks & Backprop (MLPs, loss functions, optimizers, backpropagation)
5. Module 04: Transformers & Attention Deep Dive (Scaled Dot-Product Attention, QKV, Multi-Head Attention, RoPE, KV cache)
6. Module 05: Modern RAG & Retrieval (Hybrid search, pgvector, BM25, Reciprocal Rank Fusion, Cross-Encoder rerankers, ColPali)
7. Module 06: Autonomous Agents & MCP (Anthropic Model Context Protocol, CodeAgents, tool calling, smolagents)
8. Module 07: Fine-Tuning & Quantization (LoRA, QLoRA, 4-bit NF4, Unsloth, PEFT, Colab Zero-GPU)
9. Module 08: Reasoning Models & GRPO (DeepSeek-R1, Group Relative Policy Optimization, chain-of-thought, reward functions)
10. Module 09: Rust Axum AI Gateway (High-performance serving, streaming SSE, Axum 0.8, Tokio concurrency)
11. Module 10: Production MLOps Capstone (CI/CD, evaluation, observability, model monitoring, deployment)
And all related Machine Learning, Deep Learning, and AI Systems Engineering topics in the curriculum.

OFF-TOPIC REFUSAL POLICY:
If the user's question is NOT about AI engineering, machine learning, Python/Rust for AI, or the course modules (e.g. general chit-chat, cooking, politics, sports, entertainment, or programming unrelated to AI):
You MUST politely refuse in Roman Urdu:
"Main AI Ustaad hoon aur sirf AI Mastery curriculum ke 15 modules (Python, ML, DL, Transformers, RAG, Agents/MCP, Fine-Tuning, MLOps, Rust AI) ke sawalaat ka jawab deta hoon. Baraye meherbani AI curriculum se mutaliq sawal poochein."
Provide 2-3 relevant course questions in suggested_followups.

LANGUAGE AND STYLE:
- Respond in Roman Urdu mixed naturally with English technical terms (e.g., "Scaled Dot-Product Attention", "Tensors", "Loss function", "Gradients", "Backpropagation").
- First-principles conceptual clarity and practical engineering intuition.
- ABSOLUTELY NO EMOJIS anywhere in your response under any circumstances.

OUTPUT SCHEMA:
You MUST respond with valid raw JSON only. Do not wrap in markdown or backticks.
The JSON must follow this exact schema:
{
  "reply_urdu": "Markdown formatted Roman Urdu explanation with English technical terms. No emojis.",
  "code_snippet": {
    "language": "python",
    "title": "Title of snippet",
    "code": "# Runnable code without emojis"
  },
  "diagram_script": "@preset midnight\\n@animate flow\\narch LR: Title\\n  a[Input] -> b[Output]*",
  "suggested_followups": [
    "Relevant followup question 1 in Roman Urdu / English",
    "Relevant followup question 2 in Roman Urdu / English",
    "Relevant followup question 3 in Roman Urdu / English"
  ]
}
If code_snippet is not needed, set it to null.
If diagram_script is not needed, set it to null.
suggested_followups must contain 2-3 relevant questions.`;

function stripEmojis(text: string): string {
	return text.replace(
		/[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{1F000}-\u{1F02F}\u{1F0A0}-\u{1F0FF}\u{1F100}-\u{1F64F}\u{1F680}-\u{1F6FF}\u{1F900}-\u{1F9FF}\u{1FA00}-\u{1FA6F}\u{1FA70}-\u{1FAFF}]/gu,
		''
	);
}

function normalizeMentorObject(
	parsed: Record<string, unknown>,
	fallbackText: string
): MentorResponse {
	let replyUrdu = '';
	if (typeof parsed.reply_urdu === 'string' && parsed.reply_urdu.trim()) {
		replyUrdu = parsed.reply_urdu.trim();
	} else if (typeof parsed.content === 'string' && parsed.content.trim()) {
		replyUrdu = parsed.content.trim();
	} else {
		replyUrdu = fallbackText;
	}

	let codeSnippet: MentorResponse['code_snippet'] = null;
	if (
		parsed.code_snippet &&
		typeof parsed.code_snippet === 'object' &&
		'code' in parsed.code_snippet &&
		typeof (parsed.code_snippet as { code: unknown }).code === 'string' &&
		(parsed.code_snippet as { code: string }).code.trim()
	) {
		const cs = parsed.code_snippet as { language?: unknown; title?: unknown; code: string };
		codeSnippet = {
			language: typeof cs.language === 'string' ? cs.language : 'python',
			title: typeof cs.title === 'string' ? cs.title : 'Code Implementation',
			code: stripEmojis(cs.code)
		};
	}

	let diagramScript: string | null = null;
	if (typeof parsed.diagram_script === 'string' && parsed.diagram_script.trim()) {
		diagramScript = stripEmojis(parsed.diagram_script.trim());
	}

	let followups: string[] = [];
	if (Array.isArray(parsed.suggested_followups)) {
		followups = parsed.suggested_followups
			.filter((f): f is string => typeof f === 'string' && f.trim().length > 0)
			.map((f) => stripEmojis(f.trim()))
			.slice(0, 4);
	}
	if (followups.length === 0) {
		followups = [
			'Transformer ka Self-Attention formula aur intuition samjhao',
			'Modern RAG mein ColPali aur BM25 re-ranking ka kya role hai?',
			'Google Colab Free GPU par bina paise diye LoRA fine-tuning kaise karein?'
		];
	}

	return {
		reply_urdu: stripEmojis(replyUrdu),
		code_snippet: codeSnippet,
		diagram_script: diagramScript,
		suggested_followups: followups
	};
}

function parseMentorResponse(raw: string): MentorResponse {
	const sanitized = stripEmojis(raw).trim();
	const textWithoutThink = sanitized.replace(/<think>[\s\S]*?<\/think>/gi, '').trim();

	// 1. Try direct JSON parse
	try {
		const parsed = JSON.parse(textWithoutThink);
		if (parsed && typeof parsed === 'object') {
			return normalizeMentorObject(parsed as Record<string, unknown>, textWithoutThink);
		}
	} catch {
		// Continue
	}

	// 2. Try markdown code block extraction
	const blockMatch = textWithoutThink.match(/```(?:json)?\s*([\s\S]*?)\s*```/i);
	if (blockMatch && blockMatch[1]) {
		try {
			const parsed = JSON.parse(blockMatch[1].trim());
			if (parsed && typeof parsed === 'object') {
				return normalizeMentorObject(parsed as Record<string, unknown>, textWithoutThink);
			}
		} catch {
			// Continue
		}
	}

	// 3. Try outermost JSON object brackets { ... }
	const startIdx = textWithoutThink.indexOf('{');
	const endIdx = textWithoutThink.lastIndexOf('}');
	if (startIdx !== -1 && endIdx > startIdx) {
		try {
			const jsonSub = textWithoutThink.substring(startIdx, endIdx + 1);
			const parsed = JSON.parse(jsonSub);
			if (parsed && typeof parsed === 'object') {
				return normalizeMentorObject(parsed as Record<string, unknown>, textWithoutThink);
			}
		} catch {
			// Continue
		}
	}

	// 4. Fallback: return entire text as reply_urdu
	return {
		reply_urdu: textWithoutThink || 'Jawab generate nahi ho saka. Baraye meherbani dobara koshish karein.',
		code_snippet: null,
		diagram_script: null,
		suggested_followups: [
			'Transformer ka Self-Attention formula aur intuition samjhao',
			'Modern RAG mein ColPali aur BM25 re-ranking ka kya role hai?',
			'Google Colab Free GPU par bina paise diye LoRA fine-tuning kaise karein?'
		]
	};
}

async function runWithTimeout<T>(promise: Promise<T>, ms: number, label: string): Promise<T> {
	let timer: ReturnType<typeof setTimeout> | undefined;
	const timeoutPromise = new Promise<never>((_, reject) => {
		timer = setTimeout(() => reject(new Error(`${label} timed out after ${ms}ms`)), ms);
	});
	try {
		return await Promise.race([promise, timeoutPromise]);
	} finally {
		if (timer) clearTimeout(timer);
	}
}

export const POST: RequestHandler = async ({ request, platform }) => {
	try {
		const body = await request.json();
		const message = (body.message || '').trim();
		const rawHistory = Array.isArray(body.history) ? body.history : [];

		if (!message) {
			return json({ error: 'Message cannot be empty' }, { status: 400 });
		}

		const formattedHistory = rawHistory.slice(-6).map((h: unknown) => {
			const item = h as { role?: unknown; content?: unknown };
			return {
				role: item?.role === 'assistant' ? 'assistant' : 'user',
				content: typeof item?.content === 'string' ? item.content : ''
			};
		});

		// (1) Cloudflare Workers AI with Meta Llama models
		if (platform?.env?.AI && typeof platform.env.AI.run === 'function') {
			const candidateModels = [
				'@cf/meta/llama-3.3-70b-instruct-fp8-fast',
				'@cf/meta/llama-3.1-8b-instruct'
			];

			for (const model of candidateModels) {
				try {
					const aiCall = platform.env.AI.run(model, {
						messages: [
							{ role: 'system', content: SYSTEM_PROMPT },
							...formattedHistory,
							{ role: 'user', content: message }
						],
						max_tokens: 1500,
						temperature: 0.3
					});

					const aiRes = (await runWithTimeout(aiCall, 9000, `Workers AI ${model}`)) as
						| { response?: unknown }
						| string
						| undefined;

					let rawText = '';
					if (aiRes && typeof aiRes === 'object') {
						if (typeof aiRes.response === 'string') {
							rawText = aiRes.response;
						} else if (typeof aiRes.response === 'object' && aiRes.response !== null) {
							return json(
								normalizeMentorObject(
									aiRes.response as Record<string, unknown>,
									JSON.stringify(aiRes.response)
								)
							);
						} else {
							rawText = JSON.stringify(aiRes);
						}
					} else if (typeof aiRes === 'string') {
						rawText = aiRes;
					}

					if (rawText && rawText.trim()) {
						const parsedResponse = parseMentorResponse(rawText);
						return json(parsedResponse);
					}
				} catch (cfErr) {
					console.warn(`Workers AI (${model}) attempt failed:`, cfErr);
					// Continue to fallback model or next tier
				}
			}
		}

		// (2) Groq llama-3.3-70b-versatile if GROQ_API_KEY is available
		const groqKey =
			(typeof platform?.env?.GROQ_API_KEY === 'string' ? platform.env.GROQ_API_KEY : undefined) ||
			(typeof process !== 'undefined' ? process.env?.GROQ_API_KEY : undefined);

		if (groqKey) {
			try {
				const controller = new AbortController();
				const timeoutId = setTimeout(() => controller.abort(), 7500);

				const groqRes = await fetch('https://api.groq.com/openai/v1/chat/completions', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${groqKey}`
					},
					body: JSON.stringify({
						model: 'llama-3.3-70b-versatile',
						messages: [
							{ role: 'system', content: SYSTEM_PROMPT },
							...formattedHistory,
							{ role: 'user', content: message }
						],
						response_format: { type: 'json_object' },
						temperature: 0.3,
						max_tokens: 1500
					}),
					signal: controller.signal
				});
				clearTimeout(timeoutId);

				if (groqRes.ok) {
					const groqData = (await groqRes.json()) as {
						choices?: Array<{ message?: { content?: string } }>;
					};
					const content = groqData.choices?.[0]?.message?.content;
					if (content && content.trim()) {
						const parsedResponse = parseMentorResponse(content);
						return json(parsedResponse);
					}
				} else {
					console.warn('Groq API error response status:', groqRes.status);
				}
			} catch (groqErr) {
				console.warn('Groq call failed, falling back to built-in knowledge engine:', groqErr);
			}
		}

		// (3) Existing built-in Roman Urdu AI Ustaad Knowledge Engine
		const lowerMsg = message.toLowerCase();
		for (const entry of KNOWLEDGE_BASE) {
			if (entry.match(lowerMsg)) {
				return json(entry.generate());
			}
		}

		return json(generateGeneralReply(message));
	} catch (err: unknown) {
		const msg = err instanceof Error ? err.message : 'Server error in mentor endpoint';
		return json({ error: msg }, { status: 500 });
	}
};

