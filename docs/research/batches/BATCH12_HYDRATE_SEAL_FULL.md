# Batch 12 — Hydrate · Retrieve · Seal · Crypto Routing (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-300-fb37`  
> **Scope:** Tier-5/6 runway — hydrate/retrieve routing, pack composition, privacy/seal/crypto, memory eval probes. Papers **not** already FULL in CORPUS §2 or Batch4–8. age/Wormhole/MLS/Biscuits/Macaroons already FULL in SEALED_PACK memo — not re-marked.  
> **Method:** Full arXiv HTML (ar5iv fallback) or PDF→text when HTML thin; cache `/tmp/kedger-papers/full/{id}.{html,txt,pdf}`. Mechanism cards only — not abstract skim.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new body deep-read; ID not previously FULL in CORPUS §2 / Batch4–8) | **17** | 2310.17884 (ConfAIde: Contextual Integrity Benchmark…); 2505.23643 (Fides: Securing AI Agents with Informati…); 2601.06966 (RealMem: Realistic Project-Oriented Memo…); 2506.21605 (MemBench: Comprehensive Memory Capabilit…); 2605.27825 (MRMMIA: Membership Inference on Chat-Age…); 2309.04697 (Leakage-Abuse Attacks on Searchable Symm…); 2510.06719 (DP Synthetic Text for RAG Memorization M…); 2511.03506 (HaluMem: Hallucination in Agent Memory E…); 2601.03785 (Membox: Topic-Continuity Long-Range Memo…); 2407.02485 (RankRAG: Unifying Context Ranking with R…); 2505.23052 (RAGRouter: RAG-Aware Query Routing Acros…); 2505.23841 (SkewRoute: Training-Free KG-RAG LLM Rout…); 2601.12331 (ppRAG / CAPRISE: Distance-Preserving Enc…); 2509.21325 (PIR-RAG: Private Information Retrieval f…); 2604.26525 (PRAG: End-to-End Privacy-Preserving RAG …); 2212.10496 (HyDE: Hypothetical Document Embeddings f…); 2312.10997 (Retrieval-Augmented Generation for LLMs:…) |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped (no invented content)** | **0** | Fides (`2505.23643`) via PDF extract; all carded IDs have `.txt` ≥23k chars |
| **Identified / cached but not carded (room)** | 0 | — |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt` (all FULL IDs present).

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded. Numbers are from paper text/tables.

---

## 1. Mechanism cards

### 1.1 ConfAIde  
**arXiv:2310.17884** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6, S7, S8 |
| **problem** | Privacy evals focus on training leakage, not contextual inappropriateness at inference. |
| **representation** | ConfAIde benchmark (contextual integrity): 4 tiers ending in theory-of-mind privacy reasoning. |
| **write / read / forget** | Eval-only: models decide disclose/withhold given social context. Not a memory store. |
| **conflict** | Conflicts between utility vs contextual norms — distinct from factual SUPERSEDES. |
| **privacy** | GPT-4 leaks in human-wouldn't contexts ~39%; ChatGPT ~57% on hardest tier. |
| **Kedger lessons** | (1) Inv-Scope must include contextual appropriateness, not only ACL tags. (2) S7 packs need purpose binding (CaMeL/Fides alignment). (3) ConfAIde tier-4 as seal regression fixture. |
| **metric_impact** | Contextual disclosure accuracy vs human judgments across four tiers. |
| **refine_candidate** | **yes** |

---

### 1.2 Fides  
**arXiv:2505.23643** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | Tool agents lack planner-side IFC — untrusted retrieved text hijacks actions. |
| **representation** | Fides planner IFC with confidentiality+integrity labels; policy engine allow/deny; hide/reveal primitives; PIA defenses. |
| **write / read / forget** | Read = labeled memory/tool outputs constrained by policy at plan time. Write = labeled actions checked before execution. |
| **conflict** | Integrity labels block conflicting unauthorized updates. |
| **privacy** | Core IFC paper for sealed handoff — pack inherits max label. |
| **Kedger lessons** | (1) Hydrated Evidence is untrusted data plane (pair with CaMeL). (2) Map visibility classes → labels. (3) Sealed pack plaintext label = max included row sensitivity. |
| **metric_impact** | Policy violation rate on agent tasks; deterministic vs probabilistic PIA tradeoffs. |
| **refine_candidate** | **yes** |

---

### 1.3 RealMem  
**arXiv:2601.06966** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Benchmarks cover chit-chat or narrow tasks, not multi-session **project** evolution. |
| **representation** | RealMem: 2000+ dialogues, 11 project scenarios; synthesis pipeline with project foundation + multi-agent generation + schedule/memory management. |
| **write / read / forget** | Eval harness for memory systems on evolving project state — not a store. |
| **conflict** | Projects require reconciling shifting goals — implicit conflict over time. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Add RealMem-style project fixtures to eval harness. (2) Track schedule + memory co-evolution SLIs. (3) Cross-session dependency graph for hydrate tests. |
| **metric_impact** | Accuracy on natural user queries over long project arcs. |
| **refine_candidate** | **yes** |

---

### 1.4 MemBench  
**arXiv:2506.21605** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Memory evals lack diversity across memory levels and interaction modes. |
| **representation** | MemBench dataset: **factual vs reflective** memory levels × **participation vs observation** scenarios; metrics for effectiveness, efficiency, capacity. |
| **write / read / forget** | Benchmark protocol — agents tested under varied interaction modes. |
| **conflict** | Reflective memory introduces belief revision tests. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Extend EVAL_HARNESS with participation/observation modes. (2) Measure capacity separately from accuracy. (3) Reflective tier ≈ S3 cognify quality tests. |
| **metric_impact** | Effectiveness/efficiency/capacity scores across MemBench splits. |
| **refine_candidate** | **yes** |

---

### 1.5 MRMMIA  
**arXiv:2605.27825** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6, S7 |
| **problem** | Chat-agent memory stores vulnerable to membership inference via crafted recall queries. |
| **representation** | MRMMIA: generate recall queries → probe responses → score membership of candidate records. |
| **write / read / forget** | Attack on read path; poisons/scores whether specific memory present. |
| **conflict** | Silent. |
| **privacy** | Core MIA on memory APIs — complements MEXTRA/MemLeak. |
| **Kedger lessons** | (1) 404 not 403 on denied hydrate; minimize existence oracles. (2) Rate-limit memory probes. (3) Constant-shape responses for absent vs forbidden. |
| **metric_impact** | MIA AUC vs defenses; ablations on scoring weights. |
| **refine_candidate** | **yes** |

---

### 1.6 Leakage-Abuse Attacks on Searchable Symmetric Encryption  
**arXiv:2309.04697** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6, S7 |
| **problem** | Searchable encryption claims forward/backward privacy but leakage-abuse still recovers keywords. |
| **representation** | Volume/access-pattern attacks on SSE schemes; query recovery from observed search traces. |
| **write / read / forget** | Read-path leakage model for encrypted search indexes. |
| **conflict** | Silent. |
| **privacy** | Do **not** rely on encrypted semantic search alone for Inv-Scope. |
| **Kedger lessons** | (1) Partition plaintext indexes by visibility under Inv-Scope gate, seal for transit. (2) SSE metadata is an oracle — avoid for cross-tenant memory. (3) Pair with CAPRISE/PIR only with access-pattern analysis. |
| **metric_impact** | Keyword recovery success under leakage profiles. |
| **refine_candidate** | **no** |

---

### 1.7 DP Synthetic Text for RAG Memorization Mitigation  
**arXiv:2510.06719** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6 |
| **problem** | RAG corpora memorization risk when publishing shared digests. |
| **representation** | DP synthetic text generation to populate RAG indexes with reduced memorization. |
| **write / read / forget** | Write = synthetic shared corpus; Read = standard RAG over synthetic store. |
| **conflict** | Silent. |
| **privacy** | Optional path for shareable digests — not substitute for capabilities. |
| **Kedger lessons** | (1) `repo_shared_safe` synthetic summaries may use DP when publishing. (2) Never replace per-row capability checks. (3) Measure memorization vs utility tradeoff. |
| **metric_impact** | Memorization probes vs answer quality on DP-synthetic index. |
| **refine_candidate** | **no** |

---

### 1.8 HaluMem  
**arXiv:2511.03506** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7, S8 |
| **problem** | Memory systems hallucinate false user facts that pollute long-term store. |
| **representation** | HaluMem benchmark measuring hallucinated memory insertion and downstream QA corruption. |
| **write / read / forget** | Eval of write+read fidelity — detects false memory writes. |
| **conflict** | False memories vs ground truth — SUPERSEDES/detection needed. |
| **privacy** | False memories may include inferred private traits. |
| **Kedger lessons** | (1) Cognify write audit for unsupported fact inserts. (2) S8 `why` must cite Evidence for each Anchor claim. (3) HaluMem-style fixture in eval harness. |
| **metric_impact** | Hallucination rate in memory writes + downstream QA F1. |
| **refine_candidate** | **yes** |

---

### 1.9 Membox  
**arXiv:2601.03785** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Long-range agent memory loses **topic continuity** across sessions. |
| **representation** | Membox weaves topic-continuity threads through long-range memory indexing/retrieval. |
| **write / read / forget** | Write = topic-thread metadata on episodes. Read = continuity-aware retrieval spanning sessions. |
| **conflict** | Topic drift can fork threads — needs merge/supersede. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Topic thread id on L2 episodes (extends DialSTART/HyperSeg). (2) Hydrate boosts within-thread Evidence first. (3) Idle boundary + topic switch triggers cognify. |
| **metric_impact** | Long-range QA with topic switches vs flat retrieval. |
| **refine_candidate** | **yes** |

---

### 1.10 RankRAG  
**arXiv:2407.02485** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | RAG prepends noisy contexts; separate rerankers add latency/complexity. |
| **representation** | RankRAG instruction-tunes one LM for **context ranking** (True/False relevance) and **generation**; retrieve→rerank top-k→generate pipeline. |
| **write / read / forget** | Read-only over corpus; ranks retrieved passages before pack compile. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S7 pack compile includes rerank pass before truncate. (2) Train/tune lightweight ranker head or prompt for Evidence scoring. (3) Keep k≪N like RankRAG top-k filter. |
| **metric_impact** | QA accuracy on biomedical benchmarks vs separate reranker+LLM. |
| **refine_candidate** | **yes** |

---

### 1.11 RAGRouter  
**arXiv:2505.23052** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | Different LLMs excel under different retrieved contexts; static router ignores RAG shift. |
| **representation** | RAGRouter: contrastive embeddings for query+documents → route among multiple RAG-augmented LLMs. |
| **write / read / forget** | Read-path routing only. |
| **conflict** | Silent. |
| **privacy** | Routing metadata must not leak unauthorized doc classes. |
| **Kedger lessons** | (1) Hydrate service can route pack to model tier by query+Evidence embedding. (2) Score-threshold latency modes. (3) Document-conditioned routing beats query-only. |
| **metric_impact** | Win rate vs best single LLM across knowledge-intensive tasks. |
| **refine_candidate** | **no** |

---

### 1.12 SkewRoute  
**arXiv:2505.23841** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7 |
| **problem** | KG-RAG multi-hop queries need expensive large LLMs; training routers costly. |
| **representation** | SkewRoute: training-free routing using **skewness** of retrieval score distributions — low skew → small LLM, high skew → large LLM. |
| **write / read / forget** | Read-path compute router for KG-RAG. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Use retrieval score skew as S7 compute/latency knob. (2) >3× routing effectiveness vs baselines at ~0.001× runtime. (3) Pairs with PropRAG/HippoRAG scorers. |
| **metric_impact** | Cost-quality curve on KG-RAG benchmarks vs uniform large model. |
| **refine_candidate** | **yes** |

---

### 1.13 ppRAG / CAPRISE  
**arXiv:2601.12331** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6, S7 |
| **problem** | Cloud RAG exposes query embeddings and database vectors. |
| **representation** | ppRAG with **CAPRISE** conditional distance-preserving encryption + **DistanceDP** query perturbation for top-k over encrypted embeddings. |
| **write / read / forget** | Read = encrypted similarity search; write = encrypt outsourced embeddings/docs. |
| **conflict** | Silent. |
| **privacy** | Hides vector geometry except query-to-DB orderings; defends reconstruction/MIA. |
| **Kedger lessons** | (1) Sealed hydrate may use CAPRISE-class encryption for at-rest vector indexes. (2) DistanceDP before encrypt for query privacy. (3) Do not claim SSE alone — combine with capability gates. |
| **metric_impact** | Retrieval accuracy vs plaintext; attack resilience; throughput vs PHE baselines. |
| **refine_candidate** | **no** |

---

### 1.14 PIR-RAG  
**arXiv:2509.21325** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6, S7 |
| **problem** | RAG leaks user queries to service provider during retrieval. |
| **representation** | PIR-RAG: semantic clustering prunes search space + lattice PIR fetches whole clusters; optimizes **RAG-ready latency**. |
| **write / read / forget** | Read = private cluster fetch; client-side embedding→one-hot cluster selection encrypted. |
| **conflict** | Silent. |
| **privacy** | Query-hidden retrieval for sensitive intents. |
| **Kedger lessons** | (1) Sealed handoff can batch-fetch Evidence clusters via PIR. (2) Coarse cluster PIR + local rerank. (3) Measure end-to-end RAG-ready latency, not crypto ops alone. |
| **metric_impact** | RAG-ready latency vs graph-PIR/Tiptoe baselines at scale. |
| **refine_candidate** | **no** |

---

### 1.15 PRAG  
**arXiv:2604.26525** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6, S7 |
| **problem** | Partial encryption/noise hurts RAG recall; need end-to-end confidential retrieval. |
| **representation** | PRAG dual-mode: **PRAG-I** homomorphic-friendly approximations; **PRAG-II** interactive client assist; **OEE** stabilizes ranking under HE noise; encrypted HNSW. |
| **write / read / forget** | Read over encrypted index; documents+queries confidential end-to-end. |
| **conflict** | Silent. |
| **privacy** | Graph reconstruction attack resistance; access-pattern protections. |
| **Kedger lessons** | (1) `.kxp` decrypt only after capability verify — PRAG secures cloud index half. (2) OEE-like rank stabilization for noisy hydrate scorers. (3) Dual interactive/non-interactive modes for latency tiers. |
| **metric_impact** | Recall 72–74% vs plaintext RAG; retrieval latency at million-scale. |
| **refine_candidate** | **no** |

---

### 1.16 HyDE  
**arXiv:2212.10496** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | Zero-shot dense retrieval without labeled pairs underperforms. |
| **representation** | HyDE: LLM generates hypothetical answer doc → encoder embeds → retrieves real neighbors; hallucinations filtered by encoder bottleneck. |
| **write / read / forget** | Read-only retrieval augmentation. |
| **conflict** | Silent. |
| **privacy** | Hypothetical docs may hallucinate sensitive content — do not log raw HyDE outputs to shared tiers. |
| **Kedger lessons** | (1) S7 optional HyDE booster when embedding recall weak. (2) Never treat hypothetical text as Evidence — only retrieved real L0. (3) Average multiple HyDE samples for stability. |
| **metric_impact** | Zero-shot retrieval vs Contriever across QA/search/fever tasks. |
| **refine_candidate** | **yes** |

---

### 1.17 Retrieval-Augmented Generation for LLMs  
**arXiv:2312.10997** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | RAG literature fragmented — hard to pick routing/compression/seal mechanisms. |
| **representation** | RAG survey taxonomy: retrieval, augmentation, generation; covers routing, compression, evaluation. |
| **write / read / forget** | Survey index — not a system. |
| **conflict** | Surveys note knowledge conflicts / attribution as open issues. |
| **privacy** | Surveys privacy-preserving RAG as emerging area. |
| **Kedger lessons** | (1) Map Kedger S7 subsystems to survey axes (passive/active/self-RAG). (2) Use as citation map for future FULL passes. (3) Align pack composition checklist with survey failure modes. |
| **metric_impact** | Taxonomy coverage — informs harness design, not numeric SLI. |
| **refine_candidate** | **no** |

---

## 2. Cross-cutting map → Kedger stages

| Stage | Papers | Takeaway |
|-------|--------|----------|
| S2 working | Membox | Topic-continuity threads across sessions |
| S3 cognify | HaluMem, MemBench reflective tier | Hallucination audits on write path |
| S6 seal | ConfAIde, Fides, MRMMIA, SSE, ppRAG/PRAG/PIR-RAG | IFC + encrypted retrieve + MIA/oracle hardening |
| S7 hydrate | RankRAG, HyDE, RAGRouter, SkewRoute, RAG survey | Rerank→pack; routing by retrieval signals; zero-shot HyDE booster |
| S8 why | ConfAIde contextual norms | Do not disclose in inappropriate contexts even if factually retrievable |

---

## 3. Refine tickets (≤3)

1. **ConfAIde + Fides seal fixture (S6/S7)** — Contextual integrity tier-4 + IFC deny on cross-purpose hydrate; metric: inappropriate disclosure rate.
2. **MRMMIA + SSE oracle probes** — Memory membership + encrypted-search leakage regression; metric: MIA AUC / keyword recovery @ Inv-Scope hardening.
3. **RankRAG + SkewRoute pack router (S7)** — Rerank Evidence then route model tier by score skew; metric: QA utility vs cost curve.

---

## 4. Successfully FULL-read IDs

```
2310.17884
2505.23643
2601.06966
2506.21605
2605.27825
2309.04697
2510.06719
2511.03506
2601.03785
2407.02485
2505.23052
2505.23841
2601.12331
2509.21325
2604.26525
2212.10496
2312.10997
```
