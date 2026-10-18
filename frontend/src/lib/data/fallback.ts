// Fallback syllabus and content for standalone deployment (ai-ustaad.pages.dev)
// Ensures 100% production-ready rich UI even if Supabase is offline or not configured.

export const FALLBACK_COURSE = {
	title: 'AI Ustaad — Zero se Production tak',
	slug: 'ai-mastery-zero-to-production',
	subtitle: 'Pakistan aur South Asia ka pehla complete, production-grade Roman Urdu AI Engineering curriculum.',
	description: 'Python aur tensors se le kar Deep Learning, Transformers, Modern RAG, Autonomous Multi-Agent Systems, DeepSeek-R1 GRPO, aur Production MLOps tak.'
};

export const FALLBACK_PHASES = [
	{
		id: 'phase-1',
		phase_number: 1,
		slug: 'phase-1-foundations',
		title: 'Foundations of Modern AI',
		weeks_range: 'Weeks 1-4',
		level: 'Beginner to Intermediate',
		description: 'Python 3.12, Vectorization, Matrix Calculus, raw PyTorch tensors, autograd engine from scratch, aur Zero-GPU Cloud setups.',
		modules: [
			{
				id: 'm1',
				module_number: 1,
				slug: 'm01-python-math-for-ai',
				title: 'Python 3.12, Vectorized NumPy & Tensor Math',
				weeks_range: 'Weeks 1-2',
				estimated_hours: 24,
				real_world_deliverable: 'Vectorized NumPy & Tensor Linear Algebra Library'
			},
			{
				id: 'm2',
				module_number: 2,
				slug: 'm02-pytorch-from-scratch',
				title: 'PyTorch From Scratch & Autograd Computational Graph',
				weeks_range: 'Weeks 3-4',
				estimated_hours: 28,
				real_world_deliverable: 'Custom Micrograd-style Autograd Engine in Pure Python'
			}
		]
	},
	{
		id: 'phase-2',
		phase_number: 2,
		slug: 'phase-2-deep-learning-transformers',
		title: 'Deep Learning & Transformer Architectures',
		weeks_range: 'Weeks 5-8',
		level: 'Intermediate',
		description: 'Multi-layer Perceptrons, Backpropagation calculus, Scaled Dot-Product Attention, Multi-Head Attention, RoPE, aur KV Cache optimization.',
		modules: [
			{
				id: 'm3',
				module_number: 3,
				slug: 'm03-neural-networks-backprop',
				title: 'Neural Networks, Backpropagation & Optimizers',
				weeks_range: 'Weeks 5-6',
				estimated_hours: 26,
				real_world_deliverable: 'Full Neural Net with Custom AdamW Optimizer from scratch'
			},
			{
				id: 'm4',
				module_number: 4,
				slug: 'm04-transformers-attention-deep-dive',
				title: 'Transformers Architecture & Self-Attention Deep Dive',
				weeks_range: 'Weeks 7-8',
				estimated_hours: 32,
				real_world_deliverable: 'Production GPT-style Decoder with Causal Masking & KV Cache'
			}
		]
	},
	{
		id: 'phase-3',
		phase_number: 3,
		slug: 'phase-3-modern-rag-agents',
		title: 'Modern RAG & Autonomous Agentic Swarms',
		weeks_range: 'Weeks 9-12',
		level: 'Advanced',
		description: 'Hybrid Retrieval (Dense + Sparse BM25), Reciprocal Rank Fusion, Cohere/BGE Re-ranking, ColPali Vision Retrieval, aur Anthropic MCP tool swarms.',
		modules: [
			{
				id: 'm5',
				module_number: 5,
				slug: 'm05-production-rag-retrieval',
				title: 'Production Hybrid RAG, pgvector & Re-ranking',
				weeks_range: 'Weeks 9-10',
				estimated_hours: 30,
				real_world_deliverable: 'Enterprise RAG with PostgreSQL pgvector, BM25 & BGE Reranker'
			},
			{
				id: 'm6',
				module_number: 6,
				slug: 'm06-autonomous-agents-mcp',
				title: 'Autonomous Agents, Anthropic MCP & smolagents',
				weeks_range: 'Weeks 11-12',
				estimated_hours: 34,
				real_world_deliverable: 'Multi-Agent Code-Execution Swarm using Model Context Protocol'
			}
		]
	},
	{
		id: 'phase-4',
		phase_number: 4,
		slug: 'phase-4-fine-tuning-reasoning',
		title: 'Fine-Tuning, Reasoning Models & GRPO',
		weeks_range: 'Weeks 13-16',
		level: 'Expert',
		description: 'Unsloth QLoRA 4-bit fine-tuning, Dataset curation, DeepSeek-R1 GRPO (Group Relative Policy Optimization) without critic models.',
		modules: [
			{
				id: 'm7',
				module_number: 7,
				slug: 'm07-qlora-unsloth-finetuning',
				title: 'QLoRA & Unsloth Zero-GPU Fine-Tuning',
				weeks_range: 'Weeks 13-14',
				estimated_hours: 28,
				real_world_deliverable: 'Fine-tuned Roman Urdu Medical & Legal 8B Specialist LLM'
			},
			{
				id: 'm8',
				module_number: 8,
				slug: 'm08-deepseek-grpo-reasoning',
				title: 'DeepSeek-R1 GRPO Reinforcement Learning',
				weeks_range: 'Weeks 15-16',
				estimated_hours: 32,
				real_world_deliverable: 'Self-Verifying Chain-of-Thought Math Solver trained via GRPO'
			}
		]
	},
	{
		id: 'phase-5',
		phase_number: 5,
		slug: 'phase-5-production-mlops',
		title: 'Enterprise MLOps & High-Performance Rust Gateways',
		weeks_range: 'Weeks 17-20',
		level: 'Mastery / Production',
		description: 'Rust Axum 0.8 streaming microservices, vLLM Continuous Batching, OpenTelemetry tracing, LLM evaluation pipelines, aur Capstone deployment.',
		modules: [
			{
				id: 'm9',
				module_number: 9,
				slug: 'm09-rust-axum-ai-gateway',
				title: 'Rust Axum 0.8 High-Performance AI Gateway',
				weeks_range: 'Weeks 17-18',
				estimated_hours: 30,
				real_world_deliverable: 'Sub-millisecond Rust Axum SSE Streaming Gateway'
			},
			{
				id: 'm10',
				module_number: 10,
				slug: 'm10-production-mlops-capstone',
				title: 'Production MLOps, Tracing & Enterprise Capstone',
				weeks_range: 'Weeks 19-20',
				estimated_hours: 36,
				real_world_deliverable: 'Production Enterprise Capstone deployed to Cloudflare Pages'
			}
		]
	}
];

export const FALLBACK_TRACKS = [
	{
		id: 'track-a',
		track_code: 'Track A',
		title: 'Software Engineers to AI Engineers',
		description: 'Full-stack aur backend developers ke liye optimized path: Python, PyTorch, RAG, MCP swarms aur Rust Axum gateways.',
		topics: ['Vector Databases & Embeddings', 'Model Context Protocol (MCP)', 'Rust High-Throughput Microservices', 'OpenTelemetry Tracing']
	},
	{
		id: 'track-b',
		track_code: 'Track B',
		title: 'Data Scientists to LLM Specialists',
		description: 'Pandas aur Scikit-Learn users ke liye: Transformers, LoRA/QLoRA fine-tuning, DeepSeek GRPO reasoning, aur synthetic dataset generation.',
		topics: ['Unsloth 4-bit Quantization', 'Group Relative Policy Optimization', 'Direct Preference Optimization (DPO)', 'Multi-Head Attention Math']
	},
	{
		id: 'track-c',
		track_code: 'Track C',
		title: 'Zero to Hero (Beginners & Students)',
		description: 'Bina gaming GPU ke pehli baar AI seekhne walay students ke liye: Free Colab T4, Kaggle 30h, aur step-by-step Roman Urdu.',
		topics: ['Zero-GPU Cloud Survival Guide', 'Python 3.12 First-Principles', 'Visual Intuition with DiagramKit', 'Free Cloud Hosting on Cloudflare']
	}
];

export const FALLBACK_BLOGS = [
	{
		id: 'blog-1',
		slug: 'transformer-attention-math-roman-urdu',
		title: 'Scaled Dot-Product Attention: First-Principles Tensor Math in Roman Urdu',
		category: 'Deep Learning',
		reading_time_minutes: 8,
		summary_roman_urdu: 'Transformer attention formula Q*K^T/sqrt(d_k)*V ka step-by-step mathematical derivation aur PyTorch tensor implementation.',
		diagram_script: `@preset midnight\n@animate flow\nflow LR: Attention Math\n  q[Query Q] -> dot((MatMul))\n  k[Key K] -> dot\n  dot -> sm[Softmax Weights] ~purple\n  v[Value V] -> out_mult((MatMul))\n  sm -> out_mult -> out[Attended Context]* ~ok`
	},
	{
		id: 'blog-2',
		slug: 'modern-hybrid-rag-colpali-pgvector',
		title: '2026 Modern RAG: ColPali Vision Retrieval, BM25 & pgvector Re-ranking',
		category: 'Architecture',
		reading_time_minutes: 10,
		summary_roman_urdu: 'Purane chunking ko alvida bolein: Hybrid retrieval, Reciprocal Rank Fusion, aur Cohere Cross-Encoder re-ranking ka complete production blueprint.',
		diagram_script: `@preset midnight\n@animate pulse\narch LR: Hybrid RAG Pipeline\n  query[Query] -> dense[pgvector] $database\n  query -> sparse[BM25] $terminal\n  dense -> rrf[RRF Fusion] ~purple\n  sparse -> rrf\n  rrf -> rerank[BGE Reranker] ~teal\n  rerank -> llm[LLM Context]* ~ok $brain`
	},
	{
		id: 'blog-3',
		slug: 'deepseek-r1-grpo-unsloth-zero-gpu',
		title: 'DeepSeek-R1 GRPO & Unsloth QLoRA: Fine-Tuning Reasoning on Free Google Colab',
		category: 'Fine-Tuning',
		reading_time_minutes: 12,
		summary_roman_urdu: 'Critic model ke baghair Group Relative Policy Optimization (GRPO) kaise kaam karta hai aur 100% free Colab T4 par kaise chalayein.',
		diagram_script: `@preset midnight\n@animate wave\narch LR: DeepSeek GRPO\n  prompt[Prompt] -> llm[LLM Policy] $brain\n  llm -> g1[Group Candidate 1] ~info\n  llm -> g2[Group Candidate 2] ~teal\n  g1 -> norm[Group Normalization] ~purple\n  g2 -> norm\n  norm -> update[Policy Gradient Update]* ~ok $cpu`
	}
];
