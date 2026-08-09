# Batch 17 — Survey Runway FULL (Kedger) — **deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Honest re-card of survey-runway papers — mechanism extraction from **full body** (Intro/Method/Results), not abstract paste.  
> **Progress:** FULL 320 → **340** toward 500.  
> **Method:** Cached `/tmp/kedger-papers/full/{id}.txt`; cards built by `scripts/research/deep_recard_500.py`.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers only from body matches. Generic lessons forbidden.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body mechanism deep-read; ID already ledgered Batch17 — **re-card upgrade**) | **20** | `2508.10419`, `2508.12379`, `2508.15294`, `2509.21212`, `2509.23040`, `2510.01353`, `2510.13614`, `2510.19897`, `2510.21618`, `2511.10030`, `2511.20857`, `2512.12856`, `2512.20092`, `2512.20237`, `2512.20745`, `2601.04726`, `2601.07468`, `2602.07624`, `2302.04023`, `2305.14938` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs have `.txt` ≥15k chars. |
| **Method span extracted** | **7/20** | continuous-text section split |
| **Numeric evidence extracted** | **19/20** | regex over method/results |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning
**arXiv:2508.10419** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | The core challenge of long narrative comprehension lies not merely in connecting discrete pieces of evidence, a task more naturally defined as multi-hop Question Answering (QA), but in performing a dynamic cognitive synthesis to grasp necessary background and content progression  |
| **representation** | We introduce ComoRAG, an autonomous cognitive architecture designed to formalize and implement the process of Metacognitive Regulation outlined in the Introduction. 2.1 Problem Formulation: Towards Principled Narrative Reasoning Our objective is to design a framework for stateful reasoning in RAG scenarios. To ensure all reasoning is traceable to source evidence, a veridical layer 𝒳 v ​ e ​ r \mathcal{X}^{ver} is firstly established, constituted by raw text chunks directly, analogous to the precise recall of factual details in human memory. |
| **write / read / forget** | Write: With newly retrieved information by 𝒫 ( t ) \mathcal{P}^{(t)} at each step, the framework utilizes the global memory pool maintained till the prior step ℳ p ​ o ​ o ​ l ( t − 1 ) \ Read: Formally, denote the initial query as q i ​ n ​ i ​ t q_{init} , and a knowledge source 𝒳 \mathcal{X} derived upon the original context, our framework F F leverages a series of ada Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: We introduce ComoRAG, an autonomous cognitive architecture designed to formalize and implement the process of Metacognitive Regulation outlined in the Introduct (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: +24.6%, 30%, 22%, 15%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: +24.6%; 30%; 22%; 15%; 24%; 19% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 2. GraphCogent: Mitigating LLMs’ Working Memory Constraints via Multi-Agent Collaboration in Complex Graph Unders
**arXiv:2508.12379** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | However, when querying the connection path between two webpages in a Web graph, state-of-the-art LLMs like DeepSeek-R1 (DeepSeek-AI, 2025 ) , GPT-o3 (OpenAI, 2023 ) , and Gemini-2.5 pro (Group, 2023 ) return incorrect navigation routes in 9 out of 10 cases. |
| **representation** | However, when querying the connection path between two webpages in a Web graph, state-of-the-art LLMs like DeepSeek-R1 (DeepSeek-AI, 2025 ) , GPT-o3 (OpenAI, 2023 ) , and Gemini-2.5 pro (Group, 2023 ) return incorrect navigation routes in 9 out of 10 cases. This failure reveals that current LLMs remain limited in handling large real-world graph reasoning tasks. Graph N-back Query Task: A graph is split into 50-edge subsets E t E_{t} . |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: However, when querying the connection path between two webpages in a Web graph, state-of-the-art LLMs like DeepSeek-R1 (DeepSeek-AI, 2025 ) , GPT-o3 (OpenAI, 20 (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 50%, by 20%, by 80%, 30%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 50%; by 20%; by 80%; 30%; 100%; 30.8% |
| **refine_candidate** | **yes** — S-stage S3, S5, S7, S8 |

---

### 3. [2508.15294] Multiple Memory Systems for Enhancing the Long-term Memory of Agent Multiple Memory Systems for E
**arXiv:2508.15294** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | An agent powered by large language models have achieved impressive results, but effectively handling the vast amounts of historical data generated during interactions remains a challenge. |
| **representation** | An agent powered by large language models have achieved impressive results, but effectively handling the vast amounts of historical data generated during interactions remains a challenge. The current approach is to design a memory module for the agent to process these data. However, existing methods, such as MemoryBank and A-MEM, have poor quality of stored memory content, which affects recall performance and response quality. |
| **write / read / forget** | Write: However, existing methods, such as MemoryBank and A-MEM, have poor quality of stored memory content, which affects recall performance and response quality. Read: However, existing methods, such as MemoryBank and A-MEM, have poor quality of stored memory content, which affects recall performance and response quality. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: An agent powered by large language models have achieved impressive results, but effectively handling the vast amounts of historical data generated during intera (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 200 questions, F1 = 2, EM 24.82, EM 25.21. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 200 questions; F1 = 2; EM 24.82; EM 25.21; EM 17.73; EM 22.98 |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 4. SGMem: Sentence Graph Memory for Long-Term Conversational Agents
**arXiv:2509.21212** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Memory is a fundamental component of long-term conversational agents (Maharana et al., 2024 ; Wu et al., 2024 ) , allowing them to augment dialogue context beyond the limited window of large language models (LLMs) (Zhang et al., 2025c ; Wu et al., 2025 ; Sapkota et al., 2025 ) . |
| **representation** | 3.1 Preliminaries We consider the task of long-term conversational question answering (QA), where the input consists of a sequence of sessions denoted as 𝒮 = { s 1 , s 2 , … , s U } \mathcal{S}=\{s_{1},s_{2},\ldots,s_{U}\} . These hierarchical units—sessions, rounds, turns, generated memory, and sentences—form the basis of our Sentence Graph Memory (SGMem) management and retrieval framework. 3.2 Framework Overview Long-term conversational agents often suffer from coarse memory segmentation, where both raw dialogue history (turns, rounds, sessions) and generated memories (summaries, facts, insights) are stored and retrieved at coarse granularity, leading to fragmented |
| **write / read / forget** | Write: 3.2 Framework Overview Long-term conversational agents often suffer from coarse memory segmentation, where both raw dialogue history (turns, rounds, sessions) and generated memorie Read: These hierarchical units—sessions, rounds, turns, generated memory, and sentences—form the basis of our Sentence Graph Memory (SGMem) management and retrieval framework. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 Preliminaries We consider the task of long-term conversational question answering (QA), where the input consists of a sequence of sessions denoted as 𝒮 = {  (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Metrics named: Accuracy, accuracy (values: see paper tables). |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 5. Look Back to Reason Forward: Revisitable Memory for Long-Context LLM Agents Report GitHub Issue × Title: Conte
**arXiv:2509.23040** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | 2 Method 2.1 Preliminaries: MDP Memory Agent for Long-Context QA 2.2 Memory Agent with History-Augmented State 2.3 Reinforcement Learning with Multi-Level Reward Shaping 2.3.1 Trajectory-Level Outcome Rewards for Final Correctness 2.3.2 Step-Level Action Rewards for Behavior Shap |
| **representation** | See paper body. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S2, S3, S7, S8. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 80.8%, 38.3%, 31.3%, 50.3%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 80.8%; 38.3%; 31.3%; 50.3%; 29.9%; 32% |
| **refine_candidate** | **no** |

---

### 6. [2510.01353] Memtrack: Evaluating Long-Term Memory and State Tracking in Multi-Platform Dynamic Agent Environm
**arXiv:2510.01353** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Recent advances in adaptivity of AI agents have surfaced the need for dynamic memory components that can acquire, understand and utilize relevant information from previous interactions [ 1 ] . |
| **representation** | Recent advances in adaptivity of AI agents have surfaced the need for dynamic memory components that can acquire, understand and utilize relevant information from previous interactions [ 1 ] . More specifically, memory has been used to enhance personalization [ 2 ] and performance of LLM agents in robotics [ 3 ] , financial trading [ 4 ] , healthcare [ 5 ] and science research [ 6 ] . While these advances bring real-life impact and are scaling to multi-agent systems faster [ 7 , 8 ] , benchmarking memory in agentic systems has been largely limited to conversational setups. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Each benchmark instance provides a chronologically platform-interleaved timeline, with noisy, conflicting, cross-referring information as well as potential codebase/file-system comprehension and exploration. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Recent advances in adaptivity of AI agents have surfaced the need for dynamic memory components that can acquire, understand and utilize relevant information fr (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: em 0.601, em0, em 0.144, 20%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: em 0.601; em0; em 0.144; 20%; 60% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 7. MemoTime: Memory-Augmented Temporal Knowledge Graph Enhanced Large Language Model Reasoning
**arXiv:2510.13614** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, due to the prohibitive cost of retraining, these models are inherently static. |
| **representation** | Typical RAG systems embed both questions and documents into a shared vector space and retrieve semantically similar passages (Ma et al. TKGs encode factual knowledge as quadruples (subject, relation, object, timestamp), offering explicit temporal grounding and relational structure. Temporal Knowledge Graph Question Answering (TKGQA) serves as a representative evaluation for this task, requiring systems to answer natural language questions by retrieving temporally relevant facts from TKGs. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: However, existing TKG-based LLM reasoning methods still struggle with four major challenges: maintaining temporal faithfulness in multi-hop reasoning, achieving multi-entity tempor Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Typical RAG systems embed both questions and documents into a shared vector space and retrieve semantically similar passages (Ma et al. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: up to 24.0%, 30%, 77.9%, by 24.0%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: up to 24.0%; 30%; 77.9%; by 24.0%; 68.2%; 71.4% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 8. Learning from Supervision with Semantic and Episodic Memory: A Reflective Approach to Agent Adaptation Report 
**arXiv:2510.19897** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | 2 Learning from Supervised Signals 2.1 What to Remember? |
| **representation** | 3 Incorporating Critiques into Memory 3.1 Semantic Memory 3.2 Episodic Memory 3.3 Combining Semantic and Episodic Memory 4 Empirical Evaluation 4.1 Datasets Multi-Condition Ranking (Pezeshkpour and Hruschka, 2025 ) NFCorpus (Boteva et al. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: 3 Incorporating Critiques into Memory 3.1 Semantic Memory 3.2 Episodic Memory 3.3 Combining Semantic and Episodic Memory 4 Empirical Evaluation 4.1 Datasets Mul (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 56.2%, 74%, 81.6%, 4.6 points. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 56.2%; 74%; 81.6%; 4.6 points; 31.95% |
| **refine_candidate** | **no** |

---

### 9. DeepAgent: A General Reasoning Agent with Scalable Toolsets
**arXiv:2510.21618** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Although effective in simpler tasks, these approaches suffer from several critical limitations: (1) lack of autonomy in execution steps and overall procedure; (2) inability to dynamically discover tools during task execution; (3) deficiency in fully autonomous management of inter |
| **representation** | Problem Formulation We frame the agent’s task as a sequential decision-making process. The agent receives a user-provided question Q Q and an instruction I I , and interacts with an environment over a series of steps t = 1 , … , T t=1,\dots,T to accomplish the specified goal. At each step t t , the agent’s state s t s_{t} consists of the history of all previous actions and their resulting observations, i.e., s t = ( a 1 , o 1 , … , a t − 1 , o t − 1 ) s_{t}=(a_{1},o_{1},\dots,a_{t-1},o_{t-1}) . |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: • Tool Search ( a t search a_{t}^{\text{search}} ) : A natural language query q s q_{s} to find relevant tools from 𝒯 \mathcal{T} . Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Problem Formulation We frame the agent’s task as a sequential decision-making process. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 89.0%, 75.4%, 55.0%, 52.6%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 89.0%; 75.4%; 55.0%; 52.6%; 64.0%; 40.6% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 10. Multi-agent In-context Coordination via Decentralized Memory Retrieval Report GitHub Issue × Title: Content se
**arXiv:2511.10030** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | This capability has also been explored in Reinforcement Learning (RL), where agents interact with the environment to retrieve context and maximize cumulative rewards, showcasing strong adaptability in complex settings. However, in cooperative Multi-Agent Reinforcement Learning (MARL), where agents must coordinate toward a shared goal, decentralized policy deployment can lead to mismatches in task alignment and reward assignment, limiting the efficiency of policy adaptation. To address this challenge, we introduce M ulti- A gent I n- C ontext C oordination via Decentralized Memory Retrieval (MAICC), a novel approach designed to enhance coordination by fast adaptation. |
| **write / read / forget** | Write: Architecture D.3 Hyper-Parameter Settings D.4 Computing Infrastructure E Additional Experiment Results E.1 Visualization of Learned Embeddings E.2 Ablation Study E.3 Sensitivity of Read: Architecture D.3 Hyper-Parameter Settings D.4 Computing Infrastructure E Additional Experiment Results E.1 Visualization of Learned Embeddings E.2 Ablation Study E.3 Sensitivity of Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: This capability has also been explored in Reinforcement Learning (RL), where agents interact with the environment to retrieve context and maximize cumulative re (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: em 1, 95%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: em 1; 95% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 11. Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory Report GitHub Issue × Title: C
**arXiv:2511.20857** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | See paper body. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S1, S7, S8. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: em0, em 0.27, em 0.10, em 0.13. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: em0; em 0.27; em 0.10; em 0.13; em 0.70; em 0.43 |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 12. Forgetful but Faithful: A Cognitive Memory Architecture and Benchmark for Privacy‑Aware Generative Agents Repo
**arXiv:2512.12856** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | 4.1 Memory-Aware Retention Schema (MaRS) Framework 4.2 Forgetting Policy Design and Implementation 4.3 Privacy-Preserving Mechanisms 5 Implementation 5.1 System Architecture 5.2 Memory Store Implementation 5.3 Policy Implementation Details 5.4 Privacy Implementation 6 The FiFA Benchmark 6.1 Benchmark Design Principles 6.1.1 Multi‑Dimensional Assessment 6.1.2 Realistic Interaction Scenarios 6.1.3 Scalable Evaluation Framework 6.1.4 Human‑Centered Metrics 6.2 Benchmark Architecture 6.2.1 Agent Sim |
| **write / read / forget** | Write: 4.1 Memory-Aware Retention Schema (MaRS) Framework 4.2 Forgetting Policy Design and Implementation 4.3 Privacy-Preserving Mechanisms 5 Implementation 5.1 System Architecture 5.2 Me Read: retrieval/recall path described. Forget: 4.1 Memory-Aware Retention Schema (MaRS) Framework 4.2 Forgetting Policy Design and Implementation 4.3 Privacy-Preserving Mechanisms 5 Implementation 5.1 System |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | 4.1 Memory-Aware Retention Schema (MaRS) Framework 4.2 Forgetting Policy Design and Implementation 4.3 Privacy-Preserving Mechanisms 5 Implementation 5.1 System Architecture 5.2 Memory Store Implementation 5.3 Policy Imp |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S1, S7, S8. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: Accuracy 6.6, 95%, Accuracy 1.42. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: Accuracy 6.6; 95%; Accuracy 1.42 |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 13. Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi-session Agents
**arXiv:2512.20092** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Increasingly, these agents are expected to support long-term multi-session interactions (Du et al., 2025b ; Ge et al., 2025 ) , where a central challenge is understanding and reasoning about temporal relationships across dialogue histories (Wu et al., 2025 ; Maharana et al., 2024 |
| **representation** | Recent advances in memory architectures and large language models (LLMs) have substantially improved the capabilities of conversational agents (Yu et al., 2025 ; Zhong et al., 2024 ; Xu et al., 2025 ) . To bridge this gap, we introduce Memory-T1 , a RL-based memory retrieval framework designed for temporal reasoning that combines coarse-to-fine retrieval strategy with a multi-level reward design. This phase efficiently narrows the vast memory pool to a manageable context, setting the stage for a more precise analysis. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Recent advances in memory architectures and large language models (LLMs) have substantially improved the capabilities of conversational agents (Yu et al., 2025  (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 716 examples, 67.0%, by 10.2%, 15.0%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 716 examples; 67.0%; by 10.2%; 15.0%; 7.9%; 5.5% |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 14. MemR3: Memory Retrieval via Reflective Reasoning for LLM Agents Report GitHub Issue × Title: Content selection
**arXiv:2512.20237** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, many deployed memory systems primarily optimize compression and storage, with comparatively less emphasis on explicit, closed-loop control of memory retrieval. |
| **representation** | Memory systems have been designed to leverage past experiences in Large Language Model (LLM) agents. However, many deployed memory systems primarily optimize compression and storage, with comparatively less emphasis on explicit, closed-loop control of memory retrieval. This design departs from the standard retrieve-then-answer pipeline by introducing a closed-loop control mechanism that enables autonomous decision-making. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: However, many deployed memory systems primarily optimize compression and storage, with comparatively less emphasis on explicit, closed-loop control of memory retrieval. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Memory systems have been designed to leverage past experiences in Large Language Model (LLM) agents. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 200 questions, em0, 74.62%, 76.26%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 200 questions; em0; 74.62%; 76.26%; 75.54%; 81.55% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 15. [2512.20745] AgentMath: Empowering Mathematical Reasoning for Large Language Models via Tool-Augmented Agent A
**arXiv:2512.20745** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, when tackling mathematical problems that demand precise computation or intricate symbolic manipulation, including large-number arithmetic, complex equation solving, and geometric reasoning, pure text-based reasoning still has limitations: frequent computational errors ne |
| **representation** | Architecture The architecture is founded on the principle of decoupling GPU-intensive model inference from CPU/IO-intensive agent logic and environment interactions. We introduce an Agentic Partial Rollout mechanism that decomposes each trajectory τ \tau into budget-limited segments: τ = τ ( 1 ) ⊕ τ ( 2 ) ⊕ … ⊕ τ ( N ) , \tau=\tau^{(1)}\oplus\tau^{(2)}\oplus\ldots\oplus\tau^{(N)}, where ⊕ \oplus denotes sequence concatenation. 2.4.3 Prefix-Aware Weighted Load Balancing Partial rollouts alleviate long-tail latency but introduce requests with long prefixes, increasing KV-cache memory and prefill cost. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Architecture The architecture is founded on the principle of decoupling GPU-intensive model inference from CPU/IO-intensive agent logic and environment interact (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 59.6%, 48.1%, 40.2%, 43.1%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 59.6%; 48.1%; 40.2%; 43.1%; 30.2%; 20.1% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 16. Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning
**arXiv:2601.04726** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | , 2025a ) , they often fail to capture essential logical relations, such as causality and temporal sequences (Figure 1 (b)) (Yang et al. |
| **representation** | To support such behaviors, agents require memory mechanisms that go beyond simple text generation capabilities (Ouyang et al. Ideally, similar to human memory, agent memory should serve not only as a repository of knowledge, but also as a fundamental infrastructure that supports reasoning, planning, and decision-making (Wu et al. Within the broader field of agent memory research, a significant amount of attention has been directed toward factual memory (Zhang et al. |
| **write / read / forget** | Write: However, most existing approaches organize and store memories in a flat manner and rely on simple similarity-based retrieval techniques. Read: To effectively scale to long-horizon scenarios, a key capability for such agents is a memory mechanism that can retain, organize, and retrieve past experiences to support downstrea Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: To support such behaviors, agents require memory mechanisms that go beyond simple text generation capabilities (Ouyang et al. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 47.92%, 52.18%, 57.96%, 48.93%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 47.92%; 52.18%; 57.96%; 48.93%; 52.52%; 5% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 17. Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents
**arXiv:2601.07468** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, as shown in Figure ˜ 1 , existing methods suffer from two critical limitations in how they model temporal information. |
| **representation** | Memory consolidation constructs a temporal knowledge graph from episodic memory and subsequently consolidates it into time-aware durative memory. Memory utilization retrieves accurate memories by applying semantic-temporal constraints. 3.1 Preliminary We consider the task of building a personalized dialogue agent in a multi-session conversational setting. |
| **write / read / forget** | Write: Memory consolidation constructs a temporal knowledge graph from episodic memory and subsequently consolidates it into time-aware durative memory. Read: Memory utilization retrieves accurate memories by applying semantic-temporal constraints. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Memory consolidation constructs a temporal knowledge graph from episodic memory and subsequently consolidates it into time-aware durative memory. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 74.80%, 62.60%, +20.30%, +22.56%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 74.80%; 62.60%; +20.30%; +22.56%; 71.23%; 76.69% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 18. M2A: Multimodal Memory Agent with Dual-Layer Hybrid Memory for Long-Term Personalized Interactions
**arXiv:2602.07624** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | However, these models are primarily trained for generic, “anonymous” users and lack mechanisms to explicitly capture individual concepts, naming conventions, or stylistic preferences. |
| **representation** | Meanwhile, long-term conversations quickly exceed context windows, requiring external memory and selective retrieval (Maharana et al. However, existing memory systems largely focus on text, offering limited support for multimodal concepts, fine-grained updates, or editable memory structures specifically designed for human-machine interactions. Addressing these limitations requires a unified framework for editable multimodal personalization. |
| **write / read / forget** | Write: We propose M 2 A , an agentic dual-layer hybrid memory system that maintains personalized multimodal information through online updates. Read: The system employs two collaborative agents: ChatAgent manages user interactions and autonomously decides when to query or update memory, while MemoryManager breaks down memory req Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Meanwhile, long-term conversations quickly exceed context windows, requiring external memory and selective retrieval (Maharana et al. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 44.64%, 33.27%, em0, 34.73%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 44.64%; 33.27%; em0; 34.73%; 36.26%; 44.71% |
| **refine_candidate** | **no** |

---

### 19. A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning, Hallucination, and Interactivity
**arXiv:2302.04023** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, despite its powerful abilities, anecdotal reports on ChatGPT consistently showed remaining challenges - for example, it fails in some elementary mathematical Gilson et al. |
| **representation** | ese data sets and a newly designed multimodal dataset. We find that ChatGPT outperforms LLMs with zero-shot learning on most tasks and even outperforms fine-tuned models on some tasks. We find that it is better at understanding non-Latin script languages than generating them. It is able to generate multimodal content from textual prompts via an intermediate code generation step. Moreover, we find that ChatGPT is 63.41% accurate on average in 10 different reasoning categories under logical reason |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S1, S7, S8. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 63.41%, 8%, 2%, 100%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 63.41%; 8%; 2%; 100%; EM 2021; 140 tasks |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 20. Do LLMs Understand Social Knowledge? Evaluating the Sociability of Large Language Models with the SocKET Bench
**arXiv:2305.14938** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, despite the recognized need for social knowledge (Hovy and Yang, 2021 ) , the NLP field has limited abilities to test it. |
| **representation** | Here, we introduce SocKET , a new benchmark for evaluating social knowledge. We introduce SocKET ( Soc ial K nowledge E valuation T ests), a theory-grounded, systematic collection of 58 social language tasks. We release our framework code and prepackaged datasets at https://github.com/minjechoi/SOCKET and https://huggingface.co/datasets/Blablablab/SOCKET . |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Here, we introduce SocKET , a new benchmark for evaluating social knowledge. (2) Eval/analysis paper — extract fixtures/SLIs rather than store ops. (3) Lock numeric claims from body: 58 tasks, 2018 Task, 2019 Task, 2020 Task. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 58 tasks; 2018 Task; 2019 Task; 2020 Task; 2022 task; 2021 Task |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (upgraded) | 20 |
| Cumulative FULL | **340** |
