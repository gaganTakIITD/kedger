# Batch 11 — Graph · Conflict · Compose · Multi-Agent Memory (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-300-fb37`  
> **Scope:** Tier-4 runway — graph memory toolkits, multi-agent compose, entity resolution, procedural/collaborative memory. Papers **not** already FULL in CORPUS §2 or Batch4–8.  
> **Method:** Full arXiv HTML (ar5iv fallback) or PDF→text when HTML thin; cache `/tmp/kedger-papers/full/{id}.{html,txt,pdf}`. Mechanism cards only — not abstract skim.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new body deep-read; ID not previously FULL in CORPUS §2 / Batch4–8) | **17** | 2505.24478 (Optimizing the Interface Between Knowled…); 2604.04853 (MemMachine: Ground-Truth-Preserving Memo…); 2511.00628 (AgentGit: Git-like Version Control for L…); 2606.06036 (MRAgent: Graph Memory with Active Recons…); 2601.02744 (SYNAPSE: Episodic-Semantic Memory via Sp…); 2507.07957 (MIRIX: Six-Type Multi-Agent Memory Syste…); 2305.09645 (StructGPT: IRR over Structured Data (KG/…); 2308.10848 (AgentVerse: Multi-Agent Collaboration wi…); 2508.08997 (Intrinsic Memory Agents: Heterogeneous M…); 2503.21760 (MemInsight: Autonomous Memory Augmentati…); 2508.06433 (Memp: Agent Procedural Memory); 2604.22085 (Memanto: Typed Semantic Memory with Info…); 2510.26486 (LINK-KG: LLM Coreference-Resolved KG Con…); 2409.03284 (iText2KG: Incremental Zero-Shot KG Const…); 2403.06434 (BoostER: LLM-Enhanced Entity Resolution); 2401.03426 (On Leveraging LLMs for Entity Resolution…); 2410.12480 (KcMF: Knowledge-Compliant Schema/Entity …) |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped (no invented content)** | **0** | Fides (`2505.23643`) via PDF extract; all carded IDs have `.txt` ≥23k chars |
| **Identified / cached but not carded (room)** | 0 | — |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt` (all FULL IDs present).

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded. Numbers are from paper text/tables.

---

## 1. Mechanism cards

### 1.1 Optimizing the Interface Between Knowledge Graphs and LLMs (  
**arXiv:2505.24478** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | KG+LLM stacks expose many hyperparameters (chunking, graph build, retrieval, prompting) but tuning is ad hoc. |
| **representation** | Cognee modular pipeline: chunk → entity/relation extract → graph + vector index; studies interface between KG structure and LLM reasoning. |
| **write / read / forget** | Write = ingest/cognify graph+embeddings. Read = hybrid graph/vector retrieval for multi-hop QA. Forget = not primary. |
| **conflict** | Silent on SUPERSEDES; focuses retrieval quality not belief conflict. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Kedger S5/S7 knobs (chunk size, neighbor depth, rerank) need explicit tuning SLIs like Cognee sweep. (2) Graph construction quality dominates hydrate — not embedding alone. (3) Triplet/path retrieval complements flat Evidence packs. |
| **metric_impact** | Multi-hop EM/F1 on HotpotQA/2Wiki/MuSiQue vs chunk/retrieval ablations. |
| **refine_candidate** | **yes** |

---

### 1.2 MemMachine  
**arXiv:2604.04853** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S5, S7 |
| **problem** | RAG/context-window memory loses raw episodes and over-extracts via routine LLM summarization. |
| **representation** | Ground-truth-preserving store: short-term + episodic graph + profile SQL; contextualized retrieval expands nucleus hits with neighboring turns. |
| **write / read / forget** | Write = store raw conversational episodes + minimal extraction. Read = vector/graph search + **Retrieval Agent** routes direct / split-query / chain-of-query strategies (`agent_mode`). Forget = profile updates; episodic append-only bias. |
| **conflict** | Query-bias correction + conflict resolution in typed schema (Memanto lineage in same ecosystem). |
| **privacy** | Multi-tenant isolation; ground-truth preservation aids audit. |
| **Kedger lessons** | (1) Do not LLM-summarize away L0 before cognify when audit matters. (2) Hydrate agent_mode ≈ PropRAG/IRCoT router for multi-hop. (3) Context expansion (`expand_context`) for chronological Evidence neighbors. |
| **metric_impact** | LoCoMo 0.9169 overall; LongMemEvalS 93% with retrieval-stage ablations dominating ingestion. |
| **refine_candidate** | **yes** |

---

### 1.3 AgentGit  
**arXiv:2511.00628** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S8 |
| **problem** | MAS lack rollback/branch — errors force full reruns; parallel strategy exploration is expensive. |
| **representation** | Git-like checkpoints over LangGraph state: messages, tool records, env vars; commit/revert/branch with optional tool reversal. |
| **write / read / forget** | Write = state commit checkpoints. Read = checkout/branch from checkpoint. Forget = non-destructive branches preserve alternate timelines. |
| **conflict** | Branches hold divergent beliefs — compose must pick projection, not merge blindly. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Parallel compose can use checkpoint branches for ConflictSet tournaments. (2) Tool reversal hooks pair with SUPERSEDES audit for side effects. (3) SQLite-backed checkpoint store mirrors Evidence append-only + projection pattern. |
| **metric_impact** | Runtime/token reduction vs LangGraph/AutoGen on prompt A/B arXiv abstract task. |
| **refine_candidate** | **yes** |

---

### 1.4 MRAgent  
**arXiv:2606.06036** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Static retrieve-then-reason cannot adapt paths using mid-inference evidence. |
| **representation** | **Cue–Tag–Content** graph: tags bridge cues to contents; **MRAgent** actively explores/prunes retrieval paths with LLM routing. |
| **write / read / forget** | Write = LLM distillation populates multi-granular layers. Read = iterative reconstruction with controlled traversal (not one-shot top-k). Forget = silent. |
| **conflict** | Prunes inconsistent paths during reconstruction; no typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate = active path search, not passive embedding NN. (2) Tag layer ≈ Anchor edge types guiding expand. (3) Cap traversal steps like IRCoT/GraphReader budgets. |
| **metric_impact** | Up to ~23% gain on LoCoMo/LongMemEval vs passive RAG; lower token/runtime. |
| **refine_candidate** | **yes** |

---

### 1.5 SYNAPSE  
**arXiv:2601.02744** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Flat vector stores miss structurally related but semantically distant memories (contextual tunneling). |
| **representation** | Unified episodic-semantic graph; **spreading activation** + lateral inhibition + temporal decay; triple hybrid retrieval (embed + activation traverse). |
| **write / read / forget** | Write = episodic logs → semantic concept nodes/edges. Read = inject activation from query anchors; retrieve activated subgraph. Forget = decay suppresses stale nodes. |
| **conflict** | Inhibition reduces contradictory hub explosion; not explicit ConflictSet. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) PPR/activation walk complements HippoRAG when seeds are weak. (2) Temporal decay maps to bi-temporal invalidation. (3) Fan-effect inhibition → cap hub Anchor degree in hydrate. |
| **metric_impact** | LoCoMo multi-hop/temporal categories; up to ~23% over SOTA RAG; ~95% token reduction vs full context. |
| **refine_candidate** | **yes** |

---

### 1.6 MIRIX  
**arXiv:2507.07957** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S3, S4, S6, S7 |
| **problem** | Flat single-store agent memory cannot separate secrets, procedures, resources, and persona blocks. |
| **representation** | Six memory types (Core/Episodic/Semantic/Procedural/Resource/Knowledge Vault) + eight agents (6 managers + meta + chat). Active retrieval requires topic before answer. |
| **write / read / forget** | Write = screen/IDE capture debounced (1.5s), batch ~20 frames → type-specific managers; Core rewrite at 90% capacity. Read = topic-gated active retrieval into system prompt. Forget = abstraction compresses raw screenshots (~99.9% vs RAG on ScreenshotVQA). |
| **conflict** | Temporal ambiguity when consolidated event overwrites earlier plan — implicit conflict. |
| **privacy** | Knowledge Vault sensitivity tiers; secrets not in casual retrieve. |
| **Kedger lessons** | (1) Map Kedger Anchor kinds to MIRIX taxonomy. (2) Active retrieval gate before S7 pack compile. (3) Vault ≠ L3 Anchors — sealed sidecar. |
| **metric_impact** | ScreenshotVQA near 20k frames/seq; LoCoMo with constrained chat-only-from-memory. |
| **refine_candidate** | **yes** |

---

### 1.7 StructGPT  
**arXiv:2305.09645** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | LLMs struggle to reason over structured stores (KG, tables, SQL) in zero/few-shot. |
| **representation** | **StructGPT** IRR: specialized interfaces read structured data; LLM reasons via invoke-linearize-generate loops. |
| **write / read / forget** | Read-only structured access in eval; iterative interface calls accumulate evidence. Write N/A in framework. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate over graph DB/SQL should expose typed read interfaces, not dump rows. (2) Multi-step IRR ≈ graph walk + compose. (3) Cap interface iterations. |
| **metric_impact** | WebQSP +11.4% Hits@1 vs ChatGPT zero-shot; TabFact/Spider gains. |
| **refine_candidate** | **no** |

---

### 1.8 AgentVerse  
**arXiv:2308.10848** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S8 |
| **problem** | Static multi-agent teams mis-match task phase; no dynamic recruitment/evaluation loop. |
| **representation** | Four-stage loop: expert recruitment → collaborative decision → action → evaluation/feedback; dynamic group adjustment. |
| **write / read / forget** | Write = shared conversation/tool traces per stage. Read = agents consume group state each round. Forget = silent. |
| **conflict** | Emergent disagreement in decision stage; no typed merge. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Compose projections may need per-stage principal sets (recruitment ≈ capability attenuation). (2) Evaluation stage feeds S8 `why` + promotion gates. (3) Parallel AgentGit branches for alternative team compositions. |
| **metric_impact** | Task success vs single-agent across text/reasoning/code/tool/embodied suites. |
| **refine_candidate** | **no** |

---

### 1.9 Intrinsic Memory Agents  
**arXiv:2508.08997** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S4, S5 |
| **problem** | Shared flat memory breaks role adherence in heterogeneous multi-agent teams. |
| **representation** | Per-agent **intrinsic memory** updated from each agent's own outputs (not external summarizer); generic memory template. |
| **write / read / forget** | Write = intrinsic update from agent utterances/actions. Read = agent-specific memory injected per role. Forget = silent. |
| **conflict** | Role-aligned memories may diverge — compose must reconcile for shared Anchors. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Workstream-private L2 before promote to shared L3. (2) No central summarizer for multi-agent capture — preserve actor field. (3) Heterogeneous retrieve filters before merge. |
| **metric_impact** | PDDL/FEVER/ALFWorld vs SOTA multi-agent memory; pipeline design quality rubric. |
| **refine_candidate** | **yes** |

---

### 1.10 MemInsight  
**arXiv:2503.21760** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Growing unstructured memory hurts semantic retrieval without autonomous restructuring. |
| **representation** | MemInsight autonomously augments historical interactions with semantic annotations/metadata for richer indexing. |
| **write / read / forget** | Write = autonomous augmentation pass enriches stored turns. Read = improved recall via augmented representations (+34% recall vs RAG baseline on LoCoMo). Forget = silent. |
| **conflict** | Silent. |
| **privacy** | Augmentation must not leak private fields into shared indexes. |
| **Kedger lessons** | (1) Cognify cron includes autonomous metadata enrichment (not only summarization). (2) Re-embed after augmentation migration. (3) Measure recall@k post-augmentation. |
| **metric_impact** | LoCoMo recall +34% vs RAG; +14% recommendation persuasiveness on LLM-REDIAL. |
| **refine_candidate** | **yes** |

---

### 1.11 Memp  
**arXiv:2508.06433** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Agents repeat trial-and-error without durable **procedural** memory of successful workflows. |
| **representation** | Procedural memory bank of reusable workflows; storage, retrieval, and update operators for agent skills. |
| **write / read / forget** | Write = distill successful trajectories into procedures after tasks. Read = retrieve relevant procedures to shorten trials. Forget = update/refine procedures with new evidence. |
| **conflict** | Stale procedures persist without supersession — risk if not versioned. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) L3 procedural Anchors distinct from episodic Evidence. (2) Promotion gate for shared runbooks. (3) SUPERSEDES when procedure steps change. |
| **metric_impact** | Accuracy↑ and trial count↓; transfer from strong to weak models. |
| **refine_candidate** | **yes** |

---

### 1.12 Memanto  
**arXiv:2604.22085** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S5, S7 |
| **problem** | Untyped memory graphs add complexity without beating optimized vector recall in production. |
| **representation** | Typed semantic memory schema + information-theoretic retrieval (Moorcheh); explicit **conflict resolution** and **temporal versioning**; session/namespace isolation. |
| **write / read / forget** | Write = typed ingest with namespaces. Read = recall expansion + prompt-optimized retrieval prioritizing recall over precision. Forget = temporal versioning + conflict resolver. |
| **conflict** | First-class conflict resolution module for contradictory typed statements. |
| **privacy** | Namespace/session isolation for multi-tenant agents. |
| **Kedger lessons** | (1) Typed Anchor kinds before graph complexity. (2) Conflict resolver before near-dup merge (MemClaw order). (3) Recall-first hydrate for long-horizon agents. |
| **metric_impact** | Progressive ablation across five stages; overhead vs graph-heavy baselines. |
| **refine_candidate** | **yes** |

---

### 1.13 LINK-KG  
**arXiv:2510.26486** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5 |
| **problem** | Chunk-wise KG extraction duplicates entities and breaks coreference across long documents. |
| **representation** | Three-stage LLM coreference pipeline + **type-specific prompt cache** (alias→canonical per entity type) before triple extraction. |
| **write / read / forget** | Write = resolve coref then extract KG. Read N/A (construction focus). Forget = cache prevents redundant alias re-add. |
| **conflict** | Duplicate nodes create false conflicts — resolution reduces noise. |
| **privacy** | Legal-domain PII in source texts — cache holds aliases. |
| **Kedger lessons** | (1) Entity resolve stage mandatory before Anchor merge (P3 τ=0.8). (2) Type-specific caches ≈ workstream-scoped alias tables. (3) Plural/role-shift prompts for engineering logs. |
| **metric_impact** | −45.21% node duplication; −32.22% noisy nodes vs baselines. |
| **refine_candidate** | **yes** |

---

### 1.14 iText2KG  
**arXiv:2409.03284** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5 |
| **problem** | Batch KG builders need post-hoc dedup; topic-dependent schemas brittle. |
| **representation** | iText2KG: Document Distiller → incremental entity extractor → relation extractor → graph integrator; zero-shot, topic-independent. |
| **write / read / forget** | Write = incremental integration merges new docs without full rebuild. Read = unified KG for downstream RAG. Forget = update via re-integration. |
| **conflict** | Graph Integrator handles duplicate entities/relations during merge. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Cognify incremental graph merge, not nightly full rebuild. (2) Schema/blueprint JSON steers extraction (like Anchor kinds). (3) Zero-shot IE quality gates before promote. |
| **metric_impact** | Superior vs baselines on paper→graph, website→graph, CV→graph scenarios. |
| **refine_candidate** | **no** |

---

### 1.15 BoostER  
**arXiv:2403.06434** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5 |
| **problem** | Entity resolution usually needs heavy supervised pipelines. |
| **representation** | BoostER selects informative match questions for LLM verification; refines ER distribution with LLM answers under token budget. |
| **write / read / forget** | Read/write via questioning — no parametric training. Write = merge decisions update ER clusters. |
| **conflict** | Merge vs non-merge decisions affect downstream graph conflict surface. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) P3 entity resolve can use LLM pairwise verify with budgeted questions. (2) Greedy question selection ≈ active learning for ALIAS edges. (3) Log merge provenance for SUPERSEDES. |
| **metric_impact** | ER quality vs cost on real-world datasets; token spend caps. |
| **refine_candidate** | **yes** |

---

### 1.16 On Leveraging LLMs for Entity Resolution (Cost-Efficient)  
**arXiv:2401.03426** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5 |
| **problem** | LLM ER at scale is expensive if every pair is queried. |
| **representation** | Cost-efficient LLM ER: blocking + selective LLM matching questions; optimizes spend vs quality. |
| **write / read / forget** | Write = cluster merges after LLM confirmation. Read = retrieve canonical entity for hydrate graph walks. |
| **conflict** | False merges create false conflicts; false splits duplicate Anchors. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Two-stage resolve: cheap blocking then LLM verify (BoostER/Li pipeline). (2) Track confidence on ALIAS edges. (3) Human gate for high-impact merges to shared tier. |
| **metric_impact** | Cost vs F1 on ER benchmarks; comparison to full LLM pairwise. |
| **refine_candidate** | **yes** |

---

### 1.17 KcMF  
**arXiv:2410.12480** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5 |
| **problem** | Schema/entity matching with fine-tuned LLMs is heavy; hallucinated match rules. |
| **representation** | KcMF: pseudo-code task decomposition + Dataset-as-Knowledge / Examples-as-Knowledge + Inconsistency-tolerant Generation Ensembling (IntGE). |
| **write / read / forget** | Write = schema/entity alignment decisions ingested to graph. Read = matching for hydrate/joins across sources. |
| **conflict** | IntGE suppresses malformed match outputs — reduces spurious duplicate nodes. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Entity/schema matching prompts as executable pseudo-code checklists in cognify. (2) IntGE voting for IE/match ops. (3) External knowledge snippets as Evidence, not silent params. |
| **metric_impact** | Outperforms fine-tuning-free LLM baselines on schema+entity matching suites. |
| **refine_candidate** | **no** |

---

## 2. Cross-cutting map → Kedger stages

| Stage | Papers | Takeaway |
|-------|--------|----------|
| S3 cognify | Cognee, iText2KG, LINK-KG, MemInsight, Memanto | Incremental typed graph build + coreference before merge |
| S4 promote | Memanto, Memp, Intrinsic Memory | Conflict resolver before shared procedural/runbook promote |
| S5 graph | SYNAPSE, MRAgent, StructGPT, MemMachine agent_mode | Activation/path walks + structured read interfaces |
| S6 seal | MIRIX Vault | Secrets outside L3; sensitivity tiers |
| S7 hydrate | MemMachine, MRAgent, Cognee, Memanto | Recall-first + active routing + rerank |
| S8 why | AgentGit branches | Checkpoint provenance for alternate compose paths |

---

## 3. Refine tickets (≤3)

1. **Entity resolve + LINK-KG cache (P3)** — Type-specific alias cache + BoostER/KcMF verify before ALIAS/SUPERSEDES; metric: duplication/noisy-node rate on eng log fixture.
2. **Active reconstruction hydrate (MRAgent/SYNAPSE)** — Tag-guided traverse with step cap; metric: LoCoMo multi-hop F1 vs passive top-k @ token budget.
3. **AgentGit compose branches (S4/S5)** — Checkpoint divergent promotions; metric: ConflictSet resolution accuracy + token saved vs rerun.

---

## 4. Successfully FULL-read IDs

```
2505.24478
2604.04853
2511.00628
2606.06036
2601.02744
2507.07957
2305.09645
2308.10848
2508.08997
2503.21760
2508.06433
2604.22085
2510.26486
2409.03284
2403.06434
2401.03426
2410.12480
```
