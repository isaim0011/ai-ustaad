# seed_modules_phase3.py
# Phase 3 Modules: 6, 7, 8 (18 comprehensive lessons)

def get_modules_phase3():
    return [
        # =========================================================================
        # MODULE 6: Building AI Applications & Modern APIs
        # =========================================================================
        {
            "phase_slug": "phase-3-modern-genai-stack",
            "module_number": 6,
            "slug": "building-ai-applications-and-apis",
            "real_world_deliverable": "WhatsApp/Web AI Customer Support Bot with SSE Streaming & Fallback",
            "zero_gpu_recipe": {
                'platform': 'Local CPU / Fly.io Free Tier / Render',
                'vram_required': '0 GB (CPU)',
                'estimated_cost': '$0.00 Free',
                'compute_units_tip': 'Host async FastAPI or Rust Axum server on free tier connected to Groq API.',
                'one_click_command': 'uvicorn main:app --workers 4'
            },
            "title": "Module 6: Building AI Applications & Modern APIs",
            "weeks_range": "Weeks 11-12",
            "estimated_hours": 14,
            "learning_outcomes": [
                "Real-time token streaming via Server-Sent Events (SSE) aur HTTP/2",
                "Full-stack AI architectures: Frontend state, Svelte 5 Runes aur abort controllers",
                "Asynchronous background worker queues with FastAPI and Redis",
                "Token cost optimization: Semantic Caching via Redis & vector cosine thresholds",
                "Real-time bidirectional AI streaming via WebSockets and connection pooling",
                "Resilient enterprise streaming gateway with circuit breakers and fallback providers"
            ],
            "practical_tasks": [
                "FastAPI SSE token streaming endpoint implement karein",
                "Svelte 5 client-side streaming reader with cancel button build karein",
                "Redis vector semantic cache wrapper design karein for 80% token savings",
                "Bidirectional WebSocket streaming server implement karein with ping/pong heartbeats",
                "Production multi-provider failover AI Gateway build karein"
            ],
            "resources": [
                {"title": "FastAPI Streaming Responses", "url": "https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse"},
                {"title": "Svelte 5 Runes Overview", "url": "https://svelte.dev/docs/svelte/overview"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 6 Modern Streaming AI Stack
  user[User Browser Svelte 5] $browser -> sse_req[HTTP/2 SSE Request] $terminal
  sse_req -> gateway[Axum / FastAPI Gateway] $server
  gateway -> cache[Redis Semantic Cache] $database
  gateway -> llm[LLM Async Streaming Engine] $cpu
  llm -> user: Chunked Token Stream *""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "app-builder",
            "order_index": 6,
            "lessons": [
                {
                    "lesson_code": "6.1",
                    "slug": "streaming-llm-apis",
                    "title": "Streaming LLM APIs: Server-Sent Events (SSE) & Async Iterators",
                    "duration_minutes": 30,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab user LLM se 500 words ka response mangta hai, to agar aap poora response complete hone tak intezar karein to user ko 5 se 10 seconds tak blank screen dekhni paregi! Yeh terrible User Experience (UX) hai.

Iska industry standard solution **Server-Sent Events (SSE)** hai (`Content-Type: text/event-stream`). Server HTTP connection open rakhta hai aur jaise hi LLM ek naya token generate karta hai, server use foran client ko push kar deta hai:
`data: {"token": "Pakistan"}\\n\\n`

Client-side par JavaScript ka `ReadableStream` aur `TextDecoder` har token ko instant UI mein append karte hain.""",
                    "english_summary": "Architect low-latency streaming endpoints utilizing HTTP/2 Server-Sent Events (SSE) and asynchronous token iterators.",
                    "code_example": """import asyncio
from typing import AsyncGenerator
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

async def mock_token_generator(prompt: str) -> AsyncGenerator[str, None]:
    words = f"Salam! Aapne poocha: '{prompt}'. Hum real-time token streaming seekh rahe hain!".split()
    for word in words:
        await asyncio.sleep(0.08)
        yield f"data: {word} \\n\\n"
    yield "data: [DONE]\\n\\n"

@app.get("/api/chat/stream")
async def chat_stream(prompt: str):
    return StreamingResponse(
        mock_token_generator(prompt),
        media_type="text/event-stream"
    )""",
                    "diagram_script": """@preset midnight
seq: Real-Time SSE Token Streaming
  client[Svelte 5 Client] -> server[FastAPI / Axum Gateway]: GET /api/chat/stream
  server -> llm[LLM Provider]: Stream Completion
  llm -> server: Token: 'Salam'
  server -> client: data: 'Salam'
  llm -> server: Token: 'Pakistan'
  server -> client: data: 'Pakistan' *
  server -> client: data: [DONE]""",
                    "diagram_type": "seq",
                    "resources": [{"title": "MDN Server-Sent Events", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events"}],
                    "xp_reward": 20,
                    "order_index": 1
                },
                {
                    "lesson_code": "6.2",
                    "slug": "fullstack-ai-architecture",
                    "title": "Full-Stack AI Architecture: State & Token Management",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, ek professional AI frontend mein teen cheezein lazmi honi chahiye:
1. **AbortController**: Agar user response ke beech mein 'Stop Generating' dabaye to foran HTTP stream abort ho jaye taake token waste na hon.
2. **Optimistic Updates**: User ka message foran screen par show ho bina network latency ka wait kiye.
3. **Token Accounting**: Har message ke input tokens aur output tokens count karke database mein log karna taake billing aur rate limits track ho sakein.""",
                    "english_summary": "Manage client-side chat state, optimistic UI rendering, AbortController request cancellation, and database token accounting.",
                    "code_example": """// Svelte 5 / TypeScript Stream Reader with AbortController
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
        if (err.name === 'AbortError') console.log('Generation aborted by user.');
    }
}""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Abortable Stream Lifecycle
  user[User Clicks Stop] $browser -> abort[AbortController.abort()] $terminal
  abort -> stream[ReadableStream Closed] $code
  stream -> server[Server Halts LLM Inference] $server *""",
                    "diagram_type": "flow",
                    "resources": [{"title": "Web Fetch API Streams", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Streams_API"}],
                    "xp_reward": 25,
                    "order_index": 2
                },
                {
                    "lesson_code": "6.3",
                    "slug": "fastapi-async-worker-queues",
                    "title": "Production Async AI Gateways with FastAPI & Redis Task Queues",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab aapke AI platform par 500 users aik sath heavy requests bhejte hain (jaise document extraction ya image embedding), to seedha FastAPI worker par run karne se poora server block ho jata hai!

Iska production pattern hai **Async Background Worker Queue (Celery / ARQ + Redis)**:
1. FastAPI request receive karta hai, ek unique `job_id` generate karta hai, aur foran `202 Accepted` return kar deta hai (sub-10ms response).
2. Background Redis Queue mein job enqueue hoti hai.
3. Dedicated GPU/CPU worker process job utha kar execute karta hai aur status database mein update karta hai.
4. Client polling ya WebSocket ke zariye progress bar update karta hai.""",
                    "english_summary": "Decouple synchronous HTTP request handlers from long-running AI compute tasks using FastAPI, Redis queues, and background worker pools.",
                    "code_example": """import asyncio
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
    return job_store.get(job_id, {"status": "not_found"})""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Async Worker Queue Architecture
  client[Client HTTP Ingest] $browser -> api[FastAPI Gateway] $server
  api -> queue[Redis Job Queue] $database
  api -> client: 202 Accepted {job_id} *
  queue -> worker[Background AI Worker Process] $cpu
  worker -> db[PostgreSQL Result Cache] $database""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "FastAPI Background Tasks", "url": "https://fastapi.tiangolo.com/tutorial/background-tasks/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "6.4",
                    "slug": "semantic-caching-redis-gptcache",
                    "title": "Semantic Caching with Redis & Vector Similarity for 80% Cost Reduction",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, agar ek user pooche *"Pakistan ka capital kya hai?"* aur 5 minute baad doosra user pooche *"What is the capital city of Pakistan?"*, to traditional exact-match caching (jaise standard Redis key-value) fail ho jayegi kyunke strings mukhtalif hain!

Dono dafa LLM API ko call karne se aapke paise aur latency waste honge.
Iska solution hai **Semantic Caching (GPTCache / Redis Vector Search)**:
1. Incoming prompt ka vector embedding banayein.
2. Redis vector index mein search karein: agar pichle kisi query se Cosine Similarity > 0.95 hai, to LLM ko call kiye baghair pichla answer return kar dein!
3. Is se enterprise AI bills **70% se 80% reduce** ho jate hain aur response time 1.5s se gir kar **15 milliseconds** par aa jata hai!""",
                    "english_summary": "Implement semantic vector caching using Redis and embedding similarity thresholds to serve repetitive LLM queries in under 20ms.",
                    "code_example": """import numpy as np

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
    print(f"Answer: {cached_ans} (Saved 100% LLM token cost!)")""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Semantic Caching Flow
  prompt[User Query Prompt] $terminal -> emb[Embedding Model (bge-small)] $brain
  emb -> cache_lookup[Redis Vector Index Search] $database
  cache_lookup -> hit{Similarity >= 0.95?} $code
  hit -- YES --> fast_out[Instant Cache Return (15ms)] $server *
  hit -- NO --> llm_call[Call Frontier LLM ($$$)] $cloud""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "GPTCache Architecture", "url": "https://github.com/zilliztech/GPTCache"}
                    ],
                    "xp_reward": 30,
                    "order_index": 4
                },
                {
                    "lesson_code": "6.5",
                    "slug": "websockets-realtime-ai-streams",
                    "title": "Real-Time Bidirectional AI Streams with WebSockets",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, Server-Sent Events (SSE) sirf unidirectional hote hain (Server se Client). Lekin modern agentic applications (jaise voice bots, real-time typing corrections, interactive AI canvas) mein **Bidirectional Communication** chahiye hoti hai jahan client aur server aapas mein continuous messages exchange kar sakein.

Yahan kaam aata hai **WebSockets (`ws://` aur `wss://`)**:
Ek single TCP connection establish hota hai jo full-duplex communication provide karta hai. Client user ka keystroke ya audio chunk bhejta rehta hai, aur server simultaneously tokens aur UI widget states push karta rehta hai.
Is lesson mein hum FastAPI WebSockets aur heartbeat ping/pong connection resilience ko master karenge.""",
                    "english_summary": "Build full-duplex, low-latency bidirectional AI applications using WebSockets, structured event framing, and heartbeat keep-alives.",
                    "code_example": """from fastapi import FastAPI, WebSocket, WebSocketDisconnect
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
        print("Client gracefully disconnected.")""",
                    "diagram_script": """@preset midnight
seq: Bidirectional WebSocket AI Flow
  client[Web Browser / React Client] -> server[FastAPI WebSocket]: WS Handshake (101 Switching Protocols)
  client -> server: {"action": "user_input", "text": "Plan my flight"}
  server -> client: {"type": "status", "state": "Invoking Booking Tool"}
  server -> client: {"type": "token", "val": "Found 3 flights..."} *
  client -> server: {"action": "confirm", "flight_id": "PK301"}""",
                    "diagram_type": "seq",
                    "resources": [
                        {"title": "FastAPI WebSockets Guide", "url": "https://fastapi.tiangolo.com/advanced/websockets/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "6.6",
                    "slug": "module-6-capstone-ai-gateway",
                    "title": "Module 6 Capstone: Enterprise Resilient Streaming AI Gateway Service",
                    "duration_minutes": 55,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, Module 6 ke Grand Capstone mein aap ek **Production-Grade Resilient AI Gateway** banayenge jo enterprise applications ko serve karega!

Real world mein agar Groq down ho jaye to aapki company ka customer support bot band nahi hona chahiye. Aapka gateway:
1. Multi-provider fallback cascade implement karega (Groq -> Cerebras -> Gemini Flash).
2. Semantic Cache layer check karega (Redis vector similarity).
3. Token-Bucket Rate Limiter lagaye ga taake koi spammer API budget burn na kare.
4. Server-Sent Events (SSE) ke through sub-100ms streaming ensure karega!""",
                    "english_summary": "Ship a production-grade AI gateway service featuring multi-provider failover cascades, semantic caching, token-bucket rate limiting, and SSE streaming.",
                    "code_example": """import asyncio
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

asyncio.run(test_gateway())""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Resilient AI Gateway Cascade
  req[User Streaming Request] $terminal -> rate[Token-Bucket Rate Limiter] $code
  rate -> cache[Redis Semantic Cache] $database
  cache -> primary[Primary Provider (Groq 400 tok/s)] $server
  primary -. Circuit Breaker Failure .-> fallback[Fallback Provider (Gemini / Cerebras)] $cloud *
  primary -> sse_out[SSE Client Stream] $browser
  fallback -> sse_out""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "OpenAI Compatible Gateways", "url": "https://github.com/BerriAI/litellm"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        },

        # =========================================================================
        # MODULE 7: Vector Databases & Modern RAG Architecture (ColPali)
        # =========================================================================
        {
            "phase_slug": "phase-3-modern-genai-stack",
            "module_number": 7,
            "slug": "vector-databases-and-modern-rag",
            "real_world_deliverable": "Multimodal PDF/Report RAG with ColPali Multi-Vector Search & Reranking",
            "zero_gpu_recipe": {
                'platform': 'Colab T4 / Supabase pgvector / Qdrant Cloud Free',
                'vram_required': '0 GB - 4 GB (ColPali)',
                'estimated_cost': '$0.00 Free Tier',
                'compute_units_tip': 'Supabase pgvector and Qdrant free tier provide 1M vectors for free. Run ColPali indexing on Colab T4.',
                'one_click_command': 'docker run -p 6333:6333 qdrant/qdrant'
            },
            "title": "Module 7: Vector Databases & Modern RAG Architecture (ColPali)",
            "weeks_range": "Weeks 13-14",
            "estimated_hours": 16,
            "learning_outcomes": [
                "Embedding models geometry, Cosine vs Inner Product vs Euclidean metrics",
                "Approximate Nearest Neighbor (ANN) indexing: HNSW, IVFFlat, aur PQ",
                "Advanced Hybrid Search: Dense vectors + Sparse BM25 via Reciprocal Rank Fusion (RRF)",
                "Document parsing and semantic chunking strategies",
                "Query transformations: HyDE (Hypothetical Document Embeddings) and Multi-Query",
                "2026 SOTA: ColPali Vision-Language Multi-Vector RAG without OCR text errors"
            ],
            "practical_tasks": [
                "PostgreSQL pgvector extension enable karein aur HNSW vector index build karein",
                "BM25 sparse search aur dense embeddings ka hybrid fusion algorithm likhein",
                "Semantic document chunker implement karein based on embedding cosine similarity",
                "Cross-Encoder Re-ranker (FlashRank / Cohere) se top-k chunks re-order karein",
                "ColPali multi-vector late interaction scoring implement karein on complex PDF tables"
            ],
            "resources": [
                {"title": "pgvector GitHub Repository", "url": "https://github.com/pgvector/pgvector"},
                {"title": "ColPali SOTA Paper", "url": "https://arxiv.org/abs/2407.01449"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 7 Modern RAG Pipeline
  doc[Complex PDF Document with Tables] $terminal -> colpali[ColPali Vision Multi-Vector Embeddings] $brain
  query[User Natural Query] $code -> hybrid[Hybrid HNSW + BM25 Search] $database
  hybrid -> rerank[Cross-Encoder Re-Ranker] $server
  rerank -> llm[LLM with Grounded Citations] $cpu *""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "rag-master",
            "order_index": 7,
            "lessons": [
                {
                    "lesson_code": "7.1",
                    "slug": "embeddings-vector-indexes",
                    "title": "Vector Embeddings & Indexing: HNSW, IVFFlat & pgvector",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, agar aapke database mein 1 million documents ke embeddings hain, to har query par 1 million dot products calculate karna ($O(N)$ brute-force) bohot slow ho jayega.

Isliye hum **Approximate Nearest Neighbor (ANN)** indexing use karte hain:
1. **IVFFlat (Inverted File Flat)**: Space ko Voronoi cells mein divide karta hai. Query aane par sirf sab se qareebi cell ke points check hote hain.
2. **HNSW (Hierarchical Navigable Small World)**: Graph-based indexing hai jo skip-lists ki tarah multi-layer graph banati hai. Yeh fastest search speed ($O(\\log N)$) aur 98%+ recall deti hai!

PostgreSQL mein `pgvector` extension HNSW index natively support karti hai.""",
                    "english_summary": "Understand vector embeddings geometry, ANN search indexing algorithms (IVFFlat vs HNSW), and pgvector execution.",
                    "code_example": """-- PostgreSQL pgvector Schema and HNSW Index Creation
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

SELECT id, content, 1 - (embedding <=> '[0.12, -0.45, ...]'::vector) AS similarity
FROM document_embeddings
ORDER BY embedding <=> '[0.12, -0.45, ...]'::vector
LIMIT 5;""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: HNSW Hierarchical Navigation
  layer2[Layer 2: Sparse Long-Jump Highway] $layers -> layer1[Layer 1: Medium-Density Clusters] $layers
  layer1 -> layer0[Layer 0: Dense Full-Vector Graph] $database *
  query[Query Vector] $terminal -> layer2""",
                    "diagram_type": "arch",
                    "resources": [{"title": "Pinecone HNSW Guide", "url": "https://www.pinecone.io/learn/series/faiss/hnsw/"}],
                    "xp_reward": 25,
                    "order_index": 1
                },
                {
                    "lesson_code": "7.2",
                    "slug": "advanced-rag-reranking",
                    "title": "Advanced RAG: Hybrid Search & Cross-Encoder Re-Ranking",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, standard RAG aksar production mein fail ho jata hai kyunke:
- Dense Vector Search exact keywords (jaise part numbers, CNIC, phone numbers, exact error codes) miss kar deta hai.
- Keyword Search (BM25) semantic meaning miss kar deta hai.

Iska production solution hai **Hybrid Search with Reciprocal Rank Fusion (RRF)**:
$$\\text{RRF Score}(d) = \\frac{1}{60 + \\text{Rank}_{\\text{Dense}}(d)} + \\frac{1}{60 + \\text{Rank}_{\\text{BM25}}(d)}$$

Uske baad hum top-20 results ko ek **Cross-Encoder Re-Ranker** (jaise Cohere Re-rank ya FlashRank) se pass karte hain jo query aur document chunk ko ikattha cross-attend karta hai aur sab se relevant top-3 chunks extract karta hai.""",
                    "english_summary": "Implement production Hybrid Search combining dense semantic embeddings with sparse BM25, fused via RRF and Cross-Encoder re-ranking.",
                    "code_example": """import numpy as np

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
    print(f"  {doc:18s}: RRF Score = {score:.4f}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Hybrid RAG Pipeline
  query[User Query] $terminal -> dense[Dense HNSW Search] $brain
  query -> sparse[Sparse BM25 Search] $code
  dense -> rrf[Reciprocal Rank Fusion] $layers
  sparse -> rrf
  rrf -> rerank[Cross-Encoder Reranker] $server
  rerank -> final[Top-3 Pristine Context Chunks] $cube *""",
                    "diagram_type": "flow",
                    "resources": [{"title": "Cohere Rerank Documentation", "url": "https://docs.cohere.com/docs/reranking"}],
                    "xp_reward": 30,
                    "order_index": 2
                },
                {
                    "lesson_code": "7.3",
                    "slug": "colpali-visual-rag",
                    "title": "2026 SOTA: ColPali Vision-Language Multi-Vector RAG",
                    "duration_minutes": 45,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, traditional RAG ka sab se bara dard **PDF Parsing & OCR** hai. Jab PDF mein complex tables, charts, diagrams, ya Urdu Nastaliq font hota hai to OCR tool (Tesseract/PyPDF) kachra text generate karta hai.

2024-2026 ka sab se bara breakthrough hai **ColPali (ColBERT + PaliGemma)**!
ColPali text extraction nahi karta. Yeh PDF ke har page ka ek visual screenshot leta hai aur Vision-Language Model se har page ke liye multiple patch-level vectors generate karta hai.

Query ke waqt **Late Interaction (MaxSim)** algorithm use hota hai:
$$\\text{Score}(Q, D) = \\sum_{q \\in Q} \\max_{d \\in D} (q \\cdot d)$$
Query ka har word page ke exact visual table cell ya chart bar se match karta hai! Zero OCR errors!""",
                    "english_summary": "Understand ColPali multi-vector retrieval, visual document indexing directly from page images, and Late Interaction (MaxSim) operator mechanics.",
                    "code_example": """import torch

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
print(f"ColPali Late Interaction MaxSim Score: {score:.3f}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: ColPali Multi-Vector Late Interaction
  pdf_page[PDF Page Screenshot] $terminal -> vlm[PaliGemma Vision Encoder] $brain
  vlm -> patches[Page Patch Vectors (1024 Multi-Vectors)] $database
  q_text[Query: 'Q3 EBITDA margin'] $code -> q_vecs[Query Token Vectors] $layers
  patches -> maxsim[MaxSim Late Interaction Sum-Max] $cpu *
  q_vecs -> maxsim""",
                    "diagram_type": "flow",
                    "resources": [{"title": "ColPali GitHub Repository", "url": "https://github.com/illuin-tech/colpali"}],
                    "xp_reward": 35,
                    "order_index": 3
                },
                {
                    "lesson_code": "7.4",
                    "slug": "document-chunking-hierarchical",
                    "title": "Advanced Document Parsing & Semantic Chunking",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, agar aap document ko bilkul andha-dhund fixed 500 characters par split kar dein, to sentence beech mein kat jayega aur context destroy ho jayega!

Isliye modern RAG mein teen advanced chunking strategies use hoti hain:
1. **Recursive Character Chunking**: Paragraphs (`\\n\\n`), phir sentences (`\\n`), phir spaces par split karta hai taake natural boundaries preserve hon.
2. **Semantic Chunking**: Har sentence ka embedding banata hai aur jahan do consecutive sentences ki Cosine Similarity achanak drop ho (Topic Shift), wahan naya chunk shuru karta hai.
3. **Parent-Document (Hierarchical) Retrieval**: Chotay 200-token chunks par search karta hai, lekin LLM ko poora parent paragraph (800 tokens) pass karta hai taake context complete rahay!""",
                    "english_summary": "Master recursive chunking, semantic similarity boundary detection, and parent-document hierarchical chunk retrieval.",
                    "code_example": """import numpy as np

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
    print(f"Chunk {idx+1}: {c}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Semantic Chunking Workflow
  raw_doc[Continuous Raw Document Text] $database -> sents[Sentence Segmenter] $code
  sents -> sim_calc[Consecutive Embedding Cosine Drop] $brain
  sim_calc -> split[Topic-Boundary Split] $layers
  split -> parent_child[Parent Document Hierarchical Store] $server *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "LangChain Semantic Chunking", "url": "https://python.langchain.com/docs/how_to/semantic_chunker/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 4
                },
                {
                    "lesson_code": "7.5",
                    "slug": "query-transformation-hyde-multi",
                    "title": "Query Transformations: HyDE, Multi-Query & Step-Back",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, user ka original query aksar chota, ambiguous, ya incomplete hota hai (maslan: *"loan documents"*). Agar aap seedha is query ka embedding banayein to database se acche chunks nahi milenge.

Yahan kaam aati hain **Query Transformations**:
1. **HyDE (Hypothetical Document Embeddings)**: LLM se pehle ek farzi (hypothetical) ideal answer generate karwayein. Phir us generated answer ka embedding banayein! Document-to-document similarity hamesha query-to-document se 10x behtar hoti hai!
2. **Multi-Query**: LLM se ek query ke 3 mukhtalif synonyms generate karwayein aur parallel vector search karein.
3. **Step-Back Prompting**: Specific sawal se pehle broad foundational concept retrieve karna.""",
                    "english_summary": "Supercharge retrieval recall using query expansion strategies: Hypothetical Document Embeddings (HyDE), multi-query generation, and step-back abstractions.",
                    "code_example": """def generate_hyde_prompt(user_query: str) -> str:
    return (
        "Please write a short hypothetical paragraph answering this question accurately.\\n"
        "Do not worry about specific facts, focus on domain vocabulary and scientific concepts.\\n"
        f"Question: {user_query}\\nHypothetical Answer:"
    )

query = "PyTorch AMP memory leak fix"
hypothetical_answer = (
    "When training with PyTorch Automatic Mixed Precision (AMP), ensure you call "
    "scaler.unscale_ before clipping gradients and invoke scaler.update(). Avoid storing tensors "
    "with attached computation graphs in history lists."
)

print("Original User Query:", query)
print("\\nGenerated HyDE Passage (Matches doc space perfectly):")
print(hypothetical_answer)""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: HyDE Query Transformation
  raw_q[Short User Query] $terminal -> llm_gen[LLM Generates Hypothetical Doc] $brain
  llm_gen -> hyde_doc[Hypothetical Target Answer] $code
  hyde_doc -> vector_search[Doc-to-Doc High-Precision Search] $database *""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "HyDE Research Paper", "url": "https://arxiv.org/abs/2212.10496"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "7.6",
                    "slug": "module-7-capstone-enterprise-rag",
                    "title": "Module 7 Capstone: Zero-Hallucination Enterprise RAG with Source Verification",
                    "duration_minutes": 60,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, Module 7 ka Grand Capstone aapko real-world Enterprise AI architect banayega!

Is capstone mein aap ek **Zero-Hallucination Production RAG System** build karenge:
1. Multi-page financial report PDF ko parse aur semantic chunks mein split karna.
2. PostgreSQL `pgvector` HNSW index + BM25 sparse search se Hybrid Search run karna.
3. Cross-Encoder reranker se top-3 chunks prioritize karna.
4. LLM prompt mein strict citation rules lagana (e.g. `[Doc 1, Page 4]`).
5. Automated faithfulness check karna: agar answer context se substantiate na ho to model explicit *"I cannot answer based on the provided documents"* return kare!""",
                    "english_summary": "Ship an end-to-end enterprise RAG pipeline featuring hybrid HNSW+BM25 search, Cross-Encoder reranking, grounded citation generation, and hallucination guardrails.",
                    "code_example": """def generate_grounded_rag_prompt(query: str, retrieved_chunks: list) -> str:
    context_str = ""
    for idx, c in enumerate(retrieved_chunks):
        context_str += f"[Source {idx+1} | Page {c['page']}]: {c['text']}\\n"
        
    prompt = (
        f"Context Information:\\n{context_str}\\n"
        "Task: Answer the user question strictly using the provided sources.\\n"
        "Every factual claim must cite its source e.g. [Source 1, Page 2].\\n"
        "If the context does not contain the answer, reply: 'Information not found in verified documents.'\\n\\n"
        f"Question: {query}\\nGrounded Answer:"
    )
    return prompt

mock_chunks = [
    {"page": 4, "text": "Net revenue for Q3 2025 reached PKR 45.2 Billion, an increase of 18% YoY."},
    {"page": 7, "text": "Operating expenses were reduced by 6% due to automated AI workflows."}
]

rag_prompt = generate_grounded_rag_prompt("What was the Q3 2025 revenue?", mock_chunks)
print("Production Grounded Prompt:")
print(rag_prompt)""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Enterprise Zero-Hallucination RAG
  query[User Natural Query] $terminal -> hybrid[Hybrid HNSW + BM25 Search] $database
  hybrid -> rerank[Cross-Encoder Reranker] $server
  rerank -> context[Top-3 Verified Context Chunks] $layers
  context -> llm[LLM with Citation Grounding] $brain
  llm -> verifier[Faithfulness Verifier] $code
  verifier -> out[Guaranteed Grounded Output with Citations] $terminal *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Ragas: Automated Evaluation of RAG", "url": "https://docs.ragas.io/"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        },

        # =========================================================================
        # MODULE 8: Autonomous Agents, MCP & Tool Use
        # =========================================================================
        {
            "phase_slug": "phase-3-modern-genai-stack",
            "module_number": 8,
            "slug": "autonomous-agents-and-tool-use",
            "real_world_deliverable": "Autonomous Multi-Agent Swarm with Anthropic MCP & Sandboxed Code Execution",
            "zero_gpu_recipe": {
                'platform': 'Local CPU / Groq Cloud / Gemini API Free Tier',
                'vram_required': '0 GB (Tool Use APIs)',
                'estimated_cost': '$0.00 Free Tier',
                'compute_units_tip': 'Agent reasoning loops run on cloud API free tier (Groq / Gemini 2.0 Flash) with zero GPU cost.',
                'one_click_command': 'pip install mcp smolagents langgraph langchain-core && python agent.py'
            },
            "title": "Module 8: Autonomous Agents, MCP & Tool Use (Anthropic MCP, smolagents)",
            "weeks_range": "Weeks 15-16",
            "estimated_hours": 16,
            "learning_outcomes": [
                "The ReAct Pattern: Reasoning + Acting cyclic execution loops",
                "2026 Industry Standard: Anthropic Model Context Protocol (MCP) Client & Server Architecture",
                "HuggingFace smolagents: Code-First Agents vs JSON-Action agents",
                "Function and tool calling specifications with OpenAPI and JSON Schemas",
                "Stateful cyclic multi-agent graphs with LangGraph and memory checkpoints",
                "Multi-agent collaboration patterns: Supervisor, Worker, and Critique"
            ],
            "practical_tasks": [
                "Custom SQLite database query tool implement karein with strict schema validation",
                "Anthropic MCP server create karein jo local system diagnostics provide kare",
                "smolagents sandboxed Python interpreter agent build karein",
                "LangGraph state machine graph construct karein with human-in-the-loop review",
                "Autonomous Multi-Agent Bug Fixing swarm build karein"
            ],
            "resources": [
                {"title": "Anthropic Model Context Protocol (MCP)", "url": "https://modelcontextprotocol.io/"},
                {"title": "HuggingFace smolagents Documentation", "url": "https://huggingface.co/docs/smolagents/"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 8 Agentic Architecture
  user[User High-Level Task] $terminal -> planner[ReAct Supervisor Agent] $brain
  planner -> mcp[Anthropic MCP Server Tools] $code
  mcp -> env[Sandboxed Execution Environment] $server
  env -> obs[Observation & Self-Correction] $database
  obs -> planner: Cyclic Thought Loop *""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "agent-architect",
            "order_index": 8,
            "lessons": [
                {
                    "lesson_code": "8.1",
                    "slug": "react-agent-architecture",
                    "title": "ReAct Pattern: Reasoning + Acting Ka Mukammal Framework",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab hum LLM ko tools (APIs, Database, Calculator) dete hain to wo sirf text generator nahi rehta, balke ek **Autonomous Agent** ban jata hai!

Sab se famous pattern hai **ReAct (Reasoning + Acting)**:
1. **Thought**: Model sochta hai ke agla qadam kya hona chahiye: *"Mujhe pehle customer ka order number dhoondna hai."*
2. **Action**: Model specific tool call karta hai with exact parameters: `lookup_order(order_id=9821)`.
3. **Observation**: Environment tool ka result wapis LLM ko bhejta hai: `Order status: Shipped, Tracking: TCS102`.
4. **Reflection**: Model observation dekh kar agla step decide karta hai ya final user response generate karta hai.

Agar tool koi error de to model **Self-Correction** karta hai aur doosra tareeqa azmata hai!""",
                    "english_summary": "Implement the ReAct paradigm: alternating between Reasoning thoughts, Action tool executions, and Observations with autonomous error correction.",
                    "code_example": """import json

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
print("Tool Execution Observation:", json.dumps(observation))""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: ReAct Autonomous Agent Loop
  thought[Thought: Model Reasons] $brain -> action[Action: Tool Call Generated] $code
  action -> env[Environment Executes Tool] $server
  env -> obs[Observation: Raw Tool Result] $database
  obs -> thought: Loop until Task Solved *
  thought -> final_ans[Final Resolved Answer] $terminal""",
                    "diagram_type": "flow",
                    "resources": [{"title": "ReAct Research Paper (Yao et al.)", "url": "https://arxiv.org/abs/2210.03629"}],
                    "xp_reward": 25,
                    "order_index": 1
                },
                {
                    "lesson_code": "8.2",
                    "slug": "anthropic-mcp-deepdive",
                    "title": "2026 Standard: Anthropic Model Context Protocol (MCP) Deep Dive",
                    "duration_minutes": 45,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, pehle har company apna custom tool format likhti thi (LangChain tools alag, OpenAI functions alag, AutoGen alag). Is fragmented dunya ko khatam karne ke liye Anthropic ne **Model Context Protocol (MCP)** launch kiya jo 2026 ka universal USB-C standard ban chuka hai!

MCP Architecture ke 3 arkaan hain:
1. **MCP Host**: Application jismein LLM chal raha hai (jaise Claude Desktop, Antigravity IDE, ya aapka backend).
2. **MCP Client**: Jo host ke andar server se connection banata hai.
3. **MCP Server**: Lightweight microservice jo tools, prompts, aur resources expose karti hai via JSON-RPC 2.0 (stdio ya SSE transport).

Ek dafa aapne MCP server likh diya, wo kisi bhi AI client mein bina modification plug-and-play chalega!""",
                    "english_summary": "Master the Model Context Protocol (MCP): Host, Client, and Server architecture communicating via JSON-RPC 2.0 stdio/SSE transports.",
                    "code_example": """import json

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

sample_rpc = '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}'
response = handle_mcp_request(sample_rpc)
print("MCP Server Response:\\n", response)""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Anthropic MCP Architecture
  host[MCP Host (AI Platform)] $browser -> client[MCP Client Engine] $terminal
  client -> transport[JSON-RPC 2.0 via stdio / SSE] $layers
  transport -> server[MCP Server (Local Tools / DB / APIs)] $server *""",
                    "diagram_type": "arch",
                    "resources": [{"title": "Official MCP Documentation", "url": "https://modelcontextprotocol.io/"}],
                    "xp_reward": 30,
                    "order_index": 2
                },
                {
                    "lesson_code": "8.3",
                    "slug": "smolagents-code-agents",
                    "title": "HuggingFace smolagents: Code-First Agents & Sandboxing",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, traditional agents har step par JSON tool calls generate karte hain:
`{"action": "add", "args": {"a": 5, "b": 10}}`
Agar aapko 100 calculations karni hon to 100 round-trips lagte hain jo bohot slow aur mehanga hota hai!

HuggingFace ne **smolagents** ke zariye **Code-First Agents** introduce kiye!
Model actions ko JSON mein nahi balke seedha **Python Code Block** mein likhta hai:
```python
results = [math.sqrt(x) for x in range(100)]
final_sum = sum(results)
print(final_sum)
```
Yeh code ek secure sandboxed AST interpreter mein execute hota hai. 1 single LLM call mein complex loops, data transformation, aur multi-tool logic execute ho jata hai!""",
                    "english_summary": "Explore HuggingFace smolagents: replacing clunky multi-turn JSON tool schemas with direct sandboxed Python code synthesis.",
                    "code_example": """import math

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
    "values = [math.factorial(n) for n in range(1, 6)]\\n"
    "total = sum(values)"
)
res = agent.execute_agent_code(generated_code)
print("Sandboxed Code Execution Result:", res['locals']['total'])""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Code-First smolagents Execution
  prompt[User Data Analytics Request] $terminal -> llm[LLM Synthesizes Python Code] $brain
  llm -> ast_check[Sandboxed AST Security Inspection] $code
  ast_check -> py_exec[Python Local Interpreter Execution] $cpu *
  py_exec -> final_res[Instant Mathematical Result] $server""",
                    "diagram_type": "flow",
                    "resources": [{"title": "HuggingFace smolagents Blog", "url": "https://huggingface.co/blog/smolagents"}],
                    "xp_reward": 30,
                    "order_index": 3
                },
                {
                    "lesson_code": "8.4",
                    "slug": "function-calling-json-schemas",
                    "title": "Function Calling Specifications & Runtime Schema Validation",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab LLM kisi tool ko call karta hai to aksar numbers ko string bana deta hai (`"50"` instead of `50`) ya required keys miss kar deta hai.

Iska production solution hai **Runtime Schema Validation via Pydantic & OpenAPI**.
Hum tool ki exact specification define karte hain:
- Tool name
- Clear description (jo model ko batati hai ke kab call karna hai)
- Pydantic parameters with type annotations aur default values.

Agar LLM ghalat arguments return kare to validator foran error trap karta hai aur model ko auto-correction prompt bhejta hai: *"Validation failed: age must be an integer >= 18"*. Model agle turn par theek argument generate karta hai!""",
                    "english_summary": "Define robust function specifications using OpenAPI schemas and Pydantic models with automated schema validation and correction loops.",
                    "code_example": """from pydantic import BaseModel, Field, ValidationError

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
print("Valid Tool Execution:", execute_validated_tool(good_input))""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Function Calling Validation Loop
  llm_call[LLM Tool Call Arguments] $brain -> pydantic[Pydantic Runtime Schema Check] $code
  pydantic -- Valid --> exec[Execute Python Tool Function] $server *
  pydantic -- Invalid --> retry[Error Context Feedback to LLM] $terminal
  retry -> llm_call""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "OpenAI Function Calling Guide", "url": "https://platform.openai.com/docs/guides/function-calling"}
                    ],
                    "xp_reward": 25,
                    "order_index": 4
                },
                {
                    "lesson_code": "8.5",
                    "slug": "langgraph-cyclic-workflows",
                    "title": "Stateful Multi-Agent Cyclic Graphs with LangGraph",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, puraane agent frameworks (jaise original LangChain chains) Linear DAGs (Directed Acyclic Graphs) thay — yaani data sirf aage move kar sakta tha, pichle step par wapis nahi aa sakta tha!

Lekin real-world problem solving **Cyclic (Chakkar wali)** hoti hai:
Codegen -> Run Tests -> Error Found -> Wapis Codegen par jao -> Dubara test karo!

Iske liye 2026 mein **LangGraph** industry standard ban chuka hai.
LangGraph mein:
1. **State**: Ek shared dictionary jo tamam agents read/write karte hain.
2. **Nodes**: Python functions ya AI agents (Researcher, Coder, Reviewer).
3. **Edges & Conditional Edges**: Jo decide karte hain ke agla node kon sa chalay ga based on current state!
4. **Human-in-the-Loop**: Execution ko pause karke human approval ka wait karna.""",
                    "english_summary": "Architect stateful, cyclic agent workflows using LangGraph state machines, conditional edges, and human-in-the-loop checkpoints.",
                    "code_example": """from typing import TypedDict

class AgentState(TypedDict):
    code: str
    test_passed: bool
    iterations: int

def coder_node(state: AgentState) -> AgentState:
    print(f"Coder: Writing code attempt {state['iterations'] + 1}...")
    state['code'] = "def add(a, b): return a + b"
    state['iterations'] += 1
    return state

def tester_node(state: AgentState) -> AgentState:
    print("Tester: Running pytest suite...")
    state['test_passed'] = (state['iterations'] >= 2)
    return state

def should_continue(state: AgentState) -> str:
    if state['test_passed'] or state['iterations'] >= 3:
        return "END"
    return "coder_node"

state = {"code": "", "test_passed": False, "iterations": 0}
while True:
    state = coder_node(state)
    state = tester_node(state)
    next_step = should_continue(state)
    if next_step == "END":
        print(f"Workflow Finished! Final Code: {state['code']}, Passed: {state['test_passed']}")
        break""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: LangGraph Cyclic State Machine
  coder[Coder Agent Node] $code -> tester[Tester Validation Node] $server
  tester -> cond{Tests Passed?} $terminal
  cond -- NO --> coder
  cond -- YES --> end_node[Production Artifact Ready] $cube *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "LangGraph Official Documentation", "url": "https://langchain-ai.github.io/langgraph/"}
                    ],
                    "xp_reward": 30,
                    "order_index": 5
                },
                {
                    "lesson_code": "8.6",
                    "slug": "module-8-capstone-autonomous-swarm",
                    "title": "Module 8 Capstone: Autonomous Multi-Agent Software Engineering Swarm",
                    "duration_minutes": 60,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, Module 8 ka Grand Capstone aapko **Autonomous Swarm Engineer** banayega!

Is capstone mein aap ek **Multi-Agent Software Development Swarm** implement karenge jismein 3 specialized agents aapas mein collaborate karte hain:
1. **Supervisor Agent**: User ki feature request ko decompose karta hai aur sub-tasks assign karta hai.
2. **Coder Agent**: Anthropic MCP server ke zariye file read/write tools execute karke code files create karta hai.
3. **Critic & Security Agent**: Code ko audit karta hai (SQL injection check, type errors) aur passing verdict deta hai.

Swarm ek cyclic loop mein chalega jab tak security audit 100% pass na ho jaye!""",
                    "english_summary": "Construct an autonomous multi-agent swarm with Supervisor, Worker, and Critic roles utilizing MCP tools and self-correcting feedback loops.",
                    "code_example": """class MultiAgentSwarm:
    def __init__(self):
        self.history = []

    def run_swarm(self, user_objective: str):
        print(f"=== Supervisor: Planning tasks for: '{user_objective}' ===")
        task = "Build sanitized SQL query builder"
        
        print("=== Coder Agent: Generating Python implementation ===")
        code = "def safe_query(user_id: int): return f'SELECT * FROM users WHERE id = {int(user_id)}'"
        
        print("=== Security Critic Agent: Auditing for SQL Injection ===")
        audit_passed = "int(" in code
        print(f"Security Audit Result: {'PASS' if audit_passed else 'FAIL'}")
        
        return {"task": task, "code": code, "audit_status": "APPROVED"}

swarm = MultiAgentSwarm()
result = swarm.run_swarm("Create user query function")
print("\\nSwarm Final Production Deliverable:", result)""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Multi-Agent Software Swarm
  user[User Feature Request] $terminal -> supervisor[Supervisor Planner Agent] $brain
  supervisor -> coder[Coder Agent (MCP File Tools)] $code
  coder -> critic[Security & Quality Critic Agent] $server
  critic -- Feedback & Bug Fixes --> coder
  critic -- Approved --> release[Production Git PR] $cube *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Multi-Agent Systems Patterns", "url": "https://arxiv.org/abs/2308.08155"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        }
    ]
