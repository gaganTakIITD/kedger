# Batch 22 — Survey Runway FULL (Kedger) — **deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Honest re-card of survey-runway papers — mechanism extraction from **full body** (Intro/Method/Results), not abstract paste.  
> **Progress:** FULL 420 → **440** toward 500.  
> **Method:** Cached `/tmp/kedger-papers/full/{id}.txt`; cards built by `scripts/research/deep_recard_500.py`.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers only from body matches. Generic lessons forbidden.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body mechanism deep-read; ID already ledgered Batch22 — **re-card upgrade**) | **20** | `2309.06794`, `2309.07870`, `2310.02172`, `2310.03025`, `2310.05036`, `2310.06500`, `2310.09233`, `2310.10436`, `2311.05876`, `2311.05997`, `2311.11315`, `2311.17227`, `2312.04889`, `2401.05459`, `2401.07128`, `2402.14034`, `2402.18485`, `2403.04317`, `2403.17134`, `2404.09982` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs have `.txt` ≥15k chars. |
| **Method span extracted** | **10/20** | continuous-text section split |
| **Numeric evidence extracted** | **13/20** | regex over method/results |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. [2309.06794] Cognitive Mirage: A Review of Hallucinations in Large Language Models Cognitive Mirage: A Review 
**arXiv:2309.06794** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | While the privacy and timeliness of data in the real world (Lazaridou et al., 2022 ; Shi et al., 2023b ) unfortunately exacerbate this problem, leaving models difficult to maintain a comprehensive and up-to-date understanding of the facts. |
| **representation** | Architecture Resources Hallucination Types Research Method Raunak et al. ( 2023 ) Question and Answer Only-Dec MEDMCQA, Headqa, USMILE, Medqa, Pubmed Reasoning hallucination, Memory-based hallucination Medical benchmark Med-HALT Dziri et al. ( 2023 ) Knowledge graph generation Only-Dec TekGen, WebNLG Subject hallucination, relation hallucination, object hallucination Ontology driven KGC benchmark Text2KGBench Li et al. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Architecture Resources Hallucination Types Research Method Raunak et al. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | ( 2023 ) Summarization System Enc-Dec, Only-Dec CNN/DM, XSum Factually inconsistent summaries Generate summaries from given models Cao et al. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Architecture Resources Hallucination Types Research Method Raunak et al. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 2. Agents: An Open-source Framework for Autonomous Language Agents
**arXiv:2309.07870** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | “An autonomous agent is a system situated within and a part of an environment that senses the environment and acts on it, over time, in pursuit of its own agenda and so as to effect what it senses in the future.” Is it an Agent, or just a Program?: A Taxonomy for Autonomous Agent |
| **representation** | In addition, most (if not all) existing language agent frameworks solely depend on a short task description and rely completely on the abilities of LLMs to plan and act. To this end, we release Agents , an open-source library and framework for language agents dedicated to supporting LLM-powered language agents. Therefore, the ability to maintain long-short term memory is very important for autonomous agents. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: Recent advances on large language models (LLMs) enable researchers and developers to build autonomous language agents that can automatically solve various tasks and interact with e Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: In addition, most (if not all) existing language agent frameworks solely depend on a short task description and rely completely on the abilities of LLMs to plan (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S3, S5, S7, S8 |

---

### 3. Lyfe Agents: Generative agents for low-cost real-time social interactions
**arXiv:2310.02172** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, a salient difference remains: while all animals, including humans, are autonomous, characterized by self-driven, adaptive, continuous interactions with the environments, standalone LLMs fall short of these capabilities. |
| **representation** | Architecture In this section, we present a high-level overview of the modular architecture underlying Lyfe Agents’ brains (Fig. In general, natural-language inputs are processed by a sensory module, the output of which is added to the agent’s internal states. The internal states are a collection of agent-specific states that are continuously updated both by external inputs and through internal recurrent processing. |
| **write / read / forget** | Write: The internal states are a collection of agent-specific states that are continuously updated both by external inputs and through internal recurrent processing. Read: Internal states The internal states are a collection of text-based states, including the current goal, related memory retrieved from a Memory module, summary of recent events, work Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Architecture In this section, we present a high-level overview of the modular architecture underlying Lyfe Agents’ brains (Fig. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 4. Retrieval meets Long Context Large Language Models
**arXiv:2310.03025** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | The long context large language models (LLM) have recently received a lot of attention in production (e.g., Anthropic, 2023 ; OpenAI, 2023b ) , research community (e.g., Chen et al., 2023 ; Liu et al., 2023 ; Tworkowski et al., 2023 ) , and open source community (e.g., Kaiokendev |
| **representation** | The long context large language models (LLM) have recently received a lot of attention in production (e.g., Anthropic, 2023 ; OpenAI, 2023b ) , research community (e.g., Chen et al., 2023 ; Liu et al., 2023 ; Tworkowski et al., 2023 ) , and open source community (e.g., Kaiokendev Conceptually, the retrieval-augmented decoder-only LLM can be viewed as applying the sparse attention over its long context window, where the sparsity pattern is not predefined as Child et al. In other words, unretrieved context is treated as irrelevant and has zero-valued attention weights. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Extending the context window of large language models (LLMs) is getting popular recently, while the solution of augmenting LLMs with retrieval has existed for years. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: The long context large language models (LLM) have recently received a lot of attention in production (e.g., Anthropic, 2023 ; OpenAI, 2023b ) , research communi (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Metrics named: accuracy (values: see paper tables). |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 5. [2310.05036] AvalonBench: Evaluating LLMs Playing the Game of Avalon AvalonBench : Evaluating LLMs Playing the
**arXiv:2310.05036** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | Intelligent Agents V, Agent Theories, Architectures, and Languages, 5th International Workshop, ATAL ’98, Paris, France, July 4-7, 1998, Proceedings , volume 1555 of Lecture Notes in Computer Science , 1999. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Intelligent Agents V, Agent Theories, Architectures, and Languages, 5th International Workshop, ATAL ’98, Paris, France, July 4-7, 1998, Proceedings , volume 15 (2) Eval/analysis paper — extract fixtures/SLIs rather than store ops. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 6. MetaAgents: Large Language Model Based Agents for Decision-making on Teaming MetaAgents
**arXiv:2310.06500** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, these multi-agent systems are largely bound to human-prescribed team compositions and workflows. |
| **representation** | Large language models (LLMs), such as ChatGPT [ 38 ] and GPT-4 [ 39 ] , have gained significant attention due to their exceptional abilities in natural language processing. A noteworthy development in this domain is LLM-based agent [ 57 ] , which employ LLMs to carry out human-like actions, ranging from planning and conversational interaction [ 42 ] to task solving [ 44 ; 24 ] . An area yet to be fully explored is LLM-based agents’ social intelligence—specifically, organizing teams and aligning agent expertise with relevant roles in the team. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Large language models (LLMs), such as ChatGPT [ 38 ] and GPT-4 [ 39 ] , have gained significant attention due to their exceptional abilities in natural language (2) Primarily a write/store design — gate promote before L3 commit. (3) Lock numeric claims from body: 64%, 48%, 12%, 44%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 64%; 48%; 12%; 44%; 56%; 22% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 7. [2310.09233] AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems AgentCF: 
**arXiv:2310.09233** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | However, in addition to dialogue, real-world human behaviors also involve non-verbal aspects like user-item interactions in recommender systems, which implicitly reflect user preferences and have the potential to facilitate personalized user modeling. |
| **representation** | In this section, we present the proposed agent-based collaborative filtering approach, named AgentCF . The overall framework of our proposed AgentCF is depicted in Figure 1 . The overall framework of AgentCF and a case about the optimization process of agents: (1) The user and item agents are first prompted to autonomously interact. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: In this section, we present the proposed agent-based collaborative filtering approach, named AgentCF . (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 95%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 95% |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 8. EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities
**arXiv:2310.10436** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | However, customizing decision-making mechanisms for each agent presents substantial difficulties. |
| **representation** | Early empirical statistical models, such as the Phelps Model Phelps ( 1967 ) , and the work of Kydland and Prescott Kydland and Prescott ( 1982 ) , focused on data-driven analysis and policy outcome prediction but struggled to handle significant shocks. In the last two decades, agent-based modeling (ABM) has emerged as a promising paradigm for simulating macroeconomics from the bottom up, allowing diverse agents to interact without assuming a predetermined equilibrium Farmer and Foley ( 2009 ) . Early models Tesfatsion and Judd ( 2006 ); Brock and Hommes ( 1998 ) relied on predetermined rules but made oversimplified assumptions about agent behaviors. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Early empirical statistical models, such as the Phelps Model Phelps ( 1967 ) , and the work of Kydland and Prescott Kydland and Prescott ( 1982 ) , focused on d (2) Eval/analysis paper — extract fixtures/SLIs rather than store ops. (3) Lock numeric claims from body: 3.00%, 46%, 5%, 20%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 3.00%; 46%; 5%; 20%; 2%; 12% |
| **refine_candidate** | **no** |

---

### 9. Trends in Integration of Knowledge and Large Language Models: A Survey and Taxonomy of Methods, Benchmarks, an
**arXiv:2311.05876** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, they still suffer from serious challenges in knowledge-intensive tasks Petroni et al. |
| **representation** | Large language models (LLMs) have demonstrated an impressive ability to encode real-world knowledge in their parameters and a remarkable capacity for solving various natural language processing tasks Brown et al. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: In order to address these challenges, researchers have pursued two primary strategies, knowledge editing and retrieval augmentation, to enhance LLMs by incorporating external infor Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Large language models (LLMs) have demonstrated an impressive ability to encode real-world knowledge in their parameters and a remarkable capacity for solving va (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 10. JARVIS-1: Open-world Multi-task Agents with Memory-Augmented Multimodal Language Models
**arXiv:2311.05997** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | This calls out the need for agents to propose their own tasks and self-improve. |
| **representation** | Architecture of JARVIS -1 and its self-improving mechanism . (a) JARVIS -1 comprises a memory-augmented multimodal language model (MLM) that produces plans and a low-level action controller. JARVIS -1 also utilizes a multimodal memory to store and obtain experiences as references for planning. |
| **write / read / forget** | Write: JARVIS -1 also utilizes a multimodal memory to store and obtain experiences as references for planning. Read: Upon receiving a task and the current observation, JARVIS -1 first utilizes the MLM to generate a multimodal query ( query gen ) that retrieves relevant planning experiences from t Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Architecture of JARVIS -1 and its self-improving mechanism . (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 2.5%, 8.99%, 2.42%, 6%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 2.5%; 8.99%; 2.42%; 6%; 200 tasks; up to 12.5% |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 11. [2311.11315] TPTU-v2: Boosting Task Planning and Tool Usage of Large Language Model-based Agents in Real-world
**arXiv:2311.11315** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, leveraging LLMs for complex tasks presents formidable challenges. |
| **representation** | In response to the typical challenges of deploying LLMs within intricate real-world systems, we propose a comprehensive framework that fundamentally bolsters the capabilities of LLMs in Task Planning and Tool Usage (TPTU). This section first introduces our proposed framework, which systemically integrates three specialized components: an API Retriever, an LLM Finetuner, and a Demo Selector. Subsequently, we delve into a comprehensive description of each component, elucidating their unique contributions to the overall framework. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: This section first introduces our proposed framework, which systemically integrates three specialized components: an API Retriever, an LLM Finetuner, and a Demo Selector. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: In response to the typical challenges of deploying LLMs within intricate real-world systems, we propose a comprehensive framework that fundamentally bolsters th (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 45 APIs, 100 questions, 000 questions, 84.64%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 45 APIs; 100 questions; 000 questions; 84.64%; Recall@10; 98.47% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 12. [2311.17227] War and Peace (WarAgent): LLM-based Multi-Agent Simulation of World Wars War and Peace (WarAgent)
**arXiv:2311.17227** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Traditional methods of studying conflict through historical analysis, while insightful, are inherently limited by their static nature and the bias of hindsight. |
| **representation** | Architecture This section provides a comprehensive introduction to the architecture of the WarAgent Multi-Agent System (MAS), detailing its core components and the information flow among agents. The section then shifts to explore the mechanisms of information exchange within the MAS, particularly focusing on (1) Agent-Secretary interaction and (2) Agent-Agent interaction. 4.1 Building Blocks 4.1.1 Country Agents Each country agent is defined by its corresponding country profile. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | We propose WarAgent , an LLM-powered multi-agent AI system, to simulate the participating countries, their decisions, and the consequences, in historical international conflicts, including the World War I (WWI), the Worl |
| **privacy** | WarAgent is built upon four foundational building blocks: (1) Country agents, (2) Secretary agents, (3) Board, (4) Stick. |
| **Kedger lessons** | (1) Mechanism to port: Architecture This section provides a comprehensive introduction to the architecture of the WarAgent Multi-Agent System (MAS), detailing its core components and  (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 100%, 85.7%, 75%, 90%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 100%; 85.7%; 75%; 90%; 14.8%; 4.9% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 13. [2312.04889] KwaiAgents: Generalized Information-seeking Agent System with Large Language Models KwaiAgents: G
**arXiv:2312.04889** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | However, Research in cognitive science reveals that humans, on average, forget approximately 50% of newly acquired information within an hour, a phenomenon termed the forgetting curve (Ebbinghaus, 1885 ) . |
| **representation** | For instance, while many can effortlessly recall that Mount Everest is “the highest mountain in the world”, the identity of “the fifth highest mountain” often eludes memory. Closed-source LLMs, like ChatGPT and GPT-4, have demonstrated their utility in various agent systems. , 2023a , b ) have shown their potential in specific agent systems when fine-tuned with targeted instructional prompts (Patil et al . |
| **write / read / forget** | Write: Despite not having the capacity to process and memorize vast amounts of information in their brains, humans excel in critical thinking, planning, reflection, and harnessing availab Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: For instance, while many can effortlessly recall that Mount Everest is “the highest mountain in the world”, the identity of “the fifth highest mountain” often e (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 63.04%, 50%, 57.21%, 68.66%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 63.04%; 50%; 57.21%; 68.66%; 79.60%; 83.58% |
| **refine_candidate** | **no** |

---

### 14. Personal LLM Agents: Insights and Survey about the Capability, Efficiency and Security
**arXiv:2401.05459** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | 2 A Brief History of Intelligent Personal Assistants 2.1 Timeline View of the Intelligent Personal Assistants History 2.2 Technical View of the Intelligent Personal Assistants History 2.2.1 Template-based Programming 2.2.2 Supervised Learning Methods 2.2.3 Reinforcement Learning  |
| **representation** | Architecture: Running LLMs on resource-limited mobile devices needs to balance the performance and quality of task completion. 2) Practical Local-Remote Collaborative Architecture: Local-remote collaborative architecture of LLM is considered promising, which is desired to inherit both the fast/low-cost response ability of local model and the high-quality generation ability of the cloud model. Memorization (§ 4.3 ) is to record the user data, enabling the agent to recall past events, summarize knowledge and self-evolve. |
| **write / read / forget** | Write: This may involve updates at the operating system level and the development of application programming interfaces (APIs) for better integration and utilization of LLM’s functionalit Read: Memorization (§ 4.3 ) is to record the user data, enabling the agent to recall past events, summarize knowledge and self-evolve. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | 1) Data Security and Privacy Protection: Ensuring the security of personal data and the protection of user privacy is critical when using personal data to train and execute LLMs. |
| **Kedger lessons** | (1) Mechanism to port: Architecture: Running LLMs on resource-limited mobile devices needs to balance the performance and quality of task completion. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 1%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 1% |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 15. EHRAgent: Code Empowers Large Language Models for Few-shot Complex Tabular Reasoning on Electronic Health Reco
**arXiv:2401.07128** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6, S7 |
| **problem** | It eliminates the need for specialized expertise or extra effort from data engineers, which is typically required when dealing with EHRs in existing clinical settings ( left ). |
| **representation** | Clinicians specify tasks in natural language, and the LLM agent autonomously generates and executes code to interact with EHRs ( right ) for answers. In clinical research and practice, clinicians actively interact with EHR systems to access and retrieve patient data, ranging from detailed individual-level records to comprehensive population-level insights (Cowie et al., 2017 ) . Alternatively, an autonomous agent could facilitate clinicians to communicate with EHRs in natural languages, translating clinical questions into machine-interpretable queries, planning a sequence of actions, and ultimately delivering the final responses. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: Clinicians often rely on data engineers to retrieve complex patient information from electronic health record (EHR) systems, a process that is both inefficient and time-consuming. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | We first inject relevant medical information to enable EHRAgent to effectively reason about the given query, identifying and extracting the required rec |
| **Kedger lessons** | (1) Mechanism to port: Clinicians specify tasks in natural language, and the LLM agent autonomously generates and executes code to interact with EHRs ( right ) for answers. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: up to 29.6%, 40%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: up to 29.6%; 40% |
| **refine_candidate** | **yes** — S-stage S4, S6, S7 |

---

### 16. AgentScope: A Flexible yet Robust Multi-Agent Platform
**arXiv:2402.14034** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Multi-agent systems, as upgraded extensions of single-agent systems, require collaborative efforts from multiple agents working in concert (Wang et al., 2023 ; Xi et al., 2023 ) . |
| **representation** | 2.2 Architecture of AgentScope We present AgentScope as an infrastructural platform to facilitate the creation, management, and deployment of multi-agent applications integrated with LLMs. The architecture of AgentScope comprises three hierarchical layers and a set of user interaction interfaces, as shown in Fig. These layers provide support for multi-agent applications from different levels, including elementary and advanced functionalities of a single agent (utility layer), resources and runtime management (manager and wrapper layer), and agent-level to workflow-level programming interf |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: 2.2 Architecture of AgentScope We present AgentScope as an infrastructural platform to facilitate the creation, management, and deployment of multi-agent applic (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 17. A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist
**arXiv:2402.18485** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Rule-based trading systems are rigid and struggle to adapt to market volatility, often resulting in underperformance in evolving markets. |
| **representation** | Market Intelligence Tool Use Inference & Extension News Reports Price Visual Data Info Tools Preference Training Scheme Planning Explainability Generalization Rule-based ✗ ✗ ✓ ✗ ✗ ✗ ✗ Hyper-parameter Tuning Myopic - Single trading task RL method ✗ ✗ ✓ ✗ ✗ ✗ ✗ Model training Sequential ✗ Single trading task FinGPT ✓ ✗ ✓ ✗ ✗ ✗ ✗ LLM Fine-tuning Myopic ✓ Limited trading tasks FinMem ✓ ✓ ✓ ✗ ✗ ✗ ✓ Reflection Myopic ✓ Multiple trading tasks FinAgent ✓ ✓ ✓ ✓ ✓ ✓ ✓ Reflection Sequential ✓ Multiple trad |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S2, S3, S7, S8. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 10%, 19%, 84%, 118%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 10%; 19%; 84%; 118%; 40%; 42% |
| **refine_candidate** | **no** |

---

### 18. Online Adaptation of Language Models with a Memory of Amortized Contexts
**arXiv:2403.04317** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7 |
| **problem** | However, LMs are typically static artifacts, and as the world changes, the knowledge encoded in their parameters becomes outdated. |
| **representation** | During online adaptation, we store the amortized contexts into a memory bank ℳ ℳ {\mathcal{M}} caligraphic_M , then adapt the LM via aggregating the memory bank based on the given question. However, even large models often fail to update their learned knowledge when the retrieved document consists of counterfactual information [ 48 , 44 , 75 ] and it may not be suited for edge computing as a large number of documents poses expensive computation for model inference [ This system extracts knowledge from incoming documents, builds a memory bank, and learns to automatically select relevant information from this memory bank, which is subsequently passed as additional input to the target model. |
| **write / read / forget** | Write: To address the crucial need to keep models updated, online learning has emerged as a critical tool when utilizing LLMs for real-world applications. Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: During online adaptation, we store the amortized contexts into a memory bank ℳ ℳ {\mathcal{M}} caligraphic_M , then adapt the LM via aggregating the memory bank (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: F1 4, 23.90%, 26.25%, 68.0%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: F1 4; 23.90%; 26.25%; 68.0%; 90.31%; by 96.2% |
| **refine_candidate** | **yes** — S-stage S1, S2, S7 |

---

### 19. RepairAgent: An Autonomous, LLM-Based Agent for Program Repair I Introduction II Background on LLM-Based, Auto
**arXiv:2403.17134** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | This paper introduces RepairAgent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). |
| **representation** | Chaudhuri, “An in-context learning agent for formal theorem-proving,” 2024. Press, “Swe-agent: Agent-computer interfaces enable automated software engineering,” 2024. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Chaudhuri, “An in-context learning agent for formal theorem-proving,” 2024. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 99%, 25%, 81%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 99%; 25%; 81% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 20. INMS: Memory Sharing for Large Language Model based Agents Report GitHub Issue × Title: Content selection save
**arXiv:2404.09982** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | To bridge this gap, we propose the IN teractive M emory S haring (INMS) framework, an asynchronous interaction paradigm for multi-agent systems. |
| **representation** | To bridge this gap, we propose the IN teractive M emory S haring (INMS) framework, an asynchronous interaction paradigm for multi-agent systems. By integrating real-time memory filtering, storage, and retrieval, INMS establishes a shared conversational memory pool. This enables continuous, dialogue-like memory sharing among agents, promoting collective self-enhancement and dynamically refining the retrieval mediator based on interaction history. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: By integrating real-time memory filtering, storage, and retrieval, INMS establishes a shared conversational memory pool. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: To bridge this gap, we propose the IN teractive M emory S haring (INMS) framework, an asynchronous interaction paradigm for multi-agent systems. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 20%, 40%, 25%, 50%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 20%; 40%; 25%; 50%; 75%; 100% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (upgraded) | 20 |
| Cumulative FULL | **440** |
