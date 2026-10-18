# module_08.py
# Module 8: Autonomous Agents, MCP & Tool Use (Anthropic MCP, smolagents)
# Lessons 8.1 to 8.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 8.1: ReAct Pattern: Reasoning + Acting Ka Mukammal Framework
# ==============================================================================
LESSON_CONTENT['8.1'] = r"""### Part 1: Mental Model & South Asian Analogy
Aam LLM sirf baatein kar sakta hai ("Lafzon ka sher"), lekin autonomous agent asal dunya mein kaam kar sakta hai ("Hathon ka karigar"). Agent internet se data dhoond sakta hai, database mein query chala sakta hai, email bhej sakta hai, aur code run kar sakta hai. Is azeem inqilab ka bunyadi framework **ReAct (Reasoning + Acting)** hai!
Isay samajhne ke liye kisi Mashhoor Mechanic aur Ustaad Chotu ki misaal lein:
1. Pure Reasoning (Khayali Pulao): Agar ustaad sirf sochta rahe aur haath se pana (wrench) na uthaye to gaari kabhi theek nahi ho sakti.
2. Pure Acting (Andha-Dhundh Pana Chalana): Agar chotu baghair soche samjhe har nut-bolt kholna shuru kar de to engine toot jata hai.
3. The ReAct Loop (Soch, Amal, Mushahida):
   - Step 1: Thought (Zehni Soch): "Gaari start nahi ho rahi. Pehle battery ka voltage check karna chahiye."
   - Step 2: Action (Auzaar Ka Istemaal / Tool Call): Chotu multimeter uthata hai aur battery ke terminals par lagata hai: `multimeter.measure_voltage()`.
   - Step 3: Observation (Nateeja / Reality Check): Multimeter screen par 12.6V (Normal voltage) dikhata hai.
   - Step 4: Next Thought (Agli Soch): "Battery theek hai! Iska matlab masla spark plug ya fuel pump mein hai."
   Jab tak masla hal nahi ho jata, yeh Thought $\to$ Action $\to$ Observation ka chakar lagataar chalta rehta hai jab tak aakhir mein Final Answer na nikal aaye!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein ReAct Loop ke Token Consumption aur Maximum Turn Termination ki math trace karte hain.
ReAct Agent Step Equations:
At iteration $t$:
- History Context: $H_t = [H_{t-1}, \text{Thought}_t, \text{Action}_t, \text{Observation}_t]$
- Token Footprint at step $t$: $K_t = K_{t-1} + \Delta_{\text{thought}} + \Delta_{\text{action}} + \Delta_{\text{observation}}$

Worked Scenario:
- Base Prompt + Tool Definitions = 600 tokens
- Average Thought length = 40 tokens
- Action Tool Call JSON = 30 tokens
- Tool Observation (e.g. SQL result or web search snippet) = 150 tokens
- Growth per turn: $\Delta = 40 + 30 + 150 = 220 \text{ tokens per turn}$.

Step-by-Step Cumulative Token Footprint:
- Turn 1: $600 + 220 = 820 \text{ tokens}$
- Turn 2: $820 + 220 = 1040 \text{ tokens}$
- Turn 3: $1040 + 220 = 1260 \text{ tokens}$
- Turn 4: $1260 + 220 = 1480 \text{ tokens}$

Infinite Loop Risk (Bina Break Ke Qad-e-Hayat):
Agar model galat parameter deta rahe aur tool baar baar error phenkay to model infinite loop mein ja sakta hai ($t \to \infty$).
Safety Invariant Rule:
$\text{If } t \ge T_{\text{max}} (5) \implies \text{Force Abort and return: 'Failed to resolve within allowed turns'}$.
Max Turns limit agent ko hazaron dollars ke API bill burn karne se bachata hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete ReAct Agent framework from scratch implement karte hain: Thought/Action parsing, deterministic tool dispatch, observation injection, aur infinite loop safety guards.

```python
import re
from typing import Dict, Callable, Any

# 1. Registered Tool Suite
def calculate_dhaba_tax(amount: float) -> str:
    \"\"\"Calculates exact 16% sales tax on order amount.\"\"\"
    tax = round(amount * 0.16, 2)
    return f"Calculated 16% GST: PKR {tax} (Total payable: PKR {round(amount + tax, 2)})"

def lookup_item_price(item_name: str) -> str:
    \"\"\"Returns menu price for dhaba item.\"\"\"
    menu = {"doodh_patti": 60.0, "paratha": 120.0, "samosa": 40.0}
    clean = item_name.strip().lower()
    if clean in menu:
        return f"Price of {clean} is PKR {menu[clean]}"
    return f"Item '{clean}' not found in menu."

TOOL_REGISTRY: Dict[str, Callable[..., str]] = {
    "calculate_dhaba_tax": calculate_dhaba_tax,
    "lookup_item_price": lookup_item_price
}

# 2. Production ReAct Execution Engine
class SimpleReActAgent:
    def __init__(self, max_turns: int = 5) -> None:
        self.max_turns = max_turns

    def run(self, user_query: str) -> str:
        scratchpad = f"User Query: {user_query}\\n"
        print(f"Starting ReAct Loop for Query: '{user_query}'\\n")

        for turn in range(1, self.max_turns + 1):
            print(f"--- Turn {turn}/{self.max_turns} ---")
            
            # Simulated LLM Step: Generates Thought and Action based on current scratchpad
            if turn == 1:
                thought = "I need to check the price of paratha first."
                action = "lookup_item_price('paratha')"
            elif turn == 2:
                thought = "Now I need to calculate the 16% tax on 120 PKR."
                action = "calculate_dhaba_tax(120.0)"
            else:
                thought = "I have all the information to answer the user."
                final_answer = "Paratha costs PKR 120 and with 16% tax the total is PKR 139.20."
                scratchpad += f"Thought: {thought}\\nFinal Answer: {final_answer}"
                return final_answer

            scratchpad += f"Thought: {thought}\\nAction: {action}\\n"
            print(f"  Thought: {thought}")
            print(f"  Action:  {action}")

            # Execute tool safely
            match = re.match(r"(\w+)\((.*)\)", action)
            if not match:
                observation = "Error: Invalid action syntax."
            else:
                tool_name, raw_args = match.group(1), match.group(2)
                if tool_name not in TOOL_REGISTRY:
                    observation = f"Error: Tool '{tool_name}' does not exist."
                else:
                    # Clean arg
                    arg_clean = raw_args.strip("'\" ")
                    func = TOOL_REGISTRY[tool_name]
                    # Parse numeric if needed
                    val = float(arg_clean) if arg_clean.replace('.', '', 1).isdigit() else arg_clean
                    observation = func(val)

            scratchpad += f"Observation: {observation}\\n"
            print(f"  Observation: {observation}\\n")

        return "Agent aborted: Maximum turn limit reached without resolution."

# Execution test
if __name__ == "__main__":
    agent = SimpleReActAgent(max_turns=4)
    result = agent.run("Paratha ki total cost tax ke sath kitni hai?")
    print("Final Agent Response:", result)
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Unbounded Tool Execution Loop (Infinite Financial Drain): Agar agent kisi tool ke syntax error par phans jaye aur bar bar wahi ghalat call karta rahe to $T_{\text{max}}$ ke baghair hazaron API calls execute ho jati hain. Hamesha strict `max_turns=5` ya `10` enforce karein.
2. Passing Unsanitized Tool Outputs Directly to Model: Agar external tool 50,000 characters ka raw HTML dump return kar de to context window foran overflow ho jati hai. Tool output ko hamesha truncate aur summarize karein.
3. Lack of Error Recovery in Action Parsing: Agar model action format mein single quotes ki jagah extra space daal de aur regex crash kar jaye to poora agent collapse ho jata hai. Hamesha graceful error observation inject karein taake model apni ghalti theek kar sake.

Zero-GPU Tip:
ReAct agent loop, tool registration, regex parsing, aur state management 100% CPU bound string operations hain. Chote fast models (jaise LLaMA-3.3-70B on Groq ya Gemini 2.0 Flash) ke sath aap apne laptop par zero GPU compute kharch kiye pure autonomous agents chala sakte hain.

Self-Check Questions:
1. ReAct pattern mein 'Thought', 'Action', aur 'Observation' ka aapas mein kya talluq hota hai?
2. Maximum Turn Limit ($T_{\text{max}}$) agent architecture mein kyun ek critical safety invariant hai?
3. Tool execution fail hone par agent ko crash karne ke bajaye 'Error Observation' wapas bhejna kyun zaroori hai?

What to Build Next:
Ek ReAct Agent banayein jo ek Calculator Tool aur ek Wikipedia Search Tool use karke kisi shakhsiyat ki pedaish ka saal dhoond kar uski mojooda umar calculate kare."""

# ==============================================================================
# LESSON 8.2: 2026 Standard: Anthropic Model Context Protocol (MCP) Deep Dive
# ==============================================================================
LESSON_CONTENT['8.2'] = r"""### Part 1: Mental Model & South Asian Analogy
Pichle saalon mein har company (OpenAI, LangChain, LlamaIndex) apna alag custom tool format banati thi. Nateeja yeh tha ke agar aapne ek database connector banaya to woh doosre platform par nahi chalta tha. 2026 mein dunya ek azeem universal standard par muttahid ho chuki hai: **Anthropic Model Context Protocol (MCP)**!
Isay samajhne ke liye kisi Universal USB-C Port aur Charger ki misaal lein:
1. The Old Chaos (20 Mukhtalif Mobile Pin Chargers): 10 saal pehle har mobile ka alag charger hota tha: Nokia ki bareek pin, Samsung ka alag pin, Sony ka alag dabba. Agar charger kho jaye to dukan dukan dhoondna parta tha.
2. The MCP Standard (Universal Type-C Cable): MCP artificial intelligence ka Universal Type-C Port hai! Chahe aapka AI client Claude ho, ChatGPT ho, open-source LLaMA ho, ya VS Code extension ho; aur doosri taraf chahe Postgres database ho, GitHub repository ho, ya Slack ho — dono ke darmiyan sirf ek standard MCP cable lagti hai!
3. Three Core Primitives of MCP:
   - Resources (Dastawaizat / Files): Client server se data read karta hai (jaise `file:///logs/app.log` ya `postgres://schema`).
   - Tools (Af'aal / Functions): Model actions execute karta hai (jaise `run_sql_query`, `create_github_issue`).
   - Prompts (Templates): Reusable standardized workflows.
4. JSON-RPC 2.0 Architecture: MCP client aur server ke darmiyan standard lightweight JSON-RPC 2.0 messages chalte hain jo standard input/output (stdio) ya Server-Sent Events (SSE) par safar karte hain.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein MCP JSON-RPC 2.0 Protocol ke Request/Response Framing ka exact hisab trace karte hain.
Protocol Specifications:
Har message ek structured JSON object hota hai with strict keys:
- `jsonrpc`: Must be exactly `"2.0"`
- `id`: Unique integer or string matching request to response
- `method`: Action identifier (e.g. `"tools/list"`, `"tools/call"`)
- `params`: Arguments dictionary

Step 1: Client sends `tools/call` Request Frame
```json
{
  "jsonrpc": "2.0",
  "id": 101,
  "method": "tools/call",
  "params": {
    "name": "query_dhaba_sales",
    "arguments": {"category": "chai", "min_amount": 500}
  }
}
```
Payload size $\approx 180 \text{ Bytes}$.

Step 2: Server Executes Function & Emits `tools/call` Response Frame
```json
{
  "jsonrpc": "2.0",
  "id": 101,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Found 14 orders in 'chai' category exceeding 500 PKR. Total: 12,400 PKR."
      }
    ],
    "isError": false
  }
}
```

Step 3: Verification Math
Client checks:
- Does response `id` (101) match outstanding request `id` (101)? YES.
- Is `isError` true? NO.
- Extract `content[0].text` and inject directly into LLM observation stream!
Standardized JSON-RPC protocol kisi bhi programming language (Python, TypeScript, Rust, Go) ke darmiyan 100% interoperable tool connection faraham karta hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete Model Context Protocol (MCP) compliant server handler implement karte hain: tool discovery, JSON-RPC schema dispatch, aur structured response packaging.

```python
import json
from typing import Dict, Any, List

# 1. Define Standard MCP Tool Specifications
MCP_TOOLS_CATALOG: List[Dict[str, Any]] = [
    {
        "name": "get_dhaba_inventory",
        "description": "Returns current stock count for ingredients like milk, tea leaves, and sugar.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "item_name": {"type": "string", "description": "Ingredient identifier"}
            },
            "required": ["item_name"]
        }
    }
]

# 2. Local Backend Tool Logic
def handle_inventory_lookup(item_name: str) -> str:
    inventory = {"milk": "45 Liters", "patti": "12 Kilograms", "sugar": "30 Kilograms"}
    clean = item_name.strip().lower()
    return inventory.get(clean, f"Stock item '{clean}' not found in inventory registry.")

# 3. Production MCP JSON-RPC 2.0 Dispatcher
class MockMCPServer:
    def __init__(self) -> None:
        pass

    def handle_json_rpc_request(self, raw_json_message: str) -> str:
        try:
            req = json.loads(raw_json_message)
        except json.JSONDecodeError as err:
            return json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}})

        req_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})

        # Route 1: Tool Discovery
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"tools": MCP_TOOLS_CATALOG}
            })

        # Route 2: Tool Execution
        elif method == "tools/call":
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})

            if tool_name == "get_dhaba_inventory":
                item = tool_args.get("item_name", "")
                result_text = handle_inventory_lookup(item)
                return json.dumps({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": result_text}],
                        "isError": False
                    }
                })
            else:
                return json.dumps({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32601, "message": f"Tool '{tool_name}' not found"}
                })

        return json.dumps({"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}})

# Execution test
if __name__ == "__main__":
    server = MockMCPServer()

    # 1. Discover tools
    disc_req = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list"})
    disc_res = json.loads(server.handle_json_rpc_request(disc_req))
    print(f"MCP Tool Discovery: Found {len(disc_res['result']['tools'])} tools.")
    print("Discovered Tool:", disc_res["result"]["tools"][0]["name"])

    # 2. Execute tool via JSON-RPC
    call_req = json.dumps({
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {"name": "get_dhaba_inventory", "arguments": {"item_name": "patti"}}
    })
    call_res = json.loads(server.handle_json_rpc_request(call_req))
    print("\\nMCP Tool Execution Result:")
    print("Observation Content:", call_res["result"]["content"][0]["text"])
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Deviating from JSON-RPC 2.0 Error Codes: Standard JSON-RPC specifications mein fixed error codes hote hain (jaise `-32601` for method not found, `-32700` for parse error). Custom error numbers use karne se MCP clients (jaise Claude Desktop) tool crash report kar dete hain.
2. Blocking Stdio Streams with Unformatted Print Statements: MCP stdio mode mein chalta hai jahan stdout sirf aur sirf JSON-RPC messages ke liye makhsoos hota hai. Agar aap code mein `print("debugging...")` likh dein to client ka JSON parser foran crash ho jata hai. Logs hamesha `sys.stderr` par likhein!
3. Missing Tool InputSchema Validation: Agar client galat parameters bhej de aur tool schema validate na kare to python runtime error crash kar deta hai.

Zero-GPU Tip:
MCP server aur client pure communication protocols hain jo CPU par chalte hain. Aap apne laptop par local MCP servers (jaise SQLite MCP ya File System MCP) likh kar Claude Desktop ya open-source models ke sath connect kar sakte hain with zero GPU hardware.

Self-Check Questions:
1. Model Context Protocol (MCP) ke teen core primitives (Resources, Tools, Prompts) kya hain?
2. MCP standard mein JSON-RPC 2.0 transport protocol kyun use kiya jata hai?
3. Stdio transport mode mein debug logging stdout ke bajaye stderr par kyun karni chahiye?

What to Build Next:
Ek Local SQLite MCP Server banayein jo `tools/list` par database tables expose kare, `read_query` tool execute kare, aur standard MCP JSON-RPC format mein result return kare."""

# ==============================================================================
# LESSON 8.3: HuggingFace smolagents: Code-First Agents & Sandboxing
# ==============================================================================
LESSON_CONTENT['8.3'] = r"""### Part 1: Mental Model & South Asian Analogy
Pichle tamam agent frameworks (jaise standard LangChain ya AutoGen) actions ke liye JSON schemas use karte the: `{"action": "search", "query": "..."}`. Lekin 2026 mein HuggingFace ne ek azeem tehqeeq pesh ki: **LLMs JSON ke muqablay Python Code likhne mein 10x zyada taqatwar aur natural hain!** Yahan paida hua **smolagents (Code-First Agents)**!
Isay samajhne ke liye kisi Account Office ke Form vs Python Script ki misaal lein:
1. JSON Actions (Sarkari Form Ka Azaab): Agar aapko 50 alag alag logon ka hisab nikalna ho aur har dafa ek naya JSON form bharna paray: Form 1 submit karo, response aane ka intezar karo, Form 2 submit karo ($O(N)$ HTTP Round-trips).
2. Code-First Agents (Pure Python Script Likhnay Wala Chotu): Code agent se aap kehte hain: "Tamam dhabon ka data collect karke unka average nikaal kar graph banao." Model JSON nahi likhta! Model seedha ek chota sa Python code block likhta hai:
   ```python
   orders = [fetch_order(i) for i in range(50)]
   total = sum(o.price for o in orders if o.category == 'chai')
   print(f"Total: {total}")
   ```
   Ek hi single execution step mein poori loop, filtering, aur math execute ho jati hai!
3. The Danger (Aag Se Khelna / Code Injection): Agar model achanak likh de `import os; os.system('rm -rf /')` to poora server urr sakta hai!
4. Sandboxing (Bulletproof Kanch Ka Kamra): smolagents ek restricted Abstract Syntax Tree (AST) Python interpreter chalata hai jo kisi bhi dangerous module (`os`, `sys`, `subprocess`, file writing) ko execute karne ki ijazat nahi deta. Code kanch ke safe kamray mein chalta hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein JSON Tool Calls vs Code Action Latency aur Token Roundtrips ka exact hisab lagayein.
Task:
Search for prices of 5 items, filter items $> 50 \text{ PKR}$, compute total with 16% tax.

Scenario A: Standard JSON ReAct Tool Calls
- Turn 1: Call item 1 $\to$ Observation 1 (Roundtrip 1)
- Turn 2: Call item 2 $\to$ Observation 2 (Roundtrip 2)
- Turn 3: Call item 3 $\to$ Observation 3 (Roundtrip 3)
- Turn 4: Call item 4 $\to$ Observation 4 (Roundtrip 4)
- Turn 5: Call item 5 $\to$ Observation 5 (Roundtrip 5)
- Turn 6: Call tax calculation tool $\to$ Observation 6 (Roundtrip 6)
- Turn 7: Final Answer.
Total LLM API Calls = 7 calls!
Total Latency $= 7 \times 1.5\text{s} = 10.5 \text{ seconds}$.
Total Tokens $= 7 \times 800 \approx 5,600 \text{ tokens}$.

Scenario B: smolagents Code-First Execution
Model generates single Python snippet:
```python
prices = [get_price(item) for item in ["chai", "paratha", "lassi", "bun", "tea"]]
valid = [p for p in prices if p > 50]
final_total = sum(valid) * 1.16
print(f"Grand Total: {final_total}")
```
Single execution in local sandboxed interpreter:
- Total LLM API Calls = 1 call!
- Total Latency $= 1.5\text{s} + 0.01\text{s (Python execution)} = 1.51 \text{ seconds}$.
- Total Tokens $= 600 \text{ tokens}$.
Performance Gain:
$7.0\times \text{ Faster Execution}$ aur $9.3\times \text{ Cheaper Token Cost}$! Yahi Code-First agents ka inqilab hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum AST-based Secure Sandboxed Python Code Executor implement karte hain jo safe operations allow karta hai aur dangerous system imports ko block karta hai.

```python
import ast
from typing import Dict, Any

class SafeSandboxExecutor:
    \"\"\"Restricted AST-based Python executor preventing unauthorized OS calls.\"\"\"
    # Strictly prohibited AST nodes and module imports
    FORBIDDEN_NODES = {ast.Import, ast.ImportFrom}
    FORBIDDEN_NAMES = {"os", "sys", "subprocess", "eval", "exec", "open", "__import__"}

    def __init__(self, allowed_tools: Dict[str, Any]) -> None:
        self.scope = {
            "__builtins__": {
                "print": print, "range": range, "len": len, 
                "sum": sum, "min": min, "max": max, "round": round
            }
        }
        # Inject safe callable tools into execution environment
        self.scope.update(allowed_tools)

    def validate_ast(self, tree: ast.AST) -> None:
        for node in ast.walk(tree):
            if type(node) in self.FORBIDDEN_NODES:
                raise SecurityError("Imports are strictly forbidden in safe agent sandbox.")
            if isinstance(node, ast.Name) and node.id in self.FORBIDDEN_NAMES:
                raise SecurityError(f"Access to dangerous symbol '{node.id}' is blocked.")

    def execute_code(self, code_str: str) -> str:
        try:
            tree = ast.parse(code_str)
            self.validate_ast(tree)
            # Compile and execute within strictly bounded scope
            compiled_bytecode = compile(tree, filename="<agent_sandbox>", mode="exec")
            exec(compiled_bytecode, self.scope)
            return "Execution completed successfully."
        except Exception as exc:
            return f"Execution Error: {exc}"

# Execution test
if __name__ == "__main__":
    # Allowed tools in sandbox
    def fetch_menu_price(item: str) -> float:
        prices = {"doodh_patti": 60.0, "paratha": 120.0, "samosa": 40.0}
        return prices.get(item.lower(), 0.0)

    sandbox = SafeSandboxExecutor(allowed_tools={"get_price": fetch_menu_price})

    # Test Case 1: Legitimate Agent Multi-Step Code Action
    valid_code = \"\"\"
items = ['doodh_patti', 'paratha', 'samosa']
costs = [get_price(it) for it in items]
total_bill = round(sum(costs) * 1.16, 2)
print(f"Sandboxed Computed Total Bill with GST: PKR {total_bill}")
\"\"\"
    print("Testing Legitimate Code Action:")
    res1 = sandbox.execute_code(valid_code)
    print("Status:", res1)

    # Test Case 2: Malicious Code Action Injection
    malicious_code = \"\"\"
import os
os.system('echo Hacked!')
\"\"\"
    print("\\nTesting Malicious Injection:")
    res2 = sandbox.execute_code(malicious_code)
    print("Firewall Interception:", res2)
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Using Naive `exec(code)` Without AST Validation: Baghair sandbox ke raw `exec()` chalana server par direct Remote Code Execution (RCE) vulnerability banata hai jahan koi bhi prompt injection server ka sara data chura sakti hai.
2. Incomplete Builtins Sanitization: Agar aap `__builtins__` ko restrict na karein to attacker `__builtins__.__import__('os').system('...')` ke zariye AST check ko bypass kar sakta hai. Hamesha `__builtins__` ko explicit safe dictionary se replace karein.
3. Infinite While Loops in Agent Code: Agar agent `while True:` likh de to worker thread freeze ho jati hai. Hamesha execution timeout (e.g. 2 seconds via `signal` ya subprocess worker) enforce karein.

Zero-GPU Tip:
Code-first execution pure Python interpreter logic hai. Hugging Face `smolagents` local CPU par microsecond speed se sandboxed code chalata hai, jisse multi-turn agent latency 80% ghir jati hai.

Self-Check Questions:
1. Code-First Agents (jaise smolagents) traditional JSON Tool-Calling agents ke muqablay API round-trips kaise kam karte hain?
2. AST (Abstract Syntax Tree) validation dangerous code ko execute hone se pehle kaise intercept karti hai?
3. Sandboxed execution environment mein `__builtins__` ko restrict karna kyun lazmi hota hai?

What to Build Next:
Ek Smolagent Runner banayein jo DuckDuckGo Search tool aur Python Math tool use kare, user ke multi-step puzzle ko single python script mein solve kare, aur result print kare."""

# ==============================================================================
# LESSON 8.4: Function Calling Specifications & Runtime Schema Validation
# ==============================================================================
LESSON_CONTENT['8.4'] = r"""### Part 1: Mental Model & South Asian Analogy
OpenAI, Gemini, aur Anthropic models jab kisi external function ko call karte hain, to woh magic se code nahi chalate; woh ek sakht **JSON Schema Specification** ke mutabiq function ka naam aur arguments emit karte hain.
Isay samajhne ke liye kisi Passport Office ke Form aur Verification Khirki ki misaal lein:
1. The Tool Specification (Sarkari Form Ka Khali Khaka): Form par pehle se likha hota hai: "Pura Naam (String, 3 se 50 haroof), CNIC Number (Exact 13 digits), Umeedwar ki Umar (Integer, 18 se 100)". Yeh JSON Schema specification hai jo hum API call ke waqt model ko dete hain.
2. The Model's Prediction (Umeedwar Ka Bhara Hua Form): Model form ke khano ko dekh kar unme data bharta hai: `{"name": "Muhammad Ali", "cnic": "4210112345671", "age": 28}`.
3. Runtime Schema Validation (Verification Officer Ki Mohar): Khirki par baitha afsar (Pydantic / JSON Schema Validator) form ko check karta hai:
   - Kya koi lazmi khana khali to nahi chhoota?
   - Kya umar ki jagah string to nahi likh di?
   Agar sab theek ho to woh mohar laga kar function execute kar deta hai. Agar form mein ghalti ho to woh form wapas munh par phenkta hai (Validation Error) aur model dobara theek karke bhejta hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein JSON Schema Invariant Validation ka logic trace karte hain.
Schema Specification for Tool: `book_dhaba_table`
Properties:
1. `table_id`: Type integer, minimum 1, maximum 20.
2. `guest_count`: Type integer, minimum 1, maximum 8.
3. `customer_phone`: Type string, pattern `^03[0-9]{9}$` (Pakistani mobile format: 11 digits starting with 03).
Required fields: `["table_id", "guest_count", "customer_phone"]`.

Incoming Model Function Call Payloads:
Payload A:
`{"table_id": 4, "guest_count": 5, "customer_phone": "03001234567"}`
Validation Checks:
- `table_id = 4`: $1 \le 4 \le 20$ -> PASS.
- `guest_count = 5`: $1 \le 5 \le 8$ -> PASS.
- `customer_phone = "03001234567"`: Matches regex `^03[0-9]{9}$` (Exact 11 digits) -> PASS.
Result: Schema Validated! Dispatch to database.

Payload B (Model Hallucination / Corruption):
`{"table_id": 25, "guest_count": 0, "customer_phone": "phone_num"}`
Validation Checks:
- `table_id = 25`: $25 > 20$ -> FAIL (Table ID out of bounds).
- `guest_count = 0`: $0 < 1$ -> FAIL (At least 1 guest required).
- `customer_phone = "phone_num"`: Regex match failed -> FAIL.
Error Packet sent back to model:
`"Error: table_id exceeds max (20), guest_count below min (1), phone format invalid."`
Model pichli ghalti parh kar foran corrected arguments ke sath agla tool call bhejta hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Pydantic V2 use karke automatic OpenAI/Gemini tool declaration schema generation, incoming argument validation, aur error repair loop implement karte hain.

```python
import json
import re
from typing import Dict, Any, Type
from pydantic import BaseModel, Field, ValidationError

# 1. Define Production Tool Arguments Schema with Pydantic V2
class BookTableArgs(BaseModel):
    table_id: int = Field(ge=1, le=20, description="Dhaba table number from 1 to 20")
    guest_count: int = Field(ge=1, le=8, description="Number of seating guests")
    customer_phone: str = Field(description="Pakistani mobile phone starting with 03 (11 digits)")

    def validate_phone(self) -> None:
        if not re.match(r"^03\d{9}$", self.customer_phone):
            raise ValueError(f"Invalid Pakistani phone format: '{self.customer_phone}'. Expected format: 03XXXXXXXXX")

# 2. Export Standard OpenAI Tool Specification
def generate_tool_spec(model_cls: Type[BaseModel], name: str, description: str) -> Dict[str, Any]:
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": model_cls.model_json_schema()
        }
    }

# 3. Runtime Dispatcher with Schema Guard
def execute_table_booking(raw_args_json: str) -> Dict[str, Any]:
    try:
        args_dict = json.loads(raw_args_json)
        # Enforce strict Pydantic validation
        validated_args = BookTableArgs.model_validate(args_dict)
        validated_args.validate_phone()
        
        # Simulated database booking action
        return {
            "status": "success",
            "message": f"Table #{validated_args.table_id} confirmed for {validated_args.guest_count} guests. Confirmation SMS sent to {validated_args.customer_phone}."
        }
    except (json.JSONDecodeError, ValidationError, ValueError) as err:
        return {
            "status": "error",
            "error_type": "SchemaValidationError",
            "feedback_to_model": str(err)
        }

# Execution test
if __name__ == "__main__":
    spec = generate_tool_spec(BookTableArgs, "book_dhaba_table", "Books a table at the dhaba with customer mobile.")
    print("Exported OpenAI Tool Specification:")
    print(json.dumps(spec, indent=2))

    # Test valid execution
    valid_call = '{"table_id": 5, "guest_count": 4, "customer_phone": "03123456789"}'
    res_valid = execute_table_booking(valid_call)
    print(f"\\nValid Call Dispatch:\\n  {res_valid}")

    # Test invalid execution
    invalid_call = '{"table_id": 99, "guest_count": 0, "customer_phone": "12345"}'
    res_invalid = execute_table_booking(invalid_call)
    print(f"\\nInvalid Call Trapped:\\n  {res_invalid}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Assuming Model Always Emits Valid JSON: Model aksar trailing commas `{"a": 1,}` ya unquoted keys emit kar deta hai. Agar parser bina `try/except` ke ho to poori application crash ho jati hai. Hamesha robust error handling lagayein.
2. Vague Tool Descriptions in JSON Schema: Agar schema mein tool description sirf "books table" likha ho to model ko samajh nahi aati ke kab call karna hai. Description hamesha wazeh aur misalon ke sath likhein ("Call this tool when the user explicitly requests to reserve seating at the dhaba").
3. Too Many Tools in Single API Call (Attention Confusion): Model ko 50 tools ek sath de dene se model confuse ho jata hai aur ghalat tool select kar leta hai. Hamesha relevant tools ko dynamically filter karke sirf 3 se 5 tools pass karein.

Zero-GPU Tip:
Tool schema export aur Pydantic argument validation pure CPU par microsecond speed se chalti hai. Local automated testing mein model ke mock JSON payloads pass karke boundary values verify karein.

Self-Check Questions:
1. Pydantic schema se JSON Schema generate karne ka kya faida hota hai?
2. Schema validation fail hone par error feedback model ko wapas bhejne se self-correction kaise trigger hoti hai?
3. Tool definition mein parameter descriptions (`Field(description="...")`) model ki accuracy ko kaise barhate hain?

What to Build Next:
Ek Multi-Tool Schema Registry banayein jo 5 mukhtalif tools (Order, Cancel, Refund, CheckStatus, ApplyDiscount) ke schemas manage kare aur incoming model tool-call ko unke respective Pydantic validators par route kare."""

# ==============================================================================
# LESSON 8.5: Stateful Multi-Agent Cyclic Graphs with LangGraph
# ==============================================================================
LESSON_CONTENT['8.5'] = r"""### Part 1: Mental Model & South Asian Analogy
Linear pipelines (jaise chain: Step A $\to$ Step B $\to$ Step C) simple tasks ke liye theek hain, lekin real-world software engineering mein kaam seedha nahi chalta. Agar tester ko code mein bug mil jaye to code wapas developer ke paas aata hai (Cyclic Loop). 2026 mein stateful multi-agent workflows ka industry standard **LangGraph** hai!
Isay samajhne ke liye kisi Software House ki Team aur Daily Standup ki misaal lein:
1. The Shared Project Board (The Graph State): Darmiyan mein ek white board hai jisme current state likhi hai: Current Code, Error Logs, Test Status, aur Approval Status. Har agent board par likhta hai aur doosre agent ki likhi hui cheez parhta hai.
2. Specialized Agent Nodes:
   - Node 1: Coder Agent (Code likhta hai aur board par save karta hai).
   - Node 2: Tester Agent (Unit tests run karta hai).
3. Conditional Edges (The Crossroads / Faislay Ki Deewar):
   - Agar tamam tests pass ho gaye -> Send to Senior Architect Node (Human-in-the-Loop Approval).
   - Agar tests fail ho gaye -> Loop back to Coder Agent with error traceback!
4. Human-in-the-Loop Interrupts (Ustaad Ka Sign): Agar koi khatarnak operation ho (jaise production deployment ya bank payment), to graph achanak ruk jata hai (Breakpoint). Ustaad UI par aakar "Approve" ka button dabata hai, tabhi graph aglay step par jata hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein State Transition Graph aur Cyclic Edge Routing ka finite state machine (FSM) hisab trace karte hain.
State Schema:
$S = \{\text{code}: \text{str}, \text{errors}: \text{List}[\text{str}], \text{test\_passed}: \text{bool}, \text{revision\_count}: \text{int}\}$
Maximum allowed revisions: $R_{\text{max}} = 3$.

Transition Rules:
- Node `coder`: increments `revision_count += 1`.
- Node `tester`: if syntax errors exist $\implies \text{test\_passed} = \text{False}$; else $\text{test\_passed} = \text{True}$.
- Conditional Router Edge at `tester`:
  - If $\text{test\_passed} == \text{True} \implies$ Go to Node `deploy`.
  - If $\text{test\_passed} == \text{False}$ and $\text{revision\_count} < R_{\text{max}} \implies$ Loop back to Node `coder`.
  - If $\text{test\_passed} == \text{False}$ and $\text{revision\_count} \ge R_{\text{max}} \implies$ Go to Node `escalate_to_human`.

Worked State Trace:
- Initial: `revision_count = 0, test_passed = False`
- Step 1: `coder` writes buggy code -> `revision_count = 1`
- Step 2: `tester` finds `SyntaxError` -> `test_passed = False`
  Router: $1 < 3 \implies$ Cycle back to `coder`!
- Step 3: `coder` reads error, fixes syntax -> `revision_count = 2`
- Step 4: `tester` runs tests -> All pass! -> `test_passed = True`
  Router: `test_passed == True` $\implies$ Direct to Node `deploy`!
Cyclic loop ne automated self-healing achieve ki bina kisi human intervention ke!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum pure Python ke sath State Graph State Machine, typed state channels, conditional cyclic edge routing, aur human-in-the-loop approval gate implement karte hain.

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable

@dataclass
class WorkflowState:
    \"\"\"Shared graph state passed across all agent nodes.\"\"\"
    task_description: str
    code_artifact: str = ""
    unit_test_log: str = ""
    tests_passed: bool = False
    iterations: int = 0
    requires_human_approval: bool = False
    approved_by_human: bool = False

class StatefulAgentGraph:
    \"\"\"Simulates LangGraph cyclic multi-agent workflow engine.\"\"\"
    def __init__(self, max_iterations: int = 3) -> None:
        self.max_iterations = max_iterations

    # Node 1: Coder Agent
    def coder_node(self, state: WorkflowState) -> WorkflowState:
        state.iterations += 1
        print(f"[Coder Node] Working on code revision {state.iterations}...")
        if state.iterations == 1:
            # First attempt: intentional buggy code
            state.code_artifact = "def calculate_tax(p): return p * 0.16 + 'error'"
        else:
            # Fixed code after observing test failure
            state.code_artifact = "def calculate_tax(p): return round(p * 0.16, 2)"
        return state

    # Node 2: Tester Agent
    def tester_node(self, state: WorkflowState) -> WorkflowState:
        print("[Tester Node] Executing unit tests in sandbox...")
        if "error" in state.code_artifact:
            state.tests_passed = False
            state.unit_test_log = "TypeError: unsupported operand + for float and str"
        else:
            state.tests_passed = True
            state.unit_test_log = "All unit tests PASSED (100% assertions verified)."
        return state

    # Conditional Routing Logic
    def route_after_test(self, state: WorkflowState) -> str:
        if state.tests_passed:
            return "human_gate"
        if state.iterations >= self.max_iterations:
            return "escalate"
        return "coder"

    def run(self, initial_state: WorkflowState) -> WorkflowState:
        state = initial_state
        current_node = "coder"

        while True:
            if current_node == "coder":
                state = self.coder_node(state)
                current_node = "tester"
            elif current_node == "tester":
                state = self.tester_node(state)
                next_step = self.route_after_test(state)
                print(f"  [Routing Gate] Decision: '{next_step}'")
                if next_step == "coder":
                    current_node = "coder"
                elif next_step == "human_gate":
                    current_node = "human_gate"
                else:
                    current_node = "escalate"
            elif current_node == "human_gate":
                print("[Human Gate] All tests passed! Pausing for human verification...")
                # Simulate human supervisor approval
                state.approved_by_human = True
                print("[Human Gate] Supervisor approved deployment.")
                break
            elif current_node == "escalate":
                print("[Escalate Node] Max retries exhausted. Escalated to senior engineer.")
                break

        return state

# Execution test
if __name__ == "__main__":
    graph = StatefulAgentGraph(max_iterations=3)
    init_state = WorkflowState(task_description="Implement GST billing calculator")
    
    final_state = graph.run(init_state)
    print("\\nWorkflow Finished Successfully!")
    print(f"Total Cycles Taken: {final_state.iterations}")
    print(f"Final Artifact:     {final_state.code_artifact}")
    print(f"Human Approved:     {final_state.approved_by_human}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Unbounded Graph Cycles Without State Counters: Conditional edge mein agar `iterations` counter na ho aur tests kabhi pass na hon to graph hamesha ke liye ghoomta rehta hai. Hamesha state mein cycle counter aur maximum threshold rakhein.
2. In-Place State Mutation Across Concurrent Branches: Multi-agent graphs mein agar do nodes aik hi waqt mein ek mutable state dictionary ko tabdeel karein to data race condition paida hoti hai. LangGraph Reducer functions (jaise `operator.add`) use karna zaroori hai.
3. Bypassing Human-in-the-Loop on Destructive Actions: Database drop ya external fund transfer jaisi sensitive operations ko direct autonomous execution par chhorna catastrophically dangerous hai. Hamesha explicit breakpoint lagayein.

Zero-GPU Tip:
State graphs, conditional edge routers, aur finite state machines pure asynchronous Python control flow hain. Inhe local CPU par comprehensive unit tests ke sath test karein.

Self-Check Questions:
1. LangGraph jaise cyclic multi-agent systems linear chains (jaise standard LangChain LCEL) se kyun behtar hain?
2. Conditional Edge ka decision rule graph routing mein kaise kaam karta hai?
3. Human-in-the-loop breakpoint agent reliability aur safety ko kaise barhata hai?

What to Build Next:
Ek LangGraph Software Team banayein jisme Planner, Coder, aur Reviewer nodes hon jo markdown PR description aur unit tests cyclic loop mein generate karein."""

# ==============================================================================
# LESSON 8.6: Module 8 Capstone: Autonomous Multi-Agent Software Swarm
# ==============================================================================
LESSON_CONTENT['8.6'] = r"""### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne Autonomous Agents aur Tool Use ke tamam ahem sutoon (ReAct loop, Anthropic MCP protocol, Hugging Face smolagents, Function calling schemas, aur LangGraph stateful cyclic graphs) mukammal kar liye hain. Ab waqt hai aapke **Pehle Autonomous Multi-Agent Software Engineering Swarm** ka!
Is Capstone project ka zehni khaka kisi Top Software Agency (Jaise Systems Limited ya 10Pearls) ke Engineering Floor jaisa hai:
1. Product Manager Agent (The Blueprint Architect): User aam zaban mein kehta hai: "Mujhe ek Dhaba Billing CLI chahiye jisme tax aur discount calculation ho." Product Manager requirement ko breakdown karta hai aur detailed technical specifications board par likhta hai.
2. Software Architect Agent (The Tech Lead): Architect specifications dekh kar architecture design karta hai: modules, classes, schemas, aur file layouts define karta hai.
3. Coder Agent (The Heavy Lifter): Coder agent terminal par code likhta hai, sandboxed tools use karta hai, aur files create karta hai.
4. QA & Security Auditor Agent (The Strict Gatekeeper): Tester agent code ko inspect karta hai, unit tests generate karke run karta hai, aur security vulnerabilities scan karta hai. Agar koi bug ho to code wapas Coder ke paas chala jata hai!
5. Deployment Agent (The Shipper): Jab tamam tests pass ho jate hain to Shipper code ko package karke verified release tag bana deta hai.

Yeh multi-agent swarm autonomous software development ka 2026 production paradigm hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Multi-Agent Swarm ke Communication Overhead aur Task Convergence ka exact hisab lagayein.
Parameters:
- Agents in Swarm $K = 4$ (Product Manager, Architect, Coder, QA)
- Shared State Board Size at Start = 500 tokens
- Average agent deliberation turn $= 150 \text{ tokens}$
- Total workflow steps $= 6 \text{ steps}$

Communication Overhead Growth:
Har step par pichle agents ka output aglay agent ka input context banta hai:
- Step 1 (PM): Context = $500 \text{ tokens}$. Output = $200 \text{ tokens}$. Board = $700 \text{ tokens}$.
- Step 2 (Architect): Context = $700 \text{ tokens}$. Output = $250 \text{ tokens}$. Board = $950 \text{ tokens}$.
- Step 3 (Coder): Context = $950 \text{ tokens}$. Output = $350 \text{ tokens}$ (Code artifact). Board = $1300 \text{ tokens}$.
- Step 4 (QA Audit): Context = $1300 \text{ tokens}$. Output = $150 \text{ tokens}$ (Test report). Board = $1450 \text{ tokens}$.

Total Token Consumption of Swarm:
$\text{Total Tokens} = 500 + 700 + 950 + 1300 = 3450 \text{ input tokens}$
$\text{Total Output} = 200 + 250 + 350 + 150 = 950 \text{ output tokens}$
Total Swarm Cost at Groq LLaMA-3.3-70B rates (\$0.50 per 1M blended):
$\text{Total Cost} = \frac{4400}{1,000,000} \times \$0.50 \approx \$0.0022 \text{ USD}$ (Aadha rupaya per full software lifecycle)!
Aadhe rupaye mein complete autonomous multi-agent feature implement aur test ho jata hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum complete Multi-Agent Swarm implement karte hain: shared blackboard state, specialized agent role handlers, automated QA unit testing, aur release artifact packaging.

```python
import time
from typing import Dict, Any, List
from dataclasses import dataclass, field

@dataclass
class SwarmBlackboard:
    goal: str
    specifications: List[str] = field(default_factory=list)
    code_artifact: str = ""
    qa_report: str = ""
    is_ready_for_ship: bool = False
    audit_trail: List[str] = field(default_factory=list)

class AutonomousSoftwareSwarm:
    \"\"\"Multi-agent collaborative software engineering swarm.\"\"\"
    def __init__(self, blackboard: SwarmBlackboard) -> None:
        self.board = blackboard

    def agent_pm(self) -> None:
        print("[Agent PM] Breaking down user goal into formal user stories...")
        self.board.specifications = [
            "Requirement 1: MenuItem dataclass with validation",
            "Requirement 2: Calculate tax (16%) and 10% loyalty discount",
            "Requirement 3: Clean CLI invoice summary"
        ]
        self.board.audit_trail.append("PM created specifications.")

    def agent_architect(self) -> None:
        print("[Agent Architect] Designing data models and interface contracts...")
        self.board.audit_trail.append("Architect approved modular single-file CLI architecture.")

    def agent_coder(self) -> None:
        print("[Agent Coder] Synthesizing production Python code artifact...")
        self.board.code_artifact = \"\"\"
from dataclasses import dataclass

@dataclass(slots=True)
class DhabaItem:
    name: str
    price: float

def compute_bill(items: list[DhabaItem], discount_pct: float = 0.0) -> float:
    subtotal = sum(i.price for i in items)
    discounted = subtotal * (1.0 - (discount_pct / 100.0))
    return round(discounted * 1.16, 2)
\"\"\"
        self.board.audit_trail.append("Coder implemented core billing logic.")

    def agent_qa(self) -> None:
        print("[Agent QA] Running automated static analysis and test validation...")
        # Verify code artifact contains core functions
        if "compute_bill" in self.board.code_artifact and "slots=True" in self.board.code_artifact:
            self.board.qa_report = "QA Assessment: Clean code, slots=True verified, zero security flaws."
            self.board.is_ready_for_ship = True
            self.board.audit_trail.append("QA signed off on artifact quality.")
        else:
            self.board.qa_report = "QA Assessment: Code missing critical invariants."
            self.board.is_ready_for_ship = False

    def run_swarm(self) -> None:
        t0 = time.perf_counter()
        print(f"Initiating Autonomous Swarm for Goal: '{self.board.goal}'\\n")
        
        self.agent_pm()
        self.agent_architect()
        self.agent_coder()
        self.agent_qa()

        elapsed_ms = (time.perf_counter() - t0) * 1000.0
        print(f"\\nSwarm Lifecycle Completed in {elapsed_ms:.2f} ms!")
        print(f"Ship Ready Status: {self.board.is_ready_for_ship}")
        print("\\nFinal Delivered Code Artifact:\\n", self.board.code_artifact)
        print("Audit Trail Summary:")
        for log in self.board.audit_trail:
            print(f"  - {log}")

# Execution test
if __name__ == "__main__":
    initial_board = SwarmBlackboard(goal="Build a production Dhaba billing engine with strict dataclasses")
    swarm = AutonomousSoftwareSwarm(initial_board)
    swarm.run_swarm()
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Unconstrained Agent Chatter (Context Window Explosion): Agar agents aapas mein be-maqsad lambi polite guftagu shuru kar dein ("Thank you dear colleague!", "You are very welcome!"), to context window fazool baaton se bhar jati hai. Agents ko hamesha structured schema ya bulleted blackboard updates par force karein.
2. Lack of Central Single-Source-of-Truth Blackboard: Agar agent A direct agent B ko alag message bheje aur agent C ko pata na ho, to poore swarm ka state sync toot jata hai. Hamesha shared centralized blackboard state pattern use karein.
3. Not Isolating Code Execution Environments: Coder agent ke likhe hue code ko usi process mein direct run kar dena pure system ko compromise kar sakta hai. QA agent ko hamesha isolated Docker container ya secure AST sandbox mein code run karna chahiye.

Zero-GPU Tip:
Multi-agent swarm coordination, prompt routing, aur shared state transitions 100% CPU bound orchestration hai. Fast free tier APIs (Groq Cloud LLaMA-3.3 ya Gemini 2.0 Flash) ke zariye aap apne laptop se poori software engineering agency autonomous chala sakte hain.

Self-Check Questions:
1. Multi-Agent Swarm mein Shared Blackboard Pattern ka kya faida hota hai?
2. Specialized Agent roles (PM, Architect, Coder, QA) general single-prompt LLM ke muqablay accuracy kyun barhate hain?
3. Swarm mein agent-to-agent chatter ko rokne ke liye communication protocols kaise design kiye jate hain?

What to Build Next:
Is Autonomous Swarm ko extend karein taake Coder aur QA agents ke darmiyan live cyclic retry loop ho: agar QA fail ho to error logs Coder ko bhej kar 3 attempts tak auto-debug kare."""
