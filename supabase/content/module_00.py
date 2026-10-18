# module_00.py
# Module 0: Python Zero Se Hero (Prerequisite Track: Pehle Python, Phir AI)
# Lessons 0.1 to 0.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 0.1: Python Mental Model, Setup & Fast Syntax
# ==============================================================================
LESSON_CONTENT['0.1'] = """### Part 1: Mental Model & South Asian Analogy
Python ko samajhne ke liye sab se pehle iska zehni khaka (mental model) banana zaroori hai. C++ ya Rust jaisi compiled languages ko aap ek aisi factory samjhein jahan raw material aane se pehle poora blueprint banta hai aur aakhir mein ek finished, rigid lohay ka dabba nikalta hai jise direct chalaya jata hai. Agar blueprint mein ek centimeter ka bhi farq ho to poori factory ruk jati hai. Iske bar-aks, Python ek live chai ke dhabay jaisa hai jahan ustaad aur chotu aamne saamne khare hain. Ustaad (developer) chotu (Python interpreter) ko live aawaz deta hai: "Chotu, do cup doodh patti banao!" Chotu usi waqt bartan uthata hai, doodh daalta hai, aur patti ubaalta hai. Agar achanak ustaad kahe "Ab isme cheeni ki jagah namak daal do", to chotu pehle se inkar nahi karega; jab namak daalne ka waqt aayega tabhi woh dekhega ke masala ho gaya hai.

Is live dhabay ke model ko computer science mein 'Interpreted Bytecode Execution' kehte hain. Jab aap terminal par likhte hain `python main.py`, to dar-haqeeqat teen marhalay tay hote hain:
1. Parser aapke likhe hue text ko Abstract Syntax Tree (AST) mein tabdeel karta hai.
2. Compiler is AST ko CPython Virtual Machine ke samajhne laiq intermediate instructions yani bytecode (.pyc) mein tabdeel karta hai.
3. CPython Virtual Machine (VM) ek sequential execution loop chalati hai jo har instruction ko C language ke function calls ke zariye run karti hai.

Variables ka mental model bhi bohot ahem hai. C language mein variable ek lohay ka box hota hai jis par 'int' ya 'float' ka thappa laga hota hai aur usme sirf wahi cheez aa sakti hai. Python mein variable box nahi hai, balki ek resham ka dhaga (pointer / reference) hai jo heap memory mein paray kisi azad object se bandha hota hai. Agar aap `x = 42` likhte hain, to memory mein ek `PyObject` banta hai jiska type integer hai aur `x` ka dhaga uski taraf point kar deta hai. Agli line mein agar aap `x = "Chai"` likh dein, to wahi dhaga purane integer ko chhor kar nayi string se bandh jata hai. Purana integer garbage collector ke hawale ho jata hai.

### Part 2: First-Principles Logic & Worked Numeric Example
CPython interpreter andar se ek Stack Machine ke taur par kaam karta hai. Aayein dekhte hain ke ek nihayat saada expression `total = price + tax` interpreter ke andar kaise execute hoti hai. Farz karein:
- `price = 60`
- `tax = 10`

Jab CPython VM iska bytecode generate karti hai, to instructions kuch is tarah hoti hain:
1. `LOAD_NAME 0 (price)`: Value 60 ko Evaluation Stack par push kiya jata hai. Stack state: `[60]`.
2. `LOAD_NAME 1 (tax)`: Value 10 ko Evaluation Stack par push kiya jata hai. Stack state: `[60, 10]`.
3. `BINARY_OP 0 (+)`: VM stack se top do values ko pop karti hai: `a = 10`, `b = 60`. C-level function `PyNumber_Add(60, 10)` execute hota hai jo result 70 return karta hai. Result wapas stack par push ho jata hai: `[70]`.
4. `STORE_NAME 2 (total)`: Stack se top value (70) pop hoti hai aur current local namespace dictionary mein `{"total": 70}` key-value pair save ho jata hai.

Ab agar tax ka percentage nikalna ho jahan total bill banta hai:
`final_bill = price * (1 + rate)`
Farz karein `price = 100.0` aur `rate = 0.16` (16 percent GST).
Pehle parentheses solve honge: `1 + 0.16 = 1.16`.
Phir multiplication: `100.0 * 1.16 = 116.0`.
Stack evaluation left-to-right aur operator precedence ke mutabiq chalti hai. Dynamic typing ka matlab yeh hai ke agar ghalti se `rate = "0.16"` (string) ho jaye, to runtime par `1 + "0.16"` `TypeError: unsupported operand type(s) for +: 'int' and 'str'` phenk dega kyunke integer object string ke sath addition ka C protocol support nahi karta.

### Part 3: Annotated Production Code
Neeche diye gaye production-grade code mein hum Python 3.12 ke modern type annotations, walrus operator `:=`, aur structural pattern matching `match-case` ko dekhte hain.

```python
import sys
from typing import Final

# Configuration constants defined with Final type annotation
DEFAULT_CURRENCY: Final[str] = "PKR"
TAX_RATE: Final[float] = 0.16  # 16% Sales Tax

def calculate_item_price(item_name: str, quantity: int) -> float:
    \"\"\"Calculates item subtotal using Python 3.10+ match-case semantics.
    
    Inputs:
      item_name: String identifier for dhaba inventory item.
      quantity: Positive integer count of items ordered.
    Returns:
      Raw subtotal in floating-point PKR.
    \"\"\"
    # Input validation contract
    if quantity <= 0:
        raise ValueError(f"Quantity must be strictly positive, got {quantity}")
    
    # Modern structural pattern matching
    match item_name.strip().lower():
        case "doodh_patti" | "chai":
            unit_price = 60.0
        case "elaichi_chai":
            unit_price = 80.0
        case "paratha" | "lachha_paratha":
            unit_price = 120.0
        case "samosa":
            unit_price = 40.0
        case unknown:
            raise KeyError(f"Item '{unknown}' not found in Dhaba menu registry.")
            
    return unit_price * float(quantity)

def generate_invoice(item_name: str, quantity: int) -> dict[str, float | str]:
    # Production error handling pipeline
    try:
        subtotal = calculate_item_price(item_name, quantity)
    except (ValueError, KeyError) as err:
        return {"status": "error", "message": str(err)}
    
    tax_amount = round(subtotal * TAX_RATE, 2)
    grand_total = round(subtotal + tax_amount, 2)
    
    return {
        "status": "success",
        "item": item_name,
        "quantity": float(quantity),
        "subtotal": subtotal,
        "tax": tax_amount,
        "grand_total": grand_total,
        "currency": DEFAULT_CURRENCY
    }

if __name__ == "__main__":
    # Test safe execution
    order = generate_invoice("doodh_patti", 3)
    print(f"Order Processed: {order}")
    # Shape of returned output: Structured dict with 7 strict schema keys
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Mutable Default Arguments: Function definition mein `def add_order(item, orders=[])` likhna sab se bara trap hai. Python mein default list ek hi martaba memory mein allocate hoti hai, is liye har function call usi list mein append karti rehti hai. Hamesha `orders=None` likhein aur function ke andar `orders = [] if orders is None else orders` karein.
2. Floating Point Precision Trap: Financial calculation mein `0.1 + 0.2 == 0.3` False return karta hai kyunke binary representation mein float numbers exact nahi hote. Sensitive billing ke liye Python ka `decimal.Decimal` module use karein.
3. String Concatenation in Loops: Loop ke andar `text += line` likhne se har dafa nayi memory allocate hoti hai jo $O(N^2)$ ban jati hai. Hamesha list mein collect karke `''.join(lines)` karein.

Zero-GPU Tip:
Python syntax aur interpreter logic seekhne ke liye kisi GPU ki zaroorat nahi hai. Aap apne kisi bhi purane laptop par ya Google Colab ke default CPU runtime par terminal open karke Python REPL (`python -i`) chala sakte hain jo zero cost par instant feedback deta hai.

Self-Check Questions:
1. Agar `a = [1, 2, 3]` ho aur hum `b = a` karein, phir `b.append(4)` karein, to `a` ki value kya hogi aur kyun? (Answer: `a` bhi `[1, 2, 3, 4]` hoga kyunke dono variables heap ke ek hi list object ki taraf point kar rahe hain).
2. Python ke CPython execution cycle mein AST aur Bytecode (.pyc) mein kya farq hai?
3. Walrus operator `:=` ka faida kya hai aur yeh while loop ke condition check ko kaise optimize karta hai?

What to Build Next:
Ek interactive terminal CLI banayein jo user se chai ke dhabay ke orders le, walrus operator se loop control kare, aur match-case ke zariye discount codes (e.g. 'JUMMA10' for 10% off) apply karke final bill print kare."""

# ==============================================================================
# LESSON 0.2: Data Structures Deep-Dive
# ==============================================================================
LESSON_CONTENT['0.2'] = """### Part 1: Mental Model & South Asian Analogy
Data structures ko samajhne ke liye apne mohallay ke bazaar ki misaal lein. Bazaar mein alag alag qisam ki dukanain hoti hain aur har dukan ka samaan rakhne ka apna dhang hota hai:
1. List ek lambi qataar (queue) jaisi hai jo metro bus station ya utility store par lagti hai. Har shaks ka ek number hai (index 0, 1, 2...). Agar line ke aakhir mein naya banda aakar khara ho jaye to koi masla nahi ($O(1)$ append). Lekin agar line ke bilkul darmiyan mein kisi ko ghusana paray to peeche khare tamam logon ko ek qadam peeche hatna parta hai ($O(N)$ shift).
2. Tuple ek sealed parcel jaisa hai jo TCS ya courier company se seal band hokar aata hai. Ek dafa seal lag gayi to aap andar ka samaan badal nahi sakte (immutable). Yeh regulatory aur safety records ke liye behtareen hai.
3. Set ek aisi deg jaisi hai jisme shadi ka zarda pak raha hai. Is deg mein har chawal ka daana aapas mein mila hua hai, koi tarteeb (order) nahi hai, lekin do bilkul aik jaisi khas cheezain duplicate nahi ho saktin. Agar aap deg mein hath daal kar check karein ke badam maujood hai ya nahi, to hash lookup ki wajah se foran pata chal jata hai.
4. Dictionary mohallay ke kiryana store ke munshi ka khata register hai. Munshi customer ke naam (Unique Key) se uska hisab (Value) nikalta hai. Munshi ko poora register shuru se aakhir tak padhne ki zaroorat nahi parti; woh index kholta hai aur seedha us naam par ungli rakh deta hai ($O(1)$ lookup).

Memory level par, Python list dar-haqeeqat continuous memory block mein C-pointers ka array hoti hai. Jab list full hoti hai to Python 1.125x memory over-allocate kar leta hai taake bar bar memory reallocate na karni paray. Jabke Dictionary aur Set open-addressing Hash Tables par mushtamil hote hain jahan keys ko `hash(key)` function se guzar kar index banaya jata hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Hash Table ki riyazi ko bilkul pehli bunyad se samjhein. Farz karein hamare paas 8 slots ki ek empty hash table hai (size $M = 8$).
Hamare paas teen keys hain jinhe store karna hai:
1. Key A = "chai"
2. Key B = "paratha"
3. Key C = "lassi"

Step 1: Python ka built-in hash function har string ko ek bara integer banata hai.
Farz karein simulated integer hashes yeh hain:
- `hash("chai") = 5021`
- `hash("paratha") = 9184`
- `hash("lassi") = 7037`

Step 2: Table index nikalne ke liye modulo arithmetic use hoti hai:
`index = hash_value % table_size`
- For "chai": `5021 % 8 = 5` (Kyunke $5021 = 627 \\times 8 + 5$). Slot 5 par pointer save ho gaya.
- For "paratha": `9184 % 8 = 0` (Kyunke $9184 = 1148 \\times 8 + 0$). Slot 0 par pointer save ho gaya.
- For "lassi": `7037 % 8 = 5` (Kyunke $7037 = 879 \\times 8 + 5$).

Step 3: Collision Resolution!
Dekhein, "chai" aur "lassi" dono ka index 5 aa gaya! Isay 'Hash Collision' kehte hain. Python isay solve karne ke liye Perturbation open-addressing algorithm use karta hai jo agla khali slot calculate karta hai:
`next_index = (5 * current_index + 1 + perturb) % table_size`
Farz karein next slot 6 khali mil gaya, to "lassi" slot 6 par store ho jayegi.
Jab aap `menu["chai"]` dhoondte hain to interpreter direct index 5 par jump karta hai aur $O(1)$ time mein data mil jata hai. List mein agar 10 lakh items hon to dhoondne mein 10 lakh comparisons lag sakte hain ($O(N)$), jabke dictionary mein 10 lakh items ke bawajood average sirf 1 step lagta hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum AI token deduplication, dictionary indexing, aur nested comprehensions ko high-performance andaaz mein implement karte hain.

```python
import time
from typing import Dict, List, Set, Tuple

# Raw token stream from simulated Urdu/English corpus
raw_corpus_tokens: List[str] = [
    "ai", "ustaad", "python", "chai", "code", "ai", "machine", "learning",
    "python", "tensor", "gpu", "data", "chai", "model", "inference", "ai"
]

# 1. High-Performance Deduplication using Hash Sets (O(N) total runtime)
unique_tokens_set: Set[str] = set(raw_corpus_tokens)
print(f"Total tokens: {len(raw_corpus_tokens)} | Vocabulary size: {len(unique_tokens_set)}")

# 2. Token-to-ID Vocabulary mapping via Dictionary Comprehension
# Emulates tokenizer vocabulary building in modern LLMs
vocab_to_id: Dict[str, int] = {token: idx for idx, token in enumerate(sorted(unique_tokens_set))}
id_to_vocab: Dict[int, str] = {idx: token for token, idx in vocab_to_id.items()}

# 3. Filtering & Transformation via Dictionary Comprehension
# Compute token frequency distribution
token_frequencies: Dict[str, int] = {
    token: raw_corpus_tokens.count(token) 
    for token in unique_tokens_set
}

# Filter tokens with frequency > 1 using comprehension
frequent_tokens: Dict[str, int] = {
    token: count 
    for token, count in token_frequencies.items() 
    if count > 1
}

# 4. Safe Dictionary Access with default fallback
def lookup_token_id(token: str, vocab_map: Dict[str, int], unk_token_id: int = -1) -> int:
    \"\"\"Performs O(1) hash lookup with explicit out-of-vocabulary handling.\"\"\"
    return vocab_map.get(token.lower().strip(), unk_token_id)

# Execution test
test_token = "python"
print(f"Token '{test_token}' mapped to ID: {lookup_token_id(test_token, vocab_to_id)}")
print(f"Frequent tokens distribution: {frequent_tokens}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. List Search Inside Loop ($O(N^2)$ Disaster): Agar aapke paas 100,000 items ki list hai aur aap check karte hain `if item in my_list:`, to yeh linear scan hai. Loop ke andar karne se code ghanton tak atak jata hai. Hamesha list ko pehle `set(my_list)` mein convert karein phir `if item in my_set:` karein ($O(1)$ instant).
2. Modifying a Collection While Iterating: Loop chalate hue usi list ya dictionary se elements delete karna (`for x in my_list: my_list.remove(x)`) index skipping ka baais banta hai. Hamesha list comprehension se nayi list banayein ya copy par iterate karein.
3. Unhashable Type as Dict Key: Python list ya dictionary ko dict ki key nahi banaya ja sakta (`my_dict[[1, 2]] = "val"` fails with `TypeError: unhashable type: 'list'`). Hamesha immutable tuple use karein: `my_dict[(1, 2)] = "val"`.

Zero-GPU Tip:
Hash tables aur comprehensions CPU ke Level 1 aur Level 2 cache mein process hoti hain. Colab ke standard dual-core CPU par 10 lakh items ka set lookup sirf 40 nanoseconds leta hai, jo kisi bhi GPU overhead se kahin zyada tez hai.

Self-Check Questions:
1. List aur Tuple mein memory footprint ka farq kyun hota hai? (Answer: List dynamic hoti hai aur over-allocation buffer rakhti hai, jabke Tuple fixed size C-array struct hota hai jisme koi extra overhead nahi hota).
2. Hash Collision kya hai aur Python isay kaise handle karta hai?
3. Dictionary comprehension aur generator expression `(x*2 for x in data)` mein memory allocation ka kya farq hai?

What to Build Next:
Ek In-Memory Tokenizer Vocabulary Builder banayein jo ek Urdu/English text paragraph ko sanitize kare, unique tokens ka set banaye, unhe frequency ke mutabiq sort kare, aur token-to-ID aur ID-to-token dictionaries return kare."""

# ==============================================================================
# LESSON 0.3: Functions, Scope, Closures, *args/**kwargs & Lambdas
# ==============================================================================
LESSON_CONTENT['0.3'] = """### Part 1: Mental Model & South Asian Analogy
Programming mein functions ko samajhne ke liye kisi bare government office ya daftari nizaam ki misaal lein. Har daftar mein alag alag clerks (functions) baithe hote hain jinhe ek makhsoos kaam sonpa gaya hota hai: ek clerk stamp lagata hai, doosra verification karta hai, teesra file aage bhejta hai.
1. Functions First-Class Citizens Hain: Iska matlab yeh hai ke Python mein function koi pathar ki lakeer ya rigid institution nahi hai, balki ek aam afrad (object) ki tarah hai. Aap kisi clerk ko variable mein bithha sakte hain, ek clerk ko doosre clerk ke paas training ke liye bhej sakte hain (higher-order function), aur ek clerk nayi shamliat bana kar naya clerk paida kar sakta hai (closure).
2. Variable Scope (LEGB Rule): Misaal lein ek joint family system ki. 
   - Local (L): Aapke kamray ki almaari jisme sirf aapka samaan hai.
   - Enclosing (E): Aapke ghar ka drawing room jahan ghar ke tamam afrad baith sakte hain.
   - Global (G): Mohallay ka park jise gali ka har banda dekh sakta hai.
   - Built-in (B): Mulk ka aaeen aur qanoon (Python built-ins jese `print`, `len`) jo sab par laagu hai.
   Agar aapko koi cheez dhoondni hai to aap pehle apne kamray (Local) mein dekhte hain, wahan na mile to drawing room (Enclosing) mein, wahan bhi na mile to mohallay (Global) mein, aur aakhir mein mulk ke dastoor (Built-in) mein.
3. Closures: Yeh aisi misaal hai jese koi karigar dukan chhor kar ghar chala jaye lekin dukan ke dharay ki chaabi apni jeb mein saath le jaye. Ek inner function apne parent function ke khatam hone ke baad bhi uske variables ko yaad rakhta hai.
4. Decorators: Yeh aisi misaal hai jese kisi aam mehmaan ko VIP protocol de diya jaye. Mehmaan wahi rehta hai, lekin uske aage aur peeche protocol ki gaariyan (logging, timing, security check) lag jati hain bina uske andar koi tabdeeli kiye.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein ek Mathematical Closure aur Decorator ki execution ko number-by-number trace karte hain.
Farz karein hum ek Learning Rate Decay Scheduler function bana rahe hain jo base learning rate ko har step par exponential factor se multiply karta hai:
Formula: $\\eta_{t} = \\eta_0 \\times \\gamma^t$
Jahan:
- $\\eta_0 = 0.1$ (Initial Learning Rate)
- $\\gamma = 0.9$ (Decay Factor)
- $t$ = Step number (0, 1, 2...)

Closure banate waqt:
```python
def make_scheduler(eta_0: float, gamma: float):
    step = 0
    def get_lr():
        nonlocal step
        current_lr = eta_0 * (gamma ** step)
        step += 1
        return current_lr
    return get_lr
```
Execution Trace:
1. `scheduler = make_scheduler(0.1, 0.9)` call hua. CPython heap par ek closure frame banta hai jisme `eta_0=0.1`, `gamma=0.9`, aur `step=0` lock ho jate hain. Function reference return ho jata hai.
2. Step 1 Call: `scheduler()`
   - `current_lr = 0.1 * (0.9 ** 0) = 0.1 * 1.0 = 0.1000`
   - `step` increment hokar 1 ban gaya.
3. Step 2 Call: `scheduler()`
   - `current_lr = 0.1 * (0.9 ** 1) = 0.1 * 0.9 = 0.0900`
   - `step` increment hokar 2 ban gaya.
4. Step 3 Call: `scheduler()`
   - `current_lr = 0.1 * (0.9 ** 2) = 0.1 * 0.81 = 0.0810`
   - `step` increment hokar 3 ban gaya.

Yahan `step` variable global nahi hai, lekin function calls ke darmiyan persistent rehta hai! Yahi state encapsulation AI optimization pipelines ka dil hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum flexible `*args` aur `**kwargs` dispatching, custom timing decorator, aur closures ko implement karte hain.

```python
import time
from functools import wraps
from typing import Callable, Any

def audit_telemetry(func: Callable[..., Any]) -> Callable[..., Any]:
    \"\"\"Production decorator to measure execution latency and track arguments.
    Uses functools.wraps to preserve original function docstrings and signature.
    \"\"\"
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_ns = time.perf_counter_ns()
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as exc:
            print(f"[Telemetry Error] Exception in {func.__name__}: {exc}")
            raise
        finally:
            elapsed_ms = (time.perf_counter_ns() - start_ns) / 1_000_000.0
            print(f"[Telemetry] {func.__name__} executed in {elapsed_ms:.4f} ms")
            
    return wrapper

@audit_telemetry
def run_model_inference(
    model_name: str, 
    *prompt_batch: str, 
    temperature: float = 0.7, 
    max_tokens: int = 512, 
    **metadata: Any
) -> dict[str, Any]:
    \"\"\"Simulates production LLM batch dispatch with dynamic arguments.
    
    *prompt_batch captures arbitrary positional prompts into a Tuple[str, ...].
    **metadata captures system tags and user context into a Dict[str, Any].
    \"\"\"
    batch_size = len(prompt_batch)
    if batch_size == 0:
        raise ValueError("Prompt batch cannot be empty.")
        
    simulated_responses = [
        f"Response to: '{prompt}' (temp={temperature})" 
        for prompt in prompt_batch
    ]
    
    return {
        "model": model_name,
        "batch_size": batch_size,
        "completions": simulated_responses,
        "max_tokens": max_tokens,
        "tags": metadata
    }

# Execution test
if __name__ == "__main__":
    result = run_model_inference(
        "llama-3.2-3b",
        "Chai kaise banayein?",
        "Python seekhne ka asan tareeqa?",
        temperature=0.2,
        user_id="bimo_001",
        region="ap-southeast-1"
    )
    print("Inference Batch Output:", result)
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Missing `@wraps(func)` in Decorators: Agar aap custom decorator banate waqt `@functools.wraps` use nahi karte, to decorate hone ke baad original function ka naam `__name__` badal kar `wrapper` ho jata hai aur docstrings gayab ho jati hain, jisse debugging aur API documentation tools crash ho jate hain.
2. Unintended Global Mutation: Function ke andar kisi bahar ke variable ko modify karne ke liye agar aap baghair samjhe `global x` likh dete hain to code spaghetti ban jata hai aur multi-threaded / async environment mein data race conditions paida hoti hain.
3. Late-Binding Closure Gotcha: Loop ke andar lambdas banate waqt `funcs = [lambda: i for i in range(5)]` likhne par tamam lambdas 4 return karte hain kyunke `i` lookup call hone par hota hai. Iska hal default parameter binding hai: `lambda i=i: i`.

Zero-GPU Tip:
Decorators aur functional pipelines Python ke memory stack par run karte hain. Testing ke liye aap synthetic latency create karne ke liye `time.sleep(0.01)` use karein taake bina kisi cloud GPU kharch kiye batch latency metrics verify ho sakein.

Self-Check Questions:
1. `*args` aur `**kwargs` function ke andar kis data type mein convert hote hain? (Answer: `*args` tuple banta hai, jabke `**kwargs` dictionary banta hai).
2. `nonlocal` keyword aur `global` keyword mein kya farq hai?
3. Function closure memory leak ka baais kab ban sakti hai?

What to Build Next:
Ek Retry & Rate-Limiter Decorator likhein jo kisi failing function ko exponential backoff ke sath 3 dafa retry kare aur agar teeno dafa fail ho jaye to custom exception raise kare."""

# ==============================================================================
# LESSON 0.4: Object-Oriented Programming (OOP) for AI
# ==============================================================================
LESSON_CONTENT['0.4'] = """### Part 1: Mental Model & South Asian Analogy
AI Engineering mein Object-Oriented Programming (OOP) ka role aam web development se bohot mukhtalif hai. PyTorch ka har neural network module (`nn.Module`), Hugging Face ka har transformer, aur LangChain ka har agent dar-haqeeqat ek Python Class hai!
Misaal lein aik traditional Kapray Silwane wale Darzi (Tailor Master) ki:
1. Class vs Object: Class darzi ke paas mojud suit ka 'Khaaka / Pattern Paper' hai jo batata hai ke kameez ke kitne baazu honge, collar kaisa hoga, aur jeb kahan lagegi. Object woh haqeeqi suit hai jo us pattern ke mutabiq laatha ya wash-and-wear kapray par sil kar taiyar hota hai aur almari mein jagah (memory) leta hai.
2. State & Behavior: Har suit ka apna naap (State: chest=40, length=42) hota hai, aur uske upar functions (Behavior: press_karna(), pehanna()) chalte hain.
3. Dunder (Double Underscore) Methods: Yeh Python ke shahi darwazay hain. Misaal ke taur par, jab darzi suit ko pohnchey se pakar kar naapta hai, to woh dar-haqeeqat `__len__()` call kar raha hota hai. Jab aap kisi model ko input dete hain `model(x)`, to PyTorch ka `__call__()` method parde ke peeche trigger hota hai jo `forward(x)` ko chalata hai.
4. `@dataclass(slots=True)`: Aam Python class mein har banne wale object ke sath ek dynamic dictionary `__dict__` jurti hai taake agar baad mein koi naya attribute add karna ho to flexibility mil sake. Lekin AI mein jahan 10 lakh embeddings ya data samples process ho rahe hon, yeh dictionary har object par 150 bytes se zyada memory zaaya karti hai. `@dataclass(slots=True)` Python ko kehti hai: "Faltu dictionary mat banao, balki C struct ki tarah memory mein fixed offsets allocate karo." Isse memory 25-30% bach jati hai aur attribute access 20% tez ho jata hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein dekhte hain ke PyTorch-style class ke andar parameter counter aur forward pass kaise kaam karta hai.
Farz karein hum ek custom `LinearLayer` class bana rahe hain jisme:
- Input Features $D_{in} = 3$
- Output Features $D_{out} = 2$

Mathematics:
$y = x \\cdot W^T + b$
Jahan:
- Input $x$ ka shape hai $[1, 3]$: Farz karein $x = [[2.0, 1.0, 3.0]]$
- Weights $W$ ka shape hai $[2, 3]$:
  $W = \\begin{bmatrix} 0.5 & -0.2 & 0.1 \\\\ 0.1 & 0.4 & -0.5 \\end{bmatrix}$
- Bias $b$ ka shape hai $[2]$: $b = [0.1, -0.2]$

Calculation Step-by-Step:
Output neuron 1 ($y_0$):
$y_0 = (2.0 \\times 0.5) + (1.0 \\times -0.2) + (3.0 \\times 0.1) + b_0$
$y_0 = 1.0 - 0.2 + 0.3 + 0.1 = 1.20$

Output neuron 2 ($y_1$):
$y_1 = (2.0 \\times 0.1) + (1.0 \\times 0.4) + (3.0 \\times -0.5) + b_1$
$y_1 = 0.2 + 0.4 - 1.5 - 0.2 = -1.10$

Final output vector: $y = [[1.20, -1.10]]$, shape $[1, 2]$.
Jab hum class ke andar `__call__` define karte hain, to user ko `layer.forward(x)` likhne ki zaroorat nahi rehti; user seedha `layer(x)` likhta hai aur Python automatically calculation execute kar deta hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum `@dataclass(slots=True)`, custom dunder methods (`__call__`, `__len__`, `__repr__`), aur inheritance hierarchy ko implement karte hain.

```python
from dataclasses import dataclass, field
from typing import List, Sequence

# Modern memory-efficient dataclass with C-aligned memory slots
@dataclass(slots=True)
class DataSample:
    sample_id: int
    text_content: str
    token_count: int
    embedding_vector: List[float] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.token_count < 0:
            raise ValueError(f"token_count cannot be negative: {self.token_count}")

class MiniDataset:
    \"\"\"Emulates PyTorch Dataset protocol with __len__ and __getitem__.\"\"\"
    def __init__(self, samples: Sequence[DataSample]) -> None:
        self._samples: List[DataSample] = list(samples)

    def __len__(self) -> int:
        \"\"\"Enables len(dataset) syntax.\"\"\"
        return len(self._samples)

    def __getitem__(self, index: int) -> DataSample:
        \"\"\"Enables dataset[i] random access indexing.\"\"\"
        return self._samples[index]

    def __repr__(self) -> str:
        return f"<MiniDataset: {len(self)} samples stored in memory>"

class MockLinearModule:
    \"\"\"Emulates PyTorch nn.Module callable pattern.\"\"\"
    def __init__(self, weights: List[float], bias: float) -> None:
        self.weights = weights
        self.bias = bias

    def forward(self, features: List[float]) -> float:
        if len(features) != len(self.weights):
            raise ValueError(f"Shape mismatch: expected {len(self.weights)} features, got {len(features)}")
        # Vector dot-product: sum(w * x) + b
        dot_product = sum(w * x for w, x in zip(self.weights, features))
        return dot_product + self.bias

    def __call__(self, features: List[float]) -> float:
        \"\"\"Allows calling instance directly like a function: model(x).\"\"\"
        return self.forward(features)

# Verification execution
if __name__ == "__main__":
    sample1 = DataSample(1, "Chai peeni hai", 4, [0.1, 0.4, -0.2])
    sample2 = DataSample(2, "AI Ustaad course", 5, [0.9, 0.1, 0.3])
    
    dataset = MiniDataset([sample1, sample2])
    print(f"Dataset status: {dataset}")
    print(f"First sample text: '{dataset[0].text_content}'")
    
    layer = MockLinearModule(weights=[0.5, -0.2, 0.1], bias=0.1)
    output = layer(sample1.embedding_vector)
    print(f"Linear projection output: {output:.4f}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Calling `self.forward(x)` Instead of `self(x)`: PyTorch aur modern AI libraries mein agar aap direct `model.forward(x)` call karte hain to hooks (profilers, telemetry, gradient trackers) bypass ho jate hain. Hamesha instance ko directly call karein: `model(x)`.
2. Modifying Class Attributes Instead of Instance Attributes: Agar aap class ke andar `class Model: layers = []` define karte hain to woh tamaam instances ke darmiyan share ho jati hai. Hamesha `__init__` ke andar `self.layers = []` karein.
3. Deep Inheritance Chains: AI engineering mein 5-level gehri inheritance banana anti-pattern hai. Hamesha Composition over Inheritance prefer karein (ek class doosri class ko as an attribute contain kare).

Zero-GPU Tip:
Dataclass slots aur PyTorch dataset abstractions ko test karne ke liye zero GPU chahiye hota hai. Python standard library ka `sys.getsizeof()` use karke aap verify kar sakte hain ke standard class ke muqablay `@dataclass(slots=True)` kitne bytes save kar rahi hai.

Self-Check Questions:
1. `@dataclass(slots=True)` use karne se memory kyun kam hoti hai aur iska kya nuqsan ho sakta hai? (Answer: Yeh `__dict__` ko khatam kar deta hai, iska nuqsan yeh hai ke runtime par dynamic naye attributes add nahi kiye ja sakte).
2. Python mein `__getitem__` aur `__len__` implement karne se object ko kaun kaun se Python built-in operations mil jate hain? (Answer: Slicing, indexing, `for item in dataset` iteration, aur `len()` support).
3. Dunder method `__repr__` aur `__str__` mein ahem farq kya hai?

What to Build Next:
Ek `MiniBatchDataLoader` class banayein jo ek `MiniDataset` ko accept kare, user ke diye gaye `batch_size` ke mutabiq samples ko chunk kare, shuffle flag support kare, aur generator ke zariye batches yield kare."""

# ==============================================================================
# LESSON 0.5: File Handling, JSON, Parquet & REST APIs
# ==============================================================================
LESSON_CONTENT['0.5'] = """### Part 1: Mental Model & South Asian Analogy
AI pipelines ka sara daromadar data par hai. Model train karna ho ya RAG database banana ho, pehle data ko disk se uthana aur network se mangwana parta hai.
Is process ko samajhne ke liye kisi bare grain market (Galla Mandi) ki misaal lein:
1. File Handling & Context Managers (`with` block): Farz karein aap galla mandi ke godown (warehouse) mein boriyan uthane gaye hain. Agar aap godown ka tala khol kar andar jayein aur wapas aate waqt darwaza khula chhor dein, to raat ko chori ho jayegi ya barish se ghalla kharab ho jayega (Resource Leak / File Lock Bug). Python ka `with open(...)` block ek security guard jaisa hai jo aapke sath rehta hai: jaise hi aapka kaam khatam ho ya aapke hath se bori gir kar phat jaye (error/exception), guard foran tala band kar deta hai.
2. JSON vs JSONL (JSON Lines): 
   - Standard JSON ek bohot bari bori jaisi hai jisme 10,000 amrood bandhe hue hain. Agar aapko sirf ek amrood check karna ho, to poori bori khol kar farsh par ulatni parti hai (Memory Out-Of-Memory Crash).
   - JSONL (JSON Lines) aisi hai jese har amrood alag alag khulay dibbay mein ek conveyor belt par aa raha hai. Har line par ek mukammal JSON document hota hai. LLM fine-tuning datasets (Hugging Face, Unsloth, OpenAI) 100% JSONL format use karte hain kyunke agar dataset 50 GB ka bhi ho, to aap ek waqt mein sirf ek line memory mein load karke stream kar sakte hain.
3. Parquet: Yeh modern columnar storage format hai. Traditional CSV har row ko line-by-line store karta hai. Agar aapko 100 columns mein se sirf 'price' ka column chahiye to poori 10 GB ki CSV read karni parti hai. Parquet columnar hota hai aur snappily compressed hota hai; yeh disk se sirf 'price' ka column uthata hai aur baqi 99 columns ko chhoota bhi nahi.
4. REST APIs: Yeh aisi misaal hai jese restaurant mein waiter ko order dena. Waiter (HTTP Client) kitchen (Remote Server) jata hai, aapka request menu (Payload) deta hai, aur wahan se khana (JSON Response) le kar aata hai. Agar kitchen mein rash ho to waiter keh sakta hai "Wait karein" (HTTP 429 Rate Limit).

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein dekhte hain ke Memory Streaming vs Full In-Memory Loading mein RAM ka kitna farq parta hai.
Farz karein hamare paas ek dataset file hai jisme:
- Total records $N = 100,000$ (1 lakh sentences).
- Average sentence length = 200 characters $\\approx$ 250 bytes per JSON record.
- File size on disk $\\approx 100,000 \\times 250 \\text{ bytes} = 25 \\text{ MB}$.

Scenario A: Naive `json.load(open('data.json'))`
1. Python poori file ko raw string ke taur par RAM mein read karta hai (+25 MB).
2. JSON parser string ko parse karke 100,000 Python dictionary aur string objects banata hai. Har Python string aur dict ka memory overhead $\\approx 4\\times$ hota hai (+100 MB).
3. Temporary garbage buffers (+25 MB).
Total Peak RAM Used: $\\approx 150 \\text{ MB}$.
Agar file 25 MB ke bajaye 2 GB ki hoti, to standard free container ya laptop crash ho jata!

Scenario B: Line-by-Line Streaming with JSONL
```python
with open('data.jsonl', 'r') as f:
    for line in f:
        record = json.loads(line)
        process(record)
```
1. File buffer memory: Sirf 8 KB default I/O buffer.
2. At any point in time, memory mein sirf 1 record (250 bytes) mojud hota hai.
Total Peak RAM Used: $< 1 \\text{ MB}$ (Constant $O(1)$ Memory)!
File chahe 25 MB ki ho ya 500 GB ki, RAM kabhi explode nahi hoti.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum JSONL streaming writer & reader, robust error-handled REST API request with exponential backoff, aur disk persistence ko implement karte hain.

```python
import json
import os
import tempfile
import time
from typing import Iterator, Dict, Any

# 1. Production Streaming JSONL Writer
def stream_write_jsonl(filepath: str, records: Iterator[Dict[str, Any]]) -> int:
    \"\"\"Streams records to disk line-by-line to guarantee zero memory spikes.\"\"\"
    written_count = 0
    with open(filepath, "w", encoding="utf-8") as f:
        for record in records:
            json_line = json.dumps(record, ensure_ascii=False)
            f.write(json_line + "\\n")
            written_count += 1
    return written_count

# 2. Production Streaming JSONL Reader Generator
def stream_read_jsonl(filepath: str) -> Iterator[Dict[str, Any]]:
    \"\"\"Yields one deserialized record at a time via Python generator.\"\"\"
    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            clean_line = line.strip()
            if not clean_line:
                continue
            try:
                yield json.loads(clean_line)
            except json.JSONDecodeError as err:
                print(f"[Warning] Corrupted JSON at line {line_num}: {err}")
                continue

# 3. Simulated Resilient REST API Client with Retry
def fetch_remote_resource_mock(endpoint: str, retries: int = 3) -> Dict[str, Any]:
    \"\"\"Emulates production HTTP client with error handling & backoff.\"\"\"
    for attempt in range(1, retries + 1):
        try:
            # Simulate network round-trip
            if endpoint == "https://api.dhaba.local/status":
                return {"status_code": 200, "data": {"health": "ok", "active_orders": 14}}
            raise ConnectionError("Simulated network timeout")
        except ConnectionError as err:
            wait_time = 0.1 * (2 ** (attempt - 1))  # Exponential backoff: 0.1s, 0.2s, 0.4s
            print(f"[Attempt {attempt}/{retries}] Failed: {err}. Retrying in {wait_time}s...")
            time.sleep(wait_time)
            if attempt == retries:
                raise RuntimeError(f"Endpoint {endpoint} unreachable after {retries} attempts.")
    return {}

# Verification execution
if __name__ == "__main__":
    sample_dataset = (
        {"id": i, "prompt": f"Roman Urdu sample {i}", "label": "positive" if i % 2 == 0 else "neutral"}
        for i in range(10)
    )
    
    with tempfile.NamedTemporaryFile(suffix=".jsonl", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        count = stream_write_jsonl(tmp_path, sample_dataset)
        print(f"Successfully streamed {count} records to JSONL on disk.")
        
        # Read back via streaming generator
        print("Reading back top 3 records:")
        for idx, item in enumerate(stream_read_jsonl(tmp_path)):
            if idx >= 3:
                break
            print(f"  Record {item['id']}: {item['prompt']}")
            
        api_res = fetch_remote_resource_mock("https://api.dhaba.local/status")
        print("API Health Status:", api_res)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Missing `encoding='utf-8'`: Windows par default encoding aksar CP1252 ya ANSI hoti hai. Agar aap `open('file.txt', 'w')` mein explicit `encoding='utf-8'` nahi likhte, to Urdu ya Arabic characters save karte waqt `UnicodeEncodeError` aa jata hai. Hamesha `encoding='utf-8'` likhein.
2. In-Memory Buffering of Massive Datasets: 5 GB ki file par `lines = f.readlines()` likhna foran RAM ko crash kar deta hai kyunke yeh tamam lines ka Python object array memory mein load karta hai. Hamesha `for line in f:` generator use karein.
3. Ignoring REST API HTTP 429 Status Codes: LLM APIs (OpenAI, Anthropic, Groq) use karte waqt agar aap exponential backoff implement nahi karte, to thodi si traffic aate hi rate-limit exceptions poore server ko gira deti hain.

Zero-GPU Tip:
File serialization aur JSONL streaming 100% I/O bound aur CPU bound hain. Colab ya local drive par fast SSD read/write speeds use karein. Test datasets ke liye hamesha standard library ka `tempfile` module use karein taake disk clutter na ho.

Self-Check Questions:
1. JSON aur JSONL format mein structural aur memory streaming ka kya farq hai?
2. `with open(...)` block ke peeche kaun se do dunder methods kaam karte hain? (Answer: `__enter__` aur `__exit__`).
3. Exponential backoff algorithm retry attempts ke darmiyan wait time kyun barhata hai?

What to Build Next:
Ek Command-Line Data Harvester script banayein jo ek mock REST API se 500 records paginate karke fetch kare, unhe sanitize kare, aur disk par safely partitioned `.jsonl` file mein append kare."""

# ==============================================================================
# LESSON 0.6: NumPy & Pandas Foundations
# ==============================================================================
LESSON_CONTENT['0.6'] = """### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne pure Python ke bunyadi sutoon (syntax, data structures, functions, OOP, aur file I/O) master kar liye hain. Ab hum dakhil ho rahe hain AI Engineering ke darwazay par: **Numerical & Tabular Python**!
NumPy aur Pandas ko samajhne ke liye kisi bare National Bank ya State Bank ke cash counter ki misaal lein:
1. Pure Python List vs NumPy Array: 
   - Pure Python list aisi hai jese ek thela jisme alag alag shakal aur size ke sikkay aur note bhare hue hon. Ek 5000 ka note hai, ek 10 ka sikka hai, ek resham ka dhaga hai. Cashier ko har note ko alag se dekhna parta hai ke yeh kya cheez hai aur iska size kitna hai.
   - NumPy array aisi hai jese naye karak 100-rupaye ke notes ki ek sealed machine-packed gaddi. Har note ka size, wazan, aur orientation bilkul barabar (Homogeneous 32-bit Float) hai aur memory mein lagataar (Contiguous C Block) rakhi hui hai. Bank ki currency counting machine is gaddi ko ek second mein gin leti hai kyunke use har note ki type check karne ki zaroorat nahi parti.
2. SIMD (Single Instruction, Multiple Data): Modern CPU processors mein khaas registers hote hain (AVX-512 ya ARM Neon). Agar aapke paas 4 numbers hain aur unhe 2 se multiply karna hai, to standard Python 4 alag alag instructions chalata hai. NumPy CPU ko sirf ek single instruction deta hai: "In 4 numbers ko ek hi clock cycle mein parallel multiply kar do!"
3. Dimensions & Tensors:
   - 0D: Ek akela number = Scalar (e.g. Chai ki qeemat = 60).
   - 1D: Aik qataar = Vector (e.g. Aik customer ke features = [age, bill, visits]).
   - 2D: Aik table / chatai = Matrix (e.g. 100 customers ka tabular data).
   - 3D+: Multidimensional cube = Tensor (e.g. Batch of token sequences in Transformers).
4. Pandas DataFrame: Yeh NumPy ke upar bani hui aisi table hai jisme har column ka ek insani naam (Label) hota hai (jese Excel ya SQL table), jisse data filtering, grouping, aur aggregation nihayat aasan ho jati hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein NumPy ke sab se taqatwar concept **Vector Broadcasting & Dot Product** ki calculation ko first-principles se samjhein.
Farz karein hamare paas ek Dhaba sales vector hai:
Prices Vector $P = [60, 120, 80]$ (Prices of Chai, Paratha, Elaichi Chai)
Quantities Vector $Q = [10, 5, 2]$ (Sold units)

Calculation 1: Element-wise Multiplication (Hadamard Product)
$R_i = P_i \\times Q_i$
- Item 0: $60 \\times 10 = 600$
- Item 1: $120 \\times 5 = 600$
- Item 2: $80 \\times 2 = 160$
Result Vector: $R = [600, 600, 160]$

Calculation 2: Dot Product (Total Revenue)
Dot product in tamam element-wise products ka sum hota hai:
$\\text{Total Revenue} = P \\cdot Q = \\sum_{i=0}^{2} P_i Q_i = 600 + 600 + 160 = 1360$

Calculation 3: Broadcasting (Flat 10% Discount)
Agar hum pure array par 10% discount lagana chahein to scalar $s = 0.9$ ko multiply karte hain:
$P_{\\text{discounted}} = P \\times 0.9$
NumPy scalar $0.9$ ko automatically $[0.9, 0.9, 0.9]$ vector mein broadcast (stretch) karta hai bina memory copy kiye:
- $60 \\times 0.9 = 54.0$
- $120 \\times 0.9 = 108.0$
- $80 \\times 0.9 = 72.0$
Result: $[54.0, 108.0, 72.0]$.
Yeh computation CPU ke hardware registers mein direct execute hoti hai aur Python ke `for` loop se 50x se 100x tez hoti hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum NumPy vectorized operations, broadcasting, benchmarking vs pure Python, aur Pandas tabular aggregation ko implement karte hain.

```python
import time
import numpy as np
import pandas as pd

# 1. Benchmark: Pure Python Loop vs NumPy Vectorization
ARRAY_SIZE = 1_000_000

py_list_a = list(range(ARRAY_SIZE))
py_list_b = list(range(ARRAY_SIZE))

# Measure pure Python execution
t0 = time.perf_counter()
py_result = [a + b for a, b in zip(py_list_a, py_list_b)]
py_duration = time.perf_counter() - t0

# Measure NumPy SIMD vectorized execution
np_arr_a = np.arange(ARRAY_SIZE, dtype=np.int32)
np_arr_b = np.arange(ARRAY_SIZE, dtype=np.int32)

t0 = time.perf_counter()
np_result = np_arr_a + np_arr_b
np_duration = time.perf_counter() - t0

print(f"Pure Python Loop Time: {py_duration*1000:.2f} ms")
print(f"NumPy Vectorized Time: {np_duration*1000:.2f} ms")
print(f"NumPy Speedup: {py_duration / max(np_duration, 1e-9):.1f}x faster!")

# 2. Vector Math: Dot Product & Cosine Geometry
prices = np.array([60.0, 120.0, 80.0, 40.0], dtype=np.float32)  # Shape: (4,)
quantities = np.array([15.0, 8.0, 12.0, 20.0], dtype=np.float32) # Shape: (4,)

total_revenue = np.dot(prices, quantities)
print(f"Total Revenue via Dot Product: PKR {total_revenue:.2f}")

# 3. Pandas Tabular Analytics Pipeline
sales_records = {
    "item": ["Doodh Patti", "Lachha Paratha", "Elaichi Chai", "Samosa", "Bun Kabab"],
    "category": ["Beverage", "Food", "Beverage", "Snack", "Food"],
    "unit_price": [60.0, 120.0, 80.0, 40.0, 150.0],
    "units_sold": [120, 45, 60, 80, 35]
}

df = pd.DataFrame(sales_records)
# Vectorized feature creation
df["total_sales"] = df["unit_price"] * df["units_sold"]

print("\\n--- Sales DataFrame ---")
print(df)

# Aggregation by category
category_summary = (
    df.groupby("category")
    .agg(
        total_items_sold=("units_sold", "sum"),
        category_revenue=("total_sales", "sum"),
        avg_unit_price=("unit_price", "mean")
    )
    .reset_index()
)
print("\\n--- Category Revenue Summary ---")
print(category_summary)
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Iterating Over Pandas Rows with `for index, row in df.iterrows()`: Yeh Pandas ka sab se bara anti-pattern hai. `iterrows()` har row par ek naya Pandas Series object banata hai jo code ko 100x slow kar deta hai. Hamesha vectorized operations (`df['a'] * df['b']`) ya NumPy arrays use karein.
2. Incompatible Shapes in Array Broadcasting: Jab aap do arrays ko multiply ya add karte hain jinke dimensions match nahi hote (e.g. Shape `(3, 4)` and `(3,)`), to NumPy `ValueError: operands could not be broadcast together` throw karta hai. Hamesha array ka shape check karein: `print(arr.shape)`.
3. Unnecessary Copying of Large Arrays: NumPy mein slice karte waqt `b = a[0:10]` ek View return karta hai, nayi copy nahi banata. Agar aap `b` ko modify karenge to `a` bhi modify ho jayega. Agar aapko azad array chahiye to explicit `a[0:10].copy()` karein.

Zero-GPU Tip:
NumPy aur Pandas CPU par chalte hain aur modern SIMD extensions (AVX2, AVX-512) se fully accelerated hote hain. Colab ke free tier CPU par aap lakhoon rows ka data chund milliseconds mein process kar sakte hain bina kisi GPU credit ko zaaya kiye.

Self-Check Questions:
1. NumPy array aur Python list mein memory layout aur type homogeneity ka kya farq hai?
2. Dot product aur element-wise multiplication mein riyazi ka kya farq hai?
3. Pandas mein Vectorization ka kya matlab hai aur yeh `iterrows()` se kyun behtar hai?

What to Build Next:
Ek Complete Dhaba Analytics Script likhein jo 1,000 synthetic orders ka Pandas DataFrame banaye, daily revenue calculate kare, top 3 best-selling items nikalay, aur NumPy dot product se sales tax aur net profit calculate kare."""
