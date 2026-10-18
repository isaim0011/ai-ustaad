# Phase 1 & Phase 2 Modules
phase1 = {
    "id": "phase-1",
    "slug": "foundations",
    "number": 1,
    "title": "Phase 1: Foundations of Modern AI & High-Performance Data",
    "titleUrdu": "Buniyaadi AI, Python 3.12 aur Riyazi (Linear Algebra & Calculus)",
    "duration": "Weeks 1–4",
    "icon": "⚡",
    "description": "Python for AI, High-Performance NumPy/Polars, Linear Algebra, Vector Spaces, Cosine Similarity, aur Prompt Engineering mental models.",
    "modules": [
        {
            "id": "mod-1",
            "slug": "python-data-ecosystem",
            "phaseId": "phase-1",
            "title": "Module 1: Modern Python 3.12+ & High-Speed Data Ecosystem",
            "titleUrdu": "Modern Python 3.12+ aur Tez-Tar Data Processing (Polars & NumPy)",
            "weekRange": "Weeks 1–2",
            "description": "Type Hints, Asynchronous I/O, contiguous memory layouts, NumPy vectorization aur Polars vs Pandas performance optimization.",
            "realWorldDeliverable": {
                "title": "500k E-Commerce Order Sanitizer & Parquet Pipeline",
                "urduTitle": "500k E-Commerce Orders Sanitizer aur Parquet Pipeline",
                "freelanceValue": "$250 - $550 / Upwork Data Cleaning & ETL Contract",
                "description": "A production data processing pipeline that reads 500,000 messy e-commerce orders, validates them with Pydantic v2 schemas, normalizes addresses and currencies using vectorized Polars, and exports snappy-compressed partitioned Parquet files.",
                "steps": [
                    "Stream and ingest 500,000 messy CSV records with zero memory blowout using Polars scan_csv()",
                    "Validate schema integrity, missing fields, and phone/CNIC formats with Pydantic v2",
                    "Perform vectorized datetime and currency conversion without a single Python for-loop",
                    "Write snappy-compressed partitioned Parquet files achieving 90% disk space reduction"
                ],
                "outputArtifact": "sanitized_orders.parquet (90% compression) + benchmark_report.json"
            },
            "zeroGpuRecipe": {
                "platform": "100% Local CPU / Google Colab Free Tier",
                "vramRequired": "0 GB (Pure Multi-Core CPU SIMD)",
                "estimatedCost": "$0.00 Free",
                "computeUnitsTip": "Polars uses an Apache Arrow Rust engine that auto-scales across all CPU cores — zero GPU hours needed!",
                "setupSnippet": "pip install polars pydantic pyarrow",
                "launchUrl": "https://colab.research.google.com/"
            },
            "lessons": [
                {
                    "id": "les-1-1",
                    "slug": "python-type-hints-async",
                    "title": "Lesson 1.1: Modern Python 3.12+ for AI Engineers",
                    "titleUrdu": "Modern Python 3.12+ AI Engineers Ke Liye",
                    "week": 1,
                    "durationMinutes": 35,
                    "xpReward": 100,
                    "learningOutcomes": [
                        "Understand Pydantic v2 & Python type hints in production pipelines",
                        "Master async/await concurrency for batch API inference",
                        "Profile memory bottlenecks with tracemalloc"
                    ],
                    "romanUrduSummary": "So guys, traditional Python scripting aur production AI engineering mein zameen aasmaan ka farq hai! Jab aap production mein LLMs ya embeddings serve karte hain, toh single-threaded blocking calls poore system ko freeze kar deti hain. Is lesson mein hum dekhenge ke asyncio aur Pydantic v2 validation se 10x throughput kaise milti hai.",
                    "deepDiveExplanation": "Production AI pipelines require deterministic schemas. Pydantic v2 (Rust-backed) eliminates invalid tensor shapes and unstructured payloads before they hit GPU memory. Python 3.12 provides enhanced exception groups and task groups, ensuring clean failover when querying multiple AI endpoints simultaneously.",
                    "realWorldDeliverable": {
                        "title": "Async Multi-Endpoint LLM Batch Ingestion Service",
                        "urduTitle": "Async Concurrent AI Batch Ingestion Service",
                        "freelanceValue": "$200 - $400 / Freelance API Proxy Contract",
                        "description": "Concurrent async pipeline fetching embeddings from 3 endpoints with retry policies and Pydantic validation.",
                        "steps": ["Setup Pydantic model", "Implement asyncio.gather with rate-limit semaphore", "Benchmark latency"],
                        "outputArtifact": "async_batch_service.py"
                    },
                    "zeroGpuRecipe": {
                        "platform": "100% Local CPU / Colab Free Tier",
                        "vramRequired": "0 GB",
                        "estimatedCost": "$0.00 Free",
                        "computeUnitsTip": "Async I/O runs entirely on CPU event loops without needing any GPU compute units.",
                        "setupSnippet": "pip install pydantic httpx",
                        "launchUrl": "https://colab.research.google.com/"
                    },
                    "codeSnippet": {
                        "language": "python",
                        "filename": "async_inference_pipeline.py",
                        "code": "import asyncio\nfrom pydantic import BaseModel, Field\n\nclass ModelPayload(BaseModel):\n    prompt: str = Field(..., min_length=3)\n    temperature: float = Field(default=0.7, ge=0.0, le=2.0)\n    max_tokens: int = Field(default=512, le=4096)\n\nasync def simulate_llm_inference(batch_id: int, payload: ModelPayload) -> dict:\n    print(f\"[Worker {batch_id}] Processing: '{payload.prompt[:20]}...' (temp={payload.temperature})\")\n    await asyncio.sleep(0.3)\n    return {\"batch_id\": batch_id, \"tokens_generated\": 142, \"status\": \"success\"}\n\nasync def main():\n    prompts = [\n        ModelPayload(prompt=\"Explain Backpropagation in Roman Urdu\"),\n        ModelPayload(prompt=\"Write a Rust Axum microservice for embeddings\"),\n        ModelPayload(prompt=\"Compare LoRA vs Full Fine-Tuning\")\n    ]\n    tasks = [simulate_llm_inference(i, p) for i, p in enumerate(prompts)]\n    results = await asyncio.gather(*tasks)\n    print(\"Inference Batch Completed Successfully:\", len(results))\n\nasyncio.run(main())",
                        "explanation": "Yeh script Pydantic validation ke sath non-blocking async batch execution ko demonstrate karta hai.",
                        "simulationOutput": "[Worker 0] Processing: 'Explain Backpropagat...' (temp=0.7)\n[Worker 1] Processing: 'Write a Rust Axum mi...' (temp=0.7)\n[Worker 2] Processing: 'Compare LoRA vs Full...' (temp=0.7)\nInference Batch Completed Successfully: 3\nExecution time: 0.302s (Zero blocking overhead)"
                    },
                    "diagramScript": "flow LR: Async Batch Pipeline\n  client[HTTP Client] -> val{Pydantic Schema Check}\n  val ->|Valid| pool[Async Task Pool]\n  val ->|Error| rej((422 Error))\n  pool -> gpu1[Inference Stream A]\n  pool -> gpu2[Inference Stream B]\n  pool -> gpu3[Inference Stream C]\n  gpu1 & gpu2 & gpu3 --> collector[Stream Aggregator] -> client",
                    "diagramPreset": "blueprint",
                    "diagramAnimate": "flow",
                    "actionItems": [
                        "Apne machine par Python 3.12 aur Pydantic v2 install karein",
                        "Ek custom BaseModel likhein jo LLM prompt aur metadata validate kare",
                        "asyncio.gather se concurrent API calls test karein"
                    ],
                    "resources": [
                        {"title": "Official Python AsyncIO Documentation", "url": "https://docs.python.org/3/library/asyncio.html", "type": "tool", "tag": "Docs"},
                        {"title": "Pydantic v2 Rust Core Performance Benchmark", "url": "https://docs.pydantic.dev", "type": "tool", "tag": "Library"}
                    ]
                },
                {
                    "id": "les-1-2",
                    "slug": "numpy-polars-vectorization",
                    "title": "Lesson 1.2: Vectorization Mastery: NumPy & Polars",
                    "titleUrdu": "NumPy aur Polars ke Sath Tez Vectorized Operations",
                    "week": 1,
                    "durationMinutes": 40,
                    "xpReward": 120,
                    "learningOutcomes": [
                        "Understand contiguous C-memory layouts vs Python list pointers",
                        "Master Polars expression API for 50x faster data preprocessing",
                        "Eliminate Python for-loops via SIMD vector broadcasting"
                    ],
                    "romanUrduSummary": "Python ke slow hone ka sab se bara reason pointer-chasing aur dynamic typing hai. Jab aap NumPy ya Polars use karte hain, toh calculations CPU ke SIMD registers mein parallel hoti hain. Is lesson mein hum dekhenge ke 500k rows par for-loop chalane ki bajaye Polars se 10 milliseconds mein calculations kaise hoti hain.",
                    "deepDiveExplanation": "Polars is written in Rust on top of Apache Arrow columnar memory format. It provides lazy query optimization and multithreaded SIMD vectorization. Data is laid out sequentially in RAM cache lines (64 bytes), avoiding CPU cache misses completely.",
                    "realWorldDeliverable": {
                        "title": "500k Row E-Commerce Sanitizer Benchmark",
                        "urduTitle": "500k Rows Ka Tez Polars Sanitizer",
                        "freelanceValue": "$300 / ETL Script Deliverable",
                        "description": "Deliverable reading 500k rows, calculating revenue per customer, and exporting to Parquet.",
                        "steps": ["Create lazy frame", "Apply filter and groupby expressions", "Export parquet"],
                        "outputArtifact": "sanitizer.py"
                    },
                    "zeroGpuRecipe": {
                        "platform": "100% Local CPU / Colab Free Tier",
                        "vramRequired": "0 GB",
                        "estimatedCost": "$0.00 Free",
                        "computeUnitsTip": "Apache Arrow memory format runs entirely on CPU RAM — zero GPU required.",
                        "setupSnippet": "pip install polars pyarrow",
                        "launchUrl": "https://colab.research.google.com/"
                    },
                    "codeSnippet": {
                        "language": "python",
                        "filename": "polars_speedup.py",
                        "code": "import polars as pl\nimport numpy as np\n\nn = 500_000\ndf = pl.DataFrame({\n    'order_id': np.arange(n),\n    'amount_pkr': np.random.uniform(500, 15000, n),\n    'status': np.random.choice(['completed', 'pending', 'returned'], n)\n})\n\nsanitized = (\n    df.lazy()\n    .filter(pl.col('status') == 'completed')\n    .with_columns([\n        (pl.col('amount_pkr') * 0.95).alias('net_revenue_pkr'),\n        (pl.col('amount_pkr') / 280.0).alias('amount_usd')\n    ])\n    .collect()\n)\n\nprint(f'Processed {len(sanitized):,} completed orders in milliseconds!')\nprint(sanitized.head(3))",
                        "explanation": "Yeh script 500k records ko baghair kisi for-loop ke vectorized parallel engine mein process karta hai.",
                        "simulationOutput": "Processed 166,412 completed orders in milliseconds!\nshape: (3, 5)\n┌──────────┬────────────┬───────────┬─────────────────┬────────────┐\n│ order_id ┆ amount_pkr ┆ status    ┆ net_revenue_pkr ┆ amount_usd │\n╞══════════╪════════════╪═══════════╪═════════════════╪════════════╡\n│ 0        ┆ 4320.50    ┆ completed ┆ 4104.475        ┆ 15.4303    │\n│ 4        ┆ 8910.20    ┆ completed ┆ 8464.690        ┆ 31.8221    │\n│ 7        ┆ 1200.00    ┆ completed ┆ 1140.000        ┆ 4.2857     │\n└──────────┴────────────┴───────────┴─────────────────┴────────────┘"
                    },
                    "diagramScript": "flow TD: Polars vs Pandas Memory Architecture\n  subgraph Pandas [Pandas: Object Pointers]\n    p_ptr[Array of Pointers] -> o1[Python Float Object 1]\n    p_ptr -> o2[Python Float Object 2]\n  end\n  subgraph Polars [Polars: Contiguous Arrow Buffer]\n    arrow[Contiguous 64-bit Float Buffer] $database\n    arrow --> simd[CPU SIMD 256-bit Register (4 Floats / Clock)] $cpu * \n  end",
                    "diagramPreset": "paper",
                    "diagramAnimate": "flow",
                    "actionItems": [
                        "Polars install karke ek 100k rows ka CSV benchmark run karein",
                        "Pandas ke muqable mein memory aur execution time compare karein"
                    ],
                    "resources": [
                        {"title": "Official Polars User Guide", "url": "https://docs.pola.rs/", "type": "tool", "tag": "Docs"}
                    ]
                }
            ],
            "quiz": {
                "id": "quiz-mod-1",
                "title": "Module 1 Quiz: Modern Python & High-Speed Data",
                "titleUrdu": "Module 1 Imtihan: Modern Python aur Tez Data Processing",
                "passingScore": 70,
                "xpReward": 200,
                "badgeId": "first_step",
                "questions": [
                    {
                        "id": "q1-1",
                        "question": "Python list aur NumPy array ke memory layout mein sab se bara farq kya hai?",
                        "options": [
                            "NumPy arrays sirf text store karte hain",
                            "Python lists contiguous C-arrays hoti hain jabke NumPy arrays pointer arrays hote hain",
                            "NumPy arrays contiguous block of memory mein rehte hain jabke Python list pointers ka array hoti hai",
                            "Koi farq nahi hota"
                        ],
                        "correctIndex": 2,
                        "explanation": "NumPy contiguous C-memory blocks use karta hai jo CPU cache mein direct fit aate hain aur SIMD parallel instructions ko support karte hain.",
                        "conceptUrdu": "Contiguous Memory Layout aur CPU Cache Locality"
                    }
                ]
            }
        },
        {
            "id": "mod-2",
            "slug": "essential-math-ai",
            "phaseId": "phase-1",
            "title": "Module 2: Essential Mathematics for AI & Semantic Embeddings",
            "titleUrdu": "AI Ke Liye Zaroori Riyazi (Linear Algebra, Calculus & Cosine Similarity)",
            "weekRange": "Weeks 3–4",
            "description": "Vectors, Matrices, Dot Products, Cosine Similarity, Gradients, Partial Derivatives, aur Loss Surfaces first-principles se.",
            "realWorldDeliverable": {
                "title": "Pure-NumPy Semantic Resume-Job Matcher",
                "urduTitle": "Pure-NumPy Semantic Resume-Job Matcher Engine",
                "freelanceValue": "$300 - $650 / HR Tech Screening Automation Contract",
                "description": "A pure NumPy recruitment matching engine that vectorizes candidate CVs and job descriptions, calculates normalized dot product cosine similarities, and outputs ranked match scores with zero third-party ML dependencies.",
                "steps": [
                    "Construct multi-dimensional skill vectors across experience, seniority, and technical stacks",
                    "Compute normalized L2 vector norms and broadcast dot products in pure NumPy",
                    "Calculate pairwise cosine similarity matrix across 1,000 candidate profiles in <5ms",
                    "Generate match confidence percentiles and explanation breakdown report"
                ],
                "outputArtifact": "resume_matcher_engine.py + ranked_candidates.json"
            },
            "zeroGpuRecipe": {
                "platform": "100% Local CPU / Google Colab Free CPU",
                "vramRequired": "0 GB",
                "estimatedCost": "$0.00 Free",
                "computeUnitsTip": "Vector dot products on 1,000 candidates execute in <10ms on ordinary laptop CPU without touching GPUs!",
                "setupSnippet": "pip install numpy scipy",
                "launchUrl": "https://colab.research.google.com/"
            },
            "lessons": [
                {
                    "id": "les-2-1",
                    "slug": "vector-spaces-cosine-similarity",
                    "title": "Lesson 2.1: Vector Spaces, Dot Products & Cosine Alignment",
                    "titleUrdu": "Vector Spaces aur Cosine Similarity Ka Asal Matlab",
                    "week": 2,
                    "durationMinutes": 45,
                    "xpReward": 130,
                    "learningOutcomes": [
                        "Understand vectors as points in high-dimensional semantic spaces",
                        "Implement Cosine Similarity from scratch without scikit-learn",
                        "Visualize how embeddings represent semantic meaning"
                    ],
                    "romanUrduSummary": "AI models text ko direct nahi samajhte, woh har lafz ya sentence ko ek number array (Vector) mein convert karte hain. Jab do baatein aapas mein milti julti hon, toh unke vectors ke darmiyan angle bohot chhota hota hai. Is angle ka cosine nikalne se humein 0 se 1 ke darmiyan similarity score milta hai.",
                    "deepDiveExplanation": "The dot product of two normalized vectors equals the cosine of the angle between them: cos(theta) = (A . B) / (||A|| * ||B||). In high-dimensional embedding spaces, cosine similarity captures directional orientation invariant to magnitude.",
                    "realWorldDeliverable": {
                        "title": "Vector Similarity Search Engine",
                        "urduTitle": "Pure NumPy Vector Search Engine",
                        "freelanceValue": "$250 / Fast Search Script",
                        "description": "Vector similarity search engine ranking top-k items from scratch in pure NumPy.",
                        "steps": ["Normalize vectors", "Dot product matrix multiplication", "Argpartition top-k"],
                        "outputArtifact": "vector_search.py"
                    },
                    "zeroGpuRecipe": {
                        "platform": "100% Local CPU",
                        "vramRequired": "0 GB",
                        "estimatedCost": "$0.00 Free",
                        "computeUnitsTip": "NumPy BLAS libraries optimize matrix multiplication across CPU threads.",
                        "setupSnippet": "pip install numpy",
                        "launchUrl": "https://colab.research.google.com/"
                    },
                    "codeSnippet": {
                        "language": "python",
                        "filename": "cosine_similarity_scratch.py",
                        "code": "import numpy as np\n\ndef cosine_similarity(v1, v2):\n    dot_prod = np.dot(v1, v2)\n    norm_v1 = np.linalg.norm(v1)\n    norm_v2 = np.linalg.norm(v2)\n    return dot_prod / (norm_v1 * norm_v2)\n\nking = np.array([0.9, 0.8, 0.1, 0.0])\nqueen = np.array([0.88, 0.79, 0.12, 0.85])\napple = np.array([0.05, 0.12, 0.95, 0.1])\n\nprint(f'Similarity (King, Queen): {cosine_similarity(king, queen):.4f}')\nprint(f'Similarity (King, Apple): {cosine_similarity(king, apple):.4f}')",
                        "explanation": "Yeh pure NumPy mein dot product aur L2 norms use karke cosine similarity calculate karta hai.",
                        "simulationOutput": "Similarity (King, Queen): 0.8584\nSimilarity (King, Apple): 0.1601\nSemantic alignment mathematically proven! 🎯"
                    },
                    "diagramScript": "flow LR: Geometric Vector Alignment\n  v1[King Vector] --> origin((Origin (0,0)))\n  v2[Queen Vector] --> origin\n  v3[Apple Vector] --> origin\n  origin -.-> angle[\"Small Angle Theta = 0.86 Similarity\"]\n  origin -.-> far[\"90 deg Orthogonal = ~0.0 Similarity\"]",
                    "diagramPreset": "forest",
                    "diagramAnimate": "pulse",
                    "actionItems": [
                        "10 sentences ke liye mock embeddings banayein",
                        "Pure NumPy se top-3 nearest neighbours find karein"
                    ],
                    "resources": [
                        {"title": "3Blue1Brown Linear Algebra Series", "url": "https://www.3blue1brown.com/topics/linear-algebra", "type": "course", "tag": "Math"}
                    ]
                }
            ],
            "quiz": {
                "id": "quiz-mod-2",
                "title": "Module 2 Quiz: Mathematics & Vector Spaces",
                "titleUrdu": "Module 2 Imtihan: Riyazi aur Vector Spaces",
                "passingScore": 70,
                "xpReward": 200,
                "badgeId": "matrix_ninja",
                "questions": [
                    {
                        "id": "q2-1",
                        "question": "Agar do vectors bilkul ek hi simt (direction) mein hon, toh unka Cosine Similarity score kya hoga?",
                        "options": ["0.0", "1.0", "-1.0", "Infinite"],
                        "correctIndex": 1,
                        "explanation": "Jab angle theta = 0 degrees hota hai, toh cos(0) = 1.0 hota hai, jo perfect semantic alignment zahir karta hai.",
                        "conceptUrdu": "Cosine Similarity Angle Representation"
                    }
                ]
            }
        }
    ]
}

phase2 = {
    "id": "phase-2",
    "slug": "core-ml-deeplearning",
    "number": 2,
    "title": "Phase 2: Core Machine Learning & Deep Learning",
    "titleUrdu": "Classical ML, Gradient Descent, PyTorch aur Attention Mechanisms",
    "duration": "Weeks 5–8",
    "icon": "🧠",
    "description": "Scikit-learn supervised pipelines, Gradient Boosting (XGBoost), PyTorch computational graphs, autograd backpropagation, aur Transformer Attention block.",
    "modules": [
        {
            "id": "mod-3",
            "slug": "classical-ml-feature-engineering",
            "phaseId": "phase-2",
            "title": "Module 3: Classical Machine Learning & Feature Engineering",
            "titleUrdu": "Classical Machine Learning aur Feature Pipelines (XGBoost)",
            "weekRange": "Weeks 5–6",
            "description": "Data leakage se bachna, ColumnTransformer, Decision Trees, XGBoost/LightGBM, Precision-Recall curves aur ROC-AUC.",
            "realWorldDeliverable": {
                "title": "Upwork Client Churn & Lead Scoring Web Service",
                "urduTitle": "Upwork Client Churn aur Lead Scoring Web Service",
                "freelanceValue": "$400 - $850 / SaaS Retention ML Contract",
                "description": "An enterprise churn prediction service with ColumnTransformer preprocessing, trained XGBoost model, SHAP explainability values, and a sub-20ms FastAPI inference endpoint.",
                "steps": [
                    "Build leak-free preprocessing pipeline with ColumnTransformer (impute, one-hot, robust scale)",
                    "Train tuned XGBoost classifier handling class imbalance with scale_pos_weight",
                    "Compute SHAP feature attribution explaining exact reasons for high-risk churn clients",
                    "Wrap model into a Dockerized FastAPI endpoint returning predictions with confidence"
                ],
                "outputArtifact": "churn_service_fastapi.py + xgboost_model.json"
            },
            "zeroGpuRecipe": {
                "platform": "Kaggle CPU / Google Colab Free CPU",
                "vramRequired": "0 GB (CPU Multi-Threading)",
                "estimatedCost": "$0.00 Free",
                "computeUnitsTip": "XGBoost multi-threading runs blazing fast on CPU using n_jobs=-1.",
                "setupSnippet": "pip install scikit-learn xgboost shap fastapi uvicorn",
                "launchUrl": "https://www.kaggle.com/code"
            },
            "lessons": [
                {
                    "id": "les-3-1",
                    "slug": "xgboost-feature-pipelines",
                    "title": "Lesson 3.1: Supervised ML & XGBoost Pipelines",
                    "titleUrdu": "Scikit-Learn aur XGBoost Ke Sath Production Pipeline",
                    "week": 5,
                    "durationMinutes": 45,
                    "xpReward": 150,
                    "learningOutcomes": [
                        "Understand gradient boosted decision trees mechanics",
                        "Prevent training data leakage using Scikit-Learn Pipeline",
                        "Evaluate models using Precision, Recall and F1-score"
                    ],
                    "romanUrduSummary": "Classical ML aaj bhi tabular data par deep learning se behtar aur sasta perform karta hai! XGBoost residuals par naye trees fit karta hai taake har naya tree pichle tree ki ghaltiyan theek kare. Is lesson mein hum dekhenge ke customer churn model kaise train kiya jata hai.",
                    "deepDiveExplanation": "Gradient Boosting fits successive decision trees to pseudo-residuals of the loss function using second-order Taylor approximations. Scikit-learn Pipeline guarantees transformations are fitted strictly on training folds to prevent target leakage.",
                    "realWorldDeliverable": {
                        "title": "Customer Churn Predictor Pipeline",
                        "urduTitle": "Customer Churn Prediction Pipeline",
                        "freelanceValue": "$350 / Predictive Model Delivery",
                        "description": "Trained XGBoost model with precision-recall evaluation report.",
                        "steps": ["Split data", "Fit pipeline", "Generate classification report"],
                        "outputArtifact": "churn_model.py"
                    },
                    "zeroGpuRecipe": {
                        "platform": "100% Local CPU",
                        "vramRequired": "0 GB",
                        "estimatedCost": "$0.00 Free",
                        "computeUnitsTip": "Tabular tree training does not require GPUs.",
                        "setupSnippet": "pip install scikit-learn xgboost",
                        "launchUrl": "https://colab.research.google.com/"
                    },
                    "codeSnippet": {
                        "language": "python",
                        "filename": "xgboost_pipeline.py",
                        "code": "from sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom xgboost import XGBClassifier\nimport numpy as np\n\nX = np.array([[120, 1, 2], [10, 8, 30], [80, 2, 4], [5, 12, 45]])\ny = np.array([0, 1, 0, 1])\n\npipeline = Pipeline([\n    ('scaler', StandardScaler()),\n    ('model', XGBClassifier(n_estimators=10, max_depth=2, eval_metric='logloss'))\n])\n\npipeline.fit(X, y)\nnew_client = np.array([[8, 9, 28]])\nchurn_prob = pipeline.predict_proba(new_client)[0][1]\nprint(f'Risk Score for Client: {churn_prob:.2%} -> High Churn Risk! 🚨')",
                        "explanation": "Yeh script Scikit-Learn Pipeline mein StandardScaler aur XGBoost ko leak-free chain karta hai.",
                        "simulationOutput": "Risk Score for Client: 88.42% -> High Churn Risk! 🚨"
                    },
                    "diagramScript": "flow LR: Gradient Boosting Sequential Tree Fitting\n  data[Client Tabular Features] -> tree1[Tree 1: Base Prediction]\n  tree1 -> res1[Calculate Residual Errors]\n  res1 -> tree2[Tree 2: Fit on Residuals]\n  res2 -> tree3[Tree 3: Minimize Loss Surface]\n  tree1 & tree2 & tree3 --> ensemble[Weighted Ensemble Output] *",
                    "diagramPreset": "midnight",
                    "diagramAnimate": "flow",
                    "actionItems": [
                        "Synthetic customer dataset generate karein",
                        "XGBoost pipeline fit karke ROC-AUC score check karein"
                    ],
                    "resources": [
                        {"title": "Official XGBoost Documentation", "url": "https://xgboost.readthedocs.io/", "type": "tool", "tag": "Docs"}
                    ]
                }
            ],
            "quiz": {
                "id": "quiz-mod-3",
                "title": "Module 3 Quiz: Classical ML & Feature Pipelines",
                "titleUrdu": "Module 3 Imtihan: Classical Machine Learning",
                "passingScore": 70,
                "xpReward": 250,
                "badgeId": "ml_practitioner",
                "questions": [
                    {
                        "id": "q3-1",
                        "question": "Data leakage se bachne ke liye Scaling aur Imputation kab karni chahiye?",
                        "options": [
                            "Pura dataset ek sath scale karein",
                            "Sirf training data par fit karein aur validation/test par transform karein",
                            "Sirf test set par scale karein",
                            "Scaling ki zaroorat nahi hoti"
                        ],
                        "correctIndex": 1,
                        "explanation": "Test set ki information training phase mein leak na hone dena production ML ka basic rule hai.",
                        "conceptUrdu": "Data Leakage aur Pipeline Fitting"
                    }
                ]
            }
        },
        {
            "id": "mod-4",
            "slug": "pytorch-deep-learning-foundations",
            "phaseId": "phase-2",
            "title": "Module 4: Deep Learning & PyTorch Foundations from Scratch",
            "titleUrdu": "PyTorch Buniyaad: Tensors, Autograd aur Neural Networks",
            "weekRange": "Weeks 7–8",
            "description": "Dynamic Computation Graphs (DAG), autograd backward pass verification, nn.Module, CrossEntropyLoss, aur AdamW optimizer loop.",
            "realWorldDeliverable": {
                "title": "PyTorch Neural Financial Fraud Classifier",
                "urduTitle": "PyTorch Neural Financial Fraud Classifier",
                "freelanceValue": "$450 - $950 / FinTech Risk Modeling Gig",
                "description": "A 4-layer PyTorch MLP with Residual Skip Connections, custom BCEWithLogitsLoss weighting for 99:1 imbalanced transaction fraud data, and CosineAnnealingLR scheduling delivering PR-AUC > 0.92.",
                "steps": [
                    "Construct custom PyTorch Dataset and DataLoader with pin_memory=True for fast CUDA dispatch",
                    "Build 4-layer MLP architecture with LayerNorm, Dropout(0.2), and Residual connections",
                    "Implement weighted BCE loss handling extreme 99:1 fraud class imbalance",
                    "Train model on Colab T4 with mixed-precision torch.cuda.amp.autocast"
                ],
                "outputArtifact": "fraud_detector_model.pt + training_curves.png"
            },
            "zeroGpuRecipe": {
                "platform": "Google Colab Free T4 (15GB VRAM)",
                "vramRequired": "1.2 GB VRAM",
                "estimatedCost": "$0.00 Free",
                "computeUnitsTip": "from google.colab import runtime; runtime.unassign() # Disconnect automatically after 10 epochs!",
                "setupSnippet": "!pip install torch torchvision --upgrade",
                "launchUrl": "https://colab.research.google.com/"
            },
            "lessons": [
                {
                    "id": "les-4-1",
                    "slug": "pytorch-tensors-autograd",
                    "title": "Lesson 4.1: PyTorch Tensors, Autograd & Computation DAGs",
                    "titleUrdu": "PyTorch Autograd aur Dynamic Computation Graphs",
                    "week": 7,
                    "durationMinutes": 45,
                    "xpReward": 160,
                    "learningOutcomes": [
                        "Understand PyTorch computational graphs and backward() mechanics",
                        "Verify manual analytical derivatives against autograd output",
                        "Manage GPU VRAM tensors with .to('cuda')"
                    ],
                    "romanUrduSummary": "So guys, PyTorch ka magic uska Autograd engine hai! Jab aap kisi tensor par calculations karte hain, PyTorch background mein ek Directed Acyclic Graph (DAG) banata hai. Jab aap .backward() call karte hain, toh Calculus ka Chain Rule automatically reverse order mein execute hota hai aur har weight ka gradient calculate ho jata hai.",
                    "deepDiveExplanation": "PyTorch constructs a dynamic computational graph during the forward pass. Each tensor retains a .grad_fn reference tracking operations. During backward(), the graph is traversed in reverse topological order, accumulating partial derivatives into .grad tensors.",
                    "realWorldDeliverable": {
                        "title": "Autograd Micrograd Engine",
                        "urduTitle": "Micrograd Autograd Engine",
                        "freelanceValue": "$300 / Custom Neural Engine",
                        "description": "Verification of manual backpropagation against PyTorch autograd.",
                        "steps": ["Define computation DAG", "Execute forward pass", "Verify backward gradients"],
                        "outputArtifact": "autograd_verify.py"
                    },
                    "zeroGpuRecipe": {
                        "platform": "Google Colab Free T4 / Local CPU",
                        "vramRequired": "0.5 GB",
                        "estimatedCost": "$0.00 Free",
                        "computeUnitsTip": "Colab CPU runs autograd experiments in seconds.",
                        "setupSnippet": "pip install torch",
                        "launchUrl": "https://colab.research.google.com/"
                    },
                    "codeSnippet": {
                        "language": "python",
                        "filename": "autograd_demo.py",
                        "code": "import torch\n\nx = torch.tensor(3.0, requires_grad=True)\nw = torch.tensor(2.0, requires_grad=True)\nb = torch.tensor(1.0, requires_grad=True)\n\ny = w * x + b\nloss = (y - 10.0) ** 2\nloss.backward()\n\nprint(f'Forward Output y: {y.item()}')\nprint(f'Loss Value      : {loss.item()}')\nprint(f'dLoss / dw      : {w.grad.item():.2f}')\nprint(f'dLoss / dx      : {x.grad.item():.2f}')",
                        "explanation": "Yeh script autograd ke dynamic DAG aur Chain Rule gradient calculation ko demonstrate karta hai.",
                        "simulationOutput": "Forward Output y: 7.0\nLoss Value      : 9.0\ndLoss / dw      : -18.00\ndLoss / dx      : -12.00\nAutograd verified successfully! 🚀"
                    },
                    "diagramScript": "flow TD: PyTorch Autograd Dynamic Graph\n  w[w: Weight (2.0)] & x[x: Input (3.0)] --> mul[Mul Node (*)]\n  mul --> wx[w * x = 6.0]\n  wx & b[b: Bias (1.0)] --> add[Add Node (+)]\n  add --> y[y = 7.0]\n  y & target[Target = 10.0] --> sub[Sub Node (-)]\n  sub --> sqr[Pow Node (^2)]\n  sqr --> loss[Loss = 9.0]\n  loss -.->|loss.backward()| w *",
                    "diagramPreset": "paper",
                    "diagramAnimate": "flow",
                    "actionItems": [
                        "Custom loss function likhein aur analytical derivative se compare karein",
                        "Multi-layer linear model train karke loss curve inspect karein"
                    ],
                    "resources": [
                        {"title": "Andrej Karpathy: Micrograd Video", "url": "https://karpathy.ai/zero-to-hero.html", "type": "course", "tag": "Tutorial"}
                    ]
                }
            ],
            "quiz": {
                "id": "quiz-mod-4",
                "title": "Module 4 Quiz: PyTorch & Autograd",
                "titleUrdu": "Module 4 Imtihan: PyTorch aur Autograd",
                "passingScore": 70,
                "xpReward": 300,
                "badgeId": "core_pytorch",
                "questions": [
                    {
                        "id": "q4-1",
                        "question": "Training loop mein optimizer.zero_grad() call karna kyun zaroori hota hai?",
                        "options": [
                            "GPU ki memory free karne ke liye",
                            "PyTorch default tor par gradients accumulate karta rehta hai; zero_grad() na karein toh pichle batches ke gradients mix ho jate hain",
                            "Model ko save karne ke liye",
                            "Learning rate barhane ke liye"
                        ],
                        "correctIndex": 1,
                        "explanation": "Default gradient accumulation PyTorch ka feature hai, isliye har step par zero_grad() karna zaroori hai.",
                        "conceptUrdu": "Optimizer Zero Grad Accumulation"
                    }
                ]
            }
        },
        {
            "id": "mod-5",
            "slug": "attention-and-transformers",
            "phaseId": "phase-2",
            "title": "Module 5: \"Attention Is All You Need\" & Modern LLMs",
            "titleUrdu": "Attention aur Transformers: Q-K-V se Mini-GPT Tak",
            "weekRange": "Weeks 9–10",
            "description": "Scaled Dot-Product Attention mathematical proof, Rotary Position Embeddings (RoPE), Multi-Head Attention, Causal Masking aur Mini-GPT decoder.",
            "realWorldDeliverable": {
                "title": "Roman Urdu Mini-GPT & Attention Heatmap",
                "urduTitle": "Roman Urdu Mini-GPT aur Attention Heatmap Engine",
                "freelanceValue": "$550 - $1,200 / Custom Domain Language Model Demo",
                "description": "A 6-layer custom character/BPE decoder-only Transformer trained on Roman Urdu poetry and conversational corpora, complete with RoPE embeddings and an interactive attention weights heatmap visualizer.",
                "steps": [
                    "Tokenize Roman Urdu corpus with custom vocabulary mapping",
                    "Implement Scaled Dot-Product Multi-Head Attention with Causal Lower-Triangular Mask",
                    "Integrate RoPE (Rotary Position Embeddings) and RMSNorm",
                    "Extract and plot token-to-token attention probability heatmaps during generation"
                ],
                "outputArtifact": "roman_urdu_mini_gpt.py + attention_weights_heatmap.png"
            },
            "zeroGpuRecipe": {
                "platform": "Google Colab Free T4 (15GB VRAM)",
                "vramRequired": "3.8 GB VRAM",
                "estimatedCost": "$0.00 Free",
                "computeUnitsTip": "from google.colab import runtime; runtime.unassign() # Disconnect immediately after Mini-GPT checkpoint export!",
                "setupSnippet": "!pip install torch matplotlib seaborn tiktoken",
                "launchUrl": "https://colab.research.google.com/"
            },
            "lessons": [
                {
                    "id": "les-5-1",
                    "slug": "scaled-dot-product-attention",
                    "title": "Lesson 5.1: Scaled Dot-Product & Multi-Head Attention",
                    "titleUrdu": "Scaled Dot-Product Attention Ka Mathematical Proof",
                    "week": 9,
                    "durationMinutes": 50,
                    "xpReward": 200,
                    "learningOutcomes": [
                        "Derive Q-K-V attention equation and the sqrt(d_k) factor",
                        "Implement Causal Autoregressive Masking in PyTorch",
                        "Plot token attention weights matrix"
                    ],
                    "romanUrduSummary": "Transformer architecture modern AI ka dil hai! Query (jo aap dhoond rahe hain), Key (jo data ke paas hai), aur Value (actual content). sqrt(d_k) se divide karne ki wajah yeh hai ke high dimensions par dot product bohot bara ho jata hai jis se Softmax ka gradient zero ho jata hai.",
                    "deepDiveExplanation": "The scale factor 1/sqrt(d_k) counters the variance growth of dot products under assumption of independent zero-mean unit-variance components. Causal masking ensures position i can only attend to positions <= i during autoregressive training.",
                    "realWorldDeliverable": {
                        "title": "Multi-Head Attention Tensor Block",
                        "urduTitle": "Multi-Head Attention Block",
                        "freelanceValue": "$400 / Architecture Component",
                        "description": "Production Multi-Head Attention layer in pure PyTorch.",
                        "steps": ["Linear projections", "Scaled dot product", "Causal masking", "Residual connection"],
                        "outputArtifact": "mha_block.py"
                    },
                    "zeroGpuRecipe": {
                        "platform": "Google Colab Free T4 / Local CPU",
                        "vramRequired": "1.5 GB",
                        "estimatedCost": "$0.00 Free",
                        "computeUnitsTip": "Mini-GPT training runs smoothly on Colab Free T4.",
                        "setupSnippet": "pip install torch matplotlib",
                        "launchUrl": "https://colab.research.google.com/"
                    },
                    "codeSnippet": {
                        "language": "python",
                        "filename": "attention_block.py",
                        "code": "import torch\nimport torch.nn.functional as F\nimport math\n\ndef scaled_dot_product_attention(Q, K, V, mask=None):\n    d_k = Q.size(-1)\n    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)\n    if mask is not None:\n        scores = scores.masked_fill(mask == 0, -1e9)\n    attn_probs = F.softmax(scores, dim=-1)\n    output = torch.matmul(attn_probs, V)\n    return output, attn_probs\n\nQ = torch.randn(1, 4, 8)\nK = torch.randn(1, 4, 8)\nV = torch.randn(1, 4, 8)\nmask = torch.tril(torch.ones(4, 4))\nout, weights = scaled_dot_product_attention(Q, K, V, mask)\nprint('Attention output tensor shape:', out.shape)\nprint('Causal Masked Weights Row 0:', weights[0, 0].tolist())",
                        "explanation": "Yeh script Causal mask ke sath Scaled Dot-Product Attention implement karta hai.",
                        "simulationOutput": "Attention output tensor shape: torch.Size([1, 4, 8])\nCausal Masked Weights Row 0: [1.0, 0.0, 0.0, 0.0]"
                    },
                    "diagramScript": "flow TD: Scaled Dot-Product Attention Flow\n  q[Query Matrix Q] & k[Key Matrix K] --> dot[MatMul: Q x K^T]\n  dot --> scale[Scale by 1/sqrt(d_k)]\n  scale --> mask{Causal Autoregressive Mask}\n  mask --> sm[Softmax Along Columns]\n  sm & v[Value Matrix V] --> out_dot[MatMul: Probs x V]\n  out_dot --> proj[Output Projection] *",
                    "diagramPreset": "grape",
                    "diagramAnimate": "flow",
                    "actionItems": [
                        "Custom 4-head MultiHeadAttention class likhein",
                        "Sinusoidal vs RoPE embeddings compare karein"
                    ],
                    "resources": [
                        {"title": "The Illustrated Transformer (Jay Alammar)", "url": "https://jalammar.github.io/illustrated-transformer/", "type": "paper", "tag": "Guide"}
                    ]
                }
            ],
            "quiz": {
                "id": "quiz-mod-5",
                "title": "Module 5 Quiz: Transformers & Attention",
                "titleUrdu": "Module 5 Imtihan: Attention aur Transformers",
                "passingScore": 70,
                "xpReward": 350,
                "badgeId": "attention_is_all_you_need",
                "questions": [
                    {
                        "id": "q5-1",
                        "question": "Attention formula mein Q x K^T ko sqrt(d_k) se divide kyun kiya jata hai?",
                        "options": [
                            "Execution speed barhane ke liye",
                            "Taake bare dimensions par dot-products bohot bare na hon aur Softmax gradients zero na ho jayein",
                            "Vectors ki length barhane ke liye",
                            "Batch size double karne ke liye"
                        ],
                        "correctIndex": 1,
                        "explanation": "Without scaling by sqrt(d_k), dot products grow large in variance, pushing Softmax into regions with extremely small gradients.",
                        "conceptUrdu": "Scaled Dot Product Gradient Vanishing Prevention"
                    }
                ]
            }
        }
    ]
}
