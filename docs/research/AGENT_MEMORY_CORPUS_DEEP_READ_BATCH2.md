# Agent Memory Corpus Deep-Read — Batch 2 (MoDeX)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/memory-architecture-spec-2e45`  
> **Scope:** Priority FULL-read queue after Batch 1 (`AGENT_MEMORY_CORPUS_DEEP_READ.md`).  
> **Method:** Full arXiv HTML or PDF body text fetched and read (not abstract-only). Honesty marks below.  
> **MoDeX lens:** Anchors+Evidence, L0–L4, SUPERSEDES/CONTRADICTS, workstreams, promotion/privacy, sealed handoff.

---

## 0. Honesty about coverage (this batch)

| Status | Papers |
|--------|--------|
| **FULL deep-read** (complete body from arXiv HTML or PDF; mechanisms extracted) | MemoryOS (2506.06326); LightMem (2510.18866); MAGMA (2601.03236); Memory-R1 (2508.19828); ConfAIde (2310.17884); Fides IFC (2505.23643 PDF); LoCoMo (2402.17753); MemoryAgentBench (2507.05257); AriGraph (2407.04363 PDF); Reflexion (2303.11366); Voyager skill-library aspects (2305.16291) |
| **FULL re-read extras** (already FULL in SHAREABLE memo; this batch adds mechanism extras) | Collaborative Memory (2505.18279) |
| **Not claimed FULL this batch** | CaMeL (2503.18813) — identified; queued; not fetched this pass |

**Count of new FULL deep-reads this batch:** **11** primary texts (+ Collaborative Memory extras on already-FULL paper).

**Do not invent:** Where a paper is silent (e.g., no privacy model, no typed SUPERSEDES), that silence is recorded. Reported numbers below are taken from the papers’ own tables/text.

---

## 1. Per-paper deep extracts

### 1.1 MemoryOS — OS-inspired hierarchical agent memory  
**arXiv:2506.06326** · Kang, Ji, Zhao, Bai · 2025 · **FULL-READ** (HTML)

**Problem setup.** Fixed context windows break long-conversation coherence and personalization; prior systems isolate storage *or* retrieval *or* update — no unified “OS” for agent memory.

**Memory representation.** Four modules: Storage, Updating, Retrieval, Generation. Three tiers:
1. **STM (Short-Term Memory):** dialogue **pages** \(page_i=\{Q_i,R_i,T_i\}\); **dialogue chains** add LLM-generated \(meta^{chain}\) linking contiguous turns or resetting on semantic discontinuity.
2. **MTM (Mid-Term Memory):** **segmented paging** — pages with same topic → segments; segment membership by \(\mathcal{F}_{score}=\cos(e_s,e_p)+\mathrm{Jaccard}(K_s,K_p)>\theta\); LLM segment summaries.
3. **LPM (Long-term Persona Memory):** User Persona (static profile + User KB + 90-dim User Traits) and Agent Persona (profile + dynamic Agent Traits). User KB / Assistant Traits are fixed-size queues (e.g. 100) with FIFO.

**Write / read / forget.**
- **STM→MTM:** FIFO — when STM queue full, oldest page migrates to MTM and merges into segments by score.
- **MTM heat:** \(\mathrm{Heat}=\alpha N_{visit}+\beta L_{interaction}+\gamma R_{recency}\) with \(R_{recency}=\exp(-\Delta t/\mu)\). Lowest-heat segments **evicted** when capacity exceeded.
- **MTM→LPM:** segments with Heat \(>\tau\) (paper uses \(\tau=5\)) update User Traits / User KB / Agent Traits via LLM extraction.
- **Read:** STM = all recent pages; MTM = two-stage (segment match → page retrieve; bump visit/recency); LPM = top-10 semantic KB/traits + full profiles/traits into prompt.
- **Forget:** heat eviction (MTM) + FIFO on KB/traits queues — **not** typed contradiction invalidation.

**Compaction.** Segment summaries + persona extraction; pages remain inside segments until eviction.

**Conflict / supersession.** No bi-temporal edge invalidation; persona/KB updates overwrite via LLM extract into FIFO queues.

**Privacy / sharing.** Single-user personalization framing; no multi-principal ACL.

**MoDeX design lessons (6):**
1. **Page → segment → persona** maps cleanly to L0/L2/L3 (dialogue units → topic episodes → durable Anchors/traits).
2. **Heat = visits × length × recency** is a concrete hydrate-ranking prior complementary to Generative Agents’ importance.
3. Two-stage MTM retrieve (segment then page) = locate-then-rerank — same pattern as ES-Mem boundaries.
4. Dialogue-chain meta on STM is a cheap continuity signal for eng sessions (same PR / same failure thread).
5. FIFO eviction of LPM KB is **unsafe** for engineering decisions — MoDeX Anchors must not silently drop under queue pressure; archive/SUPERSEDES instead.
6. Claimed LoCoMo gains (avg +49.11% F1 / +46.18% BLEU-1 vs baselines on GPT-4o-mini — paper’s own figure) are chat-persona metrics; do not treat as eng-judgment evidence.

---

### 1.2 LightMem — Lightweight memory-augmented generation  
**arXiv:2510.18866** · Fang, Deng, Xu, Jiang et al. · 2025 · **FULL-READ** (HTML)

**Problem setup.** Conventional memory pipelines summarize/extract/update **every turn online**, wasting tokens and coupling expensive maintenance to inference latency; sensory input is redundant; updates conflict with real-time serving.

**Memory representation.** Three “Light” modules:
1. **Light1 Sensory memory:** LLMLingua-2 (or generative) **pre-compression** retains tokens with \(P(\mathrm{retain})>\tau\) (percentile threshold by ratio \(r\)); hybrid **topic segmentation** \(\mathcal{B}=\mathcal{B}_1\cap\mathcal{B}_2\) (attention local-maxima ∩ similarity drop).
2. **Light2 Topic-aware STM:** buffer of `{topic, message turns}`; when token threshold \(th\) hit → LLM summarize → LTM entry `{topic, embed(sum), user, model}`.
3. **Light3 LTM with sleep-time update:** online **soft update** = direct insert + build similarity update queues offline; **offline parallel update** runs \(f_{update}\) per entry’s queue (later timestamps may update earlier; top-\(k\) similar candidates).

**Write / read / forget.**
- Write path filters → segments → buffered summarize → insert.
- Soft update decouples maintenance from the critical path; parallel offline queues cut sequential update latency.
- Paper emphasizes efficiency (token/API/runtime) vs MemoryOS/Mem0/A-MEM/LangMem on LongMemEval-S and LoCoMo; forget is implicit via update consolidation, not a first-class typed DELETE algebra in the architecture section.

**Compaction.** Pre-compression + topic-gated summarization + offline consolidation (“sleep-time”).

**Conflict / supersession.** Timestamp-ordered update candidates; online path deliberately avoids heavy conflict resolution at inference.

**Privacy / sharing.** None.

**MoDeX design lessons (7):**
1. **Pre-compress L0 before LLM extract** — huge cost win; MoDeX hooks should drop boilerplate (diff noise, formatter spam) before cognify.
2. **Topic segmentation before summarize** prevents mixed-topic Anchors (matches Nemori/ES-Mem).
3. **Soft insert online + consolidate offline** is the right latency model for local-first MoDeX (capture cheap; promotion/cognify async).
4. Timestamp constraint \(t_j\ge t_i\) for updates ≈ prefer newer Evidence when resolving — still need audit rows (TOKI), not silent overwrite.
5. Budget STM by **token threshold \(th\)**, not only turn count.
6. Efficiency is a first-class architecture constraint — LightMem’s complexity table is a template for MoDeX cost accounting.
7. Do not treat offline update as “solved forgetting”; MoDeX still needs explicit SUPERSEDES for eng truth.

---

### 1.3 MAGMA — Multi-graph agentic memory  
**arXiv:2601.03236** · Jiang, Li, Li, Li · 2026 · **FULL-READ** (HTML)

**Problem setup.** MAG systems usually organize memory by associative proximity only; long-horizon reasoning needs **heterogeneous relations** (temporal, causal, entity, semantic) and intent-aware traversal.

**Memory representation.** Unified graph \(\mathcal{G}\) with vector DB + four edge subspaces over event nodes \(n_i=(c_i,\tau_i,\ldots)\):
- \(\mathcal{E}_{temp}\): immutable temporal backbone (\(\tau_i<\tau_j\))
- \(\mathcal{E}_{causal}\): directed logical entailment
- \(\mathcal{E}_{sem}\): undirected similarity (\(\cos>\theta\))
- \(\mathcal{E}_{ent}\): event↔entity (object permanence across timelines)

**Write / read / forget.**
- **Fast path (synaptic ingestion):** segment event → append temporal edge → vector index → enqueue for slow path (non-blocking).
- **Slow path (structural consolidation):** async LLM infers causal + entity edges from local neighborhood.
- **Read:** query analysis (intent \(T_q\in\{\textsc{Why},\textsc{When},\textsc{Entity},\ldots\}\), temporal window, dense+sparse) → RRF anchors → **Adaptive Traversal** (heuristic beam search with intent-weighted edge affinity + semantic sim + decay) → topological sort / linearize with `<t:τ> content <ref:id>` → salience token budget (low-score nodes summarized).
- Forget/invalidation: not a primary operator (graph densifies; no bi-temporal expire API in the design section).

**Compaction.** Salience-based budgeting at serialize time; async structural densification.

**Conflict / supersession.** Not first-class ConflictSets; ablation shows knowledge-update category can lag full-context on LongMemEval (paper Table 2: MAGMA knowledge-update 52.6% vs full-context 78.2% on gpt-4o-mini — paper’s numbers).

**Privacy / sharing.** None.

**MoDeX design lessons (7):**
1. **Separate edge types** (temporal / causal / entity / semantic) — MoDeX should not overload LINKED_TO; keep ABOUT, CAUSES/BECAUSE, TEMPORAL_NEXT, SIMILAR as distinct.
2. **Intent-routed hydrate** (why→causal, when→temporal) for pack compile.
3. Fast ingest + slow densify matches MoDeX hooks vs cognify.
4. Provenance refs in linearized context (`<ref:id>`) = Evidence IDs in sealed packs.
5. Salience token budgeting = L4 pack budget.
6. Immutable temporal backbone is good; still add SUPERSEDES for belief change (MAGMA weak on knowledge-update vs full context).
7. Paper LoCoMo overall judge 0.700 (gpt-4o-mini) vs MemoryOS 0.553 / Nemori 0.590 / A-MEM 0.580 — useful relative signal only under their judge protocol.

---

### 1.4 Memory-R1 — RL-trained memory manage + utilize  
**arXiv:2508.19828** · Yan, Yang, Huang, Nie et al. · 2025 · **FULL-READ** (HTML)

**Problem setup.** Deciding ADD/UPDATE/DELETE/NOOP and filtering retrieved memories for answers is hard to supervise; SFT lacks labels for every memory op.

**Memory representation.** External **memory bank** of natural-language entries; two specialized agents:
1. **Memory Manager** policy \(\pi_\theta(o,m'\mid x,\mathcal{M}_{old})\) with \(o\in\{\mathrm{ADD},\mathrm{UPDATE},\mathrm{DELETE},\mathrm{NOOP}\}\).
2. **Answer Agent** \(\pi_\theta(y\mid q,\mathcal{M}_{ret})\) over top-~60 similarity-retrieved candidates (Mem0-style retrieval cited).

**Write / read / forget.**
- Training via **PPO** and **GRPO**; reward for Manager = EM of frozen Answer Agent after applying the op; Answer Agent reward = EM vs gold.
- Forget = learned **DELETE**; update = learned **UPDATE**; no audit/bi-temporal guarantee — policy may erase.
- Evaluation on LoCoMo-style multi-session QA (paper tables compare vs A-Mem, Mem0, MemoryOS, etc.).

**Compaction.** Emergent from UPDATE/DELETE policy under QA reward — not an explicit hierarchy.

**Conflict / supersession.** Implicit in UPDATE/DELETE actions; optimized for answer EM, **not** safe abstention or audit.

**Privacy / sharing.** None.

**MoDeX design lessons (6):**
1. Explicit op enum ADD/UPDATE/DELETE/NOOP matches Mem0 — MoDeX should keep the enum but map DELETE→**SUPERSEDES+archive**, never hard erase sealed Anchors.
2. **Outcome-driven rewards** (downstream task success) are powerful for tuning promotion heuristics — but eng memory must add governance rewards (Inv-Scope, no-leak), not EM alone.
3. Separating Manager vs Answerer mirrors capture/cognify vs hydrate.
4. RL memory controllers are **v2+** for MoDeX (architecture lock = heuristic + CLI first); treat Memory-R1 as evidence that learned policies beat prompted CRUD *on chat QA*, not as v1 requirement.
5. Retrieving ~60 then filtering is a hydrate pattern (candidate pool → recognition filter).
6. Danger: EM-maximizing DELETE can destroy minority-true engineering constraints — ConflictSet/disputed status must remain first-class.

---

### 1.5 ConfAIde — Contextual integrity privacy benchmark  
**arXiv:2310.17884** · Mireshghallah, Kim, Zhou, Tsvetkov, Sap · 2023/2024 · **FULL-READ** (HTML)  
*(Paper title: “Can LLMs Keep a Secret? … via Contextual Integrity Theory”; benchmark name ConfAIde.)*

**Problem setup.** LLMs handle sensitive information poorly; need a benchmark grounded in **contextual integrity** (Nissenbaum): privacy = appropriate information flow given context, not secrecy alone.

**Memory representation.** Not an agent memory system — a **four-tier evaluation**:
1. **Tier 1:** out-of-context sensitivity ratings (Pew information types).
2. **Tier 2.a/2.b:** information-flow vignettes (type × actor × use); 2.b adds short-story context.
3. **Tier 3:** theory-of-mind secret-sharing scenarios (X shares with Y; Y tempted to tell Z); metrics = free-form leakage (string + proxy recovery), ToM access errors, binary control questions.
4. **Tier 4:** meeting transcripts mixing **private secret** + **public action items**; tasks = action items for X + meeting summary to all — privacy–utility tradeoff.

**Write / read / forget.** N/A (benchmark). Human annotations for Tiers 1–3; Tier 4 error if leak secret **or** drop public item.

**Key empirical claims (paper’s own):** human–model privacy expectation correlation drops as tiers grow; GPT-4 Tier-3 string-match leakage **0.22**, ChatGPT **0.93** (Table 3); Tier 4 still high leakage even with privacy-preserving instructions; helpfulness alignment can override privacy (e.g. “helping others” incentive increases leakage).

**Privacy / sharing.** Core contribution — CI parameters (sender, recipient, subject, information type, transmission principle) as the right privacy ontology.

**MoDeX design lessons (6):**
1. MoDeX shareability ≠ “not secret text”; appropriateness depends on **actors + purpose** (workstream vs repo_shared_safe).
2. Tier-3 ToM failures warn: agents will leak private Anchors into “helpful” summaries — sealed packs need **capability + redaction**, not prompt “please respect privacy”.
3. Tier-4 privacy–utility tradeoff = pack compile: must include public decisions while excluding private_raw / workstream_private.
4. Binary “is sharing OK?” accuracy ≠ free-form non-leakage — eval MoDeX with **generation probes**, not only classify.
5. Do not auto-promote on recurrence alone (already in SHAREABLE memo) — ConfAIde is the why.
6. No contradiction to architecture locks; strengthens promotion-gate rationale.

---

### 1.6 Fides — Information-flow control for AI agents  
**arXiv:2505.23643** · Costa, Köpf, Kolluri, Paverd, Russinovich et al. (Microsoft) · 2025 · **FULL-READ** (PDF; ar5iv HTML failed)

**Problem setup.** Prompt injection + consequential tools → exfiltration; probabilistic defenses insufficient. Need **deterministic** IFC on agent planners.

**Memory representation (planner memory).** Planner state = conversation history + **labeled** tool-result **variables** in planner memory. Labels from confidentiality × integrity lattice (e.g. \(\{L,H\}\) or \(\mathcal{P}(U)\)); join \(\sqcup\) on combine. Tools read/write datastore variables with static authorized labels.

**Write / read / forget.**
- Dynamic taint-tracking on messages, actions, tool calls/results (Algorithms 5–7).
- **Policy engine** allow/deny consequential actions from labels.
- **Selective hiding:** only store in variables data that would raise context label and block future tools (improvement on Dual LLM).
- **Revealing:** quarantined LLM + **constrained decoding** (typed schema) to inspect variables without fully tainting planner context; enables robust declassification/endorsement escapes when typed.
- Security goals: **integrity noninterference** (PIA cannot trigger consequential actions); **explicit secrecy** for confidentiality (allows confidential data to influence control flow — pragmatic compromise).

**Compaction.** Not about episodic compaction; about minimizing label inflation via selective variable introduction.

**Conflict / supersession.** N/A for belief memory; conflicts are policy deny vs utility loss.

**Privacy / sharing.** First-class IFC — closest formal twin to MoDeX capability-gated sealed packs / Inv-Scope.

**MoDeX design lessons (7):**
1. Treat pack fields and tool I/O as **labeled** — confidentiality (visibility class) × integrity (who may write Anchors).
2. **Planner/context taint:** once private_raw enters L1 WorkingState, deny shareable promotion / external tool exfil without declassify.
3. Selective hide-behind-capability (variable/ocap) > putting all retrieved memory into the prompt.
4. Quarantined extract-with-schema ≈ redaction/promotion LLM that outputs typed Anchor JSON without echoing secrets into free prose.
5. Explicit secrecy vs noninterference: MoDeX docs should state which guarantee sealed handoff aims for (likely explicit secrecy + integrity NI on share actions).
6. Policy-as-code predicates over labels — align with capability checks, not only prompt policy.
7. Prior SHAREABLE memo’s abstract-only note on Fides is superseded by this FULL read — no architecture contradiction; IFC strengthens sealed-pack story.

---

### 1.7 LoCoMo — Very long-term conversational memory benchmark  
**arXiv:2402.17753** · Maharana, Lee, Tulyakov, Bansal, Barbieri, Fang · 2024 · **FULL-READ** (HTML)

**Problem setup.** Prior dialogue memory evals ≤~5 sessions; need ultra-long, multi-session, multimodal dialogues with causal life events.

**Dataset / tasks (not a memory system).**
- Machine–human pipeline: personas + **temporal event graphs** (causally linked life events) + reflect&respond agents + image share/react; human edit for long-term consistency.
- Stats (paper Table 1): avg **304.9 turns**, **19.3 sessions**, **~9,209 tokens**, months-scale gaps, multimodal.
- Eval tasks: (1) **QA** — single-hop, multi-hop, temporal, open-domain, **adversarial** (unanswerable); (2) **event summarization** (FactScore vs event graph); (3) multimodal dialogue generation.
- Finding highlighted: long-context LLMs struggle especially on **adversarial** QA (~83% lower than base in paper’s claim).

**Write / read / forget.** Agents in the generative pipeline use short-term + long-term memory with observation logging; benchmark consumers supply their own memory systems.

**Conflict / supersession.** Adversarial questions probe refusal; event graphs encode causal change over time but LoCoMo is not a belief-revision unit test (see MemoryAgentBench SF).

**Privacy / sharing.** Personas may contain sensitive life facts — dataset hygiene concern for MoDeX eval copies; not an ACL theory paper.

**MoDeX design lessons (5):**
1. Use LoCoMo as **regression suite for temporal + multi-hop hydrate**, not as eng-judgment gold.
2. Keep an **adversarial / unanswerable** slice in MoDeX evals (abstain > hallucinate).
3. Causal event graphs as generator = idea for synthetic eng timelines (incident → mitigation → revert).
4. FactScore-style atomic claims for summarization eval ≈ Evidence coverage metrics.
5. Session count and month-scale gaps stress-test recurrence/heat ranking.

---

### 1.8 MemoryAgentBench — Four memory competencies  
**arXiv:2507.05257** · Hu, Wang, McAuley · 2025/2026 · **FULL-READ** (HTML)

**Problem setup.** Long-context benchmarks ≠ memory benchmarks: memory is a **compressed, incrementally updated** state. Prior memory QA sets miss competencies beyond accurate retrieval.

**Four competencies.**
1. **AR — Accurate Retrieval** (single/multi-hop, LongMemEval-S*, EventQA)
2. **TTL — Test-Time Learning** (classify/recommend from in-context demos without training)
3. **LRU — Long-Range Understanding** (≥100k; summarization + detective QA)
4. **SF — Selective Forgetting** — new **FactConsolidation** (SH/MH) from MQUAKE counterfactual edit pairs; later facts should overwrite; reason on final state

**Protocol.** Chunks \(c_1..c_n\) wrapped as user–assistant turns; agent must **absorb incrementally**, then answer. Evaluates long-context, RAG variants, and agentic memory (MemGPT, MIRIX, etc.). Paper’s thesis: existing agents do not simultaneously excel at all four.

**Conflict / supersession.** SF is the explicit conflict slice MoDeX needs: prefer later, consistent final state — but gold=latest can hide StateFuse-style legitimate disputes; use SF for **invalidation correctness**, plus separate disputed-projection tests.

**Privacy / sharing.** Not in scope.

**MoDeX design lessons (6):**
1. MoDeX eval matrix should track **AR / TTL / LRU / SF** explicitly (map TTL→skill/playbook uptake; SF→SUPERSEDES).
2. Incremental chunk protocol matches hook-stream ingestion better than one-shot long context.
3. FactConsolidation is the primary academic SF fixture to adapt for eng (API version bumps, reverted decisions).
4. Commercial memory agents still fail SF/LRU in paper’s study — do not assume MemGPT-style tools alone solve forgetting.
5. Compression distinction (memory vs long context) validates L0→L3 promotion rather than retaining full raw forever in hydrate.
6. No architecture contradiction; strengthens WORKSTREAM/promotion eval plans.

---

### 1.9 AriGraph — KG world model + episodic memory  
**arXiv:2407.04363** · Anokhin, Semenov, Sorokin, Evseev et al. · 2024/2025 · **FULL-READ** (PDF)

**Problem setup.** Unstructured history/summary/RAG memory fails complex interactive decision-making; need structured world model from exploration.

**Memory representation.** AriGraph \(G=(V_s,E_s,V_e,E_e)\):
- Semantic vertices/edges = triplets \((obj_1,rel,obj_2)\) from observations.
- Episodic vertex \(v_e^t=o_t\); episodic edges link all triplets extracted at \(t\) to that observation (“happened at the same time” — hyperedge-like).

**Write / read / forget.**
- **Write:** extract new triplets → retrieve incident semantic edges for mentioned objects → LLM detects **outdated** edges vs new → **remove outdated** → add new semantic + episodic nodes/edges.
- **Read:** SemanticSearch (Contriever + graph expand depth \(d\), width \(w\)) → EpisodicSearch scoring observations by incident retrieved triplets (Eq. 1 with \(\log N_i\) weighting) → working memory.
- Ariadne agent: working memory = goal + observation + recent history + retrieved semantic/episodic + plan; planning module + ReAct decision; optional `go to location` via spatial relations.

**Compaction.** Semantic graph is the compressed world model; episodic observations retained as vertices linked to triplets.

**Conflict / supersession.** Explicit **outdated edge deletion** on update — history of removed edges not emphasized as audit (contrast Graphiti invalidate-with-timestamps).

**Privacy / sharing.** None (TextWorld/NetHack / multi-hop QA).

**MoDeX design lessons (6):**
1. Episodic hyperedge “co-observed” is a strong Evidence pattern (all facts from one eng session chunk).
2. Write-time **outdated detection among entity-incident edges** ≈ Graphiti/Mem0 conflict check — MoDeX should **invalidate+audit**, not hard-delete like AriGraph.
3. Two-stage semantic→episodic retrieval = Anchor hit → pull supporting Episode/Evidence.
4. Spatial `go to` via KG ≈ navigate file/symbol graph in eng hydrate.
5. Working memory vs AriGraph LTM mirrors L1 vs L2/L3.
6. Useful world-model for exploratory agents; for MoDeX truth layer, prefer StateFuse/TOKI audit semantics over AriGraph’s remove.

---

### 1.10 Reflexion — Verbal reinforcement as episodic memory  
**arXiv:2303.11366** · Shinn, Cassano, Berman, Gopinath et al. · 2023 · **FULL-READ** (HTML)

**Problem setup.** Gradient RL on LLM agents is expensive; need learning from failures via language.

**Memory representation.**
- **Short-term:** trajectory history \(\tau_t=[a_0,o_0,\ldots]\).
- **Long-term `mem`:** list of verbal self-reflections \(sr_t\) (bounded max window; older slide out).
- Modules: Actor \(M_a\), Evaluator \(M_e\), Self-Reflection \(M_{sr}\).

**Write / read / forget.**
- After each trial: evaluate → reflect → **append** \(sr_t\) to `mem`.
- Next trial Actor conditions on `mem` + trajectory.
- Forget = sliding window on `mem` (capacity bound), not semantic invalidation.
- Feedback sources: binary success, heuristics, LLM judges, unit tests (programming).

**Compaction.** Reflection text is the compression of a failed/successful trial into a lesson.

**Conflict / supersession.** Newer reflections appended; no contradiction algebra between lessons.

**Privacy / sharing.** None.

**MoDeX design lessons (5):**
1. Verbal self-reflection ≠ shareable Anchor — store as L2/L3 **candidate** with Evidence to trajectory; never auto `repo_shared_safe`.
2. Evaluator→Reflection pipeline is the right shape for eng postmortems (test fail → gotcha Anchor).
3. Bound reflection memory; promote durable lessons via recurrence/gap gates (RecMem/Nemori), not unbounded append.
4. Policy = memory encoding + LLM (no finetune) — aligns with MoDeX local-first.
5. Failures improved across AlfWorld/HotPotQA/HumanEval in paper — use as motivation for reflection pass, not as schema.

---

### 1.11 Voyager — Skill library as procedural memory  
**arXiv:2305.16291** · Wang, Xie, Jiang, Mandlekar et al. · 2023 · **FULL-READ** (HTML; focus: skill library / memory aspects)

**Problem setup.** Lifelong embodied agents need compositional, reusable skills — not only episodic chat memory.

**Memory representation (skill library).**
- Skills = **executable code programs** (Mineflayer APIs), temporally extended and compositional.
- Vector DB index: key = embedding of GPT-generated **skill description**; value = program.
- On success (self-verification), **add** skill; on new tasks, **retrieve** relevant skills into GPT-4 prompt for composition.
- Companion modules: automatic curriculum; iterative prompting with env feedback, execution errors, self-verification.

**Write / read / forget.**
- Write: verified programs only enter the library.
- Read: embedding retrieval of relevant skills + primitives into context.
- Forget: not primary; ablation shows plateau without library.
- Generalization: skill library transferable to unseen tasks / can warm-start other agents (AutoGPT + Voyager skills).

**Compaction.** Skills are already compressed procedures; curriculum avoids proposing impossible tasks somewhat.

**Conflict / supersession.** No versioned skill invalidation story; self-verify gates admission.

**Privacy / sharing.** Skills can encode environment-specific strategies — sharing = code exfil risk in eng analogues.

**MoDeX design lessons (6):**
1. **Procedural memory ≠ factual Anchors** — map skills to future playbooks/scripts layer; do not overload L3 decision Anchors.
2. Index by **description embedding**, store executable/proven artifact + Evidence (passing verification).
3. Only admit skills after **tool-verified success** — same as MoDeX “test-backed rejection/decision” discipline.
4. Retrieval-for-composition = hydrate related playbooks into L4 pack.
5. Self-verification GPT judge is fallible (paper limitations) — prefer deterministic checks when available.
6. Ablation: without skill library, progress plateaus — justifies a dedicated procedural store in MoDeX roadmap (not v1 lock change).

---

### 1.12 Collaborative Memory — extras beyond SHAREABLE memo  
**arXiv:2505.18279** · Rezazadeh, Li, Lou, Zhao et al. · 2025 · **FULL re-read** (HTML; primary coverage already in `SHAREABLE_ANCHOR_POLICY_RESEARCH.md`)

**Extras worth recording for MoDeX (mechanism-level):**
1. Accessible fragment set \(\mathcal{M}(u,a,t)\) requires both agent-set and resource-set of fragment ⊆ current permissions — **dual closure** (user↔agent and agent↔resource). MoDeX sealed packs should similarly require recipient capability **and** resource scope.
2. Cross-access includes: same user’s other agents; same agent’s other users; other users’ fragments if agent/resource graphs allow — enumerates leak paths AgentLeak-style topology must block.
3. Policies \(\pi^{read}\), \(\pi^{write/private}\), \(\pi^{write/shared}\) may be global / per-user / per-agent / time-varying — MoDeX promotion policy should be **named and versioned**, not ambient.
4. Shared write may anonymize/redact/block — confirms promotion ≠ raw copy.
5. Implementation sketch: coordinator LLM + specialized agents + embedding retrieval under filtered \(\mathcal{M}(u,a,t)\) — filter **before** embed search (Inv-Scope), not after.

No contradiction to architecture locks; reinforces SHAREABLE dual-tier model.

---

## 2. Cross-cutting synthesis (Batch 2 → MoDeX)

### 2.1 Reinforced agreements
1. **Tiered stores + async consolidation** (MemoryOS, LightMem, MAGMA) validate L0 cheap / L3 expensive-offline.
2. **Typed multi-relation graphs** (MAGMA, AriGraph) beat single similarity graph for why/when/entity questions.
3. **CRUD memory ops** appear everywhere (Mem0, Memory-R1); MoDeX should keep the enum but govern DELETE.
4. **Eval must include SF + adversarial abstain** (MemoryAgentBench, LoCoMo) — not only friendly QA.
5. **Privacy is contextual + IFC**, not keyword redaction (ConfAIde, Fides).

### 2.2 Disagreements / traps
| Trap | MoDeX stance |
|------|----------------|
| FIFO drop of durable persona/KB (MemoryOS) | Never FIFO-drop sealed Anchors |
| EM-maximizing DELETE (Memory-R1) | SUPERSEDES + audit; disputed allowed |
| Hard-remove outdated edges (AriGraph) | Invalidate + retain audit |
| Prompt-only privacy (fails ConfAIde) | Capability + labels + promotion gates |
| Skills as free-text memories (vs Voyager code) | Keep procedural artifacts separate |

### 2.3 No architecture-lock contradictions
Nothing in this batch forces a change to Anchors+Evidence / L0–L4 / sealed capability packs. Strongest additive pressure: **IFC labels on planner context** (Fides) and **SF eval slice** (MemoryAgentBench) — both already compatible with existing locks; capture in research memos / eval plans only.

---

## 3. CORPUS INDEX (Batch 2)

| paper | year | deep-read? | one-paragraph insight | MoDeX relevance |
|-------|------|------------|----------------------|-----------------|
| MemoryOS (2506.06326) | 2025 | **FULL** | STM pages+chains / MTM segmented paging+heat / LPM persona queues; FIFO+heat eviction. | Tiering + heat ranking; avoid FIFO loss of Anchors. |
| LightMem (2510.18866) | 2025 | **FULL** | Sensory pre-compress + topic STM + soft insert / offline parallel sleep-time updates; major token savings. | Cheap L0 filter; async cognify; cost model. |
| MAGMA (2601.03236) | 2026 | **FULL** | Multi-graph temp/causal/sem/entity; intent-adaptive beam traversal; fast ingest + slow consolidation. | Edge-type hygiene; intent-routed hydrate; provenance linearization. |
| Memory-R1 (2508.19828) | 2025 | **FULL** | RL (PPO/GRPO) Memory Manager ADD/UPDATE/DELETE/NOOP + Answer Agent; EM rewards. | Learned controllers later; map DELETE→SUPERSEDES; add governance rewards. |
| ConfAIde (2310.17884) | 2023 | **FULL** | Four-tier contextual-integrity privacy benchmark; free-form leakage persists even when binary privacy Q looks OK. | Promotion gates; pack privacy–utility; generation probes. |
| Fides (2505.23643) | 2025 | **FULL** | IFC planner with conf×integ labels, policy engine, selective variables, quarantined typed inspect; NI + explicit secrecy. | Labelled handoff/tool I/O; declassify schema; Inv-Scope. |
| LoCoMo (2402.17753) | 2024 | **FULL** | ~9k-token, 19-session persona+event-graph dialogues; QA incl. adversarial; event summarization; multimodal. | Temporal/multi-hop/adversarial eval harness. |
| MemoryAgentBench (2507.05257) | 2025 | **FULL** | AR/TTL/LRU/SF competencies; incremental chunk protocol; FactConsolidation conflict slice. | MoDeX eval matrix + SUPERSEDES tests. |
| AriGraph (2407.04363) | 2024 | **FULL** | Semantic KG + episodic co-observation hyperedges; outdated edge removal; semantic→episodic retrieve. | Evidence co-observation; invalidate≠delete. |
| Reflexion (2303.11366) | 2023 | **FULL** | Actor/Evaluator/Self-Reflection; verbal lessons in bounded episodic `mem`. | Reflection→candidate Anchors; not auto-share. |
| Voyager (2305.16291) | 2023 | **FULL** | Skill library of verified code indexed by description embeddings; retrieve-to-compose. | Procedural memory layer separate from Anchors. |
| Collaborative Memory (2505.18279) | 2025 | **FULL extras** | Dual bipartite permissions; \(\mathcal{M}(u,a,t)\) closure; versionable read/write policies. | Already in SHAREABLE; extras reinforce filter-before-retrieve. |

---

## 4. Source fetch log (Batch 2)

| ID | Fetch path |
|----|------------|
| 2506.06326, 2510.18866, 2601.03236, 2508.19828, 2310.17884, 2402.17753, 2507.05257, 2303.11366, 2305.16291, 2505.18279 | `arxiv.org/html` → plaintext |
| 2505.23643, 2407.04363 | `arxiv.org/pdf` → `pdftotext` (HTML/ar5iv insufficient) |

---

*End of Batch 2. Mechanism detail preferred over buzzwords; no invented experimental results.*
