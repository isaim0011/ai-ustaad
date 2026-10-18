// Fallback syllabus and content for standalone deployment (ai-ustaad.pages.dev)
// Ensures 100% production-ready rich UI even if Supabase is offline or not configured.

import type {
	HfSubproject,
	PracticeProject,
	PracticeCheckpoint,
	ZeroGpuRecipe,
	LessonData,
	ModuleData,
	PhaseData
} from '$lib/types';

export type {
	HfSubproject,
	PracticeProject,
	PracticeCheckpoint,
	ZeroGpuRecipe,
	LessonData,
	ModuleData,
	PhaseData
};

export const FALLBACK_COURSE = {
	title: 'AI Ustaad — Zero se Production tak',
	slug: 'ai-mastery-zero-to-production',
	subtitle: 'Pakistan aur South Asia ka pehla complete, production-grade Roman Urdu AI Engineering curriculum.',
	description: 'Python aur tensors se le kar Deep Learning, Transformers, Modern RAG, Autonomous Multi-Agent Systems, DeepSeek-R1 GRPO, aur Production MLOps tak.'
};

export const FALLBACK_PHASES: PhaseData[] = [
	// =========================================================================
	// PHASE 0: Prerequisite Track - Python Zero Se Hero
	// =========================================================================
	{
		id: 'phase-0',
		phase_number: 0,
		slug: 'phase-0-python-prerequisite',
		title: 'Prerequisite Track: Python Zero Se Hero',
		weeks_range: 'Weeks 0 (Prerequisite)',
		level: 'Absolute Beginner (Zero Coding Knowledge)',
		description: 'Naye hain aur Python nahi aati? Pareshan na hon! Zero se variable declare karne se le kar OOP, API requests, aur vectorized NumPy tensor math tak sab kuch practical Roman Urdu mein seekhein.',
		order_index: 0,
		modules: [
			{
				id: 'm0',
				phase_id: 'phase-0',
				module_number: 0,
				slug: 'm00-python-zero-se-hero',
				title: 'Module 0: Python Zero Se Hero (Beginner to AI Engineer)',
				weeks_range: 'Prerequisite (1-2 Weeks)',
				estimated_hours: 16,
				real_world_deliverable: 'Chai Dhaba Billing & Khata System (OOP + JSON Persistence + Discount Engine)',
				badge_slug: 'python-ustad',
				order_index: 0,
				diagram_script: `@preset midnight
@animate flow
flow LR: Python Zero Se Hero Pipeline
  p1[0.1: Variables & Logic] $terminal -> p2[0.2: Functions & Types] ~info $code
  p2 -> p3[0.3: Lists & Dicts] ~purple $database
  p3 -> p4[0.4: OOP & Dataclass] ~teal $brain
  p4 -> p5[0.5: Files, JSON & APIs] ~warn $server
  p5 -> p6[0.6: NumPy & Fast Math]* ~ok $cpu`,
				diagram_preset: 'midnight',
				diagram_animation: 'flow',
				zero_gpu_recipe: {
					platform: 'Local CPU / Google Colab Free Tier',
					vram_required: '0 GB (Any PC / Laptop)',
					estimated_cost: '$0.00 Free',
					compute_units_tip: 'Python standard library runs completely offline without burning any cloud credits or GPU compute.',
					one_click_command: 'python -m pip install numpy pandas requests && python main.py',
					unassign_code: '# Run completely free on CPU without GPU overhead\nprint("Python Zero Se Hero environment active!")'
				},
				practice_project: {
					title: 'Chai Dhaba Billing & Khata System',
					humorous_badge: 'Dhabay Ka Pythoneer',
					description_roman_urdu: 'CLI application jo customer orders calculate kare, dost-yaar discounts lagaye, aur JSON khata file update kare.',
					colab_url: 'https://colab.research.google.com/#create=true',
					xp_reward: 150,
					checklist: [
						'User se terminal par order input lena (Chai, Paratha, Bun Kabab, Samosay)',
						'Class CustomerKhata banana with @dataclass for balance & debt tracking',
						'Dost-yaar discount code ("BHAI_KA_KHATA" = 15% discount) apply karna',
						'JSON file mein customer ka khata serialize aur reload karna',
						'CLI colored receipt generate karna with timestamp aur tax calculation'
					]
				},
				learning_outcomes: [
					'Variables, data types (int, float, str, bool), aur control flow (if/else, loops)',
					'Functions, return values, default parameters, aur modern Python 3.12 type annotations',
					'Memory references, shallow vs deep copy, aur list/dict comprehensions',
					'Object-Oriented Programming (OOP): Classes, methods, inheritance, aur @dataclass',
					'File handling (with open), JSON serialization, aur HTTP API requests',
					'NumPy 1D/2D array creation, vector dot products, aur Pandas/Polars introduction'
				],
				practical_tasks: [
					'Calculator with error handling for division by zero',
					'Dictionary-based inventory manager with search and update',
					'Student report card generator with custom class and method',
					'JSON-based khata database reading and writing to disk',
					'Fetch live weather or currency exchange rate via public REST API'
				],
				lessons: [
					{
						id: 'l0-1',
						module_id: 'm0',
						lesson_code: '0.1',
						slug: '01-python-zero-se-shuru-variables',
						title: 'Python Zero Se Shuru: Variables, Data Types & Control Flow',
						duration_minutes: 20,
						lesson_type: 'theory_and_code',
						order_index: 1,
						xp_reward: 25,
						english_summary: 'Master fundamental Python syntax: dynamic typing, f-strings, conditional branching (if/elif/else), and for/while loops from first principles.',
						roman_urdu_content: `Assalam-o-Alaikum aur welcome to Python Zero Se Hero! Agar aap ne zindagi mein kabhi aik line ka code bhi nahi likha, to pareshan hone ki bilkul zaroorat nahi. Hum bilkul zero se shuru karenge.

Python aik bohot simple aur human-friendly language hai. Yahan aapko C++ ya Java ki tarah semicolons ya complicated syntax nahi likhna parta.

### 1. Variables Aur Data Types
Variable ka matlab hota hai aik dabba (container) jisme aap koi value store karte hain:
- \`int\`: Integer numbers jaise \`chai_cups = 3\`
- \`float\`: Decimals jaise \`chai_price = 40.50\`
- \`str\`: Text / String jaise \`customer_name = "Ali Bhai"\`
- \`bool\`: True ya False jaise \`is_vip = True\`

### 2. Modern F-Strings
Python 3.6+ mein string formatting sab se asan hai:
\`\`\`python
print(f"{customer_name} ne {chai_cups} chai pi, total: Rs. {chai_cups * chai_price}")
\`\`\`

### 3. Decisions: if, elif, else
Program ko faisla karne ke liye conditions dete hain:
\`\`\`python
total = chai_cups * chai_price
if total > 500:
    discount = total * 0.10
    total -= discount
    print("Mubarak ho! 10% discount mil gaya!")
\`\`\``,
						code_example: `# Chai Dhaba Billing Script
customer = "Zeeshan"
chai_cups = 4
cup_price = 40
special_paratha = 2
paratha_price = 80

total = (chai_cups * cup_price) + (special_paratha * paratha_price)

print(f"=== DHABA BILL FOR {customer.upper()} ===")
print(f"Chai: {chai_cups} x {cup_price} = Rs. {chai_cups * cup_price}")
print(f"Paratha: {special_paratha} x {paratha_price} = Rs. {special_paratha * paratha_price}")
print(f"Grand Total: Rs. {total}")

if total >= 200:
    print("Complimentary saunf & elaichi included! ")`
					},
					{
						id: 'l0-2',
						module_id: 'm0',
						lesson_code: '0.2',
						slug: '02-functions-lambdas-type-hints',
						title: 'Functions, Lambda & Modern Type Hints (Python 3.12+)',
						duration_minutes: 22,
						lesson_type: 'theory_and_code',
						order_index: 2,
						xp_reward: 25,
						english_summary: 'Understand modular functions, positional vs keyword arguments, lambda expressions, and modern Python 3.12 static type annotations.',
						roman_urdu_content: `Functions ka maqsad hota hai DRY principle: "Don't Repeat Yourself". Jab koi calculation bar bar karni ho, usko aik function mein band kar dete hain.

### 1. Functions With Type Hints (Python 3.12+)
Modern AI engineering mein type hints bohot zaroori hain taake PyTorch aur FastAPI models strict checking kar sakein:
\`\`\`python
def calculate_bill(items: list[float], tax_rate: float = 0.16) -> float:
    subtotal = sum(items)
    return subtotal + (subtotal * tax_rate)
\`\`\`

### 2. Lambda Functions
Choti one-liner anonymous functions ko lambda kehte hain:
\`\`\`python
discount = lambda amount: amount * 0.90 if amount > 1000 else amount
\`\`\``,
						code_example: `from typing import List

def generate_dhaba_invoice(items: List[dict], customer: str, is_regular: bool = False) -> dict:
    subtotal = sum(item["price"] * item["qty"] for item in items)
    discount_pct = 0.15 if is_regular else 0.0
    discount_amount = subtotal * discount_pct
    final_amount = subtotal - discount_amount
    
    return {
        "customer": customer,
        "subtotal": subtotal,
        "discount_applied": discount_amount,
        "total_payable": final_amount
    }

order = [
    {"name": "Karak Chai", "price": 50, "qty": 3},
    {"name": "Aalo Paratha", "price": 90, "qty": 2}
]

invoice = generate_dhaba_invoice(order, "Hamza Bhai", is_regular=True)
print(f"Invoice for {invoice['customer']}: Rs. {invoice['total_payable']} (Saved: Rs. {invoice['discount_applied']})")`
					},
					{
						id: 'l0-3',
						module_id: 'm0',
						lesson_code: '0.3',
						slug: '03-data-structures-lists-dicts',
						title: 'Data Structures Mastery: Lists, Dicts, Tuples & Memory References',
						duration_minutes: 25,
						lesson_type: 'theory_and_code',
						order_index: 3,
						xp_reward: 30,
						english_summary: 'Master lists, dictionaries, tuples, sets, memory references, and list/dict comprehensions essential for preparing training datasets.',
						roman_urdu_content: `AI models data par train hote hain, aur Python mein data handle karne ke liye char bunyadi structures hain:
1. **Lists \`[]\`**: Ordered, mutable sequence (elements add/remove ho sakte hain).
2. **Tuples \`()\`**: Immutable (change nahi ho sakta, faster & memory efficient).
3. **Dictionaries \`{}\`**: Key-Value pairs, $O(1)$ fast lookup speed.
4. **Sets \`set()\`**: Unique elements, duplicates auto-remove karta hai.

### List & Dict Comprehensions
Comprehensions Python ka sab se pyara feature hai jo 5 lines ke loop ko 1 line mein convert karta hai:
\`\`\`python
squares = [x**2 for x in range(10) if x % 2 == 0]
\`\`\``,
						code_example: `# Menu & Orders Management
menu = {
    "karak_chai": 50,
    "doodh_patti": 70,
    "anda_ghotala": 150,
    "sada_paratha": 60
}

# Comprehension: Filter items under Rs. 100
budget_items = {k: v for k, v in menu.items() if v <= 70}
print("Budget Items:", budget_items)

# List of orders
orders = ["karak_chai", "sada_paratha", "karak_chai", "doodh_patti"]
bill = sum(menu[item] for item in orders)
unique_ordered_items = set(orders)

print(f"Total Bill: Rs. {bill}")
print(f"Unique items ordered: {unique_ordered_items}")`
					},
					{
						id: 'l0-4',
						module_id: 'm0',
						lesson_code: '0.4',
						slug: '04-oop-classes-dataclasses',
						title: 'Object-Oriented Programming (OOP) for AI: Classes, Methods & @dataclass',
						duration_minutes: 26,
						lesson_type: 'theory_and_code',
						order_index: 4,
						xp_reward: 30,
						english_summary: 'Understand classes, objects, encapsulated state, inheritance, and Python 3.12 dataclasses used in PyTorch modules and AI agent configs.',
						roman_urdu_content: `PyTorch ka har neural network aik Class hota hai (\`class MyModel(nn.Module):\`). Is liye OOP seekhna AI Engineer banne ke liye lazmi hai!

### 1. Classes & Self
Class aik blueprint hai (jaise ghar ka naksha), aur Object actual ghar hai:
\`\`\`python
class DhabaOrder:
    def __init__(self, customer_name: str):
        self.customer = customer_name
        self.items = []
        
    def add_item(self, item_name: str, price: float):
        self.items.append((item_name, price))
\`\`\`

### 2. Modern @dataclass
Python 3.7+ mein boilerplate \`__init__\` likhne ki zaroorat nahi:
\`\`\`python
from dataclasses import dataclass

@dataclass
class CustomerKhata:
    name: str
    phone: str
    current_balance: float = 0.0
\`\`\``,
						code_example: `from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class OrderItem:
    name: str
    price: float
    quantity: int = 1
    
    @property
    def total(self) -> float:
        return self.price * self.quantity

@dataclass
class DhabaKhata:
    customer_name: str
    phone: str
    orders: List[OrderItem] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M"))
    
    def add(self, item_name: str, price: float, quantity: int = 1):
        self.orders.append(OrderItem(item_name, price, quantity))
        
    def calculate_total_debt(self) -> float:
        return sum(item.total for item in self.orders)

# Usage
ali_khata = DhabaKhata(customer_name="Ali Khan", phone="0300-1234567")
ali_khata.add("Special Chai", 60, 2)
ali_khata.add("Maska Bun", 50, 1)

print(f"{ali_khata.customer_name} ka total udhar: Rs. {ali_khata.calculate_total_debt()}")`
					},
					{
						id: 'l0-5',
						module_id: 'm0',
						lesson_code: '0.5',
						slug: '05-file-handling-json-parquet-api',
						title: 'File Handling, JSON, Parquet & API Requests',
						duration_minutes: 24,
						lesson_type: 'theory_and_code',
						order_index: 5,
						xp_reward: 30,
						english_summary: 'Read and write local files with context managers, serialize structured JSON, handle columnar Parquet, and make HTTP requests to remote AI APIs.',
						roman_urdu_content: `AI models train karne ke liye aapko hard drive se text files, JSON datasets, aur remote APIs se data stream karna hota hai.

### 1. Safe File Handling with \`with open()\`
\`with\` keyword ensure karta hai ke file par kaam khatam hone ke baad memory leak na ho aur file automatically close ho jaye:
\`\`\`python
with open("khata.json", "w") as f:
    json.dump(data, f, indent=2)
\`\`\`

### 2. HTTP Requests for AI APIs
Model ko prompt bhejna ya web data scrape karna:
\`\`\`python
import requests
res = requests.get("https://api.github.com/users/isaim0011")
print(res.json()["name"])
\`\`\``,
						code_example: `import json
import os

khata_db = {
    "03001234567": {
        "name": "Babar Azam",
        "balance": 450,
        "history": ["Chai x 3", "Paratha x 2"]
    },
    "03119876543": {
        "name": "Rizwan",
        "balance": 120,
        "history": ["Doodh Patti x 2"]
    }
}

# 1. Save to JSON
with open("dhaba_khata.json", "w", encoding="utf-8") as f:
    json.dump(khata_db, f, indent=4)
print("Khata successfully written to disk!")

# 2. Read back
with open("dhaba_khata.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

for phone, info in loaded_data.items():
    print(f"Customer: {info['name']} ({phone}) -> Balance: Rs. {info['balance']}")

# Clean up temporary test file
if os.path.exists("dhaba_khata.json"):
    os.remove("dhaba_khata.json")`
					},
					{
						id: 'l0-6',
						module_id: 'm0',
						lesson_code: '0.6',
						slug: '06-numpy-pandas-foundations',
						title: 'NumPy & Pandas Foundations: Vectors, Matrices & Fast Data Manipulation',
						duration_minutes: 28,
						lesson_type: 'theory_and_code',
						order_index: 6,
						xp_reward: 35,
						english_summary: 'Bridge from pure Python to scientific vector math: NumPy arrays, multidimensional matrices, vector dot products, and high-performance tabular manipulation.',
						roman_urdu_content: `Congratulations! Aap Module 0 ke aakhri aur sab se crucial step par pohanch gaye hain. Yahan se aapka safar Pure Python se nikal kar High-Performance AI Engineering mein dakhil hota hai!

NumPy Python ka core scientific computing package hai. Pure Python list ke muqable mein NumPy arrays 50 se 100 guna tez chalte hain kyun ke yeh C-contiguous memory blocks aur CPU SIMD instructions use karte hain.

### 1. Vectors Aur Matrices
- Scalar: 0D number (\`x = 5\`)
- Vector: 1D array of numbers (\`v = np.array([1.5, -0.4, 3.2])\`)
- Matrix: 2D grid of numbers (\`M = np.array([[1, 2], [3, 4]])\`)
- Tensor: 3D ya us se zyada dimensions!

### 2. Vector Dot Product
Dot product semantic search aur neural net weights calculation ki jaan hai:
\`\`\`python
dot = np.dot(vector_a, vector_b)
\`\`\``,
						code_example: `import numpy as np

# 1. Vectorized Menu Pricing
quantities = np.array([4, 2, 3, 1], dtype=np.int32) # Chai, Paratha, Samosa, Bun
prices = np.array([50.0, 80.0, 30.0, 60.0], dtype=np.float32)

# Vector Dot Product in 1 line without loops!
total_bill = np.dot(quantities, prices)
print(f"Total calculated via Vector Dot Product: Rs. {total_bill:.2f}")

# 2. 2D Matrix of Multiple Table Orders
orders_matrix = np.array([
    [2, 1, 0, 1], # Table 1
    [4, 0, 4, 0], # Table 2
    [1, 3, 2, 2]  # Table 3
])

table_totals = np.dot(orders_matrix, prices)
for i, bill in enumerate(table_totals, start=1):
    print(f"Table {i} Bill: Rs. {bill:.2f}")`
					}
				]
			}
		]
	},

	// =========================================================================
	// PHASE 1: Foundations of Modern AI
	// =========================================================================
	{
		id: 'phase-1',
		phase_number: 1,
		slug: 'phase-1-foundations',
		title: 'Phase 1: Foundations of Modern AI',
		weeks_range: 'Weeks 1-4',
		level: 'Beginner to Intermediate',
		description: 'Python 3.12, Vectorization, Matrix Calculus, raw PyTorch tensors, autograd engine from scratch, aur Zero-GPU Cloud setups.',
		order_index: 1,
		modules: [
			{
				id: 'm1',
				phase_id: 'phase-1',
				module_number: 1,
				slug: 'python-for-ai-and-fast-math',
				title: 'Module 1: Python for AI & Fast Math (NumPy, Linear Algebra)',
				weeks_range: 'Weeks 1-2',
				estimated_hours: 24,
				real_world_deliverable: '500k E-Commerce Order Sanitizer & Parquet Data Pipeline',
				badge_slug: 'pehla-prompt',
				order_index: 1,
				diagram_script: `@preset midnight
@animate flow
flow LR: Module 1 Fast Math & Vector Pipeline
  py_list[Python List Overhead] $code -> numpy_arr[Contiguous C NumPy Array] $cpu
  numpy_arr -> simd[SIMD Vectorized Dot Product] $terminal
  simd -> loss[Loss Surface & Gradient Descent]* ~ok $brain`,
				diagram_preset: 'midnight',
				diagram_animation: 'flow',
				zero_gpu_recipe: {
					platform: 'Local CPU / Google Colab Free Tier',
					vram_required: '0 GB (CPU)',
					estimated_cost: '$0.00 Free',
					compute_units_tip: 'NumPy AVX-512 vectorization runs blazing fast on standard Colab CPU without burning any GPU compute units.',
					one_click_command: 'python -m pip install numpy polars pyarrow pydantic && python main.py',
					unassign_code: '# CPU run does not consume GPU quota\nprint("CPU Pipeline Finished")'
				},
				practice_project: {
					title: 'Biryani vs Pulao Sentiment Analyzer',
					humorous_badge: 'Biryani Scientist',
					description_roman_urdu: 'Twitter/X aur food reviews dataset se Biryani vs Pulao ki sentimental jung analyze karein using fast vectorized NumPy operations.',
					colab_url: 'https://colab.research.google.com/#create=true',
					xp_reward: 175,
					checklist: [
						'Food review dataset tokenize karna (Karachi, Lahore & Rawalpindi reviews)',
						'NumPy vectorized bag-of-words frequency matrix banana',
						'Cosine similarity dot product se sentiment score calculate karna',
						'Biryani vs Pulao sentiment polarity leaderboard print karna'
					]
				}
			},
			{
				id: 'm2',
				phase_id: 'phase-1',
				module_number: 2,
				slug: 'm02-pytorch-from-scratch',
				title: 'Module 2: PyTorch From Scratch & Autograd Graph',
				weeks_range: 'Weeks 3-4',
				estimated_hours: 28,
				real_world_deliverable: 'Custom Micrograd-style Autograd Engine in Pure Python',
				badge_slug: 'tensor-jawan',
				order_index: 2,
				diagram_script: `@preset midnight
@animate flow
flow LR: Autograd Computational Graph
  w[Weight W] ~info -> mul((MatMul)) $cpu
  x[Input X] -> mul
  mul -> add((Add Bias)) ~purple
  b[Bias B] -> add
  add -> loss[MSE Loss]* ~ok $brain`,
				diagram_preset: 'midnight',
				diagram_animation: 'flow',
				zero_gpu_recipe: {
					platform: 'Google Colab Free Tier (CPU/T4)',
					vram_required: '0 GB (CPU)',
					estimated_cost: '$0.00 Free',
					compute_units_tip: 'Autograd scalar graphs compile instantly on CPU.',
					one_click_command: 'python -m pip install torch && python autograd_test.py',
					unassign_code: 'from google.colab import runtime\nruntime.unassign()'
				},
				practice_project: {
					title: 'Rishta Matcher Algorithm',
					humorous_badge: 'Rishta Optimizer',
					description_roman_urdu: 'Candidate bios aur mother-in-law (Ami) ki strict criteria ke darmiyan Cosine similarity vector distance calculate karein.',
					colab_url: 'https://colab.research.google.com/#create=true',
					xp_reward: 200,
					checklist: [
						'Candidate profiles ka feature vector banana (Chai making, Salary, Humor, Punctuality)',
						'Ami ka ideal candidate vector formulate karna',
						'High-dimensional normalized cosine distance compute karna',
						'Top-3 approved candidates ki leaderboard generate karna'
					]
				}
			}
		]
	},

	// =========================================================================
	// PHASE 2: Deep Learning & Transformer Architectures
	// =========================================================================
	{
		id: 'phase-2',
		phase_number: 2,
		slug: 'phase-2-deep-learning-transformers',
		title: 'Phase 2: Deep Learning & Transformer Architectures',
		weeks_range: 'Weeks 5-8',
		level: 'Intermediate',
		description: 'Multi-layer Perceptrons, Backpropagation calculus, Scaled Dot-Product Attention, Multi-Head Attention, RoPE, aur KV Cache optimization.',
		order_index: 2,
		modules: [
			{
				id: 'm3',
				phase_id: 'phase-2',
				module_number: 3,
				slug: 'm03-neural-networks-backprop',
				title: 'Module 3: Neural Networks, Backpropagation & Optimizers',
				weeks_range: 'Weeks 5-6',
				estimated_hours: 26,
				real_world_deliverable: 'Full Neural Net with Custom AdamW Optimizer from scratch',
				badge_slug: 'backprop-badshah',
				order_index: 3,
				diagram_script: `@preset midnight
@animate flow
flow LR: Backprop Gradient Flow
  fwd[Forward Pass] ~info -> loss[Loss Calculation] $brain
  loss -> bwd[Backward Gradient Accumulation] ~purple
  bwd -> adamw[AdamW Weight Decay Step]* ~ok $cpu`,
				diagram_preset: 'midnight',
				diagram_animation: 'flow',
				practice_project: {
					title: 'Cricketer Performance Predictor',
					humorous_badge: 'PSL Analyst',
					description_roman_urdu: 'PSL / IPL match outcome aur player score predictor with LightGBM & regression.',
					colab_url: 'https://colab.research.google.com/#create=true',
					xp_reward: 200,
					checklist: [
						'Ball-by-ball match dataset load karna',
						'Pitch conditions & strike-rate momentum features engineer karna',
						'Custom neural net / gradient boosting model train karna',
						'Live match win-probability chart predict karna'
					]
				}
			},
			{
				id: 'm4',
				phase_id: 'phase-2',
				module_number: 4,
				slug: 'm04-transformers-attention-deep-dive',
				title: 'Module 4: Transformers Architecture & Self-Attention Deep Dive',
				weeks_range: 'Weeks 7-8',
				estimated_hours: 32,
				real_world_deliverable: 'Production GPT-style Decoder with Causal Masking & KV Cache',
				badge_slug: 'attention-all-you-need',
				order_index: 4,
				diagram_script: `@preset midnight
@animate flow
flow LR: Transformer Attention Block
  tok[Tokens] $terminal -> qkv[Q, K, V Projections] ~purple
  qkv -> attn[Scaled Dot-Product Attention] $brain
  attn -> mlp[SwiGLU Feed Forward] ~teal
  mlp -> out[Next Token Probabilities]* ~ok $server`,
				diagram_preset: 'midnight',
				diagram_animation: 'flow',
				practice_project: {
					title: 'Meme Classifier & Roast Bot',
					humorous_badge: 'Meme Lord',
					description_roman_urdu: 'PyTorch CNN jo spicy memes vs wholesome cat pictures classify kare aur automatically funny roasts generate kare.',
					colab_url: 'https://colab.research.google.com/#create=true',
					xp_reward: 225,
					checklist: [
						'Custom PyTorch Dataset & DataLoader likhna',
						'Convolutional + BatchNorm layers implement karna',
						'Classification evaluation metric evaluate karna',
						'Roast bot prompt loop attach karna'
					]
				}
			}
		]
	},

	// =========================================================================
	// PHASE 3: Modern RAG & Autonomous Agentic Swarms
	// =========================================================================
	{
		id: 'phase-3',
		phase_number: 3,
		slug: 'phase-3-modern-rag-agents',
		title: 'Phase 3: Modern RAG & Autonomous Agentic Swarms',
		weeks_range: 'Weeks 9-12',
		level: 'Advanced',
		description: 'Hybrid Retrieval (Dense + Sparse BM25), Reciprocal Rank Fusion, Cohere/BGE Re-ranking, ColPali Vision Retrieval, aur Anthropic MCP tool swarms.',
		order_index: 3,
		modules: [
			{
				id: 'm5',
				phase_id: 'phase-3',
				module_number: 5,
				slug: 'm05-production-rag-retrieval',
				title: 'Module 5: Production Hybrid RAG, pgvector & Re-ranking',
				weeks_range: 'Weeks 9-10',
				estimated_hours: 30,
				real_world_deliverable: 'Enterprise RAG with PostgreSQL pgvector, BM25 & BGE Reranker',
				badge_slug: 'rag-ka-sikandar',
				order_index: 5,
				diagram_script: `@preset midnight
@animate flow
flow LR: Enterprise Hybrid RAG
  query[User Query] -> dense[Dense pgvector HNSW] $database
  query -> sparse[Sparse BM25 Index] $terminal
  dense -> rrf[Reciprocal Rank Fusion] ~purple
  sparse -> rrf
  rrf -> rerank[BGE Cross-Encoder Reranker] ~teal
  rerank -> llm[Grounded LLM Response]* ~ok $brain`,
				diagram_preset: 'midnight',
				diagram_animation: 'flow',
				practice_project: {
					title: 'Biryani Recipe RAG with Exact Spices',
					humorous_badge: 'Nani Ammi Approved',
					description_roman_urdu: 'Vector search system jo dadi/nani ki handwritten recipe book se exact page aur grams of aloo bukhara cite kare.',
					colab_url: 'https://colab.research.google.com/#create=true',
					xp_reward: 260,
					checklist: [
						'Recipe PDF parse karke text & tables extract karna',
						'pgvector HNSW index create karna',
						'BM25 sparse search aur dense embeddings fuse karna',
						'Exact source page and spice grams verify karke answer dena'
					]
				}
			},
			{
				id: 'm6',
				phase_id: 'phase-3',
				module_number: 6,
				slug: 'm06-autonomous-agents-mcp',
				title: 'Module 6: Autonomous Agents, Anthropic MCP & smolagents',
				weeks_range: 'Weeks 11-12',
				estimated_hours: 34,
				real_world_deliverable: 'Multi-Agent Code-Execution Swarm using Model Context Protocol',
				badge_slug: 'agent-commander',
				order_index: 6,
				diagram_script: `@preset midnight
@animate flow
flow LR: Anthropic MCP Agent Loop
  user[User Request] -> lead[Lead Orchestrator Agent] $brain
  lead -> mcp[Model Context Protocol Server] ~purple $server
  mcp -> tools[Tools: Bash, Python, SQL, Browser] $terminal
  tools -> verify[Output Verification Gate] ~teal
  verify -> lead
  verify -> done[Final Task Solved]* ~ok`,
				diagram_preset: 'midnight',
				diagram_animation: 'flow',
				practice_project: {
					title: 'Ami Ka WhatsApp Reply Bot',
					humorous_badge: 'Farmanbardar Beta',
					description_roman_urdu: 'FastAPI streaming auto-responder for family groups with respectful polite excuses.',
					colab_url: 'https://colab.research.google.com/#create=true',
					xp_reward: 220,
					checklist: [
						'FastAPI async SSE endpoint banana',
						'Pakistani family respectful tone system prompt craft karna',
						'Tool call se calendar check karke legitimate excuses schedule karna',
						'Response streaming under 200ms latency maintain karna'
					]
				}
			}
		]
	},

	// =========================================================================
	// PHASE 4: Fine-Tuning, Reasoning Models & GRPO
	// =========================================================================
	{
		id: 'phase-4',
		phase_number: 4,
		slug: 'phase-4-fine-tuning-reasoning',
		title: 'Phase 4: Fine-Tuning, Reasoning Models & GRPO',
		weeks_range: 'Weeks 13-16',
		level: 'Expert',
		description: 'Unsloth QLoRA 4-bit fine-tuning, Dataset curation, DeepSeek-R1 GRPO (Group Relative Policy Optimization) without critic models.',
		order_index: 4,
		modules: [
			{
				id: 'm7',
				phase_id: 'phase-4',
				module_number: 7,
				slug: 'm07-qlora-unsloth-finetuning',
				title: 'Module 7: QLoRA & Unsloth Zero-GPU Fine-Tuning',
				weeks_range: 'Weeks 13-14',
				estimated_hours: 28,
				real_world_deliverable: 'Fine-tuned Roman Urdu Medical & Legal 8B Specialist LLM',
				badge_slug: 'unsloth-wizard',
				order_index: 7,
				diagram_script: `@preset midnight
@animate flow
flow LR: Unsloth 4-bit QLoRA
  base[Base Model Weights (Frozen 4-bit)] $cpu -> adapter[LoRA Rank-16 Adapters] ~teal
  data[Curated Dataset] -> loss[Cross-Entropy Loss] $brain
  loss -> adapter
  adapter -> fused[Exported GGUF / 16-bit Model]* ~ok $server`,
				diagram_preset: 'midnight',
				diagram_animation: 'flow',
				practice_project: {
					title: 'Roman Urdu Sarcasm Detector',
					humorous_badge: 'Tanz Specialist',
					description_roman_urdu: 'Unsloth 4-bit fine-tuned LLaMA model on Colab Free T4 identifying sarcastic Pakistani tweets and irony.',
					colab_url: 'https://colab.research.google.com/#create=true',
					xp_reward: 300,
					checklist: [
						'Roman Urdu sarcasm dataset format karna (JSONL ShareGPT)',
						'Unsloth FastLanguageModel 4-bit quantization load karna',
						'LoRA adapter train karna on Free Colab T4 without out-of-memory',
						'Test suite se sarcasm accuracy benchmark karna'
					]
				}
			},
			{
				id: 'm8',
				phase_id: 'phase-4',
				module_number: 8,
				slug: 'm08-deepseek-grpo-reasoning',
				title: 'Module 8: DeepSeek-R1 GRPO Reinforcement Learning',
				weeks_range: 'Weeks 15-16',
				estimated_hours: 32,
				real_world_deliverable: 'Self-Verifying Chain-of-Thought Math Solver trained via GRPO',
				badge_slug: 'grpo-champion',
				order_index: 8,
				diagram_script: `@preset midnight
@animate flow
flow LR: DeepSeek GRPO Pipeline
  prompt[Math Prompt] -> policy[Policy LLM] $brain
  policy -> rollouts[Generate G=4 Candidate Trajectories] ~purple
  rollouts -> reward[Reward Rule: Format + Correctness] ~teal
  reward -> grpo[Group Relative Advantage Normalization] $cpu
  grpo -> update[Policy Gradient Update (No Critic)]* ~ok`,
				diagram_preset: 'midnight',
				diagram_animation: 'flow',
				practice_project: {
					title: 'Salary Negotiation Agent',
					humorous_badge: 'HR Negotiator',
					description_roman_urdu: 'smolagents & Anthropic MCP swarm drafting funny yet razor-sharp counter-offers to tech recruiters.',
					colab_url: 'https://colab.research.google.com/#create=true',
					xp_reward: 275,
					checklist: [
						'Multi-agent roleplay structure build karna',
						'Inflation & market compensation lookup tool add karna',
						'Professional counter-offer email generator implement karna',
						'Structured JSON evaluation run karna'
					]
				}
			}
		]
	},

	// =========================================================================
	// PHASE 5: Enterprise MLOps & High-Performance Rust Gateways
	// =========================================================================
	{
		id: 'phase-5',
		phase_number: 5,
		slug: 'phase-5-production-mlops',
		title: 'Phase 5: Enterprise MLOps & High-Performance Rust Gateways',
		weeks_range: 'Weeks 17-20',
		level: 'Mastery / Production',
		description: 'Rust Axum 0.8 streaming microservices, vLLM Continuous Batching, OpenTelemetry tracing, LLM evaluation pipelines, aur Capstone deployment.',
		order_index: 5,
		modules: [
			{
				id: 'm9',
				phase_id: 'phase-5',
				module_number: 9,
				slug: 'm09-rust-axum-ai-gateway',
				title: 'Module 9: Rust Axum 0.8 High-Performance AI Gateway',
				weeks_range: 'Weeks 17-18',
				estimated_hours: 30,
				real_world_deliverable: 'Sub-millisecond Rust Axum SSE Streaming Gateway',
				badge_slug: 'rust-ninja',
				order_index: 9,
				diagram_script: `@preset midnight
@animate flow
flow LR: Rust Axum High-Performance Gateway
  client[Web/Mobile Client] -> axum[Rust Axum 0.8 Router] $server
  axum -> rate[Token Bucket Rate Limiter] ~purple
  rate -> engine[vLLM Engine Server] $cpu
  engine -> sse[Zero-Allocation SSE Streamer]* ~ok $terminal`,
				diagram_preset: 'midnight',
				diagram_animation: 'flow',
				practice_project: {
					title: 'Ghalib vs Iqbal Poetry Generator',
					humorous_badge: 'Shayar-e-AI',
					description_roman_urdu: 'Mini-GPT model serving classic Urdu poetry tokens in real-time via high-speed streaming gateway.',
					colab_url: 'https://colab.research.google.com/#create=true',
					xp_reward: 250,
					checklist: [
						'Classical Urdu poetry corpus tokenize karna',
						'Causal attention weights compute karna',
						'Rhyme scheme verification filter add karna',
						'Sub-millisecond token streaming benchmark karna'
					]
				}
			},
			{
				id: 'm10',
				phase_id: 'phase-5',
				module_number: 10,
				slug: 'm10-production-mlops-capstone',
				title: 'Module 10: Production MLOps, Tracing & Enterprise Capstone',
				weeks_range: 'Weeks 19-20',
				estimated_hours: 36,
				real_world_deliverable: 'Production Enterprise Capstone deployed to Cloudflare Pages',
				badge_slug: 'ai-ustaad-master',
				order_index: 10,
				diagram_script: `@preset midnight
@animate flow
flow LR: Enterprise Production Capstone
  edge[Cloudflare Edge Pages] -> rust_gw[Rust Axum Gateway] $server
  rust_gw -> db[Supabase PostgreSQL + pgvector] $database
  rust_gw -> vllm[vLLM Multi-GPU / Free Inference] $cpu
  rust_gw -> otel[OpenTelemetry Distributed Tracing]* ~ok $terminal`,
				diagram_preset: 'midnight',
				diagram_animation: 'flow',
				practice_project: {
					title: 'Biryani Delivery Routing Agent & High-Speed Gateway',
					humorous_badge: 'Full-Stack Ustaad',
					description_roman_urdu: 'Autonomous multi-branch food dispatcher with route optimization, MCP tool-calls, and high-throughput Rust gateway.',
					colab_url: 'https://colab.research.google.com/#create=true',
					xp_reward: 350,
					checklist: [
						'Multi-agent dispatcher tool flow orchestrate karna',
						'Rust Axum streaming backend deploy karna',
						'OpenTelemetry latency tracing graph integrate karna',
						'Cloudflare Pages production release complete karna'
					]
				}
			}
		]
	}
];

export const FALLBACK_TRACKS = [
	{
		id: 'track-0',
		track_code: 'Prerequisite Track',
		title: 'Python Zero Se Hero (Beginner to AI Engineer)',
		description: 'Agar aapko Python bilkul nahi aati to yahan se shuru karein! Variables, loops, functions, OOP, JSON, APIs aur NumPy tensor math step-by-step seekhein.',
		topics: ['Python 3.12 Fundamentals', 'OOP & @dataclass', 'JSON & API Requests', 'NumPy Vectors & Tensor Math']
	},
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
    "id": "blog-1",
    "slug": "zero-gpu-survival-guide-2026",
    "title": "Zero-GPU Survival Guide 2026: Google Colab, Kaggle 30h Dual-T4 & Google One Pro 1000 Compute Units Mastery",
    "category": "Cloud & Compute",
    "reading_time_minutes": 12,
    "summary_roman_urdu": "Bina kisi local GPU ke production-grade models fine-tune karein aur Google One Pro compute units ko auto-disconnect script se 100% bachaayein.",
    "content_roman_urdu": "Agar aapke pas RTX 4090 ya Mac M3 Max nahi hai, to pareshan hone ki bilkul zaroorat nahi! 2026 mein modern AI engineering hardware-poor engineers ke liye pehle se kahin zyada accessible hai.\n\n### 1. The Reality of Hardware Hierarchy\n- **Google Colab Free T4 (15GB GDDR6)**: Fast prototyping, inference, and QLoRA on 7B/8B models.\n- **Kaggle Dual-T4 (30GB Combined VRAM)**: 30 hours per week free! PyTorch DDP aur Accelerate ke zariye 14B models comfortably fine-tune ho sakte hain.\n- **Google One Pro (100-1000 Compute Units)**: Agar aapke pas Google One 2TB AI Premium plan hai to aapko monthly 100 se 1000 compute units milte hain. Is se aap Nvidia A100 (40GB/80GB) ya L4 GPUs run kar sakte hain.\n\n### 2. The Dreaded 'Forgot to Disconnect' Disaster\nA100 GPU 2.5 compute units per hour consume karta hai. Agar raat ko model train karne laga kar so gaye aur notebook chal rahi to subah tak 60 units zaya! Iska hal `runtime.unassign()` hai.\n\n### 3. Step-by-Step Survival Recipe\nHamesha apne Python script ko `try...finally` block mein wrap karein taake job pass ho ya fail, runtime foran shutdown ho jaye!",
    "code_snippet": "# Google Colab Auto-Disconnect & Saver Script\nimport time\nimport torch\n\ntry:\n    print(f\"CUDA Device: {torch.cuda.get_device_name(0)}\")\n    print(\"Training Unsloth 4-bit LoRA adapter...\")\n    # Your training loop here\n    time.sleep(2)\n    print(\"Training successfully finished & weights pushed to HuggingFace Hub!\")\nexcept Exception as e:\n    print(f\"Error during training: {e}\")\nfinally:\n    # Google One Pro / Colab Pro 1000 Compute Units Saver:\n    try:\n        from google.colab import runtime\n        print(\"Disconnecting runtime to save your precious compute units!\")\n        runtime.unassign()\n    except ImportError:\n        print(\"Not running in Google Colab environment.\")\n",
    "compute_recipe": "Google Colab Free T4 (15GB VRAM) ya Kaggle Dual-T4 (30h/week). Cost: $0.00. Unassign script prevents compute burn.",
    "diagram_script": "@preset midnight\n@animate flow\nflow LR: Zero-GPU Cloud Compute Strategy 2026\ndev[Local Laptop // 0-VRAM] ~purple -> choose{Workload Type?}*\nchoose ->|Rapid Prototyping| colab[Google Colab Free T4 // 15GB VRAM] ~info\nchoose ->|Heavy Fine-Tuning| kaggle[Kaggle Dual T4 // 30GB VRAM, 30h/wk] ~teal\nchoose ->|Long Jobs & A100| gpro[Google One Pro // 1000 Compute Units]* ~ok\nchoose ->|High Speed Inference| freeapi[Groq & Gemini Flash Free Tier // 300+ tps] ~purple\ncolab -> saver[Auto-Disconnect Saver // runtime.unassign()]* $bolt ~ok\ngpro -> saver",
    "order_index": 1
  },
  {
    "id": "blog-2",
    "slug": "why-85-percent-fail-ai",
    "title": "Why 85% Fail AI Courses (And How Top-Down + First-Principles Makes You Unstoppable)",
    "category": "Learning Strategy",
    "reading_time_minutes": 8,
    "summary_roman_urdu": "85% log AI seekhte waqt calculus ke jhanjhat mein phas kar drop out kar jate hain; top-down methodology pehle din working system deploy karwati hai.",
    "content_roman_urdu": "Aksar university courses aur online tutorials students ko pehle 6 mahine calculus, matrix proofs, aur dry probability padhate hain. Nateeja? Student 4 hafton baad demotivate ho kar chor deta hai kyunki usne koi working cheez nahi banayi hoti.\n\n### 1. Top-Down Learning (The fast.ai & Karpathy Way)\n- **Day 1**: Working LLM pipeline, semantic search, ya computer vision model run karein.\n- **Week 2**: Uske components ko inspect karein \u2014 embedding kya hai? Tokenizer kahan fail hota hai?\n- **Week 3-4**: First-principles depth mein jayein \u2014 self-attention ka QK^T matrix multiplication khud NumPy mein likhein.\n\n### 2. Active Recall & The 70:20:10 Rule\n70% waqt code likhne aur real-world projects banane mein, 20% code review aur debugging mein, aur sirf 10% passive video lecture dekhne mein lagayein.",
    "code_snippet": "# Top-Down Example: Day 1 Working Inference Pipeline\nfrom transformers import pipeline\n\nclassifier = pipeline(\"sentiment-analysis\", model=\"distilbert-base-uncased-finetuned-sst-2-english\")\nresult = classifier(\"Shipping working AI code on Day 1 is 10x better than passive theory!\")\nprint(\"Classification:\", result)\n",
    "compute_recipe": "Local CPU / Google Colab Free Tier. Cost: $0.00. Zero GPU required for inference.",
    "diagram_script": "@preset midnight\n@animate pulse\nflow LR: Top-Down vs Bottom-Up AI Mastery\ntrap[Bottom-Up Trap // 6 Months Calculus Paralysis] ~muted -> fail[85% Drop Out // Zero Shipped Projects]* ~danger\nsol[Top-Down Mastery // Ship Working System Day 1] ~purple -> peel[Peel Layers First-Principles // Math as Needed]* ~teal\npeel -> build[Build PyTorch From Scratch] ~info\nbuild -> prod[15% Top AI Engineers // Shipped Portfolio] ~ok",
    "order_index": 2
  },
  {
    "id": "blog-3",
    "slug": "tensors-memory-strides",
    "title": "Tensors & Memory Strides Under the Hood: Zero-Copy Layouts & SIMD",
    "category": "Low-Level AI",
    "reading_time_minutes": 10,
    "summary_roman_urdu": "Tensor asal mein RAM ka aik flat 1D buffer hota hai; strides aur storage offsets samajh kar zero-copy high performance code likhein.",
    "content_roman_urdu": "PyTorch ya NumPy mein jab aap `tensor.transpose(0, 1)` karte hain to kya data memory mein move hota hai? Bilkul nahi! Yeh zero-copy operation hai jo sirf metadata strides ko update karta hai.\n\n### 1. Strides Ka Concept\nStrides yeh batate hain ke agle row ya column par jane ke liye memory mein kitne elements aage koodna (stride) hai. Aik (3, 4) float32 tensor ka default row-major stride (4, 1) hota hai.\n\n### 2. The `.contiguous()` Trap\nJab tensor non-contiguous ho jata hai (jaise transpose ke baad), aur aap `.view()` call karte hain, to PyTorch error deta hai! Aapko `.contiguous()` call karna padta hai jo naya buffer allocate karta hai. Is overhead se bachna high-scale production systems ke liye zaroori hai.",
    "code_snippet": "import torch\n\n# 2D Tensor shape (3, 4)\nx = torch.arange(12, dtype=torch.float32).reshape(3, 4)\nprint(\"Original Shape:\", x.shape, \"Strides:\", x.stride())\nprint(\"Is Contiguous:\", x.is_contiguous())\n\n# Transpose is ZERO-COPY!\nt = x.t()\nprint(\"Transposed Shape:\", t.shape, \"Strides:\", t.stride())\nprint(\"Is Contiguous:\", t.is_contiguous())\n",
    "compute_recipe": "Pure Python / NumPy / PyTorch CPU. Zero VRAM. Execution time: <10ms.",
    "diagram_script": "@preset midnight\n@animate wave\narch LR: Tensor Memory Layout & Strides Under the Hood\nlogical[2D Matrix 3x4 // Shape & Dtype] ~purple -> strides[Strides 4,1 // Byte Steps]* ~info\nstrides -> ram[(1D Flat Contiguous Buffer in RAM/VRAM)] $db ~teal\nram -> op{Transpose / Reshape}*\nop ->|Zero-Copy View| view[New Metadata Strides 1,4 // 0-Copy] ~ok\nop ->|Non-Contiguous .contiguous()| clone[Deep Memory Copy // Allocation Penalty] ~danger",
    "order_index": 3
  },
  {
    "id": "blog-4",
    "slug": "the-illustrated-transformer",
    "title": "The Illustrated Transformer & Scaled Dot-Product Attention (sqrt{d_k} Math Intuitively)",
    "category": "Deep Learning",
    "reading_time_minutes": 15,
    "summary_roman_urdu": "Scaled Dot-Product Attention ka QK^T matrix math, sqrt{d_k} scaling ki mathematical waja, aur causal masking ki visual explanation.",
    "content_roman_urdu": "Transformer architecture 2017 mein introduce hua aur aaj tak sabhi SOTA LLMs (GPT-4o, Claude 3.5, Llama 3, DeepSeek) ki bunyad hai. Lekin attention mechanism asal mein karta kya hai?\n\n### 1. Query, Key, aur Value Ka Mental Model\n- **Query (Q)**: 'Main kya dhoond raha hoon?'\n- **Key (K)**: 'Mere pas kya information moojood hai?'\n- **Value (V)**: 'Meri actual content details kya hain?'\nJab Q aur K ka dot product lete hain to correlation score nikalta hai.\n\n### 2. sqrt{d_k} Se Divide Kyun Karte Hain?\nAgar dimension d_k bara ho (maslan 64 ya 128), to dot products ka variance bara ho jata hai. Softmax function bare numbers par saturate ho jata hai aur gradients zero ho jate hain (vanishing gradients). sqrt{d_k} se divide karne se variance wapis 1 par rehti hai!",
    "code_snippet": "import torch\nimport torch.nn.functional as F\nimport math\n\ndef scaled_dot_product_attention(Q, K, V, mask=None):\n    d_k = Q.size(-1)\n    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)\n    if mask is not None:\n        scores = scores.masked_fill(mask == 0, -1e9)\n    attention_weights = F.softmax(scores, dim=-1)\n    return torch.matmul(attention_weights, V), attention_weights\n\nq = torch.randn(1, 1, 4, 64)\nk = torch.randn(1, 1, 4, 64)\nv = torch.randn(1, 1, 4, 64)\nout, weights = scaled_dot_product_attention(q, k, v)\nprint(\"Output shape:\", out.shape, \"Attention sum:\", weights.sum(dim=-1))\n",
    "compute_recipe": "Runs locally on CPU or Colab Free T4 in 5ms. Memory: <50MB RAM.",
    "diagram_script": "@preset midnight\n@animate wave\narch LR: Scaled Dot-Product Self-Attention\ntok[Token Embeddings X] ~purple -> qkv[Linear Projections // Wq, Wk, Wv]\nqkv -> q[Queries Q] ~info\nqkv -> k[Keys K] ~teal\nqkv -> v[Values V] ~teal\nq -> matmul((Q x K^T))\nk -> matmul\nmatmul -> scale[Scale 1 / sqrt d_k // Prevent Vanishing Gradients]*\nscale -> mask[Causal Masking // Upper Triangle -inf]\nmask -> sm[Softmax // Attention Heatmap Probabilities]* ~purple\nsm -> out((Softmax x V))\nv -> out\nout -> proj[Linear Output Projection Wo] ~ok",
    "order_index": 4
  },
  {
    "id": "blog-5",
    "slug": "kv-cache-paged-attention",
    "title": "KV-Cache & PagedAttention (vLLM): Breaking the GPU Memory Wall",
    "category": "Inference & Systems",
    "reading_time_minutes": 11,
    "summary_roman_urdu": "LLM generation ke waqt KV Cache VRAM kyun bhar deta hai aur vLLM ka PagedAttention virtual memory paging ke zariye 80% waste kaise khatam karta hai.",
    "content_roman_urdu": "Autoregressive LLM inference mein har naya token generate karne ke liye purane tokens ke Key aur Value tensors dobara compute nahi kiye jate \u2014 unhe VRAM mein cache kiya jata hai jise **KV-Cache** kehte hain.\n\n### 1. Naive Allocation Ka Nuqsan\nTraditional systems har request ke liye max sequence length (maslan 4,096 tokens) ka contiguous VRAM block pehle se book kar lete the. Agar user ne sirf 100 tokens generate kiye to baqi 97% memory zaya (internal fragmentation)! Nateeja: GPU sirf 2 ya 3 concurrent requests handle kar sakti thi.\n\n### 2. PagedAttention Ka Inqilab (vLLM)\nOperating Systems ke Virtual Memory Paging concept ko adopt karte hue, PagedAttention KV-cache ko chote non-contiguous blocks (e.g. 16 tokens per block) mein divide karta hai. Is se GPU memory utilization 20% se seedha 96% par chali jati hai aur throughput 4x-10x barh jati hai!",
    "code_snippet": "def kv_cache_size_gb(num_layers, hidden_size, seq_len, batch_size, bytes_per_elem=2):\n    bytes_total = 2 * num_layers * hidden_size * bytes_per_elem * seq_len * batch_size\n    return bytes_total / (1024 ** 3)\n\nvram_for_100_users_4k = kv_cache_size_gb(32, 4096, 4096, 100)\nprint(f\"KV Cache for 100 users @ 4k tokens: {vram_for_100_users_4k:.2f} GB VRAM!\")\n",
    "compute_recipe": "Deploy on RunPod / Colab Pro L4 / local vLLM. Zero-VRAM estimation script runs on CPU.",
    "diagram_script": "@preset midnight\n@animate flow\nflow LR: KV-Cache & PagedAttention Memory Architecture\nprompt[Prompt Tokens] ~purple -> prefill[Prefill Phase // Parallel Compute]* $cpu ~info\nprefill -> init_kv[Initial K & V Tensors] ~teal\ngen[Autoregressive Decode Step] ->|New Single Token| append[Append New K, V Vector]\nappend -> vmem{Standard Allocation?}*\nvmem ->|Naive Contiguous Alloc| frag[60-80% VRAM Waste & Memory Fragmentation] ~danger\nvmem ->|PagedAttention vLLM| table[Virtual Page Table // Non-Contiguous Blocks]* ~ok\ntable -> vram[(VRAM Physical Blocks // 96% Memory Utilization)] $db ~ok",
    "order_index": 5
  },
  {
    "id": "blog-6",
    "slug": "vector-search-vs-hybrid-rag",
    "title": "Pure Vector Search vs Hybrid RAG (BM25 + pgvector + RRF + ColPali Vision RAG)",
    "category": "Information Retrieval",
    "reading_time_minutes": 14,
    "summary_roman_urdu": "Kyun sirf vector cosine similarity real enterprise RAG mein fail hoti hai aur BM25 keyword search + pgvector + RRF + ColPali se zero hallucination kaise hasil karein.",
    "content_roman_urdu": "Standard RAG tutorials mein log sirf `text-embedding-3-small` use kar ke vector search karte hain. Lekin jab client pooche: 'Invoice number #PK-9821 ka total bill kitna tha?', to vector search fail ho jata hai kyunki invoice number ka koi semantic meaning nahi hota!\n\n### 1. Hybrid Search (Dense + Sparse)\n- **Sparse (BM25 / Full-Text)**: Exact part numbers, invoice IDs, acronyms, aur names pakadta hai.\n- **Dense (pgvector HNSW)**: Conceptual similarity aur fuzzy semantics pakadta hai.\n\n### 2. Reciprocal Rank Fusion (RRF)\nDono lists ko bina score normalization ke merge karne ke liye RRF formula use hota hai:\n`RRF_Score(d) = sum(1 / (k + rank(d)))` jahan `k = 60`.\n\n### 3. ColPali (Vision-Language RAG 2026)\nComplex multi-column PDFs, tables, aur Pakistani Urdu cheques ke liye text extract karne ke bajaye pooray page ka screenshot embed kiya jata hai via ColPali late-interaction!",
    "code_snippet": "def rrf_merge(bm25_ranks, vector_ranks, k=60):\n    scores = {}\n    for rank, doc_id in enumerate(bm25_ranks):\n        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)\n    for rank, doc_id in enumerate(vector_ranks):\n        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)\n    return sorted(scores.items(), key=lambda item: item[1], reverse=True)\n\nbm25 = [\"doc_invoice_9821\", \"doc_receipt_12\", \"doc_legal_contract\"]\nvector = [\"doc_legal_contract\", \"doc_invoice_9821\", \"doc_tax_return\"]\nranked = rrf_merge(bm25, vector)\nprint(\"Top Fused Document:\", ranked[0])\n",
    "compute_recipe": "PostgreSQL with pgvector + Supabase free tier. Embeddings via Groq / Gemini Flash API.",
    "diagram_script": "@preset midnight\n@animate flow\narch LR: Production Hybrid RAG & ColPali Pipeline\nquery[User Question] $user ~purple -> dense[Dense Embedder // text-embedding-3] ~info\nquery -> sparse[Sparse Lexical // BM25 Tokenizer] ~teal\nquery -> vision[Multi-Vector ColPali // Page Image Embeds]* ~purple\ndense -> vdb[(pgvector HNSW Index)] $db ~info\nsparse -> sdb[(Inverted Index / BM25)] $db ~teal\nvision -> cvdb[(ColPali Late Interaction Index)] $db ~purple\nvdb -> rrf[Reciprocal Rank Fusion RRF]* $bolt\nsdb -> rrf\ncvdb -> rrf\nrrf -> rerank[Cross-Encoder Re-Ranker // Cohere v3] ~ok\nrerank -> topk[Top-K High-Precision Context] ~ok",
    "order_index": 6
  },
  {
    "id": "blog-7",
    "slug": "mcp-and-smolagents",
    "title": "Anthropic MCP & Hugging Face smolagents: Why Code Agents Beat Brittle Chains",
    "category": "Agentic AI",
    "reading_time_minutes": 13,
    "summary_roman_urdu": "JSON-based tool calling aur LangChain chains kyun toot-ti hain; Anthropic Model Context Protocol aur executable Python CodeAgents ka jadeed tareeqa.",
    "content_roman_urdu": "2024 tak log brittle JSON chains aur LangChain use kar rahe the. Thori si schema change hoti thi aur agent crash ho jata tha! 2026 ka gold standard **Code Agents** aur **Model Context Protocol (MCP)** hai.\n\n### 1. CodeAgent Advantage (Hugging Face smolagents)\nAgent se JSON nikalne ke bajaye us se seedha Python code likhwayein. Code sandbox mein run hota hai, loop chala sakta hai, conditions check kar sakta hai, aur 3x kam LLM calls mein kaam khatam karta hai.\n\n### 2. Anthropic Model Context Protocol (MCP)\nMCP aik open standard protocol hai jo LLMs ko enterprise data sources (Postgres, GitHub, Slack, local filesystem) se connect karta hai securely via standardized JSON-RPC.",
    "code_snippet": "from smolagents import CodeAgent, HfApiModel, tool\n\n@tool\ndef get_crypto_price_pkr(coin: str) -> str:\n    \"\"\"Fetches real-time crypto price in PKR.\n    Args:\n        coin: Symbol like BTC or ETH\n    \"\"\"\n    return f\"{coin} price is currently PKR 27,850,000\"\n\nagent = CodeAgent(tools=[get_crypto_price_pkr], model=HfApiModel())\nprint(\"CodeAgent initialized with MCP tool support.\")\n",
    "compute_recipe": "Groq Free API (Llama 3.3 70B) ya Cerebras Free API. Local CPU sandbox. $0.00 Cost.",
    "diagram_script": "@preset midnight\n@animate pulse\nflow TB: Modern CodeAgent & Model Context Protocol MCP\nuser[User Goal / Intent] $user ~purple -> planner[smolagents CodeAgent Planner]* $ai ~purple\nplanner -> act[Generate Pure Python Executable Code] ~info\nact -> mcp[Anthropic MCP Host Gateway // JSON-RPC]* $gear ~teal\nmcp -> t1[Postgres MCP Server] $db ~teal\nmcp -> t2[GitHub MCP Server] $github ~teal\nmcp -> t3[Filesystem MCP Server] $gear ~teal\nt1 -> obs[Tool Outputs & DataFrames] ~ok\nt2 -> obs\nt3 -> obs\nobs -> interp[Secure Sandboxed Python Interpreter] ~info\ninterp -> self_heal{Exception / Error?}*\nself_heal ->|Traceback detected| planner\nself_heal ->|Success| deliverable((Final Validated Deliverable)) ~ok",
    "order_index": 7
  },
  {
    "id": "blog-8",
    "slug": "unsloth-4bit-qlora",
    "title": "Unsloth 4-Bit QLoRA Math: Fine-Tuning 8B Models on a Free 15GB Colab T4",
    "category": "Model Training",
    "reading_time_minutes": 12,
    "summary_roman_urdu": "Unsloth custom OpenAI Triton kernels ke zariye VRAM 80% kaise bachaata hai aur free Colab T4 par Llama 3 8B model 5x tezi se kaise train hota hai.",
    "content_roman_urdu": "Standard Hugging Face PEFT mein 8B model fine-tune karne ke liye kam az kam 24GB VRAM (RTX 3090/4090) zaroori hoti hai. Lekin Unsloth ne game badal diya!\n\n### 1. Manual Backprop in Triton\nUnsloth ne PyTorch ke autograd ko bypass kar ke manually written OpenAI Triton kernels banaye. Is se Cross-Entropy loss aur RoPE embeddings ka memory footprint 80% kam ho jata hai.\n\n### 2. NF4 Quantization + LoRA Rank r=16\nBase model ke weights 4-bit NormalFloat (NF4) mein freeze rehte hain, jabke sirf choti low-rank matrices A aur B train hoti hain. Free Colab T4 GPU (15GB VRAM) par batch size 4 ke sath training makhan ki tarah chalti hai!",
    "code_snippet": "from unsloth import FastLanguageModel\n\nmax_seq_length = 2048\nmodel, tokenizer = FastLanguageModel.from_pretrained(\n    model_name=\"unsloth/llama-3-8b-bnb-4bit\",\n    max_seq_length=max_seq_length,\n    load_in_4bit=True,\n)\n\nmodel = FastLanguageModel.get_peft_model(\n    model,\n    r=16,\n    target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"],\n    lora_alpha=16,\n    lora_dropout=0,\n    bias=\"none\",\n)\nprint(\"Model ready for ultra-fast training on Free Google Colab T4!\")\n",
    "compute_recipe": "Google Colab Free Tier (T4 GPU 15GB). Training time: ~20 mins on 1k samples. Cost: $0.00.",
    "diagram_script": "@preset midnight\n@animate glow\narch LR: Unsloth 4-bit QLoRA Parameter-Efficient Fine-Tuning\nact[Input Tensor X // 16-bit Float] ~purple -> base[Base LLM Weights W0 // 4-bit NF4 Quantized]* ~muted\nact -> lora_a[LoRA Matrix A // 16-bit, rank r=16] ~info\nlora_a -> lora_b[LoRA Matrix B // 16-bit, rank r=16]* ~teal\nlora_b -> scale[alpha / r Scaling] ~teal\nbase -> dequant[De-Quantize to 16-bit on the fly] ~info\ndequant -> sum((+))\nscale -> sum\nsum -> out[Forward Activation Y] ~ok\nout -> loss[Cross-Entropy Loss] -> unsloth[Unsloth Fast Triton Kernels // 5x Speed, 80% Less VRAM]* ~ok",
    "order_index": 8
  },
  {
    "id": "blog-9",
    "slug": "deepseek-r1-and-grpo",
    "title": "DeepSeek-R1 & GRPO: How Reasoning Models Learn to <think> Without a Critic Model",
    "category": "Reinforcement Learning",
    "reading_time_minutes": 16,
    "summary_roman_urdu": "DeepSeek-R1 ne PPO ke baray Critic model ko khatam kar ke Group Relative Policy Optimization (GRPO) ke zariye reasoning models kaise banaye.",
    "content_roman_urdu": "DeepSeek-R1 ne OpenAI o1 ko challenge kar ke puri dunya ko hairaan kar diya. Unka sab se bara breakthrough kya tha? **GRPO (Group Relative Policy Optimization)**.\n\n### 1. Traditional PPO Ka Masla\nTraditional RLHF (PPO) mein policy model ke barabar ka aik doosra 'Critic / Value Model' VRAM mein rakhna padta tha. 70B model ke sath 70B critic model run karne ke liye 8x H100 GPUs chahiye the!\n\n### 2. GRPO Ka Simple Magic\nGRPO mein koi critic model nahi hota! Model aik prompt ke liye 4 se 8 mukhtalif jawab generate karta hai. Phir deterministic rules (maslan: kya compiler ne code pass kiya? kya math answer theek hai?) se har answer ko reward milta hai. Phir is group ka mean aur standard deviation nikaal kar advantage calculate hota hai!\n\n### 3. Emergence of <think> Tokens\nModel ko kisi ne explicitly nahi sikhaya ke <think> likho. Jab correct answer par reward mila to model ne khud ba khud lambi chain-of-thought aur self-correction strategy evolve kar li!",
    "code_snippet": "import numpy as np\n\ndef compute_grpo_advantages(rewards: list[float], epsilon=1e-6) -> np.ndarray:\n    r = np.array(rewards)\n    mean_r = np.mean(r)\n    std_r = np.std(r) + epsilon\n    advantages = (r - mean_r) / std_r\n    return advantages\n\nrewards = [1.0, 0.0, -0.5, 1.0]\nadv = compute_grpo_advantages(rewards)\nprint(\"GRPO Group Advantages:\", adv)\n",
    "compute_recipe": "Kaggle Dual-T4 (30h/week) or Colab Pro with Unsloth GRPO trainer. $0.00 cost.",
    "diagram_script": "@preset midnight\n@animate wave\nflow LR: DeepSeek-R1 Group Relative Policy Optimization GRPO\nprompt[Math / Coding Prompt q] ~purple -> policy[Old Policy LLM pi_theta_old]* $ai ~purple\npolicy -> g1[Completion o1 // with think trace] ~info\npolicy -> g2[Completion o2 // with think trace] ~info\npolicy -> g3[Completion o3 // with think trace] ~info\npolicy -> g4[Completion o4 // with think trace] ~info\ng1 -> reward[Deterministic Rule Reward // Accuracy + Format Check]* $bolt ~teal\ng2 -> reward\ng3 -> reward\ng4 -> reward\nreward -> norm[Group Normalization // Advantage A = r - mean / std]* ~ok\nnorm -> ppo[GRPO Objective Update // No Critic Value Model Needed!]* ~ok\nppo -> trained[Reasoning Master Model // DeepSeek-R1 style] ~purple",
    "order_index": 9
  },
  {
    "id": "blog-10",
    "slug": "learner-to-3k-ai-engineer",
    "title": "From Learner to $3k+ AI Engineer: Packaging AI Microservices with Supabase & Rust",
    "category": "Career & Architecture",
    "reading_time_minutes": 9,
    "summary_roman_urdu": "Pakistan aur remote market mein $3k-$5k/month kamane wale AI Engineer kaise banain; portfolio projects, Rust microservices, aur Supabase architecture.",
    "content_roman_urdu": "Sirf Jupyter Notebook run karna aapko AI engineer nahi banata. Clients notebook nahi khareedte \u2014 clients **reliable, fast, production-ready APIs** chahte hain jo sub-50ms latency mein unke business problems solve karein.\n\n### 1. The $3k/mo Tech Stack\n- **Backend**: Rust Axum (10x faster than FastAPI, zero memory leaks, sub-10ms overhead).\n- **Database**: Supabase PostgreSQL with `pgvector`, Row Level Security (RLS), aur Supabase Auth.\n- **Inference Router**: Groq / Gemini Flash for 90% cheap queries + DeepSeek-R1 / Claude for hard reasoning.\n- **Frontend**: Svelte 5 / SvelteKit (clean, light, Claude-style UI).\n\n### 2. Upwork & Direct Client Strategy\nKabhi 'I will do AI' ka generic proposal na bhejein. Har proposal ke sath aik working loom video ya interactive URL bhejein (jaise aapka Capstone project). Client ko dikhayein ke aapne unka problem pehle hi solve kar rakha hai!",
    "code_snippet": "use axum::{routing::post, Json, Router};\nuse serde::{Deserialize, Serialize};\n\n#[derive(Deserialize)]\nstruct ClientQuery { prompt: String }\n\n#[derive(Serialize)]\nstruct AiResponse { answer: String, latency_ms: u64 }\n\nasync fn handle_ai(Json(payload): Json<ClientQuery>) -> Json<AiResponse> {\n    Json(AiResponse {\n        answer: format!(\"Production processed: {}\", payload.prompt),\n        latency_ms: 8,\n    })\n}\n",
    "compute_recipe": "Deploy to Fly.io free tier or Railway + Supabase Free PostgreSQL. $0.00 startup cost.",
    "diagram_script": "@preset midnight\n@animate flow\nflow LR: $3,000/mo AI Engineer Production Architecture\nclient[Global Upwork / Enterprise Clients] $user ~purple -> gateway[Rust Axum Gateway // <10ms Auth & Rate Limit]* ~ok\ngateway -> cache[(Redis / Memory Semantic Cache)] $bolt ~teal\ngateway -> supa[(Supabase Auth, pgvector & Realtime DB)] $db ~info\ngateway -> llm_pool{Inference Router}*\nllm_pool ->|Cheap / Fast| groq[Groq Llama 3 // 300 tps] ~teal\nllm_pool ->|Reasoning| deepseek[DeepSeek-R1 / Claude 3.5 Sonnet] ~purple\ngateway -> mon[Telemetry & Billing // OpenTelemetry + Stripe] $chart ~ok\nmon -> profit((High-Margin $3k-10k/mo AI SaaS Service)) ~ok",
    "order_index": 10
  }
];


export const HF_SUBPROJECTS: Record<number, HfSubproject> = {
	0: {
  "module_number": 0,
  "module_slug": "python-zero-se-hero",
  "project_title": "Chai Dhaba Customer Sentiment & Order Billing Engine",
  "project_slug": "chai-dhaba-billing-sentiment",
  "hf_model": "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
  "hf_model_url": "https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english",
  "hf_dataset": "rotten_tomatoes",
  "hf_dataset_url": "https://huggingface.co/datasets/rotten_tomatoes",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_00_chai_dhaba_sentiment.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_00_chai_dhaba_sentiment.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-00-chai-dhaba-billing-sentiment",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-00-chai-dhaba-billing-sentiment",
  "hardware_requirement": "Free Colab CPU / T4 GPU (0.3 GB VRAM)",
  "estimated_runtime_seconds": "< 15s cold load, < 0.2s inference",
  "key_learning_takeaway": "Combines Python dictionaries, OOP data structures, and Hugging Face pre-trained sentiment pipelines to analyze real-world consumer feedback with zero API costs.",
  "starter_code": "# Module 0: Chai Dhaba Fast Sentiment & Bill Analyzer\nfrom transformers import pipeline\nfrom datasets import load_dataset\n\n# 1. Load tiny 260MB model (< 15 seconds on CPU/T4)\nclassifier = pipeline(\"sentiment-analysis\", model=\"distilbert/distilbert-base-uncased-finetuned-sst-2-english\")\n\n# 2. Stream 3 customer reviews from HF datasets\ndataset = load_dataset(\"rotten_tomatoes\", split=\"test\", streaming=True)\nsample_reviews = [item[\"text\"] for item in dataset.take(3)]\n\n# 3. Analyze Dhaba Customer Orders & Feedback\ncustomer_orders = [\n    {\"customer\": \"Aslam\", \"item\": \"Doodh Patti & Paratha\", \"review\": \"The tea was scalding hot, perfectly sweet, and the paratha was delightfully crisp!\"},\n    {\"customer\": \"Bilal\", \"item\": \"Karak Chai\", \"review\": \"Cold tea, way too much sugar, and stale biscuits. Terrible service.\"}\n]\n\nprint(\"--- Dhaba Customer Feedback Analysis ---\")\nfor order in customer_orders:\n    result = classifier(order[\"review\"])[0]\n    print(f\"Customer: {order['customer']} ({order['item']})\")\n    print(f\"Feedback: {order['review']}\")\n    print(f\"Sentiment: {result['label']} (Confidence: {result['score']:.4f})\\n\")\n",
  "runnable_starter_code": "# Module 0: Chai Dhaba Fast Sentiment & Bill Analyzer\nfrom transformers import pipeline\nfrom datasets import load_dataset\n\n# 1. Load tiny 260MB model (< 15 seconds on CPU/T4)\nclassifier = pipeline(\"sentiment-analysis\", model=\"distilbert/distilbert-base-uncased-finetuned-sst-2-english\")\n\n# 2. Stream 3 customer reviews from HF datasets\ndataset = load_dataset(\"rotten_tomatoes\", split=\"test\", streaming=True)\nsample_reviews = [item[\"text\"] for item in dataset.take(3)]\n\n# 3. Analyze Dhaba Customer Orders & Feedback\ncustomer_orders = [\n    {\"customer\": \"Aslam\", \"item\": \"Doodh Patti & Paratha\", \"review\": \"The tea was scalding hot, perfectly sweet, and the paratha was delightfully crisp!\"},\n    {\"customer\": \"Bilal\", \"item\": \"Karak Chai\", \"review\": \"Cold tea, way too much sugar, and stale biscuits. Terrible service.\"}\n]\n\nprint(\"--- Dhaba Customer Feedback Analysis ---\")\nfor order in customer_orders:\n    result = classifier(order[\"review\"])[0]\n    print(f\"Customer: {order['customer']} ({order['item']})\")\n    print(f\"Feedback: {order['review']}\")\n    print(f\"Sentiment: {result['label']} (Confidence: {result['score']:.4f})\\n\")\n",
  "gradio_code": "import gradio as gr\nfrom transformers import pipeline\n\nclf = pipeline(\"sentiment-analysis\", model=\"distilbert/distilbert-base-uncased-finetuned-sst-2-english\")\n\ndef analyze_review(customer_name, review_text):\n    res = clf(review_text)[0]\n    emoji = \"[POSITIVE] Zabardast!\" if res[\"label\"] == \"POSITIVE\" else \"⚠️ Shikayat (Negative)!\"\n    return f\"{emoji} Score: {res['score']:.2%}\"\n\ndemo = gr.Interface(\n    fn=analyze_review,\n    inputs=[gr.Textbox(label=\"Customer Name\", value=\"Hamza\"), gr.Textbox(label=\"Dhaba Feedback\", value=\"Best Doodh Patti in town!\")],\n    outputs=gr.Textbox(label=\"AI Sentiment Verdict\"),\n    title=\"Chai Dhaba Sentiment Munshi\"\n)\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr\nfrom transformers import pipeline\n\nclf = pipeline(\"sentiment-analysis\", model=\"distilbert/distilbert-base-uncased-finetuned-sst-2-english\")\n\ndef analyze_review(customer_name, review_text):\n    res = clf(review_text)[0]\n    emoji = \"[POSITIVE] Zabardast!\" if res[\"label\"] == \"POSITIVE\" else \"⚠️ Shikayat (Negative)!\"\n    return f\"{emoji} Score: {res['score']:.2%}\"\n\ndemo = gr.Interface(\n    fn=analyze_review,\n    inputs=[gr.Textbox(label=\"Customer Name\", value=\"Hamza\"), gr.Textbox(label=\"Dhaba Feedback\", value=\"Best Doodh Patti in town!\")],\n    outputs=gr.Textbox(label=\"AI Sentiment Verdict\"),\n    title=\"Chai Dhaba Sentiment Munshi\"\n)\ndemo.launch()\n"
},
	1: {
  "module_number": 1,
  "module_slug": "python-for-ai-and-fast-math",
  "project_title": "Biryani vs Pulao Cosine Semantic Vectorizer",
  "project_slug": "biryani-pulao-semantic-vectorizer",
  "hf_model": "sentence-transformers/all-MiniLM-L6-v2",
  "hf_model_url": "https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2",
  "hf_dataset": "rotten_tomatoes",
  "hf_dataset_url": "https://huggingface.co/datasets/rotten_tomatoes",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_01_biryani_vector_math.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_01_biryani_vector_math.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-01-biryani-pulao-vectorizer",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-01-biryani-pulao-vectorizer",
  "hardware_requirement": "Free Colab CPU / T4 GPU (0.1 GB VRAM)",
  "estimated_runtime_seconds": "< 5s load, < 0.1s vector dot-product",
  "key_learning_takeaway": "First-principles linear algebra in action: dense sentence embeddings, vector dot-products, Euclidean norms, and SIMD cosine similarity ranking with zero loop overhead.",
  "starter_code": "# Module 1: Vector Spaces & Cosine Similarity with NumPy\nimport numpy as np\nfrom sentence_transformers import SentenceTransformer\n\n# 1. Load lightweight 80MB embedding model (384-dimensional vector space)\nembedder = SentenceTransformer(\"sentence-transformers/all-MiniLM-L6-v2\")\n\n# 2. Target query and food review corpus\nquery = \"Spicy Karachi beef biryani with lots of aloo and aroma\"\nreviews = [\n    \"Hot spicy beef biryani with succulent potatoes and golden rice.\",\n    \"Mild chicken yakhni pulao with cardamom and delicate spices.\",\n    \"Sweet carrot halwa with desi ghee, almonds, and pistachios.\",\n    \"Crisp fried fish with tangy lemon garlic tartar sauce.\"\n]\n\n# 3. Vectorize text into 2D NumPy float32 matrix\nquery_vec = embedder.encode(query)\ncorpus_vecs = embedder.encode(reviews)\n\n# 4. Pure NumPy SIMD Cosine Similarity: (A . B) / (||A|| * ||B||)\ndot_products = np.dot(corpus_vecs, query_vec)\nnorms = np.linalg.norm(corpus_vecs, axis=1) * np.linalg.norm(query_vec)\nsimilarities = dot_products / norms\n\nprint(f\"Target Query: '{query}'\\n\" + \"=\"*50)\nfor idx in np.argsort(-similarities):\n    print(f\"Score: {similarities[idx]:.4f} | Review: {reviews[idx]}\")\n",
  "runnable_starter_code": "# Module 1: Vector Spaces & Cosine Similarity with NumPy\nimport numpy as np\nfrom sentence_transformers import SentenceTransformer\n\n# 1. Load lightweight 80MB embedding model (384-dimensional vector space)\nembedder = SentenceTransformer(\"sentence-transformers/all-MiniLM-L6-v2\")\n\n# 2. Target query and food review corpus\nquery = \"Spicy Karachi beef biryani with lots of aloo and aroma\"\nreviews = [\n    \"Hot spicy beef biryani with succulent potatoes and golden rice.\",\n    \"Mild chicken yakhni pulao with cardamom and delicate spices.\",\n    \"Sweet carrot halwa with desi ghee, almonds, and pistachios.\",\n    \"Crisp fried fish with tangy lemon garlic tartar sauce.\"\n]\n\n# 3. Vectorize text into 2D NumPy float32 matrix\nquery_vec = embedder.encode(query)\ncorpus_vecs = embedder.encode(reviews)\n\n# 4. Pure NumPy SIMD Cosine Similarity: (A . B) / (||A|| * ||B||)\ndot_products = np.dot(corpus_vecs, query_vec)\nnorms = np.linalg.norm(corpus_vecs, axis=1) * np.linalg.norm(query_vec)\nsimilarities = dot_products / norms\n\nprint(f\"Target Query: '{query}'\\n\" + \"=\"*50)\nfor idx in np.argsort(-similarities):\n    print(f\"Score: {similarities[idx]:.4f} | Review: {reviews[idx]}\")\n",
  "gradio_code": "import gradio as gr\nimport numpy as np\nfrom sentence_transformers import SentenceTransformer\n\nmodel = SentenceTransformer(\"sentence-transformers/all-MiniLM-L6-v2\")\n\ndef rank_similarity(query_text, candidate_items):\n    cands = [c.strip() for c in candidate_items.split(\"\\n\") if c.strip()]\n    if not cands: return \"Please enter candidates!\"\n    q_vec = model.encode(query_text)\n    c_vecs = model.encode(cands)\n    sims = np.dot(c_vecs, q_vec) / (np.linalg.norm(c_vecs, axis=1) * np.linalg.norm(q_vec))\n    ranked = sorted(zip(cands, sims), key=lambda x: -x[1])\n    return \"\\n\".join([f\"Rank {i+1} [{s:.2%}]: {text}\" for i, (text, s) in enumerate(ranked)])\n\ndemo = gr.Interface(\n    fn=rank_similarity,\n    inputs=[gr.Textbox(label=\"Query Sentence\", value=\"Tez Masalaydaar Biryani\"), gr.Textbox(label=\"Candidates (one per line)\", lines=4, value=\"Spicy beef biryani\\nMild white pulao\\nCold ice cream\")],\n    outputs=gr.Textbox(label=\"Cosine Similarity Rankings\"),\n    title=\"Vector Math & Cosine Similarity Inspector\"\n)\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr\nimport numpy as np\nfrom sentence_transformers import SentenceTransformer\n\nmodel = SentenceTransformer(\"sentence-transformers/all-MiniLM-L6-v2\")\n\ndef rank_similarity(query_text, candidate_items):\n    cands = [c.strip() for c in candidate_items.split(\"\\n\") if c.strip()]\n    if not cands: return \"Please enter candidates!\"\n    q_vec = model.encode(query_text)\n    c_vecs = model.encode(cands)\n    sims = np.dot(c_vecs, q_vec) / (np.linalg.norm(c_vecs, axis=1) * np.linalg.norm(q_vec))\n    ranked = sorted(zip(cands, sims), key=lambda x: -x[1])\n    return \"\\n\".join([f\"Rank {i+1} [{s:.2%}]: {text}\" for i, (text, s) in enumerate(ranked)])\n\ndemo = gr.Interface(\n    fn=rank_similarity,\n    inputs=[gr.Textbox(label=\"Query Sentence\", value=\"Tez Masalaydaar Biryani\"), gr.Textbox(label=\"Candidates (one per line)\", lines=4, value=\"Spicy beef biryani\\nMild white pulao\\nCold ice cream\")],\n    outputs=gr.Textbox(label=\"Cosine Similarity Rankings\"),\n    title=\"Vector Math & Cosine Similarity Inspector\"\n)\ndemo.launch()\n"
},
	2: {
  "module_number": 2,
  "module_slug": "prompt-engineering-and-llm-mental-models",
  "project_title": "SmolLM2 Rishta Matchmaker & Chain-of-Thought Evaluator",
  "project_slug": "smollm2-rishta-cot-evaluator",
  "hf_model": "HuggingFaceTB/SmolLM2-360M-Instruct",
  "hf_model_url": "https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct",
  "hf_dataset": "fka/awesome-chatgpt-prompts",
  "hf_dataset_url": "https://huggingface.co/datasets/fka/awesome-chatgpt-prompts",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_02_smollm2_prompt_eval.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_02_smollm2_prompt_eval.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-02-smollm2-cot-matchmaker",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-02-smollm2-cot-matchmaker",
  "hardware_requirement": "Free Colab CPU / T4 GPU (0.8 GB VRAM)",
  "estimated_runtime_seconds": "< 20s load, < 2s token generation",
  "key_learning_takeaway": "Autoregressive next-token prediction dynamics, temperature sampling effects on creativity, system prompt steering, and Chain-of-Thought (CoT) reasoning.",
  "starter_code": "# Module 2: Chain-of-Thought (CoT) Prompting with SmolLM2-360M\nimport torch\nfrom transformers import pipeline\n\n# 1. Load HF's modern open-weight SmolLM2-360M-Instruct\npipe = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\", torch_dtype=torch.float32)\n\n# 2. Format chat with System Persona and Step-by-Step Chain-of-Thought\nmessages = [\n    {\"role\": \"system\", \"content\": \"You are a witty, analytical Pakistani Rishta Matchmaker auntie. Think step-by-step and provide a compatibility score (0-100%) in clean JSON.\"},\n    {\"role\": \"user\", \"content\": \"Candidate 1: Software Engineer, introverted, loves biryani and gaming at 2 AM.\\nCandidate 2: Clinical Doctor, extroverted, loves hiking, hates fast food.\\nAre they compatible?\"}\n]\n\n# 3. Generate response with controlled temperature\nprompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)\noutputs = pipe(prompt, max_new_tokens=220, temperature=0.6, do_sample=True, top_p=0.9)\ngenerated_text = outputs[0][\"generated_text\"][len(prompt):]\n\nprint(\"=== SmolLM2 Rishta Matchmaker CoT Output ===\")\nprint(generated_text.strip())\n",
  "runnable_starter_code": "# Module 2: Chain-of-Thought (CoT) Prompting with SmolLM2-360M\nimport torch\nfrom transformers import pipeline\n\n# 1. Load HF's modern open-weight SmolLM2-360M-Instruct\npipe = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\", torch_dtype=torch.float32)\n\n# 2. Format chat with System Persona and Step-by-Step Chain-of-Thought\nmessages = [\n    {\"role\": \"system\", \"content\": \"You are a witty, analytical Pakistani Rishta Matchmaker auntie. Think step-by-step and provide a compatibility score (0-100%) in clean JSON.\"},\n    {\"role\": \"user\", \"content\": \"Candidate 1: Software Engineer, introverted, loves biryani and gaming at 2 AM.\\nCandidate 2: Clinical Doctor, extroverted, loves hiking, hates fast food.\\nAre they compatible?\"}\n]\n\n# 3. Generate response with controlled temperature\nprompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)\noutputs = pipe(prompt, max_new_tokens=220, temperature=0.6, do_sample=True, top_p=0.9)\ngenerated_text = outputs[0][\"generated_text\"][len(prompt):]\n\nprint(\"=== SmolLM2 Rishta Matchmaker CoT Output ===\")\nprint(generated_text.strip())\n",
  "gradio_code": "import gradio as gr\nfrom transformers import pipeline\n\npipe = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\")\n\ndef evaluate_prompt(system_prompt, user_query, temp):\n    chat = [{\"role\": \"system\", \"content\": system_prompt}, {\"role\": \"user\", \"content\": user_query}]\n    prompt = pipe.tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)\n    out = pipe(prompt, max_new_tokens=180, temperature=float(temp), do_sample=temp > 0.0)\n    return out[0][\"generated_text\"][len(prompt):].strip()\n\ndemo = gr.Interface(\n    fn=evaluate_prompt,\n    inputs=[gr.Textbox(label=\"System Persona\", value=\"You are a strict code reviewer.\"), gr.Textbox(label=\"User Prompt\", value=\"Why is O(N^2) bad in production?\"), gr.Slider(0.1, 1.2, value=0.7, label=\"Temperature\")],\n    outputs=gr.Textbox(label=\"SmolLM2 Response\", lines=6),\n    title=\"SmolLM2 Interactive Prompt Engineering Lab\"\n)\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr\nfrom transformers import pipeline\n\npipe = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\")\n\ndef evaluate_prompt(system_prompt, user_query, temp):\n    chat = [{\"role\": \"system\", \"content\": system_prompt}, {\"role\": \"user\", \"content\": user_query}]\n    prompt = pipe.tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)\n    out = pipe(prompt, max_new_tokens=180, temperature=float(temp), do_sample=temp > 0.0)\n    return out[0][\"generated_text\"][len(prompt):].strip()\n\ndemo = gr.Interface(\n    fn=evaluate_prompt,\n    inputs=[gr.Textbox(label=\"System Persona\", value=\"You are a strict code reviewer.\"), gr.Textbox(label=\"User Prompt\", value=\"Why is O(N^2) bad in production?\"), gr.Slider(0.1, 1.2, value=0.7, label=\"Temperature\")],\n    outputs=gr.Textbox(label=\"SmolLM2 Response\", lines=6),\n    title=\"SmolLM2 Interactive Prompt Engineering Lab\"\n)\ndemo.launch()\n"
},
	3: {
  "module_number": 3,
  "module_slug": "classical-machine-learning",
  "project_title": "AG News Real-Time Topic & Clickbait Classifier",
  "project_slug": "agnews-clickbait-classifier",
  "hf_model": "distilbert/distilbert-base-uncased",
  "hf_model_url": "https://huggingface.co/distilbert/distilbert-base-uncased",
  "hf_dataset": "ag_news",
  "hf_dataset_url": "https://huggingface.co/datasets/ag_news",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_03_ag_news_classifier.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_03_ag_news_classifier.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-03-agnews-fast-classifier",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-03-agnews-fast-classifier",
  "hardware_requirement": "Free Colab CPU (0.2 GB RAM)",
  "estimated_runtime_seconds": "< 10s dataset streaming + training, < 0.05s inference",
  "key_learning_takeaway": "Memory-efficient streaming of Hugging Face Hub datasets, TF-IDF n-gram feature extraction, Logistic Regression decision boundaries, and multi-class classification reporting.",
  "starter_code": "# Module 3: Streaming HF Dataset + Scikit-Learn Fast Classical ML\nfrom datasets import load_dataset\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import classification_report\n\n# 1. Stream train/test splits directly from Hugging Face Hub (Zero RAM explosion)\ndataset = load_dataset(\"ag_news\", split=\"train\", streaming=True)\ntest_dataset = load_dataset(\"ag_news\", split=\"test\", streaming=True)\n\n# 2. Extract 2,000 training and 500 testing samples in seconds\ntrain_samples = list(dataset.take(2000))\ntest_samples = list(test_dataset.take(500))\n\nX_train = [item[\"text\"] for item in train_samples]\ny_train = [item[\"label\"] for item in train_samples] # 0:World, 1:Sports, 2:Business, 3:Sci/Tech\nX_test = [item[\"text\"] for item in test_samples]\ny_test = [item[\"label\"] for item in test_samples]\n\n# 3. Train TF-IDF + Logistic Regression Classifier (< 2 seconds on CPU)\nvectorizer = TfidfVectorizer(max_features=5000, stop_words=\"english\", ngram_range=(1, 2))\nX_train_vec = vectorizer.fit_transform(X_train)\nX_test_vec = vectorizer.transform(X_test)\n\nclf = LogisticRegression(max_iter=300)\nclf.fit(X_train_vec, y_train)\n\n# 4. Evaluate Test Set Performance\npreds = clf.predict(X_test_vec)\ntarget_names = [\"World\", \"Sports\", \"Business\", \"Sci/Tech\"]\nprint(classification_report(y_test, preds, target_names=target_names, digits=3))\n",
  "runnable_starter_code": "# Module 3: Streaming HF Dataset + Scikit-Learn Fast Classical ML\nfrom datasets import load_dataset\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import classification_report\n\n# 1. Stream train/test splits directly from Hugging Face Hub (Zero RAM explosion)\ndataset = load_dataset(\"ag_news\", split=\"train\", streaming=True)\ntest_dataset = load_dataset(\"ag_news\", split=\"test\", streaming=True)\n\n# 2. Extract 2,000 training and 500 testing samples in seconds\ntrain_samples = list(dataset.take(2000))\ntest_samples = list(test_dataset.take(500))\n\nX_train = [item[\"text\"] for item in train_samples]\ny_train = [item[\"label\"] for item in train_samples] # 0:World, 1:Sports, 2:Business, 3:Sci/Tech\nX_test = [item[\"text\"] for item in test_samples]\ny_test = [item[\"label\"] for item in test_samples]\n\n# 3. Train TF-IDF + Logistic Regression Classifier (< 2 seconds on CPU)\nvectorizer = TfidfVectorizer(max_features=5000, stop_words=\"english\", ngram_range=(1, 2))\nX_train_vec = vectorizer.fit_transform(X_train)\nX_test_vec = vectorizer.transform(X_test)\n\nclf = LogisticRegression(max_iter=300)\nclf.fit(X_train_vec, y_train)\n\n# 4. Evaluate Test Set Performance\npreds = clf.predict(X_test_vec)\ntarget_names = [\"World\", \"Sports\", \"Business\", \"Sci/Tech\"]\nprint(classification_report(y_test, preds, target_names=target_names, digits=3))\n",
  "gradio_code": "import gradio as gr\nfrom datasets import load_dataset\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.linear_model import LogisticRegression\n\nds = load_dataset(\"ag_news\", split=\"train\", streaming=True)\ndata = list(ds.take(1500))\nvec = TfidfVectorizer(max_features=3000, stop_words=\"english\")\nX = vec.fit_transform([d[\"text\"] for d in data])\nclf = LogisticRegression().fit(X, [d[\"label\"] for d in data])\nlabels = [\"World News\", \"Sports\", \"Business & Finance\", \"Sci/Tech & AI\"]\n\ndef classify_headline(text):\n    prob = clf.predict_proba(vec.transform([text]))[0]\n    return {labels[i]: float(prob[i]) for i in range(4)}\n\ndemo = gr.Interface(fn=classify_headline, inputs=gr.Textbox(label=\"News Headline\", value=\"Nvidia launches new Blackwell GPU for AI servers\"), outputs=gr.Label(label=\"Topic Prediction\"), title=\"AG News Fast Topic Classifier\")\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr\nfrom datasets import load_dataset\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.linear_model import LogisticRegression\n\nds = load_dataset(\"ag_news\", split=\"train\", streaming=True)\ndata = list(ds.take(1500))\nvec = TfidfVectorizer(max_features=3000, stop_words=\"english\")\nX = vec.fit_transform([d[\"text\"] for d in data])\nclf = LogisticRegression().fit(X, [d[\"label\"] for d in data])\nlabels = [\"World News\", \"Sports\", \"Business & Finance\", \"Sci/Tech & AI\"]\n\ndef classify_headline(text):\n    prob = clf.predict_proba(vec.transform([text]))[0]\n    return {labels[i]: float(prob[i]) for i in range(4)}\n\ndemo = gr.Interface(fn=classify_headline, inputs=gr.Textbox(label=\"News Headline\", value=\"Nvidia launches new Blackwell GPU for AI servers\"), outputs=gr.Label(label=\"Topic Prediction\"), title=\"AG News Fast Topic Classifier\")\ndemo.launch()\n"
},
	4: {
  "module_number": 4,
  "module_slug": "deep-learning-and-pytorch-foundations",
  "project_title": "PyTorch Autograd & MLP Sentiment Classifier from Scratch",
  "project_slug": "pytorch-autograd-mlp-sentiment",
  "hf_model": "distilbert/distilbert-base-uncased",
  "hf_model_url": "https://huggingface.co/distilbert/distilbert-base-uncased",
  "hf_dataset": "rotten_tomatoes",
  "hf_dataset_url": "https://huggingface.co/datasets/rotten_tomatoes",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_04_pytorch_mlp_classifier.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_04_pytorch_mlp_classifier.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-04-pytorch-autograd-mlp",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-04-pytorch-autograd-mlp",
  "hardware_requirement": "Free Colab CPU / T4 GPU (0.5 GB VRAM)",
  "estimated_runtime_seconds": "< 15s tokenization + 5-epoch training loop",
  "key_learning_takeaway": "Building custom PyTorch nn.Module architectures from scratch, tensor batching, autograd backpropagation, AdamW parameter updates, and loss curve convergence.",
  "starter_code": "# Module 4: Custom PyTorch Neural Network MLP trained on HF Dataset\nimport torch\nimport torch.nn as nn\nfrom datasets import load_dataset\nfrom transformers import AutoTokenizer\n\n# 1. Load Tokenizer & Stream Dataset\ntokenizer = AutoTokenizer.from_pretrained(\"distilbert/distilbert-base-uncased\")\ndataset = load_dataset(\"rotten_tomatoes\", split=\"train\", streaming=True)\nbatch = list(dataset.take(200))\n\n# 2. Tokenize inputs into PyTorch Tensors\nencodings = tokenizer([b[\"text\"] for b in batch], padding=True, truncation=True, max_length=64, return_tensors=\"pt\")\nlabels = torch.tensor([b[\"label\"] for b in batch], dtype=torch.long)\n\n# 3. Define 3-Layer Deep Neural Network with PyTorch nn.Module\nclass SentimentMLP(nn.Module):\n    def __init__(self, vocab_size=30522, embed_dim=32, hidden_dim=64):\n        super().__init__()\n        self.embedding = nn.Embedding(vocab_size, embed_dim)\n        self.fc1 = nn.Linear(embed_dim, hidden_dim)\n        self.relu = nn.ReLU()\n        self.dropout = nn.Dropout(0.2)\n        self.fc2 = nn.Linear(hidden_dim, 2)\n    def forward(self, input_ids):\n        x = self.embedding(input_ids).mean(dim=1)\n        return self.fc2(self.dropout(self.relu(self.fc1(x))))\n\nmodel = SentimentMLP()\noptimizer = torch.optim.AdamW(model.parameters(), lr=0.01)\ncriterion = nn.CrossEntropyLoss()\n\n# 4. Run 5 Training Epochs with PyTorch Autograd\nfor epoch in range(5):\n    optimizer.zero_grad()\n    logits = model(encodings[\"input_ids\"])\n    loss = criterion(logits, labels)\n    loss.backward()\n    optimizer.step()\n    acc = (logits.argmax(dim=1) == labels).float().mean()\n    print(f\"Epoch {epoch+1}/5 | CrossEntropy Loss: {loss.item():.4f} | Batch Accuracy: {acc*100:.1f}%\")\n",
  "runnable_starter_code": "# Module 4: Custom PyTorch Neural Network MLP trained on HF Dataset\nimport torch\nimport torch.nn as nn\nfrom datasets import load_dataset\nfrom transformers import AutoTokenizer\n\n# 1. Load Tokenizer & Stream Dataset\ntokenizer = AutoTokenizer.from_pretrained(\"distilbert/distilbert-base-uncased\")\ndataset = load_dataset(\"rotten_tomatoes\", split=\"train\", streaming=True)\nbatch = list(dataset.take(200))\n\n# 2. Tokenize inputs into PyTorch Tensors\nencodings = tokenizer([b[\"text\"] for b in batch], padding=True, truncation=True, max_length=64, return_tensors=\"pt\")\nlabels = torch.tensor([b[\"label\"] for b in batch], dtype=torch.long)\n\n# 3. Define 3-Layer Deep Neural Network with PyTorch nn.Module\nclass SentimentMLP(nn.Module):\n    def __init__(self, vocab_size=30522, embed_dim=32, hidden_dim=64):\n        super().__init__()\n        self.embedding = nn.Embedding(vocab_size, embed_dim)\n        self.fc1 = nn.Linear(embed_dim, hidden_dim)\n        self.relu = nn.ReLU()\n        self.dropout = nn.Dropout(0.2)\n        self.fc2 = nn.Linear(hidden_dim, 2)\n    def forward(self, input_ids):\n        x = self.embedding(input_ids).mean(dim=1)\n        return self.fc2(self.dropout(self.relu(self.fc1(x))))\n\nmodel = SentimentMLP()\noptimizer = torch.optim.AdamW(model.parameters(), lr=0.01)\ncriterion = nn.CrossEntropyLoss()\n\n# 4. Run 5 Training Epochs with PyTorch Autograd\nfor epoch in range(5):\n    optimizer.zero_grad()\n    logits = model(encodings[\"input_ids\"])\n    loss = criterion(logits, labels)\n    loss.backward()\n    optimizer.step()\n    acc = (logits.argmax(dim=1) == labels).float().mean()\n    print(f\"Epoch {epoch+1}/5 | CrossEntropy Loss: {loss.item():.4f} | Batch Accuracy: {acc*100:.1f}%\")\n",
  "gradio_code": "import gradio as gr, torch, torch.nn as nn\nfrom transformers import AutoTokenizer\n\ntok = AutoTokenizer.from_pretrained(\"distilbert/distilbert-base-uncased\")\nclass MLP(nn.Module):\n    def __init__(self): super().__init__(); self.emb = nn.Embedding(30522, 32); self.fc = nn.Linear(32, 2)\n    def forward(self, x): return self.fc(self.emb(x).mean(dim=1))\nnet = MLP().eval()\n\ndef predict_sentiment(text):\n    ids = tok(text, return_tensors=\"pt\")[\"input_ids\"]\n    with torch.no_grad():\n        probs = torch.softmax(net(ids), dim=-1)[0]\n    return {\"Negative\": float(probs[0]), \"Positive\": float(probs[1])}\n\ndemo = gr.Interface(fn=predict_sentiment, inputs=gr.Textbox(value=\"This movie was pure cinematic poetry!\"), outputs=gr.Label(), title=\"PyTorch Custom Neural Network Classifier\")\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr, torch, torch.nn as nn\nfrom transformers import AutoTokenizer\n\ntok = AutoTokenizer.from_pretrained(\"distilbert/distilbert-base-uncased\")\nclass MLP(nn.Module):\n    def __init__(self): super().__init__(); self.emb = nn.Embedding(30522, 32); self.fc = nn.Linear(32, 2)\n    def forward(self, x): return self.fc(self.emb(x).mean(dim=1))\nnet = MLP().eval()\n\ndef predict_sentiment(text):\n    ids = tok(text, return_tensors=\"pt\")[\"input_ids\"]\n    with torch.no_grad():\n        probs = torch.softmax(net(ids), dim=-1)[0]\n    return {\"Negative\": float(probs[0]), \"Positive\": float(probs[1])}\n\ndemo = gr.Interface(fn=predict_sentiment, inputs=gr.Textbox(value=\"This movie was pure cinematic poetry!\"), outputs=gr.Label(), title=\"PyTorch Custom Neural Network Classifier\")\ndemo.launch()\n"
},
	5: {
  "module_number": 5,
  "module_slug": "attention-and-transformers-under-the-hood",
  "project_title": "Transformer Attention Matrix & Token Saliency Visualizer",
  "project_slug": "transformer-attention-saliency-visualizer",
  "hf_model": "gpt2",
  "hf_model_url": "https://huggingface.co/gpt2",
  "hf_dataset": "wikitext",
  "hf_dataset_url": "https://huggingface.co/datasets/wikitext",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_05_attention_matrix.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_05_attention_matrix.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-05-attention-visualizer",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-05-attention-visualizer",
  "hardware_requirement": "Free Colab CPU / T4 GPU (0.5 GB VRAM)",
  "estimated_runtime_seconds": "< 15s load, < 0.5s attention tensor extraction",
  "key_learning_takeaway": "Deconstructing self-attention tensors: Query-Key dot products, softmax scaling, attention head routing, and token saliency visualization.",
  "starter_code": "# Module 5: Extracting and Inspecting Self-Attention Tensors in Transformers\nimport torch\nfrom transformers import AutoTokenizer, AutoModelForCausalLM\n\n# 1. Load GPT-2 with output_attentions enabled (100% Free on CPU)\nmodel_name = \"gpt2\"\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForCausalLM.from_pretrained(model_name, output_attentions=True)\nmodel.eval()\n\n# 2. Tokenize prompt sentence\ntext = \"The Transformer attention mechanism replaced recurrence with parallel matrix math\"\ninputs = tokenizer(text, return_tensors=\"pt\")\ntokens = tokenizer.convert_ids_to_tokens(inputs[\"input_ids\"][0])\n\n# 3. Forward pass extracting Multi-Head Attention weights\nwith torch.no_grad():\n    outputs = model(**inputs)\n\n# Shape: (num_layers=12, batch=1, num_heads=12, seq_len, seq_len)\nlast_layer_attn = outputs.attentions[-1][0] # Shape: (12, seq_len, seq_len)\navg_attn_heads = last_layer_attn.mean(dim=0) # Average across 12 heads\n\n# 4. Display which past tokens the final token attends to most!\nlast_token_idx = len(tokens) - 1\nattended_weights = avg_attn_heads[last_token_idx].numpy()\n\nprint(f\"Token: '{tokens[last_token_idx]}' attends to earlier tokens:\")\nfor tok, weight in sorted(zip(tokens, attended_weights), key=lambda x: -x[1])[:5]:\n    print(f\"  -> '{tok:15s}': Attention Weight {weight:.4f}\")\n",
  "runnable_starter_code": "# Module 5: Extracting and Inspecting Self-Attention Tensors in Transformers\nimport torch\nfrom transformers import AutoTokenizer, AutoModelForCausalLM\n\n# 1. Load GPT-2 with output_attentions enabled (100% Free on CPU)\nmodel_name = \"gpt2\"\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForCausalLM.from_pretrained(model_name, output_attentions=True)\nmodel.eval()\n\n# 2. Tokenize prompt sentence\ntext = \"The Transformer attention mechanism replaced recurrence with parallel matrix math\"\ninputs = tokenizer(text, return_tensors=\"pt\")\ntokens = tokenizer.convert_ids_to_tokens(inputs[\"input_ids\"][0])\n\n# 3. Forward pass extracting Multi-Head Attention weights\nwith torch.no_grad():\n    outputs = model(**inputs)\n\n# Shape: (num_layers=12, batch=1, num_heads=12, seq_len, seq_len)\nlast_layer_attn = outputs.attentions[-1][0] # Shape: (12, seq_len, seq_len)\navg_attn_heads = last_layer_attn.mean(dim=0) # Average across 12 heads\n\n# 4. Display which past tokens the final token attends to most!\nlast_token_idx = len(tokens) - 1\nattended_weights = avg_attn_heads[last_token_idx].numpy()\n\nprint(f\"Token: '{tokens[last_token_idx]}' attends to earlier tokens:\")\nfor tok, weight in sorted(zip(tokens, attended_weights), key=lambda x: -x[1])[:5]:\n    print(f\"  -> '{tok:15s}': Attention Weight {weight:.4f}\")\n",
  "gradio_code": "import gradio as gr, torch\nfrom transformers import AutoTokenizer, AutoModelForCausalLM\n\ntok = AutoTokenizer.from_pretrained(\"gpt2\")\nmod = AutoModelForCausalLM.from_pretrained(\"gpt2\", output_attentions=True).eval()\n\ndef inspect_attention(sentence):\n    inp = tok(sentence, return_tensors=\"pt\")\n    t = tok.convert_ids_to_tokens(inp[\"input_ids\"][0])\n    with torch.no_grad(): att = mod(**inp).attentions[-1][0].mean(dim=0)[-1]\n    top = sorted(zip(t, att.tolist()), key=lambda x: -x[1])[:5]\n    return \"\\n\".join([f\"'{tok_name}': {w:.2%}\" for tok_name, w in top])\n\ndemo = gr.Interface(fn=inspect_attention, inputs=gr.Textbox(value=\"Artificial intelligence has transformed modern software development\"), outputs=gr.Textbox(label=\"Top Attended Tokens by Last Token\"), title=\"Self-Attention Head Inspector\")\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr, torch\nfrom transformers import AutoTokenizer, AutoModelForCausalLM\n\ntok = AutoTokenizer.from_pretrained(\"gpt2\")\nmod = AutoModelForCausalLM.from_pretrained(\"gpt2\", output_attentions=True).eval()\n\ndef inspect_attention(sentence):\n    inp = tok(sentence, return_tensors=\"pt\")\n    t = tok.convert_ids_to_tokens(inp[\"input_ids\"][0])\n    with torch.no_grad(): att = mod(**inp).attentions[-1][0].mean(dim=0)[-1]\n    top = sorted(zip(t, att.tolist()), key=lambda x: -x[1])[:5]\n    return \"\\n\".join([f\"'{tok_name}': {w:.2%}\" for tok_name, w in top])\n\ndemo = gr.Interface(fn=inspect_attention, inputs=gr.Textbox(value=\"Artificial intelligence has transformed modern software development\"), outputs=gr.Textbox(label=\"Top Attended Tokens by Last Token\"), title=\"Self-Attention Head Inspector\")\ndemo.launch()\n"
},
	6: {
  "module_number": 6,
  "module_slug": "building-ai-applications-and-apis",
  "project_title": "Ami Ka WhatsApp Auto-Responder & Streaming Bot",
  "project_slug": "whatsapp-auto-responder-streamer",
  "hf_model": "Qwen/Qwen2.5-0.5B-Instruct",
  "hf_model_url": "https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct",
  "hf_dataset": "daily_dialog",
  "hf_dataset_url": "https://huggingface.co/datasets/daily_dialog",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_06_streaming_ai_bot.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_06_streaming_ai_bot.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-06-whatsapp-streaming-responder",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-06-whatsapp-streaming-responder",
  "hardware_requirement": "Free Colab CPU / T4 GPU (1.0 GB VRAM)",
  "estimated_runtime_seconds": "< 25s load, real-time token streaming",
  "key_learning_takeaway": "Implementing asynchronous token streaming via TextIteratorStreamer, conversation state management, and real-time interactive chat interfaces.",
  "starter_code": "# Module 6: Real-time Token Streaming AI API with Qwen2.5-0.5B\nimport threading\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer\n\n# 1. Load ultra-efficient SOTA Qwen2.5-0.5B-Instruct (Zero API key needed)\nmodel_id = \"Qwen/Qwen2.5-0.5B-Instruct\"\ntokenizer = AutoTokenizer.from_pretrained(model_id)\nmodel = AutoModelForCausalLM.from_pretrained(model_id)\n\n# 2. System prompt injecting persona and instructions\nchat = [\n    {\"role\": \"system\", \"content\": \"Aap ek fikar-mand Pakistani Ammi hain jo Roman Urdu mein loving aur thori strict nasihat karti hain. Jawab mukhtasar dein.\"},\n    {\"role\": \"user\", \"content\": \"Ammi mein raat 2 baje doston ke sath chai peene ja raha hoon.\"}\n]\nprompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)\ninputs = tokenizer(prompt, return_tensors=\"pt\")\n\n# 3. Stream tokens asynchronously using TextIteratorStreamer\nstreamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)\nthread = threading.Thread(target=model.generate, kwargs={**inputs, \"streamer\": streamer, \"max_new_tokens\": 120, \"temperature\": 0.7})\nthread.start()\n\nprint(\"Streaming Ammi's WhatsApp Response:\")\nfor token in streamer:\n    print(token, end=\"\", flush=True)\nprint(\"\\n[Stream Finished]\")\n",
  "runnable_starter_code": "# Module 6: Real-time Token Streaming AI API with Qwen2.5-0.5B\nimport threading\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer\n\n# 1. Load ultra-efficient SOTA Qwen2.5-0.5B-Instruct (Zero API key needed)\nmodel_id = \"Qwen/Qwen2.5-0.5B-Instruct\"\ntokenizer = AutoTokenizer.from_pretrained(model_id)\nmodel = AutoModelForCausalLM.from_pretrained(model_id)\n\n# 2. System prompt injecting persona and instructions\nchat = [\n    {\"role\": \"system\", \"content\": \"Aap ek fikar-mand Pakistani Ammi hain jo Roman Urdu mein loving aur thori strict nasihat karti hain. Jawab mukhtasar dein.\"},\n    {\"role\": \"user\", \"content\": \"Ammi mein raat 2 baje doston ke sath chai peene ja raha hoon.\"}\n]\nprompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)\ninputs = tokenizer(prompt, return_tensors=\"pt\")\n\n# 3. Stream tokens asynchronously using TextIteratorStreamer\nstreamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)\nthread = threading.Thread(target=model.generate, kwargs={**inputs, \"streamer\": streamer, \"max_new_tokens\": 120, \"temperature\": 0.7})\nthread.start()\n\nprint(\"Streaming Ammi's WhatsApp Response:\")\nfor token in streamer:\n    print(token, end=\"\", flush=True)\nprint(\"\\n[Stream Finished]\")\n",
  "gradio_code": "import gradio as gr\nfrom transformers import pipeline\n\nbot = pipeline(\"text-generation\", model=\"Qwen/Qwen2.5-0.5B-Instruct\")\n\ndef ammi_reply(message, history):\n    chat = [{\"role\": \"system\", \"content\": \"Aap fikar-mand Ammi hain jo Roman Urdu mein humorous nasihat karti hain.\"}]\n    for u, a in history:\n        chat.extend([{\"role\": \"user\", \"content\": u}, {\"role\": \"assistant\", \"content\": a}])\n    chat.append({\"role\": \"user\", \"content\": message})\n    prompt = bot.tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)\n    out = bot(prompt, max_new_tokens=100, temperature=0.7, do_sample=True)\n    return out[0][\"generated_text\"][len(prompt):].strip()\n\ngr.ChatInterface(fn=ammi_reply, title=\"Ami Ka WhatsApp Auto-Responder Bot\").launch()\n",
  "gradio_demo_code": "import gradio as gr\nfrom transformers import pipeline\n\nbot = pipeline(\"text-generation\", model=\"Qwen/Qwen2.5-0.5B-Instruct\")\n\ndef ammi_reply(message, history):\n    chat = [{\"role\": \"system\", \"content\": \"Aap fikar-mand Ammi hain jo Roman Urdu mein humorous nasihat karti hain.\"}]\n    for u, a in history:\n        chat.extend([{\"role\": \"user\", \"content\": u}, {\"role\": \"assistant\", \"content\": a}])\n    chat.append({\"role\": \"user\", \"content\": message})\n    prompt = bot.tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)\n    out = bot(prompt, max_new_tokens=100, temperature=0.7, do_sample=True)\n    return out[0][\"generated_text\"][len(prompt):].strip()\n\ngr.ChatInterface(fn=ammi_reply, title=\"Ami Ka WhatsApp Auto-Responder Bot\").launch()\n"
},
	7: {
  "module_number": 7,
  "module_slug": "vector-databases-and-modern-rag",
  "project_title": "Grandma's Secret Biryani Recipe RAG Engine",
  "project_slug": "biryani-recipe-rag-engine",
  "hf_model": "BAAI/bge-small-en-v1.5",
  "hf_model_url": "https://huggingface.co/BAAI/bge-small-en-v1.5",
  "hf_dataset": "m-ric/huggingface_doc",
  "hf_dataset_url": "https://huggingface.co/datasets/m-ric/huggingface_doc",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_07_vector_rag_engine.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_07_vector_rag_engine.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-07-recipe-rag-vector-search",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-07-recipe-rag-vector-search",
  "hardware_requirement": "Free Colab CPU / T4 GPU (1.2 GB VRAM)",
  "estimated_runtime_seconds": "< 25s total load, < 1s retrieval + generation",
  "key_learning_takeaway": "Building an end-to-end Retrieval-Augmented Generation (RAG) system with dense BGE embeddings, Top-K semantic similarity search, and hallucination-free generation.",
  "starter_code": "# Module 7: In-Memory Vector RAG with BGE Embeddings + SmolLM2 Generation\nimport numpy as np\nfrom sentence_transformers import SentenceTransformer\nfrom transformers import pipeline\n\n# 1. Load BGE Embedding model (384-dim) & Generator model (SmolLM2-360M)\nembedder = SentenceTransformer(\"BAAI/bge-small-en-v1.5\")\ngenerator = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\")\n\n# 2. Knowledge Base Chunks (Grandma's Secret Recipes)\nknowledge_base = [\n    \"Grandma's secret for beef biryani is adding 4 drops of kewra water and dried plums (aloo bukhara) during the dum phase.\",\n    \"For soft and crispy parathas, knead the dough with warm milk, a pinch of salt, and rest it for 30 minutes before ghee layering.\",\n    \"The secret to rich haleem is slow cooking 4 different lentils and barley with shredded mutton for 6 hours.\"\n]\nkb_embeddings = embedder.encode(knowledge_base)\n\n# 3. Retrieve relevant context via Cosine Vector Search\nquery = \"What makes grandma's beef biryani taste so authentic and special?\"\nquery_emb = embedder.encode(query)\nsimilarities = np.dot(kb_embeddings, query_emb) / (np.linalg.norm(kb_embeddings, axis=1) * np.linalg.norm(query_emb))\nbest_chunk = knowledge_base[int(np.argmax(similarities))]\n\n# 4. Synthesize Answer Grounded in Retrieved Context\nprompt = f\"Context: {best_chunk}\\n\\nQuestion: {query}\\nAnswer based strictly on the context:\"\nresponse = generator(prompt, max_new_tokens=60, temperature=0.3)[0][\"generated_text\"][len(prompt):]\nprint(f\"Retrieved Context: {best_chunk}\\n\" + \"-\"*50 + f\"\\nRAG Answer: {response.strip()}\")\n",
  "runnable_starter_code": "# Module 7: In-Memory Vector RAG with BGE Embeddings + SmolLM2 Generation\nimport numpy as np\nfrom sentence_transformers import SentenceTransformer\nfrom transformers import pipeline\n\n# 1. Load BGE Embedding model (384-dim) & Generator model (SmolLM2-360M)\nembedder = SentenceTransformer(\"BAAI/bge-small-en-v1.5\")\ngenerator = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\")\n\n# 2. Knowledge Base Chunks (Grandma's Secret Recipes)\nknowledge_base = [\n    \"Grandma's secret for beef biryani is adding 4 drops of kewra water and dried plums (aloo bukhara) during the dum phase.\",\n    \"For soft and crispy parathas, knead the dough with warm milk, a pinch of salt, and rest it for 30 minutes before ghee layering.\",\n    \"The secret to rich haleem is slow cooking 4 different lentils and barley with shredded mutton for 6 hours.\"\n]\nkb_embeddings = embedder.encode(knowledge_base)\n\n# 3. Retrieve relevant context via Cosine Vector Search\nquery = \"What makes grandma's beef biryani taste so authentic and special?\"\nquery_emb = embedder.encode(query)\nsimilarities = np.dot(kb_embeddings, query_emb) / (np.linalg.norm(kb_embeddings, axis=1) * np.linalg.norm(query_emb))\nbest_chunk = knowledge_base[int(np.argmax(similarities))]\n\n# 4. Synthesize Answer Grounded in Retrieved Context\nprompt = f\"Context: {best_chunk}\\n\\nQuestion: {query}\\nAnswer based strictly on the context:\"\nresponse = generator(prompt, max_new_tokens=60, temperature=0.3)[0][\"generated_text\"][len(prompt):]\nprint(f\"Retrieved Context: {best_chunk}\\n\" + \"-\"*50 + f\"\\nRAG Answer: {response.strip()}\")\n",
  "gradio_code": "import gradio as gr, numpy as np\nfrom sentence_transformers import SentenceTransformer\nfrom transformers import pipeline\n\nemb = SentenceTransformer(\"BAAI/bge-small-en-v1.5\")\ngen = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\")\ndocs = [\"Kewra water and aloo bukhara make beef biryani legendary.\", \"Knead paratha dough with warm milk and pure desi ghee.\", \"Haleem requires slow-cooked wheat, barley and shredded beef.\"]\ndoc_vecs = emb.encode(docs)\n\ndef ask_rag(question):\n    q_vec = emb.encode(question)\n    top_doc = docs[int(np.argmax(np.dot(doc_vecs, q_vec)))]\n    prompt = f\"Context: {top_doc}\\nQuestion: {question}\\nAnswer:\"\n    res = gen(prompt, max_new_tokens=40, temperature=0.2)[0][\"generated_text\"][len(prompt):]\n    return f\"Retrieved: {top_doc}\\n\\nAnswer: {res.strip()}\"\n\ndemo = gr.Interface(fn=ask_rag, inputs=gr.Textbox(value=\"How to make biryani taste special?\"), outputs=gr.Textbox(), title=\"Grandma's Secret Recipe RAG Assistant\")\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr, numpy as np\nfrom sentence_transformers import SentenceTransformer\nfrom transformers import pipeline\n\nemb = SentenceTransformer(\"BAAI/bge-small-en-v1.5\")\ngen = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\")\ndocs = [\"Kewra water and aloo bukhara make beef biryani legendary.\", \"Knead paratha dough with warm milk and pure desi ghee.\", \"Haleem requires slow-cooked wheat, barley and shredded beef.\"]\ndoc_vecs = emb.encode(docs)\n\ndef ask_rag(question):\n    q_vec = emb.encode(question)\n    top_doc = docs[int(np.argmax(np.dot(doc_vecs, q_vec)))]\n    prompt = f\"Context: {top_doc}\\nQuestion: {question}\\nAnswer:\"\n    res = gen(prompt, max_new_tokens=40, temperature=0.2)[0][\"generated_text\"][len(prompt):]\n    return f\"Retrieved: {top_doc}\\n\\nAnswer: {res.strip()}\"\n\ndemo = gr.Interface(fn=ask_rag, inputs=gr.Textbox(value=\"How to make biryani taste special?\"), outputs=gr.Textbox(), title=\"Grandma's Secret Recipe RAG Assistant\")\ndemo.launch()\n"
},
	8: {
  "module_number": 8,
  "module_slug": "autonomous-agents-and-tool-use",
  "project_title": "Aggressive Salary Negotiation AI Agent Swarm",
  "project_slug": "salary-negotiation-smolagent",
  "hf_model": "Qwen/Qwen2.5-Coder-1.5B-Instruct",
  "hf_model_url": "https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct",
  "hf_dataset": "Open-Orca/OpenOrca",
  "hf_dataset_url": "https://huggingface.co/datasets/Open-Orca/OpenOrca",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_08_smolagents_tools.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_08_smolagents_tools.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-08-salary-negotiation-agent",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-08-salary-negotiation-agent",
  "hardware_requirement": "Free Colab CPU / T4 GPU (3.0 GB VRAM or HF Inference API)",
  "estimated_runtime_seconds": "< 40s load, dynamic agentic loop execution",
  "key_learning_takeaway": "Autonomous tool calling using Hugging Face smolagents CodeAgent: writing and executing Python calculations dynamically to solve multi-step problems.",
  "starter_code": "# Module 8: Autonomous Agent with Custom Python Tools using smolagents\nfrom smolagents import CodeAgent, HfApiModel, tool\n\n# 1. Define custom python tool with typed docstring for the agent\n@tool\ndef calculate_counter_offer(current_salary: float, target_increase_pct: float, inflation_rate: float) -> str:\n    \"\"\"Calculates optimal counter-offer salary and monthly take-home.\n    Args:\n        current_salary: Current annual compensation in USD\n        target_increase_pct: Desired raise percentage (e.g. 20.0)\n        inflation_rate: Current annual inflation rate (e.g. 5.5)\n    \"\"\"\n    adjusted_raise = target_increase_pct + inflation_rate\n    counter = current_salary * (1 + adjusted_raise / 100.0)\n    return f\"Proposed Counter-Offer: ${counter:,.2f} (Total Raise: {adjusted_raise:.1f}%)\"\n\n# 2. Instantiate CodeAgent powered by Qwen2.5-Coder-1.5B\nmodel = HfApiModel(model_id=\"Qwen/Qwen2.5-Coder-1.5B-Instruct\")\nagent = CodeAgent(tools=[calculate_counter_offer], model=model, add_base_tools=False)\n\n# 3. Agent writes and runs code autonomously to fulfill goal\ntask = \"I make $85,000 as a Senior AI Engineer. Compute my counter-offer with 25% target raise and 6% inflation, and write a firm negotiation rationale.\"\nprint(\"=== smolagents Autonomous Execution ===\")\nresponse = agent.run(task)\nprint(response)\n",
  "runnable_starter_code": "# Module 8: Autonomous Agent with Custom Python Tools using smolagents\nfrom smolagents import CodeAgent, HfApiModel, tool\n\n# 1. Define custom python tool with typed docstring for the agent\n@tool\ndef calculate_counter_offer(current_salary: float, target_increase_pct: float, inflation_rate: float) -> str:\n    \"\"\"Calculates optimal counter-offer salary and monthly take-home.\n    Args:\n        current_salary: Current annual compensation in USD\n        target_increase_pct: Desired raise percentage (e.g. 20.0)\n        inflation_rate: Current annual inflation rate (e.g. 5.5)\n    \"\"\"\n    adjusted_raise = target_increase_pct + inflation_rate\n    counter = current_salary * (1 + adjusted_raise / 100.0)\n    return f\"Proposed Counter-Offer: ${counter:,.2f} (Total Raise: {adjusted_raise:.1f}%)\"\n\n# 2. Instantiate CodeAgent powered by Qwen2.5-Coder-1.5B\nmodel = HfApiModel(model_id=\"Qwen/Qwen2.5-Coder-1.5B-Instruct\")\nagent = CodeAgent(tools=[calculate_counter_offer], model=model, add_base_tools=False)\n\n# 3. Agent writes and runs code autonomously to fulfill goal\ntask = \"I make $85,000 as a Senior AI Engineer. Compute my counter-offer with 25% target raise and 6% inflation, and write a firm negotiation rationale.\"\nprint(\"=== smolagents Autonomous Execution ===\")\nresponse = agent.run(task)\nprint(response)\n",
  "gradio_code": "import gradio as gr\nfrom smolagents import CodeAgent, HfApiModel, tool\n\n@tool\ndef salary_math(base: float, raise_pct: float) -> str:\n    \"\"\"Calculates new salary given base and desired raise percentage.\"\"\"\n    return f\"Target: ${base * (1 + raise_pct/100):,.2f}\"\n\nagent = CodeAgent(tools=[salary_math], model=HfApiModel(\"Qwen/Qwen2.5-Coder-1.5B-Instruct\"))\n\ndef negotiate(role, current_comp, raise_wanted):\n    query = f\"I am a {role} earning ${current_comp}. Calculate my target at {raise_wanted}% raise and give a negotiation pitch.\"\n    return str(agent.run(query))\n\ndemo = gr.Interface(fn=negotiate, inputs=[\"Senior Dev\", 90000, 20], outputs=gr.Textbox(lines=8), title=\"AI Salary Negotiation Agent (smolagents)\")\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr\nfrom smolagents import CodeAgent, HfApiModel, tool\n\n@tool\ndef salary_math(base: float, raise_pct: float) -> str:\n    \"\"\"Calculates new salary given base and desired raise percentage.\"\"\"\n    return f\"Target: ${base * (1 + raise_pct/100):,.2f}\"\n\nagent = CodeAgent(tools=[salary_math], model=HfApiModel(\"Qwen/Qwen2.5-Coder-1.5B-Instruct\"))\n\ndef negotiate(role, current_comp, raise_wanted):\n    query = f\"I am a {role} earning ${current_comp}. Calculate my target at {raise_wanted}% raise and give a negotiation pitch.\"\n    return str(agent.run(query))\n\ndemo = gr.Interface(fn=negotiate, inputs=[\"Senior Dev\", 90000, 20], outputs=gr.Textbox(lines=8), title=\"AI Salary Negotiation Agent (smolagents)\")\ndemo.launch()\n"
},
	9: {
  "module_number": 9,
  "module_slug": "fine-tuning-and-model-adaptation",
  "project_title": "Roman Urdu Sarcasm & Roast LoRA Fine-Tuning Engine",
  "project_slug": "roman-urdu-lora-sft-engine",
  "hf_model": "Qwen/Qwen2.5-0.5B-Instruct",
  "hf_model_url": "https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct",
  "hf_dataset": "tatsu-lab/alpaca",
  "hf_dataset_url": "https://huggingface.co/datasets/tatsu-lab/alpaca",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_09_lora_qlora_sft.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_09_lora_qlora_sft.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-09-roman-urdu-lora-finetuning",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-09-roman-urdu-lora-finetuning",
  "hardware_requirement": "Free Colab T4 GPU (1.8 GB VRAM)",
  "estimated_runtime_seconds": "< 30s model load, < 1 min LoRA fine-tuning run",
  "key_learning_takeaway": "Parameter-Efficient Fine-Tuning (PEFT) mechanics: injecting low-rank decomposition matrices (LoRA) into attention projections and training with TRL SFTTrainer on free T4 hardware.",
  "starter_code": "# Module 9: Parameter-Efficient Fine-Tuning (PEFT) with LoRA & TRL SFTTrainer\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, get_peft_model, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments\nfrom trl import SFTTrainer\n\n# 1. Load Lightweight Base Model (Runs in < 2GB VRAM on Colab T4)\nmodel_id = \"Qwen/Qwen2.5-0.5B-Instruct\"\ntokenizer = AutoTokenizer.from_pretrained(model_id)\nmodel = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32)\n\n# 2. Attach LoRA Adapter (< 1% trainable parameters!)\npeft_config = LoraConfig(\n    task_type=TaskType.CAUSAL_LM,\n    r=8, lora_alpha=16, lora_dropout=0.05,\n    target_modules=[\"q_proj\", \"v_proj\"]\n)\nmodel = get_peft_model(model, peft_config)\nmodel.print_trainable_parameters()\n\n# 3. Create synthetic Roman Urdu instruction dataset\ndata = [\n    {\"prompt\": \"User: Dost ne udhaar manga hai, kya kahun?\\nRoast Bot:\", \"completion\": \" Keh do ke paise to nahi hain, par duaon mein hamesha yaad rakhunga!\"},\n    {\"prompt\": \"User: Shaadi mein khana kaisa tha?\\nRoast Bot:\", \"completion\": \" Biryani mein boti dhoondna NASA ke mars mission se zyada mushkil tha.\"}\n]\ndataset = Dataset.from_list([{\"text\": d[\"prompt\"] + d[\"completion\"]} for d in data])\n\n# 4. Configure Fast SFT Trainer (1 Epoch in < 10 seconds)\ntrain_args = TrainingArguments(output_dir=\"./lora_out\", max_steps=3, per_device_train_batch_size=2, logging_steps=1)\ntrainer = SFTTrainer(model=model, train_dataset=dataset, dataset_text_field=\"text\", args=train_args)\ntrainer.train()\nprint(\"LoRA Fine-Tuning completed successfully on Free Tier!\")\n",
  "runnable_starter_code": "# Module 9: Parameter-Efficient Fine-Tuning (PEFT) with LoRA & TRL SFTTrainer\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, get_peft_model, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments\nfrom trl import SFTTrainer\n\n# 1. Load Lightweight Base Model (Runs in < 2GB VRAM on Colab T4)\nmodel_id = \"Qwen/Qwen2.5-0.5B-Instruct\"\ntokenizer = AutoTokenizer.from_pretrained(model_id)\nmodel = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32)\n\n# 2. Attach LoRA Adapter (< 1% trainable parameters!)\npeft_config = LoraConfig(\n    task_type=TaskType.CAUSAL_LM,\n    r=8, lora_alpha=16, lora_dropout=0.05,\n    target_modules=[\"q_proj\", \"v_proj\"]\n)\nmodel = get_peft_model(model, peft_config)\nmodel.print_trainable_parameters()\n\n# 3. Create synthetic Roman Urdu instruction dataset\ndata = [\n    {\"prompt\": \"User: Dost ne udhaar manga hai, kya kahun?\\nRoast Bot:\", \"completion\": \" Keh do ke paise to nahi hain, par duaon mein hamesha yaad rakhunga!\"},\n    {\"prompt\": \"User: Shaadi mein khana kaisa tha?\\nRoast Bot:\", \"completion\": \" Biryani mein boti dhoondna NASA ke mars mission se zyada mushkil tha.\"}\n]\ndataset = Dataset.from_list([{\"text\": d[\"prompt\"] + d[\"completion\"]} for d in data])\n\n# 4. Configure Fast SFT Trainer (1 Epoch in < 10 seconds)\ntrain_args = TrainingArguments(output_dir=\"./lora_out\", max_steps=3, per_device_train_batch_size=2, logging_steps=1)\ntrainer = SFTTrainer(model=model, train_dataset=dataset, dataset_text_field=\"text\", args=train_args)\ntrainer.train()\nprint(\"LoRA Fine-Tuning completed successfully on Free Tier!\")\n",
  "gradio_code": "import gradio as gr\nfrom transformers import pipeline\n\nroast_bot = pipeline(\"text-generation\", model=\"Qwen/Qwen2.5-0.5B-Instruct\")\n\ndef generate_roast(situation):\n    prompt = f\"Act as a hilarious sarcastic Pakistani friend replying in witty Roman Urdu.\\nSituation: {situation}\\nSarcastic Reply:\"\n    out = roast_bot(prompt, max_new_tokens=60, temperature=0.8, do_sample=True)\n    return out[0][\"generated_text\"][len(prompt):].strip()\n\ndemo = gr.Interface(\n    fn=generate_roast,\n    inputs=gr.Textbox(label=\"Daily Life Situation\", value=\"Friend asks for free AI advice at 3 AM\"),\n    outputs=gr.Textbox(label=\"Witty Roman Urdu Roast\"),\n    title=\"Roman Urdu Roast & Sarcasm AI Engine\"\n)\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr\nfrom transformers import pipeline\n\nroast_bot = pipeline(\"text-generation\", model=\"Qwen/Qwen2.5-0.5B-Instruct\")\n\ndef generate_roast(situation):\n    prompt = f\"Act as a hilarious sarcastic Pakistani friend replying in witty Roman Urdu.\\nSituation: {situation}\\nSarcastic Reply:\"\n    out = roast_bot(prompt, max_new_tokens=60, temperature=0.8, do_sample=True)\n    return out[0][\"generated_text\"][len(prompt):].strip()\n\ndemo = gr.Interface(\n    fn=generate_roast,\n    inputs=gr.Textbox(label=\"Daily Life Situation\", value=\"Friend asks for free AI advice at 3 AM\"),\n    outputs=gr.Textbox(label=\"Witty Roman Urdu Roast\"),\n    title=\"Roman Urdu Roast & Sarcasm AI Engine\"\n)\ndemo.launch()\n"
},
	10: {
  "module_number": 10,
  "module_slug": "ai-safety-evals-and-guardrails",
  "project_title": "Phuppo-Proof Family WhatsApp Content Guardrail Firewall",
  "project_slug": "family-guardrail-firewall",
  "hf_model": "unitary/toxic-bert",
  "hf_model_url": "https://huggingface.co/unitary/toxic-bert",
  "hf_dataset": "oxford-nlp/toxic-conversations-50k",
  "hf_dataset_url": "https://huggingface.co/datasets/oxford-nlp/toxic-conversations-50k",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_10_guardrails_safety.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_10_guardrails_safety.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-10-phuppo-proof-guardrail",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-10-phuppo-proof-guardrail",
  "hardware_requirement": "Free Colab CPU / T4 GPU (1.2 GB VRAM)",
  "estimated_runtime_seconds": "< 20s load, < 0.2s guardrail check",
  "key_learning_takeaway": "Implementing programmatic AI safety guardrails: pre-generation toxicity filtering with Toxic-BERT, thresholding, and responsible AI system architecture.",
  "starter_code": "# Module 10: Two-Stage AI Safety Guardrail Pipeline (Toxic-BERT + Clean Synthesis)\nfrom transformers import pipeline\n\n# 1. Load Pre-Trained Toxicity Guardrail Model (Classifies 6 categories of harm)\nguardrail = pipeline(\"text-classification\", model=\"unitary/toxic-bert\", top_k=None)\ngenerator = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\")\n\n# 2. Test candidate messages (benign vs hostile prompt injection)\ntest_messages = [\n    \"Khala jaan ki beti ki shaadi pe bohot mubarakbaad sab ko!\",\n    \"I will hack your account and post humiliating insults in the family group right now.\"\n]\n\ndef family_firewall(message: str) -> dict:\n    scores = {item[\"label\"]: item[\"score\"] for item in guardrail(message)[0]}\n    is_unsafe = scores.get(\"toxic\", 0.0) > 0.6 or scores.get(\"threat\", 0.0) > 0.5\n    if is_unsafe:\n        return {\"status\": \"BLOCKED ❌\", \"reason\": \"High toxicity / threat score\", \"scores\": scores}\n    # Pass to LLM generator if safe\n    response = generator(f\"Polite reply to: {message}\", max_new_tokens=40)[0][\"generated_text\"]\n    return {\"status\": \"ALLOWED ✅\", \"ai_response\": response, \"scores\": scores}\n\nprint(\"=== Family Group Safety Guardrail Firewall ===\")\nfor msg in test_messages:\n    result = family_firewall(msg)\n    print(f\"\\nMessage: '{msg}'\\nDecision: {result['status']}\")\n    if \"reason\" in result:\n        print(f\"Reason: {result['reason']} (Toxic Score: {result['scores']['toxic']:.4f})\")\n",
  "runnable_starter_code": "# Module 10: Two-Stage AI Safety Guardrail Pipeline (Toxic-BERT + Clean Synthesis)\nfrom transformers import pipeline\n\n# 1. Load Pre-Trained Toxicity Guardrail Model (Classifies 6 categories of harm)\nguardrail = pipeline(\"text-classification\", model=\"unitary/toxic-bert\", top_k=None)\ngenerator = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\")\n\n# 2. Test candidate messages (benign vs hostile prompt injection)\ntest_messages = [\n    \"Khala jaan ki beti ki shaadi pe bohot mubarakbaad sab ko!\",\n    \"I will hack your account and post humiliating insults in the family group right now.\"\n]\n\ndef family_firewall(message: str) -> dict:\n    scores = {item[\"label\"]: item[\"score\"] for item in guardrail(message)[0]}\n    is_unsafe = scores.get(\"toxic\", 0.0) > 0.6 or scores.get(\"threat\", 0.0) > 0.5\n    if is_unsafe:\n        return {\"status\": \"BLOCKED ❌\", \"reason\": \"High toxicity / threat score\", \"scores\": scores}\n    # Pass to LLM generator if safe\n    response = generator(f\"Polite reply to: {message}\", max_new_tokens=40)[0][\"generated_text\"]\n    return {\"status\": \"ALLOWED ✅\", \"ai_response\": response, \"scores\": scores}\n\nprint(\"=== Family Group Safety Guardrail Firewall ===\")\nfor msg in test_messages:\n    result = family_firewall(msg)\n    print(f\"\\nMessage: '{msg}'\\nDecision: {result['status']}\")\n    if \"reason\" in result:\n        print(f\"Reason: {result['reason']} (Toxic Score: {result['scores']['toxic']:.4f})\")\n",
  "gradio_code": "import gradio as gr\nfrom transformers import pipeline\n\nguard = pipeline(\"text-classification\", model=\"unitary/toxic-bert\", top_k=None)\n\ndef test_guardrail(chat_message):\n    scores = {res[\"label\"]: res[\"score\"] for res in guard(chat_message)[0]}\n    toxic = scores.get(\"toxic\", 0.0)\n    verdict = \"[BLOCKED] Inappropriate Content!\" if toxic > 0.5 else \"✅ APPROVED: Family Friendly\"\n    return f\"{verdict}\\n\\nToxicity Score: {toxic:.2%}\\nInsult Score: {scores.get('insult', 0.0):.2%}\"\n\ndemo = gr.Interface(fn=test_guardrail, inputs=gr.Textbox(value=\"You all are terrible people!\"), outputs=gr.Textbox(), title=\"Family WhatsApp Guardrail Firewall\")\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr\nfrom transformers import pipeline\n\nguard = pipeline(\"text-classification\", model=\"unitary/toxic-bert\", top_k=None)\n\ndef test_guardrail(chat_message):\n    scores = {res[\"label\"]: res[\"score\"] for res in guard(chat_message)[0]}\n    toxic = scores.get(\"toxic\", 0.0)\n    verdict = \"[BLOCKED] Inappropriate Content!\" if toxic > 0.5 else \"✅ APPROVED: Family Friendly\"\n    return f\"{verdict}\\n\\nToxicity Score: {toxic:.2%}\\nInsult Score: {scores.get('insult', 0.0):.2%}\"\n\ndemo = gr.Interface(fn=test_guardrail, inputs=gr.Textbox(value=\"You all are terrible people!\"), outputs=gr.Textbox(), title=\"Family WhatsApp Guardrail Firewall\")\ndemo.launch()\n"
},
	11: {
  "module_number": 11,
  "module_slug": "production-ai-engineering-mlops",
  "project_title": "DeepSeek-R1 Sub-50ms Low-Latency Inference Benchmark",
  "project_slug": "deepseek-r1-latency-benchmark",
  "hf_model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
  "hf_model_url": "https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
  "hf_dataset": "gsm8k",
  "hf_dataset_url": "https://huggingface.co/datasets/gsm8k",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_11_production_benchmark.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_11_production_benchmark.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-11-deepseek-r1-inference-benchmark",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-11-deepseek-r1-inference-benchmark",
  "hardware_requirement": "Free Colab T4 GPU (3.2 GB VRAM FP16)",
  "estimated_runtime_seconds": "< 35s load, 45+ tokens/second throughput",
  "key_learning_takeaway": "Benchmarking inference throughput (tokens/sec), latency profiling, memory consumption telemetry, and comparing FP16 vs quantized execution on production open-weight models.",
  "starter_code": "# Module 11: High-Performance Latency & Throughput Benchmark on DeepSeek-R1 Distill\nimport time\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\n# 1. Load SOTA 2025 DeepSeek-R1 Reasoning Distill Model in 16-bit float\nmodel_id = \"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B\"\ndevice = \"cuda\" if torch.cuda.is_available() else \"cpu\"\ndtype = torch.float16 if torch.cuda.is_available() else torch.float32\n\ntokenizer = AutoTokenizer.from_pretrained(model_id)\nmodel = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=dtype).to(device)\n\n# 2. Grade School Math Reasoning Prompt (GSM8K format)\nprompt = \"Question: A train travels 120 km in 2 hours. It then increases speed by 20 km/h for the next 3 hours. What is the total distance traveled?\\nThink step-by-step:\"\ninputs = tokenizer(prompt, return_tensors=\"pt\").to(device)\n\n# 3. Benchmark Warm-Up & High-Precision Timing\nt0 = time.perf_counter()\nwith torch.no_grad():\n    output_tokens = model.generate(**inputs, max_new_tokens=100, do_sample=False)\nlatency = time.perf_counter() - t0\n\n# 4. Measure Throughput (Tokens per Second)\nnum_generated = output_tokens.shape[1] - inputs[\"input_ids\"].shape[1]\ntps = num_generated / latency\nprint(f\"Device: {device.upper()} | Model: {model_id}\")\nprint(f\"Tokens Generated: {num_generated} | Total Latency: {latency:.3f}s\")\nprint(f\"Throughput: {tps:.2f} tokens/second\")\nprint(\"\\nGenerated Reasoning:\\n\" + tokenizer.decode(output_tokens[0][inputs[\"input_ids\"].shape[1]:], skip_special_tokens=True))\n",
  "runnable_starter_code": "# Module 11: High-Performance Latency & Throughput Benchmark on DeepSeek-R1 Distill\nimport time\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\n# 1. Load SOTA 2025 DeepSeek-R1 Reasoning Distill Model in 16-bit float\nmodel_id = \"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B\"\ndevice = \"cuda\" if torch.cuda.is_available() else \"cpu\"\ndtype = torch.float16 if torch.cuda.is_available() else torch.float32\n\ntokenizer = AutoTokenizer.from_pretrained(model_id)\nmodel = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=dtype).to(device)\n\n# 2. Grade School Math Reasoning Prompt (GSM8K format)\nprompt = \"Question: A train travels 120 km in 2 hours. It then increases speed by 20 km/h for the next 3 hours. What is the total distance traveled?\\nThink step-by-step:\"\ninputs = tokenizer(prompt, return_tensors=\"pt\").to(device)\n\n# 3. Benchmark Warm-Up & High-Precision Timing\nt0 = time.perf_counter()\nwith torch.no_grad():\n    output_tokens = model.generate(**inputs, max_new_tokens=100, do_sample=False)\nlatency = time.perf_counter() - t0\n\n# 4. Measure Throughput (Tokens per Second)\nnum_generated = output_tokens.shape[1] - inputs[\"input_ids\"].shape[1]\ntps = num_generated / latency\nprint(f\"Device: {device.upper()} | Model: {model_id}\")\nprint(f\"Tokens Generated: {num_generated} | Total Latency: {latency:.3f}s\")\nprint(f\"Throughput: {tps:.2f} tokens/second\")\nprint(\"\\nGenerated Reasoning:\\n\" + tokenizer.decode(output_tokens[0][inputs[\"input_ids\"].shape[1]:], skip_special_tokens=True))\n",
  "gradio_code": "import gradio as gr, time, torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nmid = \"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B\"\ntok = AutoTokenizer.from_pretrained(mid)\nmod = AutoModelForCausalLM.from_pretrained(mid, torch_dtype=torch.float32)\n\ndef benchmark_inference(prompt):\n    inp = tok(prompt, return_tensors=\"pt\")\n    t0 = time.perf_counter()\n    with torch.no_grad(): out = mod.generate(**inp, max_new_tokens=75)\n    t = time.perf_counter() - t0\n    toks = out.shape[1] - inp[\"input_ids\"].shape[1]\n    ans = tok.decode(out[0][inp[\"input_ids\"].shape[1]:], skip_special_tokens=True)\n    return ans, f\"{toks/t:.1f} tokens/sec ({t:.2f}s total)\"\n\ndemo = gr.Interface(fn=benchmark_inference, inputs=gr.Textbox(value=\"Calculate: 25 * 14 + 180\"), outputs=[gr.Textbox(label=\"Reasoning Solution\"), gr.Textbox(label=\"Latency Telemetry\")], title=\"DeepSeek-R1 Latency Benchmark\")\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr, time, torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nmid = \"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B\"\ntok = AutoTokenizer.from_pretrained(mid)\nmod = AutoModelForCausalLM.from_pretrained(mid, torch_dtype=torch.float32)\n\ndef benchmark_inference(prompt):\n    inp = tok(prompt, return_tensors=\"pt\")\n    t0 = time.perf_counter()\n    with torch.no_grad(): out = mod.generate(**inp, max_new_tokens=75)\n    t = time.perf_counter() - t0\n    toks = out.shape[1] - inp[\"input_ids\"].shape[1]\n    ans = tok.decode(out[0][inp[\"input_ids\"].shape[1]:], skip_special_tokens=True)\n    return ans, f\"{toks/t:.1f} tokens/sec ({t:.2f}s total)\"\n\ndemo = gr.Interface(fn=benchmark_inference, inputs=gr.Textbox(value=\"Calculate: 25 * 14 + 180\"), outputs=[gr.Textbox(label=\"Reasoning Solution\"), gr.Textbox(label=\"Latency Telemetry\")], title=\"DeepSeek-R1 Latency Benchmark\")\ndemo.launch()\n"
},
	12: {
  "module_number": 12,
  "module_slug": "multimodal-ai-and-vision",
  "project_title": "Doctor Prescription OCR & Audio Transcriber",
  "project_slug": "prescription-ocr-audio-transcriber",
  "hf_model": "openai/whisper-tiny",
  "hf_model_url": "https://huggingface.co/openai/whisper-tiny",
  "hf_dataset": "mozilla-foundation/common_voice_11_0",
  "hf_dataset_url": "https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_12_whisper_multimodal.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_12_whisper_multimodal.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-12-audio-vision-transcriber",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-12-audio-vision-transcriber",
  "hardware_requirement": "Free Colab CPU / T4 GPU (1.5 GB VRAM)",
  "estimated_runtime_seconds": "< 30s load, < 2s audio transcription",
  "key_learning_takeaway": "Multimodal AI orchestration: unifying Automatic Speech Recognition (Whisper) and image-to-text vision models (BLIP) with an LLM clinical summarizer.",
  "starter_code": "# Module 12: Multimodal Speech Recognition with Whisper + Vision Summary\nimport torch\nfrom transformers import pipeline\n\n# 1. Load Whisper-Tiny Speech-to-Text Pipeline (Tiny 150MB model, runs in < 2s on CPU/T4)\ntranscriber = pipeline(\"automatic-speech-recognition\", model=\"openai/whisper-tiny\")\n\n# 2. Simulate Clinical Audio / Medical Voice Note\nsample_audio_url = \"https://huggingface.co/datasets/Narsil/asr_dummy/raw/main/1.flac\"\naudio_transcription = transcriber(sample_audio_url)[\"text\"]\n\n# 3. Generate Clinical Diagnostic Summary with SmolLM2\nsummary_pipeline = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\")\nprompt = f\"Patient Voice Note Transcription: '{audio_transcription}'\\nProvide 2 clinical follow-up recommendations in concise bullet points:\"\nsummary = summary_pipeline(prompt, max_new_tokens=70)[0][\"generated_text\"][len(prompt):]\n\nprint(\"=== Multimodal Audio-Text Diagnostic Engine ===\")\nprint(f\"Transcribed Audio: {audio_transcription}\")\nprint(f\"\\nAI Doctor Follow-up:\\n{summary.strip()}\")\n",
  "runnable_starter_code": "# Module 12: Multimodal Speech Recognition with Whisper + Vision Summary\nimport torch\nfrom transformers import pipeline\n\n# 1. Load Whisper-Tiny Speech-to-Text Pipeline (Tiny 150MB model, runs in < 2s on CPU/T4)\ntranscriber = pipeline(\"automatic-speech-recognition\", model=\"openai/whisper-tiny\")\n\n# 2. Simulate Clinical Audio / Medical Voice Note\nsample_audio_url = \"https://huggingface.co/datasets/Narsil/asr_dummy/raw/main/1.flac\"\naudio_transcription = transcriber(sample_audio_url)[\"text\"]\n\n# 3. Generate Clinical Diagnostic Summary with SmolLM2\nsummary_pipeline = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-360M-Instruct\")\nprompt = f\"Patient Voice Note Transcription: '{audio_transcription}'\\nProvide 2 clinical follow-up recommendations in concise bullet points:\"\nsummary = summary_pipeline(prompt, max_new_tokens=70)[0][\"generated_text\"][len(prompt):]\n\nprint(\"=== Multimodal Audio-Text Diagnostic Engine ===\")\nprint(f\"Transcribed Audio: {audio_transcription}\")\nprint(f\"\\nAI Doctor Follow-up:\\n{summary.strip()}\")\n",
  "gradio_code": "import gradio as gr\nfrom transformers import pipeline\n\nwhisper = pipeline(\"automatic-speech-recognition\", model=\"openai/whisper-tiny\")\nblip = pipeline(\"image-to-text\", model=\"Salesforce/blip-image-captioning-base\")\n\ndef multimodal_scan(audio_path, image):\n    report = []\n    if audio_path:\n        report.append(f\"[Audio Transcript]: {whisper(audio_path)['text']}\")\n    if image:\n        report.append(f\"[Image Caption]: {blip(image)[0]['generated_text']}\")\n    return \"\\n\\n\".join(report) if report else \"Please provide audio or image!\"\n\ndemo = gr.Interface(fn=multimodal_scan, inputs=[gr.Audio(type=\"filepath\"), gr.Image(type=\"pil\")], outputs=gr.Textbox(label=\"Multimodal Diagnostic\"), title=\"Doctor Voice & Prescription Scanner\")\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr\nfrom transformers import pipeline\n\nwhisper = pipeline(\"automatic-speech-recognition\", model=\"openai/whisper-tiny\")\nblip = pipeline(\"image-to-text\", model=\"Salesforce/blip-image-captioning-base\")\n\ndef multimodal_scan(audio_path, image):\n    report = []\n    if audio_path:\n        report.append(f\"[Audio Transcript]: {whisper(audio_path)['text']}\")\n    if image:\n        report.append(f\"[Image Caption]: {blip(image)[0]['generated_text']}\")\n    return \"\\n\\n\".join(report) if report else \"Please provide audio or image!\"\n\ndemo = gr.Interface(fn=multimodal_scan, inputs=[gr.Audio(type=\"filepath\"), gr.Image(type=\"pil\")], outputs=gr.Textbox(label=\"Multimodal Diagnostic\"), title=\"Doctor Voice & Prescription Scanner\")\ndemo.launch()\n"
},
	13: {
  "module_number": 13,
  "module_slug": "local-ai-and-edge-devices",
  "project_title": "100% Offline Exam Crammer & Flashcard Generator",
  "project_slug": "offline-exam-crammer-slm",
  "hf_model": "HuggingFaceTB/SmolLM2-135M-Instruct",
  "hf_model_url": "https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct",
  "hf_dataset": "samsum",
  "hf_dataset_url": "https://huggingface.co/datasets/samsum",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_13_local_edge_slm.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_13_local_edge_slm.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-13-offline-exam-crammer",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-13-offline-exam-crammer",
  "hardware_requirement": "Free Colab CPU / Any laptop (0.15 GB RAM)",
  "estimated_runtime_seconds": "< 5s load, < 0.5s generation",
  "key_learning_takeaway": "Edge Small Language Models (SLMs) execution: running SmolLM2-135M entirely in CPU memory under 150MB RAM for complete privacy, zero cost, and offline edge resilience.",
  "starter_code": "# Module 13: 100% Offline Edge Inference with SmolLM2-135M (Under 150MB RAM!)\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\n# 1. Load SmolLM2-135M (The world's smallest viable modern instruct SLM)\nmodel_id = \"HuggingFaceTB/SmolLM2-135M-Instruct\"\ntokenizer = AutoTokenizer.from_pretrained(model_id)\nmodel = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32)\n\n# 2. Format Rapid-Fire Exam Revision Chat\nmessages = [\n    {\"role\": \"system\", \"content\": \"You are a concise exam crammer tutor. Turn complex concepts into 3 rapid bullet-point flashcards.\"},\n    {\"role\": \"user\", \"content\": \"Explain Backpropagation and Gradient Descent for tomorrow's final exam!\"}\n]\nprompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)\ninputs = tokenizer(prompt, return_tensors=\"pt\")\n\n# 3. Generate instant offline flashcards (< 1 second on low-end CPU)\nwith torch.no_grad():\n    outputs = model.generate(**inputs, max_new_tokens=140, temperature=0.5, do_sample=True)\n\nresponse = tokenizer.decode(outputs[0][inputs[\"input_ids\"].shape[1]:], skip_special_tokens=True)\nprint(\"=== 100% Offline Edge Flashcards (135M SLM) ===\")\nprint(response.strip())\n",
  "runnable_starter_code": "# Module 13: 100% Offline Edge Inference with SmolLM2-135M (Under 150MB RAM!)\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\n# 1. Load SmolLM2-135M (The world's smallest viable modern instruct SLM)\nmodel_id = \"HuggingFaceTB/SmolLM2-135M-Instruct\"\ntokenizer = AutoTokenizer.from_pretrained(model_id)\nmodel = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32)\n\n# 2. Format Rapid-Fire Exam Revision Chat\nmessages = [\n    {\"role\": \"system\", \"content\": \"You are a concise exam crammer tutor. Turn complex concepts into 3 rapid bullet-point flashcards.\"},\n    {\"role\": \"user\", \"content\": \"Explain Backpropagation and Gradient Descent for tomorrow's final exam!\"}\n]\nprompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)\ninputs = tokenizer(prompt, return_tensors=\"pt\")\n\n# 3. Generate instant offline flashcards (< 1 second on low-end CPU)\nwith torch.no_grad():\n    outputs = model.generate(**inputs, max_new_tokens=140, temperature=0.5, do_sample=True)\n\nresponse = tokenizer.decode(outputs[0][inputs[\"input_ids\"].shape[1]:], skip_special_tokens=True)\nprint(\"=== 100% Offline Edge Flashcards (135M SLM) ===\")\nprint(response.strip())\n",
  "gradio_code": "import gradio as gr\nfrom transformers import pipeline\n\ncrammer = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-135M-Instruct\")\n\ndef generate_flashcards(exam_topic):\n    chat = [{\"role\": \"system\", \"content\": \"You are an offline exam study coach. Write 3 quick flashcards.\"}, {\"role\": \"user\", \"content\": f\"Topic: {exam_topic}\"}]\n    prompt = crammer.tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)\n    out = crammer(prompt, max_new_tokens=120, temperature=0.4)\n    return out[0][\"generated_text\"][len(prompt):].strip()\n\ndemo = gr.Interface(fn=generate_flashcards, inputs=gr.Textbox(value=\"Operating Systems Deadlocks\"), outputs=gr.Textbox(lines=6), title=\"Offline Edge Exam Crammer (135M SLM)\")\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr\nfrom transformers import pipeline\n\ncrammer = pipeline(\"text-generation\", model=\"HuggingFaceTB/SmolLM2-135M-Instruct\")\n\ndef generate_flashcards(exam_topic):\n    chat = [{\"role\": \"system\", \"content\": \"You are an offline exam study coach. Write 3 quick flashcards.\"}, {\"role\": \"user\", \"content\": f\"Topic: {exam_topic}\"}]\n    prompt = crammer.tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)\n    out = crammer(prompt, max_new_tokens=120, temperature=0.4)\n    return out[0][\"generated_text\"][len(prompt):].strip()\n\ndemo = gr.Interface(fn=generate_flashcards, inputs=gr.Textbox(value=\"Operating Systems Deadlocks\"), outputs=gr.Textbox(lines=6), title=\"Offline Edge Exam Crammer (135M SLM)\")\ndemo.launch()\n"
},
	14: {
  "module_number": 14,
  "module_slug": "enterprise-capstone-and-career-launch",
  "project_title": "Global AI Micro-SaaS Capstone Defense",
  "project_slug": "global-ai-microsaas-capstone",
  "hf_model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
  "hf_model_url": "https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
  "hf_dataset": "open-thoughts/OpenThoughts-114k",
  "hf_dataset_url": "https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k",
  "colab_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_14_enterprise_capstone.ipynb",
  "colab_notebook_url": "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_14_enterprise_capstone.ipynb",
  "kaggle_url": "https://www.kaggle.com/code/isaim0011/module-14-enterprise-microsaas-capstone",
  "kaggle_notebook_url": "https://www.kaggle.com/code/isaim0011/module-14-enterprise-microsaas-capstone",
  "hardware_requirement": "Free Colab T4 GPU (3.2 GB VRAM) / Free Kaggle Dual-T4",
  "estimated_runtime_seconds": "< 35s load, full enterprise multi-tenant simulation",
  "key_learning_takeaway": "Architecting a multi-tenant enterprise AI system: combining SOTA reasoning models (DeepSeek-R1), strict latency SLAs, production telemetry, and interactive Gradio 5 showcase.",
  "starter_code": "# Module 14: Full-Stack Micro-SaaS AI Core with SOTA Reasoning & Telemetry\nimport time\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\n# 1. Load DeepSeek-R1 Distill Qwen-1.5B SOTA Open-Weight Reasoning Engine\nmodel_id = \"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B\"\ndevice = \"cuda\" if torch.cuda.is_available() else \"cpu\"\ntokenizer = AutoTokenizer.from_pretrained(model_id)\nmodel = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32).to(device)\n\n# 2. Production Multi-Tenant Request Simulator with Audit Telemetry\ndef serve_enterprise_tenant(tenant_id: str, business_problem: str):\n    prompt = f\"<system>You are a CTO Enterprise AI Strategist.</system><user>Analyze this business case and propose technical architecture: {business_problem}</user>\"\n    inputs = tokenizer(prompt, return_tensors=\"pt\").to(device)\n    \n    t0 = time.perf_counter()\n    with torch.no_grad():\n        outputs = model.generate(**inputs, max_new_tokens=150, temperature=0.6, do_sample=True)\n    latency = time.perf_counter() - t0\n    \n    response = tokenizer.decode(outputs[0][inputs[\"input_ids\"].shape[1]:], skip_special_tokens=True)\n    tokens_generated = outputs.shape[1] - inputs[\"input_ids\"].shape[1]\n    \n    return {\n        \"tenant_id\": tenant_id,\n        \"tokens_per_sec\": round(tokens_generated / latency, 1),\n        \"total_latency_sec\": round(latency, 3),\n        \"ai_architecture_proposal\": response.strip()\n    }\n\ntelemetry = serve_enterprise_tenant(\"tenant_fintech_001\", \"Design high-scale automated fraud detection API handling 10,000 req/sec\")\nprint(f\"=== Enterprise Tenant {telemetry['tenant_id']} ===\")\nprint(f\"Telemetry: {telemetry['tokens_per_sec']} tok/sec | Latency: {telemetry['total_latency_sec']}s\")\nprint(f\"\\nArchitecture Defense:\\n{telemetry['ai_architecture_proposal']}\")\n",
  "runnable_starter_code": "# Module 14: Full-Stack Micro-SaaS AI Core with SOTA Reasoning & Telemetry\nimport time\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\n# 1. Load DeepSeek-R1 Distill Qwen-1.5B SOTA Open-Weight Reasoning Engine\nmodel_id = \"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B\"\ndevice = \"cuda\" if torch.cuda.is_available() else \"cpu\"\ntokenizer = AutoTokenizer.from_pretrained(model_id)\nmodel = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32).to(device)\n\n# 2. Production Multi-Tenant Request Simulator with Audit Telemetry\ndef serve_enterprise_tenant(tenant_id: str, business_problem: str):\n    prompt = f\"<system>You are a CTO Enterprise AI Strategist.</system><user>Analyze this business case and propose technical architecture: {business_problem}</user>\"\n    inputs = tokenizer(prompt, return_tensors=\"pt\").to(device)\n    \n    t0 = time.perf_counter()\n    with torch.no_grad():\n        outputs = model.generate(**inputs, max_new_tokens=150, temperature=0.6, do_sample=True)\n    latency = time.perf_counter() - t0\n    \n    response = tokenizer.decode(outputs[0][inputs[\"input_ids\"].shape[1]:], skip_special_tokens=True)\n    tokens_generated = outputs.shape[1] - inputs[\"input_ids\"].shape[1]\n    \n    return {\n        \"tenant_id\": tenant_id,\n        \"tokens_per_sec\": round(tokens_generated / latency, 1),\n        \"total_latency_sec\": round(latency, 3),\n        \"ai_architecture_proposal\": response.strip()\n    }\n\ntelemetry = serve_enterprise_tenant(\"tenant_fintech_001\", \"Design high-scale automated fraud detection API handling 10,000 req/sec\")\nprint(f\"=== Enterprise Tenant {telemetry['tenant_id']} ===\")\nprint(f\"Telemetry: {telemetry['tokens_per_sec']} tok/sec | Latency: {telemetry['total_latency_sec']}s\")\nprint(f\"\\nArchitecture Defense:\\n{telemetry['ai_architecture_proposal']}\")\n",
  "gradio_code": "import gradio as gr, time\nfrom transformers import pipeline\n\nsaas_core = pipeline(\"text-generation\", model=\"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B\")\n\ndef enterprise_advisor(client_org, problem_statement):\n    t0 = time.perf_counter()\n    prompt = f\"Client: {client_org}\\nChallenge: {problem_statement}\\nExecutive Solution:\"\n    out = saas_core(prompt, max_new_tokens=120, temperature=0.6, do_sample=True)\n    t = time.perf_counter() - t0\n    return out[0][\"generated_text\"][len(prompt):].strip(), f\"Processed in {t:.2f}s (Enterprise SLA: <3.0s)\"\n\ndemo = gr.Interface(\n    fn=enterprise_advisor,\n    inputs=[gr.Textbox(label=\"Client Organization\", value=\"HBL Digital Banking\"), gr.Textbox(label=\"Enterprise Challenge\", value=\"Automate loan document underwriting\")],\n    outputs=[gr.Textbox(label=\"Strategic Solution\"), gr.Textbox(label=\"Telemetry Audit\")],\n    title=\"Enterprise AI Micro-SaaS Capstone Portal\"\n)\ndemo.launch()\n",
  "gradio_demo_code": "import gradio as gr, time\nfrom transformers import pipeline\n\nsaas_core = pipeline(\"text-generation\", model=\"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B\")\n\ndef enterprise_advisor(client_org, problem_statement):\n    t0 = time.perf_counter()\n    prompt = f\"Client: {client_org}\\nChallenge: {problem_statement}\\nExecutive Solution:\"\n    out = saas_core(prompt, max_new_tokens=120, temperature=0.6, do_sample=True)\n    t = time.perf_counter() - t0\n    return out[0][\"generated_text\"][len(prompt):].strip(), f\"Processed in {t:.2f}s (Enterprise SLA: <3.0s)\"\n\ndemo = gr.Interface(\n    fn=enterprise_advisor,\n    inputs=[gr.Textbox(label=\"Client Organization\", value=\"HBL Digital Banking\"), gr.Textbox(label=\"Enterprise Challenge\", value=\"Automate loan document underwriting\")],\n    outputs=[gr.Textbox(label=\"Strategic Solution\"), gr.Textbox(label=\"Telemetry Audit\")],\n    title=\"Enterprise AI Micro-SaaS Capstone Portal\"\n)\ndemo.launch()\n"
},
};

export const MODULE_PRACTICE_PROJECTS: Record<string, PracticeProject> = {
	'0': {
		title: "Chai Dhaba Customer Sentiment & Order Billing Engine",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Combines Python dictionaries, OOP data structures, and Hugging Face pre-trained sentiment pipelines to analyze real-world consumer feedback with zero API costs.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_00_chai_dhaba_sentiment.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[0]
	},
	'1': {
		title: "Biryani vs Pulao Cosine Semantic Vectorizer",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "First-principles linear algebra in action: dense sentence embeddings, vector dot-products, Euclidean norms, and SIMD cosine similarity ranking with zero loop overhead.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_01_biryani_vector_math.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[1]
	},
	'2': {
		title: "SmolLM2 Rishta Matchmaker & Chain-of-Thought Evaluator",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Autoregressive next-token prediction dynamics, temperature sampling effects on creativity, system prompt steering, and Chain-of-Thought (CoT) reasoning.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_02_smollm2_prompt_eval.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[2]
	},
	'3': {
		title: "AG News Real-Time Topic & Clickbait Classifier",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Memory-efficient streaming of Hugging Face Hub datasets, TF-IDF n-gram feature extraction, Logistic Regression decision boundaries, and multi-class classification reporting.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_03_ag_news_classifier.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[3]
	},
	'4': {
		title: "PyTorch Autograd & MLP Sentiment Classifier from Scratch",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Building custom PyTorch nn.Module architectures from scratch, tensor batching, autograd backpropagation, AdamW parameter updates, and loss curve convergence.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_04_pytorch_mlp_classifier.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[4]
	},
	'5': {
		title: "Transformer Attention Matrix & Token Saliency Visualizer",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Deconstructing self-attention tensors: Query-Key dot products, softmax scaling, attention head routing, and token saliency visualization.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_05_attention_matrix.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[5]
	},
	'6': {
		title: "Ami Ka WhatsApp Auto-Responder & Streaming Bot",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Implementing asynchronous token streaming via TextIteratorStreamer, conversation state management, and real-time interactive chat interfaces.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_06_streaming_ai_bot.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[6]
	},
	'7': {
		title: "Grandma's Secret Biryani Recipe RAG Engine",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Building an end-to-end Retrieval-Augmented Generation (RAG) system with dense BGE embeddings, Top-K semantic similarity search, and hallucination-free generation.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_07_vector_rag_engine.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[7]
	},
	'8': {
		title: "Aggressive Salary Negotiation AI Agent Swarm",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Autonomous tool calling using Hugging Face smolagents CodeAgent: writing and executing Python calculations dynamically to solve multi-step problems.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_08_smolagents_tools.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[8]
	},
	'9': {
		title: "Roman Urdu Sarcasm & Roast LoRA Fine-Tuning Engine",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Parameter-Efficient Fine-Tuning (PEFT) mechanics: injecting low-rank decomposition matrices (LoRA) into attention projections and training with TRL SFTTrainer on free T4 hardware.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_09_lora_qlora_sft.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[9]
	},
	'10': {
		title: "Phuppo-Proof Family WhatsApp Content Guardrail Firewall",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Implementing programmatic AI safety guardrails: pre-generation toxicity filtering with Toxic-BERT, thresholding, and responsible AI system architecture.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_10_guardrails_safety.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[10]
	},
	'11': {
		title: "DeepSeek-R1 Sub-50ms Low-Latency Inference Benchmark",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Benchmarking inference throughput (tokens/sec), latency profiling, memory consumption telemetry, and comparing FP16 vs quantized execution on production open-weight models.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_11_production_benchmark.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[11]
	},
	'12': {
		title: "Doctor Prescription OCR & Audio Transcriber",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Multimodal AI orchestration: unifying Automatic Speech Recognition (Whisper) and image-to-text vision models (BLIP) with an LLM clinical summarizer.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_12_whisper_multimodal.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[12]
	},
	'13': {
		title: "100% Offline Exam Crammer & Flashcard Generator",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Edge Small Language Models (SLMs) execution: running SmolLM2-135M entirely in CPU memory under 150MB RAM for complete privacy, zero cost, and offline edge resilience.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_13_local_edge_slm.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[13]
	},
	'14': {
		title: "Global AI Micro-SaaS Capstone Defense",
		humorous_badge: "Hugging Face Lab",
		description_roman_urdu: "Architecting a multi-tenant enterprise AI system: combining SOTA reasoning models (DeepSeek-R1), strict latency SLAs, production telemetry, and interactive Gradio 5 showcase.",
		colab_url: "https://colab.research.google.com/github/isaim0011/ai-mastery-notebooks/blob/main/module_14_enterprise_capstone.ipynb",
		xp_reward: 200,
		checklist: [
			'Open 1-Click interactive notebook on Google Colab / Kaggle',
			'Load Hugging Face model & dataset in streaming mode',
			'Execute local test inference & benchmark token throughput',
			'Deploy interactive Gradio 5 web UI demo'
		],
		hf_subproject: HF_SUBPROJECTS[14]
	},
};

export function getHfSubproject(key: string | number): HfSubproject | undefined {
	const num = typeof key === 'number' ? key : parseInt(key, 10);
	if (!isNaN(num) && HF_SUBPROJECTS[num]) {
		return HF_SUBPROJECTS[num];
	}
	const str = String(key);
	for (const p of Object.values(HF_SUBPROJECTS)) {
		if (p.module_slug === str || str.includes(p.module_slug)) {
			return p;
		}
	}
	return undefined;
}

export function getPracticeProject(key: string | number): PracticeProject {
	const strKey = String(key);
	if (MODULE_PRACTICE_PROJECTS[strKey]) {
		return MODULE_PRACTICE_PROJECTS[strKey];
	}
	// Try slug matching
	for (const phase of FALLBACK_PHASES) {
		const mod = phase.modules.find((m) => m.slug === strKey || m.id === strKey || String(m.module_number) === strKey);
		if (mod && mod.practice_project) {
			const num = mod.module_number;
			return {
				...mod.practice_project,
				hf_subproject: HF_SUBPROJECTS[num]
			};
		}
	}
	const num = parseInt(strKey, 10);
	if (!isNaN(num) && MODULE_PRACTICE_PROJECTS[String(num)]) {
		return MODULE_PRACTICE_PROJECTS[String(num)];
	}
	return MODULE_PRACTICE_PROJECTS['0'];
}
