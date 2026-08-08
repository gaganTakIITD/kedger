# MoDeX Research Corpus Inventory

> **Date:** 2026-08-08  
> **Purpose:** Honest tracking of what was **deep-read** vs **survey-indexed** vs **not yet read**.  
> **User constraint:** Do not keyword-skim the literature — gather mechanism-level insights.

---

## 0. Coverage honesty (read this first)

We **cannot** truthfully claim end-to-end reading of 200+ full papers in one agent session. Claiming that would be keyword theater.

What we *can* and *did* do:

1. **Deep-read** the load-bearing primary sources for each design lock (full HTML/PDF bodies).
2. **Deep-read multiple 2024–2026 surveys** that curate the wider corpus, then extract taxonomies + citation maps.
3. Keep an inventory so future passes expand **FULL** coverage deliberately instead of pretending it already exists.

| Bucket | Approx count | Meaning |
|--------|--------------|---------|
| **FULL deep-read** | **~110+ distinct primary texts** | Full body mechanisms extracted into memos (incl. P1–P5 + Batch 2/3) |
| **On-disk fulltext cache** | **240+** files in `/tmp/modex-papers/full/` | Fetched bodies available for continued extraction |
| **Survey-indexed** | 150–300+ via survey bibliographies | Named + one-line role from surveys; not independently full-read |
| **Stub / TODO** | remainder of agent-memory + crypto/auth literature | Queued for later FULL passes |

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
| ACL'26 | MAMA topology leakage | 2026 | SHAREABLE |
| 2606.29788 | MemLeak | 2026 | SHAREABLE + **P4** |
| 2605.10614 | PRISM | 2026 | SHAREABLE |
| 2505.18279 | Collaborative Memory | 2025 | SHAREABLE + **P3/P4** |
| — | VAULT (eKNOW 2025) | 2025 | SHAREABLE |
| — | Capability Myths Demolished | 2003 | SHAREABLE |
| — | Spritely / OcapPub | 2023+ | SHAREABLE |
| RFC 2693 | SPKI Certificate Theory | 1999 | SHAREABLE |

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
| Cognee | Queryable graph embeddings library (docs/product; limited arXiv) |
| OpenMemory / MemMachine / Memary | Graph memory toolkits |
| LoCoMo / LongMemEval / MemoryAgentBench / MemoryArena / MemBench / RealMem | Evaluation suites — LoCoMo/LongMemEval/MemoryAgentBench/DialSim/MemoryBench now FULL |
| RETRO / Memorizing Transformers / RMT | **FULL in P1/P2** — neural parametric / retrieval memory lineage |
| Memory Networks / NTM / DNC | Memory Networks FULL in P1; NTM supporting in classical table |
| ReAct | **FULL in P1** — trajectory-as-short-horizon-memory |
| FLEX | Semantic gating for trajectory merge |
| ConfAIde / CaMeL / Fides | ConfAIde + Fides FULL in Batch 2; CaMeL still queued |
| Classic REBEL paper | Seq2seq RE; arXiv ID collision in fetch — use HippoRAG OpenIE practice for MoDeX v1 |
| MemU / Memobase | Product names; no matching arXiv primary papers found in Batch 3 search |
| … | See bibliographies of 2512.13564, 2603.07670, 2602.05665, 2309.07864 for the long tail |

**Next FULL-read batches (priority):**
1. CaMeL (privacy IFC) — still queued after Batch 2
2. Cognee docs + remaining toolkit READMEs (OpenMemory / MemMachine / Memary)
3. Remaining MemClaw-cited leakage papers not yet FULL
4. Clean REBEL / Stanford OpenIE canonical PDFs (non-arXiv if needed)
5. Memento 2 (2512.22716) stateful reflective memory follow-on
6. LongMemEval-V2 (2605.12493) if eng-colleague eval claims hold

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
| 2026-08-08 | Initial honest inventory after first multi-cluster deep-read pass. |
| 2026-08-08 | P3/P4 implementation pass: ≥55 FULL bodies; `impl/P3_ANCHORS_GRAPH.md` + `impl/P4_CONFLICT_COMPOSE.md`; expanded ledger (AriGraph, HyperGraphRAG, MAGMA, G-Memory, Selective Supersession, MemoryOS, Memory-R1, multi-agent frameworks, ReLiK, surveys). |
| 2026-08-08 | **Batch 3:** 15 new FULL + 3 re-read extras in `AGENT_MEMORY_CORPUS_DEEP_READ_BATCH3.md` (Memento, ReasoningBank, MEM1, LEGOMem, MemAct, O-Mem, Agent KB, H-Mem, MemoryBench, DialSim, MemoChat, Memory-as-a-Tool, Sleep-SCM, LTM Self-Evolution, LLM-Agents §memory; extras: MemoryBank/SCM/TiM). P5 hydrate IDs recorded in ledger. |
| 2026-08-08 | P2 major expansion: ES-Mem (2601.07582), Membox (2601.03785), RecMem body thresholds, MemoryBank; cognify HARD/SOFT rules + `boundary_summary` + episode SQL. |
| 2026-08-08 | P2 FULL deep-read pass: **28** mechanism cards in `impl/P2_EPISODE_COGNIFY.md` (~785 lines); ledger adds MemoryBank, SCM, HEMA, Cognitive Weave, RecSumBooks, TiM, StreamingLLM, Lost-in-Middle, MemOS, DialSTART, HyperSeg, GranularityTopicSeg; Graphiti/A-MEM/Nemori/… marked **P2**. |
| 2026-08-08 | **P1 FULL deep-read pass:** `impl/P1_CAPTURE_WORKING.md` (**32** mechanism cards) — MemGPT/GenAgents/ReAct/Reflexion + KV lineage (StreamingLLM/H₂O/SnapKV/Landmark/Compressive/Tr-XL/Memorizing/RMT/AutoCompressors/Unlimiformer/ICAE) + RAG/Toolformer/SCM/MemoryBank/TiM + Claude/Cursor hooks & compaction/context-editing docs + AIOS/MemOS/RET-LLM. **P2 expanded to 39 cards** (Voyager/Larimar/MemAgent/LoCoMo/LongMemEval/RETRO/AriGraph/MemoryAgentBench/RecSumDialogue/surveys). Ledger + hooks/compaction rows updated. |
