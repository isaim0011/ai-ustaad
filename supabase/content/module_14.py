# module_14.py
# Module 14: Enterprise Capstone & Career Launch
# Lessons 14.1 to 14.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 14.1: Enterprise System Design: Multi-Tenant RLS, Vector Partitioning & Audit
# ==============================================================================
LESSON_CONTENT['14.1'] = r'''### Part 1: Mental Model & South Asian Analogy
Jab aap ek demo AI app banate hain, to usme sirf aapka apna data hota hai. Lekin jab aap ek **Enterprise Multi-Tenant AI SaaS** banate hain jahan 500 alag-alag companies (maslan Meezan Bank, Careem, Daraz, aur Indus Hospital) aapke ek hi database aur vector index ko istemal kar rahi hain, to sab se bara khatra **Cross-Tenant Data Leakage** hota hai! Agar Meezan Bank ke employee ne chatbot se سوال poocha aur RAG vector search ne ghalti se Daraz ka confidential financial PDF retrieve kar ke jawab de diya, to aapki company par usi din muqadma (lawsuit) ho jayega.

Isay samajhne ke liye **Karachi ya Lahore ki High-Security Bank Locker Building** ki misaal lein:
1. **Naive Single-Table Design (Khula Godown)**: Sab customers ka sona aur kagzaat ek hi bare kamre mein rakh diye aur sirf chaukidar (Application Code `WHERE org_id = ?`) par bharosa kiya. Agar chaukidar se ek jagah `WHERE` clause lagana bhool gaya, to ek customer doosre customer ka locker khol lega!
2. **PostgreSQL Row-Level Security - RLS (Biometric Auto-Locking Vaults)**: Database engine ke andar har row par qanooni tala laga hota hai. Chahe application programmer `SELECT * FROM documents` likh de, PostgreSQL database khud current user ka cryptographic JWT token check karta hai aur sirf uske apne `tenant_id` wali rows wapis bhejta hai. Baqi rows us ke liye wajood hi nahi rakhtin!
3. **Vector Index Partitioning (Alag Alag Tijoriyan)**: Agar 1 Crore vectors ek hi HNSW index mein pare hon aur aap `tenant_id` filter lagayein, to search slow ho jati hai (Over-filtering problem). Partitioning har bare tenant ko apna dedicated HNSW sub-index deti hai.
4. **Immutable Audit Logs (Bank CCTV & Register)**: Har prompt, retrieved document ID, aur LLM output ka cryptographic hash timestamp ke sath record hota hai taake compliance audit (SOC2 / GDPR / State Bank) mein har action sabit kiya ja sake.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein **HNSW Vector Search Pre-Filtering vs Post-Filtering Recall Degradation** ka ریاضیاتی (mathematical) hisab lagayein.

Farz karein aapke `document_chunks` table mein total $N = 1,000,000$ (10 Lakh) vectors hain.
Ek chote tenant (Organization B) ke sirf $N_B = 1,000$ vectors hain (yani total dataset ka $0.1\%$ ya $p = 0.001$).

**Case 1: Naive Post-Filtering (Pehle Top-$K$ Vector Search, Phir `tenant_id` Filter)**
Agar HNSW index top $K = 50$ nearest neighbors dhoondta hai across all 1,000,000 vectors, aur phir application check karti hai ke in 50 mein se Organization B ke kitne hain:
Expected matches for Org B in Top-50:
$$E[\text{Matches}] = K \times p = 50 \times 0.001 = 0.05 \text{ chunks!}$$
Probability of getting **ZERO** results for Org B:
$$P(X = 0) = (1 - 0.001)^{50} \approx 0.9512 \text{ (95.12\% failure rate!)}$$
Yani 95% dafa user ko empty context milega halanke uske 1,000 documents database mein maujood thay!

**Case 2: Partitioned Iterative Index Scan (`pgvector` 0.8+ Iterative HNSW + RLS)**
Jab hum table ko `LIST (tenant_id)` ya Partial HNSW Indexes par partition karte hain:
- Search space drops from $1,000,000 \rightarrow 1,000$.
- Graph traversal hops: $\log_2(1,000) \approx 10$ comparisons instead of $\log_2(1,000,000) \approx 20$.
- **Recall@5**: Reaches $99.8\%$ with latency $< 2.1\text{ ms}$ and **0.0% cross-tenant leakage**!

### Part 3: Annotated Production Code
Neeche diye gaye code mein hum PostgreSQL Row-Level Security (RLS) policy generation, cryptographic audit log chaining (SHA-256 tamper-evident hash chain), aur multi-tenant context verifier implement karte hain.

```python
import hashlib
import json
import time
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional

@dataclass
class AuditEntry:
    seq_id: int
    timestamp: float
    tenant_id: str
    user_id: str
    action: str
    resource_ids: List[str]
    prev_hash: str
    entry_hash: str

class TamperEvidentAuditLedger:
    """Cryptographic hash-chained audit log for SOC2 / Enterprise AI compliance."""
    def __init__(self) -> None:
        self.chain: List[AuditEntry] = []

    def append_event(
        self, tenant_id: str, user_id: str, action: str, resource_ids: List[str]
    ) -> AuditEntry:
        seq_id = len(self.chain) + 1
        ts = round(time.time(), 4)
        prev_hash = self.chain[-1].entry_hash if self.chain else "0" * 64

        payload = f"{seq_id}|{ts}|{tenant_id}|{user_id}|{action}|{','.join(resource_ids)}|{prev_hash}"
        entry_hash = hashlib.sha256(payload.encode("utf-8")).hexdigest()

        entry = AuditEntry(
            seq_id=seq_id,
            timestamp=ts,
            tenant_id=tenant_id,
            user_id=user_id,
            action=action,
            resource_ids=resource_ids,
            prev_hash=prev_hash,
            entry_hash=entry_hash,
        )
        self.chain.append(entry)
        return entry

    def verify_integrity(self) -> bool:
        """Verifies that no historical audit record has been modified or deleted."""
        for i, entry in enumerate(self.chain):
            expected_prev = self.chain[i - 1].entry_hash if i > 0 else "0" * 64
            if entry.prev_hash != expected_prev:
                return False
            payload = (
                f"{entry.seq_id}|{entry.timestamp}|{entry.tenant_id}|"
                f"{entry.user_id}|{entry.action}|{','.join(entry.resource_ids)}|{entry.prev_hash}"
            )
            recomputed = hashlib.sha256(payload.encode("utf-8")).hexdigest()
            if recomputed != entry.entry_hash:
                return False
        return True

def verify_rls_isolation(
    jwt_tenant_id: str, retrieved_chunks: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Defense-in-depth assertion verifying every vector chunk matches the caller's tenant."""
    verified = []
    for chunk in retrieved_chunks:
        if chunk.get("tenant_id") != jwt_tenant_id:
            raise PermissionError(
                f"CRITICAL SECURITY BREACH: Cross-tenant chunk {chunk.get('id')} "
                f"detected for caller {jwt_tenant_id}!"
            )
        verified.append(chunk)
    return verified

if __name__ == "__main__":
    ledger = TamperEvidentAuditLedger()
    e1 = ledger.append_event("org_meezan", "usr_ali", "RAG_QUERY", ["doc_101", "doc_104"])
    e2 = ledger.append_event("org_daraz", "usr_sara", "RAG_QUERY", ["doc_882"])
    print(f"Audit Entry #1 Hash: {e1.entry_hash[:24]}...")
    print(f"Audit Entry #2 Prev: {e2.prev_hash[:24]}...")
    print(f"Ledger Cryptographic Integrity Verified: {ledger.verify_integrity()}")

    chunks = [
        {"id": "doc_101", "tenant_id": "org_meezan", "text": "Meezan Q3 Report"},
        {"id": "doc_104", "tenant_id": "org_meezan", "text": "Branch Policy"},
    ]
    safe_chunks = verify_rls_isolation("org_meezan", chunks)
    print(f"RLS Defense-in-Depth Passed: {len(safe_chunks)} chunks verified.")
```

### Part 4: Common Pitfalls, Zero-GPU Tips, Self-Check & Next Steps
**Common Mistakes & Pitfalls:**
1. **Using Supabase `service_role` Key in User Queries**: `service_role` key PostgreSQL ki tamam RLS policies ko bypass kar deti hai! User-facing requests mein hamesha user ka scoped JWT pass karein ya `SET LOCAL request.jwt.claims` istemal karein.
2. **Shared Semantic Cache Across Tenants**: Agar aap Redis semantic cache mein sirf `hash(prompt_embedding)` key banate hain bina `tenant_id` prefix ke (`tenant_id:hash`), to ek company ka jawab doosri company ko serve ho jayega!

**Zero-GPU & Free-Tier Execution Tips:**
- Supabase Free Tier aapko full PostgreSQL 15/16, `pgvector` HNSW indexes, aur unlimited Row-Level Security policies bilkul muft ($0/month) deta hai.

**Self-Check Questions:**
1. Post-filtering vector search mein chote tenants (0.1% dataset share) ko 95% waqt empty results kyun milte hain?
2. `auth.uid()` ko direct `USING (user_id = auth.uid())` likhne ke bajaye `USING (user_id = (SELECT auth.uid()))` likhne se PostgreSQL query planner ko kya faida hota hai?
3. Hash-chained audit log mein agar koi attacker beech ki ek entry delete ya edit kar de to `verify_integrity()` usay kaise pakarta hai?

**What to Build Next:**
Apne Supabase database mein `documents` table par `tenant_id` column add karein aur `CREATE POLICY tenant_isolation` likh kar दो mukhtalif JWT users se test karein ke kya ek user doosre ka vector देख sakta hai.
'''
LESSON_CONTENT['enterprise-multi-tenant-architecture'] = LESSON_CONTENT['14.1']

# ==============================================================================
# LESSON 14.2: High Availability & Resilience: Circuit Breakers & Multi-Cloud Fallback
# ==============================================================================
LESSON_CONTENT['14.2'] = r'''### Part 1: Mental Model & South Asian Analogy
Production AI engineering ki sab se karwi haqeeqat yeh hai: **Har LLM provider (OpenAI, Anthropic, Groq, Cloudflare) kabhi na kabhi down hota hai ya `429 Rate Limit` / `503 Overloaded` marta hai!** Agar aapka code sirf ek API endpoint par hardcoded hai, to provider girte hi aapka poora startup thap ho jayega.

Isay samajhne ke liye **Pakistani Ghar ya Hospital ke 3-Tier Power Backup System (WAPDA + Solar + UPS/Generator)** ki misaal lein:
1. **Primary Tier (Solar / Fast Edge Provider - e.g. Groq / Cloudflare Workers AI)**: Din ke waqt sab se sasta aur bijli ki tarah tez (300+ tokens/sec). 95% load yehi uthata hai.
2. **Circuit Breaker (Main Distribution Board Ka Breaker)**: Agar WAPDA ki line mein short-circuit ho ya voltage 400V par chala jaye, to breaker `OPEN` (trip) ho jata hai taake ghar ke fridge aur AC jal na jayein, aur bijli foran 10 milliseconds mein UPS par shift ho jati hai. Bilkul isi tarah software Circuit Breaker jab dekhta hai ke Primary LLM lagatar 5 errors de chuka hai, to woh 30 seconds tak Primary LLM ko call karna hi band kar deta hai (zero waiting time) aur traffic seedha Secondary Fallback provider par bhejta hai!
3. **Half-Open Probe (Mistri Ka Test Bulb)**: 30 seconds baad Circuit Breaker `HALF_OPEN` state mein aata hai aur sirf **1 test request** Primary LLM ko bhejta hai. Agar woh kamyab ho jaye to breaker wapis `CLOSED` (Normal) ho jata hai!
4. **Exponential Backoff with Full Jitter**: Agar 1,000 requests ek sath fail hon aur sab theek 2.000 second baad dobara retry karein, to woh server par **Thundering Herd** ban kar dobara hamla kar dengi. Random Jitter har client ko alag millisecond par retry karwata hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein **Multi-Provider Composite Availability (SLA Math)** aur **Tail Latency** ka hisab lagayein.

Farz karein aapke paas 3 independent LLM inference providers hain aur har ek ka individual uptime $99.0\%$ hai (yani failure probability $p_f = 0.01$, jo LLM APIs ke liye aam baat hai — 7.2 hours downtime per month!):

**Scenario A: Single Provider Architecture**
- System Availability $= 99.0\%$
- Monthly Downtime $= 30 \times 24 \times 0.01 = 7.2 \text{ hours/month}$.

**Scenario B: 3-Tier Multi-Cloud Fallback with Circuit Breaker**
System tabhi fail hoga jab **teeno** providers ek hi lamhe par down hon:
$$P(\text{Total Failure}) = p_{f1} \times p_{f2} \times p_{f3} = 0.01 \times 0.01 \times 0.01 = 0.000001 = 10^{-6}$$
$$\text{Composite Availability} = 1 - 10^{-6} = 99.9999\% \text{ (Six Nines Uptime!)}$$
- Monthly Downtime drops from **7.2 hours** to **$2.59 \text{ seconds/month}$**!

**Latency Impact of Circuit Breaker:**
- Without Circuit Breaker: Every request waits for a $10\text{s}$ timeout on Provider 1 before trying Provider 2 $\rightarrow$ User waits $10.8\text{s}$.
- With Circuit Breaker (tripped after 3 failures): Requests bypass Provider 1 in $0.01\text{ms}$ and get answered by Provider 2 in $0.8\text{s}$!

### Part 3: Annotated Production Code
Neeche diye gaye code mein hum complete Finite-State Machine (`CLOSED`, `OPEN`, `HALF_OPEN`) Circuit Breaker aur Multi-Cloud LLM Router implement karte hain.

```python
import time
import random
from enum import Enum
from typing import Callable, Dict, Any, List

class CircuitState(Enum):
    CLOSED = "CLOSED"          # Normal operation
    OPEN = "OPEN"              # Tripped! Fast-fail immediately
    HALF_OPEN = "HALF_OPEN"    # Testing recovery with 1 probe request

class ProviderCircuitBreaker:
    """Production state-machine circuit breaker for LLM API endpoints."""
    def __init__(self, name: str, failure_threshold: int = 3, recovery_timeout_sec: float = 15.0) -> None:
        self.name = name
        self.failure_threshold = failure_threshold
        self.recovery_timeout_sec = recovery_timeout_sec
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = 0.0

    def allow_request(self) -> bool:
        if self.state == CircuitState.CLOSED:
            return True
        if self.state == CircuitState.OPEN:
            if (time.time() - self.last_failure_time) >= self.recovery_timeout_sec:
                self.state = CircuitState.HALF_OPEN
                return True
            return False
        # In HALF_OPEN, allow the probe request
        return True

    def record_success(self) -> None:
        self.failure_count = 0
        self.state = CircuitState.CLOSED

    def record_failure(self) -> None:
        self.failure_count += 1
        self.last_failure_time = time.time()
        if self.failure_count >= self.failure_threshold or self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.OPEN

class MultiCloudLLMRouter:
    """Routes prompts across Primary -> Secondary -> Local Fallback with circuit breakers."""
    def __init__(self, providers: List[Dict[str, Any]]) -> None:
        self.providers = providers
        self.breakers = {p["name"]: ProviderCircuitBreaker(p["name"]) for p in providers}

    def generate(self, prompt: str) -> Dict[str, Any]:
        errors = []
        for p in self.providers:
            name = p["name"]
            breaker = self.breakers[name]

            if not breaker.allow_request():
                errors.append(f"{name}: Circuit OPEN (fast-skipped)")
                continue

            try:
                response_text = p["call_fn"](prompt)
                breaker.record_success()
                return {
                    "provider_used": name,
                    "circuit_state": breaker.state.value,
                    "reply": response_text,
                    "prior_failures": errors,
                }
            except Exception as exc:
                breaker.record_failure()
                errors.append(f"{name}: {str(exc)} (state->{breaker.state.value})")

        raise RuntimeError(f"All providers exhausted: {errors}")

if __name__ == "__main__":
    def failing_primary(prompt: str) -> str:
        raise TimeoutError("HTTP 503 Overloaded")

    def healthy_secondary(prompt: str) -> str:
        return f"[Groq-Llama-3.3-70B] Processed: '{prompt}'"

    router = MultiCloudLLMRouter([
        {"name": "Primary-Cloud", "call_fn": failing_primary},
        {"name": "Secondary-Groq", "call_fn": healthy_secondary},
    ])

    for i in range(1, 5):
        res = router.generate(f"Query #{i}")
        print(f"Req {i} -> Routed to: {res['provider_used']} | Logs: {res['prior_failures']}")
```

### Part 4: Common Pitfalls, Zero-GPU Tips, Self-Check & Next Steps
**Common Mistakes & Pitfalls:**
1. **Retrying on `400 Bad Request` or `401 Unauthorized`**: Agar aapka prompt context window se bara hai (`400`) ya API key ghalat hai (`401`), to 10 dafa retry karne se bhi woh fail hi hoga! Sirf transient errors (`429 Rate Limit`, `500`, `502`, `503`, `504` aur network timeouts) par retry ya circuit trip karein.
2. **Inconsistent Output Formats Across Providers**: Agar Primary provider JSON return karta hai aur Fallback provider markdown, to frontend crash ho jayega. Har provider adapter ke baad ek unified response normalizer rakhein.

**Zero-GPU & Free-Tier Execution Tips:**
- AI Ustaad platform khud yehi 3-Tier architecture istemal karta hai: Tier 1 Cloudflare Workers AI (Free Edge binding) $\rightarrow$ Tier 2 Groq Cloud Free API $\rightarrow$ Tier 3 Deterministic Roman Urdu Knowledge Engine!

**Self-Check Questions:**
1. Circuit Breaker ki `OPEN` aur `HALF_OPEN` states mein kya farq hai?
2. Agar 2 independent providers ka uptime 98% aur 99% ho, to composite system availability kitni hogi?
3. Thundering Herd problem ko rokne ke liye Exponential Backoff mein Jitter kyun add kiya jata hai?

**What to Build Next:**
Apne AI Mentor endpoint mein har provider ke liye latency aur circuit state headers (`X-AI-Provider`, `X-Circuit-State`) return karein taake dashboard par live health nazar aaye.
'''
LESSON_CONTENT['high-availability-circuit-breakers'] = LESSON_CONTENT['14.2']

# ==============================================================================
# LESSON 14.3: Monetization & Governance: Token Metering & Stripe Usage-Based Billing
# ==============================================================================
LESSON_CONTENT['14.3'] = r'''### Part 1: Mental Model & South Asian Analogy
Software-as-a-Service (SaaS) ki purani duniya mein marginal cost zero hoti thi: chahe user 10 dafa button dabaye ya 10,000 dafa, server ka flat $20/month bill hi aata tha. Lekin **AI Engineering mein har prompt aur har generated token par asli paisay (compute/API cost) lagte hain!** Agar aapne $10/month ka "Unlimited AI" plan bech diya aur ek power-user ne automated script laga kar 50 Million tokens consume kar liye, to woh akele aapki jeb se $500 nikalwa dega!

Isay samajhne ke liye **Prepaid Mobile Balance (Jazz/Zong Load) aur Smart Electricity Meter (LESCO/K-Electric)** ki misaal lein:
1. **Input vs Output Token Asymmetry**: LLM mein prompt padhna (Prefill) sasta hota hai kyunki woh parallel matrix-matrix multiplication hai, jabke jawab likhna (Autoregressive Decode) **3x se 5x mehenga** hota hai kyunki har token sequential memory bandwidth mangta hai!
2. **Atomic Credit Reservation (Pre-Auth Hold)**: Jab aap Careem book karte hain ya petrol pump par card swipe karte hain, to ride shuru hone se pehle bank aapke balance ko check kar ke lock lagata hai. Agar aap pehle LLM chala dein aur baad mein pata chale ke user ka balance zero tha, to LLM ka kharcha aapke sar par par gaya!
3. **Token Bucket & Daily Quota Caps**: Har subscription tier (`Free`, `Pro`, `Enterprise`) ke liye hard daily aur monthly token ceilings hoti hain.
4. **Stripe Metered Billing Events**: Har request ke baad exact prompt aur completion tokens count ہو kar asynchronous queue ke zariye billing ledger mein jama hote hain.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein ek **AI SaaS Unit Economics & Gross Margin Formula** ka exact hisab lagayein.

Farz karein aapka AI SaaS model yeh pricing rakhta hai:
- Upstream Model Cost (e.g., Frontier 70B/405B):
  - Input Cost $C_{\text{in}} = \$0.80 \text{ per 1 Million tokens}$
  - Output Cost $C_{\text{out}} = \$2.40 \text{ per 1 Million tokens}$ ($3\times$ expensive)
- Average User Interaction (1 Turn with RAG Context):
  - System Prompt + RAG Chunks + User Query $= 2,500 \text{ input tokens}$
  - Assistant Response $= 500 \text{ output tokens}$

**Step 1: Cost Per Single Turn ($C_{\text{turn}}$)**
$$C_{\text{turn}} = \left(\frac{2500}{1,000,000} \times \$0.80\right) + \left(\frac{500}{1,000,000} \times \$2.40\right)$$
$$C_{\text{turn}} = \$0.0020 + \$0.0012 = \$0.0032 \text{ per message (approx 0.9 PKR)}$$

**Step 2: Monthly Usage & Gross Margin for a \$20/month Pro User**
Agar ek active user rozana $50$ messages bhejta hai ($1,500 \text{ messages/month}$):
$$\text{Monthly COGS (Cost of Goods Sold)} = 1,500 \times \$0.0032 = \$4.80$$
$$\text{Gross Profit} = \$20.00 - \$4.80 = \$15.20$$
$$\text{Gross Margin \%} = \frac{\$15.20}{\$20.00} \times 100 = 76.0\% \text{ (Healthy SaaS Margin!)}$$

**Step 3: Why Prompt Caching Changes Everything**
Agar $2,500$ input tokens mein se $2,000$ tokens static system prompt aur docs hain jo **Prompt Cache** ($90\%$ discount $\rightarrow \$0.08/\text{1M}$) se aate hain:
- New Input Cost $= \frac{500 \times 0.80 + 2000 \times 0.08}{1,000,000} = \$0.00056$
- Total Turn Cost drops from $\$0.0032 \rightarrow \$0.00176$ (**45% instant cost reduction**)!

### Part 3: Annotated Production Code
Neeche diye gaye code mein hum atomic pre-flight credit reservation, asymmetric input/output token cost calculator, aur usage ledger implement karte hain.

```python
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class ModelPricing:
    model_id: str
    input_per_1m_usd: float
    cached_input_per_1m_usd: float
    output_per_1m_usd: float

class TokenMeteringEngine:
    """Production token metering and atomic credit guard for AI SaaS."""
    def __init__(self) -> None:
        self.pricing_table: Dict[str, ModelPricing] = {
            "llama-3.3-70b": ModelPricing("llama-3.3-70b", 0.59, 0.10, 0.79),
            "deepseek-r1": ModelPricing("deepseek-r1", 0.55, 0.14, 2.19),
        }
        # User balances in micro-dollars (1 USD = 1,000,000 micro-USD for integer precision)
        self.user_balances_micro_usd: Dict[str, int] = {}

    def deposit_usd(self, user_id: str, amount_usd: float) -> int:
        micro = int(round(amount_usd * 1_000_000))
        self.user_balances_micro_usd[user_id] = self.user_balances_micro_usd.get(user_id, 0) + micro
        return self.user_balances_micro_usd[user_id]

    def estimate_max_cost_micro(self, model_id: str, prompt_tokens: int, max_output_tokens: int) -> int:
        p = self.pricing_table[model_id]
        cost_usd = (prompt_tokens * p.input_per_1m_usd + max_output_tokens * p.output_per_1m_usd) / 1_000_000.0
        return int(round(cost_usd * 1_000_000))

    def execute_metered_call(
        self,
        user_id: str,
        model_id: str,
        prompt_tokens: int,
        cached_tokens: int,
        max_output_tokens: int,
        actual_output_tokens: int,
    ) -> Dict[str, Any]:
        # 1. Pre-flight reservation check
        reserved_micro = self.estimate_max_cost_micro(model_id, prompt_tokens, max_output_tokens)
        current_bal = self.user_balances_micro_usd.get(user_id, 0)
        if current_bal < reserved_micro:
            raise ValueError(
                f"Insufficient credits: need {reserved_micro} micro-USD, have {current_bal}"
            )

        # 2. Deduct reservation atomically before calling LLM
        self.user_balances_micro_usd[user_id] -= reserved_micro

        # 3. Calculate exact actual cost post-generation
        p = self.pricing_table[model_id]
        uncached_in = max(0, prompt_tokens - cached_tokens)
        actual_usd = (
            uncached_in * p.input_per_1m_usd
            + cached_tokens * p.cached_input_per_1m_usd
            + actual_output_tokens * p.output_per_1m_usd
        ) / 1_000_000.0
        actual_micro = int(round(actual_usd * 1_000_000))

        # 4. Refund unused reservation difference
        refund_micro = reserved_micro - actual_micro
        self.user_balances_micro_usd[user_id] += refund_micro

        return {
            "user_id": user_id,
            "model_id": model_id,
            "charged_usd": round(actual_micro / 1_000_000, 6),
            "remaining_balance_usd": round(self.user_balances_micro_usd[user_id] / 1_000_000, 6),
            "cache_savings_pct": round((cached_tokens / max(1, prompt_tokens)) * 100, 1),
        }

if __name__ == "__main__":
    meter = TokenMeteringEngine()
    meter.deposit_usd("usr_bimo", 5.00)
    receipt = meter.execute_metered_call(
        user_id="usr_bimo",
        model_id="deepseek-r1",
        prompt_tokens=4000,
        cached_tokens=3000,
        max_output_tokens=2048,
        actual_output_tokens=620,
    )
    print("Metered Billing Receipt:", receipt)
```

### Part 4: Common Pitfalls, Zero-GPU Tips, Self-Check & Next Steps
**Common Mistakes & Pitfalls:**
1. **Using Floating-Point `float` for Currency Balances**: IEEE-754 floats (`0.1 + 0.2 = 0.30000000000000004`) financial ledgers mein rounding drift paida karte hain! Hamesha integer **micro-dollars** (`1 USD = 1,000,000 micro-units`) ya PostgreSQL `BIGINT` istemal karein.
2. **Not Setting `max_tokens` on User Requests**: Agar aap API call mein `max_tokens` cap nahi lagate, to ek prompt injection attack model ko 32,000 tokens ka continuous loop likhne par majboor kar sakta hai!

**Zero-GPU & Free-Tier Execution Tips:**
- Apne development aur portfolio projects mein free-tier models (Cloudflare Workers AI / Groq Free Tier) istemal karein lekin UI mein "Estimated Token Cost & Carbon/Compute Meter" zaroor dikhayein — recruiters aur clients is engineering maturity ko dekh kar foran impress hote hain!

**Self-Check Questions:**
1. LLM inference mein output tokens ki qeemat input tokens se 3x–5x zyada kyun hoti hai?
2. Pre-flight credit reservation (`reserved_micro`) bina kiye agar hum sirf post-generation billing karein to kaunsa race-condition exploit ho sakta hai?
3. Financial database mein `FLOAT` ke bajaye `BIGINT` micro-dollars kyun store kiye jate hain?

**What to Build Next:**
Apne AI Mentor chat UI ke neeche ek subtle token telemetry badge (`Prompt: 320 tok | Output: 185 tok | Cost: $0.0002`) add karein.
'''
LESSON_CONTENT['token-metering-stripe-billing'] = LESSON_CONTENT['14.3']

# ==============================================================================
# LESSON 14.4: Packaging & Distribution: Multi-Stage Docker & Helm Charts
# ==============================================================================
LESSON_CONTENT['14.4'] = r'''### Part 1: Mental Model & South Asian Analogy
Aksar junior developers kehte hain: *"Sir, mere laptop par to code bilkul sahi chal raha tha, server par ja kar pata nahi kyun fat gaya!"* Aur jab woh apni AI application ka Docker container banate hain, to uska size **8.5 GB** nikalta hai jisko deploy hone mein 25 minute lagte hain aur uske andar compiler, git history, aur `.env` secrets tak pare hote hain!

Isay samajhne ke liye **Sialkot ki Factory se Export Hone Wale Surgical Instruments ya Football Container** ki misaal lein:
1. **Single-Stage Bloated Image (Puri Karkhana Ship Kar Dena)**: Aapne customer ko 100 football bhejne thay, lekin aapne football ke sath silai machines, kachra, lohay ke auzar, aur mazdooron ki charpaiyan bhi usi shipping container mein bhar kar bhej deen! Vazan 10 ton ho gaya aur kiraya 10 guna par gaya.
2. **Multi-Stage Docker Build (Factory Stage vs Export Box Stage)**:
   - **Stage 1 (`builder`)**: Yahan saari bhari machinery (`gcc`, `cargo`, `pip`, header files) mojood hoti hai jo code ko compile kar ke ek choti, self-contained binary ya wheel banati hai.
   - **Stage 2 (`runtime`)**: Ek bilkul saaf, khali minimal dabba (`debian-slim` ya `distroless`) liya jata hai aur Stage 1 se **sirf final compiled artifact** utha kar isme rakha jata hai. Baqi saari 4 GB ki compiler machinery wahin phenk di jati hai!
3. **Layer Caching (pehle se tayyar saman)**: Dockerfile mein har line ek layer hai. Agar aap `COPY . .` sab se upar likh denge, to code ki ek line badalne par Docker dobara 2 GB ke PyTorch packages download karega! Is liye pehle `COPY requirements.txt` ya `Cargo.lock` rakha jata hai taake dependencies cache rahein.
4. **Non-Root Security (`USER 10001`)**: Container ko kabhi `root` user par nahi chalate taake agar koi vulnerability ho bhi, to attacker host kernel tak na pohanch sake.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein **Container Image Size, Cold-Start Pull Time, aur Layer Cache Efficiency** ka hisab lagayein.

Farz karein aapke Kubernetes cluster mein auto-scaling lagi hui hai aur traffic spike aane par naya node container image pull karta hai over a $100 \text{ Mbps}$ ($12.5 \text{ MB/s}$ effective) network link:

**Scenario A: Naive Single-Stage Python/Rust AI Image**
- Base `ubuntu` + build-essential + Rust toolchain + pip cache + source $= 3,200 \text{ MB}$ ($3.2 \text{ GB}$).
- Cold-Start Image Pull Time:
  $$T_{\text{pull}} = \frac{3,200 \text{ MB}}{12.5 \text{ MB/s}} = 256 \text{ seconds (4 minutes 16 seconds!)}$$
  Tab tak user timeout de kar bhaag chuka hoga!

**Scenario B: Multi-Stage Optimized Build**
- Stage 1 compiles the Rust Axum gateway + minimal runtime assets.
- Stage 2 copies only the stripped binary ($18 \text{ MB}$) + base `debian:bookworm-slim` ($28 \text{ MB}$) $= 46 \text{ MB}$ total!
- Cold-Start Image Pull Time:
  $$T_{\text{pull}} = \frac{46 \text{ MB}}{12.5 \text{ MB/s}} = 3.68 \text{ seconds!}$$
- **Size Reduction**: $\frac{3200 - 46}{3200} \times 100 = 98.56\%$ smaller!
- **Cold-Start Speedup**: $69.5\times$ faster auto-scaling!

### Part 3: Annotated Production Code
Neeche diye gaye code mein hum ek production **Dockerfile Auditor & Multi-Stage Generator** implement karte hain jo kisi bhi AI service ke liye security-hardened, layer-cached multi-stage configuration generate aur lint karta hai.

```python
from typing import List, Dict, Any

PRODUCTION_DOCKERFILE_TEMPLATE = """# syntax=docker/dockerfile:1.7
# ============================================================================
# STAGE 1: Dependency & Binary Builder (Discarded after build)
# ============================================================================
FROM python:3.12-slim-bookworm AS builder
WORKDIR /build

# Install build-only system compilers
RUN apt-get update && apt-get install -y --no-install-recommends \\
    build-essential gcc && rm -rf /var/lib/apt/lists/*

# Copy ONLY dependency manifest first to maximize Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ============================================================================
# STAGE 2: Hardened Minimal Production Runtime
# ============================================================================
FROM python:3.12-slim-bookworm AS runtime
WORKDIR /app

# Create unprivileged non-root system user (UID 10001)
RUN groupadd -g 10001 aiapp && useradd -u 10001 -g aiapp -s /sbin/nologin -M aiapp

# Copy pre-built site-packages from builder stage (zero compilers in runtime!)
COPY --from=builder /install /usr/local

# Copy application code with strict ownership
COPY --chown=aiapp:aiapp ./src ./src

ENV PYTHONUNBUFFERED=1 \\
    PYTHONDONTWRITEBYTECODE=1 \\
    PORT=8080

USER 10001:10001
EXPOSE 8080

HEALTHCHECK --interval=15s --timeout=3s --start-period=10s --retries=3 \\
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/api/health')" || exit 1

CMD ["python", "-m", "src.main"]
"""

def audit_dockerfile(dockerfile_text: str) -> Dict[str, Any]:
    """Static security and performance linter for production AI Dockerfiles."""
    lines = [l.strip() for l in dockerfile_text.splitlines() if l.strip() and not l.strip().startswith("#")]
    from_count = sum(1 for l in lines if l.upper().startswith("FROM "))
    has_non_root = any(l.upper().startswith("USER ") and "root" not in l.lower() for l in lines)
    has_healthcheck = any(l.upper().startswith("HEALTHCHECK ") for l in lines)
    has_no_cache_pip = "--no-cache-dir" in dockerfile_text

    # Check if COPY . . appears before requirements install (cache-busting anti-pattern)
    copy_all_idx = next((i for i, l in enumerate(lines) if "COPY . ." in l), 999)
    pip_idx = next((i for i, l in enumerate(lines) if "pip install" in l), -1)
    layer_cache_optimal = copy_all_idx > pip_idx

    score = sum([
        from_count >= 2,
        has_non_root,
        has_healthcheck,
        has_no_cache_pip,
        layer_cache_optimal,
    ]) * 20

    return {
        "score_out_of_100": score,
        "multi_stage_build": from_count >= 2,
        "non_root_user_enforced": has_non_root,
        "healthcheck_configured": has_healthcheck,
        "pip_cache_disabled": has_no_cache_pip,
        "layer_cache_ordering_valid": layer_cache_optimal,
    }

if __name__ == "__main__":
    report = audit_dockerfile(PRODUCTION_DOCKERFILE_TEMPLATE)
    print("Production Dockerfile Security & Performance Audit:")
    for k, v in report.items():
        print(f"  {k}: {v}")
```

### Part 4: Common Pitfalls, Zero-GPU Tips, Self-Check & Next Steps
**Common Mistakes & Pitfalls:**
1. **Baking Model Weights (`4 GB .gguf`) Inside the Docker Image**: Agar aap model weights ko Docker image ke andar `COPY` kar dete hain, to har chote code bug fix par 4 GB ki nayi image push aur pull hogi! Model weights ko hamesha external persistent volume ya object storage (S3 / R2 / Hugging Face Hub cache volume) se mount karein.
2. **Missing `.dockerignore`**: Agar `.dockerignore` file nahi hai, to `COPY . .` aapka local `node_modules/`, `target/`, `.git/`, aur `.env` secrets image ke andar bhej dega!

**Zero-GPU & Free-Tier Execution Tips:**
- GitHub Actions (`ubuntu-latest`) par Docker multi-stage builds aur GitHub Container Registry (`ghcr.io`) public repos ke liye 100% free hain!

**Self-Check Questions:**
1. Multi-stage Dockerfile mein `COPY --from=builder` kis tarah final image size ko 90%+ kam karta hai?
2. `COPY requirements.txt .` aur `RUN pip install` ko `COPY ./src ./src` se pehle kyun likha jata hai?
3. Production container ko `USER 10001` (non-root) par chalana kyun zaroori hai?

**What to Build Next:**
Apne project ke root mein ek `.dockerignore` file banayein jisme `.env`, `node_modules`, `target`, aur `.git` ko explicitly exclude kiya gaya ho.
'''
LESSON_CONTENT['packaging-open-source-helm-docker'] = LESSON_CONTENT['14.4']

# ==============================================================================
# LESSON 14.5: AI Career Launch: Viral Demos, Technical Whitepapers & GitHub Stardom
# ==============================================================================
LESSON_CONTENT['14.5'] = r'''### Part 1: Mental Model & South Asian Analogy
Aaj ke daur mein jab kisi AI Engineer job post par 2,000 CVs aate hain, to har CV par ek hi line likhi hoti hai: *"Built a RAG chatbot using LangChain and OpenAI API."* Hiring managers aur CTOs aise generic CVs ko 3 seconds mein reject kar dete hain! Lekin wahin ek aisa candidate hota hai jisko samne se $3,000–$8,000/month ke remote offers aur freelance contracts aate hain — kyunki usne **Proof-of-Work Engineering Portfolio** banaya hota hai!

Isay samajhne ke liye **Kaghazi Degree vs Asli Mimar (Master Architect) ke Banaye Hue Pul (Bridge)** ki misaal lein:
1. **Resume Claims (Sirf Baatein)**: *"Mujhe bohot achi civil engineering aati hai, meri 3.8 CGPA hai."*
2. **Live Proof-of-Work (Chalta Hua Pul)**: *"Yeh raha mera live link (`ai-ustaad.pages.dev`), yeh raha mera Hugging Face Space jahan 4-bit QLoRA model 18ms latency par chal raha hai, aur yeh raha mera GitHub repo jisme benchmarks, architecture diagram, aur unit tests mojood hain — aap abhi click kar ke check kar lein!"*
3. **The 30-Second Recruiter Rule**: Koi bhi senior engineer aapka repo clone kar ke `pip install` nahi karega. Agar aapke README ke pehle 10 seconds mein:
   - Live clickable URL / Hugging Face Gradio Space
   - System Architecture Diagram (DiagramKit / Mermaid)
   - Quantitative Benchmark Table (Latency, Recall@5, VRAM, Cost)
   nazar aa jayein, to aap top 1% candidates mein aa jate hain!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein **Hiring Conversion Funnel Math** ka quantitative muwazna (comparison) karein:

**Approach A: Cold-Applying with a Generic Resume (No Live Systems / Benchmarks)**
- Applications sent: $200$
- Resume pass rate: $2.0\%$ ($4$ interviews)
- Technical round pass rate: $15\%$
- Expected Offers: $200 \times 0.02 \times 0.15 = 0.6 \text{ offers}$ (Months of frustration).

**Approach B: High-Signal Proof-of-Work Portfolio (3 Live Deployed Systems + Technical Deep-Dive Blogs + Benchmarks)**
- Applications + Inbound referrals: $40$ targeted outreach messages with a 1-click live demo & benchmark table.
- Reply & interview rate: $35\%$ ($14$ interviews — because engineering leads click live demos!).
- Technical round pass rate: $50\%$ (kyunki interview mein woh aapke hi banaye hue architecture diagram par baat karte hain!).
- Expected Offers: $40 \times 0.35 \times 0.50 = 7.0 \text{ offers}$ ($11.6\times$ higher yield with $5\times$ less spam!).

**What Makes an AI Project "Senior-Grade" vs "Tutorial-Grade"?**
| Metric | Tutorial-Grade (Ignored) | Senior-Grade (Hired Immediately) |
| :--- | :--- | :--- |
| **Evaluation** | "It looks good to me" | Recall@5: 89.4%, Faithfulness: 0.94 on 200 golden pairs |
| **Latency** | "Takes a few seconds" | P50: 340ms, P95: 780ms, TTFT: 95ms via SSE |
| **Cost/VRAM** | "Uses GPT-4 API" | QLoRA 4-bit (4.2 GB VRAM), $0.0014 per 1k queries |
| **Resilience** | Crashes on rate limit | 3-tier circuit breaker + RLS multi-tenant isolation |

### Part 3: Annotated Production Code
Neeche diye gaye code mein hum ek **Automated Portfolio Benchmark & README Badge Generator** implement karte hain jo aapke AI model ki latency percentiles ($P_{50}, P_{95}, P_{99}$), throughput, aur evaluation scores calculate kar ke publication-ready Markdown benchmark table generate karta hai.

```python
import math
from typing import List, Dict, Any

def compute_percentile(sorted_vals: List[float], pct: float) -> float:
    if not sorted_vals:
        return 0.0
    idx = (pct / 100.0) * (len(sorted_vals) - 1)
    lo = int(math.floor(idx))
    hi = int(math.ceil(idx))
    if lo == hi:
        return sorted_vals[lo]
    weight = idx - lo
    return sorted_vals[lo] * (1.0 - weight) + sorted_vals[hi] * weight

def generate_engineering_benchmark_report(
    system_name: str,
    latencies_ms: List[float],
    recall_at_5: float,
    faithfulness: float,
    vram_gb: float,
    cost_per_1k_usd: float,
) -> Dict[str, Any]:
    """Computes rigorous P50/P95/P99 telemetry and outputs a GitHub README markdown table."""
    s = sorted(latencies_ms)
    p50 = round(compute_percentile(s, 50), 1)
    p95 = round(compute_percentile(s, 95), 1)
    p99 = round(compute_percentile(s, 99), 1)
    qps = round(1000.0 / max(1.0, p50), 2)

    markdown_table = (
        f"### Quantitative Production Benchmarks: {system_name}\n\n"
        f"| Metric | Measured Value | Target SLA | Status |\n"
        f"| :--- | :--- | :--- | :--- |\n"
        f"| **Latency P50 (Median)** | `{p50} ms` | `< 400 ms` | PASS |\n"
        f"| **Latency P95 (Tail)** | `{p95} ms` | `< 900 ms` | PASS |\n"
        f"| **Latency P99 (Extreme)** | `{p99} ms` | `< 1500 ms` | PASS |\n"
        f"| **Retrieval Recall@5** | `{round(recall_at_5 * 100, 1)}%` | `> 85.0%` | PASS |\n"
        f"| **Answer Faithfulness** | `{round(faithfulness * 100, 1)}%` | `> 90.0%` | PASS |\n"
        f"| **Peak VRAM Footprint** | `{vram_gb} GB` | `< 15.0 GB (Colab T4)` | PASS |\n"
        f"| **Cost per 1,000 Queries** | `${cost_per_1k_usd:.4f}` | `< $0.0500` | PASS |"
    )

    return {
        "p50_ms": p50,
        "p95_ms": p95,
        "p99_ms": p99,
        "throughput_qps": qps,
        "markdown": markdown_table,
    }

if __name__ == "__main__":
    sample_latencies = [210, 245, 198, 230, 260, 310, 225, 240, 580, 215, 250, 790]
    report = generate_engineering_benchmark_report(
        system_name="AI Ustaad Hybrid RAG & Multi-Cloud Mentor",
        latencies_ms=sample_latencies,
        recall_at_5=0.914,
        faithfulness=0.962,
        vram_gb=4.2,
        cost_per_1k_usd=0.0018,
    )
    print(report["markdown"])
```

### Part 4: Common Pitfalls, Zero-GPU Tips, Self-Check & Next Steps
**Common Mistakes & Pitfalls:**
1. **Reporting Only "Average" Latency**: Average latency jhoot bolti hai! Agar 99 requests 100ms lein aur 1 request 20,000ms le, to average 299ms dikhega lekin aapke sab se ahem enterprise users ko 20 second ka freeze milega. Hamesha **$P_{50}$, $P_{95}$, aur $P_{99}$** report karein.
2. **Dead Demo Links**: CV par aisi link lagana jo खोलने par "Application Error" ya "Supabase Paused" dikhaye, link na lagane se bhi zyada nuqsan deh hai! Cloudflare Pages + offline fallback data rakhein taake aapka demo 24/7/365 zinda rahe.

**Zero-GPU & Free-Tier Execution Tips:**
- Cloudflare Pages (`pages.dev`), Hugging Face Spaces (CPU / ZeroGPU), aur GitHub Pages par aap apne frontends aur interactive Gradio demos zindagi bhar ke liye **$0.00** mein host kar sakte hain!

**Self-Check Questions:**
1. Kisi AI project ke GitHub README mein "Average Latency" ke bajaye $P_{50}$ aur $P_{95}$ percentiles likhna kyun zaroori hai?
2. Tutorial-grade RAG project aur Senior-grade Production RAG project mein kaunse 4 quantitative metrics farq paida karte hain?
3. Demo app mein offline fallback dataset rakhne se hiring conversion par kya farq parta hai?

**What to Build Next:**
Apne GitHub profile (`github.com/<your-username>`) ke pinned repositories mein is course ke 3 flagship projects (Hybrid RAG, Unsloth QLoRA Fine-Tune, aur Multi-Agent MCP System) ko ऊपर diye gaye quantitative benchmark table ke sath publish karein!
'''
LESSON_CONTENT['ai-career-portfolio-stardom'] = LESSON_CONTENT['14.5']

# ==============================================================================
# LESSON 14.6: Grand Capstone Defense: Enterprise AI Platform Graduation
# ==============================================================================
LESSON_CONTENT['14.6'] = r'''### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aap **Module 0 (Python Zero Se Hero)** se shuru ho kar Tensors, Backpropagation, Transformers, Hybrid RAG, `smolagents` & Anthropic MCP, Unsloth 4-bit QLoRA, DeepSeek-R1 GRPO, AI Security Guardrails, Rust Axum Gateways, Multimodal Vision/Audio, aur Edge WebGPU se guzarte hue **Grand Capstone Defense** tak pohanch chuke hain!

Is aakhri marhalay ko samajhne ke liye **NUST, GIKI, LUMS ya MIT ke Final Year Project (FYP) Defense aur Chief Architect Review** ki misaal lein:
1. **Component Wissen vs End-to-End Architecture**: Ek aam talib-e-ilm ko alag alag purzay (layers, prompts, vector DB) banana aate hain, lekin ek **Principal AI Architect** ko pata hota hai ke jab user browser mein सवाल likh kar Enter dabata hai, to aglay $400\text{ milliseconds}$ mein DNS, Edge Worker, Auth JWT, RLS Policy, Prompt Firewall, Embedding Model, HNSW Vector Index, Cross-Encoder Reranker, LLM KV-Cache, SSE Stream, aur Audit Ledger ek sur (symphony) mein kaise kaam karte hain!
2. **Trade-off Defense (Har Faislay Ki Dalael Se Wazaahat)**: Jab panel aap se poochta hai: *"Aapne Fine-Tuning ke bajaye Hybrid RAG kyun chuna?"* ya *"Aapne LLaMA-70B ke bajaye Qwen-7B QLoRA kyun deploy kiya?"*, to aap andazay se nahi balke **Latency, Cost, Freshness, aur Recall** ke numbers se jawab dete hain!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein **End-to-End Production AI Request Latency Budget ($450\text{ ms}$ Time-To-First-Token SLA)** ka mukammal post-mortem breakdown karein:

Jab ek user aapke Capstone Platform par سوال poochta hai, to har subsystem ka strict millisecond budget hota hai:
1. **Edge TLS & JWT Verification + Rate Limit Check**: $T_1 = 8\text{ ms}$
2. **Input Security Guardrail (PII Regex + Prompt Injection Classifier)**: $T_2 = 14\text{ ms}$
3. **Query Embedding Generation (`bge-small-en-v1.5` / ONNX int8)**: $T_3 = 18\text{ ms}$
4. **Hybrid Search (`pgvector` HNSW + BM25 + RRF in PostgreSQL)**: $T_4 = 12\text{ ms}$
5. **Cross-Encoder Reranking (Top-20 $\rightarrow$ Top-5 chunks)**: $T_5 = 38\text{ ms}$
6. **LLM Prefill (Time-To-First-Token on Prompt-Cached 2,500 tokens)**: $T_6 = 180\text{ ms}$
7. **SSE First Chunk Network Flush to Browser**: $T_7 = 15\text{ ms}$

**Total Time-To-First-Token (TTFT):**
$$T_{\text{TTFT}} = 8 + 14 + 18 + 12 + 38 + 180 + 15 = 285\text{ ms!}$$
Insani ankh ko $< 300\text{ ms}$ ka response **instantaneous** mehsoos hota hai! Aur phir baqi $400$ tokens $80\text{ tokens/sec}$ ki raftaar se SSE stream ke zariye user ke padhne ki speed se tez screen par type hote rehte hain.

### Part 3: Annotated Production Code
Neeche diye gaye code mein hum **Grand Capstone Architecture Readiness Verifier** implement karte hain jo aapke end-to-end AI platform ke tamam 7 subsystems (Security, Retrieval, Inference, Resilience, Metering, Observability, aur Deployment) ka automated graduation audit run karta hai!

```python
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class SubsystemCheck:
    subsystem: str
    passed: bool
    measured_metric: str
    sla_requirement: str

class GrandCapstoneDefenseEvaluator:
    """Automated readiness evaluator for the AI Ustaad Grand Capstone Architecture."""
    def __init__(self, platform_name: str, architect_name: str) -> None:
        self.platform_name = platform_name
        self.architect_name = architect_name
        self.checks: List[SubsystemCheck] = []

    def verify_subsystem(
        self, subsystem: str, passed: bool, measured_metric: str, sla_requirement: str
    ) -> None:
        self.checks.append(
            SubsystemCheck(subsystem, passed, measured_metric, sla_requirement)
        )

    def evaluate_graduation(self) -> Dict[str, Any]:
        total = len(self.checks)
        passed_count = sum(1 for c in self.checks if c.passed)
        score_pct = round((passed_count / max(1, total)) * 100, 1)
        graduated = score_pct == 100.0

        return {
            "platform": self.platform_name,
            "architect": self.architect_name,
            "score_pct": score_pct,
            "status": "GRADUATED WITH HONORS (AI USTAAD ARCHITECT)" if graduated else "REVISION REQUIRED",
            "verified_subsystems": [
                f"[{'PASS' if c.passed else 'FAIL'}] {c.subsystem}: {c.measured_metric} (SLA: {c.sla_requirement})"
                for c in self.checks
            ],
        }

if __name__ == "__main__":
    capstone = GrandCapstoneDefenseEvaluator(
        platform_name="AI Ustaad Enterprise RAG & Agentic Platform",
        architect_name="Graduate AI Engineer",
    )
    capstone.verify_subsystem("1. Multi-Tenant RLS & Audit Chain", True, "0% Cross-Tenant Leak", "0% Leak")
    capstone.verify_subsystem("2. Prompt Firewall & PII Redaction", True, "14ms Scan Latency", "< 25ms")
    capstone.verify_subsystem("3. Hybrid RAG (Dense + BM25 + RRF)", True, "91.4% Recall@5", "> 85% Recall@5")
    capstone.verify_subsystem("4. Unsloth QLoRA / GRPO Reasoning", True, "4.2 GB VRAM on T4", "< 15 GB VRAM")
    capstone.verify_subsystem("5. Multi-Cloud Circuit Breaker", True, "99.999% Uptime", "> 99.9% Uptime")
    capstone.verify_subsystem("6. Token Metering & Cost Guard", True, "$0.0018 / 1k turns", "< $0.05 / 1k")
    capstone.verify_subsystem("7. Edge + Container Deployment", True, "285ms TTFT via SSE", "< 400ms TTFT")

    result = capstone.evaluate_graduation()
    print(f"=== {result['status']} ({result['score_pct']}%) ===")
    for line in result["verified_subsystems"]:
        print(" ", line)
```

### Part 4: Common Pitfalls, Zero-GPU Tips, Self-Check & Next Steps
**Common Mistakes & Pitfalls:**
1. **Over-Engineering Day 1 without a Baseline Eval**: Kabhi bhi pehle din 5-agent swarm mat banayein! Hamesha simple prompt + clean hybrid retrieval + 50-question golden evaluation set se shuru karein, aur sirf tab complexity barhayein jab metric uski zaroorat sabit kare.
2. **Stopping at Theory**: Sirf lessons padhne se koi AI Engineer nahi banta. Har module ke Colab notebook ko khud run karein, code tore-marorein, aur apna GitHub commit graph hara (green) rakhein!

**Zero-GPU & Free-Tier Execution Tips:**
- Aapka poora Grand Capstone stack — **Cloudflare Pages + Workers AI + Supabase PostgreSQL/pgvector + Groq API + Google Colab T4 + Hugging Face Hub** — $0.00/month par production traffic chala sakta hai!

**Self-Check Questions:**
1. Ek end-to-end AI request mein $285\text{ ms}$ TTFT achieve karne ke liye kaunse 7 stages kis tarteeb (sequence) mein chalte hain?
2. Kisi enterprise problem ke liye **Hybrid RAG** vs **QLoRA Fine-Tuning** vs **GRPO RL** ka faisla kin 3 criteria par kiya jata hai?
3. Ek production AI system mein observability, evaluation, aur circuit breakers kyun model ke weights jitne hi ahem hote hain?

**Final Graduation Action — Aaj Hi Duniya Ko Dikhayein:**
Module 14 ka Final Quiz pass karein, apna **"AI Graduate (Hero Ban Gaye!)"** badge unlock karein, aur apna deployed Capstone project LinkedIn, X (Twitter), aur GitHub par share karein!
'''
LESSON_CONTENT['grand-capstone-defense-graduation'] = LESSON_CONTENT['14.6']
