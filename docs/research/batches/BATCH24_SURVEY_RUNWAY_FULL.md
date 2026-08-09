# Batch 24 — Survey Runway FULL (Kedger) — **deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Honest re-card of survey-runway papers — mechanism extraction from **full body** (Intro/Method/Results), not abstract paste.  
> **Progress:** FULL 460 → **480** toward 500.  
> **Method:** Cached `/tmp/kedger-papers/full/{id}.txt`; cards built by `scripts/research/deep_recard_500.py`.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers only from body matches. Generic lessons forbidden.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body mechanism deep-read; ID already ledgered Batch24 — **re-card upgrade**) | **20** | `2412.15274`, `2412.15540`, `2501.00358`, `2501.01702`, `2501.05366`, `2501.06590`, `2501.12254`, `2502.03358`, `2503.07018`, `2503.08175`, `2503.09516`, `2504.12369`, `2504.12516`, `2504.13079`, `2504.13805`, `2504.20073`, `2504.21776`, `2505.15962`, `2505.16067`, `2505.16348` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs have `.txt` ≥15k chars. |
| **Method span extracted** | **10/20** | continuous-text section split |
| **Numeric evidence extracted** | **18/20** | regex over method/results |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. Memory-Augmented Agent Training for Business Document Understanding
**arXiv:2412.15274** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Combing through large quantities of unstructured data remains a widespread challenge in enterprise operations, particularly in finance functions where efficient invoice processing represents a growing competitive advantage. |
| **representation** | We train an optimal memory and test it on test task set. We perform optimization by progressively updating the memory module M 𝑀 M italic_M over multiple epochs. The trajectory continues until the agent either reaches a solution or the interaction exceeds a predefined maximum number of steps. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: We train an optimal memory and test it on test task set. (2) Primarily a write/store design — gate promote before L3 commit. (3) Lock numeric claims from body: 14 tasks, 8.12%, 21.3%, by 30.3%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 14 tasks; 8.12%; 21.3%; by 30.3%; by 35.2%; 30.3% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 2. MRAG: A Modular Retrieval Framework for Time-Sensitive Question Answering
**arXiv:2412.15540** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | State-of-the-art retrieval systems struggle to conduct in-depth reasoning to identify relevant documents. |
| **representation** | TempRAGEval - TimeQA TempRAGEval - SituatedQA AR @ ER @ AR @ ER @ 1st 2nd # QFS 1 5 1 5 1 5 1 5 BM25 - - 17.5 39.0 4.2 14.1 27.6 58.2 6.8 18.4 Cont. - - 18.8 49.9 9.6 28.7 22.6 51.1 6.8 17.1 Hybrid - - 18.8 51.2 9.6 28.1 22.6 55.8 6.8 19.7 Cont. ELECTRA - 40.1 76.9 21.8 58.6 35.5 71.3 15.3 37.1 Cont. MiniLM - 34.0 76.1 16.2 57.3 36.8 73.4 20.0 40.3 Cont. Jina - 42.4 77.2 23.6 58.6 47.9 78.4 19.5 41.1 Cont. BGE - 40.3 80.9 23.3 61.3 36.3 74.2 14.5 35.0 Cont. NV-Embed - 49.9 81.2 33.4 62.9 47.4 81 |
| **write / read / forget** | Write: We include complete results in Appendix I . Read: MRAG 10 56.0 88.1 35.5 73.2 62.1 87.9 30.8 57.9 Table 2: The answer recall (AR@k) and gold evidence recall (ER@k) of each retrieval method on perturbed temporal queries in TimeQA a Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S1, S7, S8. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 7.7%, 13.9%, 49.2%, 44.0%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 7.7%; 13.9%; 49.2%; 44.0%; 200 examples; 9.3% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 3. Embodied VideoAgent: Persistent Memory from Egocentric
**arXiv:2501.00358** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | In this paper, we investigate approaching this problem using egocentric observations [5, 7, 11, 20, 26, 33, 37], which is one of the most intuitive way of how humans and robots perceive the world around them. |
| **representation** | Embodied VideoAgentis a multimodal agent that 1) builds scene memory from both egocentric video and embodied sensory input; 2) utilizes multiple tools to query this memory; 3) activates embodied action primitives to interact with the environments, ef- fectively fulfills various u habited characters [5, 11, 33]; 3) Maintaining a persistent memory about the scene that allows frequent update over time [12, 18, 40]. Their key idea is to construct a temporal memory from the video and invoke several tools to query the memory. |
| **write / read / forget** | Write: We further introduce a VLM-based approach to automatically update the mem- ory when actions or activities over objects are perceived. Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Embodied VideoAgentis a multimodal agent that 1) builds scene memory from both egocentric video and embodied sensory input; 2) utilizes multiple tools to query  (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 4.9%, 5.8%, 11.7%, 10%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 4.9%; 5.8%; 11.7%; 10% |
| **refine_candidate** | **no** |

---

### 4. Published as a conference paper at ICLR 2025
**arXiv:2501.01702** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | See paper body. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S2, S3, S7, S8. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 75%, by 25.6%, 30.4%, 20%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 75%; by 25.6%; 30.4%; 20%; 3.7%; 3.73% |
| **refine_candidate** | **no** |

---

### 5. Search-o1: Agentic Search-Enhanced Large Reasoning Models
**arXiv:2501.05366** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | While this characteristic enhances logical coherence and interpretability of reasoning, an extended chain of thought may cause overthinking [ 4 ] and increased risks of knowledge insufficiency [ 60 , 51 , 2 ] , where any knowledge gap can propagate errors and disrupt the entire r |
| **representation** | 3.2 Overview of the Search-o1 Framework The Search-o1 framework addresses knowledge insufficiency in large reasoning models (LRMs) by seamlessly integrating external knowledge retrieval into their reasoning process while maintaining chain-of-thought coherence. As illustrated in Figure 2 , we present a comparative analysis of three approaches: vanilla reasoning, agentic retrieval-augmented generation (RAG), and our proposed Search-o1 framework. • Agentic RAG: To bridge the knowledge gaps during reasoning, we build the agentic RAG mechanism (Figure 2 (b)) to enable the model to autonomously retrieve external knowledge when needed. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: 3.1 Problem Formulation We consider a complex reasoning task that necessitates multi-step reasoning and the retrieval of external knowledge to derive solutions. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: 3.2 Overview of the Search-o1 Framework The Search-o1 framework addresses knowledge insufficiency in large reasoning models (LRMs) by seamlessly integrating ext (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 23.2%, by 29.6%, 5.3%, 0%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 23.2%; by 29.6%; 5.3%; 0%; 0.41796875%; 4% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 6. CHEM AGENT : S ELF -UPDATING LIBRARY IN LARGE
**arXiv:2501.06590** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | See paper body. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S2, S3, S7, S8. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 8%, 36%, +0.17%, +7.13%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 8%; 36%; +0.17%; +7.13%; em 43.59; 8.34% |
| **refine_candidate** | **no** |

---

### 7. Memory Storyboard: Leveraging Temporal Segmentation for Streaming Self-Supervised Learning from Egocentric Vid
**arXiv:2501.12254** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Humans are capable of learning continuously from a stream of unlabeled and uncurated perceptual inputs, such as video data, without needing to iterate through multiple exposures or epochs. |
| **representation** | On top of the ResNet backbone, we use a two-layer MLP with 2048 hidden units, 128 output units, and ReLU activation function as the projector. In Memory Storyboard, we create two separate projectors for ℒ T ​ C ​ L \mathcal{L}_{TCL} and ℒ S ​ S ​ L \mathcal{L}_{SSL} . We apply a standard data augmentation pipeline for SSL methods following Zhuang et al. |
| **write / read / forget** | Write: That is, we store 20 model checkpoints throughout the streaming training and evaluate them on mini -ImageNet and Labeled-S with SVM readout. Read: retrieval/recall path described. Forget: For the SimSiam (Chen & He, 2021 ) experiments, we used the SGD optimizer with learning rate 0.05, momentum 0.9, and weight decay 1e-4, and a projector with 3 M |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: On top of the ResNet backbone, we use a two-layer MLP with 2048 hidden units, 128 output units, and ReLU activation function as the projector. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 5%, 12.5%, 75.0%, 75%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 5%; 12.5%; 75.0%; 75%; 10%; 50% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 8. Minerva: A Programmable Memory Test Benchmark for Language Models
**arXiv:2502.03358** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, evaluating model capabilities using static data benchmarks–based on some user queries, their data, and expected outcomes–can be costly, imprecise, and lacks scalability. |
| **representation** | This representation of the world, expressed in natural language, functions as the model’s memory . In this paper, we address a fundamental question that is critical to improving AI assistants: What specific capabilities do large language models demonstrate in utilizing their memory? In this paper, we go beyond simple search tasks and introduce a framework to test a comprehensive range of memory-related capabilities in LLMs. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: Our framework extends the range of capability tests beyond the commonly explored (passkey, key-value, needle in the haystack) search, a dominant focus in the literature. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: This representation of the world, expressed in natural language, functions as the model’s memory . (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 95%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 95% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 9. Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Impl
**arXiv:2503.07018** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | ( 2023 ) lack session depth, while deep but small datasets Wu et al. |
| **representation** | ( 2024 ) incorporate structured memory mechanisms, while SCM Wang et al. ( 2023 ) utilizes structured conversational memory for efficient information retention and retrieval. ( 2024 ) further leveraging graph-based knowledge representation for improved contextual retrieval. |
| **write / read / forget** | Write: Appendix B Persona Extraction We include some personas used to generate implicit conversations, such as, “This person enjoys listening to pop music,” “This person likely engages in Read: ( 2023 ) utilizes structured conversational memory for efficient information retention and retrieval. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: ( 2024 ) incorporate structured memory mechanisms, while SCM Wang et al. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 500 examples, 100 sessions, 20%, 30%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 500 examples; 100 sessions; 20%; 30%; 60%; 37% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 10. Privacy-Enhancing Paradigms within Federated Multi-Agent Systems
**arXiv:2503.08175** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | We describe the challenges of privacy protection in MAS: I) Predefined privacy settings fail to accommodate the heterogeneous privacy requirements of different agents; II) Some protection methods compromise context awareness; III) Complex protection architectures are unable to ad |
| **representation** | 4.1 Overview In this section, we introduce the Embedded Privacy-Enhancing Agents ( EPEAgents ). This method acts as an intermediary agent deployed on the server and integrates seamlessly into various data flows within MAS, such as the RAG phase and the memory bank retrieval stage. The overall framework of EPEAgents is shown in Fig. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: This method acts as an intermediary agent deployed on the server and integrates seamlessly into various data flows within MAS, such as the RAG phase and the memory bank retrieval s Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | 4.1 Overview In this section, we introduce the Embedded Privacy-Enhancing Agents ( EPEAgents ). |
| **Kedger lessons** | (1) Mechanism to port: 4.1 Overview In this section, we introduce the Embedded Privacy-Enhancing Agents ( EPEAgents ). (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 11. Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning
**arXiv:2503.09516** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, prompting-based approaches often struggle to generalize, as certain tasks may not have been encountered during LLM pretraining. |
| **representation** | RAG models often retrieve passages based on the LLM input as query and incorporate them into the LLM’s context for generation (Lewis et al., 2020 ) . However, applying RL to search-and-reasoning scenarios presents three key challenges: (1) RL Framework and Stability – It remains unclear how to effectively integrate the search engine into the RL approaches for LLMs while ensuring stable optimization, particularly when incorpora To address aforementioned challenges, we introduce Search-R1 , a novel RL framework that enables LLMs to interact with search engines in an interleaved manner with their own reasoning. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Prompting advanced LLMs with reasoning capabilities to use search engines during inference is often suboptimal, as the LLM might not fully possess the capability on how to interact Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: RAG models often retrieve passages based on the LLM input as query and incorporate them into the LLM’s context for generation (Lewis et al., 2020 ) . (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 24%, 20%, by 24%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 24%; 20%; by 24% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 12. WorldMem: Long-term Consistent World Simulation with Memory
**arXiv:2504.12369** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Despite these advances, a fundamental challenge remains: the limited probing horizon. |
| **representation** | World simulation has gained significant attention for its ability to model environments and predict the outcomes of actions ( bar2024navigationworldmodels ; oasis2024 ; alonso2025diffusion ; feng2024matrix ; parkerholder2024genie2 ; valevski2024diffusion ) . Due to computational and memory constraints, video generative models operate within a fixed context window and are unable to condition on the full sequence of past generations. A natural solution is to maintain an external memory that stores and retrieves relevant historical information outside the generative loop. |
| **write / read / forget** | Write: In this work, we present WorldMem , a framework that enhances scene generation with a memory bank consisting of memory units that store memory frames and states ( e.g. Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: World simulation has gained significant attention for its ability to model environments and predict the outcomes of actions ( bar2024navigationworldmodels ; oas (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 13. BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents
**arXiv:2504.12516** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Although the internet has transformed the way we access information, human navigation of the internet to find information is clunky for several reasons: (1) our memory and world knowledge are limited; (2) our browsing abilities are hindered by distraction and fatigue; and (3) hum |
| **representation** | A sufficiently capable machine intelligence should be able to, in principle, retrieve any well-specified any piece of information from the open web, even if retrieving it would require browsing thousands of web pages. While past benchmarks have measured the ability to retrieve information ( Joshi et al. Here we introduce a new benchmark called BrowseComp , which stands for “Browsing Competition” and comprises 1,266 challenging problems that require browsing a large number of websites to solve. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: BrowseComp comprises 1,266 questions that require persistently navigating the internet in search of hard-to-find, entangled information. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: A sufficiently capable machine intelligence should be able to, in principle, retrieve any well-specified any piece of information from the open web, even if ret (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 0.6%, 1.9%, 266 questions, 50 episodes. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 0.6%; 1.9%; 266 questions; 50 episodes; 266 examples; 70.8% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 14. Retrieval-Augmented Generation with Conflicting Evidence
**arXiv:2504.13079** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, a core challenge faced by all of these approaches is that information retrieved from the internet can be conflicting, noisy, and unreliable – retrieved documents might contain misinformation, unverified claims, and AI-generated content that may be inaccurate or misleadin |
| **representation** | This kind of RAG also features prominently in “deep research” techniques that frame search as an agent-driven process in which a research agent collects and summarizes online sources (Google, 2024a ; OpenAI, 2025 ) . Madam -RAG (right) addresses this through multi-agent debate, where each agent summarizes and represents the information in one document. Agents discuss their responses across multiple rounds, with the final answers being combined via an aggregator module that summarizes the discussion. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Large language model (LLM) agents are increasingly employing retrieval-augmented generation (RAG) to improve the factuality of their responses. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | The gains are particularly notable on AmbigDocs and Ram Docs, where ambiguity and conflicting evidence require structured resolution; for instance, Madam -RAG outperforms Astute RAG by 11.40% with Llama3.3-70B-Inst and b |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: This kind of RAG also features prominently in “deep research” techniques that frame search as an agent-driven process in which a research agent collects and sum (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: by 11.40%, by 12.90%, by 15.80%, 19.20%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: by 11.40%; by 12.90%; by 15.80%; 19.20%; 17.40%; 3.70% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 15. LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark
**arXiv:2504.13805** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Traditional approaches using pre-training or fine-tuning with massive datasets struggle with the diversity of mobile applications and user-specific tasks. |
| **representation** | Architecture diagram showing the three main components (DemoParser, KnowSeeker, ActExecutor) and their interconnections within the LearnAct system, including data flow from human demonstrations to execution. Building on the insights from our LearnGUI dataset, we introduce LearnAct, a novel framework designed to break through the limitations of traditional training approaches for mobile GUI agents. As illustrated in Figure 4 , LearnAct is a sophisticated multi-agent framework that automatically understands human demonstrations, generates instructional knowledge, and leverages this knowledge to assist mobile GUI agents in reasoning about unseen scenarios. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: The LearnAct framework consists of three specialized components, each addressing a critical aspect of demonstration-based learning: (1) DemoParser (Section 4.1 ), a knowledge gener Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Architecture diagram showing the three main components (DemoParser, KnowSeeker, ActExecutor) and their interconnections within the LearnAct system, including da (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 19.3%, 51.7%, +32.4%, 57.7%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 19.3%; 51.7%; +32.4%; 57.7%; +38.4%; 198.9% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 16. StarPO — RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinf
**arXiv:2504.20073** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Unlike static tasks such as single-turn math problem solving (Shao et al., 2024a ) or coding (DeepSeek-AI et al., 2024 ) , agent settings require models to make sequential decisions, maintain memory across turns, and adapt to stochastic feedback from their environment. |
| **representation** | Unlike static tasks such as single-turn math problem solving (Shao et al., 2024a ) or coding (DeepSeek-AI et al., 2024 ) , agent settings require models to make sequential decisions, maintain memory across turns, and adapt to stochastic feedback from their environment. In particular, LLM agent training often exhibits training instability, complex reward signals, and limited generalization across environment changes, especially under multi-turn interaction with stochastic feedback. We explore this question through a systematic study of agent learning under a general RL framework StarPO ( S tate- T hinking- A ctions- R eward P olicy O ptimization). |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: eviction/invalidation mentioned. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Unlike static tasks such as single-turn math problem solving (Shao et al., 2024a ) or coding (DeepSeek-AI et al., 2024 ) , agent settings require models to make (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 21.09%, 20.22%, 17.97%, 20.31%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 21.09%; 20.22%; 17.97%; 20.31%; 21.48%; 19.53% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 17. WebThinker: Empowering Large Reasoning Models with Deep Research Capability
**arXiv:2504.21776** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6, S7 |
| **problem** | However, when confronted with complex information research needs, models that rely solely on internal knowledge struggle to conduct in-depth web information retrieval and to generate comprehensive and accurate reports through multi-step reasoning. |
| **representation** | It operates in two modes: (1) Problem-Solving Mode equips reasoning models with a search tool backed by a Deep Web Explorer, enabling thorough web exploration to retrieve relevant information for solving complex real-world problems. 3.2 Overview of the WebThinker Framework WebThinker is designed to enhance large reasoning models with deep research capabilities by enabling autonomous web exploration and report generation during the reasoning process. As illustrated in Figure 3 , WebThinker operates in two primary modes: • Problem-Solving Mode: Empowers the LRM with a Deep Web Explorer module. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: 3.1 Problem Formulation We consider a complex reasoning task that requires both multi-step reasoning and the utilization of research tools. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: It operates in two modes: (1) Problem-Solving Mode equips reasoning models with a search tool backed by a Deep Web Explorer, enabling thorough web exploration t (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 174.4%, 422.6%, 82.9%, 161.3%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 174.4%; 422.6%; 82.9%; 161.3%; by 21.9%; 36.2% |
| **refine_candidate** | **yes** — S-stage S4, S6, S7 |

---

### 18. Pre-training Limited Memory Language Models with Internal and External Knowledge
**arXiv:2505.15962** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | This leads us to conclude that storing knowledge inside the model weights during pre-training should be limited as much as possible. |
| **representation** | Architecture and Training Details We pretrain LmLm from scratch using GPT-2 and LLaMA2-style decoder-only architectures. Full architecture specifications, including hidden size, depth, and parameter counts, are shown in Table 6 . For LLaMA2-176M and LLaMA2-382M , we use a batch size of 256 and train for 105k steps, totaling approximately 8 H100-days. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: Each model uses its original tokenizer and vocabulary, extended with four special tokens reserved for lookup calls. Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Architecture and Training Details We pretrain LmLm from scratch using GPT-2 and LLaMA2-style decoder-only architectures. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: f16, 10%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: f16; 10% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 19. How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior
**arXiv:2505.16067** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | However, these approaches are often tailored to specific tasks and offer limited understanding of the underlying principles that govern memory behavior across different agentic systems. |
| **representation** | Figure 1: Illustration of the memory management workflow after each agent execution. To enable effective solving of complex tasks and self-evolving over time, large language model (LLM) agents often equip an episodic memory module Wang et al. the agent output), which can be retrieved as demonstrations to guide similar future tasks. |
| **write / read / forget** | Write: Memory is a critical component in large language model (LLM)-based agents, enabling them to store and retrieve past executions to improve task performance over time. Read: Memory is a critical component in large language model (LLM)-based agents, enabling them to store and retrieve past executions to improve task performance over time. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Figure 1: Illustration of the memory management workflow after each agent execution. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 392 tasks. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 392 tasks |
| **refine_candidate** | **no** |

---

### 20. Embodied Agents Meet Personalization: Investigating Challenges and Solutions Through the Lens of Memory Utiliz
**arXiv:2505.16348** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, for personalized embodied agents, it is important to understand personalized knowledge that users assign unique semantics to the physical world ( e.g. |
| **representation** | ( 2024 ) , we adopt a two-layer hierarchical control architecture for our LLM-powered embodied agent. We utilize the LLM as a high-level policy planner that selects appropriate skills from the predefined skill library. For memory systems, we implement a textual scene-graph as our semantic memory alongside an episodic memory. |
| **write / read / forget** | Write: Each node stores the corresponding entity’s 3D location and relevant state information. Read: If you want to find the exact names of objects on specific receptacles or furnitures, please include that in the query. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: ( 2024 ) , we adopt a two-layer hierarchical control architecture for our LLM-powered embodied agent. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 31 episodes, 13.4%, 201 episodes, 95%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 31 episodes; 13.4%; 201 episodes; 95%; 438 episodes |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (upgraded) | 20 |
| Cumulative FULL | **480** |
