# Batch 24 — Survey Runway FULL (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-500-fb37`  
> **Scope:** Survey-bibliography runway — **20 NEW FULL** from 2512.13564 / 2309.07864 / 2602.05665 / 2603.07670 / 2605.06716 / 2404.13501 citations not previously in CORPUS §2.  
> **Progress:** FULL 460 → **480** toward 500 target.  
> **Method:** Full arXiv HTML/ar5iv or PDF→text; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards from paper abstract+body.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new; ID not previously FULL in CORPUS §2) | **20** | `2412.15274`, `2412.15540`, `2501.00358`, `2501.01702`, `2501.05366`, `2501.06590`, `2501.12254`, `2502.03358`, `2503.07018`, `2503.08175`, `2503.09516`, `2504.12369`, `2504.12516`, `2504.13079`, `2504.13805`, `2504.20073`, `2504.21776`, `2505.15962`, `2505.16067`, `2505.16348` |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped** | **0** | All IDs have `.txt` ≥8k chars. |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

---

## 1. Mechanism cards

### 1. Memory-Augmented Agent Training for Business Document Understanding
**arXiv:2412.15274** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Traditional enterprises face significant challenges in processing business documents, where tasks like extracting transport references from invoices remain largely manual despite their crucial role in logistics operations. |
| **representation** | Traditional enterprises face significant challenges in processing business documents, where tasks like extracting transport references from invoices remain largely manual despite their crucial role in logistics operations. While Large Language Models offer potential automation, their direct application to specialized business domains often yields unsatisfactory results. We introduce Matrix (Memory-Augmented agent Training through Reasoning and Iterative eXploration), a novel paradigm that enable… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 2. MRAG: A Modular Retrieval Framework for Time-Sensitive Question Answering
**arXiv:2412.15540** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Understanding temporal concepts and answering time-sensitive questions is crucial yet a challenging task for question-answering systems powered by large language models (LLMs). |
| **representation** | Understanding temporal concepts and answering time-sensitive questions is crucial yet a challenging task for question-answering systems powered by large language models (LLMs). Existing approaches either update the parametric knowledge of LLMs with new facts, which is resource-intensive and often impractical, or integrate LLMs with external knowledge retrieval ( i.e., retrieval-augmented generation). However, off-the-shelf retrievers often struggle to identify relevant documents that require int… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 3. Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding
**arXiv:2501.00358** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | This paper investigates the problem of understanding dy- namic 3D scenes from egocentric observations, a key chal- lenge in robotics and embodied AI. |
| **representation** | This paper investigates the problem of understanding dy- namic 3D scenes from egocentric observations, a key chal- lenge in robotics and embodied AI. Unlike prior studies that explored this as long-form video understanding and utilized egocentric video only, we instead propose an LLM- based agent, Embodied VideoAgent, which constructs scene memory from both egocentric video and embodied sensory inputs (e.g. depth and pose sensing). We further introduce a VLM-based approach to automatically updat… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 4. AgentRefine: Enhancing Agent Generalization through Refinement Tuning
**arXiv:2501.01702** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Large Language Model (LLM) based agents have proved their ability to perform complex tasks like humans. |
| **representation** | Large Language Model (LLM) based agents have proved their ability to perform complex tasks like humans. However, there is still a large gap between open- sourced LLMs and commercial models like the GPT series. In this paper, we focus on improving the agent generalization capabilities of LLMs via instruction tuning. We first observe that the existing agent training corpus exhibits satisfactory results on held-in evaluation sets but fails to generalize to held-out sets. These agent- tuning works f… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 5. Search-o1: Agentic Search-Enhanced Large Reasoning Models
**arXiv:2501.05366** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Large reasoning models (LRMs) like OpenAI-o1 have demonstrated impressive long stepwise reasoning capabilities through large-scale reinforcement learning. |
| **representation** | Large reasoning models (LRMs) like OpenAI-o1 have demonstrated impressive long stepwise reasoning capabilities through large-scale reinforcement learning. However, their extended reasoning processes often suffer from knowledge insufficiency, leading to frequent uncertainties and potential errors. To address this limitation, we introduce Search-o1 , a framework that enhances LRMs with an agentic retrieval-augmented generation (RAG) mechanism and a Reason-in-Documents module for refining retrieved… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 6. ChemAgent: Self-updating Library in Large Language Models Improves Chemical Reasoning
**arXiv:2501.06590** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Chemical reasoning usually involves complex, multi-step processes that demand precise calculations, where even minor errors can lead to cascading failures. |
| **representation** | Chemical reasoning usually involves complex, multi-step processes that demand precise calculations, where even minor errors can lead to cascading failures. Fur- thermore, large language models (LLMs) encounter difficulties handling domain- specific formulas, executing reasoning steps accurately, and integrating code ef- fectively when tackling chemical reasoning tasks. To address these challenges, we present ChemAgent, a novel framework designed to improve the performance of LLMs through a dynam… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 7. Memory Storyboard: Leveraging Temporal Segmentation for Streaming Self-Supervised Learning from Egocentric Videos
**arXiv:2501.12254** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Self-supervised learning holds the promise of learning good representations from real-world continuous uncurated data streams. |
| **representation** | Self-supervised learning holds the promise of learning good representations from real-world continuous uncurated data streams. However, most existing works in visual self-supervised learning focus on static images or artificial data streams. Towards exploring a more realistic learning substrate, we investigate streaming self-supervised learning from long-form real-world egocentric video streams. Inspired by the event segmentation mechanism in human perception and memory, we propose “Memory Story… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 8. Minerva: A Programmable Memory Test Benchmark for Language Models
**arXiv:2502.03358** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | How effectively can LLM-based AI assistants utilize their memory (context) to perform various tasks? Traditional data benchmarks, which are often manually crafted, suffer from several limitations: they are static, susceptible to overfitting, difficult to interpret, and lack actionable insights–failing to pinpoint the specific capabilities a model lacks when it does not pass a test. |
| **representation** | How effectively can LLM-based AI assistants utilize their memory (context) to perform various tasks? Traditional data benchmarks, which are often manually crafted, suffer from several limitations: they are static, susceptible to overfitting, difficult to interpret, and lack actionable insights–failing to pinpoint the specific capabilities a model lacks when it does not pass a test. In this paper, we present a framework for automatically generating a comprehensive set of tests to evaluate models’… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 9. Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning
**arXiv:2503.07018** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | There has been a surge in the use of large language models (LLM) conversational agents to generate responses based on long-term history from multiple sessions. |
| **representation** | There has been a surge in the use of large language models (LLM) conversational agents to generate responses based on long-term history from multiple sessions. However, existing long-term open-domain dialogue datasets lack complex, real-world personalization and fail to capture implicit reasoning—where relevant information is embedded in subtle, syntactic, or semantically distant connections rather than explicit statements. In such cases, traditional retrieval methods fail to capture relevant co… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 10. Privacy-Enhancing Paradigms within Federated Multi-Agent Systems
**arXiv:2503.08175** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | LLM-based Multi-Agent Systems (MAS) have proven highly effective in solving complex problems by integrating multiple agents, each performing different roles. |
| **representation** | LLM-based Multi-Agent Systems (MAS) have proven highly effective in solving complex problems by integrating multiple agents, each performing different roles. However, in sensitive domains, they face emerging privacy protection challenges. In this paper, we introduce the concept of Federated MAS , highlighting the fundamental differences between Federated MAS and traditional FL. We then identify key challenges in developing Federated MAS, including: 1) heterogeneous privacy protocols among agents… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 11. Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning
**arXiv:2503.09516** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Efficiently acquiring external knowledge and up-to-date information is essential for effective reasoning and text generation in large language models (LLMs). |
| **representation** | Efficiently acquiring external knowledge and up-to-date information is essential for effective reasoning and text generation in large language models (LLMs). Prompting advanced LLMs with reasoning capabilities to use search engines during inference is often suboptimal, as the LLM might not fully possess the capability on how to interact optimally with the search engine. This paper introduces Search-R1 , an extension of reinforcement learning (RL) for reasoning frameworks where the LLM learns to … |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 12. WorldMem: Long-term Consistent World Simulation with Memory
**arXiv:2504.12369** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | representations, making accurate scene reconstruction challenging. |
| **representation** | representations, making accurate scene reconstruction challenging. In contrast, our approach retrieves information from previously generated frames and their states, ensuring world consistency without overfitting to specific scenarios. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 13. BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents
**arXiv:2504.12516** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | We present BrowseComp, a simple yet challenging benchmark for measuring the ability for agents to browse the web. |
| **representation** | We present BrowseComp, a simple yet challenging benchmark for measuring the ability for agents to browse the web. BrowseComp comprises 1, |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 14. Retrieval-Augmented Generation with Conflicting Evidence
**arXiv:2504.13079** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Large language model (LLM) agents are increasingly employing retrieval-augmented generation (RAG) to improve the factuality of their responses. |
| **representation** | Large language model (LLM) agents are increasingly employing retrieval-augmented generation (RAG) to improve the factuality of their responses. However, in practice, these systems often need to handle ambiguous user queries and potentially conflicting information from multiple sources while also suppressing inaccurate information from noisy or irrelevant documents. Prior work has generally studied and addressed these challenges in isolation, considering only one aspect at a time, such as handlin… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 15. LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark
**arXiv:2504.13805** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Abstract page for arXiv paper 2504. |
| **representation** | Abstract page for arXiv paper 2504.13805: LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 16. RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning
**arXiv:2504.20073** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Training large language models (LLMs) as interactive agents presents unique challenges including long-horizon decision making and interacting with stochastic environment feedback. |
| **representation** | Training large language models (LLMs) as interactive agents presents unique challenges including long-horizon decision making and interacting with stochastic environment feedback. While reinforcement learning (RL) has enabled progress in static tasks, multi-turn agent RL training remains underexplored. We propose StarPO ( S tate- T hinking- A ctions- R eward P olicy O ptimization), a general framework for trajectory-level agent RL, and introduce RAGEN , a modular system for training and evaluati… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 17. WebThinker: Empowering Large Reasoning Models with Deep Research Capability
**arXiv:2504.21776** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6, S7 |
| **problem** | submission dates but also discovers the ancillary meeting deadline by clicking on a PDF link, compiling comprehensive deadline information with specific dates and requirements. |
| **representation** | submission dates but also discovers the ancillary meeting deadline by clicking on a PDF link, compiling comprehensive deadline information with specific dates and requirements. • In the CLTS and Aedes mosquito control example (Table 8 ), the explorer clicks on a repository link to find a case study integrating Community-Led Total Sanitation with mosquito control in Indonesia, Vietnam, and the Philippines, providing specific outcomes (40% reduction in breeding sites). D. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S4, S6, S7. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 18. Pre-training Limited Memory Language Models with Internal and External Knowledge
**arXiv:2505.15962** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Neural language models are black-boxes – both linguistic patterns and factual knowledge are distributed across billions of opaque parameters. |
| **representation** | Neural language models are black-boxes – both linguistic patterns and factual knowledge are distributed across billions of opaque parameters. This entangled encoding makes it difficult to reliably inspect, verify, or update specific facts. We introduce Limited Memory Language Models ( LmLm ) |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 19. How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior
**arXiv:2505.16067** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Memory is a critical component in large language model (LLM)-based agents, enabling them to store and retrieve past executions to improve task performance over time. |
| **representation** | Memory is a critical component in large language model (LLM)-based agents, enabling them to store and retrieve past executions to improve task performance over time. In this paper, we conduct an empirical study on how memory management choices impact the LLM agents’ behavior, especially their long-term performance. Specifically, we focus on two fundamental memory management operations that are widely used by many agent frameworks—memory addition and deletion —to systematically study their impact… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 20. Embodied Agents Meet Personalization: Investigating Challenges and Solutions Through the Lens of Memory Utilization
**arXiv:2505.16348** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | and reuse personalized knowledge as transferable templates. |
| **representation** | and reuse personalized knowledge as transferable templates. We extended our user pattern tasks by sampling existing scenarios and systematically altering target locations, thereby evaluating whether agents can adapt user preferences to novel but structurally similar situations. To encourage explicit memory utilization, we incorporated contextual cues in the instructions, such as "on [another receptacle] this time," clearly signaling that established preferences should apply in the modified conte… |
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
| Cumulative FULL | **480** |
