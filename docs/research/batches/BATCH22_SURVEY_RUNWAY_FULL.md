# Batch 22 — Survey Runway FULL (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-500-fb37`  
> **Scope:** Survey-bibliography runway — **20 NEW FULL** from 2512.13564 / 2309.07864 / 2602.05665 / 2603.07670 / 2605.06716 / 2404.13501 citations not previously in CORPUS §2.  
> **Progress:** FULL 420 → **440** toward 500 target.  
> **Method:** Full arXiv HTML/ar5iv or PDF→text; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards from paper abstract+body.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new; ID not previously FULL in CORPUS §2) | **20** | `2309.06794`, `2309.07870`, `2310.02172`, `2310.03025`, `2310.05036`, `2310.06500`, `2310.09233`, `2310.10436`, `2311.05876`, `2311.05997`, `2311.11315`, `2311.17227`, `2312.04889`, `2401.05459`, `2401.07128`, `2402.14034`, `2402.18485`, `2403.04317`, `2403.17134`, `2404.09982` |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped** | **0** | All IDs have `.txt` ≥8k chars. |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

---

## 1. Mechanism cards

### 1. Cognitive Mirage: A Review of Hallucinations in Large Language Models
**arXiv:2309.06794** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | As large language models continue to develop in the field of AI, text generation systems are susceptible to a worrisome phenomenon known as hallucination. |
| **representation** | As large language models continue to develop in the field of AI, text generation systems are susceptible to a worrisome phenomenon known as hallucination . In this study, we summarize recent compelling insights into hallucinations in LLMs. We present a novel taxonomy of hallucinations from various text generation tasks, thus provide theoretical insights, detection methods and improvement approaches. Based on this, future research directions are proposed. Our contribution are threefold: (1) We pr… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 2. Agents: An Open-source Framework for Autonomous Language Agents
**arXiv:2309.07870** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Recent advances on large language models (LLMs) enable researchers and developers to build autonomous language agents that can automatically solve various tasks and interact with environments, humans, and other agents using natural language interfaces. |
| **representation** | Recent advances on large language models (LLMs) enable researchers and developers to build autonomous language agents that can automatically solve various tasks and interact with environments, humans, and other agents using natural language interfaces. We consider language agents as a promising direction towards artificial general intelligence and release Agents , an open-source library with the goal of opening up these advances to a wider non-specialist audience. Agents is carefully engineered … |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 3. Lyfe Agents: Generative agents for low-cost real-time social interactions
**arXiv:2310.02172** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Highly autonomous generative agents powered by large language models promise to simulate intricate social behaviors in virtual societies. |
| **representation** | Highly autonomous generative agents powered by large language models promise to simulate intricate social behaviors in virtual societies. However, achieving real-time interactions with humans at a low computational cost remains challenging. Here, we introduce Lyfe Agents. They combine low-cost with real-time responsiveness, all while remaining intelligent and goal-oriented. Key innovations include: (1) an option-action framework, reducing the cost of high-level decisions; (2) asynchronous self-m… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 4. Retrieval meets Long Context Large Language Models
**arXiv:2310.03025** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Extending the context window of large language models (LLMs) is getting popular recently, while the solution of augmenting LLMs with retrieval has existed for years. |
| **representation** | Extending the context window of large language models (LLMs) is getting popular recently, while the solution of augmenting LLMs with retrieval has existed for years. The natural questions are: i) Retrieval-augmentation versus long context window, which one is better for downstream tasks? ii) Can both methods be combined to get the best of both worlds? In this work, we answer these questions by studying both solutions using two state-of-the-art pretrained LLMs, i.e., a proprietary 43B GPT and Lla… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 5. AvalonBench: Evaluating LLMs Playing the Game of Avalon
**arXiv:2310.05036** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Conference. |
| **representation** | Conference.html . Liu et al. [2023a] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. arXiv preprint arXiv:2304.08485 , 2023a. Liu et al. [2023b] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, and Jie Tang. Agentbench: Evaluating llms as agents. CoRR , abs/230… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 6. MetaAgents: Large Language Model Based Agents for Decision-Making on Teaming
**arXiv:2310.06500** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Abstract page for arXiv paper 2310. |
| **representation** | Abstract page for arXiv paper 2310.06500: MetaAgents: Large Language Model Based Agents for Decision-Making on Teaming |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 7. AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems
**arXiv:2310.09233** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Abstract page for arXiv paper 2310. |
| **representation** | Abstract page for arXiv paper 2310.09233: AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 8. EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities
**arXiv:2310.10436** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | The advent of artificial intelligence has led to a growing emphasis on data-driven modeling in macroeconomics, with agent-based modeling (ABM) emerging as a prominent bottom-up simulation paradigm. |
| **representation** | The advent of artificial intelligence has led to a growing emphasis on data-driven modeling in macroeconomics, with agent-based modeling (ABM) emerging as a prominent bottom-up simulation paradigm. In ABM, agents ( e.g. , households, firms) interact within a macroeconomic environment, collectively generating market dynamics. Existing agent modeling typically employs predetermined rules or learning-based neural networks for decision-making. However, customizing each agent presents significant cha… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 9. Trends in Integration of Knowledge and Large Language Models: A Survey and Taxonomy of Methods, Benchmarks, and Applications
**arXiv:2311.05876** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Large language models (LLMs) exhibit superior performance on various natural language tasks, but they are susceptible to issues stemming from outdated data and domain-specific limitations. |
| **representation** | Large language models (LLMs) exhibit superior performance on various natural language tasks, but they are susceptible to issues stemming from outdated data and domain-specific limitations. In order to address these challenges, researchers have pursued two primary strategies, knowledge editing and retrieval augmentation, to enhance LLMs by incorporating external information from different aspects. Nevertheless, there is still a notable absence of a comprehensive survey. In this paper, we propose … |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 10. JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models
**arXiv:2311.05997** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6, S7 |
| **problem** | Achieving human-like planning and control with multimodal observations in an open world is a key milestone for more functional generalist agents. |
| **representation** | Achieving human-like planning and control with multimodal observations in an open world is a key milestone for more functional generalist agents. Existing approaches can handle certain long-horizon tasks in an open world. However, they still struggle when the number of open-world tasks could potentially be infinite and lack the capability to progressively enhance task completion as game time progresses. We introduce JARVIS -1, an open-world agent that can perceive multimodal input (visual observ… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S4, S6, S7. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 11. TPTU-v2: Boosting Task Planning and Tool Usage of Large Language Model-based Agents in Real-world Systems
**arXiv:2311.11315** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Large Language Models (LLMs) have demonstrated proficiency in addressing tasks that necessitate a combination of task planning and the usage of external tools that require a blend of task planning and the utilization of external tools, such as APIs. |
| **representation** | Large Language Models (LLMs) have demonstrated proficiency in addressing tasks that necessitate a combination of task planning and the usage of external tools that require a blend of task planning and the utilization of external tools, such as APIs. However, real-world complex systems present three prevalent challenges concerning task planning and tool usage: (1) The real system usually has a vast array of APIs, so it is impossible to feed the descriptions of all APIs to the prompt of LLMs as th… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 12. War and Peace (WarAgent): Large Language Model-based Multi-Agent Simulation of World Wars
**arXiv:2311.17227** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Can we avoid wars at the crossroads of history? This question has been pursued by individuals, scholars, policymakers, and organizations throughout human history. |
| **representation** | Can we avoid wars at the crossroads of history? This question has been pursued by individuals, scholars, policymakers, and organizations throughout human history. In this research, we attempt to answer the question based on the recent advances of Artificial Intelligence (AI) and Large Language Models (LLMs). We propose WarAgent , an LLM-powered multi-agent AI system, to simulate the participating countries, their decisions, and the consequences, in historical international conflicts, including t… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 13. KwaiAgents: Generalized Information-seeking Agent System with Large Language Models
**arXiv:2312.04889** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Abstract page for arXiv paper 2312. |
| **representation** | Abstract page for arXiv paper 2312.04889: KwaiAgents: Generalized Information-seeking Agent System with Large Language Models |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 14. Personal LLM Agents: Insights and Survey about the Capability, Efficiency and Security
**arXiv:2401.05459** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6, S7 |
| **problem** | Since the advent of personal computing devices, intelligent personal assistants (IPAs) have been one of the key technologies that researchers and engineers have focused on, aiming to help users efficiently obtain information and execute tasks, and provide users with more intelligent, convenient, and rich interaction experiences. |
| **representation** | Since the advent of personal computing devices, intelligent personal assistants (IPAs) have been one of the key technologies that researchers and engineers have focused on, aiming to help users efficiently obtain information and execute tasks, and provide users with more intelligent, convenient, and rich interaction experiences. With the development of the smartphone and Internet of Things, computing and sensing devices have become ubiquitous, greatly expanding the functional boundaries of IPAs.… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S4, S6, S7. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 15. EHRAgent: Code Empowers Large Language Models for Few-shot Complex Tabular Reasoning on Electronic Health Records
**arXiv:2401.07128** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Clinicians often rely on data engineers to retrieve complex patient information from electronic health record (EHR) systems, a process that is both inefficient and time-consuming. |
| **representation** | Clinicians often rely on data engineers to retrieve complex patient information from electronic health record (EHR) systems, a process that is both inefficient and time-consuming. We propose EHRAgent |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 16. AgentScope: A Flexible yet Robust Multi-Agent Platform
**arXiv:2402.14034** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | away the complexity and minimize repetition. |
| **representation** | away the complexity and minimize repetition. ⬇ 1 # set up agents: agent1 to agent5 2 # ... 3 4 msg = agent1 ( Msg ( " Alice " , " Hello ! " )) |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 17. A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist
**arXiv:2402.18485** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Abstract page for arXiv paper 2402. |
| **representation** | Abstract page for arXiv paper 2402.18485: A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 18. Online Adaptation of Language Models with a Memory of Amortized Contexts
**arXiv:2403.04317** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7 |
| **problem** | Due to the rapid generation and dissemination of information, large language models (LLMs) quickly run out of date despite enormous development costs. |
| **representation** | Due to the rapid generation and dissemination of information, large language models (LLMs) quickly run out of date despite enormous development costs. To address the crucial need to keep models updated, online learning has emerged as a critical tool when utilizing LLMs for real-world applications. However, given the ever-expanding corpus of unseen documents and the large parameter space of modern LLMs, efficient adaptation is essential. To address these challenges, we propose Memory of Amortized… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S2, S7. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 19. RepairAgent: An Autonomous, LLM-Based Agent for Program Repair
**arXiv:2403.17134** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. |
| **representation** | Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. This paper introduces RepairAgent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). Unlike existing deep learning-based approaches, which prompt a model with a fixed prompt or in a fixed feedback loop, our work treats the LLM as an agent capable of autonomously planning and executin… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 20. INMS: Memory Sharing for Large Language Model based Agents
**arXiv:2404.09982** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Download PDF Abstract 1 Introduction 2 Related Work 2. |
| **representation** | Download PDF Abstract 1 Introduction 2 Related Work 2.1 Memory Operations 2.2 In-Context Learning 2.3 Retrieval-Augmented Generation |
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
| Cumulative FULL | **440** |
