# Batch 22 — Survey Runway FULL (Kedger) — **honest deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Body-grounded mechanism cards (Intro/Method/Results) replacing 2026-08-08 abstract-template cards.  
> **Progress:** FULL 420 → **440**.  
> **Method:** Fulltext `/tmp/kedger-papers/full/{id}.txt` + agent deep-read cards.  
> **Kedger stages:** S1–S8  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers from body only.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body deep-read; deep-recard upgrade of Batch22) | **20** | `2309.06794`, `2309.07870`, `2310.02172`, `2310.03025`, `2310.05036`, `2310.06500`, `2310.09233`, `2310.10436`, `2311.05876`, `2311.05997`, `2311.11315`, `2311.17227`, `2312.04889`, `2401.05459`, `2401.07128`, `2402.14034`, `2402.18485`, `2403.04317`, `2403.17134`, `2404.09982` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs cached |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. Cognitive Mirage: A Review of Hallucinations in Large Language Models
**arXiv:2309.06794** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S7, S8 |
| **problem** | LLM text generation produces hallucinations (intrinsic conflict with input / extrinsic unverifiable content); taxonomy, detection, and mitigation are fragmented across tasks. |
| **representation** | Survey taxonomy of hallucinations across generation tasks: Intrinsic (conflicts with input) vs Extrinsic (unverifiable fabricated facts); analyzes causes, detection methods, and improvement approaches; proposes future directions. Frames faithfulness vs factualness orientations. |
| **write / read / forget** | Write: silent — survey of generation failures, not a memory store. Read: surveys detection over model outputs vs sources. Forget: silent. |
| **conflict** | Core lens: intrinsic hallucination = conflict with input; survey also covers knowledge/factual inconsistency. No typed SUPERSEDES protocol. |
| **privacy** | Mentions privacy/timeliness of real-world data as a contributing factor to outdated/hallucinated knowledge; no membership attack study. |
| **Kedger lessons** | (1) S8 `why` / Anchor promotion must distinguish intrinsic (Evidence contradiction) vs extrinsic (unsupported claim) failures. (2) S7 pack compile should run faithfulness checks against retrieved Evidence before answer. (3) Do not treat parametric fluency as Anchor ground truth — require cite spans. (4) Survey-only — extract fixture classes for hallucination SLIs, not a store op. |
| **metric_impact** | Taxonomy coverage / detection-method catalog (no single numeric leaderboard in body). |
| **refine_candidate** | **yes — S4/S7/S8 hallucination taxonomy fixtures for promote+hydrate** |

---

### 2. Agents: An Open-source Framework for Autonomous Language Agents
**arXiv:2309.07870** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S5, S7 |
| **problem** | Building controllable LLM agents is hard for non-specialists; frameworks often rely on short task descriptions and suffer run-to-run inconsistency without symbolic plans. |
| **representation** | Agents library: Agent + Environment + SOP (Standard Operating Procedure) symbolic plans from plain-text config. Long-term memory via VectorDB semantic search; short-term working memory via scratchpad; tool/web navigation; multi-agent communication; Agent Hub + auto system creation. |
| **write / read / forget** | Write: store/retrieve long-term memory in VectorDB; regularly update short-term scratchpad. Read: semantic search over long-term memory. Forget: silent on eviction — config chooses LTM/STM/both. |
| **conflict** | SOP symbolic control targets run inconsistency vs free-form LLM planning; silent on typed SUPERSEDES among Anchors. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Separate L2 scratchpad WorkingState from L3 VectorDB long-term like Agents' dual memory config. (2) SOP-style symbolic plans map to Kedger sealed workflows — reduce hydrate nondeterminism. (3) Multi-agent message hubs need explicit memory ownership per agent. (4) Prefer config-declared memory toggles over always-on unbounded VectorDB growth. |
| **metric_impact** | Case-study systems (single/multi-agent); no aggregate QA metric — library paper. |
| **refine_candidate** | **no (framework pattern already covered by MemGPT/AIOS lineage)** |

---

### 3. Lyfe Agents: Generative agents for low-cost real-time social interactions
**arXiv:2310.02172** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Generative agents are too expensive for real-time human interaction while remaining goal-oriented and socially coherent. |
| **representation** | Lyfe Agents modular brain: sensory → internal states + Memory. Three mechanisms: (1) option-action framework (cheap high-level options, rare LLM decisions); (2) asynchronous self-monitoring for goal adherence; (3) Summarize-and-Forget (SaF) hierarchical memory prioritizing critical items. Eval in LyfeGame 3D multi-agent scenarios (murder mystery, activity fair). |
| **write / read / forget** | Write: experiences into hierarchical memory with SaF summarization. Read: retrieve prioritized critical items for decisions. Forget: explicit Summarize-and-Forget discards low-priority detail while retaining summaries. |
| **conflict** | Self-monitoring reduces self-inconsistency; silent on inter-doc SUPERSEDES. |
| **privacy** | Scenario lore includes secrets among agents (eval content); silent on system privacy controls. |
| **Kedger lessons** | (1) WorkingState pressure should use Summarize-and-Forget, not only truncate. (2) Option-action ≈ cheap cognify vs rare expensive plan calls under token budget. (3) Async self-monitor is an S8 consistency probe mid-session. (4) Cost SLI must track $/agent-hour for multi-agent sims, not only EM. |
| **metric_impact** | Social behavior / opinion-change interviews; ablations of option-action, self-monitor, SaF; cost analysis vs Generative Agents-class baselines. |
| **refine_candidate** | **yes — S2/S3 Summarize-and-Forget under WorkingState pressure** |

---

### 4. Retrieval meets Long Context Large Language Models
**arXiv:2310.03025** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Unclear whether extending context windows or retrieval-augmentation is better for long-context tasks, and whether they combine. |
| **representation** | Compare 4K→16K/32K context via positional interpolation vs retrieval-augmented generation on proprietary GPT-43B and Llama2-70B across nine long-context tasks (QA, query summarization, few-shot). Retrieval treated as sparse attention over context (unretrieved tokens zero weight). |
| **write / read / forget** | Write: silent — no persistent memory; retrieval over external corpus at generation. Read: retrieve then generate; optionally combine with long window. Forget: silent (truncation of non-retrieved context). |
| **conflict** | Silent. |
| **privacy** | Notes train-test leakage concerns in hard MSQ construction; silent on embedding privacy. |
| **Kedger lessons** | (1) S7 hydrate: 4K+retrieve can match 16K finetuned long-context (paper: GPT-43B avg 29.32 vs 29.45; Llama2-70B 36.02 vs 36.78) at far less compute — prefer retrieve over blind window growth. (2) Best reported: retrieval-augmented Llama2-70B-32K beats GPT-3.5-turbo-16k / Davinci-003 avg score. (3) Do not assume long window makes retrieve obsolete — combine when both available. (4) Measure compute×quality, not window size alone. |
| **metric_impact** | Average score on nine long-context tasks; ablations 4K/16K/32K ± retrieval. |
| **refine_candidate** | **yes — S7 retrieve-vs-long-context budget SLI** |

---

### 5. AvalonBench: Evaluating LLMs Playing the Game of Avalon
**arXiv:2310.05036** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Strategic social deduction (Resistance Avalon) requires deception, deduction, and multi-phase decisions — existing LLM agent benches under-test hidden-role social reasoning. |
| **representation** | AvalonBench: game environment + rule-based bots + ReAct-style LLM agents with role-specific prompts. Agents must discuss, deceive, accuse, and vote across quest phases without revealing true identity. |
| **write / read / forget** | Write: silent persistent memory beyond in-game dialogue history. Read: observe discussion/votes; ReAct tool-style act loop. Forget: prompt instructs agents not to forget identity — no memory eviction API. |
| **conflict** | Deception/accusation create intentional conflicting claims; no structured ConflictSet. |
| **privacy** | Hidden roles / confidential identity are game mechanics; silent on PII. |
| **Kedger lessons** | (1) Multi-agent S8 must track belief vs stated claim under deception — Avalon-style fixtures. (2) Role prompts are S1 hooks that must not leak across agents. (3) Eval SLI = win rate vs rule bots + human-like persuasion quality, not EM. (4) Patience/baseline-behavior cues ≈ provenance signals for untrusted peer Evidence. |
| **metric_impact** | Win rates of ReAct LLM agents vs rule-based bots across Avalon roles; qualitative discussion competence. |
| **refine_candidate** | **yes — S7/S8 multi-agent deception/belief fixtures** |

---

### 6. MetaAgents: Large Language Model Based Agents for Decision-Making on Teaming
**arXiv:2310.06500** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | LLM social sims underexplore task-oriented teaming — matching expertise to roles and assembling workflows. |
| **representation** | MetaAgents social simulation: LLM agents converse and decide to form teams / design workflows in progressive scenarios of increasing participant complexity; evaluates alignment of agent expertise to roles. |
| **write / read / forget** | Write: agents maintain conversational state / role commitments across teaming decisions. Read: retrieve info via communication among agents. Forget: silent. |
| **conflict** | Agents often agree even when answers contradict pre-defined settings (misplacement); honesty/alignment failures under scale. |
| **privacy** | Silent (social sim). |
| **Kedger lessons** | (1) Multi-agent promote: expertise↔role matching is an S5 graph constraint, not free chat. (2) Paper: Scenario1 success 64% → Scenario2 48% → Scenario3 12% as participants grow — scale stress tests for team compose. (3) Dishonest/agreeable agents → require capability-scope checks before role commit. (4) Team assembly SLI separate from task-solve EM. |
| **metric_impact** | Team formation success rate / correct expertise-workflow match across scenarios (64%/48%/12%/56% reported). |
| **refine_candidate** | **yes — S5 multi-agent role-alignment promote gate** |

---

### 7. AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems
**arXiv:2310.09233** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | LLM agents mostly simulate dialogue; user-item preference behaviors for recommender CF are underexplored due to language↔behavior gap. |
| **representation** | AgentCF: both user and item are agents with memory of preferences/adopter tastes. Loop: prompt user↔item autonomous interaction → compare to real interaction → collaborative reflection to fix misconceptions → preference propagation to other agents. Trains on ~0.07% of full dataset in reported setting. |
| **write / read / forget** | Write: update user/item agent memories from reflections on interaction disparities. Read: memories condition next autonomous choices. Forget: preference signal decays across propagation (information diffusion). |
| **conflict** | Reflection targets inconsistent decisions vs real-user records; collaborative fix rather than typed SUPERSEDES. |
| **privacy** | Item memory injected into interacting users' preferences — preference leakage across users; paper is recsys not privacy-first. |
| **Kedger lessons** | (1) Dual-agent memory (user+item) maps to bidirectional Anchors with interaction edges. (2) Collaborative reflection ≈ S3 cognify when hydrate disagrees with observed outcome. (3) Preference propagation needs decay/forget like paper's diffusion — unbounded share pollutes. (4) ~95% correct user-agent choices at reported step — use as CF-memory SLI, not chat EM. |
| **metric_impact** | Recommendation ranking / choice accuracy under sparse training; propagation ablations. |
| **refine_candidate** | **yes — S3 collaborative reflection when memory≠observed outcome** |

---

### 8. EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities
**arXiv:2310.10436** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Macro ABM agents use rigid rules or opaque NNs — hard to customize heterogeneity and incorporate multi-period market dynamics. |
| **representation** | EconAgent: LLM household/firm agents with perception of market dynamics + memory module. Memory pool keeps 2L+1 conversations (prior L months env+decisions); quarterly LLM reflection on labor/consumption/financial phenomena to guide later decisions. |
| **write / read / forget** | Write: append monthly env/decision dialogues; quarterly reflect summaries into memory. Read: condition decisions on memory pool. Forget: pool windowed to 2L+1 (implicit FIFO beyond L). |
| **conflict** | Silent on contradictory market beliefs; realism via emergent inflation/unemployment vs rule baselines. |
| **privacy** | Silent (sim). |
| **Kedger lessons** | (1) Rolling memory window + periodic reflect = S2/S3 pattern for long-running agents. (2) Quarterly reflection is cognify cadence, not every-turn summarize. (3) Heterogeneous prompt personas ≈ capability-scoped agent profiles. (4) Eval via macroeconomic realism (inflation/unemployment), not QA EM — choose SLIs accordingly. |
| **metric_impact** | Realism of inflation / unemployment vs rule-based and learning-based ABM baselines. |
| **refine_candidate** | **no (domain sim; pattern absorbed by Lyfe/Generative Agents memory tickets)** |

---

### 9. Trends in Integration of Knowledge and Large Language Models: A Survey and Taxonomy
**arXiv:2311.05876** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S5, S7 |
| **problem** | LLMs suffer outdated/domain-limited knowledge; knowledge editing and retrieval augmentation evolved separately without a unifying survey. |
| **representation** | Survey taxonomy of knowledge integration: knowledge editing vs retrieval augmentation; methods, benchmarks, applications; dedicated Knowledge Conflict section (internal parametric conflict vs external retrieved conflict). |
| **write / read / forget** | Write: surveys parameter/edit writes and RAG indexes. Read: surveys retrieve-augmented generation. Forget: cites deletion/unlearning work; not a new mechanism. |
| **conflict** | Taxonomizes Internal vs External knowledge conflict (§3.4) — primary conflict map for RAG+edit systems. |
| **privacy** | Touches injected knowledge / sensitive deletion literature; not a privacy system. |
| **Kedger lessons** | (1) Treat knowledge editing (parametric) and RAG (Evidence) as distinct write paths — don't conflate in S3/S4. (2) ConflictSet must cover internal↔external clashes per survey taxonomy. (3) Use survey as catalog for hydrate strategies, not duplicate GraphRAG community summaries. (4) Benchmarks listed → SLI menu for knowledge freshness. |
| **metric_impact** | Survey taxonomy completeness; cites existing KE/RAG benchmarks (no new single score). |
| **refine_candidate** | **no (survey catalog)** |

---

### 10. JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models
**arXiv:2311.05997** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Open-world Minecraft agents fail when task space is huge and cannot progressively improve planning from survival experience. |
| **representation** | JARVIS-1: multimodal LLM planner + low-level controller + multimodal memory storing scenarios and successful plans; retrieves relevant past plans for new tasks. Self-instruct exploration proposes tasks and saves experiences. Completes >200 Minecraft Universe Benchmark tasks. |
| **write / read / forget** | Write: save successful planning experiences (scenario+plan) into multimodal memory; self-instruct growth. Read: retrieve relevant memory entries to strengthen planning. Forget: silent explicit eviction. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Experience memory should store (situation, successful plan) pairs for S7 hydrate — not raw frames only. (2) Self-instruct exploration = optional S3 growth loop gated by success. (3) Diamond pickaxe: up to 12.5% success; ~3× DEPS on related metrics (8.99% vs 2.42%) — long-horizon SLIs need time budgets. (4) Memory-augmented planning improves weaker LMs toward GPT-4-class Minecraft plans per paper tables. |
| **metric_impact** | Success rates on 200+ Minecraft tasks; ObtainDiamondPickaxe reliability vs VPT/DEPS; long-horizon improvement over game time. |
| **refine_candidate** | **yes — S7 multimodal experience-memory retrieve for planning** |

---

### 11. TPTU-v2: Boosting Task Planning and Tool Usage of Large Language Model-based Agents
**arXiv:2311.11315** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7 |
| **problem** | Real systems expose huge API sets; can't stuff all descriptions in prompt; demos hard to select; base LLMs weak at planning+tool use. |
| **representation** | TPTU-v2 framework: (1) API Retriever selects pertinent APIs; (2) LLM Finetuner improves planning/tool usage; (3) Demo Selector picks useful few-shots. Eval on commercial security-system APIs (~45 APIs, 11 functionalities). |
| **write / read / forget** | Write: finetune/demo pool offline. Read: retrieve APIs + demos into prompt for task. Forget: silent. |
| **conflict** | Silent on conflicting API results. |
| **privacy** | Eval uses commercial security system APIs — domain sensitivity; silent on data exfil defenses. |
| **Kedger lessons** | (1) S1/S7: never hydrate all tools — API Retriever (Recall@5 84.64%, Recall@10 98.47%). (2) Demo selector alone lifts base LLM accuracy dramatically (paper: 38.89%→95.55% with demos+oracle APIs path). (3) Finetuned LLM + retriever ~80% — combine retrieve+tune. (4) Tool Evidence must be capability-scoped like security APIs. |
| **metric_impact** | API Recall@5/@10; end-task accuracy across base/finetuned × retriever/demo ablations. |
| **refine_candidate** | **yes — S7 tool/API retrieve before pack compile** |

---

### 12. War and Peace (WarAgent): Large Language Model-based Multi-Agent Simulation of World Wars
**arXiv:2311.17227** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Can LLM multi-agent sims reproduce historical conflict dynamics (WWI/WWII/Warring States) and distinguish memory regurgitation from reasoning? |
| **representation** | WarAgent: country agents with diplomatic actions (alliance, war declaration, non-intervention, etc.); Board visualizations; experiments testing whether outcomes stem from LLM memory vs reasoning under varied settings. |
| **write / read / forget** | Write: agents update diplomatic state across turns. Read: observe boards/other agents' actions. Forget: silent. |
| **conflict** | Core object is international conflict simulation; alliances may be confidential or betrayed — social conflict, not doc SUPERSEDES. |
| **privacy** | Alliances can be confidential; betrayal possible — confidentiality as game rule. |
| **Kedger lessons** | (1) Multi-agent S8 should log casus belli / decision boards as `why` traces. (2) Separate parametric historical memory from simulation reasoning — paper's two experiments. (3) 100% war-declaration rate in reported sims → over-aggression SLI for multi-agent. (4) Confidential alliance state ≈ Inv-Scope share tiers among agents. |
| **metric_impact** | Simulation fidelity vs historical timelines; alliance/war declaration frequencies across runs. |
| **refine_candidate** | **no (historical sim; S8 board-logging pattern only)** |

---

### 13. KwaiAgents: Generalized Information-seeking Agent System with Large Language Models
**arXiv:2312.04889** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Information-seeking needs planning, tool use, memory, and reflection under constrained LLM size — humans compensate with tools despite forgetting ~50% new info/hour. |
| **representation** | KwaiAgents: KAgentSys loop (memory bank + tool library + task planner + concluding module); KAgentLMs open-source finetuned suite; time-aware search-browse toolkit. Benchmark mixes no-memory / conversational / task-history / external-knowledge queries (20.64%/48.12%/16.23%/15.01%). |
| **write / read / forget** | Write: update internal memory bank from interactions. Read: retrieve memory + external search/browse. Forget: cites human forgetting curve as motivation; system keeps memory bank (no explicit decay API detailed in abstract). |
| **conflict** | Benchmark includes conflicting information types vs query; Reflection vs Planning&Tool-use distinguished. |
| **privacy** | Memory blocks optionally injected into prompts — memory-aware generation; silent on unshare. |
| **Kedger lessons** | (1) Hydrate path must branch: memory vs tools vs external knowledge per query type mix. (2) Concluding module = S8 answer synthesis after tool/memory loop. (3) Time-aware search ≈ recency prior on Evidence. (4) Eval split by memory type (none/conv/task/external) — don't collapse into one EM. |
| **metric_impact** | KAgentBench-style task success across memory/tool settings; open vs closed LLM cores. |
| **refine_candidate** | **yes — S7 memory-type-conditioned hydrate routing** |

---

### 14. Personal LLM Agents: Insights and Survey about the Capability, Efficiency and Security
**arXiv:2401.05459** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S6, S7 |
| **problem** | Personal assistants deep-integrated with personal data/devices need architecture, capability, efficiency, and security guidance beyond generic LLM agents. |
| **representation** | Survey of Personal LLM Agents: architecture components (sensing, memory, task automation), expert-opinion analysis, challenges/solutions for intelligent/efficient/secure personal agents; levels of personalization. |
| **write / read / forget** | Write/read: surveys personal memory over device/personal data. Forget: discusses workflow pruning of bad explorations (related work). |
| **conflict** | Consistency checks across multiple responses as reliability signal when answers contradict. |
| **privacy** | First-class: security & privacy section; expert survey — 88% prefer edge-cloud collaboration; personal data is the threat surface. |
| **Kedger lessons** | (1) Personal Anchors require Inv-Scope / device-local tiers before cloud hydrate. (2) Architecture must separate sensing → memory → automation like survey stack. (3) Efficiency (edge-cloud) is an SLI alongside quality — 58.33% support local deploy in survey opinions. (4) Use as design checklist for S6 seal of personal packs, not another GraphRAG. |
| **metric_impact** | Expert preference rates; capability-level taxonomy (no single model score). |
| **refine_candidate** | **yes — S6 personal-data Inv-Scope checklist from survey** |

---

### 15. EHRAgent: Code Empowers Large Language Models for Few-shot Complex Tabular Reasoning on EHRs
**arXiv:2401.07128** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7, S8 |
| **problem** | Clinicians can't efficiently query complex multi-table EHRs; need LLM agents that generate/execute code with domain knowledge under few-shot limits. |
| **representation** | EHRAgent: tool-use formulation for multi-tabular EHR reasoning; autonomous code generation/execution; long-term memory of successful cases with dynamic few-shot selection; interactive debugging / plan modification loop. |
| **write / read / forget** | Write: store successful code+query cases in long-term memory. Read: select relevant few-shots for new queries; execute code tools on EHR tables. Forget: silent. |
| **conflict** | Notes conflict between limited context and number of few-shots; debugging resolves execution failures, not doc contradictions. |
| **privacy** | Medical EHR domain — injects relevant medical info for reasoning; clinical privacy critical though not a crypto contribution. |
| **Kedger lessons** | (1) Code-as-tool hydrate for structured stores beats pure text RAG on tables. (2) Success-case memory = S3 promote of verified trajectories for few-shot. (3) Up to +29.6% success vs strongest baseline / multi-hop — lock as EHR-agent SLI. (4) Debug loop must update plan (S8) not blindly retry. |
| **metric_impact** | Success rate on EHR multi-table QA; multi-hop gains; debugging ablations. |
| **refine_candidate** | **yes — S7 code-tool hydrate + success-case memory** |

---

### 16. AgentScope: A Flexible yet Robust Multi-Agent Platform
**arXiv:2402.14034** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S5, S7 |
| **problem** | Multi-agent apps hard to build robustly under LLM erraticness; need developer-centric platform with reliable messaging. |
| **representation** | AgentScope: message-exchange core; built-in agents/services; memory module + message hub; syntactic tools; critique modes (self/pairwise/human-augmented) for semantic error checking; logging; robust distribution utilities. |
| **write / read / forget** | Write: agent memory module stores messages/state. Read: message hub distribution among agents. Forget: hub.delete(agent) removes participants from broadcast. |
| **conflict** | Critique path targets factual inaccuracy / logical inconsistency / contextual incoherence. |
| **privacy** | Silent beyond platform logging concerns. |
| **Kedger lessons** | (1) Multi-agent Kedger should standardize message envelopes like AgentScope hubs. (2) Memory module per agent + shared hub = ownership clarity. (3) Built-in critique ≈ S8 verify before promote. (4) Robustness hooks (retry/logging) belong in S1, not only model prompts. |
| **metric_impact** | Platform case studies / robustness features (developer paper). |
| **refine_candidate** | **no (platform engineering pattern)** |

---

### 17. FinAgent: A Multimodal Foundation Agent for Financial Trading
**arXiv:2402.18485** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7, S8 |
| **problem** | Financial trading needs multimodal (news/price/Kline) reasoning, tools, and diversified memory — prior DL/RL agents lack generalist tool-augmented trading. |
| **representation** | FinAgent: market intelligence over numerical/textual/visual data; tool augmentation; diversified memory retrieval; reasoning-for-actions for trust; trading decisions across assets/tasks. |
| **write / read / forget** | Write: store diversified historical trading experiences in memory. Read: diversified memory retrieval + tools for market analysis. Forget: silent explicit eviction. |
| **conflict** | Discusses forecast vs market contradiction cases (prediction inconsistency). |
| **privacy** | Emphasizes capital security / long-term prudence; not PII privacy. |
| **Kedger lessons** | (1) Diversified memory retrieval (not single similarity) for S7 when modalities differ. (2) Action rationale required for S8 trust in high-stakes domains. (3) Paper: >36% avg profit metric improvement; 92.27% return (84.39% relative) on reported asset — domain SLIs ≠ QA. (4) Tool-augmented multimodal Evidence packs over price-only features. |
| **metric_impact** | Six financial metrics / profit return vs FinMem and other trading baselines. |
| **refine_candidate** | **no (finance-domain agent; memory diversification lesson only)** |

---

### 18. Online Adaptation of Language Models with a Memory of Amortized Contexts (MAC)
**arXiv:2403.04317** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | LLMs go stale; online adaptation over streaming documents must be memory/time efficient without catastrophic forgetting. |
| **representation** | MAC (Memory of Amortized Contexts): compress/extract features from new documents into compact amortized contexts stored in memory bank M; adapt LM by aggregating memory given a question. Strong retention vs CaMeLS; works with other adapters. |
| **write / read / forget** | Write: compress new docs into amortized memory entries. Read: aggregate relevant memory for query-time adaptation. Forget: compression discards raw doc tokens; retains amortized features (catastrophic forgetting mitigated vs full finetune). |
| **conflict** | Cites entity-based knowledge conflicts literature; not MAC's core algorithm. |
| **privacy** | Notes privacy concerns when saving user documents — responsible use caveat. |
| **Kedger lessons** | (1) Online cognify should amortize docs into compact memory tokens, not store raw. (2) MAC: −68.0% memory vs CaMeLS per-doc; retains 96.2% initial performance vs CaMeLS 70.8%. (3) F1 71.83→74.89 on LLaMA-2-7B reported case — adaptation SLI. (4) Private raw docs must not enter shared amortized banks without Inv-Scope. |
| **metric_impact** | Online adaptation F1/perplexity; memory bytes; wall-time vs CaMeLS/RAG alternatives. |
| **refine_candidate** | **yes — S3 amortized context memory for online doc ingest** |

---

### 19. RepairAgent: An Autonomous, LLM-Based Agent for Program Repair
**arXiv:2403.17134** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Prior APR uses fixed prompts/feedback loops; need an LLM agent that autonomously plans tool use to gather info, ingredients, and validate fixes. |
| **representation** | RepairAgent: autonomous LLM agent with finite-state guidance invoking tools (read code, write fix, run tests, discard_hypothesis, etc.); interleaves information gathering, repair, validation on Defects4J. |
| **write / read / forget** | Write: write_fix tool proposes patches; hypotheses tracked in agent state. Read: gather bug/repair ingredients via tools. Forget: discard_hypothesis / discard paths return to earlier states. |
| **conflict** | Hypothesis discard when inconsistent with evidence; test failures drive replanning. |
| **privacy** | Security vulnerabilities as bug class; silent on secrets in repos. |
| **Kedger lessons** | (1) S1 tool allowlist + state machine constrains agent actions like RepairAgent. (2) discard_hypothesis = explicit belief invalidation for S8. (3) 164/835 Defects4J bugs fixed incl. 39 unique; ~270k tokens (~$0.14) per bug — cost SLI. (4) 99% time in tool execution — hydrate budget is tools, not prompt length. |
| **metric_impact** | Defects4J bugs fixed; unique fixes vs prior APR; token/$ cost; tool-call stats. |
| **refine_candidate** | **yes — S1/S7 state-machine tool agent for repair-like loops** |

---

### 20. INMS: Interactive Memory Sharing for Large Language Model based Agents
**arXiv:2404.09982** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S6, S7 |
| **problem** | Open-ended LLM agents stay isolated on static DBs — miss dynamic knowledge exchange of human dialogue; shared pools risk echo chambers. |
| **representation** | INMS: asynchronous multi-agent memory sharing with real-time filtering, storage, retrieval into a shared conversational memory pool; mediator refined from interaction history; mitigates echo chamber from initial biased pools; domain-specific vs integrated pools studied. |
| **write / read / forget** | Write: agents contribute filtered memories to shared pool. Read: retrieve curated experiential context per query. Forget: filtering/selection limits what enters pool; dynamics as pool expands 0→100%. |
| **conflict** | Echo chamber = biased shared memory dominating answers; INMS curation mitigates. |
| **privacy** | Shareable memories across agents/tasks — cross-agent leakage surface; paper focuses on utility not ACLs. |
| **Kedger lessons** | (1) Shared memory pools need S6 share policies + filters before cross-agent hydrate. (2) Domain-specific pools beat one integrated pool for relevance (paper Fig.3 lesson). (3) Track echo-chamber SLI as pool grows (0/25/50/75/100%). (4) Cross-task shareable memories can help if filtered — not blanket isolate. |
| **metric_impact** | Agent response quality/accuracy across three datasets; ablations on pool composition and interaction accumulation. |
| **refine_candidate** | **yes — S5/S6 filtered shared-memory pool with echo-chamber SLI** |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (honest deep-recard) | 20 |
| Cumulative FULL | **440** |
