# Batch 15 — Eval Runway · Multi-hop · Temporal · Dialogue Memory (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-300-fb37`  
> **Scope:** Final **8 NEW FULL** tier-1/3 runway papers from seed queue not yet in `CORPUS_INVENTORY.md` §2 — closes **300 FULL** milestone (292→300).  
> **Method:** Full arXiv HTML/ar5iv or PDF→text; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards only.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Lens:** Interactive agent eval, multi-hop hydrate, temporal SUPERSEDES, multi-session cognify, retrieve lineage, tool-user reliability

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new body deep-read; ID not previously FULL in CORPUS §2) | **8** | AppWorld (`2407.18901`); MuSiQue (`2108.00573`); RealTime QA (`2207.13332`); SituatedQA (`2109.06157`); MSC / Beyond Goldfish Memory (`2107.07567`); FiD (`2007.01282`); SWE-bench (`2310.06770`); τ-bench (`2406.12045`) |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped** | **0** | τ-bench ar5iv truncated → **PDF extract** (130k chars); all 8 IDs have `.txt` ≥26k chars |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

---

## 1. Mechanism cards

### 1.1 AppWorld — interactive coding agents in app sandbox
**arXiv:2407.18901** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7, S8 |
| **problem** | Tool benchmarks test simple API call sequences; real agents need iterative rich code over multi-app state. |
| **representation** | AppWorld Engine: 9 apps, **457** APIs, ~100 simulated users; Benchmark: **750** tasks, state-based unit tests, collateral-damage checks. |
| **write / read / forget** | Agents read/write app DB state via generated code; evaluation compares final DB to goal state (not action trace match). |
| **conflict** | Unintended side effects flagged as collateral damage. |
| **privacy** | Per-user simulated credentials in sandbox — not crypto seal. |
| **Kedger lessons** | (1) Dogfood needs **state-based** graders like AppWorld, not string-match hooks. (2) Multi-app memory = cross-workstream Anchors with audit. (3) GPT-4o ~49% normal / ~30% challenge — long-horizon memory still open. (4) Collateral-damage probes ↔ Inv-Scope side-effect tests. |
| **metric_impact** | Task success + collateral-damage rate on interactive coding trajectories. |
| **refine_candidate** | **yes** — state-based eval harness |

---

### 1.2 MuSiQue — multihop via composed single-hop questions
**arXiv:2108.00573** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Multihop QA datasets often solvable via shortcuts without true multi-step reasoning. |
| **representation** | Bottom-up construction: compose pairs of single-hop questions with shared entities; **~25k** 2–4 hop questions; harder than HotpotQA/2Wiki at matched hop count. |
| **write / read / forget** | Eval-only; tests retrieve+reason chains over multiple evidence pieces. |
| **conflict** | Composed questions require consistent bridging entities — silent on SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate fixtures should require **all** Evidence IDs, not single-chunk luck. (2) Shortcut-resistant construction ≈ typed Anchor dependency chains in eval. (3) Report per-hop-count slices. (4) Pair with IRCoT/GraphReader interleaved retrieve patterns. |
| **metric_impact** | Multi-hop EM/F1 by hop count vs shortcut-prone baselines. |
| **refine_candidate** | **yes** — multi-hop hydrate recall |

---

### 1.3 RealTime QA — dynamic weekly QA about the present
**arXiv:2207.13332** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S7, S8 |
| **problem** | Static QA benchmarks assume frozen world; deployed systems must answer about **now**. |
| **representation** | Weekly release of ~**30** multiple-choice questions from news (CNN, The Week, USA Today); ongoing platform since Jun 2022; six real-time baselines (open/closed book + retrieval). |
| **write / read / forget** | Read = fresh retrieval over current corpus; stale parametric answers fail even with updated docs when evidence insufficient. |
| **conflict** | Facts change weekly — SUPERSEDES / invalidation stress test. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Anchor `valid_from`/`invalid_at` must be first-class for temporal SUPERSEDES. (2) Hydrate should detect **unanswerable with current Evidence** and abstain. (3) Weekly cadence ≈ rolling eval harness for promote/hydrate SLIs. (4) GPT-3 updates with new docs but returns outdated answers when retrieval thin. |
| **metric_impact** | Weekly accuracy + abstention when evidence stale/missing. |
| **refine_candidate** | **yes** — temporal invalidation + abstention |

---

### 1.4 SituatedQA — extra-linguistic temporal/geographic context
**arXiv:2109.06157** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S7, S8 |
| **problem** | QA evals ignore when/where a question is asked; answers vary by temporal and geographic context. |
| **representation** | Open-retrieval QA with (question, context, answer) triples; ~**16.5%** of NQ-Open context-dependent; temporal + geographical alternate contexts crowd-sourced. |
| **write / read / forget** | Context value (date/location) must bind hydrate pack; models trained on past data drop ~**15** points on present-time questions even with updated corpus. |
| **conflict** | Same question, different contexts → different correct answers (not factual error — situational SUPERSEDES). |
| **privacy** | Geographic context — light Inv-Scope for locale-bound Anchors. |
| **Kedger lessons** | (1) Hydrate packs need explicit **situation** metadata (time, locale). (2) Promote must not collapse context-specific Anchors. (3) Eval slices: frequently-updated vs uncommon locations. (4) Pair with RealTime QA for temporal; PrefEval for preference. |
| **metric_impact** | Context-conditioned EM + present-time generalization gap. |
| **refine_candidate** | **yes** — situation-bound hydrate |

---

### 1.5 MSC — Multi-Session Chat / Beyond Goldfish Memory
**arXiv:2107.07567** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Dialogue models trained/evaluated on short chats; long-term open-domain conversation under-studied. |
| **representation** | Human-human **5-session** chats (≤14 utterances/session) with hours/days between sessions; session summaries of important personal points annotated. |
| **write / read / forget** | Baselines: RAG/FiD over full history; **SumMem** read-write summarizing memory; truncation fails on long history. |
| **conflict** | Silent. |
| **privacy** | Personal facts in summaries — capability/ACL relevant. |
| **Kedger lessons** | (1) MSC = canonical multi-session cognify fixture (used by AgentMemBench, EvolMem). (2) On-the-fly summarize→store ≈ cognify L2 digests. (3) RAG memory never forgets but costs grow — budget SLI. (4) Session-gap boundaries ↔ IDLE_BOUNDARY + SESSION_END hooks. |
| **metric_impact** | BLEU/F1/DISTINCT across sessions vs truncation/RAG/SumMem. |
| **refine_candidate** | **yes** — multi-session cognify fixture |

---

### 1.6 FiD — Fusion-in-Decoder retrieval-augmented generation
**arXiv:2007.01282** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | Generative QA without retrieval needs huge LMs; retrieve-then-read pipelines under-use cross-passage attention. |
| **representation** | **Fusion-in-Decoder (FiD):** encode each retrieved passage independently; decoder cross-attends to **all** passages jointly; T5-base/large/xl variants. |
| **write / read / forget** | Read-only retrieve at inference; no memory write. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate pack compile = FiD-style multi-Evidence reader (encode Anchors separately, fuse at generation). (2) Lineage anchor for Atlas/REPLUG/BATCH14 retrieve cluster. (3) Top-k passage count is a budget knob. (4) Prefer late fusion over naive concat for long Evidence sets. |
| **metric_impact** | Open-domain QA EM vs concat-RAG at matched retrieve k. |
| **refine_candidate** | no (lineage; S7 pack fusion already tracked) |

---

### 1.7 SWE-bench — real GitHub issue resolution
**arXiv:2310.06770** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7, S8 |
| **problem** | LM evals lack realistic software-engineering frontier; need sustainable hard testbed. |
| **representation** | **2,294** Issue–PR pairs from **12** Python repos; agent given codebase + issue text; graded by running repo test suite on generated patch. |
| **write / read / forget** | Read = repo context + issue; write = patch; forget N/A — eval is one-shot resolve. |
| **conflict** | Silent. |
| **privacy** | Public repos only. |
| **Kedger lessons** | (1) Kedger dogfood ≈ SWE-bench class: hooks capture L0, hydrate prior Anchors, patch is promote output. (2) Functional test grader > BLEU for eng tasks. (3) Best models still low resolve rate — memory of prior fixes across sessions is open. (4) Trajectory logging for `why` provenance on failed patches. |
| **metric_impact** | % resolved (tests pass) on full/lite subsets. |
| **refine_candidate** | **yes** — functional resolve harness |

---

### 1.8 τ-bench — tool-agent-user interaction with pass^k reliability
**arXiv:2406.12045** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S4, S7, S8 |
| **problem** | Benchmarks ignore human-in-the-loop tool use and domain policy compliance; single-trial success hides inconsistency. |
| **representation** | Simulated user + agent with domain APIs + policy guidelines; retail/airline domains; DB-state grading; **pass^k** metric (success on all k independent trials). |
| **write / read / forget** | Tool calls mutate simulated DB; policy engine constrains allowed actions. |
| **conflict** | Policy violations vs user intent conflicts. |
| **privacy** | Domain policies ≈ capability IFC (pair with Fides/CaMeL). |
| **Kedger lessons** | (1) pass^k ↔ Kedger reliability SLI for repeated hydrate/recall under noise. (2) GPT-4o <50% success; pass^8 <25% retail — memory of prior turns/policy critical. (3) State-based grading like AppWorld/WebArena. (4) Policy doc = sealed pack visibility rules. |
| **metric_impact** | pass^k @ k∈{1,4,8} per domain + policy violation rate. |
| **refine_candidate** | **yes** — pass^k reliability fixture |

---

## 2. Batch delta summary

| Metric | Value |
|--------|------:|
| New FULL (unique IDs) | **8** |
| Prior CORPUS FULL count | 292 |
| Post-batch FULL count | **300** |
| Target milestone | **300** ✓ |
