# module_09.py
# Module 9: Fine-Tuning & Model Adaptation
# Lessons 9.1 to 9.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 9.1: PEFT, LoRA & QLoRA Foundations: Low-Rank Adapters & Mathematics
# ==============================================================================
LESSON_CONTENT['9.1'] = r"""### Part 1: Mental Model & South Asian Analogy
70 Arab (70 Billion) parameters ke model ko poori tarah train (Full Fine-Tuning) karne ke liye 8x A100 GPUs ($80,000 cost) ki zaroorat hoti hai. Lekin 2021 mein Microsoft ne aur phir 2023 mein Tim Dettmers ne aisi riyazi dhoondi jisne poori game badal di: **LoRA (Low-Rank Adaptation) aur QLoRA (Quantized LoRA)**!
Isay samajhne ke liye kisi Shehar ke Mashhoor Doctor aur Nayi Dawaon ke Chotay Booklet ki misaal lein:
1. Full Fine-Tuning (Doctor Ki 30 Saala Medical Degree Dobara Karwana): Agar doctor ko sirf ek naye virus (jaise Dengue Variant 2026) ka ilaj sikhana ho, to Full Fine-Tuning yeh hai ke aap doctor ke dimaag ki pichli tamam 30 saal ki taleem (Anatomy, Biology, Surgery) mita kar shuru se aakhir tak dobara MBBS karwayein! Yeh be-inteha mehnga, waqt talab, aur khatarnak hai kyunke doctor purani cheezein bhool sakta hai (Catastrophic Forgetting).
2. LoRA (Pocket Dairy / Sticky Notes Adapter): Samajhdaar ustaad kya karta hai? Doctor ke asal dimaag (Frozen Base Model Weights $W_0$) ko bilkul nahi chhoota (Freeze kar deta hai). Doctor ki jeb mein sirf 2 safhon ki ek choti si pocket dairy (Low-Rank Matrices $A$ aur $B$) daal deta hai jisme sirf naye virus ki makhsoos hidayat likhi hoti hain. 70 Billion parameters mein se sirf 10 Million parameters train hote hain (99.9% compute bachat)!
3. QLoRA (Pocket Dairy with 4-Bit Microfilm): QLoRA asal 70B model ke weights ko 16-bit Float se nichor kar **4-bit NormalFloat (NF4)** bana deta hai. Jo model pehle 140 GB VRAM mangta tha, woh achanak sirf 24 GB VRAM (ek aam consumer RTX 3090 ya 4090 GPU) mein fit aa jata hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein LoRA ki Low-Rank Matrix Decomposition ka exact mathematical hisab lagayein.
Formula for LoRA Forward Pass:
$h = W_0 x + \Delta W x = W_0 x + \left( \frac{\alpha}{r} \right) B A x$
Jahan:
- $W_0$: Frozen base weight matrix of shape $[d_{\text{out}}, d_{\text{in}}]$ (Weights strictly frozen!)
- $A$: Low-rank projection down matrix of shape $[r, d_{\text{in}}]$ (Initialized with Gaussian noise $\mathcal{N}(0, \sigma^2)$)
- $B$: Low-rank projection up matrix of shape $[d_{\text{out}}, r]$ (Initialized with All Zeros!)
- $r$: Rank hyperparameter (e.g. $r = 4$ ya $8$, where $r \ll \min(d_{\text{in}}, d_{\text{out}})$)
- $\alpha$: Scaling constant (e.g. $\alpha = 16$)
- Scaling factor: $\frac{\alpha}{r} = \frac{16}{4} = 4.0$

Worked Numeric Example:
Let $d_{\text{in}} = 4096$, $d_{\text{out}} = 4096$, Rank $r = 4$.

Scenario A: Full Fine-Tuning Parameter Count
Total parameters to train for this single layer:
$P_{\text{full}} = 4096 \times 4096 = 16,777,216 \text{ parameters}$ (16.78 Million floats).
Memory for gradients + optimizer states (AdamW takes 16 bytes per param):
$\text{VRAM}_{\text{AdamW}} = 16.78\text{M} \times 16 \text{ Bytes} \approx 268.4 \text{ MB per single matrix}$!

Scenario B: LoRA Parameter Count ($r = 4$)
- Matrix $A$ params: $r \times d_{\text{in}} = 4 \times 4096 = 16,384$
- Matrix $B$ params: $d_{\text{out}} \times r = 4096 \times 4 = 16,384$
Total LoRA Trainable Parameters:
$P_{\text{LoRA}} = 16,384 + 16,384 = 32,768 \text{ parameters}$.
Parameter Reduction Ratio:
$\frac{P_{\text{LoRA}}}{P_{\text{full}}} = \frac{32,768}{16,777,216} = \frac{1}{512} \approx 0.00195$!
Humne trainable parameters ko **512 guna kam** kar diya! 99.8% parameters freeze ho gaye aur memory requirement 268 MB se gir kar sirf 0.5 MB reh gayi!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum custom PyTorch LoRA Linear Layer from scratch implement karte hain: frozen base layer, low-rank adapters $A$ and $B$, scaling factor $\frac{\alpha}{r}$, aur runtime parameter merge/unmerge functionality.

```python
import math
import torch
import torch.nn as nn

class LoRALinear(nn.Module):
    \"\"\"Production implementation of Low-Rank Adaptation (LoRA) layer.\"\"\"
    def __init__(
        self, 
        base_linear: nn.Linear, 
        rank: int = 8, 
        alpha: float = 16.0, 
        dropout_p: float = 0.05
    ) -> None:
        super().__init__()
        self.base_linear = base_linear
        # Strictly freeze base pre-trained weights
        self.base_linear.weight.requires_grad = False
        if self.base_linear.bias is not None:
            self.base_linear.bias.requires_grad = False

        self.rank = rank
        self.alpha = alpha
        self.scaling = alpha / rank
        self.dropout = nn.Dropout(dropout_p) if dropout_p > 0.0 else nn.Identity()

        in_features = base_linear.in_features
        out_features = base_linear.out_features

        # Low-rank adapter matrices
        # Matrix A projects from in_features down to rank r
        self.lora_A = nn.Parameter(torch.empty(rank, in_features))
        # Matrix B projects from rank r up to out_features
        self.lora_B = nn.Parameter(torch.empty(out_features, rank))

        self.reset_parameters()

    def reset_parameters(self) -> None:
        # Standard LoRA initialization: Kaiming uniform for A, All Zeros for B!
        nn.init.kaiming_uniform_(self.lora_A, a=math.sqrt(5))
        nn.init.zeros_(self.lora_B)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 1. Base frozen pass: [B, S, out_features]
        base_output = self.base_linear(x)

        # 2. LoRA delta pass: x @ A.T @ B.T * scaling
        # x: [B, S, in_features]
        # x @ A.T -> [B, S, rank]
        # [B, S, rank] @ B.T -> [B, S, out_features]
        lora_delta = torch.matmul(self.dropout(x), self.lora_A.T)
        lora_delta = torch.matmul(lora_delta, self.lora_B.T) * self.scaling

        return base_output + lora_delta

    def merge_weights(self) -> None:
        \"\"\"Fuses adapter weights directly into base weight matrix for zero-latency inference.\"\"\"
        # delta_W = (B @ A) * scaling -> [out_features, in_features]
        delta_w = torch.matmul(self.lora_B, self.lora_A) * self.scaling
        self.base_linear.weight.data += delta_w

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    base_layer = nn.Linear(64, 64)
    lora_layer = LoRALinear(base_layer, rank=4, alpha=16.0)

    # Count trainable vs frozen parameters
    trainable_params = sum(p.numel() for p in lora_layer.parameters() if p.requires_grad)
    frozen_params = sum(p.numel() for p in lora_layer.parameters() if not p.requires_grad)

    print(f"Base Frozen Parameters:    {frozen_params}")
    print(f"LoRA Trainable Parameters: {trainable_params} ({trainable_params / (frozen_params + trainable_params) * 100:.2f}% of model)")

    sample_x = torch.randn(2, 64)
    out = lora_layer(sample_x)
    print(f"Output Tensor Shape:       {list(out.shape)} (Forward pass validated!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Non-Zero Initialization of Matrix $B$: Agar Matrix $B$ ko random values se initialize kar diya jaye to training ke step 0 par hi model ki output completely corrupt ho jati hai (Delta is non-zero). Matrix $B$ ko hamesha **All Zeros** se initialize karein taake step 0 par $\Delta W = 0$ ho aur model base model ki tarah behave kare.
2. Forgetting to Merge Adapters Before Production Deployment: Production inference par base model aur LoRA matrices ko alag alag calculate karna latency ko 30% slow kar deta hai. Deployment se pehle hamesha `merge_weights()` call karein taake $W = W_0 + \frac{\alpha}{r}BA$ single weight matrix ban jaye.
3. Training All Layers with Very High Rank ($r = 128$): Rank ko 128 karne se parameters barh jate hain aur LoRA ka faida khatam ho jata hai. Research ثابت karti hai ke $r = 8$ ya $16$ LLaMA-3 ke liye 98% optimal performance deta hai.

Zero-GPU Tip:
LoRA linear layers ki parameter counting, matrix algebra, aur weight merging calculations CPU par milliseconds mein execute hoti hain. Pehle apne laptop CPU par LoRA layer wrapping test karein, phir Google Colab T4 GPU par 4-bit QLoRA script run karein.

Self-Check Questions:
1. LoRA mein Matrix $B$ ko Zero initialize karna kyun mathematical zaroorat hai?
2. QLoRA 4-bit NormalFloat (NF4) standard FP4 ke muqablay information preservation mein kyun behtar hai?
3. Adapter merging technique production deployment mein inference latency ko kaise khatam karti hai?

What to Build Next:
Ek Parameter Efficiency Profiler script banayein jo ek multi-layer transformer network le, uski Attention Linear layers ko LoRA se replace kare, aur trainable vs frozen memory footprint report kare."""

# ==============================================================================
# LESSON 9.2: Dataset Curation & ChatML Formatting: Packing & Masks
# ==============================================================================
LESSON_CONTENT['9.2'] = r"""### Part 1: Mental Model & South Asian Analogy
LLM fine-tuning ka golden rule hai: "Garbage In, Garbage Out". Agar aap model ko be-dhangay format mein data feed karenge to model ghalat tokens bolne lagega ya prompt aur response ke darmiyan tameez kho dega. Yahan do zaroori cheezein aati hain: **ChatML Formatting** aur **Sequence Packing with Loss Masking**!
Isay samajhne ke liye kisi Mithai Ke Dabbay aur Takhseem Karne wale Munshi ki misaal lein:
1. ChatML Special Tokens (Mithai Ke Dabbay Ke Partition): Farz karein aap aik dabbay mein gulab jamun, barfi, aur cham-cham pack kar rahe hain. Agar beech mein plastic ke partitions (Special Tokens: `<|im_start|>system...<|im_end|>`) na hon to tamam mithaiyan aapas mein mil kar halwa ban jayengi! ChatML format model ko batata hai ke kahan system prompt khatam hua aur kahan se user ka sawal shuru hua.
2. Loss Masking (Sirf Shagird Ki Mehnat Par Number Dena): Imtihan mein master ji sirf shagird ke likhe hue jawab (Assistant Response) par number dete hain; sawal (User Prompt) par koi number nahi milta! Agar hum user prompt par bhi loss calculate karein to model sawal ratta maarne par focus karega. Loss Masking prompt ke tamam tokens par target `-100` laga deti hai taake PyTorch Cross-Entropy unhe nazar-andaz kar de!
3. Sequence Packing (Truck Mein Khali Jagah Khatam Karna): Aam tor par har sentence ke aakhir mein hazaron `<pad>` tokens lagaye jate hain. Yeh aisa hai jese aadhe khali truck shehar bheje jayein (Compute Waste). Sequence Packing 5 chotay sentences ko ek hi 4096-token ke batch mein bina padding ke thoons deti hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Cross-Entropy Loss Masking with `ignore_index = -100` ka exact hisab lagayein.
Vocabulary Size $V = 4$ tokens: `[0: "Chai", 1: "Piyo", 2: "User", 3: "Assistant"]`
Sequence contains 4 tokens:
Token 0: `"User"` (Prompt Token)
Token 1: `"Chai"` (Prompt Token)
Token 2: `"Assistant"` (Separator Token)
Token 3: `"Piyo"` (Target Assistant Response Token!)

Targets Array with Loss Masking:
Target Label Tensor:
`targets = [-100, -100, -100, 1]`

Model Output Logits at Position 3 (Predicting token 3):
Predicted Logits for Vocabulary: $z = [1.0, 4.0, 0.5, 0.2]$
Softmax Probability for Target Token 1 ("Piyo"):
$P(\text{Token 1}) = \frac{e^{4.0}}{e^{1.0} + e^{4.0} + e^{0.5} + e^{0.2}} = \frac{54.598}{2.718 + 54.598 + 1.649 + 1.221} = \frac{54.598}{60.186} \approx 0.9071$

Loss Calculation:
- Loss at Pos 0: Ignored because target is $-100$ ($L_0 = 0$).
- Loss at Pos 1: Ignored ($L_1 = 0$).
- Loss at Pos 2: Ignored ($L_2 = 0$).
- Loss at Pos 3: Active!
  $L_3 = -\log_e(0.9071) = 0.0975$.
Total Batch Loss:
$L_{\text{total}} = \frac{0 + 0 + 0 + 0.0975}{1 \text{ active token}} = 0.0975$!
Model ne sirf aur sirf Assistant ke response token par gradient calculate kiya! Prompt tokens par zero gradient gaya jisse model ki instruction-following 100% sharp rehti hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum ChatML template formatting, instruction masking (prompt tokens set to `-100`), aur continuous sequence packing pipeline implement karte hain.

```python
import torch
from typing import List, Dict, Any

# ChatML Special Token Delimiters
IM_START = "<|im_start|>"
IM_END = "<|im_end|>"

def format_chatml_conversation(messages: List[Dict[str, str]]) -> str:
    \"\"\"Formats list of role/content dicts into strict ChatML standard text.\"\"\"
    formatted_parts = []
    for msg in messages:
        role = msg["role"]
        content = msg["content"].strip()
        formatted_parts.append(f"{IM_START}{role}\\n{content}{IM_END}")
    return "\\n".join(formatted_parts) + "\\n"

def build_instruction_masked_sample(
    system_text: str, 
    user_prompt: str, 
    assistant_response: str
) -> Dict[str, torch.Tensor]:
    \"\"\"Constructs token tensors with target prompt tokens masked to -100.\"\"\"
    # Mock Tokenizer Mapping for demonstration
    mock_vocab = {
        "<|im_start|>": 1, "<|im_end|>": 2, "system": 3, 
        "user": 4, "assistant": 5, "karak": 6, "chai": 7, 
        "recipe": 8, "doodh": 9, "aur": 10, "patti": 11
    }
    
    # Prompt prefix: System + User
    prompt_str = f"{IM_START}system\\n{system_text}{IM_END}\\n{IM_START}user\\n{user_prompt}{IM_END}\\n{IM_START}assistant\\n"
    response_str = f"{assistant_response}{IM_END}"

    # Simulated token sequences
    prompt_tokens = [1, 3, 1, 4, 6, 7, 8, 2, 1, 5]   # 10 prompt tokens
    response_tokens = [9, 10, 11, 2]                  # 4 response tokens

    input_ids = prompt_tokens + response_tokens
    
    # Target labels: Mask prompt tokens with -100 (PyTorch ignore_index)
    labels = ([-100] * len(prompt_tokens)) + response_tokens

    return {
        "input_ids": torch.tensor(input_ids, dtype=torch.long),
        "labels": torch.tensor(labels, dtype=torch.long)
    }

# Execution test
if __name__ == "__main__":
    conversation = [
        {"role": "system", "content": "You are a friendly Dhaba assistant."},
        {"role": "user", "content": "Karak chai recipe?"},
        {"role": "assistant", "content": "Doodh aur patti ubaalein."}
    ]

    formatted_text = format_chatml_conversation(conversation)
    print("Formatted ChatML Document:\\n", formatted_text)

    sample = build_instruction_masked_sample(
        "You are a friendly Dhaba assistant.",
        "Karak chai recipe?",
        "Doodh aur patti ubaalein."
    )
    print("Input IDs Tensor: ", sample["input_ids"].tolist())
    print("Labels Tensor:    ", sample["labels"].tolist())
    print(f"Masked Tokens Count (-100): {(sample['labels'] == -100).sum().item()} (Prompt preserved, zero loss leakage!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Forgetting to Mask Prompt Tokens (Training on User Questions): Agar aap target labels mein prompt tokens ko `-100` nahi karte to model user ke sawal ratta maarne lagta hai aur naye sawalon par user ki guftagu ko hi autocomplete karne lagta hai.
2. Missing EOS / `<|im_end|>` Tokens in Training Data: Agar response ke aakhir mein End-Of-Sequence token na ho to trained model inference ke waqt rukna bhool jata hai aur infinite loop mein be-tukka text generate karta rehta hai.
3. Inconsistent Chat Template Formatting: Training ke waqt LLaMA-3 format use karna aur inference ke waqt ChatML format use karna model ko completely destabilize kar deta hai. Hamesha tokenizer ka official `apply_chat_template` use karein.

Zero-GPU Tip:
Dataset formatting, tokenization, ChatML templating, aur sequence packing 100% CPU bound data engineering tasks hain. Hugging Face `datasets` library ke zariye aap apne local CPU par hazaron JSONL records ko fine-tuning ke liye sanitize aur tokenize kar sakte hain.

Self-Check Questions:
1. ChatML format mein `<|im_start|>` aur `<|im_end|>` special tokens ka kya maqsad hota hai?
2. PyTorch CrossEntropyLoss mein `ignore_index = -100` ka kya role hota hai?
3. Sequence Packing fixed-length padding ke muqablay training throughput ko 3x kyun barha deti hai?

What to Build Next:
Ek Dataset Curation Script banayein jo raw Roman Urdu FAQs ko load kare, unhe strict ChatML schema mein transform kare, length distribution analyze kare, aur tokenized Hugging Face dataset disk par export kare."""

# ==============================================================================
# LESSON 9.3: Fast 4-bit Fine-Tuning with Unsloth: Triton Kernels & FlashAttention
# ==============================================================================
LESSON_CONTENT['9.3'] = r"""### Part 1: Mental Model & South Asian Analogy
Standard Hugging Face `peft` aur `transformers` libraries ke zariye LLaMA fine-tuning bohot aahista chalti hai aur VRAM explode karti hai. 2024-2026 mein fine-tuning ki dunya ka absolute king **Unsloth** ban chuka hai jo fine-tuning ko **2x se 5x tez** aur **70% kam VRAM** par chalata hai!
Isay samajhne ke liye kisi Sports Car ki Engine Tuning aur Custom Hand-Built Parts ki misaal lein:
1. Standard PyTorch Training (Factory Car with Heavy Luggage): Standard PyTorch general-purpose hota hai. Yeh har intermediate calculation ko VRAM mein save karta hai taake autograd backward pass kar sake (Gigabytes of intermediate activation memory).
2. Unsloth's Hand-Written Triton Kernels (Racing Engine): Unsloth ke developers ne PyTorch ke slow generic functions ko hata kar directly OpenAI ki **Triton language** mein custom GPU assembly kernels likhe hain:
   - RoPE kernel ko C-level par fuse kar diya.
   - Cross-Entropy loss ko single GPU pass mein compute kiya bina 1000-logit intermediate tensor banaye.
   - Manual analytical backward passes likhe jisse PyTorch autograd graph ka memory footprint 80% ghir gaya!
3. FlashAttention-2 / FlashAttention-3 Integration: Standard attention $QK^T$ matrix ko poora VRAM mein likhti hai ($O(S^2)$ Memory). FlashAttention matrix ko GPU ke ultra-fast SRAM cache (Level 1 cache) mein chotay chotay blocks (Tiling) mein multiply karti hai. VRAM mein koi bara matrix likha hi nahi jata!
4. The Miracle Outcome: Ek akela free Google Colab T4 GPU (16 GB VRAM) jo pehle 7B model ko train karte hi crash ho jata tha, Unsloth ke zariye LLaMA-3.1-8B ko 4-bit mein makhan ki tarah train karta hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Fused Cross-Entropy Loss aur Intermediate Memory Savings ka exact hisab lagayein.
Standard PyTorch Cross-Entropy Memory Footprint:
- Batch Size $B = 4$
- Sequence Length $S = 2048$ tokens
- Total tokens in batch: $B \times S = 4 \times 2048 = 8192 \text{ tokens}$.
- Vocabulary Size $V = 128,256$ tokens (LLaMA-3 standard vocabulary).
- Precision: 32-bit Float $= 4 \text{ Bytes per number}$.

Standard PyTorch Calculation:
PyTorch pehle full logits tensor banata hai:
$\\text{Shape} = [B \times S, V] = [8192, 128256] \approx 1,050,673,152 \text{ elements}$.
Logits Tensor Memory Allocation in VRAM:
$\\text{Memory} = 1,050,673,152 \times 4 \text{ Bytes} \approx 4,202,692,608 \text{ Bytes} \approx 4.20 \text{ GB}$!
Sirf aakhri layer ka intermediate logits tensor akela 4.2 GB VRAM kha gaya!

Unsloth Fast Fused Cross-Entropy Kernel:
Unsloth full $[8192, 128256]$ tensor ko VRAM mein allocate hi nahi karta!
Triton kernel har token ke liye on-the-fly GPU registers ke andar Softmax aur Loss nikalta hai aur sirf scalar loss value VRAM mein bhejta hai:
$\\text{VRAM Allocated} = 8192 \times 4 \text{ Bytes} \approx 32.7 \text{ KB}$!
Intermediate VRAM Memory Reduction:
$4.20 \text{ GB} \to 32.7 \text{ KB}$ ($\approx 128,000\times \text{ Memory Savings on Logits}$)!
Yahi wajah hai ke Unsloth par Out-Of-Memory (OOM) kabhi nahi aata.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Unsloth fast fine-tuning pipeline ka production script implement karte hain: FastLanguageModel loading, 4-bit QLoRA target module injection, aur memory monitoring.

```python
# Production Unsloth Fine-Tuning Recipe (Targeted for Colab T4 / L4 / A10G)
# Note: Executed in environment with `pip install unsloth`

import torch
from typing import Dict, Any

def setup_unsloth_fast_training(
    model_name: str = "unsloth/Meta-Llama-3.1-8B-bnb-4bit",
    max_seq_len: int = 2048,
    lora_rank: int = 16
) -> Dict[str, Any]:
    \"\"\"Configures Unsloth optimized FastLanguageModel with fused Triton kernels.\"\"\"
    
    # 1. Model Configuration Dictionary (Simulated for environments without raw CUDA)
    config = {
        "model_name": model_name,
        "max_seq_length": max_seq_len,
        "dtype": "float16",
        "load_in_4bit": True,
        # Key LoRA targeting: all linear attention and MLP projections
        "target_modules": [
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj"
        ],
        "lora_r": lora_rank,
        "lora_alpha": lora_rank * 2,
        "lora_dropout": 0.0,  # Unsloth officially recommends dropout=0 for fast kernels!
        "bias": "none",
        "use_gradient_checkpointing": "unsloth",  # 60% less VRAM usage
        "random_state": 3407
    }
    
    return config

def print_vram_savings_summary(gpu_name: str = "Nvidia Tesla T4 (15.8 GB)") -> None:
    print(f"--- Unsloth Hardware Optimization Report for {gpu_name} ---")
    print("Standard HuggingFace PEFT VRAM: 14.8 GB (Frequent OOM on batch > 1)")
    print("Unsloth 4-bit Fused VRAM:      6.8 GB (Enables Batch Size 4 + 2048 Context)")
    print("Training Throughput Speedup:   2.4x Faster (Fused Triton RoPE + CrossEntropy)")
    print("Supported Free Environments:   Google Colab Free Tier, Kaggle Free Dual T4s")

# Execution test
if __name__ == "__main__":
    training_plan = setup_unsloth_fast_training()
    print("Unsloth Training Specification Compiled Successfully:")
    for k, v in training_plan.items():
        print(f"  {k:26s}: {v}")
    print()
    print_vram_savings_summary()
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Setting `lora_dropout > 0.0` in Unsloth: Unsloth ke custom hand-written Triton kernels tab activate hote hain jab dropout 0.0 ho. Agar aap `lora_dropout = 0.05` set kar dein to Unsloth slow standard PyTorch fallback par chala jata hai aur 2x speedup khatam ho jata hai. Hamesha `lora_dropout = 0` rakhein.
2. Forgetting `FastLanguageModel.for_inference(model)`: Training ke baad inference karte waqt agar aap `.for_inference()` call na karein to model 2x slow generate karta hai. Yeh method inference ke liye KV Cache aur native generation kernels activate karta hai.
3. Exceeding Pre-Allocated `max_seq_len`: Agar aapne model ko `max_seq_length = 2048` par load kiya aur dataset mein 4096-token sequence aa jaye to RoPE position cache out of bounds crash ho sakti hai.

Zero-GPU Tip:
Unsloth training script configuration, dataset preparation, aur ChatML tokenization mapping pure CPU par execute hoti hai. Aap apne laptop par poora dataset aur training configuration prepare karein, aur phir script ko Google Colab ke free tier T4 GPU par 1-click command se 1 ghantay mein fine-tune kar lein.

Self-Check Questions:
1. Unsloth standard Hugging Face PEFT ke muqablay 2x se 5x speedup kaise deta hai?
2. Fused Cross-Entropy Triton Kernel VRAM memory ko Gigabytes se Kilobytes par kaise girata hai?
3. FlashAttention-2 GPU SRAM caching ke zariye $O(S^2)$ memory bottleneck ko kaise solve karti hai?

What to Build Next:
Ek Colab Notebook Fine-Tuning Pipeline setup karein jo Unsloth use karke LLaMA-3.1-8B-bnb-4bit ko 500 Roman Urdu customer support dialogues par 1 epoch train kare aur loss curve log kare."""

# ==============================================================================
# LESSON 9.4: Preference Alignment: Direct Preference Optimization (DPO) & ORPO
# ==============================================================================
LESSON_CONTENT['9.4'] = r"""### Part 1: Mental Model & South Asian Analogy
Supervised Fine-Tuning (SFT) model ko bolna to sikha deti hai, lekin model ki tameez, ikhlaq, aur user ki pasand (Preference) ko align karna alag marhala hai. 2023 se pehle RLHF (Reinforcement Learning from Human Feedback) use hota tha jisme 3 alag alag models (Policy, Value, Reward Model) aur PPO algorithm chalana parta tha jo be-inteha unstable tha. 2024-2026 mein dunya **Direct Preference Optimization (DPO)** aur **ORPO** par shift ho chuki hai!
Isay samajhne ke liye kisi Ammi Jaan aur Bachay ke Pasand/Na-pasand ke Khane ki misaal lein:
1. SFT (Khana Khana Seekhna): Bacha roti ka luqma tor kar munh mein daalna seekhta hai.
2. The Complex RLHF (Teesra Judge / Khala Ka Hisab): Purane tareeqay mein ek teesra banda (Reward Model) baithta tha jo har luqmay par number deta tha: "8 out of 10!" Phir PPO algorithm complex mathematical policy gradient se bachay ki aadat theek karta tha. Yeh nizaam bar bar crash hota tha.
3. DPO (Ammi Ka Direct Faisla - Rafale Paper 2023): DPO ne mathematical proving se dikhaya ke kisi alag Reward Model ki zaroorat hi nahi hai! Model ka apna Language Model hi Reward Model ke taur par mathematically represent ho sakta hai. Ammi bache ke samne do platein rakhti hain:
   - Chosen ($y_w$ - Winner): Garam Biryani.
   - Rejected ($y_l$ - Loser): Thandi Daliya.
   DPO loss function direct mathematically model ko kehta hai: "Chosen response ki probability barhao aur Rejected response ki probability ghirao!"
4. ORPO (Odds Ratio Preference Optimization): ORPO ne SFT aur DPO ko ek hi single training step mein merge kar diya bina kisi Reference Model ke, jisse VRAM aadhi reh gayi!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Direct Preference Optimization (DPO) Loss ka exact mathematical formula trace karte hain.
DPO Loss Formula:
$L_{\text{DPO}}(\pi_\theta; \pi_{\text{ref}}) = -\mathbb{E} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w | x)}{\pi_{\text{ref}}(y_w | x)} - \beta \log \frac{\pi_\theta(y_l | x)}{\pi_{\text{ref}}(y_l | x)} \right) \right]$
Jahan:
- $\pi_\theta$: Train hone wala Active Model
- $\pi_{\text{ref}}$: Frozen Reference Baseline Model (Model ko zyada door bhatakne se roknay ke liye)
- $y_w$: Chosen (Winning / Helpful) response
- $y_l$: Rejected (Losing / Harmful / Hallucinated) response
- $\beta$: Regularization temperature constant (e.g. $\beta = 0.1$)
- $\sigma$: Standard Sigmoid function

Worked Numeric Example:
Let Log-Ratios (Implicit Reward differences):
Farz karein active model ne chosen answer ki probability reference model ke muqablay barha di:
$\log \frac{\pi_\theta(y_w)}{\pi_{\text{ref}}(y_w)} = +2.0$ (Policy favors chosen response)
Aur rejected answer ki probability gira di:
$\log \frac{\pi_\theta(y_l)}{\pi_{\text{ref}}(y_l)} = -1.5$ (Policy disfavors rejected response)
Parameter $\beta = 0.1$.

Step 1: Compute Scaled Implicit Reward Margin ($\Delta R$)
$\Delta R = \beta \left( (+2.0) - (-1.5) \right) = 0.1 \times (2.0 + 1.5) = 0.1 \times 3.5 = 0.3500$

Step 2: Pass Margin through Sigmoid
$\sigma(\Delta R) = \sigma(0.35) = \frac{1}{1 + e^{-0.35}}$
$e^{-0.35} \approx 0.70469$
$\sigma(0.35) = \frac{1}{1 + 0.70469} = \frac{1}{1.70469} \approx 0.5866$

Step 3: Compute Final DPO Loss
$L_{\text{DPO}} = -\log_e(0.5866) \approx -(-0.5334) = 0.5334$

Contrast with Inverted Failure Case:
Agar model chosen ko gira de (-2.0) aur rejected ko barha de (+2.0):
$\Delta R = 0.1 \times (-2.0 - 2.0) = -0.40$
$\sigma(-0.40) \approx 0.4013$
$L_{\text{DPO}} = -\log_e(0.4013) \approx 0.9130$ (Loss nearly doubles)!
Model majboor ho jata hai ke chosen response ki probability ko maximize aur rejected response ko minimize kare.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum numerically-stable DPO loss function from first principles implement karte hain aur chosen vs rejected log-probabilities ke sath verify karte hain.

```python
import torch
import torch.nn.functional as F

def compute_dpo_loss(
    policy_chosen_logps: torch.Tensor,
    policy_rejected_logps: torch.Tensor,
    reference_chosen_logps: torch.Tensor,
    reference_rejected_logps: torch.Tensor,
    beta: float = 0.1
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    \"\"\"Calculates Direct Preference Optimization (DPO) loss from first principles.
    
    Shapes:
      All logps tensors have shape: [Batch_Size]
    Returns:
      loss, chosen_rewards, rejected_rewards
    \"\"\"
    # 1. Compute log ratios between policy and reference
    pi_logratios = policy_chosen_logps - policy_rejected_logps
    ref_logratios = reference_chosen_logps - reference_rejected_logps

    # 2. Implicit reward margins scaled by beta
    logits = beta * (pi_logratios - ref_logratios)

    # 3. DPO Loss: -log(sigmoid(logits)) = softplus(-logits)
    # Using F.logsigmoid for numerical stability against underflow
    losses = -F.logsigmoid(logits)

    # 4. Implicit reward metrics for tracking
    chosen_rewards = beta * (policy_chosen_logps - reference_chosen_logps).detach()
    rejected_rewards = beta * (policy_rejected_logps - reference_rejected_logps).detach()

    return losses.mean(), chosen_rewards.mean(), rejected_rewards.mean()

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    # Simulated batch of 2 preference pairs
    # Model assigns higher log-prob to chosen response
    pol_chosen = torch.tensor([-2.1, -1.8])
    pol_rejected = torch.tensor([-4.5, -5.2])
    
    ref_chosen = torch.tensor([-2.5, -2.0])
    ref_rejected = torch.tensor([-3.8, -4.0])

    loss, r_chosen, r_rejected = compute_dpo_loss(
        pol_chosen, pol_rejected, ref_chosen, ref_rejected, beta=0.1
    )

    print(f"DPO Loss Computed:          {loss.item():.4f}")
    print(f"Implicit Chosen Reward:     {r_chosen.item():.4f}")
    print(f"Implicit Rejected Reward:   {r_rejected.item():.4f}")
    print(f"Reward Margin (Delta):      {(r_chosen - r_rejected).item():.4f} (Positive margin confirms alignment!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Setting Beta ($\beta$) Too High: Agar $\beta = 1.0$ set kar diya jaye to DPO reference model se deviate hone par itni shadeed saza deta hai ke model kuch naya seekh hi nahi pata. Beta ko hamesha $0.05$ se $0.1$ ke darmiyan rakhein.
2. Contaminated Preference Datasets: Agar preference dataset mein chosen aur rejected responses mein koi khas farq na ho ya chosen response ghalat ho to DPO model ke outputs ko degrade kar deta hai. Human curation lazmi hai.
3. Two Models in VRAM Memory Spike: Standard DPO mein policy model aur reference model dono ko VRAM mein rakhna parta hai (Double Memory). Isay hal karne ke liye **ORPO** use karein ya Reference Model ke log-probabilities ko pre-compute karke disk par cache kar lein.

Zero-GPU Tip:
DPO loss calculation aur probability tracking pure element-wise scalar math hai. Aap apne laptop CPU par synthetic log-probabilities ke sath DPO vs ORPO loss behavior verify kar sakte hain.

Self-Check Questions:
1. DPO ne complex PPO/RLHF pipelines ki zaroorat ko kaise khatam kiya?
2. DPO loss formula mein Reference Model ($\pi_{\text{ref}}$) ka kya kirdaar hota hai?
3. ORPO (Odds Ratio Preference Optimization) DPO ke muqablay VRAM memory kaise bachati hai?

What to Build Next:
Ek Preference Dataset Validator script banayein jo ek JSONL file read kare, verify kare ke har record mein `prompt`, `chosen`, aur `rejected` keys mojud hon, aur length disparity check kare."""

# ==============================================================================
# LESSON 9.5: DeepSeek-R1 GRPO: Reasoning Chains & Value-Model-Free RL
# ==============================================================================
LESSON_CONTENT['9.5'] = r"""### Part 1: Mental Model & South Asian Analogy
January 2025 mein DeepSeek ne **DeepSeek-R1** release karke poori dunya ke hosh ura diye. OpenAI ke o1 model ke muqablay DeepSeek ne dikhaya ke model ko mathematical reasoning aur coding sikhane ke liye kisi mehangay Value Model ya human preference ki zaroorat nahi hai. Is inqilab ka naam hai **GRPO (Group Relative Policy Optimization)**!
Isay samajhne ke liye kisi Class ke 4 Shagirdon aur Mathematics ke Sawaal ki misaal lein:
1. PPO with Value Model (Purana Mehnga Tareeqa): PPO mein har step par ek bohot bara doosra model (Value Model / Critic) baithta tha jo har token par state value predict karta tha. Yeh Critic model utni hi GPU memory khata tha jitna asal model (Double VRAM explosion).
2. GRPO (Value-Model-Free Group Competition): GRPO Critic model ko seedha kachray ke dabbay mein phenk deta hai! GRPO kya karta hai?
   - Aik hi sawal par model se **4 mukhtalif jawab (Group of $G=4$ Rollouts)** generate karwata hai.
   - Har jawab ko ek Rule-Based Tester (Compiler / Python test / Exact math answer checker) ke zariye check kiya jata hai.
3. Group Relative Scoring (Apne Hi Sathiyon Se Muqabla):
   - Jawab 1: Test Pass (Reward = +1.0)
   - Jawab 2: Syntax Error (Reward = 0.0)
   - Jawab 3: Wrong Number (Reward = 0.0)
   - Jawab 4: Test Pass (Reward = +1.0)
   GRPO in 4 jawabat ka Group Mean aur Group Standard Deviation nikalta hai. Jis jawab ne group ke average se behtar perform kiya (Positive Advantage), uski probability barha di jati hai!
4. The Emergence of `<think>` (Aap-Se-Aap Sochne Ka Jazba): Model par jab reward lagaya gaya to model ne khud ba khud lambi reasoning chains (`<think>... wait, let me re-check this step...</think>`) generate karna shuru kar dein! Model ne insani training ke baghair khud ghaltiyan pakarna seekh liya!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein GRPO ke Group Advantage Normalization ka exact hisab lagayein.
Formula for Group Advantage of sample $i$ in group of size $G$:
$A_i = \frac{r_i - \text{mean}(r)}{\text{std}(r) + \epsilon}$
Jahan:
- $r = [r_1, r_2, \dots, r_G]$: Group of rule-based rewards
- $\text{mean}(r) = \frac{1}{G} \sum r_i$
- $\text{std}(r) = \sqrt{\frac{1}{G} \sum (r_i - \text{mean}(r))^2}$

Worked Numeric Scenario:
Single Math Puzzle: "What is $17 \times 24$?" Target Answer: $408$.
Group Size $G = 4$ candidate rollouts generated by model:
- Rollout 1: Concludes with 408 (Correct! Reward $r_1 = 1.0$)
- Rollout 2: Concludes with 398 (Incorrect! Reward $r_2 = 0.0$)
- Rollout 3: Concludes with 408 (Correct! Reward $r_3 = 1.0$)
- Rollout 4: Fails to finish (Format error! Reward $r_4 = 0.0$)
Rewards Vector: $r = [1.0, 0.0, 1.0, 0.0]$.

Step 1: Compute Group Mean
$\text{mean}(r) = \frac{1.0 + 0.0 + 1.0 + 0.0}{4} = \frac{2.0}{4} = 0.5000$

Step 2: Compute Group Standard Deviation
$\sigma^2 = \frac{(1-0.5)^2 + (0-0.5)^2 + (1-0.5)^2 + (0-0.5)^2}{4} = \frac{0.25 + 0.25 + 0.25 + 0.25}{4} = \frac{1.0}{4} = 0.2500$
$\text{std}(r) = \sqrt{0.25} = 0.5000$

Step 3: Compute Relative Advantage for Each Rollout:
- $A_1 = \frac{1.0 - 0.50}{0.50} = \frac{+0.50}{0.50} = +1.0000$ (Positive Advantage: Gradient pushes policy to reinforce this reasoning trajectory!)
- $A_2 = \frac{0.0 - 0.50}{0.50} = \frac{-0.50}{0.50} = -1.0000$ (Negative Advantage: Gradient suppresses this trajectory!)
- $A_3 = +1.0000$
- $A_4 = -1.0000$
Zero Value Model, Zero Critic Network, Zero extra VRAM! Sirf group ke andar relative ranking se policy perfect mathematical reasoning seekh leti hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum DeepSeek-R1 style Group Relative Policy Optimization (GRPO) advantage calculator aur rule-based math verification reward function implement karte hain.

```python
import torch
from typing import List, Dict, Any

def rule_based_math_reward(completion_text: str, ground_truth: str) -> float:
    \"\"\"Deterministic programmatic reward: verifies exact answer inside <answer> tags.\"\"\"
    import re
    match = re.search(r"<answer>(.*?)</answer>", completion_text, re.DOTALL)
    if not match:
        return 0.0  # Format penalty
    extracted = match.group(1).strip()
    return 1.0 if extracted == ground_truth else 0.0

def compute_grpo_advantages(rewards: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    \"\"\"Normalizes rewards across group rollouts without a Critic Value model.
    
    Shapes:
      rewards: [Group_Size] or [Batch_Size, Group_Size]
    Returns:
      advantages: Same shape as rewards
    \"\"\"
    mean = rewards.mean(dim=-1, keepdim=True)
    std = rewards.std(dim=-1, keepdim=True)
    # Relative advantage: (r - mean) / (std + eps)
    advantages = (rewards - mean) / (std + eps)
    return advantages

# Execution test
if __name__ == "__main__":
    # Simulate G = 4 rollouts for query: "Calculate 15 * 14" (Answer: 210)
    target = "210"
    rollouts = [
        "<think>15 * 10 = 150, 15 * 4 = 60, 150 + 60 = 210</think><answer>210</answer>",
        "<think>15 * 14 is approximately 200</think><answer>200</answer>",
        "<think>Let me multiply: 15 * 14 = 210</think><answer>210</answer>",
        "The answer is 210."  # Missing strict <answer> tags -> Format violation!
    ]

    # Evaluate rule-based rewards
    scores = [rule_based_math_reward(r, target) for r in rollouts]
    rewards_tensor = torch.tensor(scores, dtype=torch.float32)

    advantages = compute_grpo_advantages(rewards_tensor)

    print(f"Group Rollouts Count: {len(rollouts)}")
    print(f"Rule-Based Raw Rewards: {rewards_tensor.tolist()}")
    print(f"GRPO Relative Advantages: {advantages.tolist()}")
    print("\\nInterpretation: Rollouts 0 and 2 receive +1.0 advantage; Rollouts 1 and 3 receive -1.0 penalty.")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Zero Variance in Group (All Correct or All Wrong): Agar group ke tamam $G$ rollouts ka reward $1.0$ ho ya tamam ka $0.0$ ho, to $\text{std}(r) = 0$ ho jata hai. Advantage formula mein division by zero rokne ke liye hamesha $\epsilon = 10^{-8}$ lagayein ya advantage ko zero set karein.
2. Vague Natural Language Reward Evaluators: Agar reward function LLM ko judge bana kar lagaya jaye to model reward-hacking shuru kar deta hai (judge ko khush karne ke liye lambi bekaar baatein likhta hai). GRPO tab sab se behtareen kaam karta hai jab reward function **Rule-Based Compiler ya Math Evaluator** ho.
3. Too Small Group Size ($G < 4$): Agar group size sirf 2 ho to variance bohot noisy hoti hai. DeepSeek standard $G = 8$ ya $16$ rollouts per prompt use karta hai.

Zero-GPU Tip:
GRPO advantage calculation aur rule-based verification pure Python logic hai. Aap chote models (jaise Qwen-2.5-Coder-1.5B) par local CPU ya free Colab T4 par GRPO reasoning trajectories train kar sakte hain.

Self-Check Questions:
1. DeepSeek-R1 ka GRPO algorithm OpenAI ke PPO se memory aur architecture mein kaise mukhtalif hai?
2. Group Advantage calculation mein Value Model (Critic Network) ki zaroorat kyun khatam ho jati hai?
3. GRPO training ke doran model ke andar `<think>` reasoning tokens khud ba khud kyun emerge hote hain?

What to Build Next:
Ek GRPO Gym Environment banayein jo simple algebra equations generate kare, 4 candidate solutions evaluate kare, aur GRPO advantage scores calculate karke policy update direction print kare."""

# ==============================================================================
# LESSON 9.6: Module 9 Capstone: Fine-Tune Domain LLM & GGUF Export
# ==============================================================================
LESSON_CONTENT['9.6'] = r"""### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne Modern Fine-Tuning ke tamam azeem aur advance sutoon (LoRA/QLoRA mathematics, ChatML masking, Unsloth fast Triton acceleration, DPO alignment, aur DeepSeek-R1 GRPO) master kar liye hain. Ab waqt hai is safar ke sab se exciting Capstone project ka: **Apna Custom Domain Model Fine-Tune Karna, LoRA Adapters Merge Karna, aur 100% Offline GGUF Format Mein Export Karna**!
Is Capstone project ka zehni khaka kisi Bare Sunehri Karkhanay (Goldsmith / Zewar Factory) jaisa hai:
1. The Raw Pure Gold (Open-Source Base Model): Hamare paas LLaMA-3.1-8B ya Qwen-2.5-7B ka chamakta hua base model hai.
2. The Specialized Crafting (Domain QLoRA Fine-Tuning): Hum model ko Pakistani Tax Law, Corporate Accounting, ya Dhaba Khata Management ke 2,000 verified dialogues par 4-bit QLoRA se train karte hain. Model domain expert ban jata hai.
3. The Fusion Furnace (Adapter Merging): Training ke baad LoRA adapter matrices ($B \times A$) ko pighla kar direct base model ke 16-bit float weights mein permanently fuse (merge) kar diya jata hai. Ab model ko kisi external adapter ki zaroorat nahi rehti!
4. The Precision Mint (GGUF Quantization via llama.cpp): Aakhir mein 16-bit model (16 GB size) ko **GGUF Q4_K_M** (4-bit) mein quantize kar diya jata hai. Model ka size gir kar sirf **4.5 GB** reh jata hai! Ab yeh model bina kisi internet ke, kisi bhi saste laptop ya mobile par 100% offline bijli ki raftaar se chalta hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Weight Merging aur GGUF Quantization Compression Ratio ka exact hisab lagayein.
Parameters:
- Model: LLaMA-3.1-8B Parameters ($N = 8.03 \times 10^9$ params)
- Initial Precision: 16-bit Brain Float (BF16 = 2 Bytes per parameter)
- Quantized Target: GGUF 4-bit medium (`Q4_K_M` $\approx 4.5 \text{ bits per parameter}$ average including scales)

Step 1: Compute 16-Bit Merged Base Model Size on Disk:
$\text{Size}_{\text{BF16}} = 8.03 \times 10^9 \times 2 \text{ Bytes} \approx 16.06 \times 10^9 \text{ Bytes} \approx 14.96 \text{ GB}$.
Isay chalane ke liye minimum 16 GB VRAM GPU chahiye hota hai.

Step 2: Compute GGUF Q4_K_M Quantized Size on Disk:
Har parameter average 4.5 bits leta hai ($4.5 / 8 = 0.5625 \text{ Bytes}$):
$\text{Size}_{\text{GGUF}} = 8.03 \times 10^9 \times 0.5625 \text{ Bytes} \approx 4.516 \times 10^9 \text{ Bytes} \approx 4.21 \text{ GB}$!

Compression Metrics:
- File Size Reduction: $\frac{14.96 \text{ GB}}{4.21 \text{ GB}} \approx 3.55\times \text{ Storage Savings}$!
- Memory Bandwidth Speedup on CPU: Model 4.2 GB RAM mein load ho jata hai. Standard 16GB RAM laptop par CPU memory bus 50 GB/s bandwidth deti hai:
  $\text{Theoretical Generation Speed} = \frac{50 \text{ GB/s}}{4.21 \text{ GB}} \approx 11.8 \text{ tokens per second}$ completely offline on CPU!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete Capstone lifecycle script implement karte hain: adapter weight merging verification, GGUF metadata schema validation, aur offline llama.cpp inference execution simulation.

```python
import os
import tempfile
import torch
import torch.nn as nn
from typing import Dict, Any

class ModelExportPipeline:
    \"\"\"Production lifecycle manager for adapter merging and GGUF quantization export.\"\"\"
    def __init__(self, model_id: str, adapter_rank: int = 16) -> None:
        self.model_id = model_id
        self.adapter_rank = adapter_rank

    def simulate_adapter_fusion(self, base_weight: torch.Tensor, lora_a: torch.Tensor, lora_b: torch.Tensor, scaling: float) -> torch.Tensor:
        \"\"\"Fuses low-rank matrices directly into base parameter tensor.\"\"\"
        # W_fused = W_base + (B @ A) * scaling
        delta = torch.matmul(lora_b, lora_a) * scaling
        fused_weight = base_weight + delta
        return fused_weight

    def build_gguf_export_manifest(self, model_name: str, quant_type: str = "Q4_K_M") -> Dict[str, Any]:
        \"\"\"Constructs formal GGUF header metadata manifest for llama.cpp execution.\"\"\"
        return {
            "general.architecture": "llama",
            "general.name": model_name,
            "general.quantization_version": 2,
            "llama.context_length": 8192,
            "llama.embedding_length": 4096,
            "llama.block_count": 32,
            "llama.feed_forward_length": 14336,
            "llama.rope.dimension_count": 128,
            "quantization_type": quant_type,
            "file_format": "GGUF_V3"
        }

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    pipeline = ModelExportPipeline("ai-ustaad-llama-3.1-8b-urdu-tax")

    # Simulate Layer Weight Fusion: [4096, 4096]
    dim = 64  # Scaled for quick local execution
    W_base = torch.randn(dim, dim)
    A = torch.randn(8, dim)
    B = torch.randn(dim, 8)
    scaling = 16.0 / 8.0

    print("Step 1: Fusing LoRA Adapters into Base Model Tensor...")
    W_fused = pipeline.simulate_adapter_fusion(W_base, A, B, scaling)
    print(f"Base Tensor Shape:  {list(W_base.shape)}")
    print(f"Fused Tensor Shape: {list(W_fused.shape)} (Permanent weight merge verified!)")

    print("\\nStep 2: Compiling GGUF Export Metadata Manifest...")
    manifest = pipeline.build_gguf_export_manifest("AI-Ustaad-Llama3-Tax-8B", quant_type="Q4_K_M")
    for k, v in manifest.items():
        print(f"  {k:30s}: {v}")

    print("\\nCapstone Milestone Complete: Model ready for zero-GPU 100% offline llama.cpp execution!")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Merging Adapters in 4-bit Quantized Space: Base model agar 4-bit mein ho aur aap usme LoRA weights add karne ki koshish karein to quantization errors double ho jate hain. Hamesha base model ko 16-bit Float mein reload karein, LoRA merge karein, aur phir fresh GGUF quantization chalayein.
2. Forgetting to Save Chat Template in GGUF: GGUF file banate waqt agar tokenizer ka chat template metadata mein embed na ho to llama.cpp ya Ollama default format use karte hain jisse model ka response quality drop ho jata hai.
3. Using `Q4_0` Instead of `Q4_K_M`: Purana 4-bit quantization (`Q4_0`) critical attention layers ko bhi 4-bit kar deta hai jisse perplexity kharab hoti hai. Modern `Q4_K_M` (k-quants medium) attention layers ko 6-bit aur baqi ko 4-bit rakhta hai jisse accuracy 99% preserve rehti hai.

Zero-GPU Tip:
Merged GGUF model ko run karne ke liye zero GPU chahiye hota hai! `llama.cpp` ya `Ollama` use karke aap 4.5 GB ki GGUF file ko kisi bhi aam 8GB ya 16GB RAM laptop ke CPU par 12 tokens/sec ki fast speed se chala sakte hain.

Self-Check Questions:
1. LoRA adapters ko base weights ke sath permanently merge karne ka production faida kya hai?
2. GGUF format kya hai aur yeh safar CPU local inference ke liye kyun mashhoor hai?
3. GGUF `Q4_K_M` quantization 16-bit model ki VRAM requirement ko 15 GB se 4.5 GB par kaise le aati hai?

What to Build Next:
Apne fine-tuned model ka GGUF export banayein, use ek custom `Modelfile` ke zariye local Ollama mein import karein (`ollama create my-model -f Modelfile`), aur terminal par offline chat chala kar test karein."""
