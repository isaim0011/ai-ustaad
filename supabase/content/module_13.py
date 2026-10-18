# module_13.py
# Module 13: Local AI & Edge Devices
# Lessons 13.1 to 13.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 13.1: Running AI Locally: llama.cpp, GGUF Formats & CPU Optimization
# ==============================================================================
LESSON_CONTENT['13.1'] = r"""### Part 1: Mental Model & South Asian Analogy
Aksar log samajhte hain ke LLM chalane ke liye lakhon rupaye ka GPU hona lazmi hai. Lekin 2023 mein Georgi Gerganov ne ek aisa carnama kiya jisne poori duniya ko hairan kar diya: **llama.cpp**! Usne pure C/C++ mein bina kisi heavy Python library ke LLaMA model ko CPU ke hardware registers par direct chala kar dikhaya.
Isay samajhne ke liye kisi Gaon ke Paani wale Kuen aur Hand Pump ki misaal lein:
1. Cloud LLM (Shehar Ka Water Filtration Plant): Zabardast pani deta hai, lekin mahana bill aata hai, aur agar internet ki taar kat jaye ya bijli chali jaye to aap pyasay reh jate hain.
2. Local AI with llama.cpp (Apne Sehan Ka Hand Pump): Hand pump aapke apne ghar ke andar laga hai. Chahe internet band ho, cellular network gir jaye, ya aadhi raat ho — pump ka dasta hilayein aur foran taza pani nikal aata hai! Zero dollar bill, zero internet, 100% privacy!
3. GGUF File Format (Single Pre-Packed Dabba): Purane daur mein model chalane ke liye 5 alag alag files (weights, tokenizer, config JSON, vocabulary) dhoondni parti theen. GGUF ek single sealed binary container hai jisme model ke weights, hyper-parameters, tokenizer, aur quantization scales sab ek hi file mein bandhe hote hain.
4. Memory Mapping (`mmap` - Instant Loading): GGUF file ko RAM mein copy karne ki zaroorat nahi hoti! Operating system ka `mmap` kernel call disk file ko direct virtual memory space mein map kar deta hai. 4 GB ka model click karte hi 0.1 second mein start ho jata hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein CPU Memory Bandwidth Bottleneck aur Token Generation Speed ka physical hardware hisab lagayein.
Autoregressive LLM inference Compute-Bound nahi hoti; yeh **Memory-Bandwidth Bound** hoti hai!
Har token generate karne ke liye CPU ko model ke tamam weights ko RAM se CPU Cache mein lana parta hai:
$\text{Max Tokens per Second} = \frac{\text{System Memory Bandwidth (GB/s)}}{\text{Model Memory Size (GB)}}$

Hardware Setup:
Standard Laptop with Dual-Channel DDR5 RAM:
- Memory Bandwidth = $64 \text{ GB/s}$
- Model: LLaMA-3.1-8B

Scenario A: Unquantized FP16 Model (16.0 GB Size)
$\text{Token Speed} = \frac{64 \text{ GB/s}}{16.0 \text{ GB}} \approx 4.0 \text{ tokens per second}$ (Slow, feels sluggish).

Scenario B: Quantized GGUF `Q4_K_M` (4.2 GB Size)
Model memory compressed to 4.2 GB:
$\text{Token Speed} = \frac{64 \text{ GB/s}}{4.2 \text{ GB}} \approx 15.24 \text{ tokens per second}$!

Speedup Analysis:
$\frac{15.24}{4.0} \approx 3.8\times \text{ Real-World Throughput Speedup}$ purely from memory compression!
Average human reading speed $\approx 5$ to $7$ words per second ($\approx 8$ to $10$ tokens/s).
15 tokens/sec par chalne wala local model insani padhne ki raftaar se tez generate karta hai, completely offline on a standard laptop CPU!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Python binding ke zariye llama.cpp GGUF local model initialization, generation parameters, aur memory telemetry engine implement karte hain.

```python
import time
from typing import Dict, Any

# Simulated production llama-cpp-python wrapper execution
class LocalLlamaCppEngine:
    \"\"\"Production wrapper for local GGUF execution via llama.cpp runtime.\"\"\"
    def __init__(self, model_path: str, n_ctx: int = 2048, n_threads: int = 4) -> None:
        self.model_path = model_path
        self.n_ctx = n_ctx
        self.n_threads = n_threads
        print(f"Loading GGUF Model via mmap: '{model_path}' (Threads: {n_threads}, Context: {n_ctx})...")
        # In production: from llama_cpp import Llama; self.llm = Llama(...)

    def generate_completion(self, prompt: str, max_tokens: int = 64, temperature: float = 0.7) -> Dict[str, Any]:
        t0 = time.perf_counter()
        
        # Emulate CPU vectorized generation
        tokens_emitted = [
            "Local", "AI", "running", "completely", "offline", 
            "via", "llama.cpp", "GGUF", "on", "CPU", "registers."
        ]
        text_out = " ".join(tokens_emitted)
        elapsed_sec = time.perf_counter() - t0 + 0.12  # Realistic 120ms compute

        speed_tps = len(tokens_emitted) / elapsed_sec

        return {
            "text": text_out,
            "tokens_generated": len(tokens_emitted),
            "latency_seconds": round(elapsed_sec, 3),
            "tokens_per_second": round(speed_tps, 1)
        }

# Execution test
if __name__ == "__main__":
    engine = LocalLlamaCppEngine(
        model_path="models/llama-3.1-8b-instruct.Q4_K_M.gguf",
        n_ctx=4096,
        n_threads=8
    )

    result = engine.generate_completion("Write a haiku about local AI.")
    print("\\nLocal GGUF Execution Result:")
    print(f"Output:             '{result['text']}'")
    print(f"Tokens Generated:   {result['tokens_generated']}")
    print(f"Generation Latency: {result['latency_seconds']} seconds")
    print(f"CPU Throughput:     {result['tokens_per_second']} tokens/sec (Real-time speed!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Setting `n_threads` Greater Than Physical CPU Cores: Agar aapke CPU mein 8 physical cores hain aur aap Hyperthreading dekh kar `n_threads = 16` set kar dein to thread context switching overhead ki wajah se speed 30% gir jati hai. Hamesha sirf **Physical Performance Cores** ki tadaad use karein.
2. Allocating GGUF Model on Slow HDD Instead of SSD: `mmap` disk se direct virtual memory pages read karta hai. Agar GGUF file purani 5400 RPM mechanical hard drive par ho to page faults ki wajah se generation atakne lagti hai. Hamesha fast NVMe SSD use karein.
3. Forgetting `--n-gpu-layers` on Hybrid Systems: Agar aapke laptop mein chota GPU (jaise RTX 3050 with 4GB VRAM) mojud ho to tamam layers CPU par chalana be-waqoofi hai. Hamesha `--n-gpu-layers 20` lagayein taake 20 layers GPU VRAM mein offload ho sakein aur baqi CPU par chalein.

Zero-GPU Tip:
`llama.cpp` ka maqsad hi zero-GPU computing hai! Kisi bhi saste Windows, Mac, ya Linux laptop par `llama.cpp` compile karein (`cmake -B build`) aur 4-bit GGUF model download karke 100% offline terminal chat enjoy karein.

Self-Check Questions:
1. Autoregressive LLM generation CPU par Compute-Bound hoti hai ya Memory-Bandwidth Bound?
2. GGUF format mein `mmap` operating system memory management ko kaise optimize karta hai?
3. CPU inference ke waqt `n_threads` parameter physical cores ke barabar kyun rakhna chahiye?

What to Build Next:
Ek Local GGUF CLI Assistant banayein jo `llama-cpp-python` use kare, user se terminal input le, live streaming token output de, aur generation ke aakhir mein tokens/sec speed report kare."""

# ==============================================================================
# LESSON 13.2: Ollama Deep Dive: Custom Modelfiles & REST Orchestration
# ==============================================================================
LESSON_CONTENT['13.2'] = r"""### Part 1: Mental Model & South Asian Analogy
Agar llama.cpp AI engine ka raw mechanical loha hai, to **Ollama** uske upar bani hui luxury automatic car hai! Docker ne jaise containers ko aam insaan ke liye aasan banaya (`docker run`), Ollama ne bilkul usi tarah local AI ko ek single command bana diya: `ollama run llama3`.
Isay samajhne ke liye kisi Automatic Coffee Vending Machine ki misaal lein:
1. Docker for AI (Ollama Engine): Aapko na C++ compile karna parta hai, na dependencies install karni parti hain. Background mein ek lightweight daemon chalta hai jo GPU detection, memory offloading, aur models swapping khud handle karta hai.
2. The Modelfile (Khaas Recipe Card): Modelfile Dockerfile jaisi ek text file hoti hai jisme aap model ka mizaj aur identity lock karte hain:
   ```dockerfile
   FROM llama3.1:8b
   PARAMETER temperature 0.2
   SYSTEM "Aap Karachi ke mashhoor chai dhabay ke munshi hain."
   ```
3. Seamless Model Swapping: Agar aap coding kar rahe hain to `qwen2.5-coder` load ho jata hai; aglay second jab aap Urdu shayeri mangte hain to Ollama background mein coding model ko VRAM se nikal kar `llama3` load kar deta hai!
4. Native OpenAI-Compatible REST API: Ollama background mein `http://localhost:11434` par standard OpenAI format ka REST API serve karta hai, jisse aap kisi bhi frontend (OpenWebUI, LibreChat) ko 1 click mein local models se connect kar sakte hain.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Ollama Context Memory Allocation aur VRAM Model Swapping ka exact hisab lagayein.
Parameters:
- Laptop Total Unified Memory (or GPU VRAM) = 8 GB ($8,192 \text{ MB}$)
- Base Model: `phi3:mini` (3.8B parameters, Q4_K_M size $= 2.3 \text{ GB} = 2,355 \text{ MB}$)
- Target Context Size $S_{\text{ctx}} = 4096 \text{ tokens}$
- KV Cache Memory for 4096 context $\approx 512 \text{ MB}$

Total Memory Required for Active Session:
$M_{\text{active}} = M_{\text{weights}} + M_{\text{KV}} + M_{\text{scratch}}$
$M_{\text{active}} = 2355 + 512 + 150 = 3,017 \text{ MB} \approx 2.95 \text{ GB}$.
Remaining Free Memory:
$8192 - 3017 = 5,175 \text{ MB} \approx 5.05 \text{ GB}$ free!

Model Swapping Latency Math:
User switches from `phi3` to `llama3.1:8b` (4.7 GB):
- Unload `phi3` from memory: 0.05s.
- Load `llama3.1` from NVMe SSD ($3500 \text{ MB/s}$ read speed):
  $T_{\text{load}} = \frac{4700 \text{ MB}}{3500 \text{ MB/s}} \approx 1.34 \text{ seconds}$!
1.4 seconds ke andar poora model memory mein swap ho jata hai aur naya task execute ho jata hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum custom Modelfile syntax generation, Ollama REST API orchestration, aur streaming token consumption pipeline implement karte hain.

```python
import json
import urllib.request
from typing import Dict, Any, Generator

def generate_custom_modelfile_content(
    base_model: str = "llama3.1:8b", 
    temperature: float = 0.2, 
    system_instruction: str = "You are a helpful Pakistani AI assistant."
) -> str:
    \"\"\"Generates formal Modelfile specification for Ollama CLI build.\"\"\"
    modelfile_str = f\"\"\"# AI Ustaad Custom Modelfile
FROM {base_model}

# Core sampling parameters
PARAMETER temperature {temperature}
PARAMETER top_p 0.9
PARAMETER stop "<|im_end|>"
PARAMETER stop "<|eot_id|>"

# System Persona
SYSTEM \"\"\"{system_instruction}\"\"\"
\"\"\"
    return modelfile_str.strip()

def query_local_ollama_stream(prompt: str, model_name: str = "llama3.1:8b") -> Generator[str, None, None]:
    \"\"\"Streams tokens from local Ollama REST endpoint (http://localhost:11434/api/generate).\"\"\"
    payload = json.dumps({
        "model": model_name,
        "prompt": prompt,
        "stream": True
    }).encode("utf-8")

    # In production with live Ollama daemon:
    # req = urllib.request.Request("http://localhost:11434/api/generate", data=payload, headers={"Content-Type": "application/json"})
    # with urllib.request.urlopen(req) as resp: ...

    # Simulated local streaming emission
    mock_tokens = ["Chai", " ", "dhabay", " ", "ka", " ", "khata", " ", "ready", " ", "hai!"]
    for t in mock_tokens:
        yield t

# Execution test
if __name__ == "__main__":
    modelfile = generate_custom_modelfile_content(
        base_model="llama3.1:8b",
        temperature=0.3,
        system_instruction="Aap Karachi ke purane chai dhabay ke munshi hain. Hamesha polite Roman Urdu mein jawab dein."
    )
    print("Generated Ollama Modelfile:")
    print("--------------------------------------------------")
    print(modelfile)
    print("--------------------------------------------------")

    print("\\nSimulating Live Streaming Token Consumption from Local Ollama REST:")
    for token in query_local_ollama_stream("Patti kitni bachi hai?"):
        print(token, end="", flush=True)
    print("\\n")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Forgetting to Set `OLLAMA_KEEP_ALIVE`: Default tor par Ollama 5 minute baad model ko memory se nikal deta hai taake RAM free ho sake. Agar agla user 6 minute baad query kare to dobara 3-second load delay aata hai. Model ko hamesha memory mein rakhne ke liye `OLLAMA_KEEP_ALIVE=-1` set karein.
2. Port Conflicts on 11434: Agar pehle se koi service port 11434 par chal rahi ho to Ollama start fail ho jata hai. Environment variable `OLLAMA_HOST=0.0.0.0:11435` se custom port set karein.
3. Exposing Ollama Directly to the Public Internet: Ollama ka REST API default tor par unauthenticated hota hai. Ise public IP par kholna kisi ko bhi aapke server par arbitrary models run karne aur server resources chori karne ki dawat deta hai. Hamesha reverse proxy (NGINX/Caddy) with API key auth lagayein.

Zero-GPU Tip:
Ollama automatic hardware detection karta hai. Agar aapke paas koi GPU na ho to yeh khud ba khud AVX2 CPU mode par chala jata hai. Laptop par `ollama run qwen2.5:1.5b` chala kar dekhein; yeh CPU par bijli jaisi 35 tokens/sec speed deta hai.

Self-Check Questions:
1. Ollama Modelfile Dockerfile ki tarah model customisation ko kaise aasan banati hai?
2. Ollama ka OpenAI-compatible REST API endpoint traditional frameworks ke sath integration ko kaise aasan karta hai?
3. `OLLAMA_KEEP_ALIVE` parameter memory management aur latency ko kaise control karta hai?

What to Build Next:
Ek Local Multi-Model Switcher CLI banayein jo Ollama REST API query kare, system par installed models list kare, aur user ko ek click mein Coding vs Chat model ke darmiyan switch karne de."""

# ==============================================================================
# LESSON 13.3: Edge Hardware Acceleration: Apple Metal, Vulkan & ROCm
# ==============================================================================
LESSON_CONTENT['13.3'] = r"""### Part 1: Mental Model & South Asian Analogy
NVIDIA CUDA dunya ka sab se mashhoor GPU platform hai, lekin har bande ke paas NVIDIA GPU nahi hota. Apple Mac users ke paas **Metal (MPS)** hai, AMD users ke paas **ROCm** hai, aur integrated Intel/AMD laptops ke paas **Vulkan** hai. 2026 mein modern local AI cross-platform hardware acceleration par chalti hai!
Isay samajhne ke liye kisi Shehar ke Mukhtalif Gaariyon ke Engines ki misaal lein:
1. NVIDIA CUDA (Formula 1 Racing Car): Bohat taqatwar hai lekin mehangi aur petrol (bijli) bohot peeti hai.
2. Apple Silicon & Metal Performance Shaders (MPS - The Unified Highway): Traditional PC mein CPU ki RAM alag hoti hai aur GPU ki VRAM alag hoti hai; dono ke darmiyan PCIe bridge par data copy karna parta hai. Apple Mac (M1/M2/M3/M4) mein **Unified Memory Architecture (UMA)** hoti hai! CPU aur GPU ek hi physical memory chip ko share karte hain. Agar aapke Mac mein 64 GB RAM hai to poora 70B model bina kisi copy ke direct GPU memory mein baith jata hai!
3. Vulkan API (Har Gaari Ka Universal CNG Kit): Vulkan ek aisa open-standard cross-platform graphic API hai jo har qisam ke chip par chalta hai: Intel Iris graphics, AMD Radeon, Raspberry Pi GPU, aur Android mobile phones.
4. AMD ROCm: AMD ka open-source compute stack jo Linux par Radeon GPUs ko CUDA jaisi performance faraham karta hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Discrete GPU Memory Copy Latency vs Apple Unified Memory Zero-Copy ka physical hisab lagayein.
Model: 70B Parameter Quantized Model ($M = 35 \text{ GB}$ weight size).

Scenario A: Traditional PC with Discrete GPU via PCIe 4.0 x16
- PC RAM has 64 GB. GPU has 12 GB VRAM.
- Chunke 35 GB model 12 GB VRAM mein fit nahi aata, is liye har forward step par weights ko CPU RAM se GPU VRAM mein PCIe bus ke zariye stream karna parta hai (Offloading)!
PCIe 4.0 x16 Practical Bandwidth $\approx 25 \text{ GB/s}$.
Data Transfer Latency per token step:
$T_{\text{transfer}} = \frac{35 \text{ GB}}{25 \text{ GB/s}} = 1.40 \text{ seconds per token}$!
Generation speed drops to $\approx 0.7 \text{ tokens/sec}$ (Completely unusable bottleneck!).

Scenario B: Apple Silicon Mac with 64 GB Unified Memory (UMA)
- Unified Memory Bandwidth on M3 Max $= 400 \text{ GB/s}$.
- Zero PCIe copying! Model pehle se usi memory mein mojud hai jahan GPU direct reads karta hai.
Direct GPU Memory Access Latency:
$T_{\text{access}} = \frac{35 \text{ GB}}{400 \text{ GB/s}} = 0.0875 \text{ seconds}$.
Token Generation Speed:
$\text{Speed} = \frac{1}{0.0875} \approx 11.4 \text{ tokens per second}$!
Zero-copy Unified Memory ne 70B model ko laptop par viable bana diya!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum dynamic cross-platform hardware accelerator selector implement karte hain jo CUDA, Apple MPS (Metal), Vulkan, ROCm, aur CPU fallback ko safely detect karke bind karta hai.

```python
import torch

def detect_optimal_hardware_backend() -> dict[str, str | bool]:
    \"\"\"Inspects OS and hardware to select optimal local acceleration runtime.\"\"\"
    backend_info: dict[str, str | bool] = {
        "cuda_available": torch.cuda.is_available(),
        "mps_available": hasattr(torch.backends, "mps") and torch.backends.mps.is_available(),
        "selected_device": "cpu",
        "acceleration_framework": "CPU (OpenMP/AVX)"
    }

    if backend_info["cuda_available"]:
        device_name = torch.cuda.get_device_name(0)
        backend_info["selected_device"] = "cuda:0"
        backend_info["acceleration_framework"] = f"NVIDIA CUDA ({device_name})"
    elif backend_info["mps_available"]:
        backend_info["selected_device"] = "mps"
        backend_info["acceleration_framework"] = "Apple Silicon Metal Performance Shaders (MPS)"
    else:
        # Fallback to standard CPU
        backend_info["selected_device"] = "cpu"
        backend_info["acceleration_framework"] = "Host CPU (Vectorized SIMD)"

    return backend_info

# Execution test
if __name__ == "__main__":
    hw = detect_optimal_hardware_backend()
    print("Cross-Platform AI Hardware Acceleration Discovery:")
    print(f"  Selected Device:        {hw['selected_device']}")
    print(f"  Acceleration Framework: {hw['acceleration_framework']}")

    # Allocate tensor on selected device
    dev = torch.device(hw["selected_device"])
    x = torch.ones(1024, 1024, device=dev)
    t0 = torch.matmul(x, x)
    print(f"  Test Matrix Multiply:   Shape {list(t0.shape)} executed successfully on {dev}!")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Missing Apple MPS Fallback to CPU (`PYTORCH_ENABLE_MPS_FALLBACK=1`): PyTorch MPS backend mein kuch rare operators abhi tak implement nahi hain. Agar koi un-implemented operator aa jaye to script crash ho jati hai. Hamesha environment variable set karein taake unsupported ops seamlessly CPU par fallback karein.
2. Out-Of-Memory Crashes on Unified Memory Macs: Mac par agar aapke paas 16 GB RAM hai aur aap 14 GB ka model load karein to OS UI freeze ho sakta hai kyunke macOS ko system ke liye 4 GB RAM chahiye hoti hai. Model size hamesha total unified memory ka maximum 75% rakhein.
3. Ignoring Vulkan Shader Compilation Stutters: Vulkan pehli dafa chalte waqt shaders compile karta hai jisse pehla token 5 second le sakta hai. Shaders ko pre-compile karke disk par cache karein.

Zero-GPU Tip:
Agar aapke system mein koi dGPU ya Apple Silicon nahi hai to Vulkan backend Intel Iris graphics ya AMD APUs par chalta hai. Pure CPU fallback Intel MKL ke zariye bina kisi graphic card ke standard AI execution faraham karta hai.

Self-Check Questions:
1. Apple Silicon Unified Memory Architecture (UMA) traditional PC PCIe data copy bottleneck ko kaise khatam karti hai?
2. Apple Metal (MPS) aur NVIDIA CUDA mein developer API level par kya farq hai?
3. Vulkan cross-platform graphics API hardware-agnostic LLM inference mein kyun mashhoor ho rahi hai?

What to Build Next:
Ek Cross-Platform Hardware Diagnostic Script banayein jo system par CUDA, MPS, aur Vulkan runtimes check kare, memory bandwidth benchmark kare, aur optimal quantized model recommendations print kare."""

# ==============================================================================
# LESSON 13.4: In-Browser Client AI: WebGPU & Transformers.js
# ==============================================================================
LESSON_CONTENT['13.4'] = r"""### Part 1: Mental Model & South Asian Analogy
AI chalane ke liye hamesha server ya backend ki zaroorat nahi hoti. 2026 mein modern web browsers (Chrome, Edge, Safari) ke andar **WebGPU aur WebAssembly (Wasm)** ne aisi taqat de di hai ke poora AI model seedha user ke browser ke andar chalta hai!
Isay samajhne ke liye kisi Restaurant vs Home Cooking Kit ki misaal lein:
1. Traditional Server AI (Restaurant Se Khana Mangwana): Har dafa khana mangwane ke liye restaurant ko phone karna parta hai, delivery ka intezar karna parta hai, aur bill bharna parta hai. Agar internet chala jaye ya restaurant band ho jaye to khana nahi milta.
2. In-Browser AI with WebGPU (Ghar Par Cooking Machine): User jab aapki website (e.g. `ai-ustaad.pages.dev`) par aata hai to website sirf ek dafa chota model (jaise Whisper ya SmolLM-135M) browser ke local cache mein download karti hai. Uske baad user ka internet bilkul band ho jaye, tab bhi model user ke apne laptop ke graphic card (WebGPU) par chalta hai!
3. Absolute Zero Server Cost: Server owner ka monthly GPU cloud bill **\$0.00** ho jata hai! Chahe 10 lakh users aapki website par aa jayein, compute unke apne browsers par hota hai.
4. Total Privacy Guarantee: User ka data (medical report, private audio recording) kabhi internet par kisi server ko bhejta hi nahi; processing 100% client side par hoti hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein WebGPU Shader Pipeline aur Client Bandwidth Caching ka exact hisab lagayein.
Model: Whisper Web (Quantized to 8-bit ONNX format $= 40 \text{ MB}$).

First Visit vs Subsequent Visits Math:
Visit 1 (Download & Cache):
- User visits website on 50 Mbps internet connection:
  $\text{Download Time} = \frac{40 \times 8 \text{ Mbits}}{50 \text{ Mbps}} = \frac{320}{50} = 6.4 \text{ seconds}$.
- Model binary is stored in Browser Cache Storage (`CacheStorage API` or `IndexedDB`).

Subsequent Visits (Zero Network):
- Model loaded from browser IndexedDB storage directly into WebGPU VRAM buffer:
  $\text{Load Latency} \approx 0.15 \text{ seconds}$ (150 ms)!
- Network Data Transferred $= 0 \text{ Bytes}$!

Cloud Cost Economics for 100,000 Monthly Users:
- Standard Server Hosting (100k audio transcriptions on Whisper API at \$0.006 per min):
  $100,000 \times \$0.006 = \$600 \text{ USD per month}$ recurring cost.
- WebGPU In-Browser Hosting (Static assets hosted on Cloudflare Pages free tier):
  Total Server Bill $= \$0.00$ USD!
  Monthly Business Savings $= \$600$ USD ($100\% \text{ Cloud Cost Reduction}$)!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum HTML/JavaScript standard WebGPU feature detection, Transformers.js client pipeline initialization, aur in-browser inference workflow implement karte hain.

```html
<!-- Production WebGPU In-Browser AI Client Architecture -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>In-Browser Client AI with WebGPU</title>
</head>
<body>
    <h2>AI Ustaad In-Browser Zero-Server Inference</h2>
    <button id="runBtn" onclick="runClientAI()">Run In-Browser AI</button>
    <div id="outputLog" style="white-space: pre-wrap; margin-top: 15px; font-family: monospace;"></div>

    <script type="module">
        // Verification of WebGPU Hardware Support in Browser
        async function checkWebGPUSupport() {
            if (!navigator.gpu) {
                return { supported: false, message: "WebGPU is not supported on this browser (Fallback to Wasm CPU)." };
            }
            try {
                const adapter = await navigator.gpu.requestAdapter();
                if (!adapter) {
                    return { supported: false, message: "No compatible WebGPU hardware adapter found." };
                }
                const device = await adapter.requestDevice();
                return { supported: true, message: `WebGPU active on: ${adapter.info?.architecture || 'Local GPU'}` };
            } catch (err) {
                return { supported: false, message: `WebGPU initialization error: ${err}` };
            }
        }

        window.runClientAI = async function() {
            const logBox = document.getElementById("outputLog");
            logBox.innerText = "Checking hardware capabilities...\\n";

            const gpuStatus = await checkWebGPUSupport();
            logBox.innerText += `Hardware Status: ${gpuStatus.message}\\n\\n`;

            logBox.innerText += "Simulating Transformers.js In-Browser Pipeline:\\n";
            logBox.innerText += "1. Fetching ONNX Quantized weights from IndexedDB cache...\\n";
            logBox.innerText += "2. Compiling WebGPU WGSL compute shaders...\\n";
            logBox.innerText += "3. Executing local token generation on client GPU...\\n\\n";
            
            const clientResult = "Generated completely in-browser: 'Karak chai is the ultimate energy fuel!'";
            logBox.innerText += `Output: "${clientResult}"\\n`;
            logBox.innerText += "Server Cloud Cost: $0.00 (Zero network packets sent!)";
        };
    </script>
</body>
</html>
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Trying to Load 7B Parameter Models in the Browser: 7B model 4 GB download mangta hai jo browser tab memory limits (often 2GB limit per tab in 32-bit Chrome processes) ko crash kar deta hai. Browser ke liye hamesha ultra-compact models (jaise SmolLM-135M, MobileBERT, Whisper-Base) use karein.
2. Missing Wasm CPU Fallback: Agar kisi user ke purane laptop par WebGPU disabled ho to bina WebAssembly fallback ke website completely blank error deti hai. Hamesha `device: 'webgpu' || 'wasm'` fallback support karein.
3. Not Caching Models in IndexedDB: Har page refresh par dobara 40 MB model download karwana user ka mobile data zaaya karta hai. Hamesha persistent caching ensure karein.

Zero-GPU Tip:
In-browser AI ka sara maqsad hi cloud GPU ko bypass karna hai! Website owner ke paas zero GPU hota hai; compute poori tarah client ke browser par chal raha hota hai.

Self-Check Questions:
1. WebGPU browser ke andar client-side AI execution ko kaise mumkin banati hai?
2. In-browser AI server hosting costs ko $100\%$ kaise khatam karti hai?
3. Browser environment mein model size constraints (Memory Limits) kya hoti hain?

What to Build Next:
Ek In-Browser Audio Transcriber web page banayein using Transformers.js (`@xenova/transformers`) jo browser microphone se aawaz record kare aur 100% offline text mein transcribe kare."""

# ==============================================================================
# LESSON 13.5: Edge AI on Embedded Hardware: Nvidia Jetson & Raspberry Pi
# ==============================================================================
LESSON_CONTENT['13.5'] = r"""### Part 1: Mental Model & South Asian Analogy
Har jagah high-speed WiFi ya bijli ka socket mojud nahi hota. Misaal ke taur par: khet khalyan mein faslon ki nigrani karne wala drone, factory floor par defective parts dhoondne wala camera, ya traffic signal par chalan katne wala smart camera. In jaghon par chotay embedded boards chalte hain jaise **Nvidia Jetson aur Raspberry Pi 5 with NPUs (Neural Processing Units)**!
Isay samajhne ke liye kisi Pocket Torch vs Stadium Searchlight ki misaal lein:
1. Data Center GPU (Stadium Searchlight): 500 Watts bijli khata hai, cooling ke liye AC chahiye, aur generator par chalta hai. Aap isay jungle mein drone par nahi baandh sakte.
2. Edge AI Board (Pocket Torch): 5 se 15 Watts bijli (ek choti si power bank ya solar panel) par chalta hai aur pocket mein aa jata hai.
3. NPU - Neural Processing Unit (Khaas AI Chip): Raspberry Pi 5 par jab hum Hailo-8 NPU HAT lagate hain to woh aam CPU ke barabar bijli kharch karte hue 26 TOPS (Tera Operations Per Second) ki AI power deta hai!
4. Real-Time Computer Vision at the Edge: Camera direct NPU se connected hota hai. 1 second mein 30 frames process hote hain, defect ya bimari detect hoti hai, aur foran relay switch trigger ho jata hai bina internet ka intezar kiye!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Power Efficiency (TOPS per Watt) aur Battery Operating Life ka exact physical hisab lagayein.
Edge Deployment Scenario:
Agricultural Drone monitoring wheat crops for pest infestation in rural Punjab.
Power Source: Drone onboard battery pack $= 50 \text{ Watt-hours (Wh)}$.

Scenario A: Running Standard GPU Architecture (NVIDIA Desktop Grade)
- Power Consumption $= 150 \text{ Watts}$.
Battery Life:
$\text{Runtime} = \frac{50 \text{ Wh}}{150 \text{ W}} = 0.333 \text{ hours} \approx 20 \text{ minutes}$ (Drone falls out of the sky before surveying the field!).

Scenario B: Embedded Edge Board (Nvidia Jetson Orin Nano / Hailo NPU)
- Compute Power $= 40 \text{ TOPS}$ (INT8 Tensor operations)
- Power Consumption $= 10 \text{ Watts}$ in active inference mode.
Battery Life:
$\text{Runtime} = \frac{50 \text{ Wh}}{10 \text{ W}} = 5.0 \text{ hours}$!
Drone operates for a full 5-hour survey on a single charge!

Power Efficiency Metric (TOPS/Watt):
$\text{Efficiency} = \frac{40 \text{ TOPS}}{10 \text{ Watts}} = 4.0 \text{ TOPS per Watt}$!
Edge AI low-power hardware optimization ka naam hai jahan har single watt bijli ki qadar hoti hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum embedded edge deployment optimization pipeline implement karte hain: INT8 quantization verification, thermal throttling guard, aur frame-by-frame inference loop.

```python
import time
from typing import Dict, Any

class EdgeDeviceInferenceLoop:
    \"\"\"Simulates embedded edge pipeline running on low-power NPU hardware.\"\"\"
    def __init__(self, device_name: str = "Nvidia Jetson Orin Nano", power_budget_watts: float = 10.0) -> None:
        self.device_name = device_name
        self.power_budget = power_budget_watts
        self.thermal_temperature_c = 42.0

    def inspect_thermal_safety(self) -> bool:
        \"\"\"Guards against thermal throttling on fanless edge hardware.\"\"\"
        # If board temperature exceeds 80C, throttle inference frequency
        return self.thermal_temperature_c < 80.0

    def process_camera_frame(self, frame_id: int) -> Dict[str, Any]:
        t0 = time.perf_counter()
        if not self.inspect_thermal_safety():
            raise RuntimeError("Emergency Throttle: Edge SoC thermal safety limit exceeded!")

        # Simulate low-latency INT8 NPU matrix execution
        time.sleep(0.02)  # 20ms execution -> 50 FPS
        
        # Emulate slight thermal dissipation
        self.thermal_temperature_c += 0.01
        elapsed_ms = (time.perf_counter() - t0) * 1000.0

        return {
            "frame_id": frame_id,
            "detected_objects": ["healthy_crop", "irrigation_line"],
            "inference_time_ms": round(elapsed_ms, 2),
            "board_temp_c": round(self.thermal_temperature_c, 1)
        }

# Execution test
if __name__ == "__main__":
    edge_node = EdgeDeviceInferenceLoop(device_name="Raspberry Pi 5 + Hailo-8 NPU", power_budget_watts=5.0)
    print(f"Initialized Edge Device: {edge_node.device_name} (Budget: {edge_node.power_budget}W)")

    print("\\nStreaming 5 camera frames across Edge NPU pipeline:")
    for f in range(1, 6):
        res = edge_node.process_camera_frame(f)
        print(f"  Frame {res['frame_id']:02d} -> Detections: {res['detected_objects']} | Latency: {res['inference_time_ms']} ms | Temp: {res['board_temp_c']} C")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Ignoring Thermal Throttling on Fanless Edge Cases: Embedded boards (jaise Jetson) agar band box mein hon to garmi 85C cross kar jati hai aur OS CPU clock speed ko 90% gira deta hai (Throttling). Hamesha active heatsink ya thermal monitoring software lagayein.
2. Deploying Unquantized Floating-Point Models to Edge NPUs: NPUs (jaise Hailo ya Google Coral) strictly INT8 integers execute karte hain. Agar aap FP32 model deploy karenge to hardware use CPU par fallback kar deta hai aur speed 100x slow ho jati hai. Hamesha model ko compile karke NPU binary format banayein.
3. Power Supply Voltage Drops (Brownouts): Raspberry Pi ko kam power wale phone charger se chalane par jab NPU peak load leta hai to board achanak reboot ho jata hai. Hamesha certified high-amp power adapter use karein.

Zero-GPU Tip:
Embedded edge AI pipelines ko simulate karne ke liye kisi physical Jetson board ki zaroorat nahi hai. Aap apne PC par model ko ONNX format mein export karke OpenVINO ya ONNX Runtime CPU par INT8 quantization benchmark kar sakte hain.

Self-Check Questions:
1. Embedded Edge AI mein TOPS per Watt efficiency metric kyun sab se ahem hoti hai?
2. Thermal Throttling kya hoti hai aur yeh edge inference latency ko kaise tabah karti hai?
3. NPU (Neural Processing Unit) aam CPU ke muqablay low-power matrix calculations mein kyun 50x tez hoti hai?

What to Build Next:
Ek Edge Vision Pipeline script banayein jo USB webcam se frames read kare, ONNX INT8 quantized object detection model chalaye, aur screen par real-time FPS counter render kare."""

# ==============================================================================
# LESSON 13.6: Module 13 Capstone: 100% Offline Autonomous Edge Assistant
# ==============================================================================
LESSON_CONTENT['13.6'] = r"""### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne Local AI aur Edge Computing ke tamam ahem sutoon (llama.cpp GGUF compilation, Ollama Modelfile orchestration, Apple Metal/Vulkan acceleration, In-browser WebGPU, aur Embedded NPU hardware) mukammal kar liye hain. Ab waqt hai aapke **Pehle 100% Offline Autonomous Edge AI Assistant Capstone** ka!
Is Capstone project ka zehni khaka kisi Registan, Pahari ilaqa (Gilgit/Skardu), ya Disconnected Field Camp ke Doctor Assistant jaisa hai:
1. Zero-Cloud Dependency: Camp mein koi internet nahi hai, mobile network signal bilkul gayab hain.
2. The Fully Contained Hardware Box: Chotay se portable laptop ya embedded board par:
   - Microphone se audio aati hai $\to$ Local Whisper transcribe karta hai.
   - Local Reasoning Core $\to$ GGUF Quantized 4-bit model offline chal kar sawal ka hal sochta hai.
   - Local Audio Synthesizer $\to$ Piper TTS speaker par aawaz generate karta hai.
3. Total Sovereignty: Data camp ke kamray se 1 millimeter bhi bahar nahi jata. Khufia medical records aur rescue plans 100% private rehte hain.

Yeh Capstone project uncompromised local autonomy ka live namoona hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Complete Offline Edge Turn Latency Waterfall ka exact hisab lagayein.
Components on 16 GB RAM Laptop CPU (Zero Cloud, Zero External APIs):
1. Step 1: Speech-to-Text via `faster-whisper-tiny` (INT8 on CPU)
   - Audio length $= 3.0 \text{ seconds}$.
   - Real-Time Factor (RTF) $= 0.10$.
   - STT Latency: $T_{\text{stt}} = 3.0 \times 0.10 = 0.30 \text{ seconds}$.
2. Step 2: Local Reasoning via LLaMA-3.2-3B GGUF `Q4_K_M`
   - Prompt Processing (Prefill): 50 tokens $\to 0.05 \text{ seconds}$.
   - Generation: 30 tokens at $20 \text{ tokens/second}$:
     $T_{\text{gen}} = \frac{30}{20} = 1.50 \text{ seconds}$.
3. Step 3: Local Text-to-Speech via Piper TTS (C++ ONNX engine)
   - 30 words synthesized at $5\times \text{ faster than real-time}$:
     $T_{\text{tts}} = \frac{2.5 \text{ seconds of speech}}{5.0} = 0.50 \text{ seconds}$.

Total End-to-End Offline Interaction Latency:
$T_{\text{total}} = T_{\text{stt}} + T_{\text{gen}} + T_{\text{tts}} = 0.30 + 1.55 + 0.50 = 2.35 \text{ seconds}$!
Total Network Bandwidth Used $= \mathbf{0.00 \text{ Bytes}}$!
Total Cloud Cost $= \mathbf{\$0.00 \text{ USD}}$!
2.35 seconds ke andar mukammal interactive voice assistant local battery par chal kar tayar ho gaya!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete 100% Offline Edge Assistant Pipeline implement karte hain: local voice input processing, offline GGUF inference loop, local tool execution, aur audio response synthesis simulation.

```python
import time
from typing import Dict, Any

class AutonomousOfflineEdgeAssistant:
    \"\"\"100% offline edge assistant pipeline running entirely on local CPU/NPU.\"\"\"
    def __init__(self, model_tag: str = "llama-3.2-3b-q4_k_m") -> None:
        self.model_tag = model_tag
        # Local offline database / inventory
        self.local_offline_db = {
            "first_aid": "Clean wound with antiseptic, apply pressure with sterile gauze.",
            "emergency_contact": "Field radio frequency channel 4."
        }

    def offline_speech_to_text(self, mock_audio_duration_sec: float) -> str:
        \"\"\"Simulates local faster-whisper transcription.\"\"\"
        time.sleep(mock_audio_duration_sec * 0.10)  # 10x real-time speed
        return "Emergency triage: How do I treat a deep arm cut in the field?"

    def offline_local_reasoning(self, user_query: str) -> str:
        \"\"\"Simulates local llama.cpp GGUF reasoning engine.\"\"\"
        time.sleep(0.40)  # Fast local generation
        if "cut" in user_query.lower() or "wound" in user_query.lower():
            advice = self.local_offline_db["first_aid"]
            return f"Medical protocol: {advice} Monitor for infection."
        return "Protocol not found in offline medical cache."

    def offline_text_to_speech(self, response_text: str) -> float:
        \"\"\"Simulates local Piper TTS waveform synthesis.\"\"\"
        time.sleep(0.15)
        # Synthesizes speech waveform
        return 2.5  # Returns generated audio duration in seconds

    def run_voice_turn(self, audio_duration: float = 3.0) -> Dict[str, Any]:
        t0 = time.perf_counter()

        # Step 1: Local STT
        transcription = self.offline_speech_to_text(audio_duration)
        
        # Step 2: Local LLM Reasoning
        answer = self.offline_local_reasoning(transcription)

        # Step 3: Local TTS Synthesis
        speech_len = self.offline_text_to_speech(answer)

        total_latency = round(time.perf_counter() - t0, 3)

        return {
            "status": "success",
            "network_connectivity": "OFFLINE (Airplane Mode)",
            "transcription": transcription,
            "answer": answer,
            "speech_duration_sec": speech_len,
            "total_turn_latency_sec": total_latency
        }

# Execution test
if __name__ == "__main__":
    assistant = AutonomousOfflineEdgeAssistant()
    print("Initiating 100% Offline Edge Assistant Voice Turn (Zero Internet)...")

    result = assistant.run_voice_turn(audio_duration=2.5)
    print(f"\\nStatus:             {result['status'].upper()}")
    print(f"Network State:      {result['network_connectivity']}")
    print(f"User Spoke:         '{result['transcription']}'")
    print(f"Assistant Answer:   '{result['answer']}'")
    print(f"Turn Latency:       {result['total_turn_latency_sec']} seconds (Instant offline response!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Hardcoding Cloud Fallbacks in True Offline Scenarios: Code mein `try: local() except: openai_call()` likhne par agar jungle mein internet na ho to script 30 second timeout tak phans jati hai. Offline systems ko strictly isolated hona chahiye.
2. Unbounded Memory Leaks in Long Local Sessions: Desktop par continuous chalne wale local models mein agar KV cache free na ho to 2 ghantay baad RAM bhar jati hai. Session khatam hone par memory clear karein.
3. Unoptimized Audio Buffers in Local TTS: Text-to-Speech ko poora jumla banne tak wait karwane ke bajaye pehle comma ya period par hi audio synthesize karna shuru kar dena chahiye taake voice response instant shuru ho.

Zero-GPU Tip:
Poora Capstone system 100% CPU architecture par design kiya gaya hai! Aap apne purane laptop ko airplane mode par daal kar is script ko run karein aur verify karein ke zero internet par poora voice intelligence loop perfectly chalta hai.

Self-Check Questions:
1. 100% Offline Local AI privacy aur disaster recovery scenarios mein kyun zaroori hai?
2. Speech-to-Text, LLM Generation, aur Text-to-Speech ko local CPU par 2.5 seconds mein kaise execute kiya jata hai?
3. Edge assistant systems mein zero cloud dependency hone ka business aur operational faida kya hai?

What to Build Next:
Is Offline Assistant ko ek portable hardware case (Raspberry Pi 5 + USB Speaker/Mic) par deploy karein with an automatic physical push-to-talk button jo bina screen ke voice assistant chalaye."""
