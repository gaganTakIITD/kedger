# Batch 9 — Eval · Privacy · Active Retrieve · Prompt-Injection Memory (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-300-fb37`  
> **Scope:** Tier-1/5 eval/privacy + FLARE/ConflictRAG-adjacent retrieve + prompt-injection memory papers **not** previously FULL in `CORPUS_INVENTORY.md` §2.  
> **Priority queue:** ConfAIde, MemBench, RealMem, Fides, HaluMem → **RE-READ** (already FULL elsewhere). FLARE/ConflictRAG already Batch8 FULL — not duplicated.  
> **Method:** Full arXiv HTML/PDF bodies; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards only.  

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new; ID not previously FULL in CORPUS §2) | **17** | AMA-Bench (2602.22769); EvoMemBench (2605.18421); AgentMemBench (2608.00009); Leakage-Abuse Attacks on Searchable Symmetric Encryption (2309.04697); DP Synthetic Text for RAG (DP-SynRAG) (2510.06719); MRMMIA (2605.27825); … |
| **RE-READ** (prior FULL; inventory backfill mapping only) | **5** | ConfAIde — contextual integrity / Can LLMs Keep a Secret? (2310.17884); MemBench — multi-scenario multi-level memory eval (2506.21605); RealMem — project-oriented memory interaction benchmark (2601.06966); Fides — IFC for AI agent planners (2505.23643); HaluMem — operation-level memory hallucination eval (2511.03506) |
| **Fetch failed / skipped** | **0** | All listed IDs have `.txt` ≥45k chars (RE-READ included) |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

---

## 1. Mechanism cards

### 1.1 AMA-Bench  
**arXiv:2602.22769** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Dialogue-centric memory benchmarks miss machine-generated agent-environment trajectories (states, actions, tool outputs). |
| **representation** | AMA-Bench: real agentic trajectories + expert QA and synthetic trajectories scaling to arbitrary length; rule-based and expert QA. AMA-Agent adds causality graph + tool-augmented retrieval. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Kedger eval needs agent-env trajectories, not only chat logs. (2) Causal/objective state beats similarity-only retrieve on long horizons. (3) GPT-5.2 ~72% on AMA-Bench — far from saturated. (4) AMA-Agent +11.16% over strongest baseline; ~57% avg accuracy in paper. |
| **metric_impact** | Agentic trajectory QA accuracy @ 32K–128K; causality-graph retrieve vs embedding-only hydrate. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.2 EvoMemBench  
**arXiv:2605.18421** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S4, S8 |
| **problem** | Existing benches don't systematically test memory update/reuse across scopes and content types. |
| **representation** | 2×2 grid: in-episode vs cross-episode × knowledge-oriented vs execution-oriented. 15 memory methods vs long-context baselines under unified protocol. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Map Kedger fixtures to four EvoMem cells (episode-local cognify vs cross-episode promote). (2) Long-context baselines stay competitive — memory SLIs must include difficult/insufficient-context cases. (3) Retrieval wins knowledge; procedural memory wins execution when structure matches. (4) No single memory form dominates all settings. |
| **metric_impact** | Per-quadrant accuracy; cross-environment transfer on execution memory. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.3 AgentMemBench  
**arXiv:2608.00009** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7, S8 |
| **problem** | Fair comparison across memory strategies (EKV, graph episodic, compression, web-augmented) lacking. |
| **representation** | Five strategies on MSC/PersonaChat/LongDial: EKV, GEM, CBS, ICW, WAM. Metrics: Recall@k, nDCG, answer score, faithfulness, footprint, latency over 491 annotated turns. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) EKV best macro recall (~0.792) but ~5100 vs ~300 tokens footprint — explicit accuracy–efficiency trade-off for S2 packs. (2) Long-range recall (gold turn many sessions back) collapses ICW/recency — dense retrieve scales. (3) CBS runner-up by inheriting turn provenance — cognify summaries need Evidence links. (4) WAM external results carry no in-corpus provenance — hydrate must tag source tier. |
| **metric_impact** | Recall@k + faithfulness + memory footprint on multi-session dialogue fixtures. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.4 Leakage-Abuse Attacks on Searchable Symmetric Encryption  
**arXiv:2309.04697** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6, S7 |
| **problem** | Forward/backward-private DSSE still leaks via access/volume patterns exploitable by leakage-abuse attacks. |
| **representation** | LAAs on DSSE schemes; keyword recovery from search/update traces despite linkability breaking. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Encrypted semantic index ≠ Inv-Scope — pattern leakage remains. (2) Prefer capability-scoped plaintext indexes under process gates + sealed `.kxp` transit, not ciphertext search as v1 security boundary. (3) Tombstone/unshare must consider access-pattern oracles. (4) Paper recovery rates up to ~93% class — treat as red-team fixture class. |
| **metric_impact** | Keyword recovery rate under SSE trace simulation; post-unshare access-pattern residual. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.5 DP Synthetic Text for RAG (DP-SynRAG)  
**arXiv:2510.06719** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6, S7 |
| **problem** | RAG corpora memorization risk when indexing sensitive text. |
| **representation** | Two-stage DP-SynRAG: soft clustering + differentially private synthetic text generation for RAG indexing/training. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Shared/community Anchor digests may need DP synthesis before publish — not raw L0. (2) Utility–privacy trade on synthetic RAG corpora informs S6 shareable tier policy. (3) Not a substitute for capability attenuation. (4) Evaluate memorization probes on published synthetic packs. |
| **metric_impact** | Downstream QA utility vs membership/memorization probes on DP-synthetic index. |
| **refine_candidate** | **no** |

---

### 1.6 MRMMIA  
**arXiv:2605.27825** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6, S7, S8 |
| **problem** | MIAs studied for training/RAG DBs but under-explored for persistent chat-agent memory. |
| **representation** | Adversary probes whether target interaction lives in agent memory via query/response signals. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Inv-Scope 404 on deny — no existence leak via hydrate APIs. (2) Rate-limit id/recipient probes on memory APIs. (3) Minimize pack metadata that confirms membership. (4) S8 must not echo stored private spans that enable MIA features. |
| **metric_impact** | MIA AUC on memory store vs baseline absent record. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.7 M3-Agent  
**arXiv:2508.09736** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S3, S7 |
| **problem** | Multimodal streaming (video/audio) needs memory beyond text dialogue benchmarks. |
| **representation** | M3-Bench-robot/web; long-term memory module with memorization + control; automatic eval on multimodal traces. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) L0 capture must normalize multimodal Evidence (not text-only hooks). (2) Memory control policy separate from answer model — maps to cognify cron vs hydrate. (3) Benchmark multimodal agent memory separately from LoCoMo-class text. (4) Silent on typed SUPERSEDES — use invalidate+audit for AV facts. |
| **metric_impact** | Multimodal QA/recall on M3-Bench vs text-only memory baselines. |
| **refine_candidate** | **no** |

---

### 1.8 MIRIX  
**arXiv:2507.07957** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S4, S5, S7 |
| **problem** | Monolithic memory modules don't separate episodic/semantic/procedural/resource facets for agents. |
| **representation** | Six memory components (Core, Episodic, Semantic, Procedural, Resource, Knowledge Vault) + multi-agent update/retrieval workflows and active retrieval design. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Map Kedger Anchor kinds to MIRIX facets — procedural ≠ episodic promote gates. (2) Active retrieval workflow ≈ S7 tiered hydrate with component-specific indexes. (3) Multi-agent memory marketplace implies capability-scoped share per component. (4) Wearable-device use case → edge capture + seal before cloud cognify. |
| **metric_impact** | Component-wise recall + update latency on MemoryAgentBench-class tasks (paper cross-eval). |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.9 Cross-Session Stored Prompt Injection  
**arXiv:2606.04425** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S3, S4, S6, S8 |
| **problem** | Prompt injection research focuses on single session; agent persistent state enables stored XSS-like attacks across sessions. |
| **representation** | Lifecycle taxonomy: persistence channels (memory, filesystem, AGENTS.md, checkpoints) + incorporation (direct load vs conditional retrieve). Sandbox toolkit + benchmark. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Treat memory writes as privileged — log causing prompt; gate promote on instruction-like content. (2) S6 unshare/tombstone must purge stored injection residues. (3) Conditional retrieve (RAG/memory) is activation path — ConflictSet before trust. (4) State-centric security, not interaction-only filters. |
| **metric_impact** | Attack success rate across persistence channels/models; residual activation after unshare. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.10 LPCI  
**arXiv:2507.10457** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S3, S6, S7 |
| **problem** | Encoded/delayed payloads in memory/vector stores bypass input filters and trigger across sessions. |
| **representation** | LPCI lifecycle: tool poisoning → logic-layer payload → role override via memory entrenchment → vector persistence. 1700 structured tests; up to ~49% execution on less-protected models. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Memory integrity validation + prompt risk scoring at cognify/write. (2) Vector-store payload persistence ≈ MINJA/AgentPoison class — provenance gates. (3) Runtime attestation for external tool/docs feeding L0. (4) Enterprise agent memory needs session-aware controls beyond static PI regex. |
| **metric_impact** | LPCI execution rate @ model/platform; detection precision of memory-integrity scanner. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.11 REPLUG  
**arXiv:2301.12652** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Retrieval-augmented LMs often require white-box cross-attention training. |
| **representation** | Tuneable retriever + frozen LM; prepend retrieved docs to input; LM likelihood weights supervise retriever. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) S7 can swap retrieve-then-prepend without finetuning reader — matches black-box API hydrate. (2) Retriever tuning signal from LM feedback ≈ eng-judgment on hydrate utility. (3) FLARE-adjacent: forward needs still require active/interleaved variants. (4) Paper gains ~4–6% on knowledge tasks — retrieve quality dominates. |
| **metric_impact** | End-task accuracy vs retrieve@k ablation on fixed LM reader. |
| **refine_candidate** | **no** |

---

### 1.12 DSP  
**arXiv:2212.14024** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Composing retrieval and LMs for knowledge-intensive NLP lacks modular training-free patterns. |
| **representation** | Pipeline: demonstrate (ICL templates) → search (retrieve) → predict (LM); composes independently tuned modules. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Hydrate pack compile = modular DSP stages — demo facets, search Evidence, predict answer/`why`. (2) Swap search module without retraining cognify — aligns plugin retrievers. (3) FLARE/IRCoT extend with interleaving; DSP is single-shot compose baseline. (4) Strong multi-hop gains when search module matched to task. |
| **metric_impact** | Multi-hop QA F1 vs module ablation (demonstrate/search/predict). |
| **refine_candidate** | **no** |

---

### 1.13 Astute RAG  
**arXiv:2410.07176** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S7, S8 |
| **problem** | Imperfect retrieval introduces noise and parametric–context conflicts that hurt RAG. |
| **representation** | Adaptive internal knowledge generation + iterative source-aware consolidation + answer finalization before generation. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Conflict-aware where noted. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) S4/S7 ConflictSet before pack compile — Astute consolidation ≈ pre-hydrate conflict resolve (ConflictRAG-adjacent). (2) Allow parametric fallback when retrieve set is noisy. (3) Source-aware weighting mirrors Anchor provenance fields. (4) Paper reports large gains under real-world imperfect retrieval. |
| **metric_impact** | Answer correctness under noisy/contradictory retrieve sets vs vanilla RAG. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.14 Riddle Me This  
**arXiv:2502.00306** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6, S7 |
| **problem** | Standard MIA queries detectable; RAG systems leak membership via interrogation-style prompts. |
| **representation** | Interrogation attack: generated queries + ground-truth answer matching for membership inference on RAG corpora. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Hydrate APIs must not enable high-precision membership oracles on sealed packs. (2) Rate-limit + perturb responses on repeated probe patterns. (3) Complements MRMMIA/RAG-MIA fixtures. (4) Stealthy probes harder to block with regex — behavioral detection. |
| **metric_impact** | MIA AUC under stealthy interrogation vs naive shadow-model attack. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.15 Review of LLM-Agent Paradigms (tool/RAG/planning/feedback)  
**arXiv:2406.05804** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Agent memory eval must sit inside broader tool-use/planning/feedback paradigms. |
| **representation** | Survey taxonomy: LLM-profiled roles, task universality (decision vs information envs), tool/RAG/planning/feedback learning clusters. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Kedger hooks capture tool/RAG traces as L0 — align with survey's information-processing envs. (2) Memory maintenance latency must be measured inside full agent loop, not isolated QA. (3) Feedback-learning agents need SUPERSEDES on policy updates. (4) Use as bibliography harvest for tier-1/2 runway. |
| **metric_impact** | Taxonomy coverage checklist for eval harness env classes. |
| **refine_candidate** | **no** |

---

### 1.16 LLM-Augmented Agents in Melting Pot  
**arXiv:2403.11381** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S6, S8 |
| **problem** | Multi-agent cooperation with LLM-augmented agents under-evaluated in memory-sharing settings. |
| **representation** | Melting Pot environments; GPT-4/3.5 LAAs; cooperation metrics vs reference policies. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Shared-memory topology affects cooperation — complements MAMA hub-restriction fixtures. (2) Memory of prior episodes can help or hinder social dilemmas — test promote gates. (3) Eval privacy leakage in multi-agent + shared graph settings. (4) Preliminary: cooperation propensity but imperfect coordination. |
| **metric_impact** | Cooperation rate vs memory-sharing policy ablation in gridworld/social dilemmas. |
| **refine_candidate** | **no** |

---

### 1.17 Automatic Universal Prompt Injection Attacks  
**arXiv:2403.04957** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | Manual prompt injections don't scale; need optimization-based universal attacks on integrated LLM apps. |
| **representation** | Momentum gradient search on prompt suffixes/prefixes with universal transfer objectives across models/apps. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Privacy/security focus. |
| **Kedger lessons** | (1) Untrusted Evidence in hydrate must pass injection scanner before entering WorkingState. (2) Universal suffixes transfer — don't rely on single-model regex defenses. (3) Combine with HouYi/AgentDojo fixtures from Batch7/8. (4) Attack success ~50%+ class in paper on open models — assume hostile reader. |
| **metric_impact** | Attack success rate (ASR) vs defense stack on tool-integrated apps. |
| **refine_candidate** | **yes** — S6/S7 fixture ticket |

---

### 1.18 ConfAIde  
**arXiv:2310.17884** · **RE-READ** (Batch2/P6 FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6, S8 |
| **note** | Prior FULL deep-read; re-extracted for Batch 9 Kedger S1–S8 mapping. Does **not** count toward NEW FULL quota. |
| **refine_candidate** | **yes** where eval/privacy probes already ticketed in `EVAL_HARNESS.md` |

---

### 1.19 MemBench  
**arXiv:2506.21605** · **RE-READ** (Batch2/BATCH_SYSTEMS FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7, S8 |
| **note** | Prior FULL deep-read; re-extracted for Batch 9 Kedger S1–S8 mapping. Does **not** count toward NEW FULL quota. |
| **refine_candidate** | **yes** where eval/privacy probes already ticketed in `EVAL_HARNESS.md` |

---

### 1.20 RealMem  
**arXiv:2601.06966** · **RE-READ** (P5/Batch4 RE-READ)

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7, S8 |
| **note** | Prior FULL deep-read; re-extracted for Batch 9 Kedger S1–S8 mapping. Does **not** count toward NEW FULL quota. |
| **refine_candidate** | **yes** where eval/privacy probes already ticketed in `EVAL_HARNESS.md` |

---

### 1.21 Fides  
**arXiv:2505.23643** · **RE-READ** (Batch2/P6 FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S4, S6 |
| **note** | Prior FULL deep-read; re-extracted for Batch 9 Kedger S1–S8 mapping. Does **not** count toward NEW FULL quota. |
| **refine_candidate** | **yes** where eval/privacy probes already ticketed in `EVAL_HARNESS.md` |

---

### 1.22 HaluMem  
**arXiv:2511.03506** · **RE-READ** (BATCH_SYSTEMS FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S8 |
| **note** | Prior FULL deep-read; re-extracted for Batch 9 Kedger S1–S8 mapping. Does **not** count toward NEW FULL quota. |
| **refine_candidate** | **yes** where eval/privacy probes already ticketed in `EVAL_HARNESS.md` |

---

## 2. Successfully FULL-read IDs (NEW only)

```
2602.22769
2605.18421
2608.00009
2309.04697
2510.06719
2605.27825
2508.09736
2507.07957
2606.04425
2507.10457
2301.12652
2212.14024
2410.07176
2502.00306
2406.05804
2403.11381
2403.04957
```

**RE-READ IDs (not counted NEW):**
```
2310.17884
2506.21605
2601.06966
2505.23643
2511.03506
```
