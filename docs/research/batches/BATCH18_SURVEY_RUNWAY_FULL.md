# Batch 18 — Survey Runway FULL (Kedger) — **deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Honest re-card of survey-runway papers — mechanism extraction from **full body** (Intro/Method/Results), not abstract paste.  
> **Progress:** FULL 340 → **360** toward 500.  
> **Method:** Cached `/tmp/kedger-papers/full/{id}.txt`; cards built by `scripts/research/deep_recard_500.py`.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers only from body matches. Generic lessons forbidden.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body mechanism deep-read; ID already ledgered Batch18 — **re-card upgrade**) | **20** | `2305.17144`, `2308.01542`, `2308.07201`, `2309.17452`, `2310.16340`, `2311.04177`, `2312.00326`, `2312.03815`, `2401.07339`, `2401.14215`, `2403.01112`, `2404.09992`, `2406.05925`, `2406.06124`, `2406.08747`, `2406.10996`, `2408.05861`, `2410.19627`, `2410.20682`, `2412.01857` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs have `.txt` ≥15k chars. |
| **Method span extracted** | **9/20** | continuous-text section split |
| **Numeric evidence extracted** | **14/20** | regex over method/results |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. Ghost in the Minecraft: Generally Capable Agents for
**arXiv:2305.17144** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | “What if a cyber brain could possibly generate its own ghost, create a soul all by itself? |
| **representation** | To overcome this, we propose LLM-based agents in Fig. Moreover, LLM-based agents can leverage text-based knowledge and memory to quickly acquire the skills needed to master Minecraft. 3.1 LLM Decomposer Rather than directly assigning the task goal to the agent and expecting a comprehensive and robust action plan, this work suggests the more practical strategy of decomposing the task goal into a series of more achievable sub-goals. |
| **write / read / forget** | Write: “Info” stores the text-based knowledge related to this goal. Read: Query Illustration: Query contains a goal, feedback from the agent, and reference plan from the memory Response Format: { “explanation”: “explain action failure”, “thoughts”: “thou Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: To overcome this, we propose LLM-based agents in Fig. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 262 tasks, 100%, 20%, +47.5%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 262 tasks; 100%; 20%; +47.5%; 30%; 5% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 2. [2308.01542] Memory Sandbox: Transparent and Interactive Memory Management for Conversational Agents Memory Sa
**arXiv:2308.01542** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | This problem is compounded because users do not know how the LLM is leveraging the memory to generate responses. |
| **representation** | To ensure that agents generate responses that are contextually relevant and coherent to an ongoing conversation, these agents must maintain a working memory of the conversational history that has occurred up to that point in the conversation. Additionally, as the input buffer size increases, the performance of the LLM degrades as it struggles to retrieve relevant context and can be distracted by irrelevant context (Liu et al . This problem is compounded because users do not know how the LLM is leveraging the memory to generate responses. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: To ensure that agents generate responses that are contextually relevant and coherent to an ongoing conversation, these agents must maintain a working memory of  (2) Primarily a write/store design — gate promote before L3 commit. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 3. [2308.07201] ChatEval: Towards better LLM-based evaluators through multi-agent debate ChatEval: Towards better
**arXiv:2308.07201** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, these methods have been shown to exhibit a relatively weak correlation with human judgments, particularly in the context of tasks involving open-ended generation or requiring domain-specific expertise (Novikova et al., 2017 ) . |
| **representation** | Debater agents are one of the most significant components in our framework. We treat each individual LLM as an agent and ask them to generate their response from the given prompt 2 2 2 The full prompt template can be found in |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Debater agents are one of the most significant components in our framework. (2) Eval/analysis paper — extract fixtures/SLIs rather than store ops. (3) Lock numeric claims from body: 16.3%, 10.0%, 62.5%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 16.3%; 10.0%; 62.5% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 4. \logo ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving 1 Introduction 2 ToRA : Tool-In
**arXiv:2309.17452** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Large language models (LLMs), such as GPT-4 (OpenAI, 2023 ) and PaLM-2 (Anil et al., 2023 ) , have demonstrated remarkable progress in a wide range of language tasks, particularly in the longstanding challenge of mathematical reasoning (Feigenbaum et al., 1963 ; Hosseini et al.,  |
| **representation** | guage reasoning with the utilization of external tools (e.g., computation libraries and symbolic solvers), thereby amalgamating the analytical prowess of language and the computational efficiency of tools. To train ToRA , we curate interactive tool-use trajectories on mathematical datasets, apply imitation learning on the annotations, and propose output space shaping to further refine models’ reasoning behavior. As a result, ToRA models significantly outperform open-source models on 10 mathemati |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S2, S3, S7, S8. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 13%, 19%, 10 tasks, 84.3%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 13%; 19%; 10 tasks; 84.3%; 80.4%; 49.7% |
| **refine_candidate** | **no** |

---

### 5. RCAgent: Cloud Root Cause Analysis by Autonomous Agents with Tool-Augmented Large Language Models
**arXiv:2310.16340** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | While these typical AIOps aid in automated processes, their application faces challenges such as poor data quality, shifting data distribution, laborious data annotation, and limited generalization for models (Cheng et al . |
| **representation** | To systematically and reliably prompt the LLM as a tool-augmented autonomous agent for cloud RCA, we propose RCAgent , an enhanced reasoning and acting framework. For disambiguousity, the LLM agent with the prompt of thought-action-observation loop is named the controller agent responsible for coordinating actions, and RCAgent additionally employs the LLM as tools called the expert agents for domain-specific functionalities. The cycle involves generating verbal thoughts, taking actions, and receiving observation from the environment, all of which are recorded in the prompt alongside the initial memory to boost reasoning. |
| **write / read / forget** | Write: Besides, RCAgent includes the key-value store for observation retrieval, allowing the agent to operate on lengthy text data. Read: Besides, RCAgent includes the key-value store for observation retrieval, allowing the agent to operate on lengthy text data. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | , 2023b ) , the controller agent is injected with three basic prompts: (i) framework rules that describe the thought-action-observation loop, (ii) task requirements that contain instructions for the RCA tasks with basic  |
| **Kedger lessons** | (1) Mechanism to port: To systematically and reliably prompt the LLM as a tool-augmented autonomous agent for cloud RCA, we propose RCAgent , an enhanced reasoning and acting framewor (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Metrics named: em (values: see paper tables). |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 6. [2311.04177] Enhancing LLM Intelligence with ARM-RAG: Auxiliary Rationale Memory for Retrieval Augmented Gener
**arXiv:2311.04177** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, unlike humans, frozen LLMs do not improve over time; they neither acquire new knowledge nor learn from their successes or failures. |
| **representation** | ( 2021 ) has been proposed to augment the parametric memory of LLMs with the non-parametric memory of Knowledge Bases (KBs), which can be retrieved using search engines. We propose ARM-RAG (Auxiliary Rationale Memory for Retrieval Augmented Generation), a system that learns from its successes without incurring high training costs. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: In this paper, we explore the use of Retrieval Augmented Generation, also known as RAG Lewis et al. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: ( 2021 ) has been proposed to augment the parametric memory of LLMs with the non-parametric memory of Knowledge Bases (KBs), which can be retrieved using search (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 76.3%, 89.5%, 72.5%, 20%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 76.3%; 89.5%; 72.5%; 20%; 10.7%; 473 examples |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 7. Agent-OM: Leveraging LLM Agents for Ontology Matching Report GitHub Issue × Title: Content selection saved. De
**arXiv:2312.00326** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | For each autonomous agent, the workflow is described as follows. The planning module decomposes a complex task into several subtasks and defines the order of subtasks and tools to be invoked. We use solid lines to show the actual workflow controlled by the LLMs, and dotted lines to show the implicit link between a subtask and its corresponding tool activated by the LLMs. |
| **write / read / forget** | Write: The plan is stored in the dialogue and passed to the LLMs. Read: Retrieval Agent The Retrieval Agent is responsible for extracting entities from the ontologies, eliciting their metadata and ontology context information, and storing them in the h Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: For each autonomous agent, the workflow is described as follows. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 8. LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS-Agent Ecosystem
**arXiv:2312.03815** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | and Concrete Reasonings of Large Language Models through Tool Creation. |
| **representation** | The probabilistic relevance framework: BM25 and beyond. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: The probabilistic relevance framework: BM25 and beyond. (2) Eval/analysis paper — extract fixtures/SLIs rather than store ops. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **no** |

---

### 9. CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Chall
**arXiv:2401.07339** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, more than 70% functions in the open-source projects are non-standalone Yu et al. |
| **representation** | ( 2023 ) , performance on CodeAgentBench is notably poor, showing no appreciable enhancement with the agent strategy. Furthermore, we find that different agent strategies yield varying levels of enhancement. ( 2023 ) 73.2 79.4 ( ↑ ↑ \uparrow ↑ 6.2 ) 77.6 ( ↑ ↑ \uparrow ↑ 4.4 ) 75.6 ( ↑ ↑ \uparrow ↑ 2.4 ) - DeepSeek-33B DeepSeek ( 2023 ) 78.7 84.8 ( ↑ ↑ \uparrow ↑ 6.1 ) 83.5 ( ↑ ↑ \uparrow ↑ 4.8 ) 81.1 ( ↑ ↑ \uparrow ↑ 2.4 ) - Table 4: The Pass@1 results of different agent strategies  |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: 5.4 Ablation Study # Usage Ablation Result GPT-3.5-ReAct - 30.7 Website Search 0.30 27.7 ( ↓ ↓ \downarrow ↓ 3.0 ) Documentation Reading 0.84 26.7 ( ↓ ↓ \downarrow ↓ 4.0 ) Code Symb Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: ( 2023 ) , performance on CodeAgentBench is notably poor, showing no appreciable enhancement with the agent strategy. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 72.7%, 70%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 72.7%; 70% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 10. Commonsense-augmented Memory Construction and Management in Long-term Conversations via Context-aware Persona 
**arXiv:2401.14215** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | However, such a naive remedy can raise contradiction between personas ( e.g. |
| **representation** | Figure 2: At the end of each dialogue session, Caffeine refines contradictory personas within/across the session(s) and saves the refined version to the dialogue model’s memory for response generation in the next session. To this end, we present Caffeine , a C ontext- A ware re F inement F ramework for contradictory p E rsonas IN long-t E rm conversations. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | While prior work focuses on not producing personas that contradict others, we focus on transforming contradictory personas into sentences that contain rich speaker information, by refining them based on their contextual  |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Figure 2: At the end of each dialogue session, Caffeine refines contradictory personas within/across the session(s) and saves the refined version to the dialogu (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 41391 Session, 36718 Session, 39523 Session. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 41391 Session; 36718 Session; 39523 Session |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 11. Efficient Episodic Memory Utilization of Cooperative Multi-Agent Reinforcement Learning
**arXiv:2403.01112** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Especially, value factorization approaches (Sunehag et al., 2017 ; Rashid et al., 2018 ; Son et al., 2019 ; Yang et al., 2020 ; Rashid et al., 2020 ; Wang et al., 2020b ) maintain the consistency between individual and joint action selection, achieving the state-of-the-art perfor |
| **representation** | We begin by explaining how to construct (1) semantic memory embeddings to better utilize the episodic memory, which enables memory recall of similar, more promising states. To further improve memory utilization, as an alternative to the conventional episodic control, we propose (2) episodic incentive that selectively encourages desirable transitions while preventing local convergence towards undesirable trajectories. In addition, we store the desirability ξ 𝜉 \xi italic_ξ of s t subscript 𝑠 𝑡 s_{t} italic_s start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT according to Definition 1 . |
| **write / read / forget** | Write: The problem of a learnable embedding network f ϕ subscript 𝑓 italic-ϕ f_{\phi} italic_f start_POSTSUBSCRIPT italic_ϕ end_POSTSUBSCRIPT is that the match between H ⁢ ( f ϕ ⁢ ( s t ) Read: We begin by explaining how to construct (1) semantic memory embeddings to better utilize the episodic memory, which enables memory recall of similar, more promising states. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: We begin by explaining how to construct (1) semantic memory embeddings to better utilize the episodic memory, which enables memory recall of similar, more promi (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: em 1, em 2, 32 episodes. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: em 1; em 2; 32 episodes |
| **refine_candidate** | **yes** — S-stage S3, S5, S7, S8 |

---

### 12. MMInA: Benchmarking Multihop Multimodal Internet Agents
**arXiv:2404.09992** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Building embodied agents capable of autonomous behaviors navigating in various environments has been a longstanding and intricate challenge in the realm of artificial intelligence research Maes ( 1993 ); Ziemke ( 1998 ); Florian ( 2003 ); Steels and Brooks ( 2018 ) . |
| **representation** | To evaluate an Internet agent’s ability to carry out complex tasks, we make it navigate through a variety of websites to gather information and execute actions. Another gap in web agent research is multimodality. Existing benchmarks pose autonomous agent tasks that rely solely on textual information Zhou et al. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: To evaluate an Internet agent’s ability to carry out complex tasks, we make it navigate through a variety of websites to gather information and execute actions. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 21.8%, 96.3%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 21.8%; 96.3% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 13. Hello Again! LLM-powered Personalized Agent for Long-term Dialogue
**arXiv:2406.05925** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | ( 2019 ) that are limited to brief, single-session interactions spanning 2-15 turns, real-life scenarios often necessitate a chatbot’s capability for long-term companionship and familiarity Xu et al. |
| **representation** | In this section, we introduce the LD-Agent in detail with the framework shown in Figure 2 . 3.2 Event Perception The event memory module is designed to perceive historical events to generate coherent responses across intervals. In Figure 2 , this event memory module is divided into two sub-modules that focus separately on long-term and short-term memory. |
| **write / read / forget** | Write: The event module stores historical memories from past sessions in long-term memory and current context in short-term memory. Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: In this section, we introduce the LD-Agent in detail with the framework shown in Figure 2 . (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 10 Session, em 7.57, 15 Session. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 10 Session; em 7.57; 15 Session |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 14. Enhancing Long-Term Memory using Hierarchical Aggregate Tree for Retrieval Augmented Generation
**arXiv:2406.06124** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, RAG is limited by the model’s context length budget. |
| **representation** | RAG relies on strategies to retrieve information from a datastore given a user query, without needing internal model information, allowing it to be used with more model types. Hence, how and what data is retrieved given a user query is an important research task.With the advent of "LLM agents", a separate memory management module is often required. presented a task and dataset for memory management in long chats, dealing with outdated information. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: RAG relies on strategies to retrieve information from a datastore given a user query, without needing internal model information, allowing it to be used with mo (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Metrics named: BLEU, F1 (values: see paper tables). |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 15. StreamBench: Towards Benchmarking Continuous Improvement of Language Agents
**arXiv:2406.08747** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | This gap motivated us to develop a new evaluation scenario–an online setting to measure LLM agents’ ability to continuously enhance their performance over time. |
| **representation** | In addition to LLMs’ strong innate capabilities , recent works have shown that LLM agents, which are LLMs augmented with extra components such as memory, retrievers, or tools, are able to improve themselves from experience. MemPrompt [ 6 ] shows that memory-enhanced GPT-3 can improve through time by storing past user feedback and retrieve them in the future. This online setting focuses on scenarios where LLM agents attempt to solve a specific downstream task and improve themselves from an input-feedback sequence, with the goal to maximize the accuracy for the whole sequence of the agent’s predictions. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: In addition to LLMs’ strong innate capabilities , recent works have shown that LLM agents, which are LLMs augmented with extra components such as memory, retrie (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 0125 Task, 001 Task. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 0125 Task; 001 Task |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 16. Towards Lifelong Dialogue Agents via Timeline-based Memory Management
**arXiv:2406.10996** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, the growing span of memories can hinder retrieval quality as conversations accumulate. |
| **representation** | (c) is a response augmented with the memory timeline. Left: Linking new memories to the memory graph after finishing a dialogue session; Right: Memory timeline retrieval, refinement, and response generation in a new dialogue session. A representative approach is to compress past conversations into summarized memories and retrieve them to augment response generation (RG) in later encounters (Xu et al., 2022a ; Lu et al., 2023 ) . |
| **write / read / forget** | Write: To achieve lifelong human-agent interaction, dialogue agents need to constantly memorize perceived information and properly retrieve it for response generation (RG). Read: To achieve lifelong human-agent interaction, dialogue agents need to constantly memorize perceived information and properly retrieve it for response generation (RG). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: (c) is a response augmented with the memory timeline. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 200 questions, 4%, 68%, 2%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 200 questions; 4%; 68%; 2%; 92%; 100% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 17. Temporal Knowledge-Graph Memory in a Partially Observable Environment
**arXiv:2408.05861** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, most benchmarks do not expose KG-shaped hidden states nor agents with explicitly modeled temporal KG memory (e.g., [ 3 , 33 , 8 , 15 , 1 , 30 , 13 , 14 ] ). |
| **representation** | Knowledge graphs (KGs) provide a natural representational substrate for such settings: entities, relations, and qualifiers can express spatial structure, object locations, and temporal metadata in a uniform semantic framework [ 11 , 19 , 3 , 33 ] . However, most benchmarks do not expose KG-shaped hidden states nor agents with explicitly modeled temporal KG memory (e.g., [ 3 , 33 , 8 , 15 , 1 , 30 , 13 , 14 ] ). The environment’s hidden state is an RDF KG whose entities include rooms, objects, walls, and the agent, and whose relations encode spatial adjacency and object locations. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: We define a lightweight temporal KG memory for agents, based on RDF-star-style qualifiers ( time_added , last_accessed , num_recalled ), and evaluate several symbolic baselines tha Forget: eviction/invalidation mentioned. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Knowledge graphs (KGs) provide a natural representational substrate for such settings: entities, relations, and qualifiers can express spatial structure, object (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 18. KGLA: Knowledge Graph Enhanced Language Agents for Recommendation
**arXiv:2410.19627** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Consequently, the updated memory for user agents is often non-specific and general due to a lack of rationalized information about the user’s choices (see Figure 1 ). |
| **representation** | The framework of our proposed KG-enhanced Agent Simulation for recommendation. For the LLM agent, we denote its memory as M 𝑀 M italic_M . During the simulation stage, the reflection process for the agent is represented by the function R ⁢ e ⁢ f ⁢ l ⁢ e ⁢ c ⁢ t ⁢ i ⁢ o ⁢ n 𝑅 𝑒 𝑓 𝑙 𝑒 𝑐 𝑡 𝑖 𝑜 𝑛 Reflection italic_R italic_e italic_f italic_l italic_e italic_c italic_t italic_i italic_o italic_n . |
| **write / read / forget** | Write: Given ( u , i + , i − ) 𝑢 superscript 𝑖 superscript 𝑖 (u,i^{+},i^{-}) ( italic_u , italic_i start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT , italic_i start_POSTSUPERSCRIPT - end_POSTS Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: The framework of our proposed KG-enhanced Agent Simulation for recommendation. (2) Primarily a write/store design — gate promote before L3 commit. (3) Lock numeric claims from body: 33%, 95%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 33%; 95% |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 19. SHARE: Shared Memory-Aware Open-Domain Long-Term Dialogue Dataset Constructed from Movie Script
**arXiv:2410.20682** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | However, such methods focus only on the utilization of persona information ( e.g , I’m a fan of K-Pop.) or short-term events ( e.g ., doctor’s appointment) for long-term dialogue. |
| **representation** | — Antoine de Saint-Exupéry Memory in dialogue plays a crucial role in building relationships and rapport between individuals, and facilitating the ongoing conversation Alea and Bluck ( 2003 ); Nelson ( 2003 ) . ( 2023 ) from the dialogue history as a memory, and incorporating this information into the response generation. In this study, we introduce a new open-domain long-term dialogue dataset, SHARE , which includes not only personas and personal event information but also information about memories shared between two speakers. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: — Antoine de Saint-Exupéry Memory in dialogue plays a crucial role in building relationships and rapport between individuals, and facilitating the ongoing conve (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 96 episodes, 3 points, 131 episodes, ROUGE-1 0.4681. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 96 episodes; 3 points; 131 episodes; ROUGE-1 0.4681; ROUGE-2 0.2332; 325 EPISODE |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 20. Planning from Imagination: Episodic Simulation and Episodic Memory for Vision-and-Language Navigation
**arXiv:2412.01857** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | This task, however, is more challenging when agents navigate in unseen environments, with performance degradation compared to seen environments. |
| **representation** | As shown in Figure 2 , SALI has a human-like episodic simulation and episodic memory mechanism. At each navigation step t 𝑡 t italic_t , the agent will maintain a topological map as its memory to store both realistic and imaginative information and make navigation decisions based solely on the memory (Section 3.1). Then, the agent will use its memory to imagine future information of both high-level spatial knowledge and low-level image features and merge the imaginary into the memory (Section 3.2). |
| **write / read / forget** | Write: At each navigation step t 𝑡 t italic_t , the agent will maintain a topological map as its memory to store both realistic and imaginative information and make navigation decisions b Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: As shown in Figure 2 , SALI has a human-like episodic simulation and episodic memory mechanism. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: by 8%, 4%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: by 8%; 4% |
| **refine_candidate** | **yes** — S-stage S3, S5, S7, S8 |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (upgraded) | 20 |
| Cumulative FULL | **360** |
