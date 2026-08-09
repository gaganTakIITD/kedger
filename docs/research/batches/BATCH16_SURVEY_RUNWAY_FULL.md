# Batch 16 — Survey Runway FULL (Kedger) — **honest deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Body-grounded mechanism cards (Intro/Method/Results) replacing 2026-08-08 abstract-template cards.  
> **Progress:** FULL 300 → **320**.  
> **Method:** Fulltext `/tmp/kedger-papers/full/{id}.txt` + agent deep-read cards.  
> **Kedger stages:** S1–S8  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers from body only.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body deep-read; deep-recard upgrade of Batch16) | **20** | `2508.12630`, `2508.19855`, `2509.10852`, `2511.06179`, `2506.13356`, `2508.10391`, `2510.06664`, `2511.01448`, `2511.17467`, `2601.01885`, `2405.07960`, `2406.00057`, `2409.19401`, `2501.09136`, `2503.05193`, `2505.11942`, `2505.20096`, `2506.03141`, `2507.21428`, `2507.22925` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs cached |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. Semantic Anchoring in Agentic Memory: Leveraging Linguistic Structures for Persistent Conversational Context
**arXiv:2508.12630** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S3, S7 |
| **problem** | Dense-vector RAG for dialogue stores utterances as embeddings that miss syntax, discourse relations, and coreference, so multi-session recall fails under paraphrase and ellipsis. |
| **representation** | Semantic Anchoring: parse each utterance with dependency parse + coreference resolver + discourse tagger; store in hybrid index (FAISS dense vectors + symbolic inverted index keyed by entity IDs/dependency features/discourse tags); fused retrieval score blends dense similarity with symbolic feature match before LLM prompt serialization. |
| **write / read / forget** | Write: parsed linguistic features + embedding into hybrid index per utterance. Read: fused dense+symbolic retrieval into LLM context. Forget: discusses agentic store/update/forget policies but focuses on representation; no dedicated eviction algorithm. |
| **conflict** | Silent on typed SUPERSEDES; UCS Likert marks contradictions as continuity failures only. |
| **privacy** | Silent (eval blinding mentions prompt leakage controls only). |
| **Kedger lessons** | (1) Cognify should emit Anchor facets for entities/coref/discourse, not embedding-only Evidence. (2) S7 hydrate fusion = dense score + symbolic inverted-index keys, not vector-only. (3) Multi-session FR/DC: paper reports >75% recall at 10 sessions and up to ~18% gains over RAG baselines — use as LoCoMo-class SLI targets. (4) Error taxonomy (coref 27%, parse 19%, discourse 15%) → S1 fixture classes for bad linguistic hooks. |
| **metric_impact** | >75% recall at 10-session distance; up to ~18% FR/DC gain over strong RAG baselines; failure mix coref 27% / parse 19% / discourse 15% / other 39%. |
| **refine_candidate** | **yes — S3 linguistic-facet cognify + hybrid symbolic/dense hydrate** |

---

### 2. Youtu-GraphRAG: Vertically Unified Agents for Graph Retrieval-Augmented Complex Reasoning
**arXiv:2508.19855** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | GraphRAG work optimizes construction or retrieval in isolation, so domain shift and noisy open extraction degrade multi-hop reasoning and waste tokens. |
| **representation** | Youtu-GraphRAG vertically unifies: (i) schema-bounded extraction agent with seed entity/relation/attribute types + continuous schema expansion; (ii) dually-perceived community detection → four-level knowledge tree; (iii) agentic retriever with iterative reflection; (iv) AnonyRAG + Anonymity Reversion task to curb parametric knowledge leak. |
| **write / read / forget** | Write: schema-bounded graph extract + community knowledge tree indexing. Read: agentic retriever with reflection over graph. Forget: Silent. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Addresses pretrain knowledge leaking via anonymous dataset / Anonymity Reversion — not ACL/membership privacy for user memory. |
| **Kedger lessons** | (1) S3/S5 graph promote should be schema-bounded, not open IE dump. (2) Dual topology+semantics communities ≈ hierarchical Anchor communities for pack compile. (3) AnonyRAG-style parametric-vs-retrieve split belongs in S8 eval fixtures. (4) Token Pareto: paper claims up to 90.71% token-cost saving with +16.62% accuracy — budget SLI for graph hydrate. |
| **metric_impact** | Up to 90.71% token-cost saving and +16.62% accuracy; top-20 acc e.g. 86.5%/85.5%/53.6% (HotpotQA/2Wiki/MuSiQue, DeepSeek-V3); abstain-mode 81.2%/77.6%/47.5%. |
| **refine_candidate** | **yes — S5 schema-bounded graph promote + anonymous leak eval** |

---

### 3. Pre-Storage Reasoning for Episodic Memory: Shifting Inference Burden to Memory for Personalized Dialogue
**arXiv:2509.10852** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Multi-session conversational memory systems dump synthesis onto response-time reasoning, so quality collapses with smaller models and cross-session evolution is poorly tracked. |
| **representation** | PREMem: (1) extract episodic fragments labeled factual/experiential/subjective; (2) pre-storage reasoning — cluster, temporal-link, apply evolution patterns (extension/accumulation/specification/transformation/connection); (3) inference retrieves pre-reasoned memories instead of raw turns. |
| **write / read / forget** | Write: fragment extract + cross-session reasoned links at construction. Read: retrieve synthesized memories at dialogue time. Forget: explicitly notes absence of memory-decay/forgetting mechanisms; similarity threshold only filters retrieve. |
| **conflict** | Motivates resolving preference contradictions across sessions; no typed SUPERSEDES operator — evolution patterns imply updates. |
| **privacy** | Mentions privacy considerations for retaining user info across sessions; no concrete ACL mechanism. |
| **Kedger lessons** | (1) Move heavy cognify to S3/S4 pre-storage, keep S7 hydrate light — especially for small local models. (2) Typed evolution patterns (transform/extend) are richer than overwrite-only promote. (3) Ablation: removing Step 1 extraction collapses EM (~−50% class drops) — don’t skip fragment typing. (4) Lack of decay → pair with Kedger INVALIDATE/Ebbinghaus-class forget. |
| **metric_impact** | LoCoMo PREMem ~68.0/71.0 in main table; ablation w/o Step 1 drops sharply (e.g., 68→31.2, −51.8%); w/o Step 2 smaller (±0.5% to −5.5%). |
| **refine_candidate** | **yes — S3 pre-storage evolution patterns before promote** |

---

### 4. MemoriesDB: A Temporal-Semantic-Relational Database for Long-Term Agent Memory
**arXiv:2511.06179** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S5, S7 |
| **problem** | Long-term agent memory decoheres when time, meaning, and relation live in separate stores (time-series vs vector vs graph), so identity/coherence over experience fragments. |
| **representation** | MemoriesDB: each memory is a time–semantic–relational vertex (microsecond timestamp + embedding + relations) on PostgreSQL+pgvector; append/commit API; temporal–semantic stack; coherence metric C; background maintenance and local coherence tracking; query blends time, semantic ANN, and graph edges. |
| **write / read / forget** | Write: append-only commit of timestamped memory records + edges. Read: multi-axis query (temporal+semantic+relational). Forget: append-only design explicitly complicates deletion/privacy; no first-class forget API in prototype. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Limitations note append-only complicates deletion and privacy — no GDPR-style erase implemented. |
| **Kedger lessons** | (1) Kedger L3 schema should co-index time, embedding, and graph edges in one record like MemoriesDB. (2) Coherence C as SLI for drift/forgetting detection. (3) Append-only without delete blocks S6 unshare — require tombstones. (4) Background maintenance ≈ async promote/consolidate jobs, not on-turn. |
| **metric_impact** | Prototype performance discussed qualitatively; no clean public QA EM/F1 table extracted — treat as systems paper. |
| **refine_candidate** | **yes — unified temporal-semantic-relational store schema** |

---

### 5. StoryBench: A Dynamic Benchmark for Evaluating Long-Term Memory with Multi Turns
**arXiv:2506.13356** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Existing LTM benchmarks poorly stress knowledge retention and sequential reasoning over branching multi-turn decisions, and lack flexibility across modes. |
| **representation** | StoryBench: interactive-fiction branching narratives; two modes — Immediate Feedback (hint on wrong choice) vs Self Recovery (continue to failure ending; model must revise earlier decisions); metrics for knowledge retention and sequential reasoning (L-ctx, LTM+STM). |
| **write / read / forget** | Write: N/A (benchmark). Read: models must recall earlier story facts/decisions. Forget: Silent. |
| **conflict** | Sequential-reasoning tasks require resolving contradictions from prior decisions; no typed SUPERSEDES API. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Add StoryBench-style Self Recovery fixtures where hydrate must revise prior Anchors after silent failure. (2) Separate SLIs for knowledge retention vs sequential state tracking. (3) Immediate Feedback mode ≈ teacher-forced S8 why debugging. (4) Branching narrative stress-tests WorkingState continuity beyond LoCoMo QA. |
| **metric_impact** | Immediate-feedback overall Acc e.g. GPT-4o 80.98±1.31, Claude 3.5 71.88±1.03, DeepSeek-R1 74.86±1.05; Self Recovery much harder (success counts near 0–2). |
| **refine_candidate** | **yes — S7/S8 Self-Recovery narrative fixtures** |

---

### 6. LeanRAG: Knowledge-Graph-Based Generation with Semantic Aggregation and Hierarchical Retrieval
**arXiv:2508.10391** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7 |
| **problem** | Flat or poorly coordinated hierarchical GraphRAG retrieves redundant/incomplete context, bloating prompts and hurting answer quality. |
| **representation** | LeanRAG: recursive semantic clustering builds aggregated entities/relations bottom-up; retrieval anchors query to fine-grained entities then traverses Lowest-Common-Ancestor (LCA) semantic pathways to gather concise evidence; chunk selection strategy controls textual context. |
| **write / read / forget** | Write: hierarchical KG aggregation (cluster → aggregated entities/relations). Read: LCA-path structured retrieval. Forget: Silent. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S5 graph should store aggregated summary nodes above raw Evidence chunks. (2) LCA-path hydrate beats dumping all neighbors — cut redundancy. (3) Paper: ~46% smaller retrieved context vs baselines with competitive/superior win rates. (4) Keep textual chunks optional (RQ4) — graph path may suffice for some queries. |
| **metric_impact** | ~46% retrieval redundancy reduction; pairwise win rates often 50–80%+ vs GraphRAG/HiRAG; vs NaiveRAG overall wins e.g. 97.3%/60.5%/76.5%/84.0% across domains in reported table. |
| **refine_candidate** | **yes — S7 LCA-path hierarchical graph hydrate** |

---

### 7. ToolMem: Enhancing Multimodal Agents with Learnable Tool Capability Memory
**arXiv:2510.06664** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Multimodal agents cannot learn which generative tools excel/fail at which capabilities, so tool selection among similar tools is weak. |
| **representation** | ToolMem: structured capability memory taxonomy by proficiency; learn/update from experience feedback (human or auto judges); at inference retrieve relevant capability entries into context for tool selection and solution generation; evaluated on GenAI-Bench (image) and BiGGen Bench (text). |
| **write / read / forget** | Write: initialize taxonomy then update capability entries from tool-output feedback (don’t remove known capabilities unless contradicted). Read: retrieve capability memories for current task. Forget: Silent (no capability expiry). |
| **conflict** | Update rule: only revise when new feedback explicitly contradicts prior capability claims — informal contradict handling, not SUPERSEDES graph. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Promote tool-capability Anchors separate from task Evidence. (2) S7 hydrate should inject tool skill cards before tool choice. (3) +21%/ +24% absolute tool-selection gains; 14.8–28.7% better performance prediction vs Generic agent. (4) Contradiction-gated update mirrors promote-vs-INVALIDATE discipline. |
| **metric_impact** | Tool performance prediction: MAE ↓14.8% (text) / ↓28.7% (image) vs Generic; tool selection +21% (GenAI-Bench) / +24% (BiGGen) absolute. |
| **refine_candidate** | **yes — S4 tool-capability memory cards** |

---

### 8. LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning
**arXiv:2511.01448** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Graph agent memories entangle semantics inside heavy nodes/edges, causing redundant storage, unstructured retrieval, and slow updates on long dialogues. |
| **representation** | LiCoMemory + CogniGraph: hierarchical graph where entities/relations are a lightweight semantic indexing layer (not full text warehouse); query processing with hierarchy+temporal-aware integrated rerank; real-time interaction updates. |
| **write / read / forget** | Write: real-time CogniGraph updates (entities/relations as index over dialogue knowledge). Read: hierarchical temporal search + integrated rerank. Forget: cites expire-style ops in related systems; own focus is efficient update/retrieve. |
| **conflict** | Notes inconsistent/fragmented returns from conventional pipelines; no typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Keep S5 graph as index over Evidence blobs, not duplicate full text in every edge. (2) Temporal+hierarchy rerank belongs in S7 pack compile. (3) Up to ~23% accuracy gain with reduced update latency on LoCoMo/LongMemEval. (4) Real-time update path = online cognify, not batch-only sleep. |
| **metric_impact** | Up to ~23% accuracy improvement over second-best reported; latency/token tables vs MemoryBank/MemOS/Mem0/A-Mem on LoCoMo/LongMemEval. |
| **refine_candidate** | **yes — lightweight CogniGraph-style index layer** |

---

### 9. PersonaAgent with GraphRAG: Community-Aware Knowledge Graphs for Personalized LLM
**arXiv:2511.17467** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7 |
| **problem** | Persona agents lack a way to combine individual preference history with collective community patterns for personalized generation. |
| **representation** | PersonaAgent+GraphRAG: heterogeneous KG (interactions, categories, concepts) with GraphRAG community summaries; personalized prompt = user-history summary from KG + community-level patterns from graph community detection. |
| **write / read / forget** | Write: LLM-derived graph index over user docs/interactions + community summaries. Read: GraphRAG retrieval into personalized prompt. Forget: Silent. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S5 should support user-local vs community-shared subgraph tiers. (2) Hydrate packs can mix personal Anchors + community summaries without flattening. (3) LaMP gains: news F1 +11.1%, movie tagging F1 +56.1%, product rating MAE −10.4%. (4) Persona consistency is a prompt-compose concern (S7) not only retrieve recall. |
| **metric_impact** | LaMP-2N Acc/F1 up to 0.804/0.591; LaMP-2M Acc/F1 to 0.653/0.662 (+56.1% F1 vs prior); LaMP-3 MAE 0.241→0.216 (−10.4%). |
| **refine_candidate** | **no** |

---

### 10. Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents
**arXiv:2601.01885** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S4, S7 |
| **problem** | LLM agents treat LTM and STM as separate modules with hand-written policies, lacking a learned unified controller for store/retrieve/update/delete under long-horizon tasks. |
| **representation** | AgeMem: memory ops exposed as tools (Retrieve/Add/Update/Delete/Summary/Filter); three-stage progressive RL; step-wise GRPO for unified LTM+STM management; reward mixes task success with memory-quality signals; context reset between stages to force true memory use. |
| **write / read / forget** | Write: Add/Update via tool actions into LTM; STM is working context. Read: Retrieve/Summary/Filter tools. Forget: Delete tool + learned forgetting/prioritization (paper contrasts with non-adaptive forget heuristics). |
| **conflict** | Update when new info supersedes/refines prior memory — informal supersede in tool semantics; not a typed ConflictSet. |
| **privacy** | Stage resets prevent cross-phase information leakage during RL; not end-user privacy ACL. |
| **Kedger lessons** | (1) Expose Kedger memory ops as tool interface the policy can call. (2) Train/evaluate with forced context reset so agents can’t cheat via residual STM. (3) Unified LTM+STM controller beats LTM-only (+LT gains e.g. +10.6/+14.2/+7.4 reported). (4) AgeMem avg 41.96% (Qwen2.5-7B) / 54.31% (Qwen3-4B) with large relative gains vs no-memory. |
| **metric_impact** | Avg 41.96% (Qwen2.5-7B) and 54.31% (Qwen3-4B); relative gains vs no-memory 49.59% / 23.52%; context tokens reduced vs AgeMem-RAG (~3.1–5.1%). |
| **refine_candidate** | **yes — tool-callable unified LTM/STM policy** |

---

### 11. AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments
**arXiv:2405.07960** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Static medical QA misses sequential clinical decision-making with patient dialogue, exams, and multimodal measurements. |
| **representation** | AgentClinic: simulated clinic with Patient, Doctor, Measurement, and Moderator agents; doctor may use tools (e.g., persistent notebook); multimodal exams; specialties/languages; sequential dialogue until diagnosis. |
| **write / read / forget** | Write: optional notebook tool persists notes across cases. Read: dialogue + measurement results + notes. Forget: notebook contents can be deleted if not maintained — warned in prompts. |
| **conflict** | MedAgents-style conflicting diagnostic opinions in related setups; AgentClinic itself is an eval environment. |
| **privacy** | Warns about data leakage advantages from pretraining on MedQA-like material; simulated PHI not real patient privacy tech. |
| **Kedger lessons** | (1) Hydrate eval must be multi-turn tool environments, not single-shot EM. (2) Persistent notebook ≈ WorkingState discipline — Llama-3 up to 92% relative gain with notebook tool. (3) Bias/specialty/language axes → fixture diversity for S1. (4) Moderator agent pattern useful for S8 eng-judgment harnesses. |
| **metric_impact** | Llama-3 up to 92% relative improvement with notebook tool; USMLE-era references 38.1%→90.2% cited as background; AgentClinic diagnostic accuracy varies widely by backbone/tooling. |
| **refine_candidate** | **no** |

---

### 12. Toward Conversational Agents with Context and Time Sensitive Long-term Memory
**arXiv:2406.00057** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Conversational RAG fails on time/event meta-data queries and ambiguous references that need surrounding dialogue context, which semantic vector search alone mishandles. |
| **representation** | Builds a dataset of time-based, ambiguous, and hybrid meta-data questions over long-form dialogues; models combine semantic retrieval with conversational meta-data (time/speaker/event) and context resolution for ambiguous queries. |
| **write / read / forget** | Write: index dialogue with meta-data fields (time, speaker, etc.). Read: retrieve by content and/or meta-data constraints. Forget: Silent. |
| **conflict** | Dataset construction aims for non-contradictory conversations; no SUPERSEDES mechanism. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Anchor schema must include dialogue meta-data (time/speaker/session), not only text embeds. (2) Ambiguous query resolution needs local context pack, not top-k semantic only. (3) Time-based hydrate filters are first-class S7 operators. (4) Use this dataset class beside LoCoMo for temporal QA SLIs. |
| **metric_impact** | CoTable+Semantic (GPT-3.5) recall e.g. 90.47 / 78.34 / 90.17 / 32.19 / 90.32 / 55.27 across query types in Table 1; meta-semantic classification ablation shown. |
| **refine_candidate** | **yes — meta-data-aware conversational retrieve** |

---

### 13. Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs
**arXiv:2409.19401** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S7 |
| **problem** | Smartphone personal memories are scattered and hard to edit/select for LLM personalization under collection, editability, and selectability constraints. |
| **representation** | EMG-RAG: Editable Memory Graph supporting insert/delete/replace; RL (MDP) selects memories on EMGs for RAG; cold-start and application discussion; deployed into smartphone AI assistant. |
| **write / read / forget** | Write: insert/replace into EMG. Read: RL policy selects memories for RAG. Forget: deletion as first-class editable op on the graph. |
| **conflict** | Data-generation prompts require no logical conflicts among memories; not a runtime SUPERSEDES resolver. |
| **privacy** | Explicit Q3 privacy discussion on cross-user EMG isolation and training data collection. |
| **Kedger lessons** | (1) Personal memory graph needs editable insert/delete/replace, not append-only. (2) RL memory selection ≈ learned S7 pack compile under budget. (3) ~10% improvement over best existing approach on real-world dataset. (4) Cross-user isolation is an Inv-Scope / S6 requirement called out by the paper. |
| **metric_impact** | ~10% improvement over best existing approach; real-device assistant transfer claimed. |
| **refine_candidate** | **yes — editable personal memory graph ops** |

---

### 14. Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG
**arXiv:2501.09136** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Static RAG pipelines fail on dynamic multi-step reasoning, tool use, and adaptive control; the field lacks a taxonomy of agentic RAG patterns. |
| **representation** | Survey taxonomy: single-agent router, multi-agent, hierarchical, corrective, adaptive, graph-based (Agent-G/GeAR), document workflows; workflow patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer). |
| **write / read / forget** | Write/Read/Forget: survey of systems — patterns include iterative retrieve/correct; no single WRF implementation. |
| **conflict** | Discusses conflicting objectives in multi-agent settings at architectural level; Silent on typed SUPERSEDES. |
| **privacy** | Silent (footer noise only). |
| **Kedger lessons** | (1) Prefer corrective/adaptive RAG loops for S7 when first retrieve fails. (2) Orchestrator-workers maps to Kedger multi-tool hydrate. (3) Evaluator-optimizer ≈ S8 verify before commit. (4) Use survey as pattern checklist, not a store design. |
| **metric_impact** | Survey — comparative qualitative tables; no single new SOTA number. |
| **refine_candidate** | **no** |

---

### 15. Memory-augmented Query Reconstruction for LLM-based Knowledge Graph Reasoning
**arXiv:2503.05193** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7, S8 |
| **problem** | KGQA agents mix tool invocation with knowledge reasoning, harming readability and causing hallucinated tool calls. |
| **representation** | MemQ: decouple via memory construction (store question↔query pairs), knowledge reasoning in NL, then memory-augmented query reconstruction to emit tool/SPARQL calls; key-value memory over past successful queries. |
| **write / read / forget** | Write: save successful question–query pairs into memory M. Read: retrieve similar queries to reconstruct tool calls. Forget: Silent. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent (example SPARQL membership relation is KG schema, not privacy). |
| **Kedger lessons** | (1) Separate S8 reasoning trace from tool/query syntax via reconstruct step. (2) Promote successful tool queries as procedural Anchors. (3) KV memory of past queries reduces hallucinated invocations. (4) Applicable to Kedger sqlite/graph query tools. |
| **metric_impact** | KGQA Hits/F1 tables vs ToG/UniKGQA/NSM etc. (e.g., baselines ToG ChatGPT 0.758 Hits class; MemQ improves over tool-confused LLM baselines in §4). |
| **refine_candidate** | **yes — memory-augmented tool-query reconstruction** |

---

### 16. Evaluating LLM Agents as Lifelong Learners (LifelongAgentBench)
**arXiv:2505.11942** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S4, S7 |
| **problem** | LLM agents are evaluated as stateless systems; no unified benchmark measures lifelong accumulation/transfer across sequential tasks while avoiding catastrophic forgetting. |
| **representation** | LifelongAgentBench: six-component harness (model pool, agent, environment, chat-history factory, controller, callbacks); containerized snapshots; tasks stress retention/transfer; analyzes failure of naive experience replay under irrelevant history. |
| **write / read / forget** | Write: experience/chat history across sequential tasks. Read: replay past experience into agent context. Forget: catastrophic forgetting is an evaluated failure mode; not a solved policy. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Uses leakage-prevention methodology when constructing eval data. |
| **Kedger lessons** | (1) Lifelong SLI: retention + transfer, not single-task EM. (2) More past experience can hurt — promote selectively (S4 gate). (3) Deterministic containerized envs for memory regression CI. (4) Catastrophic forgetting fixtures belong in Kedger eval suite. |
| **metric_impact** | Benchmark scale reported with large task pools (hundreds–thousands of instances across environments); key finding: more replay ≠ better. |
| **refine_candidate** | **yes — lifelong retention/transfer SLIs** |

---

### 17. MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning
**arXiv:2505.20096** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | End-to-end RAG struggles with ambiguous information-seeking where planning, evidence extraction, and QA need specialized stages. |
| **representation** | MA-RAG multi-agent pipeline: Planner → Step Definer → Extractor → QA Agents collaborating via CoT; system-level RAG as staged reasoning, not naive concat of passages. |
| **write / read / forget** | Write: none persistent — ephemeral agent messages. Read: retrieve then extract relevant spans per step. Forget: Silent. |
| **conflict** | Case study includes conflicting dates across docs; agents must handle NCWC-style conflicts in reasoning — no typed SUPERSEDES store. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Split hydrate into plan/define/extract/answer agents rather than one-shot compose. (2) Extractor agent ≈ per-Evidence note before answer. (3) SOTA on NQ/HotpotQA/TriviaQA/2Wiki reported vs standalone LLMs and prior RAG. (4) Conflict examples → ConflictSet fixtures even if architecture is soft. |
| **metric_impact** | SimpleQA: MA-RAG (GPT-4o-mini, web) 86.4% vs GPT-4o 40.1%; SOTA open-domain QA tables on NQ/HotpotQA/TriviaQA/2Wiki in §4. |
| **refine_candidate** | **yes — multi-agent staged hydrate** |

---

### 18. Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval
**arXiv:2506.03141** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Interactive long video generation loses scene consistency because models underuse historical frames as memory. |
| **representation** | Context-as-Memory: store historical frames raw; Memory Retrieval selects relevant past frames via camera-trajectory search; condition DiT generation on retrieved context frames (spatial/spatio-temporal/cross-attn blocks). |
| **write / read / forget** | Write: append historical context frames as memory. Read: trajectory-based retrieval of relevant frames for next generation. Forget: Silent (bounded by selection, not explicit erase). |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Working memory can be raw modality buffers, not only text Anchors. (2) Retrieve-by-trajectory/structure beats random past frames. (3) Don’t over-postprocess memory before retrieve. (4) Cross-attn conditioning pattern informs multimodal hydrate. |
| **metric_impact** | Video consistency metrics in §5 (scene-consistency / user studies); qualitative gains vs interactive baselines. |
| **refine_candidate** | **no** |

---

### 19. MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversations
**arXiv:2507.21428** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Fixed context windows fill with accumulated tools/MCP servers across multi-turn sessions, degrading tool use without active short-term tool-memory management. |
| **representation** | MemTool three modes: Autonomous Agent (LLM searches/removes tools via tools), Workflow (deterministic management), Hybrid; evaluated 13+ LLMs on ScaleMCP over 100 consecutive interactions. |
| **write / read / forget** | Write: add tools/MCP servers into working tool context. Read: use currently available tools to answer. Forget: explicit tool-removal actions — core contribution (reasoning models 90–94% removal efficiency over 3-window avg). |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S2 WorkingState must manage tool handles, not only dialogue tokens. (2) Autonomous remove-tool action prevents context bloat. (3) Hybrid mode when small models forget to remove tools. (4) Track tool-removal efficiency SLI (90–94% for strong reasoners). |
| **metric_impact** | Autonomous mode tool-removal efficiency 90–94% (3-window avg) for reasoning LLMs; ScaleMCP multi-turn (100 interactions) across 13+ models. |
| **refine_candidate** | **yes — S2 tool-context eviction ops** |

---

### 20. H-MEM: Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents
**arXiv:2507.22925** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Flat vector or entangled KG memories make long-term dialogue retrieval inefficient and weakly structured for reasoning. |
| **representation** | H-MEM four-level store: Domain → Category → Memory Trace → Episode (bottom holds episodic content + user profile); position-index layer-by-layer search; updates; forgetting strategies inspired by Ebbinghaus curve. |
| **write / read / forget** | Write: structure dialogue into hierarchical layers via analyze-agent prompt. Read: hierarchical positional index search. Forget: Ebbinghaus-inspired decay strategies for long-term retention management. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Explicit user privacy/security concerns for storing long-term dialogue — acknowledged limitation, not a mechanism. |
| **Kedger lessons** | (1) Index layers above episode blobs for efficient S7. (2) Ebbinghaus-style decay is a concrete S4/S6 forget prior. (3) User-profile episode tier vs domain/category indices. (4) Privacy note → seal/unshare requirements when adopting H-MEM shapes. |
| **metric_impact** | Hierarchical H-MEM outperforms flat LCM/RA/MB/MG baselines across LoCoMo-style EM/F1 columns in §4 model-size tables (1.5b–3b+). |
| **refine_candidate** | **yes — hierarchical index + decay forget** |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (honest deep-recard) | 20 |
| Cumulative FULL | **320** |
