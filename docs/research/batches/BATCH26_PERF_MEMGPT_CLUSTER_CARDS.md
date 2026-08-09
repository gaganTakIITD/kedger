# Batch26 — MemGPT / A-MEM / MemoryOS / GraphReader cluster cards

> **Date:** 2026-08-09  
> **Source:** deep-read subagent over `/tmp/kedger-papers/full/{id}.txt`  
> **Kedger already has:** HARD PreCompact · L0 warn 0.70 / flush 0.85 · notebook_walk · HANDOFF_MAX_BYTES=32768 · explicit_only  

**Cluster maintain vs pursue:** KEEP pressure→externalize, heat promote, notebook walk, sealed byte budgets. REJECT product KV layer, Neo4j-as-brain, eager LLM every turn.

---

### 2310.08560 — MemGPT

| Field | Content |
|-------|---------|
| **arxiv_id** | 2310.08560 |
| **title** | MemGPT: Towards LLMs as Operating Systems |
| **kedger_stages** | S1, S2, S3, S7 |
| **problem** | Fixed context windows break multi-session chat and multi-doc QA. |
| **representation** | Main context = RO instructions + RW working + FIFO queue; external = recall DB + archival store. |
| **write_read_forget** | Warn ~70% → pressure msg; flush ~100% → evict ~50% queue + recursive summary to recall. |
| **numbers** | DMR: GPT-4 32.1%→**92.5%**; GPT-4 Turbo 35.3%→**93.4%**. |
| **kedger_lessons** | **KEEP** HARD PreCompact + L0 0.70/0.85. **REJECT** agent self-write alone — hooks autocapture. |
| **refine_candidate** | **no** — pressure path locked |

---

### 2502.12110 — A-MEM

| Field | Content |
|-------|---------|
| **arxiv_id** | 2502.12110 |
| **title** | A-Mem: Agentic Memory for LLM Agents |
| **kedger_stages** | S3, S4, S5, S7 |
| **problem** | Static predefined memory ops can’t adapt structure. |
| **representation** | Zettelkasten atomic notes + embeddings + LLM link/evolve. |
| **numbers** | LoCoMo GPT-4o-mini Temporal F1 **45.85** vs MemGPT 25.52; tokens ~**2,520** vs ~**16,910** (**85–93%** fewer). |
| **kedger_lessons** | **KEEP** atomic claims ≈ Anchors. **REJECT** eager LLM link+evolve every turn; silent in-place overwrite → SUPERSEDES. Neo4j not required. |
| **refine_candidate** | **no** — claim extract covers atomicity |

---

### 2506.06326 — Memory OS of AI Agent

| Field | Content |
|-------|---------|
| **arxiv_id** | 2506.06326 |
| **title** | Memory OS of AI Agent (MemoryOS) |
| **kedger_stages** | S2–S5, S7 |
| **problem** | Flat FIFO fails long-dialogue coherence / persona. |
| **representation** | STM pages → MTM segments (θ=0.6) → LPM; Heat=αN+βL+γR, τ=5. |
| **numbers** | LoCoMo GPT-4o-mini avg **+49.11% F1 / +46.18% BLEU-1** over baselines (paper); efficiency **3,874** tokens / **4.9** calls. |
| **kedger_lessons** | **KEEP** `HEAT_TAU=5`, `SEGMENT_THETA=0.60`. **REJECT** eager LLM trait rewrite every turn. |
| **refine_candidate** | **no** — heat/θ aligned |

---

### 2603.04428 — Agent Memory Below the Prompt (Q4 KV)

| Field | Content |
|-------|---------|
| **arxiv_id** | 2603.04428 |
| **title** | Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge |
| **kedger_stages** | S1 (infra) |
| **numbers** | Q4 **4×** agent density; TTFT **27×** vs cold prefill (Gemma 4K). |
| **kedger_lessons** | **REJECT product KV layer** — serving infra ≠ Anchors. Persistence → sealed packs. |
| **refine_candidate** | **no** — REJECT |

---

### 2509.17396 — EpiCache

| Field | Content |
|-------|---------|
| **arxiv_id** | 2509.17396 |
| **title** | Episodic KV Cache Management for Long Conversational QA |
| **kedger_stages** | S1 (infra), S3 (episode analogy) |
| **numbers** | Peak mem **9.6 GB** vs Full **36.3** (~**4×**); EpiCache Single Acc **54.6** vs Full **60.3** @8K RealTalk. |
| **kedger_lessons** | Episode clustering ≈ cognify boundaries as **symbolic** L2 — **REJECT** product KV. |
| **refine_candidate** | **no** — REJECT product KV |

---

### 2606.17872 — AnchorKV

| Field | Content |
|-------|---------|
| **arxiv_id** | 2606.17872 |
| **title** | Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor |
| **kedger_stages** | S1 (infra); S6/S8 analogy |
| **numbers** | FastKV can **raise** jailbreak ASR; AnchorKV λ=10 ASR **−81%** vs FastKV peak; LongBench loss &lt;0.5 pt at small λ. |
| **kedger_lessons** | Name ≠ Kedger Anchors. **REJECT product KV.** Hydrate must not drop policy Anchors under byte pressure. |
| **refine_candidate** | **no** — REJECT |

---

### 2412.10319 — SCBench

| Field | Content |
|-------|---------|
| **arxiv_id** | 2412.10319 |
| **title** | SCBench: A KV Cache-Centric Analysis of Long-Context Methods |
| **kedger_stages** | S1 (infra), S7 (reuse analogy) |
| **numbers** | Query-conditioned compress fails when next query differs; Retr.String collapses under aggressive τ. |
| **kedger_lessons** | Multi-turn hydrate = re-rank durable Anchors per query under **32KB**, not one-shot drop of store. **REJECT** product KV roadmap merge. |
| **refine_candidate** | **no** — eval design only |

---

### 2406.14550 — GraphReader

| Field | Content |
|-------|---------|
| **arxiv_id** | 2406.14550 |
| **title** | GraphReader: Building Graph-based Agent to Enhance Long-Context Abilities of LLMs |
| **kedger_stages** | S3, S5, S7, S8 |
| **numbers** | Defaults: window 4k, chunk ≤2k, N=5 starts, ≤10 calls/path; HotpotQA ablation plan/node selection matter. |
| **kedger_lessons** | **KEEP** `notebook_walk` + call budget. **REJECT** unbounded walk / Neo4j-as-brain. |
| **refine_candidate** | **no** — notebook_walk done |

---

## Cluster verdict

| KEEP | REJECT |
|------|--------|
| HARD PreCompact + L0 0.70/0.85 | Product KV (Q4, EpiCache, AnchorKV, SCBench serving) |
| Heat τ=5, segment θ≈0.6, atomic claims | Neo4j-as-brain / Mem0 graph DB as SoT |
| Budgeted notebook_walk under 32KB | Eager LLM link/evolve every turn |
| explicit_only + sealed handoff | Flat FIFO as sole LTM; silent Anchor overwrite |
