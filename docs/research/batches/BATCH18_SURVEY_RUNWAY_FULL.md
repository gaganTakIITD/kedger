# Batch 18 — Survey Runway FULL (Kedger) — **honest deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Body-grounded mechanism cards (Intro/Method/Results) replacing 2026-08-08 abstract-template cards.  
> **Progress:** FULL 340 → **360**.  
> **Method:** Fulltext `/tmp/kedger-papers/full/{id}.txt` + agent deep-read cards.  
> **Kedger stages:** S1–S8  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers from body only.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body deep-read; deep-recard upgrade of Batch18) | **20** | `2305.17144`, `2308.01542`, `2308.07201`, `2309.17452`, `2310.16340`, `2311.04177`, `2312.00326`, `2312.03815`, `2401.07339`, `2401.14215`, `2403.01112`, `2404.09992`, `2406.05925`, `2406.06124`, `2406.08747`, `2406.10996`, `2408.05861`, `2410.19627`, `2410.20682`, `2412.01857` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs cached |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. Ghost in the Minecraft (GITM): Generally Capable Agents via LLMs with Text-based Knowledge and Memory
**arXiv:2305.17144** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S1', 'S3', 'S7', 'S8'] |
| **problem** | Minecraft agents overfit ObtainDiamond (~20% SOTA) and fail to generalize across the Overworld tech tree; RL maps long-horizon goals directly to low-level controls. |
| **representation** | GITM hierarchy: LLM Decomposer builds sub-goal tree with goal tuple (Object,Count,Material,Tool,Info); LLM Planner emits structured action lists using feedback + reference plans from memory; LLM Interface maps to keyboard/mouse. Text knowledge + episodic reference plans retrieved on failure/replan. |
| **write / read / forget** | Write: store successful/failed plans and goal Info text in memory. Read: retrieve reference plans + external item knowledge into planner query. Forget: Silent (no eviction policy stated). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S3 cognify should decompose Anchors into prerequisite trees (Material/Tool) before hydrate, not one-shot plans. (2) On action failure, mid-turn S7 replan should pull reference plans like GITM memory, not restart from user utterance. (3) Persist structured action traces as S8 why for audit of long-horizon agents. (4) External wiki-like Info is Evidence, not Anchor statements—gate promote separately. |
| **metric_impact** | ObtainDiamond success +47.5% vs prior; unlocks all 262 Overworld items (vs DEPS 69/262, VPT 15/262); memory lifts axes success 95.0%/67.5% (+37.5/+32.5 pts vs no-memory); learning from first failures raises success 35%→47.5%. |
| **refine_candidate** | **yes — S7 failure-triggered reference-plan hydrate for tool/agent loops** |

---

### 2. Memory Sandbox: Transparent and Interactive Memory Management for Conversational Agents
**arXiv:2308.01542** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S1', 'S2', 'S6', 'S7'] |
| **problem** | Users cannot see or control what conversational LLM agents remember, causing poor mental models and breakdowns when memory is wrong or overfull. |
| **representation** | Design probe UI treating conversation turns as manipulable memory objects: toggle visibility (hide from model context), add/edit/delete, summarize/combine, share across conversations; Next.js + GPT-3.5-turbo; shared representation so UI state == model context. |
| **write / read / forget** | Write: user-curated add/edit/summarize of memory objects. Read: only visible objects enter LLM context. Forget: explicit user delete + hide (soft exclude from hydrate). |
| **conflict** | Silent on automated SUPERSEDES; user manually edits contradictions. |
| **privacy** | Silent on formal privacy (share-memory affordance is UX, not ACL). |
| **Kedger lessons** | (1) Kedger needs user-facing WorkingState inspector aligned with S2 pack contents (what hydrate sees). (2) Toggle-visibility maps to Inv-Scope / soft tombstone without hard delete. (3) Summarize-combine is user-gated cognify—do not auto-promote without consent. (4) Cross-conversation share requires S6 seal + ACL, not raw object copy. |
| **metric_impact** | Design/probe paper — no quantitative QA metrics in body; contribution is interaction affordances (7 operations listed). |
| **refine_candidate** | **yes — S2/S6 memory-object inspector + visibility toggles for pack compile** |

---

### 3. ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate
**arXiv:2308.07201** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S1', 'S7', 'S8'] |
| **problem** | Single-agent LLM-as-judge correlates weakly with humans on open-ended generation; one persona introduces bias. |
| **representation** | ChatEval multi-agent debate: diverse persona-assigned debater agents communicate over rounds (various strategies) then form final judgment; inspired by collaborative human annotation. |
| **write / read / forget** | Write: Silent (ephemeral debate transcript, not persistent memory store). Read: Silent / prompt-only. Forget: Silent. |
| **conflict** | Silent on knowledge SUPERSEDES; debate addresses evaluator disagreement, not doc conflict. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S8 why / eng-judgment can use multi-persona debate rather than single LLM judge. (2) Cap roles ~3–4 (Acc peaks 62.5% there) to avoid degeneration-of-thought. (3) Persona diversity is a fixture for eval harness SLIs, not memory write. (4) Report Acc+Kappa vs humans—don't treat LLM judge alone as ground truth. |
| **metric_impact** | Multi-agent +6.2 Acc pts ChatGPT / +2.5 GPT-4 vs single-agent; Kendall-Tau +0.096 (16.3%) and +0.057 (10.0%); Acc apex 62.5% at 3–4 roles; human Acc 71.7%. |
| **refine_candidate** | **no — eval harness pattern; not a storage/hydrate ticket** |

---

### 4. ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving
**arXiv:2309.17452** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S1', 'S7', 'S8'] |
| **problem** | LLMs struggle on competition math; pure natural-language CoT lacks reliable computation; tool-only code lacks rationale. |
| **representation** | ToRA agents interleave natural-language rationales with tool calls (computation libraries / symbolic solvers); trained via imitation on curated interactive tool-use trajectories + output-space shaping; family ToRA / ToRA-Code across 7B–70B. |
| **write / read / forget** | Write: Silent persistent memory (training trajectories only). Read: tool observations into next reasoning step. Forget: Silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S1 tool returns are first-class Evidence for math/code hydrate—keep interleaved rationale+code in why. (2) Output-space shaping ≈ reject bad trajectories before promote. (3) Prefer tool-integrated packs over pure parametric CoT for numeric Anchors. (4) Ablations show rationale and shaping both required—don't drop either in agent loops. |
| **metric_impact** | Absolute +13–19% avg across 10 math tasks vs prior open-source; ToRA-Code-34B 50.8% MATH (near GPT-4-Code 51.8%); ToRA-70B 49.7% MATH (+25.6 vs WizardMath-70B); w/o rationale −7.8 to −8.9 MATH pts; shaping +~3–4 pts GSM8k/MATH. |
| **refine_candidate** | **no — tool-agent training recipe covered elsewhere; keep as eval reference** |

---

### 5. RCAgent: Cloud Root Cause Analysis by Autonomous Agents with Tool-Augmented LLMs
**arXiv:2310.16340** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S1', 'S2', 'S7', 'S8'] |
| **problem** | Industrial cloud RCA with LLMs still uses manual workflows; GPT-family APIs raise privacy/context-length/action-validity issues. |
| **representation** | RCAgent: controller ReAct loop + LLM expert-agent tools (code/log analysis); Observation Snapshot Key (OBSK) KV store for long observations; JSON repair + error handling; self-consistency aggregation over text votes and tool trajectories; runs on internally deployed model. |
| **write / read / forget** | Write: OBSK key-value snapshots of lengthy observations. Read: retrieve OBSK entries into controller context. Forget: Silent. |
| **conflict** | Silent on SUPERSEDES; self-consistency votes reconcile trajectory disagreements. |
| **privacy** | Core design: privacy-aware industrial RCA on internal model (not GPT APIs); challenge section names Privacy explicitly. |
| **Kedger lessons** | (1) Long tool observations need S2 OBSK-style paging—don't dump raw logs into WorkingState. (2) Expert-agent tools + controller mirrors Kedger tiered hydrate. (3) Self-consistency over tool traces is an S8 confidence gate before promote. (4) Privacy constraint ⇒ prefer sealed local model + Inv-Scope for ops Evidence. |
| **metric_impact** | +6.52 METEOR root-cause vs ReAct; resolution +3.51 METEOR / +4.50 BLEURT / +2.28%; Pass Rate 99.38% within 15 steps, Invalid Rate 7.93%; stability >90% Pass (collapses to 70.19% without enhancements); OoD precision 82.06%. |
| **refine_candidate** | **yes — S2 observation-snapshot KV + privacy-local tool hydrate** |

---

### 6. ARM-RAG: Auxiliary Rationale Memory for Retrieval Augmented Generation
**arXiv:2311.04177** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S3', 'S4', 'S7'] |
| **problem** | Frozen LLMs don't learn from successful problem-solving; fine-tuning (e.g., STaR) is expensive; need cheap improvement from successes. |
| **representation** | ARM-RAG: on correct GSM8K solutions, store question+answer+rationale chains in Pyserini (neural IR) index; at inference retrieve similar rationales as hints for new problems—Auxiliary Rationale Memory without weight updates. |
| **write / read / forget** | Write: index successful rationale chains. Read: retrieve rationales as few-shot hints. Forget: Silent (no prune of wrong/stale rationales). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Promote only successful S8 why traces into a rationale index—failure traces stay WorkingState. (2) Rationale-as-Evidence hydrate beats question-only RAG for procedural tasks. (3) Cheap IR over traces is an alternative to STaR-style fine-tune for Kedger dogfood. (4) Record silence on forgetting—stale rationales can poison without invalidate. |
| **metric_impact** | Basic ARM-RAG 75.3% vs 73.2% non-ARM baseline on GSM8K-style setup; multi-attempt+hints reach 91.9% from 73.2%; paper cites STaR 89.5% after 16 iters / baseline 76.3% as context. |
| **refine_candidate** | **yes — S4 promote-on-success rationale index for hydrate hints** |

---

### 7. Agent-OM: Leveraging LLM Agents for Ontology Matching
**arXiv:2312.00326** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S1', 'S5', 'S7'] |
| **problem** | Ontology matching needs planning+tools beyond single-pass LLM prompting; hallucinations and weak non-linguistic reasoning hurt OM automation. |
| **representation** | Agent-OM: Siamese Retrieval Agent (entity/metadata/context → hybrid index) + Matching Agent; planning decomposes OM into subtasks with tool calling; memory holds plan/dialogue state; evaluated on OAEI tracks. |
| **write / read / forget** | Write: Retrieval Agent stores ontology entities/metadata/context in hybrid store; plan kept in dialogue memory. Read: retrieval for candidate entities then match. Forget: Silent. |
| **conflict** | Silent (matching decides alignments; no typed conflict set). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Schema/ontology Alignment is an S5 graph compose path with dedicated retrieve+match agents. (2) Tool-calling planning reduces hallucination vs pure chat OM. (3) Hybrid entity index ≈ Anchor+metadata hydrate, not embedding-only. (4) Treat few-shot/complex OM gains as ticket for structured matching tools in Kedger. |
| **metric_impact** | Body claims near long-standing best on simple OAEI tracks and significant gains on complex/few-shot OM; detailed F1 tables thin in HTML extract—use OAEI track reports / artifact repo for exact F1. |
| **refine_candidate** | **no — domain OM tooling; pattern reference only** |

---

### 8. LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS-Agent Ecosystem
**arXiv:2312.03815** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S2', 'S6', 'S7'] |
| **problem** | Need a systems metaphor for LLM agents: memory, storage, tools, and multi-agent apps lack OS-like resource management and security. |
| **representation** | Vision paper: LLM as AIOS kernel (reasoning/planning/self-improve); context window as memory; external storage as files (formats+retrieval); tools as devices/libraries with drivers/APIs; Agents as apps; NL as programming interface; discusses memory/tool management, communication, security. |
| **write / read / forget** | Write/Read/Forget: conceptual mapping only (context=memory, external store=files); no concrete algorithm. |
| **conflict** | Mentions expert inconsistency feedback in related multi-agent setups; not a typed ConflictSet. |
| **privacy** | Security section flagged; no membership/Inv-Scope mechanism. |
| **Kedger lessons** | (1) Map Kedger stages to AIOS layers: WorkingState≈context memory, Anchors≈files, tools≈devices. (2) Resource management (memory+tool quotas) belongs in S2/S6 policy, not ad-hoc prompts. (3) Multi-agent apps need explicit IPC contracts like OS processes. (4) Use as architecture vocabulary—not an implementable ticket alone. |
| **metric_impact** | No empirical tables—position/vision paper. |
| **refine_candidate** | **no — architectural metaphor; already reflected in Kedger OS framing** |

---

### 9. CodeAgent: Tool-Integrated Agents for Real-World Repo-level Coding Challenges
**arXiv:2401.07339** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S1', 'S7', 'S8'] |
| **problem** | LLMs handle standalone functions but fail on repo-level code with >70% non-standalone functions, dependencies, and docs. |
| **representation** | CodeAgent: LLM agent + five programming tools (Website Search, Documentation Reading, Code Symbol Navigator, etc.); strategies Rule-based / ReAct / Tool-Planning / OpenAI function-calling; new CodeAgentBench for repo-level tasks. |
| **write / read / forget** | Write: Silent persistent memory (tool observations in-session). Read: tool fetches docs/symbols/web into context. Forget: Silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Repo hydrate needs symbol-nav + docs tools, not embedding search alone. (2) Rule-based and ReAct beat Tool-Planning on CodeAgentBench—prefer constrained tool policies. (3) Ablations: removing Documentation Reading / Symbol Navigator hurts Pass@1 (e.g., −3 to −4 pts on GPT-3.5-ReAct). (4) Log tool traces as S8 why for coding agents. |
| **metric_impact** | GPT-4 CodeAgentBench: up to +15.8 Pass@1 (72.7% relative over NoAgent); HumanEval Pass@1 e.g. GPT-3.5 Rule-based 82.3 (↑9.7), DeepSeek-33B 84.8 (↑6.1). |
| **refine_candidate** | **yes — S1/S7 repo tool pack (docs+symbol nav) for code agents** |

---

### 10. Caffeine: Commonsense-augmented Memory via Context-aware Persona Refinement
**arXiv:2401.14215** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S3', 'S4', 'S5', 'S7'] |
| **problem** | COMET persona expansion creates contradictions across sessions; NLI-removal is suboptimal and unlike context-dependent human personality. |
| **representation** | Caffeine: expand personas with COMET; link personas to contextual backgrounds; refine contradictory personas into richer context-aware sentences (not delete); store refined personas for next-session RG; Contriever retrieval. |
| **write / read / forget** | Write: refined persona sentences into dialogue memory after session. Read: retrieve personas for response generation. Forget: refine-in-place rather than delete (NLI-remove baseline discarded). |
| **conflict** | Core: detect contradictory personas within/across sessions and refine via context (human-like), vs NLI-remove. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S4/S5 SUPERSEDES for personas should refine+contextualize, not only tombstone. (2) Attach contextual background links when promoting persona Anchors. (3) Commonsense expansion without conflict refine pollutes memory—gate COMET-like writes. (4) Human prefs: Naturalness 73%* etc. favor refinement over removal. |
| **metric_impact** | Human RG prefs e.g. Naturalness 73%*, Consistency 66%*, Engagingness 63%* (Caffeine vs GOLD/COMET-EXP/NLI-remove tables); 69% agreement on human-likeness of refinements. |
| **refine_candidate** | **yes — S4 persona ConflictSet refine-instead-of-delete** |

---

### 11. EMU: Efficient Episodic Memory Utilization for Cooperative MARL
**arXiv:2403.01112** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S3', 'S7'] |
| **problem** | Cooperative MARL is slow and stuck in local optima on complex SMAC/GRF tasks; episodic memory underused for semantically coherent recall. |
| **representation** | EMU: semantic memory embedding of episodic states + episodic incentive reward shaping; overall learning objective couples embedding loss with RL; memory construction stores global states; utilized for coherent recall during training. |
| **write / read / forget** | Write: episodic global-state memory bank with semantic embeddings. Read: recall coherent episodes to accelerate learning. Forget: Silent (capacity implied by dataset size; CPU memory <1% of RL training). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Episodic banks need semantic embeddings, not FIFO replay alone, for S3/S7. (2) Episodic incentive ≈ intrinsic reward for recalling useful Anchors. (3) Memory overhead can be tiny (<1% CPU)—don't reject episodic stores on cost alone. (4) MARL-specific; port incentive idea, not SMAC trainer. |
| **metric_impact** | Overall win-rate μ̄_w and final win-rate on SMAC/GRF (figures/tables); episodic memory CPU usage <1% of RL training (e.g., 0.4–1.2 GiB / 1M data on SMAC maps). |
| **refine_candidate** | **no — RL episodic control; incentive idea only** |

---

### 12. MMInA: Benchmarking Multihop Multimodal Internet Agents
**arXiv:2404.09992** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S7', 'S8'] |
| **problem** | Existing web-agent benches miss evolving real multimodal sites and multihop cross-website tasks. |
| **representation** | MMInA benchmark: evolving real multimodal websites, accessibility trees + images, multihop tasks across 14 sites; eval must_include/keyword and multihop metrics; studies memory-augmented agents. |
| **write / read / forget** | Write/Read: benchmark supports memory-augmented agent variants (ablation of memory in appendix); Forget: Silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Multihop web hydrate must carry cross-site state as S8 why, not restart each hop. (2) Multimodal Evidence (a11y tree+images) required—text-only agents underperform. (3) Use MMInA as hard SLI for internet agents (GPT-4V 21.8% SR vs human 96.3%). (4) Early-hop failures dominate—budget mid-task replan. |
| **metric_impact** | GPT-4V ~21.8% success (above text baselines) vs human 96.3%; multihop markedly harder than single-hop. |
| **refine_candidate** | **no — benchmark fixture; memory ablation already noted** |

---

### 13. Hello Again! LD-Agent: LLM-powered Personalized Agent for Long-term Dialogue
**arXiv:2406.05925** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S2', 'S3', 'S4', 'S7'] |
| **problem** | Most dialogue systems are single-session; long-term companionship needs event memory + dynamic personas. |
| **representation** | LD-Agent: long-term memory (store, event summary, retrieval) + short-term memory; dynamic persona extraction; response generation conditioned on both; multi-session eval on MSC etc. |
| **write / read / forget** | Write: event summaries + extracted personas into LTM. Read: retrieve events/personas for RG. Forget: Silent (summarization compresses). |
| **conflict** | Related-work mentions conflict-resolution scenarios; LD-Agent itself Silent on typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Split S2 STM vs S3 event-summary LTM like LD-Agent. (2) Persona extractor is a promote path separate from event Anchors. (3) Ablations on MSC show each module helps—don't ship retrieval-only. (4) Cross-domain/cross-task generality claimed—test Kedger personalization transfer. |
| **metric_impact** | Automatic RG tables on MSC (e.g., tuned LDA* BLEU/F1-style scores up to ~10.70/5.63/23.31 vs weaker zero-shot); human eval on topic coherence/fluency/satisfaction (details in §4.6). |
| **refine_candidate** | **yes — S3 event-summary + dynamic persona promote for multi-session** |

---

### 14. Hierarchical Aggregate Tree (HAT) for Long-Term Memory RAG
**arXiv:2406.06124** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S2', 'S3', 'S5', 'S7'] |
| **problem** | LLM context limits block long multi-turn dialogue; flat retrieval misses breadth/depth tradeoff. |
| **representation** | HAT: hierarchical tree nodes recursively aggregate children dialogue context; Memory Agent finds optimal conditional traversal to a node whose aggregate answers the query; depth control for coverage. |
| **write / read / forget** | Write: insert utterances into tree with upward aggregates. Read: traverse HAT for best context node. Forget: Silent (leaf growth noted as footprint risk in limitations). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S5 pack compile can be tree-traversal over aggregates, not only flat top-k. (2) Conditional depth control ≈ hydrate budget. (3) Watch leaf explosion—need eviction/merge policy Kedger already has. (4) Prefer aggregate nodes as Evidence summaries with provenance to leaves. |
| **metric_impact** | Results: BFS context BLEU-1/2 0.652/0.532 DISTINCT-1/2 0.072/0.064; DFS 0.624/0.501 & 0.064/…; summary quality >0.8 BLEU/DISTINCT vs references (table in §5). |
| **refine_candidate** | **yes — S5 hierarchical aggregate traversal hydrate** |

---

### 15. StreamBench: Benchmarking Continuous Improvement of Language Agents
**arXiv:2406.08747** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S3', 'S7', 'S8'] |
| **problem** | Agent benches measure static skill, not improvement over an input-feedback stream after deployment. |
| **representation** | StreamBench online setting: agents receive sequential (x_t, feedback); baselines GrowPrompt, MemPrompt, Self-StreamICL, Multi-Agentic-Memory StreamICL, StreamICL across Text-to-SQL/Tool/Medical/HotpotQA etc. |
| **write / read / forget** | Write: store (x, ŷ, fb) in sliding window or external memory M. Read: retrieve past correct self-outputs into prompt. Forget: sliding-window eviction (GrowPrompt). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Kedger needs streaming SLIs: quality vs time under feedback, not one-shot EM. (2) Store correct self-outputs only—noise feedback poisons M. (3) Multi-agent shared memory can beat single-agent average cost-neutral. (4) Robustness to shuffle/distribution shift is a required fixture. |
| **metric_impact** | Table 2 averages across LLM endpoints on Spider/CoSQL/BIRD/DS-1000/ToolBench/DDXPlus/HotpotQA; streaming methods beat non-streaming (Zero/Few/CoT/Self-Refine)—exact per-cell scores in paper tables. |
| **refine_candidate** | **yes — S3/S7 feedback-memory streaming SLI harness** |

---

### 16. Theanine: Timeline-based Memory Management for Lifelong Dialogue Agents
**arXiv:2406.10996** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S3', 'S5', 'S7', 'S8'] |
| **problem** | Prior lifelong agents delete outdated memories; old memories encode valuable behavior-change context for RG. |
| **representation** | Theanine: Phase I memory graph G=(V,E) with relation-aware linking (cause-effect commonsense); Phase II timeline retrieve+untangle+context-aware refine; Phase III timeline-augmented RG; TeaFarm counterfactual eval. |
| **write / read / forget** | Write: link session memories into graph (no removal). Read: retrieve whole timelines then refine. Forget: discards memory removal by design. |
| **conflict** | Edges encode cause-effect; human judges check entail/contradict/neutral to past (4% contradictory responses noted in analyses). |
| **privacy** | Limitation notes API LLMs may raise privacy issues—no mechanism. |
| **Kedger lessons** | (1) Do not default-delete 'stale' Anchors—timeline context is a feature for S7. (2) Retrieve timelines as wholes, not isolated top-k snippets. (3) Relation-aware graph linking ≈ S5 promote with typed edges. (4) TeaFarm-style counterfactual questions are good memory SLIs beyond G-Eval. |
| **metric_impact** | Human/G-Eval: higher retrieval helpfulness+accuracy; 92% judges agree cause-effect linking; helpful-info elicitation 100%/100 samples in fig analysis; TeaFarm counterfactual pipeline results in §5.2. |
| **refine_candidate** | **yes — S5 timeline graph without eager forget + TeaFarm SLI** |

---

### 17. Temporal Knowledge-Graph Memory in a Partially Observable Environment
**arXiv:2408.05861** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S5', 'S6', 'S7'] |
| **problem** | POMDP agents need persistent memory; few benches make both world and memory explicitly graph-shaped. |
| **representation** | Room Environment v3: hidden state RDF KG, observations as triples; agent LTM as temporal KG with RDF-star qualifiers (time_added, last_accessed, num_recalled); symbolic baselines with capacity/eviction vs LSTM/Transformer. |
| **write / read / forget** | Write: assert observed triples into temporal KG with qualifiers. Read: deterministic graph queries/BFS for QA. Forget: capacity limits + simple eviction heuristics. |
| **conflict** | Silent (graph integrity via RDF; no LLM conflict module). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Temporal qualifiers on edges are first-class for S5/S6 Anchor provenance. (2) Capacity eviction should use last_accessed/num_recalled signals. (3) Symbolic KG memory can beat neural seq models under same PO env (~4× QA). (4) Use Room v3 as graph-memory fixture. |
| **metric_impact** | RDF-star ~fourfold higher test QA than neural baselines; symbolic agents beat neural from capacity 32; full coverage of 49 rooms (RDF-star timestep 70 vs RDF 74). |
| **refine_candidate** | **yes — S5/S6 temporal edge qualifiers + capacity eviction** |

---

### 18. KGLA: Knowledge Graph Enhanced Language Agents for Recommendation
**arXiv:2410.19627** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S5', 'S7'] |
| **problem** | LLM rec agents simulate interactions but miss rationales; user profiles inaccurate without KG paths. |
| **representation** | KGLA: extract 2-/3-hop KG paths, translate paths to text, incorporate into agent memory/user profiles for recommendation ranking; reduces input word count vs dumping KG. |
| **write / read / forget** | Write: path-translated text into agent memory/profiles. Read: KG path text for ranking decisions. Forget: Silent. |
| **conflict** | Case study notes profile text can contradict stated dislikes if KG paths wrong—signal only. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Prefer path-to-text Evidence over raw KG dumps for S7 pack size. (2) 2-hop vs 3-hop ablations inform Anchor expansion depth. (3) Agent memory quality (profiles) mediates ranking gains—measure profile fidelity. (4) Watch path noise creating preference contradictions. |
| **metric_impact** | Relative NDCG@1 gains vs best baseline 95.34% / 33.24% / 40.79% on three benchmarks; ~33–95% NDCG@1 boost claimed; also word-count reduction RQ5. |
| **refine_candidate** | **no — rec-specific; path-to-text pattern already common** |

---

### 19. SHARE/EPISODE: Shared Memory-Aware Long-Term Dialogue from Movie Scripts
**arXiv:2410.20682** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S3', 'S4', 'S7'] |
| **problem** | Long-term dialogue ignores shared memories between two speakers that sustain engagement. |
| **representation** | SHARE dataset from movie scripts: personas, events, shared memories; EPISODE framework selects/extracts/updates shared+personal memory during dialogue. |
| **write / read / forget** | Write: extract persona/event/shared memory; update on conflict. Read: memory selection for RG. Forget/update: when extracted info conflicts with existing memory, update policy applies (appendix). |
| **conflict** | Explicit: conflicting extracted info triggers memory update. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Dual-party shared Anchors are distinct from private personas—model share scope. (2) Conflict→update path needed in S4 for shared memories. (3) Dataset prior: 61.57% episodes contain ≥1 shared memory. (4) Engagement metrics should include shared-memory utilization, not only persona hit. |
| **metric_impact** | 61.57% episodes have shared memory; 4,206 shared memories / 20,703 mutual events in SHARE; automatic + human engagingness/coherence tables for EPISODE vs ablations (Gemma rows e.g. metric bundles in §5). |
| **refine_candidate** | **yes — S4 shared-memory scope + conflict update** |

---

### 20. Planning from Imagination: Episodic Simulation and Memory for VLN
**arXiv:2412.01857** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S2', 'S3', 'S7'] |
| **problem** | VLN agents lack human-like episodic simulation/memory for unseen environments. |
| **representation** | Reality–imagination hybrid memory map; recurrent imagination tree with high-fidelity RGB generation + cross-correction; multimodal transformer + imagination pretraining; dynamic action planning over memory. |
| **write / read / forget** | Write: update hybrid map from real observations and imagined futures. Read: plan actions from memory map. Forget: Silent. |
| **conflict** | Silent (cross-correction aligns imagination vs reality). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Embodied S2 can hold imagined futures as provisional Evidence (not Anchors). (2) Cross-correction before promote prevents hallucinated map Anchors. (3) Reality-only ablation lags SoTA by 12%/9%—imagination is load-bearing. (4) Keep simulation traces out of sealed packs until verified. |
| **metric_impact** | SPL +8% (R2R) and +4% (REVERIE) unseen vs prior; SoTA 12% and 9% higher than reality-only. |
| **refine_candidate** | **no — embodied VLN-specific simulation** |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (honest deep-recard) | 20 |
| Cumulative FULL | **360** |
