# seed_modules_phase1_2.py
# Modules 1 to 5: Foundations, Prompt Engineering, Classical ML, PyTorch, Attention & Transformers
# Total 30 comprehensive lessons (6 lessons per module: 1.1-1.6, 2.1-2.6, 3.1-3.6, 4.1-4.6, 5.1-5.6)

def get_modules_phase1_2():
    modules = [
        # =========================================================================
        # MODULE 1: Python for AI & Fast Math (NumPy, Linear Algebra)
        # =========================================================================
        {
            "phase_slug": "phase-1-foundations",
            "module_number": 1,
            "slug": "python-for-ai-and-fast-math",
            "real_world_deliverable": "500k E-Commerce Order Sanitizer & Parquet Data Pipeline",
            "zero_gpu_recipe": {
                'platform': 'Local CPU / Google Colab Free Tier',
                'vram_required': '0 GB (CPU)',
                'estimated_cost': '$0.00 Free',
                'compute_units_tip': 'NumPy AVX-512 vectorization runs blazing fast on standard Colab CPU without burning any GPU compute units.',
                'one_click_command': 'python -m pip install numpy polars pyarrow pydantic && python main.py'
            },
            "title": "Module 1: Python for AI & Fast Math (NumPy, Linear Algebra)",
            "weeks_range": "Weeks 1-2",
            "estimated_hours": 14,
            "learning_outcomes": [
                "Python lists vs contiguous C-aligned NumPy memory layout ka farq",
                "High-performance vectorized operations aur SIMD parallelism",
                "Vector spaces, Dot products, projections aur Cosine similarity",
                "Calculus fundamentals: Gradients, partial derivatives, aur Loss surfaces",
                "Python 3.12 GIL, memory profiling, and AsyncIO event loops for AI pipelines",
                "High-throughput tabular wrangling with Polars & Apache Arrow"
            ],
            "practical_tasks": [
                "Pure Python nested loop ko NumPy vectorized broadcasting mein convert karein",
                "Cosine similarity function zero external libraries ke sath implement karein",
                "Gradient descent optimization loop for linear regression likhein",
                "tracemalloc aur AsyncIO se parallel batch LLM requests profile karein",
                "500k record dataset ko Polars lazy streaming pipeline se sanitize karein"
            ],
            "resources": [
                {"title": "NumPy Illustrated Guide", "url": "https://numpy.org/doc/stable/"},
                {"title": "3Blue1Brown Linear Algebra Series", "url": "https://www.3blue1brown.com/topics/linear-algebra"},
                {"title": "Polars Official User Guide", "url": "https://docs.pola.rs/"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 1 Fast Math & Vector Pipeline
  py_list[Python List Overhead] $code -> numpy_arr[Contiguous C NumPy Array] $cpu
  numpy_arr -> simd[SIMD Vectorized Dot Product] $terminal
  simd -> loss[Loss Surface & Gradient Descent] $brain *""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "pehla-prompt",
            "order_index": 1,
            "lessons": [
                {
                    "lesson_code": "1.1",
                    "slug": "python-vectors-tensors",
                    "title": "Python Data Structures Se NumPy Tensors Tak",
                    "duration_minutes": 25,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, aaj hum AI Engineering ka sab se pehla aur ahem qadam utha rahe hain! Aksar log samajhte hain ke AI koi jaadu hai, lekin dar-haqeeqat modern AI model ek bohot bara mathematical function hai jo numbers (Tensors) input leta hai aur numbers return karta hai.

Python mein standard `list` dynamic hoti hai — iska matlab yeh hai ke memory mein har element ka pointer alag jagah store hota hai (pointer chasing). Jab aap 1 million numbers par Python ka `for` loop chalate hain to CPU cache misses ki wajah se program bohot slow ho jata hai.

Iske bar-aks **NumPy Arrays** C-contiguous memory blocks use karte hain. Iska faida yeh hota hai ke modern CPUs ke SIMD (Single Instruction Multiple Data) registers ek hi clock cycle mein 4 se 8 numbers ko parallel process kar sakte hain! Yeh wahi concept hai jo aage chal kar GPU acceleration ka bunyadi pillar banta hai.""",
                    "english_summary": "Understand CPU memory locality, cache hierarchy, and why NumPy vectorized operations deliver 50x-100x speedups over pure Python loops.",
                    "code_example": """import time
import numpy as np

# 1. Pure Python Loop
size = 5_000_000
list_a = list(range(size))
list_b = list(range(size))

start = time.perf_counter()
py_result = [a * b for a, b in zip(list_a, list_b)]
py_time = time.perf_counter() - start

# 2. NumPy Vectorized Operation (SIMD)
np_a = np.arange(size, dtype=np.float32)
np_b = np.arange(size, dtype=np.float32)

start = time.perf_counter()
np_result = np_a * np_b
np_time = time.perf_counter() - start

print(f"Python Loop Time: {py_time:.4f}s")
print(f"NumPy Vector Time: {np_time:.4f}s")
print(f"Speedup: {py_time / np_time:.1f}x tez!")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Vectorized Memory Layout
  mem_py[Python List: Scattered Pointers] $code -> cpu[CPU Cache Misses] $server
  mem_np[NumPy: Contiguous 32-bit Float Block] $database -> simd[CPU SIMD 8-lane Parallel] $cpu *""",
                    "diagram_type": "flow",
                    "resources": [{"title": "NumPy Array Memory Layout", "url": "https://numpy.org/doc/stable/reference/arrays.ndarray.html"}],
                    "xp_reward": 15,
                    "order_index": 1
                },
                {
                    "lesson_code": "1.2",
                    "slug": "linear-algebra-intuition",
                    "title": "Linear Algebra Intuition: Dot Products, Projections & Embeddings",
                    "duration_minutes": 30,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab hum kisi word ya document ko AI ke hawaley karte hain, to computer text ko direct nahi samajhta. Hum har word ya text chunk ko ek **High-Dimensional Vector (Embedding)** mein convert karte hain (jaise 1536 ya 3072 numbers ka vector).

Lekin do vectors kitne similar hain yeh kaise pata chale ga? Yahan kaam aata hai **Dot Product** aur **Cosine Similarity**!
Dot product ka geometrical formula hai:
$u \\cdot v = |u| |v| \\cos(\\theta)$

Agar dono vectors ek hi direction mein point kar rahe hain to $\\cos(0) = 1$ (100% semantic similarity). Agar dono aapas mein perpendicular (90 degrees) hain to $\\cos(90) = 0$ (koi similarity nahi). Yahi formula poori RAG (Retrieval-Augmented Generation) aur Vector Search ki bunyad hai!""",
                    "english_summary": "Explore geometric intuition of vector spaces, dot products, projections, and cosine similarity underlying vector search and RAG.",
                    "code_example": """import numpy as np

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    # u . v / (||u|| * ||v||)
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
    return float(dot_product / (norm_v1 * norm_v2))

# Real Embedding Simulation
king = np.array([0.91, 0.12, 0.85], dtype=np.float32)
queen = np.array([0.89, 0.15, 0.82], dtype=np.float32)
apple = np.array([0.11, 0.95, -0.42], dtype=np.float32)

print(f"Similarity (King, Queen): {cosine_similarity(king, queen):.4f}") # High
print(f"Similarity (King, Apple): {cosine_similarity(king, apple):.4f}") # Low""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Embedding Vector Angle
  vec_a[Vector A: King] $terminal -> dot[Dot Product u . v] $brain
  vec_b[Vector B: Queen] $terminal -> dot
  dot -> norm[Norm Normalization ||u|| ||v||] $layers
  norm -> sim[Cosine Similarity: 0.98 Close] $chart *""",
                    "diagram_type": "arch",
                    "resources": [{"title": "Cosine Similarity Mathematics", "url": "https://en.wikipedia.org/wiki/Cosine_similarity"}],
                    "xp_reward": 20,
                    "order_index": 2
                },
                {
                    "lesson_code": "1.3",
                    "slug": "calculus-gradient-descent",
                    "title": "Calculus & Gradient Descent: Cost Function Ko Zero Karna",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, ab sawal yeh paida hota hai ke AI Model "Seekhta" kaise hai?
Jawab hai: **Calculus aur Gradient Descent**!

Har neural network mein lakhoon ya arabon parameters hote hain (weights aur biases). Shuru mein yeh weights bilkul random hote hain, to model ghalat predictions deta hai. Hum ek **Loss Function** (jaise Mean Squared Error ya Cross Entropy) calculate karte hain jo batata hai ke model kitni bari ghalti kar raha hai.

Gradient dar-haqeeqat multi-variable derivative hota hai:
$\\nabla L = \\left[ \\frac{\\partial L}{\\partial w_1}, \\frac{\\partial L}{\\partial w_2}, \\dots \\right]$
Yeh vector batata hai ke "kis direction mein chalne se loss sab se tez barhega".
Is liye hum loss kam karne ke liye gradient ke **opposite (negative)** direction mein chalte hain:
$w = w - \\eta \\cdot \\nabla L$
Jahan $\\eta$ (eta) learning rate hai!""",
                    "english_summary": "Understand multivariable calculus, partial derivatives, loss surfaces, and parameter updates via gradient descent.",
                    "code_example": """import numpy as np

# Synthetic Dataset: y = 3x + 2 + noise
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1) * 0.1

# Initialize Weight and Bias randomly
w = np.random.randn(1, 1)
b = np.zeros((1, 1))
learning_rate = 0.05
epochs = 200

# Training Loop: Gradient Descent from scratch
for epoch in range(epochs):
    # 1. Forward Pass: y_hat = Xw + b
    y_pred = X.dot(w) + b
    loss = np.mean((y_pred - y) ** 2)
    
    # 2. Compute Gradients: dL/dw and dL/db
    N = len(X)
    dw = (2 / N) * X.T.dot(y_pred - y)
    db = (2 / N) * np.sum(y_pred - y)
    
    # 3. Update Parameters
    w -= learning_rate * dw
    b -= learning_rate * db
    
    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch+1:03d} | Loss: {loss:.4f} | w: {w[0,0]:.3f} | b: {b[0,0]:.3f}")

print(f"Final Learned Equation: y = {w[0,0]:.2f}x + {b[0,0]:.2f} (Target was ~ 3.00x + 4.00)")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Gradient Descent Step
  weights[Current Weights w] $database -> fwd[Forward Prediction Xw + b] $cpu
  fwd -> loss[Loss Surface L(w)] $chart
  loss -> grad[Gradient dL/dw] $brain
  grad -> update[Weight Update: w - eta*grad] $terminal *
  update -> weights""",
                    "diagram_type": "flow",
                    "resources": [{"title": "Calculus for Deep Learning", "url": "https://ml-cheatsheet.readthedocs.io/en/latest/gradient_descent.html"}],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "1.4",
                    "slug": "memory-profiling-gil-async",
                    "title": "Python 3.12 GIL, Memory Profiling & AsyncIO for AI Pipelines",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab hum production AI applications banate hain, to sab se bara bottleneck Python ka **GIL (Global Interpreter Lock)** aur memory leaks bante hain!

Aksar log sochte hain ke Python mein multi-threading se sab kuch fast ho jayega, lekin CPU-bound tasks (jaise tensor math) mein GIL sirf ek CPU core use karne deta hai. Jabke I/O-bound tasks (jaise remote LLM API calls, vector search queries, document streaming) ke liye **AsyncIO** sab se best solution hai. Ek single async event loop par aap thousands of concurrent LLM streams serve kar sakte hain!

Sath hi, Python 3.12 mein strict typing aur `@dataclass(slots=True)` use karne se memory 20% kam use hoti hai kyunke Python per-instance `__dict__` allocate nahi karta, balke C-struct jaisa fixed memory block banata hai. Is lesson mein hum `tracemalloc` se memory profiling aur `asyncio.gather` se concurrent streaming master karenge.""",
                    "english_summary": "Master Python GIL constraints, memory profiling with tracemalloc, dataclass slots memory savings, and AsyncIO event loops for high-throughput AI API calls.",
                    "code_example": """import asyncio
import tracemalloc
import time
from dataclasses import dataclass

@dataclass(slots=True)
class PromptTask:
    task_id: int
    prompt: str
    temperature: float

async def simulate_llm_stream(task: PromptTask) -> dict:
    await asyncio.sleep(0.05)
    return {
        "task_id": task.task_id,
        "tokens": len(task.prompt.split()) * 4,
        "status": "completed"
    }

async def run_batch():
    tracemalloc.start()
    tasks = [PromptTask(i, f"Roman Urdu AI prompt number {i}", 0.7) for i in range(500)]
    
    start_time = time.perf_counter()
    results = await asyncio.gather(*(simulate_llm_stream(t) for t in tasks))
    elapsed = time.perf_counter() - start_time
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Processed {len(results)} LLM calls in {elapsed:.3f}s via AsyncIO!")
    print(f"Peak RAM used: {peak / 1024:.2f} KB (slots=True efficiency)")

asyncio.run(run_batch())""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: AsyncIO High-Concurrency LLM Streamer
  event_loop[AsyncIO Single Event Loop] $server -> req1[Async LLM Stream 1] $cloud
  event_loop -> req2[Async LLM Stream 2] $cloud
  event_loop -> req3[Async LLM Stream 3] $cloud
  req1 -> collector[Token Accumulator] $database
  req2 -> collector
  req3 -> collector *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Python AsyncIO Documentation", "url": "https://docs.python.org/3/library/asyncio.html"},
                        {"title": "Python Dataclasses Slots", "url": "https://docs.python.org/3/library/dataclasses.html"}
                    ],
                    "xp_reward": 25,
                    "order_index": 4
                },
                {
                    "lesson_code": "1.5",
                    "slug": "polars-arrow-data-wrangling",
                    "title": "High-Performance Data Wrangling with Polars & Apache Arrow",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, classical AI tutorials mein sab Pandas sikhate hain, lekin 2026 production AI pipelines mein Pandas outdated ho chuka hai! Pandas single-threaded hai aur har operation par data ki nayi copy banata hai (RAM explosion).

Modern standard hai **Polars** jo Rust mein likha gaya hai aur **Apache Arrow** columnar memory format par chalta hai. Polars ke 3 baray faiday hain:
1. **Multi-threaded Execution**: CPU ke tamam cores ko parallel use karta hai.
2. **Lazy Evaluation (`lazy()`)**: Aapke filters aur transformations ko pehle analyze karke optimal query execution plan banata hai (Predicate Pushdown).
3. **Zero-Copy Arrow Memory**: Parquet files ko direct RAM mein stream karta hai bina kisi overhead ke.""",
                    "english_summary": "Leverage Polars and Apache Arrow for zero-copy memory layouts, multi-threaded SIMD parallel query execution, and streaming data pipelines.",
                    "code_example": """import polars as pl
import numpy as np

# Create synthetic 100k e-commerce records
n_records = 100_000
df = pl.DataFrame({
    "order_id": np.arange(n_records),
    "customer_region": np.random.choice(["Karachi", "Lahore", "Islamabad", "Peshawar"], n_records),
    "order_amount": np.random.uniform(500, 15000, n_records),
    "is_returned": np.random.choice([True, False], n_records, p=[0.12, 0.88])
})

query = (
    df.lazy()
    .filter(pl.col("is_returned") == False)
    .group_by("customer_region")
    .agg([
        pl.count().alias("total_delivered_orders"),
        pl.col("order_amount").sum().round(2).alias("total_revenue"),
        pl.col("order_amount").mean().round(2).alias("avg_order_value")
    ])
    .sort("total_revenue", descending=True)
)

result = query.collect()
print("Polars Aggregation Results:")
print(result)""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Polars Apache Arrow Columnar Engine
  raw[Raw Parquet Ingestion] $database -> arrow[Apache Arrow Columnar Layout] $cube
  arrow -> rust_engine[Rust Multi-Threaded Query Optimizer] $cpu *
  rust_engine -> pred[Predicate Pushdown & SIMD Filtering] $layers
  pred -> out[Sanitized Clean Batch] $terminal""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "Polars Documentation", "url": "https://docs.pola.rs/"},
                        {"title": "Apache Arrow Specification", "url": "https://arrow.apache.org/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "1.6",
                    "slug": "module-1-capstone-ingestion",
                    "title": "Module 1 Capstone: 500k Record Enterprise Ingestion & Sanitization Engine",
                    "duration_minutes": 50,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, mubarak ho! Aapne Module 1 ke tamam foundational concepts (NumPy, Linear Algebra, Calculus, Memory Profiling aur Polars) mukammal kar liye hain. Ab waqt hai aapke **Pehle Real-World Production Capstone** ka!

Is capstone mein aap ek end-to-end Enterprise Ingestion Pipeline implement karenge jo 500,000 raw customer feedback comments ko stream karegi:
1. Dirty text sanitization (HTML removal, unicode normalization, Urdu/English mixed character cleaning).
2. Data validation with strict typed schema.
3. Fast token length distribution calculation via Polars.
4. Exporting to partitioned Parquet chunks jo aglay modules mein Embedding generation ke liye 100% ready honge!""",
                    "english_summary": "Build an end-to-end multi-threaded data ingestion and sanitization pipeline processing 500k records into embedding-ready Parquet partitions.",
                    "code_example": """import polars as pl
import re

def clean_urdu_english_text(raw_text: str) -> str:
    clean = re.sub(r'<.*?>', '', raw_text)
    clean = re.sub(r'http\\S+', '', clean)
    clean = re.sub(r'\\s+', ' ', clean).strip()
    return clean

raw_batch = pl.DataFrame({
    "id": [101, 102, 103, 104],
    "comment": [
        "<b>Bohot zabardast product hai!</b> 100% recommend: https://shop.com/p1",
        "Delivery bohot late thi... <br> lekin customer support accha tha.",
        "Quality bilkul bakwas hai, refund chahiye!",
        "AI course ne meri coding style transform kar di! Highly recommended."
    ]
})

sanitized_batch = raw_batch.with_columns(
    pl.col("comment").map_elements(clean_urdu_english_text, return_dtype=pl.Utf8).alias("clean_comment")
).with_columns(
    pl.col("clean_comment").str.len_chars().alias("char_count")
)

print("Capstone Sanitized Data:")
print(sanitized_batch)""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Enterprise Ingestion Pipeline
  raw[Raw Webhook Stream (500k Records)] $cloud -> validator[Pydantic Type Validator] $code
  validator -> polars_sink[Polars Streaming Sink] $database
  polars_sink -> parquet_store[Embedding-Ready Parquet Chunks] $server *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Data Pipeline Best Practices", "url": "https://docs.pola.rs/user-guide/concepts/streaming/"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        },

        # =========================================================================
        # MODULE 2: Prompt Engineering & LLM Mental Models
        # =========================================================================
        {
            "phase_slug": "phase-1-foundations",
            "module_number": 2,
            "slug": "prompt-engineering-and-llm-mental-models",
            "real_world_deliverable": "Multi-Step Medical Triage Prompt Pipeline with JSON Schemas",
            "zero_gpu_recipe": {
                'platform': 'Groq Cloud / Google AI Studio Free Tier',
                'vram_required': '0 GB (API-Based)',
                'estimated_cost': '$0.00 Free Tier',
                'compute_units_tip': 'Groq Cloud free tier provides 30 req/min for LLaMA-3.3-70B; Gemini 2.0 Flash provides 1,500 req/day with zero credit card.',
                'one_click_command': 'curl https://api.groq.com/openai/v1/models -H "Authorization: Bearer $GROQ_API_KEY"'
            },
            "title": "Module 2: Prompt Engineering & LLM Mental Models",
            "weeks_range": "Weeks 3-4",
            "estimated_hours": 12,
            "learning_outcomes": [
                "Next-Token Prediction mechanism aur Sampling parameters (Temperature, Top-P, Repetition Penalty)",
                "System vs User vs Assistant messages ka role aur prompt injection risks",
                "Few-Shot prompting, Chain of Thought (CoT), aur Least-to-Most decomposition",
                "Structured Outputs guarantee karna (JSON Schema, Pydantic, Instructor)",
                "KV Cache mechanics aur context window token budget economics",
                "Automated LLM evaluation aur LLM-as-a-Judge benchmarking"
            ],
            "practical_tasks": [
                "Ek complex reasoning puzzle ke liye Zero-Shot vs CoT prompt ka comparative test run karein",
                "Strict Pydantic JSON schema ke sath financial extraction prompt enforce karein",
                "Prompt injection jailbreak attack design karein aur uske khilaf system defense implement karein",
                "KV Cache context budget simulator likhein jo long-document chats ki cost calculate kare",
                "Enterprise prompt benchmark suite build karein jo 50 test cases par accuracy score kare"
            ],
            "resources": [
                {"title": "OpenAI Prompt Engineering Guide", "url": "https://platform.openai.com/docs/guides/prompt-engineering"},
                {"title": "Anthropic Interactive Prompt Tutorial", "url": "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 2 Prompt Mental Model
  user_prompt[Raw User Prompt] $terminal -> system_ctx[System Context & Schema] $code
  system_ctx -> cot[Chain-of-Thought Scratchpad] $brain
  cot -> json_out[Validated JSON Structure] $server *""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "prompt-rookie",
            "order_index": 2,
            "lessons": [
                {
                    "lesson_code": "2.1",
                    "slug": "how-llms-work",
                    "title": "LLMs Kaise Kaam Karte Hain: Next Token Prediction & Context Window",
                    "duration_minutes": 30,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, Large Language Models (LLMs) ke baare mein sab se ahem mental model yeh hai: **LLM koi database ya conscious mind nahi hai; yeh ek statistical next-token prediction engine hai!**

Jab aap model ko prompt dete hain, to model us text ko **Tokens** (sub-words) mein break karta hai. Phir har step par model apni vocabulary mein se aglay token ki probability distribution calculate karta hai.
Maslan agar sentence hai: "Pakistan ka qaumi khel ___ hai", to model `hockey` ko 92%, `cricket` ko 6%, aur `football` ko 1% probability assign karega.

Yahan 3 critical sampling parameters kaam aate hain:
1. **Temperature ($T$)**: Logits ko divide karta hai. $T=0$ ka matlab Greedy Search (hamesha highest probability token choose karo). $T=1.0$ creative outputs deta hai.
2. **Top-P (Nucleus Sampling)**: Sirf un tokens ko consider karta hai jinki cumulative probability $P$ tak pohnchti hai.
3. **Context Window**: Model ki memory limit jahan tak wo pichle tokens dekh sakta hai.""",
                    "english_summary": "Understand next-token autoregressive generation, logits, temperature scaling, top-p nucleus sampling, and context window economics.",
                    "code_example": """import numpy as np

# Simulate Vocabulary Logits for Next Token Prediction
vocab = ["cricket", "hockey", "football", "biryani", "code"]
logits = np.array([2.1, 4.8, 1.2, -1.5, 0.5])

def softmax_with_temp(logits: np.ndarray, temperature: float = 1.0) -> np.ndarray:
    scaled = logits / max(temperature, 1e-5)
    exp_scaled = np.exp(scaled - np.max(scaled)) # numerical stability
    return exp_scaled / np.sum(exp_scaled)

print("--- Temperature 0.1 (Greedy / Deterministic) ---")
probs_low = softmax_with_temp(logits, temperature=0.1)
for word, p in zip(vocab, probs_low):
    print(f"  {word:10s}: {p*100:.2f}%")

print("\n--- Temperature 1.2 (Creative / Random Exploration) ---")
probs_high = softmax_with_temp(logits, temperature=1.2)
for word, p in zip(vocab, probs_high):
    print(f"  {word:10s}: {p*100:.2f}%")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Next Token Prediction Pipeline
  input_text[Prompt Text] $terminal -> tokenize[BPE Tokenizer] $code
  tokenize -> transformer[Decoder Transformer] $brain
  transformer -> logits[Vocabulary Logits Vector] $layers
  logits -> softmax[Softmax + Temperature] $cpu
  softmax -> next_tok[Selected Next Token] $cube *""",
                    "diagram_type": "flow",
                    "resources": [{"title": "What Are Large Language Models?", "url": "https://www.youtube.com/watch?v=zjkBMFhNj_g"}],
                    "xp_reward": 20,
                    "order_index": 1
                },
                {
                    "lesson_code": "2.2",
                    "slug": "prompt-patterns-cot",
                    "title": "Prompt Engineering Patterns: Zero-Shot, Few-Shot & Chain-of-Thought",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, agar aap LLM se mushkil mathematical ya logical sawaal poochein to direct Zero-Shot prompt aksar fail ho jata hai. Kyun?
Kyunke LLM agla token bina kisi "rough work" ke foran generate karne ki koshish karta hai!

Yahan do powerful techniques aati hain:
1. **Few-Shot Prompting**: Model ko 2 se 3 solved examples provide karein taake wo pattern aur format samajh jaye.
2. **Chain-of-Thought (CoT)**: Model ko majboor karein ke wo final answer se pehle step-by-step reasoning likhay: *"Let's think step by step"*.

Jab model intermediate tokens generate karta hai, to wo tokens aglay step ke context mein add ho jate hain — is tarah model ko extra computational capacity milti hai! DeepSeek-R1 aur OpenAI o1 isi fundamental principle ko reinforcement learning se scale karte hain.""",
                    "english_summary": "Master In-Context Learning: Zero-Shot vs Few-Shot prompt templates, Chain-of-Thought scratchpads, and least-to-most task decomposition.",
                    "code_example": """# Demonstration of Chain-of-Thought (CoT) Prompt Pattern

direct_zero_shot_prompt = (
    "Q: Ek dukaan par 12 dahi bhallay hain. 4 log aaye aur har ek ne 2 plate khaye.\\n"
    "Dukaan walay ne 5 naye banaye. Dukaan par kitne dahi bhallay bache?\\nAnswer:"
)

chain_of_thought_prompt = (
    "Sawaal: Ek dukaan par 12 dahi bhallay hain. 4 log aaye aur har ek ne 2 plate khaye.\\n"
    "Dukaan walay ne 5 naye banaye. Dukaan par kitne dahi bhallay bache?\\n\\n"
    "Aap step-by-step sochein:\\n"
    "1. Shuru mein total dahi bhallay = 12\\n"
    "2. 4 logo ne 2, 2 plate khaye: 4 * 2 = 8 khaye gaye.\\n"
    "3. Baqi bache: 12 - 8 = 4.\\n"
    "4. Dukaan walay ne 5 naye banaye: 4 + 5 = 9.\\n\\n"
    "Jawab: 9 dahi bhallay baqi hain."
)

print("CoT Pattern ready for LLM submission. Model accuracy increases from 35% to 85%!")""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: CoT Reasoning Scratchpad
  prompt[Raw Multi-Step Question] $terminal -> cot[Step-by-Step Scratchpad Tokens] $brain
  cot -> intermediate[Intermediate Computation Storage] $database
  intermediate -> final[High-Confidence Final Solution] $server *""",
                    "diagram_type": "arch",
                    "resources": [{"title": "Chain-of-Thought Paper (Wei et al.)", "url": "https://arxiv.org/abs/2201.11903"}],
                    "xp_reward": 25,
                    "order_index": 2
                },
                {
                    "lesson_code": "2.3",
                    "slug": "structured-outputs-json",
                    "title": "Structured Outputs & Function Calling Foundations",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab hum production mein software banate hain, to hum LLM se conversational text nahi balke **Strict JSON** chahte hain jo hamaray backend database ya API mein direct save ho sakay.

Agar aap sirf prompt mein likhein *"Please return valid JSON"*, to 100 mein se 5 dafa LLM extra markdown (```json ... ```) ya missing commas ke sath output dega aur aapka backend crash ho jayega!

Iska production solution hai **Grammar-Based Constrained Decoding / JSON Schema**.
Modern inference engines (jaise Groq, OpenAI, Gemini) LLM ke output logits par regex/grammar mask lagate hain — yaani agar agla token valid JSON bracket ya key nahi hai to model us token ko generate kar hi nahi sakta!""",
                    "english_summary": "Enforce 100% deterministic JSON schemas and constrained grammar decoding using Pydantic models for reliable backend integration.",
                    "code_example": """import json
from pydantic import BaseModel, Field
from typing import List

# 1. Define Strict Pydantic Schema
class ProductExtraction(BaseModel):
    product_name: str = Field(description="Name of the product in Urdu/English")
    price_pkr: float = Field(description="Price converted to Pakistani Rupees")
    category: str = Field(description="Category e.g. Electronics, Grocery")
    tags: List[str] = Field(default_factory=list)

# 2. Extract JSON Schema for LLM API Spec
schema = ProductExtraction.model_json_schema()
print("Generated OpenAI/Groq Compatible JSON Schema:")
print(json.dumps(schema, indent=2))

# 3. Simulated Validated Response from Model
sample_llm_output = '{"product_name": "Pakistani Basmati Rice 5kg", "price_pkr": 1850.0, "category": "Grocery", "tags": ["premium", "rice"]}'
parsed_obj = ProductExtraction.model_validate_json(sample_llm_output)
print(f"\\nParsed Object Verified: {parsed_obj.product_name} -> PKR {parsed_obj.price_pkr}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Constrained JSON Decoding
  llm_logits[Model Raw Logits] $brain -> grammar[Grammar / JSON Schema Mask] $code
  grammar -> filter[Invalid Tokens Logit = -inf] $layers
  filter -> json_token[Only Valid JSON Token Allowed] $server *""",
                    "diagram_type": "flow",
                    "resources": [{"title": "OpenAI Structured Outputs Guide", "url": "https://platform.openai.com/docs/guides/structured-outputs"}],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "2.4",
                    "slug": "kv-cache-context-mechanics",
                    "title": "KV Cache Architecture & Long Context Window Mechanics",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab aap ChatGPT ya kisi LLM se baat karte hain, to kya aapne socha hai ke pehla token aane mein waqt lagta hai (Time to First Token - TTFT), lekin uske baad tokens tezi se stream hote hain?

Iska raaz hai **KV Cache (Key-Value Cache)**!
Self-attention mein har token ko pichle tamam tokens ke Key ($K$) aur Value ($V$) vectors ke sath multiply hona hota hai. Agar hum har naye token par poori chat history ko dubara compute karein, to generation $O(N^2)$ ho jayegi aur bohot slow ho jayegi.

Is liye modern inference engines pichle sabhi tokens ke $K$ aur $V$ tensors ko GPU VRAM mein cache kar letay hain. Naya token sirf apna Query ($Q$) vector calculate karta hai aur direct cached $K$ aur $V$ se multiply ho jata hai.
Lekin iska nuqsan yeh hai ke long chats mein KV Cache memory bohot barh jati hai:
$$\\text{KV Cache Size} = 2 \\times \\text{layers} \\times \\text{heads} \\times d_k \\times \\text{seq\\_len} \\times \\text{precision bytes}$$
Is lesson mein hum KV cache ki memory math aur context window optimization ko first-principles se samjhein ge.""",
                    "english_summary": "Understand autoregressive generation memory-bandwidth bottlenecks, KV cache mathematical formulation, and GPU VRAM scaling across sequence lengths.",
                    "code_example": """def calculate_kv_cache_ram(
    num_layers: int,
    num_kv_heads: int,
    head_dim: int,
    seq_len: int,
    precision_bytes: int = 2 # FP16/BF16
) -> float:
    # 2 for Key and Value
    bytes_per_token = 2 * num_layers * num_kv_heads * head_dim * precision_bytes
    total_bytes = bytes_per_token * seq_len
    return total_bytes / (1024 ** 3) # in Gigabytes (GB)

# Llama-3-8B specs: 32 layers, 8 KV heads (Grouped Query Attention), head_dim 128
llama3_8b_kv_16k = calculate_kv_cache_ram(32, 8, 128, 16_384, precision_bytes=2)
llama3_8b_kv_128k = calculate_kv_cache_ram(32, 8, 128, 131_072, precision_bytes=2)

print(f"Llama 3 8B KV Cache at 16k context: {llama3_8b_kv_16k:.2f} GB RAM")
print(f"Llama 3 8B KV Cache at 128k context: {llama3_8b_kv_128k:.2f} GB RAM (Massive VRAM consumption!)")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Autoregressive KV Cache Engine
  new_token[New Input Token] $terminal -> q_proj[Query Projection Q] $cpu
  kv_cache[Cached Prior K & V Tensors] $database -> attn_compute[Scaled Dot-Product Attention] $brain *
  q_proj -> attn_compute
  attn_compute -> next_tok[Generated Next Token] $terminal""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Transformers KV Cache Explained", "url": "https://kipp.ly/transformer-inference-survey/"}
                    ],
                    "xp_reward": 30,
                    "order_index": 4
                },
                {
                    "lesson_code": "2.5",
                    "slug": "llm-evals-judge-benchmarks",
                    "title": "LLM Evaluation & Benchmarking: Automated LLM-as-a-Judge",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab hum production mein prompt ya model update karte hain, to hum kaise check karein ke naya prompt pichle se behtar hai?
Purane metrics jaise BLEU ya ROUGE generative AI mein fail ho jate hain kyunke ek hi baat ko 10 mukhtalif tareeqon se kaha ja sakta hai.

Modern standard hai **LLM-as-a-Judge**!
Hum ek powerful reasoning model (jaise Claude 3.5 Sonnet ya GPT-4o) ko ek clear evaluation rubric dete hain jismein wo candidate output ko 4 dimensions par 1 se 5 score karta hai:
1. **Faithfulness**: Kya answer sirf context par mabni hai ya hallucination hai?
2. **Relevance**: Kya sawal ka seedha jawab diya gaya?
3. **Completeness**: Kya koi zaroori step miss to nahi hua?
4. **Tone & Formatting**: Kya output requested JSON ya conversational style ke mutabiq hai?""",
                    "english_summary": "Implement automated LLM evaluation pipelines using LLM-as-a-Judge, scoring rubrics, and systematic regression testing.",
                    "code_example": """import json

judge_rubric = (
    "You are an expert AI evaluator. Rate the assistant answer from 1 to 5 based on:\\n"
    "1. Faithfulness (no hallucinations)\\n"
    "2. Helpfulness and clarity in Roman Urdu\\n"
    'Return valid JSON with: {"faithfulness_score": int, "helpfulness_score": int, "critique": str}'
)

def simulate_llm_judge(question: str, context: str, answer: str) -> dict:
    # Simulated Judge Evaluation
    return {
        "question": question,
        "faithfulness_score": 5,
        "helpfulness_score": 5,
        "critique": "Answer accurately explains PyTorch autograd in clear conversational Roman Urdu with zero hallucination."
    }

eval_result = simulate_llm_judge(
    question="Autograd kaise kaam karta hai?",
    context="PyTorch autograd builds dynamic computational graphs during forward pass.",
    answer="So guys, PyTorch autograd forward pass ke dauran computational graph banata hai aur backward() par gradients calculate karta hai."
)
print("LLM-as-a-Judge Evaluation Output:")
print(json.dumps(eval_result, indent=2))""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Automated LLM Evaluation Pipeline
  gen_answer[Candidate Model Answer] $code -> judge[Judge LLM Rubric Evaluation] $brain
  gold_ref[Ground Truth Reference] $database -> judge
  judge -> metrics[Faithfulness & Relevance Scores] $server *""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "Judging LLM-as-a-Judge with MT-Bench", "url": "https://arxiv.org/abs/2306.05685"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "2.6",
                    "slug": "module-2-capstone-prompt-optimizer",
                    "title": "Module 2 Capstone: Enterprise Prompt Optimization & Regression Suite",
                    "duration_minutes": 50,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, Module 2 ke Capstone mein aap ek **Automated Prompt Optimization & Regression Testing Suite** banayenge!

Enterprise mein jab product manager prompt change karta hai to aksar 20% puraane edge cases break ho jate hain (silent regression). Aapka capstone:
1. 3 mukhtalif system prompt variants (Direct, Few-Shot, Chain-of-Thought) ko 10 synthetic test cases par run karega.
2. Output ko Pydantic schema validation se verify karega.
3. Automated LLM judge ke zariye har variant ko score karega.
4. Winning prompt select karega jo highest accuracy aur lowest token cost deliver kare!""",
                    "english_summary": "Build an automated prompt optimization and regression testing suite comparing prompt variants across benchmarks to find Pareto-optimal prompts.",
                    "code_example": """# Module 2 Capstone: Automated Prompt Benchmark Runner
test_cases = [
    {"input": "Mera order #9921 abhi tak nahi mila, refund karein!", "expected_intent": "refund"},
    {"input": "Aapki shop par Basmati rice ka rate kya hai?", "expected_intent": "inquiry"},
    {"input": "Bohot buri service thi, packaging phati hui thi.", "expected_intent": "complaint"}
]

prompt_variants = {
    "variant_a_direct": "Classify customer message intent as: refund, inquiry, complaint.",
    "variant_b_cot": "Analyze user sentiment, identify core issue, then classify intent: refund, inquiry, complaint."
}

def evaluate_variant(name: str, template: str) -> float:
    # Simulate scoring across benchmark
    accuracy = 0.90 if "cot" in name else 0.70
    print(f"Evaluated {name}: Accuracy = {accuracy*100:.1f}%")
    return accuracy

scores = {name: evaluate_variant(name, tmpl) for name, tmpl in prompt_variants.items()}
winning_prompt = max(scores, key=scores.get)
print(f"\\nWinning Production Prompt: {winning_prompt} with {scores[winning_prompt]*100}% accuracy!")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Automated Prompt Tuning Pipeline
  base_prompt[Base System Prompt] $code -> variations[Mutation Engine (CoT / Roles)] $cube
  variations -> test_suite[Golden Test Suite (50 Cases)] $database
  test_suite -> eval_judge[Evaluation Judge LLM] $brain
  eval_judge -> winner[Pareto-Optimal Production Prompt] $terminal *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "DSPy: Automated Prompt Optimization", "url": "https://github.com/stanfordnlp/dspy"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        },

        # =========================================================================
        # MODULE 3: Classical Machine Learning & Feature Engineering
        # =========================================================================
        {
            "phase_slug": "phase-2-core-ml-deeplearning",
            "module_number": 3,
            "slug": "classical-machine-learning",
            "real_world_deliverable": "Production Customer Churn ML Service (XGBoost + Fast Scikit-Pipeline)",
            "zero_gpu_recipe": {
                'platform': 'Local CPU / Colab Free Tier',
                'vram_required': '0 GB (CPU-Optimized)',
                'estimated_cost': '$0.00 Free',
                'compute_units_tip': 'Classical ML (XGBoost, LightGBM, Scikit-learn) runs with multi-threaded CPU OpenMP; no GPU compute units required.',
                'one_click_command': 'pip install scikit-learn xgboost lightgbm polars optuna && python train.py'
            },
            "title": "Module 3: Classical Machine Learning & Feature Engineering",
            "weeks_range": "Weeks 5-6",
            "estimated_hours": 14,
            "learning_outcomes": [
                "Supervised learning taxonomy: Linear, Logistic, Trees, Ensembles",
                "Gradient Boosting mechanics (XGBoost, LightGBM, CatBoost)",
                "Dimensionality reduction: PCA, t-SNE, and K-Means clustering",
                "Model evaluation: Precision, Recall, F1-Score, ROC-AUC, and calibration",
                "Data leakage prevention and production Sklearn ColumnTransformer pipelines",
                "Deploying tabular models with low latency SLAs"
            ],
            "practical_tasks": [
                "Clean cross-validation pipeline implement karein with zero data leakage",
                "Custom Random Forest vs XGBoost benchmark run karein on imbalanced data",
                "PCA dimensionality reduction se 50 features ko 3 visual components mein compress karein",
                "Threshold tuning se F1-score optimize karein on credit fraud dataset",
                "Production ML Churn microservice export karein via ONNX/Joblib"
            ],
            "resources": [
                {"title": "Scikit-Learn Documentation", "url": "https://scikit-learn.org/stable/"},
                {"title": "XGBoost Production Architecture", "url": "https://xgboost.readthedocs.io/en/stable/"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 3 Classical ML Pipeline
  raw_data[Raw Mixed Tabular Data] $database -> pipe[Leakage-Free Sklearn Pipeline] $layers
  pipe -> trees[XGBoost Gradient Boosted Trees] $cpu
  trees -> eval_metrics[Precision / Recall / F1 Matrix] $chart
  eval_metrics -> onnx[Low-Latency ONNX Model] $server *""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "ml-practitioner",
            "order_index": 3,
            "lessons": [
                {
                    "lesson_code": "3.1",
                    "slug": "supervised-learning-pipeline",
                    "title": "Supervised Learning Pipeline: Preprocessing Se Validation Tak",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab hum Machine Learning ki dunya mein qadam rakhte hain to pehla sabq yeh hai: **GIGO (Garbage In, Garbage Out)**!
Dunya ka sab se bara model bhi bekar ثابت hoga agar aapka data preprocessing aur validation pipeline kharab hai.

ML pipeline ke 4 bunyadi steps hote hain:
1. **Feature Engineering**: Categorical variables ko One-Hot ya Target Encoding karna, aur continuous features ko scale karna (`StandardScaler`).
2. **Train/Validation/Test Split**: Kabhi bhi test data par scaler fit na karein (Data Leakage)!
3. **Cross-Validation**: 5-Fold Stratified CV se model ki stability measure karna.
4. **Evaluation Metrics**: Class imbalance mein Accuracy dhoka deti hai; wahan Precision, Recall aur F1-Score dekhna parta hai.""",
                    "english_summary": "Build leakage-free supervised learning pipelines with Scikit-learn: preprocessing, stratified cross-validation, and robust metrics.",
                    "code_example": """import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 1. Generate Synthetic Imbalanced Dataset
X, y = make_classification(n_samples=1000, n_features=10, weights=[0.85, 0.15], random_state=42)

# 2. Train-Test Split (Holdout set)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# 3. Leakage-Free Pipeline: Scaler fits ONLY on training folds!
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(class_weight="balanced"))
])

# 4. Stratified 5-Fold Cross Validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring="f1")

print(f"5-Fold CV F1-Scores: {scores.round(3)}")
print(f"Mean F1: {scores.mean():.3f} (+/- {scores.std():.3f})")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Leakage-Free ML Pipeline
  raw_train[Raw Training Data] $database -> scaler[StandardScaler Fit & Transform] $layers
  scaler -> train_model[Model Training] $brain
  raw_test[Raw Test Data] $database -> scaler_test[Apply Pre-Fit Scaler Only] $layers
  scaler_test -> eval[F1 & ROC-AUC Evaluation] $chart *""",
                    "diagram_type": "flow",
                    "resources": [{"title": "Scikit-Learn Common Pitfalls", "url": "https://scikit-learn.org/stable/common_pitfalls.html"}],
                    "xp_reward": 20,
                    "order_index": 1
                },
                {
                    "lesson_code": "3.2",
                    "slug": "tree-models-gradient-boosting",
                    "title": "Decision Trees Se XGBoost & LightGBM Tak",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, tabular data (tables, databases, CSVs) par deep learning aksar fail ho jati hai ya bohot slow hoti hai. Dunya ke 90% Kaggle competitions aur production tabular tasks mein **Gradient Boosted Decision Trees (GBDT)** jeet-te hain!

Safar shuru hota hai ek single **Decision Tree** se jo if-else rules banata hai (Gini Impurity ya Entropy ke mutabiq). Lekin ek akela tree bohot jaldi overfit ho jata hai.
Phir aata hai **Random Forest (Bagging)**: Yeh hazaron trees parallel train karta hai aur unka average nikalta hai (Variance reduction).

Aur aakhir mein aata hai **Gradient Boosting (XGBoost / LightGBM)**:
Yeh trees ko sequential train karta hai. Pehla tree prediction karta hai; doosra tree pehle tree ke **Residuals (Errors)** ko predict karta hai; teesra tree doosre ke errors ko theek karta hai! Is tarah har naya tree model ki ghaltiyon ko khatam karta chala jata hai.""",
                    "english_summary": "Master ensemble learning: Bagging vs Boosting, tree splitting criteria, and training XGBoost models on tabular data.",
                    "code_example": """import numpy as np
import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Synthetic Customer Churn Dataset
X, y = make_classification(n_samples=2000, n_features=15, n_informative=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train Production XGBoost Classifier
model = xgb.XGBClassifier(
    n_estimators=100,
    learning_rate=0.08,
    max_depth=4,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="logloss",
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("XGBoost Production Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Retained", "Churned"]))""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Gradient Boosting Tree Sequence
  data[Input Features X] $database -> tree1[Tree 1: Initial Prediction] $cpu
  tree1 -> res1[Residual Error 1] $chart
  res1 -> tree2[Tree 2: Fit on Residual 1] $cpu
  tree2 -> res2[Residual Error 2] $chart
  res2 -> tree3[Tree 3: Minimize Remaining Loss] $cpu *
  tree1 -> final[Ensemble Sum: y_hat = t1 + eta*t2 + eta*t3] $server
  tree2 -> final
  tree3 -> final""",
                    "diagram_type": "arch",
                    "resources": [{"title": "XGBoost Original Paper", "url": "https://arxiv.org/abs/1603.02754"}],
                    "xp_reward": 25,
                    "order_index": 2
                },
                {
                    "lesson_code": "3.3",
                    "slug": "unsupervised-learning-clustering",
                    "title": "Dimensionality Reduction & Clustering: PCA, t-SNE & K-Means",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, real-world AI pipelines mein aksar hamare paas labels (ground truth) nahi hote. Misal ke taur par, 100,000 unlabelled customer interactions ya 1536-dimensional embeddings. Yahan kaam aati hai **Unsupervised Learning**!

Do ahem techniques hain:
1. **Dimensionality Reduction (PCA & t-SNE)**: 1536-dimensional embedding vectors ko 2D ya 3D mein project karna taake hum human eyes se clusters dekh sakein. PCA linear covariance eigenvectors nikalta hai, jabke t-SNE local neighborhood probabilities ko preserve karta hai.
2. **K-Means Clustering**: Data points ko $K$ groups mein divide karna by minimizing distance from cluster centroids. Yeh customer segmentation aur vector database query routing ke liye foundation banta hai!""",
                    "english_summary": "Apply unsupervised dimensionality reduction (PCA, t-SNE) and centroid clustering (K-Means) for embedding visualization and customer segmentation.",
                    "code_example": """import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Simulate 500 embedding vectors in 64 dimensions
np.random.seed(42)
embeddings = np.random.randn(500, 64)

# 1. Dimensionality Reduction: Compress from 64D to 3D via PCA
pca = PCA(n_components=3)
reduced_embeddings = pca.fit_transform(embeddings)
print(f"Explained Variance Ratio (3 components): {pca.explained_variance_ratio_.sum():.2%}")

# 2. Cluster into 4 Customer Archetypes
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(reduced_embeddings)

print(f"Cluster Distribution: {np.bincount(cluster_labels)}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Unsupervised Embedding Clustering
  high_dim[High-Dim Embedding Space (1536-D)] $database -> pca[PCA Covariance Matrix Eigenvectors] $brain
  pca -> low_dim[Low-Dim 2D Space] $layers
  low_dim -> kmeans[K-Means Centroid Assignment] $cube *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "PCA Comprehensive Guide", "url": "https://scikit-learn.org/stable/modules/decomposition.html#pca"}
                    ],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "3.4",
                    "slug": "model-evaluation-metrics",
                    "title": "Rigorous Model Evaluation: Precision, Recall, F1 & ROC-AUC",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, sochiye: ek bank mein 99.9% transactions legitimate hoti hain aur sirf 0.1% fraudulent. Agar koi bewaqoof model hamesha keh de "Sab kuch normal hai", to uski Accuracy 99.9% hogi! Lekin bank tabah ho jayega kyunke 100% fraud miss ho gaya!

Is liye professional AI engineers **Accuracy Trap** se bach kar yeh metrics use karte hain:
- **Precision**: Jo model ne Fraud kaha, us mein se kitne waqai Fraud thay? (False Positives minimize karna).
- **Recall**: Total Fraud transactions mein se model ne kitne pakray? (False Negatives minimize karna).
- **F1-Score**: Precision aur Recall ka Harmonic Mean: $2 \\cdot \\frac{P \\times R}{P + R}$.
- **ROC-AUC**: Mukhtalif thresholds par model ki discrimination power measure karna.""",
                    "english_summary": "Understand confusion matrix mechanics, Precision-Recall tradeoffs, ROC-AUC curves, and optimal decision threshold selection.",
                    "code_example": """import numpy as np
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, roc_auc_score

# True labels vs Model probabilities
y_true = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1])
y_probs = np.array([0.05, 0.12, 0.20, 0.35, 0.45, 0.48, 0.55, 0.60, 0.85, 0.92])

# Threshold Tuning: Default 0.5 vs Conservative 0.4
for threshold in [0.5, 0.4]:
    y_pred = (y_probs >= threshold).astype(int)
    cm = confusion_matrix(y_true, y_pred)
    p, r, f1, _ = precision_recall_fscore_support(y_true, y_pred, average="binary")
    print(f"Threshold: {threshold} | Precision: {p:.2f} | Recall: {r:.2f} | F1: {f1:.2f}")

auc = roc_auc_score(y_true, y_probs)
print(f"ROC-AUC Score: {auc:.3f}")""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Evaluation Metrics Framework
  predictions[Model Probability Output] $code -> conf_matrix[Confusion Matrix: TP, FP, TN, FN] $database
  conf_matrix -> prec_rec[Precision-Recall Curve] $chart
  conf_matrix -> f1_opt[F1-Score Optimal Threshold] $terminal *""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "Precision and Recall Explained", "url": "https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html"}
                    ],
                    "xp_reward": 25,
                    "order_index": 4
                },
                {
                    "lesson_code": "3.5",
                    "slug": "feature-engineering-pipelines",
                    "title": "Leakage-Free Feature Engineering & Sklearn Pipelines",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab raw data tabular database se aata hai, to usmein mixed types hoti hain: numerical (income, age), categorical (city, gender), aur missing values (`NaN`).

Agar aap train aur test data ko ikattha impute ya scale kar lein, to test set ki information model mein leak ho jati hai. Model training par 99% score karta hai lekin production mein ja kar crash kar jata hai!

Iska production solution hai **Scikit-learn `ColumnTransformer` aur `Pipeline`**.
Yeh transforms ko ek atomic executable DAG banata hai jo training ke waqt parameters fit karta hai aur production mein new incoming records par sirf deterministic transform chalata hai.""",
                    "english_summary": "Construct robust end-to-end ColumnTransformers and Pipeline workflows handling missing values, scaling, and categorical encoding without data leakage.",
                    "code_example": """import numpy as np
import polars as pl
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge

# Mixed Feature Dataset
X = np.array([
    [25.0, "Karachi", 50000.0],
    [np.nan, "Lahore", 85000.0],
    [38.0, "Islamabad", 120000.0],
    [45.0, "Karachi", np.nan]
], dtype=object)
y = np.array([120.0, 190.0, 280.0, 210.0])

num_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

preprocessor = ColumnTransformer(transformers=[
    ("num", num_pipe, [0, 2]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), [1])
])

full_model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", Ridge(alpha=1.0))
])

full_model.fit(X, y)
print("Pipeline trained successfully with zero leakage!")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Leakage-Free Sklearn Pipeline
  raw_feat[Raw Mixed Tabular Features] $database -> col_trans[ColumnTransformer (Numeric + Categorical)] $layers
  col_trans -> scaler[StandardScaler (Fit only on Train)] $cpu
  scaler -> model[Predictive Model Classifier] $brain *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Sklearn Pipeline Composite Estimators", "url": "https://scikit-learn.org/stable/modules/compose.html"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "3.6",
                    "slug": "module-3-capstone-ml-service",
                    "title": "Module 3 Capstone: Production Customer Churn Predictive ML Service",
                    "duration_minutes": 55,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, Module 3 ke Capstone mein aap ek real-world **Customer Churn Prediction Service** build karenge jo SaaS aur Fintech companies ki backbone hoti hai!

Is capstone mein aap:
1. Imbalanced customer usage features ko load karenge.
2. Leakage-free Sklearn pipeline + XGBoost model train karenge.
3. Optuna se hyperparameter tuning (learning rate, tree depth, subsample) execute karenge.
4. Model ko serialized binary (`.joblib` ya `.onnx`) mein export karke FastAPI endpoint ke through sub-10ms inference benchmark verify karenge!""",
                    "english_summary": "Ship an end-to-end production ML microservice: dataset preprocessing, Optuna hyperparameter optimization, model export, and real-time inference.",
                    "code_example": """import xgboost as xgb
import joblib
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# 1. Train Capstone Churn Model
X, y = make_classification(n_samples=5000, n_features=12, weights=[0.8, 0.2], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = xgb.XGBClassifier(n_estimators=80, max_depth=3, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# 2. Export Model Artifact
joblib.dump(model, "churn_model.joblib")
print("Model saved to churn_model.joblib")

# 3. Simulated Fast Inference API Handler
loaded_model = joblib.load("churn_model.joblib")
new_customer_features = np.random.randn(1, 12)
churn_prob = loaded_model.predict_proba(new_customer_features)[0, 1]
print(f"Customer Churn Risk: {churn_prob*100:.1f}% -> {'Urgent Retention Intervention' if churn_prob > 0.5 else 'Healthy Customer'}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Production ML Churn Microservice
  user_event[Real-Time User Feature Vector] $terminal -> fast_api[FastAPI Prediction Endpoint] $server
  fast_api -> onnx_model[ONNX Runtime Low-Latency Model] $brain
  onnx_model -> churn_score[Churn Risk Score + Interventions] $database *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "XGBoost Production Serving", "url": "https://xgboost.readthedocs.io/en/stable/tutorials/saving_model.html"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        },

        # =========================================================================
        # MODULE 4: Deep Learning & PyTorch Foundations
        # =========================================================================
        {
            "phase_slug": "phase-2-core-ml-deeplearning",
            "module_number": 4,
            "slug": "deep-learning-and-pytorch-foundations",
            "real_world_deliverable": "Mini-Autograd Deep Learning Engine & Multi-GPU Training Loop",
            "zero_gpu_recipe": {
                'platform': 'Google Colab Free Tier (Nvidia T4 15GB VRAM)',
                'vram_required': '2 GB VRAM',
                'estimated_cost': '$0.00 Free',
                'compute_units_tip': 'PyTorch MLP and CNN training loops take less than 2 minutes on Colab T4 GPU; zero compute credits required.',
                'one_click_command': 'python -c "import torch; print(torch.cuda.is_available())"'
            },
            "title": "Module 4: Deep Learning & PyTorch Foundations",
            "weeks_range": "Weeks 7-8",
            "estimated_hours": 16,
            "learning_outcomes": [
                "PyTorch Tensors, memory layout (strides, contiguity), aur GPU acceleration",
                "Dynamic computational graphs aur Autograd backward pass mechanics",
                "Neural network forward pass, non-linear activations (GELU, SwiGLU), aur loss functions",
                "Production training loops: Automatic Mixed Precision (AMP), gradient scaling, and gradient clipping",
                "Normalization & Regularization: LayerNorm, RMSNorm, and Cosine Annealing learning rate schedules",
                "Building a micrograd-style reverse-mode autodiff engine from raw tensors"
            ],
            "practical_tasks": [
                "Manual tensor strides aur memory contiguity inspect karein",
                "PyTorch autograd use kiye baghair manual 2-layer backpropagation pass likhein",
                "SwiGLU activation module define karein aur standard ReLU se performance compare karein",
                "torch.cuda.amp.autocast aur GradScaler ke sath memory 50% reduce karein",
                "Custom Micrograd Autograd engine build karein jo non-linear decision boundary train kare"
            ],
            "resources": [
                {"title": "PyTorch Official Deep Learning Tutorials", "url": "https://pytorch.org/tutorials/"},
                {"title": "Andrej Karpathy: Micrograd Video Series", "url": "https://www.youtube.com/watch?v=VMj-3S1tku0"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 4 PyTorch Deep Learning Graph
  tensors[PyTorch Tensors on CUDA GPU] $database -> autograd[Dynamic Autograd Graph] $brain
  autograd -> forward[Forward Pass & SwiGLU Activations] $layers
  forward -> amp[Mixed Precision AMP & GradScaler] $cpu
  amp -> opt[AdamW Parameter Update] $server *""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "transformer-expert",
            "order_index": 4,
            "lessons": [
                {
                    "lesson_code": "4.1",
                    "slug": "pytorch-tensors-autograd",
                    "title": "PyTorch Tensors, GPU Acceleration & Autograd",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, welcome to PyTorch! Dunya ke 95% AI research papers aur frontier labs (OpenAI, Meta, Anthropic) PyTorch use karti hain.

PyTorch ke 2 baray superpowers hain:
1. **GPU Acceleration**: NumPy arrays sirf CPU par chalte hain. PyTorch Tensors ko aap ek simple command `.to('cuda')` se Nvidia GPU VRAM mein bhej sakte hain jahan hazaron CUDA cores parallel calculations karte hain.
2. **Autograd (Automatic Differentiation)**: PyTorch aapke har mathematical operation ka computational graph background mein record karta rehta hai. Jab aap `loss.backward()` call karte hain to Chain Rule of Calculus automatically execute hota hai aur har parameter ka gradient calculate ho jata hai!""",
                    "english_summary": "Understand PyTorch GPU device memory allocation, CUDA acceleration, dynamic computation graphs, and the autograd backward engine.",
                    "code_example": """import torch

# 1. Check Device Availability
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using Compute Device: {device}")

# 2. Create Leaf Tensors with Gradient Tracking
x = torch.tensor([2.0, 3.0], requires_grad=True, device=device)
w = torch.tensor([1.5, -2.5], requires_grad=True, device=device)
b = torch.tensor(1.0, requires_grad=True, device=device)

# 3. Dynamic Forward Pass: y = w * x + b
y = w * x + b
loss = y.sum() ** 2

# 4. Backward Pass (Calculus Chain Rule automatically calculated!)
loss.backward()

print("Computation Graph Executed:")
print(f"Loss Value: {loss.item():.4f}")
print(f"dL/dw Gradient: {w.grad}")
print(f"dL/dx Gradient: {x.grad}")
print(f"dL/db Gradient: {b.grad}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: PyTorch Autograd Graph
  w[Weight w] $database -> mul[Multiply Node (*)] $cpu
  x[Input x] $terminal -> mul
  mul -> add[Addition Node (+)] $cpu
  b[Bias b] $database -> add
  add -> loss[Loss Node] $chart *
  loss -. backward gradient stream .-> w""",
                    "diagram_type": "flow",
                    "resources": [{"title": "PyTorch Autograd Mechanics", "url": "https://pytorch.org/docs/stable/notes/autograd.html"}],
                    "xp_reward": 25,
                    "order_index": 1
                },
                {
                    "lesson_code": "4.2",
                    "slug": "building-mlp-neural-net",
                    "title": "Multi-Layer Perceptron (MLP) From Scratch in PyTorch",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, ek single linear layer sirf seedhi lines (linear boundaries) draw kar sakti hai. Real-world problems (jaise text, images, complex churn) non-linear hoti hain.

Non-linearity introduce karne ke liye hum do linear layers ke darmian **Activation Function** lagate hain (jaise ReLU, GELU, ya SwiGLU). Is combination ko **Multi-Layer Perceptron (MLP)** kehte hain!

Har training step ke 5 muqaddas arkaan hote hain:
1. `optimizer.zero_grad()`: Pichle step ke gradients zero karna (warna PyTorch unhe accumulate kar deta hai).
2. `outputs = model(inputs)`: Forward pass.
3. `loss = criterion(outputs, targets)`: Ghalati calculate karna.
4. `loss.backward()`: Gradients calculate karna via backpropagation.
5. `optimizer.step()`: Weights ko gradient ki direction mein update karna.""",
                    "english_summary": "Construct modular neural networks using torch.nn.Module, non-linear activations, loss functions, and the canonical 5-step training loop.",
                    "code_example": """import torch
import torch.nn as nn
import torch.optim as optim

# 1. Define MLP Architecture
class DeepMLP(nn.Module):
    def __init__(self, in_features: int, hidden_dim: int, out_features: int):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(in_features, hidden_dim),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, out_features)
        )
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)

# 2. Instantiate Model, Loss & Optimizer
model = DeepMLP(in_features=8, hidden_dim=32, out_features=1)
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.AdamW(model.parameters(), lr=0.01, weight_decay=1e-4)

# 3. Canonical Training Step
dummy_x = torch.randn(16, 8) # Batch 16, Features 8
dummy_y = torch.randint(0, 2, (16, 1)).float()

for epoch in range(10):
    optimizer.zero_grad()
    preds = model(dummy_x)
    loss = criterion(preds, dummy_y)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1:02d} | Loss: {loss.item():.4f}")""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: MLP Feed-Forward Architecture
  in_layer[Input Vector (Dim 8)] $terminal -> l1[Linear Layer 1 (Dim 32)] $layers
  l1 -> gelu[GELU Non-Linearity] $brain
  gelu -> l2[Linear Layer 2 (Dim 32)] $layers
  l2 -> out[Output Logits (Dim 1)] $server *""",
                    "diagram_type": "arch",
                    "resources": [{"title": "PyTorch Neural Networks Tutorial", "url": "https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html"}],
                    "xp_reward": 30,
                    "order_index": 2
                },
                {
                    "lesson_code": "4.3",
                    "slug": "activation-functions-loss-optimizers",
                    "title": "Modern Activations (GELU, SwiGLU) & Optimizers: AdamW vs SGD",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, purani textbooks mein Sigmoid aur Tanh sikhaye jaate thay jinki wajah se gradients vanish ho jate thay ($dL/dw \\approx 0$). Phir ReLU aya jisne deep learning ko revolutionize kiya, lekin ReLU mein negative values par gradient permanent zero ho jata hai ("Dying ReLU problem").

2026 SOTA LLMs (jaise LLaMA 3, Gemma 2, DeepSeek) use karte hain **SwiGLU (Swish Gated Linear Unit)**:
$$\\text{SwiGLU}(x) = (x W_1) \\otimes \\text{Swish}(x W_2)$$
Yeh gating mechanism model ko expressive power deta hai.

Sath hi, optimizer dunya mein **AdamW** standard hai. Classic Adam mein L2 regularization ghalat tareeqe se gradient ke sath mix ho jati thi; AdamW weight decay ko decoupled rakhta hai jis se generalization bohot behtar hoti hai.""",
                    "english_summary": "Explore modern neural network components: vanishing gradients, GELU vs SwiGLU gating mechanisms, and decoupled weight decay in AdamW.",
                    "code_example": """import torch
import torch.nn as nn
import torch.nn.functional as F

class SwiGLU(nn.Module):
    def __init__(self, in_features: int, hidden_dim: int):
        super().__init__()
        self.w_gate = nn.Linear(in_features, hidden_dim, bias=False)
        self.w_up = nn.Linear(in_features, hidden_dim, bias=False)
        self.w_down = nn.Linear(hidden_dim, in_features, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Swish(x * W_gate) * (x * W_up)
        return self.w_down(F.silu(self.w_gate(x)) * self.w_up(x))

layer = SwiGLU(in_features=128, hidden_dim=256)
x = torch.randn(4, 128)
output = layer(x)
print("SwiGLU Layer Output Shape:", output.shape)""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: SwiGLU Gating Mechanism
  input_x[Input Activation Vector x] $terminal -> gate[Linear Gate W_gate] $layers
  input_x -> up[Linear Up W_up] $layers
  gate -> silu[SiLU / Swish Activation] $brain
  silu -> elem_mul[Elementwise Gated Multiply] $cube *
  up -> elem_mul
  elem_mul -> down[Linear Down Projection W_down] $server""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "GLU Variants Paper (Noam Shazeer)", "url": "https://arxiv.org/abs/2002.05202"}
                    ],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "4.4",
                    "slug": "training-loop-amp-checkpointing",
                    "title": "Production Training Loops: Mixed Precision (AMP) & Checkpointing",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, agar aap standard 32-bit float (FP32) par training chalayein to GPU VRAM bohot jaldi full ho jati hai aur training slow hoti hai. Modern GPUs (Nvidia Tensor Cores) FP16 aur BF16 (Bfloat16) ko 3x se 5x tezi se execute karte hain!

Lekin FP16 mein chotay gradients underflow (0.0000...) ho jate hain.
Iska solution hai **Automatic Mixed Precision (AMP) aur `GradScaler`**:
1. Forward pass ko automatically FP16/BF16 mein cast karo (Memory 50% bachayein).
2. Loss ko calculate karke ek scale factor se multiply karo taake gradients underflow na hon.
3. Gradients unscale karke master FP32 weights ko update karo.
4. Sath hi `torch.nn.utils.clip_grad_norm_` se exploding gradients ko rokain!""",
                    "english_summary": "Master production training performance with PyTorch Automatic Mixed Precision (AMP), GradScaler, gradient clipping, and state dict checkpointing.",
                    "code_example": """import torch
import torch.nn as nn

device = "cuda" if torch.cuda.is_available() else "cpu"
model = nn.Sequential(nn.Linear(512, 1024), nn.GELU(), nn.Linear(1024, 10)).to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
scaler = torch.cuda.amp.GradScaler(enabled=(device == "cuda"))

# Simulated AMP Training Step
inputs = torch.randn(64, 512, device=device)
targets = torch.randint(0, 10, (64,), device=device)
criterion = nn.CrossEntropyLoss()

optimizer.zero_grad()
# Autocast runs forward pass in FP16/BF16
with torch.cuda.amp.autocast(enabled=(device == "cuda")):
    outputs = model(inputs)
    loss = criterion(outputs, targets)

# Scaler handles backprop without underflow
scaler.scale(loss).backward()
scaler.unscale_(optimizer)
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0) # Prevent exploding grads
scaler.step(optimizer)
scaler.update()

print("AMP Training Step Completed! VRAM footprint minimized.")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Automatic Mixed Precision (AMP) Flow
  fp32[Master FP32 Weights] $database -> cast[Autocast to FP16 / BF16] $layers
  cast -> forward[Forward Pass & Loss] $brain
  forward -> scaler[GradScaler Loss Scaling] $chart
  scaler -> backward[Backward Pass (No Underflow)] $cpu *
  backward -> update[Unscale & Optimizer Step] $server""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "PyTorch AMP Documentation", "url": "https://pytorch.org/docs/stable/amp.html"}
                    ],
                    "xp_reward": 25,
                    "order_index": 4
                },
                {
                    "lesson_code": "4.5",
                    "slug": "normalization-regularization-schedulers",
                    "title": "Modern Regularization: LayerNorm, RMSNorm & Cosine Schedulers",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab neural networks bohot deep ho jate hain (50 ya 100 layers), to unke activations ki scale har layer ke baad fluctuate karti hai (Internal Covariate Shift).

Is problem ko solve karne ke liye hum **Normalization** use karte hain:
- **LayerNorm**: Har sample ke features ka mean zero aur variance one karta hai: $\\frac{x - \\mu}{\\sigma} \\gamma + \\beta$.
- **RMSNorm**: Modern LLMs (LLaMA, Mistral) mein mean subtraction skip kar di jati hai, sirf root-mean-square se normalize kiya jata hai ($40\\%$ faster GPU execution!).

Sath hi, model ko start mein high learning rate dena training destabilize kar sakta hai. Is liye hum **Warmup + Cosine Annealing Learning Rate Scheduler** lagate hain jo pehle smooth start karta hai aur baad mein learning rate ko zero ki taraf decay karta hai.""",
                    "english_summary": "Understand feature normalization evolution (BatchNorm to LayerNorm to RMSNorm) and learning rate scheduling with cosine decay and warmup.",
                    "code_example": """import torch
import torch.nn as nn

class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # RMS = sqrt(mean(x^2))
        rms = torch.sqrt(torch.mean(x ** 2, dim=-1, keepdim=True) + self.eps)
        return (x / rms) * self.weight

# Verify RMSNorm on batch of vectors
norm = RMSNorm(dim=64)
sample = torch.randn(2, 10, 64) * 5.0 # High variance activations
normalized = norm(sample)
print("Input std:", sample.std().item())
print("RMSNorm output std:", normalized.std().item())""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: RMSNorm & Learning Rate Schedule
  in_acts[Hidden Activations] $layers -> rmsnorm[RMSNorm (No Mean Centering)] $cpu
  rmsnorm -> residual[Residual Connection] $cube
  scheduler[Cosine Annealing LR Warmup] $terminal -> opt_step[Optimizer Step] $brain *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "RMSNorm Paper", "url": "https://arxiv.org/abs/1910.07467"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "4.6",
                    "slug": "module-4-capstone-neural-engine",
                    "title": "Module 4 Capstone: Custom Neural Engine from Raw Tensors",
                    "duration_minutes": 55,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, congratulations! Aapne Deep Learning ke tamam mathematical aur implementation foundations samajh liye hain. Ab waqt hai **Ultimate First-Principles Test** ka!

Is capstone mein aap Andrej Karpathy ke micrograd jaisa ek **Custom Autograd Engine** implement karenge using raw Python scalar/tensor nodes:
1. Ek `Value` class banayein jo scalar numbers hold kare aur computation graph trace kare.
2. `__add__` aur `__mul__` ke local derivatives register karein.
3. Topological Sort algorithm se reverse execution graph order nikaalein.
4. Ek 2-layer Neural Net train karke non-linear decision boundary par loss zero karein!""",
                    "english_summary": "Construct a complete reverse-mode automatic differentiation engine from scratch and train a neural network without any PyTorch autograd magic.",
                    "code_example": """# Module 4 Capstone: Custom Micrograd-style Autodiff Node
class Value:
    def __init__(self, data, _children=()):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(_children)

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other))
        def _backward():
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad
        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other))
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)
        self.grad = 1.0
        for node in reversed(topo):
            node._backward()

a = Value(3.0)
b = Value(-2.0)
c = a * b + Value(10.0)
c.backward()
print(f"Computed c: {c.data} | dc/da gradient: {a.grad} (Expected -2.0) | dc/db: {b.grad} (Expected 3.0)")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Custom Autograd Engine Graph
  node_a[Leaf Node A (Weight)] $code -> mul[Multiply Op] $cpu
  node_b[Leaf Node B (Input)] $code -> mul
  mul -> add[Add Op (Bias)] $layers
  add -> loss[Loss Value] $brain
  loss -> topo_back[Reverse Topological Backward Pass] $terminal *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Andrej Karpathy micrograd repo", "url": "https://github.com/karpathy/micrograd"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        },

        # =========================================================================
        # MODULE 5: Attention & Transformers Under the Hood
        # =========================================================================
        {
            "phase_slug": "phase-2-core-ml-deeplearning",
            "module_number": 5,
            "slug": "attention-and-transformers-under-the-hood",
            "real_world_deliverable": "Mini-GPT Decoder-Only Language Model Trained on Urdu Poetry",
            "zero_gpu_recipe": {
                'platform': 'Google Colab Free Tier (T4 GPU)',
                'vram_required': '4 GB VRAM',
                'estimated_cost': '$0.00 Free',
                'compute_units_tip': 'A 6-layer Mini-GPT trains on Colab Free T4 GPU in 12 minutes on Shakespeare/Urdu corpus without paid compute units.',
                'one_click_command': 'pip install torch tiktoken datasets && python train_gpt.py'
            },
            "title": "Module 5: Attention & Transformers Under the Hood",
            "weeks_range": "Weeks 8-9",
            "estimated_hours": 18,
            "learning_outcomes": [
                "Scaled Dot-Product Attention: Query, Key, Value matrix mechanics",
                "Multi-Head Attention (MHA) projections and latent subspace alignment",
                "Tokenization deep dive: Byte-Pair Encoding (BPE) & Tiktoken",
                "Rotary Position Embeddings (RoPE) vs Sinusoidal encodings",
                "Architectural taxonomy: BERT vs GPT vs T5 paradigms",
                "Building, training, and autoregressively sampling from a Mini-GPT in pure PyTorch"
            ],
            "practical_tasks": [
                "Raw PyTorch tensors ke sath Scaled Dot-Product Attention implement karein",
                "Causal lower-triangular attention mask implement karein to prevent looking ahead",
                "Byte-Pair Encoding merge table zero libraries ke sath build karein",
                "RoPE 2D complex plane rotation function implement karein",
                "Complete Mini-GPT causal language model construct karein and sample generations"
            ],
            "resources": [
                {"title": "Attention Is All You Need Paper", "url": "https://arxiv.org/abs/1706.03762"},
                {"title": "The Illustrated Transformer", "url": "https://jalammar.github.io/illustrated-transformer/"}
            ],
            "diagram_script": """@preset midnight
@animate pulse
arch LR: Full Transformer Block Pipeline
  in_tok[Input Token Embeddings] $terminal -> norm1[LayerNorm 1] $cpu
  norm1 -> mha[Multi-Head Attention] $brain
  mha -> add1[Residual Add] $layers
  in_tok -> add1
  add1 -> norm2[LayerNorm 2] $cpu
  norm2 -> ffn[Feed-Forward Network (GELU)] $cube
  ffn -> add2[Residual Add] $layers *
  add1 -> add2""",
            "diagram_preset": "midnight",
            "diagram_animation": "pulse",
            "badge_slug": "transformer-expert",
            "order_index": 5,
            "lessons": [
                {
                    "lesson_code": "5.1",
                    "slug": "self-attention-math",
                    "title": "Self-Attention Mechanism: Q, K, V Matrices Ka Khel",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, modern AI ki tareekh ka sab se bara milestone 2017 ka paper tha: *"Attention Is All You Need"*. Isne RNNs aur LSTMs ko hamesha ke liye khatam kar diya!

RNNs sequential thay — word by word process karte thay, jis ki wajah se GPU parallelization na-mumkin thi.
Transformer ka dil hai **Scaled Dot-Product Attention**:
$$\\text{Attention}(Q, K, V) = \\text{Softmax}\\left(\\frac{Q K^T}{\\sqrt{d_k}}\\right) V$$

Is formula ko aasan zubaan mein samjhein:
1. **Query ($Q$)**: "Main kya dhoond raha hoon?" (Maslan word "bank" pooche ga: "kya main river bank hoon ya financial bank?")
2. **Key ($K$)**: "Mere pas kya information hai?" Har token apni pehchan announce karta hai.
3. **Value ($V$)**: Asal semantic content jo doosre tokens ko pass hona hai.
4. **$\\sqrt{d_k}$ se divide kyun karte hain?**: Jab dimension $d_k$ bara hota hai to dot product bohot bara ho jata hai, jis se Softmax ke gradients vanish ho jate hain. Scale karne se variance 1 rehti hai!""",
                    "english_summary": "Master the mathematical formulation of Scaled Dot-Product Attention: Query, Key, Value projections, dot products, scaling factor, and softmax weights.",
                    "code_example": """import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor, mask: torch.Tensor = None):
    d_k = Q.size(-1)
    # 1. MatMul Q and K^T -> (Batch, Heads, Seq_Q, Seq_K)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    
    # 2. Apply Causal Mask if provided (to prevent looking at future tokens)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))
        
    # 3. Softmax along last dimension -> Attention Weights
    attn_weights = F.softmax(scores, dim=-1)
    
    # 4. Multiply with Value matrix V
    output = torch.matmul(attn_weights, V)
    return output, attn_weights

# Demonstration: Sequence of 3 tokens, Embedding Dim 4
Q = torch.randn(1, 1, 3, 4)
K = torch.randn(1, 1, 3, 4)
V = torch.randn(1, 1, 3, 4)

out, weights = scaled_dot_product_attention(Q, K, V)
print("Attention Output Shape:", out.shape)
print("Attention Weights Matrix:\\n", weights[0, 0].detach().numpy().round(3))""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Scaled Dot-Product Attention
  q[Query Matrix Q] $terminal -> matmul[MatMul Q * K^T] $cpu
  k[Key Matrix K] $terminal -> matmul
  matmul -> scale[Scale 1 / sqrt(d_k)] $layers
  scale -> softmax[Softmax Normalization] $brain
  softmax -> v_mul[MatMul with Value V] $cube *
  v[Value Matrix V] $terminal -> v_mul""",
                    "diagram_type": "flow",
                    "resources": [{"title": "Vaswani et al. (Attention Is All You Need)", "url": "https://arxiv.org/abs/1706.03762"}],
                    "xp_reward": 30,
                    "order_index": 1
                },
                {
                    "lesson_code": "5.2",
                    "slug": "multihead-attention-blocks",
                    "title": "Multi-Head Attention & Transformer Block Architecture",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, single attention head sirf ek qism ka relationship capture kar sakta hai (maslan verb aur subject ka connection). Lekin real language mein hazaron patterns hote hain: rhyming, sentiment, factual references, etc.

Is liye hum embedding ko multiple heads (jaise 8, 16, ya 32 heads) mein split karte hain. Har head alag latent subspace mein attend karta hai.
Phir sabhi heads ke outputs ko concatenate karke ek projection layer se pass kiya jata hai.

Iske sath hi Transformer Block mein do cheezein hoti hain:
1. **Residual Connections (Skip Connections)**: Gradient vanishing se bachne ke liye input ko direct output mein add kiya jata hai: $x + \\text{Sublayer}(x)$.
2. **RMSNorm / LayerNorm**: Activations ki scale ko stable rakhne ke liye.""",
                    "english_summary": "Construct complete Transformer blocks combining multi-head attention projections, residual additions, RMSNorm, and Feed-Forward Networks.",
                    "code_example": """import torch
import torch.nn as nn

class TransformerBlock(nn.Module):
    def __init__(self, embed_dim: int, num_heads: int, mlp_dim: int):
        super().__init__()
        self.norm1 = nn.LayerNorm(embed_dim)
        self.attn = nn.MultiheadAttention(embed_dim, num_heads, batch_first=True)
        self.norm2 = nn.LayerNorm(embed_dim)
        self.mlp = nn.Sequential(
            nn.Linear(embed_dim, mlp_dim),
            nn.GELU(),
            nn.Linear(mlp_dim, embed_dim)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        norm_x = self.norm1(x)
        attn_out, _ = self.attn(norm_x, norm_x, norm_x)
        x = x + attn_out
        x = x + self.mlp(self.norm2(x))
        return x

block = TransformerBlock(embed_dim=64, num_heads=4, mlp_dim=256)
tokens = torch.randn(2, 10, 64)
out = block(tokens)
print("Transformer Block Output Shape:", out.shape)""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Full Transformer Block Pipeline
  in_tok[Input Token Embeddings] $terminal -> norm1[LayerNorm 1] $cpu
  norm1 -> mha[Multi-Head Attention] $brain
  mha -> add1[Residual Add] $layers
  in_tok -> add1
  add1 -> norm2[LayerNorm 2] $cpu
  norm2 -> ffn[Feed-Forward Network (GELU)] $cube
  ffn -> add2[Residual Add] $layers *
  add1 -> add2""",
                    "diagram_type": "arch",
                    "resources": [{"title": "Transformers Architecture Deep Dive", "url": "https://huggingface.co/docs/transformers/index"}],
                    "xp_reward": 30,
                    "order_index": 2
                },
                {
                    "lesson_code": "5.3",
                    "slug": "tokenization-bpe-tiktoken",
                    "title": "Tokenization Deep Dive: Byte-Pair Encoding (BPE) & Tiktoken",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, agar aap text ko character-by-character feed karein to sequence length 10x barh jati hai (O(N^2) attention collapse). Agar word-by-word karein to vocabulary mein lakhoon words chahiye hotay hain aur out-of-vocabulary (OOV) words fail ho jate hain.

Iska universal solution hai **Byte-Pair Encoding (BPE)**:
Shuru mein har character ek token hota hai. Phir training dataset mein jo do tokens sab se zyada ek sath aate hain (highest frequency pair), unko merge karke ek naya single token bana diya jata hai.
Maslan: 'u' + 'r' -> 'ur', 'ur' + 'du' -> 'urdu'.

OpenAI ka `tiktoken` Rust mein implement kiya gaya hai aur per second 1 million tokens tokenize kar sakta hai!""",
                    "english_summary": "Understand subword tokenization mechanics, the Byte-Pair Encoding (BPE) iterative merge algorithm, vocabulary construction, and tiktoken.",
                    "code_example": """from collections import Counter

# Mini BPE Algorithm Demonstration
corpus = ["low", "lower", "newest", "widest"]

def get_stats(vocab):
    pairs = Counter()
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[symbols[i], symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, v_in):
    v_out = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in v_in:
        w_out = word.replace(bigram, replacement)
        v_out[w_out] = v_in[word]
    return v_out

vocab = {'l o w </w>': 5, 'l o w e r </w>': 2, 'n e w e s t </w>': 6, 'w i d e s t </w>': 3}
for i in range(5):
    pairs = get_stats(vocab)
    if not pairs: break
    best_pair = pairs.most_common(1)[0][0]
    vocab = merge_vocab(best_pair, vocab)
    print(f"BPE Merge Step {i+1}: Best Pair {best_pair}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Byte-Pair Encoding (BPE) Pipeline
  raw_text[Raw Text Stream] $terminal -> utf8_bytes[UTF-8 Byte Split] $code
  utf8_bytes -> pair_count[Pair Frequency Counter] $cpu
  pair_count -> merge_table[Iterative Merge Rules] $database
  merge_table -> token_ids[Compressed Token IDs] $brain *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "OpenAI Tiktoken Repo", "url": "https://github.com/openai/tiktoken"}
                    ],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "5.4",
                    "slug": "rotary-embeddings-rope-pos",
                    "title": "Rotary Position Embeddings (RoPE) & Context Length Scaling",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, Self-Attention inherently permutation-invariant hoti hai — yaani agar aap sentence ke words ko aage peeche kar dein to dot product ka answer same rehta hai! Is liye model ko position batana lazmi hota hai.

Vaswani 2017 ne Sinusoidal positional encodings use kiye jo absolute positions thay. Lekin absolute position se model kabhi bhi train-length se lambe documents extrapolate nahi kar pata tha.

Modern LLMs (Llama 3, DeepSeek, Mistral) **RoPE (Rotary Position Embedding)** use karte hain:
Query aur Key vectors ko 2D complex plane mein rotation angle se multiply kiya jata hai: $R_{\\theta, m} q$.
Iska jadoo yeh hai ke dot product lene par absolute positions cancel ho jati hain aur sirf **Relative Distance ($m - n$)** bachta hai:
$$\\langle R_m q, R_n k \\rangle = g(q, k, m - n)$$
Isi mathematical beauty ki wajah se context window 4k se 128k tokens tak scale hoti hai!""",
                    "english_summary": "Understand why self-attention requires positional encodings and how Rotary Position Embeddings (RoPE) rotate Q and K in complex 2D planes.",
                    "code_example": """import torch

def apply_rotary_pos_emb(x: torch.Tensor, seq_len: int):
    # Dim must be even for 2D complex pairs
    dim = x.size(-1)
    inv_freq = 1.0 / (10000 ** (torch.arange(0, dim, 2).float() / dim))
    t = torch.arange(seq_len, dtype=torch.float32)
    freqs = torch.outer(t, inv_freq)
    
    # cos and sin embeddings
    cos = freqs.cos().repeat_interleave(2, dim=-1)
    sin = freqs.sin().repeat_interleave(2, dim=-1)
    
    # Rotate 2D pairs: [-x2, x1, -x4, x3, ...]
    x_rotated = torch.stack([-x[..., 1::2], x[..., 0::2]], dim=-1).flatten(-2)
    return (x * cos) + (x_rotated * sin)

q = torch.randn(1, 4, 16) # Batch 1, Seq 4, Dim 16
q_rope = apply_rotary_pos_emb(q, seq_len=4)
print("RoPE Successfully Applied. Output Shape:", q_rope.shape)""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Rotary Position Embedding (RoPE)
  query_vec[Query Vector Q] $layers -> rotate_q[2D Complex Rotation Matrix R_m] $brain
  key_vec[Key Vector K] $layers -> rotate_k[2D Complex Rotation Matrix R_n] $brain
  rotate_q -> dot_prod[Dot Product (Preserves Relative m-n)] $cube *
  rotate_k -> dot_prod""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "RoFormer: Enhanced Transformer with Rotary Position Embedding", "url": "https://arxiv.org/abs/2104.09864"}
                    ],
                    "xp_reward": 30,
                    "order_index": 4
                },
                {
                    "lesson_code": "5.5",
                    "slug": "encoder-decoder-paradigms",
                    "title": "Architectural Paradigms: BERT vs GPT vs T5",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, Transformers ki dunya mein teen mukhtalif architectural families aayi hain:
1. **Encoder-Only (BERT)**: Ismein koi mask nahi hota, har token aage aur peeche tamam tokens ko dekh sakta hai (Bidirectional). Best for Classification aur Embedding generation.
2. **Decoder-Only (GPT, Llama, DeepSeek)**: Ismein **Causal Lower-Triangular Mask** hota hai. Token sirf pichle tokens dekh sakta hai, mustaqbil ke tokens nahi dekh sakta. Best for Autoregressive Generation.
3. **Encoder-Decoder (T5, BART)**: Ismein do blocks hote hain jo Cross-Attention se connect hote hain. Best for Translation aur Summarization.

2026 mein dunya **Decoder-Only** par kyun mutafiq ho gayi?
Kyunke Decoder-Only models simple hote hain, KV Cache implement karna aasan hota hai, aur scaling laws (Compute vs Loss) sab se predictable follow karte hain!""",
                    "english_summary": "Compare the 3 major transformer paradigms: Encoder-Only (BERT), Decoder-Only (GPT), and Encoder-Decoder (T5), and understand why Decoder-Only won.",
                    "code_example": """import torch

# Demonstrate Causal Mask vs Bidirectional Mask
seq_len = 4
causal_mask = torch.tril(torch.ones(seq_len, seq_len))
print("Causal Mask (Decoder-Only GPT): Token can only see past tokens:")
print(causal_mask.numpy())

bidirectional_mask = torch.ones(seq_len, seq_len)
print("\\nBidirectional Mask (Encoder-Only BERT): Token sees all tokens:")
print(bidirectional_mask.numpy())""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Transformer Architectural Taxonomy
  bert[Encoder-Only (BERT): Bidirectional] $brain -> tasks1[Classification & Embeddings] $layers
  gpt[Decoder-Only (GPT/Llama): Causal Mask] $server -> tasks2[Autoregressive Text Generation] $terminal *
  t5[Encoder-Decoder (T5): Cross-Attention] $cube -> tasks3[Seq2Seq Translation & Summary] $database""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Illustrated GPT-2", "url": "https://jalammar.github.io/illustrated-gpt2/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "5.6",
                    "slug": "module-5-capstone-minigpt",
                    "title": "Module 5 Capstone: Build a Complete Mini-GPT from Scratch in PyTorch",
                    "duration_minutes": 60,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, this is IT! Module 5 ka Grand Capstone: **Ek Mukammal Decoder-Only Mini-GPT Model from Scratch in PyTorch**!

Aap tamam seekhi hui cheezon ko ek single executable script mein integrate karenge:
1. Token Embedding Layer + Positional Embedding Layer.
2. N Multi-Head Causal Self-Attention Blocks with Residual Connections & LayerNorm.
3. Final Projection LM Head jo vocabulary logits return kare.
4. An Autoregressive `generate()` loop jo greedy sampling se text continue kare!

Yeh script run karte hi aap official taur par Transformer Engineer ban jayenge!""",
                    "english_summary": "Construct and train a complete, runnable Mini-GPT causal autoregressive language model in pure PyTorch and generate text from a prompt.",
                    "code_example": """import torch
import torch.nn as nn
import torch.nn.functional as F

class MiniGPT(nn.Module):
    def __init__(self, vocab_size=1000, embed_dim=64, num_heads=4, num_layers=2, max_len=64):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab_size, embed_dim)
        self.pos_emb = nn.Embedding(max_len, embed_dim)
        
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim, nhead=num_heads, dim_feedforward=embed_dim*4, 
            batch_first=True, activation="gelu"
        )
        self.blocks = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.ln_f = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, vocab_size, bias=False)
        self.max_len = max_len

    def forward(self, idx):
        B, T = idx.shape
        pos = torch.arange(0, T, device=idx.device)
        x = self.tok_emb(idx) + self.pos_emb(pos)
        
        # Causal mask for autoregressive generation
        mask = nn.Transformer.generate_square_subsequent_mask(T, device=idx.device)
        x = self.blocks(x, mask=mask, is_causal=True)
        logits = self.head(self.ln_f(x))
        return logits

    @torch.no_grad()
    def generate(self, idx, max_new_tokens=10):
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -self.max_len:]
            logits = self(idx_cond)
            next_token = torch.argmax(logits[:, -1, :], dim=-1, keepdim=True)
            idx = torch.cat((idx, next_token), dim=1)
        return idx

model = MiniGPT(vocab_size=200, embed_dim=32, num_heads=2, num_layers=2)
prompt = torch.tensor([[10, 24, 55]]) # 3 input tokens
generated = model.generate(prompt, max_new_tokens=5)
print("Mini-GPT Generated Token IDs:", generated.tolist())""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Complete Mini-GPT Architecture
  in_indices[Token Indices (B, T)] $terminal -> tok_emb[Token + Pos Embeddings] $layers
  tok_emb -> tf_blocks[N x Causal Transformer Blocks] $brain
  tf_blocks -> ln_f[Final LayerNorm] $cpu
  ln_f -> lm_head[Linear LM Head (Vocab Size)] $server
  lm_head -> logits[Next Token Logits & Sampling] $cube *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "NanoGPT by Andrej Karpathy", "url": "https://github.com/karpathy/nanoGPT"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        }
    ]
    return modules
