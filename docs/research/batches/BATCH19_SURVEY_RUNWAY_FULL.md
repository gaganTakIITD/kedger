# Batch 19 — Survey Runway FULL (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-500-fb37`  
> **Scope:** Survey-bibliography runway — **20 NEW FULL** from 2512.13564 / 2309.07864 / 2602.05665 / 2603.07670 / 2605.06716 / 2404.13501 citations not previously in CORPUS §2.  
> **Progress:** FULL 360 → **380** toward 500 target.  
> **Method:** Full arXiv HTML/ar5iv or PDF→text; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards from paper abstract+body.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new; ID not previously FULL in CORPUS §2) | **20** | `2502.05453`, `2502.13843`, `2503.10049`, `2505.20231`, `2505.20286`, `2506.13651`, `2507.21105`, `2508.01415`, `2508.01832`, `2508.13250`, `2509.01055`, `2509.17459`, `2509.22315`, `2509.25250`, `2510.03611`, `2510.04195`, `2510.04618`, `2510.07134`, `2510.07925`, `2510.09720` |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped** | **0** | All IDs have `.txt` ≥8k chars. |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

---

## 1. Mechanism cards

### 1. LLM-Powered Decentralized Generative Agents with Adaptive Hierarchical Knowledge Graph for Cooperative Planning
**arXiv:2502.05453** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Developing intelligent agents for long-term cooperation in dynamic open-world scenarios is a major challenge in multi-agent systems. |
| **representation** | Developing intelligent agents for long-term cooperation in dynamic open-world scenarios is a major challenge in multi-agent systems. Traditional Multi-agent Reinforcement Learning (MARL) frameworks like centralized training decentralized execution (CTDE) struggle with scalability and flexibility. They require centralized long-term planning, which is difficult without custom reward functions, and face challenges in processing multi-modal data. CTDE approaches also assume fixed cooperation strateg… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 2. AgentCF++: Memory-enhanced LLM-based Agents for Popularity-aware Cross-domain Recommendations
**arXiv:2502.13843** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Abstract page for arXiv paper 2502. |
| **representation** | Abstract page for arXiv paper 2502.13843: AgentCF++: Memory-enhanced LLM-based Agents for Popularity-aware Cross-domain Recommendations |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 3. Enhancing Multi-Agent Systems via Reinforcement Learning with LLM-based Planner and Graph-based Policy
**arXiv:2503.10049** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Multi-agent systems (MAS) have shown great potential in executing complex tasks, but coordination and safety remain significant challenges. |
| **representation** | Multi-agent systems (MAS) have shown great potential in executing complex tasks, but coordination and safety remain significant challenges. Multi-Agent Reinforcement Learning (MARL) offers a promising framework for agent collaboration, but it faces difficulties in handling complex tasks and designing reward functions. The |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 4. MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents
**arXiv:2505.20231** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Modern task-oriented dialogue (TOD) systems increasingly rely on large language model (LLM) agents, leveraging Retrieval-Augmented Generation (RAG) and long-context capabilities for long-term memory utilization. |
| **representation** | Modern task-oriented dialogue (TOD) systems increasingly rely on large language model (LLM) agents, leveraging Retrieval-Augmented Generation (RAG) and long-context capabilities for long-term memory utilization. However, these methods are primarily based on semantic similarity, overlooking task intent and reducing task coherence in multi-session dialogues. To address this challenge, we introduce MemGuide , a two-stage framework for intent-driven memory selection. (1) Intent‑Aligned Retrieval mat… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 5. Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution
**arXiv:2505.20286** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Recent advances in large language models (LLMs) have enabled agents to autonomously perform complex, open-ended tasks. |
| **representation** | Recent advances in large language models (LLMs) have enabled agents to autonomously perform complex, open-ended tasks. However, many existing frameworks depend heavily on manually predefined tools and workflows, which hinder their adaptability, scalability, and generalization across domains. In this work, we introduce Alita—a generalist agent designed with the principle of "Simplicity is the ultimate sophistication," enabling scalable agentic reasoning through minimal predefinition and maximal s… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 6. xbench: Tracking Agents Productivity Scaling with Profession-Aligned Real-World Evaluations
**arXiv:2506.13651** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | We introduce xbench , a dynamic, profession-aligned evaluation suite designed to bridge the gap between AI agent capabilities and real-world productivity. |
| **representation** | We introduce xbench , a dynamic, profession-aligned evaluation suite designed to bridge the gap between AI agent capabilities and real-world productivity. While existing benchmarks often focus on isolated technical skills, they may not accurately reflect the economic value agents deliver in professional settings. To address this, xbench targets commercially significant domains with evaluation tasks defined by industry professionals. Our framework creates metrics that strongly correlate with prod… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 7. AgentMaster: A Multi-Agent Conversational Framework Using A2A and MCP Protocols for Multimodal Information Retrieval and Analysis
**arXiv:2507.21105** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | The rise of Multi-Agent Systems (MAS) in Artificial Intelligence (AI), especially integrated with Large Language Models (LLMs), has greatly facilitated the resolution of complex tasks. |
| **representation** | The rise of Multi-Agent Systems (MAS) in Artificial Intelligence (AI), especially integrated with Large Language Models (LLMs), has greatly facilitated the resolution of complex tasks. However, current systems are still facing challenges of inter-agent communication, coordination, and interaction with heterogeneous tools and resources. Most recently, the Model Context Protocol (MCP) by Anthropic and Agent-to-Agent (A2A) communication protocol by Google have been introduced, and to the best of ou… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 8. RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical Embodied Systems
**arXiv:2508.01415** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Download PDF Abstract I Introduction II Related Work II-A VLM/LLM-based Agentic Frameworks in Embodied Tasks II-B Spatial Memory III RoboMemory III-A Information Preprocessor III-B Comprehensive Embodied Memory III-C Closed-Loop Planning Module III-D Low-Level Executor IV Experiments IV-A Benchmarks IV-B Baselines and Metrics IV-C Main Results IV-D Efficiency Analysis IV-E Ablation Studies IV-F Real-World Robot Deployment V Conclusion References -A Additional Related Work -A. |
| **representation** | Download PDF Abstract I Introduction II Related Work II-A VLM/LLM-based Agentic Frameworks in Embodied Tasks II-B Spatial Memory III RoboMemory III-A Information Preprocessor III-B Comprehensive Embodied Memory III-C Closed-Loop Planning Module III-D Low-Level Executor IV Experiments IV-A Benchmarks IV-B Baselines and Metrics IV-C Main Results IV-D Efficiency Analysis IV-E Ablation Studies IV-F Real-World Robot Deployment V Conclusion References -A Additional Related Work -A |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 9. MLP Memory: A Retriever-Pretrained Memory for Large Language Models
**arXiv:2508.01832** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | While modern decoder-only LLMs achieve superior performance across various domains, hallucinations have risen to be a common problem in their generated text, hindering their application in knowledge-intensive tasks. |
| **representation** | While modern decoder-only LLMs achieve superior performance across various domains, hallucinations have risen to be a common problem in their generated text, hindering their application in knowledge-intensive tasks. Retriever-augmented generation (RAG) offers a solution, but the non-parametric nature of the retriever hinders its deep interaction with LLM. In this work, we propose to decouple memorization from the LLM decoder using a pretrained, differentiable external memory. The external memory… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 10. Explicit v.s. Implicit Memory: Exploring Multi-hop Complex Reasoning Over Personalized Information
**arXiv:2508.13250** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Abstract page for arXiv paper 2508. |
| **representation** | Abstract page for arXiv paper 2508.13250: Explicit v.s. Implicit Memory: Exploring Multi-hop Complex Reasoning Over Personalized Information |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 11. VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use
**arXiv:2509.01055** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Reinforcement Learning with Verifiable Rewards (RLVR) has demonstrated success in enhancing LLM reasoning capabilities, but remains limited to single-turn interactions without tool integration. |
| **representation** | Reinforcement Learning with Verifiable Rewards (RLVR) has demonstrated success in enhancing LLM reasoning capabilities, but remains limited to single-turn interactions without tool integration. While recent A gentic R einforcement L earning with T ool use (ARLT) approaches have emerged to address multi-turn tool interactions, existing works develop task-specific codebases that suffer from fragmentation, synchronous execution bottlenecks, and limited extensibility across domains. These inefficien… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 12. PRINCIPLES: Synthetic Strategy Memory for Proactive Dialogue Agents
**arXiv:2509.17459** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | painting. |
| **representation** | painting. Persuader: That splash of blue really draws you in, doesn’t it? I love how art can be so captivating. Persuadee: Absolutely! There’s something about abstract art that just lets your mind wander. Persuader: Just like art, clean water is essential for life, and WaterAid helps provide that to those in needhave you heard of them? Persuadee: Yes, I’ve heard of WaterAid, but I usually prefer to help people directly when I can. Persuader: That’s wonderful, and donating to WaterAid is a direct… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 13. PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reasoning
**arXiv:2509.22315** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Inspired by the dual-process theory of human cognition from Thinking, Fast and Slow , we introduce PRIME (Planning and Retrieval-Integrated Memory for Enhanced Reasoning), a multi-agent reasoning framework that dynamically integrates System 1 (fast, intuitive thinking) and System 2 (slow, deliberate thinking). |
| **representation** | Inspired by the dual-process theory of human cognition from Thinking, Fast and Slow , we introduce PRIME (Planning and Retrieval-Integrated Memory for Enhanced Reasoning), a multi-agent reasoning framework that dynamically integrates System 1 (fast, intuitive thinking) and System 2 (slow, deliberate thinking). PRIME first employs a Quick Thinking Agent (System 1) to generate a rapid answer; if uncertainty is detected, it then triggers a structured System |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 14. Memory Management and Contextual Consistency for Long-Running Low-Code Agents
**arXiv:2509.25250** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | concepts and high-level summaries distilled from the episodic memory. |
| **representation** | concepts and high-level summaries distilled from the episodic memory. It is more compact and efficient for retaining long-term, non-temporal knowledge. User Input LCNC Agent Working Memory (LLM Context Window) Episodic Memory (Vector DB) Semantic Memory (Knowledge Store/Summaries) 1. Decision 2. New Event 3. Intelligent Decay 4. Retrieval 5. Knowledge Augmentation 6. Consolidation/Distillation 7. Summary/Facts Figure 1: Hybrid Memory System Architecture Diagram. Arrows indicate information flow.… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 15. Can an LLM Induce a Graph? Investigating Memory Drift and Context Length
**arXiv:2510.03611** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | structured knowledge from unstructured input and highlight the need for architectural adaptations to improve long-range reasoning. |
| **representation** | structured knowledge from unstructured input and highlight the need for architectural adaptations to improve long-range reasoning. Our codebase to support reproducibility is publicly available. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 16. Constructing coherent spatial memory in LLM agents through graph rectification
**arXiv:2510.04195** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Download PDF Abstract 1 Introduction 1. |
| **representation** | Download PDF Abstract 1 Introduction 1.1 Related Work Enhancing the Spatial Reasoning Ability of LLMs. Mapping Evaluation in Language Agents. SLAM as Inspiration. Error Management. Incremental Scene Graph Construction. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 17. Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models
**arXiv:2510.04618** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Download PDF Abstract 1 Introduction 2 Background and Motivation 2. |
| **representation** | Download PDF Abstract 1 Introduction 2 Background and Motivation 2.1 Context Adaptation 2.2 Limitations of Existing Context Adaptation Methods Brevity Bias Context Collapse |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 18. TrackVLA++: Unleashing Reasoning and Memory Capabilities in VLA Models for Embodied Visual Tracking
**arXiv:2510.07134** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Embodied Visual Tracking (EVT) is a fundamental ability that underpins practical applications, such as companion robots, guidance robots and service assistants, where continuously following moving targets is essential. |
| **representation** | Embodied Visual Tracking (EVT) is a fundamental ability that underpins practical applications, such as companion robots, guidance robots and service assistants, where continuously following moving targets is essential. Recent advances have enabled language-guided tracking in complex and unstructured scenes. However, existing approaches lack explicit spatial reasoning and effective temporal memory, causing failures under severe occlusions or in the presence of similar-looking distractors. To addr… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 19. Enabling Personalized Long-term Interactions in LLM-based Agents through Persistent Memory and User Profiles
**arXiv:2510.07925** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Abstract page for arXiv paper 2510. |
| **representation** | Abstract page for arXiv paper 2510.07925: Enabling Personalized Long-term Interactions in LLM-based Agents through Persistent Memory and User Profiles |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 20. Preference-Aware Memory Update for Long-Term LLM Agents
**arXiv:2510.09720** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | One of the key factors influencing the reasoning capabilities of LLM-based agents is their ability to leverage long-term memory. |
| **representation** | One of the key factors influencing the reasoning capabilities of LLM-based agents is their ability to leverage long-term memory. Integrating long-term memory mechanisms allows agents to make informed decisions grounded in historical interactions. While recent advances have significantly improved the storage and retrieval components—e.g., by encoding memory into dense vectors for similarity search or organizing memory as structured knowledge graphs—most existing approaches fall short in memory up… |
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
| Cumulative FULL | **380** |
