# Batch 5 — Eval / Failure-Mode Deep-Read (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch5-eval-full-fb37`  
> **Scope:** Tier-1 **eval / failure-mode** literature **not** already FULL in CORPUS_INVENTORY / Batch4 (no ConfAIde, MemBench, RealMem, MAB, LoCoMo, LME, HaluMem, MemoryArena, FLEX, PrefEval, Memento2, LME-V2, CaMeL).  
> **Method:** Full arXiv HTML (ar5iv fallback) or PDF→text when HTML thin; cache `/tmp/kedger-papers/full/{id}.{html,txt,pdf}`. Mechanism cards only — not abstract skim.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Lens:** Anchors+Evidence, SUPERSEDES, workstream capability, `.kxp` seal, Inv-Scope, `kedger why`.

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new body deep-read; not previously FULL in inventory/Batch4 for this ID) | **18** | AgentBench (2308.03688); GAIA (2311.12983); WebArena (2307.13854); CRAG Comprehensive (2406.04744); Corrective RAG (2401.15884); MultiHop-RAG (2401.15391); Adaptive Chameleon / knowledge-conflict (2305.13300); FreshLLMs/FreshQA (2310.03214); LongBench (2308.14508); LongBench v2 (2412.15204); RULER (2404.06654); ∞Bench (2402.13718); Self-RAG (2310.11511); RGB (2309.01431); PerLTQA (2402.16288); NeedleBench (2407.11963); HotpotQA (1809.09600); 2WikiMultiHopQA (2011.01060) |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped (no invented content)** | **0** | LongBench + LongBench v2 HTML were thin (~8 KB ar5iv stubs) → **PDF extracts used** (66k / 87k chars) and counted FULL |
| **Identified but not carded** | — | Survey-seed “ConflictQA” maps to Adaptive Chameleon (2305.13300) — paper names **counter-memory** construction, not a “ConflictQA” title string in body |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt` (all 18 IDs present, each ≥48k chars).

**Do not invent:** Where a paper is silent (typed SUPERSEDES, capability ACL, sealed packs), silence is recorded. Numbers are from paper text/tables.

---

## 1. Mechanism cards

### 1.1 AgentBench — Evaluating LLMs as Agents  
**arXiv:2308.03688** · Liu, Yu, Zhang, et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7, S8 |
| **problem** | Need multi-environment quantitative eval of LLMs **as interactive agents**, not single-task QA. |
| **write / read / forget** | Interactive trajectories across **8 environments** (Code: OS / DB / KG; Game: card / lateral puzzles / ALFWorld-style house-holding; Web: shopping / browsing). Failures attributed to poor **long-term reasoning**, decision-making, instruction following. |
| **conflict** | Ambivalent effect of code training across tasks; not typed knowledge conflict. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Dogfood fixtures must be **interactive + multi-env**, not only hydrate QA. (2) Log failure taxonomy: instruction-follow vs long-horizon plan vs tool misuse. (3) Server–client harness pattern ≈ Kedger eval CLI wrapping hooks→hydrate loops. (4) Multi-round alignment data quality matters more than “more code.” |
| **metric_impact** | Per-env success + failure-reason mix for S1/S7 agent loops. |
| **refine_candidate** | **yes** — multi-env interactive failure taxonomy |

---

### 1.2 GAIA — Benchmark for General AI Assistants  
**arXiv:2311.12983** · Mialon, Fourrier, Swift, Wolf, LeCun, Scialom · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Tool-using assistants fail on conceptually simple real-world questions humans solve (~92% human vs ~15% GPT-4+plugins). |
| **write / read / forget** | **466** questions; Level 1–3 by tool/step depth; exact-match answers; web/tools/multimodal evidence. Answers retained for leaderboard on 300. |
| **conflict** | False paths / tool errors; not SUPERSEDES. |
| **privacy** | Datacard; not capability ACL. |
| **Kedger lessons** | (1) Prefer **unambiguous short answers** for CI SLIs (like GAIA exact match). (2) Stratify fixtures by tool-depth (L1–L3) for hydrate+hooks. (3) Human-easy / model-hard is a useful eng-dogfood filter. (4) Do not hide answers in training dumps — sealed gold packs. |
| **metric_impact** | Exact-match @ tool-depth levels for assistant-style tasks. |
| **refine_candidate** | no (harness pattern; AgentBench owns interactive ticket) |

---

### 1.3 WebArena — Realistic web agents  
**arXiv:2307.13854** · Zhou, Xu, Zhu, et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7 |
| **problem** | Synthetic web agents ≠ realistic multi-site tasks; need functional correctness validators. |
| **write / read / forget** | Self-hostable sites (ecommerce, forum, gitlab-like, CMS) + tools/manuals. Best GPT-4 agent **14.41%** SR vs human **78.24%**. Includes **unachievable (N/A)** intents; UA hints trade off false-impossible vs success. Paper flags future **memory** for strategy reuse. |
| **conflict** | Latent site state / permission constraints; consistency across template siblings. |
| **privacy** | User-permission constraints in UA tasks — light ACL signal. |
| **Kedger lessons** | (1) Grade **functional state**, not string match of action traces. (2) Explicit unachievable intents ↔ hydrate abstention + `why` reason codes. (3) Cross-template consistency = workstream replay SLI. (4) Memory carryover across sessions is an open gap WebArena names — feed MemoryArena-style fixtures. |
| **metric_impact** | Functional SR + UA precision/recall + template-consistency. |
| **refine_candidate** | **yes** — functional validators + UA abstention |

---

### 1.4 CRAG — Comprehensive RAG Benchmark  
**arXiv:2406.04744** · Yang, Sun, Xin, et al. (Meta) · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Prior RAG datasets miss dynamism, popularity skew, and real web/KG APIs. |
| **write / read / forget** | **4,409** QA pairs; 5 domains; **8** question categories; mock web + KG APIs; dynamism years→seconds; head/torso/tail entities. Straightforward RAG lifts ≤34% LLM → ~44%; industry SOTA still ~63% without hallucination. Harder on finance/sports, real-time, tail, set/post-process, false-premise. |
| **conflict** | False-premise + stale/dynamic facts; truthfulness scoring. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Slice hydrate metrics by **dynamism × popularity × complexity**. (2) Mock tool APIs for deterministic CI (web/KG). (3) Truthfulness (not only EM) for eng answers. (4) Head entities can **worsen** with naive RAG — prefer typed Evidence over dump-all. |
| **metric_impact** | CRAG-style truthfulness slices for S7. |
| **refine_candidate** | **yes** — dynamism/popularity hydrate slices |

---

### 1.5 Corrective Retrieval Augmented Generation (method CRAG)  
**arXiv:2401.15884** · Yan, Gu, Zhu, Ling · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7, S8 |
| **problem** | Bad retrieval contaminates generation; need corrective actions, not always-trust top-k. |
| **write / read / forget** | Lightweight **retrieval evaluator** (T5-large) → confidence → actions: use / refine (decompose–recompose knowledge strips) / **web search fallback** when Incorrect. Plug-and-play with RAG systems; compared vs Self-RAG retrievals. |
| **conflict** | Irrelevant/noisy docs filtered; not SUPERSEDES between Anchors. |
| **privacy** | Silent (web search expands blast radius). |
| **Kedger lessons** | (1) Hydrate should gate on **retrieval confidence**, not always inject. (2) Knowledge-strip refine ≈ Evidence packing before reader. (3) Incorrect → external fetch is optional; default to abstain/`why` for sealed eng. (4) Keep evaluator smaller than generator (cost SLI). |
| **metric_impact** | Evaluator calibration + corrective-action rate vs hallucination. |
| **refine_candidate** | no (feeds S7 gate design; CRAG bench owns slice ticket) |

---

### 1.6 MultiHop-RAG  
**arXiv:2401.15391** · Tang & Yang · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | RAG evals under-test **multi-hop** retrieve+reason over many evidence pieces. |
| **write / read / forget** | News KB; **2,556** queries: Inference / Comparison / Temporal / **Null**; evidence counts 0–4. Separate retrieval vs generation experiments; existing RAG unsatisfactory on both. Null queries stress hallucination refusal. |
| **conflict** | Temporal/comparison contradictions across articles. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Eng hydrate fixtures: multi-Evidence compose (comparison/temporal). (2) Null-query abstention SLI. (3) Score retrieval Recall@k of **all** required Evidence IDs, then answer EM. (4) Prefer non-Wikipedia news-like L0 to reduce parametric bleed. |
| **metric_impact** | Multi-hop retrieval recall + typed-query accuracy + null refusal. |
| **refine_candidate** | no (Hotpot/2Wiki/MultiHop family; one ticket covers) |

---

### 1.7 Adaptive Chameleon / Stubborn Sloth — knowledge conflicts  
**arXiv:2305.13300** · Xie et al. (OSU NLP) · 2023 · **FULL**  
*(survey-seed “ConflictQA”; paper constructs parametric vs **counter-memory**)*

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S7, S8 |
| **problem** | How receptive are LLMs to external evidence that conflicts with parametric memory? |
| **write / read / forget** | Elicit parametric memory (PopQA + StrategyQA); generate coherent **counter-memory** (vs brittle entity-substitution). Settings: counter-only vs dual evidence. Finding: highly receptive to coherent counter-memory alone; strong **confirmation bias** when both present. |
| **conflict** | Core: Mem-Ans vs Ctr-Ans vs Uncertain; memorization ratio. |
| **privacy** | Disinfo risk if malicious tools supply coherent counter-evidence. |
| **Kedger lessons** | (1) SUPERSEDES must win over parametric LLM bias — grade with dual-Evidence fixtures. (2) Coherent false Evidence is dangerous → seal + provenance for promote. (3) Offer Uncertain/`why` when ConflictSet non-empty. (4) Entity-sub tests underestimate receptiveness; use full conflicting passages. |
| **metric_impact** | Memorization ratio / counter-adoption under single vs dual Evidence. |
| **refine_candidate** | **yes** — dual-Evidence confirmation-bias fixture |

---

### 1.8 FreshLLMs / FreshQA  
**arXiv:2310.03214** · Vu et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S7, S8 |
| **problem** | Static QA misses fast-changing world knowledge and false premises. |
| **write / read / forget** | **FreshQA**: ~**600** questions; never-/slow-/fast-changing + **false-premise**; two-mode eval (Relaxed / Strict); search-augmented FreshPrompt. Large human judgment effort (~50k). |
| **conflict** | False premises must be rebutted; freshness conflicts with stale params. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Tag Anchors with **freshness class** + valid_at. (2) False-premise fixtures → rebut + SUPERSEDES, not answer-as-asked. (3) Strict vs Relaxed grading modes for SLIs. (4) Search-augment is optional; sealed store should answer from Evidence first. |
| **metric_impact** | Freshness-slice accuracy + false-premise rebuttal rate. |
| **refine_candidate** | no (CRAG dynamism ticket overlaps) |

---

### 1.9 LongBench  
**arXiv:2308.14508** · Bai et al. · 2023 · **FULL** (PDF; HTML stub discarded)

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Unified bilingual multitask long-context eval beyond few-k tokens. |
| **write / read / forget** | **21** datasets / 6 categories (single-/multi-doc QA, summarization, few-shot, synthetic, code); EN avg ~6.7k words; multi-doc built from HotpotQA / 2Wiki / MuSiQue. Context compression helps; commercial 16k still struggles. |
| **conflict** | Multi-doc hops; position sensitivity (lost-in-middle). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Don’t equate “fits in window” with hydrate quality — use multi-doc compose. (2) Code-repo + synthetic categories map to eng L0. (3) Unified auto-eval format for Kedger bench runners. |
| **metric_impact** | Category-averaged long-context scores as regression smoke. |
| **refine_candidate** | no |

---

### 1.10 LongBench v2  
**arXiv:2412.15204** · Bai, Tu, Zhang, et al. · 2024 · **FULL** (PDF; HTML stub discarded)

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Prior long-context benches too easy; need deep understanding/reasoning to 2M words. |
| **write / read / forget** | **503** hard MCQs; 8k–2M words; 6 categories incl. **long-dialogue history**, code repo, structured data. Human experts **53.7%** @15 min; best direct model ~50.1%; o1-preview **57.7%** with longer reasoning. RAG + inference-time compute insights. |
| **conflict** | Multi-doc / dialogue history contradictions under length. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Long-dialogue history category ≈ cognify→hydrate over episodes. (2) Hard MCQ format good for CI stability. (3) Inference-time compute vs RAG tradeoff for `why` depth. (4) Code-repo understanding fixtures for eng. |
| **metric_impact** | Hard MCQ accuracy @ length buckets + dialogue-history slice. |
| **refine_candidate** | no (RULER/NeedleBench own synthetic tickets) |

---

### 1.11 RULER — Real context size beyond NIAH  
**arXiv:2404.06654** · Hsieh, Sun, et al. (NVIDIA) · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S5, S7 |
| **problem** | Vanilla needle-in-haystack is a superficial long-context test. |
| **write / read / forget** | Synthetic suite: NIAH variants, **multi-hop Variable Tracking**, **aggregation** (CWE/FWE), QA with distractors; flexible length/complexity. 17 models; many claim ≥32k but half fail effective 32k on RULER. Failures: distractor blindness, copy-from-context, parametric fallback. |
| **conflict** | Multi-needle / hard distractors. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Kedger long-context smoke = RULER-style VT + aggregation, not only NIAH. (2) Variable tracking ≈ Anchor alias / SUPERSEDES chain following. (3) Watch parametric fallback when Evidence present. (4) Synthetic control of SNR for capacity curves. |
| **metric_impact** | Effective context length threshold @ task categories. |
| **refine_candidate** | **yes** — VT/aggregation long-context smoke (shared with NeedleBench) |

---

### 1.12 ∞Bench (InfiniteBench)  
**arXiv:2402.13718** · Zhang et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Public long-context benches cluster ~10k; need >100k average length. |
| **write / read / forget** | EN/ZH synthetic+realistic tasks requiring long dependencies (not solvable by retrieving few passages). SOTA long-context LLMs still degrade badly at 100k+. Analyses of long-context behavior; EM scoring caveats. |
| **conflict** | Long-range dependency conflicts. |
| **privacy** | Annotator ethics note. |
| **Kedger lessons** | (1) Stress cognify: store must beat stuffing 100k into prompt. (2) Tasks needing whole-context aggregation justify graph/community summaries. (3) EM fragility → normalize answer parsers in harness. |
| **metric_impact** | >100k dependency tasks as scale stress (optional nightly). |
| **refine_candidate** | no |

---

### 1.13 Self-RAG — retrieve / generate / critique  
**arXiv:2310.11511** · Asai, Wu, Wang, Sil, Hajishirzi · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7, S8 |
| **problem** | Always-retrieve RAG hurts versatility; need on-demand retrieve + critique. |
| **write / read / forget** | Train LM with **reflection tokens** (retrieve / relevance / support / utility). Adaptive retrieval; segment-level control at inference. Beats ChatGPT + RAG baselines on QA, reasoning, fact verification; better factuality/citations in long-form. |
| **conflict** | Critique unsupported claims vs Evidence. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate on-demand (hooks decide Retrieve) not always-on. (2) Reflection tokens ≈ structured `why` facets: IsRel / IsSup / IsUse. (3) Controllable inference thresholds as SLI knobs. (4) Don’t require Self-RAG fine-tune for v1 — import the critique checklist. |
| **metric_impact** | Citation support rate + adaptive-retrieval necessity accuracy. |
| **refine_candidate** | no (Corrective RAG gate overlaps) |

---

### 1.14 RGB — Retrieval-Augmented Generation Benchmark  
**arXiv:2309.01431** · Chen, Lin, Han, Sun · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Diagnose RAG ability gaps across LLMs with controlled testbeds. |
| **write / read / forget** | EN/ZH corpus from recent news + search docs. Four abilities: **noise robustness**, **negative rejection**, **information integration**, **counterfactual robustness**. LLMs OK-ish on noise; weak on rejection, integration, false info. |
| **conflict** | Counterfactual docs; integration of multi-doc facts. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Four RGB axes → four hydrate SLI families. (2) Negative rejection = empty/irrelevant Evidence → refuse. (3) Counterfactual robustness = prefer sealed Evidence over injected lies. (4) Integration axis = multi-Anchor compose. |
| **metric_impact** | RGB four-axis scores for S7 regression. |
| **refine_candidate** | no (covered by CRAG + conflict tickets) |

---

### 1.15 PerLTQA — Personal long-term memory QA  
**arXiv:2402.16288** · Du, Wang, Zhao, et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Personal QA needs semantic + episodic memory (profiles, relations, events, dialogues), not Wikipedia-only. |
| **write / read / forget** | **8,593** questions / **30** characters; memory types WK/PRO/SR/DLG/EVT. Framework: **Memory Classification → Retrieval → Synthesis**. BERT classifiers beat ChatGPT/ChatGLM3 on classification; synthesis quality depends on integration. |
| **conflict** | Cross-type memory mix-ups (semantic vs episodic). |
| **privacy** | Personal profiles/social graph — high sensitivity (paper silent on ACL). |
| **Kedger lessons** | (1) Classify memory kind before retrieve (Anchor types). (2) Persona/project profiles ≠ dialogue Evidence — separate stores. (3) Synthesis step = compose pack for reader. (4) Privacy: personal memories need Inv-Scope before any share. |
| **metric_impact** | Classification F1 + retrieval + synthesis QA for personal/project memory. |
| **refine_candidate** | no (LoCoMo/LME already cover personal chat; use for type-routing) |

---

### 1.16 NeedleBench — retrieval & reasoning across densities  
**arXiv:2407.11963** · Li, Zhang, Zhang, et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Classic NIAH is information-sparse; real tasks vary density. |
| **write / read / forget** | Single-/Multi-Retrieval + Multi-Reasoning needles; **Ancestral Trace Challenge (ATC)** as information-dense continuous reasoning. Documents **under-thinking** (premature stop) even in strong reasoning models. |
| **conflict** | Multi-needle interference; dense ancestral chains. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Pair sparse NIAH with dense ATC-like eng traces (decision chains). (2) Measure under-thinking: early abort before all Evidence used. (3) Multi-retrieval recall of *all* needles = multi-Evidence hydrate. (4) Bilingual scores if eng corpus mixed. |
| **metric_impact** | Sparse vs dense long-context scores + under-thinking rate. |
| **refine_candidate** | no (merge with RULER smoke ticket) |

---

### 1.17 HotpotQA — explainable multi-hop QA  
**arXiv:1809.09600** · Yang, Qi, Zhang, et al. · 2018 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Prior QA lacked multi-hop reasoning + explanation supervision. |
| **write / read / forget** | **113k** questions; bridge + comparison; **sentence-level supporting facts**; free-form Wikipedia multi-hop (not KB-schema-bound). |
| **conflict** | Comparison questions force multi-fact contrast. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Gold supporting sentences ≈ Evidence IDs for `why`. (2) Bridge-entity hops ≈ graph path hydrate. (3) Comparison template for eng “diff two decisions” fixtures. (4) Strong supervision of supporting facts improves explainability — keep in harness. |
| **metric_impact** | Answer EM/F1 + supporting-fact F1 as hydrate explainability. |
| **refine_candidate** | no |

---

### 1.18 2WikiMultiHopQA  
**arXiv:2011.01060** · Ho, Nguyen, Sugawara, Aizawa · 2020 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Multi-hop QA needs comprehensive reasoning-step evaluation; Hotpot shortcuts possible. |
| **write / read / forget** | Up to 5-hop template-synthesized questions from Wikidata+Wikipedia; evidence + inference paths; comparison/inference types designed to block shortcuts. |
| **conflict** | Multi-hop path contradictions / missing hops. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Require full inference-path Evidence coverage in scoring. (2) Template synthesis for deterministic eng multi-hop probes. (3) Use with Hotpot: Hotpot for natural phrasing, 2Wiki for hop-strictness. |
| **metric_impact** | Path-complete multi-hop accuracy (no shortcut credit). |
| **refine_candidate** | no |

---

## 2. Cross-cutting map → Kedger stages

| Stage | Papers | Takeaway |
|-------|--------|----------|
| S1 hooks | AgentBench, GAIA, WebArena | Interactive / tool failure taxonomy; functional validators |
| S2 working | LongBench, RULER, ∞Bench, NeedleBench | Effective context ≠ claimed window; sparse vs dense |
| S3 cognify | Self-RAG, Corrective RAG, PerLTQA, LBv2 dialogue | Classify / critique / compress before store |
| S4 promote | FreshQA, Adaptive Chameleon, PerLTQA | Freshness + conflict checks before promote |
| S5 graph | HotpotQA, 2Wiki, MultiHop-RAG, RGB | Multi-Evidence paths + integration |
| S6 seal | (light) WebArena permissions; Adaptive Chameleon disinfo | Seal provenance against coherent false Evidence |
| S7 hydrate | All RAG/long-context cards | Confidence gates, null/UA abstain, slices |
| S8 why | Hotpot supporting facts, Self-RAG reflection, RGB rejection | Evidence IDs + critique tokens + abstain reasons |

---

## 3. Refine tickets (≤3)

1. **Dual-Evidence confirmation-bias fixture (Adaptive Chameleon)** — For a sealed eng fact Anchor, inject coherent counter-Evidence; score SUPERSEDES/ConflictSet/`why Uncertain` vs silent parametric win. Metric: counter-adoption under dual evidence; false-promote rate.  
2. **CRAG-style dynamism × popularity hydrate slices** — Tag fixtures never/slow/fast + head/torso/tail; score truthfulness and abstention on real-time/false-premise.  
3. **RULER/NeedleBench long-context smoke (VT + multi-needle + under-thinking)** — Synthetic Variable Tracking + multi-Evidence recall; fail if model copies distractors or aborts before all needles used. Gate cognify necessity when window stress rises.

---

## 4. Successfully FULL-read IDs

```
2308.03688
2311.12983
2307.13854
2406.04744
2401.15884
2401.15391
2305.13300
2310.03214
2308.14508
2412.15204
2404.06654
2402.13718
2310.11511
2309.01431
2402.16288
2407.11963
1809.09600
2011.01060
```
