# Batch 17 — Survey Runway FULL (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-500-fb37`  
> **Scope:** Survey-bibliography runway — **20 NEW FULL** from 2512.13564 / 2309.07864 / 2602.05665 / 2603.07670 / 2605.06716 / 2404.13501 citations not previously in CORPUS §2.  
> **Progress:** FULL 320 → **340** toward 500 target.  
> **Method:** Full arXiv HTML/ar5iv or PDF→text; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards from paper abstract+body.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new; ID not previously FULL in CORPUS §2) | **20** | `2508.10419`, `2508.12379`, `2508.15294`, `2509.21212`, `2509.23040`, `2510.01353`, `2510.13614`, `2510.19897`, `2510.21618`, `2511.10030`, `2511.20857`, `2512.12856`, `2512.20092`, `2512.20237`, `2512.20745`, `2601.04726`, `2601.07468`, `2602.07624`, `2302.04023`, `2305.14938` |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped** | **0** | All IDs have `.txt` ≥8k chars. |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

---

## 1. Mechanism cards

### 1. ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning
**arXiv:2508.10419** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Narrative comprehension on long stories and novels has been a challenging domain attributed to their intricate plotlines and entangled, often evolving relations among characters and entities. |
| **representation** | Narrative comprehension on long stories and novels has been a challenging domain attributed to their intricate plotlines and entangled, often evolving relations among characters and entities. Given the LLM’s diminished reasoning over extended context and its high computational cost, retrieval-based approaches remain a pivotal role in practice. However, traditional RAG methods could fall short due to their stateless, single-step retrieval process, which often overlooks the dynamic nature of captu… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 2. GraphCogent: Mitigating LLMs' Working Memory Constraints via Multi-Agent Collaboration in Complex Graph Understanding
**arXiv:2508.12379** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Abstract page for arXiv paper 2508. |
| **representation** | Abstract page for arXiv paper 2508.12379: GraphCogent: Mitigating LLMs' Working Memory Constraints via Multi-Agent Collaboration in Complex Graph Understanding |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S3, S5, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 3. A Multi-Memory Segment System for Generating High-Quality Long-Term Memory Content in Agents
**arXiv:2508.15294** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | An agent powered by large language models have achieved impressive results, but effectively handling the vast amounts of historical data generated during interactions remains a challenge. |
| **representation** | An agent powered by large language models have achieved impressive results, but effectively handling the vast amounts of historical data generated during interactions remains a challenge. The current approach is to design a memory module for the agent to process these data. However, existing methods, such as MemoryBank and A-MEM, have poor quality of stored memory content, which affects recall performance and response quality. In order to better construct high-quality long-term memory content, w… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 4. SGMem: Sentence Graph Memory for Long-Term Conversational Agents
**arXiv:2509.21212** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Long-term conversational agents require effective memory management to handle dialogue histories that exceed the context window of large language models (LLMs). |
| **representation** | Long-term conversational agents require effective memory management to handle dialogue histories that exceed the context window of large language models (LLMs). Existing methods based on fact extraction or summarization reduce redundancy but struggle to organize and retrieve relevant information across different granularities of dialogue and generated memory. We introduce SGMem (Sentence Graph Memory), which represents dialogue as sentence-level graphs within chunked units, capturing association… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 5. Look Back to Reason Forward: Revisitable Memory for Long-Context LLM Agents
**arXiv:2509.23040** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Download PDF Abstract 1 Introduction 2 Method 2. |
| **representation** | Download PDF Abstract 1 Introduction 2 Method 2.1 Preliminaries: MDP Memory Agent for Long-Context QA 2.2 Memory Agent with History-Augmented State 2. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 6. MEMTRACK: Evaluating Long-Term Memory and State Tracking in Multi-Platform Dynamic Agent Environments
**arXiv:2510.01353** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Recent works on context and memory benchmarking have primarily focused on conversational instances but the need for evaluating memory in dynamic enterprise environments is crucial for its effective application. |
| **representation** | Recent works on context and memory benchmarking have primarily focused on conversational instances but the need for evaluating memory in dynamic enterprise environments is crucial for its effective application. We introduce Memtrack , a benchmark designed to evaluate long-term memory and state tracking in multi-platform agent environments. Memtrack models realistic organizational workflows by integrating asynchronous events across multiple communication and productivity platforms such as Slack, … |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 7. MemoTime: Memory-Augmented Temporal Knowledge Graph Enhanced Large Language Model Reasoning
**arXiv:2510.13614** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | reasoning induction. |
| **representation** | reasoning induction . In ACL , Cited by: Appendix D , §1 , §1 , §1 , Table 1 , Table 1 , Table 1 . Z. Chen, J. Liao, and X. Zhao (2023a) Multi-granularity temporal question answering over knowledge graphs . In ACL , pp. 11378–11392 . Cited by: Appendix D , Table 1 . Z. Chen, J. Liao, and X. Zhao (2023b) Multi-granularity temporal question answering over knowledge graphs . In ACL , pp. 11378–11392 . Cited by: Appendix D . J. Devlin, M. Chang, et al. (2019) Bert: pre-training of deep bidirectional… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 8. Learning from Supervision with Semantic and Episodic Memory: A Reflective Approach to Agent Adaptation
**arXiv:2510.19897** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Download PDF Abstract. |
| **representation** | Download PDF Abstract. 1 Introduction 2 Learning from Supervised Signals 2.1 What to Remember? 3 Incorporating Critiques into Memory 3. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 9. DeepAgent: A General Reasoning Agent with Scalable Toolsets
**arXiv:2510.21618** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Abstract page for arXiv paper 2510. |
| **representation** | Abstract page for arXiv paper 2510.21618: DeepAgent: A General Reasoning Agent with Scalable Toolsets |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 10. Multi-agent In-context Coordination via Decentralized Memory Retrieval
**arXiv:2511.10030** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Download PDF Abstract 1 Introduction 2 Related Work 3 Background 3. |
| **representation** | Download PDF Abstract 1 Introduction 2 Related Work 3 Background 3.1 Multi-Agent Reinforcement Learning 3.2 Decision Transformer 3. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 11. Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory
**arXiv:2511.20857** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Download PDF Abstract 1 Introduction 2 Related Work 2. |
| **representation** | Download PDF Abstract 1 Introduction 2 Related Work 2.1 Test-time Learning 2.2 Self-evolving Memory 3 Evo-Memory: Evaluating Self-Evolving Memory in LLM Agents 3. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 12. Forgetful but Faithful: A Cognitive Memory Architecture and Benchmark for Privacy-Aware Generative Agents
**arXiv:2512.12856** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Download PDF Abstract 1 Introduction 2 Related Work 2. |
| **representation** | Download PDF Abstract 1 Introduction 2 Related Work 2.1 Cognitive Architectures and Memory Systems 2.2 Generative Agents and Memory Management 2. |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 13. Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi-session Agents
**arXiv:2512.20092** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Temporal reasoning over long, multi-session dialogues is a critical capability for conversational agents. |
| **representation** | Temporal reasoning over long, multi-session dialogues is a critical capability for conversational agents. However, existing works and our pilot study have shown that as dialogue histories grow in length and accumulate noise, current long-context models struggle to accurately identify temporally pertinent information, significantly impairing reasoning performance. To address this, we introduce Memory-T1 , a framework that learns a time-aware memory selection policy using reinforcement learning (R… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 14. MemR$^3$: Memory Retrieval via Reflective Reasoning for LLM Agents
**arXiv:2512.20237** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Download PDF Abstract 1 Introduction 2 Related Work 2. |
| **representation** | Download PDF Abstract 1 Introduction 2 Related Work 2.1 Memory for LLM Agents 2.2 Agentic Retrieval-Augmented Generation |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 15. AgentMath: Empowering Mathematical Reasoning for Large Language Models via Tool-Augmented Agent
**arXiv:2512.20745** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | syntax tree depth) are enforced to eliminate instances of unnecessary code invocation, thereby reinforcing necessity-aware tool utilization patterns. |
| **representation** | syntax tree depth) are enforced to eliminate instances of unnecessary code invocation, thereby reinforcing necessity-aware tool utilization patterns. Self-Correction Capability Injection. Beyond correct tool invocation, a robust agent need also recover from erroneous tool feedback. We sample trajectories that were excluded during refinement due to execution failures, and for each failed program c fail c_{\text{fail}} with error output o error = ℰ ​ ( c fail ) o_{\text{error}}=\mathcal{E}(c_{\tex… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 16. Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning
**arXiv:2601.04726** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Large language models (LLMs) are increasingly deployed as intelligent agents that reason, plan, and interact with their environments. |
| **representation** | Large language models (LLMs) are increasingly deployed as intelligent agents that reason, plan, and interact with their environments. To effectively scale to long-horizon scenarios, a key capability for such agents is a memory mechanism that can retain, organize, and retrieve past experiences to support downstream decision-making. However, most existing approaches organize and store memories in a flat manner and rely on simple similarity-based retrieval techniques. Even when structured memory is… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 17. Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents
**arXiv:2601.07468** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S7 |
| **problem** | Memory enables Large Language Model (LLM) agents to perceive, store, and use information from past dialogues, which is essential for personalization. |
| **representation** | Memory enables Large Language Model (LLM) agents to perceive, store, and use information from past dialogues, which is essential for personalization. However, existing methods fail to properly model the temporal dimension of memory in two aspects: 1) Temporal inaccuracy: memories are organized by dialogue time rather than their actual occurrence time; 2) Temporal fragmentation: existing methods focus on point-wise memory, losing durative information that captures persistent states and evolving p… |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S2, S7. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 18. M2A: Multimodal Memory Agent with Dual-Layer Hybrid Memory for Long-Term Personalized Interactions
**arXiv:2602.07624** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | This work addresses the challenge of personalized question answering in long-term human-machine interactions: when conversational history spans weeks or months and exceeds the context window, existing personalization mechanisms struggle to continuously absorb and leverage users’ incremental concepts, aliases, and preferences. |
| **representation** | This work addresses the challenge of personalized question answering in long-term human-machine interactions: when conversational history spans weeks or months and exceeds the context window, existing personalization mechanisms struggle to continuously absorb and leverage users’ incremental concepts, aliases, and preferences. Current personalized multimodal models are predominantly static—concepts are fixed at initialization and cannot evolve during interactions. We propose M |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S2, S3, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **no** |

---

### 19. A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning, Hallucination, and Interactivity
**arXiv:2302.04023** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | This paper proposes a framework for quantitatively evaluating interactive LLMs such as ChatGPT using publicly available data sets, using. |
| **representation** | This paper proposes a framework for quantitatively evaluating interactive LLMs such as ChatGPT using publicly available data sets, using |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | Silent or partial — see paper. |
| **privacy** | Silent or partial — see paper. |
| **Kedger lessons** | (1) Map paper mechanisms to Kedger S-stage S1, S7, S8. (2) Use as survey-bibliography runway evidence for measure→refine. (3) Extract constants only from paper tables — do not invent. (4) Cross-ref stage matrix before refine tickets. |
| **metric_impact** | Paper-reported metrics on primary benchmark/task. |
| **refine_candidate** | **yes** |

---

### 20. Do LLMs Understand Social Knowledge? Evaluating the Sociability of Large Language Models with SocKET Benchmark
**arXiv:2305.14938** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Large language models (LLMs) have been shown to perform well at a variety of syntactic, discourse, and reasoning tasks. |
| **representation** | Large language models (LLMs) have been shown to perform well at a variety of syntactic, discourse, and reasoning tasks. While LLMs are increasingly deployed in many forms including conversational agents that interact with humans, we lack a grounded benchmark to measure how well LLMs understand social language. Here, we introduce a new theory-driven benchmark, SocKET , that contains |
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
| Cumulative FULL | **340** |
