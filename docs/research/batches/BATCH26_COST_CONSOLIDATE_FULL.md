# Batch 26 — Cost · Consolidate · Online/Offline Memory (Kedger)

> **Date:** 2026-08-09  
> **Branch:** `Cursor/batch26-perf-roadmap-fb37`  
> **Scope:** Agent-memory systems that win on **token/API cost** via online/offline split, dual-path evidence, sleep-time consolidate — mapped to Kedger L0→L4.  
> **Method:** arXiv HTML/ar5iv → `/tmp/kedger-papers/full/{id}.{html,txt}`; mechanism cards from body text (not abstract-only).  
> **Companion:** [`BATCH26_RETRIEVE_KV_PERF_FULL.md`](BATCH26_RETRIEVE_KV_PERF_FULL.md) · [`BATCH26_PERF_LIGHTMEM_CLUSTER_CARDS.md`](BATCH26_PERF_LIGHTMEM_CLUSTER_CARDS.md) · [`BATCH26_PERF_MEMGPT_CLUSTER_CARDS.md`](BATCH26_PERF_MEMGPT_CLUSTER_CARDS.md) · [`PERFORMANCE_PROGRESS_ROADMAP.md`](../PERFORMANCE_PROGRESS_ROADMAP.md)

---

## 0. Honesty table

| Status | Count | Notes |
|--------|------:|-------|
| **FULL** new body deep-read (this memo) | **10** | LightMem, LightMem-repro, LeanMem, SLM-agent-memory, All-Mem, HeLa-Mem, A-MEM, Memory OS, MemGPT (re-read body), A-MemGuard |
| **Substantial body on disk** | yes | all IDs below ≥20KB txt except where noted |
| **Not claimed** | — | Did not FULL-read entire 1674 scrape |

**Cache:** `/tmp/kedger-papers/full/`

---

## 1. Mechanism cards

### 1.1 LightMem — Lightweight and Efficient Memory-Augmented Generation  
**arXiv:2510.18866** · Fang et al. · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S3, S7 |
| **problem** | Tight coupling of memory update with online inference → long latency; historical info poorly leveraged. |
| **representation** | Three stages: (1) **sensory** lightweight compression + topic grouping; (2) **topic-aware STM** consolidate/summarize; (3) **LTM with sleep-time update** — offline consolidation decoupled from online inference. |
| **write / read / forget** | Write online filter → topic groups; offline sleep consolidate into LTM; read retrieves structured entries. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent. |
| **numbers** | LongMemEval / LoCoMo; GPT & Qwen: QA **+7.7% / +29.3%** vs strong baselines; total tokens **↓ up to 38× / 20.9×**; API calls **↓ 30× / 55.5×**; pure online test-time cost **↓ up to 106× / 117×**. |
| **kedger_lessons** | (1) Kedger already offline-ish cognify — make **sleep-time merge queue** explicit. (2) Topic grouping ≈ pre-L2 compress. (3) Do **not** put LLM consolidate on SessionStart. (4) Cost wins come from decoupling, not denser vectors. |
| **metric_impact** | Token/API per QA; online latency; LongMemEval/LoCoMo accuracy. |
| **refine_candidate** | **yes** — P1 sleep-time merge + topic pre-group |

---

### 1.2 Reproducing LightMem — Naive RAG Is Just as Good  
**arXiv:2607.29104** · Zhou & Wang · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7 |
| **problem** | LightMem claims unclear under retriever swap; is constructed memory necessary? |
| **representation** | Reproduce LightMem vs **Naive RAG** over raw user turns; ablate retriever only. |
| **write / read / forget** | Constructed store vs raw-turn index. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **numbers** | Retriever swap on fixed LightMem store: accuracy **58.1% → 75.5%**. Naive RAG generally better at matched depths; LightMem better mainly under **tight answering-token budgets**. Oracle: construction **drops** some answer-relevant info. |
| **kedger_lessons** | (1) Kedger must not claim “memory beats RAG” broadly — claim **policy survival + sealed handoff under tight budgets**. (2) Dual-path: keep raw-ish Evidence/transcript optional under byte quotas (LeanMem-aligned). (3) Fixtures must ablate retrieve depth vs pack size. |
| **metric_impact** | Accuracy vs answering-token budget; construction loss oracle. |
| **refine_candidate** | **yes** — P0 dual-path Evidence+Anchors under 32KB |

---

### 1.3 LeanMem — Simple and Efficient Long-Term Memory for LLM Agents  
**arXiv:2608.03463** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Uniform summarize/retrieve → either token blow-up or irreversible loss of fine-grained evidence. |
| **representation** | Filter low-value → store as **profile** (compact) / **event** (temporal) / **record** (source-grounded). Maintenance updates only evolving events. Inference: **adaptive evidence composition** — select memory types + allocate retrieval budgets by query. |
| **write / read / forget** | Controlled write; selective evolution; adaptive read. |
| **conflict** | Silent on explicit contradiction graph. |
| **privacy** | Silent. |
| **numbers** | LoCoMo & LongMemEval-S; GPT-4.1-mini & Qwen3-8B: accuracy **up to +15.1 points** over strongest memory baseline at lowest/near-lowest construction & inference cost. |
| **kedger_lessons** | (1) Map profile→Anchors, event→Episodes, record→Evidence/transcript. (2) **Separate byte quotas** in 32KB pack. (3) Query-adaptive composition ≈ topic/purpose hydrate. |
| **metric_impact** | Accuracy vs construction/inference cost. |
| **refine_candidate** | **yes** — P0 dual-path packing |

---

### 1.4 Lightweight LLM Agent Memory with Small Language Models  
**arXiv:2604.07798** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7 |
| **problem** | Full LLM for memory ops is expensive. |
| **representation** | Use **small LMs** for memory write/retrieve helpers. |
| **write / read / forget** | SLM-assisted memory pipeline. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **numbers** | Body emphasizes cost reduction vs full-LLM memory controllers (see paper tables). |
| **kedger_lessons** | Reinforces Kedger **deterministic cognify** — even cheaper than SLM controllers; keep LLM distill Phase F. |
| **metric_impact** | Memory-op cost vs quality. |
| **refine_candidate** | no (maintain deterministic path) |

---

### 1.5 All-Mem — Agentic Lifelong Memory via Dynamic Topology Evolution  
**arXiv:2603.19595** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7 |
| **problem** | Lifelong agents: write forever + retrieve under fixed context/latency — degradation via redundant/outdated/noisy context. |
| **representation** | Online: retrieve from **bounded visible surface**, expand typed links under hop/candidate budgets, re-rank. Offline: LLM diagnoser proposes Split/Merge/Update with gating. |
| **write / read / forget** | Topology evolution offline; bounded online search. |
| **conflict** | Merge/Update operators — soft conflict handling. |
| **privacy** | Silent. |
| **numbers** | Emphasizes bounded coarse search cost via visible surface (see paper experiments). |
| **kedger_lessons** | (1) Name Kedger’s `anchors[:5]` seed as **visible surface**. (2) Keep expand caps. (3) Offline Split/Merge ≈ sleep-time Anchor merge — **gated**, not continuous LLM. |
| **metric_impact** | Latency vs recall as bank grows. |
| **refine_candidate** | **yes** — P1 visible-surface + expand caps fixtures |

---

### 1.6 HeLa-Mem — Hebbian Learning and Associative Memory  
**arXiv:2604.16839** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5 |
| **problem** | Associative strengthening of useful links over time. |
| **representation** | Hebbian-style updates on memory associations. |
| **write / read / forget** | Strengthen co-activated links; decay unused. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **kedger_lessons** | Edge weights on ABOUT/SUPPORTS could heat with recurrence (`HEAT_TAU=5` already) — optional refine, not P0. |
| **metric_impact** | Associative hit rate over sessions. |
| **refine_candidate** | no (covered by recurrence promote) |

---

### 1.7 A-MEM — Agentic Memory for LLM Agents  
**arXiv:2502.12110** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5 |
| **problem** | Atomic notes need write-time linking and evolution. |
| **representation** | Atomic memories + links + evolution ops. |
| **write / read / forget** | Write-time link; evolve structure. |
| **conflict** | Evolution may supersede. |
| **privacy** | Silent. |
| **kedger_lessons** | Aligns Anchor atomicity + graph edges; maintain claim-extract → promote. |
| **metric_impact** | Multi-session continuity. |
| **refine_candidate** | no (already in spine) |

---

### 1.8 Memory OS of AI Agent  
**arXiv:2506.06326** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1–S3, S7 |
| **problem** | OS-like hierarchy for agent memory. |
| **representation** | Memory OS layers (STM/MTM/LTM style). |
| **write / read / forget** | Hierarchical store with promotion. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **kedger_lessons** | Maps cleanly to L1/L2/L3; maintain MemGPT-like pressure ratios. |
| **metric_impact** | Hierarchy ablations. |
| **refine_candidate** | no |

---

### 1.9 MemGPT — Towards LLMs as Operating Systems  
**arXiv:2310.08560** · Packer et al. · 2023 · **FULL** (body re-read)

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7 |
| **problem** | Bounded context → need hierarchical memory + control. |
| **representation** | Main context vs archival; functions to page memory. |
| **write / read / forget** | Explicit page in/out; archival store. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **kedger_lessons** | **Maintain** L0 warn/flush + PreCompact; archival ≈ Anchors+packs — not KV. |
| **metric_impact** | Task completion under memory pressure. |
| **refine_candidate** | no (maintain) |

---

### 1.10 A-MemGuard — Proactive Defense for Agent Memory  
**arXiv:2510.02373** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6 |
| **problem** | Poisoned / adversarial memory writes. |
| **representation** | Defense framework around agent memory. |
| **write / read / forget** | Gate writes; audit. |
| **conflict** | Adversarial contradictions. |
| **privacy** | Integrity of memory. |
| **kedger_lessons** | Reinforces redact + explicit share; not a perf P0 — security track. |
| **metric_impact** | Attack success rate. |
| **refine_candidate** | no (security backlog) |

---

## 2. Batch refine tickets (into roadmap)

| ID | Ticket | Priority |
|----|--------|----------|
| B26-C1 | Dual-path Evidence + Anchors byte quotas @ 8/16/32KB | **P0** |
| B26-C2 | Sleep-time merge queue (offline Anchor/episode consolidate) | P1 |
| B26-C3 | Visible-surface naming + fixtures for seed[:K] | P1 |

---

## 3. Maintain vs reject

**Maintain:** deterministic cognify; L0→L4; ≤32KB; survival rank; explicit_only.  
**Reject:** eager LLM every turn; GraphRAG rebuilds; replacing Anchors with Naive RAG as SoT.
