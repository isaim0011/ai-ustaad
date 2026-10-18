const fs = require('fs');
const path = require('path');

const syllabusDataCode = `import type { Phase, Badge, DiagramGalleryItem, UserProfile } from './types';

export const PHASES_DATA: Phase[] = [
  // =========================================================================
  // PHASE 1: FOUNDATIONS OF MODERN AI (WEEKS 1–4)
  // =========================================================================
  {
    id: 'phase-1',
    slug: 'foundations',
    number: 1,
    title: 'Phase 1: Foundations of Modern AI & High-Performance Data',
    titleUrdu: 'Buniyaadi AI, Python 3.12 aur Riyazi (Linear Algebra & Calculus)',
    duration: 'Weeks 1–4',
    icon: '⚡',
    description: 'Python for AI, High-Performance NumPy/Polars, Linear Algebra, Vector Spaces, Cosine Similarity, aur Prompt Engineering mental models.',
    modules: [
      {
        id: 'mod-1',
        slug: 'python-data-ecosystem',
        phaseId: 'phase-1',
        title: 'Module 1: Modern Python 3.12+ & High-Speed Data Ecosystem',
        titleUrdu: 'Modern Python 3.12+ aur Tez-Tar Data Processing (Polars & NumPy)',
        weekRange: 'Weeks 1–2',
        description: 'Type Hints, Asynchronous I/O, contiguous memory layouts, NumPy vectorization aur Polars vs Pandas performance optimization.',
        realWorldDeliverable: {
          title: '500k E-Commerce Order Sanitizer & Parquet Pipeline',
          urduTitle: '500k E-Commerce Orders Sanitizer aur Parquet Pipeline',
          freelanceValue: '$250 - $550 / Upwork Data Cleaning & ETL Contract',
          description: 'A production data processing pipeline that reads 500,000 messy e-commerce orders, validates them with Pydantic v2 schemas, normalizes addresses and currencies using vectorized Polars, and exports snappy-compressed partitioned Parquet files.',
          steps: [
            'Stream and ingest 500,000 messy CSV records with zero memory blowout using Polars scan_csv()',
            'Validate schema integrity, missing fields, and phone/CNIC formats with Pydantic v2',
            'Perform vectorized datetime and currency conversion without a single Python for-loop',
            'Write snappy-compressed partitioned Parquet files achieving 90% disk space reduction'
          ],
          outputArtifact: 'sanitized_orders.parquet (90% compression) + benchmark_report.json'
        },
        zeroGpuRecipe: {
          platform: '100% Local CPU / Google Colab Free Tier',
          vramRequired: '0 GB (Pure Multi-Core CPU SIMD)',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'Polars uses an Apache Arrow Rust engine that auto-scales across all CPU cores — zero GPU hours needed!',
          setupSnippet: 'pip install polars pydantic pyarrow',
          launchUrl: 'https://colab.research.google.com/'
        },
        lessons: [
          {
            id: 'les-1-1',
            slug: 'python-type-hints-async',
            title: 'Lesson 1.1: Modern Python 3.12+ for AI Engineers',
            titleUrdu: 'Modern Python 3.12+ AI Engineers Ke Liye',
            week: 1,
            durationMinutes: 35,
            xpReward: 100,
            learningOutcomes: [
              'Understand Pydantic v2 & Python type hints in production pipelines',
              'Master async/await concurrency for batch API inference',
              'Profile memory bottlenecks with tracemalloc'
            ],
            romanUrduSummary: 'So guys, traditional Python scripting aur production AI engineering mein zameen aasmaan ka farq hai! Jab aap production mein LLMs ya embeddings serve karte hain, toh single-threaded blocking calls poore system ko freeze kar deti hain. Is lesson mein hum dekhenge ke asyncio aur Pydantic v2 validation se 10x throughput kaise milti hai.',
            deepDiveExplanation: 'Production AI pipelines require deterministic schemas. Pydantic v2 (Rust-backed) eliminates invalid tensor shapes and unstructured payloads before they hit GPU memory. Python 3.12 provides enhanced exception groups and task groups, ensuring clean failover when querying multiple AI endpoints simultaneously.',
            realWorldDeliverable: {
              title: 'Async Multi-Endpoint LLM Batch Ingestion Service',
              urduTitle: 'Async Concurrent AI Batch Ingestion Service',
              freelanceValue: '$200 - $400 / Freelance API Proxy Contract',
              description: 'Concurrent async pipeline fetching embeddings from 3 endpoints with retry policies and Pydantic validation.',
              steps: ['Setup Pydantic model', 'Implement asyncio.gather with rate-limit semaphore', 'Benchmark latency'],
              outputArtifact: 'async_batch_service.py'
            },
            zeroGpuRecipe: {
              platform: '100% Local CPU / Colab Free Tier',
              vramRequired: '0 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Async I/O runs entirely on CPU event loops without needing any GPU compute units.',
              setupSnippet: 'pip install pydantic httpx',
              launchUrl: 'https://colab.research.google.com/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'async_inference_pipeline.py',
              code: \`import asyncio
from pydantic import BaseModel, Field

class ModelPayload(BaseModel):
    prompt: str = Field(..., min_length=3)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=512, le=4096)

async def simulate_llm_inference(batch_id: int, payload: ModelPayload) -> dict:
    print(f"[Worker {batch_id}] Processing: '{payload.prompt[:20]}...' (temp={payload.temperature})")
    await asyncio.sleep(0.3)
    return {"batch_id": batch_id, "tokens_generated": 142, "status": "success"}

async def main():
    prompts = [
        ModelPayload(prompt="Explain Backpropagation in Roman Urdu"),
        ModelPayload(prompt="Write a Rust Axum microservice for embeddings"),
        ModelPayload(prompt="Compare LoRA vs Full Fine-Tuning")
    ]
    tasks = [simulate_llm_inference(i, p) for i, p in enumerate(prompts)]
    results = await asyncio.gather(*tasks)
    print("Inference Batch Completed Successfully:", len(results))

asyncio.run(main())\`,
              explanation: 'Yeh script Pydantic validation ke sath non-blocking async batch execution ko demonstrate karta hai.',
              simulationOutput: \`[Worker 0] Processing: 'Explain Backpropagat...' (temp=0.7)
[Worker 1] Processing: 'Write a Rust Axum mi...' (temp=0.7)
[Worker 2] Processing: 'Compare LoRA vs Full...' (temp=0.7)
Inference Batch Completed Successfully: 3
Execution time: 0.302s (Zero blocking overhead)\`
            },
            diagramScript: \`flow LR: Async Batch Pipeline
  client[HTTP Client] -> val{Pydantic Schema Check}
  val ->|Valid| pool[Async Task Pool]
  val ->|Error| rej((422 Error))
  pool -> gpu1[Inference Stream A]
  pool -> gpu2[Inference Stream B]
  pool -> gpu3[Inference Stream C]
  gpu1 & gpu2 & gpu3 --> collector[Stream Aggregator] -> client\`,
            diagramPreset: 'blueprint',
            diagramAnimate: 'flow',
            actionItems: [
              'Apne machine par Python 3.12 aur Pydantic v2 install karein',
              'Ek custom BaseModel likhein jo LLM prompt aur metadata validate kare',
              'asyncio.gather se concurrent API calls test karein'
            ],
            resources: [
              { title: 'Official Python AsyncIO Documentation', url: 'https://docs.python.org/3/library/asyncio.html', type: 'tool', tag: 'Docs' },
              { title: 'Pydantic v2 Rust Core Performance Benchmark', url: 'https://docs.pydantic.dev', type: 'tool', tag: 'Library' }
            ]
          },
          {
            id: 'les-1-2',
            slug: 'numpy-polars-vectorization',
            title: 'Lesson 1.2: Vectorization Mastery: NumPy & Polars',
            titleUrdu: 'NumPy aur Polars ke Sath Tez Vectorized Operations',
            week: 1,
            durationMinutes: 40,
            xpReward: 120,
            learningOutcomes: [
              'Understand contiguous C-memory layouts vs Python list pointers',
              'Master Polars expression API for 50x faster data preprocessing',
              'Eliminate Python for-loops via SIMD vector broadcasting'
            ],
            romanUrduSummary: 'Python ke slow hone ka sab se bara reason pointer-chasing aur dynamic typing hai. Jab aap NumPy ya Polars use karte hain, toh calculations CPU ke SIMD registers mein parallel hoti hain. Is lesson mein hum dekhenge ke 500k rows par for-loop chalane ki bajaye Polars se 10 milliseconds mein calculations kaise hoti hain.',
            deepDiveExplanation: 'Polars is written in Rust on top of Apache Arrow columnar memory format. It provides lazy query optimization and multithreaded SIMD vectorization. Data is laid out sequentially in RAM cache lines (64 bytes), avoiding CPU cache misses completely.',
            realWorldDeliverable: {
              title: '500k Row E-Commerce Sanitizer Benchmark',
              urduTitle: '500k Rows Ka Tez Polars Sanitizer',
              freelanceValue: '$300 / ETL Script Deliverable',
              description: 'Deliverable reading 500k rows, calculating revenue per customer, and exporting to Parquet.',
              steps: ['Create lazy frame', 'Apply filter and groupby expressions', 'Export parquet'],
              outputArtifact: 'sanitizer.py'
            },
            zeroGpuRecipe: {
              platform: '100% Local CPU / Colab Free Tier',
              vramRequired: '0 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Apache Arrow memory format runs entirely on CPU RAM — zero GPU required.',
              setupSnippet: 'pip install polars pyarrow',
              launchUrl: 'https://colab.research.google.com/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'polars_speedup.py',
              code: \`import polars as pl
import numpy as np

# Simulate 500,000 e-commerce orders
n = 500_000
df = pl.DataFrame({
    "order_id": np.arange(n),
    "amount_pkr": np.random.uniform(500, 15000, n),
    "status": np.random.choice(["completed", "pending", "returned"], n)
})

# Vectorized Polars lazy expression
sanitized = (
    df.lazy()
    .filter(pl.col("status") == "completed")
    .with_columns([
        (pl.col("amount_pkr") * 0.95).alias("net_revenue_pkr"),
        (pl.col("amount_pkr") / 280.0).alias("amount_usd")
    ])
    .collect()
)

print(f"Processed {len(sanitized):,} completed orders in milliseconds!")
print(sanitized.head(3))\`,
              explanation: 'Yeh script 500k records ko baghair kisi for-loop ke vectorized parallel engine mein process karta hai.',
              simulationOutput: \`Processed 166,412 completed orders in milliseconds!
shape: (3, 5)
┌──────────┬────────────┬───────────┬─────────────────┬────────────┐
│ order_id ┆ amount_pkr ┆ status    ┆ net_revenue_pkr ┆ amount_usd │
│ ---      ┆ ---        ┆ ---       ┆ ---             ┆ ---        │
│ i32      ┆ f64        ┆ str       ┆ f64             ┆ f64        │
╞══════════╪════════════╪═══════════╪═════════════════╪════════════╡
│ 0        ┆ 4320.50    ┆ completed ┆ 4104.475        ┆ 15.4303    │
│ 4        ┆ 8910.20    ┆ completed ┆ 8464.690        ┆ 31.8221    │
│ 7        ┆ 1200.00    ┆ completed ┆ 1140.000        ┆ 4.2857     │
└──────────┴────────────┴───────────┴─────────────────┴────────────┘\`
            },
            diagramScript: \`flow TD: Polars vs Pandas Memory Architecture
  subgraph Pandas [Pandas: Object Pointers]
    p_ptr[Array of Pointers] -> o1[Python Float Object 1]
    p_ptr -> o2[Python Float Object 2]
    p_ptr -> o3[Python Float Object 3]
  end
  subgraph Polars [Polars: Contiguous Arrow Buffer]
    arrow[Contiguous 64-bit Float Buffer: [4320.5, 8910.2, 1200.0]] $database
    arrow --> simd[CPU SIMD 256-bit Register (4 Floats / Clock)] $cpu *
  end\`,
            diagramPreset: 'paper',
            diagramAnimate: 'flow',
            actionItems: [
              'Polars install karke ek 100k rows ka CSV benchmark run karein',
              'Pandas ke muqable mein memory aur execution time compare karein',
              'Parquet export ko verify karein'
            ],
            resources: [
              { title: 'Official Polars User Guide', url: 'https://docs.pola.rs/', type: 'tool', tag: 'Docs' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-1',
          title: 'Module 1 Quiz: Modern Python & High-Speed Data',
          titleUrdu: 'Module 1 Imtihan: Modern Python aur Tez Data Processing',
          passingScore: 70,
          xpReward: 200,
          badgeId: 'first_step',
          questions: [
            {
              id: 'q1-1',
              question: 'Python list aur NumPy array ke memory layout mein sab se bara farq kya hai?',
              options: [
                'NumPy arrays sirf text store karte hain',
                'Python lists contiguous C-arrays hoti hain jabke NumPy arrays pointer arrays hote hain',
                'NumPy arrays contiguous block of memory mein rehte hain jabke Python list pointers ka array hoti hai',
                'Koi farq nahi hota'
              ],
              correctIndex: 2,
              explanation: 'NumPy contiguous C-memory blocks use karta hai jo CPU cache mein direct fit aate hain aur SIMD parallel instructions ko support karte hain.',
              conceptUrdu: 'Contiguous Memory Layout aur CPU Cache Locality'
            },
            {
              id: 'q1-2',
              question: 'Production AI microservice mein Pydantic v2 ka sab se ahem faida kya hai?',
              options: [
                'Yeh GPU ki speed 2x kar deta hai',
                'Yeh input request payload ko Rust-backed engine se validate karta hai taake invalid shapes ya types GPU tak na pohnchein',
                'Yeh CSS generate karta hai',
                'Yeh model ke weights compress karta hai'
              ],
              correctIndex: 1,
              explanation: 'Pydantic v2 ka core Rust mein likha gaya hai, jo incoming JSON payloads ko microseconds mein validate karta hai.',
              conceptUrdu: 'Pydantic Schema Validation in AI Serving'
            }
          ]
        }
      },
      {
        id: 'mod-2',
        slug: 'essential-math-ai',
        phaseId: 'phase-1',
        title: 'Module 2: Essential Mathematics for AI & Semantic Embeddings',
        titleUrdu: 'AI Ke Liye Zaroori Riyazi (Linear Algebra, Calculus & Cosine Similarity)',
        weekRange: 'Weeks 3–4',
        description: 'Vectors, Matrices, Dot Products, Cosine Similarity, Gradients, Partial Derivatives, aur Loss Surfaces first-principles se.',
        realWorldDeliverable: {
          title: 'Pure-NumPy Semantic Resume-Job Matcher',
          urduTitle: 'Pure-NumPy Semantic Resume-Job Matcher Engine',
          freelanceValue: '$300 - $650 / HR Tech Screening Automation Contract',
          description: 'A pure NumPy recruitment matching engine that vectorizes candidate CVs and job descriptions, calculates normalized dot product cosine similarities, and outputs ranked match scores with zero third-party ML dependencies.',
          steps: [
            'Construct multi-dimensional skill vectors across experience, seniority, and technical stacks',
            'Compute normalized L2 vector norms and broadcast dot products in pure NumPy',
            'Calculate pairwise cosine similarity matrix across 1,000 candidate profiles in <5ms',
            'Generate match confidence percentiles and explanation breakdown report'
          ],
          outputArtifact: 'resume_matcher_engine.py + ranked_candidates.json'
        },
        zeroGpuRecipe: {
          platform: '100% Local CPU / Google Colab Free CPU',
          vramRequired: '0 GB',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'Vector dot products on 1,000 candidates execute in <10ms on ordinary laptop CPU without touching GPUs!',
          setupSnippet: 'pip install numpy scipy',
          launchUrl: 'https://colab.research.google.com/'
        },
        lessons: [
          {
            id: 'les-2-1',
            slug: 'vector-spaces-cosine-similarity',
            title: 'Lesson 2.1: Vector Spaces, Dot Products & Cosine Alignment',
            titleUrdu: 'Vector Spaces aur Cosine Similarity Ka Asal Matlab',
            week: 2,
            durationMinutes: 45,
            xpReward: 130,
            learningOutcomes: [
              'Understand vectors as points in high-dimensional semantic spaces',
              'Implement Cosine Similarity from scratch without scikit-learn',
              'Visualize how embeddings represent semantic meaning'
            ],
            romanUrduSummary: 'AI models text ko direct nahi samajhte, woh har lafz ya sentence ko ek number array (Vector) mein convert karte hain. Jab do baatein aapas mein milti julti hon, toh unke vectors ke darmiyan angle bohot chhota hota hai. Is angle ka cosine nikalne se humein 0 se 1 ke darmiyan similarity score milta hai.',
            deepDiveExplanation: 'The dot product of two normalized vectors equals the cosine of the angle between them: cos(theta) = (A . B) / (||A|| * ||B||). In high-dimensional embedding spaces (e.g. 1536 dims), cosine similarity captures directional orientation invariant to vector magnitude.',
            realWorldDeliverable: {
              title: 'Vector Similarity Search Engine',
              urduTitle: 'Pure NumPy Vector Search Engine',
              freelanceValue: '$250 / Fast Search Script',
              description: 'Vector similarity search engine ranking top-k items from scratch in pure NumPy.',
              steps: ['Normalize vectors', 'Dot product matrix multiplication', 'Argpartition top-k'],
              outputArtifact: 'vector_search.py'
            },
            zeroGpuRecipe: {
              platform: '100% Local CPU',
              vramRequired: '0 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'NumPy BLAS libraries optimize matrix multiplication across CPU threads.',
              setupSnippet: 'pip install numpy',
              launchUrl: 'https://colab.research.google.com/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'cosine_similarity_scratch.py',
              code: \`import numpy as np

def cosine_similarity(v1, v2):
    # First principles: dot product divided by norms product
    dot_prod = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_prod / (norm_v1 * norm_v2)

# Semantic embedding vectors (Simulated 4-dim vectors)
king   = np.array([0.9, 0.8, 0.1, 0.0])
queen  = np.array([0.88, 0.79, 0.12, 0.85])
apple  = np.array([0.05, 0.12, 0.95, 0.1])

print(f"Similarity (King, Queen): {cosine_similarity(king, queen):.4f}")
print(f"Similarity (King, Apple): {cosine_similarity(king, apple):.4f}")
print("Semantic alignment mathematically proven! 🎯")\`,
              explanation: 'Yeh pure NumPy mein dot product aur L2 norms use karke cosine similarity calculate karta hai.',
              simulationOutput: \`Similarity (King, Queen): 0.8584
Similarity (King, Apple): 0.1601
Semantic alignment mathematically proven! 🎯\`
            },
            diagramScript: \`flow LR: Geometric Vector Alignment
  v1[King Vector] --> origin((Origin (0,0)))
  v2[Queen Vector] --> origin
  v3[Apple Vector] --> origin
  origin -.-> angle["Small Angle Theta = 0.86 Similarity"]
  origin -.-> far["90 deg Orthogonal = ~0.0 Similarity"]\`,
            diagramPreset: 'forest',
            diagramAnimate: 'pulse',
            actionItems: [
              '10 sentences ke liye mock embeddings banayein',
              'Pure NumPy se top-3 nearest neighbours find karein',
              'Cosine similarity function ko test karein'
            ],
            resources: [
              { title: '3Blue1Brown Linear Algebra Series', url: 'https://www.3blue1brown.com/topics/linear-algebra', type: 'course', tag: 'Math' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-2',
          title: 'Module 2 Quiz: Mathematics & Vector Spaces',
          titleUrdu: 'Module 2 Imtihan: Riyazi aur Vector Spaces',
          passingScore: 70,
          xpReward: 200,
          badgeId: 'matrix_ninja',
          questions: [
            {
              id: 'q2-1',
              question: 'Agar do vectors bilkul ek hi simt (direction) mein hon, toh unka Cosine Similarity score kya hoga?',
              options: ['0.0', '1.0', '-1.0', 'Infinite'],
              correctIndex: 1,
              explanation: 'Jab angle theta = 0 degrees hota hai, toh cos(0) = 1.0 hota hai, jo perfect semantic alignment zahir karta hai.',
              conceptUrdu: 'Cosine Similarity Angle Representation'
            }
          ]
        }
      }
    ]
  },

  // =========================================================================
  // PHASE 2: CORE ML & DEEP LEARNING (WEEKS 5–8)
  // =========================================================================
  {
    id: 'phase-2',
    slug: 'core-ml-deeplearning',
    number: 2,
    title: 'Phase 2: Core Machine Learning & Deep Learning',
    titleUrdu: 'Classical ML, Gradient Descent, PyTorch aur Attention Mechanisms',
    duration: 'Weeks 5–8',
    icon: '🧠',
    description: 'Scikit-learn supervised pipelines, Gradient Boosting (XGBoost), PyTorch computational graphs, autograd backpropagation, aur Transformer Attention block.',
    modules: [
      {
        id: 'mod-3',
        slug: 'classical-ml-feature-engineering',
        phaseId: 'phase-2',
        title: 'Module 3: Classical Machine Learning & Feature Engineering',
        titleUrdu: 'Classical Machine Learning aur Feature Pipelines (XGBoost)',
        weekRange: 'Weeks 5–6',
        description: 'Data leakage se bachna, ColumnTransformer, Decision Trees, XGBoost/LightGBM, Precision-Recall curves aur ROC-AUC.',
        realWorldDeliverable: {
          title: 'Upwork Client Churn & Lead Scoring Web Service',
          urduTitle: 'Upwork Client Churn aur Lead Scoring Web Service',
          freelanceValue: '$400 - $850 / SaaS Retention ML Contract',
          description: 'An enterprise churn prediction service with ColumnTransformer preprocessing, trained XGBoost model, SHAP explainability values, and a sub-20ms FastAPI inference endpoint.',
          steps: [
            'Build leak-free preprocessing pipeline with ColumnTransformer (impute, one-hot, robust scale)',
            'Train tuned XGBoost classifier handling class imbalance with scale_pos_weight',
            'Compute SHAP feature attribution explaining exact reasons for high-risk churn clients',
            'Wrap model into a Dockerized FastAPI endpoint returning predictions with confidence'
          ],
          outputArtifact: 'churn_service_fastapi.py + xgboost_model.json'
        },
        zeroGpuRecipe: {
          platform: 'Kaggle CPU / Google Colab Free CPU',
          vramRequired: '0 GB (CPU Multi-Threading)',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'XGBoost multi-threading runs blazing fast on CPU using n_jobs=-1.',
          setupSnippet: 'pip install scikit-learn xgboost shap fastapi uvicorn',
          launchUrl: 'https://www.kaggle.com/code'
        },
        lessons: [
          {
            id: 'les-3-1',
            slug: 'xgboost-feature-pipelines',
            title: 'Lesson 3.1: Supervised ML & XGBoost Pipelines',
            titleUrdu: 'Scikit-Learn aur XGBoost Ke Sath Production Pipeline',
            week: 5,
            durationMinutes: 45,
            xpReward: 150,
            learningOutcomes: [
              'Understand gradient boosted decision trees mechanics',
              'Prevent training data leakage using Scikit-Learn Pipeline',
              'Evaluate models using Precision, Recall and F1-score'
            ],
            romanUrduSummary: 'Classical ML aaj bhi tabular data par deep learning se behtar aur sasta perform karta hai! XGBoost residuals par naye trees fit karta hai taake har naya tree pichle tree ki ghaltiyan theek kare. Is lesson mein hum dekhenge ke customer churn model kaise train kiya jata hai.',
            deepDiveExplanation: 'Gradient Boosting fits successive decision trees to pseudo-residuals of the loss function using second-order Taylor approximations. Scikit-learn Pipeline guarantees transformations are fitted strictly on training folds to prevent target leakage.',
            realWorldDeliverable: {
              title: 'Customer Churn Predictor Pipeline',
              urduTitle: 'Customer Churn Prediction Pipeline',
              freelanceValue: '$350 / Predictive Model Delivery',
              description: 'Trained XGBoost model with precision-recall evaluation report.',
              steps: ['Split data', 'Fit pipeline', 'Generate classification report'],
              outputArtifact: 'churn_model.py'
            },
            zeroGpuRecipe: {
              platform: '100% Local CPU',
              vramRequired: '0 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Tabular tree training does not require GPUs.',
              setupSnippet: 'pip install scikit-learn xgboost',
              launchUrl: 'https://colab.research.google.com/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'xgboost_pipeline.py',
              code: \`from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import numpy as np

# Synthetic features: [Usage Hours, Tickets Opened, Days Since Login]
X = np.array([[120, 1, 2], [10, 8, 30], [80, 2, 4], [5, 12, 45]])
y = np.array([0, 1, 0, 1]) # 1 = Churned, 0 = Retained

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', XGBClassifier(n_estimators=10, max_depth=2, eval_metric='logloss'))
])

pipeline.fit(X, y)
new_client = np.array([[8, 9, 28]])
churn_prob = pipeline.predict_proba(new_client)[0][1]
print(f"Risk Score for Client: {churn_prob:.2%} -> High Churn Risk! 🚨")\`,
              explanation: 'Yeh script Scikit-Learn Pipeline mein StandardScaler aur XGBoost ko leak-free chain karta hai.',
              simulationOutput: \`Risk Score for Client: 88.42% -> High Churn Risk! 🚨\`
            },
            diagramScript: \`flow LR: Gradient Boosting Sequential Tree Fitting
  data[Client Tabular Features] -> tree1[Tree 1: Base Prediction]
  tree1 -> res1[Calculate Residual Errors]
  res1 -> tree2[Tree 2: Fit on Residuals]
  tree2 -> res2[Calculate Remaining Error]
  res2 -> tree3[Tree 3: Minimize Loss Surface]
  tree1 & tree2 & tree3 --> ensemble[Weighted Ensemble Output] * \`,
            diagramPreset: 'midnight',
            diagramAnimate: 'flow',
            actionItems: [
              'Synthetic customer dataset generate karein',
              'XGBoost pipeline fit karke ROC-AUC score check karein',
              'Feature importances plot karein'
            ],
            resources: [
              { title: 'Official XGBoost Documentation', url: 'https://xgboost.readthedocs.io/', type: 'tool', tag: 'Docs' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-3',
          title: 'Module 3 Quiz: Classical ML & Feature Pipelines',
          titleUrdu: 'Module 3 Imtihan: Classical Machine Learning',
          passingScore: 70,
          xpReward: 250,
          badgeId: 'ml_practitioner',
          questions: [
            {
              id: 'q3-1',
              question: 'Data leakage se bachne ke liye Scaling aur Imputation kab karni chahiye?',
              options: [
                'Pura dataset ek sath scale karein',
                'Sirf training data par fit karein aur validation/test par transform karein',
                'Sirf test set par scale karein',
                'Scaling ki zaroorat nahi hoti'
              ],
              correctIndex: 1,
              explanation: 'Test set ki information training phase mein leak na hone dena production ML ka basic rule hai.',
              conceptUrdu: 'Data Leakage aur Pipeline Fitting'
            }
          ]
        }
      },
      {
        id: 'mod-4',
        slug: 'pytorch-deep-learning-foundations',
        phaseId: 'phase-2',
        title: 'Module 4: Deep Learning & PyTorch Foundations from Scratch',
        titleUrdu: 'PyTorch Buniyaad: Tensors, Autograd aur Neural Networks',
        weekRange: 'Weeks 7–8',
        description: 'Dynamic Computation Graphs (DAG), autograd backward pass verification, nn.Module, CrossEntropyLoss, aur AdamW optimizer loop.',
        realWorldDeliverable: {
          title: 'PyTorch Neural Financial Fraud Classifier',
          urduTitle: 'PyTorch Neural Financial Fraud Classifier',
          freelanceValue: '$450 - $950 / FinTech Risk Modeling Gig',
          description: 'A 4-layer PyTorch MLP with Residual Skip Connections, custom BCEWithLogitsLoss weighting for 99:1 imbalanced transaction fraud data, and CosineAnnealingLR scheduling delivering PR-AUC > 0.92.',
          steps: [
            'Construct custom PyTorch Dataset and DataLoader with pin_memory=True for fast CUDA dispatch',
            'Build 4-layer MLP architecture with LayerNorm, Dropout(0.2), and Residual connections',
            'Implement weighted BCE loss handling extreme 99:1 fraud class imbalance',
            'Train model on Colab T4 with mixed-precision torch.cuda.amp.autocast'
          ],
          outputArtifact: 'fraud_detector_model.pt + training_curves.png'
        },
        zeroGpuRecipe: {
          platform: 'Google Colab Free T4 (15GB VRAM)',
          vramRequired: '1.2 GB VRAM',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'from google.colab import runtime; runtime.unassign() # Disconnect automatically after 10 epochs!',
          setupSnippet: '!pip install torch torchvision --upgrade',
          launchUrl: 'https://colab.research.google.com/'
        },
        lessons: [
          {
            id: 'les-4-1',
            slug: 'pytorch-tensors-autograd',
            title: 'Lesson 4.1: PyTorch Tensors, Autograd & Computation DAGs',
            titleUrdu: 'PyTorch Autograd aur Dynamic Computation Graphs',
            week: 7,
            durationMinutes: 45,
            xpReward: 160,
            learningOutcomes: [
              'Understand PyTorch computational graphs and backward() mechanics',
              'Verify manual analytical derivatives against autograd output',
              'Manage GPU VRAM tensors with .to("cuda")'
            ],
            romanUrduSummary: 'So guys, PyTorch ka magic uska Autograd engine hai! Jab aap kisi tensor par calculations karte hain, PyTorch background mein ek Directed Acyclic Graph (DAG) banata hai. Jab aap .backward() call karte hain, toh Calculus ka Chain Rule automatically reverse order mein execute hota hai aur har weight ka gradient calculate ho jata hai.',
            deepDiveExplanation: 'PyTorch constructs a dynamic computational graph during the forward pass. Each tensor retains a .grad_fn reference tracking operations. During backward(), the graph is traversed in reverse topological order, accumulating partial derivatives into .grad tensors.',
            realWorldDeliverable: {
              title: 'Autograd Micrograd Engine',
              urduTitle: 'Micrograd Autograd Engine',
              freelanceValue: '$300 / Custom Neural Engine',
              description: 'Verification of manual backpropagation against PyTorch autograd.',
              steps: ['Define computation DAG', 'Execute forward pass', 'Verify backward gradients'],
              outputArtifact: 'autograd_verify.py'
            },
            zeroGpuRecipe: {
              platform: 'Google Colab Free T4 / Local CPU',
              vramRequired: '0.5 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Colab CPU runs autograd experiments in seconds.',
              setupSnippet: 'pip install torch',
              launchUrl: 'https://colab.research.google.com/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'autograd_demo.py',
              code: \`import torch

# Create scalar tensors with gradient tracking
x = torch.tensor(3.0, requires_grad=True)
w = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(1.0, requires_grad=True)

# Forward pass: y = w * x + b
y = w * x + b
# Loss = (y - 10)^2
loss = (y - 10.0) ** 2

# Backward pass (Chain rule in action!)
loss.backward()

print(f"Forward Output y: {y.item()}")
print(f"Loss Value      : {loss.item()}")
print(f"dLoss / dw      : {w.grad.item():.2f} (2 * (7 - 10) * 3 = -18.0)")
print(f"dLoss / dx      : {x.grad.item():.2f}")
print("Autograd verified successfully! 🚀")\`,
              explanation: 'Yeh script autograd ke dynamic DAG aur Chain Rule gradient calculation ko demonstrate karta hai.',
              simulationOutput: \`Forward Output y: 7.0
Loss Value      : 9.0
dLoss / dw      : -18.00 (2 * (7 - 10) * 3 = -18.0)
dLoss / dx      : -12.00
Autograd verified successfully! 🚀\`
            },
            diagramScript: \`flow TD: PyTorch Autograd Dynamic Graph
  w[w: Weight (2.0)] & x[x: Input (3.0)] --> mul[Mul Node (*)]
  mul --> wx[w * x = 6.0]
  wx & b[b: Bias (1.0)] --> add[Add Node (+)]
  add --> y[y = 7.0]
  y & target[Target = 10.0] --> sub[Sub Node (-)]
  sub --> diff[-3.0]
  diff --> sqr[Pow Node (^2)]
  sqr --> loss[Loss = 9.0]
  loss -.->|loss.backward() reverse topological traverse| w * \`,
            diagramPreset: 'paper',
            diagramAnimate: 'flow',
            actionItems: [
              'Custom loss function likhein aur analytical derivative se compare karein',
              'Multi-layer linear model train karke loss curve inspect karein'
            ],
            resources: [
              { title: 'Andrej Karpathy: Micrograd Video', url: 'https://karpathy.ai/zero-to-hero.html', type: 'course', tag: 'Tutorial' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-4',
          title: 'Module 4 Quiz: PyTorch & Autograd',
          titleUrdu: 'Module 4 Imtihan: PyTorch aur Autograd',
          passingScore: 70,
          xpReward: 300,
          badgeId: 'core_pytorch',
          questions: [
            {
              id: 'q4-1',
              question: 'Training loop mein optimizer.zero_grad() call karna kyun zaroori hota hai?',
              options: [
                'GPU ki memory free karne ke liye',
                'PyTorch default tor par gradients accumulate (add) karta rehta hai; zero_grad() na karein toh pichle batches ke gradients mix ho jate hain',
                'Model ko save karne ke liye',
                'Learning rate barhane ke liye'
              ],
              correctIndex: 1,
              explanation: 'Default gradient accumulation PyTorch ka feature hai, isliye har step par zero_grad() karna zaroori hai.',
              conceptUrdu: 'Optimizer Zero Grad Accumulation'
            }
          ]
        }
      },
      {
        id: 'mod-5',
        slug: 'attention-and-transformers',
        phaseId: 'phase-2',
        title: 'Module 5: "Attention Is All You Need" & Modern LLMs',
        titleUrdu: 'Attention aur Transformers: Q-K-V se Mini-GPT Tak',
        weekRange: 'Weeks 9–10',
        description: 'Scaled Dot-Product Attention mathematical proof, Rotary Position Embeddings (RoPE), Multi-Head Attention, Causal Masking aur Mini-GPT decoder.',
        realWorldDeliverable: {
          title: 'Roman Urdu Mini-GPT & Attention Heatmap',
          urduTitle: 'Roman Urdu Mini-GPT aur Attention Heatmap Engine',
          freelanceValue: '$550 - $1,200 / Custom Domain Language Model Demo',
          description: 'A 6-layer custom character/BPE decoder-only Transformer trained on Roman Urdu poetry and conversational corpora, complete with RoPE embeddings and an interactive attention weights heatmap visualizer.',
          steps: [
            'Tokenize Roman Urdu corpus with custom vocabulary mapping',
            'Implement Scaled Dot-Product Multi-Head Attention with Causal Lower-Triangular Mask',
            'Integrate RoPE (Rotary Position Embeddings) and RMSNorm',
            'Extract and plot token-to-token attention probability heatmaps during generation'
          ],
          outputArtifact: 'roman_urdu_mini_gpt.py + attention_weights_heatmap.png'
        },
        zeroGpuRecipe: {
          platform: 'Google Colab Free T4 (15GB VRAM)',
          vramRequired: '3.8 GB VRAM',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'from google.colab import runtime; runtime.unassign() # Disconnect immediately after Mini-GPT checkpoint export!',
          setupSnippet: '!pip install torch matplotlib seaborn tiktoken',
          launchUrl: 'https://colab.research.google.com/'
        },
        lessons: [
          {
            id: 'les-5-1',
            slug: 'scaled-dot-product-attention',
            title: 'Lesson 5.1: Scaled Dot-Product & Multi-Head Attention',
            titleUrdu: 'Scaled Dot-Product Attention Ka Mathematical Proof',
            week: 9,
            durationMinutes: 50,
            xpReward: 200,
            learningOutcomes: [
              'Derive Q-K-V attention equation and the sqrt(d_k) factor',
              'Implement Causal Autoregressive Masking in PyTorch',
              'Plot token attention weights matrix'
            ],
            romanUrduSummary: 'Transformer architecture modern AI ka dil hai! Query (jo aap dhoond rahe hain), Key (jo data ke paas hai), aur Value (actual content). sqrt(d_k) se divide karne ki wajah yeh hai ke high dimensions par dot product bohot bara ho jata hai jis se Softmax ka gradient zero ho jata hai.',
            deepDiveExplanation: 'The scale factor 1/sqrt(d_k) counters the variance growth of dot products under assumption of independent zero-mean unit-variance components. Causal masking ensures position i can only attend to positions <= i during autoregressive training.',
            realWorldDeliverable: {
              title: 'Multi-Head Attention Tensor Block',
              urduTitle: 'Multi-Head Attention Block',
              freelanceValue: '$400 / Architecture Component',
              description: 'Production Multi-Head Attention layer in pure PyTorch.',
              steps: ['Linear projections', 'Scaled dot product', 'Causal masking', 'Residual connection'],
              outputArtifact: 'mha_block.py'
            },
            zeroGpuRecipe: {
              platform: 'Google Colab Free T4 / Local CPU',
              vramRequired: '1.5 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Mini-GPT training runs smoothly on Colab Free T4.',
              setupSnippet: 'pip install torch matplotlib',
              launchUrl: 'https://colab.research.google.com/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'attention_block.py',
              code: \`import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q, K, V, mask=None):
    d_k = Q.size(-1)
    # MatMul Q and K^T scaled by sqrt(d_k)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)

    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)

    attn_probs = F.softmax(scores, dim=-1)
    output = torch.matmul(attn_probs, V)
    return output, attn_probs

# 1 batch, 4 tokens, dim 8
Q = torch.randn(1, 4, 8)
K = torch.randn(1, 4, 8)
V = torch.randn(1, 4, 8)

# Causal lower-triangular mask
mask = torch.tril(torch.ones(4, 4))
out, weights = scaled_dot_product_attention(Q, K, V, mask)

print("Attention output tensor shape:", out.shape)
print("Causal Masked Weights Row 0 (Only attends to itself):")
print(weights[0, 0].tolist())\`,
              explanation: 'Yeh script Causal mask ke sath Scaled Dot-Product Attention implement karta hai.',
              simulationOutput: \`Attention output tensor shape: torch.Size([1, 4, 8])
Causal Masked Weights Row 0 (Only attends to itself):
[1.0, 0.0, 0.0, 0.0]\`
            },
            diagramScript: \`flow TD: Scaled Dot-Product Attention Flow
  q[Query Matrix Q] & k[Key Matrix K] --> dot[MatMul: Q x K^T]
  dot --> scale[Scale by 1/sqrt(d_k)]
  scale --> mask{Causal Autoregressive Mask}
  mask --> sm[Softmax Along Columns]
  sm & v[Value Matrix V] --> out_dot[MatMul: Probs x V]
  out_dot --> proj[Output Projection] * \`,
            diagramPreset: 'grape',
            diagramAnimate: 'flow',
            actionItems: [
              'Custom 4-head MultiHeadAttention class likhein',
              'Sinusoidal vs RoPE embeddings compare karein'
            ],
            resources: [
              { title: 'The Illustrated Transformer (Jay Alammar)', url: 'https://jalammar.github.io/illustrated-transformer/', type: 'paper', tag: 'Guide' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-5',
          title: 'Module 5 Quiz: Transformers & Attention',
          titleUrdu: 'Module 5 Imtihan: Attention aur Transformers',
          passingScore: 70,
          xpReward: 350,
          badgeId: 'attention_is_all_you_need',
          questions: [
            {
              id: 'q5-1',
              question: 'Attention formula mein Q x K^T ko sqrt(d_k) se divide kyun kiya jata hai?',
              options: [
                'Execution speed barhane ke liye',
                'Taake bare dimensions par dot-products bohot bare na hon aur Softmax gradients zero na ho jayein',
                'Vectors ki length barhane ke liye',
                'Batch size double karne ke liye'
              ],
              correctIndex: 1,
              explanation: 'Without scaling by sqrt(d_k), dot products grow large in variance, pushing Softmax into regions with extremely small gradients.',
              conceptUrdu: 'Scaled Dot Product Gradient Vanishing Prevention'
            }
          ]
        }
      }
    ]
  },

  // =========================================================================
  // PHASE 3: MODERN GENAI STACK & AUTONOMOUS AGENTS (WEEKS 9–12)
  // =========================================================================
  {
    id: 'phase-3',
    slug: 'modern-genai-stack',
    number: 3,
    title: 'Phase 3: Modern GenAI Stack & Autonomous Agents',
    titleUrdu: 'Streaming APIs, Vector Databases, Advanced RAG aur Anthropic MCP Agents',
    duration: 'Weeks 9–12',
    icon: '🤖',
    description: 'Server-Sent Events (SSE) streaming, PostgreSQL pgvector, HNSW indexing, Hybrid Search with Reciprocal Rank Fusion, ColPali Visual RAG, aur Anthropic Model Context Protocol (MCP) tool agents.',
    modules: [
      {
        id: 'mod-6',
        slug: 'building-ai-apis-apps',
        phaseId: 'phase-3',
        title: 'Module 6: Building AI Applications & Modern APIs',
        titleUrdu: 'Real-Time Streaming AI APIs aur Application Architecture',
        weekRange: 'Weeks 11–12',
        description: 'Server-Sent Events (SSE), HTTP/2 token streaming, token-bucket rate limiting, Redis semantic caching, Svelte 5 streaming chat UI with abort controllers.',
        realWorldDeliverable: {
          title: 'WhatsApp/Web AI Customer Support Bot with SSE Streaming',
          urduTitle: 'WhatsApp/Web AI Customer Support Bot with SSE Streaming',
          freelanceValue: '$600 - $1,400 / E-Commerce AI Support Bot Client Setup',
          description: 'A production customer support bot supporting streaming responses via Server-Sent Events (SSE), token-bucket rate limiter, Redis semantic cache for frequent queries, and client-side abort controllers.',
          steps: [
            'Create async FastAPI/Axum streaming endpoint using EventSourceResponse / SSE',
            'Implement semantic caching with Redis: return cached responses for cosine similarity > 0.94',
            'Configure distributed token-bucket rate limiter per IP / User API key',
            'Build Svelte 5 frontend with Runes ($state), auto-scrolling stream, and instant cancel button'
          ],
          outputArtifact: 'streaming_ai_gateway.py + SvelteChatStream.svelte'
        },
        zeroGpuRecipe: {
          platform: 'Groq Free Tier (300+ tok/s) / Google AI Studio Gemini Flash Free Tier',
          vramRequired: '0 GB (Cloud Serverless Inference)',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'Groq Free Tier provides up to 30 requests/min and 14,400 req/day with ultra-fast 300+ tokens/second — zero GPU compute needed!',
          setupSnippet: 'pip install groq fastapi uvicorn sse-starlette redis',
          launchUrl: 'https://console.groq.com/'
        },
        lessons: [
          {
            id: 'les-6-1',
            slug: 'sse-token-streaming-apis',
            title: 'Lesson 6.1: Server-Sent Events (SSE) Token Streaming',
            titleUrdu: 'Real-Time Token Streaming via Server-Sent Events',
            week: 11,
            durationMinutes: 40,
            xpReward: 180,
            learningOutcomes: [
              'Understand chunked HTTP streaming vs blocking JSON responses',
              'Implement an SSE streaming endpoint with FastAPI / Axum',
              'Consume token streams in Svelte 5 with AbortController'
            ],
            romanUrduSummary: 'Jab koi LLM 500 tokens generate karta hai toh 4 se 5 seconds lagte hain. Agar aap user ko blank screen dikha kar wait karwayenge toh woh website close kar dega! SSE streaming se jaise hi pehla token banta hai (Time To First Token < 300ms), user ki screen par word-by-word type hona shuru ho jata hai.',
            deepDiveExplanation: 'Server-Sent Events operate over standard HTTP/1.1 or HTTP/2 persistent connections using content-type: text/event-stream. The server pushes data frames prefixed with "data: " without requiring WebSocket handshake overhead.',
            realWorldDeliverable: {
              title: 'FastAPI SSE Streaming Gateway',
              urduTitle: 'FastAPI SSE Streaming Gateway',
              freelanceValue: '$300 / Streaming API Endpoint',
              description: 'FastAPI streaming gateway emitting chunked tokens over SSE.',
              steps: ['Setup async generator', 'Wrap in EventSourceResponse', 'Client fetch stream'],
              outputArtifact: 'sse_gateway.py'
            },
            zeroGpuRecipe: {
              platform: 'Groq Free Tier / Local CPU',
              vramRequired: '0 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Groq API requires no local GPU.',
              setupSnippet: 'pip install fastapi sse-starlette httpx',
              launchUrl: 'https://console.groq.com/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'sse_streaming_endpoint.py',
              code: \`from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def mock_token_generator(prompt: str):
    tokens = f"Aapka sawal tha: '{prompt}'. Modern AI engineers streaming APIs use karte hain taake Time-To-First-Token sub-300ms rahe!".split()
    for token in tokens:
        await asyncio.sleep(0.08) # Simulating GPU generation latency
        yield f"data: {token} \\n\\n"
    yield "data: [DONE]\\n\\n"

@app.get("/api/chat/stream")
async def chat_stream(prompt: str = "AI Mastery"):
    return StreamingResponse(mock_token_generator(prompt), media_type="text/event-stream")

# Verification demo
async def test_client():
    async for chunk in mock_token_generator("AI Mastery"):
        print(chunk.strip(), end=" ", flush=True)

asyncio.run(test_client())\`,
              explanation: 'Yeh script Server-Sent Events (SSE) chunked token streaming generator ko demonstrate karta hai.',
              simulationOutput: \`data: Aapka data: sawal data: tha: data: 'AI data: Mastery'. data: Modern data: AI data: engineers data: streaming data: APIs data: use data: karte data: hain data: taake data: Time-To-First-Token data: sub-300ms data: rahe! data: [DONE]\`
            },
            diagramScript: \`flow LR: Server-Sent Events Streaming Architecture
  user[User Svelte 5 Browser] -> req[GET /api/chat/stream] $terminal
  req -> gw[Axum / FastAPI Gateway] $server
  gw -> llm[LLM Token Generator] $cpu
  llm -.->|Token 1 (<200ms TTFT)| user
  llm -.->|Token 2| user
  llm -.->|Token 3| user
  llm -.->|data: [DONE]| user * \`,
            diagramPreset: 'ocean',
            diagramAnimate: 'flow',
            actionItems: [
              'FastAPI mein SSE endpoint setup karein',
              'Browser mein EventSource ya fetch() stream reader test karein'
            ],
            resources: [
              { title: 'MDN Server-Sent Events Guide', url: 'https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events', type: 'tool', tag: 'Docs' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-6',
          title: 'Module 6 Quiz: AI Applications & Streaming APIs',
          titleUrdu: 'Module 6 Imtihan: Streaming APIs aur Architecture',
          passingScore: 70,
          xpReward: 300,
          badgeId: 'app_builder',
          questions: [
            {
              id: 'q6-1',
              question: 'LLM responses ke liye WebSockets ke muqable mein Server-Sent Events (SSE) kyun prefer kiye jaate hain?',
              options: [
                'SSE sirf images transfer karta hai',
                'SSE standard HTTP connection use karta hai, firewall-friendly hai, automatic reconnect support karta hai, aur unidirectional streaming ke liye zero protocol overhead deta hai',
                'WebSockets saste hote hain',
                'SSE encryption ko disable kar deta hai'
              ],
              correctIndex: 1,
              explanation: 'SSE standard HTTP/2 use karta hai aur unidirectional token streaming ke liye simplest aur most reliable protocol hai.',
              conceptUrdu: 'Server-Sent Events vs WebSockets for LLMs'
            }
          ]
        }
      },
      {
        id: 'mod-7',
        slug: 'vector-databases-and-hybrid-rag',
        phaseId: 'phase-3',
        title: 'Module 7: Vector Databases & Modern RAG Architecture',
        titleUrdu: 'Vector Databases, Hybrid RAG (pgvector + BM25) aur ColPali',
        weekRange: 'Weeks 13–14',
        description: 'Dense vector embeddings, PostgreSQL pgvector, HNSW vs IVFFlat indexes, Hybrid Search with Reciprocal Rank Fusion (RRF), Cross-Encoder reranking, aur 2026 ColPali Vision RAG.',
        realWorldDeliverable: {
          title: 'Urdu/English Legal Contract & Bank Statement Hybrid RAG',
          urduTitle: 'Urdu/English Legal Contract aur Bank Statement Hybrid RAG',
          freelanceValue: '$800 - $2,000 / Enterprise Document Search & QA Contract',
          description: 'An enterprise hybrid retrieval pipeline indexing complex financial and legal PDF documents using PostgreSQL pgvector (HNSW) + BM25 full-text search, fused with RRF (k=60), and cross-encoder reranking with citation attribution.',
          steps: [
            'Parse complex PDF tables and clauses into semantically coherent chunk windows',
            'Store chunks in Supabase PostgreSQL with pgvector using HNSW cosine index',
            'Execute parallel BM25 sparse keyword search and dense embedding search',
            'Fuse rankings with Reciprocal Rank Fusion (RRF) and rerank top 10 with FlashRank',
            'Generate grounded answers with exact page numbers and verbatim citations'
          ],
          outputArtifact: 'hybrid_rag_pipeline.py + evaluation_ragas.json'
        },
        zeroGpuRecipe: {
          platform: 'Google AI Studio Free Embeddings (text-embedding-004) + Free Supabase pgvector Cloud',
          vramRequired: '0 GB (100% Cloud Serverless)',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'Supabase Free Tier includes free PostgreSQL with pgvector; Google AI Studio provides 1,500 free embedding requests/minute — $0 infrastructure expense!',
          setupSnippet: 'pip install supabase psycopg[binary] flashrank google-genai rank_bm25',
          launchUrl: 'https://aistudio.google.com/'
        },
        lessons: [
          {
            id: 'les-7-1',
            slug: 'pgvector-hnsw-hybrid-search',
            title: 'Lesson 7.1: PostgreSQL pgvector & Hybrid Search (BM25 + Dense)',
            titleUrdu: 'pgvector HNSW Index aur Hybrid RRF Search',
            week: 13,
            durationMinutes: 45,
            xpReward: 220,
            learningOutcomes: [
              'Setup pgvector and build HNSW index in PostgreSQL',
              'Combine BM25 keyword matching with dense vector search',
              'Implement Reciprocal Rank Fusion (RRF k=60) algorithm'
            ],
            romanUrduSummary: 'Agar aap sirf vector similarity par rely karenge toh invoice numbers, legal clause numbers, ya exact names miss ho jayenge! Hybrid RAG mein hum do taqatein combine karte hain: PostgreSQL ka built-in Full-Text Search (BM25) exact words dhoondta hai, aur pgvector concept ka matlab dhoondta hai. RRF dono ko merge karke best document top par lata hai.',
            deepDiveExplanation: 'HNSW (Hierarchical Navigable Small World) provides logarithmic vector search time O(log N) through multi-layer graphs. Combining HNSW dense scores with BM25 sparse scores via Reciprocal Rank Fusion prevents score distribution mismatch.',
            realWorldDeliverable: {
              title: 'Hybrid RAG Pipeline with RRF',
              urduTitle: 'Hybrid RAG Engine with RRF',
              freelanceValue: '$500 / Search Pipeline Delivery',
              description: 'Hybrid search pipeline returning deduplicated reranked documents.',
              steps: ['Vector query', 'BM25 query', 'RRF fusion formula', 'Rerank top 5'],
              outputArtifact: 'hybrid_retriever.py'
            },
            zeroGpuRecipe: {
              platform: 'Supabase Free Tier + Google AI Studio Embeddings',
              vramRequired: '0 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Free cloud hosting for vector database and embeddings.',
              setupSnippet: 'pip install psycopg[binary] rank_bm25',
              launchUrl: 'https://supabase.com/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'hybrid_rrf_retriever.py',
              code: \`def rrf(bm25_docs, vector_docs, k=60):
    scores = {}
    for r, d in enumerate(bm25_docs):
        scores[d] = scores.get(d, 0.0) + 1.0 / (k + r + 1)
    for r, d in enumerate(vector_docs):
        scores[d] = scores.get(d, 0.0) + 1.0 / (k + r + 1)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

bm25_results = ["doc_clause_4a", "doc_bank_policy", "doc_tax_reg"]
vector_results = ["doc_tax_reg", "doc_clause_4a", "doc_general_terms"]

ranked = rrf(bm25_results, vector_results)
print("🎯 Top Fused Documents (Hybrid RRF):")
for rank, (doc, score) in enumerate(ranked, 1):
    print(f"Rank {rank}: {doc} (Score: {score:.5f})")\`,
              explanation: 'Yeh script BM25 aur Vector search ke results ko Reciprocal Rank Fusion se merge karta hai.',
              simulationOutput: \`🎯 Top Fused Documents (Hybrid RRF):
Rank 1: doc_clause_4a (Score: 0.03252)
Rank 2: doc_tax_reg (Score: 0.03252)
Rank 3: doc_bank_policy (Score: 0.01613)
Rank 4: doc_general_terms (Score: 0.01587)\`
            },
            diagramScript: \`arch LR: Hybrid RAG Architecture
  query[User Natural Language Query] -> splitter{Query Router}
  splitter ->|Exact Token| bm25[PostgreSQL BM25 Search] $database
  splitter ->|Semantic Meaning| dense[pgvector HNSW Search] $server
  bm25 & dense --> rrf[Reciprocal Rank Fusion (k=60)] $cpu
  rrf --> rerank[Cross-Encoder Reranker] $brain
  rerank --> gen[LLM Grounded Response + Citations] $lock * \`,
            diagramPreset: 'blueprint',
            diagramAnimate: 'flow',
            actionItems: [
              'Supabase mein pgvector extension enable karein',
              'HNSW index create karein with m=16, ef_construction=64',
              'RRF scoring function test karein'
            ],
            resources: [
              { title: 'pgvector Official Repository', url: 'https://github.com/pgvector/pgvector', type: 'github', tag: 'Repo' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-7',
          title: 'Module 7 Quiz: Advanced RAG Architecture',
          titleUrdu: 'Module 7 Imtihan: Advanced RAG aur Vector Search',
          passingScore: 70,
          xpReward: 350,
          badgeId: 'rag_architect',
          questions: [
            {
              id: 'q7-1',
              question: 'Reciprocal Rank Fusion (RRF) mein constant k (e.g. k=60) ka kya maqsad hota hai?',
              options: [
                'Database table lock karna',
                'Top-ranked items ke score ko smooth karna taake kisi ek search method ka rank #1 poore result ko hijack na kare',
                'GPU ki speed 60x karna',
                'Tokens ki limit set karna'
              ],
              correctIndex: 1,
              explanation: 'Smoothing constant k prevents outlier top ranks from dominating the fused ranking distribution.',
              conceptUrdu: 'Reciprocal Rank Fusion Smoothing Constant'
            }
          ]
        }
      },
      {
        id: 'mod-8',
        slug: 'autonomous-agents-and-mcp',
        phaseId: 'phase-3',
        title: 'Module 8: Autonomous Agents, MCP & Tool Use',
        titleUrdu: 'Autonomous Agents, Anthropic MCP aur smolagents',
        weekRange: 'Weeks 15–16',
        description: 'The ReAct Pattern (Thought-Action-Observation), 2026 Anthropic Model Context Protocol (MCP) servers, sandboxed tool execution, aur Hugging Face smolagents CodeAgent.',
        realWorldDeliverable: {
          title: 'Autonomous Freelance Upwork Job Scraper & Proposal Agent with MCP & smolagents',
          urduTitle: 'Autonomous Upwork Job Scraper aur Proposal Agent (MCP + smolagents)',
          freelanceValue: '$1,000 - $2,500 / Lead Gen & Agency Workflow Automation',
          description: 'An autonomous multi-step agency agent powered by Anthropic Model Context Protocol (MCP) and Hugging Face smolagents CodeAgent. It scans RSS feeds for high-ticket AI jobs, extracts client pain points, inspects GitHub repositories, and synthesizes personalized proposals.',
          steps: [
            'Create an Anthropic MCP Server exposing tools: fetch_jobs(), inspect_repo(), check_budget()',
            'Configure smolagents CodeAgent that writes executable Python code for multi-step reasoning',
            'Enforce deterministic budget filtering ($1k+ minimum, 4.8+ client rating)',
            'Generate tailored technical proposals highlighting relevant case studies with zero hallucination'
          ],
          outputArtifact: 'upwork_mcp_agent.py + mcp_server.json'
        },
        zeroGpuRecipe: {
          platform: 'Google AI Studio Gemini 2.5 Flash Free Tier / Groq Free Tier',
          vramRequired: '0 GB (Tool calling runs via free API tokens)',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'CodeAgent executes lightweight Python sandboxed loops on your local CPU while delegating reasoning to free Gemini/Groq endpoints.',
          setupSnippet: 'pip install smolagents mcp httpx pydantic',
          launchUrl: 'https://aistudio.google.com/'
        },
        lessons: [
          {
            id: 'les-8-1',
            slug: 'react-pattern-mcp-tools',
            title: 'Lesson 8.1: The ReAct Pattern & Anthropic MCP Protocol',
            titleUrdu: 'ReAct Pattern aur Anthropic Model Context Protocol',
            week: 15,
            durationMinutes: 45,
            xpReward: 240,
            learningOutcomes: [
              'Understand the ReAct Thought-Action-Observation cognitive loop',
              'Build a compliant Anthropic MCP tool server',
              'Eliminate brittle JSON tool chains with smolagents CodeAgent'
            ],
            romanUrduSummary: 'Purani LangChain chains fragile JSON strings par depend karti theen jo break ho jati theen. 2026 mein Anthropic ka Model Context Protocol (MCP) industry standard ban chuka hai. Agent ab JSON object generate karne ki bajaye direct Python code likhta hai jo execute hokar answer nikalta hai.',
            deepDiveExplanation: 'The ReAct pattern interleaves reasoning traces (Thought) and task-specific actions (Tool Calling). Anthropic MCP standardizes client-server handshakes, resources, and tool discovery over JSON-RPC 2.0 / stdio / SSE transport.',
            realWorldDeliverable: {
              title: 'Custom SQLite & Weather MCP Server',
              urduTitle: 'Production Anthropic MCP Server',
              freelanceValue: '$500 / MCP Server Build',
              description: 'Production MCP server exposing SQLite queries and search tools.',
              steps: ['Define MCP tool definitions', 'Implement JSON-RPC handler', 'Connect to Claude Desktop'],
              outputArtifact: 'mcp_server.py'
            },
            zeroGpuRecipe: {
              platform: 'Local CPU / Free Gemini Flash API',
              vramRequired: '0 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'MCP servers run purely on CPU I/O.',
              setupSnippet: 'pip install mcp smolagents',
              launchUrl: 'https://modelcontextprotocol.io/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'mcp_agent_demo.py',
              code: \`# ReAct Autonomous Agent Simulation
class ReActAgent:
    def __init__(self, tools):
        self.tools = tools

    def run(self, goal: str):
        print(f"🎯 Objective: {goal}")
        print("🧠 [Thought]: Mujhe pehle database mein active clients check karne chahiye.")
        action_result = self.tools['query_db']("SELECT count(*) FROM clients WHERE status='active'")
        print(f"⚡ [Action]: query_db() -> [Observation]: {action_result}")
        print(f"🧠 [Thought]: Active clients {action_result} hain. Ab budget estimate calculate karta hoon.")
        print("✅ [Final Answer]: System mein 42 active clients hain, jin par total projected revenue \$84,000 hai.")

tools = {'query_db': lambda q: 42}
agent = ReActAgent(tools)
agent.run("Active clients aur revenue report prepare karo")\`,
              explanation: 'Yeh script ReAct pattern ke Thought, Action, aur Observation execution loop ko illustrate karta hai.',
              simulationOutput: \`🎯 Objective: Active clients aur revenue report prepare karo
🧠 [Thought]: Mujhe pehle database mein active clients check karne chahiye.
⚡ [Action]: query_db() -> [Observation]: 42
🧠 [Thought]: Active clients 42 hain. Ab budget estimate calculate karta hoon.
✅ [Final Answer]: System mein 42 active clients hain, jin par total projected revenue $84,000 hai.\`
            },
            diagramScript: \`seq: ReAct Autonomous Agent Execution Cycle
  User -> Agent: "Research Top Upwork AI Jobs"
  loop Thought-Action-Observation
    Agent -> Agent: Thought: Identify Search Query
    Agent -> MCP_Tools: Action: fetch_jobs(tag='ai-engineer')
    MCP_Tools --> Agent: Observation: 12 High-Value Jobs Found
    Agent -> Agent: Thought: Filter budget > $2,000
    Agent -> MCP_Tools: Action: draft_proposal(job_id=4)
    MCP_Tools --> Agent: Observation: Draft Ready
  end
  Agent -> User: Final Report + Personalized Proposals * \`,
            diagramPreset: 'midnight',
            diagramAnimate: 'flow',
            actionItems: [
              'Ek custom Python function ko MCP tool ke tor par expose karein',
              'smolagents CodeAgent initialize karke multi-step query solve karein'
            ],
            resources: [
              { title: 'Anthropic Model Context Protocol Specs', url: 'https://modelcontextprotocol.io/', type: 'tool', tag: 'Standard' },
              { title: 'Hugging Face smolagents Docs', url: 'https://huggingface.co/docs/smolagents', type: 'tool', tag: 'Library' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-8',
          title: 'Module 8 Quiz: Autonomous Agents & Tool Calling',
          titleUrdu: 'Module 8 Imtihan: Autonomous Agents aur MCP',
          passingScore: 70,
          xpReward: 350,
          badgeId: 'agent_commander',
          questions: [
            {
              id: 'q8-1',
              question: 'Anthropic Model Context Protocol (MCP) ka sab se bara faida kya hai?',
              options: [
                'Yeh Python ko C++ mein convert karta hai',
                'Yeh AI models aur external tools/databases ke darmiyan ek universal open standard protocol banata hai taake har tool ko har model ke liye alag se code na karna pare',
                'Yeh internet connection khatam kar deta hai',
                'Yeh model ke parameters double karta hai'
              ],
              correctIndex: 1,
              explanation: 'MCP is an open standard enabling secure, standardized connections between AI applications and data sources/tools.',
              conceptUrdu: 'Model Context Protocol (MCP) Standard'
            }
          ]
        }
      }
    ]
  },

  // =========================================================================
  // PHASE 4: FINE-TUNING & PRODUCTION MLOPS (WEEKS 13–16)
  // =========================================================================
  {
    id: 'phase-4',
    slug: 'finetuning-and-mlops',
    number: 4,
    title: 'Phase 4: Fine-Tuning & Production MLOps',
    titleUrdu: 'Model Adaptation, Unsloth QLoRA, DeepSeek-R1 GRPO aur Rust Axum Serving',
    duration: 'Weeks 13–16',
    icon: '🔥',
    description: 'Unsloth 4-bit QLoRA, DeepSeek-R1 Group Relative Policy Optimization (GRPO), AI Safety with Ragas, vLLM continuous batching, aur sub-50ms Rust Axum microservices.',
    modules: [
      {
        id: 'mod-9',
        slug: 'finetuning-unsloth-deepseek',
        phaseId: 'phase-4',
        title: 'Module 9: Fine-Tuning & Model Adaptation (Unsloth, DeepSeek-R1 GRPO)',
        titleUrdu: 'Model Fine-Tuning: Unsloth 4-bit QLoRA aur DeepSeek-R1 GRPO Reasoning',
        weekRange: 'Weeks 17–18',
        description: 'Parameter-Efficient Fine-Tuning (PEFT), Low-Rank Adaptation (LoRA), Unsloth fast Triton kernels, aur DeepSeek-R1 rule-based reasoning RL without critic models.',
        realWorldDeliverable: {
          title: 'Unsloth 4-bit QLoRA & DeepSeek-R1 GRPO Fine-Tuning on Free Colab T4',
          urduTitle: 'Unsloth 4-bit QLoRA aur DeepSeek-R1 GRPO Fine-Tuning on Free Colab T4',
          freelanceValue: '$1,200 - $3,000 / Custom Domain Fine-Tuning Gig',
          description: 'A complete fine-tuning pipeline on free Google Colab T4: quantizes Llama-3.1-8B to 4-bit NF4, trains low-rank adapters in <45 minutes with Unsloth Triton kernels, and applies GRPO group reward optimization for structured <think> reasoning tokens.',
          steps: [
            'Load Llama-3.1-8B in 4-bit NormalFloat (NF4) using FastLanguageModel from Unsloth',
            'Attach LoRA rank adapters (r=16, alpha=16) targeting all attention and MLP projection layers',
            'Train on Roman Urdu domain Q&A dataset with zero CUDA out-of-memory errors',
            'Implement GRPO rule-based reward checking mathematical correctness and <think> tag format',
            'Export fine-tuned model to 4-bit GGUF for instant local inference in Ollama'
          ],
          outputArtifact: 'unsloth_finetune.ipynb + lora_model_q4.gguf'
        },
        zeroGpuRecipe: {
          platform: 'Google Colab Free T4 (15GB VRAM) / Kaggle Dual-T4 (30GB VRAM, 30h/wk Free)',
          vramRequired: '7.2 GB VRAM (Fits easily in 15GB T4!)',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'from google.colab import runtime; runtime.unassign() # Save your compute units the moment GGUF export completes!',
          setupSnippet: '!pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git" --no-deps',
          launchUrl: 'https://colab.research.google.com/'
        },
        lessons: [
          {
            id: 'les-9-1',
            slug: 'unsloth-qlora-triton-math',
            title: 'Lesson 9.1: QLoRA 4-bit NF4 Quantization & Unsloth Triton Kernels',
            titleUrdu: 'Unsloth 4-Bit QLoRA aur Custom GPU Kernels',
            week: 17,
            durationMinutes: 45,
            xpReward: 260,
            learningOutcomes: [
              'Understand Low-Rank Adaptation (LoRA) matrix factorization',
              'Explain NF4 (NormalFloat4) quantization mechanics',
              'Train an 8B model on Colab Free T4 in 40 minutes'
            ],
            romanUrduSummary: 'Pehle 8B model fine-tune karne ke liye \$10,000 ka A100 GPU chahiye hota tha. Unsloth ne OpenAI Triton mein custom GPU kernels likhe jo memory consumption ko 70% kam aur training speed ko 4x barha dete hain. Is lesson mein hum dekhenge ke Llama-3.1-8B model Free Colab T4 par kaise train hota hai!',
            deepDiveExplanation: 'LoRA factorizes weight update matrix Delta W into B * A where rank r << min(d, k). 4-bit NormalFloat (NF4) builds an information-theoretically optimal quantile grid for normally distributed neural network weights, preserving accuracy while cutting memory 4x.',
            realWorldDeliverable: {
              title: 'Colab Unsloth Fine-Tuning Notebook',
              urduTitle: 'Unsloth 4-bit QLoRA Notebook',
              freelanceValue: '$600 / Fine-Tuning Deliverable',
              description: 'Colab notebook fine-tuning Llama-3.1-8B in 4-bit with Unsloth.',
              steps: ['Load model in NF4', 'Setup LoRA config', 'Train 100 steps', 'Export GGUF'],
              outputArtifact: 'unsloth_pipeline.py'
            },
            zeroGpuRecipe: {
              platform: 'Google Colab Free T4 (15GB VRAM)',
              vramRequired: '7.2 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Unsloth is officially certified to fit inside Colab Free 15GB T4 memory limits.',
              setupSnippet: '!pip install unsloth',
              launchUrl: 'https://colab.research.google.com/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'unsloth_trainer_demo.py',
              code: \`# Unsloth Fine-Tuning Configuration Demo
def calculate_qlora_footprint(base_params_b=8, rank=16):
    # 4-bit base weights: 8B * 0.5 bytes = ~4.0 GB
    base_vram = base_params_b * 0.5
    # LoRA adapters: ~150MB
    adapter_vram = 0.15
    # Activations with Unsloth gradient checkpointing: ~2.8 GB
    activation_vram = 2.8
    total = base_vram + adapter_vram + activation_vram
    return total

vram_needed = calculate_qlora_footprint(8, 16)
print(f"Total VRAM for 8B Model Fine-Tuning: {vram_needed:.2f} GB")
print(f"Google Colab T4 Free Memory Available: 15.0 GB")
print(f"Headroom Remaining: {15.0 - vram_needed:.2f} GB -> ZERO OOM ERRORS! 🚀")\`,
              explanation: 'Yeh calculation demonstrate karti hai ke Unsloth 4-bit QLoRA 15GB Colab T4 par easily run hota hai.',
              simulationOutput: \`Total VRAM for 8B Model Fine-Tuning: 6.95 GB
Google Colab T4 Free Memory Available: 15.0 GB
Headroom Remaining: 8.05 GB -> ZERO OOM ERRORS! 🚀\`
            },
            diagramScript: \`layers: LoRA Low-Rank Decomposition
  layer 4 - Forward Pass: Y = (W_0 * X) + (B * A * X) * (alpha / r)
  layer 3 - Trainable Matrix B: [4096 x 16] - Initialized to Zero
  layer 2 - Trainable Matrix A: [16 x 4096] - Gaussian Init
  layer 1 - Frozen Base Weights W_0: [4096 x 4096] (4-bit NF4 Quantized) * \`,
            diagramPreset: 'forest',
            diagramAnimate: 'flow',
            actionItems: [
              'Colab T4 par Unsloth notebook launch karein',
              'Apna custom Roman Urdu dataset load karein',
              'Training loss curve inspect karein'
            ],
            resources: [
              { title: 'Unsloth Official Documentation', url: 'https://docs.unsloth.ai/', type: 'tool', tag: 'Library' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-9',
          title: 'Module 9 Quiz: Fine-Tuning & Model Adaptation',
          titleUrdu: 'Module 9 Imtihan: LoRA aur DeepSeek-R1 GRPO',
          passingScore: 70,
          xpReward: 400,
          badgeId: 'finetuning_pro',
          questions: [
            {
              id: 'q9-1',
              question: 'DeepSeek-R1 ke Group Relative Policy Optimization (GRPO) ne standard PPO ke muqable mein konsa bara masla hal kiya?',
              options: [
                'Internet speed 10x barha di',
                'Critic/Value network ko eliminate kiya jo 50% GPU memory leta tha, aur group normalization se advantage nikala',
                'Python ko delete kar diya',
                'Tokens ki limit 100 kardi'
              ],
              correctIndex: 1,
              explanation: 'GRPO calculates advantages from group output rewards, completely eliminating the need for a separate Critic model network.',
              conceptUrdu: 'DeepSeek-R1 GRPO Advantage Calculation'
            }
          ]
        }
      },
      {
        id: 'mod-10',
        slug: 'ai-safety-evals-guardrails',
        phaseId: 'phase-4',
        title: 'Module 10: Enterprise AI Safety, Evaluation & Guardrails',
        titleUrdu: 'Enterprise AI Safety, Guardrails aur Ragas Automated Evals',
        weekRange: 'Weeks 19–20',
        description: 'The RAG Triad, Ragas automated evaluation metrics, Faithfulness, Context Precision, prompt injection reverse proxies, PII scrubbing, aur NeMo guardrails.',
        realWorldDeliverable: {
          title: 'Enterprise AI Security Firewall & Prompt Injection Proxy',
          urduTitle: 'Enterprise AI Security Firewall aur Prompt Injection Proxy',
          freelanceValue: '$750 - $1,800 / Enterprise Security & Compliance Audit',
          description: 'A security reverse proxy deployed in front of enterprise LLMs that scrubs Personally Identifiable Information (CNIC, phone, credit cards), classifies adversarial prompt injections via regex & semantic cosine bounds, and logs telemetry to an audit dashboard.',
          steps: [
            'Implement PII detection and token replacement filter using Presidio / Regex patterns',
            'Classify jailbreaks (DAN, developer mode, system prompt leaks) with sub-10ms semantic embeddings',
            'Setup automated Ragas evaluation pipeline testing Faithfulness and Answer Relevance',
            'Deploy security proxy as a Cloudflare Worker / Docker container'
          ],
          outputArtifact: 'ai_security_firewall.py + ragas_test_suite.json'
        },
        zeroGpuRecipe: {
          platform: 'Local CPU / Free Cloudflare Workers / Railway Free Tier',
          vramRequired: '0 GB (Pure CPU Pattern Matching & Embeddings)',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'Security filtering and evaluation scripts execute completely on CPU without consuming GPU resources.',
          setupSnippet: 'pip install ragas presidio-analyzer presidio-anonymizer',
          launchUrl: 'https://docs.ragas.io/'
        },
        lessons: [
          {
            id: 'les-10-1',
            slug: 'ragas-evaluation-guardrails',
            title: 'Lesson 10.1: The RAG Triad & Ragas Automated Evaluation',
            titleUrdu: 'RAG Triad aur Ragas Automated Evaluation Metrics',
            week: 19,
            durationMinutes: 40,
            xpReward: 250,
            learningOutcomes: [
              'Understand the RAG Triad: Context Relevance, Groundedness, Answer Relevance',
              'Run automated CI/CD evaluation benchmarks with Ragas',
              'Detect and block indirect prompt injection attacks'
            ],
            romanUrduSummary: 'Client ko model deliver karne se pehle aapko prove karna hota hai ke model jhooti batein (hallucinations) nahi kar raha. Ragas library synthetic questions banati hai aur LLM-as-a-Judge ke zariye 0 se 1 tak Faithfulness aur Context Precision ka exact score deti hai.',
            deepDiveExplanation: 'The RAG Triad decomposes evaluation into: 1) Context Relevance (did retrieval find the needle?), 2) Groundedness/Faithfulness (is the answer 100% justified by context?), and 3) Answer Relevance (did it directly address user intent?).',
            realWorldDeliverable: {
              title: 'Automated Ragas CI/CD Evaluation Suite',
              urduTitle: 'Automated Ragas CI/CD Suite',
              freelanceValue: '$400 / Eval Suite Delivery',
              description: 'Automated Python evaluation script generating Ragas benchmark scores.',
              steps: ['Create evaluation dataset', 'Run Ragas evaluate()', 'Assert faithfulness > 0.85'],
              outputArtifact: 'evaluate_rag.py'
            },
            zeroGpuRecipe: {
              platform: 'Local CPU + Free Gemini Flash API',
              vramRequired: '0 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Evaluation uses lightweight LLM-as-a-judge calls over free API tier.',
              setupSnippet: 'pip install ragas datasets',
              launchUrl: 'https://docs.ragas.io/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'rag_guardrail_check.py',
              code: \`# RAG Groundedness Guardrail Simulation
def verify_faithfulness(context: str, answer: str) -> float:
    # Check if key claims in answer are present in the retrieved context
    answer_tokens = set(answer.lower().split())
    context_tokens = set(context.lower().split())
    supported = answer_tokens.intersection(context_tokens)
    faithfulness_score = len(supported) / len(answer_tokens)
    return faithfulness_score

ctx = "Enterprise plan ki qeemat \$49 per month hai aur isme 100k tokens shamil hain."
ans1 = "Enterprise plan \$49 per month ka hai."
ans2 = "Enterprise plan \$49 ka hai aur isme unlimited GPU hours milte hain." # Hallucination!

print(f"Answer 1 Faithfulness: {verify_faithfulness(ctx, ans1):.2f} (Safe & Grounded)")
print(f"Answer 2 Faithfulness: {verify_faithfulness(ctx, ans2):.2f} (Flagged Hallucination!)")\`,
              explanation: 'Yeh script RAG responses ki context groundedness aur hallucination score ko verify karta hai.',
              simulationOutput: \`Answer 1 Faithfulness: 1.00 (Safe & Grounded)
Answer 2 Faithfulness: 0.58 (Flagged Hallucination!)\`
            },
            diagramScript: \`flow TD: RAG Triad Evaluation Loop
  query[User Query] --> cr{Context Relevance}
  ctx[Retrieved Context] --> cr
  ctx --> faith{Faithfulness / Groundedness}
  ans[LLM Generated Answer] --> faith
  query --> ar{Answer Relevance}
  ans --> ar
  cr & faith & ar --> score[Automated Ragas Score: 0.94 / 1.0] * \`,
            diagramPreset: 'paper',
            diagramAnimate: 'pulse',
            actionItems: [
              'Ragas install karein aur 5 sample test cases run karein',
              'Faithfulness metric < 0.80 par automated alert trigger karein'
            ],
            resources: [
              { title: 'Official Ragas Documentation', url: 'https://docs.ragas.io/', type: 'tool', tag: 'Docs' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-10',
          title: 'Module 10 Quiz: AI Safety & Evaluation',
          titleUrdu: 'Module 10 Imtihan: AI Safety aur Guardrails',
          passingScore: 70,
          xpReward: 350,
          badgeId: 'production_ready',
          questions: [
            {
              id: 'q10-1',
              question: 'RAG Triad mein "Faithfulness" metric kya evaluate karta hai?',
              options: [
                'Model ki response generation speed',
                'Kya generated answer mein likhi har baat retrieved context se 100% saabit hoti hai ya model ne khud se fabricate (hallucinate) kiya hai',
                'User ka mood',
                'Database connection status'
              ],
              correctIndex: 1,
              explanation: 'Faithfulness verifies that every claim in the generated answer is grounded in the retrieved context.',
              conceptUrdu: 'Ragas Faithfulness Evaluation'
            }
          ]
        }
      },
      {
        id: 'mod-11',
        slug: 'production-ai-serving-vllm-rust',
        phaseId: 'phase-4',
        title: 'Module 11: Production AI Engineering & High-Throughput Serving (vLLM, Rust)',
        titleUrdu: 'High-Throughput AI Serving: vLLM, PagedAttention aur Rust Axum',
        weekRange: 'Weeks 21–22',
        description: 'KV Cache memory wall, vLLM PagedAttention, continuous batching, chunked prefill, sub-50ms high-scale Rust Axum microservices, OpenTelemetry tracing.',
        realWorldDeliverable: {
          title: 'Sub-50ms Rust Axum High-Scale AI Gateway',
          urduTitle: 'Sub-50ms Rust Axum High-Scale AI Gateway',
          freelanceValue: '$1,500 - $3,500 / High-Performance AI Infrastructure Build',
          description: 'A high-concurrency reverse proxy and AI gateway built with Rust Axum 0.8, featuring zero-copy token streaming, Redis token-bucket rate limiting, automatic failover between LLM providers (Groq/DeepSeek), and OpenTelemetry Prometheus latency metrics.',
          steps: [
            'Implement multi-threaded asynchronous Rust Axum server with Tokio runtime',
            'Build zero-allocation streaming SSE reverse proxy pipeline relaying LLM tokens',
            'Integrate Redis-backed token-bucket rate limiter with sub-millisecond overhead',
            'Export OpenTelemetry Prometheus metrics tracking p99 Time-To-First-Token (TTFT)'
          ],
          outputArtifact: 'Cargo.toml + src/main.rs (Rust Gateway) + Dockerfile'
        },
        zeroGpuRecipe: {
          platform: 'Local Machine (Rust cargo) / Free Docker on Render / Koyeb',
          vramRequired: '0 GB (Gateway operates as a high-speed CPU proxy to remote APIs)',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'The Rust Axum gateway consumes less than 15MB of RAM on your local CPU while routing thousands of requests/sec.',
          setupSnippet: 'cargo new rust-ai-gateway && cd rust-ai-gateway',
          launchUrl: 'https://github.com/tokio-rs/axum'
        },
        lessons: [
          {
            id: 'les-11-1',
            slug: 'vllm-paged-attention-rust-gateway',
            title: 'Lesson 11.1: Solving the KV-Cache Wall with vLLM PagedAttention',
            titleUrdu: 'vLLM PagedAttention aur Rust Axum Gateway',
            week: 21,
            durationMinutes: 45,
            xpReward: 280,
            learningOutcomes: [
              'Understand the KV-cache memory wall and fragmentation in LLMs',
              'Explain how PagedAttention borrows OS virtual memory paging',
              'Build a Rust Axum microservice that acts as a low-latency gateway'
            ],
            romanUrduSummary: 'Python Flask ya Streamlit high-scale production mein fail ho jate hain kyunke single process high concurrency ko handle nahi kar sakta. Rust Axum compile hokar machine code banta hai aur sub-millisecond latency deta hai. Doosri taraf vLLM GPU memory ko virtual memory blocks mein divide karke throughput 4x barha deta hai.',
            deepDiveExplanation: 'Traditional LLM serving pre-allocates contiguous memory for maximum context length, wasting 60-80% VRAM. vLLM PagedAttention partitions KV cache into fixed-size physical blocks with dynamic block tables. Combining this with a compiled Rust gateway delivers enterprise-grade SLAs.',
            realWorldDeliverable: {
              title: 'Rust Axum Sub-Millisecond Proxy',
              urduTitle: 'Rust Axum Streaming Proxy',
              freelanceValue: '$800 / High-Scale Infrastructure',
              description: 'Rust Axum proxy dispatching concurrent streaming requests.',
              steps: ['Create Axum route', 'Implement Tokio streaming body', 'Compile release binary'],
              outputArtifact: 'main.rs'
            },
            zeroGpuRecipe: {
              platform: 'Local Machine (Rust cargo)',
              vramRequired: '0 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Cargo builds natively on your CPU with zero cloud costs.',
              setupSnippet: 'cargo check',
              launchUrl: 'https://docs.rs/axum/latest/axum/'
            },
            codeSnippet: {
              language: 'rust',
              filename: 'axum_gateway_sample.rs',
              code: \`// High-Performance Rust Axum 0.8 AI Proxy
use std::time::Instant;

fn simulate_gateway_routing(prompt: &str) -> (u16, u128, &'static str) {
    let start = Instant::now();
    // Non-blocking zero-copy route resolution
    let provider = if prompt.len() > 100 { "deepseek-r1" } else { "groq-llama3" };
    let elapsed_micros = start.elapsed().as_micros();
    (200, elapsed_micros, provider)
}

fn main() {
    let prompt = "Explain Backpropagation in Roman Urdu";
    let (status, latency, provider) = simulate_gateway_routing(prompt);
    println!("🦀 Rust Axum Gateway Dispatched!");
    println!("Status Code : {}", status);
    println!("Latency     : {} microseconds (<0.1ms overhead!)", latency);
    println!("Routed To   : {}", provider);
}\`,
              explanation: 'Yeh script Rust Axum ke zero-allocation microsecond routing overhead ko simulate karta hai.',
              simulationOutput: \`🦀 Rust Axum Gateway Dispatched!
Status Code : 200
Latency     : 2 microseconds (<0.1ms overhead!)
Routed To   : groq-llama3\`
            },
            diagramScript: \`arch LR: Rust Axum 0.8 to vLLM Serving Topology
  client[10,000 Concurrent Users] $browser -> rust_gw[Rust Axum 0.8 Gateway (<1ms latency)] $server *
  rust_gw -> redis[(Redis Token-Bucket Rate Limiter)] $database
  rust_gw -> vllm[vLLM Inference Cluster] $cpu
  vllm -> paged[PagedAttention Dynamic KV Cache Blocks] $database
  vllm -.->|Streaming SSE Tokens| rust_gw
  rust_gw -.->|Direct Zero-Copy Stream| client\`,
            diagramPreset: 'paper',
            diagramAnimate: 'flow',
            actionItems: [
              'Rust toolchain install karein (curl --proto "=https" --tlsv1.2 -sSf https://sh.rustup.rs | sh)',
              'Axum 0.8 simple ping-pong service compile karein',
              'Release mode mein build karke binary size inspect karein'
            ],
            resources: [
              { title: 'Rust Axum Documentation', url: 'https://docs.rs/axum/latest/axum/', type: 'tool', tag: 'Docs' },
              { title: 'vLLM Official Docs', url: 'https://docs.vllm.ai/', type: 'tool', tag: 'Docs' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-11',
          title: 'Module 11 Quiz: Rust AI Systems & vLLM',
          titleUrdu: 'Module 11 Imtihan: High-Scale AI Systems',
          passingScore: 70,
          xpReward: 400,
          badgeId: 'rust_turbo',
          questions: [
            {
              id: 'q11-1',
              question: 'vLLM PagedAttention ka bunyadi principle computer science ke kis classical concept se liya gaya hai?',
              options: [
                'Relational Database Indexing',
                'Operating System Virtual Memory Paging aur Page Tables',
                'DNS Resolution',
                'Garbage Collection'
              ],
              correctIndex: 1,
              explanation: 'PagedAttention adapts Operating System virtual memory paging to allocate non-contiguous physical GPU blocks for KV caches.',
              conceptUrdu: 'Operating System Virtual Memory Paging in vLLM'
            }
          ]
        }
      }
    ]
  },

  // =========================================================================
  // PHASE 5: SPECIALIZATION TRACKS, EDGE AI & CAPSTONE (WEEKS 17–20)
  // =========================================================================
  {
    id: 'phase-5',
    slug: 'specialization-and-capstone',
    number: 5,
    title: 'Phase 5: Specialization Tracks, Edge AI & Enterprise Capstone',
    titleUrdu: 'Multimodal AI, In-Browser WebGPU, Specialization Tracks aur Final Capstone',
    duration: 'Weeks 17–20',
    icon: '👑',
    description: 'Vision-Language Models (CLIP, Whisper), 100% offline in-browser WebGPU, 3 Career Specialization Tracks, aur full-scale multi-tenant Enterprise Capstone project.',
    modules: [
      {
        id: 'mod-12',
        slug: 'multimodal-ai-vision-voice',
        phaseId: 'phase-5',
        title: 'Module 12: Multimodal AI & Vision-Language Models (CLIP, Whisper)',
        titleUrdu: 'Multimodal AI: Tasweerein, Awaaz (Whisper) aur Vision Models',
        weekRange: 'Weeks 23–24',
        description: 'CLIP joint embedding spaces, Vision Transformers (ViT), Whisper speech-to-text, Silero Voice Activity Detection (VAD), aur Vision-Language document parsing.',
        realWorldDeliverable: {
          title: 'Voice WhatsApp Note Transcriber & Urdu Receipt Vision Scanner',
          urduTitle: 'Voice WhatsApp Note Transcriber aur Urdu Receipt Vision Scanner',
          freelanceValue: '$700 - $1,600 / Small Business Voice & Accounting Automation',
          description: 'A multimodal application that ingests WhatsApp audio voice notes in Urdu/English, runs Silero VAD audio segmentation and Whisper transcription, and pairs with Gemini Flash / Qwen-VL to parse handwritten grocery/pharmacy receipts into structured JSON expense ledgers.',
          steps: [
            'Chunk audio streams with Silero VAD to strip silence and ambient noise',
            'Transcribe audio chunks with Whisper into clean Urdu and English transcripts',
            'Send mobile receipt photos to Vision LLM with JSON schema prompt extraction',
            'Store line items, prices, and tax breakdown in Supabase database'
          ],
          outputArtifact: 'multimodal_scanner.py + parsed_expenses.json'
        },
        zeroGpuRecipe: {
          platform: 'Google AI Studio Gemini 2.5 Flash Free Tier / Groq Whisper Free Tier',
          vramRequired: '0 GB (Cloud Serverless Multi-Modal API)',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'Groq provides free Whisper-large-v3 transcription at 200x realtime speed without using any local GPU VRAM!',
          setupSnippet: 'pip install google-genai soundfile pillow pydantic groq',
          launchUrl: 'https://console.groq.com/'
        },
        lessons: [
          {
            id: 'les-12-1',
            slug: 'whisper-vision-models-clip',
            title: 'Lesson 12.1: Joint Multimodal Spaces with CLIP & ViT',
            titleUrdu: 'CLIP aur Vision Transformers Ka Joint Embedding Space',
            week: 23,
            durationMinutes: 45,
            xpReward: 250,
            learningOutcomes: [
              'Understand how CLIP maps text and image pixels into the same vector space',
              'Build zero-shot image classification and visual search with pure cosine distance',
              'Process speech with Whisper and Silero Voice Activity Detection'
            ],
            romanUrduSummary: 'Pehle computer vision aur NLP bilkul alag fields theen. OpenAI ke CLIP ne dono ko ek hi vector space mein daal diya! Iska matlab yeh hai ke agar aap "lal rang ki gaari" ka text embedding nikalenge aur laal car ki picture ka image embedding nikalenge, dono ka dot-product bohot high aayega!',
            deepDiveExplanation: 'CLIP uses contrastive cross-entropy loss over a batch of (image, text) pairs. Vision Transformers slice images into 16x16 pixel patches, treating them as token embeddings passed through standard Transformer encoders.',
            realWorldDeliverable: {
              title: 'Zero-Shot Product Image Search',
              urduTitle: 'Zero-Shot Visual Search Engine',
              freelanceValue: '$400 / Visual Search Engine',
              description: 'Visual similarity search finding matching product photos from text queries.',
              steps: ['Generate text vector', 'Calculate cosine with image vectors', 'Return top matches'],
              outputArtifact: 'clip_search.py'
            },
            zeroGpuRecipe: {
              platform: 'Google AI Studio / Groq Whisper Free Tier',
              vramRequired: '0 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Multimodal APIs process images and audio on remote cloud servers for free.',
              setupSnippet: 'pip install pillow google-genai',
              launchUrl: 'https://aistudio.google.com/'
            },
            codeSnippet: {
              language: 'python',
              filename: 'multimodal_search.py',
              code: \`# Simulated Multimodal Vector Alignment (CLIP Style)
import numpy as np

# In joint latent space, related image and text have high cosine similarity
text_emb = np.array([0.8, 0.4, 0.1, 0.0]) # "A cozy coffee mug on wooden desk"
img_mug  = np.array([0.78, 0.42, 0.08, 0.05]) # Image of coffee mug
img_car  = np.array([0.05, 0.1, 0.9, 0.85])  # Image of sports car

def cos_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(f"Similarity (Text 'Mug', Image 'Mug'): {cos_sim(text_emb, img_mug):.4f} (High Match!)")
print(f"Similarity (Text 'Mug', Image 'Car'): {cos_sim(text_emb, img_car):.4f} (Low Match)")\`,
              explanation: 'Yeh script text aur image embeddings ke joint multimodal space alignment ko demonstrate karta hai.',
              simulationOutput: \`Similarity (Text 'Mug', Image 'Mug'): 0.9984 (High Match!)
Similarity (Text 'Mug', Image 'Car'): 0.1654 (Low Match)\`
            },
            diagramScript: \`flow LR: CLIP Multimodal Joint Latent Space
  img[Image: 16x16 Pixel Patches] -> vit[Vision Transformer ViT]
  txt[Text: "Red Sports Car"] -> nlp[Text Transformer]
  vit --> joint((Joint Multimodal Vector Space))
  nlp --> joint
  joint -.-> match["High Cosine Dot Product = 0.96!"] * \`,
            diagramPreset: 'forest',
            diagramAnimate: 'pulse',
            actionItems: [
              'Free Gemini Flash API se image understanding query execute karein',
              'Whisper se ek 10-second voice note transcribe karein'
            ],
            resources: [
              { title: 'OpenAI CLIP Research Paper', url: 'https://arxiv.org/abs/2103.00020', type: 'paper', tag: 'Paper' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-12',
          title: 'Module 12 Quiz: Multimodal AI & Vision',
          titleUrdu: 'Module 12 Imtihan: Multimodal AI',
          passingScore: 70,
          xpReward: 350,
          badgeId: 'production_ready',
          questions: [
            {
              id: 'q12-1',
              question: 'CLIP architecture mein Text Encoder aur Image Encoder kis cheez ko optimize karte hain?',
              options: [
                'Dono ke output vectors ko alag alag databases mein save karna',
                'Matching (Image, Text) pairs ke dot product ko maximize aur non-matching pairs ke dot product ko minimize karna (Contrastive Loss)',
                'Images ko JPEG mein compress karna',
                'Audio ki volume barhana'
              ],
              correctIndex: 1,
              explanation: 'CLIP uses contrastive learning to pull matching image-text representations together while pushing non-matching pairs apart.',
              conceptUrdu: 'CLIP Contrastive Learning Mechanics'
            }
          ]
        }
      },
      {
        id: 'mod-13',
        slug: 'local-ai-edge-webgpu',
        phaseId: 'phase-5',
        title: 'Module 13: Local AI, Edge Devices & In-Browser WebGPU',
        titleUrdu: 'Local AI: Ollama, GGUF Quantization aur In-Browser WebGPU',
        weekRange: 'Weeks 25–26',
        description: 'Quantization mechanics (FP16 to INT8, INT4, AWQ, GGUF), llama.cpp, Ollama local serving, aur Transformers.js ke zariye zero-server-cost in-browser WebGPU inference.',
        realWorldDeliverable: {
          title: '100% Offline In-Browser WebGPU Chatbot',
          urduTitle: '100% Offline In-Browser WebGPU Chatbot',
          freelanceValue: '$600 - $1,400 / 100% Private Offline In-Browser AI Solution',
          description: 'A completely offline, zero-server-cost AI chatbot that runs directly in the user browser via WebGPU using Transformers.js v3. Zero API keys, zero backend servers, zero hosting bills, and 100% data privacy for confidential documents.',
          steps: [
            'Configure Transformers.js v3 pipeline utilizing navigator.gpu WebGPU backend',
            'Download and cache quantized SmolLM2-135M / Qwen-2.5-0.5B in client IndexedDB',
            'Execute streaming text generation with web worker concurrency',
            'Ensure full functionality while computer is completely disconnected from internet'
          ],
          outputArtifact: 'webgpu_chatbot.html + index.js'
        },
        zeroGpuRecipe: {
          platform: '100% Client-Side WebGPU / In-Browser (Zero Cloud GPU Required)',
          vramRequired: 'Integrated GPU / CPU WebGPU Buffer (<800MB RAM)',
          estimatedCost: '$0.00 Free',
          computeUnitsTip: 'WebGPU shaders execute directly on the end-user machine (Intel, AMD, Apple Silicon, or Nvidia). You pay exactly $0.00 in cloud bills forever!',
          setupSnippet: 'npm install @huggingface/transformers',
          launchUrl: 'https://huggingface.co/docs/transformers.js/'
        },
        lessons: [
          {
            id: 'les-13-1',
            slug: 'in-browser-webgpu-ollama',
            title: 'Lesson 13.1: Zero-Server-Cost In-Browser WebGPU Inference',
            titleUrdu: 'Browser Ke Andar WebGPU Se AI Model Run Karna',
            week: 25,
            durationMinutes: 45,
            xpReward: 260,
            learningOutcomes: [
              'Understand WebGPU compute shaders vs WebGL limitations',
              'Run quantized Small Language Models (SLMs) in browser with Transformers.js',
              'Deploy Ollama and llama.cpp locally on laptop'
            ],
            romanUrduSummary: 'Imagine karein ke aapka client chahta hai ke uske confidential legal ya medical documents internet par kisi server ko na bheje jayein. WebGPU ke sath AI model user ke apne browser ke andar run hota hai! Server ka kharcha \$0, privacy 100%, aur offline bhi chal sakta hai.',
            deepDiveExplanation: 'WebGPU provides direct low-overhead access to modern GPU hardware via WGSL (WebGPU Shading Language). When combined with ONNX Runtime Web and quantized int4 weights, lightweight models like Qwen-2.5-0.5B generate 30+ tokens/second right in Google Chrome.',
            realWorldDeliverable: {
              title: 'Stand-alone In-Browser WebGPU Web Page',
              urduTitle: 'In-Browser WebGPU Web Application',
              freelanceValue: '$500 / Zero-Cost Client Tool',
              description: 'Standalone HTML page running in-browser LLM via WebGPU.',
              steps: ['Include Transformers.js CDN', 'Request WebGPU device', 'Run text generation'],
              outputArtifact: 'local_webgpu.html'
            },
            zeroGpuRecipe: {
              platform: '100% Local Browser WebGPU',
              vramRequired: '0 GB Cloud VRAM',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Runs 100% in Chrome on your existing laptop GPU/CPU.',
              setupSnippet: 'npx serve .',
              launchUrl: 'https://huggingface.co/docs/transformers.js/'
            },
            codeSnippet: {
              language: 'javascript',
              filename: 'webgpu_inference_demo.js',
              code: \`// In-Browser WebGPU Inference using Transformers.js v3
import { pipeline, env } from '@huggingface/transformers';

async function runLocalInference() {
    console.log("⚡ Checking for WebGPU capabilities...");
    if (!navigator.gpu) {
        console.warn("WebGPU not detected, falling back to WASM CPU.");
    } else {
        console.log("✅ WebGPU Hardware Acceleration Active!");
    }

    // Load lightweight 4-bit model directly into browser VRAM
    console.log("Loading model: Qwen/Qwen2.5-0.5B-Instruct...");
    console.log("Zero cloud costs. 100% Private In-Browser Inference. 🚀");
}

runLocalInference();\`,
              explanation: 'Yeh script client-side WebGPU acceleration check aur model loading pattern demonstrate karta hai.',
              simulationOutput: \`⚡ Checking for WebGPU capabilities...
✅ WebGPU Hardware Acceleration Active!
Loading model: Qwen/Qwen2.5-0.5B-Instruct...
Zero cloud costs. 100% Private In-Browser Inference. 🚀\`
            },
            diagramScript: \`arch LR: In-Browser WebGPU Zero-Cost Topology
  user[User Chrome Browser] -> gpu[Local Hardware WebGPU Shaders] $browser
  gpu -> idb[(Browser IndexedDB Model Cache)] $database
  gpu --> screen[Instant Token Output: 35 tokens/sec] $terminal *
  user -.-> cloud((Cloud Servers: ZERO Requests, ZERO Cost, 100% Privacy))\`,
            diagramPreset: 'paper',
            diagramAnimate: 'flow',
            actionItems: [
              'Chrome browser mein chrome://gpu check karein',
              'Transformers.js WebGPU demo try karein',
              'Laptop par Ollama install karke "ollama run qwen2.5:0.5b" test karein'
            ],
            resources: [
              { title: 'Transformers.js v3 WebGPU Guide', url: 'https://huggingface.co/docs/transformers.js/', type: 'tool', tag: 'Docs' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-13',
          title: 'Module 13 Quiz: Local AI & WebGPU',
          titleUrdu: 'Module 13 Imtihan: Local AI aur WebGPU',
          passingScore: 70,
          xpReward: 350,
          badgeId: 'production_ready',
          questions: [
            {
              id: 'q13-1',
              question: 'In-browser WebGPU inference ka traditional server-hosted LLMs ke muqable mein sab se bara faida kya hai?',
              options: [
                'Model ki accuracy 100% ho jati hai',
                'Data user ke device se bahar nahi jata (100% privacy) aur server compute bills $0.00 ho jate hain',
                'Internet speed tez ho jati hai',
                'Display ki brightness barh jati hai'
              ],
              correctIndex: 1,
              explanation: 'Running models locally via WebGPU eliminates cloud inference bills entirely while offering airtight data privacy.',
              conceptUrdu: 'WebGPU Zero-Cloud-Cost and Privacy'
            }
          ]
        }
      },
      {
        id: 'mod-14',
        slug: 'enterprise-capstone-career-launch',
        phaseId: 'phase-5',
        title: 'Module 14: Enterprise Capstone Project & Career Launch',
        titleUrdu: 'Final Enterprise Capstone Project aur International Career Launch ($3k+/mo)',
        weekRange: 'Weeks 27–28',
        description: 'Multi-tenant architecture with Supabase Auth & RLS, Rust Axum gateway, Docker multi-stage builds, Cloudflare deployment, aur \$3,000+/month remote AI engineering career roadmap.',
        realWorldDeliverable: {
          title: 'Production Multi-Tenant AI Micro-SaaS on Supabase + Cloudflare',
          urduTitle: 'Production Multi-Tenant AI Micro-SaaS on Supabase + Cloudflare',
          freelanceValue: '$3,000 - $10,000+ / Full Commercial AI SaaS or $60k-$120k Remote AI Job Portfolio',
          description: 'A complete end-to-end commercial AI SaaS system featuring Supabase Auth (JWT + Magic Link), PostgreSQL Row Level Security (RLS) tenant isolation, credits/token billing, hybrid RAG with pgvector, streaming SSE tokens from Rust Axum, and a sleek Svelte 5 frontend hosted on Cloudflare Pages.',
          steps: [
            'Deploy PostgreSQL schema with Row Level Security enforcing strict tenant data isolation',
            'Implement Rust Axum gateway validating Supabase Auth JWTs and streaming LLM responses',
            'Connect hybrid RAG pipeline with pgvector HNSW indexing and RRF fusion',
            'Containerize with multi-stage Dockerfile and configure GitHub Actions automated CI/CD',
            'Publish portfolio repository with architecture diagrams and live demo link'
          ],
          outputArtifact: 'Full Stack Repository: ai-mastery-platform (Production Deployed)'
        },
        zeroGpuRecipe: {
          platform: 'Supabase Free Tier + Cloudflare Pages Free Tier + Groq / Google AI Studio Free Tiers',
          vramRequired: '0 GB (Pure Cloud Serverless & High-Speed Compiled Rust)',
          estimatedCost: '$0.00 Free (Zero infrastructure expense during development and staging)',
          computeUnitsTip: 'By combining Supabase Free Tier, Cloudflare Pages, and Groq/Gemini free tiers, you can build, showcase, and pitch a complete $10,000 enterprise platform with literally zero dollars out of pocket!',
          setupSnippet: 'npx supabase init && npm run build',
          launchUrl: 'https://cloudflare.com/'
        },
        lessons: [
          {
            id: 'les-14-1',
            slug: 'multi-tenant-capstone-architecture',
            title: 'Lesson 14.1: Multi-Tenant Enterprise Architecture with Supabase Auth & RLS',
            titleUrdu: 'Multi-Tenant Enterprise Architecture: Supabase RLS aur Security',
            week: 27,
            durationMinutes: 50,
            xpReward: 300,
            learningOutcomes: [
              'Architect multi-tenant isolation with PostgreSQL Row Level Security (RLS)',
              'Validate Supabase Auth JWTs in a compiled Rust Axum middleware',
              'Package and deploy frontend on Cloudflare Pages and backend on Docker'
            ],
            romanUrduSummary: 'Mubarak ho! Aap AI Mastery ke final module tak pohnch chuke hain. Yahan humne jo kuch seekha — Python, Tensors, PyTorch, Transformers, RAG, Agents, Unsloth, Rust — un sab ko jod kar ek commercial production grade AI SaaS banate hain jo international clients aur high-paying remote jobs ($3k - $8k/month) ke liye aapka golden portfolio banega!',
            deepDiveExplanation: 'Production multi-tenancy ensures that even if client-side code is tampered with, PostgreSQL RLS policies at the engine level prevent cross-tenant vector leakage: CREATE POLICY tenant_isolation ON documents FOR ALL USING (user_id = auth.uid()). Rust Axum middleware verifies cryptographic JWT signatures with JWKS caching.',
            realWorldDeliverable: {
              title: 'Enterprise Multi-Tenant AI Platform',
              urduTitle: 'Production AI Platform Capstone',
              freelanceValue: '$3,000+ / Full System Contract',
              description: 'Complete multi-tenant AI system deployed with auth, RAG, and telemetry.',
              steps: ['Setup Supabase schema & RLS', 'Run Rust Axum backend', 'Deploy Svelte 5 frontend'],
              outputArtifact: 'production_capstone.zip'
            },
            zeroGpuRecipe: {
              platform: 'Supabase Free Tier + Cloudflare Pages + Groq Free Tier',
              vramRequired: '0 GB',
              estimatedCost: '$0.00 Free',
              computeUnitsTip: 'Free tiers cover complete development, testing, and initial client demo.',
              setupSnippet: 'npm run build',
              launchUrl: 'https://supabase.com/'
            },
            codeSnippet: {
              language: 'sql',
              filename: 'supabase_rls_security.sql',
              code: \`-- Row Level Security (RLS) Multi-Tenant Policy
ALTER TABLE public.user_conversations ENABLE ROW LEVEL SECURITY;

-- Guarantee users can ONLY query and insert their own AI chats
CREATE POLICY "Tenant Isolation: Own Chats Only"
ON public.user_conversations
FOR ALL
TO authenticated
USING (user_id = auth.uid())
WITH CHECK (user_id = auth.uid());

-- Verify policy status
SELECT tablename, rowsecurity FROM pg_tables WHERE schemaname = 'public';\`,
              explanation: 'Yeh SQL script database level par multi-tenant isolation enforce karta hai.',
              simulationOutput: \`ALTER TABLE
CREATE POLICY
tablename          | rowsecurity
user_conversations | true
Multi-tenant security 100% active! 🛡️\`
            },
            diagramScript: \`arch LR: Complete AI Mastery Enterprise Production Topology
  user[Global Web Users] $browser -> cf[Cloudflare Edge CDN & WAF] $cloud
  cf -> svelte[Svelte 5 Runes Client Application] $browser
  svelte -> rust[Rust Axum 0.8 Gateway (<50ms)] $server *
  rust -> supa_auth[Supabase Auth JWT Middleware] $lock
  rust -> supa_db[(Supabase PostgreSQL + pgvector + RLS)] $database
  rust -> vllm_groq[Groq LPU / vLLM Inference Engine] $cpu
  rust -> otel[OpenTelemetry Metrics & Logging] $chart\`,
            diagramPreset: 'midnight',
            diagramAnimate: 'flow',
            actionItems: [
              'Supabase migration scripts run karein',
              'Svelte 5 frontend build verify karein (npm run build)',
              'Leaderboard par apna rank claim karein aur graduate badge unlock karein!'
            ],
            resources: [
              { title: 'The Twelve-Factor App for AI', url: 'https://12factor.net/', type: 'paper', tag: 'Standard' },
              { title: 'Open-Source AI Engineering Career Guide', url: 'https://github.com/isaim0011', type: 'community', tag: 'Career' }
            ]
          }
        ],
        quiz: {
          id: 'quiz-mod-14',
          title: 'Module 14 Quiz: Production Mastery & Career Launch',
          titleUrdu: 'Module 14 Imtihan: Final Production Mastery',
          passingScore: 70,
          xpReward: 500,
          badgeId: 'production_hero',
          questions: [
            {
              id: 'q14-1',
              question: 'Enterprise AI deployment mein Row Level Security (RLS) ka sab se ahem kirdar kya hota hai?',
              options: [
                'Database backup ko compress karna',
                'Yeh guarantee karna ke koi bhi user doosre user ka private AI chat history ya vectors query na kar sake chahe frontend hack bhi ho jaye',
                'GPU ki clock speed tez karna',
                'Tokens ki cost kam karna'
              ],
              correctIndex: 1,
              explanation: 'RLS database engine level par enforce hoti hai. Frontend code manipulate hone par bhi tenant isolation 100% secure rehti hai.',
              conceptUrdu: 'Row Level Security Tenant Isolation'
            }
          ]
        }
      }
    ]
  }
];

export const BADGES_DATA: Badge[] = [
  { id: 'first_step', title: 'First Step to AI Hero', titleUrdu: 'Pehla Qadam: Zero Se Safar Shuru', description: 'Complete Module 1 Quiz with 70%+ score', icon: '🚀', category: 'core' },
  { id: 'matrix_ninja', title: 'Matrix & Vector Ninja', titleUrdu: 'Vectors aur Math Ka Master', description: 'Master Linear Algebra & Cosine Similarity', icon: '📐', category: 'core' },
  { id: 'ml_practitioner', title: 'ML Practitioner', titleUrdu: 'Data Se Model Tak', description: 'Master classical machine learning, feature pipelines, and metrics', icon: '📊', category: 'core' },
  { id: 'core_pytorch', title: 'Autograd Craftsman', titleUrdu: 'PyTorch Computational Graph Engineer', description: 'Build and debug PyTorch autograd DAGs', icon: '🧠', category: 'core' },
  { id: 'attention_is_all_you_need', title: 'Attention Architect', titleUrdu: 'Transformer Q-K-V Ka Maahir', description: 'Master Scaled Dot-Product Attention & RoPE', icon: '✨', category: 'specialist' },
  { id: 'app_builder', title: 'App Builder', titleUrdu: 'Full-Stack AI Creator', description: 'Ship production-grade AI applications and streaming APIs', icon: '⚡', category: 'specialist' },
  { id: 'rag_architect', title: 'Hybrid RAG Master', titleUrdu: 'Production RAG & Vector Search King', description: 'Implement BM25 + pgvector RRF and rerankers', icon: '📚', category: 'specialist' },
  { id: 'agent_commander', title: 'Autonomous Agent Commander', titleUrdu: 'AI Agents aur ReAct Specialist', description: 'Build multi-step agent tools with deterministic guardrails', icon: '🤖', category: 'specialist' },
  { id: 'finetuning_pro', title: 'Fine-tuning Pro', titleUrdu: 'LoRA & Unsloth Wizard', description: 'Fine-tuned open-source models with Unsloth and DeepSeek-R1 GRPO', icon: '🔥', category: 'specialist' },
  { id: 'production_ready', title: 'Production Ready', titleUrdu: '0 to 1 Million Requests', description: 'Deploy low-latency LLM microservices with vLLM, Docker and Rust', icon: '🛡️', category: 'specialist' },
  { id: 'rust_turbo', title: 'Rust Turbocharged', titleUrdu: 'Rust Axum Sub-Millisecond Speedster', description: 'Deploy high-throughput Rust AI microservice', icon: '🦀', category: 'specialist' },
  { id: 'streak_warrior', title: 'Streak Warrior (7 Days)', titleUrdu: '7 Din Lagataar Seekhne Wala', description: 'Maintain a 7-day learning streak on the platform', icon: '🔥', category: 'streak' },
  { id: 'production_hero', title: 'Production AI Hero (Graduated)', titleUrdu: 'Kamyab AI Engineer (Hero Tak)', description: 'Complete all 5 Phases and Capstone Challenge', icon: '👑', category: 'mastery' }
];

export const DIAGRAM_GALLERY: DiagramGalleryItem[] = [
  {
    id: 'bloom-pyramid',
    title: "Bloom's Revised Taxonomy Pyramid",
    category: 'Pedagogy',
    description: 'Six cognitive levels: Remembering to Creating — foundational for our Roman Urdu syllabus design.',
    preset: 'sunset',
    animate: 'pulse',
    script: \`layers: Bloom's Revised Taxonomy for AI Engineers
  layer 6 - Creating: Design Novel Architectures, Deploy Production Systems
  layer 5 - Evaluating: Benchmark Latency vs Accuracy, Red-Team Guardrails
  layer 4 - Analyzing: Deconstruct Q-K-V Attention, Debug Gradient Vanishing
  layer 3 - Applying: Implement RRF Hybrid Search, Fine-Tune LoRA Adapters
  layer 2 - Understanding: Explain Backprop in Roman Urdu, Geometric Embeddings
  layer 1 - Remembering: Python Syntax, Tensor Shapes, CLI Tools\`
  },
  {
    id: 'model-70-20-10',
    title: '70:20:10 Learning Framework',
    category: 'Pedagogy',
    description: '70% Hands-on coding & debugging, 20% Peer code review & mentoring, 10% Structured theory.',
    preset: 'ocean',
    animate: 'ripple',
    script: \`pie: 70:20:10 AI Learning Model
  "70% Hands-on Coding & Projects": 70
  "20% Peer Review & Roman Urdu Mentoring": 20
  "10% Structured Theory & Readings": 10\`
  },
  {
    id: 'roadmap-20-weeks',
    title: '20-Week Master Curriculum Timeline',
    category: 'Roadmap',
    description: 'Complete 5-Phase journey from Zero to Production Hero.',
    preset: 'forest',
    animate: 'flow',
    script: \`gantt: 20-Week AI Mastery Journey
  dateFormat: Week
  section Phase 1: Foundations
    Python, LinAlg, NumPy       : p1, W1, 4w
  section Phase 2: Deep Learning
    PyTorch & Transformers      : p2, after p1, 4w
  section Phase 3: GenAI & RAG
    Advanced RAG & Agents       : p3, after p2, 4w
  section Phase 4: Production
    Rust, vLLM & Supabase       : p4, after p3, 4w
  section Phase 5: Capstone
    Track Specialization & Launch: p5, after p4, 4w\`
  },
  {
    id: 'transformer-attention',
    title: 'Scaled Dot-Product Multi-Head Attention',
    category: 'Deep Learning',
    description: 'Visual flow of Query, Key, Value calculations with causal masking.',
    preset: 'grape',
    animate: 'flow',
    script: \`flow TD: Scaled Dot-Product Attention
  q[Query Vector Q] & k[Key Vector K] --> dot[Dot Product: Q x K^T]
  dot --> scale[Scale by 1/sqrt(d_k)]
  scale --> mask{Causal Autoregressive Mask}
  mask --> sm[Softmax Probability Weights]
  sm & v[Value Vector V] --> out_dot[MatMul: Weights x V]
  out_dot --> out[Projected Representation]\`
  },
  {
    id: 'modular-rag',
    title: 'Advanced Modular RAG with Hybrid RRF & Reranker',
    category: 'Generative AI',
    description: 'Enterprise architecture preventing hallucinations and retrieving precise documents.',
    preset: 'blueprint',
    animate: 'flow',
    script: \`arch: Enterprise Hybrid RAG Engine
  user[User Query] -> router{Intent Router}
  router ->|Semantic| embed[Embedding API] -> vector_db[(Supabase pgvector)]
  router ->|Keyword| fts[Postgres BM25 Full Text]
  vector_db & fts --> rrf[Reciprocal Rank Fusion (k=60)]
  rrf --> rerank[Cross-Encoder Reranker]
  rerank --> prompt[Grounded Context Synthesis]
  prompt --> llm[LLM Generation (Claude/DeepSeek)]
  llm --> answer[Verified Answer with Citations]\`
  },
  {
    id: 'react-agent',
    title: 'Multi-Agent ReAct Orchestration',
    category: 'AI Agents',
    description: 'Thought, Action, Tool Execution and Observation cycle.',
    preset: 'midnight',
    animate: 'flow',
    script: \`seq: Autonomous ReAct Multi-Agent Workflow
  User -> AgentSupervisor: "Research recent AI papers and write summary"
  AgentSupervisor -> WebSubagent: Delegate: Search Arxiv API
  WebSubagent -> ArxivAPI: GET /api/query?search_query=transformers
  ArxivAPI --> WebSubagent: 5 Recent Papers Returned
  WebSubagent --> AgentSupervisor: Papers Retrieved
  AgentSupervisor -> SummarizerSubagent: Delegate: Synthesize into Roman Urdu
  SummarizerSubagent --> AgentSupervisor: Formatted Urdu Digest Ready
  AgentSupervisor --> User: Final Digest + Citation Links\`
  },
  {
    id: 'lora-layers',
    title: 'LoRA (Low-Rank Adaptation) Matrix Decomposition',
    category: 'Fine-Tuning',
    description: 'Efficient fine-tuning by decomposing weight updates into A (d x r) and B (r x k) matrices.',
    preset: 'paper',
    animate: 'glow',
    script: \`layers: LoRA Low-Rank Decomposition
  layer Frozen Pretrained Weights: W_0 (4096 x 4096) [Frozen FP16/INT4]
  layer Low-Rank Matrix A: Matrix A (4096 x 8) [Trainable FP32]
  layer Low-Rank Matrix B: Matrix B (8 x 4096) [Trainable FP32, Zero-Init]
  layer Adapted Forward: Output = (W_0 * x) + (B * A * x) * (alpha / r)\`
  }
];

export const INITIAL_USER_PROFILE: UserProfile = {
  id: 'guest-student-001',
  email: 'student@aimastery.urdu',
  fullName: 'Tariq Mehmood',
  role: 'AI Engineer in Training',
  track: 'developers',
  xp: 450,
  streakDays: 4,
  lastActiveDate: new Date().toISOString().split('T')[0],
  completedLessonIds: ['les-1-1'],
  unlockedBadgeIds: ['first_step'],
  isGuest: true
};
\`;

const targetFile = path.resolve(__dirname, '../frontend/src/lib/syllabus-data.ts');
fs.writeFileSync(targetFile, syllabusDataCode, 'utf8');
console.log('Successfully wrote complete 14-module syllabus-data.ts to ' + targetFile);
