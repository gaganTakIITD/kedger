# Kedger Research Corpus Inventory

> **Date:** 2026-08-08 (Track 0 reboot)  
> **Product:** Kedger (historical memos may say MoDeX — labeling only)  
> **Purpose:** Honest tracking of what was **deep-read** vs **survey-indexed** vs **not yet read**.  
> **User constraint:** Do not keyword-skim the literature — gather mechanism-level insights.  
> **Program:** Research → Measure → Refine (see `KEDGER_STAGE_RESEARCH_MATRIX.md`, `EVAL_HARNESS.md`, `RESEARCH_CADENCE.md`).

---

## 0. Coverage honesty (read this first)

We **cannot** truthfully claim end-to-end reading of 500+ full papers in one agent session. Claiming that would be keyword theater.

What we *can* and *did* do:

1. **Deep-read** the load-bearing primary sources for each design lock (full HTML/PDF bodies).
2. **Deep-read multiple 2024–2026 surveys** that curate the wider corpus, then extract taxonomies + citation maps.
3. Keep an inventory so future passes expand **FULL** coverage deliberately instead of pretending it already exists.
4. Maintain a **≥500 prioritized FULL runway** in [`queue/FULL_QUEUE_500.md`](queue/FULL_QUEUE_500.md) (`seed_placeholder` ≠ FULL).

| Bucket | Approx count | Meaning |
|--------|--------------|---------|
| **FULL deep-read** | **~250+ distinct primary texts** | Through Batch14; Batch9 (+17 eval/privacy) + Batch10 (+17 episode/capture) on `Cursor/batch-to-300-fb37`; RE-READs do not double-count |
| **FULL runway queue** | **500** slots | `queue/full_queue.jsonl` — FULL + queued + seed_placeholder |
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
