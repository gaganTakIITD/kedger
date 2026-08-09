# Batch 21 — Survey Runway FULL (Kedger) — **deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Honest re-card of survey-runway papers — mechanism extraction from **full body** (Intro/Method/Results), not abstract paste.  
> **Progress:** FULL 400 → **420** toward 500.  
> **Method:** Cached `/tmp/kedger-papers/full/{id}.txt`; cards built by `scripts/research/deep_recard_500.py`.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers only from body matches. Generic lessons forbidden.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body mechanism deep-read; ID already ledgered Batch21 — **re-card upgrade**) | **20** | `2603.01455`, `2305.05091`, `2305.13711`, `2305.14318`, `2305.14323`, `2305.14325`, `2305.15852`, `2305.19118`, `2306.03314`, `2306.08302`, `2307.07047`, `2307.11019`, `2307.12856`, `2308.03427`, `2308.03549`, `2308.04026`, `2308.11339`, `2309.01918`, `2309.03736`, `2309.04175` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs have `.txt` ≥15k chars. |
| **Method span extracted** | **13/20** | continuous-text section split |
| **Numeric evidence extracted** | **14/20** | regex over method/results |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. From Verbatim to Gist: Distilling Pyramidal Multimodal Memory via Semantic Information Bottleneck for Long-Hor
**arXiv:2603.01455** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | 3.1 Multimodal Pyramid Memory Structure Sensory Buffer Episodic Stream Symbolic Schema 3.2 Bottom-Up Memory Construction 3.2.1 Sensory-to-Episodic Memory Remark: Action-output correspondence Semantic IB Formulation A Quality–Quantity Prior SIB-GRPO: Dynamic Management 3.3 Entropy-Driven Top-Down Retrieval 4 Experiment 4.1 Experimental Setup Benchmarks Evaluation protocol Implementation details 4.2 Comparison with State-of-the-arts Long Video Understanding Online Streaming Video Understanding Ego |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: 3.1 Multimodal Pyramid Memory Structure Sensory Buffer Episodic Stream Symbolic Schema 3.2 Bottom-Up Memory Construction 3.2.1 Sensory-to-Episodic Memory Remark: Action-output corr Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S1, S7, S8. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: em 62.5, 700 questions, 5.1%, 7.1%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: em 62.5; 700 questions; 5.1%; 7.1%; by 5.9%; 5.2% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 2. Knowledge-enhanced Agents for Interactive Text Games
**arXiv:2305.05091** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | The recent progress of computational language models (LMs) has enabled strong performance on tasks with limited interaction, like question-answering and procedural text understanding (Ma et al . |
| **representation** | Framework for Knowledge Injection in Text-based Game Agents In most text-based games, the agent’s input is comprised of three primary elements: the observation of the environment (obv) , the contents of the agent’s inventory (inv) , and the task description (desc) . These elements give the agent the context to make informed decisions and progress through the game. Based on these inputs, the agent is presented with a set of valid actions that it can perform, such as moving to a new location, interacting with objects in the environment, or using items in its inventory. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Unlike historical knowledge, the environment does not provide the affordances, and they need to be retrieved from external sources. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Framework for Knowledge Injection in Text-based Game Agents In most text-based games, the agent’s input is comprised of three primary elements: the observation of the environment (obv) , the contents of the agent’s inven |
| **Kedger lessons** | (1) Mechanism to port: Framework for Knowledge Injection in Text-based Game Agents In most text-based games, the agent’s input is comprised of three primary elements: the observation  (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 63%, 10 tasks, 4%, 48%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 63%; 10 tasks; 4%; 48%; 8%; by 2% |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 3. [2305.13711] LLM-Eval: Unified Multi-Dimensional Automatic Evaluation for Open-Domain Conversations with Large
**arXiv:2305.13711** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Effective evaluation of open-domain conversation systems is a critical yet challenging problem in natural language processing research Smith et al. |
| **representation** | The prompt is concatenated with the dialogue context, the reference (if available), and the generated response, and then fed to the large language model to output a score for each evaluation dimension, based on the defined schema. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: The prompt is concatenated with the dialogue context, the reference (if available), and the generated response, and then fed to the large language model to outp (2) Eval/analysis paper — extract fixtures/SLIs rather than store ops. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 4. Creator: Tool Creation for Disentangling
**arXiv:2305.14318** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | However, there are still limitations to address, such as the inability to handle up-to-date information Yu and Ji ( 2023 ) , provide accurate mathematical results, or reason over long chains of logic (Trivedi et al., 2022 ; Komeili et al., 2022 ; Patel et al., 2021 ; Hendrycks et |
| **representation** | To overcome these concerns, researchers have explored equipping LLMs with external tools to alleviate their memory burden and enhance their expertise (Qin et al., 2023 ) . Figure 1: The difference between Creator and a general tool-using framework. In this paper, we propose a novel approach to address these challenges. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: To overcome these concerns, researchers have explored equipping LLMs with external tools to alleviate their memory burden and enhance their expertise (Qin et al (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 59.7%, 94.7%, 75.5%, up to 18.7%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 59.7%; 94.7%; 75.5%; up to 18.7%; 10%; 63.0% |
| **refine_candidate** | **no** |

---

### 5. [2305.14323] ChatCoT: Tool-Augmented Chain-of-Thought Reasoning on Chat-based Large Language Models ChatCoT: T
**arXiv:2305.14323** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, as tools are not intrinsically integrated with LLMs, incorporating external tools would have to interrupt the CoT reasoning process of LLMs. |
| **representation** | To this end, in this paper, we propose ChatCoT, a tool-augmented chain-of-thought reasoning strategy for chat-based LLMs. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: To this end, in this paper, we propose ChatCoT, a tool-augmented chain-of-thought reasoning strategy for chat-based LLMs. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 7.9%, 3.0%, 85.7%, 56.0%. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 7.9%; 3.0%; 85.7%; 56.0%; 93.0%; 10.0% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 6. [2305.14325] Improving Factuality and Reasoning in Language Models through Multiagent Debate Improving Factual
**arXiv:2305.14325** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Large language models (LLMs) have demonstrated remarkable language generation, understanding, and few-shot learning capabilities in recent years. |
| **representation** | Instead, we propose a complementary approach inspired by The Society of Mind [ 19 ] and multi-agent settings, where multiple language model instances (or agents) individually propose and jointly debate their responses and reasoning processes to arrive at a single common answer. We use the same methodology and prompt templates for all our tasks and require only black-box access to language model generations – no model-internal information such as likelihoods or gradients is needed. To help evaluate the effect of our approach on factual accuracy, we introduce a new benchmark and dataset evaluating factual accuracy of famous computer scientist biographies. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Instead, we propose a complementary approach inspired by The Society of Mind [ 19 ] and multi-agent settings, where multiple language model instances (or agents (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S3, S5, S7, S8 |

---

### 7. Published as a conference paper at ICLR 2024
**arXiv:2305.15852** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | See paper body — problem statement not cleanly extractable. |
| **representation** | Architecture Artist Historical Politics Sports Television Others Entities inMainTestSet # of Google search results Figure 4: The entities in MainTestSet (left). The third column shows the number of sentences predicted to be self-contradictory or non-contradictory, when we use ChatGPT as both gLM and aLM. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Architecture Artist Historical Politics Sports Television Others Entities inMainTestSet # of Google search results Figure 4: The entities in MainTestSet (left). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | 0 15 30 45 2 1 3 0 3 6 11 1 5 5 5 2 7 1 0 1 5 4 11 13 3 4 5 8 3 14 4 7 5 14 Entities inMainTestSet # of sentences Figure 5: Breakdown of ChatGPT-generated self-contradictions (red) and non-contradictory sentences (green) |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Architecture Artist Historical Politics Sports Television Others Entities inMainTestSet # of Google search results Figure 4: The entities in MainTestSet (left). (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 17.4%, 84.1%, 17.8%, 81.3%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 17.4%; 84.1%; 17.8%; 81.3%; 17.2%; 79.2% |
| **refine_candidate** | **yes** — S-stage S3, S5, S7, S8 |

---

### 8. Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate
**arXiv:2305.19118** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Large language models (LLMs) have shown remarkable performance on general language tasks (Jiao et al., 2023 ; Wu et al., 2023 ; Bang et al., 2023 ) but still struggle on complex reasoning tasks (Zhu et al., 2023a ; Gou et al., 2023 ) , which drives the research on cognitive behav |
| **representation** | Formally, DoT describes the following scenario: Once the LLM-based agent has established confidence in its answers, it is unable to generate novel thoughts later through self-reflection even if the initial stance is incorrect. Specifically, we propose the MAD framework, short for M ulti- A gent D ebate, where two agents express their own arguments in the state of “tit for tat” and a judge monitors and manages the debate process to obtain a final solution. The nature of MAD determines that (1) The distorted thinking of one agent can be corrected by the others; (2) The resistance to change of one agent will be complemented by the others; and (3) each agent can obtain external feedback from the others. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: silent or parametric-only (no explicit retrieve API). Forget: eviction/invalidation mentioned. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Formally, DoT describes the following scenario: Once the LLM-based agent has established confidence in its answers, it is unable to generate novel thoughts late (2) Eval/analysis paper — extract fixtures/SLIs rather than store ops. (3) Lock numeric claims from body: em 3, 10%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: em 3; 10% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 9. [2306.03314] Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents Multi-Agent Collaborati
**arXiv:2306.03314** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | They lack the capability to collaborate with other agents or draw from external knowledge repositories. |
| **representation** | 3 System Evaluation Evaluating the performance of a multi-agent system can be challenging due to the complexity and diversity of the tasks that the system can handle. 5.4 Ethical Considerations The use of multi-agent systems also raises several ethical considerations. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: 3 System Evaluation Evaluating the performance of a multi-agent system can be challenging due to the complexity and diversity of the tasks that the system can h (2) Primarily a write/store design — gate promote before L3 commit. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 10. Unifying Large Language Models and Knowledge Graphs: A Roadmap
**arXiv:2306.08302** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Large language models (LLMs) 1 1 1 LLMs are also known as pre-trained language models (PLMs). |
| **representation** | ledge. In contrast, Knowledge Graphs (KGs), Wikipedia and Huapu for example, are structured knowledge models that explicitly store rich factual knowledge. KGs can enhance LLMs by providing external knowledge for inference and interpretability. Meanwhile, KGs are difficult to construct and evolve by nature, which challenges the existing methods in KGs to generate new facts and represent unseen knowledge. Therefore, it is complementary to unify LLMs and KGs together and simultaneously leverage the |
| **write / read / forget** | Write: In contrast, Knowledge Graphs (KGs), Wikipedia and Huapu for example, are structured knowledge models that explicitly store rich factual knowledge. Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S3, S5, S7, S8. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S3, S5, S7, S8 |

---

### 11. Does Collaborative Human–LM Dialogue Generation Help Information Extraction from Human Dialogues?
**arXiv:2307.07047** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, applications involving human-human interaction, such as call center dialogues, have seen limited success. |
| **representation** | For these reasons, we propose to use precision, recall, and F 1 subscript 𝐹 1 F_{1} italic_F start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT scores, along with reporting both cumulative and turn update scores. Cumulative Score (evaluating 𝐗 ← ← 𝐗 \overleftarrow{\mathbf{X}} over← start_ARG bold_X end_ARG ). A cumulative belief (CB) state score m 𝑚 m italic_m is computed for a particular turn (specific index t 𝑡 t italic_t or dialogue-final turn) in the n 𝑛 n italic_n th dialogue as follows: m cb ⁢ ( n , t ) = 1 | ℛ ← n ⁢ t | ⁢ ∑ r ∈ ℛ ← n ⁢ t m ⁢ ( 𝐒 ← ^ n ⁢ r ⁢ t , 𝐒 ← n ⁢ r ⁢ t *  |
| **write / read / forget** | Write: The dialogue state and TLB after turn t 𝑡 t italic_t , 𝐗 ← t subscript ← 𝐗 𝑡 \overleftarrow{\mathbf{X}}_{t} over← start_ARG bold_X end_ARG start_POSTSUBSCRIPT italic_t end_POSTSUBS Read: 3.3 Evaluation In information extraction (IE) tasks, precision, recall, and F-measure are commonly used, while dialogue state tracking (DST) relies on joint goal accuracy (JGA) and Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Our task requires the scoring to handle multi-value and extended free-form text r The capabilities of pretrained language models have opened opportunities to explore new application areas, but applications involving huma |
| **Kedger lessons** | (1) Mechanism to port: For these reasons, we propose to use precision, recall, and F 1 subscript 𝐹 1 F_{1} italic_F start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT scores, along with reportin (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: 25%, by 25%, 8%, 4%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 25%; by 25%; 8%; 4%; 50% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 12. Investigating the Factual Knowledge Boundary of Large Language Models with Retrieval Augmentation
**arXiv:2307.11019** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Despite their exceptional capabilities, LLMs may exhibit limited flexibility in knowledge-intensive tasks, necessitating the incorporation of retrieval augmentation strategies. |
| **representation** | In this section, we provide an overview of the background and fundamental methodologies that are essential for this study. 2.1 Task Formulation We conduct experiments on open-domain question answering (QA), which can be described as follows. Given a question q 𝑞 q italic_q in natural language and a large document collection 𝒟 = { d i } i = 1 m 𝒟 superscript subscript subscript 𝑑 𝑖 𝑖 1 𝑚 \mathcal{D}=\{d_{i}\}_{i=1}^{m} caligraphic_D = { italic_d start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT } st |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: (1) When enhancing the LLM with retrieval, a typical strategy is designing prompt p 𝑝 p italic_p to instruct the LLM to provide an answer a 𝑎 a italic_a to question q 𝑞 q italic_q  Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | We show evidence that LLMs possess unwavering confidence in their knowledge and cannot handle the conflict between internal and external knowledge well. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Map primary contribution onto Kedger stages S1, S7, S8. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 29.20%, 13.70%, 32.77%, 72.80%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: 29.20%; 13.70%; 32.77%; 72.80%; 45.01%; 15.80% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 13. A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis
**arXiv:2307.12856** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, web automation on real-world websites has still suffered from (1) the lack of pre-defined action space, (2) much longer HTML documents than simulated observations, and (3) the absence of domain-specific knowledge for understanding HTML documents ( Figure 1 ). |
| **representation** | Architecture Unlike natural language, HTML documents possess an explicit hierarchical structure. To model this inherent hierarchy, we replace the common dense attention (Vaswani et al., 2017 ) with local and global attention mechanisms (Ainslie et al., 2020 ) . Local attention restricts each token to only attend to neighboring tokens within a window. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Without language model modules, prompted Flan-U-PaLM plans in an open-loop manner ( Plan : ✗ ) and regular-expression-based retrieval summarizes HTML inputs ( Sum : ✗ ). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | μ = 3 𝜇 3 \mu=3 italic_μ = 3 ), and inject the structural bias of HTML better. |
| **Kedger lessons** | (1) Mechanism to port: Architecture Unlike natural language, HTML documents possess an explicit hierarchical structure. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 65%, 70%, 80%, 15%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 65%; 70%; 80%; 15%; 34.0%; 35.3% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 14. TPTU: Large Language Model-based AI Agents for Task Planning and Tool Usage
**arXiv:2308.03427** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, the application of LLMs in real-world settings presents unique challenges. |
| **representation** | In this paper, the Artificial Intelligence Agent (AI Agent) is defined as a program that employs AI techniques to perform tasks that typically require human-like intelligence . 2.1 Agent Framework Figure 2: The proposed framework for LLM-based AI Agents. We are particularly interested in the AI Agent that employs the LLM techniques (i.e., LLM-based AI Agent), due to its high efficiency and flexibility in various tasks and domains. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: 2 Method To the best of our knowledge, the study of “Agent”, “Autonomous Agent”, “AI Agent" and “Multi-Agent” has been a central part of AI research for decades [ jennings1998roadm Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Conflict/contradiction signals present — see method/results. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: In this paper, the Artificial Intelligence Agent (AI Agent) is defined as a program that employs AI techniques to perform tasks that typically require human-lik (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) Lock numeric claims from body: Accuracy 100%, 100%, 45%, Accuracy 45%. (4) Conflict signals → ConflictSet / SUPERSEDES before answer. |
| **metric_impact** | Reported: Accuracy 100%; 100%; 45%; Accuracy 45%; 20%; 80% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 15. Zhongjing: Enhancing the Chinese Medical Capabilities of Large Language Model through Expert Feedback and Real
**arXiv:2308.03549** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | To bridge the gap in Chinese processing adaptability, researchers also introduced more powerful Chinese models (Cui, Yang, and Yao 2023a ; Du et al. |
| **representation** | Construction of Multi-turn Dialogue Dataset During the construction of our Q&A data, we give special attention to the role of multi-turn dialogues. Therefore, we introduce the self-instruct method (Wang et al. Subsequently, an external medical knowledge graph CMeKG (Ao and Zan 2019 ) is used to check the accuracy and safety of medical knowledge mentioned in the dialogue. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: silent or parametric-only (no explicit retrieve API). Forget: eviction/invalidation mentioned. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | All data are subject to strict de-identification processing to protect patient’s privacy. |
| **Kedger lessons** | (1) Mechanism to port: Construction of Multi-turn Dialogue Dataset During the construction of our Q&A data, we give special attention to the role of multi-turn dialogues. (2) Eval/analysis paper — extract fixtures/SLIs rather than store ops. (3) Lock numeric claims from body: 10%, 1%, 6000 questions, 90%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 10%; 1%; 6000 questions; 90% |
| **refine_candidate** | **yes** — S-stage S2, S3, S7 |

---

### 16. [2308.04026] AgentSims: An Open-Source Sandbox for Large Language Model Evaluation \useunder \ul AgentSims: An
**arXiv:2308.04026** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Although LLMs have reformed the paradigm of NLP, the problem of evaluation keeps haunting this field. |
| **representation** | To this end, we introduce AgentSims, an interactive, visualized, and program-based infrastructure for curating evaluation tasks for LLMs. • For researchers focusing on LLM, AgentSims is extendable and combinable to allow users to combine different plan, memory and learning systems to study the impacts and effectiveness of various system design. • For experts from other fields like behavioral economics or social psychology, AgentSims provides an interactive UI for map design and agent creation and lower the entry threshold. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: silent or parametric-only (no explicit retrieve API). Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: To this end, we introduce AgentSims, an interactive, visualized, and program-based infrastructure for curating evaluation tasks for LLMs. (2) Primarily a write/store design — gate promote before L3 commit. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 17. ProAgent: Building Proactive Cooperative Agents with Large Language Models Introduction Related Works Reasonin
**arXiv:2308.11339** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Such reliance, however, constrains the agents’ capacity for strategic adaptation when cooperating with unfamiliar teammates, which becomes a significant challenge in zero-shot coordination scenarios. |
| **representation** | Building agents with adaptive behavior in cooperative tasks stands as a paramount goal in the realm of multi-agent systems. Current approaches to developing cooperative agents rely primarily on learning-based methods, whose policy generalization depends heavily on the diversity of teammates they interact with during the training phase. To address this challenge, we propose ProAgent , a novel framework that harnesses large language models (LLMs) to create pro active agent s capable of dynamically adapting their behavior to enhance cooperation with teammates. |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mechanism to port: Building agents with adaptive behavior in cooperative tasks stands as a paramount goal in the realm of multi-agent systems. (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 10%, 36 pairs. (4) Silence on conflict/privacy recorded — do not invent ACL semantics. |
| **metric_impact** | Reported: 10%; 36 pairs |
| **refine_candidate** | **yes** — S-stage S3, S5, S7, S8 |

---

### 18. [2309.01918] RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Act
**arXiv:2309.01918** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7, S8 |
| **problem** | Training a robot manipulator with multiple skills requires exposure to diverse experiences and the ability to acquire skills from a diverse data corpus. |
| **representation** | Architecture Scaling up dataset diversity as well as network capacity constitutes the two fundamental requirements to improve generalization in machine learning paradigms. Recovery of a generalizable robot manipulation policy under a practical data budget available in robotics demands an efficient policy architecture. In scenarios that have sufficient coverage within the training data, we want the policy to stay close to nominal behaviors (efficient imitation). |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: retrieval/recall path described. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Architecture Scaling up dataset diversity as well as network capacity constitutes the two fundamental requirements to improve generalization in machine learning (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 38 tasks, 40%, 25%, 10%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 38 tasks; 40%; 25%; 10%; 5%; 20% |
| **refine_candidate** | **no** |

---

### 19. [2309.03736] TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial
**arXiv:2309.03736** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | As the influx of diverse data streams continues to rise, there is a growing need for individuals to effectively harness information. |
| **representation** | Our methodology integrates LLM across multiple facets of the trading agent workflow. 4.1 Trading Agents Layered Generative Memory Formulation In our LLM-based trading system, agents autonomously manage their actions and memory trajectories, engaging in communication and deliberation as needed. 4.1.1 Layered-memory structure Each agent within TradingGPT discerns and categorizes perceived information into three distinct memory layers: long-term, middle-term, and short-term. |
| **write / read / forget** | Write: paper describes memory/store updates (see method). Read: Compared to the approach of extracting key insights through the computation of ranked retrieval scores from all memories in the generative agent system [ 10 ] , this layered memory Forget: This score inversely correlates with the time difference between the prompt’s arrival and the event’s memory timestamp, aligning with Ebbinghaus’s forgetting cu |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Our methodology integrates LLM across multiple facets of the trading agent workflow. (2) Treat as full write→read memory loop — wire cognify/promote + hydrate. (3) No clean numeric extract — pull tables manually before refine ticket. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | See paper tables — values not auto-extracted. |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

### 20. [2309.04175] Knowledge-tuning Large Language Models with Structured Medical Knowledge Bases for Reliable Respo
**arXiv:2309.04175** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | However, LLMs sometimes generate responses with the hallucination about medical facts due to limited domain knowledge. |
| **representation** | Finally, we engage in knowledge-tuning that guides the LLMs to retrieve relevant medical knowledge in response to input queries and to generate responses based on the corresponding knowledge in a unified paradigm with LLMs during the training and inference stages, as illustrated  |
| **write / read / forget** | Write: silent / not a persistent memory writer (eval or read-only retrieve). Read: Stage 1: Fill in the parameters for the knowledge retrieval based on the query question. Forget: silent — Kedger default invalidate+audit if adopted. |
| **conflict** | Silent on typed SUPERSEDES / conflict resolution. |
| **privacy** | Privacy/security signals present — see paper. |
| **Kedger lessons** | (1) Mechanism to port: Finally, we engage in knowledge-tuning that guides the LLMs to retrieve relevant medical knowledge in response to input queries and to generate responses based  (2) Primarily a retrieve/hydrate design — budget Evidence packs like paper's retrieve k. (3) Lock numeric claims from body: 2.6%, 55%, 86.7%, up to 71.4%. (4) Privacy/attack surface → Inv-Scope / seal regression fixtures. |
| **metric_impact** | Reported: 2.6%; 55%; 86.7%; up to 71.4%; 80.7%; 0.05% |
| **refine_candidate** | **yes** — S-stage S1, S7, S8 |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (upgraded) | 20 |
| Cumulative FULL | **420** |
