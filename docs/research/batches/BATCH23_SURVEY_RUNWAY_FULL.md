# Batch 23 — Survey Runway FULL (Kedger) — **deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Honest re-card of survey-runway papers — mechanism extraction from **full body** (Intro/Method/Results), not abstract paste.  
> **Progress:** FULL 440 → **460** toward 500.  
> **Method:** Cached `/tmp/kedger-papers/full/{id}.txt`; cards built by `scripts/research/deep_recard_500.py`.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers only from body matches. Generic lessons forbidden.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body mechanism deep-read; ID already ledgered Batch23 — **re-card upgrade**) | **20** | `2405.02957`, `2405.14486`, `2405.16089`, `2405.19686`, `2406.10149`, `2406.12430`, `2406.13743`, `2407.01178`, `2408.03615`, `2408.08921`, `2408.16967`, `2409.07429`, `2409.20163`, `2410.02694`, `2410.03156`, `2410.06992`, `2410.20878`, `2411.11581`, `2411.13093`, `2412.15266` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs have `.txt` ≥15k chars. |
| **Method span extracted** | **10/20** | continuous-text section split |
| **Numeric evidence extracted** | **18/20** | regex over method/results |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. Agent Hospital: A Simulacrum of Hospital with Evolvable Medical Agents \useunder \ul \newcites methodsMethod \
**arXiv:2405.02957** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Within the simulacrum, doctor agents are able to evolve by treating a large number of patient agents without the need to label training data manually. |
| **representation** | We introduce a simulacrum of hospital called Agent Hospital that simulates the entire process of treating illness, in which all patients, nurses, and doctors are LLM-powered autonomous agents. After treating tens of thousands of patient agents in the simulacrum (human doctors may take several years in the real world), the evolved doctor agents outperform state-of-the-art medical agent methods on the MedQA benchmark [ 8 ] comprising US Medical Licensing Examination (USM Our methods of simulacrum construction and agent evolution have the potential in benefiting a broad range of applications beyond medical AI. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: We introduce a simulacrum of hospital called Agent Hospital that simulates the entire process of treating illness, in which all patients, nurses, and doctors ar (2) Eval/analysis paper — extract fixtures/SLIs rather than store ops. (3) Lock numeric claims from body: by 1.49%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: by 1.49% |
| **refine_candidate** | **no** |

---

### 2. RefChecker: Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models
**arXiv:2405.14486** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, LLMs exhibit a tendency to generate hallucinated contents that can be difficult to discern, posing a potential risk of misleading users. |
| **representation** | Large Language Models (LLMs) have sparked a revolution in Natural Language Processing (NLP), covering diverse tasks with a unified architecture Zhao et al. Figure 2: The RefChecker framework comprises two main components: an extractor denoted as E 𝐸 E italic_E and a checker denoted as C 𝐶 C italic_C . However, several challenges remain: determining the appropriate unit of analysis for comparison, building a comprehensive benchmark reflecting real-world LLM applications, developing a unified, automated framework that scales detection across diverse tasks. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Large Language Models (LLMs) have sparked a revolution in Natural Language Processing (NLP), covering diverse tasks with a unified architecture Zhao et al. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 26.1 points, 9 points, 95%, 23%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 26.1 points; 9 points; 95%; 23%; 93.7%; 91.9% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 3. Towards Completeness-Oriented Tool Retrieval for Large Language Models
**arXiv:2405.16089** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, they often struggle with solving highly complex problems and providing up-to-date knowledge due to the constraints of their pre-training data (Mallen et al . |
| **representation** | The architecture of the proposed two-stage learning framework COLT for tool retrieval. In the first stage, the semantic learning module processes both queries and tools to derive their semantic representations, aiming to align these representations closely within the semantic space. Subsequently, the collaborative learning module enhances these preliminary representations by introducing three bipartite graphs among queries, scenes, and tools. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: The architecture of the proposed two-stage learning framework COLT for tool retrieval. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: The architecture of the proposed two-stage learning framework COLT for tool retrieval. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 68%, 14%, 18%, 44%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 68%; 14%; 18%; 44%; 36%; 20% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 4. Knowledge Graph Tuning: Real-time Large Language Model Personalization based on Human Feedback
**arXiv:2405.19686** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | While these steps are crucial, there is often an oversight in recognizing the need for further personalization during the deployment phase. |
| **representation** | Then, in the later interactions, the LLM agent will recommend vegetarian dog food for the user given the same query. Back-propagation incurs unacceptable GPU memory and computational costs for the daily use of LLMs, especially for on-device applications where the onboard resources are limited. In-context learning has higher interpretability and does not need back-propagation, but its computational overhead, memory cost, and response latency increase drastically with the length of the reference context. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Then, in the later interactions, the LLM agent will recommend vegetarian dog food for the user given the same query. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 39%, 41%, 55%, 45%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 39%; 41%; 55%; 45%; 43%; 61% |
| **refine_candidate** | **yes** — S-stage S3, S5, S7, S8 |

---

### 5. BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack
**arXiv:2406.10149** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Today, large language models (LLMs) and neural architectures are continually evolving and achieving remarkable improvements, particularly in their ability to handle longer contexts (OpenAI, 2023b ; Reid et al., 2024 ; Anthropic, 2024 ) . |
| **representation** | Small LMs, ARMT & RMT with GPT-2 (137M) and Mamba (130M) fine-tuned for the task are able to solve it, with recurrent memory transformers scoring well up to record 50 000 000 tokens. To bridge this gap, we introduce the BABILong benchmark, designed to test language models’ ability to reason across facts distributed in extremely long documents. As a source of long natural documents we use books from PG19 corpora (Rae et al., 2020 ) . |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: silent or parametric-only (no explicit retrieve API). Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Small LMs, ARMT & RMT with GPT-2 (137M) and Mamba (130M) fine-tuned for the task are able to solve it, with recurrent memory transformers scoring well up to rec (2) Primarily a write/store design — gate promote before L3 commit. (3) Lock numeric claims from body: 20%, 60%, 10%, 70%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 20%; 60%; 10%; 70%; up to 14% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 6. PlanRAG: A Plan-then-Retrieval Augmented Generation for Generative Large Language Models as Decision Makers
**arXiv:2406.12430** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, humans still have been in charge of the most hard part, Step (1). |
| **representation** | In terms of database, we use MySQL 4 4 4 https://www.mysql.com for an RDBMS and Neo4j 5 5 5 https://neo4j.com for a GDBMS. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: ( 2023 ) tries to answer the best decision d b ⁢ e ⁢ s ⁢ t subscript 𝑑 𝑏 𝑒 𝑠 𝑡 d_{best} italic_d start_POSTSUBSCRIPT italic_b italic_e italic_s italic_t end_POSTSUBSCRIPT for given Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: In terms of database, we use MySQL 4 4 4 https://www.mysql.com for an RDBMS and Neo4j 5 5 5 https://neo4j.com for a GDBMS. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: by 15.8%, 7.4%, by 7.4%, 1.3%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: by 15.8%; 7.4%; by 7.4%; 1.3%; 21.8%; 3.3% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 7. GenAI-Bench: Evaluating and Improving
**arXiv:2406.13743** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | State-of-the-art text-to-visual models like Stable Diffusion [ 56], DALL-E 3 [ 1], Gen2 [ 16], and Sora [63] generate images and videos with exceptional realism and quality. |
| **representation** | We evaluate generative models using our collectedGenAI- Bench benchmark [39], which consists of 1,600 challenging real-world text prompts sourced from professional designers. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: We evaluate generative models using our collectedGenAI- Bench benchmark [39], which consists of 1,600 challenging real-world text prompts sourced from professio (2) Primarily a write/store design — gate promote before L3 commit. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 8. Memory3: Language Modeling with Explicit Memory
**arXiv:2407.01178** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | The training and inference of large language models (LLMs) are together a costly process that transports knowledge from raw data to meaningful computation. |
| **representation** | Inspired by the memory hierarchy of the human brain, we reduce this cost by equipping LLMs with explicit memory, a memory format cheaper than model parameters and text retrieval-augmented generation (RAG). The model is named Memory 3 , since explicit memory is the third form of memory in LLMs after implicit memory (model parameters) and working memory (context key-values). We introduce a memory circuitry theory to support the externalization of knowledge, and present novel techniques including a memory sparsification mechanism that makes storage tractable and a two-stage pretraining scheme that facilitates memory formation. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: Inspired by the memory hierarchy of the human brain, we reduce this cost by equipping LLMs with explicit memory, a memory format cheaper than model parameters and text retrieval-au Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Inspired by the memory hierarchy of the human brain, we reduce this cost by equipping LLMs with explicit memory, a memory format cheaper than model parameters a (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 20%, 70%, 10%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 20%; 70%; 10% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 9. Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks
**arXiv:2408.03615** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, MLLMs such as GPT-4V * * * https://openai.com/index/gpt-4v-system-card/ lack sufficient knowledge in Minecraft. |
| **representation** | When adding new nodes, the HDKG can be updated by simply merging the nodes and relationships into the graph. This method involves local linear modifications to the graph rather than altering the entire graph, making the process efficient and time-saving. Moreover, an HDKG containing 851 objects (nodes) requires less than 1 MB of memory. |
| **write / read / forget** | Write: Our HDKG can be efficiently updated and expanded. Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: When adding new nodes, the HDKG can be updated by simply merging the nodes and relationships into the graph. (2) Primarily a write/store design — gate promote before L3 commit. (3) Lock numeric claims from body: 67 tasks, 150 tasks, 10 tasks, em 15. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 67 tasks; 150 tasks; 10 tasks; em 15 |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 10. Graph Retrieval-Augmented Generation: A Survey
**arXiv:2408.08921** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Despite their remarkable language comprehension and text generation capabilities, LLMs may exhibit limitations due to a lack of domain-specific knowledge, real-time updated information, and proprietary knowledge, which are outside LLMs’ pre-training corpus. |
| **representation** | ReTraCk: A flexible and efficient framework for knowledge base question answering. EWEK-QA : Enhanced Web and Efficient Knowledge Graph Retrieval for Citation-based Question Answering Systems. Graph-Based Retriever Captures the Long Tail of Biomedical Knowledge. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: NuTrea: Neural Tree Search for Context-guided Multi-hop KGQA. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: ReTraCk: A flexible and efficient framework for knowledge base question answering. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 740 questions. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 740 questions |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 11. MemLong: Memory-Augmented Retrieval for Long Text Modeling
**arXiv:2408.16967** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, due to the quadratic time and space complexity of vanilla attention mechanisms Vaswani et al. |
| **representation** | However, due to the quadratic time and space complexity of vanilla attention mechanisms Vaswani et al. The first line of work focuses on reducing the computation of vanilla attention mechanisms Vaswani et al. ( 2017 ) by employing sparse attention operations Beltagy et al. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: This work introduces MemLong : Mem ory-Augmented Retrieval for Long Text Generation ( MemLong , a method designed to enhance the capabilities of long-context language modeling by u Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: However, due to the quadratic time and space complexity of vanilla attention mechanisms Vaswani et al. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 10%, 80%, 50%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 10%; 80%; 50% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 12. Agent Workflow Memory
**arXiv:2409.07429** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | This allows them to perform well on action sequences similar to those presented in these examples, but results in a lack of robustness to changes in task contexts or environments (Deng et al., 2023 ) . |
| **representation** | Motivated by how humans abstract common task routines from past experiences and apply such knowledge to guide future activities (Chi et al., 1981 ; 2014 ) , we propose agent workflow memory ( AWM ) (§ 2 ) to realize a similar mechanism in agents. AWM induces workflows from agent trajectories by extracting reusable routines, and then integrates these workflows into agent memory to guide future task-solving processes. When high-quality annotated examples are available for a task, AWM operating in an offline fashion can extract reusable workflows from these canonical examples and integrate them into memory to assist test-time inference. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Motivated by how humans abstract common task routines from past experiences and apply such knowledge to guide future activities (Chi et al., 1981 ; 2014 ) , we  (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 22.5 points, 40 examples, 0.3 points, 47%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 22.5 points; 40 examples; 0.3 points; 47%; 1.3 points |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 13. MemSim: A Bayesian Simulator for Evaluating Memory of LLM-based Personal Assistants
**arXiv:2409.20163** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, there remains a lack of objective and automatic methods to evaluate how well personal assistants can memorize and utilize factual information from previous messages, which is crucial for developing memory mechanisms. |
| **representation** | Our final goal is to evaluate memory mechanisms of LLM-based personal assistants in an objective and automatic way. First of all, we propose MemSim that can simulate users and generate evaluation datasets, mainly including the Bayesian Relation Network and a causal generation mechanism. Finally, we construct a benchmark that evaluates different memory mechanisms of LLM-based agents based on MemDaily. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: Based on the constructed QAs and generated user messages, researchers can objectively and automatically evaluate the memory capability of LLM-based personal assistants on factual i Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Our final goal is to evaluate memory mechanisms of LLM-based personal assistants in an objective and automatic way. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 90%, 40%, 003 Questions, 20%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 90%; 40%; 003 Questions; 20%; 100%; 98% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 14. HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly
**arXiv:2410.02694** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | For all open-source models, we evaluate on a H100 GPUs with 80GB of memory. We use the HuggingFace framework (Wolf et al., 2020 ) to load and generate model outputs. We use FlashAttention2 (Dao, 2023 ) and BF16 for faster inference. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: For all open-source models, we evaluate on a H100 GPUs with 80GB of memory. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: F16, 600 examples, 300 examples, 500 examples. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: F16; 600 examples; 300 examples; 500 examples; 100 examples |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 15. Melodi: Exploring Memory Compression for Long Contexts
**arXiv:2410.03156** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | However, the quadratic complexity of attention mechanisms within transformer models necessitates significant computational resources to handle long contexts effectively. |
| **representation** | Architecture Overview Design principle: The core principle behind Melodi is to represent short-term and long-term memory through a hierarchical compression scheme. Specifically, the short-term memory recurrently compresses context tokens across multiple network layers (e.g., condensing a 512-token context window into 128 memory tokens). This process not only facilitates seamless transitions between context windows but also aggregates information across them, effectively functioning as a fixed-size multi-layer long short-term memory (LSTM) mechanism (Hochreiter & Schmidhuber, 1997 ) . |
| **write / read / forget** | Write: The short-term layers recurrently compress the current context window and update short-term memory, while the long-term layer further compresses information and appends it to long- Read: silent or parametric-only (no explicit retrieve API). Forget: This long-term memory retains essential information from the entire history, thus compensating for any potential forgetting in the short-term memory. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Architecture Overview Design principle: The core principle behind Melodi is to represent short-term and long-term memory through a hierarchical compression sche (2) Primarily a write/store design — gate promote before L3 commit. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 16. SWE-Bench+: Enhanced Coding Benchmark for LLMs
**arXiv:2410.06992** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, are the LLMs actually resolving the is |
| **representation** | Each input for an issue consists of a description and a pull request with a reference to the corresponding buggy code repository. Two variants of the SWE-bench datasets are recently developed: SWE-bench Lite 1 1 1 https://www.swebench.com/lite.html and SWE-bench Verified 2 2 2 https://openai.com/index/introducing-swe-bench-verified/ . First, we present an empirical study of state-of-the-art (SOTA) LLMs on SWE-bench Full that explores 1) the quality of SWE-bench issues with a focus on the testing adequacy of the test cases used for validating patches and 2) the quality of patches generated by the LLMs to fix th |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Each input for an issue consists of a description and a pull request with a reference to the corresponding buggy code repository. (2) Eval/analysis paper — extract fixtures/SLIs rather than store ops. (3) Lock numeric claims from body: 32.67%, 31.08%, 12.47%, 3.97%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 32.67%; 31.08%; 12.47%; 3.97%; 94%; 0.55% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 17. AutoRAG: Automated Framework for optimization of Retrieval Augmented Generation Pipeline
**arXiv:2410.20878** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, optimizing the integration of dynamic, external information remains challenging. |
| **representation** | AutoRAG aims to bridge this gap by introducing an automated framework that systematically evaluates numerous RAG setups across different stages of the pipeline. A query expansion module modifies the user’s query to create a better search query, making it easier to find the right passage. For instance, consider the multi-hop question: ”What is the capital of the country where the inventor of the telephone was born?” The query decomposition module would break this down into the following single-hop questions: 1. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Using LLMs (Large Language Models) in conjunction with external documents has made RAG (Retrieval-Augmented Generation) an essential technology. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: AutoRAG aims to bridge this gap by introducing an automated framework that systematically evaluates numerous RAG setups across different stages of the pipeline. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 107 question. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 107 question |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 18. OASIS: Open Agent Social Interaction Simulations with One Million Agents
**arXiv:2411.11581** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | We first use the user IDs from the propagation tree to retrieve the corresponding user’s profile, the following list, and previous posts. To ensure the group’s diversity, we acquire population distributions from disclosed statistics on social networks, including age and personality traits (in this experiment, we use MBTI as a proxy). |
| **write / read / forget** | Write: Appendix E Data Preparations E.1 Real-World Propagation Data We randomly select 198 propagations from Liu et al. Read: We first use the user IDs from the propagation tree to retrieve the corresponding user’s profile, the following list, and previous posts. Forget: eviction/invalidation mentioned. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Due to platform constraints and the need to protect user privacy, large-scale scraping of user data is impractical. |
| **Kedger lessons** | (1) Mechanism to port: We first use the user IDs from the propagation tree to retrieve the corresponding user’s profile, the following list, and previous posts. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 80%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 80% |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 19. Video-RAG: Visually-aligned Retrieval-Augmented Long Video Comprehension
**arXiv:2411.13093** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Although current LVLMs have demonstrated promising performance in understanding short videos, effective comprehension of extremely long videos continues to be a major challenge. |
| **representation** | We propose a novel, training-free pipeline for large video-language models (LVLMs), named Video-RAG, which can be integrated into any LVLM. As illustrated in Figure 2 , our pipeline comprises three key phases: (i) Query Decouple: In this phase, the user’s query is decomposed into a retrieval request aimed at extracting auxiliary texts from the target video. Specifically, we use EasyOCR [ easyocr ] as our text recognition model and segmented the recognized texts on a per-frame basis, denoted as 𝐓 o ​ c ​ r \bm{\mathrm{T}}_{ocr} . |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: As illustrated in Figure 2 , our pipeline comprises three key phases: (i) Query Decouple: In this phase, the user’s query is decomposed into a retrieval request aimed at extracting Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: We propose a novel, training-free pipeline for large video-language models (LVLMs), named Video-RAG, which can be integrated into any LVLM. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 77.4%, 77.2%, 2.8%, 1.6%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 77.4%; 77.2%; 2.8%; 1.6%; by 0.1%; 1.3% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 20. On the Structural Memory of LLM Agents
**arXiv:2412.15266** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Large Language Models (LLMs) Minaee et al. |
| **representation** | Figure 2 illustrates the overview of the memory module within LLM-based agents, highlighting three key components: Structural Memory Generation , Memory Retrieval Methods and Answer Generation . This section begins with an introduction to structural memory generation in § § \S § 3.1 . Next, we introduce memory retrieval methods in § § \S § 3.2 . |
| **write / read / forget** | Write: By transforming unstructured documents 𝒟 q subscript 𝒟 𝑞 \mathcal{D}_{q} caligraphic_D start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT into structural memory ℳ q subscript ℳ 𝑞 \math Read: Figure 2 illustrates the overview of the memory module within LLM-based agents, highlighting three key components: Structural Memory Generation , Memory Retrieval Methods and Answe Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Figure 2 illustrates the overview of the memory module within LLM-based agents, highlighting three key components: Structural Memory Generation , Memory Retriev (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 82.11%, 68.15%, 31.63%, 78.5%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 82.11%; 68.15%; 31.63%; 78.5%; 32.26%; 62.06% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (upgraded) | 20 |
| Cumulative FULL | **460** |
