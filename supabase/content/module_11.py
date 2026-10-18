# module_11.py
# Module 11: Production AI Engineering & MLOps
# Lessons 11.1 to 11.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 11.1: High-Throughput LLM Inference: vLLM Architecture & PagedAttention
# ==============================================================================
LESSON_CONTENT['11.1'] = r"""### Part 1: Mental Model & South Asian Analogy
Aam Hugging Face `generate()` function production mein sirf 2 se 5 requests per second (RPS) serve kar pata hai kyunke har request ke liye GPU memory mein pehle se fixed 4096-token ka contiguous buffer allocate karna parta hai. 2023-2026 mein LLM serving ka sab se bara inqilab UC Berkeley ka **vLLM aur PagedAttention** hai jo serving throughput ko **10x se 24x** barha deta hai!
Isay samajhne ke liye kisi Mashhoor Parking Plaza aur Computer Operating System ki misaal lein:
1. Traditional Serving (Fixed Continuous Parking): Farz karein aik parking plaza hai jahan har aane wali choti Suzuki Alto gaari ke liye bhi poora 18-wheeler truck ka 50-foot lamba khana reserve kar diya jata hai! Agar Alto sirf 10 foot le to baqi 40 foot khali para rehta hai aur kisi doosri gaari ko khari hone ki ijazat nahi hoti (Internal Memory Fragmentation: 60% se 80% VRAM bekaar zaaya ho jati hai).
2. PagedAttention (Virtual Memory Paging): Operating systems (Linux/Windows) mein jaise virtual memory physical RAM ko 4KB ke chotay chotay Pages mein taqseem karti hai, bilkul usi tarah vLLM KV Cache ko 16 ya 32 tokens ke chotay **Blocks / Pages** mein taqseem karta hai!
3. The Block Table (Munshi Ka Room Allotment Register): Har sequence ke KV tokens physical VRAM mein aage peeche bikharay ho sakte hain (Non-contiguous blocks). Block Table track karti hai: "Logical Block 0 physical VRAM slot 9 par hai, Logical Block 1 physical slot 42 par hai."
4. Continuous Batching (Chotu Ka Dynamic Order Delivery): Purani batching mein jab tak batch ka sab se lamba jawab khatam na ho, baqi tamam chotay jawabat GPU mein latkay rehte the. Continuous batching mein jaise hi koi request complete hoti hai, naye user ki request us khali slot mein foran insert ho jati hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Memory Fragmentation aur Throughput Multiplier ka exact mathematical hisab lagayein.
GPU Specifications:
- Total VRAM Available for KV Cache = 16 GB ($16,384 \text{ MB}$)
- Model: LLaMA-3-8B (FP16 KV Cache $\approx 0.5 \text{ MB per 1000 tokens}$)
- Average user request length: Prompt = 500 tokens, Output = 200 tokens. Total = 700 tokens.
- KV Cache memory required per actual request:
  $M_{\text{actual}} = 700 \times 0.0005 \text{ MB} = 0.35 \text{ MB}$.

Scenario A: Naive Static Allocation (Hugging Face / TGI without Paging)
System allocates for maximum worst-case context ($S_{\text{max}} = 4096$ tokens):
$M_{\text{static}} = 4096 \times 0.0005 \text{ MB} = 2.048 \text{ MB per request}$!
Memory Wastage per request:
$\Delta M = 2.048 - 0.350 = 1.698 \text{ MB}$ ($\approx 82.9\% \text{ VRAM Zaaya!}$)
Concurrent Requests Supported before OOM:
$\text{Capacity}_{\text{static}} = \frac{16,384 \text{ MB}}{2.048 \text{ MB}} = 8 \text{ concurrent streams}$.

Scenario B: vLLM PagedAttention Dynamic Allocation
Block size = 16 tokens ($M_{\text{block}} = 16 \times 0.0005 = 0.008 \text{ MB}$).
Tokens needed = 700 tokens $\implies \lceil \frac{700}{16} \rceil = 44 \text{ blocks}$ allocated on demand.
Allocated memory $= 44 \times 0.008 = 0.352 \text{ MB}$.
Wastage (only at aakhri block): $0.002 \text{ MB}$ ($< 1\% \text{ Fragmentation}$)!
Concurrent Requests Supported in same 16 GB VRAM:
$\text{Capacity}_{\text{vLLM}} = \frac{16,384 \text{ MB}}{0.352 \text{ MB}} \approx 46 \text{ concurrent streams}$!
Throughput Improvement:
$\frac{46}{8} \approx 5.75\times \text{ Higher Concurrent Throughput}$ on the exact same physical GPU!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum PagedAttention Logical-to-Physical Block Table manager aur dynamic block allocator from first principles implement karte hain.

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class PhysicalBlock:
    block_id: int
    is_free: bool = True
    num_tokens_stored: int = 0
    max_tokens: int = 16

class PagedAttentionBlockManager:
    \"\"\"Manages virtual memory paging for KV cache blocks in GPU VRAM.\"\"\"
    def __init__(self, total_physical_blocks: int = 64, block_size: int = 16) -> None:
        self.block_size = block_size
        self.free_blocks: List[int] = list(range(total_physical_blocks))
        self.block_pool: Dict[int, PhysicalBlock] = {
            i: PhysicalBlock(block_id=i, max_tokens=block_size) for i in range(total_physical_blocks)
        }
        # Mapping: request_id -> List of physical block IDs
        self.block_tables: Dict[str, List[int]] = {}

    def allocate_for_request(self, request_id: str, num_tokens: int) -> List[int]:
        \"\"\"Allocates non-contiguous physical memory blocks for logical sequence.\"\"\"
        blocks_needed = (num_tokens + self.block_size - 1) // self.block_size
        if len(self.free_blocks) < blocks_needed:
            raise MemoryError(f"GPU KV Cache OOM: needed {blocks_needed} blocks, available {len(self.free_blocks)}")

        allocated_ids: List[int] = []
        for _ in range(blocks_needed):
            b_id = self.free_blocks.pop(0)
            self.block_pool[b_id].is_free = False
            allocated_ids.append(b_id)

        self.block_tables[request_id] = allocated_ids
        return allocated_ids

    def free_request(self, request_id: str) -> None:
        \"\"\"Reclaims blocks when request finishes generating tokens.\"\"\"
        if request_id not in self.block_tables:
            return
        for b_id in self.block_tables[request_id]:
            self.block_pool[b_id].is_free = True
            self.free_blocks.append(b_id)
        del self.block_tables[request_id]

# Execution test
if __name__ == "__main__":
    manager = PagedAttentionBlockManager(total_physical_blocks=20, block_size=16)
    print(f"Initial Free Physical Blocks in VRAM: {len(manager.free_blocks)}")

    # Request 1: 35 tokens -> Needs ceil(35/16) = 3 blocks
    r1_blocks = manager.allocate_for_request("req_101", num_tokens=35)
    print(f"Request 101 Allocated Physical Blocks: {r1_blocks} (Non-contiguous virtual paging)")

    # Request 2: 20 tokens -> Needs ceil(20/16) = 2 blocks
    r2_blocks = manager.allocate_for_request("req_102", num_tokens=20)
    print(f"Request 102 Allocated Physical Blocks: {r2_blocks}")

    print(f"Remaining Free VRAM Blocks: {len(manager.free_blocks)}")

    # Request 1 completes and releases VRAM
    manager.free_request("req_101")
    print(f"After Request 101 Release -> Free Blocks: {len(manager.free_blocks)} (Memory instantly recycled!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Setting Block Size Too Large or Small: Agar block size sirf 4 tokens ho to block table metadata overhead barh jata hai; agar block size 128 ho to internal fragmentation dobara barh jati hai. Research sabit karti hai ke `block_size = 16` ya `32` optimal standard hai.
2. Incompatible CUDA Drivers with vLLM C++ Kernels: vLLM pre-compiled FlashAttention C++ kernels use karta hai. Host machine par agar CUDA toolkit aur PyTorch version mismatch ho to `ImportError: cannot load custom C extension` aata hai. Hamesha official vLLM Docker container use karein.
3. Ignoring Chunked Prefill in Mixed Workloads: Agar ek user 10,000 tokens ka document bhej de aur 10 users chotay sawal poochein, to lamba prefill poore server ko 2 second ke liye freeze kar deta hai. vLLM mein hamesha `--enable-chunked-prefill` flag on karein.

Zero-GPU Tip:
vLLM CPU backend support karta hai (`vllm-cpu` build) jo OpenVINO aur AVX-512 vectorization se multi-threaded CPU par PagedAttention chalata hai. Laptop par CPU build se virtual block management test kiya ja sakta hai.

Self-Check Questions:
1. PagedAttention OS virtual memory paging ki tarah internal memory fragmentation ko kaise khatam karti hai?
2. Static contiguous memory allocation ke muqablay vLLM serving throughput ko 5x se 10x kaise barhati hai?
3. Continuous Batching aur Static Batching mein kya farq hai?

What to Build Next:
Ek Production vLLM Docker Compose setup likhein jo LLaMA-3.1-8B-Instruct ko OpenAI-compatible REST server ke taur par serve kare with max model context 8192 aur metrics logging."""

# ==============================================================================
# LESSON 11.2: Model Quantization Deep Dive: AWQ, GPTQ & KV Cache Compression
# ==============================================================================
LESSON_CONTENT['11.2'] = r"""### Part 1: Mental Model & South Asian Analogy
Deep Learning models mein har weight aam tor par 16-bit Float (FP16) hota hai. Ek 70B parameter model 140 GB VRAM mangta hai. Lekin reality yeh hai ke tamam weights barabar ahem nahi hote! 99% weights aam hote hain, jabke sirf 1% weights critical (Salient) hote hain. Yahan se paida hoti hai **Model Quantization (AWQ, GPTQ, aur FP8)**!
Isay samajhne ke liye kisi Shehar ke Road Traffic aur VIP Protocol ki misaal lein:
1. Naive Rounding (Bila Soche Samjhe Wazan Kam Karna): Agar aap tamam 16-bit numbers ko round karke seedha 4-bit integer bana dein to model andha ho jata hai aur gibberish text bolne lagta hai (Perplexity Explosion).
2. AWQ - Activation-aware Weight Quantization (VIP Gaariyon Ko VIP Protocol Dena): AWQ ek nihayat aqalmand observation par mushtamil hai: Model ke sirf 1% weights aise hote hain jin par aane wali activations bohot bari hoti hain (Salient Weights). AWQ kehta hai: "In 1% VIP weights ko bilkul touch mat karo! Inhe full precision ya high scale factor do, aur baqi 99% aam weights ko 4-bit compress kar do!" Nateeja: Model ka size 70% ghir jata hai lekin reasoning accuracy bilkul 99.5% barqarar rehti hai!
3. GPTQ (Second-Order Hessian Inversion): GPTQ ek data-driven calibration technique hai jo ek chotay dataset (e.g. 128 Wikipedia paragraphs) par calculus ka Hessian matrix calculate karti hai aur har round hone wale weight ki ghalti ko uske parosi weights par mathematically adjust kar deti hai.
4. FP8 (8-bit Floating Point - 2026 Modern Standard): NVIDIA Hopper (H100) aur Ada Lovelace (L40S) chips mein hardware FP8 Tensor Cores aaye hain jo bina kisi accuracy loss ke 2x speedup aur 50% memory reduction dete hain.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Uniform Symmetric Min-Max Quantization ka exact mathematical formula trace karte hain: 32-bit Float to 8-bit Integer (INT8).
Formula for Symmetric Quantization:
$\text{Scale} (s) = \frac{\max(|x|)}{2^{b-1} - 1} = \frac{\max(|x|)}{127}$
$\text{Quantized INT8 } (q) = \text{round}\left( \frac{x}{s} \right)$
$\text{Dequantized Float } (\hat{x}) = q \times s$

Worked Numeric Example:
Weight Vector (Floating-point weights):
$W = [-1.80, 0.45, 1.27, 2.54]$
Bits $b = 8 \implies \text{INT8 range } [-127, +127]$.

Step 1: Compute Maximum Absolute Value ($\max(|W|)$)
$\max(|-1.80|, |0.45|, |1.27|, |2.54|) = 2.5400$

Step 2: Compute Quantization Scale Factor ($s$)
$s = \frac{2.5400}{127} = 0.0200$

Step 3: Quantize Weights to INT8 Integers
- $q_0 = \text{round}\left( \frac{-1.80}{0.02} \right) = \text{round}(-90.0) = -90$
- $q_1 = \text{round}\left( \frac{0.45}{0.02} \right) = \text{round}(22.5) = +23$ (Rounded)
- $q_2 = \text{round}\left( \frac{1.27}{0.02} \right) = \text{round}(63.5) = +64$
- $q_3 = \text{round}\left( \frac{2.54}{0.02} \right) = \text{round}(127.0) = +127$
Quantized INT8 Tensor: $[-90, 23, 64, 127]$ (Each number now takes only 1 Byte instead of 4 Bytes -> $4\times \text{ Memory Reduction}$)!

Step 4: Dequantization and Error Verification ($\hat{W} = q \times 0.02$)
- $\hat{w}_0 = -90 \times 0.02 = -1.8000$ (Error: $0.000$)
- $\hat{w}_1 = 23 \times 0.02 = 0.4600$ (Error: $0.46 - 0.45 = +0.010$)
- $\hat{w}_2 = 64 \times 0.02 = 1.2800$ (Error: $1.28 - 1.27 = +0.010$)
- $\hat{w}_3 = 127 \times 0.02 = 2.5400$ (Error: $0.000$)
Maximum quantization error is only $0.010$! Hardware INT8 tensor cores multiply these 1-byte integers at 2x the speed of standard floating points.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum symmetric uniform quantization aur dequantization functions from scratch implement karte hain, quantization error (MSE) calculate karte hain, aur memory footprint benchmark karte hain.

```python
import torch
from typing import Tuple

def quantize_symmetric_int8(tensor_float: torch.Tensor) -> Tuple[torch.Tensor, float]:
    \"\"\"Quantizes continuous floating-point tensor into signed INT8 with scaling factor.\"\"\"
    max_val = torch.max(torch.abs(tensor_float)).item()
    # Scale factor mapping max float to 127
    scale = max(max_val, 1e-8) / 127.0
    
    # Quantize and clip to int8 limits [-127, 127]
    quantized = torch.round(tensor_float / scale).clamp(-127, 127).to(torch.int8)
    return quantized, scale

def dequantize_symmetric_int8(tensor_int8: torch.Tensor, scale: float) -> torch.Tensor:
    \"\"\"Reconstructs floating-point tensor from INT8 and scale factor.\"\"\"
    return tensor_int8.float() * scale

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    # Simulate weight matrix [1024, 1024]
    raw_weights = torch.randn(1024, 1024, dtype=torch.float32)

    # 1. Execute INT8 Quantization
    q_weights, scale_factor = quantize_symmetric_int8(raw_weights)
    reconstructed_weights = dequantize_symmetric_int8(q_weights, scale_factor)

    # 2. Inspect Memory Footprint
    mem_fp32 = raw_weights.element_size() * raw_weights.nelement()
    mem_int8 = q_weights.element_size() * q_weights.nelement()
    
    # 3. Compute Quantization Error Metrics
    mse_error = torch.mean((raw_weights - reconstructed_weights) ** 2).item()
    snr_db = 10.0 * torch.log10(torch.mean(raw_weights ** 2) / (torch.mean((raw_weights - reconstructed_weights) ** 2) + 1e-9)).item()

    print(f"FP32 Tensor Memory:       {mem_fp32 / 1024:.2f} KB (4 Bytes per weight)")
    print(f"INT8 Tensor Memory:       {mem_int8 / 1024:.2f} KB (1 Byte per weight)")
    print(f"Hardware Memory Savings:  {mem_fp32 / mem_int8:.1f}x compression!")
    print(f"Mean Squared Error (MSE): {mse_error:.6f}")
    print(f"Signal-to-Noise Ratio:    {snr_db:.2f} dB (High fidelity preservation)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Using Post-Training Quantization (PTQ) on Sub-1B Models: 1B se chotay models mein parameters itne kam hote hain ke unhe 4-bit karne se model completely break ho jata hai. 4-bit AWQ/GPTQ hamesha 7B ya us se baray models par behtareen kaam karti hai.
2. Quantizing Normalization Layers (LayerNorm / RMSNorm): LayerNorm aur Biases pure network mein sirf 0.01% parameters leti hain lekin scale stability maintain karti hain. Inhe quantize karne se severe perplexity loss hota hai. Hamesha sirf 2D linear weight matrices ko quantize karein.
3. Confusing AWQ with GPTQ Serving Speeds: AWQ hardware execution ke liye zyada friendly hai kyunke yeh activations ko scale karti hai bina complex permutation tables ke. Modern inference engines (vLLM) par AWQ GPTQ se 1.3x tez serve hoti hai.

Zero-GPU Tip:
Quantization math, scale calculations, aur INT8 simulation pure CPU operations hain. Local laptop par bina kisi GPU ke aap model weights ke MSE error ko verify kar sakte hain.

Self-Check Questions:
1. AWQ (Activation-aware Weight Quantization) 1% salient weights ko protected kyu rakhti hai?
2. INT8 Quantization 32-bit Float ke muqablay memory ko 4x kaise kam karti hai?
3. Modern serving mein FP8 hardware quantization FP16 ke muqablay kya speedup deti hai?

What to Build Next:
Ek Weight Quantization Simulator script banayein jo ek PyTorch model ke linear layers ko INT4 mein quantize kare, perplexity drift measure kare, aur per-layer reconstruction error report kare."""

# ==============================================================================
# LESSON 11.3: High-Concurrency LLM Reverse Proxy & Gateway in Rust Axum
# ==============================================================================
LESSON_CONTENT['11.3'] = r"""### Part 1: Mental Model & South Asian Analogy
Python backend (jaise FastAPI) AI prototypes ke liye zabardast hai. Lekin jab aapki service par rozana 50 lakh requests aa rahi hon aur aapko har microsecond latency bachani ho, to Python ka GIL aur garbage collection pauses bottleneck ban jate hain. 2026 mein enterprise AI reverse proxies aur gateways **Rust (Axum / Actix-Web)** mein likhi jati hain!
Isay samajhne ke liye kisi Rickshaw vs Metro Bullet Train ki misaal lein:
1. Python FastAPI Gateway (Rickshaw): Aam traffic mein bohot aasan hai, har gali mein murr jata hai. Lekin jab 100,000 musafir aik sath aa jayein to rickshaw ke engine se dhuwan nikalne lagta hai aur memory leak hone lagti hai.
2. Rust Axum Gateway (Bullet Train): Rust mein koi Garbage Collector (GC) nahi hota; memory compile-time par RAII (Resource Acquisition Is Initialization) aur ownership borrow checker ke zariye exact release hoti hai. Rust ka asynchronous runtime (Tokio) ek akelay server par 100,000 concurrent HTTP connections ko baghair kisi memory spike ke serve karta hai!
3. Reverse Proxy Tasks (Darwazay Ke Kam):
   - Auth JWT Verification: User token check karna (0.1ms).
   - Rate Limiting via Leaky Bucket: 100 requests per minute enforce karna.
   - Streaming SSE Pipe: GPU vLLM cluster se aane wale tokens ko client tak zero-copy pipe karna.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Token Bucket Rate Limiting Algorithm ka exact mathematical formula trace karte hain.
Token Bucket Parameters:
- Bucket Capacity $B_{\text{max}} = 10$ tokens
- Refill Rate $r = 2$ tokens per second
- Last Refill Timestamp $t_{\text{last}}$
- Current Request Timestamp $t_{\text{now}}$

Refill Calculation at Current Request:
$\Delta t = t_{\text{now}} - t_{\text{last}}$
$\text{New Tokens} = \min(B_{\text{max}}, B_{\text{current}} + \Delta t \times r)$

Worked Numeric Scenario:
User makes 10 rapid burst requests at $t = 0.0\text{s}$.
- Bucket drops from 10 to 0 tokens: All 10 requests allowed!
- At $t = 0.5\text{s}$, User sends 11th request:
  $\Delta t = 0.5 - 0.0 = 0.5 \text{ seconds}$.
  Refill: $0 + (0.5 \times 2) = 1.0 \text{ token}$.
  Request consumes 1 token. Available: 0 tokens -> ALLOWED!
- At $t = 0.6\text{s}$, User sends 12th request:
  $\Delta t = 0.6 - 0.5 = 0.1 \text{ seconds}$.
  Refill: $0 + (0.1 \times 2) = 0.2 \text{ tokens}$.
  Chunke $0.2 < 1.0$, request ke liye token mojud nahi hai!
Decision:
Gateway immediately rejects request with **HTTP 429 Too Many Requests** in 0.05 milliseconds without hitting backend vLLM GPUs!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Rust Axum architecture ke concurrent token bucket rate limiter aur proxy forwarder pattern ko high-performance Python simulation mein implement karte hain.

```python
import time
from typing import Dict, Tuple

class TokenBucketRateLimiter:
    \"\"\"Production Token Bucket algorithm implementing rate limiting for AI API gateways.\"\"\"
    def __init__(self, capacity: int = 10, refill_rate_per_sec: float = 2.0) -> None:
        self.capacity = float(capacity)
        self.refill_rate = refill_rate_per_sec
        # Maps user_id -> (current_tokens, last_refill_timestamp)
        self.buckets: Dict[str, Tuple[float, float]] = {}

    def allow_request(self, user_id: str, cost: float = 1.0) -> Tuple[bool, float]:
        now = time.monotonic()
        if user_id not in self.buckets:
            self.buckets[user_id] = (self.capacity, now)

        current_tokens, last_time = self.buckets[user_id]
        
        # 1. Refill tokens proportional to elapsed time
        elapsed = now - last_time
        refilled_tokens = min(self.capacity, current_tokens + (elapsed * self.refill_rate))

        # 2. Check if enough tokens available
        if refilled_tokens >= cost:
            # Deduct tokens and update timestamp
            self.buckets[user_id] = (refilled_tokens - cost, now)
            return True, refilled_tokens - cost
        else:
            # Reject request without modifying tokens
            self.buckets[user_id] = (refilled_tokens, now)
            return False, refilled_tokens

# Execution test
if __name__ == "__main__":
    limiter = TokenBucketRateLimiter(capacity=3, refill_rate_per_sec=2.0)
    user = "usr_karachi_401"

    print("--- Burst Traffic Simulation ---")
    for req_num in range(1, 5):
        allowed, remaining = limiter.allow_request(user)
        print(f"Request {req_num}: Allowed={allowed} | Tokens Remaining: {remaining:.2f}")

    print("\\nWaiting 1.0 second for token refill...")
    time.sleep(1.0)

    allowed, remaining = limiter.allow_request(user)
    print(f"Post-Refill Request 5: Allowed={allowed} | Tokens Remaining: {remaining:.2f} (Restored capacity!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. In-Memory Rate Limiting Across Clustered Gateways: Rate limiter state agar server memory mein ho to load balancer doosre server par request bhej deta hai aur limit bypass ho jati hai. Production mein rate limits hamesha Redis cluster (`redis-cell` ya atomic Lua scripts) mein chalayein.
2. Holding Client Connections Open on Backend Timeouts: Agar backend vLLM GPU hang ho jaye aur gateway timeout na lagaye to hazaron TCP connections leak ho jati hain. Hamesha strict 30-second socket timeout lagayein.
3. Parsing JSON Bodies in Reverse Proxy Path: Reverse proxy ko token stream karne ke liye JSON body parse karne ki zaroorat nahi hoti; raw bytes ko seedha stream (Zero-Copy chunk piping) karna chahiye taake CPU usage 0% rahe.

Zero-GPU Tip:
Reverse proxies aur rate limiters pure networking infrastructure hain jo CPU par chalte hain. Rust Axum ya Go gateways kisi bhi cheap $5/month cloud VPS par 50,000 requests per second handle kar sakte hain.

Self-Check Questions:
1. Python ke muqablay Rust Axum high-concurrency AI gateways mein memory efficiency kyun deta hai?
2. Token Bucket Algorithm burst traffic aur sustained traffic ko kaise balance karta hai?
3. HTTP 429 status code ke sath `Retry-After` header bhejne ka kya faida hota hai?

What to Build Next:
Ek Lightweight Rust Axum Reverse Proxy banayein jo incoming `/v1/chat/completions` request ko rate-limit kare, bearer token check kare, aur backend vLLM endpoint par forward kare."""

# ==============================================================================
# LESSON 11.4: Production LLM Observability: OpenTelemetry & Langfuse
# ==============================================================================
LESSON_CONTENT['11.4'] = r"""### Part 1: Mental Model & South Asian Analogy
Jab aapki AI application production mein chalti hai aur koi customer complaint karta hai: "Kal raat bot ne mujhe ghalat jawab diya tha!", to agar aapke paas logs na hon to andheray mein teer chalane jaisa hota hai. Traditional web APM (Datadog ya NewRelic) AI ke liye kafi nahi hota kyunke unhe Tokens, Cost, Prompt Versions, aur Vector Retrieval Latency ka pata nahi hota. Yahan aati hai **Production LLM Observability with OpenTelemetry & Langfuse**!
Isay samajhne ke liye kisi Black Box Flight Data Recorder (Hawai Jahaz Ka Black Box) ki misaal lein:
1. The Flight Recorder (Langfuse Tracing): Jahaz ki har movement, altitude, aur pilot ki guftagu black box mein record hoti hai. Langfuse har user request ka poora 'Trace' save karta hai:
   - Root Trace: User ne kya pucha? Kitne baje?
   - Child Span 1: Vector search ne kaun se 3 documents nikale? (Latency: 45ms)
   - Child Span 2: Re-ranker ne kis document ko top par rakha? (Latency: 20ms)
   - Child Span 3: LLM ne kitne input tokens liye aur kitne output tokens diye? (Latency: 800ms)
2. Cost & Token Accounting: Langfuse har API call ka exact hisab lagata hai: "Is session par $0.0034 kharch hue." Company ka finance director rozana dashboard par dekh sakta hai ke kis customer ya feature par kitna paisa lag raha hai.
3. User Feedback Tracking (Thumbs Up / Down): User screen par jab thumbs up ya thumbs down dabata hai, to woh feedback seedha us specific generation trace ke sath jor diya jata hai taake data scientists ghalat jawab ko fine-tuning dataset mein bhej sakein.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein OpenTelemetry Trace Tree Hierarchy aur Latency Waterfall ka exact hisab lagayein.
Hierarchical Trace Structure:
Parent Trace: `user_chat_request` ($T_{\text{total}}$)
- Span A: `input_guardrail_check` (Duration $t_A$)
- Span B: `vector_db_retrieval` (Duration $t_B$)
- Span C: `llm_generation` (Duration $t_C$)

Sequential Latency Waterfall Math:
- $t_A = 12 \text{ ms}$
- $t_B = 48 \text{ ms}$
- $t_C = 640 \text{ ms}$
Total End-to-End Latency:
$T_{\text{total}} = t_A + t_B + t_C = 12 + 48 + 640 = 700 \text{ ms}$.

Token Economics Audit Calculation:
- Prompt Tokens $= 450$ tokens
- Completion Tokens $= 150$ tokens
- Input Pricing: $\$0.15$ per 1M tokens
- Output Pricing: $\$0.60$ per 1M tokens

Cost per component:
$C_{\text{in}} = \frac{450}{1,000,000} \times 0.15 = 0.0000675 \text{ USD}$
$C_{\text{out}} = \frac{150}{1,000,000} \times 0.60 = 0.0000900 \text{ USD}$
$C_{\text{total}} = 0.0000675 + 0.0000900 = 0.0001575 \text{ USD}$.
Langfuse is trace ko instantly index karta hai: Latency 700ms, Cost $0.000157, Model LLaMA-3.3-70B. Agar latency achanak 2000ms cross kare to real-time Slack alert trigger hota hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum OpenTelemetry-compliant trace span context manager, token accounting, aur Langfuse telemetry logger implement karte hain.

```python
import time
import uuid
from typing import Dict, Any, List

class MockSpan:
    \"\"\"Represents individual telemetry execution span in an OpenTelemetry trace tree.\"\"\"
    def __init__(self, name: str, parent_id: str | None = None) -> None:
        self.span_id = f"span_{uuid.uuid4().hex[:6]}"
        self.parent_id = parent_id
        self.name = name
        self.start_time = 0.0
        self.duration_ms = 0.0
        self.attributes: Dict[str, Any] = {}

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.duration_ms = round((time.perf_counter() - self.start_time) * 1000.0, 2)

class ProductionObservabilityTracer:
    \"\"\"Telemetry collector exporting OpenTelemetry-style GenAI metrics.\"\"\"
    def __init__(self) -> None:
        self.completed_traces: List[Dict[str, Any]] = []

    def log_full_request_trace(
        self, 
        trace_id: str, 
        spans: List[MockSpan], 
        prompt_tokens: int, 
        completion_tokens: int
    ) -> Dict[str, Any]:
        # Cost calculation based on official pricing tiers
        cost_usd = (prompt_tokens / 1e6 * 0.15) + (completion_tokens / 1e6 * 0.60)
        total_latency = sum(s.duration_ms for s in spans)

        trace_record = {
            "trace_id": trace_id,
            "timestamp": time.time(),
            "total_latency_ms": round(total_latency, 2),
            "tokens": {"prompt": prompt_tokens, "completion": completion_tokens, "total": prompt_tokens + completion_tokens},
            "cost_usd": round(cost_usd, 6),
            "spans": [{ "name": s.name, "duration_ms": s.duration_ms, "attrs": s.attributes } for s in spans]
        }
        self.completed_traces.append(trace_record)
        return trace_record

# Execution test
if __name__ == "__main__":
    tracer = ProductionObservabilityTracer()
    trace_id = f"trace_{uuid.uuid4().hex[:8]}"
    active_spans = []

    # 1. Span 1: Vector Search
    with MockSpan("vector_search") as s1:
        time.sleep(0.04)  # 40ms simulation
        s1.attributes["retrieved_k"] = 3
        active_spans.append(s1)

    # 2. Span 2: LLM Generation
    with MockSpan("llm_generation") as s2:
        time.sleep(0.12)  # 120ms simulation
        s2.attributes["model"] = "llama-3.3-70b-versatile"
        active_spans.append(s2)

    # Export trace
    exported = tracer.log_full_request_trace(
        trace_id=trace_id,
        spans=active_spans,
        prompt_tokens=320,
        completion_tokens=85
    )

    print(f"OpenTelemetry Trace Logged Successfully!")
    print(f"Trace ID:      {exported['trace_id']}")
    print(f"Total Latency: {exported['total_latency_ms']} ms")
    print(f"Billed Cost:   ${exported['cost_usd']} USD")
    print("Span Waterfall Breakdown:")
    for s in exported["spans"]:
        print(f"  - {s['name']:18s}: {s['duration_ms']} ms (Metadata: {s['attrs']})")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Synchronous Logging in the Critical Request Path: Agar trace logger remote observability server (Langfuse cloud) ko synchronous HTTP call bhejta hai to user latency mein 100ms faltu add ho jate hain. Telemetry hamesha background async queue ya non-blocking worker thread se flush karein.
2. Logging Sensitive Customer PII into Traces: User ki chat history aur prompts observability dashboard par visible hote hain. Presidio se PII sanitize kiye baghair raw prompt log karna compliance audit fail kar deta hai.
3. Not Propagating Trace IDs: Frontend se aane wale request ID ko backend spans ke sath match na karne se frontend error ko backend GPU trace se link karna namumkin ho jata hai. Hamesha `traceparent` HTTP header propagate karein.

Zero-GPU Tip:
OpenTelemetry tracing, metrics calculation, aur Langfuse instrumentation 100% CPU bound background tasks hain. Inhe test karne ke liye kisi GPU ki zaroorat nahi hai. Local dockerized Langfuse instance par live traces inspect karein.

Self-Check Questions:
1. Traditional Application Performance Monitoring (APM) ke muqablay LLM Observability mein kaun se metrics khas hote hain?
2. OpenTelemetry mein Trace aur Span ke darmiyan kya talluq hota hai?
3. Telemetry logging ko synchronous request path ke bajaye asynchronous batch worker par kyun chalana chahiye?

What to Build Next:
Langfuse SDK (`langfuse-python`) ko ek FastAPI app mein integrate karein using `@observe()` decorator taake har chat endpoint ka token usage aur latency trace automated dashboard par visual stream ho."""

# ==============================================================================
# LESSON 11.5: Enterprise Cluster Serving: Kubernetes, KServe, Ray & Autoscaling
# ==============================================================================
LESSON_CONTENT['11.5'] = r"""### Part 1: Mental Model & South Asian Analogy
Jab aapki application rozana karoron tokens serve karti hai to ek akela GPU server kafi nahi hota. Aapko 20 se 50 GPUs ka poora cluster chalana parta hai jisme traffic ke mutabiq GPUs khud ba khud barhein (Scale Up) aur raat ko jab traffic kam ho to GPUs band ho kar paise bachayein (Scale Down). Is orchestration ka badshah **Kubernetes, KServe, aur Ray Cluster** hai!
Isay samajhne ke liye kisi Shehar ke Taxi Stand aur Smart Dispatcher ki misaal lein:
1. The Single Taxi (Ek Akela Server): Agar taxi stand par sirf ek taxi ho to office ke rash ke waqt 500 musafir line mein lag kar phans jate hain.
2. Kubernetes (Plaza Ka Grand Manager): Kubernetes tamam servers (Nodes) ko dekhta hai. Agar koi server kharab ho kar jal jaye to Kubernetes foran naya server khara kar ke model deploy kar deta hai (Self-Healing).
3. Ray Cluster (GPU Orchestration Fabric): Ray deep learning ka multi-node communication fabric hai. Agar model 70B ka ho jo ek GPU mein fit na aata ho, to Ray Tensor Parallelism ke zariye model ko 4 GPUs par baant deta hai (`tensor_parallel_size=4`).
4. Horizontal Pod Autoscaler (HPA - Maang Ke Mutabiq Taxis Mangwana):
   - Subah 9 baje traffic barhi: Queue mein 50 requests phans gayi $\to$ HPA foran 5 naye GPU pods launch karta hai!
   - Raat 2 baje traffic khatam hui: HPA faltu GPUs ko terminate kar deta hai taake cloud bill zero ho jaye.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Autoscaling Trigger Calculation based on vLLM Queue Concurrency ka exact hisab lagayein.
Autoscaling Metric: Concurrency per Replica ($C_{\text{target}}$)
Formula for Target Replicas:
$\text{Desired Replicas} = \lceil \frac{\text{Current Total Active Requests}}{C_{\text{target}}} \rceil$
Jahan:
- Target Concurrency per GPU Replica $C_{\text{target}} = 15$ concurrent requests (Max optimal vLLM throughput before latency degrades).
- Min Replicas $= 2$ (High availability base)
- Max Replicas $= 10$ (Budget ceiling)

Worked Traffic Surge Scenario:
Current State: 2 active GPU pods running.
Flash Sale / Breaking News Event:
Prometheus records active incoming requests spiking to:
$\text{Current Total Requests} = 85 \text{ requests}$.

Step 1: Compute Raw Required Pods
$\text{Raw Replicas} = \frac{85}{15} \approx 5.6667$

Step 2: Take Ceiling and Apply Clamp Bounds
$\text{Desired Replicas} = \lceil 5.6667 \rceil = 6 \text{ pods}$.
Clamp check:
$\text{Min (2)} \le 6 \le \text{Max (10)} \implies 6 \text{ pods accepted!}$

Step 3: Scaling Decision:
Kubernetes HPA controller triggers scaling event:
"Scaling GPU Deployment from 2 to 6 replicas (+4 GPUs launched) to absorb 85 concurrent users within 15-concurrency SLA."
User latency 400ms par stable rehti hai aur system collapse hone se bach jata hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Kubernetes HPA Autoscaler controller simulation aur Ray multi-node worker actor distribution engine implement karte hain.

```python
import math
from typing import List, Dict, Any

class MockHPAController:
    \"\"\"Simulates Kubernetes Horizontal Pod Autoscaler evaluating GPU queue depth.\"\"\"
    def __init__(self, target_concurrency: int = 15, min_pods: int = 2, max_pods: int = 10) -> None:
        self.target_concurrency = target_concurrency
        self.min_pods = min_pods
        self.max_pods = max_pods
        self.current_pods = min_pods

    def evaluate_scale(self, active_concurrency: int) -> Dict[str, Any]:
        # Desired = ceil(active / target)
        raw_desired = math.ceil(active_concurrency / self.target_concurrency)
        # Apply min/max boundary clamping
        target_pods = max(self.min_pods, min(self.max_pods, raw_desired))
        
        action = "MAINTAIN"
        if target_pods > self.current_pods:
            action = f"SCALE_UP (+{target_pods - self.current_pods} pods)"
        elif target_pods < self.current_pods:
            action = f"SCALE_DOWN (-{self.current_pods - target_pods} pods)"

        self.current_pods = target_pods

        return {
            "active_concurrency": active_concurrency,
            "target_concurrency_per_pod": self.target_concurrency,
            "allocated_pods": self.current_pods,
            "scaling_action": action
        }

# Execution test
if __name__ == "__main__":
    hpa = MockHPAController(target_concurrency=15, min_pods=2, max_pods=8)

    print("Initial Cluster State: 2 GPU Pods running.\\n")

    traffic_samples = [10, 45, 95, 20]
    for minute, traffic in enumerate(traffic_samples, 1):
        decision = hpa.evaluate_scale(traffic)
        print(f"Minute {minute:02d} -> Traffic: {decision['active_concurrency']:2d} reqs | Action: {decision['scaling_action']:18s} | Total Pods: {decision['allocated_pods']}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Autoscaling on CPU/Memory Metrics Instead of Queue Depth: LLM GPU pods hamesha 90% VRAM pre-allocate rakhte hain. Agar aap standard Kubernetes CPU/RAM metrics par autoscale karenge to pod hamesha scale up karta rahega! Hamesha vLLM metric `vllm:num_requests_waiting` (Queue depth) par autoscale karein.
2. Cold Start Latency Penalty (5-Minute Model Download): Naya GPU pod launch hote waqt agar 15 GB ka model Hugging Face se download kare to 5 minute lag jate hain aur spike guzar chuki hoti hai. Hamesha persistent network volume (NFS / EFS / Cloud Storage) par model pre-cache rakhein taake pod 15 second mein start ho sake.
3. Flapping / Thrashing (Fast Scale-Up Followed by Instant Scale-Down): Traffic mein thoda sa dip aate hi pod delete karne se aglay second dobara scale up karna parta hai. Hamesha Kubernetes `scaleDown.stabilizationWindowSeconds = 300` (5-minute cool-down) lagayein.

Zero-GPU Tip:
Kubernetes YAML manifests likhna, KEDA autoscaling rules configure karna, aur Ray cluster job scripts verify karna pure DevOps orchestration hai. Minikube ya Kind cluster local CPU par chala kar aap poora scaling logic verify kar sakte hain.

Self-Check Questions:
1. LLM serving cluster mein traditional CPU metrics ke bajaye Queue Concurrency metric par autoscale kyun kiya jata hai?
2. Ray framework multi-GPU Tensor Parallelism mein kya kirdaar ada karta hai?
3. GPU pod cold-start latency ko 5 minute se 15 second par kaise laya jata hai?

What to Build Next:
Ek Kubernetes KEDA ScaledObject manifest (`scaledobject.yaml`) likhein jo Prometheus se vLLM waiting requests query kare aur 0 se 5 GPU pods tak dynamic scale up/down automate kare."""

# ==============================================================================
# LESSON 11.6: Module 11 Capstone: Production High-Throughput Cluster (99.9% SLA)
# ==============================================================================
LESSON_CONTENT['11.6'] = r"""### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne Production MLOps aur AI Engineering ke tamam azeem sutoon (vLLM PagedAttention, AWQ Model Quantization, Rust reverse proxies, OpenTelemetry observability, aur Kubernetes cluster autoscaling) master kar liye hain. Ab waqt hai aapke **Grand Production Serving Cluster Capstone** ka!
Is Capstone project ka zehni khaka kisi Bare National Stock Exchange (PSX) ke Trading Matching Engine jaisa hai:
1. The High-Performance Front Line (Rust/FastAPI Gateway): Rozana karoron requests aati hain. Gateway 1 millisecond mein authentication, rate-limiting, aur semantic caching execute karta hai.
2. The Engine Fleet (vLLM PagedAttention GPU Pods): Multiple 4-bit AWQ quantized LLaMA-3 replicas chal rahe hain jo continuous batching ke sath 100+ requests per second generate karte hain.
3. The Auto-Pilot Dispatcher (KEDA Queue Depth Autoscaler): Cluster queue ko monitor karta hai: jaise hi rash barhta hai, naye GPU pods foran bootstrap ho jate hain.
4. The Central Black Box (OpenTelemetry & Langfuse): Har token, cost, aur latency span live Grafana dashboard par report hota hai.
5. The 99.9% High-Availability SLA: Agar koi GPU achanak hardware error se crash ho jaye to circuit breaker microsecond mein traffic doosre pod par divert kar deta hai. User ko zero downtime mehsoos hota hai.

Yeh Capstone project enterprise level standard serving architecture hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Cluster SLA Uptime aur Error Budget ka exact hisab lagayein.
SLA Target: 99.9% Uptime (The "Three Nines" Standard).
Calculation of Allowed Downtime per Month (30 Days):
Total seconds in a month:
$T_{\text{month}} = 30 \times 24 \times 3600 = 2,592,000 \text{ seconds}$.
Allowed Downtime Percentage:
$100\% - 99.9\% = 0.1\% = 0.001$.
Allowed Downtime in Seconds:
$\text{Allowed Downtime} = 2,592,000 \times 0.001 = 2,592 \text{ seconds} \approx 43.2 \text{ minutes per month}$!

Throughput & Concurrency Economics:
- Daily Query Volume = 500,000 requests
- Peak Traffic Ratio = $3\times \text{ average}$
- Average Request Rate $= \frac{500,000}{86400} \approx 5.8 \text{ RPS}$
- Peak Request Rate $= 5.8 \times 3 \approx 17.4 \text{ RPS}$
- Average Generation Latency per request $= 0.5 \text{ seconds}$.
Peak Concurrent In-Flight Connections:
By Little's Law:
$L = \lambda \times W = 17.4 \text{ req/s} \times 0.5 \text{ s} \approx 8.7 \approx 9 \text{ concurrent streams}$.
Single vLLM 4-bit LLaMA-3.1-8B GPU pod on RTX 3090 easily supports **32 concurrent streams**!
Single Pod Headroom Ratio:
$\frac{32}{9} \approx 3.5\times \text{ Safety Headroom}$!
Do pods chalane se cluster 100% redundant aur resilient rehta hai with 99.9% SLA guaranteed!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete Capstone Cluster Serving Manager implement karte hain: health checking, multi-pod load balancing, automatic failover, aur throughput metrics reporting.

```python
import time
import asyncio
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class GPUPodNode:
    pod_id: str
    is_healthy: bool = True
    active_connections: int = 0
    max_concurrency: int = 30
    total_served: int = 0

class ProductionServingCluster:
    \"\"\"Production multi-pod LLM serving cluster with active load balancing and failover.\"\"\"
    def __init__(self, pods_count: int = 2) -> None:
        self.pods: List[GPUPodNode] = [
            GPUPodNode(pod_id=f"vllm_gpu_pod_{i}") for i in range(pods_count)
        ]

    def get_optimal_healthy_pod(self) -> GPUPodNode:
        \"\"\"Least-Connections routing strategy across healthy worker pods.\"\"\"
        healthy_pods = [p for p in self.pods if p.is_healthy]
        if not healthy_pods:
            raise RuntimeError("CRITICAL ALERT: All GPU worker pods are DOWN! 99.9% SLA breached.")
        # Pick healthy pod with minimum active in-flight connections
        healthy_pods.sort(key=lambda x: x.active_connections)
        return healthy_pods[0]

    async def execute_inference(self, prompt: str) -> Dict[str, Any]:
        t0 = time.perf_counter()
        pod = self.get_optimal_healthy_pod()
        
        # Acquire slot
        pod.active_connections += 1
        try:
            # Simulate high-speed vLLM PagedAttention inference
            await asyncio.sleep(0.05)
            pod.total_served += 1
            output_text = f"Completed by {pod.pod_id}: Response for '{prompt}'"
        finally:
            pod.active_connections -= 1

        elapsed_ms = (time.perf_counter() - t0) * 1000.0
        return {
            "status": "success",
            "served_by": pod.pod_id,
            "latency_ms": round(elapsed_ms, 2),
            "output": output_text
        }

# Execution test
if __name__ == "__main__":
    async def run_cluster_simulation():
        cluster = ProductionServingCluster(pods_count=3)
        print("Initialized Production Serving Cluster with 3 GPU Pods.\\n")

        # Simulate 6 concurrent incoming requests
        prompts = [f"Batch query {i}" for i in range(1, 7)]
        print("Dispatching 6 concurrent requests via Least-Connections load balancer...")
        tasks = [cluster.execute_inference(p) for p in prompts]
        results = await asyncio.gather(*tasks)

        for res in results[:3]:
            print(f"  {res['status'].upper()} -> Pod: {res['served_by']} in {res['latency_ms']} ms")

        # Simulate Hardware Failure on Pod 0
        print("\\n[CHAOS TEST] Inducing unexpected hardware crash on vllm_gpu_pod_0...")
        cluster.pods[0].is_healthy = False

        # Dispatch additional traffic
        recovery_res = await cluster.execute_inference("Urgent query post-crash")
        print(f"Automatic Failover Succeeded! Served by: {recovery_res['served_by']} (Zero client downtime!)")

    asyncio.run(run_cluster_simulation())
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Round-Robin Routing on Variable-Length LLM Requests: Round-robin load balancing yeh nahi dekhti ke kis pod par 5000-token ka lamba document phansa hua hai. Hamesha **Least-Connections ya Queue-Depth Routing** use karein.
2. Lack of Automatic Kubernetes Liveness Probes: Agar GPU process CUDA out-of-memory par hang ho jaye lekin container exit na kare to traffic us dead pod par jati rehti hai. Hamesha `/health` endpoint par active HTTP liveness probe lagayein.
3. Hardcoded Cluster Secrets in Git: GPU cluster configuration mein secret API keys ya database passwords commit karna security disaster hai. Hamesha Kubernetes Secrets ya HashiCorp Vault use karein.

Zero-GPU Tip:
Cluster load balancing, fault injection, least-connections scheduling, aur failover simulation 100% asynchronous Python code hai. Inhe verify karne ke liye local machine par chaos engineering test scripts chalayein with zero GPU hardware.

Self-Check Questions:
1. High-Availability 99.9% SLA mein monthly kitni downtime allowed hoti hai?
2. Least-Connections load balancing LLM workloads ke liye Round-Robin se kyun behtar hoti hai?
3. GPU pod crash hone par automatic failover zero-downtime kaise provide karta hai?

What to Build Next:
Ek Complete Production MLOps Architecture Diagram aur Deployment Blueprint tayar karein jo Kubernetes Ingress, FastAPI Gateway, vLLM GPU Nodes, Redis Cache, aur Langfuse Observability ko aapas mein jor kar 99.9% SLA deliver kare."""
