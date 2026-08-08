# Batch 14 — Mixed Runway · Agent Memory · Retrieve Lineage (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-300-fb37`  
> **Scope:** Remaining high-value **agent-memory** + **retrieve lineage** papers from FULL runway seed queue with fetchable arXiv IDs not yet FULL in `CORPUS_INVENTORY.md` §2. Excludes Batch9–12 FULL (MIRIX, M3-Agent, HiAgent, ReSum, REPLUG, etc.).  
> **Method:** Full arXiv HTML/ar5iv or PDF→text; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards only.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Lens:** Symbolic+latent memory, procedural lifecycle, retrieve co-training, agent training platforms

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new body deep-read; ID not previously FULL in CORPUS §2) | **17** | `2306.03901`, `2406.04151`, `1911.00172`, `2004.12832`, `2208.03299`, `2002.08909`, `2402.04624`, `2502.00592`, `2509.24704`, `2402.04617`, `2606.29824`, `2606.23127`, `2608.03463`, `2603.24018`, `2512.18950`, `2605.30690`, `2509.08755` |
| **RE-READ** | **0** | — |
| **SKIPPED duplicate** | **0** | — |
| **Fetch failed / skipped** | **0** | All 17 IDs have `.txt` ≥25k chars |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

---

## 1. Mechanism cards

### 1. ChatDB — SQL databases as symbolic memory
**arXiv:2306.03901** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S5, S7 |
| **problem** | Neural memory accumulates errors; complex multi-hop reasoning needs exact symbolic store. |
| **representation** | LLM controller + SQL DB memory: generate SQL read/write ops; DB holds structured historical state. |
| **write / read / forget** | Write via INSERT/UPDATE SQL; read via SELECT; LLM plans multi-hop SQL programs. |
| **conflict** | SQL constraints enforce consistency; updates overwrite rows explicitly. |
| **privacy** | DB can scope tables per tenant — silent on crypto. |
| **Kedger lessons** | (1) Kedger sqlite graph = ChatDB-class symbolic memory. (2) Exact retrieval for structured facts beats fuzzy embed for tables. (3) LLM generates memory ops — audit SQL like Anchor ops. (4) Multi-hop = chained SQL not single vector search. |
| **metric_impact** | multi-hop QA ACC on structured memory |
| **refine_candidate** | **yes** |

---

### 2. AgentGym — evolving LLM agents across environments
**arXiv:2406.04151** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S3, S8 |
| **problem** | Agent training fragmented across envs; need unified platform + trajectories for cross-task evolution. |
| **representation** | AgentGym: 14+ envs (WebShop, WebArena, ALFWorld, SciWorld, …) + trajectory dataset + AgentEvol curriculum. |
| **write / read / forget** | Collect/filter trajectories across envs; behavioral cloning + iterative exploration (AgentEvol). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Memory eval needs multi-env trajectories not single chat bench. (2) AgentEvol = experience promotion across tasks. (3) Trajectory filtering before L3 ingest. (4) Cross-env generalization tests memory transfer. |
| **metric_impact** | cross-env success rate after evolution |
| **refine_candidate** | **yes** |

---

### 3. kNN-LM — nearest-neighbor language models
**arXiv:1911.00172** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Parametric LMs weak on rare facts; non-parametric datastore improves perplexity without retraining. |
| **representation** | kNN-LM: interpolate pretrained LM with kNN over embedding datastore (keys=hidden states, values=tokens). |
| **write / read / forget** | Read-only datastore at inference; optional domain adaptation by swapping neighbor corpus. |
| **conflict** | Silent. |
| **privacy** | Datastore may leak training snippets — membership concern. |
| **Kedger lessons** | (1) Kedger optional embed index = kNN datastore for hydrate. (2) Rare Anchor facts benefit from exact neighbor retrieval. (3) +2.9 perplexity points on WikiText-103. (4) Separate parametric vs non-parametric evidence in S8 provenance. |
| **metric_impact** | perplexity / rare-fact recall |
| **refine_candidate** | **yes** |

---

### 4. ColBERT — late interaction dense retrieval
**arXiv:2004.12832** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | Bi-encoder retrieval loses token-level matching; cross-encoders too slow at scale. |
| **representation** | ColBERT: contextualized late interaction — MaxSim over token embeddings; offline indexing + fast online scoring. |
| **write / read / forget** | Read-only passage index; query-time MaxSim aggregation. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S7 passage retrieve can use ColBERT-class late interaction. (2) Token-level match helps entity-heavy Anchor hydrate. (3) Index passages not whole sessions. (4) Balance latency vs bi-encoder baseline. |
| **metric_impact** | retrieve MRR/Recall@k on Anchor corpus |
| **refine_candidate** | **no** |

---

### 5. Atlas — retrieval augmented few-shot LM
**arXiv:2208.03299** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | Few-shot LM performance limited without retrieval; need joint retriever+LM training. |
| **representation** | Atlas: T5-style LM + Contriever retriever; end-to-end trained on QA with retrieved passages in context. |
| **write / read / forget** | Retrieve top-k passages → prepend to input → generate answer; retriever+LM co-trained. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate = retrieve-then-generate with co-trained components. (2) Few-shot Anchor QA benefits from Atlas pattern. (3) Passage attribution in output for S8. (4) Strong multi-hop QA with fixed retrieve budget. |
| **metric_impact** | few-shot QA F1 with retrieve budget |
| **refine_candidate** | **no** |

---

### 6. REALM — retrieval-augmented LM pre-training
**arXiv:2002.08909** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | LMs lack access to external knowledge at pretrain time; retrieval should be baked into LM training. |
| **representation** | REALM: retrieve Wikipedia chunks during masked LM pretrain; asynchronous retriever refresh. |
| **write / read / forget** | Retriever index updated during pretrain; LM learns to use retrieved docs. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Long-term: Kedger embed index refresh async like REALM. (2) Retrieval not bolt-on — train/instruct for Evidence use. (3) Open-domain QA gains from pretrain retrieve. (4) Provenance: retrieved doc ID in context. |
| **metric_impact** | open-domain QA EM |
| **refine_candidate** | **no** |

---

### 7. MemoryLLM — self-updatable LLM memory
**arXiv:2402.04624** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S4 |
| **problem** | Frozen LMs can't incorporate new facts without full finetune; need internal memory slots that update. |
| **representation** | MemoryLLM: latent memory matrix injected into transformer layers; update operator writes new knowledge into slots. |
| **write / read / forget** | Write via memory update module on new documents; read via attention to memory tokens during inference. |
| **conflict** | Updates may overwrite — implicit supersession in slots. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Parametric memory slots ≠ Kedger Anchors but inform update semantics. (2) Self-update without full finetune. (3) Track slot version for audit. (4) Pair with explicit graph invalidation for governance. |
| **metric_impact** | knowledge update ACC after write |
| **refine_candidate** | **yes** |

---

### 8. M+ — scalable long-term MemoryLLM
**arXiv:2502.00592** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S4 |
| **problem** | MemoryLLM slots limited; need scalable long-term memory without proportional param growth. |
| **representation** | M+: hierarchical/scalable extension of MemoryLLM — more slots + efficient update/retrieval over long streams. |
| **write / read / forget** | Stream documents → selective slot update → read via memory attention. |
| **conflict** | Slot overwrite = soft supersession. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Long-horizon L3 needs scalable update not unbounded context. (2) M+ patterns for memory budget management. (3) Combine parametric slots with explicit Anchor graph. (4) Measure retention after many updates. |
| **metric_impact** | long-stream knowledge retention |
| **refine_candidate** | **yes** |

---

### 9. MemGen — generative latent memory
**arXiv:2509.24704** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Retrieval-only memory misses generative synthesis; agents need latent memory that generates recall. |
| **representation** | MemGen: generative latent memory module — compress experiences to latents, generate memory-informed outputs. |
| **write / read / forget** | Write experiences → encode to latent memory → generate/decode at recall time. |
| **conflict** | Silent. |
| **privacy** | Latent memory not human-readable — governance gap. |
| **Kedger lessons** | (1) Generative recall complements retrieve-from-graph. (2) Latent memory needs export/audit path for Kedger. (3) Weave with explicit Anchors for shareable subset. (4) Agent task performance vs pure RAG. |
| **metric_impact** | agent task ACC with generative memory |
| **refine_candidate** | **yes** |

---

### 10. InfLLM — training-free long-context memory
**arXiv:2402.04617** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Context windows finite; need infinite context without training via memory hierarchy. |
| **representation** | InfLLM: local attention window + external memory unit storing distant context chunks; retrieve into window. |
| **write / read / forget** | Chunk long input → store in memory unit → retrieve relevant chunks into active window. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S2 working state = active window; L2/L3 = InfLLM memory unit. (2) Training-free → matches Kedger v1 heuristic hydrate. (3) Chunk boundary affects recall — align with episode boundaries. (4) Long-document QA benchmarks. |
| **metric_impact** | long-context QA with fixed window |
| **refine_candidate** | **yes** |

---

### 11. Neural procedural memory for LLM agents — Neural procedural memory for LLM agents
**arXiv:2606.29824** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | LLM agents repeat planning; need implicit procedural memory encoding skills without explicit scripts. |
| **representation** | Neural procedural memory: encode successful action sequences into compact neural modules recalled at execution. |
| **write / read / forget** | Write successful trajectories → distill procedural encoding → read during similar tasks. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Procedural L3 tier for tool workflows. (2) Distill multi-step plans to reusable procedures. (3) S4 promote after N successful replays. (4) Complements Memp (Batch10) explicit procedural store. |
| **metric_impact** | procedure reuse rate on tool tasks |
| **refine_candidate** | **yes** |

---

### 12. Managing procedural memory in LLM agents — Managing procedural memory in LLM agents
**arXiv:2606.23127** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S8 |
| **problem** | Procedural memory grows unbounded; need lifecycle control, adaptation, and pruning. |
| **representation** | Framework for procedural memory CRUD: acquisition, refinement, deprecation, conflict between procedures. |
| **write / read / forget** | Lifecycle ops on procedure store — consolidate, adapt, retire stale procedures. |
| **conflict** | Explicit procedure conflict detection and resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Kedger INVALIDATE for superseded procedures. (2) Consolidation pass like sleep-time compute. (3) Version procedures with superseded_by links. (4) Audit trail on procedure promotion/retirement. |
| **metric_impact** | procedure store size vs task success |
| **refine_candidate** | **yes** |

---

### 13. LeanMem — efficient long-term agent memory
**arXiv:2608.03463** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Agent memory systems too heavy; need simple efficient long-term memory with minimal overhead. |
| **representation** | LeanMem: lightweight memory architecture — selective retention + compact encoding + fast retrieval. |
| **write / read / forget** | Filter incoming observations → compact store → retrieve top-k for context injection. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Kedger v1 should stay LeanMem-simple not over-engineer. (2) Selective retention = promotion gate. (3) Compact encoding before L3 graph ingest. (4) Latency budget for memory maintenance. |
| **metric_impact** | memory ops latency + QA ACC |
| **refine_candidate** | **yes** |

---

### 14. ELITE — experiential learning and intent-aware transfer
**arXiv:2603.24018** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S8 |
| **problem** | Agents fail to transfer learned skills across intents/domains without explicit transfer mechanism. |
| **representation** | ELITE: capture experiences with intent labels → transfer relevant subsets to new tasks via intent matching. |
| **write / read / forget** | Write intent-tagged experiences → match intent at new task → read transferred subset. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Anchor metadata includes intent/workstream tags for transfer. (2) S4 promote with intent scope not global. (3) Cross-workstream hydrate filters by intent. (4) Measure transfer vs scratch performance. |
| **metric_impact** | cross-intent transfer success delta |
| **refine_candidate** | **yes** |

---

### 15. Hierarchical procedural memory (Bayesian) — Hierarchical procedural memory (Bayesian)
**arXiv:2512.18950** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S5 |
| **problem** | Flat procedure lists don't capture skill hierarchy; need structured procedural memory with uncertainty. |
| **representation** | Bayesian hierarchical procedural memory: decompose skills into tree; update beliefs on execution outcomes. |
| **write / read / forget** | Write execution outcomes → Bayesian update on hierarchy nodes → read most probable procedure path. |
| **conflict** | Competing procedures resolved by posterior weight. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Procedure graph hierarchy in Kedger L3. (2) Uncertainty-aware procedure selection. (3) S5 compose picks procedure branch by confidence. (4) Supersede low-posterior branches after evidence. |
| **metric_impact** | hierarchical procedure selection ACC |
| **refine_candidate** | **yes** |

---

### 16. ElasticMem — latent memory as learnable resource
**arXiv:2605.30690** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S4 |
| **problem** | Fixed memory capacity wastes resources; memory should elastically expand/contract with task demands. |
| **representation** | ElasticMem: learnable latent memory resource — dynamic capacity allocation based on task complexity signals. |
| **write / read / forget** | Elastic expand on high surprise/complexity → compress when stable; read latent memory during inference. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Memory budget scales with surprise (ES-Mem class signal). (2) Compress stable L2 before promote. (3) Elastic capacity for long projects. (4) Monitor memory cost SLI. |
| **metric_impact** | memory footprint vs task performance |
| **refine_candidate** | **yes** |

---

### 17. AgentGym-RL — RL for long-horizon agents
**arXiv:2509.08755** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S3, S8 |
| **problem** | Behavioral cloning insufficient for long-horizon agents; need RL on AgentGym trajectories. |
| **representation** | AgentGym-RL: RL fine-tuning on AgentGym envs for long-horizon tool use; reward from env success. |
| **write / read / forget** | Policy generates actions → env feedback → RL update; memory from successful trajectories. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Kedger v1 avoids RL memory controller but RL trajectories feed L3 promotion. (2) Long-horizon reward shapes what gets remembered. (3) Pair with AgentGym platform for eval. (4) Log trajectory provenance for promoted Anchors. |
| **metric_impact** | long-horizon env success after RL |
| **refine_candidate** | **no** |

---

## 2. Batch synthesis

| Theme | Papers | Kedger hook |
|-------|--------|-------------|
| **Symbolic memory** | ChatDB | SQL/graph as exact memory substrate |
| **Parametric/latent memory** | MemoryLLM, M+, MemGen, ElasticMem, InfLLM | Update slots; generative recall; elastic capacity |
| **Procedural memory** | Neural PM, Managing PM, Hierarchical PM | Lifecycle, hierarchy, Bayesian selection |
| **Retrieve lineage** | kNN-LM, ColBERT, Atlas, REALM | Non-parametric datastore; late interaction; co-training |
| **Agent platforms** | AgentGym, AgentGym-RL, LeanMem, ELITE | Multi-env trajectories; RL; efficient retention |

---

## 3. Cached FULL ID list

```
2306.03901
2406.04151
1911.00172
2004.12832
2208.03299
2002.08909
2402.04624
2502.00592
2509.24704
2402.04617
2606.29824
2606.23127
2608.03463
2603.24018
2512.18950
2605.30690
2509.08755
```
