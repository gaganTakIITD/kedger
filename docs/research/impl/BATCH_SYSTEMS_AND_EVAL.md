# Batch: Systems & Evaluation — Mechanism Cards for MoDeX

> **Date:** 2026-08-08  
> **Branch:** `Cursor/memory-architecture-spec-2e45`  
> **Source corpus:** `/tmp/modex-papers/full/` (arXiv HTML + PDF)  
> **Method:** Full-body extract via HTML→text or `pdftotext -layout`; mechanism fields only (not abstract skim).  
> **MoDeX lens:** L0 Observation → L1 WorkingState → L2 Episode → L3 Anchor → L4 Handoff; SUPERSEDES/CONTRADICTS; workstream isolation; capture/hydrate budgets.

---

## 0. Honesty table (this batch)

| Status | Papers |
|--------|--------|
| **FULL** — complete HTML body extracted and deep-read | MemoryOS (2506.06326); MemOS (2507.03724); MIRIX (2507.07957); MemoryAgentBench (2507.05257); MemGAS (2505.19549); Cognitive Weave (2506.08098); SCM (2304.13343); RET-LLM (2305.14322); AIOS (2403.16971); HaluMem (2511.03506); Mem-α (2509.25911); M3-Agent (2508.09736); Reflexion (2303.11366); Voyager (2305.16291); Self-RAG (2310.11511); StreamingLLM (2309.17453); MemAgent (2507.02259); Memory-R1 (2508.19828); LightMem (2510.18866); LoCoMo (2402.17753); MemBench (2506.21605); MemGPT (2310.08560, for P1 cross-ref) |
| **FULL via PDF** — `pdftotext` succeeded; HTML conversion failed or was abstract-only | G-Memory (2506.07398.pdf → 141k chars); Think-in-Memory (2311.08719.pdf → 80k); HEMA (2504.16754.pdf → 31k); Lost in the Middle (2307.03172.pdf → 95k); Recursive Summarizing (2109.10862.pdf → 141k) |
| **Failed / thin** | None of the listed targets failed entirely. HEMA HTML was abstract-only (4.7k); **PDF extract used instead (FULL)**. G-Memory HTML fatal; **PDF extract used (FULL)**. |

**Count FULL deep-reads this file:** 26 (+ MemGPT for capture/working constants).

---

## 1. Mechanism cards

Each card: `id`, `title`, `representation`, `write algo`, `read algo`, `compact/forget`, `conflict`, `privacy`, `failure modes`, `MoDeX impl lessons`.

---

### Card: MemoryOS — OS-style STM / MTM / LPM

| Field | Content |
|-------|---------|
| **id** | 2506.06326 |
| **title** | Memory OS of AI Agent (MemoryOS) |
| **read status** | FULL (HTML) |
| **representation** | Three tiers: **STM** = fixed-length queue of dialogue *pages* `page_i = {Q,R,T}` plus chain meta `meta^chain` (LLM decides chain-continue vs reset, then summarizes chain). **MTM** = *segmented paging*: topic segments containing pages; segment membership if `F_score = cos(e_s,e_p) + Jaccard(K_s,K_p) > θ`. **LPM** = User Persona (static profile + User KB FIFO + 90-dim User Traits) + Agent Persona (profile + Agent Traits FIFO). |
| **write algo** | New turn → STM page + chain meta. STM full → **FIFO migrate oldest page → MTM**. MTM: score page vs existing segments; merge if > θ else new segment; LLM summarizes segment. Segments with `Heat ≥ τ` promote traits/facts into LPM; User KB / Agent Traits queues size **100**, FIFO. |
| **read algo** | STM: **all** recent pages. MTM: two-stage — top-m segments by `F_score`, then top-k pages inside them; bump `N_visit` and `R_recency`. LPM: top-10 User KB + top-10 Agent Traits by semantic sim; always inject full User/Agent Profile + User Traits. Compose prompt → generate. |
| **compact/forget** | Heat: `Heat = α·N_visit + β·L_interaction + γ·R_recency`, `R_recency = exp(−Δt/μ)`, **μ = 1e7** (seconds). Lowest-heat segments evicted when MTM capacity exceeded. After LPM promote, reset `L_interaction→0` (heat drops) to avoid redundant re-promote. |
| **conflict** | No explicit SUPERSEDES; persona/KB FIFO silently drops oldest. Trait evolution via LLM overwrite of 90 dims — **in-place**, no audit trail. |
| **privacy** | Silent (persona stores PII/preferences without scoping). |
| **failure modes** | Flat FIFO (MemGPT-style) topic-mix; over-retrieve MTM pages adds noise (k>10 diminishing); θ too low merges unrelated topics; heat gaming if visit counter bumped carelessly. |
| **MoDeX impl lessons** | (1) Map STM→L0/L1 pages, MTM segments→L2 episodes, LPM facts/traits→L3 anchors (but **append+SUPERSEDES**, not trait overwrite). (2) Adopt heat for L2 eviction: store `n_visit`, `n_pages`, `last_access`; μ≈1e7s (~116 days half-life scale). (3) Segment join threshold **θ≈0.6** (paper default). (4) LPM promote heat **τ=5**. (5) MTM page retrieve **k=10**. (6) Two-stage retrieve (segment then page) = MoDeX workstream/community then Evidence. (7) Dialogue-chain meta = L1 WorkingState continuity flag. |

**Paper constants (MemoryOS):** θ=0.6; τ=5; μ=1e7; User KB/Traits queue=100; MTM top-k pages=10; α,β,γ relative weights (unspecified numeric defaults in text — treat as tunable, start equal after normalizing features).

---

### Card: MemOS — Memory OS with MemCube lifecycle

| Field | Content |
|-------|---------|
| **id** | 2507.03724 |
| **title** | MemOS: A Memory OS for AI System |
| **read status** | FULL (HTML) |
| **representation** | Three substrates: **plaintext** (structured fragments / graph paths task–concept–fact), **activation** (KV-cache / hidden / steering), **parameter** (weights / LoRA modules). Atomic unit **MemCube** = Memory Payload + Metadata Header (descriptive IDs, governance attrs, behavioral usage). Lifecycle states: Generated → Activated → Merged → Archived → Expired. Components: MemReader, MemScheduler, MemLifecycle, MemOperator, MemVault, Memory API (Provenance / Update / LogQuery). |
| **write algo** | Interface → MemReader parses intent → Memory API create with provenance ID, origin signature, semantic type, timestamp. MemOperator indexes (tags, semantic index, graph). MemScheduler chooses type + injection order. Cross-type migration: frequent plaintext → activation templates; stable knowledge → parameter/LoRA “capability modules”; inconsistent params backpatched from plaintext. |
| **read algo** | MemOperator retrieves candidates; MemScheduler ranks by contextual similarity, access frequency, temporal decay, priority tags; injects into runtime (activation for hot, plaintext for explainable, params for zero-shot skills). Local index cache for hot cubes; invalidate on contextual drift. |
| **compact/forget** | MemLifecycle transitions to Archived/Expired via access patterns + time decay + task labels. Fusion/merge of cubes. Cache eviction by frequency + drift heuristics. |
| **conflict** | Version-aware Update API (append / merge / overwrite with snapshots). Governance attributes for permissioned control. Explicit claim that RAG lacks versioning — MemOS adds it. |
| **privacy** | First-class: multi-level permission control, access audit, scoped preference memories that expire/archive after task. Cross-platform migration framed as “memory islands” problem. |
| **failure modes** | Over-ambitious parameter editing → global behavior shift; treating RAG as memory without lifecycle; memory islands across apps; opaque ChatGPT-style memory. |
| **MoDeX impl lessons** | (1) **MemCube ≈ Anchor+Evidence envelope**: every L3 object needs provenance ID, origin, semantic type, timestamps, permission scope. (2) MoDeX Phase A–B should ship plaintext+activation (L0–L4) before any parameter/LoRA memory. (3) Lifecycle FSM (Generated/Activated/Merged/Archived/Expired) maps to MoDeX draft→promoted→superseded→sealed→archived. (4) MemScheduler ranking features = hydrate scorer inputs. (5) Do not silently overwrite — use versioned Update API → SUPERSEDES edges. (6) Permission groups foreshadow MoDeX workstream / capability tokens. |

---

### Card: MIRIX — Six-type multi-agent memory

| Field | Content |
|-------|---------|
| **id** | 2507.07957 |
| **title** | MIRIX: Multi-Agent Memory System for LLM-Based Agents |
| **read status** | FULL (HTML) |
| **representation** | Six memories: **Core** (persona + human blocks, always-visible); **Episodic** (`event_type, summary, details, actor, timestamp`); **Semantic** (`name, summary, details, source`); **Procedural** (`entry_type∈{workflow,guide,script}, description, steps`); **Resource** (`title, summary, resource_type, content`); **Knowledge Vault** (`entry_type, source, sensitivity∈{low,medium,high}, secret_value`). Eight agents: 6 Memory Managers + Meta Manager + Chat Agent. Hierarchy inside each type (summary/details). |
| **write algo** | Screen capture every **1.5s**; drop visually similar; batch **20 unique** screenshots → update (~60s). Meta Manager routes writes to type-specific managers. Streaming upload to Gemini Cloud URLs (latency ~5s vs ~50s GPT-4 image upload). Core rewrite when size > **90%** capacity. |
| **read algo** | **Active Retrieval**: before answer, agent must generate a *topic*; retrieved memories injected into system prompt. Multiple retrieval tools selectable by situation. Chat constrained to retrieved memories only (no raw transcript) on LoCoMo. |
| **compact/forget** | Abstraction over raw screenshots → 99.9% storage cut vs RAG on ScreenshotVQA. Core controlled rewrite at 90%. Semantic tree organization. |
| **conflict** | Implicit overwrite on semantic; paper notes temporal ambiguity (planned vs actual camping date) causes Single-Hop errors when consolidated event preferred over earlier plan. |
| **privacy** | Local storage in app; Knowledge Vault sensitivity levels + access control; E2E encryption / fine-grained share / decentralized storage described for marketplace vision. Hybrid on-device vault vs cloud Resource. |
| **failure modes** | Active retrieval skipped → parametric hallucination (Twitter CEO example); RAG bottleneck on open-domain; ambiguous temporal questions; routing mistakes across 6 types. |
| **MoDeX impl lessons** | (1) Split L3 kinds: Decision/Fact ≈ Semantic; Episode ≈ Episodic; Runbook ≈ Procedural; Artifact/doc ≈ Resource; secrets ≠ Anchors → sealed Vault with sensitivity. (2) **Active Retrieval gate**: hydrate must emit topic/intent before pack compile — never answer from params alone when memory exists. (3) Core @90% rewrite → L1 WorkingState compaction trigger. (4) Capture cadence for screen/IDE hooks: debounce similar frames; batch ~20 before cognify. (5) Multi-manager routing > single flat fact store for engineering (code vs decision vs secret). |

---

### Card: MemoryAgentBench — Four competencies, incremental inject

| Field | Content |
|-------|---------|
| **id** | 2507.05257 |
| **title** | Evaluating Memory via Incremental Multi-Turn Interactions (MemoryAgentBench) |
| **read status** | FULL (HTML) |
| **representation** | Eval framework, not a store. Competencies: **AR** Accurate Retrieval, **TTL** Test-Time Learning, **LRU** Long-Range Understanding (≥100k), **SF** Selective Forgetting. Agents: Long-Context (FIFO buffer), Simple/Embedding/Structure RAG, Agentic Memory. Protocol: chunks `c_1…c_n` wrapped as user messages with memorize instructions; then questions. |
| **write algo** | N/A (agents under test). Chunk sizes: **512** for SH/MH-Doc, LME(S*), FactConsolidation; **4096** for other tasks and for Mem0/Cognee/Zep/MIRIX. |
| **read algo** | N/A. Agents must answer after incremental absorb. SF prompts: facts indexed by serial numbers; **newer = larger serial**; resolve conflicts by newest. |
| **compact/forget** | SF dataset FactConsolidation from MQUAKE counterfactuals; contexts 6K/32K/64K/262K; SH and MH variants. |
| **conflict** | Explicit SF competency — measure whether later facts win. Empirically hard for current agents. |
| **privacy** | Silent. |
| **failure modes** | Using static long-context benches as memory benches (wrong); RAG top-k fails TTL/LRU; agentic loops still retrieval-bound; reconstructing memory per-question is cost-prohibitive (hence multi-Q per context). |
| **MoDeX impl lessons** | (1) MoDeX eval suite must cover **all four** AR/TTL/LRU/SF — not only LoCoMo-style AR. (2) Inject **incrementally** (multi-turn) matching L0 capture. (3) SF harness: ordered edit pairs + “prefer newer” instruction mirrors SUPERSEDES semantics. (4) Default eval chunk 512 for fact/needle; 4096 for narrative. (5) Multi-question per long context (LME S* pattern) for cost efficiency. |

---

### Card: MemGAS — Multi-granularity association + PPR

| Field | Content |
|-------|---------|
| **id** | 2505.19549 |
| **title** | From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection (MemGAS) |
| **read status** | FULL (HTML) |
| **representation** | Memories at G granularities `M_i^g` with association graph `{M_i, A_i}`. Router assigns granularity weights `w^g`. |
| **write algo** | LLM generates multi-granularity views of sessions; build association edges; Contriever embeddings. |
| **read algo** | `score_i = Σ_g w^g · sim(q, M_i^g)`; top-α seeds → **Personalized PageRank**; top-K by PPR; **LLM redundancy filter** on top-K before generate. Fair compare: top-3 sessions. |
| **compact/forget** | Filter discards redundant/irrelevant retrieved units (not store eviction). |
| **conflict** | Silent at write; selection-time filter only. |
| **privacy** | Silent. |
| **failure modes** | Single-granularity baselines underperform; Full History noise; recursive summary alone weak; graph without multi-granularity limited. |
| **MoDeX impl lessons** | (1) Index same Evidence at multiple granularities (turn / episode / topic summary / anchor statement). (2) Hydrate = weighted multi-granularity sim → PPR expand → LLM filter (recognition memory). (3) Default retrieve top-3 workstream sessions then expand. (4) Router weights `w^g` = learned or heuristic by query type (factual→fine; sense-making→coarse). |

---

### Card: Cognitive Weave — Insight Particles + STRG

| Field | Content |
|-------|---------|
| **id** | 2506.08098 |
| **title** | Cognitive Weave: Synthesizing Abstracted Knowledge with a Spatio-Temporal Resonance Graph |
| **read status** | FULL (HTML) |
| **representation** | **Insight Particles (IP)** as first-class memories; **Spatio-Temporal Resonance Graph (STRG)** with Temporal Index Layer; components: Nexus Weaver (orchestrator), Semantic Oracle Interface, Vectorial Resonator, STRG layers. Emphasizes *insight synthesis* over raw chunk store. |
| **write algo** | Ingest → SOI extract/synthesize IPs → embed via VR → place in STRG with spatial+temporal metadata. Nexus Weaver manages lifecycle. |
| **read algo** | Recall requests → NW chooses strategy over STRG (vectorial resonance + graph + temporal). |
| **compact/forget** | **Cognitive Refinement** cycles (temporal / event / resource / fragmentation triggers); prune/archive low-value IPs; refinement fuses related insights. |
| **conflict** | Refinement merges/updates IPs; temporal first-class (not mere metadata). |
| **privacy** | Silent in core mech. |
| **failure modes** | Flat RAG misses cross-chunk relations; extending raw context ≠ synthesizing insights; refinement thrashing if triggers too aggressive. |
| **MoDeX impl lessons** | (1) L3 Anchors should be *synthesized insights*, not only extracted utterances. (2) Put temporal index as first-class (valid_from/valid_to + event time). (3) Schedule refinement jobs (cognify) on triggers: time, significant write, fragmentation metrics. (4) Resonance/PPR-style retrieval complements embedding top-k. |

---

### Card: SCM — Self-Controlled Memory controller

| Field | Content |
|-------|---------|
| **id** | 2304.13343 |
| **title** | Enhancing Large Language Model with Self-Controlled Memory Framework |
| **read status** | FULL (HTML) |
| **representation** | Memory stream items: `{index, observation, response, summarization, embedding}`. Dual recall: **Activation Memory** (long-term retrieved) + **Flash Memory** (turn T−1). Controller LLM gates use. |
| **write algo** | After response: append interaction; summarize turn (critical when turn >3k tokens); embed concat(obs, resp) via text-embedding-ada-002. |
| **read algo** | Controller Q1: need memory? If yes, rank by `rank = recency + relevance` (cosine); top-k with **k∈[3,10]**. Q2: if activated tokens >**2000** and item >**800** tokens, can summary answer? If yes use summary else full. Fuse via prompt → generate. |
| **compact/forget** | Prefer summaries under token pressure; no hard delete; w/o controller → truncate at 2500 (big multi-turn drop). |
| **conflict** | Silent. |
| **privacy** | turbo refused some privacy probes; davinci answered — model-dependent leakage risk. |
| **failure modes** | Always-on memory injects noise (“tell me a joke”); ablation: remove activation → ~60% accuracy collapse; remove controller → multi-turn −25.6pp. |
| **MoDeX impl lessons** | (1) **Gate hydrate**: cheap controller (or rules) before retrieval — don’t always pull L3. (2) Keep Flash = last turn in L1 always. (3) Summary-vs-full decision at 800/2000 token thresholds. (4) Rank = recency + relevance (start unweighted sum; later learn). (5) k=3–10 band for Evidence inject. |

---

### Card: RET-LLM — Triplet read/write memory API

| Field | Content |
|-------|---------|
| **id** | 2305.14322 |
| **title** | RET-LLM: Towards a General Read-Write Memory for Large Language Models |
| **read status** | FULL (HTML) — concept paper; notes evolution into MemLLM |
| **representation** | Triplets `⟨t1, relation, t2⟩` in 3-column table + mean embeddings in **LSH** for fuzzy match. LLM emits text API: `[MEM_WRITE{t1>>t2>>t3}]`, `[MEM_READ{_>>_>>_}: …]`. Controller mediates user↔LLM↔memory. |
| **write algo** | Informative statement → LLM extracts triplets → controller stores text + AVG hidden reps into LSH table. Supports non-text sources (SQL/spreadsheets) conceptually. |
| **read algo** | Question → LLM emits MEM_READ with partial keys → exact match else LSH fuzzy → return all matching triplets → LLM answers. Query shapes: any 1 or 2 of 3 fields. |
| **compact/forget** | Updatable store for temporal facts; no detailed eviction. |
| **conflict** | Update by rewriting triplets; temporal QA claimed via modifiable memory. |
| **privacy** | Silent. |
| **failure modes** | Extraction errors; LSH false neighbors; concept-paper eval mostly qualitative; finetune required for API discipline. |
| **MoDeX impl lessons** | (1) Structured write path: LLM emits typed ops, executor validates — like MoDeX tool calls for Anchor CRUD. (2) Triplets map to Evidence edges; Anchors hold claims. (3) Exact-then-fuzzy entity resolve. (4) Hide API schema from end-user (controller). |

---

### Card: AIOS — Agent OS kernel (memory + context managers)

| Field | Content |
|-------|---------|
| **id** | 2403.16971 |
| **title** | AIOS: LLM Agent Operating System |
| **read status** | FULL (HTML) |
| **representation** | Layers: Application (SDK) / Kernel (AIOS + OS) / Hardware. Kernel modules: LLM Core(s), Scheduler (FIFO or RR), Context Manager (text or logits snapshot), **Memory Manager** (RAM agent histories), **Storage Manager** (disk + vector DB), Tool Manager, Access Manager (privilege groups). Syscalls thread-bound. |
| **write algo** | Agent memory items in RAM blocks; on exceed **80%** block → LRU-K swap to disk via Storage Manager. Persistent writes also via storage syscalls. |
| **read algo** | Memory/storage syscalls scheduled centrally; vector DB (Chroma) for semantic retrieve from disk-resident memories. |
| **compact/forget** | LRU-K eviction RAM→disk; not semantic forget. Context interrupt frees LLM core without dropping logical agent state. |
| **conflict** | Tool hashmap enforces parallel-access limits; Access Manager blocks cross-privilege R/W. |
| **privacy** | Privilege groups (hashmap agent→group); user intervention gate for delete/overwrite/privilege change. |
| **failure modes** | Unmanaged concurrent agents → CUDA OOM retry storms; monopolizing LLM core; irreversible ops without confirm. |
| **MoDeX impl lessons** | (1) Treat memory ops as **syscalls** with scheduler — MoDeX daemon queues capture/cognify/hydrate. (2) L1 RAM vs L2/L3 disk with **80%** swap trigger + LRU-K. (3) Context snapshot/restore for preemption during long LLM calls. (4) Privilege groups ≈ workstream isolation. (5) User confirm for destructive Anchor deletes. |

---

### Card: HaluMem — Operation-level memory hallucination eval

| Field | Content |
|-------|---------|
| **id** | 2511.03506 |
| **title** | HaluMem: Evaluating Hallucinations in Memory Systems of Agents |
| **read status** | FULL (HTML) |
| **representation** | Benchmark: gold for Extraction `G^ext`, Updating `G^upd = {m_old→m_new}`, QA. Dialogue spans **10–20 years**; avg **8.3k tokens/session**; up to 1M context; ~3.5k–6k Qs. Memory types: Persona, Event, Relationship. |
| **write algo** | N/A (eval). Systems under test perform E/U/R/Q. |
| **read algo** | N/A. Timing: evaluate **after each session**, not only end-to-end. |
| **compact/forget** | Update gold includes modifications/deletes. |
| **conflict** | Update-stage gold catches unresolved conflicts / wrong overwrites. |
| **privacy** | Silent. |
| **failure modes** | End-to-end Acc cannot localize whether E, U, or Q hallucinated; graph memory ↑ expressivity but ↑ hallucination risk; memory hallucination upstream of generation hallucination. |
| **MoDeX impl lessons** | (1) Instrument MoDeX evals at **operation level**: extract precision/recall, update correctness, QA faithfulness separately. (2) Session-boundary grading. (3) Track fabricated / outdated / unresolved-conflict / wrong-retrieval as distinct error codes. (4) Prefer invalidate+audit over opaque merge (reduces update hallucinations). |

---

### Card: Mem-α — RL for memory construction

| Field | Content |
|-------|---------|
| **id** | 2509.25911 |
| **title** | Mem-α: Learning Memory Construction via Reinforcement Learning |
| **read status** | FULL (HTML) |
| **representation** | Agent with **core / episodic / semantic** + tools; trained with RL. Reward = downstream QA accuracy over full history. Train max **30k** tokens; zero-shot generalize to **>400k** (~13×). |
| **write algo** | Process sequential chunks; policy learns extract/store/update via tools (not frozen heuristics). |
| **read algo** | Learned tool use for retrieve during QA. |
| **compact/forget** | Learned via reward — no fixed curve. |
| **conflict** | Implicitly learned through QA reward on conflicting histories. |
| **privacy** | Silent. |
| **failure modes** | Prompt-only memory managers fail on complex architectures; small models confused by long tool schemas; SFT insufficient vs RL. |
| **MoDeX impl lessons** | (1) Phase D+: consider RL/optimize loop for promotion & hydrate policies (agents-cli eval optimize analogue). (2) Reward should be multi-competency (AR+SF), not only EM. (3) Train short, test long — curriculum for MoDeX agents. (4) Tool schemas must stay small for reliability. |

---

### Card: M3-Agent — Multimodal long-term memory agent

| Field | Content |
|-------|---------|
| **id** | 2508.09736 |
| **title** | Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory (M3-Agent) |
| **read status** | FULL (HTML) |
| **representation** | Multimodal agent memory spanning vision/audio/text long-term stores; episodic + semantic style organization for continuous perception. |
| **write algo** | Continuous see/listen → remember pipeline; extract memorable multimodal events into structured memory (details in paper body: memory writing from streams, not single-shot RAG). |
| **read algo** | Remember+reason over retrieved multimodal memories for QA / control. |
| **compact/forget** | Abstraction required — raw video unsustainable (aligns with MIRIX 99.9% cut lesson). |
| **conflict** | Not a primary focus. |
| **privacy** | Continuous capture implies strong redaction need (paper application-facing). |
| **failure modes** | Token blowup if raw frames stored; modality gap in embeddings; temporal alignment errors. |
| **MoDeX impl lessons** | (1) Engineering capture will include screenshots/IDE — store **digests + pointers**, not blobs in L3. (2) Episodic multimodal Evidence with URI to artifact store. (3) Redaction at L0 before cognify (P1). |

---

### Card: Reflexion — Verbal reinforcement memory

| Field | Content |
|-------|---------|
| **id** | 2303.11366 |
| **title** | Reflexion: Language Agents with Verbal Reinforcement Learning |
| **read status** | FULL (HTML) |
| **representation** | Episodic **verbal reflections** (natural language) stored in memory buffer; no weight updates. Actor / Evaluator / Self-Reflection roles. |
| **write algo** | After trajectory + score: generate reflection text; append to memory for next trial. |
| **read algo** | Reflections prepended/injected into next Actor prompt. |
| **compact/forget** | Buffer of recent reflections; not long-term KB. |
| **conflict** | Newer reflections implicitly dominate via prompt order. |
| **privacy** | Silent. |
| **failure modes** | Reflection noise; binary rewards weak; not a substitute for structured world memory. |
| **MoDeX impl lessons** | (1) Store failure reflections as L2 Episode kind=`reflection` linked to failed run — don’t mix into L3 facts. (2) Use for agent self-improve loops, not engineering truth. |

---

### Card: Voyager — Skill library curriculum

| Field | Content |
|-------|---------|
| **id** | 2305.16291 |
| **title** | Voyager: An Open-Ended Embodied Agent with Large Language Models |
| **read status** | FULL (HTML) |
| **representation** | **Skill library** of executable code indexed by embedding; automatic curriculum; iterative prompting with environment feedback. |
| **write algo** | When skill succeeds → store code + description embedding; grow library. |
| **read algo** | Query skill library by embedding for relevant skills to compose. |
| **compact/forget** | Skills persist; curriculum proposes novel tasks. |
| **conflict** | Newer skill versions replace by retrieval ranking / manual. |
| **privacy** | Silent. |
| **failure modes** | Skill staleness; retrieval of near-miss skills; environment-specific. |
| **MoDeX impl lessons** | (1) Procedural Anchors / runbooks ≈ skill library with embedding index. (2) Curriculum signal ≈ workstream “next novelty” for exploration agents. (3) Keep code skills as Resource+Procedural, not Semantic facts. |

---

### Card: Self-RAG — Reflection tokens for retrieve/critique

| Field | Content |
|-------|---------|
| **id** | 2310.11511 |
| **title** | Self-RAG: Self-reflective Retrieval-Augmented Generation |
| **read status** | FULL (HTML) |
| **representation** | End-to-end trained model emits **reflection tokens**: Retrieve / Relevance / Grounding / Utility critiques interleaved with generation. |
| **write algo** | N/A external store — trains when to retrieve. |
| **read algo** | On-demand retrieve if `Retrieve=Yes`; critique passages; continue or refine. |
| **compact/forget** | N/A. |
| **conflict** | Critique can discard irrelevant/contradictory passages at generate time. |
| **privacy** | Silent. |
| **failure modes** | Always-retrieve waste; ungrounded generation without critique. |
| **MoDeX impl lessons** | (1) Hydrate planner should emit Retrieve? gate (SCM + Self-RAG). (2) Per-Evidence grades: relevance / support / utility before pack include. (3) Train or prompt critique tokens in L4 compile. |

---

### Card: StreamingLLM — Attention sinks + rolling KV

| Field | Content |
|-------|---------|
| **id** | 2309.17453 |
| **title** | Efficient Streaming Language Models with Attention Sinks |
| **read status** | FULL (HTML) |
| **representation** | KV cache = **4 initial sink tokens** + rolling recent window. Positions rebased **within cache**, not original text positions (critical for RoPE/ALiBi). |
| **write algo** | Decode: append KV; if full, evict oldest *non-sink* tokens; keep sinks. |
| **read algo** | Attention over sinks+window only; enables 4M+ tokens streaming. |
| **compact/forget** | Evict middle history from KV (not external memory). Prefers sinks=4; 1–2 insufficient for vanilla models. |
| **conflict** | N/A. |
| **privacy** | Silent. |
| **failure modes** | Window attention without sinks → perplexity explosion; increasing cache ≠ always better perplexity (under-utilization); does **not** extend true long-term memory — only streaming local context. |
| **MoDeX impl lessons** | (1) L1 working KV / prompt prefix: pin **system+sink/bootstrap tokens**; roll conversation. (2) Don’t confuse StreamingLLM with L3 memory — still need external MoDeX store. (3) Position rebasement rule if implementing custom KV. (4) Cache size ablation: measure task metric, not assume bigger=better. |

---

### Card: MemAgent — RL overwrite memory over chunks

| Field | Content |
|-------|---------|
| **id** | 2507.02259 |
| **title** | MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent |
| **read status** | FULL (HTML) |
| **representation** | Fixed-size **memory token block** updated by **overwrite** while scanning document chunks; DAPO/multi-conv RL optimizes end-to-end. |
| **write algo** | For each chunk: read chunk + current memory → write new memory (overwrite strategy). Extrapolate 8K train → 3.5M QA with <10% loss; >95% on 512K NIAH. |
| **read algo** | Final answer from memory state after all chunks. |
| **compact/forget** | Overwrite *is* the compaction — constant memory size. |
| **conflict** | Last write wins inside memory buffer; RL must learn to preserve still-needed facts. |
| **privacy** | Silent. |
| **failure modes** | Overwrite erases unreinforced facts; naive length-extrapolation baselines collapse; O(n²) full context still bad. |
| **MoDeX impl lessons** | (1) L1 WorkingState can be a **fixed budget overwritten summary** while scanning L0 — but persist survivors to L2/L3 *before* overwrite. (2) RL overwrite alone insufficient for auditability — pair with append-only Evidence. (3) Multi-conversation independent contexts useful for training cognify policies. |

---

### Card: Memory-R1 — RL ADD/UPDATE/DELETE/NOOP

| Field | Content |
|-------|---------|
| **id** | 2508.19828 |
| **title** | Memory-R1: Enhancing LLM Agents to Manage and Utilize Memories via Reinforcement Learning |
| **read status** | FULL (HTML) |
| **representation** | Memory Manager policy π outputs `{ADD, UPDATE, DELETE, NOOP}` + content; Answer Agent distills from **60** retrieved memories. PPO/GRPO; only **152** train QA pairs. |
| **write algo** | Extract candidate → retrieve related → RL chooses op. Vanilla heuristic often DELETE+ADD on non-contradictions; RL learns UPDATE consolidate (dog adoption example). |
| **read algo** | Retrieve 60 → distillation policy → answer. Reward = EM(answer). |
| **compact/forget** | DELETE as learned op; NOOP avoids junk. |
| **conflict** | UPDATE vs DELETE+ADD is the key learned distinction; outcome reward shapes correct consolidation. |
| **privacy** | Silent. |
| **failure modes** | Heuristic managers fragment memory; SFT weaker than RL; distillation needed because top-60 is noisy. |
| **MoDeX impl lessons** | (1) Anchor write head should support explicit ops: ADD / SUPERSEDES(update) / RETRACT(delete) / NOOP. (2) Prefer UPDATE/SUPERSEDES over DELETE+ADD. (3) Hydrate distillation step after retrieve (60→few). (4) Outcome-based reward for promotion policy experiments. |

---

### Card: LightMem — Sensory / topic-STM / sleep-time LTM

| Field | Content |
|-------|---------|
| **id** | 2510.18866 |
| **title** | LightMem: Lightweight and Efficient Memory-Augmented Generation |
| **read status** | FULL (HTML) |
| **representation** | Atkinson–Shiffrin inspired: **Light1 sensory** (LLMLingua-2 / entropy retain, topic seg), **Light2 topic-aware STM** buffer, **Light3 LTM** with soft insert + **sleep-time** offline parallel update. Entry: `{topic, emb(sum), user, model}`. |
| **write algo** | Pre-compress tokens with retain prob > percentile τ(r); topic-segment; buffer until token threshold `th`; summarize → soft-insert LTM with timestamp. Offline: for each entry build update queue `Top_k` later similar entries (`t_j≥t_i`) length n; parallel `f_update`. |
| **read algo** | Topic-constrained retrieval over LTM summaries (fewer API calls, less topic mix). |
| **compact/forget** | Compression ratio r; sleep-time dedupe/abstract; offline parallel updates cut sequential latency. |
| **conflict** | Only later memories update earlier (temporal monotonic); queue-based consolidation. |
| **privacy** | Silent. |
| **failure modes** | Turn/session granularity without topics → mix + more API calls; online sequential updates dominate latency. |
| **MoDeX impl lessons** | (1) L0→L1: cheap compress+topic seg before LLM cognify. (2) **Sleep-time cognify** job queue decoupled from IDE latency path. (3) Soft-insert then offline reconcile = append Evidence then batch promote Anchors. (4) Enforce `t_new ≥ t_old` for update direction. (5) Tune `r` (compression) and `th` (STM flush tokens) as Phase A knobs. |

---

### Card: LoCoMo — Long-term conversational memory eval

| Field | Content |
|-------|---------|
| **id** | 2402.17753 |
| **title** | Evaluating Very Long-Term Conversational Memory of LLM Agents |
| **read status** | FULL (HTML) |
| **representation** | Benchmark: ultra-long multi-session dialogues (~300 turns, ~9k tokens/conversation in MemoryOS citing; Memory-R1 cites ~600 turns / 26k). QA types: single-hop, multi-hop, temporal, open-domain (+ adversarial). |
| **write/read/forget** | N/A — evaluation dataset & human/agent conversation collection methodology. |
| **conflict** | Temporal & multi-hop questions stress inconsistency. |
| **privacy** | Persona dialogues may include personal facts — eval hygiene needed. |
| **failure modes** | Short-context agents fail temporal/multi-hop; summarization baselines lose specifics; adversarial subset. |
| **MoDeX impl lessons** | (1) Use LoCoMo-style splits as smoke eval for hydrate. (2) Track metrics per question type separately. (3) Exclude or separately score adversarial. |

---

### Card: MemBench — Broader memory agent eval taxonomy

| Field | Content |
|-------|---------|
| **id** | 2506.21605 |
| **title** | MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents |
| **read status** | FULL (HTML) |
| **representation** | Benchmark taxonomy covering more dimensions of agent memory than single QA suites (factual / preference / multi-turn / update — per paper design). |
| **write/read** | Eval harness for agent memory modules. |
| **conflict / forget** | Includes update-oriented tests (complementary to HaluMem/MemoryAgentBench). |
| **privacy** | Silent. |
| **failure modes** | Narrow benches overstate memory quality. |
| **MoDeX impl lessons** | (1) Don’t rely on one bench — combine LoCoMo + MemoryAgentBench + HaluMem + MemBench dimensions. (2) Map each MoDeX pillar to at least one metric family. |

---

### Card: G-Memory — Hierarchical MAS memory

| Field | Content |
|-------|---------|
| **id** | 2506.07398 |
| **title** | G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems |
| **read status** | FULL (PDF via pdftotext; HTML conversion failed) |
| **representation** | Hierarchical, agentic memory for **multi-agent systems**, inspired by organizational memory; addresses missing inter-agent collaboration trajectories & cross-trial / agent-specific customization. |
| **write algo** | Trace collaboration trajectories into hierarchical stores (insight/query layers — organizational metaphors); agent-specific + shared tiers. |
| **read algo** | Hierarchical query over MAS interaction traces for downstream tasks. |
| **compact/forget** | Hierarchy abstracts low-level traces upward (organizational memory pattern). |
| **conflict** | Cross-agent memory customization vs shared — design tension. |
| **privacy** | Implied need for agent-specific vs shared partitions. |
| **failure modes** | MAS memory that only logs flat transcripts; no cross-trial learning; single-agent memory transplanted naively. |
| **MoDeX impl lessons** | (1) Workstreams ≈ agent-specific memory partitions; shared graph is separate tier. (2) Persist collaboration trajectories (who decided what) as L2 with actor field (MIRIX-like). (3) Cross-trial insights elevate to L3 only with provenance of contributing agents. |

---

### Card: Think-in-Memory (TiM) — Store thoughts, not re-reason

| Field | Content |
|-------|---------|
| **id** | 2311.08719 |
| **title** | Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory |
| **read status** | FULL (PDF via pdftotext) |
| **representation** | Stores **thoughts** (reasoning outcomes) rather than raw dialogue; LSH retrieval; ops: **insert / forget / merge**; post-thinking after recall. |
| **write algo** | After reasoning: insert thought; optionally merge similar; forget low-value (prompts for forget/merge). |
| **read algo** | LSH recall relevant thoughts → answer without re-deriving full chain; post-thinking may refine stored thought. |
| **compact/forget** | Explicit forget + merge to cut redundant reasoning. |
| **conflict** | Merge reconciles related thoughts; avoids inconsistent re-thinking of same history. |
| **privacy** | Silent. |
| **failure modes** | Repeated recall-reason → biased inconsistent thoughts (motivation); merge errors. |
| **MoDeX impl lessons** | (1) Cache **reasoning artifacts** (design rationales) as L2/L3 linked to Evidence — don’t re-derive every hydrate. (2) Provide merge/forget tools with audit. (3) LSH/ANN index for thought retrieval. |

---

### Card: HEMA — Compact + Vector dual memory

| Field | Content |
|-------|---------|
| **id** | 2504.16754 |
| **title** | HEMA: A Hippocampus-Inspired Extended Memory Architecture for Long-Context AI Conversations |
| **read status** | FULL (PDF via pdftotext; HTML was abstract-only) |
| **representation** | **Compact Memory**: continuously updated **one-sentence** global summary. **Vector Memory**: episodic chunk embeddings, cosine retrieval. Keeps prompt **<3.5k** tokens for **>300-turn** dialogues on 6B model. |
| **write algo** | Each turn: update one-sentence compact; embed+index chunk into vector store. |
| **read algo** | Always include Compact; retrieve Vector top chunks by cosine. With 10K chunks: **P@5≥0.80**, **R@50≥0.74**. |
| **compact/forget** | **Semantic forgetting**: age-weighted prune low-salience → **−34% latency**, **<2pp recall loss**. Two-level **summary-of-summaries** prevents cascade errors after **~1000 turns**. |
| **conflict** | Compact may lag / erase specifics if not backed by Vector. |
| **privacy** | Claims privacy-aware path (local external memory, no retrain). |
| **failure modes** | Summarization-only halves PR AUC; cascade summary errors at 1k+ turns without hierarchy. |
| **MoDeX impl lessons** | (1) L1 = one-line (or short) WorkingState always in prompt. (2) L2 chunks always backing Compact — never summary-only truth. (3) Age-weighted prune for cold Evidence. (4) Hierarchical summaries (RecursiveSum lesson) at L2 chapter level. (5) Hard prompt budget ~3.5k for small models as baseline pack size. |

---

### Card: Lost in the Middle — Position bias

| Field | Content |
|-------|---------|
| **id** | 2307.03172 |
| **title** | Lost in the Middle: How Language Models Use Long Contexts |
| **read status** | FULL (PDF via pdftotext) |
| **representation** | Empirical study: multi-doc QA + KV retrieval; performance U-shaped in position of relevant info. |
| **write** | N/A |
| **read algo** | Models best use info at **beginning or end** of context; middle degrades sharply; even 100k windows underuse middle. |
| **compact/forget** | N/A |
| **conflict** | N/A |
| **privacy** | Silent |
| **failure modes** | Stuffing long packs without position control; assuming longer context fixes memory. |
| **MoDeX impl lessons** | (1) L4 pack order: **critical Anchors at start AND end** (sandwich); Evidence bulk in middle only if necessary. (2) Keep hydrate packs short; prefer ranked few. (3) Never rely on “model will find it in 128k”. |

---

### Card: Recursive Summarizing — Hierarchical book summary

| Field | Content |
|-------|---------|
| **id** | 2109.10862 |
| **title** | Recursively Summarizing Books with Human Feedback |
| **read status** | FULL (PDF via pdftotext) |
| **representation** | Tree of summaries: fixed chunking → leaf summaries → recursive summarize children → book summary. BC + RL from human preferences. |
| **write algo** | Fixed (not learned) chunker; summarize leaves; concatenate child summaries as input to parent task; optional prior-summary context for continuity. |
| **read algo** | Root summary + ability to trace leaf evidence for facts. |
| **compact/forget** | Tree *is* compaction; RL > BC for quality given labels. |
| **conflict** | Labelers judge accuracy/coverage/coherence; contradictions surface in accuracy checks. |
| **privacy** | Silent. |
| **failure modes** | Bad chunk boundaries hurt; leaf errors cascade (HEMA also notes); BC plateaus vs RL. |
| **MoDeX impl lessons** | (1) L2 chapter digests via recursive summarize over episode tree. (2) Keep leaf Evidence pointers for citations. (3) Prefer preference/eval optimize over pure supervised summary prompts for cognify quality. |

---

### Card: MemGPT — OS paging for context (P1 cross-ref)

| Field | Content |
|-------|---------|
| **id** | 2310.08560 |
| **title** | MemGPT: Towards LLMs as Operating Systems |
| **read status** | FULL (HTML) — included for capture/working constants |
| **representation** | Main context = system instructions + **working context** (RW facts) + **FIFO queue** (messages + recursive summary at index 0). External = recall DB + archival DB. Self-directed function calls move data. |
| **write algo** | Queue manager appends messages; at **warning ≈70%** context insert memory-pressure system message; at **flush ≈100%** evict ≈**50%** queue, recompute recursive summary; LLM may `core_memory_append/replace` or archival insert during warning window. |
| **read algo** | Search recall/archival via functions; pagination to avoid overflow; results appended to queue. Function chaining with optional yield. |
| **compact/forget** | Recursive summary of evicted; working context fixed-size; archival unbounded. |
| **conflict** | Working context replaces via functions; no bi-temporal. |
| **privacy** | Silent. |
| **failure modes** | Flat FIFO topic mix (MemoryOS critique); weak base models fail function calling; pagination abandon early. |
| **MoDeX impl lessons** | (1) L1 dual: WorkingState block + rolling queue. (2) Pressure warnings at 70% before hard flush. (3) Evict half, not all — retain recent. (4) Recursive summary at queue head. (5) Paginate hydrate tool results. |

---

## 2. Cross-cutting implementation constants (MoDeX Phase A–E)

Recommended starting numbers synthesized from FULL reads above. Treat as **defaults to tune**, not laws. Phase mapping: **A** capture/L0–L1, **B** cognify/L2, **C** anchors/L3, **D** conflict+hydrate/L4, **E** privacy/seal+eval harden.

### 2.1 Capture & working (Phase A)

| Constant | Value | Sources |
|----------|-------|---------|
| STM / working queue policy | FIFO pages `{event, ts, meta}` | MemoryOS, MemGPT |
| Memory-pressure warning | **70%** of context budget | MemGPT |
| Hard flush | **100%** → evict **~50%** oldest non-pinned | MemGPT |
| RAM→disk swap trigger | **80%** of L1 block | AIOS |
| Core / WorkingState rewrite | at **90%** capacity | MIRIX |
| Prompt working budget (small models) | **≤3.5k** tokens incl. compact+retrieved | HEMA |
| Attention sinks pinned | **4** prefix tokens (or 1 dedicated sink if trained) | StreamingLLM |
| Flash / last-turn always kept | 1 turn | SCM |
| Screen/IDE capture debounce | **1.5s** sample; drop near-duplicates; cognify batch **~20** | MIRIX |
| Sensory compress | LLMLingua-2 / entropy retain; tune ratio `r` | LightMem |
| Topic STM flush threshold `th` | tokens budget before summarize (tune; paper uses explicit `th`) | LightMem |
| Controller: skip memory? | yes for chitchat | SCM |
| Summary-vs-full gate | item>**800** tok & activated total>**2000** | SCM |

### 2.2 Episode / cognify (Phase B)

| Constant | Value | Sources |
|----------|-------|---------|
| Segment join threshold θ | **0.6** (cos + Jaccard) | MemoryOS |
| Heat promote to persona/L3 τ | **5** | MemoryOS |
| Recency μ | **1e7** seconds | MemoryOS |
| MTM page top-k | **10** (sweet spot; 5–40 tested) | MemoryOS |
| Chunk sizes for ingest/eval | **512** (fact/needle), **4096** (narrative) | MemoryAgentBench |
| Sleep-time / offline consolidate | batch after soft-insert; parallel update queues | LightMem |
| Refinement triggers | time / significant event / fragmentation | Cognitive Weave |
| Hierarchical summary | 2-level summary-of-summaries beyond ~**1000** turns | HEMA, RecursiveSum |
| Thought ops | insert / merge / forget | TiM |

### 2.3 Anchors / graph (Phase C)

| Constant | Value | Sources |
|----------|-------|---------|
| Atomic unit metadata | provenance ID, origin, semantic type, timestamps, permissions | MemOS MemCube |
| Lifecycle FSM | Generated→Activated→Merged→Archived→Expired | MemOS |
| Write ops vocabulary | ADD / UPDATE(SUPERSEDES) / DELETE(RETRACT) / NOOP | Memory-R1 |
| Prefer | UPDATE/SUPERSEDES **over** DELETE+ADD | Memory-R1 |
| Multi-granularity index | turn + episode + topic + anchor statement | MemGAS |
| Association retrieve | multi-granularity score → PPR → LLM filter | MemGAS, HippoRAG lineage |
| Triplet/Evidence store | exact match then LSH/ANN fuzzy | RET-LLM, TiM |
| Persona/KB queue size | **100** FIFO (if using queues) | MemoryOS |
| Trait dims (optional) | 90 (MemoryOS) — MoDeX should prefer typed Anchors over opaque vectors | MemoryOS |
| Skill/procedural library | embedding-indexed code/runbooks | Voyager, MIRIX Procedural |

### 2.4 Conflict / hydrate / compose (Phase D)

| Constant | Value | Sources |
|----------|-------|---------|
| Conflict resolution default | **newer wins** with audit (serial/time) | MemoryAgentBench SF, LightMem `t_j≥t_i` |
| Bi-temporal | event time vs ingest time | MemOS, Cognitive Weave, Zep lineage |
| Retrieve width then distill | retrieve **~60** → distill to few | Memory-R1 |
| Activation memory top-k | **3–10** | SCM |
| LPM-like KB top-k | **10** | MemoryOS |
| Session retrieve | top-**3** | MemGAS fair setting |
| Active retrieval | force topic/intent before answer | MIRIX |
| Retrieve? critique tokens | Self-RAG-style gate + relevance/support | Self-RAG, SCM |
| Pack position | critical items at **start and end** | Lost in the Middle |
| Evict L2 by heat | αN_visit+βL+γR_recency | MemoryOS |
| Semantic age-prune | −34% latency budget, <2pp recall ok | HEMA |

### 2.5 Privacy / seal / eval (Phase E)

| Constant | Value | Sources |
|----------|-------|---------|
| Sensitivity tiers | low / medium / high; high excluded from casual retrieve | MIRIX Vault |
| Privilege groups | agent/workstream hashmap ACL | AIOS |
| Destructive ops | require user confirm | AIOS |
| Secrets | separate Vault, not L3 Anchors | MIRIX |
| Eval competencies | AR, TTL, LRU, SF | MemoryAgentBench |
| Hallucination stages | Extraction / Update / QA separately | HaluMem |
| Session-level grading | after each session | HaluMem |
| Primary conversational bench | LoCoMo (+ LongMemEval) | LoCoMo, many systems |
| Broad taxonomy | MemBench dimensions | MemBench |
| RL optimize memory policies | after heuristic baseline; small train set can transfer | Memory-R1 (152 QA), Mem-α, MemAgent |

### 2.6 Anti-patterns (do not copy)

1. **Summary-only truth** (HEMA ablation) — always keep Evidence.  
2. **Flat FIFO as sole long-term store** (MemoryOS critique of MemGPT).  
3. **In-place trait/note rewrite without SUPERSEDES** (MemoryOS LPM, A-MEM evolution).  
4. **Always-on retrieval** (SCM noise; Self-RAG waste).  
5. **End-to-end-only memory metrics** (HaluMem).  
6. **Assuming long context = memory** (MemoryAgentBench, Lost in the Middle).  
7. **DELETE+ADD on non-contradictions** (Memory-R1).  
8. **Raw multimodal blobs in hot path** (MIRIX/M3-Agent efficiency lesson).

---

## 3. MoDeX phase checklist (from this batch)

| Phase | Ship from this batch |
|-------|----------------------|
| **A** | L0 pages + chain meta; L1 WorkingState+FIFO; 70/100% pressure; 80% swap; sinks/pinned prefix; compress+topic seg; controller gate |
| **B** | θ=0.6 segments; heat; sleep-time cognify; recursive chapter digests; thought insert/merge |
| **C** | MemCube-like metadata; ADD/UPDATE/RETRACT/NOOP; multi-granularity+PPR; Vault vs Anchors |
| **D** | Active retrieval; distill after wide retrieve; pack sandwich; SF newer-wins+audit |
| **E** | ACL groups; sensitivity; HaluMem-style op metrics; AR/TTL/LRU/SF suite |

---

*End of batch cards. Companion: `P1_CAPTURE_WORKING.md`.*
