# seed_modules_phase5.py
# Phase 5 Modules: 12, 13, 14 (18 comprehensive lessons)
# Focus: Multimodal AI & Vision, Local AI & Edge Devices, Enterprise Capstone & Career Launch

def get_modules_phase5():
    return [
        # =========================================================================
        # MODULE 12: Multimodal AI & Vision
        # =========================================================================
        {
            "phase_slug": "phase-5-specialization-capstone",
            "module_number": 12,
            "slug": "multimodal-ai-and-vision",
            "real_world_deliverable": "Multimodal Document & Video Intelligence Engine with Visual Grounding",
            "zero_gpu_recipe": {
                'platform': 'Google AI Studio (Gemini 2.0 Flash) / Colab Free T4',
                'vram_required': '0 GB (via Gemini API) / 8 GB (Local Moondream / Florence-2)',
                'estimated_cost': '$0.00 Free',
                'compute_units_tip': 'Gemini 2.0 Flash on Google AI Studio provides 1,500 free multimodal requests per day with 1M context for video, audio and image processing.',
                'one_click_command': 'pip install google-genai pillow opencv-python transformers'
            },
            "title": "Module 12: Multimodal AI & Vision",
            "weeks_range": "Weeks 17-18",
            "estimated_hours": 16,
            "learning_outcomes": [
                "Foundations of Vision-Language Models (VLMs): CLIP contrastive learning aur joint embedding spaces",
                "Vision Encoders & Cross-Attention Projectors: SigLIP, Linear projection vs MLP projection aur LLaVA architecture",
                "Document & Invoice OCR Intelligence: Visual table extraction, bounding boxes aur key-value parsing",
                "Audio & Speech AI: Whisper acoustic features, Mel-spectrograms, CTC loss aur audio-LLM tokenization",
                "Video understanding: Keyframe sampling, temporal attention mechanisms aur video question answering",
                "End-to-end multimodal agent pipelines integrating images, diagrams, audio transcripts aur text"
            ],
            "practical_tasks": [
                "CLIP zero-shot image classification aur visual search engine implement karein",
                "Florence-2 / Moondream VLM use karke invoices aur receipts se structured JSON extract karein",
                "Whisper model se Roman Urdu audio speech ko stream aur transcribe karein",
                "OpenCV video frame extraction pipeline build karein for temporal video search",
                "Multimodal RAG pipeline design karein jo PDF ke diagrams aur tables ko visually retrieve kare"
            ],
            "resources": [
                {"title": "OpenAI CLIP: Learning Transferable Visual Models", "url": "https://arxiv.org/abs/2103.00020"},
                {"title": "LLaVA: Visual Instruction Tuning", "url": "https://llava-vl.github.io/"},
                {"title": "Google SigLIP: Sigmoid Loss for Language Image Pre-Training", "url": "https://arxiv.org/abs/2303.15343"},
                {"title": "OpenAI Whisper Speech Recognition", "url": "https://github.com/openai/whisper"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 12 Multimodal Architecture
  img[Visual Input: Image / Video Frame] $browser -> vis_enc[Vision Encoder: SigLIP / ViT] $cpu
  vis_enc -> proj[Linear / MLP Projector] $layers
  audio[Audio Input: Speech WAV] $terminal -> whisper[Whisper Encoder] $cpu
  proj & whisper -> llm[Multimodal LLM Backbone] $brain *
  llm -> out[Structured Visual Analysis & Grounding] $server""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "ai-graduate",
            "order_index": 12,
            "lessons": [
                {
                    "lesson_code": "12.1",
                    "slug": "vision-language-foundations-clip",
                    "title": "Foundations of Vision-Language Models: CLIP & Contrastive Learning",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, 2021 se pehle Computer Vision aur NLP do bilkul alag alag jaziray (islands) the! Computer Vision models (ResNet, EfficientNet) 1,000 fixed ImageNet classes predict karte the, jabke NLP models text par kaam karte the.

OpenAI ke **CLIP (Contrastive Language-Image Pre-training)** ne in dono dunyaon ko hamesha ke liye mila diya!
CLIP ka core concept bohot khubsurat hai: **Contrastive Learning in a Shared Joint Embedding Space**.
CLIP kaise train hota hai?
1. 400 Million (Image, Text Caption) pairs internet se liye gaye.
2. Image ko ek **Vision Encoder** (ViT ya ResNet) se pass karke vector $I_i$ banaya jata hai ($d=512$).
3. Text caption ko ek **Text Encoder** (Transformer) se pass karke vector $T_j$ banaya jata ($d=512$).
4. Ek batch mein $N$ images aur $N$ texts hote hain ($N \\times N$ similarity matrix).
5. Loss function (InfoNCE / Symmetric Cross Entropy) ka target yeh hota hai ke diagonal elements ($I_i \\cdot T_i$) ki cosine similarity maximum ho (close to 1), aur non-diagonal elements ($I_i \\cdot T_j$) ki similarity 0 ke qareeb ho!

Iska jadu: CLIP bina kisi training ke **Zero-Shot Classifier** ban jata hai! Aap prompt likhein "A photo of a Lahori samosa" aur CLIP lakhon images mein se samosa dhoond kar nikal lega!""",
                    "english_summary": "Understand OpenAI CLIP's contrastive learning objective (InfoNCE), dual-encoder architecture, shared vector embedding space, and zero-shot visual classification.",
                    "code_example": """import torch
import torch.nn.functional as F

def clip_contrastive_loss(image_embeddings: torch.Tensor, text_embeddings: torch.Tensor, temperature: float = 0.07):
    \"\"\"Calculates symmetric CLIP contrastive InfoNCE loss across a batch of N pairs.\"\"\"
    # 1. Normalize embeddings to unit hypersphere
    image_norm = F.normalize(image_embeddings, p=2, dim=-1)
    text_norm = F.normalize(text_embeddings, p=2, dim=-1)
    
    # 2. Compute cosine similarity matrix (N x N) scaled by temperature
    logits = torch.matmul(image_norm, text_norm.t()) / temperature
    
    # 3. Ground truth targets: Diagonal elements (i == j)
    labels = torch.arange(len(image_embeddings), device=image_embeddings.device)
    
    # 4. Symmetric cross-entropy loss (Image-to-Text and Text-to-Image)
    loss_img = F.cross_entropy(logits, labels)
    loss_txt = F.cross_entropy(logits.t(), labels)
    return (loss_img + loss_txt) / 2.0

# Batch of 4 images and 4 matching text captions
img_vecs = torch.randn(4, 512)
txt_vecs = torch.randn(4, 512)
loss = clip_contrastive_loss(img_vecs, txt_vecs)
print(f"Computed CLIP Contrastive Loss: {loss.item():.4f}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: CLIP Joint Contrastive Embedding Space
  img[Image Input] $browser -> img_enc[Vision Encoder ViT] $cpu
  txt[Text Caption] $terminal -> txt_enc[Text Encoder Transformer] $cpu
  img_enc -> img_vec[Normalized Image Vector I] $layers
  txt_enc -> txt_vec[Normalized Text Vector T] $layers
  img_vec & txt_vec -> mat[N x N Cosine Similarity Matrix] $database *
  mat -> loss[InfoNCE Loss: Maximize Diagonal Matches] $brain""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "CLIP Paper (Radford et al., 2021)", "url": "https://arxiv.org/abs/2103.00020"},
                        {"title": "OpenCLIP Implementation", "url": "https://github.com/mlfoundations/open_clip"}
                    ],
                    "xp_reward": 25,
                    "order_index": 1
                },
                {
                    "lesson_code": "12.2",
                    "slug": "cross-attention-projectors-siglip",
                    "title": "Vision Encoders & Projectors: SigLIP & Modern VLM Architecture",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, modern Vision-Language Models (jaise LLaVA, Qwen2-VL, aur Gemini) CLIP ke dual encoders se aage nikal chuke hain. Wo images ko sirf classify nahi karte balki images ke baare mein insani rawani ke sath guftagu karte hain!

Modern VLM ka architecture teen ahem hisson par mushtamil hota hai:
1. **Vision Encoder (SigLIP / ViT)**:
   Google ka **SigLIP (Sigmoid Loss for Language Image Pre-training)** standard Softmax ki jagah simple pairwise sigmoid loss use karta hai, jis se batch size normalization ki zaroorat khatam ho jati hai aur vision features bohot rich bante hain.
2. **Cross-Modal Projector**:
   Vision encoder image ko 16x16 patches mein tod kar har patch ka vector banata hai (maslan 576 tokens, har token dimension 1024). Lekin LLM ka input dimension 4096 hota hai!
   Is mismatch ko bridge karne ke liye ek **Projector** (2-layer MLP with GELU activation) use hota hai jo image tokens ko LLM ke text embedding space mein translate karta hai!
3. **Autoregressive LLM Backbone**:
   LLM ke liye image tokens bilkul aam text tokens ki tarah ban jate hain! System prompt + Image Tokens + User Query ek single sequence mein concatenate ho kar LLM ke attention blocks se guzar kar answer generate karte hain.""",
                    "english_summary": "Architect modern Vision-Language Models (VLMs) utilizing SigLIP vision backbones and MLP cross-modal projectors to map 2D image patch tokens directly into LLM embedding space.",
                    "code_example": """import torch
import torch.nn as nn

class VisionProjector(nn.Module):
    \"\"\"2-Layer MLP Cross-Modal Projector (LLaVA-1.5 Style).\"\"\"
    def __init__(self, vision_dim: int = 1024, llm_dim: int = 4096):
        super().__init__()
        self.linear1 = nn.Linear(vision_dim, llm_dim)
        self.act = nn.GELU()
        self.linear2 = nn.Linear(llm_dim, llm_dim)
        
    def forward(self, visual_tokens: torch.Tensor) -> torch.Tensor:
        # Input shape: [batch, num_patches (e.g. 576), vision_dim]
        # Output shape: [batch, num_patches, llm_dim]
        return self.linear2(self.act(self.linear1(visual_tokens)))

# Simulate 576 image patch tokens coming from SigLIP ViT-SO400M
projector = VisionProjector(vision_dim=1024, llm_dim=4096)
raw_patches = torch.randn(1, 576, 1024)
projected_tokens = projector(raw_patches)

print(f"Raw visual patch tokens: {raw_patches.shape}")
print(f"Projected tokens ready for LLM attention: {projected_tokens.shape}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Modern VLM (LLaVA) Architecture
  image[Input Image 336x336] $browser -> vit[SigLIP ViT Vision Encoder] $cpu
  vit -> patches[576 Visual Patch Tokens 1024-d] $layers
  patches -> mlp[2-Layer MLP Projector] $server *
  mlp -> llm_tokens[Visual Tokens in 4096-d LLM Space] $database
  prompt[User Prompt: 'Describe chart'] $terminal -> tokenizer[Text Tokenizer] $code
  tokenizer & llm_tokens -> llm[LLM Backbone Llama / Mistral] $brain
  llm -> output[Text Response Stream] $terminal""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "SigLIP Research Paper", "url": "https://arxiv.org/abs/2303.15343"},
                        {"title": "LLaVA Architecture Overview", "url": "https://github.com/haotian-liu/LLaVA"}
                    ],
                    "xp_reward": 25,
                    "order_index": 2
                },
                {
                    "lesson_code": "12.3",
                    "slug": "document-invoice-ocr-donut",
                    "title": "Document & Invoice Intelligence: Visual OCR & Structured Extraction",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, real-world enterprise applications mein sab se aam problem PDFs, scanned receipts, utility bills, aur complex tabular financial invoices ko parse karna hota hai.

Purana tarika kya tha?
1. Pehle Tesseract OCR se ganda text extract karo (jisme columns aur layout mess up ho jate the).
2. Phir mushkil Regex likho jo har invoice format ke change hone par phat jata tha!

Modern AI approach **OCR-free Visual Document Intelligence** hai (jaise Microsoft Florence-2, Donut, aur Gemini 2.0 Flash):
- Model direct image ke pixels ko dekhta hai.
- Yeh spatial relationships ko samajhta hai (maslan: "Total Amount" ke theek samne ya neechay likha hua number hi total hai chahe koi divider line na ho).
- Direct **Pydantic Structured JSON** output produce karta hai jisme invoice number, line items, tax rate, aur total amounts verified format mein milte hain.""",
                    "english_summary": "Extract structured data from complex invoices, receipts, and tabular PDFs using end-to-end Visual Document Models without brittle OCR preprocessing.",
                    "code_example": """from pydantic import BaseModel, Field
from typing import List

# 1. Define Strict Pydantic Schema for Invoice Extraction
class LineItem(BaseModel):
    description: str = Field(description="Item name or service rendered")
    quantity: int = Field(description="Quantity purchased")
    unit_price: float = Field(description="Price per unit in PKR or USD")
    total_price: float = Field(description="Total price for this line item")

class InvoiceData(BaseModel):
    invoice_number: str
    vendor_name: str
    issue_date: str
    line_items: List[LineItem]
    subtotal: float
    tax_amount: float
    total_due: float

# In production: Pass image bytes + schema to Gemini 2.0 Flash or Florence-2
sample_extracted = InvoiceData(
    invoice_number="INV-2026-0042",
    vendor_name="Systems Limited Lahore",
    issue_date="2026-10-15",
    line_items=[
        LineItem(description="Cloud GPU Hosting T4", quantity=10, unit_price=1200.0, total_price=12000.0),
        LineItem(description="LLM Inference Setup", quantity=1, unit_price=25000.0, total_price=25000.0)
    ],
    subtotal=37000.0,
    tax_amount=5920.0,
    total_due=42920.0
)

print(sample_extracted.model_dump_json(indent=2))""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Document Visual Intelligence Pipeline
  pdf[Scanned PDF / Receipt Image] $browser -> vlm[Visual Document Model Florence-2 / Gemini] $cpu
  vlm -> visual_layout[Spatial Layout & Table Understanding] $layers
  visual_layout -> schema[Pydantic JSON Validation Engine] $lock *
  schema -> clean_json[Structured Validated Invoice JSON] $server""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Donut: Document Understanding Transformer", "url": "https://arxiv.org/abs/2111.15664"},
                        {"title": "Microsoft Florence-2 Vision Foundation Model", "url": "https://huggingface.co/microsoft/Florence-2-large"}
                    ],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "12.4",
                    "slug": "whisper-speech-audio-llms",
                    "title": "Audio & Speech Processing: OpenAI Whisper & Audio-LLM Integrations",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, audio speech processing mein raw waveform (16,000 samples per second) ko direct neural network mein feed karna bohot inefficient hota hai.

OpenAI ka **Whisper** standard audio pipeline follow karta hai:
1. **Log-Mel Spectrogram**: Audio ko 25-millisecond windows (with 10ms hop length) mein divide karke Fourier Transform (FFT) apply kiya jata hai, aur frequencies ko human ear ki sensitivity (Mel scale, 80 ya 128 channels) par map kiya jata hai.
2. **Audio Encoder**: 2D Mel-spectrogram ko convolutional layers aur Transformer blocks se process karke acoustic representations banata hai.
3. **Autoregressive Text Decoder**: Multi-lingual text tokens predict karta hai with timestamp tokens (`<|0.00|>`, `<|2.40|>`) jo word-level alignments provide karte hain.

Whisper Roman Urdu aur Pakistani accents par bohot shandaar kaam karta hai jab aap initial prompt parameter mein thora context pass karein!""",
                    "english_summary": "Understand speech-to-text processing using OpenAI Whisper, Log-Mel spectrogram feature extraction, and timestamp alignment tokens for audio-LLM architectures.",
                    "code_example": """import numpy as np

def compute_mock_mel_spectrogram(audio_signal: np.ndarray, num_mel_bins: int = 80) -> np.ndarray:
    \"\"\"Conceptual representation of transforming 1D audio waveform into 2D Mel Spectrogram.\"\"\"
    # Window framing: 25ms window, 10ms hop
    hop_length = 160 # 10ms at 16kHz
    num_frames = len(audio_signal) // hop_length
    
    # 2D feature matrix: [Frequency Channels, Time Frames]
    mel_spectrogram = np.random.randn(num_mel_bins, num_frames)
    return mel_spectrogram

# 2 seconds of 16kHz audio waveform
audio = np.random.randn(32000)
mel = compute_mock_mel_spectrogram(audio)

print(f"Input Raw Audio Samples: {len(audio):,}")
print(f"Generated Mel-Spectrogram shape: {mel.shape} (80 mel bins x {mel.shape[1]} time frames)")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Whisper Speech Processing Flow
  raw_wav[1D Audio Waveform 16kHz] $terminal -> stft[Short-Time Fourier Transform FFT] $cpu
  stft -> mel[80-Channel Log-Mel Spectrogram] $layers
  mel -> enc[Whisper Audio Encoder ViT] $server *
  enc -> dec[Autoregressive Decoder + Timestamp Tokens] $brain
  dec -> urdu_txt[Transcribed Roman Urdu Text with Timestamps] $terminal""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "OpenAI Whisper Paper", "url": "https://arxiv.org/abs/2212.04356"},
                        {"title": "Hugging Face Whisper Fine-Tuning Guide", "url": "https://huggingface.co/blog/fine-tune-whisper"}
                    ],
                    "xp_reward": 25,
                    "order_index": 4
                },
                {
                    "lesson_code": "12.5",
                    "slug": "video-understanding-temporal-attention",
                    "title": "Video AI & Temporal Understanding: Keyframe Sampling & Dynamic Attention",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, video dar-asal static images ka sequence hota hai jo waqt (time dimension) ke sath badalta hai. Agar ek 10 minute ki video 30 frames per second (fps) par ho, to total 18,000 frames bante hain! Agar har frame ko VLM mein bhejenge to context window explode ho jayegi aur hazaron dollars burn honge.

Modern Video AI do intelligent sampling strategies use karti hai:
1. **Scene Change & Keyframe Extraction**: OpenCV ya ffmpeg ke zariye sirf wo frames extract kiye jate hain jahan camera angle ya screen content badalta hai (Color Histogram Differences / Optical Flow thresholding). Aam tor par 1 fps ya 0.5 fps sample rate 95% information retain karti hai.
2. **Temporal Attention**: Video tokens ko 3D grid $(T, H, W)$ mein treat kiya jata hai. Model spatial attention (frame ke andar cheezein) aur temporal attention (frame $t_1$ se $t_2$ ke darmiyan action ka sequence) ko aapas mein correlate karta hai.

Is technique se aap 1-hour lambi lecture videos ya CCTV footage ko digest karke exact second par event dhoond sakte hain!""",
                    "english_summary": "Process long-form video intelligence using OpenCV keyframe sampling, scene detection, and temporal cross-attention to analyze events across time.",
                    "code_example": """import cv2
import numpy as np

def extract_uniform_keyframes(video_path: str, max_frames: int = 8) -> list:
    \"\"\"Extracts uniformly spaced keyframes from a video file for VLM processing.\"\"\"
    # Mocking video frame extraction logic
    total_frames = 1800 # 60 seconds at 30fps
    frame_indices = np.linspace(0, total_frames - 1, max_frames, dtype=int)
    
    extracted_frames = []
    for idx in frame_indices:
        timestamp_sec = idx / 30.0
        # In production: cap.set(cv2.CAP_PROP_POS_FRAMES, idx); ret, frame = cap.read()
        extracted_frames.append({"frame_idx": int(idx), "timestamp_sec": round(timestamp_sec, 2)})
        
    return extracted_frames

frames = extract_uniform_keyframes("lecture_ai_ustaad.mp4", max_frames=6)
for f in frames:
    print(f"Extracted Frame at {f['timestamp_sec']}s (Index: {f['frame_idx']})")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Video Temporal Sampling Pipeline
  video[Raw Video Stream 30 FPS] $browser -> sampler[Uniform / Scene-Change Sampler] $cpu
  sampler -> frames[Keyframes: 1 FPS (e.g. 10 frames)] $layers
  frames -> temporal_attn[Temporal & Spatial Cross-Attention] $brain *
  temporal_attn -> qa_engine[Timestamp-Grounded Video Q&A] $server""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Google VideoPrism Foundation Model", "url": "https://arxiv.org/abs/2402.13217"},
                        {"title": "OpenCV Video Processing in Python", "url": "https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "12.6",
                    "slug": "capstone-multimodal-intelligence-engine",
                    "title": "Module 12 Capstone: Multimodal Document & Video Intelligence Engine",
                    "duration_minutes": 50,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, congratulations! Aap Module 12 ke Capstone project par pohanch chuke hain. Is capstone mein aap ek unified **Multimodal Intelligence Engine** develop karenge jo text, complex visual documents (diagrams/tables), aur audio recordings teeno ko ek sath ingest aur analyze karega!

Aapka Capstone Architecture:
1. **Visual Document Parser**: Complex technical PDF reports se tables aur flowcharts visually crop karke multimodal embeddings generate karega.
2. **Audio Transcription Layer**: Voice queries ya meeting recordings ko Whisper ke zariye timestamped text mein convert karega.
3. **Cross-Modal Retrieval**: User text ya image prompt bhej sakta hai ("Find me the quarterly revenue chart in this 50-page PDF") aur engine exact visual page crop return karega.
4. **Structured JSON Synthesizer**: Final answer visual grounding (bounding box coordinates) aur verified citations ke sath return karega.
5. **Interactive UI**: Svelte 5 ya Streamlit interface jahan user PDF upload kare, audio record kare, aur live streaming answers visual highlights ke sath dekhe!""",
                    "english_summary": "Assemble the Module 12 Capstone: a production Multimodal Document and Video Intelligence Engine combining visual table extraction, Whisper audio transcription, and cross-modal retrieval.",
                    "code_example": """# Capstone Multimodal Engine Integration Pipeline
from typing import Dict, Any

class MultimodalIntelligenceEngine:
    def __init__(self):
        print("Multimodal Engine initialized: Vision + Audio + LLM active.")
        
    def process_query(self, text_query: str, visual_asset: str = None, audio_asset: str = None) -> Dict[str, Any]:
        result = {
            "query": text_query,
            "modalities_analyzed": ["text"],
            "findings": []
        }
        
        if visual_asset:
            result["modalities_analyzed"].append("vision")
            result["findings"].append({
                "type": "chart_analysis",
                "extracted_data": {"Q3_Growth": "+24%", "Total_Users": "1.2M"},
                "confidence": 0.96
            })
            
        if audio_asset:
            result["modalities_analyzed"].append("audio")
            result["findings"].append({
                "type": "audio_transcript",
                "speaker": "Mentor",
                "snippet": "AI Ustaad production curriculum graduation complete."
            })
            
        return result

engine = MultimodalIntelligenceEngine()
output = engine.process_query(
    text_query="Summarize financial chart and verified voice note.",
    visual_asset="balance_sheet.png",
    audio_asset="meeting_note.wav"
)
print("Multimodal Engine Output:", output)""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Capstone Multimodal Engine Architecture
  user_inputs[Text + Image PDF + Audio WAV] $browser -> ingest[Multi-Modal Ingestion Gateway] $server
  ingest -> doc_vlm[Visual Document Parser] $layers
  ingest -> audio_whisper[Whisper Speech Engine] $cpu
  doc_vlm & audio_whisper -> fusion[Cross-Modal Context Fusion] $database *
  fusion -> vlm_core[Multimodal Foundation LLM] $brain
  vlm_core -> grounded_out[Visual Grounded Response + Bounding Boxes] $terminal""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "Gemini Multimodal Ingestion Docs", "url": "https://ai.google.dev/gemini-api/docs/multimodal"},
                        {"title": "Multimodal Retrieval Augmented Generation (M-RAG)", "url": "https://arxiv.org/abs/2410.08182"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        },

        # =========================================================================
        # MODULE 13: Local AI & Edge Devices
        # =========================================================================
        {
            "phase_slug": "phase-5-specialization-capstone",
            "module_number": 13,
            "slug": "local-ai-and-edge-devices",
            "real_world_deliverable": "100% Offline Autonomous Edge AI Assistant with Voice & Local RAG",
            "zero_gpu_recipe": {
                'platform': 'Local Consumer Laptop (Mac M-series / Intel / AMD) / Raspberry Pi',
                'vram_required': '0 GB GPU (Runs 100% on CPU RAM with AVX-512 / Metal)',
                'estimated_cost': '$0.00 Free',
                'compute_units_tip': 'llama.cpp and Ollama run 3B and 8B quantized GGUF models directly on standard consumer CPU RAM with zero cloud dependency.',
                'one_click_command': 'ollama run llama3.2:3b'
            },
            "title": "Module 13: Local AI & Edge Devices",
            "weeks_range": "Weeks 18-19",
            "estimated_hours": 14,
            "learning_outcomes": [
                "C++ Inference optimization: llama.cpp architecture, GGUF binary quantization formats aur CPU vectorization",
                "Ollama deep dive: Custom Modelfiles, system prompt templating, REST API automation aur memory swapping",
                "Hardware acceleration: Apple Silicon Metal Performance Shaders (MPS), Vulkan cross-platform aur AMD ROCm",
                "In-browser AI execution: WebGPU, Wasm (WebAssembly) aur Transformers.js for zero-server latency",
                "Embedded Edge AI: Nvidia Jetson Orin Nano, Raspberry Pi 5 NPU aur INT4 embedded model deployment",
                "100% privacy-preserving offline AI architectures for confidential healthcare, legal aur field operations"
            ],
            "practical_tasks": [
                "llama.cpp build karein local machine par with native AVX-512 / Metal flags",
                "Custom Ollama Modelfile create karein Roman Urdu personality aur parameter constraints ke sath",
                "In-browser sentiment classifier aur chat client deploy karein using WebGPU & Transformers.js",
                "Raspberry Pi / Jetson benchmark run karein measuring tokens per second and thermal throttling",
                "Complete offline RAG pipeline build karein using local ChromaDB and Ollama embeddings"
            ],
            "resources": [
                {"title": "llama.cpp GitHub Repository", "url": "https://github.com/ggerganov/llama.cpp"},
                {"title": "Ollama Documentation & Modelfiles", "url": "https://github.com/ollama/ollama/blob/main/docs/modelfile.md"},
                {"title": "Transformers.js In-Browser AI", "url": "https://huggingface.co/docs/transformers.js/index"},
                {"title": "WebGPU W3C Specification", "url": "https://www.w3.org/TR/webgpu/"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 13 Local AI Execution Stack
  hardware[Consumer CPU / Apple M-Chip / NPU] $cpu -> backend[llama.cpp / Vulkan / Metal] $layers
  backend -> gguf[Quantized GGUF Q4_K_M Weights] $database
  backend -> ollama[Ollama Local REST Daemon] $server *
  ollama -> app[Private Offline Application] $browser""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "production-ready",
            "order_index": 13,
            "lessons": [
                {
                    "lesson_code": "13.1",
                    "slug": "llama-cpp-gguf-cpu-optimization",
                    "title": "Running AI Locally: llama.cpp, GGUF Formats & CPU Optimization",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, agar aapke pas koi mehnga Nvidia GPU nahi hai, sirf ek normal 16GB RAM wala laptop hai, to kya aap Llama 3 ya DeepSeek run kar sakte hain? **100% YES!**

Georgi Gerganov ka **llama.cpp** software engineering ki dunya ka masterclass project hai! Yeh pure C/C++ mein likha gaya hai with zero external dependencies.
Iske ahem features:
1. **GGUF (GPT-Generated Unified Format)**:
   Model ke tamam tensors, metadata, tokenizer vocabulary, aur hyper-parameters ek single binary file mein store hote hain. GGUF memory-mapped (`mmap`) hota hai, yaani file load hote hi instant execute hona shuru ho jati hai bina poori RAM occupy kiye!
2. **K-Quants (Q4_K_M, Q5_K_M)**:
   Uniform quantization ki bajaye different tensor layers ko different bit-widths assign karta hai (critical attention layers ko 5-bit ya 6-bit aur baqi weights ko 4-bit) taake minimal RAM mein maximum intelligence mile.
3. **SIMD CPU Vectorization**:
   Modern Intel/AMD CPUs ke AVX2, AVX-512, aur ARM NEON instructions ko direct assembly level par target karta hai, jis se CPU par 15 se 30 tokens/second ki smooth speed milti hai!""",
                    "english_summary": "Understand Georgi Gerganov's llama.cpp C/C++ architecture, the unified GGUF binary format, mmap memory management, and AVX-512/ARM NEON vectorization.",
                    "code_example": """# Compiling and Running llama.cpp with Hardware Acceleration
# On Linux / Windows (MSVC or MinGW) with AVX2:
# cmake -B build -DGGML_AVX2=ON && cmake --build build --config Release

# Running Quantized Llama 3.2 3B locally on CPU:
# ./build/bin/llama-cli \\
#     -m ./models/Llama-3.2-3B-Instruct-Q4_K_M.gguf \\
#     -p "Salam! AI Ustaad par local inference kaise fast hota hai?" \\
#     -n 256 \\
#     --threads 8 \\
#     --temp 0.7

print("llama.cpp CLI configuration verified for low-latency CPU execution!")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: llama.cpp Architecture & Memory Mapping
  gguf_file[GGUF Binary File on Disk] $database -> mmap[OS mmap Zero-Copy Virtual Memory] $server
  mmap -> cpu_cores[Multi-Core CPU Threads with AVX-512] $cpu *
  cpu_cores -> simd[SIMD Vectorized Dot Product Kernels] $layers
  simd -> token_stream[Instant Token Stream Output] $terminal""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "llama.cpp GitHub Repository", "url": "https://github.com/ggerganov/llama.cpp"},
                        {"title": "GGUF File Format Specification", "url": "https://github.com/ggerganov/ggml/blob/master/docs/gguf.md"}
                    ],
                    "xp_reward": 25,
                    "order_index": 1
                },
                {
                    "lesson_code": "13.2",
                    "slug": "ollama-modelfiles-rest-orchestration",
                    "title": "Ollama Deep Dive: Custom Modelfiles, Swapping & REST APIs",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jabke llama.cpp raw engine hai, **Ollama** ne local AI ko Docker ki tarah aasan aur elegant bana diya hai!

Ollama background mein ek lightweight daemon run karta hai jo localhost port 11434 par OpenAI-compatible REST API expose karta hai.
Ahem capabilities:
1. **The Modelfile**:
   Dockerfiles ki tarah aap custom `Modelfile` likh sakte hain:
   ```dockerfile
   FROM llama3.2:3b
   PARAMETER temperature 0.2
   PARAMETER stop "<|eot_id|>"
   SYSTEM \"\"\"Aap AI Ustaad ke strict enterprise mentor hain.\"\"\"
   ```
2. **Dynamic Model Swapping**:
   Ollama automatically models ko VRAM/RAM mein swap in aur swap out karta hai. Jab request aati hai to model load hota hai, aur 5 minute idle rehne par memory release ho jati hai.
3. **Local Embedding API**:
   `/api/embeddings` endpoint se aap bina kisi third-party cost ke local text vectors generate kar sakte hain.""",
                    "english_summary": "Configure and automate local LLM workflows with Ollama, author custom Modelfiles with system templates, and orchestrate REST API inference.",
                    "code_example": """import requests
import json

def query_local_ollama(prompt: str, model: str = "llama3.2:3b") -> str:
    \"\"\"Calls local Ollama daemon streaming REST endpoint on localhost:11434.\"\"\"
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 128
        }
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        data = response.json()
        return data.get("response", "")
    except requests.exceptions.ConnectionError:
        return "Ollama daemon not running. Start with 'ollama serve'."

# Example execution
answer = query_local_ollama("AI Ustaad ka vision kya hai?")
print("Ollama Response:", answer)""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Ollama Local Daemon Architecture
  client[Desktop / Web App] $browser -> rest[HTTP REST API localhost:11434] $network
  rest -> daemon[Ollama Background Daemon] $server *
  daemon -> modelfile[Modelfile Config & Template] $code
  daemon -> engine[Embedded llama.cpp Runner] $cpu
  engine -> weights[Cached GGUF Weights in ~/.ollama] $database""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Ollama Official Documentation", "url": "https://ollama.com/"},
                        {"title": "Ollama API Specification", "url": "https://github.com/ollama/ollama/blob/main/docs/api.md"}
                    ],
                    "xp_reward": 25,
                    "order_index": 2
                },
                {
                    "lesson_code": "13.3",
                    "slug": "hardware-acceleration-metal-vulkan",
                    "title": "Edge Hardware Acceleration: Apple Metal (MPS), Vulkan & ROCm",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, local inference ko CPU se 10x tez karne ke liye humein edge hardware accelerators (Integrated GPUs aur NPUs) ka faida uthana parta hai.

Teen primary acceleration backends industry standard hain:
1. **Apple Silicon Metal (MPS)**:
   M1, M2, M3, M4 chips par **Unified Memory Architecture (UMA)** hoti hai! CPU aur GPU ek hi high-bandwidth memory pool (100 GB/s se 800 GB/s) share karte hain. Koi PCIe transfer latency nahi hoti! Metal Performance Shaders use karke 70B parameter models Mac Studio par smoothly run hote hain.
2. **Vulkan Cross-Platform**:
   Vulkan ek low-level, high-performance graphics & compute API hai jo har platform (Windows, Linux, Android, Intel iGPU, AMD APU) par GPU compute enable karti hai bina proprietary CUDA drivers ke.
3. **AMD ROCm**:
   AMD Radeon graphics cards par open-source PyTorch aur vLLM execution enable karta hai.""",
                    "english_summary": "Leverage native hardware acceleration frameworks including Apple Metal Performance Shaders (MPS), cross-platform Vulkan compute, and AMD ROCm for local inference.",
                    "code_example": """import torch

def detect_local_accelerator() -> str:
    \"\"\"Detects and returns optimal hardware acceleration device for PyTorch inference.\"\"\"
    if torch.cuda.is_available():
        device_name = torch.cuda.get_device_name(0)
        return f"CUDA Acceleration Active: {device_name}"
    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "Apple Metal Performance Shaders (MPS) Unified Memory Active"
    else:
        num_threads = torch.get_num_threads()
        return f"CPU AVX Vectorized Fallback ({num_threads} threads active)"

status = detect_local_accelerator()
print("Local Hardware Diagnostic:", status)""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Hardware Acceleration Tiers
  app[Inference Engine] $server -> dispatch[Hardware Dispatcher] $layers
  dispatch -- Apple Silicon --> mps[Apple Metal Unified RAM] $cpu *
  dispatch -- Nvidia Hardware --> cuda[CUDA Tensor Cores] $gpu
  dispatch -- AMD / Intel iGPU --> vulkan[Vulkan Compute Pipeline] $chip
  dispatch -- Fallback --> avx[Multi-Core CPU AVX-512] $database""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "Apple Metal Performance Shaders Docs", "url": "https://developer.apple.com/metal/"},
                        {"title": "Vulkan Compute Documentation", "url": "https://www.vulkan.org/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "13.4",
                    "slug": "in-browser-ai-webgpu",
                    "title": "In-Browser Client AI: WebGPU & Transformers.js",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, socho agar aap ek aisi AI web application banayein jisme aapko backend server ka **ek rupiya bhi na dena pare**, aur user ka data user ke browser se **ek inch bhi bahar na jaye**!

Yeh futuristic architecture ab **WebGPU** aur **Transformers.js (v3)** ke sath 100% possible hai!
WebGPU browser ka modern low-level graphics aur compute standard hai jo WebGL ke muqable mein direct GPU compute shaders execute karta hai.
Iska mechanism:
1. Browser user ke local GPU (Intel, Nvidia, ya Apple M-chip) se direct WebAssembly (Wasm) aur WebGPU interface establish karta hai.
2. ONNX Runtime Web model weights (jaise Phi-3.5-mini, Whisper, ya BGE-embeddings) ko user ke browser cache (IndexedDB) mein download aur cache karta hai.
3. Generation, embedding retrieval, aur sentiment classification poori tarah client-side JavaScript mein execute hoti hai!

Zero server costs, zero API rate limits, aur 100% airtight data privacy!""",
                    "english_summary": "Run deep learning transformers directly inside client web browsers using WebGPU, ONNX Runtime Web, and Transformers.js with zero server infrastructure costs.",
                    "code_example": """// In-Browser AI with Transformers.js and WebGPU (Client-side JavaScript)
// <script type=\"module\">
// import { pipeline } from 'https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.0.0';

async function initBrowserAI() {
    console.log("Initializing in-browser text classification on WebGPU...");
    
    // In production web client:
    // const classifier = await pipeline('sentiment-analysis', 'Xenova/distilbert-base-uncased-finetuned-sst-2-english', {
    //     device: 'webgpu'
    // });
    // const output = await classifier('AI Ustaad makes local edge AI incredibly practical!');
    // console.log("WebGPU Result:", output);
    
    return { status: "WebGPU pipeline ready", device: "client-side GPU" };
}

initBrowserAI().then(console.log);""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: In-Browser WebGPU Execution Flow
  browser[User Browser Tab] $browser -> idb[IndexedDB Cached ONNX Weights] $database
  browser -> webgpu[WebGPU Compute Shader API] $cpu *
  webgpu -> gpu[Local Client GPU Hardware] $chip
  gpu -> dom[Direct DOM UI Update: Zero Network Latency] $terminal""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Transformers.js Documentation", "url": "https://huggingface.co/docs/transformers.js/index"},
                        {"title": "WebGPU Fundamentals", "url": "https://webgpufundamentals.org/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 4
                },
                {
                    "lesson_code": "13.5",
                    "slug": "edge-ai-jetson-raspberry-pi",
                    "title": "Edge AI on Embedded Hardware: Nvidia Jetson & Raspberry Pi NPUs",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab hum AI ko internet se door kisi factory floor, drone, smart camera, ya agricultural farm mein deploy karte hain jahan 4G/WiFi ka nam-o-nishan nahi hota, to humein **Embedded Edge AI** hardware chahiye hota hai.

Do leading embedded computing platforms:
1. **Nvidia Jetson Orin Nano (40-67 TOPS AI Performance)**:
   Jetson ek credit-card size computer hai jisme 1024-core Nvidia Ampere GPU aur Tensor Cores mojood hote hain. Yeh 7-15 Watts power consume karta hai aur 4-bit quantized 7B models ko real-time 20+ tokens/sec par run kar sakta hai!
2. **Raspberry Pi 5 + Raspberry Pi AI Kit (Hailo-8L NPU)**:
   13 TOPS ka dedicated Neural Processing Unit (NPU) jo vision models (YOLOv8, Pose Estimation) ko sirf 2-3 Watts power par 30+ FPS video streams par execute karta hai!

Key challenge: **Thermal Management & Power Throttling**. Edge devices par fan profiles, dynamic voltage scaling, aur model batch size ko tune karna lazmi hota hai taake chip overheat ho kar restart na ho.""",
                    "english_summary": "Deploy compact quantized models on embedded hardware such as Nvidia Jetson Orin and Raspberry Pi 5 NPUs with strict power, memory, and thermal constraints.",
                    "code_example": """# Monitoring Embedded Jetson Thermals & NPU Power (Python Edge Daemon)
import subprocess
import time

def read_jetson_telemetry() -> dict:
    \"\"\"Reads Tegrastats or thermal zone on Nvidia Jetson embedded device.\"\"\"
    try:
        with open("/sys/devices/virtual/thermal/thermal_zone0/temp", "r") as f:
            temp_milli = int(f.read().strip())
            celsius = temp_milli / 1000.0
    except FileNotFoundError:
        celsius = 45.2 # Simulated baseline temperature
        
    return {
        "cpu_temp_celsius": celsius,
        "is_throttled": celsius > 80.0,
        "power_mode": "15W_6CORE_BALANCED"
    }

telemetry = read_jetson_telemetry()
print(f"Edge Device Temperature: {telemetry['cpu_temp_celsius']} C | Throttled: {telemetry['is_throttled']}")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Embedded Edge AI Pipeline
  sensor[CCTV Camera / Microphone Sensor] $browser -> npu[Hailo-8L NPU / Jetson Orin Tensor Cores] $chip *
  npu -> int4_engine[Quantized INT4 Inference 10W Power] $cpu
  int4_engine -> action[Local GPIO Relay Trigger / Alert] $server
  int4_engine -> log[Local SQLite Storage: 100% Offline] $database""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Nvidia Jetson Orin Developer Documentation", "url": "https://developer.nvidia.com/embedded/jetson-orin"},
                        {"title": "Raspberry Pi AI Kit Overview", "url": "https://www.raspberrypi.com/documentation/accessories/ai-kit.html"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "13.6",
                    "slug": "capstone-offline-edge-assistant",
                    "title": "Module 13 Capstone: 100% Offline Autonomous Edge AI Assistant",
                    "duration_minutes": 50,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, congratulations! Aap Module 13 ke Capstone project par pohanch chuke hain. Is capstone mein aap ek mukammal **100% Offline Autonomous Edge AI Assistant** build karenge jo airplane mode par bhi voice commands sunega, local documents search karega, aur Roman Urdu mein jawab dega!

Aapka Capstone Architecture:
1. **Local Speech-to-Text**: Whisper.cpp ya faster-whisper local CPU par audio stream ko text mein convert karega.
2. **Local Vector Knowledge Base**: ChromaDB ya SQLite-vec local disk par chalegi with sentence-transformers embeddings (all-MiniLM-L6-v2 ya BGE-small).
3. **Local LLM Engine**: Ollama ya llama.cpp ke zariye Llama 3.2 3B (Q4_K_M) local RAM par execute hoga.
4. **Local Text-to-Speech (TTS)**: Piper TTS ya Kokoro local audio synthesizer ke zariye instant voice playback provide karega.
5. **Zero-Network Audit**: Wireshark ya network disconnect karke prove karein ke system bina internet ke 100% functional rehta hai!""",
                    "english_summary": "Architect and deploy the Module 13 Capstone: a 100% offline, privacy-first Edge AI Assistant combining whisper.cpp speech recognition, local SQLite-vec RAG, and quantized Ollama inference.",
                    "code_example": """# Capstone Offline Assistant Coordinator
class OfflineEdgeAssistant:
    def __init__(self):
        self.device = "Local CPU / Edge Accelerator"
        print("Offline Assistant online: Network connectivity = 0 (Airtight Privacy)")
        
    def execute_voice_turn(self, audio_input_bytes: bytes) -> dict:
        # 1. Local STT (Whisper.cpp)
        transcribed_text = "AI Ustaad platform ke offline safety protocols kya hain?"
        
        # 2. Local Vector Search (SQLite-vec)
        retrieved_snippet = "Offline protocols require zero cloud telemetry and local disk encryption."
        
        # 3. Local LLM Reasoning (llama.cpp)
        answer = "So guys, offline safety protocols ke teht tamam embeddings local SQLite file mein store hoti hain aur koi network packet bahar nahi jata."
        
        return {
            "query": transcribed_text,
            "context": retrieved_snippet,
            "response": answer,
            "offline_verified": True
        }

assistant = OfflineEdgeAssistant()
result = assistant.execute_voice_turn(b"mock_audio_bytes")
print("Offline Assistant Turn Result:", result)""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: Capstone Offline Edge Assistant
  mic[Local USB Microphone] $browser -> whisper_cpp[Local Whisper.cpp STT] $cpu
  whisper_cpp -> query[Transcribed Query] $terminal
  query -> local_rag[Local SQLite-vec Database] $database
  query & local_rag -> llama_runner[llama.cpp / Ollama Engine] $server *
  llama_runner -> piper_tts[Local Piper TTS Synthesizer] $chip
  piper_tts -> speaker[Local Audio Speaker Output] $terminal""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "Whisper.cpp High-Performance C++ Port", "url": "https://github.com/ggerganov/whisper.cpp"},
                        {"title": "Piper Local Fast Neural TTS", "url": "https://github.com/rhasspy/piper"}
                    ],
                    "xp_reward": 50,
                    "order_index": 6
                }
            ]
        },

        # =========================================================================
        # MODULE 14: Enterprise Capstone & Career Launch
        # =========================================================================
        {
            "phase_slug": "phase-5-specialization-capstone",
            "module_number": 14,
            "slug": "enterprise-capstone-and-career-launch",
            "real_world_deliverable": "Multi-Tenant Enterprise AI Platform with Auth, Billing, Observability & Live Defense",
            "zero_gpu_recipe": {
                'platform': 'Fly.io / Render / Cloudflare Pages / Supabase Free Tier',
                'vram_required': '0 GB (Cloud Serverless / Microservices Architecture)',
                'estimated_cost': '$0.00 Free Tier',
                'compute_units_tip': 'Deploy multi-tenant frontend on Cloudflare Pages, backend on Render, and Postgres/pgvector on Supabase completely within free tier limits.',
                'one_click_command': 'docker compose up -d'
            },
            "title": "Module 14: Enterprise Capstone & Career Launch",
            "weeks_range": "Weeks 19-20",
            "estimated_hours": 20,
            "learning_outcomes": [
                "Enterprise multi-tenant architecture: Row-Level Security (RLS), vector workspace isolation aur compliance audit trails",
                "High availability & resilience engineering: Circuit breakers, exponential jitter backoff aur multi-cloud fallback",
                "Monetization & cost governance: Token metering, user rate limits aur Stripe usage-based billing integration",
                "Production packaging & release: Multi-stage Docker builds, Helm charts aur semantic versioning CI/CD pipelines",
                "AI engineering career positioning: Technical architecture whitepapers, GitHub portfolio stardom aur live demos",
                "Grand Capstone Defense: Live presentation, technical peer review aur graduation from the AI Ustaad curriculum"
            ],
            "practical_tasks": [
                "Supabase Postgres Row-Level Security policies configure karein multi-tenant vector partitioning ke liye",
                "Stripe metered billing webhook listener implement karein tracking input and output tokens",
                "Multi-stage Dockerfile optimize karein reducing production image size from 4GB to under 200MB",
                "Interactive live portfolio project showcase deploy karein on Cloudflare Pages / Fly.io",
                "Grand Capstone live defense conduct karein with comprehensive system architecture documentation"
            ],
            "resources": [
                {"title": "Supabase Row Level Security Deep Dive", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security"},
                {"title": "Stripe Usage-Based Metered Billing", "url": "https://stripe.com/docs/billing/subscriptions/usage-based"},
                {"title": "Docker Multi-Stage Builds Guide", "url": "https://docs.docker.com/build/building/multi-stage/"},
                {"title": "System Design for Enterprise AI Applications", "url": "https://github.com/donnemartin/system-design-primer"}
            ],
            "diagram_script": """@preset midnight
@animate flow
flow LR: Module 14 Enterprise Architecture
  client[Cloudflare Pages Frontend] $browser -> gw[Multi-Tenant Gateway] $server *
  gw -> rls[Supabase Postgres RLS & Vector Partition] $database
  gw -> billing[Stripe Token Metering] $dollar
  gw -> cluster[Resilient LLM Inference Cluster] $cpu
  gw -> audit[Immutable Audit Log] $lock""",
            "diagram_preset": "midnight",
            "diagram_animation": "flow",
            "badge_slug": "ai-graduate",
            "order_index": 14,
            "lessons": [
                {
                    "lesson_code": "14.1",
                    "slug": "enterprise-multi-tenant-architecture",
                    "title": "Enterprise System Design: Multi-Tenant RLS, Vector Partitioning & Audit",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab aap ek B2B SaaS AI product build karte hain jahan Company A (Bank) aur Company B (Hospital) dono aapka platform use kar rahe hain, to agar Company A ke user ko Company B ke confidential documents ka jawab ghalti se bhi mil gaya, to aapki company par millions dollars ka lawsuit ho sakta hai!

Enterprise Multi-Tenancy ke teen pillars hote hain:
1. **Row-Level Security (RLS)**:
   Database level par har query par automatically `WHERE tenant_id = auth.jwt()->>'tenant_id'` enforce hota hai. Chahe backend application code mein developer `WHERE` clause bhool bhi jaye, database engine kisi doosre tenant ka data return hi nahi kar sakta!
2. **Vector Space Partitioning**:
   pgvector mein har vector index mein `metadata->>'tenant_id'` par HNSW / IVFFlat partial indexes banaye jate hain taake similarity search sirf tenant ke apne documents ke darmiyan execute ho.
3. **Immutable Audit Trails**:
   Har prompt, response, model version, aur data access event ko append-only audit table mein log kiya jata hai for SOC2 and ISO-27001 compliance.""",
                    "english_summary": "Architect airtight multi-tenant enterprise AI platforms utilizing Supabase Row-Level Security (RLS), partition-isolated vector indexes, and immutable audit logs.",
                    "code_example": """-- Enterprise Multi-Tenant RLS & pgvector Partitioning (PostgreSQL)
-- 1. Enable RLS on vector documents table
ALTER TABLE public.document_embeddings ENABLE ROW LEVEL SECURITY;

-- 2. Strict Tenant Isolation Policy based on JWT claims
CREATE POLICY tenant_isolation_policy ON public.document_embeddings
    FOR ALL
    USING (tenant_id = (current_setting('request.jwt.claims', true)::jsonb ->> 'tenant_id')::uuid)
    WITH CHECK (tenant_id = (current_setting('request.jwt.claims', true)::jsonb ->> 'tenant_id')::uuid);

-- 3. Filtered HNSW Vector Index for blazing-fast isolated search
CREATE INDEX idx_tenant_hnsw_vectors ON public.document_embeddings 
USING hnsw (embedding vector_cosine_ops)
WHERE is_active = true;""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Enterprise Multi-Tenant Isolation
  req_a[Tenant A User (Bank)] $browser -> auth[JWT Auth & Tenant Context] $lock
  req_b[Tenant B User (Hospital)] $browser -> auth
  auth -> rls[Postgres Row-Level Security Engine] $server *
  rls -- Partition A --> data_a[Tenant A Isolated Vectors] $database
  rls -- Partition B --> data_b[Tenant B Isolated Vectors] $database""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "PostgreSQL Row-Level Security Guide", "url": "https://www.postgresql.org/docs/current/ddl-rowsecurity.html"},
                        {"title": "Multi-Tenancy in Vector Databases", "url": "https://supabase.com/docs/guides/ai"}
                    ],
                    "xp_reward": 25,
                    "order_index": 1
                },
                {
                    "lesson_code": "14.2",
                    "slug": "high-availability-circuit-breakers",
                    "title": "High Availability & Resilience: Circuit Breakers & Multi-Cloud Fallback",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, enterprise engineering ka qanoon hai: **"Everything fails, all the time."**
OpenAI ka API down ho sakta hai, Anthropic par rate limit lag sakti hai, ya aapka primary cloud provider network outage face kar sakta hai. Agar aapki system in failures ko gracefully handle nahi karti to aapka 99.9% uptime SLA break ho jayega.

Iska solution **Circuit Breaker Pattern** aur **Multi-Cloud Dynamic Routing** hai:
1. **Three Circuit States**:
   - **CLOSED (Normal)**: Tamam requests primary model provider (jaise vLLM / OpenAI) ko jati hain.
   - **OPEN (Tripped)**: Agar pichli 10 requests mein se 5 fail hon ya latency 3s se zyada ho, to circuit foran OPEN ho jata hai aur primary provider par requests bhejna band ho jata hai!
   - **HALF-OPEN (Recovery)**: Kuch seconds baad circuit kuch probe requests primary ko bhej kar check karta hai; agar pass hon to CLOSED ho jata hai.
2. **Exponential Jitter Backoff**:
   Retry karte waqt uniform delay ki bajaye randomized exponential backoff (`delay = min(max_delay, base * 2^attempt) + random_jitter`) use kiya jata hai taake cascading "thundering herd" problem na bane.""",
                    "english_summary": "Implement enterprise reliability patterns including Circuit Breakers (Closed/Open/Half-Open), exponential jitter backoff, and automatic multi-cloud provider failover.",
                    "code_example": """import time
import random
from enum import Enum

class CircuitState(Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

class ResilientAIGateway:
    def __init__(self, failure_threshold: int = 3, recovery_time_sec: float = 10.0):
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.recovery_time = recovery_time_sec
        self.last_failure_time = 0
        
    def call_ai_service(self, prompt: str) -> str:
        current_time = time.time()
        
        # Check if OPEN circuit can transition to HALF_OPEN
        if self.state == CircuitState.OPEN:
            if current_time - self.last_failure_time > self.recovery_time:
                self.state = CircuitState.HALF_OPEN
            else:
                # Instant Failover to Secondary Provider (e.g. Groq / Cloudflare)
                return f"[FAILOVER_PROVIDER] Handled via secondary provider: {prompt[:30]}..."
                
        try:
            # Simulate primary call
            return f"[PRIMARY_PROVIDER] Successful response: {prompt[:30]}..."
        except Exception:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
            return "[FAILOVER_PROVIDER] Handled via secondary provider fallback."

gateway = ResilientAIGateway()
print("Circuit Breaker Gateway Status:", gateway.state.value)""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Circuit Breaker State Transition
  closed[CLOSED: Normal Traffic] $server -- Failures > Threshold --> open_state[OPEN: Route to Fallover Provider] $shield
  open_state -- Recovery Timeout --> half_open[HALF-OPEN: Test Canary Probe] $layers
  half_open -- Canary Success --> closed *
  half_open -- Canary Fails --> open_state""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Martin Fowler: Circuit Breaker Pattern", "url": "https://martinfowler.com/bliki/CircuitBreaker.html"},
                        {"title": "AWS Architecture Center: Exponential Backoff And Jitter", "url": "https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 2
                },
                {
                    "lesson_code": "14.3",
                    "slug": "token-metering-stripe-billing",
                    "title": "Monetization & Governance: Token Metering & Stripe Usage-Based Billing",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, agar aapka user bohot lambi videos ya 100-page ke documents summarize karwata hai aur aap us se fixed $10/month charge kar rahe hain, to aapki company kuch hi hafton mein bankrupt ho jayegi!

Modern AI companies ka business model **Usage-Based (Metered) Billing** hota hai:
1. **Accurate Token Metering**:
   Har API response ke baad input tokens aur output tokens ko extract karke Redis TimeSeries ya Postgres mein asynchronously log kiya jata hai.
2. **Stripe Metering API Integration**:
   Stripe ke **Billing Meters** feature ko har ghante customer ka aggregated token count report kiya jata hai (`stripe.billing.meter_events.create`).
3. **Hard & Soft Quotas**:
   Jab customer apne monthly budget (jaise $50) ke 80% par pohanchta hai to automated email notification trigger hoti hai (Soft Limit); 100% par non-critical requests block ho jati hain (Hard Limit) taake runaway bill shocks se bacha ja sake.""",
                    "english_summary": "Implement precise token metering pipelines and integrate Stripe Usage-Based Billing meters to monetize AI applications sustainably with budget quotas.",
                    "code_example": """import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_mock_key")

def report_token_usage_to_stripe(customer_id: str, input_tokens: int, output_tokens: int):
    \"\"\"Reports consumed AI tokens to Stripe Usage-Based Billing Meter.\"\"\"
    total_tokens = input_tokens + output_tokens
    
    # In production with live Stripe API:
    # stripe.billing.MeterEvent.create(
    #     event_name="ai_tokens_consumed",
    #     payload={
    #         "value": str(total_tokens),
    #         "stripe_customer_id": customer_id
    #     }
    # )
    
    cost_estimate_usd = (input_tokens * 0.00000015) + (output_tokens * 0.0000006)
    return {
        "customer_id": customer_id,
        "total_tokens": total_tokens,
        "cost_estimate_usd": round(cost_estimate_usd, 6),
        "status": "reported_to_stripe"
    }

usage = report_token_usage_to_stripe("cus_PK10294", input_tokens=1540, output_tokens=420)
print("Stripe Metering Event:", usage)""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Token Metering & Stripe Billing Architecture
  gateway[AI Gateway Response] $server -> counter[Async Token Counter Worker] $cpu
  counter -> db[PostgreSQL Token Ledger] $database
  counter -> stripe[Stripe Billing Meter API] $dollar *
  stripe -> invoice[Monthly Usage-Based End Customer Invoice] $chart""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Stripe Usage-Based Metered Billing Docs", "url": "https://stripe.com/docs/billing/subscriptions/usage-based"},
                        {"title": "Managing LLM Costs & Quotas", "url": "https://www.datadoghq.com/blog/llm-cost-management/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 3
                },
                {
                    "lesson_code": "14.4",
                    "slug": "packaging-open-source-helm-docker",
                    "title": "Packaging & Distribution: Multi-Stage Docker & Helm Charts",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, jab aapka AI system local machine par chal raha hota hai to "It works on my machine!" kehna kafi nahi hota. Production deployment ke liye containerization aur automated packaging lazmi hai.

1. **Multi-Stage Docker Builds**:
   PyTorch aur CUDA libraries bohot bari hoti hain (single image 6GB se 10GB ki ban jati hai!).
   Multi-stage build mein pehla stage (Builder) dependencies compile karta hai, aur final stage (Runtime) sirf zaroori compiled artifacts copy karta hai. Nateeja? Container image size **70% chota** ho jata hai, attack surface reduce hoti hai, aur deploy speed 4x fast hoti hai!
2. **Kubernetes Helm Charts**:
   Poore platform (Frontend, Backend, Redis, Vector DB, KEDA Autoscaler) ko ek single configurable Helm chart package (`values.yaml`) mein define kiya jata hai taake enterprise client ek command `helm install ai-ustaad ./chart` se poora stack deploy kar sake!""",
                    "english_summary": "Package enterprise AI microservices with multi-stage Docker builds to slash container footprint and define declarative Kubernetes Helm charts for one-click deployment.",
                    "code_example": """# Multi-Stage Dockerfile for High-Performance AI Gateway
# Stage 1: Build stage with compiler toolchain
FROM rust:1.80-slim as builder
WORKDIR /app
COPY Cargo.toml Cargo.lock ./
COPY src ./src
RUN cargo build --release

# Stage 2: Minimal Distroless / Debian Runtime
FROM debian:bookworm-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/target/release/ai_gateway /app/ai_gateway

EXPOSE 8080
USER 1001
CMD ["/app/ai_gateway"]""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: Multi-Stage Docker Optimization
  heavy[Stage 1: Heavy Build Environment 3.5GB (Compilers + SDKs)] $layers -> compile[Compile Binary] $cpu
  compile -> light[Stage 2: Slim Runtime Environment 95MB (Zero Bloat)] $server *
  light -> registry[Deploy to Docker Hub / Cloudflare] $cloud""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "Docker Multi-Stage Builds Documentation", "url": "https://docs.docker.com/build/building/multi-stage/"},
                        {"title": "Helm: The Kubernetes Package Manager", "url": "https://helm.sh/docs/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 4
                },
                {
                    "lesson_code": "14.5",
                    "slug": "ai-career-portfolio-stardom",
                    "title": "AI Career Launch: Viral Demos, Technical Whitepapers & GitHub Stardom",
                    "duration_minutes": 35,
                    "lesson_type": "theory_and_code",
                    "roman_urdu_content": """So guys, aapne 20 hafton mein duniya ke sab se advanced AI concepts seekh liye hain. Lekin agar duniya ko aapke kaam ka pata hi nahi chalega to aapko top global AI companies (San Francisco, London, Dubai) se remote offers kaise milenge?

Aapko apna **Proof of Work** show karna hai:
1. **The Viral 60-Second Video Demo**:
   Log lambe text nahi parhte! Twitter (X) aur LinkedIn par apne Capstone ka ek 60-second crisp screen recording post karein jisme real-time token streaming, diagram visual grounding, aur speed demonstrate ho rahi ho.
2. **The Architecture Whitepaper**:
   Apne GitHub repo ke README mein clear DiagramKit architecture diagrams, benchmark graphs (Latency P99, Throughput comparison), aur design trade-offs document karein.
3. **Open-Source Contribution Blueprint**:
   Popular AI repos (vLLM, Unsloth, Langfuse, LiteLLM) mein bug fixes aur documentation PRs submit karein. Yeh GitHub profile ko global recruiters ki nazar mein golden bana deta hai!""",
                    "english_summary": "Position your AI Engineering profile globally with high-impact 60-second video demos, rigorous technical architecture READMEs, and open-source contributions.",
                    "code_example": """# GitHub Repository README Blueprint for Top AI Projects
# # Enterprise Multimodal RAG with ColPali & vLLM
# 
# [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# [![Docker Pulls](https://img.shields.io/badge/docker-ready-blue.svg)](https://hub.docker.com/)
# 
# ## 🚀 Architecture Overview
# Built with Rust Axum, vLLM PagedAttention, and Supabase pgvector.
# 
# ## 📊 Benchmarks
# - **Throughput**: 450 tokens/sec on single Nvidia L4
# - **P99 Latency**: 42ms TTFT (Time to First Token)
# - **Test Coverage**: 94% with DeepEval CI gates
# 
# ## 🛠️ Quickstart
# ```bash
# docker compose up -d
# curl -N http://localhost:8080/v1/chat/stream -d '{"prompt": "Hello"}'
# ```

print("README template validated for high-impact developer branding!")""",
                    "diagram_script": """@preset midnight
@animate flow
flow LR: AI Engineering Career Funnel
  repo[GitHub Open Source Repository] $code -> demo[60s X / LinkedIn Video Demo] $browser
  demo -> whitepaper[Technical Architecture Whitepaper] $database
  whitepaper -> interview[Global Remote Interview Offers ($100k-$180k)] $server *""",
                    "diagram_type": "flow",
                    "resources": [
                        {"title": "How to Build a World-Class Developer Portfolio", "url": "https://github.com/readme/guides"},
                        {"title": "Open Source Contribution Guide", "url": "https://opensource.guide/how-to-contribute/"}
                    ],
                    "xp_reward": 25,
                    "order_index": 5
                },
                {
                    "lesson_code": "14.6",
                    "slug": "grand-capstone-defense-graduation",
                    "title": "Grand Capstone Defense: Enterprise AI Platform Graduation",
                    "duration_minutes": 60,
                    "lesson_type": "project",
                    "roman_urdu_content": """So guys, TAMAM AI USTAAD FELLOWS KO MUBARAK HO! Aap curriculum ke aakhri aur sab se azeem marhalay par pohanch chuke hain: **The Grand Capstone Defense & Graduation**!

Aapne Python aur tensors ki pehli line se le kar Transformers, Deep Learning, Modern Hybrid RAG, Autonomous Multi-Agent Swarms, LoRA fine-tuning, DeepSeek-R1 GRPO, vLLM PagedAttention, aur Multi-Tenant Cloud Architecture tak ka 20-hafton ka safar tay kiya hai.

Aapka Final Graduation Criteria:
1. **Live Production Deployment**: Ek live public URL (jaise `https://your-capstone.pages.dev`) jahan platform active aur testable ho.
2. **Complete Full-Stack Architecture**:
   - Modern Svelte 5 / Next.js UI with real-time SSE token streaming.
   - Rust Axum ya FastAPI resilient gateway with rate-limiting.
   - Supabase Postgres with pgvector, Row-Level Security (RLS) aur audit logs.
   - NeMo Guardrails aur Presidio safety filters.
   - Distributed telemetry dashboard (Langfuse / Prometheus).
3. **Defense Presentation**: 10-minute video presentation jisme aap architecture decisions, latency trade-offs, aur edge case handling explain karein.

Jab aap yeh defense submit karenge to aapko **Official AI Ustaad Graduate Badge (🎓)** aur Certificate of Engineering Mastery se nawaza jayega!""",
                    "english_summary": "Deliver your Grand Capstone Defense: demonstrate a live multi-tenant enterprise AI system with streaming UI, Rust gateway, RLS vector storage, and safety guardrails to graduate.",
                    "code_example": """# Final AI Ustaad Platform Graduation Verification Script
def verify_graduation_readiness(checklist: dict) -> bool:
    print("AI USTAAD — ENGINEERING MASTERY GRADUATION AUDIT")
    print("=" * 55)
    all_passed = True
    for requirement, status in checklist.items():
        symbol = "✅" if status else "❌"
        print(f"{symbol} {requirement}")
        if not status:
            all_passed = False
            
    print("=" * 55)
    if all_passed:
        print("CONGRATULATIONS! You have mastered the complete AI curriculum.")
        print("Awarded: [AI Graduate Badge 🎓] | Status: PRODUCTION READY")
    else:
        print("Please resolve missing items before final graduation defense.")
    return all_passed

audit = {
    "Live Production Endpoint Deployed": True,
    "Multi-Tenant RLS & Vector Partitioning": True,
    "Real-Time SSE Streaming Gateway Active": True,
    "Enterprise Safety Rails & PII Redaction": True,
    "OpenTelemetry Distributed Tracing Configured": True,
    "Automated CI/CD Evaluation Tests Passing": True
}

verify_graduation_readiness(audit)""",
                    "diagram_script": """@preset midnight
@animate pulse
arch LR: The Complete AI Ustaad Full-Stack Universe
  learner[Zero: Eager Student] $terminal -> p1[Phase 1: Foundations] $code
  p1 -> p2[Phase 2: Core ML & Deep Learning] $layers
  p2 -> p3[Phase 3: Modern GenAI & RAG] $database
  p3 -> p4[Phase 4: Fine-Tuning & MLOps] $cpu
  p4 -> p5[Phase 5: Specialization & Enterprise] $server *
  p5 -> hero[Hero: Production AI Engineer 🎓] $cloud""",
                    "diagram_type": "arch",
                    "resources": [
                        {"title": "AI Ustaad Official Platform", "url": "https://ai-ustaad.pages.dev"},
                        {"title": "Global AI Engineering Community", "url": "https://github.com"}
                    ],
                    "xp_reward": 100,
                    "order_index": 6
                }
            ]
        }
    ]
