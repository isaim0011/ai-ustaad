use serde::{Deserialize, Serialize};

use crate::{
    error::AppError,
    models::CodeSnippet,
    services::diagram_service::DiagramService,
};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ChatMessage {
    pub role: String, // "user" or "assistant"
    pub content: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MentorChatRequest {
    pub message: String,
    #[serde(default)]
    pub module_slug: Option<String>,
    #[serde(default)]
    pub lesson_slug: Option<String>,
    #[serde(default)]
    pub history: Option<Vec<ChatMessage>>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MentorChatResponse {
    pub reply_urdu: String,
    pub code_snippet: Option<CodeSnippet>,
    pub diagram_script: Option<String>,
    pub diagram_svg: Option<String>,
    pub suggested_followups: Vec<String>,
}

pub struct MentorService;

impl MentorService {
    pub fn answer(req: &MentorChatRequest) -> Result<MentorChatResponse, AppError> {
        let msg = req.message.to_lowercase();
        let module_slug = req.module_slug.as_deref().unwrap_or("");

        // Tailor the mentor response based on keywords & module context
        let (reply, code, script, followups) = if msg.contains("attention") || msg.contains("transformer") || module_slug.contains("transformer") {
            (
                "Salam! So guys, dekhein: Transformer ka sab se core concept hai **Self-Attention**! \
                Rote memory ya LSTM ki tarah sequetially nahi chalta, balke har token ek hi waqt mein baqi tamaam tokens ko dekhta hai. \
                Formula yaad rakhein: `Attention(Q, K, V) = softmax((Q . K^T) / sqrt(d_k)) . V`. \
                Yahan **Query** poochti hai 'mujhe kya chahiye?', **Key** batati hai 'mere paas kya context hai?', aur **Value** mein actual information store hoti hai. \
                Jab dot-product zyada hota hai to softmax us pair ko high weight deta hai!".to_string(),
                Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "PyTorch Scaled Dot-Product Attention".to_string(),
                    code: r#"import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q, K, V, mask=None):
    # Q, K, V dimensions: [batch_size, num_heads, seq_len, d_k]
    d_k = Q.size(-1)
    # Step 1: MatMul Q with K transpose
    scores = torch.matmul(Q, K.transpose(-2, -1)) / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
        
    # Step 2: Softmax along last dimension
    attention_weights = F.softmax(scores, dim=-1)
    
    # Step 3: Multiply weights with Value matrix
    output = torch.matmul(attention_weights, V)
    return output, attention_weights"#.to_string(),
                    explanation: "Yeh standard PyTorch attention block hai jo multi-head attention ke andar har head execute karta hai.".to_string(),
                }),
                Some(r#"@preset midnight
@animate wave
arch LR: Attention Mechanism | Query-Key-Value Interaction
q[Query Q] ~info -> dot((Dot Product))
k[Key K] ~teal -> dot
dot -> scale[Scale 1/sqrt(d_k)] -> mask{Causal Mask?}*
mask ->|Yes| sm[Softmax Attention Map] ~purple
v[Value V] ~teal -> out_mult((Matrix Multiply))
sm -> out_mult
out_mult -> out[Attended Context Vector]* ~ok"#.to_string()),
                vec![
                    "Multi-Head Attention mein heads split karne ka kya faida hota hai?".to_string(),
                    "Causal masking decoder-only models (jaise GPT) mein kyun zaroori hai?".to_string(),
                    "FlashAttention GPU memory ko kaise optimize karta hai?".to_string(),
                ]
            )
        } else if msg.contains("rag") || msg.contains("retrieval") || msg.contains("vector") || module_slug.contains("rag") {
            (
                "So guys, dekhein: RAG (Retrieval-Augmented Generation) ka asal maqsad LLM ki **hallucination** ko khatam karna hai! \
                Jab user sawal poochta hai, hum direct LLM ko prompt nahi bhejte. Pehle sawal ki embedding banti hai, phir Vector DB (pgvector ya Qdrant) \
                se top-k relevant chunks uthate hain. Phir BM25 sparse keyword search ke sath **Reciprocal Rank Fusion (RRF)** lagate hain, \
                aur Cohere Rerank se filter karke LLM ke system prompt mein inject karte hain. Zero hallucination, 100% verified citations!".to_string(),
                Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "Production Hybrid RAG with Re-ranking".to_string(),
                    code: r#"from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi

# 1. Dense Embeddings
encoder = SentenceTransformer("BAAI/bge-m3")
query_vector = encoder.encode("What is LoRA?")

# 2. Hybrid Fusion (Dense + BM25)
# In production, query pgvector with Cosine Similarity & BM25 with textsearch
# Combined using Reciprocal Rank Fusion (RRF):
def rrf(dense_ranks, sparse_ranks, k=60):
    rrf_scores = {}
    for doc_id, rank in dense_ranks.items():
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + (1.0 / (k + rank))
    for doc_id, rank in sparse_ranks.items():
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + (1.0 / (k + rank))
    return sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)"#.to_string(),
                    explanation: "Hybrid RAG dense semantic search aur sparse exact keyword search ko combine karke unmatched accuracy deta hai.".to_string(),
                }),
                Some(r#"@preset midnight
@animate flow
arch LR: Production Hybrid RAG Pipeline
user[Query] $user ~purple -> embed[bge-m3 Embedding] $ai
user -> bm25[BM25 Index] ~teal
embed -> vec[(pgvector DB)] $db ~info
vec -> fusion[Reciprocal Rank Fusion (RRF)]* $bolt
bm25 -> fusion
fusion -> rerank[Cross-Encoder Re-ranker] ~purple
rerank -> top3[Top-3 Clean Chunks] ~ok
top3 -> llm[[LLM Prompt Injection]] $ai
llm -> ans((Grounded Answer)) ~ok
group Retrieval: vec bm25 fusion rerank"#.to_string()),
                vec![
                    "Chunking strategy (Fixed vs Semantic chunking) mein kya farq hai?".to_string(),
                    "pgvector ko HNSW index ke sath index kaise karte hain?".to_string(),
                    "Self-RAG aur Corrective RAG (CRAG) kab use karna chahiye?".to_string(),
                ]
            )
        } else if msg.contains("lora") || msg.contains("fine-tuning") || msg.contains("peft") || msg.contains("qlora") {
            (
                "Arey wah! LoRA (Low-Rank Adaptation) AI engineering ka game changer hai. \
                Dekhein, poore 70B parameter model ko train karna lakhoon dollars ka kaam hai. \
                LoRA ka intuition yeh hai ke weight update matrix `Delta W` bohot low 'intrinsic dimension' rakhta hai. \
                Isliye hum original weight matrix `W0` ko freeze kar dete hain, aur do bohot choti matrices `A` aur `B` train karte hain \
                jahan `Delta W = B x A` (agar rank `r=8` ho to parameters 99.9% kam ho jate hain!). \
                Is se consumer GPU par bhi LLM fine-tune ho jata hai!".to_string(),
                Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "PEFT LoRA Config in Python".to_string(),
                    code: r#"from peft import LoraConfig, get_peft_model, TaskType
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3-8B-Instruct")

# Configure Low-Rank Adapter
lora_config = LoraConfig(
    r=16,                         # Rank dimension
    lora_alpha=32,                # Scaling factor
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)

peft_model = get_peft_model(model, lora_config)
peft_model.print_trainable_parameters()
# Output: trainable params: 6.8M || all params: 8.03B || trainable%: 0.084%"#.to_string(),
                    explanation: "Dekhein sirf 0.08% parameters train ho rahe hain, baqi 99.92% frozen hain!".to_string(),
                }),
                Some(r#"@preset midnight
@animate glow
arch LR: LoRA Low-Rank Adapter Flow
in[Input Vector x // d=4096] ~purple -> base[Frozen Base Weights W0 // 4096 x 4096]* ~muted
in -> mat_a[Matrix A // 4096 x 16 (Rank r)] ~info
mat_a -> mat_b[Matrix B // 16 x 4096 (Init Zero)]* ~teal
base -> add((+))
mat_b -> scale[Scale alpha/r] -> add
add -> out[Output Vector y // d=4096] ~ok"#.to_string()),
                vec![
                    "QLoRA mein 4-bit NormalFloat (NF4) quantization kaise kaam karti hai?".to_string(),
                    "Rank r ki optimal value (8, 16, 64) kaise choose karein?".to_string(),
                    "Fine-tuned LoRA weights ko base model mein merge kaise karte hain?".to_string(),
                ]
            )
        } else if msg.contains("agent") || msg.contains("react") || msg.contains("tool") || module_slug.contains("agent") {
            (
                "So guys, dekhein: LLM sirf text generate karta hai, lekin **AI Agent** faislay karta hai aur dunya mein actions leta hai! \
                Agent ka basic architecture ReAct (Reasoning + Acting) pattern par mabni hai: \
                1. **Thought**: Model sochta hai ke sawal ka jawab dene ke liye kya information chahiye. \
                2. **Action**: Ek tool select karta hai (e.g. `web_search(query='gold rate today')`). \
                3. **Observation**: Execution environment tool run karke raw output model ko wapis bhejti hai. \
                4. **Reflection**: Model check karta hai ke kya target achieve ho gaya? Agar haan to Final Answer, warna next tool call!".to_string(),
                Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "Minimal ReAct Agent Loop in Python".to_string(),
                    code: r#"import json

def agent_loop(goal: str, tools: dict, llm_client):
    messages = [{"role": "system", "content": "You are a ReAct agent. Think step by step and call tools."},
                {"role": "user", "content": goal}]
    
    for step in range(5):  # Max 5 reasoning turns
        response = llm_client.generate(messages)
        if response.has_tool_call():
            tool_name = response.tool_call.name
            args = response.tool_call.arguments
            print(f"[Thought & Action] Calling {tool_name} with {args}")
            # Execute tool
            observation = tools[tool_name](**args)
            messages.append({"role": "tool", "content": json.dumps(observation)})
        else:
            print("[Final Answer]:", response.content)
            return response.content
    return "Step limit exceeded""#.to_string(),
                    explanation: "Yeh deterministic ReAct loop hai jo LangGraph ya CrewAI ke background mein chalta hai.".to_string(),
                }),
                Some(r#"@preset midnight
@animate pulse
flow TB: Autonomous Agent ReAct State Machine
start((Goal / Prompt)) ~purple -> think[Reasoning Step // LLM Thought]* $ai
think -> decide{Need Tool Call?}
decide ->|Yes| call[Execute Tool // API/DB/Search] $gear ~teal
call -> obs[Capture Observation] ~info
obs -> think
decide ->|No| done((Deliver Final Output)) ~ok"#.to_string()),
                vec![
                    "LangGraph mein cyclic workflows aur state persistence kaise banate hain?".to_string(),
                    "Human-in-the-loop approval agent pipeline mein kahan integrate hoti hai?".to_string(),
                    "Multi-agent supervisor pattern kya hai?".to_string(),
                ]
            )
        } else {
            // General AI Mentor guidance
            (
                format!(
                    "Salam! Main aapka AI Mastery Roman Urdu Mentor hoon. \
                    So guys, dekhein: AI seekhne ka sab se behtareen tareeqa hai **70% Hands-on Building, 20% Peer Review, aur 10% Deep Theory**. \
                    Aap kisi bhi module (Python, Tensors, PyTorch, Transformers, RAG, LoRA, Agents, ya MLOps) ke mutalliq sawal poochein. \
                    Main aapko har step Roman Urdu mein step-by-step code aur live DiagramKit architecture diagram ke sath samjhaunga! \
                    Aapka agla challenge kya hai?"
                ),
                Some(CodeSnippet {
                    language: "python".to_string(),
                    title: "AI Engineer's Daily Verification Template".to_string(),
                    code: r#"import torch

def verify_ai_environment():
    print("PyTorch Version:", torch.__version__)
    print("CUDA Available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU Device:", torch.cuda.get_device_name(0))
        print("VRAM Allocated (MB):", torch.cuda.memory_allocated() / (1024**2))
    print("Status: 100% Ready to train modern models!")

if __name__ == "__main__":
    verify_ai_environment()"#.to_string(),
                    explanation: "Yeh environment health check script hai jo har AI project ke start par run karni chahiye.".to_string(),
                }),
                Some(r#"@preset midnight
@animate flow
flow LR: 20-Week AI Mastery Journey
p1[Phase 1: Foundations] ~info -> p2[Phase 2: ML & PyTorch] ~teal
p2 -> p3[Phase 3: Transformers & RAG]* ~purple
p3 -> p4[Phase 4: Agents & LoRA] ~teal
p4 -> p5[Phase 5: Production MLOps] ~ok"#.to_string()),
                vec![
                    "Transformer Attention mechanism kaise kaam karta hai?".to_string(),
                    "RAG pipeline mein hallucination kaise solve karein?".to_string(),
                    "LoRA fine-tuning 8GB GPU par kaise run hoti hai?".to_string(),
                    "Autonomous AI Agents ka ReAct loop kya hota hai?".to_string(),
                ]
            )
        };

        let diagram_svg = if let Some(ref s) = script {
            DiagramService::render_script_to_svg(s, Some("midnight"), Some("flow")).ok()
        } else {
            None
        };

        Ok(MentorChatResponse {
            reply_urdu: reply,
            code_snippet: code,
            diagram_script: script,
            diagram_svg,
            suggested_followups: followups,
        })
    }
}
