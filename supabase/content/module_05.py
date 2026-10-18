# module_05.py
# Module 5: Attention & Transformers Under the Hood
# Lessons 5.1 to 5.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 5.1: Self-Attention Mechanism: Q, K, V Matrices Ka Khel
# ==============================================================================
LESSON_CONTENT['5.1'] = r"""### Part 1: Mental Model & South Asian Analogy
Modern AI ka sab se bara inqilab 2017 ke paper "Attention Is All You Need" se aaya. Lekin Self-Attention ka mathematical formula ($\text{Softmax}(\frac{Q K^T}{\sqrt{d_k}}) V$) dekh kar log ghabra jate hain.
Isay samajhne ke liye kisi Mashhoor Library ya Rishta Registry Bureau ki misaal lein:
1. The Three Matrices: Query ($Q$), Key ($K$), aur Value ($V$):
   - Query ($Q$ - "Mujhe kya chahiye?"): Farz karein aap library mein dakhil hote hain aur librarian se kehte hain: "Mujhe Biryani banane ki tareekh par kitab chahiye." Yeh aapki Query hai.
   - Key ($K$ - "Kitab ke cover par kya likha hai?"): Library ki tamam almariyon mein hazaron kitabein rakhi hain. Har kitab ke cover par uska label ya mozu (Key) likha hua hai: Maslan ek kitab par likha hai "Mughlai Recipes", doosri par "Quantum Physics", teesri par "Karachi Street Food".
   - Dot Product ($Q \cdot K^T$ - Relevance Matching): Librarian aapki Query ko har kitab ki Key ke sath match karta hai. "Mughlai Recipes" ka aapki query se 95% match nikalta hai, jabke "Quantum Physics" ka 0% match nikalta hai.
   - Value ($V$ - "Kitab ke andar ka asal mawaad"): Match hone ke baad librarian un kitabon ke andar ke safhay (Values) nikalta hai aur unke matching score ke mutabiq unka nichor (Weighted Average) bana kar aapke hawale kar deta hai!
2. Sentence Ke Andar Context Ka Taluq: Jumlay mein har lafz doosre lafz se sawal poochta hai. Maslan jumla hai: "Bank manager ne nadi ke bank par baith kar chai pee." Pehla "bank" (idara) janna chahta hai ke doosra "bank" (kinara) kaun hai. Self-Attention har token ko poore jumlay ke har doosre token ke sath match karke context-rich representation banati hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Scaled Dot-Product Attention ka exact hisab concrete choti values ke sath step-by-step karein.
Formula:
$\text{Attention}(Q, K, V) = \text{Softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V$

Toy Setup:
- Sequence Length $S = 2$ tokens (Token 1: "Chai", Token 2: "Garam")
- Head Dimension $d_k = 2$ ($\sqrt{d_k} = \sqrt{2} \approx 1.4142$)

Query Matrix $Q$ (Shape $[2, 2]$):
$Q = \begin{bmatrix} 1.0 & 0.0 \\ 0.0 & 2.0 \end{bmatrix}$

Key Matrix $K$ (Shape $[2, 2]$):
$K = \begin{bmatrix} 1.0 & 1.0 \\ 0.0 & 1.0 \end{bmatrix}$

Value Matrix $V$ (Shape $[2, 2]$):
$V = \begin{bmatrix} 10.0 & 0.0 \\ 0.0 & 20.0 \end{bmatrix}$

Step 1: Compute Raw Attention Scores ($Q K^T$)
$K^T = \begin{bmatrix} 1.0 & 0.0 \\ 1.0 & 1.0 \end{bmatrix}$
$Q K^T = \begin{bmatrix} (1 \times 1 + 0 \times 1) & (1 \times 0 + 0 \times 1) \\ (0 \times 1 + 2 \times 1) & (0 \times 0 + 2 \times 1) \end{bmatrix} = \begin{bmatrix} 1.0 & 0.0 \\ 2.0 & 2.0 \end{bmatrix}$

Step 2: Scale by $\sqrt{d_k} \approx 1.4142$
$S = \frac{Q K^T}{1.4142} = \begin{bmatrix} \frac{1.0}{1.4142} & \frac{0.0}{1.4142} \\ \frac{2.0}{1.4142} & \frac{2.0}{1.4142} \end{bmatrix} \approx \begin{bmatrix} 0.7071 & 0.0000 \\ 1.4142 & 1.4142 \end{bmatrix}$

Step 3: Apply Softmax Row-Wise
Row 0:
- $e^{0.7071} \approx 2.0281$, $e^{0.0} = 1.0000$. Sum $= 3.0281$.
- $A_{0,0} = \frac{2.0281}{3.0281} \approx 0.6698$ (67%)
- $A_{0,1} = \frac{1.0000}{3.0281} \approx 0.3302$ (33%)

Row 1:
- $e^{1.4142} \approx 4.1132$, $e^{1.4142} \approx 4.1132$. Sum $= 8.2264$.
- $A_{1,0} = 0.5000$ (50%)
- $A_{1,1} = 0.5000$ (50%)

Attention Weights Matrix $A \approx \begin{bmatrix} 0.6698 & 0.3302 \\ 0.5000 & 0.5000 \end{bmatrix}$

Step 4: Multiply Attention Weights with Values Matrix ($A V$)
Output Row 0:
$O_0 = 0.6698 \times [10.0, 0.0] + 0.3302 \times [0.0, 20.0] = [6.698, 6.604]$
Output Row 1:
$O_1 = 0.5000 \times [10.0, 0.0] + 0.5000 \times [0.0, 20.0] = [5.000, 10.000]$
Final Output Matrix: $\begin{bmatrix} 6.698 & 6.604 \\ 5.000 & 10.000 \end{bmatrix}$, Shape $[2, 2]$.
Har token ne doosre token se uske relevance score ke mutabiq value absorb kar li!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Scaled Dot-Product Attention class, causal autoregressive masking, aur attention weight distribution inspection ko PyTorch mein implement karte hain.

```python
import math
import torch
import torch.nn as nn

class ScaledDotProductAttention(nn.Module):
    \"\"\"Numerically stable scaled dot-product attention with causal mask support.\"\"\"
    def __init__(self, dropout_p: float = 0.0) -> None:
        super().__init__()
        self.dropout = nn.Dropout(dropout_p)

    def forward(
        self, 
        q: torch.Tensor, 
        k: torch.Tensor, 
        v: torch.Tensor, 
        mask: torch.Tensor | None = None
    ) -> tuple[torch.Tensor, torch.Tensor]:
        \"\"\"
        Shapes:
          q, k, v: [Batch, Heads, Seq_Len, Head_Dim]
          mask:    [Batch, 1, Seq_Len, Seq_Len] or broadcastable
        Returns:
          context: [Batch, Heads, Seq_Len, Head_Dim]
          weights: [Batch, Heads, Seq_Len, Seq_Len]
        \"\"\"
        d_k = q.size(-1)
        # 1. Matmul Q and K.T: [B, H, S, D] @ [B, H, D, S] -> [B, H, S, S]
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(d_k)

        # 2. Apply Causal / Padding Mask if provided
        if mask is not None:
            # Fill masked positions with large negative value (-1e9)
            scores = scores.masked_fill(mask == 0, -1e9)

        # 3. Softmax over last dimension (over all keys for each query)
        attn_weights = torch.softmax(scores, dim=-1)
        attn_weights = self.dropout(attn_weights)

        # 4. Context weighted aggregation: [B, H, S, S] @ [B, H, S, D] -> [B, H, S, D]
        context = torch.matmul(attn_weights, v)
        return context, attn_weights

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    B, H, S, D = 1, 1, 3, 4
    
    q = torch.randn(B, H, S, D)
    k = torch.randn(B, H, S, D)
    v = torch.randn(B, H, S, D)

    # Autoregressive Lower-Triangular Causal Mask (Cannot look at future tokens)
    causal_mask = torch.tril(torch.ones(S, S)).view(1, 1, S, S)
    print("Causal Mask Matrix (1 = allowed, 0 = masked):\\n", causal_mask[0, 0].int())

    attn_layer = ScaledDotProductAttention()
    context_out, weights = attn_layer(q, k, v, mask=causal_mask)

    print(f"\\nContext Output Tensor Shape: {list(context_out.shape)}")
    print(f"Attention Weights Shape:     {list(weights.shape)}")
    print("Computed Attention Weights for Token 0 (Can only see itself):", weights[0, 0, 0].tolist())
    print("Computed Attention Weights for Token 2 (Can see 0, 1, 2):   ", weights[0, 0, 2].tolist())
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Forgetting to Scale by $\sqrt{d_k}$: Agar dimension $d_k$ bara ho (jaise $d_k = 128$) aur scaling na ki jaye, to dot products bohot bare ho jate hain ($QK^T \approx 100$). Softmax ke andar exponentiate hone par tamam probability sirf ek token ko chali jati hai aur gradients bilkul zero (vanish) ho jate hain.
2. Inverted Causal Mask Logic: Masking karte waqt check karein ke aapka mask 1 par allow karta hai ya 0 par. Agar ghalti se allowed tokens par `-1e9` fill kar diya jaye to poora attention matrix zero ho jata hai.
3. Transposing Wrong Dimensions: `k.transpose(-2, -1)` ke bajaye `k.T` likhna batch aur head dimensions ko corrupt kar deta hai. Hamesha specific last two dimensions transpose karein.

Zero-GPU Tip:
Small sequence attention math CPU par microsecond level par run hoti hai. Standard CPU par 512 sequence length ka self-attention benchmark karein taake tensor shapes aur causal masking ka flow clear ho sake.

Self-Check Questions:
1. Self-Attention mein $\sqrt{d_k}$ se scaling kyun ki jati hai?
2. Causal Masking kya hoti hai aur Decoder models (jaise GPT) mein yeh kyun zaroori hoti hai?
3. Self-Attention ki computational complexity sequence length $N$ ke sath $O(N^2)$ kyun hoti hai?

What to Build Next:
Ek Self-Attention Visualizer script banayein jo ek sample Urdu sentence ke tokens ka pairwise attention heatmap print kare aur verify kare ke pronouns apne nouns ko kitna attention de rahe hain."""

# ==============================================================================
# LESSON 5.2: Multi-Head Attention & Transformer Blocks
# ==============================================================================
LESSON_CONTENT['5.2'] = r"""### Part 1: Mental Model & South Asian Analogy
Akela self-attention head sirf ek tarah ka talluq dekh sakta hai. Lekin insani zuban mein ek hi lafz ke kayi mukhtalif pehloo hote hain: grammar ka talluq, maani ka talluq, zamana (past/present), aur jazbaat. Yahan kaam aata hai **Multi-Head Attention (MHA)**!
Isay samajhne ke liye kisi Cricket Match ke 8 Cameras aur Commentary Panel ki misaal lein:
1. Single Head vs Multi-Head (Ek Camera vs 8 Specialized Angles):
   - Camera 1 (Head 1): Batsman ke footwork par zoom karta hai (Syntactic relationship / Grammar).
   - Camera 2 (Head 2): Bowler ki seam aur wrist position dekhta hai (Temporal / Next action).
   - Camera 3 (Head 3): Slip fielder aur wicketkeeper ki position dekhta hai (Long-range entity tracking).
   - Camera 4 (Head 4): Crowd aur stadium ka jazbaat monitor karta hai (Sentiment).
   Agar sirf ek camera ho to woh ek waqt mein sirf ek cheez dekh sakta hai. 8 heads ek hi waqt mein jumlay ke 8 mukhtalif dimensions ko parallel capture karte hain!
2. Projection Back to Reality ($W_O$): Match ke baad tamam 8 cameras ki feed production control room mein aati hai jahan director (Output Projection Matrix $W_O$) un tamam angles ko mix karke ek mukammal telecast banata hai.
3. The Full Transformer Block (The Engine Room):
   Har Transformer Block mein 3 ahem aaza hote hain:
   - Multi-Head Attention (Tokens ka aapas mein tabadla-e-khayal).
   - Add & Norm (Residual Skip Connection + Layer Normalization taake gradients smoothly flow karein).
   - Feed-Forward Network (FFN - Har token ka infiradi dimagh jo attention se mile ilm ko process karta hai).

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Multi-Head Attention ki Tensor Splitting aur Concatenation ka exact mathematical hisab lagayein.
Architecture Dimensions:
- Model Dimension $D_{\text{model}} = 8$
- Number of Heads $H = 2$
- Head Dimension $d_k = \frac{D_{\text{model}}}{H} = \frac{8}{2} = 4$
- Sequence Length $S = 3$ tokens

Step 1: Linear Projection ($Q, K, V$)
Input Tensor $X$ ka shape $[S, D_{\text{model}}] = [3, 8]$.
$Q = X W_Q$, $K = X W_K$, $V = X W_V$ (Har projection matrix $[8, 8]$).
Output $Q, K, V$ sab ka shape $[3, 8]$ hota hai.

Step 2: Reshape and Split into Heads
Har tensor ko reshape kiya jata hai:
$[S, D_{\text{model}}] \to [S, H, d_k] \to [H, S, d_k]$
- Head 0 Query: $Q_0$ Shape $[3, 4]$
- Head 1 Query: $Q_1$ Shape $[3, 4]$
K aur V bhi isi tarah split hote hain.
Dono heads par parallel Scaled Dot-Product Attention execute hoti hai:
- $\text{Head}_0 = \text{Attention}(Q_0, K_0, V_0)$ Shape $[3, 4]$
- $\text{Head}_1 = \text{Attention}(Q_1, K_1, V_1)$ Shape $[3, 4]$

Step 3: Concatenation
Dono heads ke outputs ko aapas mein jod diya jata hai:
$\text{MultiHeadOutput} = [\text{Head}_0, \text{Head}_1] \text{ along last dimension}$
Resulting Shape: $[3, 4 + 4] = [3, 8]$.

Step 4: Output Projection ($W_O$)
$\text{Final} = \text{MultiHeadOutput} \times W_O$
Matrix Multiplication: $[3, 8] \times [8, 8] \to [3, 8]$.
Output ka shape bilkul wahi $[3, 8]$ rehta hai jo shuru mein input $X$ ka tha! Yahi wajah hai ke aap hazaron transformer blocks ko ek ke upar ek stack kar sakte hain.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete Multi-Head Attention module from scratch implement karte hain without using `nn.MultiheadAttention`.

```python
import math
import torch
import torch.nn as nn

class CustomMultiHeadAttention(nn.Module):
    \"\"\"Production Multi-Head Attention with single-matrix projection optimization.\"\"\"
    def __init__(self, d_model: int, n_heads: int, dropout_p: float = 0.1) -> None:
        super().__init__()
        assert d_model % n_heads == 0, f"d_model ({d_model}) must be divisible by n_heads ({n_heads})"
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads

        # Optimized fused QKV projection: projects to 3 * d_model in a single matmul
        self.qkv_proj = nn.Linear(d_model, 3 * d_model, bias=False)
        self.out_proj = nn.Linear(d_model, d_model, bias=False)
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        # Input shape x: [Batch, Seq_Len, d_model]
        B, S, D = x.shape

        # 1. Project to Q, K, V simultaneously: [B, S, 3 * D]
        qkv = self.qkv_proj(x)
        # Reshape to [B, S, 3, H, d_k] and permute to separate Q, K, V
        qkv = qkv.reshape(B, S, 3, self.n_heads, self.d_k).permute(2, 0, 3, 1, 4)
        q, k, v = qkv[0], qkv[1], qkv[2]  # Each has shape: [B, H, S, d_k]

        # 2. Scaled Dot-Product Attention per head
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)  # [B, H, S, S]
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)

        attn_weights = torch.softmax(scores, dim=-1)
        attn_weights = self.dropout(attn_weights)
        
        # 3. Weighted aggregation: [B, H, S, S] @ [B, H, S, d_k] -> [B, H, S, d_k]
        context = torch.matmul(attn_weights, v)

        # 4. Transpose and concatenate heads back: [B, H, S, d_k] -> [B, S, H, d_k] -> [B, S, D]
        context = context.permute(0, 2, 1, 3).contiguous().reshape(B, S, D)

        # 5. Final linear projection back to residual stream
        return self.out_proj(context)

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    B, S, D, H = 2, 4, 16, 4
    x_tokens = torch.randn(B, S, D)

    # Causal triangular mask
    causal_mask = torch.tril(torch.ones(S, S)).view(1, 1, S, S)
    mha = CustomMultiHeadAttention(d_model=D, n_heads=H)
    out = mha(x_tokens, mask=causal_mask)

    print(f"Input Shape:  {list(x_tokens.shape)}")
    print(f"Output Shape: {list(out.shape)} (Preserved dimensional shape!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Missing `.contiguous()` Before `.reshape()`: Permute karne ke baad memory layout non-contiguous ho jata hai. Agar aap direct `.view()` ya `.reshape()` chalayenge to PyTorch `RuntimeError: view size is not compatible with input tensor's size and stride` throw kar deta hai. Hamesha `.contiguous().reshape()` karein.
2. Using Separate Linear Layers for Q, K, and V: Teen alag alag linear layers (`nn.Linear(d, d)`) chalane se 3 alag CUDA kernel launches hote hain. Fused `nn.Linear(d, 3*d)` use karna 3x GPU kernel overhead bachata hai.
3. Placing LayerNorm After Attention (Post-LN Instability): Original 2017 transformer mein Post-LN use hua tha jo deep networks mein train nahi hota tha. Modern standard **Pre-LN** hai: `x = x + attn(norm(x))`.

Zero-GPU Tip:
Multi-Head Attention tensor slicing aur permutations CPU par testing ke liye behtareen hain. Fused linear layers CPU ke cache footprint ko optimized rakhti hain aur bina kisi GPU ke chalti hain.

Self-Check Questions:
1. Multi-Head Attention single head attention ke muqablay model ko kya faida deti hai?
2. Fused QKV projection three separate linear layers ke muqablay memory aur latency mein kyun behtar hai?
3. Transformer block mein Pre-LayerNorm aur Post-LayerNorm mein architectural farq kya hai?

What to Build Next:
Ek Complete Transformer Decoder Block class banayein jisme Pre-LayerNorm, CustomMultiHeadAttention, SwiGLU Feed-Forward Network, aur Residual Connections shamil hon."""

# ==============================================================================
# LESSON 5.3: Tokenization Deep Dive: Byte-Pair Encoding (BPE) & Tiktoken
# ==============================================================================
LESSON_CONTENT['5.3'] = r"""### Part 1: Mental Model & South Asian Analogy
Aksar log sochte hain ke LLMs angrezi ya urdu alfaz samajhte hain. Lekin dar-haqeeqat model ke dakhilay par ek darbaan baitha hota hai jise **Tokenizer** kehte hain. Tokenizer text ko numbers mein torta hai.
Isay samajhne ke liye kisi Shehar ke Press aur Newspaper Printing Press (Typewriter Blocks) ki misaal lein:
1. Character-Level Tokenization (Har Harf Ka Alag Thappa): Agar typewriter mein sirf 26 haroof hon to har lafz (jaise "BIRYANI") likhne ke liye 7 alag alag thappay lagane parenge. Jumlay bohot lambay ho jayenge aur context window foran bhar jayegi ($O(N)$ length explosion).
2. Word-Level Tokenization (Har Lafz Ka Alag Block): Agar har lafz ka naya thappa banayein to dictionary mein 10 lakh thappay rakhne parenge (Massive Vocabulary Size). Agar koi naya lafz aa jaye (jaise "DeepSeek"), to typewriter crash ho jayega (Out-of-Vocabulary / UNK Error).
3. Byte-Pair Encoding (BPE - Samajhdaar Darzi): BPE dunya ka sab se aqalmand tareeqa hai. Yeh shuru raw bytes se karta hai (koi naya lafz UNK nahi ho sakta!). Phir text mein dekhta hai: "Kaun se do haroof sab se zyada aik sath aate hain?"
   - Misaal: "c" aur "h" hamesha sath aate hain? Inhe jod kar "ch" bana do!
   - "ch" aur "ai" sath aate hain? Inhe jod kar "chai" ka single token bana do!
   Jo alfaz rozana aate hain woh single token ban jate hain, aur naye anokhay alfaz chotay tukron mein toot kar handle ho jate hain.
4. Tiktoken (OpenAI Ka High-Speed Rust Engine): Tiktoken OpenAI ka open-source BPE tokenizer hai jo Rust mein likha gaya hai. Yeh Python ke standard tokenizers se 50x tez chalta hai aur gpt-4o, llama-3, aur deepseek ke tokens handle karta hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Byte-Pair Encoding (BPE) algorithm ka ek complete merge step hath se trace karte hain.
Raw Corpus:
Text: `"chai chai garam chai"`
Target Vocabulary merges: Find most frequent adjacent byte pair and merge them!

Initial State (Character tokens):
Tokens sequence:
`['c', 'h', 'a', 'i', ' ', 'c', 'h', 'a', 'i', ' ', 'g', 'a', 'r', 'a', 'm', ' ', 'c', 'h', 'a', 'i']`

Step 1: Count Adjacent Bigram Frequencies across corpus
- Pair `('c', 'h')`: Appears 3 times
- Pair `('h', 'a')`: Appears 3 times
- Pair `('a', 'i')`: Appears 3 times
- Pair `('i', ' ')`: Appears 3 times
- Pair `(' ', 'c')`: Appears 2 times
- Pair `('g', 'a')`: Appears 1 time

Step 2: Select Most Frequent Pair to Merge
Highest frequency pair is `('c', 'h')` (Frequency = 3).
Rule 1 added to vocabulary: `('c', 'h') -> 'ch'`

Updated Corpus after Merge 1:
`['ch', 'a', 'i', ' ', 'ch', 'a', 'i', ' ', 'g', 'a', 'r', 'a', 'm', ' ', 'ch', 'a', 'i']`

Step 3: Count Bigram Frequencies on Updated Corpus
- Pair `('ch', 'a')`: Appears 3 times! (Winner)
Rule 2 added to vocabulary: `('ch', 'a') -> 'cha'`

Updated Corpus after Merge 2:
`['cha', 'i', ' ', 'cha', 'i', ' ', 'g', 'a', 'r', 'a', 'm', ' ', 'cha', 'i']`

Step 4: Merge 3
Pair `('cha', 'i')` appears 3 times!
Rule 3 added: `('cha', 'i') -> 'chai'`

Final Tokens after 3 merges:
`['chai', ' ', 'chai', ' ', 'g', 'a', 'r', 'a', 'm', ' ', 'chai']`
Dekhein! 20 characters ka lamba corpus sirf 7 tokens mein condense ho gaya! Yahi BPE compression engine hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Byte-Pair Encoding (BPE) training algorithm from first principles implement karte hain aur adjacent pair frequencies count karke vocabulary build karte hain.

```python
from collections import Counter
from typing import List, Tuple, Dict

def get_stats(token_list: List[str]) -> Counter:
    \"\"\"Counts frequency of all adjacent bigram pairs in token sequence.\"\"\"
    pairs = Counter()
    for i in range(len(token_list) - 1):
        pairs[(token_list[i], token_list[i + 1])] += 1
    return pairs

def merge_tokens(token_list: List[str], pair_to_merge: Tuple[str, str], replacement: str) -> List[str]:
    \"\"\"Replaces all consecutive occurrences of pair_to_merge with replacement token.\"\"\"
    new_tokens: List[str] = []
    i = 0
    while i < len(token_list):
        if i < len(token_list) - 1 and (token_list[i], token_list[i + 1]) == pair_to_merge:
            new_tokens.append(replacement)
            i += 2  # Skip merged pair
        else:
            new_tokens.append(token_list[i])
            i += 1
    return new_tokens

def train_toy_bpe(corpus: str, num_merges: int = 5) -> Tuple[List[str], List[Tuple[Tuple[str, str], str]]]:
    # Start at character level
    tokens = list(corpus)
    merge_rules: List[Tuple[Tuple[str, str], str]] = []

    print(f"Initial Characters Count: {len(tokens)}")
    for iteration in range(1, num_merges + 1):
        stats = get_stats(tokens)
        if not stats:
            break
        # Pick most common pair
        best_pair, freq = stats.most_common(1)[0]
        if freq < 2:
            break  # No repeated pairs left
        new_token = "".join(best_pair)
        tokens = merge_tokens(tokens, best_pair, new_token)
        merge_rules.append((best_pair, new_token))
        print(f"Merge {iteration:02d}: {best_pair} -> '{new_token}' (occurred {freq} times)")

    return tokens, merge_rules

# Execution test
if __name__ == "__main__":
    sample_text = "karak chai aur lachha paratha karak chai aur meethi lassi"
    final_tokens, rules = train_toy_bpe(sample_text, num_merges=6)

    print(f"\\nOriginal Text Length: {len(sample_text)} characters")
    print(f"Tokenized Sequence Length: {len(final_tokens)} tokens")
    print("Final Token Sequence:", final_tokens)
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Assuming 1 Word Equals 1 Token in Multilingual Text: English mein 1 word $\approx$ 1.3 tokens hota hai, jabke Urdu ya Roman Urdu mein BPE vocabulary mein poore words na hone ki wajah se 1 word $\approx$ 3 se 4 tokens ban sakta hai. Prompt cost calculate karte waqt hamesha actual tokenizer count check karein.
2. Tokenizer Mismatch Between Training and Inference: Model ko LLaMA tokenizer par train karke inference GPT-4 tokenizer se karna poore outputs ko garbage characters bana deta hai. Hamesha exact matching tokenizer artifact use karein.
3. Whitespace Stripping Before Tokenization: Tokenization se pehle agar aap `.strip()` karke leading spaces ura dete hain to model indentation (jaise Python code mein spaces) kho deta hai. Spaces BPE tokens ka lazmi hissa hoti hain (jaise Tiktoken ka `Ġ` symbol).

Zero-GPU Tip:
Tokenization pure string aur regex matching par mushtamil hoti hai jo 100% CPU par chalti hai. `tiktoken` library Rust multi-threading use karti hai aur 10 lakh tokens ko CPU par 0.5 second mein tokenize kar deti hai.

Self-Check Questions:
1. Byte-Pair Encoding (BPE) Word-level aur Character-level tokenization ke muqablay mein kya balance faraham karta hai?
2. BPE algorithm mein vocabulary kaise grow karti hai?
3. Roman Urdu aur English mein token compression ratio mukhtalif kyun hota hai?

What to Build Next:
Ek Roman Urdu vs English Tokenization Benchmarker banayein jo `tiktoken` (cl100k_base) use karke dono zabanon ke 100 jumlon ka token-to-word ratio calculate kare aur cost disparity report kare."""

# ==============================================================================
# LESSON 5.4: Rotary Position Embeddings (RoPE) & Context Length Scaling
# ==============================================================================
LESSON_CONTENT['5.4'] = r"""### Part 1: Mental Model & South Asian Analogy
Transformers fundamentally Position-Agnostic hote hain: yani agar aap jumlay ke alfaz ko aage peeche ulat pulat kar dein ("Kutta billi ko bhagaya" vs "Billi kutte ko bhagaya"), to Self-Attention mechanism bina kisi position indicator ke dono mein koi farq nahi kar sakta.
Isay samajhne ke liye kisi Ghari (Clock Face) aur Ghanti Bajane wale Chowkidar ki misaal lein:
1. Absolute Positional Embeddings (Purana Tareeqa): Original Transformer har position par ek rigid number tag chipkata tha (Position 0, Position 1, Position 2). Yeh aisa tha jese imtihan hall mein har desk par fixed number laga ho. Masla yeh tha ke agar train karte waqt sirf 2048 desks the, to 2049th bande ke aate hi model andha ho jata tha kyunke uske paas 2049 ka koi embedding tag nahi tha!
2. Rotary Position Embeddings (RoPE - 2026 SOTA Standard): RoPE ek inqilabi idea hai jo LLaMA-3, DeepSeek-R1, aur Mistral models use karte hain. RoPE position ko add nahi karta, balki vector ko 2D complex plane mein ek makhsoos angle $\theta$ se Ghooma (Rotate) deta hai!
   - Token 0: Ghari ki sui $0^\circ$ par hai.
   - Token 1: Ghari ki sui $30^\circ$ ghoom jati hai.
   - Token 2: Ghari ki sui $60^\circ$ ghoom jati hai.
3. Relative Distance via Dot Product ($m - n$): Jab Token 5 Token 2 ki taraf dekhta hai, to dono ke darmiyan angle ka farq $5 - 2 = 3$ steps hota hai. Dot product karte waqt absolute position gayab ho jati hai aur sirf dono ke darmiyan relative faasla ($m - n$) baqi rehta hai!
4. Context Length Scaling (YaRN & RoPE Interpolation): Agar model ko 4k context se 128k context tak expand karna ho, to hum ghari ki suiyon ki raftaar ko dheema (frequency scale / interpolate) kar dete hain taake wohi purane angles 32 guna lambay context par phail sakein!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein 2D Vector par Rotary Position Embedding (RoPE) ka complex rotation math trace karte hain.
Formula for 2D RoPE Rotation at Position $m$:
$\begin{pmatrix} q_0^{(m)} \\ q_1^{(m)} \end{pmatrix} = \begin{pmatrix} \cos(m\theta) & -\sin(m\theta) \\ \sin(m\theta) & \cos(m\theta) \end{pmatrix} \begin{pmatrix} q_0 \\ q_1 \end{pmatrix}$
Jahan:
- $m$: Token position index (0, 1, 2...)
- $\theta$: Base rotation angle (Frequency $\theta = 10000^{-2i/d}$)

Worked Numeric Example:
Single 2D Query vector: $q = [1.0, 0.0]$
Base angle $\theta = \frac{\pi}{2} = 90^\circ$ ($\cos(90^\circ) = 0.0, \sin(90^\circ) = 1.0$)

Case 1: Token at Position $m = 0$
Angle: $0 \times 90^\circ = 0^\circ$ ($\cos(0^\circ) = 1.0, \sin(0^\circ) = 0.0$)
$q^{(0)} = \begin{pmatrix} 1.0 & -0.0 \\ 0.0 & 1.0 \end{pmatrix} \begin{pmatrix} 1.0 \\ 0.0 \end{pmatrix} = \begin{pmatrix} 1.0 \\ 0.0 \end{pmatrix}$ (No rotation)

Case 2: Token at Position $m = 1$
Angle: $1 \times 90^\circ = 90^\circ$
$q^{(1)} = \begin{pmatrix} 0.0 & -1.0 \\ 1.0 & 0.0 \end{pmatrix} \begin{pmatrix} 1.0 \\ 0.0 \end{pmatrix} = \begin{pmatrix} (0 \times 1 - 1 \times 0) \\ (1 \times 1 + 0 \times 0) \end{pmatrix} = \begin{pmatrix} 0.0 \\ 1.0 \end{pmatrix}$ (Vector rotated by $90^\circ$!)

Case 3: Dot Product Between Position 1 and Position 0
$\langle q^{(1)}, k^{(0)} \rangle$:
Farz karein $k = [1.0, 0.0]$ at position $n = 0 \implies k^{(0)} = [1.0, 0.0]$.
Dot product $= (0.0 \times 1.0) + (1.0 \times 0.0) = 0.0$.
Notice: $\cos((1 - 0) \times 90^\circ) = \cos(90^\circ) = 0.0$!
Dot product direct relative angle difference $(m - n)\theta$ ka function ban gaya!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum pre-computed RoPE frequencies tensor, complex rotation application, aur context length scaling logic ko PyTorch mein implement karte hain.

```python
import torch
import torch.nn as nn

def precompute_rope_frequencies(dim: int, max_seq_len: int, theta_base: float = 10000.0) -> tuple[torch.Tensor, torch.Tensor]:
    \"\"\"Precomputes cosine and sine frequency tensors for Rotary Position Embeddings.\"\"\"
    assert dim % 2 == 0, "Dimension must be even for 2D pair rotation"
    
    # Frequency bands: theta_i = 1 / (theta_base ^ (2i / dim))
    i = torch.arange(0, dim, 2).float()
    frequencies = 1.0 / (theta_base ** (i / dim))  # Shape: [dim // 2]
    
    # Position indices: [0, 1, ..., max_seq_len - 1]
    positions = torch.arange(max_seq_len).float()  # Shape: [max_seq_len]
    
    # Outer product: [max_seq_len, dim // 2]
    angles = torch.outer(positions, frequencies)
    
    # Compute Cosine and Sine components
    cos = torch.cos(angles)  # Shape: [max_seq_len, dim // 2]
    sin = torch.sin(angles)  # Shape: [max_seq_len, dim // 2]
    
    return cos, sin

def apply_rope_rotation(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor) -> torch.Tensor:
    \"\"\"Applies RoPE rotation to query or key tensor across 2D split pairs.\"\"\"
    # Input shape x: [Batch, Heads, Seq_Len, Dim]
    B, H, S, D = x.shape
    
    # Reshape last dim into pairs: [B, H, S, D // 2, 2]
    x_pairs = x.reshape(B, H, S, D // 2, 2)
    x0 = x_pairs[..., 0]  # [B, H, S, D // 2]
    x1 = x_pairs[..., 1]  # [B, H, S, D // 2]
    
    # Broadcast cos and sin: [1, 1, S, D // 2]
    cos_b = cos[:S, :].view(1, 1, S, D // 2)
    sin_b = sin[:S, :].view(1, 1, S, D // 2)
    
    # 2D Complex rotation: [x0*cos - x1*sin, x0*sin + x1*cos]
    rotated_x0 = x0 * cos_b - x1 * sin_b
    rotated_x1 = x0 * sin_b + x1 * cos_b
    
    # Stack and flatten back to original tensor dimension [B, H, S, D]
    rotated_pairs = torch.stack([rotated_x0, rotated_x1], dim=-1)
    return rotated_pairs.reshape(B, H, S, D)

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    B, H, S, D = 1, 1, 4, 8  # 4 tokens, head dimension 8
    q = torch.randn(B, H, S, D)

    cos, sin = precompute_rope_frequencies(dim=D, max_seq_len=128)
    q_rotated = apply_rope_rotation(q, cos, sin)

    print(f"Original Q Shape: {list(q.shape)}")
    print(f"Rotated Q Shape:  {list(q_rotated.shape)}")
    print(f"Vector Norm Preserved: {torch.norm(q[0, 0, 0]).item():.4f} == {torch.norm(q_rotated[0, 0, 0]).item():.4f}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Applying RoPE to the Values Matrix ($V$): RoPE sirf Query ($Q$) aur Key ($K$) par lagaya jata hai kyunke iska maqsad attention weights ke dot product ko relative position se scale karna hai. Value matrix par RoPE lagane se output representations corrupt ho jati hain.
2. Hardcoding Fixed Context Max Length: Frequencies pre-compute karte waqt agar aap buffer ko fixed 2048 set kar dein aur evaluation par 4096 tokens aa jayein to index out of bounds error aata hai. Hamesha dynamic slice generation use karein.
3. Forgetting Float32 Precision for Trigonometric Functions: FP16 mein $\sin$ aur $\cos$ frequencies compute karne se precision truncation ho jata hai jisse long sequences par rotation drift ho jati hai. Frequencies hamesha Float32 mein compute karein.

Zero-GPU Tip:
RoPE trigonometric calculations CPU par pre-compute hokar cache ho jati hain. Inference ke waqt element-wise multiply CPU ke AVX registers mein zero latency overhead ke sath execute hota hai.

Self-Check Questions:
1. Absolute Positional Embeddings ke muqablay RoPE relative distance ko kaise capture karta hai?
2. RoPE vector ki magnitude (L2 Norm) ko change kyun nahi karta? (Answer: Complex plane mein pure rotation length preserve karti hai).
3. Context length 4k se 128k scale karte waqt YaRN ya RoPE frequency scaling kya karti hai?

What to Build Next:
Ek RoPE Attention Distance Test script banayein jo do identical tokens ke darmiyan attention weight calculate kare jab unka darmiyani faasla 1 step ho vs 100 steps ho, aur relative decay verify kare."""

# ==============================================================================
# LESSON 5.5: Architectural Paradigms: BERT vs GPT vs T5
# ==============================================================================
LESSON_CONTENT['5.5'] = r"""### Part 1: Mental Model & South Asian Analogy
Transformers ki dunya mein teen mukhtalif khandani qabeelay hain: **Encoder-Only** (BERT), **Decoder-Only** (GPT), aur **Encoder-Decoder** (T5). Har qabeelay ka apna mizaaj aur maqsad hai.
Isay samajhne ke liye kisi Adalat (Courtroom) ke Teen Kirdaron ki misaal lein:
1. Encoder-Only / BERT (The CID Inspector): Inspector ka kaam kisi jurm ki tehqeeq karna hai. Woh poori file ko ek sath parhta hai: aage se peeche, peeche se aage (Bidirectional Attention). Inspector koi nayi kahani nahi likhta; woh sirf classification karta hai: "Mulzim mujrim hai ya be-gunaah?" BERT classification, sentiment analysis, aur search embeddings ke liye shahenshah hai.
2. Decoder-Only / GPT (The Dastango / Novelist): Novelist ka kaam agla lafz likhna hai. Woh mustaqbil nahi dekh sakta; woh sirf maazi (pichle tokens) dekh sakta hai (Causal Masked Attention). Agar use agla safha pehle hi dikha diya jaye to kahani ka suspense khatam ho jayega. GPT autoregressive text generation, reasoning, coding, aur conversational chatbots ka badshah hai.
3. Encoder-Decoder / T5 (The Diplomatic Translator): Translator pehle ghair-mulki safir ki poori guftagu aaram se sunta hai (Bidirectional Encoder), aur phir doosre shaks ko apni zaban mein tarjuma karke sunata hai (Autoregressive Decoder with Cross-Attention). T5 translation aur formal document summarization ke liye behtareen hai.
2026 mein generative AI aur LLMs ka 95% hissa **Decoder-Only** (LLaMA-3, DeepSeek, GPT-4) par shift ho chuka hai kyunke KV Cache scaling aur autoregressive pre-training decoder-only architectures par sab se zyada efficient hoti hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Attention Masking Matrices ke geometric structure ka hisab dekhein jo teeno architectures ko alag karta hai.
Sequence Length $S = 3$ tokens (`["Chai", "Garam", "Hai"]`).

1. Encoder-Only (BERT) Full Bidirectional Attention Matrix:
Har token poore jumlay ke har doosre token ko dekh sakta hai.
$M_{\text{BERT}} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$
Attention Mask: Zero masking! All pairwise dot products computed.

2. Decoder-Only (GPT) Causal Autoregressive Lower-Triangular Mask:
Future tokens par $-\infty$ mask lagaya jata hai taake model cheat na kar sake:
$M_{\text{GPT}} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix} \implies \text{Softmax Input} = \begin{bmatrix} S_{0,0} & -\infty & -\infty \\ S_{1,0} & S_{1,1} & -\infty \\ S_{2,0} & S_{2,1} & S_{2,2} \end{bmatrix}$
Row 0: Token "Chai" can ONLY see "Chai".
Row 1: Token "Garam" can see "Chai" and "Garam".
Row 2: Token "Hai" can see "Chai", "Garam", and "Hai".

3. Encoder-Decoder Cross-Attention (T5):
Queries Decoder se aati hain ($S_{\text{dec}} = 2$), Keys aur Values Encoder se aate hain ($S_{\text{enc}} = 3$):
$M_{\text{Cross}} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$, Shape: $[S_{\text{dec}}, S_{\text{enc}}] = [2, 3]$.
Decoder ka har step poore input document ke encoder representations par cross-attention karta hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Bidirectional vs Causal mask generators, Cross-Attention module, aur architectural paradigm comparison ko PyTorch mein implement karte hain.

```python
import torch
import torch.nn as nn
import math

class CrossAttentionBlock(nn.Module):
    \"\"\"Cross-Attention layer used in Encoder-Decoder architectures (T5 / Whisper).\"\"\"
    def __init__(self, d_model: int, n_heads: int) -> None:
        super().__init__()
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads

        # Queries from decoder state, Keys/Values from encoder output
        self.q_proj = nn.Linear(d_model, d_model, bias=False)
        self.k_proj = nn.Linear(d_model, d_model, bias=False)
        self.v_proj = nn.Linear(d_model, d_model, bias=False)
        self.out_proj = nn.Linear(d_model, d_model, bias=False)

    def forward(self, decoder_hidden: torch.Tensor, encoder_memory: torch.Tensor) -> torch.Tensor:
        # decoder_hidden: [B, S_dec, D]
        # encoder_memory: [B, S_enc, D]
        B, S_dec, D = decoder_hidden.shape
        S_enc = encoder_memory.size(1)

        q = self.q_proj(decoder_hidden).view(B, S_dec, self.n_heads, self.d_k).transpose(1, 2)
        k = self.k_proj(encoder_memory).view(B, S_enc, self.n_heads, self.d_k).transpose(1, 2)
        v = self.v_proj(encoder_memory).view(B, S_enc, self.n_heads, self.d_k).transpose(1, 2)

        # Matmul: [B, H, S_dec, d_k] @ [B, H, d_k, S_enc] -> [B, H, S_dec, S_enc]
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)
        attn = torch.softmax(scores, dim=-1)

        # Context: [B, H, S_dec, S_enc] @ [B, H, S_enc, d_k] -> [B, H, S_dec, d_k]
        context = torch.matmul(attn, v).transpose(1, 2).contiguous().view(B, S_dec, D)
        return self.out_proj(context)

# Execution test
if __name__ == "__main__":
    B, D, H = 1, 16, 2
    S_encoder = 5  # Source text tokens: "Karachi ka mausam bohot garam"
    S_decoder = 3  # Target text tokens: "Hot Karachi weather"

    enc_mem = torch.randn(B, S_encoder, D)
    dec_state = torch.randn(B, S_decoder, D)

    cross_attn = CrossAttentionBlock(d_model=D, n_heads=H)
    output = cross_attn(dec_state, enc_mem)

    print(f"Encoder Memory Shape: {list(enc_mem.shape)}")
    print(f"Decoder State Shape:  {list(dec_state.shape)}")
    print(f"Cross-Attention Output Shape: {list(output.shape)} (Matches decoder sequence length!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Using Decoder-Only Models for Dense Sentence Similarity: Decoder-only models causal masking ki wajah se aakhri token par pichle tokens ka bias rakhte hain. Pure sentence embeddings ke liye BERT-style bidirectional models ya specialized embedding architectures (BGE, ModernBERT) behtar perform karte hain.
2. Training BERT for Text Generation: BERT masked language modeling ($MLM$) par train hota hai jahan beech beech ke words mask hote hain. BERT autoregressive generation nahi kar sakta kyunke isme causal masking nahi hoti.
3. Forgetting Cross-Attention KV Cache in T5: Encoder-Decoder models mein encoder ki memory ek hi dafa encode hoti hai, jabke decoder generation ke waqt cross-attention keys aur values constant rehti hain. Unhe har step par dobara compute karna compute waste hai.

Zero-GPU Tip:
Architectural masking logic aur cross-attention simulations CPU par microsecond speed se chalti hain. Dono masks ke boolean tensors ko print karke visually inspect karein taake attention leakage ka concept crystal clear ho sake.

Self-Check Questions:
1. BERT, GPT, aur T5 ke attention mask matrices mein kya farq hota hai?
2. 2026 mein modern LLMs Encoder-Decoder ke bajaye Decoder-Only architectures par kyun converge hue hain?
3. Cross-Attention mein Queries kahan se aati hain aur Keys/Values kahan se aate hain?

What to Build Next:
Ek Unified Mask Generator function likhein jo flag ke mutabiq (`'bidirectional'`, `'causal'`, ya `'prefix_lm'`) appropriate attention mask matrix generate kare aur visual ASCII diagram print kare."""

# ==============================================================================
# LESSON 5.6: Module 5 Capstone: Build a Mini-GPT from Scratch in PyTorch
# ==============================================================================
LESSON_CONTENT['5.6'] = r"""### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne Transformer architecture ke tamam bunyadi aur advance mathematical aaza (QKV attention, Multi-Head projection, BPE tokenization, RoPE positional encoding, aur Causal masking) seekh liye hain. Ab waqt hai aapke **Sab Se Baray AI Engineering Milestone** ka: **Apna Khila-e-Awwal Mini-GPT Model Scratch Se PyTorch Mein Likhna**!
Is Capstone project ka zehni khaka kisi Automobile Factory ke Assembly Line jaisa hai:
1. The Raw Steel (Token & Position Embeddings): Input text ke token IDs aate hain. Embedding table unhe dense vectors banati hai aur RoPE ya Positional vectors unme position ka rang bharte hain.
2. The Stacked Engine Blocks (Transformer Decoder Stack): Data ek ke baad doosre Transformer Block se guzarta hai (Block 1 $\to$ Block 2 $\to$ Block 3). Har block ke andar:
   - Causal Multi-Head Self-Attention pichle tokens ka context extract karti hai.
   - Residual Connection input signal ko mehfooz rakhti hai.
   - MLP / Feed-Forward Network us context ko transform karti hai.
3. The Final Exhaust & Dashboard (Final LayerNorm & Language Model Head): Sab se aakhir mein LayerNorm signal ko normalize karti hai aur Linear LM Head unhe vocabulary size ke logits mein project kar deta hai.
4. The Generative Fuel Loop: Model aakhri token par agla token predict karta hai, use apne input mein shamil karta hai, aur loop chala kar poori kahani khud ba khud likhta chala jata hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Mini-GPT ke Total Parameter Memory Budget aur Forward Pass Shapes ko mathematically calculate karein.
Architecture Hyperparameters:
- Vocabulary Size $V = 1000$ tokens
- Sequence Length $S = 64$ tokens
- Embedding Dimension $D = 128$
- Number of Layers $L = 2$
- Number of Heads $H = 4$ ($d_k = 32$)
- Feed-Forward Hidden Dimension $D_{\text{ff}} = 4 \times D = 512$

Step 1: Calculate Parameter Breakdown
1. Token Embeddings: $V \times D = 1000 \times 128 = 128,000$ params
2. Position Embeddings: $S \times D = 64 \times 128 = 8,192$ params
3. Per Transformer Block ($L = 2$):
   - MHA QKV Projection: $D \times (3 \times D) = 128 \times 384 = 49,152$
   - MHA Out Projection: $D \times D = 128 \times 128 = 16,384$
   - LayerNorms (2 per block): $2 \times (2 \times D) = 512$
   - FFN Linear 1: $D \times D_{\text{ff}} = 128 \times 512 = 65,536$
   - FFN Linear 2: $D_{\text{ff}} \times D = 512 \times 128 = 65,536$
   - Total per block $\approx 197,120$ params.
   - For 2 blocks $= 2 \times 197,120 = 394,240$ params.
4. Final LM Head: $D \times V = 128 \times 1000 = 128,000$ params (Tied weights with embeddings save this!).
Total Model Parameters $\approx 658,432 \text{ params} \approx 0.65 \text{ Million Parameters}$.

Step 2: Tensor Shape Transitions During Forward Pass
- Input Token IDs: Shape `[Batch=2, Seq_Len=8]`
- After Embedding: Shape `[2, 8, 128]`
- After Transformer Blocks: Shape `[2, 8, 128]`
- After LM Head Projection: Shape `[2, 8, 1000]` (Logits over full vocabulary for every sequence position!)
- Cross-Entropy Loss: Computed between Logits `[2*8, 1000]` and Targets `[2*8]`.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete Mini-GPT decoder-only architecture, causal masking, autoregressive generation loop, aur text generation inference ko PyTorch mein implement karte hain.

```python
import math
import torch
import torch.nn as nn
from typing import Optional

# 1. Transformer Decoder Block with Pre-LayerNorm
class TransformerDecoderBlock(nn.Module):
    def __init__(self, d_model: int, n_heads: int, d_ff: int, dropout_p: float = 0.1) -> None:
        super().__init__()
        self.ln1 = nn.LayerNorm(d_model)
        self.attn = nn.MultiheadAttention(d_model, n_heads, dropout=dropout_p, batch_first=True)
        self.ln2 = nn.LayerNorm(d_model)
        self.mlp = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Linear(d_ff, d_model),
            nn.Dropout(dropout_p)
        )

    def forward(self, x: torch.Tensor, attn_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        # Pre-LN Self-Attention with residual connection: x + Attn(LN(x))
        normed = self.ln1(x)
        attn_out, _ = self.attn(normed, normed, normed, attn_mask=attn_mask, is_causal=True)
        x = x + attn_out
        # Pre-LN MLP with residual connection: x + MLP(LN(x))
        x = x + self.mlp(self.ln2(x))
        return x

# 2. Complete Mini-GPT Model
class MiniGPT(nn.Module):
    def __init__(self, vocab_size: int, max_seq_len: int, d_model: int, n_heads: int, n_layers: int) -> None:
        super().__init__()
        self.max_seq_len = max_seq_len
        self.token_emb = nn.Embedding(vocab_size, d_model)
        self.pos_emb = nn.Embedding(max_seq_len, d_model)
        self.drop = nn.Dropout(0.1)
        
        self.blocks = nn.ModuleList([
            TransformerDecoderBlock(d_model, n_heads, d_ff=4 * d_model)
            for _ in range(n_layers)
        ])
        self.ln_f = nn.LayerNorm(d_model)
        self.lm_head = nn.Linear(d_model, vocab_size, bias=False)

        # Weight tying: share token embedding weights with output projection
        self.lm_head.weight = self.token_emb.weight

    def forward(self, idx: torch.Tensor, targets: Optional[torch.Tensor] = None) -> tuple[torch.Tensor, Optional[torch.Tensor]]:
        # idx shape: [Batch, Seq_Len]
        B, S = idx.shape
        assert S <= self.max_seq_len, f"Sequence length {S} exceeds context limit {self.max_seq_len}"

        positions = torch.arange(0, S, device=idx.device).unsqueeze(0)  # Shape: [1, S]
        # Sum token and positional embeddings: [B, S, D]
        x = self.drop(self.token_emb(idx) + self.pos_emb(positions))

        # Pass sequentially through all transformer decoder blocks
        for block in self.blocks:
            x = block(x)

        x = self.ln_f(x)
        logits = self.lm_head(x)  # Shape: [B, S, vocab_size]

        loss = None
        if targets is not None:
            # Flatten batch and sequence dims for cross entropy calculation
            loss = nn.functional.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1))

        return logits, loss

    @torch.no_grad()
    def generate(self, prompt_tokens: torch.Tensor, max_new_tokens: int, temperature: float = 1.0) -> torch.Tensor:
        \"\"\"Autoregressive token generation loop with temperature sampling.\"\"\"
        self.eval()
        curr_tokens = prompt_tokens
        
        for _ in range(max_new_tokens):
            # Crop to context window if needed
            cond = curr_tokens[:, -self.max_seq_len:]
            logits, _ = self(cond)
            # Take logits of the very last position: [B, vocab_size]
            next_token_logits = logits[:, -1, :] / max(temperature, 1e-5)
            probs = torch.softmax(next_token_logits, dim=-1)
            next_token = torch.multinomial(probs, num_samples=1)  # [B, 1]
            curr_tokens = torch.cat([curr_tokens, next_token], dim=1)
            
        return curr_tokens

# Execution test
if __name__ == "__main__":
    torch.manual_seed(42)
    model = MiniGPT(vocab_size=256, max_seq_len=32, d_model=64, n_heads=4, n_layers=2)
    
    # Simulate batch of 2 prompts (Length 5)
    sample_prompt = torch.randint(0, 256, (2, 5))
    logits, _ = model(sample_prompt)
    print(f"Forward Pass Successful! Logits Shape: {list(logits.shape)}")

    # Autoregressive generation
    generated = model.generate(sample_prompt[:1], max_new_tokens=5, temperature=0.7)
    print(f"Generated Sequence Shape: {list(generated.shape)} (5 prompt tokens + 5 generated tokens)")
    print("Generated Token IDs:", generated.tolist()[0])
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Forgetting Weight Tying: Modern language models (GPT-2, Gemma, LLaMA) mein Token Embedding table aur Output Linear Head ke weights ko share (`lm_head.weight = token_emb.weight`) kiya jata hai. Is se na sirf 20-30% parameters bach jate hain balki validation perplexity bhi behtar hoti hai.
2. Indexing Wrong Slice During Autoregressive Generation: Agla token predict karte waqt agar aap `logits[:, 0, :]` (pehla token) le lein to model stuck ho jata hai. Hamesha aakhri predicted position `logits[:, -1, :]` uthayein.
3. Not Cropping Context Window in Generation: Loop chalte hue jab total tokens `max_seq_len` se barh jayein aur aap slice na karein (`cond = curr_tokens[:, -max_seq_len:]`), to Positional Embedding table out of bounds crash kar deti hai.

Zero-GPU Tip:
Is Mini-GPT model mein 65,000 parameters hain. Colab ya local CPU par yeh model 10,000 words ke raw Roman Urdu text par 2 minute mein train ho jata hai aur intelligible text generate karne lagta hai with zero GPU usage.

Self-Check Questions:
1. Mini-GPT ke forward pass mein token embeddings aur positional embeddings ko concatenate karne ke bajaye jama (add) kyun kiya jata hai?
2. Weight Tying technique model ke parameter count ko kaise kam karti hai?
3. Autoregressive generation mein temperature scaling aglay token ke intikhab par kya asar dalti hai?

What to Build Next:
Is Mini-GPT ko ek small character-level Urdu shayeri ya Roman Urdu chai dhabay ke dialogues dataset par 50 epochs train karein aur temperature 0.8 par nayi shayeri generate karein."""
