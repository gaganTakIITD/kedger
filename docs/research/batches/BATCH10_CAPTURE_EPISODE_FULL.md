# Batch 10 — Capture · Episode · Boundary · Working Memory · Compaction (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-300-fb37`  
> **Scope:** Tier-2/3 episode/boundary/capture/compaction/MemGPT-adjacent papers **not** previously FULL in `CORPUS_INVENTORY.md` §2.  
> **Sources:** Survey bibliographies + queue tier 2–3 (Membox, RMM, ReSum, BEAM/LIGHT, Context-Folding, HiAgent, …).  
> **Method:** Full arXiv HTML/PDF bodies; cache `/tmp/kedger-papers/full/{id}.txt`.  

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new) | **17** | Membox (2601.03785); RMM (2503.08026); ReSum (2509.13313); Neural Paging (2603.02228); BEAM benchmark + LIGHT memory framework (2510.27246); StructMem (2604.21748); … |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped** | **0** | All IDs `.txt` ≥24k chars |

---

## 1. Mechanism cards

### 1.1 Membox  
**arXiv:2601.03785** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S4, S7 |
| **problem** | Fragmentation–compensation (utterance store + embedding retrieve) breaks topic continuity and temporal reasoning. |
| **representation** | Topic Loom: sliding-window same-topic turn grouping into sealed memory boxes; Trace Weaver links boxes into long-range event timelines. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Cognify at storage time — group consecutive same-topic turns before embed index. (2) Trace Weaver ≈ bi-temporal episode links for macro-topic recurrence. (3) Up to ~68% F1 gain on temporal reasoning vs Mem0/A-MEM on LoCoMo with fewer tokens. (4) Boundary detector feeds HARD/SOFT cuts — aligns EST/segment fixtures. |
| **metric_impact** | Temporal/multi-hop F1 on LoCoMo + token budget vs turn/session baselines. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.2 RMM  
**arXiv:2503.08026** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Fixed session/turn boundaries misalign with semantic topic units in personalized dialogue. |
| **representation** | Prospective reflection: topic-based memory extraction/update at session end; Retrospective reflection: online RL refines retrieval using cited evidence. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Topic-coherent memory units > session delimiters for promote/hydrate. (2) Retrospective RL on cited evidence ≈ eng-judgment feedback on hydrate misfires. (3) Pair with granularity-aware eval (2512.17083). (4) Silent on sealed packs — use capability gates separately. |
| **metric_impact** | Personalized dialogue quality + retrieval precision vs turn/session memory. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.3 ReSum  
**arXiv:2509.13313** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7 |
| **problem** | Web/search agents hit context limits; architectural memory tokens break compatibility. |
| **representation** | Periodic summary tool compresses history to compact restart state; ReSum-GRPO trains agents for segmented trajectories (+4.5% training-free, +8.2% with GRPO in paper). |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) PreCompact hook can invoke external summarizer — reset WorkingState to (query, summary). (2) Trigger near context limit (~70–80%), not early turns. (3) Summary quality tool (ReSumTool-30B) matters — generic LLM summaries fail. (4) Plug-and-play vs MemGPT paging — simpler but summary-lossy. |
| **metric_impact** | Pass@1 on BrowseComp-class tasks vs ReAct @ fixed token budget. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.4 Neural Paging  
**arXiv:2603.02228** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2 |
| **problem** | MemGPT-style LM-managed paging wastes tokens on housekeeping; RAG is passive/coarse. |
| **representation** | Decouple LLM reasoning from learned Page Controller (neural MMU) predicting evict/prefetch; strict separation from MemGPT kernel-in-user-space. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Don't force main agent to manage KV/paging — separate controller service for S2 pressure. (2) MemGPT foil: function-call paging vs learned policy. (3) Target Turing-complete agents with bounded active context. (4) Silent on SUPERSEDES — symbolic Anchor path still authoritative. |
| **metric_impact** | Task success vs active context size + paging policy ablation. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.5 BEAM benchmark + LIGHT memory framework  
**arXiv:2510.27246** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Long-dialogue benchmarks lack narrative coherence and diverse memory abilities beyond simple recall. |
| **representation** | BEAM: auto-generated coherent conversations up to 10M tokens, 2000 questions / 10 ability types. LIGHT: episodic retrieve + working-memory buffer (recent z turns) + scratchpad of salient facts filtered per question. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Three-tier hydrate: episodic retrieve + working buffer + curated scratchpad Anchors. (2) Even 1M context models degrade on BEAM length — retrieval mandatory. (3) LIGHT +3.5–12.69% over strongest baselines. (4) Ablation: working memory helps mid-length; scratchpad critical at 10M. |
| **metric_impact** | BEAM ability-wise accuracy @ 100K–10M tokens; LIGHT ablation SLI. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.6 StructMem  
**arXiv:2604.21748** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S5, S7 |
| **problem** | Flat memory stores lose event-level bindings and cross-event structure in long horizons. |
| **representation** | Hierarchical structured memory preserving event bindings + cross-event connections; hierarchical retrieve. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Cognify emits structured episode objects, not flat strings. (2) Graph/Anchor edges encode cross-event links — StructMem validates hierarchical retrieve. (3) Long-horizon behavior tasks need structure metric, not EM alone. (4) Complements Graphiti episode→entity pipeline. |
| **metric_impact** | Long-horizon task success + structural consistency vs flat RAG memory. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.7 FluxMem  
**arXiv:2605.28773** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S5, S7 |
| **problem** | Static memory graphs don't evolve connectivity as agent experience accumulates. |
| **representation** | Heterogeneous memory graph with evolving connectivity; continual integration of new nodes/edges. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Promotion must update graph connectivity, not only append nodes. (2) Monitor edge drift/poison — governance before consolidate (SSGM-aligned). (3) Retrieve = subgraph expand with connectivity-aware PPR analog. (4) Paper reports double-digit gains on long-dialogue settings. |
| **metric_impact** | Recall + graph connectivity metrics under continual write load. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.8 MemInsight  
**arXiv:2503.21760** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Agents need autonomous decisions on what/when to augment memory without constant user cues. |
| **representation** | Autonomous memory augmentation pipeline deciding memory entries/refinement from interaction traces. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Cognify cron should auto-augment with guardrails — not unbounded LLM writes. (2) Autonomous augment ↔ RecMem recurrence gate (anti-eager). (3) Measure augment precision separately from QA end metric. (4) Provenance on augmented entries mandatory for promote. |
| **metric_impact** | Augment precision/recall + downstream task utility vs manual memory curation. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.9 Memanto  
**arXiv:2604.22085** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Untyped memory retrieval wastes context on irrelevant stored facts in long-horizon agents. |
| **representation** | Typed semantic memory schema + information-theoretic retrieval scoring for long-horizon agents. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Anchor `kind` typing should drive retrieve scoring — not embedding alone. (2) Info-theoretic score ≈ utility-per-token for S7 budget. (3) Long-horizon agents need typed forget/refresh policies. (4) Paper strong gains on multi-step tasks when types match query. |
| **metric_impact** | Retrieve precision@budget + long-horizon success vs untyped embed retrieve. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.10 Memp  
**arXiv:2508.06433** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Procedural/skills memory under-studied vs episodic/semantic in agents. |
| **representation** | Procedural memory store for reusable skills/workflows distilled from trajectories. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Voyager-style skill library = procedural tier — separate promote ACL from episodic. (2) Memp explores procedural recall for repeated tool workflows. (3) Version procedural Anchors with SUPERSEDES on skill updates. (4) Eval procedural separately in EvoMem execution quadrant. |
| **metric_impact** | Skill reuse rate + trajectory length reduction on repeated task families. |
| **refine_candidate** | **no** |

---

### 1.11 GraphRAG with Graphs  
**arXiv:2501.00309** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Graph-enhanced RAG lacks unified treatment of graph construction + retrieve for agents. |
| **representation** | Graph-first RAG pipeline: graph construction from corpus, community/summary views, graph-aware retrieval integration. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) P3 graph cognify outputs feed graph-RAG hydrate — not duplicate GraphRAG community summaries as Anchors. (2) Separate graph index refresh from Anchor invalidation. (3) Use as pattern catalog for S5 walks. (4) Large survey body — mechanism cards focus on agent-memory retrieve coupling. |
| **metric_impact** | Graph-RAG QA vs flat chunk RAG on multi-hop entity queries. |
| **refine_candidate** | **no** |

---

### 1.12 HiAgent  
**arXiv:2408.09559** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7 |
| **problem** | Long-horizon agent tasks overflow context; flat ReAct history is inefficient. |
| **representation** | Hierarchical working memory manager: subtask-scoped memory tiers + selective retention for long-horizon tasks. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) WorkingState should be hierarchical (task/subtask scopes) not one flat deque. (2) MemGPT-adjacent but explicit hierarchy for tool-heavy agents. (3) Pair with Context-Folding/ReSum compaction triggers. (4) Paper reports large gains on long-horizon agent benchmarks vs flat context. |
| **metric_impact** | Long-horizon task SR vs flat-context agent @ equal token cap. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.13 Sleep-time Compute  
**arXiv:2504.13171** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S8 |
| **problem** | Online-only memory update is expensive; humans consolidate offline. |
| **representation** | Allocate extra compute between interactions (sleep-time) to reorganize/predict memory before next session. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Cognify cron = sleep-time consolidation — decouple from online hydrate latency SLO. (2) Batch reflection/promotion candidates overnight. (3) Complements Sleep-SCM (2604.20943) already in corpus. (4) Don't block user turn on heavy cognify — async sleep jobs. |
| **metric_impact** | Next-session task utility vs online-only cognify @ fixed total compute budget. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.14 Context-Folding  
**arXiv:2510.11967** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7, S8 |
| **problem** | Linear history growth breaks long-horizon agents; summarization loses structure. |
| **representation** | Branch into sub-trajectory for subtask; return folds intermediate steps keeping concise summary; FoldGRPO dense token-level process rewards. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Subtask branch ≈ workstream-local WorkingState; return = promote summary to parent WS. (2) 32K active budget + branches beats 327K linear context (62%/58% on BrowseComp+/SWE-Bench Verified in paper). (3) FoldGRPO +20% BrowseComp vs ReAct GRPO. (4) Prefer structured fold summaries over blind compress. |
| **metric_impact** | pass@1 @ 32K×10 branches vs 327K linear on long-horizon agent benches. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.15 MemEngine  
**arXiv:2505.02099** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Research memory models lack unified modular implementation framework. |
| **representation** | Three-level MemEngine: memory functions → operations → models (MemoryBank, MemGPT, etc.); config + utility modules. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Kedger cognify/hydrate interfaces should mirror function→operation→model layering. (2) Swap memory backends without rewriting agent loop — plugin retrievers. (3) MemBench built on MemEngine — align eval harness adapters. (4) Library not governance — still need SUPERSEDES/seal. |
| **metric_impact** | Cross-model parity tests using shared MemEngine adapters in eval harness. |
| **refine_candidate** | **no** |

---

### 1.16 AgentFold  
**arXiv:2510.24699** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7 |
| **problem** | Long web-agent trajectories need proactive compaction beyond passive summarization. |
| **representation** | Granular + deep condensation with proactive fold/unfold of context; targets long-horizon web agents. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Proactive fold before pressure flush — don't wait for 100% MemGPT threshold. (2) Multi-scale condensation maps to L2 digest + L4 pack tiers. (3) Compare AgentFold vs Context-Folding branch semantics in dogfood. (4) Paper ~36–47% gains class on web agent benchmarks. |
| **metric_impact** | Web agent success @ fixed context with proactive vs reactive compaction. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.17 MemWalker  
**arXiv:2310.05029** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S5, S7, S8 |
| **problem** | Very long documents exceed context; passive retrieve misses multi-hop structure. |
| **representation** | Build memory tree over document; agent navigates/interacts with tree nodes (interactive reading) to answer. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Hydrate over long repos = tree walk, not single embedding top-k. (2) Notebook/tree navigation ≈ GraphReader function vocabulary. (3) Cap walk steps as S7 budget. (4) Paper strong gains on long-doc QA vs single-shot read. |
| **metric_impact** | Long-doc QA accuracy vs walk-budget + tree depth. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

## 2. Successfully FULL-read IDs

```
2601.03785
2503.08026
2509.13313
2603.02228
2510.27246
2604.21748
2605.28773
2503.21760
2604.22085
2508.06433
2501.00309
2408.09559
2504.13171
2510.11967
2505.02099
2510.24699
2310.05029
```
