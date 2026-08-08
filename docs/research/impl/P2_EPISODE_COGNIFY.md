# P2 — Episode Segmentation & Cognify (Implementation Deep-Read)

> **Date:** 2026-08-08  
> **Pillar:** L0 span → L2 Episode → trigger L3 promotion → L4 recompile  
> **Method:** Full arXiv HTML/PDF body reads (not abstracts). Mechanism cards extract boundary detectors, STM→MTM→LTM migration, cognify/compaction, chapterization, recurrence consolidation, and surprise signals.  
> **Design locks:** `WORKSTREAM_AND_PROMOTION_V1.md` §3; `PARALLEL_COMPOSE_AND_HOOKS_V1.md` PRE_COMPACT; `IMPLEMENTATION_FROM_LITERATURE.md` §4.  
> **Companions:** `P1_CAPTURE_WORKING.md` (STM pages); `P3_ANCHORS_GRAPH.md` (promotion after episode).

---

## 0. Honesty table

| Bucket | Count | Notes |
|--------|------:|-------|
| **FULL deep-read (this pillar pass)** | **39** | Prior 28 + Voyager/Larimar/MemAgent/LoCoMo/LongMemEval/RETRO/AriGraph/MemoryAgentBench/RecSumDialogue/surveys; cards below |
| Must-list papers FULL | **22** | Nemori…MemOS + MemoryBank + EST/topic-seg extras |
| Overlap with prior AGENT_MEMORY / P3 memos | 12 | Re-read for cognify algorithms/constants |
| Abstract-only / stub in this memo | **0** | Queued IDs stay in `CORPUS_INVENTORY.md` |

**Target ≥25 FULL mechanism cards: met (39).** Combined with P1 KV/hooks pass + P3/P4 inventory, corpus FULL ledger grows by the newly marked IDs below.

---

## 1. MoDeX mapping (P2 surface)

| MoDeX object | Literature analogue |
|--------------|---------------------|
| L0 Observation span | MemoryOS STM pages; MemGPT FIFO; RecMem subconscious; LightMem sensory+topic-STM |
| L1 WorkingState | MemGPT working context; MemoryOS chain meta; SCM flash memory |
| L2 Episode | Nemori narrative episode; ES-Mem event unit; EM-LLM surprise segment; Graphiti episode node; MemoryOS MTM segment |
| Boundary | EST cut (ES-Mem/Nemori/EM-LLM); MemoryOS chain-reset; PRE_COMPACT/SESSION_END hooks |
| Cognify | Nemori episodic integration + predict–calibrate; LightMem sleep-time; RecMem recurrence consolidate; HEMA/RecSum hierarchical summarize |
| Heat / eviction | MemoryOS Heat; MemoryBank Ebbinghaus strength; MemGPT flush; StreamingLLM sinks |
| Boundary text | ES-Mem refined boundary representation (coarse retrieve anchor) |
| Promotion signal | RecMem θ_count; MemoryOS Heat≥τ; Nemori prediction gap; Memory-R1 when-to-store |

**Research distinction (locked):** Episode boundary = chapter *inside* a workstream. Workstream identity = which objective lane. Never create a new workstream on every episode cut (`WORKSTREAM_AND_PROMOTION_V1` §2.8).

---

## 2. Mechanism cards (FULL papers)

### 2.1 Nemori / What Deserves Memory — `2508.03341` · **FULL**

**Thesis.** Assess experience utility at *distillation time* via prediction error (Predictive Coding), not only at retrieval or post-hoc access heat.

**Episodic Memory Integration (three submodules).**
1. **Local Message Partitioning** — LLM groups buffer \(\mathcal{B}_t\) into raw episodes \(\mathbf{P}\) with **high sensitivity** to topic/intent/temporal/structural shifts (prompt: split when relevance <30%, idle >30 min, explicit topic phrases; prefer 2–15 msgs/episode; when in doubt, split).
2. **Narrative Episode Generation** — each raw \(P_j\) → narrative \(N_j\) + episodic cue \(c_j\); dual-mode retrieve (narrative for efficiency, raw for precision).
3. **Associative Memory Integration** — stitch episodes split by observation-window limits.

**Semantic Knowledge Distillation.**
1. Anticipatory schema \(\hat{P}_{in}\) from cue \(c_{in}\) + Top-\(K_s\) semantic facts with \(\mathrm{sim}>\tau\).
2. Prediction-error distillation: extract \(\mathcal{K}_{in}\) = what in \(P_{in}\) *deviates from* \(\hat{P}_{in}\).
3. Agnostic consolidation into semantic store.

**Constants (paper).** \(\tau=0.70\); \(K_e=K_m=5\), \(K_s=10\); retrieve \(k=10\) narratives (\(m=2k\)); top-2 include raw (\(r=2\)).

**MoDeX.** Soft boundary ≈ Nemori partition cues; cognify digest = narrative template (deterministic v1); Tier-B surprise = prediction gap vs WorkingState/Anchors — **candidate**, not auto-share.

---

### 2.2 ES-Mem — `2601.07582` · **FULL**

**Thesis.** EST boundaries are not only storage cuts — they are **retrieval anchors**.

**Dynamic Event Segmentation (two-stage).**
1. Topical coherence: mutual-information / coupling score \(I_t\); candidates \(\mathcal{C}=\{t\mid I_t\le\mathrm{Quantile}_q(\mathbf{I})\}\) with \(q\approx 0.35\) (bottom 35%).
2. Intent-aware refinement: local windows \(\mathcal{L}_t,\mathcal{R}_t\) of \(L\) turns; LLM labels \(\mathcal{Y}_{\mathrm{shift}}\) vs \(\mathcal{Y}_{\mathrm{cont}}\); accept if \(p_{\mathrm{eb}}(t)\ge\tau_c\).

**Layered memory unit.** \(M_i=\{\text{boundary text},\,s_i\text{ summary},\,r_i\text{ raw}\}\). Boundary text describes transition \(M_{i-1}\to M_i\).

**Coarse-to-fine retrieve.** Boundary scan (top-\(k\) anchors) → expand windows → score \(\alpha\cdot S_{\mathrm{ctx}}+(1-\alpha)S_{\mathrm{sum}}\) → fetch raw of top-\(K\).

**MoDeX.** Persist `boundary_summary` on Episode; hydrate may rank digests by boundary similarity first. Soft boundary detector can use MI/quantile heuristic without LLM in v1.

---

### 2.3 EM-LLM — `2407.09450` · **FULL**

**Surprise boundary.** Token \(x_t\) is candidate boundary if
\[
-\log P(x_t\mid x_{<t}) > T,\quad T=\mu_{t-\tau:t}+\gamma\,\sigma_{t-\tau:t}.
\]
Moving-window threshold adapts; \(\gamma\) controls sensitivity (paper PG-19 uses \(\gamma=10^{-3}\) scale experiments).

**Boundary refinement (Algorithm 1).** Treat attention-key similarity as adjacency \(A\); between consecutive surprise boundaries \((\alpha,\beta)\), pick \(\hat\beta\) maximizing modularity (or min conductance). Complexity \(\mathcal{O}(nm)\) with chunk size \(m\).

**Retrieval.** Similarity buffer \(k_s\) (k-NN on event reps) + contiguity buffer \(k_c\) (neighbors \(\pm n\)); keep initial tokens + local context (StreamingLLM kinship).

**MoDeX.** Optional soft signal: tool/test surprise or Anchor contradiction ≈ Bayesian surprise. Do **not** require KV-cache modularity in v1; keep modularity idea as future refinement if embeddings of span windows are available.

---

### 2.4 RecMem — `2605.16045` · **FULL**

**Thesis.** Eager per-turn LLM consolidation is overkill; consolidate on **recurrence**.

**Subconscious layer.** Every interaction embedded lightly; always retrievable.

**Trigger.** For new unit \(s_i\), retrieve top-\(k\); \(\mathcal{R}_i=\{s_j\mid\cos\ge\theta_{\mathrm{sim}}\}\); consolidate iff \(|\mathcal{R}_i|\ge\theta_{\mathrm{count}}\).

**Episodic.** Merge-first if nearest episode \(\cos\ge\theta_{\mathrm{sim}}\); else build timestamp-sorted cluster → LLM episodic narratives.

**Semantic refinement.** After episode write, extract fine facts omitted by summary (grounds Anchors).

**Constants.** Casual: \(\theta_{\mathrm{sim}}=0.7\), \(\theta_{\mathrm{count}}=5\). Task-oriented: \(0.6\), \(4\). Retrieve budgets \(k_{\mathrm{sub}}=10\), \(k_{\mathrm{epi}}=5\), \(k_{\mathrm{sem}}=10\). Up to **87%** construction-token reduction vs eager Mem0/A-Mem.

**MoDeX.** Map to Tier-B recurrence with eng default \(\theta_{\mathrm{count}}=3\) (denser coding threads — lock already in promotion doc). Subconscious = L0 retained until cognify; never delete rare but critical one-shots (RecMem caveat) — Tier-A explicit remember bypasses recurrence.

---

### 2.5 MemoryOS — `2506.06326` · **FULL**

**Tiers.** STM (fixed FIFO dialogue pages + chain meta) → MTM (segmented paging) → LPM (persona/KB/traits).

**Page.** \(page_i^{\mathrm{chain}}=\{Q_i,R_i,T_i,meta_i^{\mathrm{chain}}\}\). Chain meta: LLM decides continue vs **reset** on topic discontinuity, then summarizes chain.

**Segment membership.**
\[
\mathcal{F}_{\mathrm{score}}=\cos(\mathbf{e}_s,\mathbf{e}_p)+\mathrm{Jaccard}(K_s,K_p);\quad
\mathrm{merge\ if\ }\mathcal{F}_{\mathrm{score}}>\theta.
\]
Paper default \(\theta=0.6\).

**Heat.**
\[
\mathrm{Heat}=\alpha N_{\mathrm{visit}}+\beta L_{\mathrm{interaction}}+\gamma R_{\mathrm{recency}},\quad
R_{\mathrm{recency}}=\exp(-\Delta t/\mu),\ \mu=10^7\mathrm{s}.
\]
Evict lowest Heat when MTM full; if \(\mathrm{Heat}\ge\tau=5\) promote traits/facts to LPM then reset \(L_{\mathrm{interaction}}\).

**Retrieve.** All STM; MTM two-stage top-\(m\) segments then top-\(k=10\) pages; LPM top-10 KB/traits.

**MoDeX.** STM→L0/L1; MTM segment→L2 Episode; LPM→L3 **candidates** only (append+SUPERSEDES, never trait overwrite / auto-share).

---

### 2.6 LightMem — `2510.18866` · **FULL**

**Atkinson–Shiffrin inspired.**
1. **Light1 sensory:** pre-compress tokens (LLMLingua-2 / entropy retain above percentile).
2. **Light2 topic-aware STM:** group by semantic/topic similarity into segments (not fixed windows); flush when token threshold `th` hit → summarize.
3. **Light3 LTM:** soft-insert with timestamp online; **sleep-time** offline parallel update queues (Top-\(k\) later similar entries with \(t_j\ge t_i\)).

**Efficiency.** Up to ~38× token / ~30× API reduction vs eager baselines on LongMemEval; sleep-time improves fidelity without online latency.

**MoDeX.** Cognify online path stays cheap (deterministic digest); schedule sleep-time job for LLM narrative polish + promotion. Enforce update direction \(t_{\mathrm{new}}\ge t_{\mathrm{old}}\).

---

### 2.7 Graphiti / Zep — `2501.13956` · **FULL**

**Episode subgraph.** Non-lossy episodic nodes \(n_i\in\mathcal{N}_e\) with reference time \(t_{\mathrm{ref}}\); semantic entities/facts build *on top of* episodes; communities optional.

**Ingest.** Episode (+ reflection window **n=4** prior messages) → NER/entity resolve → fact extract → bi-temporal invalidate on contradiction.

**MoDeX.** Episode is provenance root; cognify **must** keep `observation_ids` / span; never replace episodes with Anchors-only store.

---

### 2.8 MemGPT — `2310.08560` · **FULL**

**Main context.** System (RO) + working context (RW via functions) + FIFO queue; index-0 = recursive summary of evicted messages.

**Pressure / flush.**
- Warning at **~70%** context → system message so LLM can archive to working/archival.
- Flush at **~100%** → evict **~50%** oldest queue messages; regenerate recursive summary; evicted stay in recall DB forever.

**MoDeX.** PRE_COMPACT = hard cognify *before* IDE compact (hooks lock). Map archival writes → Episode + Anchor candidates; recursive summary → Episode digest / WorkingState notes — not sole truth.

---

### 2.9 SCM (Self-Controlled Memory) — `2304.13343` · **FULL**

**Components.** LLM agent + memory stream + **memory controller**.

**Controller gates.**
1. Activate memory? (skip for chitchat).
2. Summary vs full? Assess when item >**800** tokens **and** activated total >**2000**.

**Flash vs activation.** Short-term = previous segment; long-term = activation memory from stream.

**MoDeX.** Cognify controller: skip soft cognify on trivial lint/formatter spans; when packing digests under budget, prefer summary; keep raw Observation pointers.

---

### 2.10 HEMA — `2504.16754` · **FULL**

**Dual memory.** Compact Memory (always-visible running one-sentence / hierarchical summary) + Vector Memory (episodic chunks).

**Hierarchy.** Beyond long dialogues, **two-level summary-of-summaries** eliminates cascade errors; ablation: SoS needed with semantic forgetting.

**Semantic forgetting.** Prune low-salience vector entries (~bottom 0.5% salience in paper) — recall drop small, latency improves.

**MoDeX.** Episode digest = compact chapter; optional offline recursive SoS over episode tree for long workstreams (>~1000 turns / many episodes). Forgetting = rank/evict L2 heat, **not** hard-delete Anchors.

---

### 2.11 Cognitive Weave — `2506.08098` · **FULL**

**Insight Particles + STRG.** Nexus Weaver orchestrates lifecycle; Cognitive Refinement triggers: temporal, significant event, resource saturation, fragmentation metrics.

**Insight synthesis.** Compress raw history into higher-level memories (not only store utterances).

**MoDeX.** Sleep-time / offline cognify triggers mirror refinement conditions; L3 Anchors = synthesized insights with provenance — refinement proposes candidates.

---

### 2.12 MemGAS / multi-granularity — `2505.19549` · **FULL**

**Index same dialogue at multiple granularities** (turn / session / topic / …). Router weights \(w^g\) by query type; initial node scores → **PPR** expand → LLM recognition filter.

**Fair retrieve setting.** Often top-3 sessions then expand.

**MoDeX.** Store Episode + Observation spans + topic keywords + Anchor statements as parallel granularities; hydrate uses multi-granularity (detail in P5). Cognify emits topic keywords for segment join.

---

### 2.13 Recursive Summarizing Books — `2109.10862` · **FULL**

**Tree decomposition.** Leaf summarize → height-1 composition → full tree; RL trains node policies with human feedback; each task is its own episode for training.

**Advantage.** Decomposition beats end-to-end for long books; errors accumulate with depth — need good leaf quality.

**MoDeX.** Offline chapterization: recursive summarize over Episode NEXT_IN chain when workstream archive or handoff needs macro digest; keep leaf Evidence pointers for citations.

---

### 2.14 Think-in-Memory (TiM) — `2311.08719` · **FULL**

**Store reasoning outcomes**, not only raw dialogues. Ops: **insert / merge / forget**; LSH retrieve before generate; post-hoc reflection updates memory.

**MoDeX.** Cognify may emit thought-like fields (`failed_approaches`, `next_steps`) as structured Episode slots; merge near-dup episode digests; forget only low-heat L2 under capacity — not Anchors.

---

### 2.15 MemoryBank — `2305.10250` · **FULL** (Zhong et al.)

**Storage.** Daily conversations + event summaries + evolving user portraits.

**Ebbinghaus updater.** Retention \(R=e^{-t/S}\) (paper form \(R=e^{-t/S}\)); memory strength \(S\) increases on recall/revisit; unused memories decay and may be forgotten for anthropomorphic companions.

**MoDeX.** Use decay for **Heat/recency ranking and L2 eviction**, never as sole delete of Anchors or Tier-A judgments. Strength bump on hydrate hit ≈ MemoryOS \(N_{\mathrm{visit}}\).

---

### 2.16 A-MEM — `2502.12110` · **FULL**

**Zettelkasten notes.** Each memory note links and **evolves on write** (not only at retrieval). Continuous memory evolution / adaptive management.

**MoDeX.** Cognify timing: after Episode write, run association/evolution pass (entity links, near-dup merge candidates) — write-time organization. Evolution must use SUPERSEDES (P4), not silent overwrite.

---

### 2.17 Mem-α — `2509.25911` · **FULL**

**Learned memory policy.** RL / preference optimization over when to store, update, forget — transfers from small train sets in paper setting.

**MoDeX.** v1 = **heuristic** cognify policy (this doc). Mem-α motivates later `agents-cli eval optimize` over cognify prompts/thresholds — do not ship RL controller in Phase A/B.

---

### 2.18 Memory-R1 — `2508.19828` · **FULL**

**Memory manager ops.** ADD / UPDATE / DELETE / NOOP with preference for UPDATE over DELETE+ADD. Learns *when to store*.

**MoDeX.** Cognify→promotion: prefer UPDATE/SUPERSEDES; map DELETE→INVALIDATE+audit. “When to store” for L3 ≠ every Episode field — only promotion ladder.

---

### 2.19 MAGMA — `2601.03236` · **FULL**

**Multi-graph / multi-aspect agent memory.** Separates episodic vs semantic structures; hierarchical/migrate patterns across graphs.

**MoDeX.** Keep Episode graph (NEXT_IN, MENTIONS) separate from Anchor fact graph; migration STM→MTM→LTM is cross-layer, not flatten-to-one-KG.

---

### 2.20 StreamingLLM — `2309.17453` · **FULL**

**Attention sinks.** Window attention collapses if first tokens evicted; keep **≥4 initial tokens** + recent window. Cache size ≠ monotonic perplexity gains.

**MoDeX under pressure.** Pin: system instructions, workstream id, active constraints, WorkingState head. Evict middle episode digests first (also Lost-in-the-Middle). Cognify must externalize middle content to L2/L3 before window slide.

---

### 2.21 Lost in the Middle — `2307.03172` · **FULL**

**U-shaped use of context.** Performance best when relevant info at **beginning or end**; middle degrades.

**MoDeX packing (cognify output → L4).** Survival Anchors at **start**; WorkingState + next_step at **end**; episode digests only in middle if budget remains. Cognify summaries should be short enough that hydrate can place newest digest near edges.

---

### 2.22 MemOS — `2507.03724` · **FULL**

**MemCube lifecycle.** Generated → Activated → Merged → Archived → Expired. Atomic metadata: provenance, origin, semantic type, timestamps, permissions.

**Fuse / archive.** Consolidation is first-class OS operation, not ad-hoc summary.

**MoDeX.** Episode status FSM: `open → sealed → archived`; cognify seals; sleep-time may merge; archive on workstream archive. MemCube fields → Episode + Observation provenance columns.

---

### 2.23 Unsupervised Dialogue Topic Segmentation — `2305.02747` · **FULL**

**DialSTART.** Topic-aware utterance reps via neighboring utterance matching + pseudo-segmentation; combine with dialogue coherence; TextTiling-style cuts on similarity dips.

**MoDeX.** Cheap soft detector: embedding discontinuity between consecutive Observation windows + Jaccard file/entity sets (no LLM).

---

### 2.24 HyperSeg — `2308.10464` · **FULL**

**HDC topic segmentation.** Boundary score = cosine between surrounding utterance embeddings in hyperdimensional space; pick low-similarity boundaries; ~10× faster than neural baselines; improves downstream summarization.

**MoDeX.** Optional CPU-cheap boundary scorer for IDE-side soft cuts when MI stats unavailable.

---

### 2.25 Granularity-Aware Dialogue Topic Segmentation — `2512.17083` · **FULL**

**When F1 fails.** Topic-seg evaluation must be granularity-aware; over-segmentation vs under-segmentation trade off differently for summarization vs QA.

**MoDeX eval.** Cognify fixtures must score both **over-cut** (too many tiny episodes) and **under-cut** (topic mix); do not optimize boundary F1 alone.

---

### 2.26 Generative Agents — `2304.03442` · **FULL** (supporting P2)

**Importance accumulation → reflection.** When sum of importance since last reflection crosses threshold, consolidate memories into higher-level insights.

**MoDeX.** Soft boundary / cognify trigger: `importance_sum ≥ EPISODE_IMPORTANCE_THRESHOLD` (default 3.5 with importance∈[0,1]) per workstream lock.

---

### 2.27 Mem0 — `2504.19413` · **FULL** (supporting — eager consolidation foil)

**Eager extract every message pair** with ADD/UPDATE/DELETE/NOOP. RecMem/LightMem critique: costly.

**MoDeX.** Do not cognify-every-turn; boundary + recurrence gated.

---

### 2.28 IMPLEMENTATION / hooks corpus — Claude+Cursor PRE_COMPACT docs · **FULL**

**Hard boundary.** PreCompact / preCompact must cognify synchronously (best-effort): Anchors first, seal handoff, then allow compact. Exit-block only if emergency snapshot fails.

**MoDeX.** Hard reasons: `PRE_COMPACT`, `SESSION_END`, `modex cognify|handoff`, workstream switch, idle ≥ `IDLE_BOUNDARY_MIN`.

---


### 2.29 Voyager — Procedural skill library — `2305.16291` · **FULL**

**Thesis.** Lifelong procedural memory as an executable **skill library** indexed by description embeddings; curriculum + iterative prompting with environment feedback.

**Write.** On task success, store skill program + natural-language description; complex skills compose simpler ones.

**Read.** Embed goal → retrieve skills → propose/execute/refine.

**Forget / conflict.** Library grows; near-duplicate skills need replace/versioning.

**FAILURE MODES.** Hallucinated skills; retrieving nearly-right wrong skill.

**MoDeX.** Eng analogue = runbooks / fix playbooks as Episode `kind=skill` with code + preconditions. Do **not** mix procedural skills with factual Anchors. Cognify trigger: test/build success after a debugging chapter.

---

### 2.30 Larimar — Episodic memory control — `2403.11901` · **FULL**

**Thesis.** Controllable episodic **write / read / forget** without full retrain (neuroscience-inspired distributed memory + controllers).

**Ops.** Learned gates for one-shot knowledge updates and selective forgetting.

**FAILURE MODES.** Controller mis-gates; hard forget without audit.

**MoDeX.** Expose CLI `memory write|read|forget` but implement forget as **invalidate + audit**, never hard-erase Evidence. Controllers may suggest ops; SQLite executor enforces schema + scope.

---

### 2.31 MemAgent — Multi-conv RL memory — `2507.02259` · **FULL**

**Thesis.** RL-trained memory control reshapes long-context / multi-conversation retention policies that are hard to hand-tune.

**FAILURE MODES.** Reward hacking; expensive training; weak OOD transfer.

**MoDeX.** v1 stays heuristic (RecMem recurrence + Heat + HARD hooks). Log outcome rewards (test pass/fail, user accept/reject) so a later MemAgent-style policy can be trained offline — do not block shipping on RL.

---

### 2.32 LoCoMo — Very long-term conversational memory eval — `2402.17753` · **FULL**

**Thesis.** Benchmark multi-session ultra-long dialogues (~10–16k+ tokens) with single-hop / multi-hop / temporal / open-domain / adversarial probes.

**MoDeX.** Cognify eval must include temporal-update and adversarial memory items; measure SUPERSEDES/invalidation correctness, not only F1 (see fixtures §8 — extend with LoCoMo-style temporal flips).

---

### 2.33 LongMemEval — Long-term interactive memory — `2410.10813` · **FULL**

**Thesis.** Systematic chat-assistant memory benchmark (LongMemEval-S used at ~115k avg tokens in RecMem). Probes extraction, multi-session reasoning, knowledge updates, **abstention**.

**MoDeX.** Add abstention fixtures when Evidence conflicts; knowledge-update questions are SUPERSEDES probes after cognify+promote.

---

### 2.34 RETRO — Retrieval-enhanced transformers — `2112.04426` · **FULL**

**Thesis.** Chunked retrieval + chunked cross-attention over a huge frozen datastore.

**MoDeX.** Long Episode bodies need a **chunk sub-index** (512–1024 tokens); do not embed a 10k-token episode as a single vector only. Cognify digests point to chunk IDs for Evidence expansion.

---

### 2.35 AriGraph — KG world model + episodic memory — `2407.04363` · **FULL**

**Thesis.** Structured world-model KG extracted from observations, paired with episodic traces for planning/retrieval.

**MoDeX.** After Episode seal, async OpenIE/entity edges into P3 graph — never block L0 capture on extraction latency (aligns with MAGMA dual-stream).

---

### 2.36 MemoryAgentBench — Incremental multi-turn eval — `2507.05257` · **FULL**

**Thesis.** Evaluate memory under incremental multi-turn interactions (streaming), not only static post-hoc QA.

**MoDeX.** Integration tests must stream hooks→L0→cognify→query; report maintenance tokens/latency alongside accuracy (RecMem/LightMem cost lesson).

---

### 2.37 Recursively Summarizing Enables Long-Term Dialogue Memory — `2308.15022` · **FULL**

**Thesis.** Hierarchical recursive session summaries beat BM25/DPR top-k (k=3/5) for multi-session dialogue coherence — but errors propagate.

**MoDeX.** `episode.digest` may be recursively rolled into workstream SoS; raw Observation spans remain authoritative. Never answer factual eng questions from digest alone.

---

### 2.38 Survey — From Storage to Experience — `2605.06716` · **FULL** (P2 lens)

**Thesis.** Memory evolves Storage → Reflection → **Experience** (cross-trajectory abstraction).

**MoDeX.** L2 cognify ≈ Reflection stage; L3 Anchors ≈ Experience-class. Do not auto-share Experience.

---

### 2.39 Survey — Memory in the Age of AI Agents — `2512.13564` · **FULL** (P2 lens)

**Thesis.** Forms / functions / dynamics taxonomy; write–manage–read loops; cites MemoryOS/LightMem/A-MEM/MemGPT lineage.

**MoDeX.** Dynamics = hook capture + sleep-time cognify cron; use survey bibliography for future FULL batches only after body reads.

---

## 3. Boundary policy (implement exactly)

Aligned with `WORKSTREAM_AND_PROMOTION_V1` §3 and hooks §B5, reconciled with MemoryOS/Nemori/ES-Mem.

```text
HARD (always cognify — ignore min_span for flush/seal; still extract Anchors):
  PRE_COMPACT          # Claude PreCompact / Cursor preCompact
  SESSION_END
  explicit modex cognify | modex handoff
  workstream_switch    # close old ws chapter; do not auto-join new
  idle_gap ≥ IDLE_BOUNDARY_MIN   # default 25 min (lock); eng may use 45

SOFT (cognify only if |span| ≥ min_span_events AND confidence high):
  goal_shift                 # user intent materially changes
  topic_discontinuity        # MemoryOS chain-reset; F_score < θ vs open segment
  file_cluster_shift         # Jaccard(files) < 0.2 AND goal_shift
  surprise / prediction_gap  # Nemori/EM-LLM; contradict WorkingState/Anchors
  importance_sum ≥ EPISODE_IMPORTANCE_THRESHOLD
  optional: MI quantile candidate + intent label (ES-Mem) if LLM path enabled

NEVER split on:
  formatter/lint-only edits
  trivial same-cluster file touch
  short clarifications continuing same goal
  routine tool noise

NEVER create new workstream solely because of episode boundary.
```

---

## 4. Boundary detector pseudocode

```text
function detect_boundary(obs, state) -> (kind, reason, confidence):
  # ---- HARD ----
  if obs.type in {PRE_COMPACT, SESSION_END}:
    return HARD, obs.type, 1.0
  if obs.type == EXPLICIT_COGNIFY or obs.type == HANDOFF_CMD:
    return HARD, "explicit", 1.0
  if obs.workstream_id != state.active_workstream_id:
    return HARD, "workstream_switch", 1.0
  if state.last_event_ts and (obs.ts - state.last_event_ts) >= IDLE_BOUNDARY_MIN:
    return HARD, "idle_gap", 1.0

  # ---- SOFT features ----
  conf = 0.0
  reasons = []

  if goal_shifted(obs, state.working):               # lexical/embed
    conf += 0.45; reasons.append("goal_shift")

  open_seg = state.open_segment_centroid
  f = F_score(open_seg, obs)   # cos(e_s,e_p) + Jaccard(K_s,K_p)
  if open_seg and f < θ_segment:
    conf += 0.35; reasons.append("topic_discontinuity")

  j = jaccard(state.files_in_flight, obs.files)
  if j < FILE_CLUSTER_SHIFT_JACCARD and "goal_shift" in reasons:
    conf += 0.20; reasons.append("file_cluster_shift")

  if prediction_gap(obs, state.anchors, state.working) >= SURPRISE_GAP_MIN:
    conf += 0.40; reasons.append("surprise")

  if state.importance_sum_since_boundary >= EPISODE_IMPORTANCE_THRESHOLD:
    conf += 0.30; reasons.append("importance")

  # optional ES-Mem light path
  if state.mi_enabled and mi_candidate(obs, state, q=q_MI):
    conf += 0.15; reasons.append("mi_candidate")

  if conf >= SOFT_BOUNDARY_CONF and not is_noise(obs):
    return SOFT, join(reasons), conf
  return NONE, "", 0.0


function on_observation(obs):
  append L0(obs)
  patch_working_state(obs)            # P1
  kind, reason, conf = detect_boundary(obs, state)
  log_boundary_candidate(obs, kind, reason, conf)
  if kind == HARD:
    cognify(state.workstream_id, reason, hard=True)
  elif kind == SOFT:
    schedule_cognify(state.workstream_id, reason, hard=False)
```

---

## 5. Exact MoDeX cognify algorithm

```text
function cognify(workstream_id, reason, hard=False):
  span = SELECT observations
         WHERE workstream_id = ? AND ts > last_boundary_ts
         ORDER BY ts ASC

  if not hard and len(span) < min_span_events:
    return SKIPPED_MIN_SPAN

  if not hard and is_noise_only(span):          # SCM-style skip
    return SKIPPED_NOISE

  # --- 1) Episode (L2) ---
  ep = Episode(
    id                = new_ulid("ep_"),
    repo_fingerprint  = span.repo,
    workstream_id     = workstream_id,
    session_ids       = unique(span.session_id),
    time_start        = span[0].ts,
    time_end          = span[-1].ts,
    branch            = mode(span.branch),
    summary           = digest_v1(span),              # deterministic first
    boundary_summary  = boundary_text(prev_ep, span), # ES-Mem-style ≤400 chars
    topic_keywords    = keywords(span),               # for F_score later
    files_touched     = top_files(span, 40),
    failed_approaches = extract_failures(span),
    next_steps        = extract_next(span),
    observation_ids   = ids(span),                    # NON-LOSSY provenance
    observation_span  = {from_ts, to_ts, count},
    importance        = aggregate_importance(span),
    heat              = init_heat(span),              # N_visit=0,L=|pages|
    visibility        = workstream_private,
    status            = sealed,
    cognify_reason    = reason,
    created_at        = now()
  )
  INSERT ep
  EDGE NEXT_IN(prev_ep → ep) if prev_ep on same workstream
  EDGE MENTIONS(ep → entities extracted)

  # --- 2) Segment accounting (MemoryOS-style open segment) ---
  # If F_score(open_mtm_segment, ep) > θ_segment: merge keywords into segment
  # else open new MTM segment bucket (metadata only; Episode remains row)

  # --- 3) Promotion (do NOT auto-share) ---
  promotion.tier_A_B_C(span, ep)   # WORKSTREAM_AND_PROMOTION_V1
  # RecMem recurrence / Heat≥τ / prediction_gap → candidates (Tier B)
  # Explicit remember / judgment language → Tier A commit

  # --- 4) Write-time association (A-MEM timing) ---
  graph.associate(ep)              # links; near-dup episode merge *proposal*

  # --- 5) Compose + seal ---
  view = compose.project(workstream_id)   # P4 projection; no Layer-1 erase
  seal.mxp(view, recipients=acl.members(workstream_id), epoch++)

  # --- 6) L0 hygiene ---
  mark span compacted_at = now()
  rotate_payload_blobs(span, budget)      # may drop heavy payloads
  # NEVER delete Anchors here
  # NEVER delete observation rows needed for provenance (payload OK to rotate)

  state.last_boundary_ts = ep.time_end
  state.importance_sum_since_boundary = 0
  state.open_segment_centroid = refresh(ep)
  INSERT boundary_log(...)
  return ep


function digest_v1(span) -> str:   # no LLM required
  """
  Episode {time_start}–{time_end} on {workstream}
  Goal: {working.goal}
  Files: {top files_in_flight}
  Events: {counts by ObservationType}
  Explicit remembers: {titles}
  Tool failures: {summaries}
  """
  return truncate(template, episode_summary_max_chars)


function sleep_time_cognify(workstream_id):   # LightMem / Cognitive Weave
  # Offline: optional LLM narrative polish of sealed episodes;
  # semantic refinement (RecMem); recursive SoS if episode_count > SoS_trigger;
  # Heat eviction if MTM over capacity; promote Heat≥τ signals to Tier B.
  ...
```

### Pressure path (MemGPT × StreamingLLM × PRE_COMPACT)

```text
on_context_pressure(level):
  if level >= 0.70: warn; favor soft cognify if importance high
  if PRE_COMPACT or level >= 1.00:
    cognify(..., hard=True)                 # MUST before eviction
    pin = {system, workstream_id, active_constraints, working_head}  # ~sinks
    evict_middle_episode_digests_from_context()
    # IDE may now compact / FIFO flush ~50% non-pinned L1 queue
```

### STM → MTM → LTM migration (MemoryOS adapted)

```text
L0/STM page full  → FIFO migrate oldest pages into cognify inbox (or wait boundary)
boundary/cognify  → seal L2 Episode (MTM segment membership via F_score)
Heat ≥ τ_heat     → Tier-B promotion signals toward L3 Anchors (LTM)
L2 over capacity  → evict lowest Heat episodes to archive (status=archived)
                    keep observation_ids pointers; drop bulky payloads only
```

---

## 6. Recommended constants

| Name | Default | Source / notes |
|------|---------|----------------|
| `θ_segment` | **0.60** | MemoryOS \(\mathcal{F}_{\mathrm{score}}\) |
| `α,β,γ` heat | **1.0, 1.0, 1.0** | start equal; TUNE after normalizing features |
| `μ_recency` | **1e7** s | MemoryOS |
| `τ_heat_promote` | **5** | MemoryOS → Tier B signal only |
| `θ_sim` | **0.70** | RecMem / Nemori τ |
| `θ_count` | **3** (promotion lock) / **4** (RecMem task paper default) / 5 casual | RecMem §3.6; keep lock=3 until eval says otherwise |
| `q_MI` | **0.35** | ES-Mem candidate quantile |
| `τ_c` intent | **0.5** (TUNE) | ES-Mem boundary confidence |
| `min_span_events` | **8** | avoid tiny chapters |
| `IDLE_BOUNDARY_MIN` | **25 min** | workstream lock (eng may raise to 45) |
| `EPISODE_IMPORTANCE_THRESHOLD` | **3.5** | GenAgents-style; importance∈[0,1] |
| `FILE_CLUSTER_SHIFT_JACCARD` | **0.2** | with goal_shift |
| `SOFT_BOUNDARY_CONF` | **0.55** | detector sum threshold |
| `SURPRISE_GAP_MIN` | **0.6** | normalized contradiction score |
| `episode_summary_max_chars` | **500** recommended / **1200** hard | MEMORY_SCHEMAS_V1 |
| `boundary_summary_max_chars` | **400** | ES-Mem anchor text |
| `MTM_page_top_k` | **10** | MemoryOS retrieve |
| `pressure_warn` | **0.70** | MemGPT |
| `pressure_flush` | **1.00** → evict ~**50%** | MemGPT |
| `attention_sinks_pin` | **4** conceptual slots | StreamingLLM |
| `scm_summary_item_tok` | **800** | SCM |
| `scm_summary_total_tok` | **2000** | SCM |
| `graphiti_reflection_n` | **4** | prior msgs into cognify context |
| `cognify_batch_hint` | **~20** events | MIRIX batching (P1) |
| `SoS_trigger_episodes` | **12** | HEMA/RecSum offline hierarchy |
| `sleep_time_cron` | offline / idle | LightMem |
| `llm_topic_loom` / `llm_episode_digest` | **off** v1 | deterministic first |
| `hard_boundaries` | PRE_COMPACT, SESSION_END, explicit, ws_switch, idle | never skip |

---

## 7. SQL — episodes + boundary_log

Compatible with `MEMORY_SCHEMAS_V1` Episode object; additive columns for cognify ops.

```sql
-- L2 episodes (sealed chapters)
CREATE TABLE IF NOT EXISTS episodes (
  id                TEXT PRIMARY KEY,          -- ep_...
  schema_version    TEXT NOT NULL DEFAULT 'modex.memory.v1',
  repo_fingerprint  TEXT NOT NULL,
  workstream_id     TEXT NOT NULL,
  session_ids_json  TEXT NOT NULL DEFAULT '[]',
  time_start        TEXT NOT NULL,             -- ISO-8601
  time_end          TEXT NOT NULL,
  branch            TEXT,
  summary           TEXT NOT NULL,             -- ≤1200
  boundary_summary  TEXT,                      -- ES-Mem ≤400
  topic_keywords_json TEXT NOT NULL DEFAULT '[]',
  failed_approaches_json TEXT NOT NULL DEFAULT '[]',
  next_steps_json   TEXT NOT NULL DEFAULT '[]',
  files_touched_json TEXT NOT NULL DEFAULT '[]',
  anchor_ids_json   TEXT NOT NULL DEFAULT '[]',
  entity_ids_json   TEXT NOT NULL DEFAULT '[]',
  observation_ids_json TEXT NOT NULL DEFAULT '[]',
  observation_count INTEGER NOT NULL DEFAULT 0,
  salient_evidence_ids_json TEXT NOT NULL DEFAULT '[]',
  importance        REAL NOT NULL DEFAULT 0.0,
  -- MemoryOS heat components
  n_visit           INTEGER NOT NULL DEFAULT 0,
  n_pages           INTEGER NOT NULL DEFAULT 0,
  last_access_ts    TEXT,
  heat              REAL NOT NULL DEFAULT 0.0,
  status            TEXT NOT NULL DEFAULT 'sealed',  -- open|sealed|archived
  cognify_reason    TEXT NOT NULL,             -- PRE_COMPACT|idle_gap|...
  visibility        TEXT NOT NULL DEFAULT 'workstream_private',
  embedding         BLOB,                      -- optional narrative embed
  created_at        TEXT NOT NULL,
  updated_at        TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_episodes_ws_time
  ON episodes(workstream_id, time_end DESC);
CREATE INDEX IF NOT EXISTS idx_episodes_heat
  ON episodes(workstream_id, heat DESC);
CREATE INDEX IF NOT EXISTS idx_episodes_status
  ON episodes(status);

-- NEXT_IN and MENTIONS live in edges table (P3); example:
-- INSERT INTO edges(src_id, dst_id, rel, ...) VALUES (prev_ep, ep, 'NEXT_IN', ...);

-- Boundary decisions (audit + eval)
CREATE TABLE IF NOT EXISTS boundary_log (
  id              TEXT PRIMARY KEY,            -- bl_...
  repo_fingerprint TEXT NOT NULL,
  workstream_id   TEXT NOT NULL,
  obs_id          TEXT,                        -- triggering observation if any
  ts              TEXT NOT NULL,
  kind            TEXT NOT NULL,               -- HARD|SOFT|NONE|SKIPPED_MIN_SPAN|SKIPPED_NOISE
  reason          TEXT NOT NULL,               -- PRE_COMPACT|topic_discontinuity|...
  confidence      REAL NOT NULL DEFAULT 0.0,
  features_json   TEXT NOT NULL DEFAULT '{}',  -- {f_score, jaccard_files, importance_sum, ...}
  episode_id      TEXT,                        -- set if cognify ran
  skipped         INTEGER NOT NULL DEFAULT 0,  -- 1 if cognify skipped
  created_at      TEXT NOT NULL,
  FOREIGN KEY (episode_id) REFERENCES episodes(id)
);

CREATE INDEX IF NOT EXISTS idx_boundary_ws_ts
  ON boundary_log(workstream_id, ts DESC);
CREATE INDEX IF NOT EXISTS idx_boundary_kind
  ON boundary_log(kind, reason);
```

**Heat recompute (SQL-shaped):**

```sql
UPDATE episodes
SET heat = (:alpha * n_visit)
         + (:beta  * n_pages)
         + (:gamma * EXP((JULIANDAY(last_access_ts) - JULIANDAY('now')) * 86400.0 / :mu)),
    updated_at = :now
WHERE id = :ep_id;
```

---

## 8. Eval fixtures for cognify

Place under `tests/fixtures/cognify/` (Phase A+). Each fixture is a JSONL observation stream + expected boundary/episode outcomes. Grade with boundary quality **and** downstream hydrate usefulness (granularity-aware — `2512.17083`).

### 8.1 Fixture catalog

| ID | Scenario | Expect |
|----|----------|--------|
| `C1_pre_compact_hard` | Mid-session PRE_COMPACT after 12 file_edits | HARD cognify; Anchors from explicit judgments persist; L0 marked compacted |
| `C2_session_end` | SESSION_END with 3 events only | HARD cognify despite `< min_span`; seal handoff |
| `C3_idle_gap` | 30 min idle then new USER_PROMPT | HARD `idle_gap`; new episode |
| `C4_topic_shift_soft` | auth/* work → billing/* + goal text change | SOFT boundary; 2 episodes; no new workstream |
| `C5_no_split_lint` | 15 formatter-only edits same goal | NO boundary; single open span |
| `C6_workstream_switch` | `modex workstream use other` | HARD; old ws episode sealed; no cross-ws merge |
| `C7_recurrence_promote` | Same rejection judgment in 3 sealed episodes | Tier-B candidate (≥θ_count); not `repo_shared_safe` |
| `C8_prediction_gap` | WorkingState expects cookies; tests fail CSRF | Soft/surprise cognify; candidate invalidation |
| `C9_min_span_skip` | Soft topic dip after 2 events | SKIPPED_MIN_SPAN; boundary_log row; no episode |
| `C10_heat_evict` | MTM over capacity; one cold segment | Lowest Heat → `archived`; Anchors untouched |
| `C11_pressure_flush` | Context 100% without PRE_COMPACT hook | Cognify then ~50% queue evict; sinks pinned |
| `C12_digest_pack` | Hydrate after cognify with tight budget | Newest digest near pack edge; Anchors start; no middle-only critical constraints |
| `C13_provenance` | Cognify then delete payload blobs | `observation_ids` remain; summary still cites span count |
| `C14_overcut_guard` | Rapid tool noise with tiny embedding jitter | Must not emit >1 episode / 8 events (granularity) |

### 8.2 Minimal fixture schema

```json
{
  "id": "C4_topic_shift_soft",
  "workstream_id": "ws_auth",
  "observations": ["obs_....jsonl lines"],
  "expect": {
    "episodes": 2,
    "workstreams": 1,
    "boundaries": [
      {"kind": "SOFT", "reason_contains": "goal_shift"},
      {"kind": "HARD", "reason": "SESSION_END"}
    ],
    "invariants": [
      "every episode has observation_ids non-empty",
      "no episode.visibility == repo_shared_safe",
      "anchors_from_tier_A status active"
    ]
  }
}
```

### 8.3 Metrics

| Metric | Definition |
|--------|------------|
| Boundary precision/recall | vs human/tool-annotated cuts (DialSeg-style) |
| Over-seg rate | episodes with `< min_span` except HARD |
| Topic purity | mean intra-episode file Jaccard |
| Provenance integrity | % episodes with resolvable observation_ids after payload rotate |
| Promotion hygiene | Heat/recurrence never alone sets `shareable=true` |
| Pack survival | critical constraints present after PRE_COMPACT fixture |

---

## 9. Anti-patterns

1. **Cognify every turn** — Mem0/eager cost; RecMem shows ≤87% waste.  
2. **Fixed every-N-turns episodes** — severs EST coherence (ES-Mem/Nemori).  
3. **One Observation = one L2 atom** — Graphiti episode is a *span*, not a message.  
4. **Drop L0 / skip Anchors on HARD PRE_COMPACT** — primary failure mode in IDE agents.  
5. **Heat or recurrence auto-share to repo** — violates promotion ladder / shareable policy.  
6. **LLM summary as only truth** without `observation_ids` — HEMA ablation: summary-only collapses.  
7. **Forgetting-curve hard-delete of Anchors** — MemoryBank decay is ranking; use SUPERSEDES/archive.  
8. **New workstream on every topic boundary** — contaminates identity model.  
9. **Flat FIFO as sole long-term store** — MemoryOS critique of MemGPT-only designs.  
10. **Bury cognify digests mid-pack as only carriers of constraints** — Lost in the Middle.  
11. **Silent in-place episode overwrite** — A-MEM evolution must become append+merge proposal.  
12. **Optimize boundary F1 only** — ignore granularity / hydrate utility (`2512.17083`).

---

## 10. Final cognify boundary rule set (lock summary)

```text
HARD = PRE_COMPACT | SESSION_END | explicit cognify/handoff
     | workstream_switch | idle ≥ IDLE_BOUNDARY_MIN(25m)

SOFT = (goal_shift ∧ span≥min_span)
     | (topic_discontinuity F_score<θ_segment ∧ span≥min_span)
     | (file_cluster Jaccard<0.2 ∧ goal_shift ∧ span≥min_span)
     | (surprise/prediction_gap ≥ SURPRISE_GAP_MIN ∧ span≥min_span)
     | (importance_sum ≥ 3.5 ∧ span≥min_span)

COGNIFY =
  seal Episode(digest_v1, boundary_summary, observation_ids, heat)
  → NEXT_IN → promotion.tier_A_B_C → associate → compose.project → seal.mxp
  → mark L0 compacted; never delete Anchors

MIGRATE = STM FIFO → (boundary) MTM Episode segments(θ=0.6)
        → Heat≥5 Tier-B signals → L3 candidates
        → low Heat archive under capacity

PRESSURE = warn@70% → HARD cognify@PRE_COMPACT/100% → pin sinks → evict middle
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-08-08 | Initial P2 impl deep-read synthesis (short). |
| 2026-08-08 | FULL-body expansion: 28 mechanism cards; boundary detector + cognify pseudocode; constants; SQL; eval fixtures; anti-patterns; inventory sync. |
