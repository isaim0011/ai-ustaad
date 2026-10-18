# module_06.py
# Module 6: Building AI Applications & Modern APIs
# Lessons 6.1 to 6.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 6.1: Streaming LLM APIs: Server-Sent Events (SSE) & Async Iterators
# ==============================================================================
LESSON_CONTENT['6.1'] = r"""### Part 1: Mental Model & South Asian Analogy
LLM applications mein sab se bari user experience (UX) tabahi tab aati hai jab user prompt enter karke 15 second tak gup-chup loading spinner dekhta rehta hai. Is maslay ko hal karta hai **Token Streaming with Server-Sent Events (SSE)**!
Isay samajhne ke liye kisi Mashhoor Jalebi wale ki Dukan ki misaal lein:
1. Batch API Response (Thandi Jalebi Ka Dabba): Farz karein aap jalebi wale se kehte hain: "Mujhe 2 kilo jalebi chahiye." Halwai aapse kehta hai: "Chup chaap kone mein kharay rahein, jab tak aakhri jalebi tal kar dabba seal nahi ho jata, main aapko ek jalebi bhi chhoone nahi doonga!" Aap 20 minute tak bhookay kharay rehte hain.
2. Streaming with Server-Sent Events (Kadhai Se Garma-Garam Jalebi): Samajhdaar halwai kya karta hai? Jaise hi pehli jalebi sheeray se nikal kar aati hai, woh foran kaghaz par rakh kar aapke hath mein thama deta hai: "Lijiye pehli jalebi khayein, aglay do minute mein doosri aa rahi hai!" User pehle second se khana shuru kar deta hai.
3. Time To First Token (TTFT): User ke dimagh mein app ka ta'assur is baat se banta hai ke pehla lafz kitni jaldi screen par typewriter effect ke sath type hona shuru hua. Agar TTFT 500 milliseconds ho to user ko lagta hai ke app bijli jaisi tez hai, chahe poora lamba jawab aane mein 10 second hi kyun na lagein!
4. SSE HTTP Protocol: Standard HTTP request/response mein connection foran band ho jata hai. SSE mein client aur server ke darmiyan ek persistent unidirectional HTTP pipe khul jata hai jisme server chunks bhejta rehta hai: `data: {"token": "Chai"}\n\n`.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Perceived Latency aur Network Bandwidth Utilization ka exact mathematical hisab lagayein.
Parameters:
- Prompt Length = 200 tokens
- Generation Length = 600 tokens
- Inference Generation Speed = 40 tokens per second
- Total Generation Time: $\frac{600}{40} = 15.0 \text{ seconds}$
- Network Transit Latency = $0.2 \text{ seconds}$ (200 ms)

Scenario A: Blocking Batch REST API
User submits query at $t = 0.0\text{s}$.
- Server generates all 600 tokens: 15.0s.
- Network transfer payload: 0.2s.
- First visual feedback to user: $t = 15.2 \text{ seconds}$!
Perceived Latency by user $= 15.2\text{ seconds}$ (User feels the app is frozen or dead).

Scenario B: Streaming via Server-Sent Events (SSE)
User submits query at $t = 0.0\text{s}$.
- Time to First Token (TTFT): First token generated at $t = \frac{1}{40} = 0.025\text{s} + 0.2\text{s} = 0.225 \text{ seconds}$!
- User begins reading at $t = 0.225 \text{ seconds}$.
- Average human reading speed $\approx 5$ words per second $\approx 7$ tokens/sec.
Chunke model ki generation speed (40 tokens/sec) insani padhne ki raftaar (7 tokens/sec) se tez hai, user ko mehsoos hota hai ke system zero-latency real-time stream kar raha hai!
Perceived latency drop: $15.2\text{s} \to 0.225\text{s}$ ($\approx 67\times \text{ UX Improvement}$)!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum FastAPI asynchronous generator, standard Server-Sent Events (SSE) streaming response, aur stream heartbeat keep-alive mechanism ko implement karte hain.

```python
import asyncio
import json
import time
from typing import AsyncGenerator
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI(title="Production SSE LLM Streamer")

async def mock_llm_token_stream(prompt: str) -> AsyncGenerator[str, None]:
    \"\"\"Simulates production autoregressive LLM token emission with SSE formatting.\"\"\"
    tokens = [
        "Chai", " ", "ki", " ", "khushboo", " ", "aur", " ", 
        "subah", " ", "ka", " ", "mausam", " ", "zabardast", " ", "hai."
    ]
    
    # 1. Emit stream start event
    start_payload = json.dumps({"event": "start", "prompt_received": prompt})
    yield f"data: {start_payload}\\n\\n"
    
    # 2. Emit tokens sequentially with simulated generation delay
    for idx, token in enumerate(tokens):
        await asyncio.sleep(0.05)  # 20 tokens per second simulation
        token_payload = json.dumps({
            "event": "token",
            "index": idx,
            "text": token
        })
        # SSE standard specification requires 'data: <payload>\n\n'
        yield f"data: {token_payload}\\n\\n"

    # 3. Emit explicit completion signal
    done_payload = json.dumps({"event": "done", "total_tokens": len(tokens)})
    yield f"data: {done_payload}\\n\\n"

@app.get("/stream-chat")
async def stream_chat_endpoint(prompt: str = "Chai poetry"):
    \"\"\"FastAPI streaming endpoint returning text/event-stream.\"\"\"
    return StreamingResponse(
        mock_llm_token_stream(prompt),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # Prevents NGINX reverse-proxy from buffering tokens!
        }
    )

# Verification execution
if __name__ == "__main__":
    async def test_stream():
        print("Testing Local Async SSE Generator:")
        async for chunk in mock_llm_token_stream("Subah ki chai"):
            print(f"Received Chunk: {chunk.strip()}")
            
    asyncio.run(test_stream())
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. NGINX Reverse-Proxy Buffering SSE Streams: Production mein NGINX default tor par 4KB ya 8KB data buffer karta hai. Nateeja yeh nikalta hai ke NGINX tamam tokens jama karta rehta hai aur aakhir mein ek sath ulat deta hai, jisse streaming khatam ho jati hai. Hamesha header bhejein: `X-Accel-Buffering: no`.
2. Forgetting `\n\n` in SSE Format: SSE protocol specification ke mutabiq har event ke aakhir mein exactly do newlines `\n\n` hona lazmi hain. Agar sirf ek newline `\n` ho to browser client event trigger nahi karta aur buffer mein atak jata hai.
3. Unhandled Client Disconnections: Agar user tab band kar de ya browser refresh kar de, aur backend background mein LLM tokens generate karta rahe to API tokens aur GPU compute zaaya hote hain. Hamesha `request.is_disconnected` check karein.

Zero-GPU Tip:
SSE streaming protocol pure network layer abstraction hai. FastAPI aur Uvicorn ke sath aap apne laptop CPU par hazaron concurrent mock SSE streams benchmark kar sakte hain with zero GPU hardware.

Self-Check Questions:
1. Server-Sent Events (SSE) aur WebSockets mein protocol level par kya farq hai?
2. NGINX proxy mein `X-Accel-Buffering: no` header kyun lazmi hota hai?
3. Time To First Token (TTFT) user experience ke liye total completion time se zyada ahem kyun hota hai?

What to Build Next:
Ek Python CLI Client banayein jo `httpx.AsyncClient` use karke `/stream-chat` SSE endpoint ko connect kare aur terminal par live typewriter animation ke sath tokens render kare."""

# ==============================================================================
# LESSON 6.2: Full-Stack AI Architecture: State & Token Management
# ==============================================================================
LESSON_CONTENT['6.2'] = r"""### Part 1: Mental Model & South Asian Analogy
Aam web applications stateless hoti hain: user request bhejta hai, server database se query karta hai aur response return kar deta hai. Lekin Conversational AI Applications inherently stateful hoti hain aur har guftagu ke sath unka context window size barhta jata hai.
Isay samajhne ke liye kisi Mashhoor PCO / Call Office aur Phone Call Metering ki misaal lein:
1. The Exploding Context Ledger (PCO Ka Meter): Farz karein aap PCO se baher-mulk phone karte hain. Har minute ke baad meter par bill double hota jata hai. Agar chat lambi ho jaye to 50th turn par pichle 49 turns ka poora hisab model ko dobara bhejna parta hai. Agar aap context ko regulate na karein to ek ghantay ki chat hazaron rupaye ka bill bana sakti hai!
2. Ephemeral State vs Persistent Memory:
   - Client-Side State: React / Vue frontend mein temporary UI messages ki list hoti hai taake screen par foran chat bubble dikh sake (Optimistic UI Update).
   - Server-Side Ground Truth: Supabase / PostgreSQL database mein audit logs, timestamps, user ID, aur exact token consumption lock hoti hai.
3. Context Window Pruning (Khaata Mukhtasir Karna): Aqalmand munshi kya karta hai? Jab register ke safhay bharne lagte hain to woh pichle 20 dinon ke chotay chotay transactions ko ek single line summary bana deta hai: "Pichle maheene ka baqiya: Rs 15,000." Modern AI architecture mein hum Sliding Window plus Background LLM Summarization use karte hain taake context window hamesha 4,000 tokens ke budget ke andar rahe!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Context Pruning aur Sliding Window Token Budgeting ka exact hisab lagayein.
Parameters:
- Model Context Window Limit = 4096 tokens
- Reserved for New Response = 1000 tokens
- System Prompt & Tools = 500 tokens
- Available Budget for Chat History = $4096 - 1000 - 500 = 2596 \text{ tokens}$.

Multi-Turn Chat History Simulation:
Har message turn (User question + Assistant answer) average 200 tokens leta hai.
- Turn 1 to 10: $10 \times 200 = 2000 \text{ tokens}$ (Within budget: $2000 \le 2596$).
- Turn 15: $15 \times 200 = 3000 \text{ tokens}$ (Budget exceeded by 404 tokens! Model will crash or truncate).

Pruning Strategy: Sliding Window + Summary:
- Keep the last $K = 5$ turns verbatim (Exact recent memory):
  $5 \times 200 = 1000 \text{ tokens}$.
- Summarize the older 10 turns into a compact summary paragraph:
  Old 10 turns (2000 tokens) compressed to $\approx 150 \text{ tokens}$ via background summary.
New Memory Budget Used:
$\text{Summary} (150) + \text{Recent 5 Turns} (1000) = 1150 \text{ tokens}$.
Remaining Free Buffer in Context:
$2596 - 1150 = 1446 \text{ tokens}$ free!
Humne baghair kisi context loss ke 1850 tokens save kar liye aur model ko crashing se bacha liya!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Token-Aware Context Manager class implement karte hain jo chat turns ko monitor karti hai aur token limits ke mutabiq sliding window prune karti hai.

```python
from dataclasses import dataclass, field
from typing import List, Dict, Literal

@dataclass(slots=True)
class ChatMessage:
    role: Literal["system", "user", "assistant"]
    content: str
    token_count: int

class TokenBudgetManager:
    \"\"\"Manages multi-turn conversation context within a strict token ceiling.\"\"\"
    def __init__(self, max_history_tokens: int = 2500, system_prompt: str = "") -> None:
        self.max_history_tokens = max_history_tokens
        self.system_message = ChatMessage(
            role="system", 
            content=system_prompt, 
            token_count=len(system_prompt.split()) * 2  # Approximate heuristic
        )
        self.history: List[ChatMessage] = []

    def add_message(self, role: Literal["user", "assistant"], content: str) -> None:
        token_count = max(len(content.split()) * 2, 1)
        self.history.append(ChatMessage(role=role, content=content, token_count=token_count))

    def get_pruned_context(self) -> List[Dict[str, str]]:
        \"\"\"Prunes older turns dynamically from the left until total tokens <= budget.\"\"\"
        current_tokens = sum(m.token_count for m in self.history)
        
        # Evict oldest user-assistant pairs if over budget
        evicted_count = 0
        while current_tokens > self.max_history_tokens and len(self.history) > 2:
            # Remove oldest message
            removed = self.history.pop(0)
            current_tokens -= removed.token_count
            evicted_count += 1

        compiled_payload: List[Dict[str, str]] = [
            {"role": self.system_message.role, "content": self.system_message.content}
        ]
        for msg in self.history:
            compiled_payload.append({"role": msg.role, "content": msg.content})
            
        return compiled_payload

# Execution test
if __name__ == "__main__":
    manager = TokenBudgetManager(
        max_history_tokens=100,
        system_prompt="You are a helpful Pakistani AI tutor."
    )
    
    # Add multiple turns exceeding budget
    for i in range(1, 10):
        manager.add_message("user", f"Turn {i}: How do I optimize PyTorch code on CPU?")
        manager.add_message("assistant", f"Turn {i}: Use torch.compile and OpenMP vectorization.")

    pruned = manager.get_pruned_context()
    print(f"Total turns compiled in prompt payload: {len(pruned)} (Includes system prompt)")
    print("Oldest retained user turn:", pruned[1]["content"])
    print("Most recent user turn:     ", pruned[-2]["content"])
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Splitting User-Assistant Message Pairs During Truncation: Purani messages delete karte waqt agar aap sirf ek message delete karein jisse conversation assistant ke jawab se shuru ho jaye, to model context kho deta hai. Hamesha user-assistant pair ko ek sath evict karein.
2. Relying on Character Count Instead of Token Count: Angrezi mein 4 characters $\approx$ 1 token hota hai, lekin code ya Urdu mein 1 character 1 token le sakta hai. Character count par budget banana context window overflow ka sabab banta hai. Hamesha fast BPE tokenizer se exact tokens count karein.
3. Storing Session State in Server Memory (RAM): Stateful chatbot ko server ke global dictionary mein store karne se jaise hi multiple server instances (load balancer) aate hain, user doosre server par chala jata hai aur chat history gayab ho jati hai. State hamesha external Redis ya Supabase database mein rakhein.

Zero-GPU Tip:
Token count monitoring aur sliding window context pruning pure CPU algorithmic logic hai. Is logic ko bina kisi GPU ke local unit tests mein hazaron turns par chala kar memory stability verify ki ja sakti hai.

Self-Check Questions:
1. Context window budget mein System Prompt, History, aur Generation Reserve ka kya batwara hota hai?
2. Stateless web architecture mein multi-turn conversation memory ko Redis ya database mein kyun rakha jata hai?
3. Sliding window eviction aur LLM summarization ko aapas mein kaise jora jata hai?

What to Build Next:
Ek Conversation History Persister banayein jo SQLite database mein messages save kare, token budget check kare, aur jab total tokens exceed hon to automated background summary generate karke purane records archive kare."""

# ==============================================================================
# LESSON 6.3: Production Async AI Gateways with FastAPI & Redis Task Queues
# ==============================================================================
LESSON_CONTENT['6.3'] = r"""### Part 1: Mental Model & South Asian Analogy
Jab aapki AI application par achanak 10,000 users toot partay hain, to agar har request seedha LLM GPU server par chali jaye to GPU foran Out-of-Memory (OOM) crash ho jayega aur poori service gir jayegi. Isay sambhalne ke liye **Async AI Gateway aur Redis Task Queues** use hoti hain.
Isay samajhne ke liye kisi Mashhoor Pasban / Bank Cash Counter aur Token Machine ki misaal lein:
1. The Chaos (Direct Khirki Par Dhakkam-Pehl): Farz karein bank mein ek hi cash counter hai. 500 log aik sath khirki ke aage ghus kar shor machate hain: "Mera paisa pehle nikalo!" Cashier ghabra kar behosh ho jata hai (Server Crash 500 Internal Error).
2. The Token Machine (FastAPI Non-Blocking Gateway): Aqalmand manager darwazay par ek automatic token machine (FastAPI Gateway) laga deta hai. Har aane wale ko 1 millisecond mein ek token number (Job ID: `task_7891`) milta hai: "Aapka token number yeh hai, aaram se sofe par baithiye."
3. The Waiting Lounge (Redis In-Memory Task Queue): Tamam tasks ek orderly qataar (Redis List / Stream) mein lag jate hain. Redis memory mein second ke hazaron tasks ko baghair kisi lag ke hold kar sakta hai.
4. The Dedicated Cashiers (Celery / ARQ Background Workers): Do ya chaar worker processes hain jo aaram se sukoon ke sath qataar se ek ek task uthate hain, LLM se run karate hain, aur result Redis mein save kar dete hain. User ka frontend polling ya Webhook ke zariye apna result utha leta hai. System par chahe 1 lakh requests aa jayein, GPU server par kabhi aanch nahi aati!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Queue Wait Time aur Little's Law ($\ L = \lambda W$) ka exact hisab lagayein.
System Parameters:
- Arrival Rate ($\lambda$): 50 requests per second (RPS) peak traffic.
- Single GPU Worker Processing Time ($T_{\text{service}}$): 0.5 seconds per request.
- Worker Service Capacity per worker: $\mu = \frac{1}{0.5} = 2 \text{ RPS}$.
- Total Active Workers ($K$): 10 parallel GPU worker streams.
- Total System Processing Capacity: $C = K \times \mu = 10 \times 2 = 20 \text{ RPS}$.

Queue Accumulation Math:
Chunke Arrival Rate $\lambda = 50 \text{ RPS}$ Processing Capacity $C = 20 \text{ RPS}$ se zyada hai:
Net Queue Growth Rate:
$\Delta Q = \lambda - C = 50 - 20 = 30 \text{ requests per second}$ jama ho rahi hain!

Agar yeh surge 10 seconds tak jari rahe:
Queue Depth:
$Q_{\text{depth}} = 30 \times 10 = 300 \text{ tasks in Redis queue}$.

Wait Time for the 300th customer:
$W_{\text{wait}} = \frac{Q_{\text{depth}}}{C} = \frac{300}{20} = 15.0 \text{ seconds}$.
FastAPI Gateway user ko foran HTTP 202 Accepted return karta hai:
`{"status": "queued", "estimated_wait_seconds": 15.0}`.
Agar queue na hoti to tamam 300 requests server par aik sath crash kar jatien. Queue ne system ko 100% zinda aur resilient rakha!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum FastAPI asynchronous task enqueueing endpoint, mock in-memory worker queue, aur polling status verification engine implement karte hain.

```python
import asyncio
import time
import uuid
from typing import Dict, Any, Optional
from pydantic import BaseModel

# 1. Schemas for Async Job Contract
class InferenceRequest(BaseModel):
    prompt: str
    temperature: float = 0.7

class JobSubmissionResponse(BaseModel):
    job_id: str
    status: str
    queue_position: int

class JobStatusResponse(BaseModel):
    job_id: str
    status: str
    result: Optional[str] = None
    processing_time_ms: Optional[float] = None

# 2. In-Memory Redis Queue Simulator
class AsyncJobQueue:
    def __init__(self) -> None:
        self.queue: asyncio.Queue[tuple[str, InferenceRequest]] = asyncio.Queue()
        self.results: Dict[str, Dict[str, Any]] = {}

    async def enqueue(self, payload: InferenceRequest) -> tuple[str, int]:
        job_id = f"job_{uuid.uuid4().hex[:8]}"
        self.results[job_id] = {"status": "queued", "result": None, "time_ms": None}
        await self.queue.put((job_id, payload))
        return job_id, self.queue.qsize()

    async def get_status(self, job_id: str) -> Dict[str, Any]:
        return self.results.get(job_id, {"status": "not_found"})

    async def start_worker(self) -> None:
        \"\"\"Background worker popping tasks and executing inference.\"\"\"
        while True:
            job_id, payload = await self.queue.get()
            self.results[job_id]["status"] = "processing"
            t0 = time.perf_counter()

            # Simulate heavy GPU inference
            await asyncio.sleep(0.1)
            output = f"Generated response for: '{payload.prompt}'"

            elapsed_ms = (time.perf_counter() - t0) * 1000.0
            self.results[job_id] = {
                "status": "completed",
                "result": output,
                "time_ms": round(elapsed_ms, 2)
            }
            self.queue.task_done()

# Execution test
if __name__ == "__main__":
    async def simulate_system():
        manager = AsyncJobQueue()
        # Launch background worker
        worker_task = asyncio.create_task(manager.start_worker())

        print("Submitting 3 concurrent inference jobs...")
        j1, q1 = await manager.enqueue(InferenceRequest(prompt="Urdu poetry 1"))
        j2, q2 = await manager.enqueue(InferenceRequest(prompt="Urdu poetry 2"))
        j3, q3 = await manager.enqueue(InferenceRequest(prompt="Urdu poetry 3"))

        print(f"Jobs Enqueued: {j1} (Queue: {q1}), {j2} (Queue: {q2}), {j3} (Queue: {q3})")

        # Poll status after 250ms
        await asyncio.sleep(0.25)
        status_j1 = await manager.get_status(j1)
        status_j2 = await manager.get_status(j2)
        print(f"\\nStatus Check for {j1}: {status_j1}")
        print(f"Status Check for {j2}: {status_j2}")

        worker_task.cancel()

    asyncio.run(simulate_system())
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Blocking the FastAPI Event Loop with Synchronous Inference: FastAPI route ke andar direct `model.generate()` call karna event loop ko freeze kar deta hai jisse naye users ke requests timeout ho jate hain. Heavy inference hamesha alag Celery / ARQ worker process par bhejein.
2. Unbounded Queue Memory Growth: Agar Redis queue mein 10 lakh jobs jama ho jayein aur workers slow hon to Redis OOM crash ho sakta hai. Hamesha maximum queue limit lagayein aur overflow hone par HTTP 429 ya 503 return karein.
3. Polling Thunderstorm (Clients Hammering the Status API): Agar 5,000 clients har 100ms par `/job-status` endpoint par poll karein to database gir jata hai. Hamesha WebSockets ya exponential polling backoff (1s, 2s, 5s) enforce karein.

Zero-GPU Tip:
Async task queues, job UUID generation, aur polling state management 100% CPU aur I/O operations hain. Inhe verify karne ke liye kisi GPU ki zaroorat nahi hai; local terminal par multiple async tasks run karke resilience test karein.

Self-Check Questions:
1. High-concurrency AI systems mein Direct API Calls ke muqablay Task Queue Architecture kyun zaroori hai?
2. HTTP Status Code 202 (Accepted) ka asynchronous processing mein kya kirdaar hota hai?
3. Redis in-memory queue database-backed queue (jaise PostgreSQL table) se kyun tez hoti hai?

What to Build Next:
Ek Celery ya ARQ Redis Worker Pipeline setup karein jo heavy LLM batch jobs ko queue se uthaye, completion par Redis pub/sub par event emit kare, aur failed jobs ko dead-letter queue mein move kare."""

# ==============================================================================
# LESSON 6.4: Semantic Caching with Redis & Vector Similarity
# ==============================================================================
LESSON_CONTENT['6.4'] = r"""### Part 1: Mental Model & South Asian Analogy
Production LLM deployments mein har API call par paise kharch hote hain. Aksar dekha gaya hai ke 30% se 50% user queries taqreeban aik jaisi hoti hain! Agar aap har baar wahi sawal dobara LLM ko bhejte hain to aap lakhoon rupaye ka compute zaaya kar rahe hain.
Isay samajhne ke liye kisi Mashhoor College ke Photocopy wale Chacha ki misaal lein:
1. Exact Match Cache (Purana Tareeqa): Chacha ke paas ek register hai jisme unhone pichle papers ke hal likhe hain. Agar koi bacha aakar kahe: "2024 Physics Paper", to chacha register se nikal kar de dete hain. Lekin agar doosra bacha aakar kahe: "Physics 2024 ka paper", to purana exact cache fail ho jata hai kyunke text ke alfaz aage peeche hain!
2. Semantic Caching (Samajhdaar Chacha): Samajhdaar photocopy wale chacha kehte hain: "Dono bache dar-haqeeqat ek hi cheez maang rahe hain!" Semantic Caching text ke lafzon ko nahi dekhti; woh dono sawalat ka Embedding Vector nikal kar unka Cosine Similarity Angle dekhti hai.
3. The Threshold Gate ($\tau = 0.92$): Agar naye sawal ka vector pichle kisi sawal se 92% se zyada match karta hai, to system LLM ko call hi nahi karta! Woh Redis cache se purana jawab 5 milliseconds mein utha kar user ko de deta hai ($0.00 cost aur 100x speedup).
4. Massive Economic Savings: Agar aapki app rozana 100,000 queries serve karti hai aur 40% queries cache hit ho jayein to aapka monthly LLM bill $10,000 se seedha $6,000 par aa jata hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Semantic Cache Hit vs Cache Miss ka mathematical vector threshold check karein.
Formula:
$\\text{Similarity}(q_{\\text{new}}, k_i) = \\frac{q_{\\text{new}} \\cdot k_i}{\\|q_{\\text{new}}\\| \\times \\|k_i\\|}$
Decision Rule:
$\\text{Max Similarity} \\ge \\tau (0.90) \\implies \\text{Cache HIT (Return cached response)}$
$\\text{Max Similarity} < \\tau (0.90) \\implies \\text{Cache MISS (Call LLM and store result)}$

Cache Database mojud record:
Cached Query: "Karachi mein sab se behtareen biryani kahan milti hai?"
Cached Embedding Vector $K = [0.80, 0.50, 0.20, 0.10]$ (Normalized length $= 0.9695$)
Cached Answer: "Karachi mein Burns Road aur Saddar ki biryani sab se mashhoor hai."

Incoming Query A: "Karachi ki famous biryani ki dukan bataiye."
Embedding Vector $Q_A = [0.78, 0.52, 0.22, 0.08]$ (Normalized length $= 0.9720$)

Step 1: Compute Dot Product
$Q_A \\cdot K = (0.78 \\times 0.80) + (0.52 \\times 0.50) + (0.22 \\times 0.20) + (0.08 \\times 0.10)$
$Q_A \\cdot K = 0.624 + 0.260 + 0.044 + 0.008 = 0.9360$

Step 2: Cosine Similarity
$\\cos(\\theta) = \\frac{0.9360}{0.9695 \\times 0.9720} = \\frac{0.9360}{0.9424} \\approx 0.9932$ (99.32% Match!)
Chunke $0.9932 \\ge 0.90$, yeh **Instant Cache Hit** hai! LLM API call bypass ho gayi aur response 2ms mein serve ho gaya!

Incoming Query B: "Python mein decorators kaise kaam karte hain?"
Embedding Vector $Q_B = [0.05, -0.10, 0.90, 0.35]$
Dot product with $K$:
$Q_B \\cdot K = (0.05 \\times 0.8) + (-0.1 \\times 0.5) + (0.9 \\times 0.2) + (0.35 \\times 0.1) = 0.04 - 0.05 + 0.18 + 0.035 = 0.205$
Cosine Similarity $\\approx 0.21$ (21% Match).
Chunke $0.21 < 0.90$, yeh **Cache Miss** hai. Query LLM ko dispatch hoti hai aur return aane par cache mein add ho jati hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum In-Memory Semantic Vector Cache class, cosine similarity search, aur dynamic threshold gating ko implement karte hain.

```python
import numpy as np
from dataclasses import dataclass
from typing import Optional, Tuple, List

@dataclass(slots=True)
class CachedEntry:
    query_text: str
    embedding: np.ndarray
    response_text: str
    created_at: float

class SemanticCache:
    \"\"\"Production semantic caching layer using vector cosine similarity.\"\"\"
    def __init__(self, similarity_threshold: float = 0.90) -> None:
        self.threshold = similarity_threshold
        self.entries: List[CachedEntry] = []

    @staticmethod
    def _normalize(vec: np.ndarray) -> np.ndarray:
        norm = np.linalg.norm(vec)
        return vec / max(norm, 1e-9)

    def lookup(self, query_embedding: np.ndarray) -> Tuple[bool, Optional[str], float]:
        \"\"\"Scans cache for semantic match above similarity threshold.\"\"\"
        if not self.entries:
            return False, None, 0.0

        q_norm = self._normalize(query_embedding)
        best_sim = -1.0
        best_response = None

        for entry in self.entries:
            # Fast dot product on pre-normalized vectors
            sim = float(np.dot(q_norm, entry.embedding))
            if sim > best_sim:
                best_sim = sim
                best_response = entry.response_text

        if best_sim >= self.threshold:
            return True, best_response, best_sim
        return False, None, best_sim

    def insert(self, query_text: str, query_embedding: np.ndarray, response_text: str) -> None:
        normed_emb = self._normalize(query_embedding)
        self.entries.append(CachedEntry(
            query_text=query_text,
            embedding=normed_emb,
            response_text=response_text,
            created_at=1700000000.0
        ))

# Execution test
if __name__ == "__main__":
    cache = SemanticCache(similarity_threshold=0.88)
    
    # Seed cache with known query
    mock_emb_1 = np.array([0.8, 0.4, 0.1, 0.0], dtype=np.float32)
    cache.insert(
        query_text="Karachi ki biryani kahan achi hai?",
        query_embedding=mock_emb_1,
        response_text="Burns road ki biryani sab se lazeez hai."
    )
    print(f"Cache Initialized with {len(cache.entries)} entries.")

    # Query A: Highly similar semantically
    mock_emb_similar = np.array([0.82, 0.38, 0.09, 0.02], dtype=np.float32)
    hit, resp, score = cache.lookup(mock_emb_similar)
    print(f"Query A Lookup -> Hit: {hit} | Score: {score:.4f} | Response: '{resp}'")

    # Query B: Unrelated query
    mock_emb_unrelated = np.array([0.05, 0.1, 0.95, 0.2], dtype=np.float32)
    hit, resp, score = cache.lookup(mock_emb_unrelated)
    print(f"Query B Lookup -> Hit: {hit} | Score: {score:.4f} | Fallback to LLM needed: {not hit}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Setting Similarity Threshold Too Low ($\tau < 0.85$): Agar threshold 0.70 set kar diya jaye to "Karachi ka mausam kaisa hai?" ka jawab "Lahore ka mausam kaisa hai?" wale sawal ko mil jata hai (False Semantic Collision). Production mein hamesha $\tau \ge 0.90$ rakhein.
2. Caching Dynamic Real-Time Queries: Agar query time-sensitive ho (jaise: "Aaj dollar ka rate kya hai?"), to semantic cache purana rate return karti rehti hai. Time-sensitive queries ko hamesha cache-bypass flag dein.
3. Linearly Scanning 10 Million Vectors in Memory: Cache entries barhne par linear scan slow ho jata hai. Production mein Redis Vector Similarity Search (RediSearch) ya HNSW indexing use karein.

Zero-GPU Tip:
Semantic cache lookup pure vector dot product math hai. 5,000 cached queries ka scan CPU par 1 millisecond se kam waqt leta hai aur hazaron dollars ki GPU API cost bachata hai.

Self-Check Questions:
1. Exact keyword match cache aur Semantic vector cache mein kya farq hota hai?
2. Semantic similarity threshold ($\tau$) barhane ya ghatanay se Precision aur Recall par kya asar parta hai?
3. Redis VSS (Vector Similarity Search) semantic cache ko scaling mein kaise madad deti hai?

What to Build Next:
Ek Redis-Backed Semantic Cache pipeline banayein jo Redis hashes mein vectors store kare, cosine distance query execute kare, aur cache hit ratio aur dollar savings metrics dashboard display kare."""

# ==============================================================================
# LESSON 6.5: Real-Time Bidirectional AI Streams with WebSockets
# ==============================================================================
LESSON_CONTENT['6.5'] = r"""### Part 1: Mental Model & South Asian Analogy
Server-Sent Events (SSE) sirf ek taraf se data bhejti hai (Server to Client). Lekin agar aapko aisi interactive application banani ho jahan user bol bhi raha ho aur model sath sath sun kar jawab bhi de raha ho (jaise real-time audio chat ya interruptible agents), to **WebSockets** lazmi ho jati hain!
Isay samajhne ke liye kisi Wireless Walkie-Talkie vs Telephonic Full-Duplex Call ki misaal lein:
1. HTTP / SSE (Walkie-Talkie / One-Way Megaphone): Ek banda bolta hai "Over", phir doosra bolta hai. Agar server bol raha ho to client beech mein aawaz nahi daal sakta jab tak naya HTTP connection na kholay.
2. WebSockets (Live Telephonic Line / Full-Duplex): WebSockets mein client aur server ke darmiyan ek persistent, do-tarfa (Bi-directional) pipe khul jata hai. Dono aapas mein aik hi waqt mein baat kar sakte hain.
3. User Interruption (Barging In / Baat Kaatna): Farz karein AI model lamba jawab de raha hai: "1947 mein jab Pakistan bana to..." User achanak beech mein kehta hai: "Ruko! Mujhe 1947 ki nahi 1965 ki baat sunao!" WebSockets ke zariye client usi waqt cancel packet bhejta hai. Server foran bolna band karta hai aur foran naye sawal par switch ho jata hai! Yeh capability real-time voice assistants (jaise Gemini Live ya OpenAI Advanced Voice) ka markaz hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein WebSocket Framing Overhead vs HTTP Header Overhead ka hisab lagayein.
Farz karein hum har 50 milliseconds par user ke microphone ka audio chunk (64 bytes raw PCM data) server ko bhej rahe hain.
Stream Duration = 1 minute (60 seconds) $= 1200 \text{ chunks}$.

Scenario A: Standard HTTP POST Requests for each chunk
Har HTTP/1.1 request ke sath headers jate hain:
`Host, User-Agent, Cookie, Authorization, Content-Type...` $\approx 800 \text{ Bytes}$ per request!
Payload = 64 Bytes.
Total Data Sent per Chunk: $800 + 64 = 864 \text{ Bytes}$.
Total Network Bandwidth for 1 Minute:
$1200 \times 864 \text{ Bytes} \approx 1,036,800 \text{ Bytes} \approx 1.04 \text{ MB}$.
Bandwidth Efficiency: $\frac{64}{864} \approx 7.4\%$ (92.6% bandwidth sirf HTTP headers zaaya kar rahe hain!).

Scenario B: Persistent WebSocket Connection
Handshake sirf shuru mein ek baar hota hai. Uske baad har WebSocket frame ka header sirf **2 se 6 Bytes** ka hota hai!
Average frame header = 4 Bytes.
Total Data Sent per Chunk: $4 + 64 = 68 \text{ Bytes}$.
Total Network Bandwidth for 1 Minute:
$1200 \times 68 \text{ Bytes} \approx 81,600 \text{ Bytes} \approx 81.6 \text{ KB}$!
Bandwidth Efficiency: $\frac{64}{68} \approx 94.1\%$!
WebSockets ne network overhead ko $1.04\text{ MB}$ se gira kar sirf $81.6\text{ KB}$ kar diya ($12.7\times \text{ Network Reduction}$)!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum FastAPI WebSockets bidirectional server, message framing protocol, cancellation signal handling, aur client echo loop implement karte hain.

```python
import asyncio
import json
import time
from typing import Dict, Any

class MockWebSocketClient:
    \"\"\"Simulates bidirectional WebSocket client send/receive queues.\"\"\"
    def __init__(self) -> None:
        self.server_to_client: asyncio.Queue[str] = asyncio.Queue()
        self.client_to_server: asyncio.Queue[str] = asyncio.Queue()

    async def send_to_server(self, msg: Dict[str, Any]) -> None:
        await self.client_to_server.put(json.dumps(msg))

    async def receive_from_server(self) -> Dict[str, Any]:
        raw = await self.server_to_client.get()
        return json.loads(raw)

async def websocket_ai_session_handler(client_socket: MockWebSocketClient) -> None:
    \"\"\"Handles full-duplex session with real-time user barge-in cancellation.\"\"\"
    current_generation_task: asyncio.Task | None = None

    async def stream_ai_generation(query: str):
        tokens = ["AI", "Ustaad", "Real-Time", "Bidirectional", "Audio", "Engine", "Active"]
        for t in tokens:
            await asyncio.sleep(0.08)
            await client_socket.server_to_client.put(json.dumps({"type": "token", "payload": t}))
        await client_socket.server_to_client.put(json.dumps({"type": "complete"}))

    while True:
        try:
            # Wait for incoming client frame
            raw_msg = await client_socket.client_to_server.get()
            data = json.loads(raw_msg)
            msg_type = data.get("type")

            if msg_type == "query":
                # Cancel previous generation if user barged in
                if current_generation_task and not current_generation_task.done():
                    print("[Server] User interruption detected! Cancelling ongoing generation...")
                    current_generation_task.cancel()
                    await client_socket.server_to_client.put(json.dumps({"type": "interrupted"}))

                current_generation_task = asyncio.create_task(stream_ai_generation(data["payload"]))

            elif msg_type == "cancel":
                if current_generation_task:
                    current_generation_task.cancel()
                    await client_socket.server_to_client.put(json.dumps({"type": "cancelled"}))

            elif msg_type == "close":
                break

        except asyncio.CancelledError:
            break

# Execution test
if __name__ == "__main__":
    async def run_test():
        ws = MockWebSocketClient()
        server_coro = asyncio.create_task(websocket_ai_session_handler(ws))

        # 1. User sends first query
        print("Client: Sending Query 1...")
        await ws.send_to_server({"type": "query", "payload": "Pehla lamba jawab batao"})

        # Read first 2 tokens
        print("Client Received:", await ws.receive_from_server())
        print("Client Received:", await ws.receive_from_server())

        # 2. User barges in with Query 2
        print("\\nClient: User Interrupts with Query 2!")
        await ws.send_to_server({"type": "query", "payload": "Ruko! Naya sawal"})

        # Check interruption signal and new tokens
        print("Client Received:", await ws.receive_from_server())  # Interrupted event
        print("Client Received:", await ws.receive_from_server())  # New token

        # Close
        await ws.send_to_server({"type": "close"})
        server_coro.cancel()

    asyncio.run(run_test())
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Not Handling Broken Socket Connections: Internet disconnect hone par agar server socket write try kare to `ConnectionResetError` aata hai. Hamesha `try/except WebSocketDisconnect` block se socket teardown karein.
2. Memory Leaks from Hanging Generation Tasks: User disconnect hone par agar running async task ko cancel na kiya jaye to CPU/GPU background mein tokens generate karta rehta hai. Disconnect hook par running task ko hamesha `.cancel()` karein.
3. Sending Uncompressed Raw Audio Frames: Audio data ko raw PCM mein bhejne ke bajaye Opus codec se compress karke bhejna chahiye, warna client ka mobile data foran khatam ho jata hai.

Zero-GPU Tip:
WebSocket protocol testing, frame serialization, aur client cancellation logic pure async Python par bina kisi GPU ke chalti hai. Local automated tests mein user interruption edge cases verify karein.

Self-Check Questions:
1. WebSockets ka framing overhead HTTP/1.1 ke muqablay kyun bohot kam hota hai?
2. Real-time conversational AI mein 'Barge-In / User Interruption' kaise handle kiya jata hai?
3. WebSocket disconnect hone par server par chal rahe AI generation task ka kya karna chahiye?

What to Build Next:
Ek Full-Duplex FastAPI WebSocket Chat Server banayein jo browser microphone se base64 audio chunks receive kare, simulated audio tokens stream kare, aur user interruption par generation cancel kare."""

# ==============================================================================
# LESSON 6.6: Module 6 Capstone: Enterprise Resilient Streaming AI Gateway
# ==============================================================================
LESSON_CONTENT['6.6'] = r"""### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne Module 6 ke tamam ahem sutoon (Server-Sent Events streaming, Full-stack state management, Redis task queues, Semantic caching, aur WebSockets) mukammal kar liye hain. Ab waqt hai ek **Enterprise-Grade Resilient AI Gateway Service** develop karne ka!
Is Capstone project ka zehni khaka kisi Bare International Airport ke Flight Control Tower aur Security Terminal jaisa hai:
1. Incoming Traffic Controller (The AI Gateway): Hazaron requests aati hain. Gateway unhe evaluate karta hai: rate-limits check karta hai, authentication verify karta hai, aur payload sanitize karta hai.
2. The Fast-Track Lounge (Semantic Cache): Agar bilkul wahi sawal pichle 1 ghantay mein poocha ja chuka ho, to request foran cache se 5ms mein return ho jati hai bina kisi cloud provider ko call kiye.
3. The Intelligent Load Balancer (Circuit Breakers & Fallback): Agar primary LLM provider (jaise Groq ya OpenAI) down ho jaye ya 503 error phenkay, to Gateway user ko error nahi dikhata; balki microsecond mein secondary provider (jaise Google Gemini ya local vLLM) par traffic divert kar deta hai (Automatic Failover).
4. Real-Time Telemetry & Token Meter: Har request ki latency, token count, aur dollar cost live dashboard par stream hoti hai.

Yeh architecture modern production AI platforms ka backbone hai jo 99.99% uptime guarantee karta hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein High Availability aur Cost Optimization ka mathematical impact trace karte hain.
Parameters:
- Daily Incoming Traffic $N = 200,000$ requests
- Primary Provider (Groq Cloud): Fast & cheap (\$0.20 per 1M tokens), Uptime = 99.0%
- Secondary Provider (OpenAI/Anthropic): Expensive fallback (\$2.50 per 1M tokens), Uptime = 99.99%
- Average prompt + completion tokens = 500 tokens per request
- Semantic Cache Hit Ratio = 35%

Step 1: Traffic Breakdown
- Cache Hits (35%): $200,000 \times 0.35 = 70,000$ requests served at **\$0.00**!
- Remaining Cache Misses (65%): $200,000 \times 0.65 = 130,000$ requests need LLM inference.

Step 2: Provider Availability & Failover Routing
Primary provider is up 99% of the time:
- Sent to Primary: $130,000 \times 0.99 = 128,700$ requests.
- Failed / Timed out on Primary (1%): $130,000 \times 0.01 = 1,300$ requests.
- Routed to Secondary Fallback: All 1,300 requests automatically saved by Gateway!
Overall User Perceived Uptime: $100.0\%$ (Zero user-facing 500 errors)!

Step 3: Daily Cost Calculation
- Primary Provider Cost: $\frac{128,700 \times 500}{1,000,000} \times \$0.20 = 64.35 \times \$0.20 = \$12.87$
- Secondary Fallback Cost: $\frac{1,300 \times 500}{1,000,000} \times \$2.50 = 0.65 \times \$2.50 = \$1.63$
- Cache Savings: Without cache, all 200k requests would cost $\$20.00$.
Total Daily Spend: $\$12.87 + \$1.63 = \$14.50$ (Saved over 30% while achieving 100% resilience)!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete Resilient AI Gateway implement karte hain: semantic cache check, primary provider execution with timeout, automatic circuit-breaker fallback to secondary provider, aur audit telemetry.

```python
import time
import asyncio
from typing import Dict, Any, Optional
from pydantic import BaseModel

class GatewayRequest(BaseModel):
    user_id: str
    prompt: str
    stream: bool = False

class GatewayResponse(BaseModel):
    response_text: str
    served_by: str  # "cache", "primary_provider", or "fallback_provider"
    latency_ms: float
    token_count: int

class ResilientAIGateway:
    \"\"\"Production multi-provider resilient AI gateway with fallback routing.\"\"\"
    def __init__(self) -> None:
        # Mock semantic cache
        self.cache: Dict[str, str] = {
            "what is ai ustaad?": "AI Ustaad is Pakistan's premier AI engineering platform."
        }

    async def _call_primary_provider(self, prompt: str) -> str:
        \"\"\"Simulates primary low-latency LLM endpoint (e.g. Groq Llama 3.3).\"\"\"
        await asyncio.sleep(0.08)
        # Simulate occasional provider outage on specific trigger
        if "force_fail" in prompt:
            raise ConnectionError("Primary provider 503 Service Unavailable")
        return f"[Primary Groq] Completed: {prompt}"

    async def _call_fallback_provider(self, prompt: str) -> str:
        \"\"\"Simulates reliable fallback endpoint (e.g. Anthropic Claude / OpenAI).\"\"\"
        await asyncio.sleep(0.15)
        return f"[Fallback Anthropic] Completed: {prompt}"

    async def dispatch(self, request: GatewayRequest) -> GatewayResponse:
        t0 = time.perf_counter()
        clean_query = request.prompt.strip().lower()

        # Step 1: Semantic Cache Check
        if clean_query in self.cache:
            elapsed_ms = (time.perf_counter() - t0) * 1000.0
            return GatewayResponse(
                response_text=self.cache[clean_query],
                served_by="cache",
                latency_ms=round(elapsed_ms, 2),
                token_count=len(self.cache[clean_query].split()) * 2
            )

        # Step 2: Attempt Primary Provider with strict timeout
        try:
            # 200ms strict SLA timeout
            response_text = await asyncio.wait_for(
                self._call_primary_provider(request.prompt), 
                timeout=0.20
            )
            served_by = "primary_provider"
        except (ConnectionError, asyncio.TimeoutError) as err:
            # Step 3: Automatic Circuit-Breaker Fallback Routing
            print(f"[Gateway Alert] Primary failed ({err}). Routing to Fallback Provider...")
            response_text = await self._call_fallback_provider(request.prompt)
            served_by = "fallback_provider"

        elapsed_ms = (time.perf_counter() - t0) * 1000.0
        return GatewayResponse(
            response_text=response_text,
            served_by=served_by,
            latency_ms=round(elapsed_ms, 2),
            token_count=len(response_text.split()) * 2
        )

# Execution test
if __name__ == "__main__":
    async def run_gateway_suite():
        gateway = ResilientAIGateway()

        # Test Case 1: Cache Hit
        req1 = GatewayRequest(user_id="u1", prompt="What is AI Ustaad?")
        res1 = await gateway.dispatch(req1)
        print(f"Test 1 (Cache):    Served by {res1.served_by} in {res1.latency_ms} ms -> '{res1.response_text}'")

        # Test Case 2: Primary Provider Normal
        req2 = GatewayRequest(user_id="u2", prompt="Write a quick Python sort function.")
        res2 = await gateway.dispatch(req2)
        print(f"Test 2 (Primary):  Served by {res2.served_by} in {res2.latency_ms} ms")

        # Test Case 3: Primary Failure with Automatic Fallback
        req3 = GatewayRequest(user_id="u3", prompt="Calculate system metrics force_fail")
        res3 = await gateway.dispatch(req3)
        print(f"Test 3 (Fallback): Served by {res3.served_by} in {res3.latency_ms} ms -> '{res3.response_text}'")

    asyncio.run(run_gateway_suite())
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Retrying on Primary Without Exponential Backoff When Down: Agar primary provider 500 error de raha ho aur gateway lagataar 1,000 retries bhej de to provider ka server aur shadeed jam ho jata hai. Circuit Breaker lagana zaroori hai jo 5 consecutive errors par primary ko 30 seconds ke liye direct skip kar de.
2. Unbounded Timeout on Primary Calls: Agar primary provider par timeout na lagaya jaye to client 60 second tak latka rehta hai. Hamesha aggressive timeout (e.g. 500ms se 1s) lagayein taake fallback foran trigger ho sake.
3. Leaking Provider API Keys to Client: API Gateway ka bunyadi maqsad yeh hai ke secret LLM API keys server par mehfooz rahein aur client ko sirf authenticated JWT token mile.

Zero-GPU Tip:
AI Gateway routing, circuit breaker logic, aur semantic cache fallbacks 100% CPU par chalte hain. Inhe verify karne ke liye kisi GPU ki zaroorat nahi hai. Local async simulation se 99.99% reliability SLAs test kiye ja sakte hain.

Self-Check Questions:
1. Circuit Breaker Pattern kya hota hai aur yeh AI Gateway ko cascading failures se kaise bachata hai?
2. Multi-provider fallback architecture company ke business continuity aur SLA ko kaise guarantee karti hai?
3. Semantic caching aur failover routing mil kar monthly cloud bill ko kaise kam karti hain?

What to Build Next:
Is Gateway ko ek complete Dockerized FastAPI service banayein with Redis semantic caching, Prometheus metrics endpoint (`/metrics` for latency and error rates), aur multi-tenant API key rate limiting."""
