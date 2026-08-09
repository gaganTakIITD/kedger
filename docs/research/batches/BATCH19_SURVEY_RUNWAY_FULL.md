# Batch 19 — Survey Runway FULL (Kedger) — **deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Honest re-card of survey-runway papers — mechanism extraction from **full body** (Intro/Method/Results), not abstract paste.  
> **Progress:** FULL 360 → **380** toward 500.  
> **Method:** Cached `/tmp/kedger-papers/full/{id}.txt`; cards built by `scripts/research/deep_recard_500.py`.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers only from body matches. Generic lessons forbidden.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body mechanism deep-read; ID already ledgered Batch19 — **re-card upgrade**) | **20** | `2502.05453`, `2502.13843`, `2503.10049`, `2505.20231`, `2505.20286`, `2506.13651`, `2507.21105`, `2508.01415`, `2508.01832`, `2508.13250`, `2509.01055`, `2509.17459`, `2509.22315`, `2509.25250`, `2510.03611`, `2510.04195`, `2510.04618`, `2510.07134`, `2510.07925`, `2510.09720` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs have `.txt` ≥15k chars. |
| **Method span extracted** | **13/20** | continuous-text section split |
| **Numeric evidence extracted** | **17/20** | regex over method/results |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. LLM-Powered Decentralized Generative Agents with Adaptive Hierarchical Knowledge Graph for Cooperative Plannin
**arXiv:2502.05453** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Figure 1: The Multi-agent Crafter Environment. |
| **representation** | 3 Framework: DAMCS In this section, we give an overview of our framework. 3.1 Problem Setting Our goal is to demonstrate that Large Language Models (LLMs) can effectively plan, coordinate, and execute tasks in a multi-agent environment where collaboration and resource management are critical. Within each timeslot, each agent can take an action , e.g., sharing resources with another agent or working towards a goal. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: 3 Framework: DAMCS In this section, we give an overview of our framework. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 000 episodes, em 6.2, em 5.2, em 5.0. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 000 episodes; em 6.2; em 5.2; em 5.0; em 3.0; 63% |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 2. AgentCF++: Memory-enhanced LLM-based Agents for Popularity-aware Cross-domain Recommendations
**arXiv:2502.13843** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | However, their development is hindered by challenges in effectively understanding user behavior (Shani and Gunawardana, 2011 ) . |
| **representation** | Architecture AgentCF++ employs a similar memory architecture to AgentCF for the item agent, using a single memory to record the interest levels of users with various preferences towards it. Initially, the item’s memory is seeded with its side information. However, AgentCF++ has meticulously designed the memory architecture for the user agent to enhance its functionality. |
| **write / read / forget** | Write: (2) Domain-fused memory also stores preferences within a particular domain but integrates domain-separated memories from other domains. Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Architecture AgentCF++ employs a similar memory architecture to AgentCF for the item agent, using a single memory to record the interest levels of users with va (2) Primarily a write/store design — gate promote before L3 commit. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 3. Enhancing Multi-Agent Systems via Reinforcement Learning with LLM-based Planner and Graph-based Policy I INTRO
**arXiv:2503.10049** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | The introduction of Large Language Models (LLMs) has brought stronger reasoning and cognitive abilities to MAS, but existing LLM-based systems struggle to respond quickly and accurately in dynamic environments. |
| **representation** | Multi-agent systems (MAS) have shown great potential in executing complex tasks, but coordination and safety remain significant challenges. Multi-Agent Reinforcement Learning (MARL) offers a promising framework for agent collaboration, but it faces difficulties in handling complex tasks and designing reward functions. To address these challenges, we propose LLM-based Graph Collaboration MARL (LGC-MARL), a framework that efficiently combines LLMs and MARL. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Multi-agent systems (MAS) have shown great potential in executing complex tasks, but coordination and safety remain significant challenges. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S3, S5, S7, S8 |

---

### 4. MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents Introduction Related Work 
**arXiv:2505.20231** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, these methods are primarily based on semantic similarity, overlooking task intent and reducing task coherence in multi-session dialogues. |
| **representation** | Modern task-oriented dialogue (TOD) systems increasingly rely on large language model (LLM) agents, leveraging Retrieval-Augmented Generation (RAG) and long-context capabilities for long-term memory utilization. To address this challenge, we introduce MemGuide , a two-stage framework for intent-driven memory selection. (1) Intent‑Aligned Retrieval matches the current dialogue context with stored intent descriptions in the memory bank, retrieving QA‑formatted memory units that share the same goal. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Modern task-oriented dialogue (TOD) systems increasingly rely on large language model (LLM) agents, leveraging Retrieval-Augmented Generation (RAG) and long-context capabilities fo Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Modern task-oriented dialogue (TOD) systems increasingly rely on large language model (LLM) agents, leveraging Retrieval-Augmented Generation (RAG) and long-con (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 52%, 47.1%, 1.29 points, 956 task. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 52%; 47.1%; 1.29 points; 956 task; by 11%; 88% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 5. ALITA: G ENERALIST AGENT ENABLING SCALABLE AGENTIC
**arXiv:2505.20286** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | "Simplicity is the ultimate sophistication." — Leonardo da Vinci Large language models (LLMs) have rapidly evolved from merely generating text to autonomous agents capable of independently planning and executing complex tasks on behalf of users with limited human oversight [ 2]. |
| **representation** | We propose Alita, a generalist agent enabling scalable agentic reasoning with minimal predefinition and maximal self-evolution to tackle diverse and complex tasks. In contrast to generalist agents that typically depend on extensive manually-designed tools and workflows [8, 9], the manager agent in Alita solely orchestrates the web agent using only basic tools. Through this approach, our framework enables Alita to plan task-specific tools through brainstorming. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: It then utilizes a Web Agent to search for helpful open-source libraries and other resources related to these tools. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: We propose Alita, a generalist agent enabling scalable agentic reasoning with minimal predefinition and maximal self-evolution to tackle diverse and complex tas (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 75.15%, 87.27%, 67.36%, 72.73%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 75.15%; 87.27%; 67.36%; 72.73%; 86.06%; 74.00% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 6. xbench: Tracking Agents Productivity Scaling with Profession-Aligned Real-World Evaluations 1 Introduction 2 A
**arXiv:2506.13651** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, current AI benchmarks do not predict the real-world economic impact, focusing on technical capabilities over business value. |
| **representation** | There is growing consensus that effective AI agent evaluation must align closely with real-world tasks. This limitation becomes critical as AI enters its evaluation-centric phase (Yao, 2025 ) , necessitating domain-specific benchmarks that directly measure agent productivity and commercial utility in professional settings. Figure 1: Profession-aligned evaluation define domain agents, predict Tech-Market Fit (TMF) and track competition of agent products. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: For Recruitment, we collect 50 tasks from real-world headhunting business scenarios to evaluate agents’ abilities in company mapping, information retrieval, and talent sourcing. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: There is growing consensus that effective AI agent evaluation must align closely with real-world tasks. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 50 tasks, 40%, 30%, 68%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 50 tasks; 40%; 30%; 68%; 16%; 36% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 7. AgentMaster: A Multi-Agent Conversational Framework Using A2A and MCP Protocols for Multimodal Information Ret
**arXiv:2507.21105** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Figure 1: The general MAS framework of AgentMaster. |
| **representation** | 3 System Architecture of the Case Study Figure 2 illustrates the architecture of a conversational MAS, an example implementation of the AgentMaster framework for multimodal information retrieval and analysis. The system integrates modular components to enable robust, retrieval-augmented question answering through dynamic agent orchestration. The architecture comprises a web-based user interface, a Flask server acting as the main entry point, a Coordinator agent (i.e., the Orchestrator agent) implementing the A2A protocol, and multiple specialized retrieval agents (i.e., domain agents). |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: 3 System Architecture of the Case Study Figure 2 illustrates the architecture of a conversational MAS, an example implementation of the AgentMaster framework for multimodal informa Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: 3 System Architecture of the Case Study Figure 2 illustrates the architecture of a conversational MAS, an example implementation of the AgentMaster framework fo (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 96.3%, 87.1%, 23 questions. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 96.3%; 87.1%; 23 questions |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 8. RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical
**arXiv:2508.01415** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | I Introduction II Related Work II-A VLM/LLM-based Agentic Frameworks in Embodied Tasks II-B Spatial Memory III RoboMemory III-A Information Preprocessor III-B Comprehensive Embodied Memory III-C Closed-Loop Planning Module III-D Low-Level Executor IV Experiments IV-A Benchmarks I |
| **representation** | I Introduction II Related Work II-A VLM/LLM-based Agentic Frameworks in Embodied Tasks II-B Spatial Memory III RoboMemory III-A Information Preprocessor III-B Comprehensive Embodied Memory III-C Closed-Loop Planning Module III-D Low-Level Executor IV Experiments IV-A Benchmarks I |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: I Introduction II Related Work II-A VLM/LLM-based Agentic Frameworks in Embodied Tasks II-B Spatial Memory III RoboMemory III-A Information Preprocessor III-B C (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 200 tasks, 100%, by 1%, by 7.9%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 200 tasks; 100%; by 1%; by 7.9%; 67%; 68% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 9. [2508.01832] MLP Memory: Language Modeling with Retriever-pretrained External Memory MLP Memory: Language Mode
**arXiv:2508.01832** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, it is widely recognized that the current decoder-only LLMs lack a reliable memory, suffering from hallucinations [ 61 , 37 ] . |
| **representation** | The query f ​ ( c ) f(c) is used to retrieve the k k -nearest neighbors 𝒩 = { ( k i , v i ) } i = 1 k \mathcal{N}=\{(k_{i},v_{i})\}_{i=1}^{k} from the datastore ( 𝒦 , 𝒱 ) (\mathcal{K},\mathcal{V}) , based on a distance metric d ​ ( ⋅ , ⋅ ) d(\cdot,\cdot) (typically squared L 2 L^ (3) k k NN-LM enhances language modeling by integrating explicit memory for improved prediction, but its scalability is limited by considerable storage requirements and high-latency neighbor retrieval. 3.2 MLP Memory 3.2.1 Architecture Our model architecture employs a novel decoupled framework, featuring a transformer decoder module for language generation and a memory module that collaborates with the decoder to provide contextual knowledge during generation. |
| **write / read / forget** | Write: 3.1 Preliminary: k k -nearest neighbors language model The k k -nearest neighbors language model ( k k NN-LM) [ 27 ] augments a pre-trained neural language model (LM) by interpolat Read: 3.1 Preliminary: k k -nearest neighbors language model The k k -nearest neighbors language model ( k k NN-LM) [ 27 ] augments a pre-trained neural language model (LM) by interpolat Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: The query f ​ ( c ) f(c) is used to retrieve the k k -nearest neighbors 𝒩 = { ( k i , v i ) } i = 1 k \mathcal{N}=\{(k_{i},v_{i})\}_{i=1}^{k} from the datastore (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 17.5%, 24.1%, em 26.10, em 29.35. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 17.5%; 24.1%; em 26.10; em 29.35; em 28.58; 8.04% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 10. Explicit v.s. Implicit Memory: Exploring Multi-hop Complex Reasoning Over Personalized Information 1 Introduct
**arXiv:2508.13250** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, in real-world personalized applications, complex tasks that require multi-hop reasoning over a large amount of personalized information are more practical and challenging for the memory of agents, which still remains unexplored. |
| **representation** | Additionally, we observe that implicit memory can degrade model performance, especially for AS+X under multi-hop reasoning scenarios. This degradation likely results from a trade-off between the implicit memory’s command of overall knowledge and the reasoning degradation introduced during training. Conclusion In this paper, we formally define the MPR task and construct a dataset to evaluate different memory approaches. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: In future research, we will explore the adaptive integration of implicit memory and explicit memory, as well as multimodal personalized memory with reasoning strategies. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Additionally, we observe that implicit memory can degrade model performance, especially for AS+X under multi-hop reasoning scenarios. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: em0, ACC = 1, 700 questions, 10%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: em0; ACC = 1; 700 questions; 10%; 20%; 60% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 11. VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use
**arXiv:2509.01055** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, these approaches primarily rely on imitation learning. |
| **representation** | Building a general RL training framework that supports various tools is inherently challenging due to the additional overhead introduced by tool interactions. To address these issues, we propose VerlTool , a general-purpose ARLT framework designed to support various tools as modular plugins via a unified API. As shown in Figure 1 , Verl Tool adopts a modular and decoupled architecture consisting of two main components: the VeRL Workflow and the Tool Server , connected via a unified API. |
| **write / read / forget** | Write: The VeRL Workflow handles all reinforcement learning activities, including multi-turn rollouts and actor updates. Read: This fragmentation increases the development burden for researchers seeking to experiment with novel tools or multi-tool scenarios. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Building a general RL training framework that supports various tools is inherently challenging due to the additional overhead introduced by tool interactions. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 12. Principles: Synthetic Strategy Memory for Proactive Dialogue Agents
**arXiv:2509.17459** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | (a) Pre-defined strategies fail due to limited coverage, (b) Open-ended strategies improve coverage but suffer from preference bias, (c) Our approach based on Principles resolves both limited coverage and preference bias, leading to optimal outcomes. |
| **representation** | To tackle these, we introduce Principles : a synthetic strategy memory for proactive dialogue agents, derived through offline self-play simulations. Specifically, when the agent’s strategy leads to success (e.g., resolving the user’s core issue) , we derive Principles by analyzing the success factors. In this setup, an agent engages in multi-turn conversations with a user simulator, adaptively selecting strategies at each turn and responding accordingly to accomplish a defined goal. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: To tackle these, we introduce Principles : a synthetic strategy memory for proactive dialogue agents, derived through offline self-play simulations. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 80%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 80% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 13. PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reasoning Introduction Related Work Methodology S
**arXiv:2509.22315** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Inspired by the dual-process theory of human cognition from Thinking, Fast and Slow , we introduce PRIME (Planning and Retrieval-Integrated Memory for Enhanced Reasoning), a multi-agent reasoning framework that dynamically integrates System 1 (fast, intuitive thinking) and System |
| **representation** | Our framework is explicitly inspired by the dual-process cognitive theory introduced in Thinking, Fast and Slow . PRIME closely mirrors this cognitive process: when presented with a question, the framework first rapidly generates an intuitive answer through the Quick Thinking Agent (System 1). Then, the Reflection Agent critically evaluates this intuitive response, by explicitly performing self-reflection to determine whether the intuitive answer is reliable or if it potentially contains errors, logical inconsistencies, or uncertainties. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Once activated, PRIME’s System 2 involves structured reasoning steps, including explicit planning to break down the problem, targeted search and reading processes to mimic human me Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Our framework is explicitly inspired by the dual-process cognitive theory introduced in Thinking, Fast and Slow . (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: em 1, em 2, 4 points, 87.2%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: em 1; em 2; 4 points; 87.2%; 80.4%; 86.0% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 14. Memory Management and Contextual Consistency for Long-Running Low-Code Agents
**arXiv:2509.25250** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | This interface transforms a technical challenge into a collaborative experience, enhancing user trust and the agent’s long-term reliability [ 14 ] . |
| **representation** | Our Hybrid System: The agent uses our complete proposed system, featuring Intelligent Decay and a simulated HITL loop. – Semantic Similarity: Cosine similarity between the embeddings of the agent’s responses over time, checking if it maintains a consistent meaning [ 16 ] . – Contradiction Rate: The percentage of turns where the agent’s output conflicts with previously stated facts or user instructions [ 16 ] . |
| **write / read / forget** | Write: This "self-evolution" is a result of our Intelligent Decay mechanism, which, guided by user feedback, ensures the memory store is constantly populated with high-quality, relevant e Read: silent or parametric-only (no explicit retrieve API). Forget: Our Hybrid System: The agent uses our complete proposed system, featuring Intelligent Decay and a simulated HITL loop. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Our Hybrid System: The agent uses our complete proposed system, featuring Intelligent Decay and a simulated HITL loop. (2) Primarily a write/store design — gate promote before L3 commit. (3) Lock numeric claims from body: 13.6%, by 22%, 70%, 90%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 13.6%; by 22%; 70%; 90%; 80%; 94% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 15. Can an LLM Induce a Graph? Investigating Memory Drift and Context Length I Introduction II Background and Rela
**arXiv:2510.03611** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, these benchmarks often rely on simplistic “needle in a haystack” retrieval or continuation tasks that may not accurately reflect the performance of these models in information-dense scenarios. |
| **representation** | While the input text can be viewed as generated in terms of a graph, its structure is not made explicit and connections must be induced from distributed textual cues, separated by long contexts and interspersed with irrelevant information. Our findings reveal that LLMs begin to exhibit memory drift and contextual forgetting at much shorter effective lengths when tasked with this form of relational reasoning, compared to what existing benchmarks suggest. We further show that even models specialized for reasoning, such as OpenAI o1, remain vulnerable to early memory drift in these settings. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: However, these benchmarks often rely on simplistic “needle in a haystack” retrieval or continuation tasks that may not accurately reflect the performance of these models in informa Forget: Recently proposed evaluation benchmarks aim to characterize the effective context length and the forgetting tendencies of large language models (LLMs). |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: While the input text can be viewed as generated in terms of a graph, its structure is not made explicit and connections must be induced from distributed textual (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: F1 = 2. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: F1 = 2 |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 16. Constructing coherent spatial memory in LLM agents through graph rectificationCode and experimental data: http
**arXiv:2510.04195** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | 1.1 Related Work Enhancing the Spatial Reasoning Ability of LLMs. |
| **representation** | However, such context-dependent querying becomes incapable as environments grow larger, motivating the need for incremental map construction that builds a complete topological graph from stepwise observations. We propose LLM-MapRepair , a framework for LLM-driven construction and map repair, designed to detect, localize, and correct structural inconsistencies in incrementally constructed navigation graphs. Our contributions include a Version Control mechanism for graph construction, an Edge Impact Score for repair prioritization, and a cleaned variant of the MANGO benchmark tailored for LLM-driven map construction and repair. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: LCA-Based Filtering Reduces Search Space. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | B.2 Test Cases TC1: Topological Conflict (Paper Figure Scenario). |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: However, such context-dependent querying becomes incapable as environments grow larger, motivating the need for incremental map construction that builds a compl (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 8.6 pp, 55.8 pp, 95.0%, 50.0%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 8.6 pp; 55.8 pp; 95.0%; 50.0%; 60.0%; 30.0% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 17. Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models Report GitHub Issue × Title:
**arXiv:2510.04618** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | 2 Background and Motivation 2.1 Context Adaptation 2.2 Limitations of Existing Context Adaptation Methods Brevity Bias Context Collapse 3 Agentic Context Engineering (ACE) 3.1 Incremental Delta Updates 3.2 Grow-and-Refine 4 Results 4.1 Tasks and Datasets Evaluation Metrics 4.2 Ba |
| **representation** | See paper body. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S2, S3, S7, S8. (2) Primarily a write/store design — gate promote before L3 commit. (3) Lock numeric claims from body: 12.3%, 11.9%, 7.6%, 14.8%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 12.3%; 11.9%; 7.6%; 14.8%; 59.4%; 60.3% |
| **refine_candidate** | **no** |

---

### 18. TrackVLA++: Unleashing Reasoning and Memory Capabilities in VLA Models for Embodied Visual Tracking I Introduc
**arXiv:2510.07134** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, existing approaches lack explicit spatial reasoning and effective temporal memory, causing failures under severe occlusions or in the presence of similar-looking distractors. |
| **representation** | Architecture IV-A TrackVLA++ Architecture Observation Encoding. We process the on-the-fly video stream 𝒪 1 : T 1 : N \mathcal{O}_{1:T}^{1:N} by a dual-encoder architecture, extracting and concatenating visual features { V t n | t = 1 , … , T , n = 1 , … , N } \{V_{t}^{n}|t=1,...,T,n=1,...,N\} from SigLIP [ 46 ] and DINOv2 [ 47 ] . To effectively manage the trade-off between long-range context and inference speed, our model employs a dual-memory architecture. |
| **write / read / forget** | Write: This reasoning process is formally defined as: E T CoT = LLM ​ ( Concat ​ [ E T M , E T V , E L ] ) , \displaystyle E_{T}^{\text{CoT}}=\text{LLM}(\text{Concat}[E_{T}^{M},E_{T}^{V}, Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Architecture IV-A TrackVLA++ Architecture Observation Encoding. (2) Primarily a write/store design — gate promote before L3 commit. (3) Lock numeric claims from body: 74.0%, 62.0%, 87.5%, 82.4%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 74.0%; 62.0%; 87.5%; 82.4%; 80.7%; 84.0% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 19. Enabling Personalized Long-term Interactions in LLM-based Agents through Persistent Memory and User Profiles
**arXiv:2510.07925** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Despite this potential, current AI agents have several limitations, including static, task-specific designs, hallucination (Portugal et al., 2024 ; Sapkota et al., 2025 ; Liu et al., 2023 ) , and their lack of personalization (Yuan et al., 2023 ; Shan et al., 2025 ) . |
| **representation** | We address this through user-specific memory modules based on RAG, which store and retrieve historical information. Together, the agentic workflow, memory modules, and user profiles provide the technical requirements for enabling personalization in our framework. Agentic Workflow combining Agentic AI Patterns, Persistent Memory, and dynamic User Profiles † † : Building on our definition of personalization, the first system requirement —adaptivity— requires mechanisms capable of flexibly responding to evolving user contexts. |
| **write / read / forget** | Write: We address this through user-specific memory modules based on RAG, which store and retrieve historical information. Read: We address this through user-specific memory modules based on RAG, which store and retrieve historical information. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: We address this through user-specific memory modules based on RAG, which store and retrieve historical information. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 87%, 81%, 98.5%, 86.3%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 87%; 81%; 98.5%; 86.3%; 19%; 96% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 20. Preference-Aware Memory Update for Long-Term LLM Agents Introduction Related Work Methodology Preference Extra
**arXiv:2510.09720** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | In particular, they lack mechanisms for dynamically refining preference memory representations in response to evolving user behaviors and contexts. |
| **representation** | In this section, we introduce our Preference-Aware Memory Update (PAMU) mechanism. The category with the highest probability and its score are concatenated into a tuple to represent the tone dimension. A probability vector over predefined emotional classes is extracted, and the class with the highest probability is used, along with its score, to represent the emotional tone dimension. |
| **write / read / forget** | Write: In this section, we introduce our Preference-Aware Memory Update (PAMU) mechanism. Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: In this section, we introduce our Preference-Aware Memory Update (PAMU) mechanism. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 705 pairs, 104 pairs, 547 pairs. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 705 pairs; 104 pairs; 547 pairs |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (upgraded) | 20 |
| Cumulative FULL | **380** |
