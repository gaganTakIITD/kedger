# Batch 24 — Survey Runway FULL (Kedger) — **honest deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Body-grounded mechanism cards (Intro/Method/Results) replacing 2026-08-08 abstract-template cards.  
> **Progress:** FULL 460 → **480**.  
> **Method:** Fulltext `/tmp/kedger-papers/full/{id}.txt` + agent deep-read cards.  
> **Kedger stages:** S1–S8  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers from body only.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body deep-read; deep-recard upgrade of Batch24) | **20** | `2412.15274`, `2412.15540`, `2501.00358`, `2501.01702`, `2501.05366`, `2501.06590`, `2501.12254`, `2502.03358`, `2503.07018`, `2503.08175`, `2503.09516`, `2504.12369`, `2504.12516`, `2504.13079`, `2504.13805`, `2504.20073`, `2504.21776`, `2505.15962`, `2505.16067`, `2505.16348` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs cached |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. Matrix — Memory-Augmented Agent Training for Business Document Understanding
**arXiv:2412.15274** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S4, S7 |
| **problem** | Enterprise invoice/document extraction (e.g., transport references) fails with plain LLM prompting; agents need domain expertise distilled from experience without manual tuning. |
| **representation** | Matrix: iterative explore→optimize loop; long-term memory M stores distilled actionable insights on task structure; trajectories τ=(o,a,…) over documents; progressive memory updates across epochs; compared vs Reflexion verbal feedback. |
| **write / read / forget** | Write: distilled insights into long-term memory after exploration epochs. Read: recall from M while acting on document. Forget: silent — no typed eviction; privacy anonymization of customer invoices only. |
| **conflict** | Silent on SUPERSEDES / contradictory Anchors. |
| **privacy** | Corporate invoice data sensitive; paper releases anonymized subset only; A.3 anonymization pipeline to prevent leakage of business info. |
| **Kedger lessons** | (1) S3 cognify should distill trajectory insights into reusable L3 cards, not store raw invoice text. (2) Epoch-wise memory optimize ≈ promote gate after held-out validation. (3) Optimized memory cut API calls ~8–21% — budget hydrate cost as SLI. (4) Never promote private_raw invoices into shared store; anonymize before S4. |
| **metric_impact** | +30.3% vs CoT single LLM; +35.2% vs vanilla agent; API-call reductions 8.12%/21.3% |
| **refine_candidate** | **yes — S3 experience-distill memory for domain document agents** |

---

### 2. MRAG — Modular Retrieval for Time-Sensitive QA (TempRAGEval)
**arXiv:2412.15540** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Off-the-shelf RAG retrievers fail time-sensitive questions that need temporal reasoning (not keyword/date match). |
| **representation** | TempRAGEval benchmark with temporal perturbations + gold evidence. MRAG trainless 3 modules: (1) Question Processing → main content + temporal constraint; (2) Retrieve/split/summarize on main content; (3) Semantic–Temporal Hybrid Ranking scores semantic vs temporal relevance separately. |
| **write / read / forget** | Read-only corpus retrieve; no persistent memory write. Forget: silent. |
| **conflict** | Mentions knowledge conflicts LLM↔passages as future/analysis; silent on typed inter-doc SUPERSEDES. |
| **privacy** | Silent (AntiLeak-Bench only as future extension). |
| **Kedger lessons** | (1) S7 hydrate must split temporal constraint from content query — do not embed whole utterance. (2) Hybrid ranker ≈ separate Anchor recency facet from semantic Evidence score. (3) TempRAGEval-style temporal perturbation fixtures for retrieve SLIs. (4) +9.3% AR@1 / +11% ER@1 / +4.5 EM&F1 — measure retrieve before answer. |
| **metric_impact** | +9.3% top-1 answer recall; +11% evidence recall; +4.5 EM and F1 on TempRAGEval |
| **refine_candidate** | **yes — S7 temporal-constraint modular retrieve** |

---

### 3. Embodied VideoAgent — Persistent Memory from Egocentric Video+Sensors
**arXiv:2501.00358** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S5, S7 |
| **problem** | Dynamic 3D scene understanding from egocentric video alone lacks persistent object state under occlusion/action. |
| **representation** | Builds on VideoAgent: temporal memory MT + new persistent object memory MO (SQL+features: ID/STATE/RO/3D bbox/OBJ&CTX feats); tools query_db/temporal_loc/spatial_loc/vqa; VLM-based memory update associates actions to target objects; history buffers; embodied action primitives. |
| **write / read / forget** | Write: construct/update MO entries from video+depth+pose; VLM updates STATE/relations on actions. Read: tool queries over MT/MO. Forget: silent — updates overwrite state fields. |
| **conflict** | Silent on contradictory object states / SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Structured object Anchors (fields) beat caption-only WorkingState for scene memory. (2) S3 VLM update = cognify on action perception before promote. (3) Tool-mediated hydrate over SQL/object DB mirrors Kedger graph query. (4) Gains Ego4D-VQ3D +4.9%, OpenEQA +5.8%, EnvQA +11.7% — ablate memory update vs static. |
| **metric_impact** | +4.9% Ego4D-VQ3D; +5.8% OpenEQA; +11.7% EnvQA |
| **refine_candidate** | **no (embodied modality outside core Kedger text path)** |

---

### 4. AgentRefine — Enhancing Agent Generalization via Refinement Tuning
**arXiv:2501.01702** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S3, S4, S8 |
| **problem** | Agent-tuning overfits held-in envs (memorize obs→action); fails held-out tasks and small perturbations; stuck repeating mistakes. |
| **representation** | AgentRefine: synthesize diverse envs/tasks; strong LLM refines erroneous actions from env feedback; instruction-tune on refinement trajectories (not only success demos); eval Alfworld/BabyAI/SciWorld/PDDL/Jericho held-in vs held-out. |
| **write / read / forget** | Write: training trajectories with error→refine steps (no online persistent store). Read: env observations. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S3 cognify should train on mistake→correct pairs, not only gold trajectories. (2) Held-out generalization > held-in memorization as promote gate. (3) Perturbation robustness SLI (Agent-FLAN −30.4% SR under action-desc noise). (4) Diversify thought/env synthesis before S4 commit of procedural Anchors. |
| **metric_impact** | Leads Agent-FLAN by 13.3% SciWorld SR; baseline drops ~25–30% under perturbation vs smaller drop for AgentRefine |
| **refine_candidate** | **yes — S3 refinement-tuning from failed trajectories** |

---

### 5. Search-o1 — Agentic Search + Reason-in-Documents for LRMs
**arXiv:2501.05366** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | o1-like long CoT LRMs hit knowledge insufficiency mid-reasoning; dumping raw retrieved docs breaks coherence. |
| **representation** | Agentic RAG: model emits search when uncertain; separate Reason-in-Documents module refines verbose docs into concise injected steps; batch inference over sequences; eval science/math/coding + 6 open-domain QA. |
| **write / read / forget** | Read: dynamic search mid-reasoning; refine before inject. Write: none persistent. Forget: silent (notes catastrophic forgetting of general skills in related LRM training). |
| **conflict** | Silent on doc–doc conflicts. |
| **privacy** | Silent — 'inject' means context injection not attack. |
| **Kedger lessons** | (1) Mid-why hydrate on uncertainty (FLARE-class) for LRM chains. (2) Never dump raw Evidence — Reason-in-Documents before pack compile. (3) Agentic RAG +23.2% EM vs standard RAG multi-hop (QwQ-32B). (4) Search-o1 +5.3% EM avg vs RAgent — measure refine-before-inject ablations. |
| **metric_impact** | Avg +4.7% vs RAgent-QwQ-32B; +29.6% EM vs RAG-QwQ on multi-hop; agentic RAG +23.2% EM vs standard RAG |
| **refine_candidate** | **yes — S7 Reason-in-Documents refine gate** |

---

### 6. ChemAgent — Self-Updating Library Memory for Chemical Reasoning
**arXiv:2501.06590** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Chemical multi-step calc fails cascade from wrong constants/steps; LLMs lack structured reusable sub-task memory. |
| **representation** | Dynamic library with 3 memories: Planning Mp, Execution Me (condition,sub-task,sub-solution units), Knowledge Mk; decompose→retrieve similar units by Llama3 embed cosine≥θ; self-create synthetic Me if miss; Evaluate&Refine; discard low-confidence units at construction. |
| **write / read / forget** | Write: library construction from dev set + runtime self-update. Read: retrieve Me/Mp/Mk per sub-task. Forget: discard units below confidence threshold / wrong assert. |
| **conflict** | Silent on SUPERSEDES between chemical constants. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Split L3 into plan/exec/knowledge facets like ChemAgent Mp/Me/Mk. (2) Sub-task atomic blocks as reusable Anchors with confidence gate. (3) Self-update library only after Evaluate&Refine — S4 promote. (4) Up to +46% GPT-4 SciBench; +10–15% vs StructChem — domain memory SLI. |
| **metric_impact** | Up to +46% (GPT-4) vs base; avg +37% with memory self-improve; +10% avg / +15% max vs StructChem |
| **refine_candidate** | **yes — S3 typed multi-memory library with confidence discard** |

---

### 7. Memory Storyboard — Two-Tier Temporal Segmentation for Streaming SSL
**arXiv:2501.12254** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S6 |
| **problem** | Streaming egocentric video SSL suffers non-stationarity + temporal correlation; flat replay buffers inefficient. |
| **representation** | Two-tier memory: short-term holds recent frames → event-segmentation storyboard segments → transfer to long-term; contrastive learning on storyboard frames; vs reservoir/MinRed; SAYCam/KrishnaCam. |
| **write / read / forget** | Write: STM→LTM transfer of storyboard segments. Read: replay from LTM for SSL. Forget: buffer capacity constraints (50K frames = 0.27%/2.01% of streams); implicit eviction by hierarchy. |
| **conflict** | Notes SimCLR loss can conflict with temporal contrastive objective — method tradeoff, not belief SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S2→S3 episode boundary = storyboard temporal segments, not fixed token windows. (2) Two-tier WorkingState vs L3 mirrors STM/LTM. (3) Cap LTM like 50K — measure % coverage. (4) Prefer temporal-aware replay over reservoir for session cognify. |
| **metric_impact** | Only method competitive with/above IID; beats streaming baselines on ImageNet readout + OAK detection |
| **refine_candidate** | **no (vision SSL; episode-boundary idea already covered)** |

---

### 8. Minerva — Programmable Memory Test Benchmark for LLMs
**arXiv:2502.03358** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7, S8 |
| **problem** | Static needle/passkey tests overfit and don't diagnose which memory ops fail (search/edit/match/state). |
| **representation** | Auto-generated atomic tests: search, recall, edit, match, compare, block-structured ops, stateful set updates; plus composite tasks; accuracy/ROUGE-L with CIs; Microsoft open code. |
| **write / read / forget** | Eval-only over context-as-memory; instructions to recall/edit/maintain state. Forget: discard actions in set-state tasks as eval ops. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Kedger S2 fixtures need Minerva-class atomic ops beyond needle-in-haystack. (2) Separate SLIs: localize vs edit vs state-maintain. (3) Auto-generated programmable tests reduce overfitting. (4) Use for WorkingState ≤4KiB regression suite. |
| **metric_impact** | Per-task accuracy/ROUGE-L; model-specific failure modes (odd-group, set updates) |
| **refine_candidate** | **yes — S2 programmable memory-op fixture suite** |

---

### 9. ImplexConv + TaciTree — Hierarchical Tree Memory for Implicit Multi-Session Dialogue
**arXiv:2503.07018** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Multi-session persona dialogue needs implicit reasoning (subtle/distant cues); flat RAG/long-context inefficient. |
| **representation** | ImplexConv: 2.5k examples × ~100 sessions, high implicitness. TaciTree: hierarchical multi-level summarization tree; level-based progressive retrieve; prune irrelevant subtrees early. |
| **write / read / forget** | Write: hierarchical summaries of history into tree. Read: level-wise refine retrieve. Forget: discard unrelated details / prune irrelevant subtrees. |
| **conflict** | Silent on SUPERSEDES; opposed vs supportive reasoning scenarios in dataset. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Cognify multi-session history into hierarchical summary tree, not flat Evidence pack. (2) Progressive level retrieve ≈ S5 expand with early prune. (3) ImplexConv 20% lower query–answer similarity — test implicit hydrate. (4) +30% retrieve acc with 40–60% fewer tokens vs RAG/MemoryBank. |
| **metric_impact** | +30% retrieval accuracy; 40–60% fewer tokens; F1 supportive 55.18% / opposed 14.84% |
| **refine_candidate** | **yes — S3/S5 hierarchical session tree hydrate** |

---

### 10. EPEAgents — Privacy-Enhancing Agents for Federated MAS
**arXiv:2503.08175** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | Federated multi-agent systems share context across heterogeneous privacy protocols / dynamic conversation graphs — privacy risk. |
| **representation** | EPEAgents embedded in RAG + context retrieval: minimize data flow to task-relevant agent-specific info only; Federated MAS concept vs classic FL; generated eval dataset; Privacy score metric. |
| **write / read / forget** | Read-path filtering at retrieve/RAG; share minimized snippets. Write: silent on persistent store. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Core: up to 97.62% privacy protection effectiveness; GPT-o1 Privacy score only 15.89 without EPEAgents in finance scenario; Claude-3.5 +71.96% Privacy with EPEAgents. |
| **Kedger lessons** | (1) S6/S7 pack compile must minimize cross-agent Evidence to Inv-Scope fields. (2) Heterogeneous privacy protocols → per-agent ACL facets. (3) Privacy score SLI alongside task accuracy for multi-agent hydrate. (4) Central coordinator capability bottlenecks privacy — don't weaken seal agent. |
| **metric_impact** | Privacy protection up to 97.62%; large Privacy-score lifts (e.g., +71.96% Claude-3.5) |
| **refine_candidate** | **yes — S6/S7 EPE-style minimize-share at hydrate** |

---

### 11. Search-R1 — RL for Multi-Turn Search-Augmented Reasoning
**arXiv:2503.09516** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Prompting LLMs to use search at inference is suboptimal; need learned multi-turn search policy. |
| **representation** | RL (outcome reward) on trajectories with autonomous multi-query search; retrieved-token loss masking for stable training; seven QA datasets; Qwen2.5-3B/7B. |
| **write / read / forget** | Read: real-time search during reasoning. Write: policy update via RL (weights), not symbolic memory. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Learn search policy with RL, not only prompt ReAct. (2) Mask retrieved tokens in loss — don't backprop through Evidence text. (3) +24%/+20% relative vs RAG baselines (7B/3B). (4) Multi-turn search count as hydrate budget SLI. |
| **metric_impact** | +24% (7B) / +20% (3B) relative vs RAG; masking improves over unmasked |
| **refine_candidate** | **yes — S7 RL search policy with retrieved-token mask** |

---

### 12. WorldMem — Long-term Consistent World Simulation with Memory Bank
**arXiv:2504.12369** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S5, S7 |
| **problem** | World simulators lose 3D/long-term consistency when context window discards past frames. |
| **representation** | Memory bank of units (frames + states: poses, timestamps); state-aware memory attention retrieves relevant past frames across viewpoint/time gaps; models static + dynamic evolution. |
| **write / read / forget** | Write: store memory frames+states. Read: state-aware attention retrieve. Forget: prior methods discard generated content — WorldMem retains bank; retrieval ~10–20% of inference with 1000 candidates. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Pair Evidence with state metadata (pose/time) for retrieve. (2) Don't discard prior session frames from WorkingState without L3 spill. (3) State-aware attention > naive recent-k window. (4) Progressive sampling ablation (PSNR 23.98) informs memory train curriculum. |
| **metric_impact** | Outperforms baselines on PSNR/LPIPS/rFID long-term consistency; retrieve 10–20% inference cost @1000 |
| **refine_candidate** | **no (vision world-model; metadata-retrieve lesson noted)** |

---

### 13. BrowseComp — Benchmark for Persistent Web Browsing Agents
**arXiv:2504.12516** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Need simple, verifiable measure of agent persistence/creativity finding hard entangled web info. |
| **representation** | 1,266 short-answer questions requiring multi-hop browsing; easy verify vs reference; analogous to coding contests for browse agents; test-time compute scaling curves. |
| **write / read / forget** | Eval-only online browse read. Write: none. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Authors request not to leak examples online to prevent training contamination / agent cheating. |
| **Kedger lessons** | (1) Add BrowseComp-class fixtures for S7 web hydrate persistence. (2) Short verifiable answers = cheap CI oracles. (3) Accuracy scales with test-time browse compute — budget interactions. (4) GPT-4o browse still ~1.9% — don't claim web hydrate solved. |
| **metric_impact** | 1,266 Qs; GPT-4o browse 0.6→1.9%; Deep Research ~50%; multi-attempt +15–25% |
| **refine_candidate** | **yes — S7 BrowseComp-style persistence SLI** |

---

### 14. Madam-RAG / RamDocs — RAG under Ambiguity + Misinformation Conflict
**arXiv:2504.13079** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S7, S8 |
| **problem** | Real RAG faces simultaneous ambiguity, conflicting sources, noise/misinfo — prior work treats factors in isolation. |
| **representation** | RamDocs dataset mixes ambiguity+misinfo+noise. Madam-RAG: multi-agent multi-round debate + aggregator collates disambiguated answers and discards misinfo/noise; eval AmbigDocs, FaithEval, RamDocs. |
| **write / read / forget** | Read retrieved docs; agents debate; aggregator synthesizes. Write: none persistent. Forget: discard misinfo/noise via aggregator. |
| **conflict** | Core: multi-source conflict + ambiguity; +11.40% vs Astute RAG (Llama3.3-70B) on AmbigDocs; FaithEval +15.80%; RamDocs hard (≤32.60 EM). |
| **privacy** | Mentions malicious/adversarial retrieved content as robustness setting. |
| **Kedger lessons** | (1) ConflictSet must jointly handle ambiguity+misinfo, not single axis. (2) Multi-round debate + aggregator before S7 answer. (3) RamDocs as stress fixture (base ~32.6 EM). (4) Ablations: aggregator +19% FaithEval; rounds matter without aggregator. |
| **metric_impact** | +11.40% AmbigDocs; +15.80% FaithEval; aggregator +19% / rounds +5.30% ablations |
| **refine_candidate** | **yes — S4/S7 multi-agent conflict debate aggregator** |

---

### 15. LearnAct — Few-Shot Mobile GUI Agent from Demonstrations (LearnGUI)
**arXiv:2504.13805** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Mobile GUI agents fail on app diversity/user-specific tasks; massive pretrain ≠ personalization. |
| **representation** | LearnGUI: 2,252 offline + 101 online tasks with human demos. LearnAct multi-agent: DemoParser extracts knowledge; KnowSeeker retrieves relevant demo knowledge; ActExecutor executes with demos. |
| **write / read / forget** | Write: parse demos into knowledge. Read: retrieve relevant demo knowledge per task. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Promote human demos as L3 procedural Anchors via DemoParser. (2) KnowSeeker = S7 retrieve over demo cards not raw pixels. (3) One demo: Gemini-1.5-Pro 19.3%→51.7% offline. (4) Online SR 18.1%→32.8% UI-TARS — measure few-shot demo hydrate. |
| **metric_impact** | Offline 19.3%→51.7%; online SR 18.1%→32.8% |
| **refine_candidate** | **yes — S3/S7 demonstration-knowledge retrieve for GUI tools** |

---

### 16. RAGEN / StarPO — Multi-Turn Agent RL and Echo Trap
**arXiv:2504.20073** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S4, S8 |
| **problem** | Multi-turn agent RL under stochastic env feedback underexplored; training collapses (Echo Trap). |
| **representation** | StarPO trajectory-level State-Thinking-Action-Reward policy opt; RAGEN modular train/eval; StarPO-S: trajectory filtering, critic, gradient stabilization; findings on rollout diversity/granularity; reasoning-aware rewards needed or thoughts hallucinate. |
| **write / read / forget** | Write: RL policy updates from trajectories. Read: env states. Forget: StarPO-S discards low-information/low-variance rollouts. |
| **conflict** | Semantic-reward conflict noted in BanditRev (longer reasoning). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Filter low-variance trajectories before promote/update — Echo Trap. (2) Reasoning-aware rewards required or S8 why hallucinates. (3) Medium interaction granularity + diverse starts for rollouts. (4) StarPO-S delays/avoids collapse (FrozenLake 100→140+ steps). |
| **metric_impact** | StarPO-S retains stability; 0.5B reaches ~20–21% Sokoban/FrozenLake; filtering 50–75% rollouts helps |
| **refine_candidate** | **yes — S4 trajectory-quality filter for agent RL updates** |

---

### 17. WebThinker — Deep Research Agent with Think-Search-Draft
**arXiv:2504.21776** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | LRMs limited by static parametric knowledge for deep research reports needing multi-page web synthesis. |
| **representation** | Deep Web Explorer (search/navigate/extract); Autonomous Think-Search-and-Draft interleaves reason/gather/write; iterative online DPO for tool use; GPQA/GAIA/WebWalkerQA/HLE + Glaive reports. |
| **write / read / forget** | Read: dynamic web explore mid-reasoning; draft report incrementally. Write: report artifacts. Forget: silent. |
| **conflict** | Case study discards conflicting wrong dates on pages — informal conflict filter. |
| **privacy** | Discusses research data privacy / AI research displacement as societal note. |
| **Kedger lessons** | (1) Interleave hydrate + draft (not retrieve-then-one-shot report). (2) Online DPO preference pairs from tool-use accuracy. (3) +21.9% GAIA / +36.2% HLE vs Search-o1. (4) Don't inject full draft into reason stream — keep WorkingState slim. |
| **metric_impact** | +21.9% GAIA; +36.2% HLE vs Search-o1; RL +8.5% GAIA / +21.5% HLE over Base |
| **refine_candidate** | **yes — S7 interleaved think-search-draft hydrate** |

---

### 18. LmLm — Limited Memory LMs with Externalized Facts at Pretrain
**arXiv:2505.15962** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S6, S7 |
| **problem** | Parametric LLMs entangle facts in weights — hard to inspect/edit/unlearn; RAG/DAPT costly or incomplete. |
| **representation** | Pretrain with strategic masking of externally retrieved factual values from loss → learn lookup not memorize; external DB of facts; editable/verifiable KB; TOFU unlearning comparison. |
| **write / read / forget** | Write: facts to external DB. Read: targeted lookups at train/infer. Forget: delete DB entries (vs NPO unlearning); TOFU forget-set 5%. |
| **conflict** | Cites knowledge-conflict lit; design reduces parametric–context clash by offloading. |
| **privacy** | TOFU privacy-sensitive unlearning eval; modular delete for compliance. |
| **Kedger lessons** | (1) Prefer editable external Anchors over weight-memorized secrets. (2) S6 unshare = delete DB entries, not hope NPO. (3) Mask retrieved fact tokens in loss (aligns Search-R1). (4) Controllable knowledge offload % as Inv-Scope knob. |
| **metric_impact** | Competitive vs larger LLMs; TOFU forget 5%; offload continuum 10–90% |
| **refine_candidate** | **yes — S6/S7 externalized fact DB + loss masking** |

---

### 19. Experience-Following — Empirical Study of Agent Memory Add/Delete
**arXiv:2505.16067** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S6, S7 |
| **problem** | How memory add/delete choices shape long-term LLM agent behavior is under-studied. |
| **representation** | Empirical study: experience-following property (similar retrieved input → similar output); error propagation; misaligned experience replay; regulate experience quality; future task evals as free labels for stored memory. |
| **write / read / forget** | Write: memory addition of executions. Read: retrieve similar past. Forget: deletion policies (history-based, evaluator-gated). |
| **conflict** | Warns not to be misled by single conflicting features in judge prompts. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Experience-following ⇒ bad memories poison future — quality gate S4. (2) Error propagation SLI for memory banks. (3) Future task outcomes = free labels to prune L3. (4) Fine-tuned evaluator on ~300 trajectories already strong long-term filter. |
| **metric_impact** | Quality-regulated add/delete beats unfiltered; history-based delete can beat error-free bank |
| **refine_candidate** | **yes — S4/S6 experience-quality delete using future outcomes** |

---

### 20. Memento — Personalization Memory Bottlenecks for Embodied Agents
**arXiv:2505.16348** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Personalized embodied help needs object semantics + user pattern memories; agents fail joint-memory planning. |
| **representation** | Memento two-stage eval (single vs joint memory). Finds info overload + coordination failures. Hierarchical KG user-profile memory separates personalized knowledge; episodic memory helps ICL. |
| **write / read / forget** | Write: user-profile KG + episodic. Read: retrieve k memories (k=5 → 96.5% gold recall). Forget: filter bad episodes (13.4% removed). |
| **conflict** | Parametric commonsense vs personalized non-parametric knowledge causes agents to ignore memory. |
| **privacy** | Acknowledges privacy/security risks of embodied memory systems. |
| **Kedger lessons** | (1) Separate user-profile KG from episodic WorkingState. (2) Joint-memory tasks drop >20–30% SR — stress ConflictSet/coordination. (3) k=5 recall target for gold memories. (4) Filter zero-success episodes before promote. |
| **metric_impact** | k=5 gold recall 96.5%; joint-memory GPT-4o −30.5% SR; filter 13.4% bad episodes |
| **refine_candidate** | **yes — S5 hierarchical user-profile memory module** |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (honest deep-recard) | 20 |
| Cumulative FULL | **480** |
