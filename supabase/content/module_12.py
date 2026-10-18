# module_12.py
# Module 12: Multimodal AI & Vision
# Lessons 12.1 to 12.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 12.1: Foundations of Vision-Language Models: CLIP & Contrastive Learning
# ==============================================================================
LESSON_CONTENT['12.1'] = r"""### Part 1: Mental Model & South Asian Analogy
Pichle daur mein Computer Vision aur Natural Language Processing (NLP) do alag alag jazeeray the: Vision models images ko 1000 rigid classes (Cat, Dog, Car) mein classify karte the, jabke Text models alag text samajhte the. 2021 mein OpenAI ne **CLIP (Contrastive Language-Image Pre-training)** ke zariye dono jazeeron ke darmiyan ek azeem pul baandh diya!
Isay samajhne ke liye kisi Photographer aur Tasweer ke Niche Caption Likhnay wale Sahafi ki misaal lein:
1. Two Specialized Brains (Do Alag Alag Encoders):
   - Image Encoder (Vision Transformer / ViT): Tasweer ko dekhta hai aur 512 numbers ka ek vector banata hai.
   - Text Encoder (Transformer): Jumlay ("Karak chai in clay cup") ko parhta hai aur 512 numbers ka vector banata hai.
2. The Shared Semantic Space (Mushtarika Maanvi Maidan): CLIP ka jadu yeh hai ke dono alag alag encoders ek hi mushtarika vector space mein baat karte hain! Agar tasweer chai ki ho aur text bhi chai ka ho, to dono vectors aapas mein parallel (High Cosine Similarity) ho jate hain.
3. Contrastive Learning (Sahi Jori Ko Qareeb Lana, Ghalat Ko Door Phenkna): Farz karein table par 16 tasweerein aur 16 captions rakhay hain. CLIP ka maqsad yeh hai ke har tasweer ko uske sahi caption se joray (Diagonal Elements Maximize) aur baqi 15 ghalat captions se door dhaklay (Off-Diagonal Minimize).
4. Zero-Shot Image Classification: CLIP ne traditional classification ko khatam kar diya! Aapko naye model ko train karne ki zaroorat nahi; aap seedha text likhein "A photo of an auto-rickshaw" aur CLIP tasweer ko dekh kar bata dega ke yeh rickshaw hai ya nahi!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein CLIP ke Symmetric Cross-Entropy Contrastive Loss ka exact hisab trace karte hain.
Setup:
Batch Size $N = 2$ image-text pairs.
Image Embeddings: $I_0, I_1$ (Normalized L2 unit vectors)
Text Embeddings: $T_0, T_1$ (Normalized L2 unit vectors)
Learnable temperature parameter: $\tau = 1.0$

Similarity Matrix ($S = I \cdot T^T$):
$S = \begin{bmatrix} I_0 \cdot T_0 & I_0 \cdot T_1 \\ I_1 \cdot T_0 & I_1 \cdot T_1 \end{bmatrix}$
Suppose Cosine Dot Products are:
$S = \begin{bmatrix} 2.5 & 0.5 \\ 0.2 & 3.0 \end{bmatrix}$
Diagonal elements ($S_{0,0} = 2.5$ and $S_{1,1} = 3.0$) are ground-truth positive pairs!

Step 1: Compute Image-to-Text Loss (Row-wise Cross-Entropy)
Row 0: Target is class 0.
$P(0|I_0) = \frac{e^{2.5}}{e^{2.5} + e^{0.5}} = \frac{12.182}{12.182 + 1.649} = \frac{12.182}{13.831} \approx 0.8808$
$L_{I_0} = -\log_e(0.8808) \approx 0.1269$

Row 1: Target is class 1.
$P(1|I_1) = \frac{e^{3.0}}{e^{0.2} + e^{3.0}} = \frac{20.086}{1.221 + 20.086} = \frac{20.086}{21.307} \approx 0.9427$
$L_{I_1} = -\log_e(0.9427) \approx 0.0590$
$\text{Loss}_{I \to T} = \frac{0.1269 + 0.0590}{2} = 0.0930$

Step 2: Compute Text-to-Image Loss (Column-wise Cross-Entropy)
Col 0: Target is class 0.
$P(0|T_0) = \frac{e^{2.5}}{e^{2.5} + e^{0.2}} = \frac{12.182}{12.182 + 1.221} \approx 0.9089 \implies L_{T_0} = 0.0955$
Col 1: Target is class 1.
$P(1|T_1) = \frac{e^{3.0}}{e^{0.5} + e^{3.0}} = \frac{20.086}{1.649 + 20.086} \approx 0.9241 \implies L_{T_1} = 0.0789$
$\text{Loss}_{T \to I} = \frac{0.0955 + 0.0789}{2} = 0.0872$

Step 3: Symmetric Total CLIP Loss
$L_{\text{total}} = \frac{\text{Loss}_{I \to T} + \text{Loss}_{T \to I}}{2} = \frac{0.0930 + 0.0872}{2} = 0.0901$.
Dono directions mein contrastive loss optimize hota hai jisse text aur image representations perfectly align ho jati hain!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Symmetric Contrastive Loss function, unit normalization, aur Zero-Shot Image Classification pipeline PyTorch mein implement karte hain.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SymmetricContrastiveLoss(nn.Module):
    \"\"\"Production CLIP Symmetric Cross-Entropy Loss over image-text batch.\"\"\"
    def __init__(self, init_temperature: float = 0.07) -> None:
        super().__init__()
        # Learnable log-temperature parameter to prevent numerical instability
        self.log_tau = nn.Parameter(torch.tensor(torch.log(torch.tensor(init_temperature))))

    def forward(self, image_embeddings: torch.Tensor, text_embeddings: torch.Tensor) -> torch.Tensor:
        # Normalize vectors to unit hypersphere: [Batch, Dim]
        img_norm = F.normalize(image_embeddings, p=2, dim=-1)
        txt_norm = F.normalize(text_embeddings, p=2, dim=-1)

        tau = torch.exp(self.log_tau).clamp(min=1e-4, max=100.0)
        
        # 1. Cosine similarity logits matrix: [Batch, Batch]
        logits = torch.matmul(img_norm, txt_norm.T) / tau
        batch_size = image_embeddings.size(0)

        # Ground-truth targets: diagonal indices [0, 1, ..., N-1]
        labels = torch.arange(batch_size, device=image_embeddings.device)

        # 2. Symmetric cross entropy
        loss_i2t = F.cross_entropy(logits, labels)
        loss_t2i = F.cross_entropy(logits.T, labels)

        return 0.5 * (loss_i2t + loss_t2i)

def zero_shot_classify(image_feat: torch.Tensor, candidate_text_feats: torch.Tensor) -> torch.Tensor:
    \"\"\"Computes zero-shot classification probabilities across candidate label embeddings.\"\"\"
    img_n = F.normalize(image_feat, p=2, dim=-1)
    txt_n = F.normalize(candidate_text_feats, p=2, dim=-1)
    # Cosine similarities: [1, Num_Classes]
    similarities = torch.matmul(img_n, txt_n.T) * 100.0  # Temperature scaling
    probs = F.softmax(similarities, dim=-1)
    return probs

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    B, D = 4, 32
    img_embs = torch.randn(B, D)
    txt_embs = torch.randn(B, D)

    criterion = SymmetricContrastiveLoss()
    loss = criterion(img_embs, txt_embs)
    print(f"Contrastive Symmetric Loss Computed: {loss.item():.4f}")

    # Zero-shot classification test
    sample_img = torch.randn(1, D)
    # 3 Candidate classes: ["Chai", "Biryani", "Rickshaw"]
    candidate_labels = torch.randn(3, D)
    probs = zero_shot_classify(sample_img, candidate_labels)
    print("Zero-Shot Predicted Probabilities:", probs.tolist()[0])
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Forgetting L2 Normalization Before Dot Product: Agar image aur text vectors ko unit length par normalize na kiya jaye to vector ki length similarity score ko corrupt kar deti hai. Hamesha `F.normalize(vec, p=2, dim=-1)` karein.
2. Unclamped Temperature Parameter: Log-temperature $\tau$ ko clamp na karne se training ke doran temperature zero ya negative ho sakti hai jisse `NaN` gradients aate hain. Hamesha `.clamp(min=1e-4, max=100.0)` use karein.
3. Small Batch Size in Contrastive Learning: Contrastive learning tab behtareen chalti hai jab batch mein bohot se negative examples hon. Batch size $< 64$ par CLIP feature alignment poor rehti hai.

Zero-GPU Tip:
CLIP zero-shot inference aur cosine similarity ranking CPU par microsecond speed se chalti hai. Chote open-source models (jaise `clip-ViT-B-32` via ONNX runtime) CPU par images ko real-time classify kar sakte hain.

Self-Check Questions:
1. CLIP model mein Image Encoder aur Text Encoder ka aapas mein kya talluq hota hai?
2. Symmetric Cross-Entropy Loss mein Row-wise aur Column-wise loss dono ko kyun shamil kiya jata hai?
3. Zero-Shot Classification traditional supervised classification se kyun behtar hoti hai?

What to Build Next:
Ek Zero-Shot Image Search Engine banayein jo 100 images ke pre-computed CLIP vectors rakhe, user ke text query ka vector banaye, aur top-3 matching images unke cosine similarity scores ke sath return kare."""

# ==============================================================================
# LESSON 12.2: Vision Encoders & Projectors: SigLIP & Modern VLM Architecture
# ==============================================================================
LESSON_CONTENT['12.2'] = r"""### Part 1: Mental Model & South Asian Analogy
CLIP ne tasweer aur text ko match karna sikhaya. Lekin modern Vision-Language Models (VLMs jaise LLaVA, PaliGemma, aur GPT-4V) tasweer ko sirf match nahi karte; woh tasweer ko dekh kar us par poora mazmoon likh sakte hain aur sawalon ke jawab de sakte hain! Is architecture ka dil **Vision Encoders, SigLIP, aur Multimodal Projectors** hai.
Isay samajhne ke liye kisi Aam Insaan (LLM), Ek Cameraman (Vision Encoder), aur Ek Tarjuman (Projector) ki misaal lein:
1. The Brain / LLM (The Blind Scholar): Scholar bohot aqalmand hai, 50 kitabein padh chuka hai, lekin aankhon se andha hai. Woh sirf text tokens samajhta hai.
2. The Cameraman / SigLIP (The Visual Observer): Cameraman tasweer ke 256 chotay chotay tukray (Visual Patches) banata hai. SigLIP 2024-2026 ka advanced vision encoder hai jo standard Softmax ke bajaye Sigmoid Loss use karta hai, jisse chotay batch size par bhi vision alignment 2x behtar hoti hai.
3. The Projector / Bridge (The Translator): Masla yeh hai ke Cameraman ke patch vectors ka dimension 768 hai, jabke Blind Scholar ka token dimension 4096 hai! Projector ek choti si 2-layer MLP hoti hai jo tasweer ke 768-dim patch vectors ko 4096-dim text tokens mein translate kar deti hai.
4. Multimodal Fusion: Andhay Scholar ke liye tasweer ke patches bilkul aam text tokens ban jate hain! Model unhe aise padhta hai jese regular sentence ho: `[Patch_1, Patch_2, ..., Patch_256, "Describe this photo:"]` aur aage autoregressive generation shuru ho jati hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein SigLIP ke Pairwise Sigmoid Loss aur Vision Projector Dimension Mapping ka hisab lagayein.
CLIP Softmax Loss vs SigLIP Sigmoid Loss:
CLIP mein poori row par Softmax calculate hota hai jiske liye poore batch ka global denominator sum chahiye hota hai (Heavy memory across distributed GPUs).
SigLIP har image-text pair $(i, j)$ ko ek independent binary classification problem banata hai:
$L_{\text{SigLIP}} = -\sum_{i=1}^{B} \sum_{j=1}^{B} \log \sigma(z_{ij} (I_i \cdot T_j - b))$
Jahan $z_{ij} = +1$ if $i = j$ (Positive pair), and $z_{ij} = -1$ if $i \ne j$ (Negative pair).
Softmax denominator khatam ho gaya! Har pair azadana calculate hota hai jisse batch size scale karna bohot asan ho jata hai.

Projector Dimension Math:
- Vision Encoder: SigLIP patch output shape $= [B, N_{\text{patches}}, D_{\text{vision}}] = [2, 196, 768]$
- Target Text LLM (LLaMA-3): Input hidden dimension $= D_{\text{llm}} = 4096$
- Multimodal Projector Architecture: 2-layer MLP with GELU:
  - Linear 1: $768 \to 4096$
  - Activation: GELU
  - Linear 2: $4096 \to 4096$

Forward Projection Shape Transition:
Input visual patches: $[2, 196, 768]$
$\to$ Linear 1: $[2, 196, 4096]$
$\to$ GELU: $[2, 196, 4096]$
$\to$ Linear 2: $[2, 196, 4096]$.
Tasweer ke 196 visual patches theek 196 text token embeddings ban gaye!
Ab in 196 visual tokens ko user ke prompt tokens (e.g. 15 text tokens) ke sath concatenate kiya jata hai:
Total Sequence Length: $196 + 15 = 211 \text{ tokens}$.
LLaMA-3 model is poori multimodal sequence par standard causal self-attention chalata hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete Vision-Language MLP Projector, visual-to-text token fusion, aur multimodal forward pass sequence assembly implement karte hain.

```python
import torch
import torch.nn as nn

class MultimodalProjector(nn.Module):
    \"\"\"Projects visual patch embeddings into language model representation space (LLaVA-style).\"\"\"
    def __init__(self, vision_dim: int = 768, llm_dim: int = 4096) -> None:
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(vision_dim, llm_dim),
            nn.GELU(),
            nn.Linear(llm_dim, llm_dim)
        )

    def forward(self, visual_patches: torch.Tensor) -> torch.Tensor:
        # Input shape: [Batch, Num_Patches, vision_dim]
        # Output shape: [Batch, Num_Patches, llm_dim]
        return self.mlp(visual_patches)

class SimpleVLMSequenceBuilder(nn.Module):
    \"\"\"Merges projected visual tokens with text instruction tokens into unified LLM stream.\"\"\"
    def __init__(self, vision_dim: int = 768, llm_dim: int = 1024, vocab_size: int = 1000) -> None:
        super().__init__()
        self.projector = MultimodalProjector(vision_dim=vision_dim, llm_dim=llm_dim)
        self.text_embedding = nn.Embedding(vocab_size, llm_dim)

    def forward(self, visual_patches: torch.Tensor, text_token_ids: torch.Tensor) -> torch.Tensor:
        # 1. Project image patches to LLM embedding dimension: [B, N_patches, llm_dim]
        projected_image_tokens = self.projector(visual_patches)

        # 2. Embed text token IDs: [B, N_text, llm_dim]
        text_tokens = self.text_embedding(text_token_ids)

        # 3. Concatenate along sequence dimension: [B, N_patches + N_text, llm_dim]
        fused_sequence = torch.cat([projected_image_tokens, text_tokens], dim=1)
        return fused_sequence

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    B = 1
    N_patches = 16  # E.g. 4x4 visual patch grid
    vision_dim = 64
    llm_dim = 128
    vocab_size = 256

    mock_visual_patches = torch.randn(B, N_patches, vision_dim)
    mock_prompt_tokens = torch.tensor([[10, 45, 99, 12, 5]], dtype=torch.long)  # 5 text tokens

    vlm_builder = SimpleVLMSequenceBuilder(vision_dim=vision_dim, llm_dim=llm_dim, vocab_size=vocab_size)
    fused_embeddings = vlm_builder(mock_visual_patches, mock_prompt_tokens)

    print(f"Visual Patches Shape:     {list(mock_visual_patches.shape)}")
    print(f"Text Token IDs Shape:     {list(mock_prompt_tokens.shape)}")
    print(f"Fused VLM Sequence Shape: {list(fused_embeddings.shape)} (16 visual + 5 text = 21 tokens!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Training the Entire LLM During Initial Multimodal Alignment: Pre-training phase mein LLM weights ko direct train karne se model catastrophic forgetting ka shikar ho jata hai. Hamesha pehle phase mein LLM aur Vision Encoder dono ko **Freeze** rakhein aur sirf choti Multimodal Projector MLP ko train karein.
2. Inconsistent Image Aspect Ratio Resizing: Tasweer ko zabardasti square $224 \times 224$ mein distort karne se document text aur table borders kharab ho jate hain. Modern VLMs (jaise LLaVA-1.5 ya PaliGemma) aspect-ratio preserving padding ya high-resolution AnyRes slicing use karte hain.
3. Ignoring Vision Token Positions in Causal Masking: Visual tokens bidirectional attention use karte hain jabke aglay text tokens causal masking use karte hain. Prefix-LM masking verify karein.

Zero-GPU Tip:
Projector dimensions, visual patch concatenation, aur unified token stream assembly pure tensor matrix operations hain jo CPU par milliseconds mein execute hoti hain. Inka shape flow verify karne ke liye kisi GPU ki zaroorat nahi hai.

Self-Check Questions:
1. Modern Vision-Language Models mein Multimodal Projector ka kya kirdaar hota hai?
2. SigLIP ka pairwise Sigmoid Loss standard CLIP Softmax Loss se memory scaling mein kyun behtar hai?
3. Visual patches ko text token embeddings ke sath concatenate karke LLM kaise process karta hai?

What to Build Next:
Ek Multimodal Token Inspector script banayein jo ek sample image aur prompt ka sequence layout visualize kare aur visual vs text token positions print kare."""

# ==============================================================================
# LESSON 12.3: Document & Invoice Intelligence: Visual OCR & Structured Extraction
# ==============================================================================
LESSON_CONTENT['12.3'] = r"""### Part 1: Mental Model & South Asian Analogy
Corporate enterprise workflows (jaise Banks, Logistics, aur Retail Stores) mein rozana hazaron kaghazi receipts, bills, aur tax invoices aate hain. Traditional OCR (Tesseract) sirf raw text dump deta hai jisme yeh pata nahi chalta ke kaun sa number tax ka hai aur kaun sa total ka. Modern standard **Visual Document Intelligence (Donut, Nougat, aur VLM Structured Extraction)** hai!
Isay samajhne ke liye kisi Supermarket ke Cashier aur Receipt Scanner ki misaal lein:
1. Traditional OCR + Regex Pipeline (Kacha Munshi): Pehla banda receipt ko scan karta hai, doosra banda 50 mukhtalif regex likhta hai ("Dhoondo jahan 'Total' likha ho uske aage ka number uthao"). Agar receipt ka layout badal jaye ya dukan badal jaye to poora regex pipeline crash ho jata hai ($O(N)$ maintenance nightmare).
2. End-to-End Visual Parsing (Aankhon Wala Digital Auditor): Donut (Document Understanding Transformer) aur modern VLMs receipt ko ek hi step mein tasweer se seedha **Strict JSON Object** mein convert karte hain!
3. Layout Awareness: Model janta hai ke table ke pehle column mein "Item Name" hai, doosre mein "Price" hai, aur aakhir mein line ke neeche "Grand Total" likha hua hai. Kaghaz par chahe chai ke daagh hon ya thoda sa teerha (skewed) ho, model visual context se sahi numbers pakar leta hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Document Field Extraction Confidence aur Reconciled Math Verification ka logic trace karte hain.
Receipt Extraction Validation Rule:
$\text{Calculated Total} = \sum_{i=1}^{K} (\text{quantity}_i \times \text{unit\_price}_i) + \text{tax} - \text{discount}$
Invariant Check:
$|\text{Calculated Total} - \text{Extracted Grand Total}| \le 0.01 \text{ PKR}$

Extracted Raw Fields from Dhaba Invoice Image:
Items Extracted:
- Item 1: `Doodh Patti`, Qty = 2, Unit Price = 60.0
- Item 2: `Lachha Paratha`, Qty = 1, Unit Price = 120.0
- Tax Extracted: 38.40 PKR
- Discount: 0.00 PKR
- Extracted Grand Total: 278.40 PKR

Mathematical Step-by-Step Reconciliation:
- Subtotal Item 1: $2 \times 60.0 = 120.0 \text{ PKR}$
- Subtotal Item 2: $1 \times 120.0 = 120.0 \text{ PKR}$
- Sum of Items $= 120.0 + 120.0 = 240.0 \text{ PKR}$
- Add Tax: $240.0 + 38.40 = 278.40 \text{ PKR}$
- Subtract Discount: $278.40 - 0.0 = 278.40 \text{ PKR}$
Residual Error:
$|278.40 - 278.40| = 0.0000 \text{ PKR}$!
Reconciliation Confirmed 100%! Document extraction verified safe for automated ERP ledger entry without human intervention.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Pydantic V2 schema enforced Invoice Visual Extraction Parser aur programmatic mathematical integrity validator implement karte hain.

```python
import json
from typing import List
from pydantic import BaseModel, Field, ValidationError

# 1. Strict Enterprise Invoice Schema
class InvoiceLineItem(BaseModel):
    description: str = Field(min_length=2)
    quantity: int = Field(ge=1)
    unit_price: float = Field(ge=0.0)

    @property
    def line_total(self) -> float:
        return round(self.quantity * self.unit_price, 2)

class ExtractedInvoice(BaseModel):
    invoice_number: str
    vendor_name: str
    items: List[InvoiceLineItem] = Field(min_length=1)
    tax_amount: float = Field(ge=0.0)
    grand_total: float = Field(ge=0.0)

    def verify_financial_integrity(self) -> tuple[bool, float, str]:
        \"\"\"Mathematically verifies line item sum matches grand total.\"\"\"
        computed_subtotal = sum(item.line_total for item in self.items)
        expected_grand_total = round(computed_subtotal + self.tax_amount, 2)
        discrepancy = abs(expected_grand_total - self.grand_total)
        
        if discrepancy > 0.05:
            return False, discrepancy, f"Financial mismatch: computed {expected_grand_total} != declared {self.grand_total}"
        return True, 0.0, "Financial reconciliation 100% verified."

# 2. Simulated End-to-End VLM Document Extractor
def parse_invoice_visual_output(mock_vlm_json_str: str) -> ExtractedInvoice:
    try:
        raw_dict = json.loads(mock_vlm_json_str)
        invoice = ExtractedInvoice.model_validate(raw_dict)
        return invoice
    except (json.JSONDecodeError, ValidationError) as err:
        raise ValueError(f"Visual document parsing contract violation: {err}")

# Execution test
if __name__ == "__main__":
    # Simulated perfect extraction from receipt image
    sample_vlm_payload = \"\"\"{
        "invoice_number": "INV_PK_8821",
        "vendor_name": "Quetta Madina Chai Hotel",
        "items": [
            {"description": "Special Doodh Patti", "quantity": 3, "unit_price": 60.0},
            {"description": "Lachha Paratha", "quantity": 2, "unit_price": 120.0}
        ],
        "tax_amount": 67.20,
        "grand_total": 487.20
    }\"\"\"

    invoice = parse_invoice_visual_output(sample_vlm_payload)
    is_valid, error_diff, msg = invoice.verify_financial_integrity()

    print("Visual Document Intelligence Extraction:")
    print(f"  Invoice ID: {invoice.invoice_number}")
    print(f"  Vendor:     {invoice.vendor_name}")
    print(f"  Total Items Parsed: {len(invoice.items)}")
    print(f"  Integrity Check:    {msg} (Discrepancy: PKR {error_diff:.2f})")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Trusting VLM Extracted Grand Totals Without Math Checks: Vision-Language Models aksar numbers ko dekhne mein slight error kar dete hain (jaise 8 ko 3 padhna). Extracted grand total ko hamesha programmatic Python loop se line items ke sath mathematically verify karein.
2. Low Contrast Receipts Crashing OCR: Thermal paper receipts waqt ke sath faint ho jati hain. Image ko VLM mein bhejte waqt contrast enhancement (Adaptive Histogram Equalization / CLAHE) pre-processing lazmi karein.
3. Ignoring Multi-Page Table Continuity: Agar invoice 3 safhon par phaili ho aur har page par subtotal ho to page-by-page chunking tables ko tod sakti hai. Multi-page document models use karein.

Zero-GPU Tip:
Invoice parsing verification, Pydantic schema validation, aur mathematical reconciliation pure CPU logic hain. VLM inference ke liye free tier multimodal APIs (Gemini 2.0 Flash) use karein jo receipt images ko 500ms mein zero GPU cost par parse kar deti hain.

Self-Check Questions:
1. Donut / Nougat visual document understanding traditional OCR + regex pipelines se kyun behtar hoti hai?
2. Document extraction mein programmatic mathematical reconciliation audit kyu lazmi hota hai?
3. Pydantic validator line item totals aur grand total consistency ko kaise verify karta hai?

What to Build Next:
Ek Automated Receipt Scanner Tool banayein jo receipt image upload accept kare, Gemini 2.0 Flash se Pydantic JSON extract kare, mathematical error check kare, aur accounting database mein save kare."""

# ==============================================================================
# LESSON 12.4: Audio & Speech Processing: OpenAI Whisper & Audio-LLMs
# ==============================================================================
LESSON_CONTENT['12.4'] = r"""### Part 1: Mental Model & South Asian Analogy
Text aur tasweeron ke baad multimodal AI ka teesra azeem sutoon **Audio aur Aawaz (Speech)** hai. Insaani aawaz dar-haqeeqat hawa mein dabao ki lehron (Air Pressure Vibrations) ka naam hai. Computer is aawaz ko kaise samajhta hai? Yahan kaam aata hai **OpenAI Whisper aur Log-Mel Spectrograms**!
Isay samajhne ke liye kisi Radio aur Piano ki misaal lein:
1. Raw Audio Waves (Continuous Lehar): Microphone hawa ke dabao ko record karta hai: 1 second mein 16,000 numbers (16 kHz Sample Rate). Agar aap 1 minute ki recording lein to 960,000 numbers ban jate hain. Model in raw numbers par direct kaam nahi kar sakta.
2. The Piano Notes / Fourier Transform (Salan Ke Masalay Alag Karna): Awaaz kayi mukhtalif frequencies ka murakkab hoti hai: mardana bhaari aawaz (Low pitch / Bass) aur bachon ki bareek aawaz (High pitch / Treble). Fourier Transform continuous lehar ko alag alag suron (frequencies) mein baant deta hai.
3. Log-Mel Spectrogram (Aawaz Ka X-Ray / Tasweer): Insani kaan frequencies ko linear nahi sunte; hum choti frequencies ke farq ko zyada wazeh mehsus karte hain. Mel Scale aawaz ko insani kaan ke mutabiq 80 ya 128 frequency bands ki ek **Tasweer (2D Spectrogram)** bana deta hai!
4. Whisper Architecture: Whisper is Mel-Spectrogram tasweer ko ek standard Vision/Audio Transformer Encoder mein daalta hai aur Decoder autoregressive tareeqay se text tokens generate karta hai. Whisper Urdu, Punjabi, aur Pashto ke accents ko hairat-angez accuracy ke sath transcribe karta hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Audio Sampling, Nyquist Theorem, aur Spectrogram Dimensions ka exact hisab lagayein.
Audio Sampling Parameters:
- Audio Duration $T = 30.0 \text{ seconds}$ (Whisper standard chunk length)
- Sampling Rate $f_s = 16,000 \text{ Hz}$ (16,000 samples per second)
- Nyquist-Shannon Theorem: Maximum captured frequency $= \frac{f_s}{2} = 8,000 \text{ Hz}$ (Covers human speech perfectly).

Step 1: Total Raw Audio Samples:
$N_{\text{samples}} = T \times f_s = 30.0 \times 16,000 = 480,000 \text{ samples}$.

Step 2: Short-Time Fourier Transform (STFT) Spectrogram Windowing:
- Window Size $= 400$ samples ($25 \text{ ms}$)
- Hop Size (Stride) $= 160$ samples ($10 \text{ ms}$)
- Mel Filterbank Channels $= 80$ frequency bins

Step 3: Compute Time Frames in Spectrogram:
$N_{\text{frames}} = \frac{N_{\text{samples}}}{\text{Hop Size}} = \frac{480,000}{160} = 3,000 \text{ time frames}$.
Final Spectrogram Tensor Shape:
$[80, 3000]$ (80 Mel frequency bins $\times$ 3000 time steps).
Raw audio jo pehle 480,000 unstructured numbers thi, ab ek neat $80 \times 3000$ matrix ban gayi jise Whisper Transformer Encoder direct 2x convolution downsampling ke baad 1500 audio tokens ke taur par process karta hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum raw audio wave synthesis, log-mel spectrogram extraction pipeline, aur Whisper transcription execution pattern implement karte hain.

```python
import math
import torch
import numpy as np

def generate_synthetic_audio_wave(duration_sec: float = 1.0, sample_rate: int = 16000) -> torch.Tensor:
    \"\"\"Synthesizes pure tone speech audio wave at 440 Hz (Concert A).\"\"\"
    t = torch.linspace(0, duration_sec, int(sample_rate * duration_sec))
    # Synthetic speech wave: fundamental frequency 220Hz + harmonics
    wave = 0.6 * torch.sin(2 * math.pi * 220 * t) + 0.3 * torch.sin(2 * math.pi * 440 * t)
    return wave

def compute_mock_log_mel_spectrogram(audio_wave: torch.Tensor, n_mels: int = 80, hop_length: int = 160) -> torch.Tensor:
    \"\"\"Transforms 1D raw audio waveform into 2D Log-Mel Spectrogram representation.\"\"\"
    # Number of frames = total_samples // hop_length
    num_frames = audio_wave.size(0) // hop_length
    
    # Simulate Mel filterbank projection: [n_mels, num_frames]
    # In production: torch.stft followed by torchaudio.transforms.MelSpectrogram
    synthetic_mel = torch.randn(n_mels, num_frames)
    # Log compression: log(mel + eps)
    log_mel = torch.log(torch.clamp(synthetic_mel.abs(), min=1e-5))
    return log_mel

# Execution test
if __name__ == "__main__":
    audio = generate_synthetic_audio_wave(duration_sec=2.0, sample_rate=16000)
    print(f"Raw Audio Waveform Tensor: Shape {list(audio.shape)} ({audio.numel()} total PCM samples)")

    spectrogram = compute_mock_log_mel_spectrogram(audio, n_mels=80, hop_length=160)
    print(f"Log-Mel Spectrogram Shape: {list(spectrogram.shape)} (80 Mel channels x 200 time frames)")
    print(f"Spectrogram Dynamic Range: [{spectrogram.min().item():.2f}, {spectrogram.max().item():.2f}] dB")
    print("\\nAudio successfully transformed into visual spectrogram tensor ready for Whisper Encoder!")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Feeding Audio with Wrong Sample Rate: Whisper model strictly 16 kHz sample rate expect karta hai. Agar aap 44.1 kHz (standard music MP3) direct pass kar dein bina resampling ke, to aawaz chipmunk jaisi tez ho jati hai aur transcription complete garbage aati hai. Hamesha pehle `torchaudio.transforms.Resample(orig_sr, 16000)` karein.
2. Silent Audio Causing Hallucination Loops: Whisper ki ajeeb aadat hai ke agar audio mein lambi khamoshi (silence / background hiss) ho to model pichle phrase ko bar bar repeat karne lagta hai ("Thank you for watching... Thank you for watching..."). Voice Activity Detection (VAD - e.g. Silero VAD) se khamoshi pehle trim karein.
3. Not Using `faster-whisper` (CTranslate2): Standard Whisper Python code bohot slow chalta hai. Production mein hamesha `faster-whisper` use karein jo CTranslate2 INT8 quantization use karti hai aur 4x tez chalti hai.

Zero-GPU Tip:
`faster-whisper` CPU par OpenMP aur AVX-512 vectorization ke sath 1 minute ki audio ko sirf 1.5 seconds mein transcribe kar leti hai on a standard laptop CPU with zero GPU hardware.

Self-Check Questions:
1. Continuous sound wave ko Log-Mel Spectrogram mein tabdeel karne ka mathematical maqsad kya hota hai?
2. Nyquist-Shannon sampling theorem ke mutabiq 16 kHz sample rate par maximum kaun si frequency capture ho sakti hai?
3. Voice Activity Detection (VAD) audio pipeline mein Whisper hallucination loops ko kaise rokti hai?

What to Build Next:
Ek Local Speech-to-Text CLI Tool banayein jo laptop microphone se 5 second ki aawaz record kare, Silero VAD se silence trim kare, aur `faster-whisper` se Roman Urdu / English text print kare."""

# ==============================================================================
# LESSON 12.5: Video AI & Temporal Understanding: Keyframe Sampling
# ==============================================================================
LESSON_CONTENT['12.5'] = r"""### Part 1: Mental Model & South Asian Analogy
Images 2-dimensional (Space: Height $\times$ Width) hoti hain, jabke Video 3-dimensional (Space + Time) hoti hai. Ek 5-minute ki video mein 9,000 frames (tasweerein) hoti hain! Agar aap tamam 9,000 frames ko LLM mein feed karenge to context window foran explode kar jayegi aur hazaron dollars kharch honge. Yahan se shuru hota hai **Video AI & Temporal Understanding (Keyframe Sampling & Dynamic Pooling)**!
Isay samajhne ke liye kisi Cricket Match ke Highlights Package aur TV Umpire ki misaal lein:
1. The Full 8-Hour Match vs 10-Minute Highlights: Aam insaan poora 8 ghantay ka test match nahi dekhta; woh sirf 10 minute ke highlights dekhta hai jisme har chauka, chhakka, aur wicket ka shot hota hai.
2. Uniform Keyframe Sampling (Har 2 Second Baad Ek Photo): Sab se sada tareeqa yeh hai ke video mein se har 2 second baad 1 frame utha liya jaye (FPS = 0.5). 60 second ki video mein se sirf 30 frames aate hain.
3. Dynamic Scene-Change Sampling (Shot Boundary Detection): Samajhdaar editor tabhi frame uthata hai jab camera ka scene badlay: maslan bowler run-up par tha, phir shot laga, phir crowd ka reaction aaya. Har visual shift par naya frame sample hota hai.
4. Temporal Cross-Attention (Waqt Ka Silsila Samajhna): Model sirf alag alag tasweerein nahi dekhta; woh unhe waqt ke silsilay (Time Axis) par jorta hai: "Pehle glass table par tha (Frame 1), phir haath laga (Frame 5), phir glass zameen par gir kar toot gaya (Frame 10)." Model samajhta hai ke waqea kya hua!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Video Frame Sampling, Compression Ratio, aur Token Budgeting ka exact hisab lagayein.
Video Specifications:
- Duration $T = 180 \text{ seconds}$ (3 Minutes video clip)
- Native Framerate $= 30 \text{ frames per second (fps)}$
- Native Total Frames $= 180 \times 30 = 5,400 \text{ frames}$.
- Raw Uncompressed Video Size ($1080p$ RGB):
  $5400 \times (1920 \times 1080 \times 3) \text{ Bytes} \approx 33.5 \text{ GB}$!

Scenario A: Direct Full-Frame Token Ingestion (Impossible)
If each frame takes 256 VLM tokens:
Total Tokens $= 5400 \times 256 = 1,382,400 \text{ tokens}$ (Exceeds almost all context windows, costs \$5 per query!).

Scenario B: Uniform Keyframe Sampling ($1 \text{ frame per 4 seconds}$)
Sample Rate $f_{\text{sample}} = 0.25 \text{ fps}$.
Total Sampled Keyframes:
$N_{\text{keyframes}} = 180 \times 0.25 = 45 \text{ frames}$.
Compression Ratio:
$\frac{5400}{45} = 120\times \text{ Frame Reduction}$!

Token Footprint Calculation:
- Keyframes Count $= 45$
- Visual Tokens per Keyframe (downsampled via spatial pooling to 64 tokens):
  $\text{Tokens per frame} = 64$
Total Video Token Budget:
$\text{Total Tokens} = 45 \times 64 = 2,880 \text{ tokens}$!
3 minute ki poori video sirf 2,880 tokens mein pack ho gayi jo aasaani se kisi bhi LLaMA-3.2-Vision ya Gemini context window mein fit aa jati hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum uniform temporal keyframe selector, frame differencing motion detector, aur temporal sequence batcher implement karte hain.

```python
import numpy as np
from typing import List, Tuple

class VideoTemporalSampler:
    \"\"\"Extracts informative keyframes from video stream using motion thresholding.\"\"\"
    def __init__(self, target_fps: float = 0.5, motion_threshold: float = 0.15) -> None:
        self.target_fps = target_fps
        self.motion_threshold = motion_threshold

    def sample_keyframes_uniform(self, total_frames: int, native_fps: float = 30.0) -> List[int]:
        \"\"\"Selects equidistant temporal indices across video timeline.\"\"\"
        interval = int(native_fps / self.target_fps)
        indices = list(range(0, total_frames, max(interval, 1)))
        return indices

    def detect_scene_changes(self, frame_features: List[np.ndarray]) -> List[int]:
        \"\"\"Selects frames where consecutive visual difference exceeds motion threshold.\"\"\"
        selected_indices = [0]  # Always keep initial frame
        for i in range(len(frame_features) - 1):
            # Compute frame-to-frame L2 distance
            delta = float(np.linalg.norm(frame_features[i + 1] - frame_features[i]))
            if delta > self.motion_threshold:
                selected_indices.append(i + 1)
        return selected_indices

# Execution test
if __name__ == "__main__":
    np.random.seed(42)
    sampler = VideoTemporalSampler(target_fps=0.5, motion_threshold=0.20)
    
    # 60-second video at 30 fps = 1800 native frames
    native_frames = 1800
    uniform_indices = sampler.sample_keyframes_uniform(native_frames, native_fps=30.0)
    print(f"Uniform Sampling: {native_frames} native frames -> {len(uniform_indices)} keyframes selected (indices: {uniform_indices[:5]}...)")

    # Simulate 10 consecutive frame feature vectors with a sudden scene cut at frame 5
    simulated_feats = [np.array([0.1, 0.1]) for _ in range(5)] + [np.array([0.9, 0.8]) for _ in range(5)]
    cuts = sampler.detect_scene_changes(simulated_feats)
    print(f"\\nDynamic Scene Cut Detection: Identified shot transition at frame indices: {cuts}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Decoding Raw Video Frames on GPU (PCIe Bandwidth Jam): Video file ko CPU par decode karke uncompressed frames GPU ko bhejne se PCIe bus jam ho jati hai. Hamesha hardware video decoders (NVIDIA NVDEC / PyAV) use karein jo direct GPU VRAM mein compressed MP4 decode karte hain.
2. Missing Timestamp Metadata per Keyframe: Model ko 30 frames de dena bina yeh bataye ke kaun sa frame kis second ka hai temporal reasoning ko tabah karta hai. Hamesha har frame ke sath timestamp tag embed karein: `[Frame at 00:04], [Frame at 00:08]`.
3. Over-Sampling Static Camera Feeds: Agar security camera ki video mein 1 ghantay tak koi harkat na hui ho to 1,000 frames sample karna be-faida hai. Motion-based thresholding se static frames filter karein.

Zero-GPU Tip:
Keyframe selection, temporal index calculation, aur frame differencing algorithms pure CPU operations hain. OpenCV (`cv2`) ya PyAV CPU par 1080p MP4 file se 30 keyframes sirf 0.4 seconds mein extract kar leti hai.

Self-Check Questions:
1. Video analysis mein Uniform Sampling aur Dynamic Scene Cut Sampling mein kya farq hota hai?
2. 5,400 raw frames ko 45 keyframes par compress karne se token budget kaise preserve hota hai?
3. Temporal reasoning ke liye frame ke sath exact timestamp metadata embed karna kyun zaroori hai?

What to Build Next:
Ek Video Summarizer Pipeline banayein jo ek sample MP4 video load kare, OpenCV se har 5 second baad keyframe extract kare, unhe horizontal contact sheet image mein tile kare, aur Gemini 2.0 Flash se visual summary le."""

# ==============================================================================
# LESSON 12.6: Module 12 Capstone: Multimodal Intelligence Engine
# ==============================================================================
LESSON_CONTENT['12.6'] = r"""### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne Multimodal AI ke tamam ahem sutoon (CLIP contrastive matching, SigLIP VLM projectors, Document visual OCR extraction, Whisper audio processing, aur Video temporal sampling) mukammal kar liye hain. Ab waqt hai aapke **Pehle Complete Multimodal Intelligence Engine** ka!
Is Capstone project ka zehni khaka kisi Bare Modern Media Intelligence & Security Control Center jaisa hai:
1. The Omnipresent Intake (Har Qisam Ka Data): Control center par kisi bhi format ka raw data aa sakta hai: customer ki aawaz ka voice note (Audio WAV), kaghazi tax receipt ki photo (Image PNG), ya CCTV security camera ki recording (Video MP4).
2. The Specialized Encoders:
   - Audio Modality Router: Whisper se guzar kar verified transcript banata hai.
   - Document Modality Router: Visual OCR se structured Pydantic JSON extract karta hai.
   - Video Modality Router: Temporal keyframes sample karke event trajectory banata hai.
3. The Central Multimodal Brain (Unified Intelligence Core): Tamam alag alag modalities ek unified representation mein condense ho kar final reasoning model ke hawale hoti hain jo comprehensive multimodal intelligence report generate karta hai.

Yeh Capstone project enterprise multimodal AI system ka pinnacle hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Multimodal Cross-Modal Routing aur Latency Budgeting ka exact hisab lagayein.
Incoming Multi-Modal Case:
An e-commerce dispute packet contains:
1. Customer Voice Note: 15 seconds audio
2. Receipt Image: 1 JPEG photo
3. Unboxing Video: 30 seconds MP4 clip

Sequential Latency Waterfall vs Parallel Dispatch:
Scenario A: Sequential Execution
- Whisper Audio Transcription: $1.2 \text{ seconds}$
- Receipt Visual Extraction: $1.5 \text{ seconds}$
- Video Keyframe Extraction & VLM: $2.8 \text{ seconds}$
Total Sequential Latency:
$T_{\text{seq}} = 1.2 + 1.5 + 2.8 = 5.5 \text{ seconds}$.

Scenario B: Asynchronous Parallel Dispatch (`asyncio.gather`)
All three modality pipelines execute concurrently on separate worker threads:
$T_{\text{parallel}} = \max(T_{\text{audio}}, T_{\text{image}}, T_{\text{video}}) + T_{\text{fusion}}$
$T_{\text{parallel}} = \max(1.2, 1.5, 2.8) + 0.1 = 2.8 + 0.1 = 2.9 \text{ seconds}$!
Latency reduced from $5.5\text{s} \to 2.9\text{s}$ ($\approx 47\% \text{ Faster Response Time}$) with zero loss in extraction fidelity!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete Multimodal Intelligence Engine implement karte hain: multi-modal routing, parallel modality processors, structured cross-modal aggregation, aur comprehensive dispute resolution report generation.

```python
import asyncio
import time
from typing import Dict, Any, List
from pydantic import BaseModel

class MultimodalCaseInput(BaseModel):
    case_id: str
    audio_path: str | None = None
    receipt_image_path: str | None = None
    video_path: str | None = None

class MultimodalIntelligenceReport(BaseModel):
    case_id: str
    voice_transcript: str
    receipt_data: Dict[str, Any]
    video_events: List[str]
    dispute_verdict: str
    processing_time_ms: float

class MultimodalIntelligenceEngine:
    \"\"\"Production multi-modal orchestrator running parallel specialized sub-pipelines.\"\"\"
    async def process_audio(self, audio_path: str) -> str:
        \"\"\"Simulates Whisper transcription pipeline.\"\"\"
        await asyncio.sleep(0.08)
        return "Customer voice note: Parcel arrived completely crushed and water damaged."

    async def process_receipt_image(self, image_path: str) -> Dict[str, Any]:
        \"\"\"Simulates Visual VLM Document OCR parser.\"\"\"
        await asyncio.sleep(0.10)
        return {"vendor": "Al-Madina Electronics", "item": "Smart Watch", "paid_pkr": 8500.0}

    async def process_video_clip(self, video_path: str) -> List[str]:
        \"\"\"Simulates Keyframe Temporal Vision Sampler.\"\"\"
        await asyncio.sleep(0.12)
        return [
            "00:02 - Courier delivers sealed cardboard box",
            "00:15 - Box opened showing shattered glass screen"
        ]

    async def analyze_dispute_case(self, case: MultimodalCaseInput) -> MultimodalIntelligenceReport:
        t0 = time.perf_counter()

        # Execute all available modality pipelines concurrently
        tasks = []
        tasks.append(self.process_audio(case.audio_path) if case.audio_path else asyncio.sleep(0, result=""))
        tasks.append(self.process_receipt_image(case.receipt_image_path) if case.receipt_image_path else asyncio.sleep(0, result={}))
        tasks.append(self.process_video_clip(case.video_path) if case.video_path else asyncio.sleep(0, result=[]))

        audio_res, receipt_res, video_res = await asyncio.gather(*tasks)

        # Unified Multimodal Reasoning Decision Rule
        verdict = "Claim APPROVED: Video evidence and voice transcript corroborate transit physical damage."

        elapsed_ms = (time.perf_counter() - t0) * 1000.0
        return MultimodalIntelligenceReport(
            case_id=case.case_id,
            voice_transcript=audio_res,
            receipt_data=receipt_res,
            video_events=video_res,
            dispute_verdict=verdict,
            processing_time_ms=round(elapsed_ms, 2)
        )

# Execution test
if __name__ == "__main__":
    async def run_capstone():
        engine = MultimodalIntelligenceEngine()
        sample_case = MultimodalCaseInput(
            case_id="DISPUTE_2026_901",
            audio_path="customer_voice_note.wav",
            receipt_image_path="invoice_scan.png",
            video_path="unboxing_clip.mp4"
        )

        report = await engine.analyze_dispute_case(sample_case)
        print("Multimodal Intelligence Engine Report Generated!")
        print(f"Case ID:         {report.case_id}")
        print(f"Latency:         {report.processing_time_ms} ms (Parallel Async Execution)")
        print(f"Audio Output:    '{report.voice_transcript}'")
        print(f"Receipt Parsed:  {report.receipt_data}")
        print(f"Video Timeline:  {report.video_events}")
        print(f"Final Decision:  {report.dispute_verdict}")

    asyncio.run(run_capstone())
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Running Heavy Modalities Serially: Audio, image, aur video ko ek ke baad ek chalane se user ko 10 second wait karna parta hai. Hamesha `asyncio.gather` se tamam sub-pipelines parallel chalayein.
2. Incompatible Modality Synchronization: Video frames aur audio timestamps ko sync na karne se model confuse ho jata hai ke kaun si aawaz kis frame par aayi thi. Hamesha synchronized PTS (Presentation Time Stamp) clock use karein.
3. Lack of Fallback When Single Modality Fails: Agar video corrupt ho jaye to poora dispute process crash nahi hona chahiye. Partial modalities (Audio + Image) ke sath graceful degradation support karein.

Zero-GPU Tip:
Multimodal case orchestration, asynchronous pipeline coordination, aur report formatting pure CPU bound Python operations hain. Real models ke liye lightweight multimodal APIs (Gemini 2.0 Flash) connect karke aap zero local GPU compute par poora system serve kar sakte hain.

Self-Check Questions:
1. Asynchronous Parallel Dispatch multimodal latency ko sequential execution ke muqablay kyun aadha kar deta hai?
2. Cross-modal dispute resolution mein multiple modalities (Voice + Image + Video) hallucination ko kaise khatam karti hain?
3. Partial modality failure hone par graceful degradation kaise implement ki jati hai?

What to Build Next:
Ek Full-Stack Multimodal Dashboard banayein with a drag-and-drop interface for audio, image, and video files, real-time progress indicators, aur verified intelligence report export."""
