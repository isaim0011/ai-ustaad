import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))

checkpoints = {
    0: {
        "title": "Chai Shop Billing & Khata Management Engine",
        "urdu_title": "Chai Dhaba Billing & Munshi CLI",
        "description": "Dhabay aur chai shop ke liye real-time terminal billing tool. Har customer ka order (Doodh Patti, Elaichi Chai, Paratha), tax, discount calculate kare aur JSON khata file mein daily report append kare!",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod0_chai_billing",
        "checklist": [
            "@dataclass for MenuItem & OrderBill with auto-validation",
            "Interactive while loop CLI with clean input sanitization",
            "JSON persistence for daily transactions khata",
            "Discount & sales tax automated calculation",
            "Summary report generator showing top-selling item & profit"
        ],
        "xp_reward": 100,
        "badge_name": "chai-munshi"
    },
    1: {
        "title": "Biryani vs Pulao Sentiment & Price Vectorizer",
        "urdu_title": "Biryani vs Pulao Sentiment Analyzer",
        "description": "Karahi, Biryani aur Pulao ke 50,000 food reviews ko pure Python vs NumPy vectorized arrays se analyze karein. Cosine similarity se find karein ke kiske reviews mein sab se zyada 'Lazeez' aur 'Mirchi' ka vector overlap hai!",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod1_biryani_sentiment",
        "checklist": [
            "NumPy SIMD vectorized dot product implementation",
            "Zero-copy broadcasting array operations",
            "Cosine similarity calculator without SciPy",
            "50x speedup benchmark vs Python nested loops"
        ],
        "xp_reward": 150,
        "badge_name": "biryani-analyst"
    },
    2: {
        "title": "Rishta Matcher & Bio Compatibility Algorithm",
        "urdu_title": "Rishta Matcher Vector Distance Calculator",
        "description": "Candidate ke CV/Bio aur Mother-in-Law (Saas) ki strict 15-point demand list ke darmiyan high-dimensional embeddings calculate karein. Prompt engineering se 'Red Flags' identify karein aur automated humorous compatibility score generate karein!",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod2_rishta_matcher",
        "checklist": [
            "Few-Shot Chain of Thought prompt engineering",
            "Structured JSON output validation with Pydantic",
            "Negative constraints & Hallucination mitigation rules",
            "Automated compatibility score generation (0-100%)"
        ],
        "xp_reward": 150,
        "badge_name": "rishta-whisperer"
    },
    3: {
        "title": "PSL/IPL Match Outcome & Cricketer Performance Predictor",
        "urdu_title": "Cricketer Performance & Match Winner Predictor",
        "description": "Historical T20 pitch report, dew factor, strike rate, aur player matchups par LightGBM & XGBoost classifier train karein. Match ke 16th over mein live winning probability estimate karein!",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod3_cricket_predictor",
        "checklist": [
            "Data leakage prevention with temporal split",
            "Feature engineering (Strike rate in death overs, economy against spin)",
            "Hyperparameter tuning with Optuna",
            "Precision-Recall & ROC-AUC evaluation"
        ],
        "xp_reward": 150,
        "badge_name": "toss-ka-badshah"
    },
    4: {
        "title": "Desi Meme Classifier & Sarcastic Roast Bot",
        "urdu_title": "Meme Classifier & Roast Engine",
        "description": "PyTorch se custom convolutional/MLP neural network train karein jo viral memes ko detect kare (e.g. 'Sarfaraz Dhoka Nahi Dega' vs 'Disappointed Pakistani Fan') aur instant humorous roast dialogue generate kare.",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod4_meme_roast_bot",
        "checklist": [
            "Custom PyTorch Dataset & DataLoader",
            "CrossEntropyLoss with AdamW & CosineAnnealing",
            "Mixed Precision (AMP) training on Free Colab T4",
            "Model checkpointing and inference visualizer"
        ],
        "xp_reward": 200,
        "badge_name": "meme-roaster"
    },
    5: {
        "title": "Mirza Ghalib vs Allama Iqbal Urdu Poetry Rhyme Engine",
        "urdu_title": "Ghalib vs Iqbal Poetry Mini-GPT",
        "description": "Raw PyTorch tensors se multi-head self-attention transformer likhein jo classic Urdu ghazals ke meter aur qafiya (rhyme) ko seekh kar naye humorous shair complete kare!",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod5_ghalib_gpt",
        "checklist": [
            "Custom Causal Self-Attention mask",
            "Rotary Position Embeddings (RoPE)",
            "Byte-Pair Encoding (BPE) tokenizer integration",
            "Next-token generation with temperature & top-p sampling"
        ],
        "xp_reward": 200,
        "badge_name": "shayar-e-ai"
    },
    6: {
        "title": "Ami Ka WhatsApp Auto-Responder Bot",
        "urdu_title": "Ami Ka WhatsApp Reply Bot",
        "description": "'Beta kahan ho?', 'Roti khayi?', aur 'Dahi le aana' jese WhatsApp messages ke liye production-ready FastAPI streaming server banayein with Server-Sent Events (SSE) and token-rate streaming.",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod6_ami_reply_bot",
        "checklist": [
            "FastAPI async route with StreamingResponse",
            "Pydantic V2 request & response schemas",
            "In-memory token-bucket rate limiter",
            "CORS & Bearer token authorization middleware"
        ],
        "xp_reward": 200,
        "badge_name": "farmanbardar-beta"
    },
    7: {
        "title": "Grandma's Secret Biryani Recipe RAG Engine",
        "urdu_title": "Nani Amma Biryani Recipe RAG Search",
        "description": "Scanned handwritten recipe notes aur secret spices PDF documents ko PostgreSQL pgvector hybrid search (BM25 + Dense) se index karein. Query: 'Agar namak tez ho jaye to kya karein?' -> exact potaato trick cite kare!",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod7_secret_biryani_rag",
        "checklist": [
            "pgvector HNSW index creation in PostgreSQL",
            "Reciprocal Rank Fusion (RRF) for Hybrid search",
            "Cross-Encoder re-ranking with FlashRank",
            "Strict source citation grounding prompt"
        ],
        "xp_reward": 250,
        "badge_name": "bawarchi-rag"
    },
    8: {
        "title": "Aggressive Salary Negotiation AI Agent Swarm",
        "urdu_title": "Salary Negotiation Multi-Agent Swarm",
        "description": "Anthropic Model Context Protocol (MCP) aur smolagents use karte hue 3 agents ka swarm banayein (Analyst, Market Researcher, Hardball Negotiator) jo remote USD salary packages par counter-offers draft kare!",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod8_salary_negotiator",
        "checklist": [
            "Custom MCP tool server (Tax Calculator, Glassdoor scraper)",
            "ReAct planning & execution loop",
            "Human-in-the-loop approval checkpoint",
            "Multi-turn counter-offer generation"
        ],
        "xp_reward": 250,
        "badge_name": "dollar-earner"
    },
    9: {
        "title": "Roman Urdu Sarcasm & Roast Fine-Tuning Engine",
        "urdu_title": "Roman Urdu Sarcasm Detector (Unsloth QLoRA)",
        "description": "Free Google Colab T4 par Unsloth 4-bit QLoRA use karke Llama 3.2 3B ya Gemma 2 2B ko fine-tune karein. Model pehchane ke 'Bohot aala bhai!' tareef hai ya taana!",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod9_urdu_sarcasm",
        "checklist": [
            "Unsloth 4-bit FastLanguageModel setup",
            "ChatML dataset packing with assistant masking",
            "LoRA rank 16 / alpha 32 configuration",
            "GGUF Q4_K_M quant export for local inference"
        ],
        "xp_reward": 300,
        "badge_name": "taana-master"
    },
    10: {
        "title": "Phuppo-Proof Family Group Content Guardrail Firewall",
        "urdu_title": "Family Group PII & Jailbreak Firewall",
        "description": "Family WhatsApp groups mein fake news, toxic rishta gossip aur PII leaks ko rokne ke liye NeMo Guardrails + Microsoft Presidio firewall deploy karein jo toxic messages ko polite Roman Urdu mein rewrite kare.",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod10_family_firewall",
        "checklist": [
            "Presidio PII anonymizer (phone, CNIC, address)",
            "Semantic jailbreak detection rail",
            "Ragas faithfulness evaluation metric",
            "Automated GitHub Actions CI eval runner"
        ],
        "xp_reward": 300,
        "badge_name": "sulah-joo"
    },
    11: {
        "title": "Sub-50ms High-Scale AI Microservice Gateway",
        "urdu_title": "Sub-50ms Rust Axum LLM Gateway",
        "description": "Rust Axum mein high-throughput proxy gateway banayein jo Groq, Cerebras aur vLLM clusters ke darmiyan round-robin load balance kare with automated failover aur sub-50ms latency.",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod11_rust_gateway",
        "checklist": [
            "Rust Axum async route handlers",
            "Token-bucket rate limiter per API key",
            "Multi-provider health check & circuit breaker",
            "OpenTelemetry distributed tracing"
        ],
        "xp_reward": 350,
        "badge_name": "rocket-engineer"
    },
    12: {
        "title": "Handwritten Doctor Prescription & Urdu Audio Transcriber",
        "urdu_title": "Doctor Prescription OCR & Audio Transcriber",
        "description": "Doctor ki tehrir (handwritten bad handwriting) aur tez bolay gaye Urdu audio notes ko Whisper Large v3 + Vision LLM se parse karke structured medicine dosage JSON generate karein.",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod12_doctor_ocr",
        "checklist": [
            "Whisper audio chunking & transcription",
            "Vision LLM multimodal prompt with dosage schema",
            "Pydantic JSON schema strict enforcement",
            "Medicine interaction warning system"
        ],
        "xp_reward": 350,
        "badge_name": "hakeem-ai"
    },
    13: {
        "title": "100% Offline Exam Crammer Chatbot",
        "urdu_title": "Offline WebGPU Exam Crammer",
        "description": "Transformers.js + WebGPU ke zariye student ke browser mein Llama-3.2-1B-Instruct model 100% offline run karein taake bina internet / load-shedding ke exam revision ki ja sake.",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod13_offline_crammer",
        "checklist": [
            "WebGPU device initialization in JavaScript",
            "ONNX / Transformers.js quantized model loading",
            "Zero-server edge inference loop",
            "Local browser IndexedDB chat persistence"
        ],
        "xp_reward": 400,
        "badge_name": "bijli-proof"
    },
    14: {
        "title": "Global AI Micro-SaaS Capstone Defense",
        "urdu_title": "Commercial AI SaaS Capstone Launch",
        "description": "Supabase Auth, PostgreSQL RLS, Stripe billing aur Cloudflare Pages deployment ke sath ek commercial AI SaaS banayein aur live internet par launch karein!",
        "colab_url": "https://colab.research.google.com/drive/1ai_ustaad_mod14_capstone_defense",
        "checklist": [
            "Multi-tenant Supabase schema with RLS",
            "Stripe webhook payment integration",
            "Production deployment on Cloudflare Pages",
            "Live 60-second video demo & GitHub repository"
        ],
        "xp_reward": 500,
        "badge_name": "unicorn-founder"
    }
}

module_0_definition = {
    "phase_slug": "phase-1-foundations",
    "module_number": 0,
    "slug": "python-zero-se-hero",
    "real_world_deliverable": "Chai Dhaba Billing Engine & Khata Management CLI",
    "zero_gpu_recipe": {
        'platform': 'Local Terminal / Google Colab Free Tier',
        'vram_required': '0 GB (Any CPU / Laptop)',
        'estimated_cost': '$0.00 Free',
        'compute_units_tip': 'Pure Python logic runs 100% locally on any basic laptop or Colab CPU without requiring GPU compute.',
        'one_click_command': 'python -m pip install tabulate rich && python chai_billing.py'
    },
    "practice_checkpoint": checkpoints[0],
    "title": "Module 0: Python Zero Se Hero (Prerequisite Track: Pehle Python, Phir AI)",
    "weeks_range": "Prerequisite / Week 0",
    "estimated_hours": 12,
    "learning_outcomes": [
        "Python interpreter, REPL, aur dynamic typing mental model",
        "Core data structures: Lists, Tuples, Sets, Dictionaries aur List Comprehensions",
        "Clean modular functions: Scope, Closures, *args, **kwargs aur Lambdas",
        "Object-Oriented Programming (OOP) for AI: Classes, Inheritance, Dunder Methods aur @dataclass",
        "File I/O, JSON serialization, exception handling aur REST API calls with requests",
        "NumPy vector basics aur Pandas DataFrame tabular manipulation for AI data ingestion"
    ],
    "practical_tasks": [
        "Chai Dhaba Billing CLI script with @dataclass & JSON storage likhein",
        "Nested dictionary se customer orders ka structured JSON report generate karein",
        "Pure Python list comprehension se complex data filter aur transform karein",
        "Custom class banayein with __repr__, __len__, aur custom property methods",
        "Public REST API se JSON data fetch karke Pandas DataFrame mein load karein"
    ],
    "resources": [
        {"title": "Python 3.12 Official Tutorial", "url": "https://docs.python.org/3/tutorial/"},
        {"title": "Automate the Boring Stuff with Python", "url": "https://automatetheboringstuff.com/"},
        {"title": "Google Colab Python Beginner Guide", "url": "https://colab.research.google.com/"}
    ],
    "diagram_script": """@preset midnight
@animate flow
flow LR: Python Zero Se Hero Learning Journey
  syntax[0.1 Syntax & Mental Model] $code -> struct[0.2 Lists, Dicts & Tuples] $database
  struct -> func[0.3 Functions & *args] $terminal
  func -> oop[0.4 OOP & @dataclass] $box
  oop -> io[0.5 File I/O & JSON APIs] $cloud
  io -> np[0.6 NumPy & Pandas Intro] $cpu *""",
    "diagram_preset": "midnight",
    "diagram_animation": "flow",
    "badge_slug": "chai-munshi",
    "order_index": 0,
    "lessons": [
        {
            "lesson_code": "0.1",
            "slug": "python-mental-model-syntax",
            "title": "Python Mental Model, Setup & Fast Syntax (Interpreter, Variables & Conditionals)",
            "duration_minutes": 30,
            "lesson_type": "theory_and_code",
            "roman_urdu_content": """Khush-Aamdeed! Yeh hamara **Python Zero Se Hero** track hai jo un doston ke liye design kiya gaya hai jinhon ne pehle kabhi coding nahi ki ya Python ka basic syntax refresh karna chahte hain.

### 1. Python Ka Mental Model: Yeh Kaise Kaam Karta Hai?
C++ ya Rust ke bar-aks, jahan code pehle machine code mein compile hota hai, Python ek **interpreted bytecode** language hai. Jab aap `python main.py` likhte hain, to:
1. Python parser aapke code ko syntax tree mein convert karta hai.
2. CPython compiler isay `.pyc` bytecode mein translate karta hai.
3. CPython Virtual Machine (VM) is bytecode ko line-by-line execute karti hai.

### 2. Variables & Dynamic Typing
Python mein variables sirf ek pointer/label hote hain jo memory mein kisi object ki taraf point karte hain:
```python
x = 42          # x points to integer object 42
x = "AI Ustaad" # Ab wahi x string object ki taraf point kar raha hai
```
Isay **Dynamic Typing** kehte hain. AI pipelines mein clean code ke liye hum modern Python 3.12 **Type Hints** use karte hain:
```python
model_name: str = "llama-3.2"
batch_size: int = 32
learning_rate: float = 0.001
is_training: bool = True
```

### 3. Conditionals & Modern Match-Case
Python 3.10+ mein modern structural pattern matching introduce hui jo complex if/else chains ko clean banati hai:
```python
def route_model(task: str) -> str:
    match task:
        case "chat" | "reasoning":
            return "deepseek-r1"
        case "vision":
            return "siglip-clip"
        case _:
            return "llama-3.2-3b"
```""",
            "english_summary": "Understand Python's CPython bytecode VM architecture, dynamic typing, type annotations, truthy/falsy evaluation, and modern Python 3.10+ match-case syntax.",
            "code_example": """# Python Foundations: Mental Model & Fast Syntax
import sys

# 1. Type annotations & Variables
app_name: str = "AI Ustaad Dhaba Billing"
version: float = 1.0
active_tables: int = 12

print(f"[{app_name} v{version}] Python Interpreter: {sys.version.split()[0]}")

# 2. Modern Walrus Operator (:=) for in-line evaluation
while (user_input := input("Item code daalein (ya 'exit' likhein): ").strip().lower()) != 'exit':
    # 3. Match-Case Pattern Matching
    match user_input:
        case "c1" | "chai":
            price = 60
            print(f"Doodh Patti Selected! Price: Rs {price}")
        case "p1" | "paratha":
            price = 120
            print(f"Lachha Paratha Selected! Price: Rs {price}")
        case _:
            print("Invalid code! Try 'c1' ya 'p1'.")
    break""",
            "diagram_script": """@preset midnight
@animate flow
flow LR: Python Bytecode Virtual Machine Loop
  src[Python Source .py] $code -> comp[CPython Bytecode Compiler] $cpu
  comp -> pyc[.pyc Bytecode Instructions] $database
  pyc -> vm[CPython Execution Loop] $server
  vm -> out[Console Output / State] $terminal *""",
            "diagram_type": "flow",
            "resources": [{"title": "Python 3.12 Official Tutorial", "url": "https://docs.python.org/3/tutorial/"}],
            "xp_reward": 15,
            "order_index": 1
        },
        {
            "lesson_code": "0.2",
            "slug": "python-data-structures-deep-dive",
            "title": "Data Structures Deep-Dive: Lists, Tuples, Sets, Dictionaries & Comprehensions",
            "duration_minutes": 35,
            "lesson_type": "theory_and_code",
            "roman_urdu_content": """AI Engineering mein data ko sahi structure mein rakhna sab se zaroori skill hai. Chaliye Python ke 4 bunyadi data structures ko first-principles se samjhein:

### 1. Lists: Dynamic Arrays (Order Preserved, Mutable)
Python ki `list` C-array of pointers hoti hai. Jab list bharti hai, Python automatically 1.125x capacity over-allocate kar leta hai taake har append par realloc na karna paray.
* Lookup by index: $O(1)$ fast!
* Append at end: $O(1)$ amortized fast!
* Search by value (`x in my_list`): $O(N)$ slow!

### 2. Tuples: Immutable Arrays
Tuples list jese hote hain lekin banne ke baad badal nahi sakte (`immutable`). Iska faida:
1. Memory overhead 30% kam hota hai.
2. Dictionary ke keys ban sakte hain kyunke inka hash constant rehta hai.

### 3. Sets: Unordered Unique Hash Tables
Sets duplicate values ko allow nahi karte aur Hash Table par chalte hain.
* Search (`x in my_set`): $O(1)$ instant!
* AI vocabulary tokens deduplicate karne ke liye perfect!

### 4. Dictionaries: Key-Value Hash Maps
Python 3.7+ mein Dictionaries insertion order preserve karti hain.
```python
customer_orders = {
    "order_101": {"item": "Doodh Patti", "qty": 2, "price": 60},
    "order_102": {"item": "Karak Chai", "qty": 1, "price": 50}
}
```

### 5. Comprehensions: Fast Pythonic Transformations
Loop likhne ke bajaye single-line vectorized syntax:
```python
prices = [60, 120, 50, 40]
discounted = [p * 0.9 for p in prices if p > 50]
```""",
            "english_summary": "Deep dive into Python built-in collections: memory mechanics, algorithmic time complexity, hash tables, sets for token deduplication, and idiomatic comprehensions.",
            "code_example": """# Data Structures & Comprehensions
import time

# 1. List vs Set Lookup Benchmark
dataset_size = 100_000
raw_tokens = [f"token_{i}" for i in range(dataset_size)]
token_set = set(raw_tokens)

target = "token_99999"

# Measure List scan O(N)
t0 = time.perf_counter()
found_in_list = target in raw_tokens
t_list = time.perf_counter() - t0

# Measure Set hash lookup O(1)
t0 = time.perf_counter()
found_in_set = target in token_set
t_set = time.perf_counter() - t0

print(f"List Lookup O(N): {t_list*1000:.4f} ms")
print(f"Set Lookup O(1):  {t_set*1000:.4f} ms")
print(f"Speedup: {t_list / max(t_set, 1e-9):.1f}x tez!")

# 2. Dictionary Comprehension for Chai Menu
menu = {"chai": 60, "paratha": 120, "bun_kabab": 150}
taxed_menu = {item: round(price * 1.16, 2) for item, price in menu.items()}
print("Menu with 16% GST:", taxed_menu)""",
            "diagram_script": """@preset midnight
@animate pulse
flow LR: Data Structure Lookup Performance
  list_scan[List Linear Scan O(N)] $code -> mem_slow[Sequential Pointer Chasing] $alert
  set_hash[Set / Dict Hash Lookup O(1)] $database -> mem_fast[Direct Hash Bucket Jump] $ok *""",
            "diagram_type": "flow",
            "resources": [{"title": "Python Time Complexity Documentation", "url": "https://wiki.python.org/moin/TimeComplexity"}],
            "xp_reward": 20,
            "order_index": 2
        },
        {
            "lesson_code": "0.3",
            "slug": "python-functions-scope-closures",
            "title": "Functions, Scope, Closures, *args/**kwargs & Lambda Functions",
            "duration_minutes": 30,
            "lesson_type": "theory_and_code",
            "roman_urdu_content": """AI applications mein har model pipeline, inference engine, aur data cleaner modular functions par depend karta hai.

### 1. Functions Are First-Class Citizens
Python mein function koi alag makhlooq nahi hai, balki ek standard object hai! Iska matlab:
* Aap function ko variable mein assign kar sakte hain.
* Function ko doosre function ke andar argument ke taur par pass kar sakte hain (Callbacks).
* Function se naya function return kar sakte hain (Higher-Order Functions & Closures).

### 2. Variable Scope: LEGB Rule
Python variable ko dhoondte waqt 4 darjaat check karta hai:
1. **L (Local):** Function ke andar define kiya gaya variable.
2. **E (Enclosing):** Nested function ke parent function ka scope.
3. **G (Global):** File / Module level ka scope.
4. **B (Built-in):** Python ke apne functions jese `print`, `len`, `range`.

### 3. *args aur **kwargs: Flexible Parameter Dispatching
Jab aapko pehle se pata na ho ke function mein kitne arguments aayenge (jese AI model inference parameters):
* `*args`: Saare positional arguments ko **Tuple** bana kar accept karta hai.
* `**kwargs`: Saare named keyword arguments ko **Dictionary** bana kar accept karta hai.

### 4. Function Decorators: Logging & Telemetry
Decorator ek aisa function hota hai jo kisi doosre function ke gird wrapper bana kar uski behavior ko extend karta hai bina original code ko chhere:
```python
def log_execution(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__}...")
        return fn(*args, **kwargs)
    return wrapper
```""",
            "english_summary": "Master first-class functions, the LEGB scope hierarchy, variable arguments dispatching with *args/**kwargs, closures, and observability decorators.",
            "code_example": """import time
from functools import wraps

# 1. Production Decorator: Telemetry & Benchmark
def benchmark(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = fn(*args, **kwargs)
        duration = time.perf_counter() - t0
        print(f"[Benchmark] {fn.__name__} executed in {duration*1000:.3f} ms")
        return result
    return wrapper

# 2. Flexible Function with *args and **kwargs
@benchmark
def calculate_chai_bill(base_price: float, *extras, discount_pct: float = 0.0, **metadata):
    total = base_price + sum(extras)
    total -= total * (discount_pct / 100.0)
    print(f"Order for {metadata.get('customer', 'Guest')} at Table {metadata.get('table', 'Counter')}")
    return total

bill = calculate_chai_bill(60.0, 20.0, 15.0, discount_pct=10.0, customer="Aslam Bhai", table=4)
print(f"Final Bill Amount: Rs {bill:.2f}")""",
            "diagram_script": """@preset midnight
@animate wave
flow LR: LEGB Scope Resolution Flow
  l[Local Scope: Inside Function] $code -> e[Enclosing Scope: Parent Def] $box
  e -> g[Global Scope: Module Level] $terminal
  g -> b[Built-in Scope: Python Core] $database *""",
            "diagram_type": "flow",
            "resources": [{"title": "Real Python: Python Decorators Guide", "url": "https://realpython.com/primer-on-python-decorators/"}],
            "xp_reward": 20,
            "order_index": 3
        },
        {
            "lesson_code": "0.4",
            "slug": "python-oop-classes-dataclasses",
            "title": "Object-Oriented Programming (OOP) for AI: Classes, Methods & @dataclass",
            "duration_minutes": 40,
            "lesson_type": "theory_and_code",
            "roman_urdu_content": """PyTorch ka `nn.Module`, Hugging Face ke models, aur LangChain ke components sab Object-Oriented Programming (OOP) par bane hain! Agar aapko classes ki samajh nahi to AI code samajhna namumkin ho jata hai.

### 1. Class Aur Object Ka Falsafa
* **Class:** Blue-print ya Naqsha (jese Ghar ka blue-print).
* **Object / Instance:** Us naqshe par bana hua haqeeqi ghar jo memory mein space leta hai.
* `__init__`: Constructor jo object bante hi execute hota hai.
* `self`: Current instance ka pointer.

### 2. Dunder (Double Underscore) Magic Methods
Python ki asli taqat dunder methods mein hai:
* `__repr__`: Developer-friendly string representation.
* `__len__`: `len(my_object)` call hone par kya return ho.
* `__getitem__`: `my_object[0]` array indexing support karne ke liye (jese PyTorch Dataset).
* `__call__`: Object ko function ki tarah execute karne ke liye `model(input_tensors)`.

### 3. Modern @dataclass(slots=True)
Traditional Python classes mein har instance ke sath ek dynamic dictionary `__dict__` jurti hai jo bohot memory leti hai.
Python 3.10+ mein `@dataclass(slots=True)` use karne se:
1. `__init__`, `__repr__`, aur `__eq__` khud ba khud generate ho jate hain.
2. Memory 25% kam use hoti hai.
3. Attribute lookup 20% fast ho jata hai.""",
            "english_summary": "Understand classes, inheritance, dunder protocols (__call__, __len__, __getitem__), and memory-optimized modern @dataclass with slots.",
            "code_example": """from dataclasses import dataclass, field
from typing import List

# Modern Python 3.12 @dataclass with slots
@dataclass(slots=True)
class MenuItem:
    name: str
    price: float
    category: str = "beverage"

@dataclass(slots=True)
class DhabaOrder:
    order_id: int
    customer_name: str
    items: List[MenuItem] = field(default_factory=list)

    def add_item(self, item: MenuItem):
        self.items.append(item)

    @property
    def total_bill(self) -> float:
        return sum(item.price for item in self.items)

    def __repr__(self) -> str:
        return f"<Order #{self.order_id}: {self.customer_name} ({len(self.items)} items) -> Rs {self.total_bill}>"

# Create Order
order = DhabaOrder(order_id=1, customer_name="Hamza")
order.add_item(MenuItem("Doodh Patti", 60.0))
order.add_item(MenuItem("Samosa", 40.0, category="snack"))
order.add_item(MenuItem("Special Elaichi Chai", 80.0))

print(order)
print(f"Total payable: Rs {order.total_bill:.2f}")""",
            "diagram_script": """@preset midnight
@animate flow
flow LR: OOP Class Memory Optimization
  standard[Standard Python Class] $code -> dict_mem[Instance __dict__ Dynamic Heap] $alert
  dataclass_slot[@dataclass slots=True] $database -> fixed_struct[C-Aligned Fixed Offset Struct] $ok *""",
            "diagram_type": "flow",
            "resources": [{"title": "Python Dataclasses Documentation", "url": "https://docs.python.org/3/library/dataclasses.html"}],
            "xp_reward": 25,
            "order_index": 4
        },
        {
            "lesson_code": "0.5",
            "slug": "python-files-json-apis",
            "title": "File Handling, JSON, Parquet & REST API Requests for Data Harvesting",
            "duration_minutes": 35,
            "lesson_type": "theory_and_code",
            "roman_urdu_content": """AI models bina clean data ke bekaar hain. Is sabaq mein hum seekhein ge ke kaise disk se files read/write ki jati hain, JSON format handle hota hai, aur internet APIs se data harvest kiya jata hai.

### 1. Context Managers: Resource Leaks Ko Khatam Karein
File open karke close karna bhool jana sab se bara memory leak hai. Python ka `with` statement ensure karta hai ke file hamesha band ho chahe koi error hi kyun na aaye:
```python
with open("khata.json", "w", encoding="utf-8") as f:
    f.write(data)
```

### 2. JSON & JSONL: LLM Ka Universal Language
* **JSON:** Single document ya object ke liye perfect.
* **JSONL (JSON Lines):** Har line par ek alag JSON object hota hai. LLM fine-tuning datasets (Unsloth, OpenAI, Anthropic) 100% JSONL format use karte hain kyunke isay pura memory mein load kiye baghair stream kiya ja sakta hai!

### 3. REST API Requests With Error Handling
Internet se data fetch karte waqt hamesha network errors aur API rate limits (429 Too Many Requests) ka khayal rakhna parta hai:
```python
try:
    response = requests.get(api_url, timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")
```""",
            "english_summary": "Learn file stream safety with context managers, JSON/JSONL serialization for LLM datasets, robust try/except error handling, and REST API harvesting.",
            "code_example": """import json
import tempfile
import os

# 1. JSON Persistence (Dhaba Khata File)
khata_data = [
    {"bill_id": 101, "customer": "Bimo", "items": ["Special Chai", "Paratha"], "total": 180},
    {"bill_id": 102, "customer": "Ali", "items": ["Doodh Patti"], "total": 60}
]

with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".jsonl") as tmp:
    # Write as JSON Lines (JSONL) - SOTA AI Dataset standard
    for record in khata_data:
        tmp.write(json.dumps(record) + "\\n")
    tmp_path = tmp.name

print(f"JSONL Saved to temp file: {tmp_path}")

# Read line-by-line streaming (Zero memory spike)
print("\\nStreaming records from disk:")
with open(tmp_path, "r", encoding="utf-8") as f:
    for line in f:
        record = json.loads(line.strip())
        print(f"Bill #{record['bill_id']} -> {record['customer']}: Rs {record['total']}")

os.remove(tmp_path)""",
            "diagram_script": """@preset midnight
@animate flow
flow LR: Data Harvesting & JSONL Storage
  remote_api[Web REST API] $cloud -> parser[HTTP Client & JSON Parser] $terminal
  parser -> validator[Schema Validation] $code
  validator -> jsonl_disk[(Streaming JSONL On Disk)] $database *""",
            "diagram_type": "flow",
            "resources": [{"title": "Python JSON Documentation", "url": "https://docs.python.org/3/library/json.html"}],
            "xp_reward": 25,
            "order_index": 5
        },
        {
            "lesson_code": "0.6",
            "slug": "python-numpy-pandas-foundations",
            "title": "NumPy & Pandas Foundations: Vectors, Matrices & Fast Tabular Manipulation",
            "duration_minutes": 45,
            "lesson_type": "theory_and_code",
            "roman_urdu_content": """Mubarak ho! Aapne pure Python ke tamam zaroori pillars master kar liye hain. Ab hum qadam rakh rahe hain **Numerical & Tabular Python** mein jo AI Engineering ka gateway hai!

### 1. NumPy: High-Performance Numerical Arrays
Python list mein har number ek generic pointer hota hai. Jabke NumPy `ndarray` memory mein ek contiguous binary block hota hai.
* 1D Array = **Vector** (e.g. word embeddings ya feature list)
* 2D Array = **Matrix** (e.g. tabular dataset ya image pixels)
* 3D+ Array = **Tensor** (e.g. batch of transformer attention weights)

NumPy broadcasting se aap bina loop lagaye poore array ko multiply kar sakte hain:
```python
import numpy as np
salaries = np.array([45000, 60000, 85000, 120000])
with_bonus = salaries * 1.15 # Vectorized 15% increase in 1 CPU cycle!
```

### 2. Pandas: Data Analysis & Feature Wrangling
Pandas tabular datasets (CSVs, Excel, SQL queries) ke liye Python ka sab se powerful tool hai:
* `DataFrame`: Row aur Column table structure.
* Filtering: `df[df['sales'] > 1000]`
* Groupby: `df.groupby('city')['revenue'].mean()`

Yeh foundation aapko Module 1: Python for AI & Fast Math ke liye 100% tayar kar deti hai!""",
            "english_summary": "The bridge from pure Python to AI Engineering: NumPy n-dimensional arrays, vector broadcasting, Boolean indexing, and Pandas DataFrame data wrangling.",
            "code_example": """import numpy as np
import pandas as pd

# 1. NumPy Vectorized Operations
prices = np.array([60, 120, 50, 40, 80], dtype=np.float32)
quantities = np.array([10, 4, 15, 8, 6], dtype=np.float32)

# Vectorized Dot Product (Total Revenue)
total_revenue = np.dot(prices, quantities)
print(f"NumPy Vectorized Total Revenue: Rs {total_revenue:.2f}")

# 2. Pandas DataFrame Manipulation
sales_records = {
    "item": ["Doodh Patti", "Lachha Paratha", "Elaichi Chai", "Samosa", "Bun Kabab"],
    "category": ["Chai", "Food", "Chai", "Snack", "Food"],
    "unit_price": [60, 120, 80, 40, 150],
    "units_sold": [120, 45, 60, 80, 35]
}

df = pd.DataFrame(sales_records)
df["total_sales"] = df["unit_price"] * df["units_sold"]

print("\\n--- Dhaba Sales DataFrame ---")
print(df[["item", "category", "total_sales"]])

print("\\nCategory Wise Revenue Summary:")
summary = df.groupby("category")["total_sales"].sum()
print(summary)""",
            "diagram_script": """@preset midnight
@animate pulse
flow LR: The AI Engineering Transition Bridge
  py_syntax[Module 0: Python Core Syntax] $code -> np_vec[Module 0.6: NumPy Vectors] $cpu
  np_vec -> pd_df[Module 0.6: Pandas DataFrames] $database
  pd_df -> ai_math[Module 1: High-Performance Tensors & Fast Math] $brain *""",
            "diagram_type": "flow",
            "resources": [
                {"title": "NumPy Quickstart", "url": "https://numpy.org/doc/stable/user/quickstart.html"},
                {"title": "Pandas 10-Minute Guide", "url": "https://pandas.pydata.org/docs/user_guide/10min.html"}
            ],
            "xp_reward": 30,
            "order_index": 6
        }
    ]
}

def update_phase1_2():
    path = os.path.join(cur_dir, 'seed_modules_phase1_2.py')
    import seed_modules_phase1_2
    modules = seed_modules_phase1_2.get_modules_phase1_2()
    
    # Check if module 0 already exists
    has_mod_0 = any(m['module_number'] == 0 for m in modules)
    if not has_mod_0:
        modules.insert(0, module_0_definition)
    
    # Inject checkpoints for modules 0..5
    for m in modules:
        num = m['module_number']
        if num in checkpoints:
            m['practice_checkpoint'] = checkpoints[num]
            
    # Serialize back
    code = "# seed_modules_phase1_2.py\n# Modules 0 to 5: Python Zero Se Hero + Phase 1 & 2 Core Modules\n# Total 36 comprehensive lessons (6 lessons per module: 0.1-0.6, 1.1-1.6, ..., 5.1-5.6)\n\ndef get_modules_phase1_2():\n    return " + repr(modules) + "\n"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {path} with Module 0 and checkpoints!")

def update_phase3():
    path = os.path.join(cur_dir, 'seed_modules_phase3.py')
    import seed_modules_phase3
    modules = seed_modules_phase3.get_modules_phase3()
    for m in modules:
        num = m['module_number']
        if num in checkpoints:
            m['practice_checkpoint'] = checkpoints[num]
    code = "# seed_modules_phase3.py\n# Phase 3 Modules: 6, 7, 8 (18 comprehensive lessons with checkpoints)\n\ndef get_modules_phase3():\n    return " + repr(modules) + "\n"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {path} with checkpoints!")

def update_phase4():
    path = os.path.join(cur_dir, 'seed_modules_phase4.py')
    import seed_modules_phase4
    modules = seed_modules_phase4.get_modules_phase4()
    for m in modules:
        num = m['module_number']
        if num in checkpoints:
            m['practice_checkpoint'] = checkpoints[num]
    code = "# seed_modules_phase4.py\n# Phase 4 Modules: 9, 10, 11 (18 comprehensive lessons with checkpoints)\n\ndef get_modules_phase4():\n    return " + repr(modules) + "\n"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {path} with checkpoints!")

def update_phase5():
    path = os.path.join(cur_dir, 'seed_modules_phase5.py')
    import seed_modules_phase5
    modules = seed_modules_phase5.get_modules_phase5()
    for m in modules:
        num = m['module_number']
        if num in checkpoints:
            m['practice_checkpoint'] = checkpoints[num]
    code = "# seed_modules_phase5.py\n# Phase 5 Modules: 12, 13, 14 (18 comprehensive lessons with checkpoints)\n\ndef get_modules_phase5():\n    return " + repr(modules) + "\n"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {path} with checkpoints!")

if __name__ == '__main__':
    update_phase1_2()
    update_phase3()
    update_phase4()
    update_phase5()
    print("All seed files successfully updated!")
