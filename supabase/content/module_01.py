# module_01.py
# Module 1: Python for AI & Fast Math (NumPy, Linear Algebra)
# Lessons 1.1 to 1.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 1.1: Python Data Structures Se NumPy Tensors Tak
# ==============================================================================
LESSON_CONTENT['1.1'] = """### Part 1: Mental Model & South Asian Analogy
AI Engineering mein tensor math ko samajhne ke liye sab se pehle computer hardware aur memory locality ka farq samajhna zaroori hai. Aam tor par log sochte hain ke computer ke liye ek million numbers ko multiply karna koi bara masla nahi hona chahiye. Lekin masla CPU ki calculation speed ka nahi hai, balki data supply ka hai!
Isay samajhne ke liye ek bohot mashhoor Biryani Factory ki misaal lein:
1. Python List (Scattered Pointers / Pointer Chasing): Farz karein biryani pakanay ke liye degh ustaad ko 100 masalay darakar hain. Lekin dukan ke chotu ne har masalay ki pudiya shehar ke alag alag konon mein chupa kar rakhi hui hai: laung Saddar mein hai, elaichi Clifton mein hai, aur zeera Nazimabad mein hai. Degh ustaad ko har ek chutki masalay ke liye motorcycle par shehar ke doosre konay jana parta hai. Jitna waqt masalay ko kootnay mein nahi lagta, us se 100 guna zyada waqt motorcycle chalane (RAM se CPU Cache tak data lane) mein zaaya ho jata hai. Isay computer architecture mein 'Cache Miss' aur 'Pointer Chasing' kehte hain.
2. NumPy Tensors (Contiguous C-Memory Block): Iske bar-aks, NumPy aisi factory hai jahan degh ke bilkul barabar mein ek steel ki tray rakhi hai jisme tamam masalay ek seedhi qataar mein bilkul sequence ke sath sajaye gaye hain. Degh ustaad ek hi baar tray se 8 masalay ek sath uthata hai aur degh mein daal deta hai.
3. Hardware SIMD Acceleration: Modern CPU processors ke andar SIMD (Single Instruction Multiple Data) registers hote hain (jaise AVX-2 ya AVX-512). Yeh register 256-bit ya 512-bit choray hote hain. Ek aam 32-bit floating point number 4 bytes ka hota hai. SIMD register ek hi clock cycle mein 8 ya 16 floating-point numbers ko parallel load karke single cycle mein multiply kar deta hai. Yahi physical hardware reason hai ke NumPy arrays pure Python loops se 50x se 100x tez hote hain!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein CPU Cache line aur 1D/2D array indexing ki memory mapping ko mathematically trace karte hain.
Modern x86-64 CPUs mein CPU Cache Line ka standard size 64 Bytes hota hai.
Agar hum 32-bit single precision floats (`np.float32`) use kar rahe hain to:
$1 \\text{ float32} = 4 \\text{ Bytes}$
Ek single 64-byte cache line ke andar fit aane wale floats:
$\\text{Floats per cache line} = \\frac{64 \\text{ Bytes}}{4 \\text{ Bytes}} = 16 \\text{ floats}$

Jab CPU RAM se array ka pehla element `arr[0]` mangwata hai to memory controller sirf pehla element nahi bhejta, balki poori 64-byte ki contiguous chunk bhejta hai jisme `arr[0]` se le kar `arr[15]` tak ke tamam 16 elements CPU L1 Cache mein pohnch jate hain.
Agla 15 elements ka access 'Cache Hit' hota hai jo sirf 1 se 4 CPU clock cycles leta hai.
Iske bar-aks, Python list mein har element ek `PyObject` pointer hota hai jo memory mein random location par hota hai. Har element ke liye CPU ko RAM tak jana parta hai jisme 150 se 200 clock cycles zaaya hote hain!

Ab dekhein 2D Matrix memory offset ka formula (Row-Major Order):
Matrix $M$ jiska shape $[R, C]$ hai (Rows, Columns):
Element $(i, j)$ ka physical 1D memory address offset:
$\\text{Offset}(i, j) = (i \\times C) + j$
Numeric Example:
Farz karein matrix ka shape $[3, 4]$ hai (3 rows, 4 columns):
Element $(2, 3)$ (yani 3rd row, 4th column) ka memory offset:
$\\text{Offset}(2, 3) = (2 \\times 4) + 3 = 8 + 3 = 11$
NumPy C-engine direct 11th float address par jump karta hai bina kisi intermediate pointer lookup ke.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum pure Python vs NumPy SIMD speedup benchmark karte hain, memory stride layout inspect karte hain, aur multi-dimensional tensor shape transformations ko implement karte hain.

```python
import time
import numpy as np

# 1. Empirical Latency & Cache Locality Benchmark
DATASET_SIZE: int = 5_000_000

# Allocate pure Python dynamic pointer lists
py_list_a = [float(i) for i in range(DATASET_SIZE)]
py_list_b = [float(i * 2) for i in range(DATASET_SIZE)]

# Time pure Python sequential multiplication (Cache miss bound)
start_time = time.perf_counter()
py_res = [a * b for a, b in zip(py_list_a, py_list_b)]
py_elapsed = time.perf_counter() - start_time

# Allocate contiguous 32-bit NumPy arrays (SIMD aligned)
np_arr_a = np.arange(DATASET_SIZE, dtype=np.float32)
np_arr_b = np.arange(DATASET_SIZE, dtype=np.float32) * 2.0

# Time NumPy vectorized execution (SIMD AVX parallel)
start_time = time.perf_counter()
np_res = np_arr_a * np_arr_b
np_elapsed = time.perf_counter() - start_time

print(f"Python Loop Latency: {py_elapsed:.4f}s")
print(f"NumPy SIMD Latency:  {np_elapsed:.4f}s")
print(f"Hardware Speedup:    {py_elapsed / max(np_elapsed, 1e-9):.1f}x faster")

# 2. Strides & Contiguity Deep Dive
matrix_2d = np.ones((3, 4), dtype=np.float32)
print("\\nMatrix Shape:", matrix_2d.shape)        # Shape: (3, 4)
print("Memory Strides (Bytes):", matrix_2d.strides)  # (16, 4) -> 16 bytes per row, 4 bytes per col
print("Is Contiguous:", matrix_2d.flags['C_CONTIGUOUS'])

# 3. Safe Tensor Reshaping without Memory Copy
# Reshape from (3, 4) to (6, 2)
reshaped_view = matrix_2d.reshape(6, 2)
print("Reshaped Shape:", reshaped_view.shape)
print("Shares Base Memory:", reshaped_view.base is matrix_2d)
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Implicit 64-bit Float Bloat: NumPy default tor par `np.float64` allocate karta hai agar dtype mention na kiya jaye. AI aur deep learning models mein standard `np.float32` ya `np.float16` hota hai. Float64 use karne se RAM double kharch hoti hai aur SIMD throughput aadhi ho jati hai. Hamesha explicit `dtype=np.float32` likhein.
2. Accidental Non-Contiguous Memory (Broken Strides): Transpose lene ke baad (`arr.T`) array Fortran-order ban jata hai aur contiguous nahi rehta. Agar aap is par C-extensions ya direct memory buffers chalayenge to performance gir jayegi. Agar zaroorat ho to `np.ascontiguousarray(arr)` call karein.
3. Looping Over NumPy Arrays with `for x in arr:`: Agar aap NumPy array par Python ka `for` loop chalate hain to NumPy ka sara faida khatam ho jata hai kyunke har step par Python wrapper object banta hai. Hamesha vectorized expressions use karein.

Zero-GPU Tip:
NumPy vectorization aapke local CPU ke tamam SIMD vector lanes (SSE, AVX2, AVX-512) ko fully utilize karti hai. Google Colab ke free CPU par bhi 50 lakh numbers ka vector dot product 15 milliseconds se kam waqt mein complete ho jata hai.

Self-Check Questions:
1. CPU Cache Line kya hoti hai aur NumPy contiguous memory iska faida kaise uthati hai?
2. Array ke `strides` attribute ka kya matlab hai? (Answer: Har dimension mein agle element tak pohnchne ke liye kitne bytes memory jump karni parti hai).
3. `np.reshape()` aur `np.copy()` mein computational cost aur memory overhead ka kya farq hai?

What to Build Next:
Ek Benchmark Suite script banayein jo matrix multiplication ($1000 \\times 1000$) ko pure Python nested loops vs NumPy `np.matmul` ke sath compare kare aur memory profiling se verify kare ke dono mein kitna farq hai."""

# ==============================================================================
# LESSON 1.2: Linear Algebra Intuition: Dot Products, Projections & Embeddings
# ==============================================================================
LESSON_CONTENT['1.2'] = """### Part 1: Mental Model & South Asian Analogy
Linear Algebra modern AI ka dil aur rooh hai. Neural networks, LLMs, aur Vector Databases dar-haqeeqat high-dimensional vector spaces mein geometric operations karte hain.
Isay samajhne ke liye kisi bare shehar ke housing market (Property Dealer / Real Estate) ki misaal lein:
1. Vectors as Coordinates: Farz karein aik property dealer ke paas mukhtalif makanat ki maloomat hain. Har makan ko 3 numbers se describe kiya ja sakta hai:
   - Feature 1: Kamron ki tadaad (Rooms)
   - Feature 2: Raqba (Square feet)
   - Feature 3: Main road se doori (Kilometers)
   Yeh teen numbers mil kar 3D space mein ek teer (Vector) banate hain: $\\vec{v} = [3, 1200, 2]$.
2. Dot Product as Alignment (Samt Ka Milna): Do vectors ka dot product batata hai ke dono teer kis hadd tak ek hi direction mein ja rahe hain. Misaal ke taur par, agar do dost ek hi direction mein cycle chala rahe hon to unka energy overlap sab se zyada hota hai. Agar dono bilkul aamne saamne (opposite) cycle chala rahe hon to takkar hoti hai (negative alignment). Agar ek dost uttar (North) ja raha ho aur doosra mashriq (East) yani 90 degrees par, to dono ka ek doosre ke raste par koi asar nahi hota (Orthogonal / Zero Alignment).
3. Cosine Similarity in Vector Search (RAG): Jab hum text ko AI embedding banate hain, to sentence ek 1536-dimensional vector ban jata hai. Sentence ki lambai (magnitude) se farq nahi parta; ahem yeh hai ke dono sentences ka maani (angle $\\theta$) kitna qareeb hai! Cosine similarity do vectors ke darmiyan angle ka cosine nikal kar batati hai ke dono baatein kitni milti julti hain:
   - $\\cos(0^\\circ) = 1.0$: 100% Semantic Match (Jaise: "Chai peeni hai" aur "Mujhe tea chahiye").
   - $\\cos(90^\\circ) = 0.0$: Koi taluq nahi (Jaise: "Karachi ka mausam" aur "PyTorch optimization").

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Dot Product, Euclidean Norm (Magnitude), aur Cosine Similarity ka mukammal hisab choti raqmon ke sath step-by-step karein.
Farz karein hamare paas do 3D embedding vectors hain:
Vector $A = [1.0, 2.0, 3.0]$
Vector $B = [2.0, 4.0, 6.0]$
Aur teesra unrelated vector $C = [-3.0, 0.0, 1.0]$

Step 1: Dot Product of A and B
$A \\cdot B = (A_0 \\times B_0) + (A_1 \\times B_1) + (A_2 \\times B_2)$
$A \\cdot B = (1.0 \\times 2.0) + (2.0 \\times 4.0) + (3.0 \\times 6.0)$
$A \\cdot B = 2.0 + 8.0 + 18.0 = 28.0$

Step 2: Euclidean Norms (Lengths) of A and B
$\\|A\\| = \\sqrt{1.0^2 + 2.0^2 + 3.0^2} = \\sqrt{1 + 4 + 9} = \\sqrt{14} \\approx 3.7416$
$\\|B\\| = \\sqrt{2.0^2 + 4.0^2 + 6.0^2} = \\sqrt{4 + 16 + 36} = \\sqrt{56} \\approx 7.4833$

Step 3: Cosine Similarity Formula
$\\cos(\\theta) = \\frac{A \\cdot B}{\\|A\\| \\times \\|B\\|}$
Denominator: $\\sqrt{14} \\times \\sqrt{56} = \\sqrt{14} \\times (2 \\times \\sqrt{14}) = 2 \\times 14 = 28.0$
$\\cos(\\theta) = \\frac{28.0}{28.0} = 1.0000$
Dono vectors ka angle bilkul $0^\\circ$ hai kyunke $B = 2 \\times A$! Yeh perfectly parallel hain.

Step 4: Dot Product of A and C (Orthogonal check)
$A \\cdot C = (1.0 \\times -3.0) + (2.0 \\times 0.0) + (3.0 \\times 1.0)$
$A \\cdot C = -3.0 + 0.0 + 3.0 = 0.0$
$\\cos(\\theta) = \\frac{0.0}{\\|A\\| \\times \\|C\\|} = 0.0000$ (Angle is exactly $90^\\circ$). Inka aapas mein zero correlation hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum zero external libraries (pure NumPy) ke sath production-grade, numerically-stable batch cosine similarity matrix calculator implement karte hain jo vector search databases mein use hota hai.

```python
import numpy as np

def compute_batch_cosine_similarity(
    query_embeddings: np.ndarray, 
    document_embeddings: np.ndarray, 
    eps: float = 1e-9
) -> np.ndarray:
    \"\"\"Computes pairwise cosine similarity between query batch and document catalog.
    
    Shapes:
      query_embeddings:    [num_queries, embedding_dim]
      document_embeddings: [num_docs, embedding_dim]
    Returns:
      similarity_matrix:   [num_queries, num_docs]
    \"\"\"
    # Input assertions for dimension safety
    assert query_embeddings.ndim == 2, f"Expected 2D query tensor, got {query_embeddings.shape}"
    assert document_embeddings.ndim == 2, f"Expected 2D doc tensor, got {document_embeddings.shape}"
    assert query_embeddings.shape[1] == document_embeddings.shape[1], "Embedding dimension mismatch"

    # 1. Compute dot products via matrix multiplication [num_queries, num_docs]
    dot_products = np.matmul(query_embeddings, document_embeddings.T)

    # 2. Compute L2 Norms with numerical stability epsilon
    query_norms = np.linalg.norm(query_embeddings, axis=1, keepdims=True)  # [num_queries, 1]
    doc_norms = np.linalg.norm(document_embeddings, axis=1, keepdims=True)      # [num_docs, 1]

    # 3. Outer product of norms for denominator broadcasting
    norm_matrix = np.matmul(query_norms, doc_norms.T)  # [num_queries, num_docs]
    norm_matrix = np.maximum(norm_matrix, eps)         # Prevent division by zero

    # 4. Final normalized cosine similarity
    similarity_matrix = dot_products / norm_matrix
    return similarity_matrix

if __name__ == "__main__":
    # Simulated semantic embeddings (Dimension = 4)
    # Query: "Dhaba chai order"
    q_vec = np.array([[0.8, 0.1, 0.5, 0.2]], dtype=np.float32)  # Shape: [1, 4]

    # Candidate documents in vector DB
    # Doc 0: "Karak chai and paratha delivery" (High relevance)
    # Doc 1: "PyTorch GPU cluster setup" (Low relevance)
    # Doc 2: "Tea stall business accounting" (Medium relevance)
    doc_vecs = np.array([
        [0.78, 0.12, 0.48, 0.22],
        [0.05, 0.95, -0.20, 0.10],
        [0.60, 0.30, 0.40, 0.15]
    ], dtype=np.float32)  # Shape: [3, 4]

    scores = compute_batch_cosine_similarity(q_vec, doc_vecs)  # Shape: [1, 3]
    print("Similarity Matrix Shape:", scores.shape)
    for idx, score in enumerate(scores[0]):
        print(f"  Doc {idx} Similarity Score: {score:.4f}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Division by Zero on Zero Vectors: Agar corpus mein koi empty document ya all-zero embedding vector aa jaye to uska norm $0.0$ hoga. Division by zero ki wajah se `NaN` values poore vector index ko corrupt kar deti hain. Hamesha `np.maximum(norm, 1e-9)` shamil karein.
2. In-Loop Single Vector Multiplication ($O(N)$ Matrix-Vector Degradation): Loop chala kar ek ek document ka dot product nikalna sab se bara bottleneck hai. Hamesha matrix multiplication `np.matmul(Q, D.T)` use karein jo poore batch ko BLAS level-3 optimized library se solve karta hai.
3. Confusing Dot Product with Cosine Similarity: Dot product vector ki length par depend karta hai. Agar ek document bohot lamba ho to uska dot product bara ho sakta hai chahe maani match na kare. Hamesha normalized cosine similarity use karein jab tak vectors pehle se unit-normalized na hon.

Zero-GPU Tip:
Batch cosine similarity calculations ke liye OpenBLAS ya MKL libraries CPU ke tamam cores ko parallel use karti hain. 10,000 documents ka similarity search standard CPU par 5 milliseconds mein ho jata hai, iske liye kisi expensive GPU ki zaroorat nahi hai.

Self-Check Questions:
1. Cosine similarity aur Dot product mein geometric aur mathematical farq kya hai?
2. Agar do vectors ke darmiyan angle $90^\\circ$ ho to unka dot product kya hoga aur iska semantic matlab kya hai?
3. Matrix multiplication `A @ B.T` mein shapes ka kya rule hota hai?

What to Build Next:
Ek In-Memory Vector Search Engine banayein jo 50 synthetic text chunks ke random embeddings generate kare, user ki query embedding accept kare, top-3 closest documents unke cosine scores ke sath return kare."""

# ==============================================================================
# LESSON 1.3: Calculus & Gradient Descent
# ==============================================================================
LESSON_CONTENT['1.3'] = """### Part 1: Mental Model & South Asian Analogy
AI aur Deep Learning ka sab se bara jadu yeh hai ke model "khud seekhta hai". Lekin model koi insani dimaag nahi hai jo sochta ho; iske seekhne ka sara mechanism Calculus aur Gradient Descent par mushtamil hai.
Isay samajhne ke liye kisi Andheri Raat mein Pahari se Neeche Utarne ki misaal lein:
1. The Dark Mountain (Loss Surface): Farz karein aap Murree ya Margalla Hills ki kisi oonchi pahari par khare hain aur chaaron taraf gup andhera hai, hath ko hath sujhayi nahi de raha. Aapka maqsad pahari ki choti se nikal kar bilkul neeche wadi (Valley) mein pohnchna hai jahan aapka hotel hai. Wadi ki satah par aapka faasla (Loss / Error) zero ho jata hai.
2. Slope Under Your Foot (The Gradient / Derivative): Chunke aap aankhon se dekh nahi sakte, is liye aap apne paon se zameen ki dhalan (slope) mehsoos karte hain. Aapka paon batata hai: "Zameen is samt mein upar ja rahi hai aur pichli samt mein neeche dhalan hai." Riyazi mein is dhalan ko Derivative ya Gradient kehte hain.
3. Walking Downhill (Negative Gradient Step): Agar aap wadi mein jana chahte hain to aap dhalan ki mukhalif samt (negative direction) mein qadam barhayenge. Agar aap dhalan ke sath upar chalenge to pahari ki choti par pohnch jayenge.
4. Step Size (Learning Rate $\\eta$):
   - Agar aap bohot lambi chhalang lagayein (Very High Learning Rate, e.g. $\\eta = 10.0$), to aap wadi ko cross karke samne wali doosri pahari par ja girenge (Divergence / Exploding Loss).
   - Agar aap chiyunti ke barabar qadam uthayein (Very Small Learning Rate, e.g. $\\eta = 0.000001$), to subah ho jayegi lekin aap pahari se 2 foot bhi neeche nahi utar sakenge (Extremely Slow Convergence).
   - Sahi learning rate (e.g. $\\eta = 0.01$) woh munasib qadam hai jo har step par wadi ke qareeb karta jata hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein ek simple Linear Neuron ke upar Mean Squared Error (MSE) loss aur Gradient Descent ka ek mukammal step hath se calculate karte hain.
Model Equation:
$\\hat{y} = w \\cdot x + b$
Target Data Point:
- Input feature $x = 2.0$
- True label $y = 5.0$

Initial Parameters:
- Weight $w = 1.0$ (Random guess)
- Bias $b = 0.0$
- Learning Rate $\\eta = 0.1$

Step 1: Forward Pass (Prediction)
$\\hat{y} = (1.0 \\times 2.0) + 0.0 = 2.0$

Step 2: Compute Loss (Squared Error)
$L = (\\hat{y} - y)^2 = (2.0 - 5.0)^2 = (-3.0)^2 = 9.0$
Model ka loss 9.0 hai, jo bohot bara error hai.

Step 3: Calculus Chain Rule se Gradients nikalna
$\\frac{\\partial L}{\\partial \\hat{y}} = 2 \\times (\\hat{y} - y) = 2 \\times (2.0 - 5.0) = -6.0$ (Error Signal)
Gradient with respect to Weight ($w$):
$\\frac{\\partial L}{\\partial w} = \\frac{\\partial L}{\\partial \\hat{y}} \\times \\frac{\\partial \\hat{y}}{\\partial w} = (-6.0) \\times x = -6.0 \\times 2.0 = -12.0$
Gradient with respect to Bias ($b$):
$\\frac{\\partial L}{\\partial b} = \\frac{\\partial L}{\\partial \\hat{y}} \\times \\frac{\\partial \\hat{y}}{\\partial b} = (-6.0) \\times 1 = -6.0$

Step 4: Parameter Update Step (Negative Gradient)
$w_{\\text{new}} = w - \\eta \\times \\frac{\\partial L}{\\partial w} = 1.0 - (0.1 \\times -12.0) = 1.0 + 1.2 = 2.2$
$b_{\\text{new}} = b - \\eta \\times \\frac{\\partial L}{\\partial b} = 0.0 - (0.1 \\times -6.0) = 0.0 + 0.6 = 0.6$

Step 5: Verify Loss Improvement
Naye parameters ke sath forward pass:
$\\hat{y}_{\\text{new}} = (2.2 \\times 2.0) + 0.6 = 4.4 + 0.6 = 5.0$
Naya Loss:
$L_{\\text{new}} = (5.0 - 5.0)^2 = 0.0000$!
Sirf ek single gradient descent step mein error 9.0 se seedha 0.0 par pohnch gaya! Yahi calculus ka jaadu hai jo lakhoon parameters par chalta hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum pure NumPy ke sath multi-variable batch gradient descent optimization loop from scratch implement karte hain.

```python
import numpy as np

# Set random seed for exact reproducibility
np.random.seed(42)

# 1. Generate Synthetic Training Data (Ground truth: y = 3.5 * x + 1.2 + noise)
NUM_SAMPLES = 200
X = np.random.uniform(0.0, 5.0, size=(NUM_SAMPLES, 1)).astype(np.float32)  # Shape: [200, 1]
noise = np.random.normal(0.0, 0.2, size=(NUM_SAMPLES, 1)).astype(np.float32)
y_true = 3.5 * X + 1.2 + noise                                           # Shape: [200, 1]

# 2. Initialize Model Parameters randomly
w = np.random.randn(1, 1).astype(np.float32) * 0.01  # Weight tensor: [1, 1]
b = np.zeros((1, 1), dtype=np.float32)              # Bias tensor:   [1, 1]

LEARNING_RATE: float = 0.05
NUM_EPOCHS: int = 150

print(f"Initial State -> w: {w[0,0]:.4f}, b: {b[0,0]:.4f}")

# 3. Optimization Training Loop
for epoch in range(1, NUM_EPOCHS + 1):
    # Forward Pass: Compute predictions y_pred [200, 1]
    y_pred = np.matmul(X, w) + b
    
    # Compute Mean Squared Error (MSE) Loss
    error = y_pred - y_true                         # Shape: [200, 1]
    loss = np.mean(error ** 2)
    
    # Analytical Gradients via Calculus (Averaged over batch)
    dw = (2.0 / NUM_SAMPLES) * np.matmul(X.T, error)  # Shape: [1, 1]
    db = (2.0 / NUM_SAMPLES) * np.sum(error, keepdims=True)  # Shape: [1, 1]
    
    # Parameter Updates along Negative Gradient
    w -= LEARNING_RATE * dw
    b -= LEARNING_RATE * db
    
    if epoch % 30 == 0 or epoch == 1:
        print(f"Epoch {epoch:03d}/{NUM_EPOCHS} | Loss: {loss:.4f} | w: {w[0,0]:.3f} | b: {b[0,0]:.3f}")

print(f"\\nFinal Learned Model: y = {w[0,0]:.2f} * x + {b[0,0]:.2f}")
print("Expected Target:     y = 3.50 * x + 1.20")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Exploding Learning Rate: Agar learning rate bohot zyada ho (e.g. `lr = 5.0`), to weights har step par double hokar foran `NaN` ya `Inf` ban jate hain. Agar loss ghate ke bajaye barh raha ho to pehla qadam learning rate ko 10x kam karna hota hai.
2. Forgetting to Average Over Batch Size: Gradients calculate karte waqt agar aap sample count $N$ se divide nahi karte to batch size barhne se gradient ka magnitude itna bara ho jata hai ke optimization loop collapse ho jata hai.
3. Vanishing Gradient on Unscaled Features: Agar data features bohot bare numbers hon (e.g. Salary = 500,000 aur Age = 25), to gradients unstable ho jate hain. Training se pehle hamesha Standard Normalization ($z = \\frac{x - \\mu}{\\sigma}$) karein.

Zero-GPU Tip:
Linear regression aur standard gradient descent loops CPU par seconds mein hazaron epochs train ho jate hain. NumPy vectorization matrix multiplications ko AVX registers mein chalati hai, jisse CPU usage 100% efficient rehti hai.

Self-Check Questions:
1. Gradient Descent mein negative sign ($-$) kyun lagaya jata hai parameter update ke waqt?
2. Chain Rule ka AI backpropagation mein kya kirdaar hai?
3. Learning rate bohot chota hone se kya nuqsan hota hai?

What to Build Next:
Ek Polynomial Regression Trainer banayein jo $y = a x^2 + b x + c$ ke parameters $a, b, c$ ko gradient descent se learn kare aur loss curve ko print kare."""

# ==============================================================================
# LESSON 1.4: Python 3.12 GIL, Memory Profiling & AsyncIO
# ==============================================================================
LESSON_CONTENT['1.4'] = """### Part 1: Mental Model & South Asian Analogy
Production AI systems mein sab se bara challenge sirf model ka accuracy nahi hota, balki system throughput aur memory leaks hote hain. Python mein likhi gayi AI application aksar high concurrency par choke ho jati hai.
Isay samajhne ke liye kisi Shehar ke Mashhoor Driving License Office ki misaal lein:
1. The GIL (Global Interpreter Lock): Farz karein license office mein 8 counter (8 CPU Cores) lage hain. Har counter par ek clerk baitha hai. Lekin office ke darwazay par ek hi official Stamp (The GIL) mojud hai. Qanoon yeh hai ke jab tak kisi clerk ke paas woh stamp na ho, woh file par aage kaam nahi kar sakta. Nateeja kya nikalta hai? Ek waqt mein sirf ek hi clerk stamp use karta hai aur baqi 7 clerks haath par haath dharay baithe rehte hain! Yeh Python ka GIL hai jo CPU-bound tasks (jaise pure Python math loops) mein multi-threading ko bekaar kar deta hai.
2. I/O-Bound Tasks & AsyncIO: Lekin ab doosra manzar dekhein. Har candidate ko file submit karne ke baad medical test aur fee challan jama karwane bank jana parta hai (Network/API latency). Agar clerk har candidate ke bank se wapas aane tak kursi par khali baitha rahe to system jam ho jayega. Samajhdaar clerk (AsyncIO Event Loop) kya karta hai? Woh pehle candidate ko kehta hai: "Aap challan bharne jayein, jab tak aap wapas aayenge main aglay 50 logon ki files check karta hoon." Jaise hi koi banda challan le kar wapas aata hai (Event Ready), clerk uski file pakar kar agla step mukammal kar deta hai.
3. Memory Profiling (`tracemalloc`): Farz karein daftari almaari mein files bharte bharte kamra bhar gaya hai aur nayi file rakhne ki jagah nahi bachi (RAM Out-of-Memory). `tracemalloc` ek audit inspector jaisa hai jo har file par tag laga kar batata hai ke kaun sa function sab se zyada kaghaz (RAM bytes) kha raha hai taake fuzool data ko foran recycle kiya ja sake.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein dekhte hain ke Synchronous vs Asynchronous I/O execution mein latency aur throughput ka hisab kaise badalta hai.
Farz karein hum 100 customer prompts ko kisi remote LLM API (jaise Groq ya OpenAI) par bhej kar completions lena chahte hain.
Parameters:
- Total requests $N = 100$
- Har remote API call ka network round-trip time $T_{\\text{network}} = 0.5 \\text{ seconds}$ (500 ms).
- Server par available CPU threads = 1

Scenario A: Synchronous Sequential Processing
Har request pichli request khatam hone ke baad shuru hoti hai:
$T_{\\text{total}} = N \\times T_{\\text{network}} = 100 \\times 0.5 \\text{s} = 50.0 \\text{ seconds}$
System Throughput:
$\\text{Throughput} = \\frac{100 \\text{ requests}}{50.0 \\text{ seconds}} = 2.0 \\text{ requests per second (RPS)}$
CPU 99% waqt khali network packet ka intezar karta rehta hai!

Scenario B: AsyncIO Event Loop Concurrency
AsyncIO mein tamam 100 requests non-blocking socket ke zariye taqreeban aik sath network par dispatch ho jati hain:
Har dispatch mein lagne wala CPU time $\\approx 0.001 \\text{s}$ (1 ms).
100 requests dispatch karne ka waqt: $100 \\times 0.001 = 0.1 \\text{s}$.
Tamam requests network par parallel safar kar rahi hoti hain.
Sab se aakhri response aane ka waqt: $\\approx 0.5 \\text{s} + 0.1 \\text{s} = 0.6 \\text{s}$.
$T_{\\text{total}} \\approx 0.65 \\text{ seconds}$
System Throughput:
$\\text{Throughput} = \\frac{100 \\text{ requests}}{0.65 \\text{ seconds}} \\approx 153.8 \\text{ RPS}$
Concurrency Speedup:
$\\frac{50.0}{0.65} \\approx 76.9\\times \\text{ Throughput Increase}$ bina kisi GPU ya multi-core CPU cluster ke!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Python ke modern `asyncio` event loop, non-blocking coroutines, structured concurrency with `asyncio.TaskGroup` (Python 3.11+ standard), aur `tracemalloc` memory profiling ko implement karte hain.

```python
import asyncio
import time
import tracemalloc
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass(slots=True)
class LLMRequestPayload:
    request_id: int
    prompt_text: str
    temperature: float = 0.7

async def simulate_non_blocking_llm_call(payload: LLMRequestPayload) -> Dict[str, Any]:
    \"\"\"Simulates asynchronous I/O round-trip to remote inference endpoint.\"\"\"
    # Non-blocking async sleep emulating network I/O
    await asyncio.sleep(0.05)
    
    # Return structured completion response
    return {
        "id": payload.request_id,
        "token_count": len(payload.prompt_text.split()) * 4,
        "completion": f"Sanitized response for request {payload.request_id}",
        "status": 200
    }

async def run_concurrent_pipeline(batch_size: int = 50) -> List[Dict[str, Any]]:
    \"\"\"Processes high-concurrency requests using Python 3.11+ TaskGroup.\"\"\"
    payloads = [
        LLMRequestPayload(
            request_id=i, 
            prompt_text=f"AI Ustaad production query payload number {i}"
        ) 
        for i in range(batch_size)
    ]
    
    results: List[Dict[str, Any]] = []
    
    # Modern Python 3.11+ Structured Concurrency
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(simulate_non_blocking_llm_call(p)) for p in payloads]
        
    # All tasks guaranteed completed when exiting TaskGroup context
    results = [t.result() for t in tasks]
    return results

def main():
    # 1. Start Memory Profiler
    tracemalloc.start()
    
    t0 = time.perf_counter()
    batch_results = asyncio.run(run_concurrent_pipeline(batch_size=100))
    total_duration = time.perf_counter() - t0
    
    # 2. Inspect Peak Memory Allocation
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Processed {len(batch_results)} LLM calls in {total_duration:.4f} seconds!")
    print(f"Throughput: {len(batch_results) / total_duration:.1f} requests/sec")
    print(f"Current RAM Allocated: {current_mem / 1024:.2f} KB")
    print(f"Peak RAM Overhead:     {peak_mem / 1024:.2f} KB (Protected by slots=True)")

if __name__ == "__main__":
    main()
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Blocking Synchronous Calls Inside Coroutines: Async function ke andar `time.sleep(2)` ya `requests.get()` call karna fatal error hai. Yeh pure single-threaded event loop ko block kar deta hai aur baqi tamam concurrent tasks ruk jate hain. Hamesha non-blocking `await asyncio.sleep()` aur `httpx.AsyncClient` use karein.
2. Unbounded Task Spawning (Rate Limit & Socket Exhaustion): Ek sath 10,000 tasks spawn kar dena OS ke file descriptors (sockets) ko khatam kar deta hai aur API provider 429 Too Many Requests throw karta hai. Hamesha `asyncio.Semaphore(50)` se concurrency limit control karein.
3. Forgetting to Await a Coroutine: Agar aap `result = my_async_func()` likhte hain aur `await` lagana bhool jate hain, to function execute hi nahi hota aur `RuntimeWarning: coroutine was never awaited` milta hai.

Zero-GPU Tip:
AsyncIO pure I/O scheduling mechanism hai. Iske zariye aap apne aam laptop se hazaron concurrent LLM API requests monitor aur route kar sakte hain bina kisi GPU ya expensive server ke.

Self-Check Questions:
1. Python ke GIL aur CPU multi-threading mein kya taalluq hai?
2. AsyncIO event loop CPU-bound tasks (jaise matrix multiplication) ko tez kyun nahi kar sakta?
3. Python 3.11+ ke `asyncio.TaskGroup` ka `asyncio.gather` ke muqablay mein error handling mein kya faida hai?

What to Build Next:
Ek Resilient Async LLM Dispatcher banayein jo `asyncio.Semaphore` se maximum 10 concurrent requests allow kare, har request par exponential backoff retry lagaye, aur completion metrics report kare."""

# ==============================================================================
# LESSON 1.5: Polars & Apache Arrow Data Wrangling
# ==============================================================================
LESSON_CONTENT['1.5'] = """### Part 1: Mental Model & South Asian Analogy
Data preprocessing AI systems ki bunyad hai. Pichle 15 saal tak Pandas industry standard raha, lekin 2026 mein modern high-throughput AI pipelines mein Pandas ki jagah **Polars** aur **Apache Arrow** ne le li hai.
Is tabdeeli ko samajhne ke liye kisi bare Supermarket (Jaise Imtiaz Super Market ya Carrefour) ki misaal lein:
1. Pandas (The Traditional Single-Lane Grocery Store): Pandas 2008 mein bana tha jab CPU single-core hote the. Pandas ek single-threaded dukan jaisa hai jahan ek akela cashier khara hai. Jab aap customer ka data mangwate hain, to Pandas har column aur row ke data ki alag copy banata hai (Memory Doubling / Out-of-Memory Crash). Agar data 8 GB RAM se bara ho to system foran blue screen ya crash ho jata hai.
2. Polars (The Multi-Lane High-Tech Warehouse): Polars Rust language mein likha gaya hai. Yeh supermarket ke tamam 16 counters (16 CPU Cores) ko ek sath kholta hai. Har core ke SIMD registers parallel kaam karte hain aur data ko bina kisi lock ke parallel process karte hain.
3. Apache Arrow Columnar Format: Aam CSV ya row-based data aisa hota hai jese ek qataar mein sabzi, shampoo, chawal, aur dahi ek sath bandhe hon. Agar aapko sirf dahi ki qeemat check karni ho to poori qataar kholni parti hai. Apache Arrow Columnar Format tamam dahi ke dabbay ek alag cold-storage pipe mein rakhta hai aur sabzi ko alag pipe mein. Jab aap 'price' mangte hain to CPU seedha price wale pipe par hardware vector instruction chala deta hai.
4. Lazy Evaluation (`.lazy()`): Farz karein aapne ustaad se kaha: "Pehle 10 lakh items ko sort karo, phir unme se sirf Karachi ke customers nikalo, aur phir pehle 5 dikhao."
   - Eager Pandas: Pehle poore 10 lakh items ko sort karega (10 minute zaaya), phir filter karega, phir slice karega.
   - Lazy Polars: Ustaad poori list ko pehle analyze karega (Query Plan Optimizer) aur kahega: "Pehle hi sirf Karachi ke pehle 5 utha lo, baqi 9 lakh 99 hazar ko sort karne ki zaroorat hi kya hai!" Isay computer science mein 'Predicate Pushdown' kehte hain.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein dekhte hain ke Columnar Memory vs Row-based Memory mein CPU cache kitni efficiently use hoti hai.
Farz karein hamare paas ek table hai jisme 4 records hain aur 3 columns hain:
Columns: `[id: int32, age: int32, salary: float32]` (Har value = 4 Bytes).

Row-Based Layout (Traditional C / Python Dicts):
Memory mein data is tarteeb se rakha hota hai:
`[id_0, age_0, sal_0, id_1, age_1, sal_1, id_2, age_2, sal_2, id_3, age_3, sal_3]`
Record size = $3 \\times 4 = 12 \\text{ Bytes}$.
Agar hume sirf average salary calculate karni ho:
CPU ko pehla salary float uthana parta hai (Byte 8), phir agle salary ke liye 12 bytes jump karke Byte 20 par jana parta hai. CPU cache line mein 64 bytes aate hain jisme se do-tihai (id aur age) bekaar data hota hai jo cache ko pollute karta hai!

Columnar Arrow Layout (Polars Standard):
Memory mein har column ka apna contiguous array hota hai:
- `ids:`     `[id_0, id_1, id_2, id_3]` (16 Bytes contiguous)
- `ages:`    `[age_0, age_1, age_2, age_3]` (16 Bytes contiguous)
- `salaries:` `[sal_0, sal_1, sal_2, sal_3]` (16 Bytes contiguous)

Calculation of Average Salary:
CPU seedha `salaries` memory pointer uthata hai. Ek single 64-byte CPU cache line ke andar 16 consecutive salaries pohnch jati hain. SIMD AVX register single instruction mein tamam salaries ko parallel add kar deta hai:
$\\text{Sum} = 50000 + 60000 + 75000 + 95000 = 280000$
$\\text{Mean} = \\frac{280000}{4} = 70000.0$
Zero cache pollution, zero pointer chasing, aur 10x se 50x kam memory bandwidth consumption!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Polars lazy frame, streaming pipeline, predicate pushdown query optimization, aur zero-copy Parquet data wrangling ko implement karte hain.

```python
import polars as pl
import numpy as np

# 1. Generate Synthetic Enterprise Dataset (100,000 transaction records)
N_RECORDS: int = 100_000
np.random.seed(42)

raw_data = {
    "transaction_id": np.arange(N_RECORDS, dtype=np.int64),
    "city": np.random.choice(["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"], N_RECORDS),
    "amount_pkr": np.random.uniform(100.0, 25000.0, N_RECORDS).astype(np.float32),
    "is_fraud": np.random.choice([True, False], N_RECORDS, p=[0.02, 0.98]),
    "category": np.random.choice(["chai_dhaba", "electronics", "apparel", "grocery"], N_RECORDS)
}

# Ingest into Polars DataFrame
df = pl.DataFrame(raw_data)
print(f"Ingested DataFrame Shape: {df.shape}")

# 2. Build High-Performance Lazy Execution Plan
# Note: No computation happens here; only an AST query plan is compiled!
lazy_pipeline = (
    df.lazy()
    # Predicate Pushdown: Filter early to minimize row memory footprint
    .filter((pl.col("is_fraud") == False) & (pl.col("amount_pkr") > 500.0))
    # Group by city and category
    .group_by(["city", "category"])
    .agg([
        pl.count().alias("valid_transactions"),
        pl.col("amount_pkr").sum().round(2).alias("total_revenue_pkr"),
        pl.col("amount_pkr").mean().round(2).alias("avg_basket_size_pkr")
    ])
    # Sort descending by total revenue
    .sort("total_revenue_pkr", descending=True)
)

# 3. Print Optimized Query Plan
print("\\n--- Polars Optimized Query Execution Plan ---")
print(lazy_pipeline.explain())

# 4. Execute (Materialize) the computation across all CPU threads
materialized_results = lazy_pipeline.collect()
print("\\n--- Top 5 Revenue Aggregations ---")
print(materialized_results.head(5))
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Calling `.collect()` Prematurely: Polars mein agar aap har step ke baad `.collect()` call kar dete hain to Lazy Engine ki query optimization (filter pushdown, projection pruning) khatam ho jati hai aur intermediate results RAM mein load ho jate hain. Poori pipeline ko `.lazy()` mein chain karein aur bilkul aakhir mein ek martaba `.collect()` karein.
2. Converting Polars to Pandas for Basic Tasks: Aksar developers aadat ki wajah se `df.to_pandas()` likh dete hain. Yeh conversion Apache Arrow memory ko standard Python objects mein unpack karti hai jisse RAM foran 3x barh jati hai aur execution slow ho jati hai. Hamesha native Polars expressions use karein.
3. Ignoring Schema Typing in CSV / Parquet Reading: File read karte waqt agar aap automatic schema inference par chhor dete hain to text columns galat parse ho sakte hain. Production mein hamesha explicit `schema_overrides` provide karein.

Zero-GPU Tip:
Polars pure multi-threaded CPU engine hai jo Rust ke Rayon library par chalta hai. Agar aapke paas 8-core CPU laptop hai to Polars 8 cores par parallel data crunch karta hai. 50 lakh rows ka group-by aggregation sirf 200 milliseconds mein ho jata hai with zero GPU usage.

Self-Check Questions:
1. Row-based storage format (CSV) aur Columnar storage format (Arrow/Parquet) mein CPU cache locality ka kya farq hai?
2. Polars mein Lazy Evaluation aur Predicate Pushdown ka kya matlab hai?
3. Pandas ke muqablay Polars RAM consumption ko kaise aadha karta hai?

What to Build Next:
Ek Parquet Sanitizer Pipeline banayein jo ek raw CSV file ko read kare, null values ko mean/median se fill kare, outlier records ko filter kare, aur partitioned `.parquet` files mein export kare."""

# ==============================================================================
# LESSON 1.6: Module 1 Capstone: Enterprise Ingestion Engine
# ==============================================================================
LESSON_CONTENT['1.6'] = """### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne Module 1 ke tamam bunyadi aur advance mathematical sutoon (NumPy, Linear Algebra, Calculus, Memory Profiling, AsyncIO, aur Polars) mukammal kar liye hain. Ab waqt hai in tamam auzaar ko mila kar apna **Pehla Real-World Production Capstone** khara karne ka!
Is Capstone project ka zehni khaka samajhne ke liye kisi bare National Courier & Logistics Hub (Jaise TCS, Leopard, ya Pakistan Post) ki misaal lein:
1. Raw Incoming Stream (Unsorted Parcels): Rozana subah logistics hub mein 500,000 parcels trucks se utar kar conveyor belt par aate hain. Inme se kuch parcels phatay hue hote hain, kuch par pata galat likha hota hai, aur kuch par gandi mitti lagi hoti hai.
2. Sanitization & Normalization (Scanners & Washers): Belts par lage automatic laser scanners (Regex & Cleaners) fuzool stickers (HTML tags, tracking URLs, double spaces) ko remove karte hain aur Urdu/English mixed alphabets ko standard unicode format mein normalize karte hain.
3. Strict Schema Validation (Quality Control Gates): Har parcel ka wazan aur size check hota hai (Pydantic / Typed Schema). Agar kisi parcel ka wazan zero ya negative ho to use foran reject karke error bin mein phenk diya jata hai.
4. Tokenization & Partitioned Sinks (Container Loading): Akhir mein tamam saaf shuda parcels ko unke shehar aur size ke mutabiq 10,000-parcels ke partitioned containers (Parquet Chunks) mein seal kar diya jata hai taake aglay module mein AI models bina kisi rukawat ke in par train ho sakein.

Yeh capstone pipeline 500,000 dirty records ko handle karti hai aur production enterprise architectures ka benchmark hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein dekhte hain ke 500,000 records ke data pipeline mein RAM memory budget aur throughput ka hisab kaise lagaya jata hai.
Pipeline Specifications:
- Total raw records $N = 500,000$
- Average text length = 150 characters $\\approx$ 200 bytes per record.
- Total raw payload size $\\approx 500,000 \\times 200 \\text{ Bytes} = 100,000,000 \\text{ Bytes} \\approx 100 \\text{ MB}$.

Memory Budgeting Analysis:
Agar hum naive single-thread Python use karein jahan har line par string manipulations hon:
- Raw strings in memory: 100 MB
- Intermediate regex objects and string buffers: $\\approx 300 \\text{ MB}$
- Final python dictionary objects ($N \\times 150 \\text{ bytes}$ overhead): $\\approx 250 \\text{ MB}$
Peak RAM: $\\approx 650 \\text{ MB}$.
Agar data 500,000 ke bajaye 1 crore (10M) records ka ho to RAM requirement 13 GB cross kar jayegi aur system crash ho jayega.

Streaming Partitioning Approach:
Polars chunk streaming aur batching ke zariye:
- Chunk size = 50,000 records (10 MB per chunk).
- Worker threads = 4
- Maximum in-flight memory = $4 \\times 10 \\text{ MB} = 40 \\text{ MB}$.
- Peak RAM used: $< 80 \\text{ MB}$ constant throughout the entire run!

Throughput Calculation:
Agar 500,000 records ko process karne mein 5 seconds lagte hain:
$\\text{Throughput} = \\frac{500,000 \\text{ records}}{5.0 \\text{ seconds}} = 100,000 \\text{ records/sec}$
Is throughput par aap 1 billion records ko 2.7 ghantay mein sanitize kar sakte hain!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum end-to-end multi-threaded data ingestion, regex text sanitization, token length calculation, aur partitioned Parquet export ko implement karte hain.

```python
import os
import re
import tempfile
import time
import polars as pl
import numpy as np

# 1. High-Performance Text Normalizer using pre-compiled Regex
HTML_PATTERN = re.compile(r'<.*?>')
URL_PATTERN = re.compile(r'http[s]?://\\S+')
EXTRA_WHITESPACE_PATTERN = re.compile(r'\\s+')

def sanitize_urdu_english_text(raw_text: str) -> str:
    \"\"\"Sanitizes dirty customer feedback with robust regex normalization.\"\"\"
    if not isinstance(raw_text, str) or not raw_text:
        return ""
    # Strip HTML tags
    cleaned = HTML_PATTERN.sub('', raw_text)
    # Strip URLs
    cleaned = URL_PATTERN.sub('', cleaned)
    # Normalize multiple whitespace to single space
    cleaned = EXTRA_WHITESPACE_PATTERN.sub(' ', cleaned).strip()
    return cleaned

# 2. Synthetic Dirty Feed Generator (500,000 records)
TOTAL_RECORDS = 500_000
print(f"Generating {TOTAL_RECORDS:,} synthetic e-commerce review records...")

raw_comments = [
    "<b>Bohot umdah chai thi!</b> 100% recommended: https://dhaba.pk/order/1",
    "Delivery bohot late aayi... <br> lekin khana garam tha.",
    "Bila-wajah overcharge kiya gaya! Customer service bilkul bekaar hai.",
    "AI Ustaad course ne meri coding thinking transform kar di. Zabardast!",
    "Item received broken... contact us at support@store.com"
]

np.random.seed(42)
comments_column = np.random.choice(raw_comments, size=TOTAL_RECORDS)
user_ids_column = np.random.randint(1000, 99999, size=TOTAL_RECORDS)
ratings_column = np.random.choice([1.0, 2.0, 3.0, 4.0, 5.0], size=TOTAL_RECORDS, p=[0.05, 0.10, 0.15, 0.35, 0.35])

# Ingest into Polars DataFrame
raw_df = pl.DataFrame({
    "review_id": np.arange(TOTAL_RECORDS, dtype=np.int64),
    "user_id": user_ids_column,
    "rating": ratings_column,
    "raw_comment": comments_column
})

# 3. Production Sanitization & Feature Engineering Pipeline
t0 = time.perf_counter()

sanitized_df = (
    raw_df.lazy()
    # Map sanitization function across series elements
    .with_columns(
        pl.col("raw_comment")
        .map_elements(sanitize_urdu_english_text, return_dtype=pl.Utf8)
        .alias("clean_comment")
    )
    # Compute token length heuristics (character length and approximate word count)
    .with_columns([
        pl.col("clean_comment").str.len_chars().alias("char_count"),
        pl.col("clean_comment").str.split(" ").list.len().alias("approx_token_count")
    ])
    # Filter out empty or trivially short comments
    .filter(pl.col("char_count") > 5)
    .collect()
)

elapsed_sec = time.perf_counter() - t0
print(f"Sanitization of {TOTAL_RECORDS:,} records completed in {elapsed_sec:.3f} seconds!")
print(f"Pipeline Processing Throughput: {TOTAL_RECORDS / elapsed_sec:,.0f} records/second")

# 4. Export to Partitioned Parquet Chunks
with tempfile.TemporaryDirectory() as tmp_dir:
    output_parquet = os.path.join(tmp_dir, "sanitized_corpus.parquet")
    sanitized_df.write_parquet(output_parquet, compression="snappy")
    file_size_mb = os.path.getsize(output_parquet) / (1024 * 1024)
    print(f"Successfully serialized to Snappy Parquet: {output_parquet} ({file_size_mb:.2f} MB)")
    
    # Verify by reading top 3 rows
    verification_df = pl.read_parquet(output_parquet).head(3)
    print("\\nVerification Sample:")
    print(verification_df[["review_id", "rating", "clean_comment", "approx_token_count"]])
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Compiling Regex Inside the Function Loop: Function ke andar har baar `re.compile(pattern)` call karne se har record par regex parser dobara chalta hai. Hamesha module level par patterns ko compile karke global constants banayein.
2. In-Memory Pandas Export to CSV: 500,000 records ko CSV format mein export karna bohot slow hota hai aur disk space 5x zyada leta hai. Hamesha Snappy compressed Parquet format use karein.
3. Unvalidated Division When Computing Token Averages: Dataset mein agar filter lagane ke baad zero records bach jayein to average nikalte waqt `ZeroDivisionError` aa sakta hai. Hamesha denominator ko validate karein.

Zero-GPU Tip:
Text sanitization, regex stripping, aur Parquet encoding 100% CPU bound operations hain. Inke liye GPU ki koi zaroorat nahi hoti. Multi-core modern CPU par Polars ki SIMD multi-threading kisi bhi basic GPU se zyada tezi se text sanitize karti hai.

Self-Check Questions:
1. Regex compilation ko function ke bahar rakhne se performance par kya asar parta hai?
2. Snappy-compressed Parquet format plain CSV ke muqablay disk space aur read speed mein kyun behtar hai?
3. Data ingestion pipeline mein character count aur word count ke metrics embeddings generation ke liye kyun ahem hain?

What to Build Next:
Is Capstone pipeline ko extend karein taake yeh 10 alag alag partitioned Parquet files generate kare, har partition ka metadata JSON file mein save kare, aur memory usage ko `tracemalloc` se log kare."""
