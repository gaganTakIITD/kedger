# Batch 21 — Survey Runway FULL (Kedger) — **honest deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Body-grounded mechanism cards (Intro/Method/Results) replacing 2026-08-08 abstract-template cards.  
> **Progress:** FULL 400 → **420**.  
> **Method:** Fulltext `/tmp/kedger-papers/full/{id}.txt` + agent deep-read cards.  
> **Kedger stages:** S1–S8  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers from body only.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body deep-read; deep-recard upgrade of Batch21) | **20** | `2603.01455`, `2305.05091`, `2305.13711`, `2305.14318`, `2305.14323`, `2305.14325`, `2305.15852`, `2305.19118`, `2306.03314`, `2306.08302`, `2307.07047`, `2307.11019`, `2307.12856`, `2308.03427`, `2308.03549`, `2308.04026`, `2308.11339`, `2309.01918`, `2309.03736`, `2309.04175` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs cached |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. From Verbatim to Gist: Distilling Pyramidal Multimodal Memory via Hierarchical Compression
**arXiv:2603.01455** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Long video memory extremes: dense visual accumulate (latency) vs aggressive caption gist (detail loss/hallucination). |
| **representation** | **MM-Mem** Fuzzy-Trace pyramidal memory: bottom-up Sensory Buffer → … → Symbolic Schema; **SIB-GRPO** dynamic management removes redundant memories; **entropy-driven top-down** retrieval for query-adaptive expand. |
| **write / read / forget** | Write: hierarchical pyramid offline/bottom-up. Read: entropy-guided top-down retrieve. Forget: SIB-GRPO removes redundant memories while preserving task-relevant semantics. |
| **conflict** | Silent. |
| **privacy** | Broader-impact privacy/data protection note — no attack study. |
| **Kedger lessons** | (1) Pack compile should be **verbatim↔gist pyramid** with entropy-triggered expand (ReadAgent-class). (2) RL memory management (SIB-GRPO) for redundancy control under stream. (3) **+5.1%** rel vs Vgent on Video-MME; **+7.1%** MLVU M-Avg; streaming **+5.9%/+5.2%** Acc/Score vs Flash-VStream; HD-EPIC++ **30.28%**. (4) Don't force text-only gists for multimodal Evidence. |
| **metric_impact** | Video-MME/MLVU/streaming Acc&Score/HD-EPIC++; ablations of pyramid levels and entropy retrieve. |
| **refine_candidate** | **yes** — S7 pyramidal verbatim↔gist multimodal hydrate |

---

### 2. Knowledge-enhanced Agents for Interactive Text Games
**arXiv:2305.05091** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S5, S7 |
| **problem** | RL/LM agents in text games lack coherence and learn poorly from env feedback; need injected world knowledge. |
| **representation** | Inject **memory of correct actions (MCA)** and **ConceptNet affordances** into DRRN, KG-A2C, RoBERTa, Swift on ScienceWorld. Injection via extra GRU encodings, KG triples, input concat, or affordance pretrain QA. |
| **write / read / forget** | Write: MCA accumulates reward-positive actions within episode; affordances from ConceptNet. Read: concatenated encodings / KG. Forget: episode-scoped MCA (short-term); no long-term forget API. |
| **conflict** | Silent. |
| **privacy** | Silent (unrelated citation only). |
| **Kedger lessons** | (1) WorkingState should carry **successful action memory** separately from full action history. (2) Affordance triples belong in S5 graph, not only prompt text — KG injection beat string concat for KG-A2C. (3) Affordances help **63%** of configs; RoBERTa **+48%** rel, Swift **+8%**, DRRN **+4%** rel avg; Swift best avg **27.86→35.96**. (4) Task-relevance filter external KG before promote — biology tasks hurt by generic ConceptNet. |
| **metric_impact** | ScienceWorld cumulative reward across 10 tasks × 4 architectures × injection variants. |
| **refine_candidate** | **no** — (affordance/KG tickets exist; keep as interactive grounding reference) |

---

### 3. LLM-Eval: Unified Multi-Dimensional Automatic Evaluation for Open-Domain Conversations with Large Language Models
**arXiv:2305.13711** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S8 |
| **problem** | Conversation eval needs costly humans, references, or many LLM calls per dimension. |
| **representation** | **LLM-Eval**: single prompt with unified multi-dimensional schema scoring conversation quality in one model call (content/relevance/etc. per paper schema). |
| **write / read / forget** | Eval harness only — no agent memory WRF. |
| **conflict** | Silent. |
| **privacy** | Silent (mentions adversarial dialog datasets only as related work). |
| **Kedger lessons** | (1) Use one-call multi-dim LLM judge for S8 why/conversation quality SLIs — cheaper than per-dimension calls. (2) Schema must be explicit in prompt for stable scores. (3) Validate judge agreement before gating promote. (4) Not a memory mechanism — adopt as metric tooling only. |
| **metric_impact** | Correlation with human/baselines on open-domain dialog benchmarks; call efficiency. |
| **refine_candidate** | **no** |

---

### 4. CREATOR: Tool Creation for Disentangling Abstract and Concrete Reasoning of Large Language Models
**arXiv:2305.14318** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7, S8 |
| **problem** | Tool-using LLMs are stuck with fixed tools; abstract planning and concrete execution entangle and fail on hard problems. |
| **representation** | **CREATOR** stages: Creation (LLM writes reusable tools/docs+code) → Decision → Execution → Rectification. Emphasizes tool reusability vs linear CoT/PoT/tool-use. |
| **write / read / forget** | Write: created tools into a library for reuse. Read: decide which tools to call. Forget: silent; rectification repairs failed executions. |
| **conflict** | Notes conflicts between natural-language CoT and code paths on MATH — rectification addresses failures. |
| **privacy** | Ethics: tool creation could touch sensitive info — caution, no attack eval. |
| **Kedger lessons** | (1) Allow cognify to **create tools/skills**, not only retrieve fixed APIs. (2) Separate abstract plan from concrete tool code (disentangle). (3) Accuracies **59.7% / 94.7% / 75.5%** on three task suites; rectification **~+10%** relative; creation hints up to **+18.7%** on Creation Challenge. (4) Rectification loop is S8 repair before sealing wrong skill. |
| **metric_impact** | Accuracy on MATH/Creation Challenge suites; rectification and creation ablations. |
| **refine_candidate** | **yes** — S3 tool-creation + rectification skill promote |

---

### 5. ChatCoT: Tool-Augmented Chain-of-Thought Reasoning on Chat-based Large Language Models
**arXiv:2305.14323** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Chat LLMs need frequent tool use in multi-hop reasoning; plan-then-execute or hard-stop tool calls fit poorly. |
| **representation** | **ChatCoT**: model CoT as multi-turn chat; each turn either reason or call tool; tool knowledge + multi-round fusion (MRF) improve tool timing. |
| **write / read / forget** | No persistent memory; ephemeral tool results into chat state. Read: tools as chat turns. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate tool I/O as **chat turns** interleaved with thought — natural for chat models. (2) Tool-knowledge priming raises call frequency/success (ChatCoT tool freq **56%** success **93%** vs CoT+tool **3%/85.7%**). (3) **+7.9%** relative avg on MATH vs PHP SOTA. (4) Ablate MRF carefully — without MRF success collapses (**64.2%**). |
| **metric_impact** | MATH subtask accuracy; tool call frequency/success ablations. |
| **refine_candidate** | **no** — (tool-augmented CoT covered; keep pattern reference) |

---

### 6. Improving Factuality and Reasoning in Language Models through Multiagent Debate
**arXiv:2305.14325** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Single-model generation remains fallacious; prompting tricks still lack cross-examination of reasoning. |
| **representation** | Multiple LM instances **propose and debate** answers/reasoning over rounds; judge/consensus yields final answer. Black-box compatible; same prompts across tasks (math, strategy, factuality). |
| **write / read / forget** | No durable memory — debate transcript is ephemeral working context. |
| **conflict** | Debate surfaces disagreeing claims; resolution by multi-round argumentation, not typed SUPERSEDES store. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Before seal/answer, run **multi-agent debate** over conflicting Evidence/candidates. (2) Keep debate transcripts as optional S8 why artifacts. (3) Paper reports significant gains on math/strategic reasoning and reduced hallucinations vs single-agent baselines (see tables — use published task scores, don't invent). (4) Works on black-box APIs — good for Kedger without weight access. |
| **metric_impact** | Task accuracy on arithmetic/strategy/factuality suites vs single-agent/self-refine baselines; rounds ablation. |
| **refine_candidate** | **yes** — S8 multiagent debate before final answer |

---

### 7. Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation
**arXiv:2305.15852** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | LLMs emit **self-contradictions** within generated text; RAG can't fix many (unverifiable against web). |
| **representation** | Framework to **evaluate** prevalence, **detect** contradictions via LM prompts (gLM/aLM), and **mitigate**. Complements retrieval; many contradictions (~35.2% ChatGPT) not web-verifiable. |
| **write / read / forget** | Detection/mitigation over generated sentences — not long-term memory WRF. |
| **conflict** | Core object: intra-response self-contradiction; detector compares sentence vs alternatives. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Add self-contradiction detector before packing answers into Anchors. (2) Don't assume RAG eliminates contradictions — paper: large share unverifiable online. (3) Detection precision examples **74.2–83.8%**; prevalence e.g. ChatGPT **18.2%** predicted self-contra (vanilla) with mitigation reducing large fractions (up to **89.5%** self-contra reduction in cited setting); annotator agreement **82.7%**. (4) Pair with ConflictRAG-style inter-doc checks for full ConflictSet coverage. |
| **metric_impact** | Self-contradiction prevalence; detection P/R/F1 (~80% F1 claimed); mitigation residual rate ±RAG. |
| **refine_candidate** | **yes** — S8 self-contradiction detect+mitigate gate |

---

### 8. Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate
**arXiv:2305.19118** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S8 |
| **problem** | Self-reflection suffers **Degeneration-of-Thought (DoT)**: once confident, model won't generate novel thoughts even if wrong. |
| **representation** | **MAD**: tit-for-tat debaters + judge; forces divergent arguments. Evaluated on translation (Common MT) and reasoning; compares to self-reflect/rerank. |
| **write / read / forget** | Ephemeral debate; judge aggregates. Forget: longer debates cause debaters to forget prior views — length risk. |
| **conflict** | Opposition rate metric between debaters; addresses self-confliction of reflection. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Prefer adversarial debate over solo self-reflect when DoT risk is high. (2) Bound debate length — long transcripts degrade memory of prior arguments. (3) Translation HUMAN scores improve with MAD (e.g. GPT-4 Turbo contextual HUMAN **3.57→3.67**; Vicuna gains similarly). (4) Judge module is an S8 aggregator pattern for competing why chains. |
| **metric_impact** | Translation COMET/BLEURT/HUMAN; reasoning benchmarks; debater-count ablation (~10% manual analysis subset). |
| **refine_candidate** | **no** — (paired with Du et al. multiagent debate ticket) |

---

### 9. Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents
**arXiv:2306.03314** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7 |
| **problem** | Single LLM agents (Auto-GPT/BabyAGI) hit loops, rigidity, weak collaboration; need adaptive multi-agent framework. |
| **representation** | Conceptual framework for collaborative LLM agents with distinct roles, dynamic add/remove, case studies on Auto-GPT/BabyAGI/Gorilla API use; discusses permissions/connections. |
| **write / read / forget** | Framework-level; agents share messages/tools — no concrete durable memory design. |
| **conflict** | Notes risk of conflicts when dynamically adding agents — organizational, not belief revision. |
| **privacy** | Lists security/privacy as open challenges — no mechanism. |
| **Kedger lessons** | (1) Treat multi-agent Kedger deployments as **permissioned role graphs**, not free-form chat. (2) Dynamic agent add/remove needs inefficiency/conflict guards. (3) Use as architecture checklist vs Auto-GPT failure modes (loops). (4) No numeric claims to lock — qualitative roadmap only. |
| **metric_impact** | Case-study qualitative success on AGI-style tasks; no standard numeric leaderboard in body. |
| **refine_candidate** | **no** |

---

### 10. Unifying Large Language Models and Knowledge Graphs: A Roadmap
**arXiv:2306.08302** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | LLMs lack reliable factual access; KGs are structured but hard to evolve — need unified roadmap. |
| **representation** | Roadmap of KG→LLM, LLM→KG, and bidirectional synergy (grounding, editing, KG construction/completion with LLMs). |
| **write / read / forget** | Survey of write (KG construction/edit) and read (KG-augmented inference) patterns across literature. |
| **conflict** | Discusses inconsistency/knowledge editing challenges at roadmap level. |
| **privacy** | Silent beyond generic. |
| **Kedger lessons** | (1) Keep Anchors KG-addressable for inspectable factual hydrate. (2) LLMs can propose KG edges but must pass promote validation. (3) Bidirectional sync is the long-term S3↔S5 design target. (4) Use as bibliography map — no single metric to adopt. |
| **metric_impact** | Roadmap — cite downstream task gains from referenced KG-LLM systems when refining. |
| **refine_candidate** | **no** — (roadmap) |

---

### 11. Does Collaborative Human-LM Dialogue Generation Help Information Retrieval Evaluation?
**arXiv:2307.07047** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | IR evaluation needs realistic conversational queries; purely synthetic or human-only data are costly/biased. |
| **representation** | Study whether **human–LM collaborative** dialogue generation improves IR evaluation quality versus alternatives. |
| **write / read / forget** | Dialogue generation for eval datasets — not agent memory store. |
| **conflict** | Silent on memory conflict. |
| **privacy** | Human dialogue data collection raises privacy considerations in discussion. |
| **Kedger lessons** | (1) Human-in-the-loop dialogue synth can improve IR eval fidelity for hydrate benchmarks. (2) Don't trust fully synthetic conversations for retrieval SLIs without human checks. (3) Lock paper's reported IR metrics (nDCG/MAP-style) from tables when citing — avoid invented lifts. (4) Collaborative generation is an S8 annotation pattern, not a runtime memory. |
| **metric_impact** | IR evaluation quality metrics comparing collaborative vs human/LM-only dialogues. |
| **refine_candidate** | **no** |

---

### 12. Investigating the Factual Knowledge Boundary of Large Language Models with Retrieval Augmentation
**arXiv:2307.11019** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Unclear when LLMs know vs should retrieve; retrieval quality (golden/high/weak/random) changes behavior. |
| **representation** | Systematic study of LLM **knowledge boundary** with retrieval augmentation under controlled evidence relevance; metrics for correct/incorrect/abstain-like behaviors across models. |
| **write / read / forget** | Read-only retrieval conditions; no memory write. |
| **conflict** | Analyzes conflicts between parametric knowledge and retrieved evidence. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate policy must estimate **in-boundary vs OOD** before retrieve. (2) Weak/random retrieval can hurt — gate by relevance. (3) Tables show large swings (e.g. None vs Golden vs Retrieved vs High/Weak-related accuracy/F1 columns across models) — use as fixture matrix. (4) Pair with Chain-of-Note unknown path when retrieval irrelevant. |
| **metric_impact** | QA accuracy/F1 under None/Golden/Retrieved/High/Weak/Random evidence; per-model boundary analysis. |
| **refine_candidate** | **yes** — S7 knowledge-boundary-aware retrieve gate |

---

### 13. A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis
**arXiv:2307.12856** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7, S8 |
| **problem** | Real-website agents fail without combined planning, long HTML understanding, and program synthesis. |
| **representation** | **WebAgent**: planner + **HTML-T5** long-context HTML summarizer/understander + program synthesis actor; modular recipe on real sites and MiniWoB/Mind2Web. |
| **write / read / forget** | Working context of plans/HTML summaries; no long-term cross-session memory emphasized. |
| **conflict** | Error analysis on module coupling — not belief conflict. |
| **privacy** | Silent (real web interaction ethics implicit). |
| **Kedger lessons** | (1) Long HTML must be **summarized/programmed**, not dumped into WorkingState. (2) Couple planner with HTML-T5 — modules alone underperform. (3) **>50%** success lift on real websites; HTML-T5 **+18.7%** vs prior on MiniWoB++; modular best successes **65/70/80%** in cited settings. (4) Program synthesis actions are a hydrate output form for web tools. |
| **metric_impact** | Success on real websites, MiniWoB++, Mind2Web; ablations of planner/HTML-T5/program modules. |
| **refine_candidate** | **no** — (WebCoach/M² cover newer web memory; keep HTML-T5 pattern) |

---

### 14. TPTU: Large Language Model-based AI Agents for Task Planning and Tool Usage
**arXiv:2308.03427** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | LLMs struggle to jointly plan tasks and select/order tools under realistic tool sets. |
| **representation** | **TPTU** agents: Task Planning + Tool Usage with one-agent vs sequential-agent variants; evaluates planning of tool order, tool–subtask pairs, SQL/math tool tasks across ChatGPT/Claude/open models. |
| **write / read / forget** | Ephemeral plan+tool calls; no durable memory module. |
| **conflict** | Silent beyond incorrect tool-order failures. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Separate **plan generation** from **tool binding** evaluators in S8. (2) Open models lag badly on planning accuracy (tables: ChatGPT/Claude often **70–100%** on planning subtests vs many open models **0–55%**). (3) Sequential agent (TPTU-SA) can beat one-agent on multi-tool (e.g. ChatGPT **55%** vs OA **50%** in one table). (4) Build tool-order fixtures before trusting hydrate tool routers. |
| **metric_impact** | Accuracy on tool-order, tool-subtask, SQL, math, multi-tool settings across model agents. |
| **refine_candidate** | **no** |

---

### 15. Zhongjing: Enhancing the Chinese Medical Capabilities of Large Language Model through Expert Feedback and Real-world Multi-turn Dialogue
**arXiv:2308.03549** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Medical LLMs lack expert-aligned multi-turn dialogue ability and domain knowledge in Chinese clinical settings. |
| **representation** | **Zhongjing**: continuous pretrain → construct real-world multi-turn medical dialogues → SFT → RL with **expert feedback** to improve medical dialogue capability. |
| **write / read / forget** | Training-time dialogue corpora and preference feedback; runtime is fine-tuned model (parametric memory), not external store. |
| **conflict** | Silent on runtime SUPERSEDES; expert feedback corrects model behavior offline. |
| **privacy** | Medical dialogue data — sensitive domain; paper in medical LLM ethics regime (handle PHI carefully if adopted). |
| **Kedger lessons** | (1) Multi-turn medical/assistant packs need **expert preference** loops, not only next-token SFT. (2) Real dialogue distribution > synthetic for promote of clinical skills. (3) Prefer external Anchor KB + retrieve for medical facts rather than only parametric Zhongjing-style weights when privacy matters. (4) Expert feedback is an S8 evaluation source for sealed medical packs. |
| **metric_impact** | Chinese medical benchmarks / dialogue quality with expert ratings (see paper tables). |
| **refine_candidate** | **no** — (domain SFT path; Kedger prefers structured medical KB — see 2309.04175) |

---

### 16. AgentSims: An Open-Source Sandbox for Large Language Model Evaluation
**arXiv:2308.04026** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7 |
| **problem** | LLM agent eval lacks controllable interactive sandbox spanning social/tool settings. |
| **representation** | **AgentSims** open-source sandbox for evaluating LLM agents in simulated environments (social simulation style). |
| **write / read / forget** | Simulation state is env memory; not a portable agent memory architecture. |
| **conflict** | Silent. |
| **privacy** | Sandbox may simulate private social data — eval hygiene. |
| **Kedger lessons** | (1) Use sandboxed interactive eval for hydrate/tool policies before production. (2) Decouple env state from agent Anchors in fixtures. (3) No core numeric memory result to lock — infrastructure paper. (4) Good host for MemoryGraft/Dojo-style attacks later. |
| **metric_impact** | Sandbox capability coverage; agent task success within sims. |
| **refine_candidate** | **no** |

---

### 17. ProAgent: Building Proactive Cooperative Agents with Large Language Models
**arXiv:2308.11339** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Cooperative agents need to infer teammate intentions and correct beliefs proactively, not only react. |
| **representation** | **ProAgent** pipeline: knowledge library + language state grounding → high-level skill planning → **Belief Correction** about teammates → skill validation → action. Modular cooperative agent for Overcooked-style coordination. |
| **write / read / forget** | Maintains belief of teammate intentions + recent language state/analysis/skill; discards older skill traces as it updates. |
| **conflict** | Silent on factual SUPERSEDES; belief correction revises teammate intention estimates. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Multi-agent hydrate should track **teammate intention beliefs** with explicit correction. (2) Verificator/skill validation is mandatory — success drops to **~20%** without it in reported ablation. (3) Average **>10%** improvement vs prior SOTA with human proxy models. (4) Modular belief+plan+verify maps to S8 cooperative why. |
| **metric_impact** | Overcooked-like success over fixed steps; verificator ablation; human-proxy cooperation scores. |
| **refine_candidate** | **yes** — S8 teammate belief-correction module for coop agents |

---

### 18. RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking
**arXiv:2309.01918** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7 |
| **problem** | Universal robot manipulation lacks data; need generalization under small real-robot budgets. |
| **representation** | **RoboAgent**: semantic augmentations multiply datasets; **action chunking** policy (MT-ACT) for efficient imitation; language-conditioned multi-task skills (12 skills / 38 tasks / 6 activities). |
| **write / read / forget** | Policy learning from augmented demos — episodic robot trajectories as training memory, not retrieval store. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) For embodied promote, prefer **semantic augmentation** over collecting endless raw demos. (2) Action chunking size is a critical hydrate/control hyperparam (chunk 20 best; 40 drops **>20%**). (3) **>40%** better in unseen situations vs priors; ~**70%** success under strong variations in one eval; MT-ACT **25%** in a hard transfer env where others **0**. (4) Not a textual Anchor system — use for embodied skill packing lessons only. |
| **metric_impact** | Manipulation success across seen/unseen activities; chunk-size and augmentation ablations. |
| **refine_candidate** | **no** |

---

### 19. TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance
**arXiv:2309.03736** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Flat GPT memory doesn't prioritize immediate vs long-horizon trading info; homogeneous agents lack diversity. |
| **representation** | **TradingGPT**: each agent maintains **long/middle/short-term** layered memories with layer-specific retrieval ranking (Atkinson-style); distinct trading **characters** bias which memories matter; multi-agent deliberation. |
| **write / read / forget** | Write: events into layered memories with timestamps. Read: layered ranked retrieve. Forget: time-decay aligned with Ebbinghaus-style curves across layers. |
| **conflict** | Silent on SUPERSEDES; character disagreement via debate. |
| **privacy** | Silent (footer). |
| **Kedger lessons** | (1) Working/long memory should be **explicit layers with different decay/retrieve**, not one vector store. (2) Character/persona priors change memory salience — model as retrieve priors. (3) Prefer layered decay over single similarity rank for time-sensitive domains. (4) No reliable numeric trading returns locked from thin results section — treat as architecture prior, measure in-house. |
| **metric_impact** | Trading simulation performance vs non-layered/single-agent baselines (paper primarily architectural). |
| **refine_candidate** | **yes** — S2 layered decay memory for time-sensitive agents |

---

### 20. Knowledge-tuning Large Language Models with Structured Medical Knowledge Bases
**arXiv:2309.04175** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Medical LLMs hallucinate facts; unstructured fine-tuning doesn't ground answers in KB structure. |
| **representation** | **Knowledge-tuning**: convert structured medical KB into train instances; at inference, LLM fills retrieval parameters → fetch KB → generate grounded answer. Releases **cMedKnowQA**. |
| **write / read / forget** | Write: KB→instruction pairs for tuning. Read: structured retrieval by predicted entity/attribute then generate. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Medical KB/QA — sensitive domain; structured retrieve better for audit than opaque weights alone. |
| **Kedger lessons** | (1) Prefer **structured KB retrieve+generate** over pure medical SFT for factual Anchors. (2) Train the model to emit retrieval parameters (entity/attribute) as hydrate API. (3) Dense retrieve only **2.6%** of knowledge; BM25 **~55%** acquisition accuracy; entity prediction up to **86.7%**; attribute precision up to **71.4%**; tuning data scale matters (**80.7%** at 200 instances in one setting). (4) cMedKnowQA-style suites for medical hydrate SLIs. |
| **metric_impact** | cMedKnowQA / medical QA accuracy; retrieval acquisition accuracy; data-scale ablations. |
| **refine_candidate** | **yes** — S5/S7 structured KB knowledge-tuning hydrate |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (honest deep-recard) | 20 |
| Cumulative FULL | **420** |
