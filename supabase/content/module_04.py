# module_04.py
# Module 4: Deep Learning & Neural Networks
# Lessons 4.1 to 4.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 4.1: PyTorch Tensors, CUDA Memory & Computational Graph (Autograd)
# ==============================================================================
LESSON_CONTENT['4.1'] = r"""### Part 1: Mental Model & South Asian Analogy
Deep Learning mein PyTorch dunya ka sab se maqbool framework hai. Iska asli jadu do cheezon mein chhupa hai: High-Performance Tensors aur Automatic Differentiation (Autograd Computational Graph).
Isay samajhne ke liye kisi Film Director aur Video Editing Timeline ki misaal lein:
1. PyTorch Tensor (The Film Reel): NumPy array jahan CPU tak mehdood hoti hai, wahan PyTorch Tensor ek aisi film reel hai jo ek switch dabane par CPU se uth kar seedha GPU (CUDA Cores) par chali jati hai (`tensor.to('cuda')`). GPU ke hazaron chotay cores is reel ko parallel process karte hain.
2. The Computational Graph (Director Ka Script / Tape Recorder): Jab aap PyTorch mein `requires_grad=True` set karte hain to PyTorch ek khufia tape recorder on kar deta hai. Har mathematical operation (addition, matrix multiplication, activation) ek Node ke taur par graph mein record hota jata hai: "Pehle x aur w multiply hue, phir b add hua, phir ReLU laga." Isay 'Dynamic Computational Graph' kehte hain jo har forward pass par real-time banta hai.
3. Backward Pass (Film Rewind Karna): Jab aap aakhir mein `loss.backward()` call karte hain to film ulti (reverse) chalne lagti hai! PyTorch graph ke aakhri node (Loss) se shuru karta hai aur Calculus ke Chain Rule ke zariye har weight tak pohnchta hai aur `w.grad` mein exact derivative save kar deta hai.
4. CUDA Memory Allocation (VRAM Ka Dabba): GPU ki memory (VRAM) bohot mehangi hoti hai. PyTorch memory allocation ko tez karne ke liye Caching Allocator use karta hai. Jab aap tensor delete karte hain to woh VRAM foran OS ko wapas nahi karta, balki apne reserved pool mein rakhta hai taake aglay batch ke liye dobara allocate na karna paray.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Computational Graph aur Autograd ke Backward Pass ko ek chotay algebraic example ke sath mathematically trace karte hain.
Expression:
$y = (a + b) \times c$
Jahan:
- $a = 2.0$ (with gradient required)
- $b = 3.0$ (with gradient required)
- $c = 4.0$ (constant / no gradient)

Step 1: Forward Pass (Graph Construction)
Node 1 (Addition):
$u = a + b = 2.0 + 3.0 = 5.0$
PyTorch records: $u$ was created by `AddBackward0` with inputs $a$ and $b$.

Node 2 (Multiplication):
$y = u \times c = 5.0 \times 4.0 = 20.0$
PyTorch records: $y$ was created by `MulBackward0` with inputs $u$ and $c$.

Step 2: Backward Pass (Chain Rule Propagation)
Seed Gradient at Root:
$\frac{\partial y}{\partial y} = 1.0$

Gradient at Node 2:
$\frac{\partial y}{\partial u} = c = 4.0$
$\frac{\partial y}{\partial c} = u = 5.0$ (Ignored because $c$ does not require grad)

Gradient at Node 1 (Chain Rule):
$\frac{\partial y}{\partial a} = \frac{\partial y}{\partial u} \times \frac{\partial u}{\partial a} = 4.0 \times 1.0 = 4.0$
$\frac{\partial y}{\partial b} = \frac{\partial y}{\partial u} \times \frac{\partial u}{\partial b} = 4.0 \times 1.0 = 4.0$

Results Stored in Tensor Gradients:
- `a.grad` $= 4.0000$
- `b.grad` $= 4.0000$
PyTorch ne bina kisi analytical formula likhe, sirf step-by-step reverse graph traverse karke dono partial derivatives exact calculate kar diye!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum PyTorch tensor allocation, dynamic computational graph inspection, autograd gradient calculation, aur CUDA/CPU memory safety management ko implement karte hain.

```python
import torch

# 1. Device Agnostic Allocation Strategy
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Active Computation Device: {device}")

# 2. Tensor Creation with Autograd Tracking
# Shape: [Batch Size = 2, Features = 3]
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=torch.float32, device=device)

# Learnable Parameters requiring gradients
# Weight shape: [Features = 3, Output Neurons = 2]
w = torch.nn.Parameter(torch.randn(3, 2, dtype=torch.float32, device=device))
# Bias shape: [Output Neurons = 2]
b = torch.nn.Parameter(torch.zeros(2, dtype=torch.float32, device=device))

# 3. Dynamic Forward Pass
# Matrix Multiplication: [2, 3] @ [3, 2] -> [2, 2]
linear_out = torch.matmul(x, w) + b
# Activation: Mean Squared Error Proxy Loss -> Scalar ()
loss = torch.sum(linear_out ** 2)

print(f"Forward Output Shape: {linear_out.shape}")
print(f"Loss Value:           {loss.item():.4f}")
print(f"Loss Gradient Function: {loss.grad_fn}")  # Shows computational graph root node

# 4. Backward Pass: Trigger Chain Rule reverse traversal
loss.backward()

# 5. Inspect Computed Analytical Gradients
print(f"\\nw.grad Shape: {w.grad.shape} (Matches Weight Shape)")
print("Computed Gradients for w:\\n", w.grad)
print(f"b.grad Shape: {b.grad.shape}")
print("Computed Gradients for b:\\n", b.grad)

# 6. Safe Gradient Zeroing (Essential before next training step)
# In-place zeroing to avoid gradient accumulation
w.grad.zero_()
b.grad.zero_()
print(f"\\nGradients reset successfully. w.grad norm: {w.grad.norm().item()}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Forgetting `optimizer.zero_grad()` in Training Loops: PyTorch default tor par gradients ko har step par accumulate (jama) karta rehta hai taake large batch gradient simulation ho sake. Agar aap har step se pehle `zero_grad()` nahi call karte to purane gradients naye gradients mein add ho kar gradient explosion ka baais bante hain.
2. Creating Graph Leaks with Python Scalars: Loss ko log karte waqt `total_loss += loss` likhne se poora computational graph RAM mein zinda rehta hai aur memory leak hota hai. Hamesha `total_loss += loss.item()` likhein jo floating-point number extract karta hai.
3. Modifying In-Place Tensors Tracked by Autograd: `x += 1` jaisi in-place mutations autograd ke forward cache ko corrupt kar deti hain jisse `RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation` milta hai. Hamesha out-of-place `x = x + 1` karein.

Zero-GPU Tip:
PyTorch CPU runtime Intel MKL aur OpenMP se fully optimized hai. Autograd computational graphs aur small-scale networks CPU par chund milliseconds mein execute hote hain. Kisi GPU ki zaroorat nahi hai jab tak aap billion-parameter models train na kar rahe hon.

Self-Check Questions:
1. PyTorch mein Dynamic Computational Graph aur Static Graph (jaise purana TensorFlow 1.x) mein kya farq hai?
2. `loss.backward()` call karne par `grad_fn` attribute ka kya kirdaar hota hai?
3. `torch.no_grad()` context manager evaluation ke waqt memory aur speed kaise bachata hai? (Answer: Yeh graph tracking band kar deta hai jisse intermediate activations save nahi hotein).

What to Build Next:
Ek Custom Autograd Function class banayein jo `torch.autograd.Function` ko inherit kare, custom forward aur analytical backward pass implement kare, aur `torch.autograd.gradcheck` se verify kare."""

# ==============================================================================
# LESSON 4.2: Writing Custom Datasets & High-Performance DataLoaders
# ==============================================================================
LESSON_CONTENT['4.2'] = r"""### Part 1: Mental Model & South Asian Analogy
Deep Learning mein GPU aksar 90% waqt khali baitha rehta hai kyunke CPU uski bhook ke mutabiq tezi se data supply nahi kar pata. Is maslay ko 'Data Starvation Bottleneck' kehte hain.
Isay samajhne ke liye kisi Mashhoor Tandoor aur uske Ustaad/Shagird ki misaal lein:
1. The GPU (The Roaring Tandoor): Tandoor ke andar tez aag jal rahi hai. Tandoor wala (GPU) ek second mein 10 rotiyan sek kar nikalne ki taqat rakhta hai.
2. The Dataset (`__getitem__` - Aata Gundhna): Ek shagird hai jo aate ki bori se aata nikalta hai, pani daalta hai, aur pairay banata hai. Agar sirf ek shagird ho aur woh aahista aahista pairay banaye, to tandoor khali para rahega aur aag (expensive GPU compute) bekaar jalti rahegi.
3. DataLoader with Multi-Processing (`num_workers`): Aqalmand ustaad kya karta hai? Woh 4 shagird (`num_workers=4`) bithata hai. Jab tandoor mein pehli roti pak rahi hoti hai, chaaron shagird pehle se aglay 16 pairay (Prefetched Batches) bana kar tray mein sajaye baithe hote hain.
4. Pinned Memory (`pin_memory=True`): Aam tor par CPU RAM se GPU VRAM mein data copy karna do marhalon mein hota hai: pehle paged memory se page-locked memory, phir PCIe bus ke zariye GPU. Pinned Memory ek aisi express direct highway hai jo CPU RAM ki tray ko direct lock karke high-speed DMA (Direct Memory Access) ke zariye GPU ke hawale kar deti hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein DataLoader ke Batching, Worker Prefetching, aur Epoch Step calculations ko mathematically calculate karte hain.
Dataset Specifications:
- Total samples in dataset $N = 10,000$ images/texts.
- Batch Size $B = 64$ samples per batch.
- Number of background workers $W = 4$ CPU processes.

Step 1: Compute Total Steps (Batches) per Epoch:
Formula with `drop_last=False`:
$\\text{Total Steps} = \\lceil \\frac{N}{B} \\rceil = \\lceil \\frac{10000}{64} \\rceil = \\lceil 156.25 \\rceil = 157 \\text{ steps}$
Pehle 156 batches mein 64 samples honge. Aakhri 157th batch mein:
$10000 - (156 \\times 64) = 10000 - 9984 = 16 \\text{ samples}$ honge.
Agar `drop_last=True` ho to aakhri 16 samples discard ho jayenge aur exactly 156 steps honge.

Step 2: Worker Queue Distribution:
Har worker process round-robin ke tehat indices fetch karta hai:
- Worker 0: Batches 0, 4, 8, 12...
- Worker 1: Batches 1, 5, 9, 13...
- Worker 2: Batches 2, 6, 10, 14...
- Worker 3: Batches 3, 7, 11, 15...

Step 3: IO Throughput Calculation:
Agar har sample 50 KB ka hai:
Batch Size in Bytes $= 64 \\times 50 \\text{ KB} = 3,200 \\text{ KB} \\approx 3.125 \\text{ MB per batch}$.
Agar GPU ko ek batch train karne mein 15 milliseconds lagte hain:
Required Data Supply Throughput:
$\\text{Target Throughput} = \\frac{3.125 \\text{ MB}}{0.015 \\text{ seconds}} \\approx 208.33 \\text{ MB/sec}$.
Pinned Memory aur 4 workers ke baghair standard single-thread Python sirf 40 MB/sec supply kar pata hai, jisse GPU 80% waqt idle rehta hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum custom PyTorch `Dataset` class, dynamic memory padding collate function, aur high-performance multi-threaded `DataLoader` implement karte hain.

```python
import torch
from torch.utils.data import Dataset, DataLoader
from typing import List, Dict, Any

# 1. Custom Dataset implementing PyTorch Core Protocol
class TextClassificationDataset(Dataset):
    \"\"\"Custom Dataset representing text sequences and sentiment labels.\"\"\"
    def __init__(self, token_sequences: List[List[int]], labels: List[int]) -> None:
        assert len(token_sequences) == len(labels), "Features and labels must match in length."
        self.sequences = token_sequences
        self.labels = labels

    def __len__(self) -> int:
        \"\"\"Enables len(dataset) to allow batch step calculations.\"\"\"
        return len(self.sequences)

    def __getitem__(self, index: int) -> Dict[str, torch.Tensor]:
        \"\"\"Enables random access dataset[i] indexing returning standard PyTorch tensors.\"\"\"
        return {
            "input_ids": torch.tensor(self.sequences[index], dtype=torch.long),
            "label": torch.tensor(self.labels[index], dtype=torch.long)
        }

# 2. Custom Collate Function for Dynamic Padding
def dynamic_padding_collate_fn(batch: List[Dict[str, torch.Tensor]]) -> Dict[str, torch.Tensor]:
    \"\"\"Pads variable-length sequences to maximum length in current batch only.\"\"\"
    # Extract lists of tensors
    sequences = [item["input_ids"] for item in batch]
    labels = torch.stack([item["label"] for item in batch])
    
    # Pad sequences with 0 (PAD token ID) to batch max length
    padded_sequences = torch.nn.utils.rnn.pad_sequence(
        sequences, 
        batch_first=True, 
        padding_value=0
    )
    
    return {
        "input_ids": padded_sequences,  # Shape: [batch_size, max_seq_len_in_batch]
        "labels": labels                # Shape: [batch_size]
    }

# Execution test
if __name__ == "__main__":
    # Synthetic variable-length tokenized reviews
    toy_sequences = [
        [101, 45, 90, 102],            # Length 4
        [101, 80, 102],                # Length 3
        [101, 23, 56, 78, 99, 102],    # Length 6
        [101, 12, 102],                # Length 3
        [101, 65, 43, 21, 102]         # Length 5
    ]
    toy_labels = [1, 0, 1, 0, 1]

    dataset = TextClassificationDataset(toy_sequences, toy_labels)
    print(f"Dataset Size: {len(dataset)} samples")

    # Production DataLoader setup
    loader = DataLoader(
        dataset,
        batch_size=2,
        shuffle=True,
        collate_fn=dynamic_padding_collate_fn,
        drop_last=False
    )

    print("\\nIterating over Batches with Dynamic Padding:")
    for batch_idx, batch in enumerate(loader, 1):
        ids = batch["input_ids"]
        lbls = batch["labels"]
        print(f"  Batch {batch_idx} -> input_ids shape: {list(ids.shape)}, labels: {lbls.tolist()}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Padding Entire Dataset to 512 Tokens Globally: Tamam samples ko pehle hi 512 tokens tak pad kar dena be-inteha VRAM zaaya karta hai agar zyada tar sentences sirf 50 tokens ke hon. Hamesha dynamic batch-level padding (`collate_fn`) use karein jo sirf us batch ke longest sequence tak pad kare.
2. Setting `num_workers > 0` on Windows Without `if __name__ == '__main__':`: Windows par multi-processing fork ke bajaye spawn use karti hai. Agar script ke entry point par main guard na ho to naye processes infinite loop mein dobara script run karte hain aur system freeze ho jata hai.
3. Reading Disk Files Inside `__len__()`: Dataset class ke `__len__` method ke andar agar aap disk scan ya database query chalayenge to poora pipeline slow ho jata hai. Dataset length hamesha `__init__` ke waqt pre-compute karein.

Zero-GPU Tip:
DataLoader pipeline ka 99% kaam CPU aur disk I/O par hota hai. Colab ke free tier CPU par aap `num_workers=2` ke sath data streaming aur augmentation benchmark kar sakte hain taake verify ho sake ke per-batch latency under 10ms hai.

Self-Check Questions:
1. PyTorch Dataset protocol ke do lazmi methods kaun se hain? (Answer: `__len__` aur `__getitem__`).
2. Custom `collate_fn` ka kya kirdaar hota hai aur variable-length sequences mein yeh kyun zaroori hai?
3. DataLoader mein `pin_memory=True` CPU se GPU data transfer ko kaise accelerate karti hai?

What to Build Next:
Ek Resilient Streaming Dataset class banayein jo disk par mojud bari JSONL file ko line-by-line read kare, sharded multi-worker streaming support kare, aur token batches yield kare."""

# ==============================================================================
# LESSON 4.3: Activation Functions & Weight Initialization Math (He, Xavier)
# ==============================================================================
LESSON_CONTENT['4.3'] = r"""### Part 1: Mental Model & South Asian Analogy
Deep Neural Networks mein do khamosh qaatil hote hain jo model ko pehle hi step par mar dete hain: **Vanishing Gradients** aur **Exploding Gradients**. In dono qaatilon se bachane ka kaam Activation Functions aur Weight Initialization karti hain.
Isay samajhne ke liye kisi Shehar ke 50 Chowkidaron ki Qataar (Chinese Whispers / Telephone Game) ki misaal lein:
1. Linear Networks (Bila Activation Ke Be-faida): Agar aap 50 linear layers ko aapas mein jod dein ($y = W_3(W_2(W_1 x))$), to linear algebra ka qanoon hai ke multiple linear transformations mil kar sirf ek akeli linear transformation ban jati hain ($W_{\text{net}} = W_3 W_2 W_1$). 50 layers lagane ka koi faida nahi hua! Non-linear activation function (jaise ReLU ya GELU) har layer ke baad zameen mein ek mourr (bend) daalti hai taake model complex curves aur patterns seekh sake.
2. Sigmoid Vanishing Gradient (Aawaz Ka Ghayab Hona): Farz karein pehla chowkidar aakhri chowkidar tak koi khabar bhejta hai. Har chowkidar suni hui baat ka sirf 20% hissa aage bolta hai (Sigmoid ka maximum derivative sirf 0.25 hai!). 10 chowkidaron ke baad aawaz itni dheemi ho jati hai ke aakhri chowkidar tak sirf khamoshi pohnchti hai ($0.25^{10} \approx 0.00000095$). Model ke shuru ke weights tak gradient pohnchta hi nahi aur training ruk jati hai!
3. Dead ReLU Problem (Coma Mein Jana): ReLU function negative numbers ko seedha zero kar deta hai ($f(x) = \max(0, x)$). Agar kisi neuron ka weight bohot bara negative ho jaye to woh har input par 0 output deta hai aur uska derivative bhi hamesha 0 rehta hai. Woh neuron hamesha ke liye coma mein chala jata hai (Dead Neuron)! Modern LLMs is liye **GELU** ya **SwiGLU** use karte hain jahan negative hissay par bhi choti si smooth dhalan rehti hai.
4. Weight Initialization (He & Xavier Math): Agar shuru mein weights bohot bare hon to signal explode kar ke infinity ban jata hai. Agar bohot chote hon to signal zero ban jata hai. Xavier aur He initialization weights ke variance ko layers ke dimensions ke mutabiq theek us satah par set karti hain jahan signal 100 layers ke baad bhi bilkul barabar rehta hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Xavier (Glorot) aur He (Kaiming) initialization ki mathematical variance preservation ko trace karein.
Formula for Layer Output Variance:
$\text{Var}(y) = N_{\text{in}} \times \text{Var}(w) \times \text{Var}(x)$
Signal ko stable rakhne ke liye shart yeh hai ke output ka variance input ke variance ke barabar ho:
$\text{Var}(y) = \text{Var}(x) \implies N_{\text{in}} \times \text{Var}(w) = 1 \implies \text{Var}(w) = \frac{1}{N_{\text{in}}}$

1. He (Kaiming) Normal Initialization (for ReLU activations):
Chunke ReLU aadhe inputs ko zero kar deta hai, is liye variance aadhi ho jati hai. Is kami ko poora karne ke liye numerator mein 2 lagaya jata hai:
$\sigma_{\text{He}}^2 = \frac{2}{N_{\text{in}}} \implies \sigma_{\text{He}} = \sqrt{\frac{2}{N_{\text{in}}}}$

2. Xavier (Glorot) Normal Initialization (for Tanh / Sigmoid):
$\sigma_{\text{Xavier}} = \sqrt{\frac{2}{N_{\text{in}} + N_{\text{out}}}}$

Worked Numeric Example:
Layer with $N_{\text{in}} = 512$ inputs, $N_{\text{out}} = 256$ outputs, using ReLU activation.

Step 1: Compute Target Standard Deviation ($\sigma_{\text{He}}$)
$\sigma_{\text{He}} = \sqrt{\frac{2}{512}} = \sqrt{\frac{1}{256}} = \frac{1}{16} = 0.0625$

Step 2: Initialize Weights Matrix $W$:
Har weight standard normal distribution $\mathcal{N}(0, 1)$ se sample hota hai aur $\sigma_{\text{He}}$ se multiply hota hai:
$W_{ij} \sim \mathcal{N}(0, 1) \times 0.0625$
Agar koi naive developer $W_{ij} \sim \mathcal{N}(0, 1)$ direct chhor deta:
Output variance $\text{Var}(y) = 512 \times 1.0 = 512.0$ ho jati! Har layer ke baad variance 512 guna barhti aur 4 layers ke baad numbers $512^4 \approx 6.8 \times 10^{10}$ par pohnch kar foran `NaN` crash de dete!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum activations (ReLU, GELU, SwiGLU), He/Xavier initializers, aur layer variance propagation test ko implement karte hain.

```python
import torch
import torch.nn as nn
import math

# 1. Modern Activation Functions from Scratch
def custom_gelu(x: torch.Tensor) -> torch.Tensor:
    \"\"\"Gaussian Error Linear Unit (GELU) used in BERT and GPT architectures.\"\"\"
    # Standard approximation formula: 0.5 * x * (1 + tanh(sqrt(2/pi) * (x + 0.044715 * x^3)))
    return 0.5 * x * (1.0 + torch.tanh(math.sqrt(2.0 / math.pi) * (x + 0.044715 * torch.pow(x, 3))))

class SwiGLUBlock(nn.Module):
    \"\"\"Swish Gated Linear Unit (SwiGLU) used in modern LLaMA & DeepSeek models.\"\"\"
    def __init__(self, dim: int, hidden_dim: int) -> None:
        super().__init__()
        self.w_gate = nn.Linear(dim, hidden_dim, bias=False)
        self.w_up = nn.Linear(dim, hidden_dim, bias=False)
        self.w_down = nn.Linear(hidden_dim, dim, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Swish(gate) * up_projection
        gate = torch.nn.functional.silu(self.w_gate(x))
        up = self.w_up(x)
        return self.w_down(gate * up)

# 2. Custom He / Kaiming Weight Initialization Function
def initialize_weights_he_normal(module: nn.Module) -> None:
    \"\"\"Iterates over module layers and applies exact He normal initialization.\"\"\"
    if isinstance(module, nn.Linear):
        fan_in = module.weight.size(1)
        std = math.sqrt(2.0 / fan_in)
        # In-place normal fill with calculated standard deviation
        with torch.no_grad():
            module.weight.normal_(mean=0.0, std=std)
            if module.bias is not None:
                module.bias.zero_()

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    
    # Create 5-layer deep linear network
    layers = []
    dim = 256
    for _ in range(5):
        linear = nn.Linear(dim, dim)
        initialize_weights_he_normal(linear)
        layers.extend([linear, nn.ReLU()])
    deep_net = nn.Sequential(*layers)

    # Pass unit-variance input
    x_input = torch.randn(32, dim)  # Batch: 32, Dim: 256
    print(f"Input Variance:  {x_input.var().item():.4f}")

    x_out = deep_net(x_input)
    print(f"Output Variance: {x_out.var().item():.4f} (Maintained across 5 layers without vanishing/exploding!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Using Sigmoid in Deep Hidden Layers: 5 layers se gehre network mein hidden layers par Sigmoid lagana vanishing gradient ki wazeh dawat hai. Sigmoid ko sirf aakhri binary classification output layer par use karein. Hidden layers ke liye hamesha GELU, SiLU, ya ReLU use karein.
2. Initializing Weights with All Zeros: Agar aap tamam weights ko 0 se initialize kar dete hain to tamam neurons bilkul aik jaisa gradient calculate karte hain (Symmetry Problem) aur network kabhi alag alag features seekh hi nahi pata.
3. Ignoring Fan-In in Custom Layers: Weight initialization karte waqt hardcoded `std=0.01` rakhne se agar layer ka dimension 4096 ho to signal collapse ho jata hai. Hamesha dynamic `math.sqrt(2.0 / fan_in)` use karein.

Zero-GPU Tip:
Activation functions aur initialization variance experiments CPU par chalana behtareen rehta hai. Ek chotay 5-layer loop mein 100 samples pass karke dekhein ke output ki variance zero ya infinity to nahi ho rahi.

Self-Check Questions:
1. He Initialization aur Xavier Initialization mein mathematical farq kya hai aur He initialization ReLU ke sath kyun zaroori hai?
2. Dead ReLU problem kya hai aur GELU ya LeakyReLU isay kaise solve karte hain?
3. Neural network mein non-linear activation function na ho to 100 layers ka network kis cheez ke barabar hota hai? (Answer: Ek single linear layer ke barabar).

What to Build Next:
Ek Variance Tracker script banayein jo 20-layer deep network mein har layer ke baad output tensor ki mean aur variance calculate kare aur plot kare ke kahan signal explode ya vanish ho raha hai."""

# ==============================================================================
# LESSON 4.4: Optimizers Under The Hood: Momentum, RMSProp & AdamW
# ==============================================================================
LESSON_CONTENT['4.4'] = r"""### Part 1: Mental Model & South Asian Analogy
Standard Gradient Descent seedhi sadhi dhalan par to theek chalta hai, lekin jab loss surface par tang wadiyan (Ravines), gadhay, aur saddle points aate hain to aam gradient descent phans jata hai. Isay nikalne ke liye modern optimizers (Momentum, RMSProp, aur AdamW) use hote hain.
Isay samajhne ke liye kisi Khel ke Maidan aur Heavy Cricket Ball ki misaal lein:
1. Standard SGD (Chhota Kankad): Aam SGD ek halkay se kankad jaisa hai. Har step par jidhar thodi si dhalan milti hai udhar ludhak jata hai. Agar aage koi chota sa pathar ya local minimum aa jaye to wahan atak kar ruk jata hai.
2. Momentum (Bhari Heavy Bowling Ball): Momentum aisi misaal hai jese lohay ki 10 kilo ki bhari ball ko dhalan par roll kar diya jaye. Ball ki apni raftaar (Velocity / Inertia) hoti hai. Agar raste mein chota mota gadha ya seedhi satah aaye bhi to pichli raftaar ki wajah se ball use phlaang kar aage nikal jati hai! Yeh oscillations ko damp karti hai aur lambi dhalan par speed barhati hai.
3. RMSProp (Paharon Ki Chadhaee Ka Gear): Kuch directions mein dhalan bohot shadeed hoti hai aur kuch directions mein bohot aahista. RMSProp har weight ke pichle gradients ka square average dekhta hai. Jis direction mein gradient bohot bara ho wahan learning rate ko aahista kar deta hai, aur jis direction mein gradient bohot chota ho wahan learning rate ko boost karta hai.
4. Adam & AdamW (The Gold Standard): Adam ne Momentum (First Moment $m$) aur RMSProp (Second Moment $v$) dono ko aapas mein mila diya. Lekin purane Adam mein ek fatal mathematical bug tha: L2 Regularization weight decay ko gradient ke sath mix kar deti thi. 2017 mein Loshchilov aur Hutter ne **AdamW** banaya jisne Weight Decay ko gradient update se Decouple (alag) kar diya. 2026 mein dunya ka har bara Transformer (LLaMA, GPT-4, DeepSeek) 100% AdamW par train hota hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein AdamW optimizer ke ek single step ki mukammal calculation hath se concrete numbers ke sath karein.
Hyperparameters:
- Learning rate $\eta = 0.1$
- First moment decay $\beta_1 = 0.9$
- Second moment decay $\beta_2 = 0.999$
- Epsilon $\epsilon = 10^{-8}$
- Weight decay $\lambda = 0.01$

Current State at Step $t = 1$:
- Weight $w_0 = 2.0$
- Incoming Gradient $g_1 = 0.5$
- Initial first moment $m_0 = 0.0$
- Initial second moment $v_0 = 0.0$

Step 1: Update Biased First Moment ($m_1$)
$m_1 = \beta_1 m_0 + (1 - \beta_1) g_1$
$m_1 = (0.9 \times 0.0) + (0.1 \times 0.5) = 0.0500$

Step 2: Update Biased Second Moment ($v_1$)
$v_1 = \beta_2 v_0 + (1 - \beta_2) g_1^2$
$v_1 = (0.999 \times 0.0) + (0.001 \times 0.5^2) = 0.001 \times 0.25 = 0.00025$

Step 3: Bias Corrections (Crucial for early steps!)
$\hat{m}_1 = \frac{m_1}{1 - \beta_1^t} = \frac{0.0500}{1 - 0.9^1} = \frac{0.0500}{0.1} = 0.5000$
$\hat{v}_1 = \frac{v_1}{1 - \beta_2^t} = \frac{0.00025}{1 - 0.999^1} = \frac{0.00025}{0.001} = 0.2500$

Step 4: Compute Adaptive Gradient Step
$\Delta w_{\text{grad}} = \frac{\hat{m}_1}{\sqrt{\hat{v}_1} + \epsilon} = \frac{0.5000}{\sqrt{0.2500} + 10^{-8}} = \frac{0.5000}{0.5000} = 1.0000$

Step 5: Apply AdamW Decoupled Parameter Update
AdamW updates weight in two explicit parts: Decoupled weight decay + Gradient step:
$w_1 = w_0 - (\eta \times \lambda \times w_0) - (\eta \times \Delta w_{\text{grad}})$
$w_1 = 2.0 - (0.1 \times 0.01 \times 2.0) - (0.1 \times 1.0000)$
$w_1 = 2.0 - 0.0020 - 0.1000 = 1.8980$
Dekhein! Weight decay ne weight ko $0.002$ shrink kiya, aur gradient update ne $0.100$ step liya! Yeh separation AdamW ki asli taqat hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum pure NumPy ke sath complete AdamW optimizer class from first principles implement karte hain aur PyTorch ke standard optimizer interface ke sath verify karte hain.

```python
import numpy as np
from typing import List

class CustomAdamW:
    \"\"\"Production implementation of AdamW optimizer with decoupled weight decay.\"\"\"
    def __init__(
        self, 
        params: List[np.ndarray], 
        lr: float = 1e-3, 
        betas: tuple[float, float] = (0.9, 0.999), 
        eps: float = 1e-8, 
        weight_decay: float = 0.01
    ) -> None:
        self.params = params
        self.lr = lr
        self.beta1, self.beta2 = betas
        self.eps = eps
        self.weight_decay = weight_decay
        self.step_count = 0

        # State buffers for first and second moments
        self.m = [np.zeros_like(p) for p in self.params]
        self.v = [np.zeros_like(p) for p in self.params]

    def step(self, grads: List[np.ndarray]) -> None:
        \"\"\"Executes single optimization step across all parameters.\"\"\"
        self.step_count += 1

        for i, (p, g) in enumerate(zip(self.params, grads)):
            # 1. Update biased 1st moment estimate
            self.m[i] = self.beta1 * self.m[i] + (1.0 - self.beta1) * g
            # 2. Update biased 2nd raw moment estimate
            self.v[i] = self.beta2 * self.v[i] + (1.0 - self.beta2) * (g ** 2)

            # 3. Compute bias-corrected estimates
            m_hat = self.m[i] / (1.0 - (self.beta1 ** self.step_count))
            v_hat = self.v[i] / (1.0 - (self.beta2 ** self.step_count))

            # 4. Decoupled Weight Decay update (Directly on parameter)
            p -= self.lr * self.weight_decay * p

            # 5. Gradient Descent step with adaptive scaling
            step_direction = m_hat / (np.sqrt(v_hat) + self.eps)
            p -= self.lr * step_direction

# Execution test
if __name__ == "__main__":
    np.random.seed(42)
    # Target parameter to optimize towards zero
    param = np.array([2.0, -3.0], dtype=np.float32)
    optimizer = CustomAdamW([param], lr=0.1, weight_decay=0.01)

    print(f"Initial Parameter State: {param}")
    for step_num in range(1, 11):
        # Simulated gradient pointing towards 0 (g = 2 * param)
        grad = 2.0 * param
        optimizer.step([grad])
        if step_num in [1, 5, 10]:
            print(f"  Step {step_num:02d} -> Param: {param.round(4)}, Norm: {np.linalg.norm(param):.4f}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Confusing L2 Regularization in Loss with AdamW Weight Decay: Standard Adam mein loss function mein `0.5 * lambda * w^2` add karne se gradient mein `lambda * w` shamil ho jata hai jo adaptive denominator $\sqrt{v}$ se divide ho jata hai, jisse baray weights par decay kam aur chotay weights par decay zyada ho jati hai. AdamW mein hamesha decoupled decay use karein.
2. Forgetting Learning Rate Warmup on AdamW: Training ke shuru ke steps mein first aur second moments unstable hote hain. Agar shuru mein hi full learning rate laga diya jaye to model destabilize ho jata hai. Hamesha pehle 1000 steps par linear warmup lagayein.
3. Setting Epsilon ($\epsilon$) Too Small in Mixed Precision: FP16 training karte waqt agar $\epsilon = 10^{-16}$ ho to floating point underflow ho jata hai. FP16 ke liye hamesha `eps=1e-6` ya `1e-8` use karein.

Zero-GPU Tip:
AdamW ka math purely element-wise array operations par chalta hai. 10 lakh parameters ke optimizer buffers CPU RAM mein sirf chund MegaBytes leti hain. Small-scale experiments par aap CPU par hi convergence speed benchmark kar sakte hain.

Self-Check Questions:
1. AdamW aur standard Adam mein bunyadi mathematical farq kya hai?
2. Bias correction factor ($1 - \beta^t$) training ke shuru mein kyun zaroori hota hai?
3. Momentum parameter ($\beta_1 = 0.9$) optimization ko saddle points se nikalne mein kaise madad karta hai?

What to Build Next:
Ek Cosine Annealing Learning Rate Scheduler with Warmup class implement karein jo har epoch par AdamW ki learning rate ko mathematically adjust kare aur schedule curve print kare."""

# ==============================================================================
# LESSON 4.5: Loss Landscapes, Overfitting & Modern Regularization
# ==============================================================================
LESSON_CONTENT['4.5'] = r"""### Part 1: Mental Model & South Asian Analogy
Deep Learning models mein lakhoon ya arabon parameters hote hain. Agar hum unhe khuli chhoot de dein to woh training data ke har akele nuqtay ko ratta maar lete hain (Overfitting). Jab unseen test data samne aata hai to model buri tarah fail ho jata hai.
Isay samajhne ke liye kisi Ratta-Mar Shagird aur Imtihan ki misaal lein:
1. Overfitting (Pichle 5 Saal Ke Papers Ka Ratta): Ek shagird hai jisne pichle 5 saal ke exam papers ke tamam sawalat aur jawab zubani yaad kar liye hain. Agar examiner pichle paper se bilkul wahi sawal daal de to bacha 100% number le leta hai. Lekin agar examiner sawal mein sirf number badal de (jaise 5 ki jagah 7 likh de), to ratta-mar bacha zero number leta hai kyunke usne concept nahi seekha!
2. Loss Landscapes (Pahari Ka Rough Khaka): Model ke Loss ka naqsha (Landscape) kaisa hai? 
   - Acha Model (Flat Minimum): Loss surface par ek wasee aur hamwar maidan hai. Agar test data mein thoda sa farq bhi ho to loss thoda sa hi badalta hai.
   - Overfitted Model (Sharp Minimum): Loss surface par bohot gehra lekin nihayat tang aur sooi jaisa gadha hai. Training data bilkul us sooi ki nok par baitha hai. Thoda sa bhi test variation aate hi model sidha pahari se gir jata hai.
3. Dropout (Team Mein Rozana Random Khiladiyon Ko Chhutti Dena): Dropout ek bohot zabardast tarbiyati tareeqa hai. Har training step par hum random tor par 20% ya 50% neurons ko bilkul switch off (zero) kar dete hain! Iska faida kya hota hai? Koi bhi akela neuron doosre neuron par sahara nahi le sakta. Har neuron ko azadana tor par zaroori features seekhne parte hain. Nateeja: Model bohot robust ban jata hai.
4. Weight Decay ($L_2$ Regularization): Yeh model ke weights par ek tax laga deta hai: "Jitna bara weight rakhoge, utna zyada tax (Loss penalty) dena parega." Iski wajah se weights hamesha chotay aur smooth rehte hain aur koi akela feature dominant nahi ho pata.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Inverted Dropout ki forward aur backward scaling math ko trace karte hain.
Standard Dropout problem: Agar training ke waqt 50% neurons band hon to testing ke waqt tamam neurons on hone par signal ki taqat double ho jayegi.
Inverted Dropout Solution:
Training ke waqt hi bache hue neurons ko $\frac{1}{1 - p}$ se divide (scale up) kar diya jata hai taake testing ke waqt zero modification karni paray!

Formula for Inverted Dropout:
$y = \frac{m \odot x}{1 - p}$
Jahan:
- $p$: Dropout probability (e.g. $p = 0.5$)
- $m \in \{0, 1\}$: Binary mask sampled from Bernoulli distribution with $P(m = 1) = 1 - p$
- Scaling factor: $\frac{1}{1 - 0.5} = \frac{1}{0.5} = 2.0$

Worked Numeric Example:
Input Activation Vector $x = [4.0, 6.0, 2.0, 8.0]$
Dropout rate $p = 0.5$.

Step 1: Sample Random Binary Mask $m$
Farz karein random sample nikla: $m = [1, 0, 1, 0]$ (Neuron 1 aur 3 band ho gaye!)

Step 2: Apply Mask and Scale Up:
- Element 0: $\frac{1 \times 4.0}{0.5} = 4.0 \times 2.0 = 8.0$
- Element 1: $\frac{0 \times 6.0}{0.5} = 0.0$
- Element 2: $\frac{1 \times 2.0}{0.5} = 2.0 \times 2.0 = 4.0$
- Element 3: $\frac{0 \times 8.0}{0.5} = 0.0$

Output Vector $y = [8.0, 0.0, 4.0, 0.0]$.

Step 3: Verify Expected Value Preservation:
Original Mean: $\frac{4 + 6 + 2 + 8}{4} = \frac{20}{4} = 5.0$
Dropout Output Mean: $\frac{8.0 + 0.0 + 4.0 + 0.0}{4} = \frac{12.0}{4} = 3.0$
Mathematical Expectation across random masks:
$\mathbb{E}[y] = (1 - p) \times \left( \frac{x}{1 - p} \right) + p \times 0 = x$!
Inverted Dropout ki wajah se test time (`model.eval()`) par signal scaling bilkul identical rehti hai aur koi computation nahi karni parti.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum custom Inverted Dropout layer, L2 Weight Decay penalty calculation, aur train vs eval mode switching ko pure PyTorch mein implement karte hain.

```python
import torch
import torch.nn as nn

class CustomInvertedDropout(nn.Module):
    \"\"\"Production implementation of Inverted Dropout from first principles.\"\"\"
    def __init__(self, p: float = 0.5) -> None:
        super().__init__()
        assert 0.0 <= p < 1.0, f"Dropout probability must be in [0, 1), got {p}"
        self.p = p

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # In eval mode (testing/inference), dropout is identity pass-through
        if not self.training or self.p == 0.0:
            return x

        # Sample binary mask from Bernoulli distribution
        keep_prob = 1.0 - self.p
        # Bernoulli mask: 1 with probability keep_prob, 0 with probability p
        mask = (torch.rand_like(x) < keep_prob).float()
        
        # Scale up surviving activations by (1 / keep_prob)
        return (x * mask) / keep_prob

class RegularizedMLP(nn.Module):
    \"\"\"Multi-layer perceptron equipped with Dropout and Weight Decay hooks.\"\"\"
    def __init__(self, in_features: int, hidden_dim: int, out_features: int, drop_rate: float = 0.3) -> None:
        super().__init__()
        self.fc1 = nn.Linear(in_features, hidden_dim)
        self.dropout = CustomInvertedDropout(p=drop_rate)
        self.act = nn.GELU()
        self.fc2 = nn.Linear(hidden_dim, out_features)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.act(self.fc1(x))
        h = self.dropout(h)
        return self.fc2(h)

    def compute_l2_penalty(self, weight_decay: float) -> torch.Tensor:
        \"\"\"Calculates analytical L2 regularization term sum(w^2) over weights.\"\"\"
        l2_sum = torch.tensor(0.0, device=self.fc1.weight.device)
        for name, param in self.named_parameters():
            if "weight" in name and param.requires_grad:
                l2_sum = l2_sum + torch.sum(param ** 2)
        return 0.5 * weight_decay * l2_sum

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    model = RegularizedMLP(in_features=8, hidden_dim=16, out_features=2, drop_rate=0.5)

    sample_x = torch.ones(2, 8)  # Batch: 2, Features: 8

    # 1. Training Mode Execution (Dropout Active)
    model.train()
    train_out = model(sample_x)
    print("Training Mode Output (Stochastic):")
    print(train_out)

    # 2. Evaluation Mode Execution (Dropout Inactive / Deterministic)
    model.eval()
    eval_out_1 = model(sample_x)
    eval_out_2 = model(sample_x)
    print("\\nEvaluation Mode Outputs (Deterministic Check):")
    print("Difference between consecutive runs:", torch.norm(eval_out_1 - eval_out_2).item())

    # 3. L2 Penalty Inspection
    penalty = model.compute_l2_penalty(weight_decay=0.01)
    print(f"Computed L2 Regularization Penalty: {penalty.item():.6f}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Forgetting `model.eval()` During Inference: Inference karte waqt agar aap `model.eval()` lagana bhool jate hain to Dropout active rehta hai aur Batch Normalization train statistics use karta hai, jisse har request par random aur kharab outputs aate hain.
2. Applying Dropout on Very Small Datasets: Chotay datasets par agar aap high dropout ($p=0.5$) lagate hain to model underfit ho jata hai aur kuch seekh hi nahi pata. Chotay datasets ke liye Data Augmentation aur Weight Decay behtar hain.
3. Applying Weight Decay to Biases and LayerNorm Weights: Production LLMs mein LayerNorm scales aur linear biases ko weight decay nahi kiya jata kyunke yeh shift parameters hote hain. Hamesha parameter groups bana kar sirf 2D weight matrices par weight decay lagayein.

Zero-GPU Tip:
Dropout aur weight decay regularizations CPU par exact mathematical simulation ke sath test kiye ja sakte hain. `model.eval()` aur `model.train()` ke behaviour ko verify karne ke liye kisi GPU ki zaroorat nahi hoti.

Self-Check Questions:
1. Inverted Dropout traditional standard dropout se kyun behtar hota hai?
2. Overfitting ko identify karne ke liye Training Loss aur Validation Loss curves mein kya dekha jata hai?
3. LayerNorm aur Biases par Weight Decay kyun nahi lagayi jati?

What to Build Next:
Ek Overfitting vs Regularization Benchmark script banayein jo ek synthetic noisy dataset par unregularized network vs Dropout+WeightDecay network train kare aur dono ke test error ka farq print kare."""

# ==============================================================================
# LESSON 4.6: Module 4 Capstone: Build & Profile a Modular Deep Neural Network
# ==============================================================================
LESSON_CONTENT['4.6'] = r"""### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne Deep Learning ke tamam bunyadi pillars (Autograd mechanics, Custom Dataset pipelines, Weight initializations, Optimizers, aur Regularization techniques) mukammal kar liye hain. Ab waqt hai aapke **Pehle Complete PyTorch Production Capstone** ka!
Is Capstone project ka zehni khaka kisi Bare Modern Hospital ke Telemetry aur Surgery ICU jaisa hai:
1. Modular Architecture (Specialized Doctors): Network ko rigid single block nahi banaya jata. Har layer ek modular component hoti hai: Input Projection, Hidden Residual Blocks, Layer Normalization, aur Classification Head.
2. The Patient Monitor (Real-Time Profiler & Telemetry): Surgery karte waqt doctor ke samne monitor hota hai jo dil ki dharkan (Loss), oxygen level (Accuracy), aur blood pressure (Gradient Norms) real-time dikhata hai. Agar achanak dil ki dharkan ruk jaye (Vanishing Gradients) ya blood pressure phat jaye (Exploding Gradients), to alarm bajta hai.
3. Checkpoint Vault (Medical Records Archive): Har surgery ke baad patient ki recovery state disk par `.pt` checkpoint file mein save ki jati hai taake agar light chali jaye ya system reboot ho to wahin se resume kiya ja sake.

Yeh Capstone project ek modular deep neural network train karta hai, validation metrics profile karta hai, aur weights safely export karta hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Training Loop ke per-step Floating Point Operations (FLOPs) aur Parameter Count ka exact hisab lagayein.
Model Architecture Specifications:
- Input Features $D_{\text{in}} = 64$
- Hidden Dimension $D_{\text{hidden}} = 128$
- Output Classes $C = 4$
- Layers: Linear 1 ($64 \to 128$) $\to$ GELU $\to$ Linear 2 ($128 \to 128$) $\to$ GELU $\to$ Linear 3 ($128 \to 4$).

Step 1: Compute Total Learnable Parameters
- Layer 1 Weights: $64 \times 128 = 8,192$. Biases: $128$. Total: $8,320$.
- Layer 2 Weights: $128 \times 128 = 16,384$. Biases: $128$. Total: $16,512$.
- Layer 3 Weights: $128 \times 4 = 512$. Biases: $4$. Total: $516$.
Total Model Parameters:
$P_{\text{total}} = 8,320 + 16,512 + 516 = 25,348 \text{ parameters}$.

Step 2: FLOPs Calculation per Forward Pass Sample
Har matrix multiplication $y = W x$ mein har weight ke liye 1 multiply aur 1 add (2 FLOPs) hote hain:
- Layer 1: $2 \times (64 \times 128) = 16,384 \text{ FLOPs}$
- Layer 2: $2 \times (128 \times 128) = 32,768 \text{ FLOPs}$
- Layer 3: $2 \times (128 \times 4) = 1,024 \text{ FLOPs}$
Total FLOPs per sample $\approx 50,176 \text{ FLOPs} \approx 0.05 \text{ MFLOPs}$.
Batch size 32 ke liye ek forward pass sirf $1.6 \text{ MFLOPs}$ leta hai jo standard laptop CPU par 0.2 milliseconds mein execute ho jata hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete modular deep neural network, He initialization, AdamW optimizer with cosine schedule, gradient clipping, training/validation loop, aur checkpoint export implement karte hain.

```python
import os
import tempfile
import time
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

# 1. Modular Deep Neural Network Architecture
class DeepModularClassifier(nn.Module):
    def __init__(self, in_features: int, hidden_dim: int, num_classes: int, dropout_p: float = 0.2) -> None:
        super().__init__()
        self.input_layer = nn.Sequential(
            nn.Linear(in_features, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout_p)
        )
        self.residual_block = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout_p)
        )
        self.head = nn.Linear(hidden_dim, num_classes)
        self._initialize_weights()

    def _initialize_weights(self) -> None:
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight, nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0.0)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Input projection: [B, in_features] -> [B, hidden_dim]
        h = self.input_layer(x)
        # Residual skip connection: h + F(h)
        h = h + self.residual_block(h)
        # Output classification logits: [B, num_classes]
        return self.head(h)

# 2. Synthetic Data & DataLoader Pipeline
torch.manual_seed(42)
N_TRAIN, N_VAL, IN_DIM, N_CLASSES = 800, 200, 64, 4

X_train = torch.randn(N_TRAIN, IN_DIM)
y_train = torch.randint(0, N_CLASSES, (N_TRAIN,))
X_val = torch.randn(N_VAL, IN_DIM)
y_val = torch.randint(0, N_CLASSES, (N_VAL,))

train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=32, shuffle=True)
val_loader = DataLoader(TensorDataset(X_val, y_val), batch_size=32, shuffle=False)

# 3. Production Training Engine with Gradient Clipping
model = DeepModularClassifier(in_features=IN_DIM, hidden_dim=128, num_classes=N_CLASSES)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-2)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=5)

print("Starting Modular Capstone Training Loop...")
for epoch in range(1, 6):
    model.train()
    total_train_loss = 0.0
    
    for batch_x, batch_y in train_loader:
        optimizer.zero_grad()
        logits = model(batch_x)
        loss = criterion(logits, batch_y)
        loss.backward()
        
        # Production Gradient Clipping to prevent explosion
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        
        optimizer.step()
        total_train_loss += loss.item() * batch_x.size(0)

    scheduler.step()
    avg_train_loss = total_train_loss / N_TRAIN

    # Validation Phase
    model.eval()
    val_correct, total_val = 0, 0
    with torch.no_grad():
        for batch_x, batch_y in val_loader:
            val_logits = model(batch_x)
            preds = torch.argmax(val_logits, dim=1)
            val_correct += (preds == batch_y).sum().item()
            total_val += batch_y.size(0)

    val_acc = (val_correct / total_val) * 100.0
    print(f"Epoch {epoch:02d}/05 | Train Loss: {avg_train_loss:.4f} | Val Accuracy: {val_acc:.1f}%")

# 4. Checkpoint Serialization
with tempfile.TemporaryDirectory() as tmp_dir:
    ckpt_path = os.path.join(tmp_dir, "model_checkpoint.pt")
    torch.save({
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
        "epoch": 5
    }, ckpt_path)
    print(f"\\nModel Checkpoint successfully persisted to: {ckpt_path}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Missing `torch.nn.utils.clip_grad_norm_`: Deep architectures mein agar koi outlier batch aa jaye to gradient achanak explode kar sakta hai. Hamesha `max_norm=1.0` ke sath gradient clipping lagana production best practice hai.
2. Saving Model with Entire Class Code (`torch.save(model)`): Poori class save karne se agar aap baad mein code refactor karein to pickle load fail ho jata hai. Hamesha sirf parameters save karein: `torch.save(model.state_dict(), path)`.
3. Not Averaging Loss by Batch Size Correctly: `loss.item()` ko direct add karne se aakhri partial batch ka wazan baqi batches ke barabar count hota hai. Hamesha `loss.item() * batch.size(0)` accumulate karein.

Zero-GPU Tip:
Is Capstone architecture mein 25,000 parameters hain jo CPU par 5 epochs sirf 0.8 seconds mein train ho jate hain. Model architecture aur training loops ko hamesha CPU par chote data par pehle debug karein, phir cloud GPU par deploy karein.

Self-Check Questions:
1. Residual skip connection ($x + F(x)$) deep networks mein gradient flow ko kaise bachati hai?
2. Gradient clipping kyu zaroori hai aur yeh gradient vector ko kaise scale karti hai?
3. `model.state_dict()` aur poore model object ko save karne mein kya farq hai?

What to Build Next:
Is Capstone training pipeline ko extend karein taake yeh Early Stopping monitor kare (agar 3 epochs tak validation loss na ghate to training rok de) aur best validation checkpoint save kare."""
