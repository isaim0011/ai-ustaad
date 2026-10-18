// Fallback syllabus and content for standalone deployment (ai-ustaad.pages.dev)
// Ensures 100% production-ready rich UI even if Supabase is offline or not configured.

export interface PracticeProject {
	title: string;
	humorous_badge: string;
	description_roman_urdu: string;
	colab_url: string;
	xp_reward: number;
	checklist: string[];
}

export interface ZeroGpuRecipe {
	platform: string;
	vram_required: string;
	estimated_cost: string;
	compute_units_tip: string;
	one_click_command: string;
	unassign_code: string;
}

export interface LessonData {
	id: string;
	module_id: string;
	lesson_code: string;
	slug: string;
	title: string;
	duration_minutes: number;
	lesson_type: string;
	roman_urdu_content: string;
	english_summary: string;
	code_example: string;
	xp_reward: number;
	order_index: number;
}

export interface ModuleData {
	id: string;
	phase_id?: string;
	module_number: number;
	slug: string;
	title: string;
	weeks_range: string;
	estimated_hours: number;
	real_world_deliverable: string;
	badge_slug?: string;
	order_index: number;
	diagram_script?: string;
	diagram_preset?: string;
	diagram_animation?: string;
	zero_gpu_recipe?: ZeroGpuRecipe;
	practice_project?: PracticeProject;
	learning_outcomes?: string[];
	practical_tasks?: string[];
	lessons?: LessonData[];
}

export interface PhaseData {
	id: string;
	phase_number: number;
	slug: string;
	title: string;
	weeks_range: string;
	level: string;
	description: string;
	order_index: number;
	modules: ModuleData[];
}

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
					humorous_badge: 'Dhabay Ka Pythoneer ☕',
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
    print("Complimentary saunf & elaichi included! ☕")`
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
					humorous_badge: 'Biryani Scientist 🍛',
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
					humorous_badge: 'Rishta Optimizer 💍',
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
					humorous_badge: 'PSL Analyst 🏏',
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
					humorous_badge: 'Meme Lord 🎭',
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
					humorous_badge: 'Nani Ammi Approved 📖',
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
					humorous_badge: 'Farmanbardar Beta 📱',
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
					humorous_badge: 'Tanz Specialist 🎯',
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
					humorous_badge: 'HR Negotiator 💼',
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
					humorous_badge: 'Shayar-e-AI ✍️',
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
					humorous_badge: 'Full-Stack Ustaad 🚀',
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

export const MODULE_PRACTICE_PROJECTS: Record<string, PracticeProject> = {
	'0': {
		title: 'Chai Dhaba Billing & Khata System',
		humorous_badge: 'Dhabay Ka Pythoneer ☕',
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
	'1': {
		title: 'Biryani vs Pulao Sentiment Analyzer',
		humorous_badge: 'Biryani Scientist 🍛',
		description_roman_urdu: 'Twitter/X aur food reviews dataset se Biryani vs Pulao ki sentimental jung analyze karein using fast vectorized NumPy operations.',
		colab_url: 'https://colab.research.google.com/#create=true',
		xp_reward: 175,
		checklist: [
			'Food review dataset tokenize karna (Karachi, Lahore & Rawalpindi reviews)',
			'NumPy vectorized bag-of-words frequency matrix banana',
			'Cosine similarity dot product se sentiment score calculate karna',
			'Biryani vs Pulao sentiment polarity leaderboard print karna'
		]
	},
	'2': {
		title: 'Rishta Matcher Algorithm',
		humorous_badge: 'Rishta Optimizer 💍',
		description_roman_urdu: 'Candidate bios aur mother-in-law (Ami) ki strict criteria ke darmiyan Cosine similarity vector distance calculate karein.',
		colab_url: 'https://colab.research.google.com/#create=true',
		xp_reward: 200,
		checklist: [
			'Candidate profiles ka feature vector banana (Chai making, Salary, Humor, Punctuality)',
			'Ami ka ideal candidate vector formulate karna',
			'High-dimensional normalized cosine distance compute karna',
			'Top-3 approved candidates ki leaderboard generate karna'
		]
	},
	'3': {
		title: 'Cricketer Performance Predictor',
		humorous_badge: 'PSL Analyst 🏏',
		description_roman_urdu: 'PSL / IPL match outcome aur player score predictor with LightGBM & regression.',
		colab_url: 'https://colab.research.google.com/#create=true',
		xp_reward: 200,
		checklist: [
			'Ball-by-ball match dataset load karna',
			'Pitch conditions & strike-rate momentum features engineer karna',
			'Custom neural net / gradient boosting model train karna',
			'Live match win-probability chart predict karna'
		]
	},
	'4': {
		title: 'Meme Classifier & Roast Bot',
		humorous_badge: 'Meme Lord 🎭',
		description_roman_urdu: 'PyTorch CNN jo spicy memes vs wholesome cat pictures classify kare aur automatically funny roasts generate kare.',
		colab_url: 'https://colab.research.google.com/#create=true',
		xp_reward: 225,
		checklist: [
			'Custom PyTorch Dataset & DataLoader likhna',
			'Convolutional + BatchNorm layers implement karna',
			'Classification evaluation metric evaluate karna',
			'Roast bot prompt loop attach karna'
		]
	},
	'5': {
		title: 'Biryani Recipe RAG with Exact Spices',
		humorous_badge: 'Nani Ammi Approved 📖',
		description_roman_urdu: 'Vector search system jo dadi/nani ki handwritten recipe book se exact page aur grams of aloo bukhara cite kare.',
		colab_url: 'https://colab.research.google.com/#create=true',
		xp_reward: 260,
		checklist: [
			'Recipe PDF parse karke text & tables extract karna',
			'pgvector HNSW index create karna',
			'BM25 sparse search aur dense embeddings fuse karna',
			'Exact source page and spice grams verify karke answer dena'
		]
	},
	'6': {
		title: 'Ami Ka WhatsApp Reply Bot',
		humorous_badge: 'Farmanbardar Beta 📱',
		description_roman_urdu: 'FastAPI streaming auto-responder for family groups with respectful polite excuses.',
		colab_url: 'https://colab.research.google.com/#create=true',
		xp_reward: 220,
		checklist: [
			'FastAPI async SSE endpoint banana',
			'Pakistani family respectful tone system prompt craft karna',
			'Tool call se calendar check karke legitimate excuses schedule karna',
			'Response streaming under 200ms latency maintain karna'
		]
	},
	'7': {
		title: 'Roman Urdu Sarcasm Detector',
		humorous_badge: 'Tanz Specialist 🎯',
		description_roman_urdu: 'Unsloth 4-bit fine-tuned LLaMA model on Colab Free T4 identifying sarcastic Pakistani tweets and irony.',
		colab_url: 'https://colab.research.google.com/#create=true',
		xp_reward: 300,
		checklist: [
			'Roman Urdu sarcasm dataset format karna (JSONL ShareGPT)',
			'Unsloth FastLanguageModel 4-bit quantization load karna',
			'LoRA adapter train karna on Free Colab T4 without out-of-memory',
			'Test suite se sarcasm accuracy benchmark karna'
		]
	},
	'8': {
		title: 'Salary Negotiation Agent',
		humorous_badge: 'HR Negotiator 💼',
		description_roman_urdu: 'smolagents & Anthropic MCP swarm drafting funny yet razor-sharp counter-offers to tech recruiters.',
		colab_url: 'https://colab.research.google.com/#create=true',
		xp_reward: 275,
		checklist: [
			'Multi-agent roleplay structure build karna',
			'Inflation & market compensation lookup tool add karna',
			'Professional counter-offer email generator implement karna',
			'Structured JSON evaluation run karna'
		]
	},
	'9': {
		title: 'Ghalib vs Iqbal Poetry Generator',
		humorous_badge: 'Shayar-e-AI ✍️',
		description_roman_urdu: 'Mini-GPT model serving classic Urdu poetry tokens in real-time via high-speed streaming gateway.',
		colab_url: 'https://colab.research.google.com/#create=true',
		xp_reward: 250,
		checklist: [
			'Classical Urdu poetry corpus tokenize karna',
			'Causal attention weights compute karna',
			'Rhyme scheme verification filter add karna',
			'Sub-millisecond token streaming benchmark karna'
		]
	},
	'10': {
		title: 'Biryani Delivery Routing Agent & High-Speed Gateway',
		humorous_badge: 'Full-Stack Ustaad 🚀',
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
};

export function getPracticeProject(key: string | number): PracticeProject {
	const strKey = String(key);
	if (MODULE_PRACTICE_PROJECTS[strKey]) {
		return MODULE_PRACTICE_PROJECTS[strKey];
	}
	// Try slug matching
	for (const phase of FALLBACK_PHASES) {
		const mod = phase.modules.find((m) => m.slug === strKey || m.id === strKey || String(m.module_number) === strKey);
		if (mod && mod.practice_project) {
			return mod.practice_project;
		}
	}
	return MODULE_PRACTICE_PROJECTS['0'];
}

