# Kedger Research Corpus Inventory

> **Date:** 2026-08-08 (Track 0 reboot)  
> **Product:** Kedger  
> **Purpose:** Honest tracking of what was **deep-read** vs **survey-indexed** vs **not yet read**.  
> **User constraint:** Do not keyword-skim the literature — gather mechanism-level insights.  
> **Program:** Research → Measure → Refine (see `KEDGER_STAGE_RESEARCH_MATRIX.md`, `EVAL_HARNESS.md`, `RESEARCH_CADENCE.md`).

---

## 0. Coverage honesty (read this first)

> **2026-08-09 honesty correction:** Batches 16–25 initially used abstract-template cards (`generate_to_500.py`). Replaced with **body deep-read mechanism cards** on `Cursor/honest-500-full-fb37` (agent deep-read + `assemble_deep_cards.py`). FULL now means mechanism fields grounded in Intro/Method/Results, not abstract paste.

We **cannot** truthfully claim end-to-end reading of 500+ full papers in one agent session. Claiming that would be keyword theater.

What we *can* and *did* do:

1. **Deep-read** the load-bearing primary sources for each design lock (full HTML/PDF bodies).
2. **Deep-read multiple 2024–2026 surveys** that curate the wider corpus, then extract taxonomies + citation maps.
3. Keep an inventory so future passes expand **FULL** coverage deliberately instead of pretending it already exists.
4. Maintain a **≥500 prioritized FULL runway** in [`queue/FULL_QUEUE_500.md`](queue/FULL_QUEUE_500.md) (`seed_placeholder` ≠ FULL).

| Bucket | Approx count | Meaning |
|--------|--------------|---------|
| **FULL deep-read** | **~484 + Batch26 (~24 new/re-read load-bearing)** | Through Batch25 (**500** ledger FULL); Batch26 = performance/cost set |
| **FULL runway queue** | **500** slots | `queue/full_queue.jsonl` — FULL + queued + seed_placeholder |
| **Perf scrape (2026-08-09)** | **1674** unique arXiv IDs | `queue/perf_corpus_seed.jsonl` — metadata index, not FULL |
| **Perf priority runway** | **300** | `queue/perf_priority_300.jsonl` |
| **On-disk fulltext cache** | `/tmp/kedger-papers/full/` | Kedger fetch path (`scripts/research/fetch_paper.py`); legacy `/tmp/modex-papers/full/` may also exist |
| **Survey-indexed** | 150–300+ via survey bibliographies | Named + one-line role from surveys; not independently full-read |
| **Stub / TODO** | remainder of agent-memory + crypto/auth literature | Queued for later FULL passes |

### 0.1 Kedger stage columns (for every FULL card / queue row)

| Column | Values |
|--------|--------|
| `kedger_stage` | `S1` hooks/capture · `S2` WorkingState · `S3` cognify · `S4` promote · `S5` graph/compose · `S6` seal/share · `S7` hydrate · `S8` why |
| `metric_impact` | Which SLI/fixture the paper informs (see `EVAL_HARNESS.md`) |
| `refine_candidate` | `yes` / `no` — only `yes` if a measurable gap vs current Kedger code exists |

Batch/pillar memos must fill these on new cards. Queue builder guesses stages for runway rows.

---

## 1. Where detailed insights live

| Memo / lock doc | Cluster |
|-----------------|---------|
| `AGENT_MEMORY_CORPUS_DEEP_READ.md` | Graphiti/Zep, HippoRAG×2, A-MEM, Nemori, Mem0, MemGPT, GenAgents, RecMem, ES-Mem, EM-LLM, StateFuse, TOKI, LightRAG, GraphRAG, SSGM, surveys |
| `AGENT_MEMORY_CORPUS_DEEP_READ_BATCH2.md` | MemoryOS, LightMem, MAGMA, Memory-R1, ConfAIde, Fides, LoCoMo, MemoryAgentBench, AriGraph, Reflexion, Voyager |
| `AGENT_MEMORY_CORPUS_DEEP_READ_BATCH3.md` | **15 new FULL + 3 re-read extras:** LTM Self-Evolution, LLM-Agents §memory, Memento, MemoryBench, ReasoningBank, MEM1, LEGOMem, MemAct, O-Mem, Agent KB, H-Mem, MemoChat, DialSim, Memory-as-a-Tool, Sleep-SCM (+ MemoryBank/SCM/TiM extras) |
| `IMPLEMENTATION_FROM_LITERATURE.md` | Cross-pillar Phase A–E algorithms/constants |
| `impl/P1_CAPTURE_WORKING.md` | **P1 impl (32 FULL cards):** hooks→L0→L1, MemGPT pressure, KV eviction (StreamingLLM/H₂O/SnapKV/Landmark/RMT/…), Claude/Cursor hooks+compaction, SQL capture recipe |
| `impl/P2_EPISODE_COGNIFY.md` | **P2 impl (39 FULL cards):** EST/boundaries, cognify, STM→MTM→LTM, Heat, surprise, recurrence, chapterization, Voyager/Larimar/eval suites, SQL, fixtures |
| `impl/P3_ANCHORS_GRAPH.md` | **P3 impl:** bi-temporal graph, entity resolve, PPR constants, promotion, edge schema + invalidation recipe |
| `impl/P4_CONFLICT_COMPOSE.md` | **P4 impl:** SUPERSEDES algorithm, ConflictSet, compose projection, audit schema |
| `impl/P5_HYDRATE_RETRIEVE.md` / `P6_PRIVACY_SEAL.md` | Hydrate scoring + Inv-Scope/seal recipes |
| `impl/BATCH_SYSTEMS_AND_EVAL.md` | 26 systems/eval mechanism cards |
| `batches/BATCH4_EVAL_SYSTEMS_FULL.md` | Batch4 eval/systems/privacy (5 FULL + 11 RE-READ) |
| `batches/BATCH5_EVAL_FAILURE_FULL.md` | **Batch5:** 18 new FULL tier-1 eval/failure (AgentBench, GAIA, WebArena, CRAG, MultiHop-RAG, …) |
| `batches/BATCH6_CAPTURE_GRAPH_FULL.md` | **Batch6:** 16 new FULL capture/compaction · episode boundaries · graph/conflict (GraphReader, MAMA, LLMLingua×3, RECOMP, KV cluster, SeCom, ToG, …) |
| `batches/BATCH7_PRIVACY_SEAL_FULL.md` | **Batch7:** 16 new FULL privacy/capability/share-leakage/seal (MEXTRA, AgentPoison, MINJA, PoisonedRAG, AgentDojo, AirGapAgent, Progent, PrivacyLens, …) |
| `batches/BATCH8_COMPRESS_RETRIEVE_FULL.md` | **Batch8:** 16 new FULL compress/retrieve/active-RAG/injection (FLARE, ConflictRAG, IRCoT, Gist, CoN, CCM, MemoRAG, xRAG, ReadAgent, KATE, RAG-Fusion, …) + ADR/QOC eng-judgment |
| `batches/BATCH9_EVAL_PRIVACY_FULL.md` | **Batch9:** 17 new FULL eval/privacy/active-retrieve/injection-memory (AMA-Bench, EvoMemBench, AgentMemBench, MRMMIA, stored PI, LPCI, Astute RAG, …) + 5 RE-READ |
| `batches/BATCH10_CAPTURE_EPISODE_FULL.md` | **Batch10:** 17 new FULL capture/episode/boundary/compaction (Membox, RMM, ReSum, BEAM/LIGHT, Context-Folding, HiAgent, MemWalker, …) |
| `batches/BATCH11_GRAPH_CONFLICT_FULL.md` | **Batch11:** 17 new FULL graph/compose/multi-agent/entity-resolve (Cognee, MemMachine, AgentGit, MRAgent, SYNAPSE, MIRIX, StructGPT, AgentVerse, …) |
| `batches/BATCH12_HYDRATE_SEAL_FULL.md` | **Batch12:** 17 new FULL hydrate/retrieve/seal/routing (ConfAIde, Fides, RealMem, MemBench, MRMMIA, RankRAG, HyDE, ppRAG, PIR-RAG, PRAG, …) |
| `batches/BATCH13_PROMOTE_WHY_FULL.md` | **Batch13:** 17 new FULL promote/eng-judgment/abstention/provenance (FEVER, VitaminC, G-Eval, Prometheus 2, R-Tuning, RAGAS, FLAME, ReMe, ERL, REVERSE, …) |
| `batches/BATCH14_MIXED_RUNWAY_FULL.md` | **Batch14:** 17 new FULL agent-memory/runway (ChatDB, AgentGym, kNN-LM, ColBERT, Atlas, REALM, MemoryLLM, M+, MemGen, InfLLM, procedural-memory cluster, …) |
| `batches/BATCH15_EVAL_RUNWAY_FULL.md` | **Batch15:** 8 new FULL eval/runway (AppWorld, MuSiQue, RealTime QA, SituatedQA, MSC, FiD, SWE-bench, τ-bench) — **300 FULL milestone** |
| `batches/BATCH16_SURVEY_RUNWAY_FULL.md` | **Batch16:** 20 new FULL survey-runway deep-reads |
| `batches/BATCH17_SURVEY_RUNWAY_FULL.md` | **Batch17:** 20 new FULL survey-runway deep-reads |
| `batches/BATCH18_SURVEY_RUNWAY_FULL.md` | **Batch18:** 20 new FULL survey-runway deep-reads |
| `batches/BATCH19_SURVEY_RUNWAY_FULL.md` | **Batch19:** 20 new FULL survey-runway deep-reads |
| `batches/BATCH20_SURVEY_RUNWAY_FULL.md` | **Batch20:** 20 new FULL survey-runway deep-reads |
| `batches/BATCH21_SURVEY_RUNWAY_FULL.md` | **Batch21:** 20 new FULL survey-runway deep-reads |
| `batches/BATCH22_SURVEY_RUNWAY_FULL.md` | **Batch22:** 20 new FULL survey-runway deep-reads |
| `batches/BATCH23_SURVEY_RUNWAY_FULL.md` | **Batch23:** 20 new FULL survey-runway deep-reads |
| `batches/BATCH24_SURVEY_RUNWAY_FULL.md` | **Batch24:** 20 new FULL survey-runway deep-reads |
| `batches/BATCH25_SURVEY_RUNWAY_FULL.md` | **Batch25:** 20 new FULL survey-runway deep-reads |
| `batches/BATCH26_COST_CONSOLIDATE_FULL.md` | **Batch26:** LightMem / LeanMem / All-Mem / Memory OS — online-offline cost |
| `batches/BATCH26_RETRIEVE_KV_PERF_FULL.md` | **Batch26:** HippoRAG seed-IDF, StreamingLLM/H2O/SnapKV, agent KV delay-k lessons |
| `PERFORMANCE_PROGRESS_ROADMAP.md` | Perf P0/P1 maintain/reject + measure plan |
| `memory-perf-roadmap.md` | Pointer / live planning surface alias |
| `SHAREABLE_ANCHOR_POLICY_RESEARCH.md` | MemClaw, AgentLeak, MAMA, MemLeak, PRISM, Collaborative Memory, VAULT, Miller/Spritely, ADR/QOC |
| `SEALED_PACK_CRYPTO_RESEARCH.md` | age, libsodium, Wormhole, MLS, Biscuits, Macaroons, StE guidance |
| `PARALLEL_COMPOSE_AND_HOOKS_V1.md` §0 | StateFuse, TOKI, MemClaw, CRDT guides, Claude/Cursor hooks |
| `WORKSTREAM_AND_PROMOTION_V1.md` | EST/ES-Mem, RecMem, importance/reflection |
| `SEALED_PACKS_AND_SHAREABLE_ANCHORS_V1.md` | Design lock synthesized from above |

---

## 2. FULL deep-read ledger (primary)

### Agent memory / graphs / compose

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2501.13956 | Zep / Graphiti | 2025 | AGENT_MEMORY + **P2/P3/P4** |
| 2405.14831 | HippoRAG | 2024 | AGENT_MEMORY + **P3** |
| 2502.14802 | HippoRAG 2 | 2025 | AGENT_MEMORY + **P3** |
| 2502.12110 | A-MEM | 2025 | AGENT_MEMORY + **P2/P3/P4** |
| 2508.03341 | Nemori / What Deserves Memory | 2025–26 | AGENT_MEMORY + **P2/P3** |
| 2504.19413 | Mem0 / Mem0g | 2025 | AGENT_MEMORY + **P2/P3/P4** |
| 2310.08560 | MemGPT | 2023 | AGENT_MEMORY + **P2/P3/P4** |
| 2304.03442 | Generative Agents | 2023 | AGENT_MEMORY + **P2/P3/P4** |
| 2605.16045 | RecMem | 2026 | AGENT_MEMORY + **P2/P3** |
| 2601.07582 | ES-Mem | 2026 | AGENT_MEMORY + **P2/P3** |
| 2407.09450 | EM-LLM | 2024 | AGENT_MEMORY + **P2/P3** |
| 2607.05844 | StateFuse | 2026 | AGENT_MEMORY + PARALLEL + **P4** |
| 2606.06240 | TOKI | 2026 | AGENT_MEMORY + PARALLEL + **P4** |
| 2410.05779 | LightRAG | 2024 | AGENT_MEMORY + **P3** |
| 2404.16130 | GraphRAG | 2024 | AGENT_MEMORY + **P3** |
| 2603.11768 | SSGM | 2026 | AGENT_MEMORY + **P3/P4** |
| 2407.04363 | AriGraph | 2024 | **P2/P3/P4** |
| 2503.21322 | HyperGraphRAG | 2025 | **P3/P4** |
| 2601.03236 | MAGMA | 2026 | **P2/P3/P4** |
| 2506.07398 | G-Memory | 2025 | **P3/P4** |
| 2402.11163 | KG-Agent | 2024 | **P3** |
| 2408.00103 | ReLiK (EL + RE) | 2024 | **P3** |
| 2603.15994 | Selective Memory / supersession chains | 2026 | PARALLEL + **P3/P4** |
| 2506.06326 | MemoryOS | 2025 | **P2/P3/P4** |
| 2508.19828 | Memory-R1 | 2025 | **P2/P3/P4** |
| 2512.22716 | Memento 2 | 2025–26 | **BATCH4** FULL · S3/S8 |
| 2605.12493 | LongMemEval-V2 | 2026 | **BATCH4** FULL · S3/S7/S8 |
| 2602.16313 | MemoryArena | 2026 | **BATCH4** FULL · S1/S7 |
| 2511.06449 | FLEX | 2025 | **BATCH4** FULL · S3/S5 |
| 2502.09597 | PrefEval | 2025 | **BATCH4** FULL · S2/S4 |
| 2503.18813 | CaMeL | 2025 | **P6** FULL + **BATCH4** RE-READ · S1/S6 |
| 2510.10397 | AssoMem | 2025 | **P3/P4** |
| 2510.18866 | LightMem | 2025 | **P2/P3/P4** |
| 2505.19549 | Multi-granularity conversational memory (MemGAS) | 2025 | **P2/P3** |
| 2509.25911 | Mem-α | 2025 | **P2/P3/P4** |
| 2507.03724 | MemOS | 2025 | **P1/P2** |
| 2305.10250 | MemoryBank (Zhong forgetting curve) | 2023–24 | **P1/P2** + **BATCH3** |
| 2304.13343 | SCM (Self-Controlled Memory) | 2023 | **P1/P2** + **BATCH3** |
| 2504.16754 | HEMA | 2025 | **P2** |
| 2506.08098 | Cognitive Weave | 2025 | **P2** |
| 2109.10862 | Recursive Summarizing Books | 2021 | **P2** |
| 2311.08719 | Think-in-Memory (TiM) | 2023 | **P2** + **BATCH3** |
| 2309.17453 | StreamingLLM | 2023 | **P1/P2** |
| 2306.14048 | H₂O Heavy-Hitter Oracle | 2023 | **P1** |
| 2404.14469 | SnapKV | 2024 | **P1** |
| 2305.16300 | Landmark Attention | 2023 | **P1** |
| 1911.05507 | Compressive Transformer | 2019 | **P1** |
| 1901.02860 | Transformer-XL | 2019 | **P1** |
| 2203.08913 | Memorizing Transformers | 2022 | **P1** |
| 2207.06881 | Recurrent Memory Transformer | 2022 | **P1** |
| 2304.11062 | RMT to 1M tokens | 2023 | **P1** |
| 1410.3916 | Memory Networks | 2014/15 | **P1** |
| 2305.14788 | AutoCompressors | 2023 | **P1** |
| 2305.01625 | Unlimiformer | 2023 | **P1** |
| 2307.06945 | ICAE (In-context Autoencoder) | 2023 | **P1** |
| 2005.11401 | RAG (Lewis et al.) | 2020 | **P1** |
| 2302.04761 | Toolformer | 2023 | **P1** |
| 2210.03629 | ReAct | 2022/23 | **P1** |
| 2303.11366 | Reflexion | 2023 | **P1** |
| 2308.15022 | Recursive Summarization (dialogue memory) | 2023 | **P1/P2** |
| 2403.16971 | AIOS | 2024 | **P1** |
| 2305.14322 | RET-LLM | 2023 | **P1** |
| 2305.16291 | Voyager | 2023 | **P2** |
| 2403.11901 | Larimar | 2024 | **P2** |
| 2507.02259 | MemAgent | 2025 | **P2** |
| 2402.17753 | LoCoMo | 2024 | **P2** / eval |
| 2112.04426 | RETRO | 2022 | **P2** |
| 2507.05257 | MemoryAgentBench | 2025 | **P2** / eval |
| — | Claude Code Hooks + Compaction + Context editing docs | 2025–26 | **P1** FULL |
| — | Cursor Hooks docs | 2025–26 | **P1** FULL |
| 2307.03172 | Lost in the Middle | 2023 | **P2/P5** |
| 2305.02747 | Unsupervised Dialogue Topic Seg (DialSTART) | 2023 | **P2** |
| 2308.10464 | HyperSeg (HDC topic seg) | 2023 | **P2** |
| 2512.17083 | Granularity-Aware Dialogue Topic Seg | 2025 | **P2** |
| 2512.13564 | Memory in the Age of AI Agents (survey) | 2025 | AGENT_MEMORY + **P3/P4** |
| 2404.13501 | Zhang memory mechanisms survey | 2024 | AGENT_MEMORY + **P1** |
| 2411.00489 | AI Long-term Memory survey | 2024 | **P3/P4** |
| 2504.15965 | From Human Memory to AI Memory survey | 2025 | **P3** |
| 2603.07670 | Memory for Autonomous LLM Agents (survey) | 2026 | CORPUS + **P3/P4** |
| 2602.19320 | Anatomy of Agentic Memory (survey) | 2026 | CORPUS + **P4** |
| 2605.06716 | From Storage to Experience (survey) | 2026 | CORPUS + **P3** |
| 2602.05665 | Graph-based Agent Memory survey | 2026 | CORPUS + **P3/P4** |
| 2602.06052 | Agent Memory Second Half survey | 2026 | CORPUS (supporting) |
| 2501.06322 | Multi-Agent Collaboration Mechanisms survey | 2025 | **P4** |
| 2410.15665 | Long Term Memory: Foundation of AI Self-Evolution | 2024 | **BATCH3** |
| 2309.07864 | Rise and Potential of LLM Agents (survey; §memory) | 2023 | **BATCH3** |
| 2508.16153 | Memento (case-based M-MDP memory) | 2025 | **BATCH3** |
| 2510.17281 | MemoryBench (continual feedback) | 2025 | **BATCH3** |
| 2509.25140 | ReasoningBank + MaTTS | 2025 | **BATCH3** |
| 2506.15841 | MEM1 (constant-size IS memory) | 2025 | **BATCH3** |
| 2510.04851 | LEGOMem (modular procedural multi-agent) | 2025 | **BATCH3** |
| 2510.12635 | Memory as Action / MemAct | 2025 | **BATCH3** |
| 2511.13593 | O-Mem (omni persona/episodic/working) | 2025 | **BATCH3** |
| 2507.06229 | Agent KB (cross-framework experience) | 2025 | **BATCH3** |
| 2605.15701 | H-Mem (hybrid tree+graph) | 2026 | **BATCH3** |
| 2308.08239 | MemoChat | 2023 | **BATCH3** |
| 2406.13144 | DialSim / LongDialQA | 2024 | **BATCH3** |
| 2601.05960 | Memory-as-a-Tool | 2026 | **BATCH3** |
| 2604.20943 | Sleep-Consolidated Memory (preview) | 2026 | **BATCH3** |
| 2401.18059 | RAPTOR | 2024 | **P5** |
| 2504.18070 | PropRAG | 2025 | **P5** |
| 2403.14403 | Adaptive-RAG | 2024 | **P5** |
| 2410.10813 | LongMemEval | 2024 | **P2/P5** / BATCH2 eval |
| 2508.04903 | RCR-Router | 2025 | **P5** |

### Capture / compaction · episode · graph/conflict (Batch 6)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2406.14550 | GraphReader | 2024 | **BATCH6** FULL · S2/S3/S5/S7 |
| 2512.04668 | Topology Matters / MAMA | 2025–26 | **BATCH6** FULL · S4/S5/S6 (was SHAREABLE `ACL'26` slug) |
| 2310.05736 | LLMLingua | 2023 | **BATCH6** FULL · S1/S2/S3 |
| 2310.06839 | LongLLMLingua | 2023–24 | **BATCH6** FULL · S2/S3/S7 |
| 2403.12968 | LLMLingua-2 | 2024 | **BATCH6** FULL · S1/S2/S3 |
| 2310.04408 | RECOMP | 2023 | **BATCH6** FULL · S3/S5/S7 |
| 2305.17118 | Scissorhands (KV persistence-of-importance) | 2023 | **BATCH6** FULL · S1/S2 |
| 2406.02069 | PyramidKV | 2024 | **BATCH6** FULL · S1/S2 |
| 2406.10774 | Quest (query-aware KV pages) | 2024 | **BATCH6** FULL · S2/S7 |
| 2304.12102 | Selective Context | 2023 | **BATCH6** FULL · S2/S3 |
| 2401.03462 | Activation Beacon | 2024 | **BATCH6** FULL · S1/S2 |
| 2305.08371 | SuperDialseg | 2023 | **BATCH6** FULL · S1/S3 |
| 2502.05589 | SeCom (segment memory + compress denoise) | 2025 | **BATCH6** FULL · S2/S3/S7 |
| 2308.10144 | ExpeL | 2023 | **BATCH6** FULL · S3/S4/S7 |
| 2307.07697 | Think-on-Graph (ToG) | 2023–24 | **BATCH6** FULL · S5/S7/S8 |
| 2310.00935 | Resolving Knowledge Conflicts in LLMs | 2023 | **BATCH6** FULL · S4/S5/S7/S8 |

### Eval / failure-mode (Batch 5)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2308.03688 | AgentBench | 2023 | **BATCH5** FULL · S1/S7 |
| 2311.12983 | GAIA | 2023 | **BATCH5** FULL · S1/S7 |
| 2307.13854 | WebArena | 2023 | **BATCH5** FULL · S1/S7 |
| 2406.04744 | CRAG (Comprehensive RAG Benchmark) | 2024 | **BATCH5** FULL · S7 |
| 2401.15884 | Corrective Retrieval Augmented Generation | 2024 | **BATCH5** FULL · S7 |
| 2401.15391 | MultiHop-RAG | 2024 | **BATCH5** FULL · S5/S7 |
| 2305.13300 | Adaptive Chameleon (knowledge conflicts) | 2023 | **BATCH5** FULL · S4/S7 |
| 2310.03214 | FreshLLMs / FreshQA | 2023 | **BATCH5** FULL · S4/S7 |
| 2308.14508 | LongBench | 2023 | **BATCH5** FULL · S2/S7 |
| 2412.15204 | LongBench v2 | 2024 | **BATCH5** FULL · S2/S7 |
| 2404.06654 | RULER | 2024 | **BATCH5** FULL · S2/S7 |
| 2402.13718 | ∞Bench (InfiniteBench) | 2024 | **BATCH5** FULL · S2/S7 |
| 2310.11511 | Self-RAG | 2023 | **BATCH5** FULL · S3/S7/S8 |
| 2309.01431 | RGB (RAG Benchmark) | 2023 | **BATCH5** FULL · S7 |
| 2402.16288 | PerLTQA | 2024 | **BATCH5** FULL · S3/S7 |
| 2407.11963 | NeedleBench | 2024 | **BATCH5** FULL · S2/S7 |
| 1809.09600 | HotpotQA | 2018 | **BATCH5** FULL · S5/S7/S8 |
| 2011.01060 | 2WikiMultiHopQA | 2020 | **BATCH5** FULL · S5/S7/S8 |

### Multi-agent frameworks (memory/sharing implications)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2308.00352 | MetaGPT | 2023 | **P4** |
| 2307.07924 | ChatDev | 2023 | **P4** |
| 2303.17760 | CAMEL | 2023 | **P4** |
| 2308.08155 | AutoGen | 2023 | **P4** |

### Privacy / share / governance

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2606.24535 | MemClaw / Governed Shared Memory | 2026 | SHAREABLE + **P3/P4** |
| 2602.11510 | AgentLeak | 2026 | SHAREABLE + **P4** |
| 2512.04668 | Topology Matters / MAMA | 2025–26 | SHAREABLE + **BATCH6** FULL · S4/S5/S6 |
| 2606.29788 | MemLeak | 2026 | SHAREABLE + **P4** |
| 2605.10614 | PRISM | 2026 | SHAREABLE |
| 2505.18279 | Collaborative Memory | 2025 | SHAREABLE + **P3/P4** |
| — | VAULT (eKNOW 2025) | 2025 | SHAREABLE |
| — | Capability Myths Demolished | 2003 | SHAREABLE |
| — | Spritely / OcapPub | 2023+ | SHAREABLE |
| RFC 2693 | SPKI Certificate Theory | 1999 | SHAREABLE |

### Privacy / capability / leakage / seal (Batch 7)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2502.13172 | MEXTRA / Unveiling Privacy Risks in LLM Agent Memory | 2025 | **BATCH7** FULL · S2/S6/S7/S8 |
| 2407.12784 | AgentPoison (memory/RAG backdoor) | 2024 | **BATCH7** FULL · S3/S4/S7 |
| 2503.03704 | MINJA (query-only memory injection) | 2025 | **BATCH7** FULL · S1/S3/S4/S7 |
| 2402.17840 | Spill the Beans (RAG datastore extraction) | 2024 | **BATCH7** FULL · S6/S7 |
| 2402.07867 | PoisonedRAG | 2024 | **BATCH7** FULL · S3/S4/S5/S7 |
| 2403.02691 | InjecAgent | 2024 | **BATCH7** FULL · S1/S6/S7 |
| 2406.13352 | AgentDojo | 2024 | **BATCH7** FULL · S1/S6/S7 |
| 2405.05175 | AirGapAgent | 2024 | **BATCH7** FULL · S2/S4/S6/S7 |
| 2504.11703 | Progent (privilege control) | 2025–26 | **BATCH7** FULL · S1/S6 |
| 2409.00138 | PrivacyLens | 2024 | **BATCH7** FULL · S4/S6/S8 |
| 2312.14197 | BIPIA (indirect prompt injection benchmark) | 2023–25 | **BATCH7** FULL · S1/S6/S7 |
| 2405.20446 | RAG membership inference | 2024 | **BATCH7** FULL · S6/S7 |
| 2305.03010 | GEIA (generative embedding inversion) | 2023 | **BATCH7** FULL · S3/S6 |
| 2411.01705 | RAG backdoor data extraction | 2024 | **BATCH7** FULL · S3/S6/S7 |
| 2510.05244 | IPI Firewalls (Minimizer + Sanitizer) | 2025 | **BATCH7** FULL · S1/S6/S7 |
| 2607.21325 | CVA (cryptographically verifiable agent authorization) | 2026 | **BATCH7** FULL · S6 |

### Compress / retrieve / active RAG / injection (Batch 8)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2305.06983 | FLARE / Active Retrieval Augmented Generation | 2023 | **BATCH8** FULL · S7/S8 |
| 2605.17301 | ConflictRAG — conflict-aware RAG | 2026 | **BATCH8** FULL · S4/S5/S7/S8 |
| 2212.10509 | IRCoT — interleaved retrieval + CoT | 2022 | **BATCH8** FULL · S5/S7/S8 |
| 2304.08467 | Gist Tokens — prompt compression | 2023 | **BATCH8** FULL · S2/S7 |
| 2310.06816 | Text Embeddings Reveal (Almost) As Much As Text | 2023 | **BATCH8** FULL · S3/S6/S7 |
| 2311.09210 | Chain-of-Note (CoN) — robust RALM | 2024 | **BATCH8** FULL · S7/S8 |
| 2306.05499 | Prompt Injection vs LLM-integrated Applications (HouYi) | 2023 | **BATCH8** FULL · S1/S6/S7 |
| 2312.03414 | Compressed Context Memory (CCM) — online KV compress | 2023 | **BATCH8** FULL · S2/S7 |
| 2409.05591 | MemoRAG — global memory-enhanced retrieval | 2024 | **BATCH8** FULL · S2/S5/S7 |
| 2405.13792 | xRAG — one-token retrieval modality fusion | 2024 | **BATCH8** FULL · S7 |
| 2402.09727 | ReadAgent — gist memory for long contexts | 2024 | **BATCH8** FULL · S2/S3/S7 |
| 2406.03007 | BadAgent — backdoor attacks on LLM agents | 2024 | **BATCH8** FULL · S1/S3/S6 |
| 2606.10525 | Assessing Automated Prompt Injection in Agentic Environments | 2026 | **BATCH8** FULL · S1/S6/S7 |
| 2101.06804 | KATE — kNN in-context example selection | 2021 | **BATCH8** FULL · S7 |
| 2402.03367 | RAG-Fusion — multi-query RRF | 2024 | **BATCH8** FULL · S7 |
| — | ADR / QOC / IBIS design-rationale practice | eng | **BATCH8** FULL · S4/S6/S8 |

### Eval / privacy / active retrieve / injection memory (Batch 9)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2602.22769 | AMA-Bench — long-horizon agentic memory eval | 2026 | **BATCH9** FULL · S1/S7/S8 |
| 2605.18421 | EvoMemBench — self-evolving memory eval | 2026 | **BATCH9** FULL · S2/S3/S4/S8 |
| 2608.00009 | AgentMemBench — strategy-agnostic dialogue memory eval | 2026 | **BATCH9** FULL · S2/S7/S8 |
| 2309.04697 | Leakage-Abuse Attacks on SSE | 2017 | **BATCH9** FULL · S6/S7 |
| 2510.06719 | DP Synthetic Text for RAG | 2025 | **BATCH9** FULL · S6/S7 |
| 2605.27825 | MRMMIA — membership inference on chat-agent memory | 2026 | **BATCH9** FULL · S6/S7/S8 |
| 2508.09736 | M3-Agent — multimodal long-term memory | 2025 | **BATCH9** FULL · S1/S2/S3/S7 |
| 2507.07957 | MIRIX — multi-agent memory system | 2025 | **BATCH9** FULL · S2/S3/S4/S5/S7 |
| 2606.04425 | Cross-Session Stored Prompt Injection | 2026 | **BATCH9** FULL · S1/S3/S4/S6/S8 |
| 2507.10457 | LPCI — logic-layer prompt control injection | 2025 | **BATCH9** FULL · S1/S3/S6/S7 |
| 2301.12652 | REPLUG — retrieval-augmented black-box LMs | 2023 | **BATCH9** FULL · S7/S8 |
| 2212.14024 | DSP — Demonstrate-Search-Predict | 2022 | **BATCH9** FULL · S5/S7/S8 |
| 2410.07176 | Astute RAG — imperfect retrieval + conflicts | 2024 | **BATCH9** FULL · S4/S5/S7/S8 |
| 2502.00306 | Stealthy MIA for RAG (Riddle Me This) | 2025 | **BATCH9** FULL · S6/S7 |
| 2406.05804 | Review of LLM-Agent Paradigms (tool/RAG/planning) | 2024 | **BATCH9** FULL · S1/S7/S8 |
| 2403.11381 | Melting Pot — LLM-augmented agent cooperation eval | 2024 | **BATCH9** FULL · S4/S5/S6/S8 |
| 2403.04957 | Automatic Universal Prompt Injection Attacks | 2024 | **BATCH9** FULL · S1/S6/S7 |

### Capture / episode / boundary / compaction (Batch 10)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2601.03785 | Membox — topic continuity memory boxes | 2026 | **BATCH10** FULL · S2/S3/S4/S7 |
| 2503.08026 | RMM — Reflective Memory Management | 2025 | **BATCH10** FULL · S2/S3/S7/S8 |
| 2509.13313 | ReSum — context summarization for search agents | 2025 | **BATCH10** FULL · S1/S2/S7 |
| 2603.02228 | Neural Paging — learned context management | 2026 | **BATCH10** FULL · S1/S2 |
| 2510.27246 | BEAM benchmark + LIGHT memory framework | 2025 | **BATCH10** FULL · S2/S3/S7/S8 |
| 2604.21748 | StructMem — structured hierarchical memory | 2026 | **BATCH10** FULL · S2/S3/S5/S7 |
| 2605.28773 | FluxMem — connectivity-evolving memory graph | 2026 | **BATCH10** FULL · S3/S4/S5/S7 |
| 2503.21760 | MemInsight — autonomous memory augmentation | 2025 | **BATCH10** FULL · S3/S4/S7 |
| 2604.22085 | Memanto — typed semantic memory + info-theoretic retrieval | 2026 | **BATCH10** FULL · S3/S5/S7/S8 |
| 2508.06433 | Memp — agent procedural memory | 2025 | **BATCH10** FULL · S3/S4/S7 |
| 2501.00309 | GraphRAG with Graphs | 2025 | **BATCH10** FULL · S3/S5/S7 |
| 2408.09559 | HiAgent — hierarchical working memory management | 2024 | **BATCH10** FULL · S1/S2/S7 |
| 2504.13171 | Sleep-time Compute | 2025 | **BATCH10** FULL · S3/S4/S8 |
| 2510.11967 | Context-Folding — branch/return context management | 2025 | **BATCH10** FULL · S1/S2/S7/S8 |
| 2505.02099 | MemEngine — modular memory library | 2025 | **BATCH10** FULL · S2/S3/S7 |
| 2510.24699 | AgentFold — proactive context management | 2025 | **BATCH10** FULL · S1/S2/S7 |
| 2310.05029 | MemWalker — interactive reading memory tree | 2023 | **BATCH10** FULL · S2/S5/S7/S8 |

### Graph / conflict / compose / multi-agent (Batch 11)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2505.24478 | Cognee / KG–LLM interface optimization | 2025 | **BATCH11** FULL · S3/S5/S7 |
| 2604.04853 | MemMachine — ground-truth-preserving agent memory | 2026 | **BATCH11** FULL · S2/S3/S5/S7 |
| 2511.00628 | AgentGit — Git-like MAS checkpoints/branching | 2025 | **BATCH11** FULL · S4/S5/S8 |
| 2606.06036 | MRAgent — active graph memory reconstruction | 2026 | **BATCH11** FULL · S5/S7/S8 |
| 2601.02744 | SYNAPSE — spreading activation episodic-semantic graph | 2026 | **BATCH11** FULL · S3/S5/S7 |
| 2305.09645 | StructGPT — IRR over structured data | 2023 | **BATCH11** FULL · S5/S7/S8 |
| 2308.10848 | AgentVerse — dynamic multi-agent collaboration | 2023 | **BATCH11** FULL · S4/S5/S8 |
| 2508.08997 | Intrinsic Memory Agents — heterogeneous MAS memory | 2025 | **BATCH11** FULL · S2/S4/S5 |
| 2510.26486 | LINK-KG — coreference-resolved KG construction | 2025 | **BATCH11** FULL · S3/S5 |
| 2409.03284 | iText2KG — incremental zero-shot KG construction | 2024 | **BATCH11** FULL · S3/S5 |
| 2403.06434 | BoostER — LLM-enhanced entity resolution | 2024 | **BATCH11** FULL · S3/S5 |
| 2401.03426 | LLM entity resolution (cost-efficient) | 2024 | **BATCH11** FULL · S3/S5 |
| 2410.12480 | KcMF — knowledge-compliant schema/entity matching | 2024 | **BATCH11** FULL · S3/S5 |

### Hydrate / retrieve / seal / routing (Batch 12)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2310.17884 | ConfAIde — contextual integrity for LLM secrecy | 2023 | **BATCH12** FULL · S4/S6/S7/S8 (BATCH9 RE-READ) |
| 2505.23643 | Fides — IFC for securing AI agents | 2025 | **BATCH12** FULL · S1/S6/S7 (BATCH9 RE-READ) |
| 2601.06966 | RealMem — project-oriented memory benchmark | 2026 | **BATCH12** FULL · S2/S3/S7/S8 (BATCH9 RE-READ) |
| 2506.21605 | MemBench — comprehensive memory eval | 2025 | **BATCH12** FULL · S2/S3/S7 (BATCH9 RE-READ) |
| 2511.03506 | HaluMem — hallucination in agent memory eval | 2025 | **BATCH12** FULL · S3/S7/S8 (BATCH9 RE-READ) |
| 2407.02485 | RankRAG — unified context ranking + generation | 2024 | **BATCH12** FULL · S7/S8 |
| 2505.23052 | RAGRouter — RAG-aware query routing | 2025 | **BATCH12** FULL · S7 |
| 2505.23841 | SkewRoute — training-free KG-RAG LLM routing | 2025 | **BATCH12** FULL · S5/S7 |
| 2601.12331 | ppRAG / CAPRISE — encrypted distance-preserving RAG | 2026 | **BATCH12** FULL · S6/S7 |
| 2509.21325 | PIR-RAG — private information retrieval for RAG | 2025 | **BATCH12** FULL · S6/S7 |
| 2604.26525 | PRAG — end-to-end privacy-preserving RAG | 2026 | **BATCH12** FULL · S6/S7 |
| 2212.10496 | HyDE — hypothetical document embeddings | 2022 | **BATCH12** FULL · S7 |
| 2312.10997 | RAG for LLMs — survey | 2023 | **BATCH12** FULL · S7/S8 |

### Promote / eng-judgment / abstention / provenance (Batch 13)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 1803.05355 | FEVER — fact extraction and verification | 2018 | **BATCH13** FULL · S4/S5/S8 |
| 2103.08541 | VitaminC — contrastive fact verification | 2021 | **BATCH13** FULL · S4/S5/S8 |
| 2303.16634 | G-Eval — GPT-4 NLG evaluation with CoT rubrics | 2023 | **BATCH13** FULL · S4/S8 |
| 2405.01535 | Prometheus 2 — open rubric-specialized judge LM | 2024 | **BATCH13** FULL · S4/S8 |
| 2311.09677 | R-Tuning — selective prediction / abstention | 2023 | **BATCH13** FULL · S4/S7/S8 |
| 2309.15217 | RAGAS — reference-free RAG evaluation | 2023 | **BATCH13** FULL · S7/S8 |
| 2405.01525 | FLAME — factuality-aware alignment | 2024 | **BATCH13** FULL · S4/S7/S8 |
| 2305.14552 | Sources of hallucination in LLMs on inference | 2023 | **BATCH13** FULL · S4/S7/S8 |
| 2512.10696 | ReMe — dynamic procedural memory | 2025 | **BATCH13** FULL · S3/S4/S8 |
| 2603.24639 | ERL — experiential reflective learning | 2026 | **BATCH13** FULL · S3/S4/S8 |
| 2210.03493 | Auto-CoT — automatic chain-of-thought prompting | 2022 | **BATCH13** FULL · S7/S8 |
| 2504.13169 | REVERSE — generate but verify | 2025 | **BATCH13** FULL · S4/S7/S8 |
| 2305.14264 | Active learning principles for in-context learning | 2023 | **BATCH13** FULL · S7/S8 |
| 2309.11054 | Design of chain-of-thought for math problem solving | 2023 | **BATCH13** FULL · S8 |
| 2308.02151 | Retroformer — retrospective LLM agents | 2023 | **BATCH13** FULL · S3/S7/S8 |
| 2510.08558 | Agent learning via early experience | 2025 | **BATCH13** FULL · S3/S4/S8 |
| 2502.07459 | PerCul — story-driven cultural evaluation | 2025 | **BATCH13** FULL · S4/S8 |

### Agent memory / retrieve runway (Batch 14)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2306.03901 | ChatDB — SQL databases as symbolic memory | 2023 | **BATCH14** FULL · S2/S3/S5/S7 |
| 2406.04151 | AgentGym — evolving LLM agents across environments | 2024 | **BATCH14** FULL · S1/S3/S8 |
| 1911.00172 | kNN-LM — nearest-neighbor language models | 2019 | **BATCH14** FULL · S2/S7 |
| 2004.12832 | ColBERT — late interaction dense retrieval | 2020 | **BATCH14** FULL · S7 |
| 2208.03299 | Atlas — retrieval augmented few-shot LM | 2022 | **BATCH14** FULL · S7 |
| 2002.08909 | REALM — retrieval-augmented LM pre-training | 2020 | **BATCH14** FULL · S7 |
| 2402.04624 | MemoryLLM — self-updatable LLM memory | 2024 | **BATCH14** FULL · S2/S3/S4 |
| 2502.00592 | M+ — scalable long-term MemoryLLM | 2025 | **BATCH14** FULL · S2/S3/S4 |
| 2509.24704 | MemGen — generative latent memory | 2025 | **BATCH14** FULL · S2/S3/S7 |
| 2402.04617 | InfLLM — training-free long-context memory | 2024 | **BATCH14** FULL · S2/S7 |
| 2606.29824 | Neural procedural memory for LLM agents | 2026 | **BATCH14** FULL · S3/S4/S7 |
| 2606.23127 | Managing procedural memory in LLM agents | 2026 | **BATCH14** FULL · S3/S4/S8 |
| 2608.03463 | LeanMem — efficient long-term agent memory | 2026 | **BATCH14** FULL · S2/S3/S7 |
| 2603.24018 | ELITE — experiential learning and intent-aware transfer | 2026 | **BATCH14** FULL · S3/S4/S8 |
| 2512.18950 | Hierarchical procedural memory (Bayesian) | 2025 | **BATCH14** FULL · S3/S4/S5 |
| 2605.30690 | ElasticMem — latent memory as learnable resource | 2026 | **BATCH14** FULL · S2/S3/S4 |
| 2509.08755 | AgentGym-RL — RL for long-horizon agents | 2025 | **BATCH14** FULL · S1/S3/S8 |

### Eval / multi-hop / temporal / dialogue runway (Batch 15 — 300 FULL milestone)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2407.18901 | AppWorld — interactive coding agents in app sandbox | 2024 | **BATCH15** FULL · S1/S2/S7/S8 |
| 2108.00573 | MuSiQue — multihop via single-hop composition | 2021 | **BATCH15** FULL · S5/S7/S8 |
| 2207.13332 | RealTime QA — dynamic weekly present-time QA | 2022 | **BATCH15** FULL · S4/S7/S8 |
| 2109.06157 | SituatedQA — temporal/geographic context QA | 2021 | **BATCH15** FULL · S4/S7/S8 |
| 2107.07567 | MSC / Beyond Goldfish Memory — multi-session chat | 2021 | **BATCH15** FULL · S2/S3/S7 |
| 2007.01282 | FiD — Fusion-in-Decoder RAG | 2020 | **BATCH15** FULL · S7 |
| 2310.06770 | SWE-bench — real GitHub issue resolution | 2023 | **BATCH15** FULL · S1/S2/S7/S8 |
| 2406.12045 | τ-bench — tool-agent-user interaction + pass^k | 2024 | **BATCH15** FULL · S1/S4/S7/S8 |

### Survey bibliography runway (Batches 16–25 — 500 FULL milestone)

| ID | Paper | Year | Memo |
|----|-------|------|------|
| 2508.12630 | Semantic Anchoring in Agentic Memory: Leveraging Linguistic Struc | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2508.19855 | Youtu-GraphRAG: Vertically Unified Agents for Graph Retrieval-Aug | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2509.10852 | Pre-Storage Reasoning for Episodic Memory: Shifting Inference Bur | 2025 | **BATCH16** FULL · S2/S3/S7 |
| 2511.06179 | MemoriesDB: A Temporal-Semantic-Relational Database for Long-Term | 2025 | **BATCH16** FULL · S3/S5/S7/S8 |
| 2506.13356 | StoryBench: A Dynamic Benchmark for Evaluating Long-Term Memory w | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2508.10391 | LeanRAG: Knowledge-Graph-Based Generation with Semantic Aggregati | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2510.06664 | ToolMem: Enhancing Multimodal Agents with Learnable Tool Capabili | 2025 | **BATCH16** FULL · S4/S6/S7 |
| 2511.01448 | LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficien | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2511.17467 | PersonaAgent with GraphRAG: Community-Aware Knowledge Graphs for  | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2601.01885 | Agentic Memory: Learning Unified Long-Term and Short-Term Memory  | 2026 | **BATCH16** FULL · S3/S5/S7/S8 |
| 2405.07960 | AgentClinic: a multimodal agent benchmark to evaluate AI in simul | 2024 | **BATCH16** FULL · S1/S7/S8 |
| 2406.00057 | Toward Conversational Agents with Context and Time Sensitive Long | 2024 | **BATCH16** FULL · S1/S7/S8 |
| 2409.19401 | Crafting Personalized Agents through Retrieval-Augmented Generati | 2024 | **BATCH16** FULL · S1/S7/S8 |
| 2501.09136 | Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2503.05193 | Memory-augmented Query Reconstruction for LLM-based Knowledge Gra | 2025 | **BATCH16** FULL · S3/S5/S7/S8 |
| 2505.11942 | LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2505.20096 | MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborat | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2506.03141 | Context as Memory: Scene-Consistent Interactive Long Video Genera | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2507.21428 | MemTool: Optimizing Short-Term Memory Management for Dynamic Tool | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2507.22925 | Hierarchical Memory for High-Efficiency Long-Term Reasoning in LL | 2025 | **BATCH16** FULL · S1/S7/S8 |
| 2508.10419 | ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful L | 2025 | **BATCH17** FULL · S1/S7/S8 |
| 2508.12379 | GraphCogent: Mitigating LLMs' Working Memory Constraints via Mult | 2025 | **BATCH17** FULL · S3/S5/S7/S8 |
| 2508.15294 | A Multi-Memory Segment System for Generating High-Quality Long-Te | 2025 | **BATCH17** FULL · S1/S7/S8 |
| 2509.21212 | SGMem: Sentence Graph Memory for Long-Term Conversational Agents | 2025 | **BATCH17** FULL · S1/S7/S8 |
| 2509.23040 | Look Back to Reason Forward: Revisitable Memory for Long-Context  | 2025 | **BATCH17** FULL · S2/S3/S7/S8 |
| 2510.01353 | MEMTRACK: Evaluating Long-Term Memory and State Tracking in Multi | 2025 | **BATCH17** FULL · S1/S7/S8 |
| 2510.13614 | MemoTime: Memory-Augmented Temporal Knowledge Graph Enhanced Larg | 2025 | **BATCH17** FULL · S1/S7/S8 |
| 2510.19897 | Learning from Supervision with Semantic and Episodic Memory: A Re | 2025 | **BATCH17** FULL · S2/S3/S7/S8 |
| 2510.21618 | DeepAgent: A General Reasoning Agent with Scalable Toolsets | 2025 | **BATCH17** FULL · S2/S3/S7/S8 |
| 2511.10030 | Multi-agent In-context Coordination via Decentralized Memory Retr | 2025 | **BATCH17** FULL · S1/S7/S8 |
| 2511.20857 | Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-E | 2025 | **BATCH17** FULL · S1/S7/S8 |
| 2512.12856 | Forgetful but Faithful: A Cognitive Memory Architecture and Bench | 2025 | **BATCH17** FULL · S1/S7/S8 |
| 2512.20092 | Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi | 2025 | **BATCH17** FULL · S2/S3/S7 |
| 2512.20237 | MemR$^3$: Memory Retrieval via Reflective Reasoning for LLM Agent | 2025 | **BATCH17** FULL · S1/S7/S8 |
| 2512.20745 | AgentMath: Empowering Mathematical Reasoning for Large Language M | 2025 | **BATCH17** FULL · S1/S7/S8 |
| 2601.04726 | Memory Matters More: Event-Centric Memory as a Logic Map for Agen | 2026 | **BATCH17** FULL · S1/S7/S8 |
| 2601.07468 | Beyond Dialogue Time: Temporal Semantic Memory for Personalized L | 2026 | **BATCH17** FULL · S1/S2/S7 |
| 2602.07624 | M2A: Multimodal Memory Agent with Dual-Layer Hybrid Memory for Lo | 2026 | **BATCH17** FULL · S2/S3/S7/S8 |
| 2302.04023 | A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Re | 2023 | **BATCH17** FULL · S1/S7/S8 |
| 2305.14938 | Do LLMs Understand Social Knowledge? Evaluating the Sociability o | 2023 | **BATCH17** FULL · S1/S7/S8 |
| 2305.17144 | Ghost in the Minecraft: Generally Capable Agents for Open-World E | 2023 | **BATCH18** FULL · S2/S3/S7/S8 |
| 2308.01542 | Memory Sandbox: Transparent and Interactive Memory Management for | 2023 | **BATCH18** FULL · S2/S3/S7/S8 |
| 2308.07201 | ChatEval: Towards Better LLM-based Evaluators through Multi-Agent | 2023 | **BATCH18** FULL · S1/S7/S8 |
| 2309.17452 | ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem  | 2023 | **BATCH18** FULL · S2/S3/S7/S8 |
| 2310.16340 | RCAgent: Cloud Root Cause Analysis by Autonomous Agents with Tool | 2023 | **BATCH18** FULL · S2/S3/S7/S8 |
| 2311.04177 | Enhancing LLM Intelligence with ARM-RAG: Auxiliary Rationale Memo | 2023 | **BATCH18** FULL · S1/S7/S8 |
| 2312.00326 | Agent-OM: Leveraging LLM Agents for Ontology Matching | 2023 | **BATCH18** FULL · S1/S7/S8 |
| 2312.03815 | LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS- | 2023 | **BATCH18** FULL · S2/S3/S7/S8 |
| 2401.07339 | CodeAgent: Enhancing Code Generation with Tool-Integrated Agent S | 2024 | **BATCH18** FULL · S1/S7/S8 |
| 2401.14215 | Commonsense-augmented Memory Construction and Management in Long- | 2024 | **BATCH18** FULL · S2/S3/S7 |
| 2403.01112 | Efficient Episodic Memory Utilization of Cooperative Multi-Agent  | 2024 | **BATCH18** FULL · S3/S5/S7/S8 |
| 2404.09992 | MMInA: Benchmarking Multihop Multimodal Internet Agents | 2024 | **BATCH18** FULL · S1/S7/S8 |
| 2406.05925 | Hello Again! LLM-powered Personalized Agent for Long-term Dialogu | 2024 | **BATCH18** FULL · S2/S3/S7 |
| 2406.06124 | Enhancing Long-Term Memory using Hierarchical Aggregate Tree for  | 2024 | **BATCH18** FULL · S1/S7/S8 |
| 2406.08747 | StreamBench: Towards Benchmarking Continuous Improvement of Langu | 2024 | **BATCH18** FULL · S1/S7/S8 |
| 2406.10996 | Towards Lifelong Dialogue Agents via Timeline-based Memory Manage | 2024 | **BATCH18** FULL · S1/S7/S8 |
| 2408.05861 | Temporal Knowledge-Graph Memory in a Partially Observable Environ | 2024 | **BATCH18** FULL · S1/S7/S8 |
| 2410.19627 | Knowledge Graph Enhanced Language Agents for Recommendation | 2024 | **BATCH18** FULL · S3/S5/S7/S8 |
| 2410.20682 | SHARE: Shared Memory-Aware Open-Domain Long-Term Dialogue Dataset | 2024 | **BATCH18** FULL · S2/S3/S7 |
| 2412.01857 | Planning from Imagination: Episodic Simulation and Episodic Memor | 2024 | **BATCH18** FULL · S2/S3/S7/S8 |
| 2502.05453 | LLM-Powered Decentralized Generative Agents with Adaptive Hierarc | 2025 | **BATCH19** FULL · S3/S5/S7/S8 |
| 2502.13843 | AgentCF++: Memory-enhanced LLM-based Agents for Popularity-aware  | 2025 | **BATCH19** FULL · S2/S3/S7/S8 |
| 2503.10049 | Enhancing Multi-Agent Systems via Reinforcement Learning with LLM | 2025 | **BATCH19** FULL · S3/S5/S7/S8 |
| 2505.20231 | MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi- | 2025 | **BATCH19** FULL · S1/S7/S8 |
| 2505.20286 | Alita: Generalist Agent Enabling Scalable Agentic Reasoning with  | 2025 | **BATCH19** FULL · S2/S3/S7/S8 |
| 2506.13651 | xbench: Tracking Agents Productivity Scaling with Profession-Alig | 2025 | **BATCH19** FULL · S1/S7/S8 |
| 2507.21105 | AgentMaster: A Multi-Agent Conversational Framework Using A2A and | 2025 | **BATCH19** FULL · S1/S7/S8 |
| 2508.01415 | RoboMemory: A Brain-inspired Multi-memory Agentic Framework for I | 2025 | **BATCH19** FULL · S1/S7/S8 |
| 2508.01832 | MLP Memory: A Retriever-Pretrained Memory for Large Language Mode | 2025 | **BATCH19** FULL · S2/S3/S7/S8 |
| 2508.13250 | Explicit v.s. Implicit Memory: Exploring Multi-hop Complex Reason | 2025 | **BATCH19** FULL · S2/S3/S7/S8 |
| 2509.01055 | VerlTool: Towards Holistic Agentic Reinforcement Learning with To | 2025 | **BATCH19** FULL · S2/S3/S7/S8 |
| 2509.17459 | PRINCIPLES: Synthetic Strategy Memory for Proactive Dialogue Agen | 2025 | **BATCH19** FULL · S2/S3/S7 |
| 2509.22315 | PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reas | 2025 | **BATCH19** FULL · S1/S7/S8 |
| 2509.25250 | Memory Management and Contextual Consistency for Long-Running Low | 2025 | **BATCH19** FULL · S1/S7/S8 |
| 2510.03611 | Can an LLM Induce a Graph? Investigating Memory Drift and Context | 2025 | **BATCH19** FULL · S3/S5/S7/S8 |
| 2510.04195 | Constructing coherent spatial memory in LLM agents through graph  | 2025 | **BATCH19** FULL · S1/S7/S8 |
| 2510.04618 | Agentic Context Engineering: Evolving Contexts for Self-Improving | 2025 | **BATCH19** FULL · S3/S5/S7/S8 |
| 2510.07134 | TrackVLA++: Unleashing Reasoning and Memory Capabilities in VLA M | 2025 | **BATCH19** FULL · S1/S7/S8 |
| 2510.07925 | Enabling Personalized Long-term Interactions in LLM-based Agents  | 2025 | **BATCH19** FULL · S2/S3/S7/S8 |
| 2510.09720 | Preference-Aware Memory Update for Long-Term LLM Agents | 2025 | **BATCH19** FULL · S1/S7/S8 |
| 2510.13363 | D-SMART: Enhancing LLM Dialogue Consistency via Dynamic Structure | 2025 | **BATCH20** FULL · S1/S2/S7 |
| 2510.23010 | TALM: Dynamic Tree-Structured Multi-Agent Framework with Long-Ter | 2025 | **BATCH20** FULL · S3/S5/S7/S8 |
| 2511.01633 | Scaling Graph Chain-of-Thought Reasoning: A Multi-Agent Framework | 2025 | **BATCH20** FULL · S3/S5/S7/S8 |
| 2511.07800 | From Experience to Strategy: Empowering LLM Agents with Trainable | 2025 | **BATCH20** FULL · S1/S7/S8 |
| 2511.12997 | WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guid | 2025 | **BATCH20** FULL · S2/S3/S7 |
| 2511.17208 | A Simple Yet Strong Baseline for Long-Term Conversational Memory  | 2025 | **BATCH20** FULL · S1/S7/S8 |
| 2511.21678 | Agentic Learner with Grow-and-Refine Multimodal Semantic Memory | 2025 | **BATCH20** FULL · S2/S3/S7/S8 |
| 2511.21726 | Goal-Directed Search Outperforms Goal-Agnostic Memory Compression | 2025 | **BATCH20** FULL · S2/S3/S7/S8 |
| 2512.02425 | WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning | 2025 | **BATCH20** FULL · S2/S3/S7/S8 |
| 2512.12360 | VideoARM: Agentic Reasoning over Hierarchical Memory for Long-For | 2025 | **BATCH20** FULL · S2/S3/S7/S8 |
| 2512.16962 | MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Exp | 2025 | **BATCH20** FULL · S1/S7/S8 |
| 2601.03192 | MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on | 2026 | **BATCH20** FULL · S1/S7/S8 |
| 2601.03417 | Implicit Graph, Explicit Retrieval: Towards Efficient and Interpr | 2026 | **BATCH20** FULL · S1/S7/S8 |
| 2601.06037 | TeleMem: Building Long-Term and Multimodal Memory for Agentic AI | 2026 | **BATCH20** FULL · S1/S7/S8 |
| 2601.06377 | HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents | 2026 | **BATCH20** FULL · S1/S7/S8 |
| 2601.08323 | AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Ope | 2026 | **BATCH20** FULL · S2/S3/S7/S8 |
| 2601.10744 | Explore with Long-term Memory: A Benchmark and Multimodal LLM-bas | 2026 | **BATCH20** FULL · S1/S7/S8 |
| 2601.14192 | Toward Efficient Agents: Memory, Tool learning, and Planning | 2026 | **BATCH20** FULL · S2/S3/S7/S8 |
| 2602.15329 | EventMemAgent: Hierarchical Event-Centric Memory for Online Video | 2026 | **BATCH20** FULL · S3/S5/S7/S8 |
| 2603.00503 | M$^2$: Dual-Memory Augmentation for Long-Horizon Web Agents via T | 2026 | **BATCH20** FULL · S1/S7/S8 |
| 2603.01455 | From Verbatim to Gist: Distilling Pyramidal Multimodal Memory via | 2026 | **BATCH21** FULL · S2/S3/S7/S8 |
| 2305.05091 | Knowledge-enhanced Agents for Interactive Text Games | 2023 | **BATCH21** FULL · S2/S3/S7/S8 |
| 2305.13711 | LLM-Eval: Unified Multi-Dimensional Automatic Evaluation for Open | 2023 | **BATCH21** FULL · S1/S7/S8 |
| 2305.14318 | CREATOR: Tool Creation for Disentangling Abstract and Concrete Re | 2023 | **BATCH21** FULL · S2/S3/S7/S8 |
| 2305.14323 | ChatCoT: Tool-Augmented Chain-of-Thought Reasoning on Chat-based  | 2023 | **BATCH21** FULL · S1/S7/S8 |
| 2305.14325 | Improving Factuality and Reasoning in Language Models through Mul | 2023 | **BATCH21** FULL · S3/S5/S7/S8 |
| 2305.15852 | Self-contradictory Hallucinations of Large Language Models: Evalu | 2023 | **BATCH21** FULL · S1/S7/S8 |
| 2305.19118 | Encouraging Divergent Thinking in Large Language Models through M | 2023 | **BATCH21** FULL · S1/S7/S8 |
| 2306.03314 | Multi-Agent Collaboration: Harnessing the Power of Intelligent LL | 2023 | **BATCH21** FULL · S1/S7/S8 |
| 2306.08302 | Unifying Large Language Models and Knowledge Graphs: A Roadmap | 2023 | **BATCH21** FULL · S3/S5/S7/S8 |
| 2307.07047 | Does Collaborative Human-LM Dialogue Generation Help Information  | 2023 | **BATCH21** FULL · S2/S3/S7 |
| 2307.11019 | Investigating the Factual Knowledge Boundary of Large Language Mo | 2023 | **BATCH21** FULL · S1/S7/S8 |
| 2307.12856 | A Real-World WebAgent with Planning, Long Context Understanding,  | 2023 | **BATCH21** FULL · S2/S3/S7/S8 |
| 2308.03427 | TPTU: Large Language Model-based AI Agents for Task Planning and  | 2023 | **BATCH21** FULL · S1/S7/S8 |
| 2308.03549 | Zhongjing: Enhancing the Chinese Medical Capabilities of Large La | 2023 | **BATCH21** FULL · S2/S3/S7 |
| 2308.04026 | AgentSims: An Open-Source Sandbox for Large Language Model Evalua | 2023 | **BATCH21** FULL · S1/S7/S8 |
| 2308.11339 | ProAgent: Building Proactive Cooperative Agents with Large Langua | 2023 | **BATCH21** FULL · S3/S5/S7/S8 |
| 2309.01918 | RoboAgent: Generalization and Efficiency in Robot Manipulation vi | 2023 | **BATCH21** FULL · S2/S3/S7/S8 |
| 2309.03736 | TradingGPT: Multi-Agent System with Layered Memory and Distinct C | 2023 | **BATCH21** FULL · S3/S5/S7/S8 |
| 2309.04175 | Knowledge-tuning Large Language Models with Structured Medical Kn | 2023 | **BATCH21** FULL · S2/S3/S7/S8 |
| 2309.06794 | Cognitive Mirage: A Review of Hallucinations in Large Language Mo | 2023 | **BATCH22** FULL · S2/S3/S7/S8 |
| 2309.07870 | Agents: An Open-source Framework for Autonomous Language Agents | 2023 | **BATCH22** FULL · S3/S5/S7/S8 |
| 2310.02172 | Lyfe Agents: Generative agents for low-cost real-time social inte | 2023 | **BATCH22** FULL · S1/S7/S8 |
| 2310.03025 | Retrieval meets Long Context Large Language Models | 2023 | **BATCH22** FULL · S1/S7/S8 |
| 2310.05036 | AvalonBench: Evaluating LLMs Playing the Game of Avalon | 2023 | **BATCH22** FULL · S1/S7/S8 |
| 2310.06500 | MetaAgents: Large Language Model Based Agents for Decision-Making | 2023 | **BATCH22** FULL · S2/S3/S7/S8 |
| 2310.09233 | AgentCF: Collaborative Learning with Autonomous Language Agents f | 2023 | **BATCH22** FULL · S2/S3/S7/S8 |
| 2310.10436 | EconAgent: Large Language Model-Empowered Agents for Simulating M | 2023 | **BATCH22** FULL · S2/S3/S7/S8 |
| 2311.05876 | Trends in Integration of Knowledge and Large Language Models: A S | 2023 | **BATCH22** FULL · S1/S7/S8 |
| 2311.05997 | JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Mult | 2023 | **BATCH22** FULL · S4/S6/S7 |
| 2311.11315 | TPTU-v2: Boosting Task Planning and Tool Usage of Large Language  | 2023 | **BATCH22** FULL · S1/S7/S8 |
| 2311.17227 | War and Peace (WarAgent): Large Language Model-based Multi-Agent  | 2023 | **BATCH22** FULL · S1/S7/S8 |
| 2312.04889 | KwaiAgents: Generalized Information-seeking Agent System with Lar | 2023 | **BATCH22** FULL · S2/S3/S7/S8 |
| 2401.05459 | Personal LLM Agents: Insights and Survey about the Capability, Ef | 2024 | **BATCH22** FULL · S4/S6/S7 |
| 2401.07128 | EHRAgent: Code Empowers Large Language Models for Few-shot Comple | 2024 | **BATCH22** FULL · S2/S3/S7/S8 |
| 2402.14034 | AgentScope: A Flexible yet Robust Multi-Agent Platform | 2024 | **BATCH22** FULL · S3/S5/S7/S8 |
| 2402.18485 | A Multimodal Foundation Agent for Financial Trading: Tool-Augment | 2024 | **BATCH22** FULL · S2/S3/S7/S8 |
| 2403.04317 | Online Adaptation of Language Models with a Memory of Amortized C | 2024 | **BATCH22** FULL · S1/S2/S7 |
| 2403.17134 | RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | 2024 | **BATCH22** FULL · S2/S3/S7/S8 |
| 2404.09982 | INMS: Memory Sharing for Large Language Model based Agents | 2024 | **BATCH22** FULL · S1/S7/S8 |
| 2405.02957 | Agent Hospital: A Simulacrum of Hospital with Evolvable Medical A | 2024 | **BATCH23** FULL · S2/S3/S7/S8 |
| 2405.14486 | RefChecker: Reference-based Fine-grained Hallucination Checker an | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2405.16089 | Towards Completeness-Oriented Tool Retrieval for Large Language M | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2405.19686 | Knowledge Graph Tuning: Real-time Large Language Model Personaliz | 2024 | **BATCH23** FULL · S3/S5/S7/S8 |
| 2406.10149 | BABILong: Testing the Limits of LLMs with Long Context Reasoning- | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2406.12430 | PlanRAG: A Plan-then-Retrieval Augmented Generation for Generativ | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2406.13743 | GenAI-Bench: Evaluating and Improving Compositional Text-to-Visua | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2407.01178 | $\text{Memory}^3$: Language Modeling with Explicit Memory | 2024 | **BATCH23** FULL · S2/S3/S7/S8 |
| 2408.03615 | Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Lon | 2024 | **BATCH23** FULL · S3/S5/S7/S8 |
| 2408.08921 | Graph Retrieval-Augmented Generation: A Survey | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2408.16967 | MemLong: Memory-Augmented Retrieval for Long Text Modeling | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2409.07429 | Agent Workflow Memory | 2024 | **BATCH23** FULL · S2/S3/S7/S8 |
| 2409.20163 | MemSim: A Bayesian Simulator for Evaluating Memory of LLM-based P | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2410.02694 | HELMET: How to Evaluate Long-Context Language Models Effectively  | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2410.03156 | MELODI: Exploring Memory Compression for Long Contexts | 2024 | **BATCH23** FULL · S2/S3/S7 |
| 2410.06992 | SWE-Bench+: Enhanced Coding Benchmark for LLMs | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2410.20878 | AutoRAG: Automated Framework for optimization of Retrieval Augmen | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2411.11581 | OASIS: Open Agent Social Interaction Simulations with One Million | 2024 | **BATCH23** FULL · S2/S3/S7/S8 |
| 2411.13093 | Video-RAG: Visually-aligned Retrieval-Augmented Long Video Compre | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2412.15266 | On the Structural Memory of LLM Agents | 2024 | **BATCH23** FULL · S1/S7/S8 |
| 2412.15274 | Memory-Augmented Agent Training for Business Document Understandi | 2024 | **BATCH24** FULL · S2/S3/S7/S8 |
| 2412.15540 | MRAG: A Modular Retrieval Framework for Time-Sensitive Question A | 2024 | **BATCH24** FULL · S1/S7/S8 |
| 2501.00358 | Embodied VideoAgent: Persistent Memory from Egocentric Videos and | 2025 | **BATCH24** FULL · S2/S3/S7/S8 |
| 2501.01702 | AgentRefine: Enhancing Agent Generalization through Refinement Tu | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2501.05366 | Search-o1: Agentic Search-Enhanced Large Reasoning Models | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2501.06590 | ChemAgent: Self-updating Library in Large Language Models Improve | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2501.12254 | Memory Storyboard: Leveraging Temporal Segmentation for Streaming | 2025 | **BATCH24** FULL · S2/S3/S7 |
| 2502.03358 | Minerva: A Programmable Memory Test Benchmark for Language Models | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2503.07018 | Toward Multi-Session Personalized Conversation: A Large-Scale Dat | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2503.08175 | Privacy-Enhancing Paradigms within Federated Multi-Agent Systems | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2503.09516 | Search-R1: Training LLMs to Reason and Leverage Search Engines wi | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2504.12369 | WorldMem: Long-term Consistent World Simulation with Memory | 2025 | **BATCH24** FULL · S2/S3/S7/S8 |
| 2504.12516 | BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agent | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2504.13079 | Retrieval-Augmented Generation with Conflicting Evidence | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2504.13805 | LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration  | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2504.20073 | RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn  | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2504.21776 | WebThinker: Empowering Large Reasoning Models with Deep Research  | 2025 | **BATCH24** FULL · S4/S6/S7 |
| 2505.15962 | Pre-training Limited Memory Language Models with Internal and Ext | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2505.16067 | How Memory Management Impacts LLM Agents: An Empirical Study of E | 2025 | **BATCH24** FULL · S2/S3/S7/S8 |
| 2505.16348 | Embodied Agents Meet Personalization: Investigating Challenges an | 2025 | **BATCH24** FULL · S1/S7/S8 |
| 2505.16421 | WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinfo | 2025 | **BATCH25** FULL · S1/S7/S8 |
| 2506.01952 | WebChoreArena: Evaluating Web Browsing Agents on Realistic Tediou | 2025 | **BATCH25** FULL · S1/S7/S8 |
| 2506.14728 | AgentDistill: Training-Free Agent Distillation with Generalizable | 2025 | **BATCH25** FULL · S3/S5/S7/S8 |
| 2506.18019 | Graphs Meet AI Agents: Taxonomy, Progress, and Future Opportuniti | 2025 | **BATCH25** FULL · S3/S5/S7/S8 |
| 2507.02592 | WebSailor: Navigating Super-human Reasoning for Web Agent | 2025 | **BATCH25** FULL · S1/S7/S8 |
| 2507.03616 | EvoAgentX: An Automated Framework for Evolving Agentic Workflows | 2025 | **BATCH25** FULL · S1/S7/S8 |
| 2507.07998 | PyVision: Agentic Vision with Dynamic Tooling | 2025 | **BATCH25** FULL · S1/S7/S8 |
| 2507.16784 | Beyond Context Limits: Subconscious Threads for Long-Horizon Reas | 2025 | **BATCH25** FULL · S2/S3/S7/S8 |
| 2507.21055 | Can Memory-Augmented LLM Agents Aid Journalism in Interpreting an | 2025 | **BATCH25** FULL · S2/S3/S7/S8 |
| 2507.21407 | Graph-Augmented Large Language Model Agents: Current Progress and | 2025 | **BATCH25** FULL · S3/S5/S7/S8 |
| 2508.03680 | Agent Lightning: Train ANY AI Agents with Reinforcement Learning | 2025 | **BATCH25** FULL · S3/S5/S7/S8 |
| 2508.04700 | SEAgent: Self-Evolving Computer Use Agent with Autonomous Learnin | 2025 | **BATCH25** FULL · S2/S3/S7/S8 |
| 2508.07010 | Narrative Memory in Machines: Multi-Agent Arc Extraction in Seria | 2025 | **BATCH25** FULL · S3/S5/S7/S8 |
| 2508.07407 | A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm | 2025 | **BATCH25** FULL · S2/S3/S7/S8 |
| 2508.09874 | Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Lang | 2025 | **BATCH25** FULL · S1/S7/S8 |
| 2508.11567 | AgentMental: An Interactive Multi-Agent Framework for Explainable | 2025 | **BATCH25** FULL · S1/S7/S8 |
| 2508.14704 | MCP-Universe: Benchmarking Large Language Models with Real-World  | 2025 | **BATCH25** FULL · S1/S7/S8 |
| 2508.15253 | Conflict-Aware Soft Prompting for Retrieval-Augmented Generation | 2025 | **BATCH25** FULL · S1/S7/S8 |
| 2508.15305 | Coarse-to-Fine Grounded Memory for LLM Agent Planning | 2025 | **BATCH25** FULL · S2/S3/S7/S8 |
| 2508.16629 | Learn to Memorize: Optimizing LLM-based Agents with Adaptive Memo | 2025 | **BATCH25** FULL · S1/S7/S8 |

### Crypto / capability / hooks

| Source | Depth | Memo |
|--------|-------|------|
| C2SP age.md | Full | SEALED_PACK |
| libsodium seal/box/sign | Full | SEALED_PACK |
| Magic Wormhole protocols | Full | SEALED_PACK |
| MLS RFC 9420 / 9750 | Substantial | SEALED_PACK |
| Biscuits DESIGN+spec | Full | SEALED_PACK |
| Macaroons NDSS 2014 | Substantial | SEALED_PACK |
| Claude Code hooks docs | Full | PARALLEL + **P1** |
| Cursor hooks docs | Full | PARALLEL + **P1** |
| Claude Compaction (`compact-2026-01-12`) | Full | **P1** |
| Claude Context editing (`clear_tool_uses` / thinking) | Full | **P1** |

### Classical / supporting FULL (context only)

| ID | Note | Memo |
|----|------|------|
| 1410.5401 | NTM | P3 supporting (not Anchor store) |
| 1805.04263 / 2004.04906 / 2205.12674 | Memory-net / memorizing-transformer lineage | P3 supporting |
| 2503.18813 / 2505.00675 / 2501.12948 | Additional fetched fulltexts used as supporting | P3/P4 |

---

## 3. Survey-derived insights (mechanism-level, not keyword)

From deep-reading the surveys above (not just their abstracts):

### 3.1 Write–manage–read loop (Du 2603.07670)

Agent memory is \(\mathcal{R}/\mathcal{U}\) inside a POMDP belief update — not a database lookup. Five tensioned objectives: **utility, efficiency, adaptivity, faithfulness, governance**. MoDeX already encodes these as Anchors survival, budgets, promotion, SUPERSEDES, capability gates.

### 3.2 Temporal × substrate × control taxonomy

- Temporal: working / episodic / semantic / procedural → maps to L1 / L2 / L3 / (skill scripts later).
- Substrate: context text / vectors / structured graphs / executable repos → MoDeX hybrid (sqlite graph + optional embeddings).
- Control: heuristic / prompted self-control / learned RL — MoDeX v1 = **heuristic + explicit CLI**, not RL memory controllers.

### 3.3 Storage → Reflection → Experience evolution (2605.06716)

Frontier “Experience” stage = active exploration + cross-trajectory abstraction. MoDeX L3 Anchors are Experience-class; do not auto-publish reflections (shareable memo).

### 3.4 Graph-memory lifecycle (2602.05665)

Extract → integrate (conflict/prune) → retrieve (entity expand / BFS / PPR) → consolidate. Bi-temporal invalidation (Graphiti) and LLM ADD/UPDATE/DELETE (Mem0) are the two dominant update schools — MoDeX adopts **invalidate+audit**, not silent DELETE.

### 3.5 Evaluation pain (2602.19320)

Benchmark saturation, judge sensitivity, backbone-dependent accuracy, and memory-maintenance latency often erase paper gains. MoDeX eval criteria (§15 architecture) must include **governance probes** (Inv-Scope, unshare cascade), not only Q&A recall.

### 3.6 P3/P4 constants locked from FULL reads

| Constant | Value | Source |
|----------|-------|--------|
| Synonym / ALIAS τ | 0.8 | HippoRAG / HippoRAG2 |
| PPR damping | 0.5 | HippoRAG / HippoRAG2 |
| Recognition top-k triples | 5 | HippoRAG2 |
| Graphiti reflection window | n=4 | Zep/Graphiti |
| Mem0 ops | ADD/UPDATE/DELETE/NOOP | Mem0 → MoDeX INVALIDATE |
| Bi-temporal fields | valid/invalid + created/expired | Graphiti + TOKI |
| Version chain | superseded_by / supersedes | 2603.15994 |
| Conflict pipeline order | conflict before near-dup | MemClaw |

### 3.7 P2 cognify constants locked from FULL reads

| Constant | Value | Source |
|----------|-------|--------|
| Segment join θ | 0.6 (cos+Jaccard) | MemoryOS |
| Heat τ promote | 5 (Tier-B signal only) | MemoryOS |
| Recency μ | 1e7 s | MemoryOS |
| RecMem θ_sim / θ_count | 0.7 / 3 (eng) | RecMem + promotion lock |
| ES-Mem MI quantile q | 0.35 | ES-Mem |
| Nemori semantic τ | 0.70 | Nemori |
| Pressure warn / flush | 70% / 100%→~50% | MemGPT |
| Attention sinks pin | 4 conceptual slots | StreamingLLM |
| IDLE_BOUNDARY_MIN | 25 min | WORKSTREAM lock |
| HARD boundaries | PRE_COMPACT, SESSION_END, explicit, ws_switch, idle | hooks + P2 |

---

## 4. Survey-indexed corpus (named, not independently FULL-read)

These appear repeatedly across surveys and are **queued** for future FULL passes. One-line roles only until deep-read:

| Paper / system | One-line role |
|----------------|---------------|
| Reflexion / Voyager | **FULL in P1/P2** (+ Batch 2) — kept here only as survey cross-refs |
| Cognee | **FULL Batch11** (`2505.24478`) — KG–LLM interface paper; toolkit docs still queued |
| OpenMemory / Memary | Graph memory toolkits (no primary arXiv yet) · **MemMachine FULL Batch11** (`2604.04853`) |
| LoCoMo / LongMemEval / MemoryAgentBench / MemoryArena / MemBench / RealMem | Evaluation suites — LoCoMo/LongMemEval/MemoryAgentBench/DialSim/MemoryBench now FULL |
| RETRO / Memorizing Transformers / RMT | **FULL in P1/P2** — neural parametric / retrieval memory lineage |
| Memory Networks / NTM / DNC | Memory Networks FULL in P1; NTM supporting in classical table |
| ReAct | **FULL in P1** — trajectory-as-short-horizon-memory |
| FLEX | Semantic gating for trajectory merge |
| ConfAIde / CaMeL / Fides | **ConfAIde FULL Batch12** (`2310.17884`); **Fides FULL Batch12** (`2505.23643`); **CaMeL FULL** in P6 + Batch4 RE-READ (`2503.18813`) |
| Classic REBEL paper | Seq2seq RE; arXiv ID collision in fetch — use HippoRAG OpenIE practice for MoDeX v1 |
| MemU / Memobase | Product names; no matching arXiv primary papers found in Batch 3 search |
| … | See bibliographies of 2512.13564, 2603.07670, 2602.05665, 2309.07864 for the long tail |

**Next FULL-read batches (priority):** see [`queue/FULL_QUEUE_500.md`](queue/FULL_QUEUE_500.md) tier-1 first.

Completed in Batch 4 (2026-08-08): Memento 2, LongMemEval-V2, MemoryArena, FLEX, PrefEval (FULL); CaMeL/ConfAIde/MAB/LoCoMo/LME/HaluMem/… RE-READ — [`batches/BATCH4_LEDGER_DELTA.md`](batches/BATCH4_LEDGER_DELTA.md).

Completed in Batch 5 (2026-08-08): **18 FULL** tier-1 eval/failure (AgentBench, GAIA, WebArena, CRAG×2, MultiHop-RAG, Adaptive Chameleon, FreshQA, LongBench×2, RULER, ∞Bench, Self-RAG, RGB, PerLTQA, NeedleBench, HotpotQA, 2Wiki) — [`batches/BATCH5_LEDGER_DELTA.md`](batches/BATCH5_LEDGER_DELTA.md).

Completed in Batch 6 (2026-08-08): **16 FULL** capture/compaction · episode boundaries · graph/conflict (GraphReader, MAMA, LLMLingua×3, RECOMP, Scissorhands, PyramidKV, Quest, Selective Context, Activation Beacon, SuperDialseg, SeCom, ExpeL, ToG, Resolving Knowledge Conflicts) — [`batches/BATCH6_LEDGER_DELTA.md`](batches/BATCH6_LEDGER_DELTA.md).

Completed in Batch 7 (2026-08-08): **16 FULL** privacy/capability/share-leakage/seal (MEXTRA, AgentPoison, MINJA, Spill the Beans, PoisonedRAG, InjecAgent, AgentDojo, AirGapAgent, Progent, PrivacyLens, BIPIA, RAG-MIA, GEIA, RAG backdoor extract, IPI Firewalls, CVA) — [`batches/BATCH7_LEDGER_DELTA.md`](batches/BATCH7_LEDGER_DELTA.md).

Completed in Batch 8 (2026-08-08): **16 FULL** compress/retrieve/active-RAG/injection (FLARE, ConflictRAG, IRCoT, Gist Tokens, Text Embeddings Reveal, Chain-of-Note, HouYi PI, CCM, MemoRAG, xRAG, ReadAgent, BadAgent, Automated PI/AgentDojo, KATE, RAG-Fusion, ADR/QOC eng-judgment) — [`batches/BATCH8_LEDGER_DELTA.md`](batches/BATCH8_LEDGER_DELTA.md).

Completed in Batch 9 (2026-08-08): **17 FULL** eval/privacy/active-retrieve/injection-memory + **5 RE-READ** (ConfAIde, MemBench, RealMem, Fides, HaluMem) — [`batches/BATCH9_LEDGER_DELTA.md`](batches/BATCH9_LEDGER_DELTA.md).

Completed in Batch 10 (2026-08-08): **17 FULL** capture/episode/boundary/compaction (Membox, RMM, ReSum, BEAM/LIGHT, Context-Folding, HiAgent, MemWalker, …) — [`batches/BATCH10_LEDGER_DELTA.md`](batches/BATCH10_LEDGER_DELTA.md).

Completed in Batch 11 (2026-08-08): **13 FULL** graph/compose/multi-agent/entity-resolve (Cognee, MemMachine, AgentGit, MRAgent, SYNAPSE, StructGPT, AgentVerse, Intrinsic Memory, LINK-KG, iText2KG, BoostER, LLM-ER, KcMF) — [`batches/BATCH11_LEDGER_DELTA.md`](batches/BATCH11_LEDGER_DELTA.md). *(MIRIX, MemInsight, Memp, Memanto ledgered under Batch9/10.)*

Completed in Batch 12 (2026-08-08): **12 FULL** hydrate/seal/routing (ConfAIde/Fides/RealMem/MemBench/HaluMem RE-READ backfill + RankRAG, RAGRouter, SkewRoute, ppRAG, PIR-RAG, PRAG, HyDE, RAG survey) — [`batches/BATCH12_LEDGER_DELTA.md`](batches/BATCH12_LEDGER_DELTA.md). *(MRMMIA, SSE, DP-RAG, Membox ledgered under Batch9/10.)*

Completed in Batch 13 (2026-08-08): **17 FULL** promote/eng-judgment/abstention/provenance (FEVER, VitaminC, G-Eval, Prometheus 2, R-Tuning, RAGAS, FLAME, hallucination sources, ReMe, ERL, Auto-CoT, REVERSE, active ICL, CoT design, Retroformer, Early Experience, PerCul) — [`batches/BATCH13_LEDGER_DELTA.md`](batches/BATCH13_LEDGER_DELTA.md).

Completed in Batch 14 (2026-08-08): **17 FULL** agent-memory/runway (ChatDB, AgentGym, kNN-LM, ColBERT, Atlas, REALM, MemoryLLM, M+, MemGen, InfLLM, neural/managing/hierarchical procedural memory, LeanMem, ELITE, ElasticMem, AgentGym-RL) — [`batches/BATCH14_LEDGER_DELTA.md`](batches/BATCH14_LEDGER_DELTA.md).

Completed in Batch 15 (2026-08-08): **8 FULL** eval/runway (AppWorld, MuSiQue, RealTime QA, SituatedQA, MSC, FiD, SWE-bench, τ-bench) — **300 FULL milestone** — [`batches/BATCH15_LEDGER_DELTA.md`](batches/BATCH15_LEDGER_DELTA.md).

Still high-priority queued:
1. OpenMemory / Memary toolkits (no primary arXiv) + Cognee product docs beyond paper  
2. Clean REBEL / Stanford OpenIE canonical PDFs  
3. Remaining tier-1 eval from 500 runway  
4. Product docs: Claude/Cursor compaction deltas beyond P1 inventory  
5. Remaining non-eval tier-2–6 items from the 500 runway

---

## 5. Process rule for future agents

When expanding this corpus:

1. Fetch full HTML/PDF.
2. Extract problem / representation / write-read-forget / compaction / conflict / privacy / MoDeX lessons.
3. Mark **FULL** in this inventory.
4. Only then promote claims into architecture locks.
5. Never cite a paper as “read” from title/abstract alone.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-08-08 | **Batch 13+14:** `batches/BATCH13_PROMOTE_WHY_FULL.md` + `BATCH14_MIXED_RUNWAY_FULL.md` — **34 NEW FULL** (17 promote/eng-judgment/abstention + 17 agent-memory/runway); deduped Batch9–12 overlap; ledger + queue rebuild on `Cursor/batch-to-300-fb37`. Cumulative arXiv FULL ≈274 (<300 target). |
| 2026-08-08 | **Batch 10:** `batches/BATCH10_CAPTURE_EPISODE_FULL.md` — **17 FULL** capture/episode/boundary/compaction (Membox, RMM, ReSum, Neural Paging, BEAM/LIGHT, StructMem, FluxMem, Context-Folding, HiAgent, MemWalker, …); deduped Batch11/12 overlap; ledger + queue rebuild. |
| 2026-08-08 | **Batch 9:** `batches/BATCH9_EVAL_PRIVACY_FULL.md` — **17 FULL** eval/privacy/active-retrieve/injection-memory (AMA-Bench, EvoMemBench, AgentMemBench, MRMMIA, stored PI, LPCI, Astute RAG, …) + **5 RE-READ**; deduped Batch11/12 overlap; ledger + queue rebuild. |
| 2026-08-08 | **Batch 12:** `batches/BATCH12_HYDRATE_SEAL_FULL.md` — **17 FULL** hydrate/retrieve/seal/routing (ConfAIde, Fides, RealMem, MemBench, MRMMIA, SSE, RankRAG, HyDE, ppRAG, PIR-RAG, PRAG, …); Fides via PDF extract; age/Wormhole/MLS already FULL in SEALED_PACK — not re-marked; ledger + queue rebuild. |
| 2026-08-08 | **Batch 11:** `batches/BATCH11_GRAPH_CONFLICT_FULL.md` — **17 FULL** graph/compose/multi-agent/entity-resolve (Cognee, MemMachine, AgentGit, MRAgent, SYNAPSE, MIRIX, LINK-KG, …); MIRIX newly ledgered (prior BATCH_SYSTEMS card only); ledger + queue rebuild. |
| 2026-08-08 | **Batch 8:** `batches/BATCH8_COMPRESS_RETRIEVE_FULL.md` — **16 FULL** compress/retrieve/active-RAG/injection (FLARE, ConflictRAG, IRCoT, Gist, CoN, CCM, MemoRAG, xRAG, ReadAgent, KATE, RAG-Fusion, HouYi PI, BadAgent, Automated PI, Text Embeddings Reveal, ADR/QOC); skipped duplicate Selective Context `2310.06201`; ledger + queue rebuild. |
| 2026-08-08 | **Batch 7:** `batches/BATCH7_PRIVACY_SEAL_FULL.md` — **16 FULL** privacy/capability/leakage/seal (MEXTRA, AgentPoison, MINJA, PoisonedRAG, AgentDojo, AirGapAgent, Progent, PrivacyLens, …); ledger + queue rebuild. |
| 2026-08-08 | **Batch 6:** `batches/BATCH6_CAPTURE_GRAPH_FULL.md` — **16 FULL** capture/compaction · episode · graph/conflict (GraphReader, MAMA arXiv ID, LLMLingua family, KV cluster, SeCom, ToG, …); ledger + queue rebuild. |
| 2026-08-08 | **Batch 5:** `batches/BATCH5_EVAL_FAILURE_FULL.md` — **18 FULL** tier-1 eval/failure; ledger + queue rebuild. |
| 2026-08-08 | **Track 0 reboot:** Kedger stage columns; FULL runway queue (500); cache path `/tmp/kedger-papers/full/`; CaMeL queue cleared; Batch4 ledger merge (+5 FULL). |
| 2026-08-08 | **Batch 4:** `batches/BATCH4_EVAL_SYSTEMS_FULL.md` — 5 FULL + 11 RE-READ (eval/systems/privacy). |
| 2026-08-08 | Initial honest inventory after first multi-cluster deep-read pass. |
| 2026-08-08 | P3/P4 implementation pass: ≥55 FULL bodies; `impl/P3_ANCHORS_GRAPH.md` + `impl/P4_CONFLICT_COMPOSE.md`; expanded ledger (AriGraph, HyperGraphRAG, MAGMA, G-Memory, Selective Supersession, MemoryOS, Memory-R1, multi-agent frameworks, ReLiK, surveys). |
| 2026-08-08 | **Batch 3:** 15 new FULL + 3 re-read extras in `AGENT_MEMORY_CORPUS_DEEP_READ_BATCH3.md` (Memento, ReasoningBank, MEM1, LEGOMem, MemAct, O-Mem, Agent KB, H-Mem, MemoryBench, DialSim, MemoChat, Memory-as-a-Tool, Sleep-SCM, LTM Self-Evolution, LLM-Agents §memory; extras: MemoryBank/SCM/TiM). P5 hydrate IDs recorded in ledger. |
| 2026-08-08 | P2 major expansion: ES-Mem (2601.07582), Membox (2601.03785), RecMem body thresholds, MemoryBank; cognify HARD/SOFT rules + `boundary_summary` + episode SQL. |
| 2026-08-08 | P2 FULL deep-read pass: **28** mechanism cards in `impl/P2_EPISODE_COGNIFY.md` (~785 lines); ledger adds MemoryBank, SCM, HEMA, Cognitive Weave, RecSumBooks, TiM, StreamingLLM, Lost-in-Middle, MemOS, DialSTART, HyperSeg, GranularityTopicSeg; Graphiti/A-MEM/Nemori/… marked **P2**. |
| 2026-08-08 | **P1 FULL deep-read pass:** `impl/P1_CAPTURE_WORKING.md` (**32** mechanism cards) — MemGPT/GenAgents/ReAct/Reflexion + KV lineage (StreamingLLM/H₂O/SnapKV/Landmark/Compressive/Tr-XL/Memorizing/RMT/AutoCompressors/Unlimiformer/ICAE) + RAG/Toolformer/SCM/MemoryBank/TiM + Claude/Cursor hooks & compaction/context-editing docs + AIOS/MemOS/RET-LLM. **P2 expanded to 39 cards** (Voyager/Larimar/MemAgent/LoCoMo/LongMemEval/RETRO/AriGraph/MemoryAgentBench/RecSumDialogue/surveys). Ledger + hooks/compaction rows updated. |
