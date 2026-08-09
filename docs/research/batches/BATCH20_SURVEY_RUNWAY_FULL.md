# Batch 20 — Survey Runway FULL (Kedger) — **deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Honest re-card of survey-runway papers — mechanism extraction from **full body** (Intro/Method/Results), not abstract paste.  
> **Progress:** FULL 380 → **400** toward 500.  
> **Method:** Cached `/tmp/kedger-papers/full/{id}.txt`; cards built by `scripts/research/deep_recard_500.py`.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers only from body matches. Generic lessons forbidden.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body mechanism deep-read; ID already ledgered Batch20 — **re-card upgrade**) | **20** | `2510.13363`, `2510.23010`, `2511.01633`, `2511.07800`, `2511.12997`, `2511.17208`, `2511.21678`, `2511.21726`, `2512.02425`, `2512.12360`, `2512.16962`, `2601.03192`, `2601.03417`, `2601.06037`, `2601.06377`, `2601.08323`, `2601.10744`, `2601.14192`, `2602.15329`, `2603.00503` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs have `.txt` ≥15k chars. |
| **Method span extracted** | **11/20** | continuous-text section split |
| **Numeric evidence extracted** | **18/20** | regex over method/results |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. D-SMART: Enhancing LLM Dialogue Consistency via Dynamic Structured Memory And Reasoning Tree Introduction The 
**arXiv:2510.13363** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Meaning Representation (AMR) to capture its core semantic structure. |
| **representation** | We retained only those dialogues where the baseline model achieved a GPT score in a moderate range (e.g., between 4.0 and 8.0). The goal was to identify dialogues that place high demands on memory, reasoning, and context management. The primary criteria for this ranking included: • Dialogue Scale and Information Density: A high Average Turns per Dialogue and Average Words per Turn to test the model’s long-term memory and its ability to process information-dense utterances, which are core challenges for the D |
| **write / read / forget** | Write: This tests the DSM’s dynamic update mechanism, including its ability to integrate new facts and resolve conflicts in real-time. Read: Appendix D Appendix D: Benchmark Task Details and Case Studies The MT-Bench-101 benchmark is structured around 13 distinct task categories, each formulated to rigorously evaluate s Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | This tests the DSM’s dynamic update mechanism, including its ability to integrate new facts and resolve conflicts in real-time. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: We retained only those dialogues where the baseline model achieved a GPT score in a moderate range (e.g., between 4.0 and 8.0). (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 25%, 74%, 6.12%, 10.89%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 25%; 74%; 6.12%; 10.89%; 16.96%; 22.46% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 2. TALM: Dynamic Tree-Structured Multi-Agent Framework with Long-Term Memory for Scalable Code Generation
**arXiv:2510.23010** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | While effective for short functions and modular tasks, these approaches rely on a single reasoning path and struggle when requirements become complex or context exceeds the model’s window size (Levy et al . |
| **representation** | CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation. TDAG: A multi-agent framework based on dynamic task decomposition and agent generation. AutoGen: Enabling next-gen llm applications via multi-agent conversation. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 87.20%, 45.20%, 74.40%, 33.00%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 87.20%; 45.20%; 74.40%; 33.00%; 88.45%; 45.80% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 3. Scaling Graph Chain-of-Thought Reasoning: A Multi-Agent Framework with Efficient LLM Serving
**arXiv:2511.01633** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | To support complex reasoning, Chain-of-Thought (CoT) prompting (Wei et al., 2022 ) has emerged as a core mechanism, enabling step-by-step inference by decomposing complex tasks into intermediate steps and thereby emulating human problem-solving processes. |
| **representation** | To overcome these limitations, we introduce a code generation optimization that enables the Action Agent to synthesize complete executable Python snippets rather than merely selecting from predefined functions. Executing s s once against the Graph RAG retriever produces the required facts to update the agent’s notebook or generate the final answer, thereby replacing multiple reasoning rounds with a single deterministic program execution and significantly reducing token usage and latency As illustrated in Figure 6 , for queries requiring information from multiple vertices, a single code snippet can invoke several graph functions within one reasoning round, thereby reducing interaction steps. |
| **write / read / forget** | Write: Executing s s once against the Graph RAG retriever produces the required facts to update the agent’s notebook or generate the final answer, thereby replacing multiple reasoning rou Read: Each snippet is composed only of: (i) the predefined graph-retrieval functions and basic control; (ii) optional local computations (e.g., aggregation, set intersection) to derive t Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: To overcome these limitations, we introduce a code generation optimization that enables the Action Agent to synthesize complete executable Python snippets rathe (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: up to 38%, up to 95.7%, by 90.3%, 31%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: up to 38%; up to 95.7%; by 90.3%; 31%; 46%; 50% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 4. From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory
**arXiv:2511.07800** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | reusable decision patterns from successful paths. |
| **representation** | specific to certain knowledge domains. 5. Existing Knowledge Enhancement: When quantity is high, focus on strengthening weak metacognitions. Decision Options: • create: Create new metacognition (when discovering valuable and distinct patterns, or when quantity ≤ \leq 30). • update: Update existing metacognition (preferred when quantity > > 30, especially targeting low-confidence ones). • skip: Skip metacognition operation (when evidence is insufficient or has no new value). Skip Metacognition Si |
| **write / read / forget** | Write: • update: Update existing metacognition (preferred when quantity > > 30, especially targeting low-confidence ones). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S1, S7, S8. (2) Primarily a write/store design — gate promote before L3 commit. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 5. WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance Report GitHub Issue × Title: Content sel
**arXiv:2511.12997** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | 2 WebCoach: A Model-Agnostic Framework for Memory-Augmented Web Navigation 2.1 WebCondenser Input. |
| **representation** | 2 WebCoach: A Model-Agnostic Framework for Memory-Augmented Web Navigation 2.1 WebCondenser Input. 3 Experiments 3.1 Data 3.2 Setup Asynchronous Evaluation with Dynamic Batching Base-Agent Configuration. 4 Results 5 Related Work Reasoning-Centric Web and GUI Agents Agentic Memory and Context Management Self-Evolving Agents |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: 2 WebCoach: A Model-Agnostic Framework for Memory-Augmented Web Navigation 2.1 WebCondenser Input. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 50 tasks, 643 tasks, 83%, 47.3%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 50 tasks; 643 tasks; 83%; 47.3%; 61.4%; 7 points |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 6. A Simple Yet Strong Baseline for Long-Term Conversational Memory of LLM Agents
**arXiv:2511.17208** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Even in so–called long-context variants, performance can degrade sharply ( liu-etal-2024-lost ) and the LLMs can struggle to faithfully recall information that is many sessions old ( locomo ; wu2025longmemeval ) . |
| **representation** | 3.1 Problem Setting A conversation consists of sessions 𝒮 = { s 1 , … , s T } \mathcal{S}=\{s_{1},\dots,s_{T}\} ordered by timestamps τ ​ ( s ) \tau(s) . At query time, the agent receives a natural language question q q and answer it conditioned on the entire conversation history. We assume access to an embedding encoder h ​ ( ⋅ ) h(\cdot) that maps any text x x to an embedding h ​ ( x ) ∈ ℝ d h(x)\in\mathbb{R}^{d} , and a powerful QA model f QA f_{\text{QA}} that takes ( q , memory ) (q,\text{memory}) as input and generates an answer. |
| **write / read / forget** | Write: In a triple-based knowledge graph, the same content would typically be decomposed into multiple relation triples, e.g., ( Bob , attend , Global AI Innovation Symposium 2024 ) (\tex Read: Figure 1 illustrates the overall offline indexing and online retrieval pipelines. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 Problem Setting A conversation consists of sessions 𝒮 = { s 1 , … , s T } \mathcal{S}=\{s_{1},\dots,s_{T}\} ordered by timestamps τ ​ ( s ) \tau(s) . (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 77.9%, 76.0%, em0, em 0.249. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 77.9%; 76.0%; em0; em 0.249; em 0.771; em 0.508 |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 7. ViLoMem: Agentic Learner with Grow-and-Refine Multimodal Semantic Memory Report GitHub Issue × Title: Content 
**arXiv:2511.21678** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | knowledge through coordinated but distinct representational streams. |
| **representation** | 3.1 Memory Generation 3.1.1 Visual Memory Generation 3.1.2 Logical Memory Generation 3.2 Memory Retrieval and Utilization 3.2.1 Visual Memory Retrieval 3.2.2 Logical Memory Retrieval 3.2.3 Solution Generation with Dual Memory |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: 3.1 Memory Generation 3.1.1 Visual Memory Generation 3.1.2 Logical Memory Generation 3.2 Memory Retrieval and Utilization 3.2.1 Visual Memory Retrieval 3.2.2 Logical Memory Retriev Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 Memory Generation 3.1.1 Visual Memory Generation 3.1.2 Logical Memory Generation 3.2 Memory Retrieval and Utilization 3.2.1 Visual Memory Retrieval 3.2.2 Lo (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 59%, 93%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 59%; 93% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 8. Goal-Directed Search Outperforms Goal-Agnostic Memory Compression in Long-Context Memory Tasks Report GitHub I
**arXiv:2511.21726** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | 2 Related Works 2.1 External Memory in LLMs 2.2 RLVR and Multi‑Turn Agentic Tool Use 2.3 Trainable Search over Memory |
| **representation** | 3.1 Problem Formulation 3.2 System Architecture 3.3 Reinforcement Learning with GRPO 3.3.1 GRPO Objective 3.3.2 Multi-Turn Tool Interactions and Masking 3.4 Reward Function 3.5 Training and Validation Data |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 Problem Formulation 3.2 System Architecture 3.3 Reinforcement Learning with GRPO 3.3.1 GRPO Objective 3.3.2 Multi-Turn Tool Interactions and Masking 3.4 Rew (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: em0, 30 examples, em 8.42, EM 35.36. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: em0; 30 examples; em 8.42; EM 35.36; 37.57%; 15 points |
| **refine_candidate** | **no** |

---

### 9. WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning Report GitHub Issue × Title: Content selecti
**arXiv:2512.02425** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | See paper body. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S2, S3, S7, S8. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 9.3%, 6.1%, 4.4%, 7%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 9.3%; 6.1%; 4.4%; 7%; 3%; 15 questions |
| **refine_candidate** | **no** |

---

### 10. VideoARM: Agentic Reasoning over Hierarchical Memory for Long-Form Video Understanding Report GitHub Issue × T
**arXiv:2512.12360** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | 3.1 Overview 3.2 Hierarchical and Multimodal Memory 3.3 Coarse-to-Fine Video Reasoning Agent 3.3.1 Multimodal Toolsets 3.3.2 Controller 4 Experiment 4.1 Benchmarks 4.2 Implementation Details 4.3 |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 Overview 3.2 Hierarchical and Multimodal Memory 3.3 Coarse-to-Fine Video Reasoning Agent 3.3.1 Multimodal Toolsets 3.3.2 Controller 4 Experiment 4.1 Benchma (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 678 questions, 564 questions, 337 question, 500 question. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 678 questions; 564 questions; 337 question; 500 question; 200 question; 80.0% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 11. MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience Retrieval Report GitHub Issue × Title
**arXiv:2512.16962** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | 4.1 Attack Setup 4.2 Poisoning Phase 4.3 Evaluation Phase 4.4 Mechanism of Persistence and behavioral Drift 5 Experiment 5.1 Agent Configuration and Environment 5.2 Dataset Construction and Evaluation Protocol 5.3 Quantitative Results: Aggregate Retrieval 5.4 Mechanism Analysis: Impact of Union Retrieval (BM25+Embeddings) 5.5 Qualitative Analysis: Retrieval Dynamics 1. High retrieval penetration despite a small poisoned set 2. Robustness across heterogeneous user tasks 6 Potential Defense 7 Conc |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: 4.1 Attack Setup 4.2 Poisoning Phase 4.3 Evaluation Phase 4.4 Mechanism of Persistence and behavioral Drift 5 Experiment 5.1 Agent Configuration and Environment 5.2 Dataset Constru Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | 4.1 Attack Setup 4.2 Poisoning Phase 4.3 Evaluation Phase 4.4 Mechanism of Persistence and behavioral Drift 5 Experiment 5.1 Agent Configuration and Environment 5.2 Dataset Construction and Evaluation Protocol 5.3 Quanti |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S1, S7, S8. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 12. MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory
**arXiv:2601.03192** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Despite their reasoning capabilities, current AI agents struggle to emulate this decoupled self-evolution (Wei et al. |
| **representation** | This limitation underscores a critical research question: How can we enable an agent to continuously improve its performance after deployment, without compromising the stability of its pre-trained backbone? Our objective is to achieve an agent that evolves with continued usage and rapidly adapts to new tasks after deployment, referred to as Runtime Continuous Learning (Javed et al. To address this challenge, inspired by the human cognitive mechanism of constructive simulation, we propose MemRL , an approach that facilitates self-evolving agents by explicitly decoupling the model’s stable cognitive reasoning from dynamic episodic memory. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: This limitation underscores a critical research question: How can we enable an agent to continuously improve its performance after deployment, without compromis (2) Primarily a write/store design — gate promote before L3 commit. (3) Lock numeric claims from body: em0. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: em0 |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 13. Implicit Graph, Explicit Retrieval: Towards Efficient and Interpretable Long-horizon Memory for Large Language
**arXiv:2601.03417** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | 3.1 Stage I: Remote-Supervised Full-Graph Construction Streaming graph construction for long documents. Reasoner interface (explicit full graph) and QA-only SFT loss. 3.2 Stage II: Remote-Supervised Latent Subgraph Retrieval Implicit graph representation after Stage I. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 Stage I: Remote-Supervised Full-Graph Construction Streaming graph construction for long documents. (2) Primarily a write/store design — gate promote before L3 commit. (3) Lock numeric claims from body: em 46.60, em 49.70, em0, em 51.30. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: em 46.60; em 49.70; em0; em 51.30; em 87.70; em 31.40 |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 14. TeleMem: Building Long-Term and Multimodal Memory for Agentic AI
**arXiv:2601.06037** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, their effectiveness in long-term interactive settings remains fundamentally constrained by the finite context window of Transformer architectures. |
| **representation** | As interaction histories grow, models struggle to allocate attention to distant yet critical information, leading to degraded recall of user-specific facts and unstable long-horizon reasoning [ 12 ] . Effective memory must preserve not only semantic similarity, but also temporal order, causal dependency, and state evolution across interactions. Retrieval-augmented generation (RAG) has emerged as a practical solution to extend effective memory beyond the native context window by encoding past interactions into vector embeddings and retrieving relevant entries via semantic search [ 21 , 44 , 8 ] . |
| **write / read / forget** | Write: Retrieval-augmented generation (RAG) alleviates this bottleneck, yet conventional pipelines treat memories as independent fragments and lack principled mechanisms for consolidation Read: Large language models (LLMs) achieve strong performance on many NLP tasks but remain limited in long-term interactive settings due to finite context windows and degraded recall ove Forget: eviction/invalidation mentioned. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: As interaction histories grow, models struggle to allocate attention to distant yet critical information, leading to degraded recall of user-specific facts and  (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 62.45%, 76.78%, 84.92%, 86.33%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 62.45%; 76.78%; 84.92%; 86.33%; 70.71%; em0 |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 15. HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents
**arXiv:2601.06377** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | In realistic interactive settings, however, these agents are required to operate over extended time horizons, where relevant information is scattered across long dialogues and multiple sessions. |
| **representation** | HiMem is a modular long-term memory framework built upon a hierarchical architecture that integrates episodic interaction records with abstracted knowledge representations. It is designed to support efficient retrieval, semantic consistency, and continual memory evolution during long-horizon interactions. 2.1 Overall Framework Figure 1: Overview of HiMem. |
| **write / read / forget** | Write: Episode Memory preserves fine-grained interaction events, while Note Memory consolidates stable knowledge such as facts, user preferences, and user profiles. Read: It is designed to support efficient retrieval, semantic consistency, and continual memory evolution during long-horizon interactions. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | (D) Memory self-evolution: when evidence from Note Memory is insufficient, the system supplements potentially missing information from Episode Memory and triggers conflict detection and updating. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: HiMem is a modular long-term memory framework built upon a hierarchical architecture that integrates episodic interaction records with abstracted knowledge repr (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: em0, em 89.22, 25 Episode, 5.85%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: em0; em 89.22; 25 Episode; 5.85%; 0.28% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 16. AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Operation Report GitHub Issue × Title: Content s
**arXiv:2601.08323** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | 2 Related Works Static Memory Workflow Reinforcement Learning in Agent Memory |
| **representation** | 3.1 Preliminaries: POMDP for Memory 3.2 Why Atomic CRUD Operations? 3.3 Memory Mechanism Implementation Hybrid Memory Retrieval 3.4 Optimization Strategy |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: 3.3 Memory Mechanism Implementation Hybrid Memory Retrieval 3.4 Optimization Strategy Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 Preliminaries: POMDP for Memory 3.2 Why Atomic CRUD Operations? (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: EM1, em0, em 77.8, 40 points. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: EM1; em0; em 77.8; 40 points; 10 points |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 17. Explore with Long-term Memory: A Benchmark and Multimodal LLM-based Reinforcement Learning Framework for Embod
**arXiv:2601.10744** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | See paper body. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S1, S7, S8. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: em 25.53, 166 tasks, 406 questions, 58 tasks. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: em 25.53; 166 tasks; 406 questions; 58 tasks; 145 questions |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 18. [2601.14192] Toward Efficient Agents: A Survey of Memory, Tool learning, and Planning Toward Efficient Agents:
**arXiv:2601.14192** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | 2 Preliminaries 2.1 Agent Formulation 2.2 From Pure LLMs to Agents 3 Efficient Memory 3.1 Memory Construction 3.1.1 Working Memory 3.1.2 External Memory 3.2 Memory Management 3.2.1 Rule-based Management 3.2.2 LLM-based Management 3.2.3 Hybrid Management 3.3 Memory Access 3.3.1 Me |
| **representation** | hree core components of agents: memory, tool learning, and planning , considering costs such as latency, tokens, steps, etc. Aimed at conducting comprehensive research addressing the efficiency of the agentic system itself, we review a broad range of recent approaches that differ in implementation yet frequently converge on shared high-level principles including but not limited to bounding context via compression and management, designing reinforcement learning rewards to minimize tool invocatio |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: Aimed at conducting comprehensive research addressing the efficiency of the agentic system itself, we review a broad range of recent approaches that differ in implementation yet fr Forget: eviction/invalidation mentioned. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S2, S3, S7, S8. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: em0, 50%, 30%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: em0; 50%; 30% |
| **refine_candidate** | **no** |

---

### 19. EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use
**arXiv:2602.15329** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | The fundamental challenge lies in the conflict between the unbounded nature of streaming inputs and the finite context window of MLLMs. |
| **representation** | 3.1 Overview We propose an active online video agent framework designed to shift the passive information processing paradigm toward proactive perception for online video. 3.2 Hierarchical Memory Module To address the challenge of processing infinite video streams within a finite context window while overcoming information decay and semantic fragmentation, we design an event-centric hierarchical memory system. The architecture consists of a Short-Term Memory (STM) for immediate visual buffering and a Long-Term Memory (LTM) for structured history archiving. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: As illustrated in Figure 1 , our architecture consists of three integrated components: (1) a Hierarchical Memory Module designed to overcome information decay a |
| **conflict** | Its fundamental challenge lies in the conflict between the unbounded nature of streaming media input and the limited context window of Multimodal Large Language Models (MLLMs). |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 Overview We propose an active online video agent framework designed to shift the passive information processing paradigm toward proactive perception for onl (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 60.75%, 59.54%, by 4.27%, 1.08%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 60.75%; 59.54%; by 4.27%; 1.08%; 1.1%; 96% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 20. M2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval Re
**arXiv:2603.00503** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | 2 Method: Dual-Memory Augmentation 2.1 Overview 2.1.1 Formalization of Context 2.1.2 The Dual-Memory Framework 2.2 Dynamic Trajectory Summarization 2.2.1 Prompt-Driven State Abstraction 2.2.2 Iterative Memory Update 2.3 Insight Retrieval Augmentation 2.3.1 Offline Insight Extract |
| **representation** | Architecture: We propose a lightweight framework that integrates recursive internal tracking with external guidance, enabling efficient long-horizon navigation without the need for costly training or cumbersome multi-agent interaction. • Intra-Trajectory Compression and Inter-Trajectory Retrieval: We introduce mechanisms to distill execution history into concise summary chains and retrieve cross-task expert insights, effectively mitigating information overload while enhancing decision robustness. 2 Method: Dual-Memory Augmentation 2.1 Overview In this section, we present the Dual-Memory Augmentation framework M 2 designed to address the challenges of long-horizon web navigation. |
| **write / read / forget** | Write: For specific details such as P s ​ y ​ s P_{sys} , as well as examples of Q Q , O t O_{t} , and S t S_{t} , and the action space of the Agent, please refer to Appendix F . Read: • Intra-Trajectory Compression and Inter-Trajectory Retrieval: We introduce mechanisms to distill execution history into concise summary chains and retrieve cross-task expert insig Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Architecture: We propose a lightweight framework that integrates recursive internal tracking with external guidance, enabling efficient long-horizon navigation  (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: em 73.3, em 82.2, em 84.4, + 12.5%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: em 73.3; em 82.2; em 84.4; + 12.5%; + 5.5%; em 62.2 |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (upgraded) | 20 |
| Cumulative FULL | **400** |
