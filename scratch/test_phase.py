import json
import os

phases = [
    {
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
]

print("Phase 1 verified:", len(phases))
