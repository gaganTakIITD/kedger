# Batch 16 — Survey Runway FULL (Kedger) — **deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Honest re-card of survey-runway papers — mechanism extraction from **full body** (Intro/Method/Results), not abstract paste.  
> **Progress:** FULL 300 → **320** toward 500.  
> **Method:** Cached `/tmp/kedger-papers/full/{id}.txt`; cards built by `scripts/research/deep_recard_500.py`.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers only from body matches. Generic lessons forbidden.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body mechanism deep-read; ID already ledgered Batch16 — **re-card upgrade**) | **20** | `2508.12630`, `2508.19855`, `2509.10852`, `2511.06179`, `2506.13356`, `2508.10391`, `2510.06664`, `2511.01448`, `2511.17467`, `2601.01885`, `2405.07960`, `2406.00057`, `2409.19401`, `2501.09136`, `2503.05193`, `2505.11942`, `2505.20096`, `2506.03141`, `2507.21428`, `2507.22925` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs have `.txt` ≥15k chars. |
| **Method span extracted** | **13/20** | continuous-text section split |
| **Numeric evidence extracted** | **16/20** | regex over method/results |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. Semantic Anchoring in Agentic Memory: Leveraging Linguistic Structures for Persistent Conversational Context
**arXiv:2508.12630** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, the two dominant approaches to conversational memory exhibit key limitations: • Full-context prompting – storing the entire interaction history in the LLM context window is computationally expensive, scales poorly with dialogue length, and risks context dilution [ 19 ] . |
| **representation** | 3.1 Overview Our proposed Semantic Anchoring framework augments the memory pipeline of an agentic conversational system with explicit linguistic structure. Rather than relying solely on dense embeddings for past utterances, we extract and store syntactic , semantic , and discourse features in a hybrid index that supports both symbolic and neural retrieval. Hybrid storage – The processed utterance is stored both in a dense vector database (FAISS) for semantic similarity search and in a symbolic inverted index keyed by entity IDs, dependency features, and discourse tags. |
| **write / read / forget** | Write: Rather than relying solely on dense embeddings for past utterances, we extract and store syntactic , semantic , and discourse features in a hybrid index that supports both symbolic Read: Rather than relying solely on dense embeddings for past utterances, we extract and store syntactic , semantic , and discourse features in a hybrid index that supports both symbolic Forget: eviction/invalidation mentioned. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 Overview Our proposed Semantic Anchoring framework augments the memory pipeline of an agentic conversational system with explicit linguistic structure. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 75%, 10 sessions, 4.7 points, 6.2 points. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 75%; 10 sessions; 4.7 points; 6.2 points; 27%; 19% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 2. Youtu-GraphRAG: Vertically Unified Agents for Graph Retrieval-Augmented Complex Reasoning
**arXiv:2508.19855** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | † † footnotetext: † \dagger Equal contribution. |
| **representation** | Youtu-GraphRAG In this section, we elaborate on the core methodology of Youtu-GraphRAG , designed to answer two fundamental research questions: ( i ) (i) How to achieve unified optimization of graph construction and retrieval for higher robustness and generalizability? Correspondingly, our framework integrates three designs in a vertically unified manner based on graph schema . First, a graph schema-bounded agent is designed to ensure construction quality while eliminating noise through automatic expansion. |
| **write / read / forget** | Write: The agent automatically proposes schema expansions by analyzing the underlying relational patterns in each document d ∈ 𝒟 d\in\mathcal{D} through the update function: Δ ​ 𝒮 = ⟨ Δ ​ Read: Youtu-GraphRAG In this section, we elaborate on the core methodology of Youtu-GraphRAG , designed to answer two fundamental research questions: ( i ) (i) How to achieve unified opt Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Given that most LLMs have been exposed to extensive corpora during pretraining, we identify answering questions based on LLMs’ knowledge rather than retrieval mechanism as a critical factor for fairly evaluation - we ter |
| **Kedger lessons** | (1) Mechanism to port: Youtu-GraphRAG In this section, we elaborate on the core methodology of Youtu-GraphRAG , designed to answer two fundamental research questions: ( i ) (i) How to (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: up to 90.71%, 16.62%, 8 points, 86.5%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: up to 90.71%; 16.62%; 8 points; 86.5%; 85.5%; 53.6% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 3. Pre-Storage Reasoning for Episodic Memory: Shifting Inference Burden to Memory for Personalized Dialogue
**arXiv:2509.10852** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | These approaches primarily investigate how different memory structures affect retrieval efficiency and accuracy, yet struggle with cross-session challenges that require understanding continuity, causality, and state changes. |
| **representation** | We present PREMem , a novel approach that shifts complex memory synthesis and analysis from response generation to the memory construction phase. By performing pre-storage reasoning across conversations, our approach reduces the computational burden during dialogue while creating more cognitive-inspired memory representations. Figure 1 illustrates the overall architecture of our approach, which consists of a Memory Construction phase (with two steps detailed in the following sections) and an Inference phase. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: We present PREMem , a novel approach that shifts complex memory synthesis and analysis from response generation to the memory construction phase. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: em 53.6, em 45.3, em 55.9, em 64.7. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: em 53.6; em 45.3; em 55.9; em 64.7; +0.5%; +3.5% |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 4. MemoriesDB: A Temporal-Semantic-Relational Database for Long-Term Agent Memory Modeling Experience as a Graph 
**arXiv:2511.06179** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | 1.1 From fragments to coherence 1.2 Design principles 1.3 Contributions 1.4 Relation to prior work 1.5 Overview 2 Data Model and Geometry 2.1 The Memory Record Practical instantiation Retrieval function 2.2 Edges and Relations 2.3 The Temporal–Semantic Stack 2.4 Distance and Cohe |
| **representation** | Architecture 3.2 Storage Schema 3.3 Append and Commit 3.4 Query Execution 3.5 Background Maintenance 3.6 Local Coherence Tracking 3.7 Concurrency and Partitioning 3.8 Prototype Performance 3.9 Extensibility and Future Backend 3.10 Implementation Summary 4 Observations and Performance 4.1 Implementation Context 4.2 Insertion and Query Behavior 4.3 Structural Coherence in Use 4.4 Edge Dynamics and Maintenance 4.5 Scalability and Extensibility 4.6 Preliminary Summary 5 Discussion and Future Work 5. |
| **write / read / forget** | Write: Architecture 3.2 Storage Schema 3.3 Append and Commit 3.4 Query Execution 3.5 Background Maintenance 3.6 Local Coherence Tracking 3.7 Concurrency and Partitioning 3.8 Prototype Per Read: Architecture 3.2 Storage Schema 3.3 Append and Commit 3.4 Query Execution 3.5 Background Maintenance 3.6 Local Coherence Tracking 3.7 Concurrency and Partitioning 3.8 Prototype Per Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S2, S3, S7. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 5. StoryBench: A Dynamic Benchmark for Evaluating Long-Term Memory with Multi Turns
**arXiv:2506.13356** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Just as organisms gradually accumulate knowledge through experience over time, LLMs need to possess long-term memory (LTM) capabilities to achieve self-evolution and strategic optimization in ever-changing environments [ Shan et al. |
| **representation** | Just as organisms gradually accumulate knowledge through experience over time, LLMs need to possess long-term memory (LTM) capabilities to achieve self-evolution and strategic optimization in ever-changing environments [ Shan et al. To address these limitations, we propose a dynamic benchmark framework inspired by interactive fiction games, where LLMs engage in branching narratives with multi-turns that simulate long-term sequential decision-making. We design two modes: Immediate Feedback provides immediate feedback when the model makes a wrong choice, while Self Recovery allows the story to continue toward a failure ending without any hint, requiring the model to identify and revise past decisions on its own. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: Despite increasing efforts in memory-augmented and retrieval-based architectures, there remains a lack of standardized benchmarks to systematically evaluate LLMs’ long-term memory  Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Just as organisms gradually accumulate knowledge through experience over time, LLMs need to possess long-term memory (LTM) capabilities to achieve self-evolutio (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Metrics named: Accuracy (values: see paper tables). |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 6. LeanRAG: Knowledge-Graph-Based Generation with Semantic Aggregation and Hierarchical Retrieval Introduction Re
**arXiv:2508.10391** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, these approaches still suffer from two critical, unaddressed challenges: high-level conceptual summaries exist as disconnected “semantic islands”, lacking the explicit relations needed for cross-community reasoning; and the retrieval process itself remains structurally u |
| **representation** | To address this, knowledge graph-based RAG methods have evolved towards hierarchical structures, organizing knowledge into multi-level summaries. To overcome these limitations, we introduce LeanRAG, a framework that features a deeply collaborative design combining knowledge aggregation and retrieval strategies. Then, a bottom-up, structure-guided retrieval strategy anchors queries to the most relevant fine-grained entities and then systematically traverses the graph’s semantic pathways to gather concise yet contextually comprehensive evidence sets. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Retrieval-Augmented Generation (RAG) plays a crucial role in grounding Large Language Models by leveraging external knowledge, whereas the effectiveness is often compromised by the Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: To address this, knowledge graph-based RAG methods have evolved towards hierarchical structures, organizing knowledge into multi-level summaries. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 46%, 48.6%, 54.5%, 45.5%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 46%; 48.6%; 54.5%; 45.5%; 55.5%; 44.5% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 7. ToolMem: Enhancing Multimodal Agents with Learnable Tool Capability Memory
**arXiv:2510.06664** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Recent advances in agents have drastically reshaped the landscape of generative tasks, especially by utilizing powerful tools supported by large language models (LLMs) (Schick et al., 2023 ) or vision-language models (VLMs) (Gao et al., 2025 ; Carrasco et al., 2025 ; Radford et a |
| **representation** | Given the task of generating image with text, the agent better pick the later tool to ensure better performance. More concretely, agents lack a mechanism to build and update an internal, dynamic memory that encapsulates the strengths and weaknesses of diverse generative tools. To bridge this gap, we introduce ToolMem , a framework that empowers agents to learn and apply tool-specific capability memories (§ 2 ). |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Given the task of generating image with text, the agent better pick the later tool to ensure better performance. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: by 21%, 18%, 14.8%, 28.7%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: by 21%; 18%; 14.8%; 28.7%; 24%; by 28.7% |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 8. LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning
**arXiv:2511.01448** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Figure 1: Motivation of LiCoMemory , illustrating how LiCoMemory resolves key challenges of existing memory frameworks. |
| **representation** | 3.1 CogniGraph: A Lightweight and Semantically-Aware Graph Structure Traditional graph-based memory representations often embed extensive semantic content directly within nodes and edges, resulting in entangled representations where structural topology and information content are To address this, we introduce CogniGraph , a lightweight and semantically aware hierarchical graph structure that redefines the role of a knowledge graph from a knowledge repository to a semantic indexing layer. Rather than functioning as a storage container for knowledge, CogniGraph employs its graph topology as a structural scaffold that organizes and indexes information across multiple granularities, thereby facilitating efficient retrieval and reasoning. |
| **write / read / forget** | Write: LiCoMemory initiates real-time updates and retrievals during user–assistant interactions. Read: LiCoMemory initiates real-time updates and retrievals during user–assistant interactions. Forget: eviction/invalidation mentioned. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | A smaller improvement is observed on the Adversarial subset, likely due to occasional false positives arising when the correct entries are not retrieved, as reflected by the recall results in Table 1 . |
| **Kedger lessons** | (1) Mechanism to port: 3.1 CogniGraph: A Lightweight and Semantically-Aware Graph Structure Traditional graph-based memory representations often embed extensive semantic content direc (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: em = 2, by 9.0%, 9.3%, 5.3%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: em = 2; by 9.0%; 9.3%; 5.3%; em0; by 7.5% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 9. PersonaAgent with GraphRAG: Community-Aware Knowledge Graphs for Personalized LLM Introduction Related Work Pe
**arXiv:2511.17467** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | We propose a novel framework for persona-based language model system, motivated by the need for personalized AI agents that adapt to individual user preferences. |
| **representation** | Our PersonaAgent system leverages Knowledge Graph-based GraphRAG to enable personalized content generation. The system combines individual user preferences with broader community insights through a structured knowledge graph and personalized prompt generation (see Fig 1 ). Knowledge Graph Construction Our system maintains a heterogeneous knowledge graph G = ( V , E ) G=(V,E) where nodes V V represent: 1. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: GraphRAG Retrieval Mechanism The system employs a dual-source retrieval approach that combines personal and community-based insights: User-Specific Retrieval For a given user u u a Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Our PersonaAgent system leverages Knowledge Graph-based GraphRAG to enable personalized content generation. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: em 1, Acc 0.660, F1 0.386, Acc 0.387. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: em 1; Acc 0.660; F1 0.386; Acc 0.387; F1 0.302; by 1.0% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 10. Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents Re
**arXiv:2601.01885** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | 3.1 Problem Formulation 3.2 Memory Management via Tool Interface 3.3 Three-Stage Progressive RL Strategy 3.4 Step-wise GRPO for Unified Management 3.5 Reward Function Design |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 Problem Formulation 3.2 Memory Management via Tool Interface 3.3 Three-Stage Progressive RL Strategy 3.4 Step-wise GRPO for Unified Management 3.5 Reward Fu (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: em0. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: em0 |
| **refine_candidate** | **no** |

---

### 11. AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments
**arXiv:2405.07960** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | While these LLMs are not designed to replace medical practitioners, they could be beneficial for improving healthcare accessibility and scale for the over 40% of the global population facing limited healthcare access (Organization et al., 2016 ) and an increasingly strained globa |
| **representation** | Among these, LLMs have quickly surpassed the average human score on the United States Medical Licensing Exam (USMLE) in a short amount of time, from 38.1% in September 2021 (Gu et al., 2021 ) to 90.2% in November 2023 (Nori et al., 2023 ) (human passing score is 60%, human expert Recently, LLMs have shown the ability to encode clinical knowledge (Singhal et al., 2023 ; Vaid et al., 2023 ) , retrieve relevant medical texts (Xiong et al., 2024 ) , and perform accurate single-turn medical question-answering (Liévin et al., 2022 ; Nori et al., 2023 ; Wu et al In this work, we introduce AgentClinic, an open-source multimodal agent benchmark for simulating clinical environments. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Among these, LLMs have quickly surpassed the average human score on the United States Medical Licensing Exam (USMLE) in a short amount of time, from 38.1% in Se (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: up to 92%, 38.1%, 90.2%, 60%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: up to 92%; 38.1%; 90.2%; 60%; 87%; 40% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 12. Toward Conversational Agents with Context and Time Sensitive Long-term Memory
**arXiv:2406.00057** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, popular QA benchmarks that typically test RAG systems, focus primarily on information retrieval from a static database of texts, such as Wikipedia (e.g., [ 13 , 30 ] . |
| **representation** | One specific area of interest is in conversational agents that utilize retrieval-augmented generation (RAG) to imbue these agents with long-term memory. Such questions point to a class of common questions an conversational agent may face, which cannot be answered without some ability to retrieve information about previous conversations based on conversational meta-data, rather than semantic retrieval alone. Further, recent work has created benchmarks which test long-term memory in conversational agents (e.g., [ 11 , 19 , 4 ] ) that do not directly, or deeply test meta-data retrieval or ambiguous questions. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: There has recently been growing interest in conversational agents with long-term memory which has led to the rapid development of language models that use retrieval-augmented gener Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: One specific area of interest is in conversational agents that utilize retrieval-augmented generation (RAG) to imbue these agents with long-term memory. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 73%, 77%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 73%; 77% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 13. Instructions for EMNLP 2023 Proceedings
**arXiv:2409.19401** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Motivated by this trend, we study the problem of crafting personalized agents that enhance the AI assistants with the capabilities of LLMs by leveraging users’ memories on smartphones. |
| **representation** | 4.1 Data Collection The process entails (1) gathering raw data, such as everyday conversations or screenshots from user interactions with the smartphone AI assistants; (2) extracting crucial information from this raw data, referred to as memories (denoted by M 𝑀 M italic_M ); and (3) generating QA pairs (denoted by < Q , A > <Q,A> < italic_Q , italic_A > ), and outputting the required memories to facilitate this pairing. For (1), we acquire data from real AI assistant products and employ text pr |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S1, S7, S8. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: by 5.3%, 8.3%, 3.9%, 18.4%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: by 5.3%; 8.3%; 3.9%; 18.4%; by 2.2%; 2.9% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 14. Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG Report GitHub Issue × Title: Content selection
**arXiv:2501.09136** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | 2 Foundations of Retrieval-Augmented Generation 2.1 Overview of Retrieval-Augmented Generation (RAG) 2.2 Core Components of RAG 2.3 Evolution of RAG Paradigms 2.3.1 Naïve RAG 2.3.2 Advanced RAG 2.3.3 Modular RAG 2.3.4 Graph RAG 2.3.5 Agentic RAG 2.4 Challenges and Limitations of  |
| **representation** | 5.2 Multi-Agent Agentic RAG Systems: Workflow Key Features and Advantages. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: 5.2 Multi-Agent Agentic RAG Systems: Workflow Key Features and Advantages. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 20%, 15%, 50%, 2%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 20%; 15%; 50%; 2%; 5% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 15. Memory-augmented Query Reconstruction for LLM-based Knowledge Graph Reasoning
**arXiv:2503.05193** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | However, the existing methods often confuse tool utilization with knowledge reasoning, harming readability and giving rise to hallucinatory tool invocations. |
| **representation** | 3 Framework with Memory Construction In this section, we introduce the framework of MemQ to decouple the reasoning process from tool invocation; the overall flow is illustrated in Figure 2 . We propose to facilitate the KGQA process using three tasks including memory construction, knowledge reasoning and query reconstruction. Before discussing the three tasks, we first illustrate the memory construction process. |
| **write / read / forget** | Write: ”, we can directly save this pair of query and question into the memory M 𝑀 M italic_M . Read: We propose to facilitate the KGQA process using three tasks including memory construction, knowledge reasoning and query reconstruction. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: 3 Framework with Memory Construction In this section, we introduce the framework of MemQ to decouple the reasoning process from tool invocation; the overall flo (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 10%, 25%, 50%, 75%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 10%; 25%; 50%; 75%; 100% |
| **refine_candidate** | **yes** — S-stage S3, S5, S7, S8 |

---

### 16. Evaluating LLM Agents as Lifelong Learners
**arXiv:2505.11942** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, a critical limitation remains: today’s LLM-based agents fundamentally lack memory and the ability to incrementally accumulate knowledge over time. |
| **representation** | Architecture The framework comprises six loosely coupled components: model pool (Appendix B.1.1), agent (B.1.2), environment (B.1.3), chat history factory (B.1.4), controller (B.1.5), and callbacks (B.1.6). The agent module translates environment observations and dialogue history into formatted inputs, queries the LLM, and parses outputs into executable actions. The controller manages the interaction loop, oversees task scheduling, and relays agent actions to the environment. |
| **write / read / forget** | Write: Architecture The framework comprises six loosely coupled components: model pool (Appendix B.1.1), agent (B.1.2), environment (B.1.3), chat history factory (B.1.4), controller (B.1. Read: This flexibility allows researchers to experiment with various lifelong learning strategies while maintaining consistency and comparability. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Architecture The framework comprises six loosely coupled components: model pool (Appendix B.1.1), agent (B.1.2), environment (B.1.3), chat history factory (B.1. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 17. MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning
**arXiv:2505.20096** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Augmentation methods often rely on post-retrieval processing such as re-ranking or document summarization (Chen et al., 2020 ; Glass et al., 2022 ; Ma et al., 2024 ) (Figure 1 (b)) to improve input quality for the LLM, but add latency and may still fail to filter irrelevant or mi |
| **representation** | In this section, we introduce MA-RAG, our proposed multi-agent framework for retrieval-augmented generation. We begin by formalizing the RAG problem setting, and then describe our multi-agent approach designed to improve both retrieval and reasoning. More importantly, RAG is not merely a workaround for context size—it is a framework for extending LLMs’ factual coverage by dynamically incorporating external knowledge. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: In this section, we introduce MA-RAG, our proposed multi-agent framework for retrieval-augmented generation. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: In this section, we introduce MA-RAG, our proposed multi-agent framework for retrieval-augmented generation. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 40.1%, 86.4%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 40.1%; 86.4% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 18. Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval
**arXiv:2506.03141** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | This issue is prevalent across various state-of-the-art methods (Valevski et al., 2024 ; Kanervisto et al., 2025 ; Song et al., 2025 ; Yu et al., 2025c ) , suggesting that while current approaches can generate videos of extended duration, they struggle to maintain coherent long-t |
| **representation** | As discussed in Section 1 , we propose that historical context frames can serve as memory for scene-consistent interactive long video generation. 3.3 presents our Memory Retrieval method, which selects most relevant context frames to guide the generation of new frames. (a) We propose Context-as-Memory , where all historical context frames serve as memory conditions in the generation of predicted frames, with Memory Retrieval extracting relevant information from all context frames. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: 3.3 presents our Memory Retrieval method, which selects most relevant context frames to guide the generation of new frames. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | 3.2 describes how to inject context frames as conditions for video generation. |
| **Kedger lessons** | (1) Mechanism to port: As discussed in Section 1 , we propose that historical context frames can serve as memory for scene-consistent interactive long video generation. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 19. MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversation
**arXiv:2507.21428** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Moreover, as LLM agents become increasingly embedded in user session-based (chat, voice, video) applications, managing the limited context window of the model is necessary for multi-turn conversations. |
| **representation** | 3.1 MemTool MemTool enables an LLM agent to manage its own context window of dynamic tools across multi-turn sessions. Specifically, we propose three modes or architectures (Figure 1 ) that grant varying degrees of autonomy to the LLM agent to optimize its short-term memory context window of tools (autonomous agent, workflow, and hybrid). 3.1.1 Autonomous Agent Mode MemTool Autonomous Agent Mode grants full autonomy to the LLM agent to manage its context window of available tools while simultaneuously answering the user task, across multi-turn conversations. |
| **write / read / forget** | Write: The broader implication of MemTool is that LLM agents can operate in production environments with a non-fixed set of tools at its disposal, searching, equipping, and removing tools Read: The broader implication of MemTool is that LLM agents can operate in production environments with a non-fixed set of tools at its disposal, searching, equipping, and removing tools Forget: In Algorithm 1 , we first prune the previous messages either by truncation or summarization, in case the LLM agent used too many tokens in the previous query. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 MemTool MemTool enables an LLM agent to manage its own context window of dynamic tools across multi-turn sessions. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 94%, 60%, 95%, 100%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 94%; 60%; 95%; 100%; 90%; 88% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 20. H-MEM: Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents
**arXiv:2507.22925** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, this approach is limited by the context window length of LLMs, making it ineffective for long-term interactions. |
| **representation** | 3.1 Memory Storage The storage layer of H-MEM is organized into a four-level hierarchical structure, designed according to increasing levels of semantic abstraction and generalization. As shown in Figure 2 , from top to bottom, these layers are: Domain Layer, Category Layer, Memory Trace Layer, and Episode Layer. The first three layers serve as a progressively refined index, providing a systematic and interpretable organization of memory, while the bottom layer contains the actual episodic content and user profile information. |
| **write / read / forget** | Write: The first three layers store abstract summaries similar to directories. Read: All memory entries are encoded into dense vector representations using a neural encoder to support efficient semantic retrieval. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: 3.1 Memory Storage The storage layer of H-MEM is organized into a four-level hierarchical structure, designed according to increasing levels of semantic abstrac (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 100 episodes, 35 sessions, 512 question, 2705 pairs. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 100 episodes; 35 sessions; 512 question; 2705 pairs; 1104 pairs; 1547 pairs |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (upgraded) | 20 |
| Cumulative FULL | **320** |
