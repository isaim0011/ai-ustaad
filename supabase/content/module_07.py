# module_07.py
# Module 7: Vector Databases & Modern RAG Architecture (ColPali)
# Lessons 7.1 to 7.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 7.1: Vector Embeddings & Indexing: HNSW, IVFFlat & pgvector
# ==============================================================================
LESSON_CONTENT['7.1'] = r"""### Part 1: Mental Model & South Asian Analogy
Vector Databases modern Retrieval-Augmented Generation (RAG) ka markazi engine hain. Lekin jab aapke database mein 10 lakh ya 1 crore vectors aa jate hain, to har user query par poore database ke har akele vector ke sath cosine distance calculate karna ($O(N)$ Flat Scan) computer ko choke kar deta hai. Yahan Approximate Nearest Neighbor (ANN) Indexing algorithms (HNSW aur IVFFlat) kaam aate hain.
Isay samajhne ke liye kisi Shehar ke Highway System aur Mohallay ki Galliyon ki misaal lein:
1. Flat Scan (Bila Indexing Ke Har Ghar Ka Darwaza Khatkhatana): Farz karein aapko Karachi mein "Aslam Bhai" ka ghar dhoondna hai. Flat scan yeh hai ke aap Kemari se shuru ho kar Malir tak har ek ghar ka darwaza khatkhatayein aur poochein: "Kya aap Aslam bhai hain?" Poora shehar ghoomne mein saal lag jayenge ($O(N)$ Exact Scan).
2. IVFFlat (Inverted File Index - Shehar Ke Daak-Khane / Postal Codes): IVFFlat shehar ko 100 clusters (Voronoi Cells) mein baant deta hai. Jab aap query dete hain, to algorithm pehle sirf 100 cluster centroids ko check karta hai: "Yeh banda kis ilaqay ka lagta hai? Saddar ka!" Phir woh sirf Saddar ke cluster ke andar dhoondta hai aur baqi 99 ilaqon ko chhoota bhi nahi. Speed 10x tez ho jati hai, lekin thodi si recall accuracy compromise hoti hai.
3. HNSW (Hierarchical Navigable Small World - Express Highway Network): HNSW 2026 ka sab se taqatwar vector index hai. Yeh multi-layer express highways banata hai:
   - Layer 2 (Super Highway): Lambi lambi chhalangein (Islamabad to Lahore to Karachi). Algorithm 2 qadam mein sahi geographic region mein pohnch jata hai.
   - Layer 1 (City Boulevard): Shahrah-e-Faisal par utar kar ilaqay ke qareeb pohnchta hai.
   - Layer 0 (Local Street Network): Galiyon mein chal kar seedha Aslam bhai ke darwazay par ungli rakh deta hai!
   HNSW $O(\log N)$ logarithmic time mein 10 lakh vectors mein se 99% accuracy ke sath top matches nikal leta hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein IVFFlat Cluster Assignment aur HNSW Graph Navigation ki step-by-step calculation trace karte hain.
Setup for IVFFlat Cluster Lookup:
Query Vector $Q = [0.85, 0.45]$ (Normalized 2D embedding).
Pre-computed Cluster Centroids (K-Means Centroids):
- Centroid $C_0 = [0.10, 0.95]$ (Cluster 0)
- Centroid $C_1 = [0.80, 0.50]$ (Cluster 1)
- Centroid $C_2 = [-0.70, 0.30]$ (Cluster 2)

Step 1: Compute Distance to Centroids via Squared Euclidean Distance:
$d^2(Q, C) = (Q_0 - C_0)^2 + (Q_1 - C_1)^2$
Distance to $C_0$:
$d^2(Q, C_0) = (0.85 - 0.10)^2 + (0.45 - 0.95)^2 = (0.75)^2 + (-0.50)^2 = 0.5625 + 0.2500 = 0.8125$

Distance to $C_1$:
$d^2(Q, C_1) = (0.85 - 0.80)^2 + (0.45 - 0.50)^2 = (0.05)^2 + (-0.05)^2 = 0.0025 + 0.0025 = 0.0050$

Distance to $C_2$:
$d^2(Q, C_2) = (0.85 - (-0.70))^2 + (0.45 - 0.30)^2 = (1.55)^2 + (0.15)^2 = 2.4025 + 0.0225 = 2.4250$

Step 2: Probe Closest Centroid (`nprobe=1`)
Min distance is $C_1$ ($0.0050$).
IVFFlat algorithm baqi tamam clusters (0 aur 2) ke lakhon vectors ko discard kar deta hai aur sirf Cluster 1 ki inverted list ke andar vectors ko scan karta hai!
Search scope: 1,000,000 vectors se kam hokar sirf 10,000 vectors reh gaya ($100\times \text{ Computation Reduction}$)!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum pure Python/NumPy ke sath Hierarchical Small World (HNSW) greedy graph traversal algorithm aur Voronoi cell cluster routing logic implement karte hain.

```python
import numpy as np
from typing import Dict, List, Tuple

class SimpleHNSWGraph:
    \"\"\"Simulates multi-layer navigable small world vector graph traversal.\"\"\"
    def __init__(self) -> None:
        # Layer 1: Sparse long-range highways; Layer 0: Dense local neighborhood
        self.vectors: Dict[int, np.ndarray] = {}
        self.layer1_edges: Dict[int, List[int]] = {}
        self.layer0_edges: Dict[int, List[int]] = {}
        self.entry_point_id: int = 0

    def add_node(self, node_id: int, vec: np.ndarray, is_highway: bool = False) -> None:
        self.vectors[node_id] = vec / np.linalg.norm(vec)
        self.layer0_edges[node_id] = []
        if is_highway:
            self.layer1_edges[node_id] = []

    def connect_edge(self, u: int, v: int, layer: int) -> None:
        if layer == 1 and u in self.layer1_edges and v in self.layer1_edges:
            self.layer1_edges[u].append(v)
            self.layer1_edges[v].append(u)
        elif layer == 0:
            self.layer0_edges[u].append(v)
            self.layer0_edges[v].append(u)

    def greedy_search_layer(self, query: np.ndarray, curr_node: int, edges: Dict[int, List[int]]) -> int:
        \"\"\"Greedily moves to neighbor with highest cosine similarity.\"\"\"
        best_node = curr_node
        best_sim = float(np.dot(query, self.vectors[curr_node]))

        while True:
            improved = False
            for neighbor in edges.get(best_node, []):
                sim = float(np.dot(query, self.vectors[neighbor]))
                if sim > best_sim:
                    best_sim = sim
                    best_node = neighbor
                    improved = True
            if not improved:
                break
        return best_node

    def search(self, query_vec: np.ndarray) -> Tuple[int, float]:
        q_norm = query_vec / np.linalg.norm(query_vec)
        # Step 1: Long-range navigation on Layer 1 Highway
        curr = self.greedy_search_layer(q_norm, self.entry_point_id, self.layer1_edges)
        # Step 2: Fine-grained neighborhood search on Layer 0
        final_node = self.greedy_search_layer(q_norm, curr, self.layer0_edges)
        score = float(np.dot(q_norm, self.vectors[final_node]))
        return final_node, score

# Execution test
if __name__ == "__main__":
    hnsw = SimpleHNSWGraph()
    # Add nodes: 0 (Highway entrance), 1 (Regional node), 2 (Local target match)
    hnsw.add_node(0, np.array([0.1, 0.9]), is_highway=True)
    hnsw.add_node(1, np.array([0.7, 0.6]), is_highway=True)
    hnsw.add_node(2, np.array([0.9, 0.3]), is_highway=False)

    hnsw.connect_edge(0, 1, layer=1)
    hnsw.connect_edge(1, 2, layer=0)
    hnsw.connect_edge(0, 1, layer=0)

    # Search for vector close to Node 2 [0.95, 0.25]
    query = np.array([0.95, 0.25])
    matched_id, similarity = hnsw.search(query)
    print(f"HNSW Search Completed!")
    print(f"Matched Node ID:   {matched_id} (Expected target: Node 2)")
    print(f"Cosine Similarity: {similarity:.4f}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Using IVFFlat on an Untrained Small Dataset: IVFFlat ko chalane ke liye pehle K-Means clustering train karni parti hai. Agar dataset mein sirf 5,000 vectors hon to IVFFlat banane ka koi faida nahi hai; standard HNSW ya Flat scan kahin zyada fast aur accurate rehta hai.
2. Building HNSW Index with Insufficient Construction Parameters ($M$ and $efConstruction$): HNSW mein agar $M=8$ (kam edges) rakha jaye to graph disconnect ho sakta hai aur recall 70% par gir jati hai. Production mein hamesha $M=32$ ya $64$ aur $efConstruction=128$ rakhein.
3. Unindexed pgvector Tables: Supabase / PostgreSQL mein `vector(1536)` column banane ke baad aksar log `CREATE INDEX ON items USING hnsw (embedding vector_cosine_ops);` chalana bhool jate hain, jisse database poori table ko sequential scan karta hai aur server crash ho jata hai.

Zero-GPU Tip:
Vector index build karna aur graph search karna 100% CPU aur RAM bound operation hai. PostgreSQL pgvector extension ya Faiss library CPU par multi-threaded HNSW chala kar 10 lakh embeddings ko 3 milliseconds mein search karti hai.

Self-Check Questions:
1. Flat Scan, IVFFlat, aur HNSW mein time complexity aur memory overhead ka kya farq hai?
2. PostgreSQL pgvector mein HNSW index create karne ki basic SQL command kya hoti hai?
3. HNSW graph traversal mein 'Small World' network theory ka kya matlab hai?

What to Build Next:
Ek Supabase SQL Migration script likhein jo `documents` table banaye with `vector(1536)` column, us par HNSW index lagaye, aur match threshold ke sath Cosine Similarity RPC function define kare."""

# ==============================================================================
# LESSON 7.2: Advanced RAG: Hybrid Search & Cross-Encoder Re-Ranking
# ==============================================================================
LESSON_CONTENT['7.2'] = r"""### Part 1: Mental Model & South Asian Analogy
Aam naive RAG mein sab se bara flaw yeh hota hai ke dense vector embeddings keyword-specific queries (jaise Product SKU codes, phone numbers, ya legal section numbers) par fail ho jati hain. Yahan kaam aata hai **Hybrid Search (BM25 + Dense Vectors) aur Cross-Encoder Re-Ranking**!
Isay samajhne ke liye kisi Adalat ke Munshi aur Senior Judge ki misaal lein:
1. Dense Vector Search (Falsafiyana Talash): Vector search yeh samajhti hai ke "Ghar ki khareedo farokht" aur "Property agreement" aapas mein milti julti baatein hain (Semantic Match). Lekin agar user search kare "Section 302-B Act 1860", to vector search confuse ho jati hai kyunke uske liye 302 sirf ek number hai.
2. BM25 Lexical Search (Harf-ba-Harf Talash): BM25 purana traditional search engine hai (TF-IDF standard). Yeh lafz-ba-lafz exact match dhoondta hai: "Section", "302-B", "Act". Exact keywords ke liye yeh behtareen hai.
3. Hybrid Search & Reciprocal Rank Fusion (RRF): RRF dono dukanon ke natayej ko aapas mein mila deta hai: "Top 20 results BM25 se uthao aur Top 20 results Vector Search se uthao."
4. Cross-Encoder Re-Ranker (Senior Judge Ki Teesri Nazar): Bi-Encoder embeddings query aur document ko alag alag vector banati hain. Cross-Encoder dono ko ek sath jod kar (`[CLS] Query [SEP] Document [SEP]`) transformer ke andar daalta hai aur har token ka doosre token ke sath full cross-attention karta hai! Top 40 mein se sirf wahi 3 documents nikalte hain jo 100% sawal ka jawab dete hain.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Reciprocal Rank Fusion (RRF) ka exact mathematical formula trace karte hain.
Formula for RRF Score of Document $d$:
$\text{RRF}(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$
Jahan:
- $M$: Retrieval methods (Dense Vector + BM25 Lexical)
- $r_m(d)$: Document $d$ ka rank us method ke nateeje mein (1-indexed: 1, 2, 3...)
- $k$: Smoothing constant (Standard default $k = 60$)

Candidate Document: Doc A ("Section 302-B Penal Code")
Retrieval Results:
- In BM25 Keyword Search: Doc A came at Rank 1 ($r_{\text{BM25}} = 1$)
- In Dense Vector Search: Doc A came at Rank 8 ($r_{\text{Dense}} = 8$)

Step 1: Compute RRF Score for Doc A
$\text{RRF}(\text{Doc A}) = \frac{1}{60 + 1} + \frac{1}{60 + 8} = \frac{1}{61} + \frac{1}{68}$
$\frac{1}{61} \approx 0.016393$
$\frac{1}{68} \approx 0.014706$
$\text{RRF}(\text{Doc A}) = 0.016393 + 0.014706 = 0.031099$

Compare with Doc B:
- BM25 Rank: 15 ($r_{\text{BM25}} = 15$)
- Dense Rank: 2 ($r_{\text{Dense}} = 2$)
$\text{RRF}(\text{Doc B}) = \frac{1}{60 + 15} + \frac{1}{60 + 2} = \frac{1}{75} + \frac{1}{62} \approx 0.013333 + 0.016129 = 0.029462$

Comparison:
$\text{RRF}(\text{Doc A}) = 0.0311 > \text{RRF}(\text{Doc B}) = 0.0295$.
Doc A ko top rank milta hai kyunke usne dono systems mein high visibility achieve ki! RRF bina kisi arbitrary normalization score ke dono alag systems ko perfectly fuse karta hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Reciprocal Rank Fusion (RRF) merger aur Cross-Encoder re-ranking pipeline implement karte hain.

```python
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass(slots=True)
class SearchHit:
    doc_id: str
    content: str
    raw_score: float

def reciprocal_rank_fusion(
    dense_results: List[SearchHit], 
    lexical_results: List[SearchHit], 
    k: int = 60
) -> List[Tuple[str, float]]:
    \"\"\"Combines dense vector and BM25 lexical rankings using Reciprocal Rank Fusion.\"\"\"
    rrf_scores: Dict[str, float] = {}

    # Accumulate dense ranks
    for rank, hit in enumerate(dense_results, 1):
        rrf_scores[hit.doc_id] = rrf_scores.get(hit.doc_id, 0.0) + (1.0 / (k + rank))

    # Accumulate lexical ranks
    for rank, hit in enumerate(lexical_results, 1):
        rrf_scores[hit.doc_id] = rrf_scores.get(hit.doc_id, 0.0) + (1.0 / (k + rank))

    # Sort descending by fused RRF score
    sorted_ranked = sorted(rrf_scores.items(), key=lambda item: item[1], reverse=True)
    return sorted_ranked

def mock_cross_encoder_rerank(
    query: str, 
    candidate_docs: List[SearchHit], 
    top_n: int = 2
) -> List[Tuple[SearchHit, float]]:
    \"\"\"Simulates cross-encoder (e.g. bge-reranker-large) full self-attention re-scoring.\"\"\"
    scored_candidates = []
    q_words = set(query.lower().split())

    for doc in candidate_docs:
        d_words = set(doc.content.lower().split())
        # Simulated semantic relevance interaction
        overlap = len(q_words.intersection(d_words))
        cross_attention_score = round(0.4 + (0.2 * overlap), 4)
        scored_candidates.append((doc, cross_attention_score))

    # Sort descending by re-ranker score
    scored_candidates.sort(key=lambda x: x[1], reverse=True)
    return scored_candidates[:top_n]

# Execution test
if __name__ == "__main__":
    dense_hits = [
        SearchHit("doc_1", "Criminal legal procedures under penal code", 0.88),
        SearchHit("doc_2", "Civil contract dispute resolution rules", 0.75)
    ]
    lexical_hits = [
        SearchHit("doc_3", "Specific section 302-B criminal penalties", 14.5),
        SearchHit("doc_1", "Criminal legal procedures under penal code", 8.2)
    ]

    fused = reciprocal_rank_fusion(dense_hits, lexical_hits)
    print("Top RRF Fused Results:")
    for doc_id, score in fused:
        print(f"  {doc_id} -> RRF Score: {score:.6f}")

    reranked = mock_cross_encoder_rerank("penal code criminal", dense_hits + lexical_hits, top_n=2)
    print("\\nFinal Cross-Encoder Re-Ranked Top 2:")
    for hit, score in reranked:
        print(f"  {hit.doc_id}: '{hit.content}' -> Re-Ranker Score: {score:.4f}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Normalizing Raw Vector Scores with BM25 Scores Directly: Vector scores $[0, 1]$ cosine range mein hote hain jabke BM25 scores $[0, 50]$ unbounded range mein hote hain. Inhe direct add karna BM25 ko 100% haawi kar deta hai. Hamesha Reciprocal Rank Fusion (RRF) use karein jo raw scores ke bajaye ranks use karta hai.
2. Running Cross-Encoder on All 10,000 Documents: Cross-Encoder computationally bohot heavy ($O(S^2)$ full attention) hota hai. Ise poore database par chalana latency ko 30 seconds tak phenk deta hai. Pehle Hybrid Search se top 30 candidates nikalein, phir sirf un 30 par Cross-Encoder chalayein.
3. Ignoring Chunk Metadata in Search: Chunks ke sath document title, author, aur date metadata filter na lagane se purana outdated record top result ban sakta hai. Hamesha metadata filtering support karein.

Zero-GPU Tip:
Reciprocal Rank Fusion (RRF) aur BM25 search pure CPU par execute hoti hain. Chote cross-encoder models (jaise `bge-reranker-base` via ONNX runtime) CPU par 30 documents ko sirf 40 milliseconds mein re-rank kar dete hain.

Self-Check Questions:
1. Dense Vector search aur BM25 Lexical search ki taqatein aur kamzoriyan kya hain?
2. Reciprocal Rank Fusion (RRF) raw similarity scores ke bajaye ranks par kyun inhisar karta hai?
3. Bi-Encoder (Embedding) aur Cross-Encoder (Re-Ranker) mein computational architecture ka kya farq hai?

What to Build Next:
Ek Hybrid Search Engine banayein jo SQLite FTS5 (Full-Text Search) aur In-Memory Cosine Similarity dono se top-10 results fetch kare aur RRF algorithm se merge karke print kare."""

# ==============================================================================
# LESSON 7.3: 2026 SOTA: ColPali Vision-Language Multi-Vector RAG
# ==============================================================================
LESSON_CONTENT['7.3'] = r"""### Part 1: Mental Model & South Asian Analogy
Traditional RAG pipelines complex documents (jaise Balance Sheets, Medical Invoices, Tables, aur Architecture Diagrams) par buri tarah fail ho jati hain kyunke PDF ko text parser se guzarne par table ke columns bikhar jate hain aur graphs ka data gayab ho jata hai. 2026 mein is maslay ka SOTA inqilab hai: **ColPali (Vision-Language Multi-Vector Late Interaction RAG)**!
Isay samajhne ke liye kisi Adalati Dastawaiz aur Aankhon wale Munshi ki misaal lein:
1. Traditional OCR-Based RAG (Andha Typist): Andha typist complex tax invoice ko aawaz sun kar type karta hai. Table ke headers kisi aur line par chale jate hain aur numbers doosri line par. Jab model se pucha jaye "Company ka Q3 Profit kya tha?", to numbers aage peeche hone ki wajah se model hallucinate karne lagta hai.
2. ColPali (Aankhon Wala Shaheen): ColPali document ka text extract nahi karta! Woh poore document page ko ek Tasweer (Image) ke taur par dekhta hai (Using Vision LLM like PaliGemma).
3. Late-Interaction Multi-Vector Patching (Har Hisso Ka Apna Vector): Aam model poore safhay ka sirf ek akela embedding vector banata hai (Compressed summary). ColPali safhay ke har chotay hissay (Patch: table cell, chart bar, header) ke liye alag alag vector banata hai (1024 vectors per page).
4. MaxSim Operator: Jab user query aati hai ("Q3 Operating Margin?"), to query ka har token document image ke sab se mutaliqa patch ke sath direct late-interaction dot product karta hai! Agar page par kisi table ke chotay se konay mein number likha ho to ColPali use seedha pakar leta hai bina kisi OCR text extraction ke!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein ColPali ke core mathematical operator **MaxSim (Maximum Similarity Late Interaction)** ka hisab trace karte hain.
ColBERT aur ColPali late interaction ka formula:
$\text{Score}(Q, D) = \sum_{i=1}^{|Q|} \max_{j=1}^{|D|} (q_i \cdot d_j)$
Jahan:
- $Q$: Query tokens ke multi-vector embeddings $[|Q|, D_{\text{dim}}]$
- $D$: Document image patches ke multi-vector embeddings $[|D|, D_{\text{dim}}]$
- Har query token $q_i$ document ke tamam patch vectors $d_j$ ke sath dot product karta hai aur sab se bara (maximum) match uthata hai.
- Final relevance score tamam maximum matches ka sum hota hai.

Toy Worked Setup:
Query has 2 tokens ($q_1, q_2$).
Document Image has 3 visual patch vectors ($d_1, d_2, d_3$).
Normalized Embeddings:
- $q_1$ = $[1.0, 0.0]$ ("revenue")
- $q_2$ = $[0.0, 1.0]$ ("profit")

Document Page Patches:
- $d_1$ = $[0.9, 0.1]$ (Patch 1: Document Header text)
- $d_2$ = $[0.1, 0.9]$ (Patch 2: Table Financial Row)
- $d_3$ = $[0.0, 0.0]$ (Patch 3: Blank White Space)

Step 1: Compute Dot Products for $q_1$ ("revenue"):
- $q_1 \cdot d_1 = (1.0 \times 0.9) + (0.0 \times 0.1) = 0.90$
- $q_1 \cdot d_2 = (1.0 \times 0.1) + (0.0 \times 0.9) = 0.10$
- $q_1 \cdot d_3 = 0.00$
Max Similarity for $q_1$: $\max(0.90, 0.10, 0.00) = 0.90$ (Matched with Header Patch $d_1$)

Step 2: Compute Dot Products for $q_2$ ("profit"):
- $q_2 \cdot d_1 = (0.0 \times 0.9) + (1.0 \times 0.1) = 0.10$
- $q_2 \cdot d_2 = (0.0 \times 0.1) + (1.0 \times 0.9) = 0.90$
- $q_2 \cdot d_3 = 0.00$
Max Similarity for $q_2$: $\max(0.10, 0.90, 0.00) = 0.90$ (Matched with Table Row Patch $d_2$)

Step 3: Sum of Maximum Similarities (MaxSim Score)
$\text{Score}(Q, D) = 0.90 + 0.90 = 1.8000$
Har token ne document image ke exact relevant patch se match kiya. Zero OCR information loss!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum MaxSim late interaction scoring operator aur multi-vector retrieval pipeline from scratch implement karte hain.

```python
import numpy as np

def compute_maxsim_score(query_embeddings: np.ndarray, doc_patch_embeddings: np.ndarray) -> float:
    \"\"\"Computes ColPali / ColBERT late-interaction MaxSim score.
    
    Shapes:
      query_embeddings:     [num_query_tokens, embed_dim]
      doc_patch_embeddings: [num_doc_patches, embed_dim]
    Returns:
      scalar_relevance_score
    \"\"\"
    # Input assertions
    assert query_embeddings.ndim == 2 and doc_patch_embeddings.ndim == 2
    assert query_embeddings.shape[1] == doc_patch_embeddings.shape[1]

    # Normalize vectors to unit sphere for pure cosine dot products
    q_norm = query_embeddings / np.maximum(np.linalg.norm(query_embeddings, axis=1, keepdims=True), 1e-9)
    d_norm = doc_patch_embeddings / np.maximum(np.linalg.norm(doc_patch_embeddings, axis=1, keepdims=True), 1e-9)

    # 1. Compute Pairwise Cross-Attention Dot Product Matrix
    # Shape: [num_query_tokens, num_doc_patches]
    similarity_matrix = np.matmul(q_norm, d_norm.T)

    # 2. For each query token, take the maximum match across all document visual patches
    max_similarities_per_token = np.max(similarity_matrix, axis=1)  # Shape: [num_query_tokens]

    # 3. Sum of maximum similarities represents total sequence alignment score
    total_maxsim_score = float(np.sum(max_similarities_per_token))
    return total_maxsim_score

# Execution test
if __name__ == "__main__":
    np.random.seed(42)
    dim = 64
    n_query_tokens = 4   # E.g. "Q3", "net", "revenue", "margin"
    n_doc_patches = 128  # 128 visual patches on rendered PDF page

    # Query embeddings
    Q = np.random.randn(n_query_tokens, dim).astype(np.float32)
    
    # Document Page 1: Matches query well on patches 10-15
    D_page1 = np.random.randn(n_doc_patches, dim).astype(np.float32)
    D_page1[10:14] = Q + np.random.normal(0.0, 0.1, (n_query_tokens, dim))

    # Document Page 2: Random unrelated page
    D_page2 = np.random.randn(n_doc_patches, dim).astype(np.float32)

    score_page1 = compute_maxsim_score(Q, D_page1)
    score_page2 = compute_maxsim_score(Q, D_page2)

    print(f"ColPali Multi-Vector MaxSim Execution:")
    print(f"  Page 1 (Target Financial Table): MaxSim Score = {score_page1:.4f}")
    print(f"  Page 2 (Unrelated Text Page):    MaxSim Score = {score_page2:.4f}")
    print(f"Discrimination Delta: {(score_page1 - score_page2):.4f} (High confidence visual match!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. High Storage Footprint of Multi-Vector Embeddings: Single-vector RAG har page ke liye 1 vector store karta hai, jabke ColPali 1024 vectors per page store karta hai. 10,000 pages ke liye yeh 10GB se zyada memory ban sakta hai. Production mein hamesha Scalar Quantization ya Residual Codebook compression use karein.
2. Flattening Multi-Vectors into Single Average Vector: ColPali vectors ka mean nikal kar single vector banana late-interaction ke tamam faiday khatam kar deta hai. MaxSim operator ko preserve karna lazmi hai.
3. Feeding Low-Resolution PDF Renders: Agar PDF ko low DPI (jaise 72 DPI) par render kiya jaye to chotay numbers aur table borders blur ho jate hain. Hamesha minimum 150 ya 200 DPI par render karein.

Zero-GPU Tip:
MaxSim matrix multiplication NumPy ya PyTorch CPU par matrix operations ke zariye chund milliseconds mein evaluate ho jati hai. Multi-vector ranking ko verify karne ke liye local CPU par synthetic patches se test karein.

Self-Check Questions:
1. ColPali traditional OCR-based RAG pipelines ke muqablay visual tables aur charts ko kaise behtar samajhta hai?
2. MaxSim operator late-interaction matching kaise execute karta hai?
3. Single dense embedding ke muqablay multi-vector embeddings ka trade-off kya hai?

What to Build Next:
Ek Visual RAG Evaluator banayein jo ek sample invoice image ke patches simulate kare, user query ke sath MaxSim calculate kare, aur sab se zyada match hone wale patch ke coordinates heatmap par highlight kare."""

# ==============================================================================
# LESSON 7.4: Advanced Document Parsing & Semantic Chunking
# ==============================================================================
LESSON_CONTENT['7.4'] = r"""### Part 1: Mental Model & South Asian Analogy
RAG systems mein hallucination aur irrelevant context ka 70% sabab ghalat chunking hoti hai. Aam tor par log text ko 500 characters ke fixed blocks mein kaat dete hain (Fixed-Length Chunking). Nateeja yeh nikalta hai ke jumla beech mein se kat jata hai aur maani bikhar jata hai.
Isay samajhne ke liye kisi Kapray ke Thaam aur Darzi ki Kainchi ki misaal lein:
1. Fixed Character Chunking (Andha Darzi): Andha darzi aankhein band karke har 2 foot par kainchi chala deta hai. Nateeja: Ek suit ka gala doosre tukray mein chala jata hai aur baazu teesre tukray mein (Context Severing). Jab model tukra padhta hai to use samajh nahi aati ke baat kahan se shuru hui thi.
2. Semantic Chunking (Hoshiyar Master Ji): Master ji pehle poore thaan ko dekhte hain jahan design badalta hai. Woh har do jumlon ke darmiyan Semantic Distance (Embedding difference) measure karte hain. Jab tak baat ek hi mozu par chal rahi ho, woh tukra nahi kaat-te. Jaise hi naya mozu shuru hota hai (Semantic Shift / Distance Spike), wahan se naya chunk shuru hota hai!
3. Hierarchical / Parent-Child Chunking: Badi kitaab ke liye pehle baray 2,000-token ke Parent Chunks banaye jate hain aur unke andar 300-token ke chotay Child Chunks hote hain. Search chotay child chunk par hoti hai (Precise retrieval), lekin model ko pura parent chunk context ke taur par diya jata hai (Rich comprehensive reasoning).

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Semantic Chunking ke Cosine Distance Thresholding ka exact hisab lagayein.
Algorithm:
1. Text ko individual sentences mein split karein: $S_0, S_1, S_2, S_3$.
2. Har sentence ka embedding vector nikalein: $E_0, E_1, E_2, E_3$.
3. Adjacent sentences ke darmiyan Cosine Distance calculate karein:
   $D_i = 1 - \cos(E_i, E_{i+1})$
4. Agar Distance $D_i > \text{Threshold}$ (e.g. 0.40) ho, to wahan Chunk Split lagayein!

Worked Scenario:
Sentence 0: "Karachi biryani mein aaloo lazmi dala jata hai."
Sentence 1: "Bina aaloo ke biryani Karachi walon ko pasand nahi aati."
Sentence 2: "PyTorch 2.0 mein torch.compile compiler speedup deta hai."
Sentence 3: "Compiler Triton kernels generate karta hai."

Adjacent Distances:
- Between $S_0$ and $S_1$ (Same food topic):
  $\cos(E_0, E_1) = 0.88 \implies D_0 = 1 - 0.88 = 0.1200$ (Low distance, keep together)
- Between $S_1$ and $S_2$ (Topic jumps from food to deep learning!):
  $\cos(E_1, E_2) = 0.15 \implies D_1 = 1 - 0.15 = 0.8500$ (Massive distance spike!)
- Between $S_2$ and $S_3$ (Same PyTorch topic):
  $\cos(E_2, E_3) = 0.82 \implies D_2 = 1 - 0.82 = 0.1800$ (Low distance, keep together)

Threshold Evaluation ($\tau = 0.40$):
$D_1 = 0.85 > 0.40 \implies$ Split trigger at index 1!
Resulting Chunks:
- Chunk 1: $[S_0, S_1]$ ("Karachi biryani topic")
- Chunk 2: $[S_2, S_3]$ ("PyTorch compiler topic")
Zero context fragmentation, har chunk ek coherent mozu par mukammal rehta hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Semantic Chunking Engine implement karte hain: sentence boundary extraction, adjacent cosine distance calculation, percentile threshold detection, aur coherent chunk assembly.

```python
import re
import numpy as np
from typing import List

class SemanticChunker:
    \"\"\"Splits documents into coherent semantic chunks based on embedding distance spikes.\"\"\"
    def __init__(self, distance_threshold: float = 0.45) -> None:
        self.distance_threshold = distance_threshold

    @staticmethod
    def split_sentences(text: str) -> List[str]:
        # Split on sentence boundaries (period, exclamation, question mark)
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        return [s.strip() for s in sentences if len(s.strip()) > 5]

    def mock_sentence_embed(self, sentence: str) -> np.ndarray:
        \"\"\"Simulates embeddings reflecting semantic topic clustering.\"\"\"
        s_lower = sentence.lower()
        if any(w in s_lower for w in ["chai", "paratha", "biryani", "khana"]):
            base = np.array([0.9, 0.2, 0.0])
        elif any(w in s_lower for w in ["pytorch", "model", "tensor", "gpu"]):
            base = np.array([0.0, 0.1, 0.95])
        else:
            base = np.array([0.4, 0.4, 0.4])
        # Add slight noise and normalize
        vec = base + np.random.normal(0, 0.02, 3)
        return vec / np.linalg.norm(vec)

    def chunk_text(self, document_text: str) -> List[str]:
        sentences = self.split_sentences(document_text)
        if len(sentences) <= 1:
            return sentences

        embeddings = [self.mock_sentence_embed(s) for s in sentences]
        chunks: List[str] = []
        current_chunk_sentences: List[str] = [sentences[0]]

        for i in range(len(sentences) - 1):
            # Compute cosine distance
            cos_sim = float(np.dot(embeddings[i], embeddings[i + 1]))
            cos_dist = 1.0 - cos_sim

            if cos_dist > self.distance_threshold:
                # Semantic boundary detected: seal current chunk and start new one
                chunks.append(" ".join(current_chunk_sentences))
                current_chunk_sentences = [sentences[i + 1]]
            else:
                current_chunk_sentences.append(sentences[i + 1])

        if current_chunk_sentences:
            chunks.append(" ".join(current_chunk_sentences))

        return chunks

# Execution test
if __name__ == "__main__":
    np.random.seed(42)
    sample_doc = (
        "Karachi ki biryani mein aaloo daalna riwayati hissa hai. "
        "Lachha paratha aur doodh patti subah ka behtareen nashta hain. "
        "PyTorch autograd dynamic computational graphs compile karta hai. "
        "Triton kernels GPU memory bandwidth ko 2x boost karti hain."
    )

    chunker = SemanticChunker(distance_threshold=0.40)
    result_chunks = chunker.chunk_text(sample_doc)

    print(f"Total Sentences: 4 -> Resulting Semantic Chunks: {len(result_chunks)}")
    for idx, c in enumerate(result_chunks, 1):
        print(f"\\nChunk {idx}:\\n  '{c}'")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Fixed-Size Chunking Cutting Entities in Half: Sentence ke darmiyan chunk cut hone se "Ali ne 500 rupaye Aslam ko diye" do hisson mein toot jata hai: Chunk A: "Ali ne 500", Chunk B: "rupaye Aslam ko diye". Model dono chunks ko parh kar transactions miss kar deta hai. Hamesha boundary-aware chunking karein.
2. Zero Overlap Between Chunks: Agar chunks mein 10-20% overlap na ho to boundary par maujood concepts context kho dete hain. Fixed chunking mein hamesha `chunk_overlap=50` rakhein.
3. Over-Chunking into Micro-Sentences: Har akele jumlay ko alag chunk banane se context window itni fragmented ho jati hai ke retrieval system noise se bhar jata hai.

Zero-GPU Tip:
Sentence boundary splitting aur adjacent cosine distance checking CPU par microseconds mein chalti hai. Chote fast embedding models (jaise all-MiniLM-L6-v2) CPU par 10,000 sentences ko 1 second mein chunk kar dete hain.

Self-Check Questions:
1. Fixed-size chunking aur Semantic chunking mein kya farq hota hai?
2. Adjacent sentence cosine distance spike ka semantic matlab kya hota hai?
3. Parent-Child (Hierarchical) chunking precision aur context richness ko kaise balance karti hai?

What to Build Next:
Ek Markdown & Code Aware Chunker banayein jo markdown headings (`#`, `##`) aur Python code blocks (```` ``` ````) ko pehchanay aur code functions ko kabhi darmiyan se na kaate."""

# ==============================================================================
# LESSON 7.5: Query Transformations: HyDE, Multi-Query & Step-Back
# ==============================================================================
LESSON_CONTENT['7.5'] = r"""### Part 1: Mental Model & South Asian Analogy
User jab search bar mein query likhta hai to aksar query adhoori, mukhtasir, ya aam bol-chal mein hoti hai (jaise: "paise wapas kaise milenge?"). Lekin company ki knowledge base mein policy formal language mein likhi hoti hai (jaise: "Refund and Reimbursement Regulatory Policy 2026"). Agar aap user ki raw query direct vector search mein daalenge to mismatch ki wajah se sahi document nahi milega!
Isay samajhne ke liye kisi Wazeer-e-Azam ke Private Secretary aur Tarjuman ki misaal lein:
1. The Raw Query (Awami Shikayat): Gaon ka ek shaks aakar kehta hai: "Mera nalka sookh gaya hai, pani nahi aa raha."
2. HyDE - Hypothetical Document Embeddings (Khyali Jawab Likhnay Wala Secretary): Secretary janta hai ke sarkari file mein "nalka sookh gaya" nahi likha hoga. Secretary pehle ek Farzi / Khyali Jawab (Hypothetical Document) likhta hai: "Wazarat-e-Aabpashi ke tehat tube-well water supply maintenance policy." Phir is farzi jawab ka embedding vector nikal kar database mein match karta hai! Chunke dono documents formal language mein hain, exact match foran mil jata hai!
3. Multi-Query Expansion (3 Mukhtalif Zawayon Se Sawal): Secretary ek sawal ke 3 mukhtalif version banata hai: "Tube-well fault", "Water supply complaint", "Irrigation repair". Teeno queries search hoti hain aur unke results combine ho jate hain.
4. Step-Back Prompting (Bara Tasawwur Dekhna): Agar user pooche "Jazz SIM par 4G bundle code kya hai?", to Step-Back query puchte hai: "Jazz ke tamam active data packages ki directory kya hai?" Bara context milne se model sahi bundle code foran nikal leta hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein HyDE (Hypothetical Document Embeddings) ki Semantic Distance Bridging ka hisab lagayein.
Semantic Space Simulation (1D / 2D Coordinate projections):
Target Ground-Truth Document $D_{\text{truth}}$:
"Section 4: Customers are entitled to full monetary refund within 14 business days of product return."
Embedding Vector $D_{\text{truth}} = [0.85, 0.50]$.

Raw User Query $Q_{\text{raw}}$:
"paise wapas chahiye"
Embedding Vector $Q_{\text{raw}} = [0.10, 0.90]$ (Colloquial words, vector points in conversational direction).
Cosine Similarity between $Q_{\text{raw}}$ and $D_{\text{truth}}$:
$Q_{\text{raw}} \cdot D_{\text{truth}} = (0.10 \times 0.85) + (0.90 \times 0.50) = 0.085 + 0.450 = 0.5350$ (Weak match: 53.5% -> Likely missed in Top-K)!

HyDE Transformation Step:
LLM generates hypothetical document from $Q_{\text{raw}}$:
$D_{\text{hypo}}$: "To request a monetary refund, customer must initiate return process for reimbursement under terms."
Embedding Vector $D_{\text{hypo}} = [0.82, 0.54]$.

Cosine Similarity between $D_{\text{hypo}}$ and $D_{\text{truth}}$:
$D_{\text{hypo}} \cdot D_{\text{truth}} = (0.82 \times 0.85) + (0.54 \times 0.50) = 0.697 + 0.270 = 0.9670$ (96.7% Match!)
Similarity $0.535 \to 0.967$ par jump kar gayi!
HyDE ne language gap ko bridge karke impossible retrieval ko guaranteed top-1 match bana diya!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Multi-Query Expansion aur HyDE hypothetical document generation pipeline implement karte hain.

```python
import numpy as np
from typing import List, Dict

class QueryTransformationEngine:
    \"\"\"Generates Multi-Query and HyDE transformations to maximize retrieval recall.\"\"\"
    def __init__(self) -> None:
        pass

    def generate_hyde_document(self, raw_query: str) -> str:
        \"\"\"Simulates fast zero-shot LLM generating a hypothetical answer passage.\"\"\"
        # Simulated fast completion (e.g. via Gemini 2.0 Flash / Groq)
        if "refund" in raw_query.lower() or "wapas" in raw_query.lower():
            return (
                "Official Refund Policy: Customers can request a full financial reimbursement "
                "within 30 days of purchase upon submitting invoice proof to customer support."
            )
        return f"Standard enterprise protocol and documentation regarding: {raw_query}"

    def generate_multi_queries(self, raw_query: str) -> List[str]:
        \"\"\"Expands raw user query into 3 complementary semantic perspectives.\"\"\"
        return [
            raw_query,
            f"Formal organizational documentation on {raw_query}",
            f"Troubleshooting guidelines and technical procedure for {raw_query}"
        ]

# Execution test
if __name__ == "__main__":
    engine = QueryTransformationEngine()
    user_input = "mujhe mere order ke paise wapas lene hain"

    # 1. Multi-Query Expansion
    expanded = engine.generate_multi_queries(user_input)
    print("Multi-Query Expansion Angles:")
    for idx, q in enumerate(expanded, 1):
        print(f"  Angle {idx}: '{q}'")

    # 2. HyDE Transformation
    hypo_doc = engine.generate_hyde_document(user_input)
    print("\\nHyDE Hypothetical Document Generated:")
    print(f"  '{hypo_doc}'")
    print("\\n(This hypothetical text embedding will now be used to query the vector DB!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. HyDE Hallucination Causing Drift: Agar user query bohot anokhi ho aur LLM farzi jawab mein ghalat facts generate kar de to HyDE bilkul ghalat documents retrieve kar sakta hai. Hamesha original query embedding aur HyDE embedding dono ka weighted average use karein.
2. Latency Penalty of Sequential Transformations: Pehle LLM se HyDE mangwana phir 3 queries chalana latency ko 2 second barha deta hai. Hamesha fast inference engines (jaise Groq LLaMA-3.3 ya vLLM) use karein aur multiple queries ko `asyncio.gather` se parallel execute karein.
3. Over-Expanding Simple Factual Lookups: "Company ka helpline number kya hai?" jaise seedhay sawal par Multi-Query aur Step-Back lagana bekaar compute waste hai. Simple queries ko direct search par route karein.

Zero-GPU Tip:
Query transformation ke liye chotay fast models (jaise LLaMA-3.2-3B ya Qwen-2.5-3B) use karein jo free tier APIs par 50 milliseconds mein 3 expanded queries generate kar dete hain.

Self-Check Questions:
1. HyDE (Hypothetical Document Embeddings) conversational query aur formal document ke darmiyan gap ko kaise khatam karta hai?
2. Multi-Query retrieval mein Reciprocal Rank Fusion (RRF) ka kya kirdaar hota hai?
3. Step-Back Prompting query abstraction ko broad karke retrieval accuracy kaise barhati hai?

What to Build Next:
Ek Dynamic Query Router banayein jo incoming user prompt ki complexity evaluate kare: agar simple ho to direct vector search chalaye, agar complex ho to HyDE + Multi-Query pipeline trigger kare."""

# ==============================================================================
# LESSON 7.6: Module 7 Capstone: Zero-Hallucination Enterprise RAG
# ==============================================================================
LESSON_CONTENT['7.6'] = r"""### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne Modern RAG ke tamam advanced sutoon (HNSW vector indexing, Hybrid search with RRF, ColPali visual RAG, Semantic chunking, aur Query transformations) mukammal kar liye hain. Ab waqt hai ek **Zero-Hallucination Enterprise RAG Engine with Grounded Source Verification** khara karne ka!
Is Capstone project ka zehni khaka kisi Supreme Court ke Muhafiz aur Reference Checker jaisa hai:
1. The Strict Court Protocol (Zero-Hallucination Mandate): Model ko sakht hidayat hoti hai: "Aap apni taraf se koi baat gharr nahi sakte! Har lafz jo aap bolenge, uske sath file ka safha number aur paragraph citation (`[Source: Page 4, Para 2]`) hona lazmi hai."
2. The Research Wing (Hybrid Retrieval & Re-ranking): Pehle user query par HyDE aur Multi-Query chalte hain, phir pgvector aur BM25 se top documents aate hain, aur Cross-Encoder unhe re-rank karta hai.
3. The Verification Gate (Faithfulness Auditor): Model ka jawab generate hone ke baad ek automated checker check karta hai: "Kya model ke jawab ka har daawa (Claim) retrieved context ke andar mojud hai?" Agar model ne ek bhi baat bahar se banayi ho to jawab foran reject ho jata hai aur system user ko kehta hai: "Mawaad mein is sawal ka jawab mojud nahi hai."

Yeh Capstone project real-world enterprise RAG ka gold standard hai jise banks aur medical companies use karti hain.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Automated Groundedness & Faithfulness Verification Score ka exact hisab lagayein.
Formula for Faithfulness Score:
$\text{Faithfulness} = \frac{|\text{Supported Claims}|}{|\text{Total Atomic Claims Generated}|}$
Decision Boundary:
- If $\text{Faithfulness} \ge 0.85 \implies$ Accept and Return with verified citations.
- If $\text{Faithfulness} < 0.85 \implies$ Reject output (Flag as Hallucination Risk).

Worked Numeric Audit:
Retrieved Verified Context:
"Standard shipping in Pakistan takes 3 to 5 business days. Delivery fee is 250 PKR. Free delivery on orders above 3000 PKR."

Generated Model Response:
"Delivery takes 3 to 5 business days in Pakistan [1]. Delivery charges are 250 PKR [2], and you get 10% discount on first order [3]."

Atomic Claims Decomposition:
- Claim 1: "Delivery takes 3 to 5 business days" -> Found in context? YES (Supported).
- Claim 2: "Delivery charges are 250 PKR" -> Found in context? YES (Supported).
- Claim 3: "10% discount on first order" -> Found in context? NO! Model hallucinated this promo from internet training weights!

Score Calculation:
Total Claims $= 3$.
Supported Claims $= 2$.
$\text{Faithfulness} = \frac{2}{3} \approx 0.6667$ (66.67%).
Since $0.6667 < 0.85$, the Verification Gate rejects Claim 3, strips the hallucination, and returns clean verified response!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete Enterprise RAG Engine implement karte hain: hybrid retrieval, prompt injection defense, citation generation, aur programmatic claim verification.

```python
import json
import time
from typing import List, Dict, Any
from pydantic import BaseModel, Field

class CitedSource(BaseModel):
    doc_id: str
    excerpt: str

class VerifiedRAGResponse(BaseModel):
    answer: str
    cited_sources: List[CitedSource]
    faithfulness_score: float = Field(ge=0.0, le=1.0)
    is_grounded: bool
    latency_ms: float

class EnterpriseRAGEngine:
    \"\"\"Production RAG engine enforcing strict source citation and zero-hallucination verification.\"\"\"
    def __init__(self) -> None:
        # Ground-truth corporate knowledge base
        self.knowledge_base: Dict[str, str] = {
            "DOC_POLICY_01": "Employees can claim up to 15,000 PKR monthly for health wellness receipts.",
            "DOC_POLICY_02": "Annual leave quota is 20 days. Unused leaves carry over up to 10 days max."
        }

    def retrieve(self, query: str) -> List[Tuple[str, str]]:
        \"\"\"Simulates hybrid retrieval + cross-encoder re-ranking returning top matches.\"\"\"
        results = []
        for doc_id, text in self.knowledge_base.items():
            if any(term in text.lower() for term in ["leave", "quota", "wellness", "pkr"]):
                results.append((doc_id, text))
        return results

    def verify_claims(self, answer: str, context: str) -> Tuple[bool, float]:
        \"\"\"Checks if generated claims are mathematically grounded in retrieved context.\"\"\"
        # Simulated claim auditor
        if "wellness" in context.lower() and "15,000" in answer:
            return True, 1.00
        return False, 0.50

    def query(self, user_question: str) -> VerifiedRAGResponse:
        t0 = time.perf_counter()
        
        # 1. Retrieval
        retrieved_docs = self.retrieve(user_question)
        if not retrieved_docs:
            elapsed_ms = (time.perf_counter() - t0) * 1000.0
            return VerifiedRAGResponse(
                answer="I apologize, but this information is not present in the verified documentation.",
                cited_sources=[],
                faithfulness_score=1.0,
                is_grounded=True,
                latency_ms=round(elapsed_ms, 2)
            )

        # 2. Compile Context & Prompt
        context_block = "\\n".join(f"[{doc_id}]: {text}" for doc_id, text in retrieved_docs)
        
        # 3. Simulated Generation with Citations
        doc_id, excerpt = retrieved_docs[0]
        generated_answer = (
            f"According to company policy, employees are eligible for up to 15,000 PKR monthly "
            f"for health and wellness claims [{doc_id}]."
        )

        # 4. Strict Groundedness Verification Gate
        is_grounded, faithfulness = self.verify_claims(generated_answer, context_block)
        elapsed_ms = (time.perf_counter() - t0) * 1000.0

        return VerifiedRAGResponse(
            answer=generated_answer,
            cited_sources=[CitedSource(doc_id=doc_id, excerpt=excerpt)],
            faithfulness_score=faithfulness,
            is_grounded=is_grounded,
            latency_ms=round(elapsed_ms, 2)
        )

# Execution test
if __name__ == "__main__":
    engine = EnterpriseRAGEngine()
    response = engine.query("What is the monthly health wellness allowance?")
    
    print("Enterprise RAG Query Completed!")
    print(f"Latency:      {response.latency_ms} ms")
    print(f"Faithfulness: {response.faithfulness_score * 100:.1f}%")
    print(f"Grounded:     {response.is_grounded}")
    print(f"Answer:\\n  {response.answer}")
    print(f"Citations:")
    for s in response.cited_sources:
        print(f"  [{s.doc_id}] -> '{s.excerpt}'")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Allowing the Model to Fallback on General Pre-Training Knowledge: Agar prompt mein sakht negative constraint ("Do NOT use outside knowledge; if not found say 'I do not know'") na ho, to model chupke se internet training data se purani ya ghalat cheezein invent kar leta hai.
2. Inaccurate or Broken Citations: Agar model jawab mein `[Doc 1]` likh de jabke retrieved documents mein `Doc 1` ka koi talluq na ho to user ka aitabar toot jata hai. Automated verification gate se citation validity check karein.
3. Giant Unchunked Context Windows: 100 safhon ka poora PDF context window mein phenk dena 'Lost in the Middle' problem paida karta hai jahan model darmiyan ke safhon par dhyan nahi deta. Hamesha targeted small chunks retrieve karein.

Zero-GPU Tip:
Enterprise RAG pipeline ka poora orchestration (Hybrid search, RRF merging, prompt assembly, aur citation extraction) CPU par chalta hai. Free tier Groq Cloud ya Gemini 2.0 Flash APIs ke zariye aap zero GPU dollar cost par zero-hallucination enterprise RAG chala sakte hain.

Self-Check Questions:
1. RAG system mein Faithfulness Score kaise calculate kiya jata hai?
2. 'Lost in the Middle' problem kya hai aur yeh long-context retrieval ko kaise affect karti hai?
3. Source citations (`[Doc ID]`) enterprise business aur legal compliance ke liye kyun lazmi hain?

What to Build Next:
Is Capstone engine ko extend karein taake yeh Ragas framework ke metrics (Faithfulness, Answer Relevance, Context Recall) ko automated CI/CD pipeline mein run kare aur 100 test queries par report banaye."""
