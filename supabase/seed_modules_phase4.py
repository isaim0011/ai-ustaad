# seed_modules_phase4.py
# Phase 4 Modules: 9, 10, 11 (18 comprehensive lessons)
# Focus: Fine-Tuning & Model Adaptation, AI Safety & Guardrails, Production AI Engineering & MLOps

def get_modules_phase4():
    return [
        # =========================================================================
        # MODULE 9: Fine-Tuning & Model Adaptation
        # =========================================================================
        {
            "phase_slug": "phase-4-production-mlops",
            "module_number": 9,
            "slug": "fine-tuning-and-model-adaptation",
            "real_world_deliverable": "Fine-Tuned Domain Reasoning LLM with Unsloth LoRA & DeepSeek-R1 GRPO",
            "zero_gpu_recipe": {
                'platform': 'Google Colab Free Tier (T4 15GB) / Kaggle Dual T4',
                'vram_required': '6-12 GB (Unsloth 4-bit QLoRA)',
                'estimated_cost': '$0.00 Free',
                'compute_units_tip': 'Unsloth 4-bit memory optimizations enable training 8B parameter models on a single free T4 GPU without OOM.',
                'one_click_command': 'pip install unsloth "xformers<0.0.27" trl peft'
            },
            "title": "Module 9: Fine-Tuning & Model Adaptation",
            "weeks_range": "Weeks 13-14",
            "estimated_hours": 16,
            "learning_outcomes": [
                "PEFT, LoRA aur QLoRA mathematics: Low-Rank decomposition, rank r, scaling factor alpha aur target projection matrices",
                "High-quality dataset curation: ChatML formatting, multi-turn packing aur token masking",
                "Fast fine-tuning with Unsloth: Triton hand-written kernels aur 2x-5x training speedups",
                "Preference alignment: Direct Preference Optimization (DPO) aur ORPO bina separate reward model ke",
                "DeepSeek-R1 style Group Relative Policy Optimization (GRPO): Self-play reasoning training",
                "Production export: Adapter merging, 16-bit float reconstruction aur GGUF / AWQ quantization"
            ],
            "practical_tasks": [
                "LoRA low-rank decomposition PyTorch custom layer se implement karein",
                "Instruction-tuning dataset ko ChatML format mein clean aur tokenize karein with padding masks",
                "Unsloth use karte hue Llama 3 / Mistral model ko 4-bit QLoRA se fine-tune karein Colab T4 par",
                "DPO trainer setup karein chosen vs rejected preference pairs par",
                "GRPO rule-based reward function likhein jo mathematical step-by-step reasoning reward kare",
                "LoRA weights ko base model mein merge karke vLLM aur llama.cpp GGUF format mein export karein"
            ],
            "resources": [
                {"title": "LoRA: Low-Rank Adaptation Paper", "url": "https://arxiv.org/abs/2106.09685"},
                {"title": "Unsloth Documentation & Notebooks", "url": "https://github.com/unslothai/unsloth"},
                {"title": "DeepSeek-R1 Technical Report & GRPO", "url": "https://arxiv.org/abs/2501.12948"},
                {"title": "Hugging Face TRL (Transformer Reinforcement Learning)", "url": "https://huggingface.co/docs/trl/index"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 9 Fine-Tuning Pipeline
  raw_data[Domain Dataset ChatML] $database -> unsloth[Unsloth Fast QLoRA] $cpu
  unsloth -> dpo[DPO / GRPO Alignment] $brain
  dpo -> merge[LoRA Weights Merge] $server
  merge -> gguf[vLLM / GGUF Export] $terminal *""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "finetuning-pro",
            "order_index": 9,
            "lessons": [
                {
                    "lesson_code": "9.1",
                    "slug": "peft-lora-qlora-foundations",
                    "title": "PEFT, LoRA & QLoRA Foundations: Low-Rank Adapters & Mathematics",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab hum kisi 8 Billion parameter model (jaise Llama-3-8B) ko poora fine-tune karne ki koshish karte hain (Full Fine-Tuning), to humein har parameter ke gradients aur Adam optimizer states (first aur second moments) store karne parte hain. Ek 8B model 16-bit floating point mein 16GB VRAM leta hai, lekin training ke waqt 60GB se 80GB VRAM mangta hai! Yeh normal developers ke budget se bahar hai.

Iska revolutionary solution **PEFT (Parameter-Efficient Fine-Tuning)** aur khusoosan **LoRA (Low-Rank Adaptation)** hai. LoRA ka fundamental insight yeh hai: model ke weight updates matrix Delta W ka intrinsic rank bohot chota (low-rank) hota hai!

Original frozen weights W (dimension d x k) ko freeze rakha jata hai, aur side par do bohot choti matrices add ki jati hain:
`Delta W = B * A`
Jahan:
- `A` matrix ka dimension `r x k` hota hai (Gaussian initialization)
- `B` matrix ka dimension `d x r` hota hai (zeros se initialize)
- `r` rank parameter hai (aam tor par 8, 16, ya 32).

Forward pass ban jata hai:
`h = W * x + (alpha / r) * (B * A * x)`

Yahan `alpha` ek scaling constant hai (jaise 16 ya 32). Agar d=4096 aur r=16 ho, to parameters 4096 x 4096 = 16,777,216 se gir kar sirf 2 x 4096 x 16 = 131,072 reh jate hain—**99.2% parameter reduction!**

**QLoRA (Quantized LoRA)** is se bhi ek qadam aage jata hai: Base model ke frozen weights ko **NF4 (NormalFloat 4-bit)** format mein compress karta hai with Double Quantization aur Paged Optimizers, jis se aap 8B model ko sirf 6GB VRAM wale GPU par train kar sakte hain!""",
                    "english_summary": "Understand Low-Rank Adaptation (LoRA) and QLoRA mathematics, parameter-efficient weight decomposition (BA), rank selection, and NF4 quantization.",
                    "code_example": """import torch
import torch.nn as nn

class LoRALinear(nn.Module):
    \"\"\"First-principles implementation of a LoRA Linear Layer.\"\"\"
    def __init__(self, in_features: int, out_features: int, rank: int = 16, alpha: float = 32.0):
        super().__init__()
        # Frozen base weight matrix
        self.base_weight = nn.Parameter(torch.randn(out_features, in_features), requires_grad=False)
        self.rank = rank
        self.scaling = alpha / rank
        
        # Trainable low-rank decomposition matrices
        # Matrix A initialized with normal distribution
        self.lora_A = nn.Parameter(torch.randn(rank, in_features) * (1.0 / rank))
        # Matrix B initialized to zero so training starts with zero delta
        self.lora_B = nn.Parameter(torch.zeros(out_features, rank))
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Base forward pass (frozen)
        base_out = torch.matmul(x, self.base_weight.t())
        # LoRA forward pass: (x @ A.T) @ B.T * scaling
        lora_out = torch.matmul(torch.matmul(x, self.lora_A.t()), self.lora_B.t()) * self.scaling
        return base_out + lora_out

# Test layer dimensions
layer = LoRALinear(in_features=4096, out_features=4096, rank=16)
x = torch.randn(2, 4096)
output = layer(x)
print("Output shape:", output.shape)
trainable_params = sum(p.numel() for p in layer.parameters() if p.requires_grad)
frozen_params = sum(p.numel() for p in layer.parameters() if not p.requires_grad)
print(f"Trainable (LoRA): {trainable_params:,} | Frozen: {frozen_params:,}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: LoRA Low-Rank Forward Pass
  input[Input Vector x] $terminal -> base[Frozen Base Weight W d x k] $database
  input -> lora_a[LoRA Matrix A r x k] $cpu
  lora_a -> lora_b[LoRA Matrix B d x r] $cpu
  lora_b -> scale[Scaling Alpha / r] $layers
  base -> add[Element-wise Sum (+)] $code
  scale -> add
  add -> output[Output Activation h] $server *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Hugging Face PEFT Library", "url": "https://huggingface.co/docs/peft/index"},
                        {"title": "QLoRA: Efficient Finetuning of Quantized LLMs", "url": "https://arxiv.org/abs/2305.14314"}
                    ],
                    "xp_reward": 25,
                    "order_index": 1
                },
                {
                    "lesson_code": "9.2",
                    "slug": "dataset-curation-chatml-packing",
                    "title": "Dataset Curation & ChatML Formatting: Tokenization Packing & Masks",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, fine-tuning mein "Garbage In, Garbage Out" ka qanoon 100% sach hai! Agar aap 10,000 low-quality samples train karenge to model confuse ho jayega, lekin agar aap 1,000 pristine, carefully structured examples train karenge to model domain master ban jayega.

Modern fine-tuning ka industry standard format **ChatML** ya standard roles format hai (`system`, `user`, `assistant`). Har conversation ko specific special tokens mein wrap kiya jata hai:
`<|im_start|>system\\nAap AI Ustaad ke medical assistant hain.<|im_end|>\\n<|im_start|>user\\nSirf sar dard hai.<|im_end|>\\n<|im_start|>assistant\\n...<|im_end|>`

Training ke waqt do critical techniques use hoti hain:
1. **Loss Masking (Prompt Masking)**: Model ko user ke prompt aur system prompt predict karne par penalize nahi kiya jata! Loss sirf aur sirf assistant ke response tokens par calculate hoti hai. PyTorch mein non-target tokens ka label `-100` set kiya jata hai (CrossEntropyLoss default ignore_index).
2. **Sample Packing (Sequence Packing)**: Agar aapka max context length 2048 hai aur aapke conversations 200-300 tokens ke hain, to padding tokens (`<pad>`) add karne se 70% GPU compute waste hota hai! Packing technique mein multiple conversations ko ek single 2048 sequence mein pack kar diya jata hai using attention masking.""",
                    "english_summary": "Structure training datasets into standardized ChatML format, apply loss masking with -100 labels on prompt tokens, and utilize sequence packing to eliminate wasted padding compute.",
                    "code_example": """from typing import List, Dict
import json

def format_chatml_example(system_prompt: str, conversations: List[Dict[str, str]]) -> str:
    \"\"\"Converts structured multi-turn conversation into ChatML formatted string.\"\"\"
    formatted = f"<|im_start|>system\\n{system_prompt}<|im_end|>\\n"
    for turn in conversations:
        role = turn["role"] # 'user' or 'assistant'
        content = turn["content"]
        formatted += f"<|im_start|>{role}\\n{content}<|im_end|>\\n"
    return formatted

# Example dataset record
record = {
    "system": "Aap AI Ustaad ke expert Python aur AI mentor hain jo Roman Urdu mein samjhate hain.",
    "conversations": [
        {"role": "user", "content": "PyTorch mein requires_grad=True ka kya maqsad hai?"},
        {"role": "assistant", "content": "So guys, jab aap requires_grad=True set karte hain, to PyTorch autograd engine ko batata hai ke is tensor par hone wale tamam mathematical operations ka computation graph track kare taake backward() call par gradients calculate ho sakein."}
    ]
}

chatml_text = format_chatml_example(record["system"], record["conversations"])
print(chatml_text)""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Sequence Packing in Context Window
  s1[Sample 1: 300 Tokens] $terminal -> pack[Packed 2048 Tensor] $cpu
  s2[Sample 2: 500 Tokens] $terminal -> pack
  s3[Sample 3: 800 Tokens] $terminal -> pack
  pack -> mask[Block-Diagonal Attention Mask] $database
  mask -> loss[Target Loss Masking: Only Assistant Labels] $brain *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Hugging Face Chat Template Documentation", "url": "https://huggingface.co/docs/transformers/main/en/chat_templating"},
                        {"title": "OpenAI ChatML Specification", "url": "https://github.com/openai/openai-python/blob/main/chatml.md"}
                    ],
                    "xp_reward": 25,
                    "order_index": 2
                },
                {
                    "lesson_code": "9.3",
                    "slug": "unsloth-fast-finetuning",
                    "title": "Fast 4-bit Fine-Tuning with Unsloth: Triton Kernels & FlashAttention",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, standard Hugging Face PEFT library se jab aap LoRA train karte hain to Python overhead aur unoptimized PyTorch autograd kernels ki wajah se training slow hoti hai aur VRAM spikes aate hain.

**Unsloth** ek open-source framework hai jo fine-tuning ko **2x se 5x fast** karta hai aur VRAM usage ko **70% reduce** karta hai!
Unsloth yeh miracle kaise karta hai?
1. **Manual Triton GPU Kernels**: RoPE (Rotary Position Embeddings), Cross-Entropy Loss, aur MLP Activations (SwiGLU) ke liye PyTorch C++ kernels ki jagah custom OpenAI Triton kernels likhe gaye hain jo memory reads/writes minimize karte hain.
2. **Gradient Checkpointing Optimization**: Backward pass ke doran intermediate activations ko intelligently discard aur recompute karta hai bina VRAM explode kiye.
3. **Native 4-bit Quantization**: BitsAndBytes ke muqable mein zero accuracy loss ke sath direct 4-bit linear projection kernels provide karta hai.

Iska sab se bara faida: Aap Google Colab ke 100% free T4 GPU (15GB VRAM) par **Llama 3.1 8B**, **Mistral 7B**, ya **Phi-4** ko aasaani se fine-tune kar sakte hain!""",
                    "english_summary": "Leverage Unsloth's hand-written OpenAI Triton kernels and optimized backpropagation to achieve 5x faster fine-tuning on free-tier consumer GPUs with 70% less VRAM.",
                    "code_example": """# Unsloth Fast Fine-Tuning Recipe (Runs seamlessly on Colab T4)
from unsloth import FastLanguageModel
import torch
from trl import SFTTrainer
from transformers import TrainingArguments

max_seq_length = 2048
dtype = None # Auto detection (Float16 for T4, Bfloat16 for Ampere+)
load_in_4bit = True # 4-bit QLoRA

# 1. Load Model & Tokenizer with Unsloth optimizations
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Meta-Llama-3.1-8B-Instruct",
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
)

# 2. Add LoRA Adapters to Attention & MLP projection matrices
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0, # Unsloth supports 0 dropout for optimized kernels
    bias="none",
    use_gradient_checkpointing="unsloth",
    random_state=3407,
)

print("Model successfully patched with Unsloth Triton kernels!")""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Unsloth Memory Architecture
  gpu_ram[15GB T4 VRAM] $database -> q4[NF4 Base Model 5.5GB] $layers
  gpu_ram -> lora[LoRA Adapters 0.2GB] $cpu
  gpu_ram -> triton[Custom Triton Kernels 2.5GB] $server *
  gpu_ram -> free[Free Headroom 6.8GB] $chart""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "Unsloth GitHub Repository", "url": "https://github.com/unslothai/unsloth"},
                        {"title": "OpenAI Triton Programming Guide", "url": "https://triton-lang.org/main/index.html"}
                    ],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "9.4",
                    "slug": "dpo-orpo-alignment",
                    "title": "Preference Alignment: Direct Preference Optimization (DPO) & ORPO",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, SFT (Supervised Fine-Tuning) se model text generate karna seekh jata hai, lekin model ko user ki preferences ke mutabiq align karna (helpful, harmless, accurate banana) SFT se mushkil hota hai.

Pehle iske liye **RLHF (Reinforcement Learning from Human Feedback)** use hota tha:
1. Ek alag **Reward Model** train kiya jata tha.
2. PPO (Proximal Policy Optimization) algorithm se policy update ki jati thi.
Lekin PPO bohot unstable tha, 4 models aik sath memory mein load karne parte the (Actor, Critic, Reference, Reward Model), aur training crash ho jati thi!

2023 mein Stanford researchers ne **DPO (Direct Preference Optimization)** introduce kiya.
DPO ka mathematical breakthrough: **Reward model ki zaroorat hi khatam kar di!**
DPO seedha policy model ki probabilities aur reference model ki probabilities ka ratio lekar closed-form mathematical derivation se loss compute karta hai:
`L_DPO = - E [ log sigma ( beta * log( pi(y_w | x) / pi_ref(y_w | x) ) - beta * log( pi(y_l | x) / pi_ref(y_l | x) ) ) ]`

Jahan:
- `y_w` = Chosen (winning/behtar) response
- `y_l` = Rejected (losing/kharab) response
- `beta` = KL divergence penalty scaling factor (aam tor par 0.1)

Model chosen response ki probability ko barhata hai aur rejected response ki probability ko exponentially drop karta hai!""",
                    "english_summary": "Master Direct Preference Optimization (DPO) and ORPO to align LLMs directly on pairwise chosen vs rejected completions without unstable reward models or PPO.",
                    "code_example": """from trl import DPOTrainer, DPOConfig
from datasets import Dataset

# Sample preference alignment dataset
preference_data = {
    "prompt": [
        "Python mein memory leak kaise debug karein?",
    ],
    "chosen": [
        "Memory leaks debug karne ke liye `tracemalloc` standard library use karein, snapshots compare karein aur circular references check karein objgraph ke sath.",
    ],
    "rejected": [
        "Memory leak koi masla nahi hota, bas computer restart kar dein ya RAM barha lein.",
    ]
}

dataset = Dataset.from_dict(preference_data)

dpo_config = DPOConfig(
    beta=0.1, # KL penalty strength
    learning_rate=5e-6,
    batch_size=2,
    gradient_accumulation_steps=4,
    max_prompt_length=512,
    max_length=1024,
    output_dir="./dpo_aligned_model"
)

print("DPO Configuration ready for preference alignment!")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Direct Preference Optimization (DPO)
  prompt[User Prompt x] $terminal -> model[Policy Model pi_theta] $cpu
  prompt -> ref[Frozen Ref Model pi_ref] $database
  model -> log_ratio[Log Probability Ratio Win vs Loss] $brain
  ref -> log_ratio
  log_ratio -> loss[DPO Loss: Boost y_w & Suppress y_l] $layers *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Direct Preference Optimization Paper (Rafailov et al.)", "url": "https://arxiv.org/abs/2305.18290"},
                        {"title": "TRL DPOTrainer Documentation", "url": "https://huggingface.co/docs/trl/dpo_trainer"}
                    ],
                    "xp_reward": 25,
                    "order_index": 4
                },
                {
                    "lesson_code": "9.5",
                    "slug": "deepseek-r1-grpo-training",
                    "title": "DeepSeek-R1 GRPO: Reasoning Chains & Value-Model-Free RL",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, January 2025 mein DeepSeek ne AI ki duniya ko hila kar rakh diya jab unhone **DeepSeek-R1** release kiya, jo OpenAI ke o1 ke barabar mathematical reasoning karta hai lekin 10x kam cost par!

DeepSeek-R1 ki sab se bari technical innovation **GRPO (Group Relative Policy Optimization)** hai.
PPO mein ek bara "Critic" ya "Value Model" chahiye hota hai jo har token ka value predict karta hai. GRPO ne Critic ko **mukammal tor par delete** kar diya!

GRPO kaise kaam karta hai?
1. Har prompt `q` ke liye, current model `G` different responses generate karta hai (jaise G=4 ya G=8 candidate reasoning chains).
2. Har response ko ek deterministic rule-based reward function score karta hai (maslan: kya final answer bracket `<answer>...</answer>` mein durust hai? Kya reasoning steps valid hain?). Scores: `r_1, r_2, ..., r_G`.
3. In `G` scores ka mean aur standard deviation compute kiya jata hai:
   `A_i = (r_i - mean(r)) / std(r)`
   Ise **Group Relative Advantage** kehte hain!
4. Agar kisi response ka score group ke average se behtar hai, to model us reasoning trajectory ko reinforce karta hai; agar group se bura hai to suppress karta hai!

Nateeja? Model bina kisi human supervision ke khud se long "Chain of Thought" (Aha! moments, self-correction, verification) develop kar leta hai!""",
                    "english_summary": "Understand DeepSeek-R1's Group Relative Policy Optimization (GRPO), eliminating the PPO Critic model by computing group relative advantages across sampled candidate reasoning trajectories.",
                    "code_example": """import torch
from typing import List

def compute_grpo_advantages(rewards: List[float], epsilon: float = 1e-8) -> torch.Tensor:
    \"\"\"Calculates Group Relative Advantage across G sampled completions (DeepSeek-R1 style).\"\"\"
    r = torch.tensor(rewards, dtype=torch.float32)
    mean = r.mean()
    std = r.std(unbiased=False)
    # Normalized relative advantage within the sampled group
    advantages = (r - mean) / (std + epsilon)
    return advantages

# Example: 4 sampled outputs for a math problem
# Output 1 got correct answer (1.0), Output 2 partial (0.5), Output 3 wrong (0.0), Output 4 wrong (0.0)
rewards = [1.0, 0.5, 0.0, 0.0]
advantages = compute_grpo_advantages(rewards)

for i, (rew, adv) in enumerate(zip(rewards, advantages)):
    status = "REINFORCE (+)" if adv > 0 else "PENALIZE (-)"
    print(f"Sample {i+1}: Reward = {rew:.2f} | Advantage = {adv.item():+.3f} -> {status}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: DeepSeek-R1 GRPO Architecture
  prompt[Math / Logic Prompt q] $terminal -> gen[Generate G=4 Reasoning Chains] $cpu
  gen -> r1[Trajectory 1: Score 1.0] $code
  gen -> r2[Trajectory 2: Score 0.5] $code
  gen -> r3[Trajectory 3: Score 0.0] $code
  gen -> r4[Trajectory 4: Score 0.0] $code
  r1 & r2 & r3 & r4 -> grpo[GRPO Advantage: (r - mean) / std] $brain *
  grpo -> update[Policy Gradient Update with KL Bound] $server""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "DeepSeek-R1: Incentivizing Reasoning Capability via RL", "url": "https://arxiv.org/abs/2501.12948"},
                        {"title": "Hugging Face TRL GRPOTrainer", "url": "https://huggingface.co/docs/trl/main/en/grpo_trainer"}
                    ],
                    "xp_reward": 30,
                    "order_index": 5
                },
                {
                    "lesson_code": "9.6",
                    "slug": "capstone-fine-tune-domain-model",
                    "title": "Module 9 Capstone: Fine-Tune Domain LLM, Adapter Merge & GGUF Export",
                    "duration_minutes": 50,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, mubarak ho! Aap Module 9 ke Capstone project par pohanch chuke hain. Is capstone mein aap ek specialized domain-specific reasoning model train karenge aur use production inference ke liye packaging karenge!

Aapka Capstone Mission:
1. **Dataset Preparation**: Ek specialized domain (jaise Urdu/English Medical Triage ya Legal Contract Analysis) ka 1,000+ samples ka ChatML dataset curate aur validate karein.
2. **Unsloth QLoRA Training**: Llama 3.1 8B ko Unsloth mein 4-bit load karke LoRA rank r=16, alpha=32 par 3 epochs train karein. Training loss curve observe karein aur evaluate karein ke loss converge ho rahi hai.
3. **Weight Merging**: LoRA adapters ko base 16-bit model weights mein merge karein (`model.merge_and_unload()`).
4. **Quantization & Export**:
   - Model ko 16-bit safetensors format mein save karein vLLM high-throughput serving ke liye.
   - Model ko **GGUF Q4_K_M** aur **Q8_0** format mein quantize karein taake laptop ya edge device par offline run ho sake!
5. **Validation Benchmark**: Base model vs fine-tuned model ke answers compare karein aur domain accuracy gain document karein.""",
                    "english_summary": "Execute the Module 9 Capstone: fine-tune a domain model with Unsloth, merge LoRA adapters into base weights, and export to GGUF and safetensors formats for production serving.",
                    "code_example": """# Capstone LoRA Merge & GGUF Export Script
from unsloth import FastLanguageModel

# 1. Load trained model with adapters
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="./lora_model",
    max_seq_length=2048,
    load_in_4bit=False, # Load in 16-bit for clean weight merging
)

# 2. Save merged 16-bit model for vLLM production serving
print("Merging LoRA adapters into base weights...")
model.save_pretrained_merged("finetuned_domain_model_16bit", tokenizer, save_method="merged_16bit")
print("16-bit model saved for vLLM deployment!")

# 3. Export directly to GGUF format for local llama.cpp / Ollama execution
print("Exporting to GGUF Q4_K_M...")
model.save_pretrained_gguf("finetuned_domain_model_gguf", tokenizer, quantization_method="q4_k_m")
print("GGUF export complete! Ready for local and serverless deployment.")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Capstone Fine-Tuning & Export Lifecycle
  dataset[Domain Dataset ChatML] $database -> train[Unsloth 4-bit LoRA Training] $cpu
  train -> eval[Validation & Loss Convergence] $chart
  eval -> merge[Merge Adapters to Base 16-bit] $server *
  merge -> vllm[vLLM High-Throughput SafeTensors] $cloud
  merge -> gguf[Local Edge GGUF Q4_K_M] $terminal""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Unsloth Saving & Exporting Guide", "url": "https://docs.unsloth.ai/basics/saving-and-exporting"},
                        {"title": "llama.cpp GGUF Quantization Formats", "url": "https://github.com/ggerganov/llama.cpp"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        },

        # =========================================================================
        # MODULE 10: AI Safety, Evals & Guardrails
        # =========================================================================
        {
            "phase_slug": "phase-4-production-mlops",
            "module_number": 10,
            "slug": "ai-safety-evals-and-guardrails",
            "real_world_deliverable": "Enterprise Safety Firewall & Multi-Layer Guardrail Gateway with PII Redaction",
            "zero_gpu_recipe": {
                'platform': 'Local CPU / Render / Fly.io Free Tier',
                'vram_required': '0 GB (CPU)',
                'estimated_cost': '$0.00 Free',
                'compute_units_tip': 'Microsoft Presidio, NeMo Guardrails, and Ragas evaluation runs efficiently on multi-core standard CPUs.',
                'one_click_command': 'pip install presidio-analyzer presidio-anonymizer ragas nemoguardrails deepeval'
            },
            "title": "Module 10: AI Safety, Evals & Guardrails",
            "weeks_range": "Weeks 14-15",
            "estimated_hours": 14,
            "learning_outcomes": [
                "Systematic LLM evaluation metrics: The Ragas Triad (Faithfulness, Answer Relevance, Context Precision)",
                "Programmable runtime guardrails using NeMo Guardrails aur Colang 2.0",
                "Automated PII detection aur irreversible data anonymization with Microsoft Presidio",
                "Hallucination detection engines and groundedness score thresholds using TruLens",
                "Automated CI/CD evaluation test gates and regression prevention with DeepEval",
                "Multi-layer enterprise safety architecture: Input rails, dialog rails aur output rails"
            ],
            "practical_tasks": [
                "Ragas evaluation pipeline build karein jo RAG responses ko 0-1 scale par mathematically score kare",
                "NeMo Guardrails flow define karein jo competitor mentions aur prompt injection block kare",
                "Presidio pipeline configure karein jo CNIC, credit card aur phone numbers redact kare",
                "TruLens Feedback Functions setup karein for groundedness and toxic sentiment detection",
                "GitHub Actions workflow likhein jo PR merge hone se pehle DeepEval evaluation suite run kare"
            ],
            "resources": [
                {"title": "Ragas: Automated Evaluation for RAG", "url": "https://docs.ragas.io/en/stable/"},
                {"title": "NeMo Guardrails Documentation", "url": "https://docs.nvidia.com/nemo/guardrails/latest/index.html"},
                {"title": "Microsoft Presidio PII Protection", "url": "https://microsoft.github.io/presidio/"},
                {"title": "DeepEval LLM Evaluation Framework", "url": "https://docs.confident-ai.com/"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 10 Enterprise Safety Architecture
  user_input[User Prompt] $browser -> presidio[Presidio PII Redactor] $lock
  presidio -> nemo_in[NeMo Input Guardrail] $shield
  nemo_in -> llm[LLM / RAG Engine] $cpu
  llm -> nemo_out[NeMo Output Rail & Hallucination Check] $shield
  nemo_out -> sanitized[Sanitized Safe Output] $server *""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "production-ready",
            "order_index": 10,
            "lessons": [
                {
                    "lesson_code": "10.1",
                    "slug": "ragas-triad-llm-evals",
                    "title": "LLM Evaluation Frameworks: The Ragas Triad (Faithfulness & Relevance)",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab aap production mein LLM ya RAG application deploy karte hain, to aap manual "vibe check" (kuch queries type karke dekhna) par bharosa nahi kar sakte! Production engineering ka asool hai: **"If you cannot measure it, you cannot improve it."**

RAG systems ko evaluate karne ka gold standard **Ragas Triad** hai:
1. **Faithfulness (Haqeeqat-Pasandi)**: Kya generated answer mukammal tor par retrieved context par mabni hai ya model ne bahar se jhoot bola hai? High faithfulness = Zero Hallucination!
2. **Answer Relevance**: Kya model ka answer user ke ahem sawaal ka direct jawab deta hai ya idhar udhar ki ghuma-phira kar baatein karta hai?
3. **Context Precision & Recall**: Kya vector database ne exact relevant chunks retrieve kiye the ya kachra context bheja tha?

Ragas framework LLM-as-a-judge paradigm use karta hai jahan ek high-reasoning model (jaise Claude 3.5 ya GPT-4o) structured prompts se har dimension par 0.0 se 1.0 ke darmiyan mathematical score assign karta hai.""",
                    "english_summary": "Implement quantitative RAG evaluation using the Ragas Triad to calculate mathematical metrics for Faithfulness, Answer Relevance, and Context Precision.",
                    "code_example": """from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevance, context_precision
from datasets import Dataset

# Sample evaluation dataset representing RAG pipeline test run
data_samples = {
    "question": ["AI Ustaad ka primary mission kya hai?"],
    "contexts": [["AI Ustaad Pakistan aur South Asia ka pehla zero-to-hero Roman Urdu AI Engineering curriculum hai jo production-grade skills sikhata hai."]],
    "answer": ["AI Ustaad ka maqsad Pakistan mein Roman Urdu ke zariye production-grade AI engineering sikhana hai."],
    "ground_truth": ["AI Ustaad Pakistan ka premier Roman Urdu AI platform hai."]
}

dataset = Dataset.from_dict(data_samples)

# Evaluate using the Ragas Triad metrics
results = evaluate(
    dataset=dataset,
    metrics=[faithfulness, answer_relevance, context_precision]
)

print("Ragas Evaluation Scores:")
print(f"Faithfulness: {results['faithfulness']:.3f}")
print(f"Answer Relevance: {results['answer_relevance']:.3f}")
print(f"Context Precision: {results['context_precision']:.3f}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: The Ragas Evaluation Triad
  query[User Query] $terminal -> ctx[Retrieved Context] $database
  ctx -> ans[Generated Answer] $cpu
  ctx & ans -> f_score[Faithfulness Metric: Context -> Answer Grounding] $brain
  query & ans -> r_score[Answer Relevance Metric: Query -> Answer Match] $brain
  query & ctx -> p_score[Context Precision: Query -> Context Quality] $brain *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Ragas Metrics Deep Dive", "url": "https://docs.ragas.io/en/stable/concepts/metrics/index.html"},
                        {"title": "Evaluating RAG Applications with TruLens", "url": "https://www.trulens.org/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 1
                },
                {
                    "lesson_code": "10.2",
                    "slug": "nemo-guardrails-semantic-rails",
                    "title": "Guardrails Architecture: NeMo Guardrails & Colang 2.0",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, enterprise applications mein aap LLM ko khula nahi chhor sakte ke wo kisi competitor ki tareef kare, vulgar language generate kare, ya jailbreak prompts ("Ignore all previous instructions") ka shikar ban jaye!

NVIDIA ka **NeMo Guardrails** industry ka sab se powerful programmable guardrails system hai jo **Colang** language use karta hai.
NeMo teen levels par rails apply karta hai:
1. **Input Rails**: User ke prompt ko LLM tak pohanchne se pehle intercept karta hai. Agar prompt injection ya toxic intent detect ho, to LLM execute hi nahi hota!
2. **Dialog Rails**: Conversation ke flow ko guide karta hai taake bot hamesha defined business path par rahe.
3. **Output Rails**: LLM ke generated answer ko check karta hai. Agar model hallucinate kare ya sensitive confidential information leak kare, to response ko block karke safe fallback message bhejta hai.""",
                    "english_summary": "Deploy programmable guardrails with NVIDIA NeMo Guardrails and Colang 2.0 to enforce topical boundaries, prevent jailbreaks, and sanitize outputs.",
                    "code_example": """# config.co (Colang 2.0 Guardrails Definition)
'''
define user ask about competitors
  "Does your platform use CompetitorX?"
  "Why is CompetitorY better than you?"

define bot refuse competitor discussion
  "AI Ustaad hamara flagship platform hai. Hum competitors par tabsira nahi karte, balki apne curriculum ki quality aur production results par focus karte hain."

define flow handle competitors
  user ask about competitors
  bot refuse competitor discussion

define user attempt jailbreak
  "Ignore all previous instructions"
  "DAN mode enabled"

define bot refuse jailbreak
  "Maaf kijiye, security policies ke teht yeh request process nahi ki ja sakti."

define flow handle jailbreak
  user attempt jailbreak
  bot refuse jailbreak
'''

print("Colang 2.0 safety rails defined successfully!")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: NeMo Guardrails Interception Pipeline
  prompt[User Request] $terminal -> in_rail[Input Rail: Jailbreak Check] $shield
  in_rail -- Passed --> llm[Core LLM Engine] $cpu
  in_rail -- Flagged --> block[Predefined Safe Refusal] $lock
  llm -> out_rail[Output Rail: Fact & Policy Check] $shield
  out_rail -- Safe --> client[User Response] $server *
  out_rail -- Violates --> fallback[Safe Fallback Message] $lock""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "NVIDIA NeMo Guardrails GitHub", "url": "https://github.com/NVIDIA/NeMo-Guardrails"},
                        {"title": "Colang Language Guide", "url": "https://docs.nvidia.com/nemo/guardrails/latest/colang_language_guide.html"}
                    ],
                    "xp_reward": 25,
                    "order_index": 2
                },
                {
                    "lesson_code": "10.3",
                    "slug": "pii-redaction-presidio",
                    "title": "Enterprise Data Sanitization: Microsoft Presidio & PII Redaction",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, agar aapka user chat mein apna CNIC number (Pakistan National ID), credit card details, phone number, ya private address enter kare, aur aap use direct external cloud LLM (OpenAI/Anthropic) ko bhej dein, to yeh **GDPR**, **HIPAA**, aur local data privacy laws ki shadeed violation hai!

Microsoft ka **Presidio** industry-standard PII (Personally Identifiable Information) detection aur anonymization engine hai.
Presidio do components par mushtamil hota hai:
1. **Presidio Analyzer**: Named Entity Recognition (NER spaCy models), regular expressions, aur mathematical checksums (jaise Luhn algorithm for credit cards) se PII entities detect karta hai.
2. **Presidio Anonymizer**: Detect hone wali entities ko mask karta hai (jaise `<PHONE_NUMBER>`, `<CNIC>`, ya sha-256 hash se replace karna).

Jab LLM response generate kar leta hai, to aap **Deanonymizer** ke zariye original values restore kar sakte hain, ya LLM ko hamesha sanitized data par hi operate karne dete hain.""",
                    "english_summary": "Sanitize and anonymize sensitive PII (CNIC, credit cards, emails, phone numbers) before cloud transmission using Microsoft Presidio Analyzer and Anonymizer.",
                    "code_example": """from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine

# 1. Initialize Presidio Engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# 2. Add custom Pakistani CNIC Recognizer (Format: 42101-1234567-1)
cnic_pattern = Pattern(name="pakistani_cnic_pattern", regex=r"\\b\\d{5}-\\d{7}-\\d{1}\\b", score=0.95)
cnic_recognizer = PatternRecognizer(supported_entity="PAK_CNIC", patterns=[cnic_pattern])
analyzer.registry.add_recognizer(cnic_recognizer)

# 3. Analyze raw incoming text
raw_text = "Salam, mera naam Ahmad hai, CNIC 42101-1234567-1 aur email ahmad@example.com hai."
results = analyzer.analyze(text=raw_text, entities=["PAK_CNIC", "EMAIL_ADDRESS", "PERSON"], language="en")

# 4. Anonymize sensitive entities
anonymized_result = anonymizer.anonymize(text=raw_text, analyzer_results=results)

print("Original:", raw_text)
print("Sanitized for LLM:", anonymized_result.text)""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Presidio PII Redaction Architecture
  user_raw[Raw Text with PII] $terminal -> analyzer[Presidio Analyzer: NER & Regex] $database
  analyzer -> entities[Detected Entities: CNIC, Email, Phone] $layers
  entities -> anon[Presidio Anonymizer: Mask / Hash] $lock *
  anon -> clean_text[Clean Redacted Text] $server
  clean_text -> cloud_llm[External Cloud LLM Provider] $cloud""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Microsoft Presidio Documentation", "url": "https://microsoft.github.io/presidio/"},
                        {"title": "Presidio PatternRecognizer Guide", "url": "https://microsoft.github.io/presidio/analyzer/customizing_nlp_models/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "10.4",
                    "slug": "hallucination-detection-trulens",
                    "title": "Real-Time Hallucination Detection & Groundedness with TruLens",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, RAG system mein sab se khatarnak cheez "Confident Hallucination" hoti hai—jahan model aisi baat pooray yaqeen ke sath likhta hai jo retrieved documents mein mojood hi nahi hoti!

Is challenge ko real-time production inference ke doran pakadne ke liye **TruLens** aur **Groundedness Verification** algorithms use kiye jate hain.
Groundedness verification ka mechanism yeh hai:
1. Model ke generated response ko atomic claims ya sentences mein split kiya jata hai (Sentence Tokenization).
2. Har claim ke liye retrieved context ke sath NLI (Natural Language Inference) entailment score calculate kiya jata hai:
   - **Entailment**: Claim context se logically sabit hota hai (Score 1.0)
   - **Neutral**: Context mein is claim ka zikr nahi hai (Score 0.5)
   - **Contradiction**: Claim context ke khilaf hai (Score 0.0)
3. Agar average Groundedness score defined threshold (maslan 0.80) se kam aye, to response ko foran suppress karke verified disclaimer ke sath fallback serve kiya jata hai!""",
                    "english_summary": "Deconstruct LLM responses into atomic propositional claims to compute real-time Natural Language Inference (NLI) Groundedness scores with TruLens.",
                    "code_example": """from typing import List, Dict

def verify_groundedness_claims(claims: List[str], context: str) -> Dict[str, any]:
    \"\"\"Mock NLI Groundedness evaluator verifying claims against retrieved context.\"\"\"
    verified_claims = []
    hallucinated_claims = []
    
    for claim in claims:
        # In production: Cross-Encoder NLI model (deberta-v3) computes entailment probability
        # Simplified token overlap heuristic for demonstration:
        words = [w.lower() for w in claim.split() if len(w) > 3]
        match_count = sum(1 for w in words if w in context.lower())
        overlap_ratio = match_count / max(len(words), 1)
        
        if overlap_ratio >= 0.6:
            verified_claims.append(claim)
        else:
            hallucinated_claims.append(claim)
            
    score = len(verified_claims) / max(len(claims), 1)
    return {
        "groundedness_score": score,
        "is_safe": score >= 0.75,
        "verified": verified_claims,
        "hallucinated": hallucinated_claims
    }

ctx = "AI Ustaad platform par 14 modules hain aur yeh Roman Urdu mein parhaya jata hai."
claims = [
    "AI Ustaad platform par 14 modules hain.",
    "AI Ustaad har student ko free Tesla car deta hai."
]

audit = verify_groundedness_claims(claims, ctx)
print(f"Groundedness Score: {audit['groundedness_score']:.2f} | Safe to deliver: {audit['is_safe']}")
print(f"Hallucinated flags: {audit['hallucinated']}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Real-Time Groundedness Verification
  resp[Generated LLM Response] $terminal -> split[Sentence / Claim Splitter] $layers
  split -> c1[Claim 1: 14 Modules] $code
  split -> c2[Claim 2: Free Tesla] $code
  c1 & c2 -> nli[NLI Entailment vs Context] $brain
  nli -> score[Groundedness Score: 0.50] $chart *
  score -- Below 0.80 --> block[Block & Alert User: High Hallucination Risk] $lock""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "TruLens Groundedness Evaluation", "url": "https://www.trulens.org/trulens_eval/groundedness/"},
                        {"title": "Hugging Face DeBERTa NLI Model", "url": "https://huggingface.co/cross-encoder/nli-deberta-v3-base"}
                    ],
                    "xp_reward": 25,
                    "order_index": 4
                },
                {
                    "lesson_code": "10.5",
                    "slug": "automated-eval-cicd-deepeval",
                    "title": "Automated CI/CD Evaluation Gates & Regression Testing with DeepEval",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab software development mein hum naya code likhte hain to unit tests (pytest / jest) chala kar check karte hain ke purana feature break to nahi hua. Lekin AI engineering mein jab aap prompt change karte hain, embedding model update karte hain, ya chunking size badalte hain, to aapko kaise pata chalega ke overall accuracy improve hui ya degrade?

Iska solution **Automated CI/CD Evaluation Gates** hai using **DeepEval**!
Har Pull Request (PR) par GitHub Actions workflow trigger hota hai:
1. Predefined "Golden Test Dataset" (maslan 100 hard real-world questions with verified answers) run hota hai.
2. DeepEval har test case par G-Eval metrics (Hallucination Metric, Answer Relevance Metric, Bias Metric) evaluate karta hai.
3. Agar average score benchmark threshold (maslan 0.85) se drop ho jaye, to **CI build fail ho jati hai aur PR merge block ho jata hai!**

Is se aapki production app silent quality regression se hamesha mehfooz rehti hai.""",
                    "english_summary": "Configure continuous integration evaluation pipelines with DeepEval and GitHub Actions to enforce strict test gates and prevent accuracy regressions before deployment.",
                    "code_example": """# test_rag_quality.py (DeepEval Pytest Suite)
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric

def test_rag_faithfulness():
    # Construct test case from current staging pipeline
    test_case = LLMTestCase(
        input="Pakistan ka capital shehar konsa hai?",
        actual_output="Pakistan ka dar-ul-hukumat Islamabad hai.",
        context=["Islamabad Pakistan ka official capital shehar hai."]
    )
    
    # Define metrics with strict production thresholds
    relevancy_metric = AnswerRelevancyMetric(threshold=0.8)
    hallucination_metric = HallucinationMetric(threshold=0.2) # Max 20% hallucination allowed
    
    # Assert will fail pytest if thresholds are violated
    assert_test(test_case, [relevancy_metric, hallucination_metric])

print("DeepEval CI/CD test case validated for automated pipeline execution!")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: GitHub Actions AI Evaluation Gate
  git_push[Git Push / PR] $terminal -> gh_action[GitHub Actions Runner] $server
  gh_action -> run_suite[DeepEval Golden Test Suite: 100 Cases] $database
  run_suite -> metrics[Compute Aggregate Scores] $chart
  metrics -- Score >= 0.85 --> pass[Green Gate: Auto-Merge Allowed] $server *
  metrics -- Score < 0.85 --> fail[Red Gate: PR Blocked & Slack Alert] $lock""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "DeepEval GitHub Actions CI/CD Integration", "url": "https://docs.confident-ai.com/docs/integrations-github-actions"},
                        {"title": "Continuous Integration for LLM Applications", "url": "https://martinfowler.com/articles/cd4ml.html"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "10.6",
                    "slug": "capstone-enterprise-safety-firewall",
                    "title": "Module 10 Capstone: Enterprise Safety Firewall & Multi-Layer Gateway",
                    "duration_minutes": 50,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, congratulations! Aap Module 10 ke Capstone par pohanch chuke hain. Is capstone mein aap ek complete, production-grade **Enterprise AI Safety Firewall** build karenge jo raw user prompts aur LLM responses ke beech bulletproof shield ka kaam karega!

Aapka Capstone Architecture:
1. **Presidio PII Interceptor**: Incoming prompt se Pakistani CNIC, Credit Card, Email aur Phone numbers ko detect aur redact karega.
2. **NeMo Topical & Jailbreak Rails**: Jailbreak attempts ("DAN mode", "Ignore instructions") aur competitor comparisons ko instant block karega.
3. **NLI Groundedness Checker**: LLM ke generated answer ke har sentence ko context ke sath cross-check karega; agar groundedness score < 0.80 ho to disclaimer inject karega.
4. **Structured Audit Logging**: Har request ka safety status, redacted fields count, aur evaluation scores structured JSON format mein log karega for compliance.
5. **FastAPI Firewall Gateway**: In tamam layers ko ek high-performance async API endpoint mein package karein.""",
                    "english_summary": "Architect and deploy the Module 10 Capstone: a multi-layered Enterprise AI Safety Firewall integrating Presidio PII redaction, NeMo Guardrails, and NLI Groundedness checks.",
                    "code_example": """import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="AI Ustaad Enterprise Safety Gateway")

class PromptRequest(BaseModel):
    query: str
    user_id: str

class SafeResponse(BaseModel):
    is_safe: bool
    sanitized_query: str
    response: str
    safety_flags: List[str]

@app.post("/api/v1/secure-chat", response_model=SafeResponse)
async def secure_chat_endpoint(req: PromptRequest):
    flags = []
    
    # 1. Jailbreak Check
    jailbreak_keywords = ["ignore previous", "dan mode", "jailbreak"]
    if any(k in req.query.lower() for k in jailbreak_keywords):
        flags.append("JAILBREAK_ATTEMPT")
        return SafeResponse(
            is_safe=False,
            sanitized_query=req.query,
            response="Security Policy Violation: Prompt injection patterns detected.",
            safety_flags=flags
        )
        
    # 2. PII Sanitization (Mock Presidio)
    sanitized = req.query
    if "@" in sanitized:
        sanitized = "[REDACTED_EMAIL]"
        flags.append("PII_EMAIL_REDACTED")
        
    # 3. Process Safe Query
    simulated_answer = f"Safe response generated for query: {sanitized}"
    
    return SafeResponse(
        is_safe=True,
        sanitized_query=sanitized,
        response=simulated_answer,
        safety_flags=flags
    )""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Capstone Enterprise Safety Gateway
  user[User Request] $browser -> pii[Layer 1: Presidio PII Sanitizer] $lock
  pii -> rails[Layer 2: NeMo Jailbreak & Topical Rail] $shield
  rails -> llm[Layer 3: Core LLM Inference Engine] $cpu
  llm -> nli[Layer 4: Real-Time Groundedness Checker] $brain *
  nli -> audit[Layer 5: Structured JSON Audit Log] $database
  nli -> safe_user[Sanitized Verified Response] $server""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "OWASP Top 10 for Large Language Models", "url": "https://owasp.org/www-project-top-10-for-large-language-model-applications/"},
                        {"title": "Enterprise AI Security Best Practices", "url": "https://nv-nemo.github.io/guardrails/"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        },

        # =========================================================================
        # MODULE 11: Production AI Engineering & MLOps
        # =========================================================================
        {
            "phase_slug": "phase-4-production-mlops",
            "module_number": 11,
            "slug": "production-ai-engineering-mlops",
            "real_world_deliverable": "High-Throughput vLLM & Rust Axum LLM Gateway with Kubernetes KServe Autoscaling",
            "zero_gpu_recipe": {
                'platform': 'Fly.io / Render Free Tier / Local CPU',
                'vram_required': '0 GB (Gateway) / 16 GB+ (vLLM Production Host)',
                'estimated_cost': '$0.00 (Development & Proxy Gateway)',
                'compute_units_tip': 'Develop and test high-concurrency Rust Axum reverse proxy locally on CPU connected to free Groq/Cerebras endpoints.',
                'one_click_command': 'cargo run --release'
            },
            "title": "Module 11: Production AI Engineering & MLOps",
            "weeks_range": "Weeks 15-16",
            "estimated_hours": 16,
            "learning_outcomes": [
                "High-throughput inference architecture: vLLM PagedAttention, Continuous Batching aur KV Cache memory management",
                "Advanced model quantization formats: AWQ, GPTQ, NF4 aur FP8 KV Cache compression",
                "Ultra-low latency reverse proxies in Rust Axum with asynchronous SSE streaming",
                "Comprehensive LLM observability: Distributed tracing with OpenTelemetry, Prometheus aur Langfuse",
                "Scalable containerized deployment on Kubernetes using KServe, Ray Serve aur Horizontal Pod Autoscalers (HPA)",
                "Enterprise production resiliency: Multi-provider circuit breakers, fallback routing aur token budget quotas"
            ],
            "practical_tasks": [
                "vLLM engine run karein with PagedAttention and continuous batching benchmark",
                "AWQ quantized model deploy karein 4x memory savings ke sath",
                "Rust Axum streaming LLM gateway build karein capable of 10,000+ concurrent requests",
                "OpenTelemetry spans aur Langfuse tracing dashboard integrate karein",
                "Kubernetes deployment manifest configure karein with GPU resource limits and KServe autoscaler"
            ],
            "resources": [
                {"title": "vLLM: Easy, Fast, and Cheap LLM Serving", "url": "https://docs.vllm.ai/en/latest/"},
                {"title": "PagedAttention Research Paper (Woosuk Kwon et al.)", "url": "https://arxiv.org/abs/2309.06180"},
                {"title": "Rust Axum Web Framework", "url": "https://github.com/tokio-rs/axum"},
                {"title": "Langfuse Open Source LLM Engineering Platform", "url": "https://langfuse.com/"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 11 Production Serving Architecture
  client[Concurrent Clients] $browser -> rust_gw[Rust Axum Gateway] $server *
  rust_gw -> otel[OpenTelemetry / Langfuse Tracing] $chart
  rust_gw -> vllm[vLLM PagedAttention Cluster] $cpu
  vllm -> gpu_cache[Paged KV Cache Blocks] $database
  vllm -> k8s[Kubernetes KServe Autoscaler] $cloud""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "production-ready",
            "order_index": 11,
            "lessons": [
                {
                    "lesson_code": "11.1",
                    "slug": "vllm-paged-attention-mechanics",
                    "title": "High-Throughput LLM Inference: vLLM Architecture & PagedAttention",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab aap production mein LLM serve karte hain, to sab se bara bottleneck GPU compute nahi balki **GPU Memory (VRAM)** hoti hai, khusoosan **KV Cache (Key-Value Cache)**!

Traditional inference systems mein har incoming request ke liye memory pehle se reserve (pre-allocate) ki jati thi max_context_length (jaise 4096 tokens) ke hisab se. Nateeja?
- **Internal Fragmentation**: Agar request sirf 100 tokens generate kare, to baqi 3996 tokens ki VRAM bilkul waste ho jati thi!
- **External Fragmentation**: Memory contiguous na hone ki wajah se VRAM hote hue bhi nayi requests reject ho jati theen. 60% se 80% VRAM waste hoti thi!

UC Berkeley ke researchers ne **PagedAttention** introduce kiya (jo vLLM ka dil hai), jo operating system ke **Virtual Memory Paging** concept se inspired hai:
1. KV Cache ko contiguous memory mein rakhne ki bajaye fixed-size **Pages / Blocks** (jaise 16 ya 32 tokens per block) mein divide kiya jata hai.
2. GPU VRAM mein ek **Block Table** maintain hoti hai jo logical token positions ko physical non-contiguous GPU blocks se map karti hai.
3. Jab naya token generate hota hai, to sirf ek chota physical block allocate hota hai—zero memory waste!
4. **Continuous Batching (Iteration-Level Scheduling)**: Nayi requests ko purani batch ke khatam hone ka intezar nahi karna parta; har token step par nayi requests batch mein enter aur exit ho sakti hain!

Nateeja? vLLM standard Hugging Face ke muqable mein **10x se 24x zyada throughput** deliver karta hai!""",
                    "english_summary": "Master vLLM's PagedAttention virtual memory architecture and continuous batching to eliminate KV-cache fragmentation and achieve 20x higher inference throughput.",
                    "code_example": """# vLLM High-Throughput Serving Script
from vllm import LLM, SamplingParams

# 1. Define Sampling Parameters
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.9,
    max_tokens=256
)

# 2. Initialize vLLM Engine with PagedAttention
# gpu_memory_utilization: Reserve 90% of GPU VRAM for model & Paged KV cache
llm = LLM(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    tensor_parallel_size=1, # Number of GPUs
    gpu_memory_utilization=0.90,
    max_model_len=4096,
    trust_remote_code=True
)

prompts = [
    "Python mein async generators kaise kaam karte hain?",
    "Explain PagedAttention in three concise sentences.",
    "Database indexing ke primary trade-offs kya hain?"
]

# Continuous batching processes all prompts concurrently
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"\\nPrompt: {prompt}\\nResponse: {generated_text.strip()}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: PagedAttention Virtual Memory Mapping
  logical[Logical Tokens: [0..15] [16..31]] $terminal -> table[vLLM Block Table] $server
  table -> p1[Physical Block 7 in VRAM] $database
  table -> p2[Physical Block 12 in VRAM] $database
  p1 & p2 -> attn[Non-Contiguous Paged Attention Kernel] $cpu *
  attn -> stream[Continuous Batching Output Stream] $chart""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "vLLM Documentation", "url": "https://docs.vllm.ai/"},
                        {"title": "PagedAttention Paper", "url": "https://arxiv.org/abs/2309.06180"}
                    ],
                    "xp_reward": 25,
                    "order_index": 1
                },
                {
                    "lesson_code": "11.2",
                    "slug": "model-quantization-awq-gptq",
                    "title": "Model Quantization Deep Dive: AWQ, GPTQ & KV Cache Compression",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, model quantization ka matlab hai weights aur activations ki numeric precision ko kam karna (jaise 16-bit Float se 4-bit ya 8-bit Integer mein convert karna) taake memory 75% kam ho jaye aur bandwidth 4x fast ho jaye!

Lekin agar aap naadani mein tamam weights ko round off kar dein, to model ki reasoning collapse ho jati hai.
Modern quantization do clever techniques use karti hai:
1. **AWQ (Activation-aware Weight Quantization)**:
   AWQ ka fundamental insight yeh hai: **Tamam weights barabar ahem nahi hote!** Sirf 1% weights aise hote hain jin par activation magnitudes bohot bare hote hain (Salient Weights). AWQ in 1% salient weights ko identify karke unhe mathematically protect karta hai aur baqi 99% weights ko 4-bit quantize kar deta hai. Nateeja? Zero perplexity loss!
2. **GPTQ (Generalized Post-Training Quantization)**:
   Second-order Taylor expansion (Hessian matrix) use karke layer-by-layer quantization errors ko compensate karta hai.
3. **KV Cache FP8 / INT8 Quantization**:
   Sirf model weights hi nahi, balki lambi conversations ke KV Cache ko bhi 16-bit float ki jagah FP8 mein compress kiya jata hai, jis se context length double ho jati hai bina extra VRAM ke!""",
                    "english_summary": "Understand AWQ (Activation-aware Weight Quantization), GPTQ, and FP8 KV-cache compression to run large models in 75% less VRAM without perplexity degradation.",
                    "code_example": """# Deploying AWQ 4-Bit Model with vLLM
from vllm import LLM, SamplingParams

# Serving quantized AWQ model directly on consumer/cloud GPU
# Notice: quantization="awq" flag instructs vLLM to use optimized GEMM W4A16 kernels
llm = LLM(
    model="TheBloke/Llama-2-7B-Chat-AWQ",
    quantization="awq",
    dtype="float16",
    max_model_len=4096
)

sampling_params = SamplingParams(temperature=0.7, max_tokens=150)
outputs = llm.generate(["What is the primary benefit of AWQ quantization?"], sampling_params)
print(outputs[0].outputs[0].text)""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: AWQ Activation-Aware Quantization
  weights[FP16 Weights 14GB] $database -> inspect[Activation Magnitude Profiler] $cpu
  inspect -> salient[Top 1% Salient Weights: Protect High Precision] $shield
  inspect -> normal[99% Normal Weights: Quantize to 4-bit INT4] $layers
  salient & normal -> pack[AWQ Compressed Model 3.8GB] $server *
  pack -> vram[Fits in 8GB VRAM GPU with Zero Perplexity Loss] $terminal""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "AWQ: Activation-aware Weight Quantization Paper", "url": "https://arxiv.org/abs/2306.00978"},
                        {"title": "AutoAWQ GitHub Repository", "url": "https://github.com/casper-hansen/AutoAWQ"}
                    ],
                    "xp_reward": 25,
                    "order_index": 2
                },
                {
                    "lesson_code": "11.3",
                    "slug": "rust-axum-llm-gateway",
                    "title": "High-Concurrency LLM Reverse Proxy & Gateway in Rust Axum",
                    "duration_minutes": 40,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab aapke platform par hazaron concurrent users token streaming requests bhej rahe hon, to Python ka asyncio runtime (uvicorn/gunicorn) Global Interpreter Lock (GIL) aur memory overhead ki wajah se bottleneck ban jata hai.

Iska high-performance solution **Rust** aur **Axum** (built on Tokio asynchronous runtime) hai!
Kyun Rust?
- **Zero-Cost Abstractions**: Rust mein koi garbage collector nahi hota; memory compile-time par deterministic hoti hai.
- **Fearless Concurrency**: Tokio multi-threaded work-stealing threadpool hazaron concurrent SSE connections ko minimal CPU aur sirf kuch megabytes RAM mein handle kar leta hai!
- **Channel Streaming**: Rust ke `tokio::sync::mpsc` channels ke zariye backend vLLM se aane wale token streams direct client HTTP response stream mein pipe ho jate hain bina intermediate allocation ke.

Is lesson mein hum ek production Rust Axum gateway banayenge jo token rate limiting, authentication, aur SSE streaming proxying provide karega.""",
                    "english_summary": "Architect an ultra-high concurrency LLM streaming gateway in Rust Axum leveraging the Tokio async runtime for sub-millisecond connection handling.",
                    "code_example": """// Rust Axum LLM Streaming Reverse Proxy (src/main.rs)
use axum::{
    routing::get,
    response::sse::{Event, KeepAlive, Sse},
    Router,
};
use futures::stream::{self, Stream};
use std::{convert::Infallible, time::Duration};
use tokio_stream::StreamExt as _;

async fn stream_tokens() -> Sse<impl Stream<Item = Result<Event, Infallible>>> {
    let words = vec!["Salam!", "Yeh", "Rust", "Axum", "high-throughput", "streaming", "gateway", "hai."];
    
    let stream = stream::iter(words).map(|word| {
        Ok(Event::default().data(word))
    }).throttle(Duration::from_millis(50));

    Sse::new(stream).keep_alive(KeepAlive::default())
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/v1/stream", get(stream_tokens));
    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();
    println!("Rust Axum Gateway listening on http://0.0.0.0:8080");
    axum::serve(listener, app).await.unwrap();
}""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Rust Axum Concurrent Gateway
  clients[10,000+ Concurrent HTTP Connections] $browser -> tokio[Tokio Work-Stealing Runtime] $cpu
  tokio -> axum[Rust Axum Router & Rate Limiter] $server *
  axum -> pool[Reqwest HTTP/2 Connection Pool] $network
  pool -> vllm[Backend vLLM Cluster] $database
  vllm -> clients: Zero-Copy Chunked SSE Streams""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Axum Web Framework Docs", "url": "https://docs.rs/axum/latest/axum/"},
                        {"title": "Tokio Asynchronous Runtime", "url": "https://tokio.rs/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "11.4",
                    "slug": "opentelemetry-langfuse-observability",
                    "title": "Production LLM Observability: OpenTelemetry, Tracing & Langfuse",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab ek user ki request aati hai aur wo agentic loop, vector retrieval, reranking, aur LLM call se guzarti hai, to agar response mein 4 seconds lag gaye ya galat answer aya, to aap kaise diagnose karenge ke masla kahan tha?
- Kya vector database slow tha?
- Kya prompt tokens bohot lambe the?
- Kya tool execution fail hui?

Iska jawab **Distributed Tracing & LLM Observability** hai using **OpenTelemetry** aur **Langfuse**!
1. **Traces & Spans**: Har request ko ek unique `trace_id` milta hai. Har internal operation (embedding generation, DB query, LLM completion) ek child `span` banata hai jisme exact latency (milliseconds), input/output tokens, aur cost track hoti hai.
2. **Token & Cost Accounting**: Har LLM provider ke input aur output tokens calculate karke exact dollar cost per user track ki jati hai.
3. **Session Replays**: User feedback (thumbs up / thumbs down) ko trace se link karke debugging dashboard mein dekha ja sakta hai.""",
                    "english_summary": "Instrument production AI pipelines with OpenTelemetry spans and Langfuse tracing to monitor latency bottlenecks, token unit economics, and end-to-end execution graphs.",
                    "code_example": """from langfuse import Langfuse
import time

# Initialize Langfuse client
langfuse = Langfuse()

def run_observed_rag_pipeline(user_query: str, user_id: str):
    # 1. Create root trace for user session
    trace = langfuse.trace(
        name="chat_interaction",
        user_id=user_id,
        input={"query": user_query}
    )
    
    # 2. Span: Vector Database Retrieval
    retrieval_span = trace.span(name="vector_retrieval", input=user_query)
    time.sleep(0.04) # Simulate DB latency
    retrieved_docs = ["Doc 1: AI Ustaad curriculum overview"]
    retrieval_span.end(output={"docs_count": len(retrieved_docs)})
    
    # 3. Generation: LLM Call with token metrics
    generation = trace.generation(
        name="llama_completion",
        model="meta-llama/llama-3.1-8b-instruct",
        input=[{"role": "user", "content": user_query}],
        output="Salam! AI Ustaad mein 14 modules hain.",
        usage={"input": 45, "output": 18, "total": 63}
    )
    
    trace.update(output="Salam! AI Ustaad mein 14 modules hain.")
    print("Trace successfully exported to Langfuse dashboard!")

run_observed_rag_pipeline("AI Ustaad mein kitne modules hain?", "student_user_101")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: OpenTelemetry Distributed Trace
  trace[Trace: User Chat Request] $terminal -> span_retrieval[Span: Hybrid Search 42ms] $database
  trace -> span_rerank[Span: FlashRank Reranker 18ms] $cpu
  trace -> span_llm[Generation: vLLM Stream 320ms] $server *
  span_llm -> metrics[Export to Langfuse & Prometheus: Tokens, Latency, Cost] $chart""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Langfuse Open Source LLM Observability", "url": "https://langfuse.com/docs"},
                        {"title": "OpenTelemetry Python SDK", "url": "https://opentelemetry.io/docs/languages/python/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 4
                },
                {
                    "lesson_code": "11.5",
                    "slug": "kubernetes-kserve-ray-autoscaling",
                    "title": "Enterprise Cluster Serving: Kubernetes, KServe, Ray & Autoscaling",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, enterprise scale par jab traffic subah 100 requests/sec se barh kar shaam ko 50,000 requests/sec ho jaye, to aap ek single GPU server par nahi reh sakte! Aapko dynamic horizontal cluster autoscaling chahiye.

Modern AI infrastructure **Kubernetes (K8s)** par build hoti hai using two dominant technologies:
1. **KServe / vLLM Operator**:
   KServe Kubernetes par serverless AI serving provide karta hai. Yeh standard CPU/Memory metrics ki bajaye **Queue Depth (vLLM Waiting Requests)** aur **KV Cache Usage** par autoscaling (HPA / KEDA) trigger karta hai! Agar waiting queue > 10 ho jaye, to foran naye GPU pods spin up ho jate hain.
2. **Ray Serve**:
   Distributed Python execution framework jo multi-node model parallelism (Tensor Parallelism across 8x H100 GPUs) aur dynamic request routing handle karta hai.

Is lesson mein hum production Kubernetes manifests (Deployment, Service, KEDA ScaledObject) configure karenge jo zero-downtime rolling updates provide karte hain.""",
                    "english_summary": "Deploy distributed LLM inference clusters on Kubernetes with KServe and Ray Serve, configuring KEDA autoscaling driven by real-time vLLM queue-depth metrics.",
                    "code_example": """# k8s-vllm-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-inference-deployment
  labels:
    app: vllm-engine
spec:
  replicas: 2
  selector:
    matchLabels:
      app: vllm-engine
  template:
    metadata:
      labels:
        app: vllm-engine
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:latest
        args: ["--model", "meta-llama/Meta-Llama-3.1-8B-Instruct", "--gpu-memory-utilization", "0.9"]
        resources:
          limits:
            nvidia.com/gpu: 1
            memory: 32Gi
            cpu: "8"
        ports:
        - containerPort: 8000
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 60
          periodSeconds: 10""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Kubernetes KServe Cluster Autoscaling
  ingress[Cloud Ingress / Load Balancer] $network -> keda[KEDA Autoscaler Controller] $server
  keda -> metric[vLLM Waiting Requests Metric] $chart
  ingress -> pod1[GPU Pod 1: vLLM Replica] $cpu
  ingress -> pod2[GPU Pod 2: vLLM Replica] $cpu
  metric -- Queue > 15 --> pod3[Scale Out: GPU Pod 3] $cloud *""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "KServe: Cloud-Native Model Serving", "url": "https://kserve.github.io/website/"},
                        {"title": "KEDA: Kubernetes Event-Driven Autoscaling", "url": "https://keda.sh/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "11.6",
                    "slug": "capstone-high-throughput-cluster",
                    "title": "Module 11 Capstone: Production High-Throughput Serving Cluster (99.9% SLA)",
                    "duration_minutes": 50,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, congratulations! Aap Phase 4 ke final Capstone project par pohanch chuke hain. Is capstone mein aap ek high-scale, resilient **Production AI Serving Cluster** architecture assemble karenge jo 99.9% uptime SLA ensure karega!

Aapka Capstone Architecture:
1. **Rust Axum Gateway Layer**: Front-facing API jo token authentication, rate limiting (sliding window), aur client SSE streaming handle karegi.
2. **Multi-Provider Fallback Circuit Breaker**: Primary vLLM cluster par requests send karega; agar local cluster busy ya down ho (latency > 2s ya 5xx errors), to automatically external failover provider (jaise Groq ya Cerebras) par seamless switch karega!
3. **Telemetry & Metrics Exporter**: Prometheus `/metrics` endpoint expose karega jo Token Latency P95/P99, Active Connections, aur Cache Hit Ratios track karega.
4. **Docker Compose & K8s Packaging**: Poore stack (Axum Proxy + vLLM + Redis Cache + Prometheus) ko containerize karein with automated health checks.
5. **Stress Test Verification**: Locust ya k6 se 500 concurrent virtual users ka load test chala kar verify karein ke zero dropped requests hon!""",
                    "english_summary": "Build and verify the Module 11 Capstone: an enterprise-grade high-throughput serving cluster with Rust Axum gateway, dynamic fallback circuit breakers, and Prometheus telemetry.",
                    "code_example": """# Prometheus Metric Exporter for LLM Serving Cluster (Python/Rust Middleware)
from prometheus_client import Counter, Histogram, generate_latest
from fastapi import FastAPI, Response

app = FastAPI()

# 1. Prometheus Metrics Definitions
REQUEST_COUNT = Counter('llm_requests_total', 'Total incoming LLM inference requests', ['model', 'status'])
LATENCY_HISTOGRAM = Histogram('llm_token_latency_seconds', 'Token generation latency in seconds', ['model'])

@app.get("/api/chat")
async def chat_handler(model: str = "llama-3.1-8b"):
    REQUEST_COUNT.labels(model=model, status="success").inc()
    with LATENCY_HISTOGRAM.labels(model=model).time():
        # Simulated inference
        pass
    return {"status": "ok", "message": "Cluster operational"}

@app.get("/metrics")
async def metrics_endpoint():
    \"\"\"Exposes standard Prometheus scrape endpoint.\"\"\"
    return Response(content=generate_latest(), media_type="text/plain")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: High-Throughput Cluster with Circuit Breaker
  traffic[High Concurrency User Traffic] $browser -> gateway[Rust Axum Gateway & Rate Limiter] $server *
  gateway -> cb[Circuit Breaker & Fallback Manager] $shield
  cb -- Normal Healthy --> vllm_cluster[Primary vLLM K8s Cluster] $cpu
  cb -- High Latency / 5xx Error --> groq[Failover Fast Cloud Groq API] $cloud
  gateway -> prometheus[Prometheus & Grafana Telemetry] $chart""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Designing Data-Intensive Applications: Reliability", "url": "https://dataintensive.net/"},
                        {"title": "Prometheus Monitoring System", "url": "https://prometheus.io/docs/introduction/overview/"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        }
    ]
