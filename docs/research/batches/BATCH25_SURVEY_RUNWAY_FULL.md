# Batch 25 — Survey Runway FULL (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-500-fb37`  
> **Scope:** Survey-bibliography runway — **20 NEW FULL** from 2512.13564 / 2309.07864 / 2602.05665 / 2603.07670 / 2605.06716 / 2404.13501 citations not previously in CORPUS §2.  
> **Progress:** FULL 480 → **500** toward 500 target.  
> **Method:** Full arXiv HTML/ar5iv or PDF→text; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards from paper abstract+body.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new; ID not previously FULL in CORPUS §2) | **20** | `2505.16421`, `2506.01952`, `2506.14728`, `2506.18019`, `2507.02592`, `2507.03616`, `2507.07998`, `2507.16784`, `2507.21055`, `2507.21407`, `2508.03680`, `2508.04700`, `2508.07010`, `2508.07407`, `2508.09874`, `2508.11567`, `2508.14704`, `2508.15253`, `2508.15305`, `2508.16629` |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped** | **0** | All IDs have `.txt` ≥8k chars. |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

---

## 1. Mechanism cards

### 1. WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning
**arXiv:2505.16421** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | While reinforcement learning (RL) has demonstrated remarkable success in enhancing large language models (LLMs), it has primarily focused on single-turn tasks such as solving math problems. |
| **representation** | While reinforcement learning (RL) has demonstrated remarkable success in enhancing large language models (LLMs), it has primarily focused on single-turn tasks such as solving math problems. Training effective web agents for multi-turn interactions remains challenging due to the complexity of long-horizon decision-making across dynamic web interfaces. In this work, we present WebAgent-R1 , a simple yet effective end-to-end multi-turn RL framework for training web agents. It learns directly from o… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 2. WebChoreArena: Evaluating Web Browsing Agents on Realistic Tedious Web Tasks
**arXiv:2506.01952** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Powered by a large language model (LLM), a web browsing agent operates web browsers in a human-like manner and offers a highly transparent path toward automating a wide range of everyday tasks. |
| **representation** | Powered by a large language model (LLM), a web browsing agent operates web browsers in a human-like manner and offers a highly transparent path toward automating a wide range of everyday tasks. As web agents become increasingly Preprint. capable and demonstrate proficiency in general browsing tasks, a critical question emerges: Can they go beyond general browsing to robustly handle tasks that are tedious and complex, or chores that humans often avoid doing themselves? In this paper, we introduce… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 3. AgentDistill: Training-Free Agent Distillation with Generalizable MCP Boxes
**arXiv:2506.14728** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | representations such as graphs or subgoal sequences, enabling student models to preserve key task structures without imitating every token. |
| **representation** | representations such as graphs or subgoal sequences, enabling student models to preserve key task structures without imitating every token. MAGDi [ 15 ] encodes multi-agent chats as interaction graphs, allowing students language model to reason over graph structure instead of raw text. Sub-goal Distillation [ 16 ] extracts high-level goals from teacher agent trajectories and trains a student agent to predict and carry out the task plan. These methods reduce sequence length while preserving key r… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 4. Graphs Meet AI Agents: Taxonomy, Progress, and Future Opportunities
**arXiv:2506.18019** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | AI agents have experienced a paradigm shift, from early dominance by reinforcement learning (RL) to the rise of agents powered by large language models (LLMs), and now further advancing towards a synergistic fusion of RL and LLM capabilities. |
| **representation** | AI agents have experienced a paradigm shift, from early dominance by reinforcement learning (RL) to the rise of agents powered by large language models (LLMs), and now further advancing towards a synergistic fusion of RL and LLM capabilities. This progression has endowed AI agents with increasingly strong abilities. Despite these advances, to accomplish complex real-world tasks, agents are required to plan and execute effectively, maintain reliable memory, and coordinate smoothly with other agen… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 5. WebSailor: Navigating Super-human Reasoning for Web Agent
**arXiv:2507.02592** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Transcending human cognitive limitations represents a critical frontier in LLM training. |
| **representation** | Transcending human cognitive limitations represents a critical frontier in LLM training. Proprietary agentic systems like DeepResearch have demonstrated su- perhuman capabilities on extremely complex information-seeking benchmarks such as BrowseComp, a feat previously unattainable. We posit that their suc- cess hinges on a sophisticated reasoning pattern absent in open-source models: the ability to systematically reduce extreme uncertainty when navigating vast information landscapes. Based on th… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 6. EvoAgentX: An Automated Framework for Evolving Agentic Workflows
**arXiv:2507.03616** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Multi-agent systems (MAS) have emerged as a powerful paradigm for orchestrating large language models (LLMs) and specialized tools to collaboratively address complex tasks. |
| **representation** | Multi-agent systems (MAS) have emerged as a powerful paradigm for orchestrating large language models (LLMs) and specialized tools to collaboratively address complex tasks. However, existing MAS frameworks often require manual workflow configuration and lack native support for dynamic evolution and performance optimization. In addition, many MAS optimization algorithms are not integrated into a unified framework. In this paper, we present EvoAgentX , an open-source platform that automates the ge… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 7. PyVision: Agentic Vision with Dynamic Tooling
**arXiv:2507.07998** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | LLMs are increasingly deployed as agents, systems capable of planning, reasoning, and dy- namically calling external tools. |
| **representation** | LLMs are increasingly deployed as agents, systems capable of planning, reasoning, and dy- namically calling external tools. However, in visual reasoning, prior approaches largely remain limited by predefined workflows and static toolsets. In this report, we present PyVision, an interactive, multi-turn framework that enables MLLMs to autonomously generate, execute, and refine Python-based tools tailored to the task at hand, unlocking flexible and interpretable problem-solving. We develop a taxono… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 8. Beyond Context Limits: Subconscious Threads for Long-Horizon Reasoning
**arXiv:2507.16784** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | To break the context limits of large language models (LLMs) that bottleneck reasoning accuracy and efficiency, we propose the Thread Inference Model (TIM. |
| **representation** | To break the context limits of large language models (LLMs) that bottleneck reasoning accuracy and efficiency, we propose the Thread Inference Model (TIM |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 9. Can Memory-Augmented LLM Agents Aid Journalism in Interpreting and Framing News for Diverse Audiences?
**arXiv:2507.21055** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Modern news is often comprehensive, weaving together information from diverse domains such as technology, finance, and agriculture. |
| **representation** | Modern news is often comprehensive, weaving together information from diverse domains such as technology, finance, and agriculture. This very comprehensiveness creates a challenge for interpretation, as audiences typically possess specialized knowledge related to their expertise, age, or standpoint. Consequently, a reader might fully understand the financial implications of a story but fail to grasp—or even actively misunderstand—its legal or technological dimensions, resulting in critical compr… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 10. Graph-Augmented Large Language Model Agents: Current Progress and Future Prospects
**arXiv:2507.21407** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Autonomous agents based on large language models (LLMs) have demonstrated impressive capabilities in a wide range of applications, including web navigation, software development, and embodied control. |
| **representation** | Autonomous agents based on large language models (LLMs) have demonstrated impressive capabilities in a wide range of applications, including web navigation, software development, and embodied control. While most LLMs are limited in several key agentic procedures, such as reliable planning, long-term memory, tool management, and multi-agent coordination, graphs can serve as a powerful auxiliary structure to enhance structure, continuity, and coordination in complex agent workflows. Given the rapi… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 11. Agent Lightning: Train ANY AI Agents with Reinforcement Learning
**arXiv:2508.03680** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | We present Agent Lightning , a flexible and extensible framework that enables Reinforcement Learning (RL)-based training of Large Language Models (LLMs) for any AI agent. |
| **representation** | We present Agent Lightning , a flexible and extensible framework that enables Reinforcement Learning (RL)-based training of Large Language Models (LLMs) for any AI agent. Unlike existing methods that tightly couple RL training with agent or rely on sequence concatenation with masking, Agent Lightning achieves complete decoupling between agent execution and training, allowing seamless integration with existing agents developed via diverse ways (e.g., using frameworks like LangChain, OpenAI Agents… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 12. SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience
**arXiv:2508.04700** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Repurposing large vision-language models (LVLMs) as computer use agents (CUAs) has led to substantial breakthroughs, primarily driven by human-labeled data. |
| **representation** | Repurposing large vision-language models (LVLMs) as computer use agents (CUAs) has led to substantial breakthroughs, primarily driven by human-labeled data. However, these models often struggle with novel and specialized software, particularly in scenarios lacking human annotations. To address this challenge, we propose SEAgent, an agentic self-evolving framework enabling CUAs to autonomously evolve through interactions with unfamiliar software. Specifically, SEAgent empowers computer-use agents… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 13. Narrative Memory in Machines: Multi-Agent Arc Extraction in Serialized TV
**arXiv:2508.07010** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Serialized television narratives present significant analytical challenges due to their complex, temporally distributed storylines that necessitate sophisticated information management. |
| **representation** | Serialized television narratives present significant analytical challenges due to their complex, temporally distributed storylines that necessitate sophisticated information management. This paper introduces a multi-agent system (MAS) designed to extract and analyze narrative arcs by implementing principles of computational memory architectures. The system conceptualizes narrative understanding through analogues of human memory: Large Language Models (LLMs) provide a form of semantic memory for … |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 14. A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems
**arXiv:2508.07407** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | yet generalisable view of most existing optimisation approaches, thereby enabling a comprehensive understanding of the field and facilitating comparative analysis across different approaches. |
| **representation** | yet generalisable view of most existing optimisation approaches, thereby enabling a comprehensive understanding of the field and facilitating comparative analysis across different approaches. 3. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 15. Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models
**arXiv:2508.09874** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Large Language Models (LLMs) have shown strong abilities in general language tasks, yet adapting them to specific domains remains a challenge. |
| **representation** | Large Language Models (LLMs) have shown strong abilities in general language tasks, yet adapting them to specific domains remains a challenge. Current method like Domain Adaptive Pretraining (DAPT) requires costly full-parameter training and suffers from catastrophic forgetting. Meanwhile, Retrieval-Augmented Generation (RAG) introduces substantial inference latency due to expensive nearest-neighbor searches and longer context. This paper introduces Memory Decoder , a plug-and-play pretrained me… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 16. AgentMental: An Interactive Multi-Agent Framework for Explainable and Adaptive Mental Health Assessment
**arXiv:2508.11567** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Mental health assessment is crucial for early intervention and effective treatment, yet traditional clinician-based approaches are limited by the shortage of qualified professionals. |
| **representation** | Mental health assessment is crucial for early intervention and effective treatment, yet traditional clinician-based approaches are limited by the shortage of qualified professionals. Recent advances in artificial intelligence have sparked growing interest in automated psychological assessment, yet most existing approaches are constrained by their reliance on static text analysis, limiting their ability to capture deeper and more informative insights that emerge through dynamic interaction and it… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 17. MCP-Universe: Benchmarking Large Language Models with Real-World Model Context Protocol Servers
**arXiv:2508.14704** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | The Model Context Protocol (MCP) has emerged as a transformative standard for connecting large language models (LLMs) to external data sources and tools, rapidly gaining adoption across major AI providers and development platforms. |
| **representation** | The Model Context Protocol (MCP) has emerged as a transformative standard for connecting large language models (LLMs) to external data sources and tools, rapidly gaining adoption across major AI providers and development platforms. However, existing benchmarks are overly simplistic and fail to capture real application challenges such as long-horizon reasoning and large, unfamiliar tool spaces. To address this critical gap, we introduce MCP-Universe , the first comprehensive benchmark specificall… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 18. Conflict-Aware Soft Prompting for Retrieval-Augmented Generation
**arXiv:2508.15253** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Retrieval-augmented generation (RAG) en- hances the capabilities of large language mod- els (LLMs) by incorporating external knowl- edge into their input prompts. |
| **representation** | Retrieval-augmented generation (RAG) en- hances the capabilities of large language mod- els (LLMs) by incorporating external knowl- edge into their input prompts. However, when the retrieved context contradicts the LLM’s parametric knowledge, it often fails to resolve the conflict between incorrect external context and correct parametric knowledge, known as context-memory conflict. To tackle this prob- lem, we introduce Conflict-Aware REtrieval- Augmented Generation (CARE), consisting of a conte… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 19. Coarse-to-Fine Grounded Memory for LLM Agent Planning
**arXiv:2508.15305** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Recent advancements in Large Language Models (LLMs) have driven growing interest in LLM-based agents for complex planning tasks. |
| **representation** | Recent advancements in Large Language Models (LLMs) have driven growing interest in LLM-based agents for complex planning tasks. To avoid costly agent training, many studies adopted memory mechanism that enhances LLM with offline experiences or online trajectory analysis. However, existing works focus on single-granularity memory derived from dynamic environmental interactions, which are inherently constrained by the quality of the collected experiences. This limitation, in turn, constrain the d… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 20. Learn to Memorize: Optimizing LLM-based Agents with Adaptive Memory Framework
**arXiv:2508.16629** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | LLM-based agents have been extensively applied across various domains, where memory stands out as one of their most essential capabilities. |
| **representation** | LLM-based agents have been extensively applied across various domains, where memory stands out as one of their most essential capabilities. Previous memory mechanisms of LLM-based agents are manually predefined by human experts, leading to higher labor costs and suboptimal performance. In addition, these methods overlook the memory cycle effect in interactive scenarios, which is critical to optimizing LLM-based agents for specific environments. To address these challenges, in this paper, we prop… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| New FULL | 20 |
| Cumulative FULL | **500** |
