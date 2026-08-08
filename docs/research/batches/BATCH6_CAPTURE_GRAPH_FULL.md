# Batch 6 — Capture / Compaction · Episode Boundaries · Graph / Conflict (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch6-measure-refine-fb37`  
> **Scope:** Tier-2/3/4 runway — **capture & compaction**, **episode / dialogue boundaries**, **graph memory & knowledge conflict**. Papers **not** already FULL in `CORPUS_INVENTORY.md` §2 arXiv ledger or Batch4/Batch5.  
> **Must-include:** GraphReader (`2406.14550`), Topology Matters / MAMA (`2512.04668`).  
> **Method:** Full arXiv HTML (ar5iv fallback) or PDF→text when HTML thin; cache `/tmp/kedger-papers/full/{id}.{html,txt,pdf}`. Mechanism cards only — not abstract skim.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Lens:** L0 capture budgets, compaction vs cognify, HARD/SOFT episode cuts, Anchor graph walks, ConflictSet / SUPERSEDES.

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new body deep-read; ID not previously FULL in CORPUS §2 arXiv ledger / Batch4 / Batch5) | **16** | GraphReader (2406.14550); MAMA / Topology Matters (2512.04668); LLMLingua (2310.05736); LongLLMLingua (2310.06839); LLMLingua-2 (2403.12968); RECOMP (2310.04408); Scissorhands (2305.17118); PyramidKV (2406.02069); Quest (2406.10774); Selective Context (2304.12102); Activation Beacon (2401.03462); SuperDialseg (2305.08371); SeCom (2502.05589); ExpeL (2308.10144); Think-on-Graph (2307.07697); Resolving Knowledge Conflicts (2310.00935) |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped (no invented content)** | **0** | Thin HTML for Selective Context / Scissorhands / SuperDialseg / FLARE-family candidates used ar5iv; all carded IDs have `.txt` ≥25k chars |
| **Identified / cached but not carded (room)** | 8 | Gist Tokens (2304.08467); MemoRAG (2409.05591); FLARE/Active RAG (2305.06983); IRCoT (2212.10509); xRAG (2405.13792); Chain-of-Note (2311.09210); ConflictRAG (2605.17301); Reading Agent gist (2402.09727 PDF) — bodies cached under `/tmp/kedger-papers/full/`, deferred |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt` (all 16 FULL IDs present).

**MAMA note:** SHAREABLE / P6 previously extracted under `ACL'26` slug; CORPUS §2 lacked arXiv `2512.04668`. This batch **fetches arXiv HTML** and cards the ID as FULL for inventory merge (not invented from prior memo alone).

**Do not invent:** Where a paper is silent (typed SUPERSEDES, capability ACL, sealed packs), silence is recorded. Numbers are from paper text/tables.

---

## 1. Mechanism cards

### 1.1 GraphReader — graph agent for long context  
**arXiv:2406.14550** · Li et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S5, S7, S8 |
| **problem** | Long-context LLMs still fail robust multi-hop over very long inputs; flat RAG chunks lose structure. |
| **representation** | Long text → chunks → **key elements** + **atomic facts** → graph nodes (normalized key elements) with **co-occurrence edges** from atomic facts. Agent holds a **notebook** of supporting facts. |
| **write / read / forget** | **Write:** graph construction compresses chunks into facts/elements. **Read:** agent plans → picks N initial nodes → coarse-to-fine explore via functions: `read_chunk`, `stop_and_read_neighbor`, `search_more`, `read_previous/subsequent_chunk`, `read_neighbor_node`, `termination`. Default practice: chunk ≈2k, N=5 starts, ≤10 function calls/path. **Forget:** not typed invalidation; exploration terminates when notebook suffices. |
| **conflict** | Silent on belief conflict; notebook aggregates supporting facts only. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Cognify should emit **atomic-fact Evidence** + element nodes, not only session summaries. (2) Hydrate = **planned graph walk** with notebook, not top-k dump. (3) Function vocabulary maps to Kedger compose steps (neighbor expand ≈ PPR/entity expand). (4) Cap walk budget (calls/path) as S7 latency knob. (5) `why` = notebook supporting facts with chunk provenance. |
| **metric_impact** | Multi-hop QA @ walk-budget; notebook recall vs chunk recall; robustness 16k–256k. Paper: outperforms GPT-4-128k full-read on long single/multi-hop mixes. |
| **refine_candidate** | **yes** — S5/S7 notebook-walk hydrate with call budget |

---

### 1.2 Topology Matters / MAMA — multi-agent memory leakage  
**arXiv:2512.04668** · 2025/26 · **FULL** (arXiv ID; prior SHAREABLE/P6 under ACL'26)

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S6, S7 |
| **problem** | Multi-agent LLM systems leak memory as a function of **communication topology**, not only prompt/ACL text. |
| **representation** | **MAMA** framework on synthetic docs with labeled PII. Agents in graphs (density, distance, centrality varied). Two-phase protocol: **Engram** (seed private info into target memory; ≤100-word MEMORY field) → **Resonance** (≤10 multi-round collab where attacker extracts). |
| **write / read / forget** | Write = Engram memory seed; Read = Resonance conversational extraction across edges; Forget = not first-class. |
| **conflict** | Integrity framed as leakage/integrity of shared memory, not SUPERSEDES. |
| **privacy** | Core result: denser connectivity, shorter attacker–target distance, higher target **centrality** ↑ leakage; early rounds dominate then plateau; spatiotemporal/location attrs leak more than identity credentials. Guidance: prefer **sparse/hierarchical** topology; limit degree/radius; **restrict hubs**. |
| **Kedger lessons** | (1) Orchestrator/CI bots must not be ambient hubs over all `repo_shared_safe` Anchors. (2) S6 seal + topology: capability-attenuated facets on high-centrality principals. (3) Measure leakage **over rounds**, not one-shot Inv-Scope. (4) Graph density is a security SLI for shared-memory edges. |
| **metric_impact** | Topology-conditioned leak rate vs density/distance/centrality; early-round AUC. |
| **refine_candidate** | **yes** — S5/S6 hub-restriction + sparse share topology fixture |

---

### 1.3 LLMLingua — coarse-to-fine prompt compression  
**arXiv:2310.05736** · Jiang et al. (MS) · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S3 |
| **problem** | CoT/ICL prompts grow to tens of thousands of tokens → cost/latency. |
| **representation** | Prompt parts: instruction / demonstrations / question. Small LM (aligned LLaMA-7B) scores token importance. |
| **write / read / forget** | **Budget controller** allocates different compression ratios to instruction vs demos vs question; demonstration-level drop then **iterative token-level** compression modeling interdependence; **distribution alignment** via instruction tuning of small LM. Up to **~20×** compression with little loss (GSM8K/BBH/ShareGPT/Arxiv-March23). |
| **conflict** | Silent. |
| **privacy** | Silent (compression can drop PII accidentally — not studied). |
| **Kedger lessons** | (1) L0→WorkingState compaction needs **part-aware budgets** (tool traces vs user ask vs system). (2) Prefer iterative token drop over one-shot entropy. (3) Align compressor distro to target model family. (4) Cognify should not re-expand discarded low-utility tokens. |
| **metric_impact** | Utility vs compression ratio on eng transcripts; latency/token $ save. |
| **refine_candidate** | **yes** — S2 part-aware compression budget |

---

### 1.4 LongLLMLingua — question-aware long-context compression  
**arXiv:2310.06839** · Jiang et al. · 2023/24 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Long context: cost ↑, quality ↓, **position bias** (lost-in-middle). Performance hinges on density/position of key info. |
| **representation** | Extends LLMLingua with **question-aware** coarse + fine compression, **document reordering** (move important docs out of middle), **dynamic** coarse/fine ratios, integrity-preserving constraints. |
| **write / read / forget** | Compress toward query; reorder for perception; NQ: up to **+21.4%** with ~**4×** fewer tokens (GPT-3.5-Turbo); LooGLE ~**94%** cost reduction claimed. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate packing should be **query-aware compress**, not FIFO truncation. (2) Reorder Evidence so load-bearing Anchors are not buried mid-context. (3) Dynamic ratios = per-Evidence compression knobs in `.kxp` packs. |
| **metric_impact** | Hydrate accuracy vs token budget + position ablation. |
| **refine_candidate** | **yes** — S7 query-aware reorder+compress |

---

### 1.5 LLMLingua-2 — task-agnostic faithful compression  
**arXiv:2403.12968** · Pan et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S3 |
| **problem** | Causal-LM entropy compression is unidirectional and misaligned with compression objective. |
| **representation** | Distill LLM → **extractive token-classification** dataset; compressor = XLM-RoBERTa-large / mBERT; keep/drop labels → **faithful** subsequence of original. Chunk-wise compression + quality controls (variation rate, alignment gap). |
| **write / read / forget** | Task-agnostic retain probs; MeetingBank / LongBench / ZeroSCROLLS / GSM8K / BBH. Faster than LLMLingua-1 small-LM path. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Prefer **extractive** compression for L0 auditability (dropped tokens recoverable). (2) LightMem-style sensory stage: LLMLingua-2 before cognify (already hinted in P1). (3) Bidirectional encoder beats causal entropy for general transcripts. |
| **metric_impact** | Faithfulness (reconstruction) × downstream QA under ratio `r`. |
| **refine_candidate** | no (feeds SeCom/LightMem path; LongLLMLingua owns hydrate ticket) |

---

### 1.6 RECOMP — retrieve-compress + selective augmentation  
**arXiv:2310.04408** · Xu, Shi, Choi · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | RALMs prepend bulky retrieved docs; many are irrelevant. |
| **representation** | Dual compressors: **extractive** (select useful sentences) + **abstractive** (synthesize multi-doc summary). Training uses end-task signal from black-box LM; critic filter; can emit **empty string** = **selective augmentation** (skip prepend). Compression rates as low as **~6%** with minimal loss (LM + ODQA: NQ/TriviaQA/HotpotQA). |
| **write / read / forget** | Compress at retrieve time; transfer compressors across LMs for LM task; faithfulness analyzed. |
| **conflict** | Empty summary when docs unhelpful — soft conflict/irrelevance gate, not SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate must support **null Evidence pack** (abstain/skip) when retrieval is junk. (2) Extractive path for auditable S8; abstractive for budgeted digests. (3) Train/tune compressor with task reward, not generic summarization. |
| **metric_impact** | Selective-augment rate + QA@compressed tokens; false-skip rate. |
| **refine_candidate** | **yes** — S7 empty-pack selective augment |

---

### 1.7 Scissorhands — persistence-of-importance KV eviction  
**arXiv:2305.17118** · Liu et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2 |
| **problem** | KV cache can exceed model weights; limits batch/throughput. |
| **representation** | **Persistence of Importance:** tokens that mattered once tend to matter later. Maintain importance record over history window `w`, recent window `r`; when `n > B`, drop `m` least-important (Alg. 1–2). **No finetune.** Up to **~5×** KV memory cut w/o quality loss; combinable with 4-bit quant. |
| **write / read / forget** | Forget = test-time eviction under fixed budget `B`. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) WorkingState eviction should track **historical importance**, not only recency (complements StreamingLLM sinks + H₂O). (2) Expose `B/w/r/m` as S2 knobs next to MemGPT 70/100% pressure. (3) Don't equate “evicted from KV” with “deleted from L0” — keep Evidence on disk. |
| **metric_impact** | Quality vs KV budget B on long eng sessions. |
| **refine_candidate** | no (constants support; PyramidKV/Quest refine path preferred) |

---

### 1.8 PyramidKV — pyramidal layer-wise KV budgets  
**arXiv:2406.02069** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2 |
| **problem** | Uniform KV budgets ignore layer-wise attention funneling. |
| **representation** | Observation: **Pyramidal Information Funneling** — lower layers scatter, higher layers consolidate to sinks/massive activations. **PyramidKV** allocates **more KV in lower layers, less in higher**. LongBench: match full-KV quality at **~12%** KV retained. |
| **write / read / forget** | Layer-heterogeneous eviction; recent + historically significant retained. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) If Kedger ever pins model-side caches, use **layer-aware** budgets. (2) Conceptual map: L0 keeps wide detail; L1/L2 digests funnel — don't store full fidelity at every tier. (3) Ablate uniform vs pyramidal retention in compaction evals. |
| **metric_impact** | Long-context utility @ %KV retained (layer sweep). |
| **refine_candidate** | no |

---

### 1.9 Quest — query-aware KV page selection  
**arXiv:2406.10774** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Token criticality for attention is **query-dependent**; static eviction hurts. |
| **representation** | Page KV cache; track per-page Key **min/max**; estimate page criticality from Query; attend Top-K pages only. Up to **~7.03×** attention speedup, **~2.23×** decode E2E; up to **~4.5×** vs prior at same accuracy. |
| **write / read / forget** | Soft sparsity at read time (pages not permanently deleted). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate Evidence selection should be **query-aware**, not static Heat-only. (2) Page/min-max metadata idea → cheap prefilters before embedding rerank. (3) Distinguish permanent SUPERSEDES vs transient non-load. |
| **metric_impact** | Hydrate latency vs recall@Top-K pages/Evidence. |
| **refine_candidate** | no (LongLLMLingua covers query-aware packing ticket) |

---

### 1.10 Selective Context — self-information filtering  
**arXiv:2304.12102** · Li et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3 |
| **problem** | Fixed context length wastes slots on low-information content. |
| **representation** | Compute **self-information** of lexical units (sentence/phrase/token); **percentile-based** retain of most informative units (adaptive vs fixed top-k). Eval: summarization/QA on papers, news, transcripts; reconstruction probes. |
| **write / read / forget** | Filter before LLM call; dropped units may be reconstructable poorly — measure. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Cheap first-pass L0 filter before LLM cognify. (2) Prefer percentile thresholds (portable across session lengths). (3) Pair with extractive LLMLingua-2 for faithfulness. |
| **metric_impact** | Downstream QA vs percentile `p`; reconstruction gap. |
| **refine_candidate** | no |

---

### 1.11 Activation Beacon — plug-in activation compression  
**arXiv:2401.03462** · Zhang et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2 |
| **problem** | Soft-prompt compression bottlenecks long-context information. |
| **representation** | Plug-in module compresses **activations (K/V per layer)** directly; fine-grained units compressed progressively; trained across compression ratios. Reports **~2×** inference accel and **~8×** KV memory reduction in abstract claims; supports flexible ratios. |
| **write / read / forget** | Beacon tokens stand in for compressed spans; not symbolic memory. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Distinguishes **neural KV compression** from **symbolic Anchor compaction** — Kedger v1 stays symbolic for audit. (2) Use as upper-bound efficiency reference for S2 budgets. (3) Progressive unit compression ↔ chunked L0→L1 pipeline. |
| **metric_impact** | Supporting only — compare symbolic compress vs activation compress cost curves. |
| **refine_candidate** | no |

---

### 1.12 SuperDialseg — supervised dialogue segmentation  
**arXiv:2305.08371** · Jiang et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S3 |
| **problem** | Unsupervised topic seg lacks labels; boundary definition ambiguous. |
| **representation** | Boundaries defined via **document-grounded** dialogues (utterance grounded on document spans). Dataset **SuperDialseg**: **9,478** dialogues from doc2dial-style corpora + inherited annotations. Benchmark: **18 models / 5 categories**. Score mixes F1, \(P_k\), WindowDiff: \(\mathrm{Score}=(2F1+(1-P_k)+(1-WD))/4\). |
| **write / read / forget** | Segmentation = episode candidates; not memory write API. |
| **conflict** | Boundary ambiguity noted (moderate annotator agreement). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Prefer **grounding-change** HARD boundaries (file/doc/ADR focus shift) over pure lexical topic. (2) Adopt multi-metric boundary score, not F1 alone (aligns with GranularityTopicSeg FULL). (3) Supervised seed set for eng dialogue→episode labeling. |
| **metric_impact** | Boundary F1 / \(P_k\) / WD on eng transcripts. |
| **refine_candidate** | **yes** — S3 grounding-aware boundary metric |

---

### 1.13 SeCom — segment memory + compression denoising  
**arXiv:2502.05589** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Turn- / session- / summary-level memory banks each fail retrieval accuracy or semantic quality. |
| **representation** | **SeCom:** conversation **Segmentation** into topically coherent segments (zero-shot + reflection on limited labels) → memory bank at **segment granularity**; **LLMLingua-2 compression as denoising** before retrieval. Wins on **LOCOMO** and Long-MT-Bench+; removing denoise drops up to **~9.46** GPT4Score on LOCOMO. |
| **write / read / forget** | Write segments (+ optional compress); retrieve segment units; summarization baselines underperform segment units. |
| **conflict** | Silent on typed conflict; denoise reduces retrieval noise. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Default L2 unit = **topic segment**, not turn or whole session. (2) Run extractive compress **before** embed/retrieve (LightMem sensory). (3) Reflection-on-few-labels = cheap way to adapt boundary model to eng corpora. (4) Ablate granularity as first-class fixture dimension. |
| **metric_impact** | LOCOMO-style retrieval accuracy × granularity × denoise on/off. |
| **refine_candidate** | **yes** — S3 segment-level memory units + denoise |

---

### 1.14 ExpeL — experiential learning without weight updates  
**arXiv:2308.10144** · Zhao et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7, S8 |
| **problem** | API LLMs can't finetune; need learning from trajectories without parametric updates. |
| **representation** | Pool of success/failure experiences (gathered via ReAct/Reflexion). Extract natural-language **insights**; at inference retrieve top-k similar successes as demos + prepend insights. Cross-task **transfer** of insights observed. |
| **write / read / forget** | Write experiences + abstracted insights; read via similarity; no typed forget. |
| **conflict** | Failures used to shape insights; not SUPERSEDES algebra. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Keep **failure Evidence** first-class (with Memento 2). (2) Promote path: trajectories → insight Anchors (L3) + case Evidence (L2). (3) Insight extraction = offline cognify job. (4) Transfer learning ≈ cross-workstream promote with provenance. |
| **metric_impact** | Success rate with/without insight bank; cross-task forward transfer. |
| **refine_candidate** | no (Memento2/case-bank tickets already cover) |

---

### 1.15 Think-on-Graph (ToG) — LLM⊗KG beam exploration  
**arXiv:2307.07697** · Sun et al. · 2023/24 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | LLM hallucination on deep reasoning; static KG-RAG underuses structure. |
| **representation** | Paradigm **LLM⊗KG**: LLM agent iteratively **beam-searches** KG. Each depth: **relation exploration** → **entity exploration** → prune to width N → reason whether enough to answer. Relation-based ToG-R variant. Traceable/correctable paths. |
| **write / read / forget** | Read-only exploration of external KG; depth/width ablations matter; naive top-1 beam accumulates calibration error — keep top-N. |
| **conflict** | Responsible reasoning / refuse when insufficient; not belief update. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S5 hydrate = beam walk with explicit depth/width caps (alongside HippoRAG PPR). (2) Persist explored paths as S8 `why` chains. (3) Prefer top-N beams over greedy. (4) Relation-first exploration useful when Anchor edge types are rich. |
| **metric_impact** | Multi-hop accuracy vs depth/width; path faithfulness; refuse rate. |
| **refine_candidate** | no (GraphReader notebook-walk ticket primary) |

---

### 1.16 Resolving Knowledge Conflicts in LLMs  
**arXiv:2310.00935** · Wang et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S7, S8 |
| **problem** | Parametric vs contextual knowledge conflicts; unclear desiderata for model behavior. |
| **representation** | Framework with synthetic conflict creation; three tasks: (1) detect contextual conflict, (2) pinpoint conflicting spans, (3) generate **distinct answers**/viewpoints. Progressive difficulty. Proposed prompting approaches per task. |
| **write / read / forget** | Eval/prompts; not a memory store. Shows models often fail to pinpoint + produce distinct answers. |
| **conflict** | Core contribution — identification, localization, multi-view generation. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) ConflictSet UX must **surface both sides**, not silently pick parametric prior. (2) S8 `why` should cite conflicting Evidence spans. (3) Promote gate: require conflict ID before overwrite/SUPERSEDES. (4) Fixtures for detect / pinpoint / distinct-answer triad (complements Adaptive Chameleon). |
| **metric_impact** | Conflict detect F1; span pinpoint; distinct-answer coverage. |
| **refine_candidate** | **yes** — S4/S8 conflict pinpoint + distinct-answer fixture |

---

## 2. Cross-cutting map → Kedger stages

| Stage | Papers | Takeaway |
|-------|--------|----------|
| S1 hooks | LLMLingua family, Selective Context, Scissorhands, PyramidKV, Beacon | Capture/compaction before cognify; part-aware budgets |
| S2 working | LongLLMLingua, Quest, PyramidKV, Scissorhands, SeCom denoise | Query-aware packing; importance+layer eviction; compress≠delete L0 |
| S3 cognify | SuperDialseg, SeCom, ExpeL, GraphReader construction, LLMLingua-2 | Segment units; grounding boundaries; atomic facts; insights from failures |
| S4 promote | ExpeL insights, MAMA hub rules, Knowledge Conflicts | Don't auto-share hub-wide; conflict detect before promote |
| S5 graph | GraphReader, ToG, MAMA topology | Planned walks + beam paths; sparse share topology |
| S6 seal | MAMA | Topology × centrality leakage probes |
| S7 hydrate | LongLLMLingua, RECOMP, Quest, SeCom, GraphReader, ToG | Query-aware compress/reorder; empty pack; notebook/beam |
| S8 why | GraphReader notebook, ToG paths, Knowledge Conflicts | Supporting facts + distinct conflicting views |

---

## 3. Refine tickets (≤3)

1. **Segment-level memory + LLMLingua-2 denoise (SeCom)** — Store L2 units as topic segments (not turns/sessions); run extractive compress before embed/retrieve. Metric: LOCOMO-style retrieval accuracy and GPT-judge delta with denoise on/off; granularity ablation.  
2. **Notebook-walk hydrate with call budget (GraphReader)** — Cognify emits atomic-fact nodes; hydrate plans + expands neighbors under ≤K function calls; `why` returns notebook Evidence IDs. Metric: multi-hop accuracy @ walk budget; orphan-chunk rate.  
3. **Conflict pinpoint + distinct-answer / hub-sparse share (Knowledge Conflicts + MAMA)** — On dual Evidence, require detect→pinpoint→ConflictSet with both views in `why`; share graph forbids ambient hub orchestrators. Metric: pinpoint F1 + distinct-view coverage; topology leak rate vs density.

---

## 4. Successfully FULL-read IDs

```
2406.14550
2512.04668
2310.05736
2310.06839
2403.12968
2310.04408
2305.17118
2406.02069
2406.10774
2304.12102
2401.03462
2305.08371
2502.05589
2308.10144
2307.07697
2310.00935
```
