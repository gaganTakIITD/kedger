# Batch 23 — Survey Runway FULL (Kedger) — **honest deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Body-grounded mechanism cards (Intro/Method/Results) replacing 2026-08-08 abstract-template cards.  
> **Progress:** FULL 440 → **460**.  
> **Method:** Fulltext `/tmp/kedger-papers/full/{id}.txt` + agent deep-read cards.  
> **Kedger stages:** S1–S8  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers from body only.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body deep-read; deep-recard upgrade of Batch23) | **20** | `2405.02957`, `2405.14486`, `2405.16089`, `2405.19686`, `2406.10149`, `2406.12430`, `2406.13743`, `2407.01178`, `2408.03615`, `2408.08921`, `2408.16967`, `2409.07429`, `2409.20163`, `2410.02694`, `2410.03156`, `2410.06992`, `2410.20878`, `2411.11581`, `2411.13093`, `2412.15266` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs cached |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. Agent Hospital: A Simulacrum of Hospital with Evolvable Medical Agents
**arXiv:2405.02957** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Medical LLM agents need experiential learning without massive manual labels; hospital workflow simulation can evolve doctors via treating patient agents. |
| **representation** | Agent Hospital simulacrum: LLM patients/nurses/doctors; doctor agents evolve by treating many patient agents (no manual labels); full illness-treatment process simulation. |
| **write / read / forget** | Write: accumulate treatment experience into doctor agent memory/skills. Read: apply evolved knowledge to new patients. Forget: silent. |
| **conflict** | Silent on conflicting diagnoses protocol. |
| **privacy** | Medical PHI simulacrum — high sensitivity; silent on formal privacy tech. |
| **Kedger lessons** | (1) Experiential evolution of agents = S3 promote from successful trajectories without labeled finetune. (2) Multi-role hospital graph (patient/nurse/doctor) for S5. (3) Med accuracy after evolution is the SLI — report from paper tables when integrating. (4) Never copy sim PHI patterns into real EHR memory without Inv-Scope. |
| **metric_impact** | Doctor agent diagnostic/treatment accuracy after evolution vs non-evolved; MedQA-style probes as reported. |
| **refine_candidate** | **yes — S3 experience-evolution loop for specialist agents** |

---

### 2. RefChecker: Reference-based Fine-grained Hallucination Checker and Benchmark
**arXiv:2405.14486** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S7, S8 |
| **problem** | Hallucination detection often too coarse; need claim-level checking of LLM responses against references. |
| **representation** | RefChecker: extractor emits claim-triplets from response; checker verifies each triplet against references. Benchmark ~2.1k responses from seven LLMs; supports proprietary/open extractors/checkers. Claim-triples beat coarser units for fine-grained hallucination detection. |
| **write / read / forget** | Write: silent store — eval/check framework. Read: check claims against reference docs. Forget: silent. |
| **conflict** | Flags claims unsupported by / conflicting with references. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S4 promote should verify claim-triples, not whole-answer blobs. (2) S8 `why` can attach per-triple check outcomes. (3) Use RefChecker-style SLI for faithfulness of hydrated answers. (4) Extractor+checker separation allows cheaper open checkers in CI. |
| **metric_impact** | Hallucination detection quality (F1/human agreement) with claim-triples vs baselines on RefChecker benchmark. |
| **refine_candidate** | **yes — S4/S8 claim-triple faithfulness gate** |

---

### 3. Towards Completeness-Oriented Tool Retrieval for Large Language Models (COLT)
**arXiv:2405.16089** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | Tool retrieval often returns incomplete tool sets; collaborative multi-tool tasks fail when recall misses required tools. |
| **representation** | COLT: completeness-oriented tool retrieval in two stages — semantic learning + collaborative learning — to improve completeness of retrieved tool sets for LLM tool use. |
| **write / read / forget** | Write: train retrieval/collaborative models offline. Read: retrieve complete tool sets for a query. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S7 tool hydrate must optimize completeness (set recall), not only top-1 similarity. (2) Collaborative learning captures tool co-occurrence — graph prior on tool Anchors. (3) Incomplete tools → impossible plans; gate plan until tool-set complete. (4) Eval with completeness-oriented metrics alongside nDCG. |
| **metric_impact** | Tool retrieval completeness / recall / downstream task success on ToolBench-style settings. |
| **refine_candidate** | **yes — S7 completeness-oriented tool retrieve** |

---

### 4. Knowledge Graph Tuning (KGT): Real-time LLM Personalization based on Knowledge Graph
**arXiv:2405.19686** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S5, S7 |
| **problem** | Deployed LLMs meet personalized factual knowledge via user feedback; full model updates are slow/forgetful; need real-time personalization. |
| **representation** | KGT: extract personalized factual triples from user queries/feedback; optimize a knowledge graph without modifying LLM weights; real-time personalization with lower latency/GPU than finetuning. |
| **write / read / forget** | Write: upsert personalized triples into user KG. Read: use KG to personalize answers. Forget: KG edits can remove/replace triples (graph-native) vs catastrophic parametric forget. |
| **conflict** | Personal facts may supersede prior triples — KG update is the conflict surface. |
| **privacy** | User-specific factual KG is PII-adjacent; personalization store must be scoped per user. |
| **Kedger lessons** | (1) Prefer KG upsert over weight edits for personal Anchors (S3/S4). (2) Real-time latency/GPU savings are SLIs for personalize path. (3) Per-user KG = natural Inv-Scope boundary. (4) Long-term accumulation of personal facts should not bloat WorkingState — keep in S5 graph. |
| **metric_impact** | Personalization quality; latency; GPU memory vs finetune/adapters. |
| **refine_candidate** | **yes — S4/S5 personal KG upsert instead of weight edit** |

---

### 5. BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack
**arXiv:2406.10149** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Long-context evals don't test reasoning over facts scattered across extremely long documents (up to millions of tokens). |
| **representation** | BABILong benchmark: bury reasoning facts in long haystacks; extendable to 50M tokens; evaluates LLMs and RAG on multi-fact reasoning across length. |
| **write / read / forget** | Write: silent — benchmark. Read: models must find/reason over distributed facts. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S7 long-hydrate SLI must include multi-fact reasoning-in-haystack, not only NIAH needle find. (2) RAG ~60% on single-fact QA independent of length — retrieve≠reason. (3) Length-extendable fixtures for regression as windows grow. (4) Separate single-fact vs multi-hop long-context scores. |
| **metric_impact** | Accuracy vs context length on BABILong tasks; RAG vs long-context model curves. |
| **refine_candidate** | **yes — S7 BABILong-style multi-fact haystack SLI** |

---

### 6. PlanRAG: A Plan-then-Retrieval Augmented Generation for Generative Decision Support
**arXiv:2406.12430** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Decision QA needs planning which data to fetch; iterative RAG that retrieves from the raw question mismatches decision workflows. |
| **representation** | Decision QA task + DQA benchmark (Locating & Building from EU4/Victoria3 game DBs). PlanRAG: LM first generates a plan for decision-making, then retriever issues queries per plan; iterate plan-retrieve-answer. |
| **write / read / forget** | Write: silent persistent memory beyond session plan. Read: plan-guided retrieval over decision DB. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Default S7 for decisions: plan-then-retrieve, not question-as-query. (2) Persist plan steps as S8 `why`. (3) +15.8% Locating / +7.4% Building vs iterative RAG SOTA — lock numeric. (4) DQA scenarios useful fixtures for structured Evidence DBs. |
| **metric_impact** | Decision accuracy on DQA Locating/Building vs iterative RAG. |
| **refine_candidate** | **yes — S7 plan-then-retrieve hydrate** |

---

### 7. GenAI-Bench: Evaluating and Improving Compositional Text-to-Visual Generation
**arXiv:2406.13743** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Text-to-image/video models fail compositional prompts (attributes, relations, higher-order reasoning); evals lack rigorous human+auto compositional grading. |
| **representation** | GenAI-Bench: compositional prompts + human study; VQAScore-style automatic metrics aligned to human judgments for compositional T2V generation. |
| **write / read / forget** | Write: silent — benchmark/metric. Read: evaluate generated images/videos vs prompts. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Multimodal Evidence faithfulness needs compositional rubrics, not CLIP-only. (2) VQAScore-class metrics usable as CI SLIs when humans scarce. (3) Attribute/relation failures map to incomplete Anchor grounding. (4) Not a memory system — metric borrow only. |
| **metric_impact** | Human compositional ratings; VQAScore correlation; model leaderboards on GenAI-Bench. |
| **refine_candidate** | **no (multimodal gen eval; metric borrow only)** |

---

### 8. Memory3: Language Modeling with Explicit Memory
**arXiv:2407.01178** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | LLM knowledge in parameters is costly; text RAG is expensive at decode — need a third cheaper memory form. |
| **representation** | Memory³: explicit memory as third form after implicit (params) and working (context KV). Memory circuitry theory externalizes knowledge into explicit memories; smaller model/train/infer cost proportional to recalled knowledge; faster decode than RAG. |
| **write / read / forget** | Write: externalize knowledge into explicit memory bank. Read: recall explicit memories during LM. Forget: knowledge not in params can be updated by editing explicit memory rather than full retrain. |
| **conflict** | Silent. |
| **privacy** | Silent — explicit memory still may leak if shared. |
| **Kedger lessons** | (1) Kedger L3 Anchors ≈ explicit memory — cheaper than params and full-text RAG. (2) Keep WorkingState (KV) distinct from explicit bank. (3) Prefer explicit memory edit for knowledge update over finetune. (4) Decode-cost SLI vs RAG for hydrate design. |
| **metric_impact** | LM quality vs parameter/RAG cost; decode speed; memory size tradeoffs. |
| **refine_candidate** | **yes — S3 explicit-memory bank as third store tier** |

---

### 9. Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks
**arXiv:2408.03615** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Long-horizon Minecraft-like agents lack structured world knowledge and abstracted multimodal experience for planning/reflection. |
| **representation** | Optimus-1 Hybrid Multimodal Memory: (1) Hierarchical Directed Knowledge Graph for world knowledge; (2) Abstracted Multimodal Experience Pool summarizing history. Knowledge-guided Planner + Experience-Driven Reflector for long-horizon Minecraft tasks. |
| **write / read / forget** | Write: structure knowledge into HDKG; summarize trajectories into experience pool. Read: planner uses KG; reflector uses experiences. Forget: abstraction compresses raw history into experience summaries. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Split world KG (S5) from experience pool (S3) — Optimus hybrid. (2) Experience-driven reflect = S8 before next plan. (3) Directed hierarchical KG better than flat notes for craft tech trees. (4) Long-horizon success requires both knowledge+experience, not retrieve-only. |
| **metric_impact** | Long-horizon Minecraft task success vs baselines; ablations of KG vs experience pool. |
| **refine_candidate** | **yes — S5 HDKG + S3 experience pool hybrid memory** |

---

### 10. Graph Retrieval-Augmented Generation: A Survey
**arXiv:2408.08921** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7 |
| **problem** | Vanilla RAG struggles with relational/global structure; GraphRAG uses entity graphs for more precise/comprehensive retrieval — needs systematic review. |
| **representation** | First comprehensive GraphRAG survey: taxonomy of graph construction, retrieval, and generation; challenges and directions for structure-aware RAG. |
| **write / read / forget** | Write: surveys graph index construction from corpora. Read: surveys structure-aware retrieval. Forget: silent / index maintenance surveyed variably. |
| **conflict** | Surveys multi-hop relational reasoning; conflict handling depends on cited systems. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) P3 graph cognify feeds graph-RAG hydrate — don't duplicate community summaries as Anchors. (2) Separate graph index refresh from Anchor invalidation. (3) Use as pattern catalog for S5 walks. (4) Large survey — mechanism cards focus on agent-memory retrieve coupling. |
| **metric_impact** | Survey taxonomy; cites system benchmarks (no new single score). |
| **refine_candidate** | **no (survey catalog)** |

---

### 11. MemLong: Memory-Augmented Retrieval for Long Text Modeling
**arXiv:2408.16967** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Long-context LMs struggle with ultra-long text; need retrieval over historical memory without fully differentiable huge caches. |
| **representation** | MemLong: non-differentiable ret-mem module + partially trainable decoder-only LM; fine-grained controllable retrieval of historical information into generation; extends usable context on single GPU vs pure long-context baselines. |
| **write / read / forget** | Write: store historical segments in memory bank for retrieval. Read: retrieve historical info into decoder. Forget: memory bank selection implies non-retrieved history unused. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hybrid ret-mem + partial train is pragmatic S2/S7 for long docs. (2) Controllable fine-grained retrieve beats opaque full attention over 80K-class caches. (3) Single-GPU extendability is an ops SLI. (4) Keep ret-mem non-diff boundary explicit for audit. |
| **metric_impact** | Long-context LM benchmarks / LongBench-style; perplexity; max context on one GPU. |
| **refine_candidate** | **yes — S2/S7 ret-mem long-text modeling** |

---

### 12. Agent Workflow Memory (AWM)
**arXiv:2409.07429** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7, S8 |
| **problem** | Web agents fail long-horizon tasks; humans reuse abstracted routines — agents need workflow memory induced from trajectories. |
| **representation** | AWM: induce reusable workflows (abstract sub-routines) from trajectories; integrate into agent memory. Offline: from canonical examples. Online: from self-generated trajectories judged correct by an evaluator. Eval WebArena + Mind2Web; LM- vs rule-based induction (~35.5–35.6% WebArena SR in induction ablation). |
| **write / read / forget** | Write: induce/store workflows into memory. Read: guide future actions with workflows. Forget: silent — workflows accumulate; quality via induction filter. |
| **conflict** | Silent; agents may diverge from workflow guidelines when needed. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Promote reusable workflows (procedures) not only episodic traces. (2) Online AWM needs success judge before write — S4 gate. (3) WebArena: up to +22.5 points over non-adaptive baseline after tens of examples; +12.0 abs / +51.1% relative vs BrowserGym — lock these SLIs. (4) Abstract sub-routines > concrete full examples to avoid overfitting element IDs. |
| **metric_impact** | WebArena success rate (+22.5pp peak / +12.0 abs vs BrowserGym); Mind2Web SR; offline vs online; cross-website generalization (+8.9–14.0 abs). |
| **refine_candidate** | **yes — S3 workflow induction memory for agents** |

---

### 13. MemSim: A Bayesian Simulator for Evaluating Memory of LLM-based Personal Assistants
**arXiv:2409.20163** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Hard to objectively evaluate personal-assistant memory — constructing reliable QAs from user messages is challenging. |
| **representation** | MemSim: Bayesian Relation Network + causal generation to simulate users and build reliable QAs; MemDaily benchmark evaluates memory mechanisms of LLM personal assistants. |
| **write / read / forget** | Write: silent — simulator/benchmark for others' memory systems. Read: evaluate agents' recall on generated QAs. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Simulated personal messages — privacy-relevant eval domain; method is Bayesian generation not attack. |
| **Kedger lessons** | (1) Personal memory SLIs need causal/Bayesian QA construction, not ad-hoc quizzes. (2) MemDaily as regression suite for S7 personal hydrate. (3) High automatic QA reliability (paper reports ~0.97-class EM metrics on construction quality) — trust fixtures carefully. (4) Separate memory-mechanism eval from chitchat quality. |
| **metric_impact** | MemDaily memory QA accuracy across mechanisms; MemSim QA construction reliability. |
| **refine_candidate** | **yes — S7 MemDaily-style personal memory eval harness** |

---

### 14. HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly
**arXiv:2410.02694** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Long-context evals are narrow/noisy (e.g., NIAH); need thorough multi-category evaluation including RAG/cite/long-doc tasks. |
| **representation** | HELMET benchmark: comprehensive long-context evaluation across categories (beyond needle-in-haystack), with careful dataset reuse/refinement, model ranking comparisons vs ∞Bench, ablations. |
| **write / read / forget** | Write: silent — eval suite. Read: models consume long contexts / RAG settings per task type. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Replace NIAH-only SLIs with HELMET-style multi-category long-context suite. (2) Include RAG/citation categories for S7 pack quality. (3) Rankings can disagree with ∞Bench — don't trust one leaderboard. (4) Ablate instruction-tuned long-context failures separately from base. |
| **metric_impact** | Per-category HELMET scores; model rankings vs ∞Bench. |
| **refine_candidate** | **yes — S7 HELMET multi-category long-context SLI** |

---

### 15. Melodi: Exploring Memory Compression for Long Contexts
**arXiv:2410.03156** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Need to process long documents with short context windows via hierarchical memory compression. |
| **representation** | Melodi: short-term memory = multi-layer recurrent compression across context windows (e.g., 512→128 tokens); long-term memory = further compress & stack compressed KV in middle layer. Transformer + hierarchical compress; vs Memorizing Transformer dense 64K KV baseline. |
| **write / read / forget** | Write: recurrently compress windows into STM; stack into LTM. Read: attend compressed memories while processing current short window. Forget: STM compression drops fine tokens; LTM retains essential history compensating STM forget. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Dual STM/LTM compression maps to WorkingState vs L3 digest. (2) Paper: perplexity 10.44 PG-19 / 2.11 arXiv Math with 512-token windows — quality@short-window SLI. (3) Prefer hierarchical compress over huge dense KV memorize. (4) LTM should compensate STM loss — don't only slide-window. |
| **metric_impact** | Perplexity on PG-19 / arXiv Math vs Memorizing Transformer and compress baselines; ablations STM/LTM. |
| **refine_candidate** | **yes — S2/S3 hierarchical Melodi-style memory compress** |

---

### 16. SWE-Bench+: Enhanced Coding Benchmark for LLMs
**arXiv:2410.06992** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | SWE-bench success inflated by solution leakage and weak tests — need cleaner coding agent benchmark. |
| **representation** | Empirical study then SWE-bench+: filters cheating patches where solutions appear in issues/comments (32.67% leakage) and suspicious passes from weak tests (31.08%); tighter evaluation of LLM coding agents. |
| **write / read / forget** | Write: silent — benchmark hygiene. Read: agents read issues/repos to patch. Forget: silent. |
| **conflict** | Highlights inconsistency between claimed pass and true fix adequacy. |
| **privacy** | Notes data leakage vs model cutoffs; contamination risk. |
| **Kedger lessons** | (1) Coding-agent SLIs must filter solution leakage like SWE-bench+. (2) Weak tests ≠ correct promote — require stronger oracles. (3) 32.67% / 31.08% contamination rates → distrust raw leaderboards. (4) S8 should cite patch+tests, not issue text that embeds answers. |
| **metric_impact** | Resolved rates on cleaned SWE-bench+ vs original; leakage/suspicious-pass fractions. |
| **refine_candidate** | **yes — S7/S8 coding eval hygiene filters** |

---

### 17. AutoRAG: Automated Framework for Optimization of Retrieval Augmented Generation Pipeline
**arXiv:2410.20878** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Many RAG modules exist; best combination is dataset-dependent and expensive to find manually. |
| **representation** | AutoRAG: auto-search over RAG pipeline modules (query expansion, decomposition, BM25/dense retrieve, etc.) to approximate optimal module combination per dataset; reports optimization results. |
| **write / read / forget** | Write: silent online memory — config search offline. Read: optimized retrieve/generate pipeline at inference. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Treat S7 pack pipeline as searchable module graph, not one fixed RAG. (2) Dataset-specific optima → per-corpus hydrate profiles. (3) Include query decomposition for multi-hop like AutoRAG modules. (4) Optimization objective must match Kedger SLI (faithfulness not only EM). |
| **metric_impact** | RAG quality on target datasets after AutoRAG module search vs defaults. |
| **refine_candidate** | **yes — S7 AutoRAG-style hydrate pipeline search** |

---

### 18. OASIS: Open Agent Social Interaction Simulations with One Million Agents
**arXiv:2411.11581** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7 |
| **problem** | Social sim agents don't scale to million-user social network dynamics with realistic profiles/interactions. |
| **representation** | OASIS: large-scale LLM agent social simulation platform targeting up to one million agents; profile/follow/post dynamics inspired by social networks; population distributions (age/MBTI etc.). |
| **write / read / forget** | Write: agents post/follow updating social graph state. Read: retrieve profiles/posts for interaction. Forget: large-scale retention policies implied by scale, not detailed as SaF. |
| **conflict** | Social conflict/propagation studied at scale; not doc SUPERSEDES. |
| **privacy** | Uses disclosed social-network population statistics; large-scale behavioral data sensitivity. |
| **Kedger lessons** | (1) S5 social graph at scale needs sharding/partition — million-agent lesson. (2) Profile priors (MBTI/age) = agent persona Anchors. (3) Propagation experiments → information diffusion SLIs. (4) Not for personal memory correctness — scale/infra pattern. |
| **metric_impact** | Scalability to ~1M agents; social interaction/propagation fidelity metrics as reported. |
| **refine_candidate** | **no (scale sim infra)** |

---

### 19. Video-RAG: Visually-aligned Retrieval-Augmented Long Video Comprehension
**arXiv:2411.13093** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | LVLMs fail on long videos due to limited context; finetuning long-context LVLMs is costly. |
| **representation** | Video-RAG training-free pipeline: Query Decouple → retrieve auxiliary texts from video (OCR via EasyOCR, ASR, etc.) with Contriever+FAISS → feed visually-aligned text to any LVLM. Single-turn retrieve, plug-and-play. |
| **write / read / forget** | Write: index OCR/ASR/auxiliary text embeddings (FAISS). Read: query-decoupled retrieve into LVLM context. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | OCR may capture sensitive on-screen text — treat as untrusted Evidence. |
| **Kedger lessons** | (1) Long multimodal hydrate: retrieve auxiliary text modalities, don't only sample frames. (2) Query decouple before retrieve like PlanRAG for video. (3) Gains on Video-MME/MLVU/LongVideoBench vs base LVLMs; competitive with Gemini-class proprietary in paper claims. (4) OCR/ASR Evidence is instruction-injection surface — sanitize. |
| **metric_impact** | Long video QA accuracy on Video-MME, MLVU, LongVideoBench; ablations of OCR/ASR/retrieve. |
| **refine_candidate** | **yes — S7 visually-aligned auxiliary-text video RAG** |

---

### 20. On the Structural Memory of LLM Agents
**arXiv:2412.15266** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Unclear which memory structures and retrieval methods best serve LLM agents for factual QA over documents. |
| **representation** | Systematic study: structural memory generation as chunks / knowledge triples / atomic facts / summaries / mixtures; compare retrieval methods and answer generation; noise-document robustness; hyperparameter sensitivity. |
| **write / read / forget** | Write: LLM transforms raw docs into chosen structural memories. Read: retrieve structured memories then answer. Forget: silent. |
| **conflict** | Silent typed; noise documents stress robustness. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Choose structure per task: triples/atomic facts for multi-hop; chunks for lexical; summaries for gist — don't one-size. (2) Mixed memory can help but budget Evidence slots. (3) Report numbers from tables (e.g., structure F1 variants ~28–82% range in extracts) before picking defaults. (4) Rerank + iterative query refine are first-class S7 options in their stack. |
| **metric_impact** | QA F1/EM across memory structures × retrievers × answer generators; noise robustness. |
| **refine_candidate** | **yes — S3/S7 structural memory A/B for agent hydrate** |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (honest deep-recard) | 20 |
| Cumulative FULL | **460** |
