# Agent Memory Corpus Deep-Read — Batch 3 (MoDeX)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/memory-architecture-spec-2e45`  
> **Scope:** Priority FULL-read queue after Batch 1 + Batch 2 + P5 hydrate pass.  
> **Method:** Full arXiv HTML or PDF body text fetched and read (not abstract-only). Honesty marks below.  
> **MoDeX lens:** Anchors+Evidence, L0–L4, SUPERSEDES/CONTRADICTS, workstreams, promotion/privacy, sealed handoff, procedural vs belief memory.

---

## 0. Honesty about coverage (this batch)

| Status | Papers |
|--------|--------|
| **FULL deep-read (new to corpus memos)** | LTM Self-Evolution (2410.15665); LLM Agents Survey memory §§ (2309.07864); Memento (2508.16153); MemoryBench (2510.17281); ReasoningBank (2509.25140); MEM1 (2506.15841); LEGOMem (2510.04851); Memory-as-Action / MemAct (2510.12635); O-Mem (2511.13593); Agent KB (2507.06229); H-Mem (2605.15701); MemoChat (2308.08239); DialSim (2406.13144); Memory-as-a-Tool (2601.05960); Sleep-Consolidated Memory (2604.20943) |
| **FULL re-read extras** (already FULL in P2 ledger; Batch 3 adds mechanism-card depth) | MemoryBank (2305.10250); SCM Self-Controlled Memory (2304.13343); Think-in-Memory (2311.08719) |
| **Already FULL elsewhere — not re-counted as Batch 3 FULL** | AssoMem (2510.10397); RCR-Router (2508.04903); RAPTOR (2401.18059); PropRAG (2504.18070); Adaptive-RAG (2403.14403); LongMemEval (2410.10813) — cards in `impl/P5_HYDRATE_RETRIEVE.md` |
| **Survey re-extract (already FULL inventory)** | From Storage to Experience (2605.06716) — Experience-stage notes in §2 only |
| **Skipped as not memory-system primary** | LongRoPE (2402.13753) — context-window extension only |
| **Not found as arXiv papers** | MemU / Memobase product names — no matching primary papers in arXiv search this pass |

**Count of new FULL deep-reads this batch:** **15** primary texts (+ **3** FULL re-read extras with Batch-3 mechanism cards).

**Do not invent:** Where a paper is silent (privacy model, typed SUPERSEDES, multi-principal ACL), that silence is recorded. Reported numbers are from the papers’ own tables/text.

---

## 1. Per-paper deep extracts

### 1.1 Long Term Memory: The Foundation of AI Self-Evolution  
**arXiv:2410.15665** · 2024 · **FULL-READ** (HTML)

**Problem setup.** Scaling data/params alone is insufficient for open-ended self-evolution; systems need **long-term memory (LTM)** that accumulates interaction-derived knowledge and feeds back into behavior (and optionally parameters).

**Memory representation.** Survey frames LTM as: (i) **outside knowledge bases** (retrieve/store/encode), (ii) **parametric compressed memory** (weights), (iii) **mixed** strategies (fine-tune retrieval / augmentation / generation stages). Contrasts prompting-as-memory vs parametric compression; draws human LTM inspiration (encoding, consolidation, retrieval).

**Write / read / forget.** Construction path: raw interaction data → collection/synthesis → LTM construction strategies → use via RAG-style external store, parameter updates, or hybrids. Forget/consolidation discussed at survey level (sleep-like consolidation, selective retention) without a single operator algebra.

**Compaction.** Parametric compression + summary/indexing of raw→LTM; hierarchical construction strategies.

**Conflict / supersession.** Not a first-class ConflictSet design; conflict appears as knowledge update / continual-learning tension.

**Privacy / sharing.** Mentions multi-agent collaboration + differentiated personalized models as self-evolution dependencies; no capability/ACL model.

**MoDeX design lessons (6):**
1. Treat LTM as **foundation of self-evolution**, not a chat accessory — aligns with MoDeX L3 Anchors as Experience-class store.
2. Keep **external structured store + optional later parametric** paths separate (MoDeX v1 = outside KB; no weight updates).
3. Mixed strategy taxonomy (retrieve-stage / augment-stage / generate-stage fine-tune) maps to hydrate vs cognify vs future learned rankers.
4. Multi-agent + personalized models as LTM consumers → workstream facets + sealed packs.
5. Self-correction loops need memory of **failures**, not only successes (ties to ReasoningBank / Memento).
6. Survey-level only on conflict — do not import vague “update memory” language into SUPERSEDES.

---

### 1.2 The Rise and Potential of LLM-Based Agents (Survey) — memory sections  
**arXiv:2309.07864** · Xi et al. · 2023 · **FULL-READ** (PDF; focus §3.1.3 Memory + bibliography map)

**Problem setup.** Early comprehensive LLM-agent survey; memory is one brain/module pillar beside perception, reasoning/planning, action.

**Memory representation (§3.1.3).** Memory stores sequences of observations, thoughts, actions. Enhancement methods catalogued as:
- **Summarizing memory** (daily/global hierarchical summaries; textual encapsulations of feedback).
- **Compressing with vectors/structures** (embeddings; triplets; memory-as-object; SQL stores — ChatDB/DB-GPT).
Retrieval: automated scoring with **Recency + Relevance + Importance** (Generative Agents lineage). Interactive memory objects allow human edit/delete/combine; command-based deletion (ChatDB).

**Write / read / forget.** Write = append/summarize/embed; read = scored retrieve into context; forget = user-command delete or object edit — **not** typed invalidation.

**Compaction.** Summarization + vector compression + hierarchical daily→global.

**Conflict / supersession.** Silent as typed belief revision; “update” via rewrite/summarize.

**Privacy / sharing.** Not a privacy paper; multi-agent communication retention noted.

**Bibliography map (memory-relevant seeds for MoDeX):** Generative Agents [22] scoring; MemoryBank / SiliconFriend lineage [170]; ChatDB [175]; Memory Sandbox [176]; Reflexion / Voyager cited elsewhere in survey for feedback and skill libraries; summarization + embedding retrieval cluster [109; 172–174].

**MoDeX design lessons (5):**
1. Confirms MoDeX hydrate score ancestors: **recency × relevance × importance**.
2. Hierarchical daily→global summaries ≈ episode digests → workstream themes (do not replace Anchors).
3. Memory-as-editable-object foreshadows Evidence/Anchor audit UX — but MoDeX edits must be capability-gated.
4. SQL/command delete is unsafe for eng truth — map to SUPERSEDES+archive.
5. Use this survey as **citation map**, not as architecture authority over later 2025–26 memory systems.

---

### 1.3 Memento — Fine-tuning LLM Agents without Fine-tuning LLMs  
**arXiv:2508.16153** · Zhou, Chen, Guo, Yan et al. · 2025 · **FULL-READ** (HTML)

**Problem setup.** Agents are either rigid handcrafted reflection workflows or expensive LLM fine-tunes; need continual adaptation **without** gradient updates to the base LLM.

**Memory representation.** **Memory-augmented MDP (M-MDP)** with episodic **case bank** \(M_t\) of tuples \((s_t,a_t,r_t)\). State encoded with frozen text encoder; actions/rewards stored raw. Two retrieval modes:
- **Non-parametric CBR:** \(\mathrm{Read}_{NP}=\mathrm{TopK}\) by cosine \(\mathrm{sim}(\mathrm{enc}(s_t),\mathrm{enc}(s_i))\).
- **Parametric:** online-updated Q-function \(Q(s,c;\theta)\) shapes case selection; single-step supervised loss \(\mathcal{L}=\mathbb{E}[(Q(s,c;\theta)-r)^2]\).

**Write / read / forget.** Write appends cases after each step (successes **and** failures). Read retrieves K similar cases to condition planning. No bi-temporal expire; growth is online case bank. Soft Q-learning / CBR policy over cases.

**Compaction.** Implicit via TopK retrieval; not hierarchical summarization.

**Conflict / supersession.** Cases coexist; selection by similarity/Q — no SUPERSEDES of beliefs.

**Privacy / sharing.** None (deep-research agent setting).

**Reported results (paper):** GAIA val Pass@3 **87.88%**, test **79.40%**; DeepResearcher F1 **66.6%** / PM **80.4%**; case memory adds **+4.7–9.6** abs. pts on OOD tasks.

**MoDeX design lessons (7):**
1. Store **failure cases**, not only wins — eng Anchors should include “what broke / what not to do”.
2. Case = (state, action, reward) ≈ Evidence trajectory + outcome label; separate from durable decision Anchors.
3. Non-parametric CBR is MoDeX-v1-friendly (embed + TopK); parametric Q-retrieval is Phase F+.
4. Continual learning via **memory rewrite/read** beats base-model fine-tune for local-first agents.
5. Reward-labeled cases must not silently overwrite sealed eng constraints.
6. Deep-research tool traces are procedural Experience — candidate for Voyager-like skill library, not persona KB.
7. OOD gains from case memory argue for cross-session promotion of high-utility failure lessons.

---

### 1.4 MemoryBench — Memory & Continual Learning for LLM Systems  
**arXiv:2510.17281** · Ai, Tang, Wang, Long, Su, Liu · 2025/2026 · **FULL-READ** (PDF)

**Problem setup.** Existing memory benches over-focus long-form reading QA; miss **continual learning from accumulated user feedback at service time**.

**Memory representation.** Not a memory system — a **benchmark + user-feedback simulation framework**. Hybrid simulator: LLM-as-user + two-stage programmable action simulator; verifiable tasks map scores → explicit/implicit feedback templates. Domains: open-domain, **legal**, **academic**; multilingual; reuses/extends datasets including LoCoMo, DialSim, LexEval, JuDGE, IdeaBench, writing benches, etc.

**Write / read / forget.** Evaluates LLMsys memory processors that ingest conversations + feedback and later improve predictions. Metrics include effectiveness **and** efficiency (memory-op time vs predict time). Stresses filtering/utilizing feedback — papers report SOTA baselines far from satisfying.

**Compaction / conflict / privacy.** Bench can inject irrelevant memory (noise robustness). Not a privacy IFC suite. Conflict appears as feedback-driven knowledge updates over streams.

**MoDeX design lessons (6):**
1. MoDeX eval must include **feedback→memory→later-task** loops, not only static recall QA.
2. Legal/academic partitions are closer to eng-doc workflows than pure persona chat.
3. Measure **memory maintenance latency** separately (LightMem lesson reinforced).
4. Noise-injection slices = Inv-Scope / wrong-workstream hydrate tests.
5. Do not treat LoCoMo alone as sufficient continual-learning proof.
6. Offline released feedback logs enable regression harnesses without live users.

---

### 1.5 ReasoningBank — Scaling Agent Self-Evolving with Reasoning Memory  
**arXiv:2509.25140** · Ouyang, Yan, Hsu, Chen et al. (Google) · 2025 · **FULL-READ** (HTML)

**Problem setup.** Persistent agents discard cross-task insights; prior memory stores raw trajectories or **success-only** routines, missing transferable reasoning and failure lessons.

**Memory representation.** **ReasoningBank** items = distilled **generalizable reasoning strategies** / actionable principles from self-judged successes **and** failures (no ground-truth labels required). Closed loop: retrieve → act → distill/consolidate back. **MaTTS** (memory-aware test-time scaling): parallel/sequential extra exploration per task yields contrastive signals for higher-quality memory.

**Write / read / forget.** Write = LLM distill of experience into strategy items; read = retrieve relevant strategies for new task; consolidation continuous. Not typed DELETE; quality via contrastive synthesis under MaTTS.

**Compaction.** Distillation from raw trajectory → strategy principles (lossy by design).

**Conflict / supersession.** Failures become preventative lessons; no explicit ConflictSet — strategies may accumulate contradictions unless distillation merges them.

**Privacy / sharing.** None.

**MoDeX design lessons (7):**
1. Promote **strategy Anchors** (how we reason) separate from **fact/decision Anchors**.
2. **Failure distillation** is first-class — matches eng postmortems.
3. Self-judge without labels is useful but risky for safety — MoDeX needs human/CI verification before shareable facet.
4. MaTTS ≈ spend more explore compute when forming L3 promotions (offline cognify budget).
5. Prefer strategies over raw trajectory dumps in L4 packs.
6. Emergent self-evolution claims are chat/web/SWE bench signals — verify on eng fixtures.
7. Contrastive multi-rollout memory synthesis is a cognify job, not a hot-path hook.

---

### 1.6 MEM1 — Synergize Memory and Reasoning for Efficient Long-Horizon Agents  
**arXiv:2506.15841** · Zhou, Qu, Wu et al. · 2025 · **FULL-READ** (HTML)

**Problem setup.** Full-context multi-turn agents grow unbounded prompts; need **constant-size** working memory co-trained with reasoning.

**Memory representation.** Memory **is** the reasoning state: at turn \(t\) emit `<IS_t>` (internal state summary) + `<query_t>` or `<answer_t>`; env returns `<info_t>`. Next turn consolidates \((IS_t, query_t, info_t)\) into `IS_{t+1}` and **prunes** prior tags. Context retains at most ~2 IS + 2 query + 1 info elements.

**Write / read / forget.** Write/forget unified: prune old tags after consolidation. Trained with RL (PPO/Reinforce++ style) under **masked trajectory** stitching because dynamic context breaks linear trajectories. Multi-objective multi-hop tasks force retention of useful info under pruning pressure.

**Compaction.** Aggressive per-turn consolidation — primary mechanism.

**Conflict / supersession.** Overwrite-in-IS; no audit trail of dropped facts.

**Privacy / sharing.** None.

**MoDeX design lessons (6):**
1. **WorkingState as consolidated IS** — keep L1 small and rewritten each turn; never rely on full transcript in pack.
2. Pruning-as-forget is OK for L1, **unsafe** for L3 Anchors — different tiers, different rules.
3. RL that rewards consolidation under forced prune is a future WorkingState compressor — v1 stays heuristic.
4. Masked-trajectory training detail warns: learned memory controllers need careful credit assignment.
5. Peak-token / dependency-length metrics belong in MoDeX cost dashboards.
6. Emergent “what to keep” behaviors are evidence that budgets shape memory content — set budgets deliberately.

---

### 1.7 LEGOMem — Modular Procedural Memory for Multi-Agent Workflow Automation  
**arXiv:2510.04851** · Han, Couturier, Diaz, Zhang, Rühle, Rajmohan (Microsoft) · 2025/2026 · **FULL-READ** (HTML)

**Problem setup.** Multi-agent office/workflow systems rediscover plans/tool patterns; need modular **procedural** memory allocation across orchestrator vs task agents.

**Memory representation.** Offline distill of **successful** trajectories into:
- **Full-task memories:** task description + high-level plan (+ answer + brief reflection).
- **Subtask memories:** subtask description + localized tool-use/observations.  
Stored in vector DB \(\mathcal{M}\) (and per-agent subtask banks in variants).

**Write / read / forget.** Write = LLM curation from successful logs only. Read variants:
1. **Vanilla:** Top-K full-task by \(\phi(d)\); statically extract subtasks to agents.
2. **Dynamic:** retrieve subtask memories during execution per agent bank.
3. **QueryRewrite:** rewrite queries to retrieve multiple candidates per subtask.  
Orchestrator gets full-task memory; agents get subtask memory; re-plan on stall.

**Compaction.** Distill logs → structured LEGO units (plan / subtrace / answer / reflection).

**Conflict / supersession.** Success-only bank; no contradiction handling across versions of procedures.

**Privacy / sharing.** Multi-agent allocation implies different memory visibility by role — but no ACL formalism.

**MoDeX design lessons (7):**
1. **Split orchestrator memory vs worker memory** — maps to pack roles (`boot_agent` vs specialized tools).
2. Procedural memory ≠ belief Anchors — keep skill/procedure store separate (Voyager lesson reinforced).
3. Orchestrator memory critical for decomposition; agent memory for tool accuracy — same in eng multi-agent.
4. Dynamic/subtask retrieval > static extraction when task shapes diverge.
5. Success-only curation misses failure modes — add failing trajectories with labels (Memento/ReasoningBank).
6. Smaller models + good procedural memory can close gaps — cheap workers + rich memory is viable.
7. OfficeBench-style tool workflows ≈ CI/devtool agents — good MoDeX procedural eval target.

---

### 1.8 Memory as Action (MemAct) — Autonomous Context Curation  
**arXiv:2510.12635** · Zhang, Shu, Ma, Lin, Wu, Sang · 2025/2026 · **FULL-READ** (HTML)

**Problem setup.** Long-context alone fails via attention dilution; external heuristic memory managers are unaware of agent reasoning state.

**Memory representation.** Working memory = editable context. Unified policy \(\pi_\theta\) over **task actions** \(\mathcal{A}_{task}\) and **memory actions** \(\mathcal{A}_{mem}\) (in-place delete/insert). Trained with **Dynamic Context Policy Optimization (DCPO)** + SFT cold-start; memory tool schema in appendix.

**Write / read / forget.** Forget/insert are first-class actions jointly optimized with task reward; reported **~51%** average context-length reduction with MemAct-RL-14B matching much larger full-context models (paper claim: accuracy of models **16×** larger).

**Compaction.** Learned active curation (not fixed summarize-every-N).

**Conflict / supersession.** Deletion can drop contradictory context without audit — optimized for task success.

**Privacy / sharing.** None.

**MoDeX design lessons (6):**
1. Treat L1 curation as **actions with audit**, not silent truncation.
2. External heuristic managers (MemGPT-style) are the MoDeX v1 path; learned MemAct is v2+.
3. Joint task+memory reward can sacrifice governance — add Inv-Scope penalties before RL.
4. In-place edit ops map to WorkingState patch events.
5. Context-length reduction is a pack-budget objective metric.
6. Do not grant ambient agents free delete over L3 sealed Anchors.

---

### 1.9 O-Mem — Omni Memory for Personalized Long-Horizon Agents  
**arXiv:2511.13593** · 2025 · **FULL-READ** (HTML)

**Problem setup.** Group-then-retrieve semantic memory misses cross-topic user attributes and injects retrieval noise.

**Memory representation.** Active user profiling with three components:
1. **Persona memory:** attributes \(P_a\) + fact events \(P_f\) with LLM ops **Add/Ignore/Update**.
2. **Working memory:** topic→interactions map \(M_t\).
3. **Episodic memory:** clue/keyword→interactions map \(M_w\) with distinctiveness filter (rare keywords).  
Hierarchical retrieval orchestrates persona + topic + clue channels (Fig. 3).

**Write / read / forget.** Each interaction \(u_i\): extract \((t_i,a_i,e_i)\); update maps; persona gated by Add/Ignore/Update. Read: multi-stage over \(P_a/P_f\), \(M_t\), \(M_w\) via embedding top-k. Claims LoCoMo **~51.67–51.76%**, PERSONAMEM **62.99%**; better latency/token Pareto vs MemoryOS/LangMem/A-Mem (paper figures).

**Compaction.** Persona abstraction + indexing (not full transcript retain).

**Conflict / supersession.** Persona Update/Ignore is soft coherence control — not bi-temporal SUPERSEDES.

**Privacy / sharing.** Persona store is high-sensitivity; paper is personalization-focused, no ACL.

**MoDeX design lessons (7):**
1. **Always hydrate durable persona/profile facets**, not only topic-similar episodes — eng analog: always include active constraints/decisions even if semantically far from query.
2. Clue/keyword episodic index complements dense retrieval (AssoMem multi-signal).
3. Add/Ignore/Update for profile rows ≈ Mem0 ops — map Update→SUPERSEDES when changing eng facts.
4. Distinctiveness filter for rare tokens = keep unique error signatures / ticket IDs.
5. Hierarchical multi-memory consult is a pack compile pattern (persona → topic → clue).
6. Chat personalization SOTA ≠ eng judgment quality — reuse structure, not scores.
7. Persona memory is default **private_raw / workstream_private** until promotion gates fire.

---

### 1.10 Agent KB — Cross-Domain Experience for Agentic Problem Solving  
**arXiv:2507.06229** · Tang, Qin, Peng et al. · 2025 · **FULL-READ** (PDF)

**Problem setup.** Agent frameworks (smolagents, OpenHands, OWL, …) trap experience inside silos; need **cross-framework** shared memory without retraining.

**Memory representation.** Framework-agnostic **experience units** in a shared KB + lightweight APIs. Inference: **two-stage hybrid retrieval** — (1) **planning** seeds workflows, (2) **feedback** applies diagnostic fixes. **Disagreement gate** blocks interfering external knowledge that would destabilize the agent’s own reasoning.

**Write / read / forget.** Aggregate trajectories → structured experiences (auto-curated ≈ manual in ablations). Read via planning+feedback stages. No classical forgetting algebra; gate refuses bad merges.

**Compaction.** Distill heterogeneous traces into abstract experience units.

**Conflict / supersession.** Disagreement gate = interference control (not belief SUPERSEDES, but closely related safety valve).

**Privacy / sharing.** Core contribution is **shared memory infrastructure** across frameworks — collective intelligence; no user-privacy IFC, but cross-tenant risk is implicit.

**Reported results (paper):** smolagents + Agent KB up to **+18.7pp** pass@3 on GAIA (55.2%→73.9%); OpenHands **+4.0pp** SWE-bench pass@1 (24.3%→28.3%).

**MoDeX design lessons (7):**
1. **Sealed shareable Anchors ≈ Agent KB experience units** — abstract away harness-specific traces.
2. Disagreement gate ≈ MoDeX compose: reject foreign Anchor that CONTRADICTS active local chain without explicit adopt.
3. Two-stage retrieve (plan seed → feedback fix) maps to boot pack vs mid-session recall.
4. Cross-framework transfer needs schema normalization (MoDeX Evidence schema).
5. Auto-curation can match manual — invest in cognify quality metrics.
6. Shared KB without capability controls is a leak surface — combine with SHAREABLE gates.
7. SWE-bench gains support procedural/eng experience sharing specifically.

---

### 1.11 MemoryBank — Long-Term Memory with Ebbinghaus Forgetting  
**arXiv:2305.10250** · Zhong et al. · 2023/2024 · **FULL-READ** (PDF)

**Problem setup.** LLMs lack long-term conversational memory for companionship / counseling / secretary scenarios.

**Memory representation.** Storage warehouse of: (i) timestamped multi-turn conversations, (ii) hierarchical **daily → global event summaries**, (iii) **daily → global user personality** portraits. SiliconFriend demo + optional psych tuning.

**Write / read / forget.** Retrieve relevant memories into prompt. Updating uses simplified Ebbinghaus: \(R=e^{-t/S}\) with discrete strength \(S\) init 1; on recall, \(S\leftarrow S+1\), \(t\leftarrow 0\). Optional forgetting for anthropomorphic companion behavior; also works with forgetting disabled.

**Compaction.** Dialog → daily events → global events; personality aggregation.

**Conflict / supersession.** Portrait/event refresh via LLM summarize — overwrite-style.

**Privacy / sharing.** Companion personal data highly sensitive; no ACL model.

**MoDeX design lessons (6):**
1. Ebbinghaus strength useful as **hydrate prior** for soft memories — **not** for sealed eng decisions (never auto-forget constraints).
2. Hierarchical event summaries ≈ L2 digests; personality ≈ durable profile Anchors.
3. Recall-reinforcement (\(S{+}{+}\)) = bump `last_retrieved` / heat (MemoryOS).
4. Dual mode (with/without forgetting) = policy flag by Anchor kind.
5. Probing QA over multi-day simulated users is a template for MoDeX recall tests.
6. Psych/companion tuning is out of scope — keep MoDeX eng-neutral.

---

### 1.12 H-Mem — Hybrid Tree+Graph Memory Evolution & Retrieval  
**arXiv:2605.15701** · Yu, Fang, Liu, Ma · 2026 · **FULL-READ** (HTML)

**Problem setup.** Vector-only / tree-only / graph-only memory each miss either **temporal evolution** or **multi-hop entity reasoning**.

**Memory representation.** Hybrid:
- **Temporal-semantic tree:** leaf = timestamped event fragment; upper nodes = summaries over time windows; nearby similar nodes merge under parent (**STM→LTM evolution**).
- **Entity KG:** entities/relations across fragments for multi-hop.  
Retrieval: decompose query → per-subquery workflow → locate fragments + multi-hop entities in graph → bottom-up evidence from tree → RAG. Taxonomy Table 1 positions H-Mem as only listed method with **both** Memory Evolution **and** Multi-hop Reasoning (vs Mem0/MemOS/MemTree/MemoryOS/EverMemOS/Zep).

**Write / read / forget.** Evolution consolidates short→long via time+similarity parent merge; retrieval agentic/vector/structure-based. Forget not primary; summaries supersede detail in upper nodes (detail remains in leaves unless pruned — paper emphasizes evolution/retrieval).

**Compaction.** Tree summarization up the hierarchy.

**Conflict / supersession.** Consolidation may blur contradictions into summaries — danger for eng.

**Privacy / sharing.** None.

**MoDeX design lessons (6):**
1. MoDeX already wants **graph + hierarchical digests** — H-Mem validates the hybrid, not vector-only.
2. Time-windowed merge is a cognify operator; keep leaf Evidence immutable.
3. Query decomposition → multi-strategy retrieve matches Adaptive-RAG / PropRAG pack modes.
4. Do not let upper-node summaries become sole truth (HippoRAG2 factual regression lesson).
5. SOTA QA claims need eng conflict fixtures before architecture changes.
6. Competitive index cost matters — track cognify CPU/latency.

---

### 1.13 SCM — Self-Controlled Memory Framework  
**arXiv:2304.13343** · Wang, Liang, Yang et al. · 2023 · **FULL-READ** (HTML)

**Problem setup.** Long inputs drown critical history; even long-context models lose key facts under noise.

**Memory representation.** Plug-and-play trio: **LLM agent** + **memory stream** + **memory controller**. Dual memories at step: **activation/long-term** + **flash/short-term** from preceding segment. Controller decides **when/how** to inject memory to avoid noise. Segments ultra-long text without fine-tuning.

**Write / read / forget.** Stream stores memories; controller updates and gates use. Annotated eval tasks: long-term dialogues, book summarization, meeting summarization.

**Compaction.** Segment processing + selective injection (not full history).

**Conflict / supersession.** Controller selection only — no typed belief revision.

**Privacy / sharing.** None.

**MoDeX design lessons (5):**
1. Explicit **memory controller** separate from generator = MoDeX hydrate/pack service (not ambient LLM self-paging over private tiers).
2. Flash vs activation memory ≈ L1 WorkingState vs L2/L3 retrieve.
3. “Introduce only necessary memory” is the anti-lost-in-the-middle packing law.
4. Plug-and-play with any instruction LLM matches local-first MoDeX.
5. Meeting summarization task ≈ eng standup/handoff digest generation.

---

### 1.14 Think-in-Memory (TiM) — Recalling and Post-thinking  
**arXiv:2311.08719** · 2023 · **FULL-READ** (PDF)

**Problem setup.** Long dialogues cause inconsistency because models don’t persistently store intermediate reasoning.

**Memory representation.** **TiM** stores reasoning traces across turns: **recall** relevant thoughts from memory, generate response, then **post-think** to write back refined thoughts — keeping a persistent thought cache beyond the prompt window.

**Write / read / forget.** Write via post-thinking; read via recalling; forget not central (cache grows/selects by relevance).

**Compaction.** Thoughts are already compressed rationales vs raw turns.

**Conflict / supersession.** Newer post-thoughts can replace prior cached thoughts implicitly.

**Privacy / sharing.** None.

**MoDeX design lessons (5):**
1. Store **reasoning traces** as Evidence (agent thoughts), not only user-visible text.
2. Post-think writeback ≈ async cognify after a turn.
3. Recall-before-answer is hydrate; enforce before high-stakes eng actions.
4. Risk: caching wrong rationales poisons future turns — needs SUPERSEDES when corrected.
5. Complements Reflexion verbal RL with more structured thought memory.

---

### 1.15 MemoChat — Tuning LLMs to Use Memos for Long-Range Consistency  
**arXiv:2308.08239** · 2023 · **FULL-READ** (PDF)

**Problem setup.** Open-domain long conversations lose consistency; need model skill to **create/use memos**.

**Memory representation.** Memo documents as external conversational memory; model tuned to decide memo write/read for consistency over long ranges.

**Write / read / forget.** Learned memo operations during dialog; emphasis on consistency maintenance rather than structured graphs.

**Compaction.** Memos are compact facts/notes vs full history.

**Conflict / supersession.** Limited — newer memos may override via model behavior.

**Privacy / sharing.** None.

**MoDeX design lessons (4):**
1. “Memo” skill ≈ agent-initiated `modex remember` — keep as explicit tool, optionally finetuned later.
2. Consistency memos map to lightweight Anchors (preferences, names, standing decisions).
3. Tuning data for memo use is an eval/training artifact, not v1 architecture dependency.
4. Without typed conflict, memo chat systems drift — MoDeX still needs SUPERSEDES.

---

### 1.16 DialSim — Long-Term Multi-Party Dialogue Understanding Eval  
**arXiv:2406.13144** · Kim et al. · 2024/2025 · **FULL-READ** (HTML)

**Problem setup.** Agent evals ignore multi-party, long-term, uncertainty-aware dialogue.

**Memory representation.** Evaluation framework: agent plays a script character; answers spontaneous questions from **dialogue history only**; must recognize insufficient info. **LongDialQA** from long-running TV shows: >1,300 sessions, >1,000 Qs each session scale, **>352k tokens**; names anonymized/swapped to reduce prior-knowledge leakage.

**Write / read / forget.** N/A (benchmark). Stresses long-term retention, multi-hop, multi-party, abstention under uncertainty.

**Privacy / sharing.** Name anonymization is an eval hygiene lesson for leakage via pretraining.

**MoDeX design lessons (5):**
1. Add **multi-party / multi-agent** slices to MoDeX eval (not only user↔assistant).
2. Abstention when history lacks info = sealed-pack honesty / SF competency.
3. Anonymization/swapping blocks false memory from pretrained knowledge — eng fixtures should rename symbols.
4. Ultra-long token histories (>LoCoMo) stress retrieve+budget packing.
5. Used inside MemoryBench — prefer DialSim for multi-party stress, LoCoMo for persona, MemoryAgentBench for SF/conflict.

---

### 1.17 Memory-as-a-Tool — Distilling Feedback into Persistent Tool Memory  
**arXiv:2601.05960** · 2026 · **FULL-READ** (HTML)

**Problem setup.** Inference-time critique/refine loops are ephemeral; learning signal in critique \(c\) dies when context resets.

**Memory representation.** Persistent memory state \(M\) accessed via **tool calls**; amortizes evaluator feedback (rubric-guided refinements) into reusable memory for future prompts.

**Write / read / forget.** Write = distill critique/refinement into \(M\); read = tool-mediated memory access on later tasks; replaces repeated multi-call refine loops.

**Compaction.** Feedback→memory distillation.

**Conflict / supersession.** Not a full belief algebra; memory updates from new critiques.

**Privacy / sharing.** Tool-mediated access is a natural capability boundary.

**MoDeX design lessons (5):**
1. **Memory tools with capability gates** > ambient prompt injection of all memory.
2. Distill CI/reviewer feedback into Anchors (eng code review loops).
3. Amortize expensive critique into store — matches offline cognify.
4. Rubric-conditioned memory ≈ typed Anchor kinds / quality criteria.
5. Prefer explicit tool API in MoDeX CLI (`recall`, `remember`, `promote`).

---

### 1.18 SCM — Sleep-Consolidated Memory with Algorithmic Forgetting  
**arXiv:2604.20943** · Shinde · 2026 · **FULL-READ** (HTML) · *research preview / prototype*

**Problem setup.** Context windows, unbounded vector DBs, and awake-only tiers lack biological consolidation + intentional forgetting.

**Memory representation.** Five components: limited working memory; **4-D importance tagging**; offline sleep with **NREM** (strengthen) + **REM** (novel associations); **value-based forgetting**; computational self-model for introspection. Encodes structured semantic concepts (not raw tokens).

**Write / read / forget.** Online encode+tag into WM; sleep cycles consolidate; intentional prune of low-value items. Claims (prototype suite): perfect recall on 10-turn conversations; **90.9%** memory-noise reduction via adaptive forgetting; search **<1 ms** at hundreds of concepts.

**Compaction.** Sleep consolidation + pruning.

**Conflict / supersession.** Associative REM linking may create unsupported edges — treat cautiously.

**Privacy / sharing.** Self-model introspection; no multi-principal ACL.

**MoDeX design lessons (6):**
1. **Offline sleep-time cognify** (LightMem + this) is the right batch lane for MoDeX.
2. Multi-dimensional importance > single scalar — consider {utility, recency, evidence-strength, shareability}.
3. Intentional forgetting ≈ archive low-heat L2 digests; never prune sealed L3 without SUPERSEDES.
4. Self-model ≈ agent/profile Anchor facet (capabilities, preferences) — keep scoped.
5. Prototype numbers are small-bench — do not lock constants from them.
6. NREM strengthen / REM associate ≈ promote vs link-suggestion passes.

---

## 2. Cross-cutting synthesis (Batch 3 → MoDeX)

### 2.1 Reinforced agreements
1. **Experience / strategy memory** (ReasoningBank, Memento, Agent KB, LEGOMem) is distinct from **persona/fact memory** (O-Mem, MemoryBank) — MoDeX should keep procedural/strategy stores separate from decision Anchors.
2. **Failure lessons matter** (Memento, ReasoningBank) — success-only banks are incomplete.
3. **Controller vs generator** (SCM, MemAct, Memory-as-a-Tool) supports MoDeX hydrate as a gated service.
4. **Hybrid indices** (H-Mem tree+graph; O-Mem persona+topic+clue) beat single-channel dense RAG.
5. **Continual feedback eval** (MemoryBench, DialSim) belongs in MoDeX acceptance, not only LoCoMo recall.

### 2.2 Disagreements / traps
| Trap | MoDeX stance |
|------|----------------|
| Ebbinghaus auto-forget of durable facts (MemoryBank) | Kind-policy: soft heat OK; sealed Anchors never auto-drop |
| Learned context delete for reward (MemAct/MEM1) | OK for L1; L3 requires SUPERSEDES+audit |
| Success-only procedural banks (LEGOMem vanilla curation) | Also store labeled failures |
| Cross-framework share without gates (Agent KB risk) | Disagreement gate **plus** capability/share facets |
| Summary-upper-nodes as sole truth (H-Mem evolution) | Leaves/Evidence remain authoritative |
| Companion forgetting anthropomorphism | Not a design goal for eng memory |

### 2.3 No architecture-lock contradictions
Nothing forces a change to Anchors+Evidence / L0–L4 / SUPERSEDES / sealed packs. Strongest additives: **disagreement gate** for foreign experience (Agent KB), **always-on persona/constraint channel** (O-Mem), **strategy-vs-fact store split** (ReasoningBank/LEGOMem), **feedback-continual eval** (MemoryBench).

---

## 3. CORPUS INDEX (Batch 3)

| paper | year | deep-read? | one-paragraph insight | MoDeX relevance |
|-------|------|------------|----------------------|-----------------|
| LTM Self-Evolution (2410.15665) | 2024 | **FULL** | LTM as foundation of AI self-evolution; external KB vs parametric vs mixed paths. | Experience-class L3; v1 external store. |
| LLM Agents Survey (2309.07864) | 2023 | **FULL** (§memory) | §3.1.3 memory taxonomy: summarize/compress; retrieve by RRI; citation map. | Hydrate score ancestry; bib map. |
| Memento (2508.16153) | 2025 | **FULL** | M-MDP case bank; NP/parametric CBR; learn without LLM finetune; keep failures. | Failure Evidence; CBR hydrate. |
| MemoryBench (2510.17281) | 2025 | **FULL** | Feedback-sim continual-learning bench across domains/languages. | Continual eval harness. |
| ReasoningBank (2509.25140) | 2025 | **FULL** | Distill strategies from self-judged success+failure; MaTTS experience scaling. | Strategy Anchors; cognify budget. |
| MEM1 (2506.15841) | 2025 | **FULL** | RL constant-size IS memory co-trained with reasoning; prune each turn. | L1 WorkingState rewrite. |
| LEGOMem (2510.04851) | 2025 | **FULL** | Modular procedural memory for orchestrator vs agents; Dynamic/QueryRewrite variants. | Role-split procedural store. |
| MemAct (2510.12635) | 2025 | **FULL** | Memory ops as RL actions; DCPO; large context cuts. | L1 curation actions; not L3 deletes. |
| O-Mem (2511.13593) | 2025 | **FULL** | Persona+working+episodic; Add/Ignore/Update; hierarchical user-centric retrieve. | Always-on constraint/persona channel. |
| Agent KB (2507.06229) | 2025 | **FULL** | Cross-framework experience KB; plan+feedback retrieve; disagreement gate. | Shareable experience + compose gate. |
| MemoryBank (2305.10250) | 2023 | **FULL** | Hierarchical events/portraits + Ebbinghaus \(R=e^{-t/S}\). | Heat prior; kind-scoped forgetting. |
| H-Mem (2605.15701) | 2026 | **FULL** | Temporal-semantic tree evolution + entity KG; hybrid retrieve. | Graph+digest hybrid cognify. |
| SCM (2304.13343) | 2023 | **FULL** | Agent + stream + controller; flash vs activation memory. | Gated hydrate controller. |
| Think-in-Memory (2311.08719) | 2023 | **FULL** | Recall + post-think persistent thought cache. | Reasoning Evidence writeback. |
| MemoChat (2308.08239) | 2023 | **FULL** | Tuned memo write/read for long-range consistency. | Explicit remember tool skill. |
| DialSim (2406.13144) | 2024 | **FULL** | Multi-party long-term QA sim; abstention; LongDialQA. | Multi-agent/abstain eval. |
| Memory-as-a-Tool (2601.05960) | 2026 | **FULL** | Distill critique loops into tool-accessible persistent memory. | Capability-gated memory tools. |
| Sleep-Consolidated SCM (2604.20943) | 2026 | **FULL** | NREM/REM sleep, 4-D value tags, intentional forgetting (preview). | Offline cognify; multi-dim importance. |

---

## 4. Source fetch log (Batch 3)

| ID | Fetch path |
|----|------------|
| 2410.15665, 2508.16153, 2509.25140, 2506.15841, 2510.04851, 2510.12635, 2511.13593, 2605.15701, 2304.13343, 2406.13144, 2601.05960, 2604.20943 | `arxiv.org/html` → plaintext |
| 2309.07864, 2510.17281, 2507.06229, 2305.10250, 2311.08719, 2308.08239 | `arxiv.org/pdf` → `pdftotext` |
| Cached reuse | Some HTML bodies already present under `/tmp/modex-papers/full/` from prior passes; re-read in full for this batch |

---

## 5. Top implementation lessons (Batch 3 → MoDeX)

1. **Split stores by kind:** strategy/procedural experience (ReasoningBank/LEGOMem/Agent KB) vs persona/facts (O-Mem/MemoryBank) vs working IS (MEM1) — do not overload L3 decision Anchors.
2. **Disagreement gate on foreign experience** before compose/share (Agent KB) — complements SUPERSEDES/CONTRADICTS.
3. **Always-on durable channel** in hydrate (O-Mem persona) = always pack active eng constraints, not only similarity hits.
4. **Failure-aware memory** (Memento/ReasoningBank) must be first-class Evidence for promotion.
5. **Eval beyond recall:** MemoryBench continual feedback + DialSim multi-party abstention + existing SF/conflict slices.

---

*End of Batch 3. Mechanism detail preferred over buzzwords; no invented experimental results.*
