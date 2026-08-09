# Batch 20 — Survey Runway FULL (Kedger) — **honest deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Body-grounded mechanism cards (Intro/Method/Results) replacing 2026-08-08 abstract-template cards.  
> **Progress:** FULL 380 → **400**.  
> **Method:** Fulltext `/tmp/kedger-papers/full/{id}.txt` + agent deep-read cards.  
> **Kedger stages:** S1–S8  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers from body only.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body deep-read; deep-recard upgrade of Batch20) | **20** | `2510.13363`, `2510.23010`, `2511.01633`, `2511.07800`, `2511.12997`, `2511.17208`, `2511.21678`, `2511.21726`, `2512.02425`, `2512.12360`, `2512.16962`, `2601.03192`, `2601.03417`, `2601.06037`, `2601.06377`, `2601.08323`, `2601.10744`, `2601.14192`, `2602.15329`, `2603.00503` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs cached |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. D-SMART: Enhancing LLM Dialogue Consistency via Dynamic Structured Memory And Reasoning Tree
**arXiv:2510.13363** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S5, S7, S8 |
| **problem** | LLMs suffer factual inconsistency and logical decay in multi-turn dialogue because history is unstructured and static RAG/working-memory still follows a single fixed reasoning path over evolving context. |
| **representation** | **D-SMART** model-agnostic stack: (1) **Dynamic Structured Memory (DSM)** — per-turn KGE pipeline SPRING AMR→OWL graph, WSD enrichment, then prune/merge conflicting triples into dialogue KG; (2) **Reasoning Tree (RT)** traverses DSM for multi-path, constraint-aware reasoning; (3) grounded response from RT leaves. NLI metrics **CS** / **DER** for entailment consistency. Eval on filtered hard subset of MT-Bench-101 (25% after complexity curation). |
| **write / read / forget** | Write: each turn asserts new OWL triples into DSM. Read: RT traverses DSM for response. Forget: Graph Pruning removes triples contradicted/superseded by 𝒢'_t before merge. |
| **conflict** | Core: DSM prune/merge resolves conflicting triples in real-time as new entities arrive; dialogue case studies highlight contradictory context turns. |
| **privacy** | Silent on membership/ACL (ethics boilerplate on AI privacy only — not a mechanism). |
| **Kedger lessons** | (1) Promote dialogue turns into a typed Anchor/OWL graph — not raw chat blobs — so WorkingState can prune SUPERSEDES losers. (2) Reasoning Tree over structured memory ≈ S8 why path with branching, not single CoT string. (3) Paper: **~48%** DER consistency lift (open+proprietary) and up to **~10.1%** quality on open models — track DER/CS as hydrate consistency SLIs. (4) New-entity introduction rate stress-tests conflict-aware promote; use similar fixture for multi-turn Anchor updates. |
| **metric_impact** | Dialogue consistency DER/CS; GPT quality score; ablations on DSM+RT vs RAG/working-memory baselines on hard MT-Bench-101 subset. |
| **refine_candidate** | **yes** — S3/S5 dialogue OWL DSM + conflict prune before hydrate |

---

### 2. TALM: Dynamic Tree-Structured Multi-Agent Framework with Long-Term Memory for Scalable Code Generation
**arXiv:2510.23010** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Multi-agent code generation uses rigid workflows; recovering from local errors forces costly full re-reasoning and weak reuse of prior successful patterns. |
| **representation** | **TALM**: extensible **tree of agents** with parent–child divide-and-conquer task decomposition; localized subtree re-reasoning replaces only failed subtrees (discard prior subtree results). **Long-term memory** module semantically queries/integrates prior successful experiences for implicit self-improvement across tasks. Eval HumanEval / BigCodeBench / ClassEval with GPT-4o(-mini). |
| **write / read / forget** | Write: store successful subtree/task experiences in LTM. Read: semantic query of LTM during generation. Forget: on re-reason, discard previous subtree rooted at failing node and regenerate children. |
| **conflict** | Silent on typed SUPERSEDES; error correction is structural (replace subtree), not belief conflict. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Map failed hydrate/plan branches to **localized subtree redo**, not full session restart — mirrors Kedger scoped invalidate. (2) Persist successful code/plan subtrees as reusable Anchors in LTM with semantic recall. (3) Ablation: TALM with memory beats without on ClassEval (e.g. GPT-4o-mini class-level **36→38%**; testcase **~77.9→80.7%** per Table 1 highlights). (4) Parent–child agent tree is a concrete S5 graph for planning, not flat multi-agent chat. |
| **metric_impact** | Pass rates on HumanEval/BigCodeBench/ClassEval (testcase & class); token cost vs MapCoder/Reflexion; with vs without memory. |
| **refine_candidate** | **yes** — S5 tree-local re-reason + LTM of successful plan subtrees |

---

### 3. Scaling Graph Chain-of-Thought Reasoning: A Multi-Agent Framework with Efficient LLM Serving
**arXiv:2511.01633** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Single-agent Graph-CoT is inaccurate, token-heavy, high-latency: monolithic prompts, repeated re-encoding, naive serving. |
| **representation** | **GLM**: multi-agent Graph-CoT — specialized agents for classification / reasoning / action / graph retrieval with branching and selective context sharing. **Serving**: Graph-CoT-aware KV-cache, priority-based eviction, pipelined execution; Action Agent can emit executable Python over graph APIs to collapse multi-round retrieve into one program. |
| **write / read / forget** | Write: notebook/facts updated from graph tool/code execution. Read: graph retrieval + selective agent context. Forget: priority-based KV-cache eviction tailored to Graph-CoT access patterns. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Split Graph-CoT into typed agents with **selective context share** — don't dump full graph into every hydrate turn. (2) Prefer code-synthesis over graph API to batch multi-hop expands (PropRAG-like budget cut). (3) Body: up to **38%** accuracy gain vs Graph-CoT; up to **95.7%** token cut vs Graph-CoT ranges; thought agent ~**82.3%** of tokens. (4) Priority KV eviction is a concrete S2 WorkingState pressure policy for graph walks. |
| **metric_impact** | Graph QA accuracy vs Base/Text-RAG/Graph-RAG/Graph-CoT; tokens/latency/throughput under serving ablations. |
| **refine_candidate** | **yes** — S5/S7 multi-agent Graph-CoT + code-batch retrieve |

---

### 4. From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory
**arXiv:2511.07800** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S5, S7 |
| **problem** | Agents either bake experience into weights (catastrophic forgetting, opaque) or prompt raw trajectories (non-adaptive); need trainable, interpretable strategy memory. |
| **representation** | Three-layer heterogeneous graph: **Query → Transition paths (FSM abstractions) → Meta-cognition** strategies. RL estimates utility of each meta-cognition via counterfactual rewards; inject **top-k** strategies into RL training. Operations create/update/skip metacognition with quantity thresholds (e.g. prefer update when >30). |
| **write / read / forget** | Write: distill trajectories into path+meta-cognition nodes; update weights from rewards. Read: retrieve top-k strategies to condition policy. Forget: silent beyond preferring update/skip when evidence weak — no tombstone API. |
| **conflict** | Silent on SUPERSEDES; strategies may accumulate without explicit conflict merge. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Cognify raw traces → FSM paths → **meta-cognition Anchors** before promote — don't store only trajectories. (2) Utility-weighted strategy retrieve for hydrate (not pure embedding similarity). (3) Reported gains e.g. **↑9.3%** / **↑25.8%** vs ITR baselines on their tables — use strategy-utility ablation SLI. (4) Cap strategy bank with create/update/skip rules akin to promote gates. |
| **metric_impact** | Downstream task scores vs EXPEL/A-MEM/CoT; cross-task generalization; strategy-count ablations. |
| **refine_candidate** | **yes** — S3/S4 trainable meta-cognition graph with utility weighting |

---

### 5. WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance
**arXiv:2511.12997** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Web agents repeat errors across sessions; no persistent cross-session learning without retraining. |
| **representation** | **WebCoach** plug-in: (1) **WebCondenser** — ≤8B LLM summarizes step logs → summary_text + 1536-d embed + success/fail modes; (2) **EMS** episodic store of completed trajectories; (3) **Coach** retrieves by similarity+recency and injects guidance into actor. Model-agnostic; no actor internals change. Leakage control: exclude same WebVoyager task ID. |
| **write / read / forget** | Write: only completed trajectories into EMS after condensation. Read: Coach similarity+recency retrieve → inject. Forget: silent (no eviction policy stated). |
| **conflict** | Silent. |
| **privacy** | Explicit **same-task leakage control** in retrieval; not differential privacy. |
| **Kedger lessons** | (1) Cross-session web/tool memory should be a **coach layer** over condensed episodes, not raw DOM traces in WorkingState. (2) Gate writes to completed episodes with fail_modes/success_workflows schemas. (3) Skywork-38B **47.3→61.4%** (+14.4 pts); Qwen-VL-32B **49.5→57.1%**; eval walltime **~83%** reduction claimed. (4) Always exclude same-task IDs when hydrating training-like memory (Inv-Scope for eval integrity). |
| **metric_impact** | WebVoyager-style success rate & steps across LLM backbones; with/without Coach; leakage-controlled retrieve. |
| **refine_candidate** | **yes** — S7 cross-session Coach inject for tool/web actors |

---

### 6. A Simple Yet Strong Baseline for Long-Term Conversational Memory of LLM Agents
**arXiv:2511.17208** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Long-term chat memory either coarsely retrieves large chunks or fragments into triples/lossy summaries; need non-compressive, event-complete units. |
| **representation** | Neo-Davidsonian **EDU event propositions** (who/what/where/when/why) extracted per session; heterogeneous graph of sessions–EDUs–arguments. **EMem-G**: dense retrieve → LLM relevance filter → PPR graph expand; **EMem**: dense+filter only. Explicitly avoids lossy compression. |
| **write / read / forget** | Write: offline index EDUs+args graph. Read: dense+filter(+PPR). Forget: deliberately **does not** forget/compress — retains information accessibly. |
| **conflict** | Silent. |
| **privacy** | Excludes adversarial LoCoMo questions per prior practice — eval hygiene, not privacy mechanism. |
| **Kedger lessons** | (1) Prefer event-complete EDU Anchors over relation-triple spray for conversational promote. (2) Two-stage retrieve+LLM filter before PPR expand matches Kedger hydrate budget discipline. (3) LoCoMo category table shows large lifts on temporal/multi-session vs weak single-session-preference (e.g. preference stays ~32% while multi-session rises into **70%+** range for strong variants — use category SLIs). (4) Non-compressive memory + query-time relevance is a viable alternative to SeCom-style lossy packs when auditability matters. |
| **metric_impact** | LoCoMo category accuracies (preference/assistant/temporal/multi-session/knowledge); token budgets of retrieved memory. |
| **refine_candidate** | **yes** — S3 EDU event graph + filter-then-PPR hydrate |

---

### 7. Agentic Learner with Grow-and-Refine Multimodal Semantic Memory
**arXiv:2511.21678** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7 |
| **problem** | Multimodal agents solve each problem de novo; trajectory memories suffer brevity bias and store only text, missing joint visual–logical error structure. |
| **representation** | **ViLoMem** dual-stream memory: **logical** guidelines (LLM error attribution) + **visual** distraction patterns (MLLM) with schema merge/create. Closed **Memory Cycle**: retrieve both streams → solve → verify → update. Visual retrieve: image-embed then question-conditioned rerank; logical: problem-analysis + text similarity. |
| **write / read / forget** | Write: selective update only on verified error trajectories (merge/create schemas). Read: dual-stream specialized retrieve. Forget: merge consolidates similar schemas; regressions analyzed when generic visual memory or empty retrieve hurts. |
| **conflict** | Notes cross-benchmark memory conflicts (e.g. MathVista vs HallusionBench utilization gaps); not a typed ConflictSet. |
| **privacy** | Silent (footer only). |
| **Kedger lessons** | (1) Split multimodal error memory into **visual vs logical streams** with different retrieve strategies. (2) Write only verifier-passed failures — don't promote every trajectory. (3) Net **+8.86%** over baseline; visual cases **59–93%** of stores; selective update cuts retrieve latency **~63.1%** and storage **~66.8%**; **66** regressions (33.3% generic visual / 66.7% empty retrieve). (4) Track regression causes as hydrate SLI, not accuracy alone. |
| **metric_impact** | Accuracy on MathVista/MathVision/MathVerse/HallusionBench etc.; ablation of streams; latency/storage of memory pool. |
| **refine_candidate** | **yes** — S3 dual-stream multimodal error memory cycle |

---

### 8. Goal-Directed Search Outperforms Goal-Agnostic Memory Compression in Long-Context Agents
**arXiv:2511.21726** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | Goal-agnostic CRUD compression injects human bias and discards details needed by unknown future queries; compression is lossy across distributions. |
| **representation** | **SUMER**: store **uncompressed** conversation messages in memory bank; RLVR/GRPO trains agent to multi-turn use `search_memory` (semantic+keyword) then `submit_answer`. No hand-crafted compress/CRUD. Trained on LoCoMo (omit adversarial). |
| **write / read / forget** | Write: preprocess embeds raw messages into bank. Read: learned multi-turn search tools. Forget: explicitly rejects goal-agnostic Delete/compress at write time. |
| **conflict** | Prompt guidance: if memories contradict, prefer most recent — soft heuristic only. |
| **privacy** | Adversarial LoCoMo category excluded for lack of labels — not a privacy mechanism. |
| **Kedger lessons** | (1) For long chat hydrate, invest in **learned search policy** over aggressive L2 compression when queries are unpredictable. (2) Dual semantic+keyword tools beat single-channel search under RL. (3) SUMER J **48.55→66.79** (+18.24, **+37.56%** rel); F1 **+73.32%** rel after GRPO. (4) Treat compression as optional, query-conditioned — default keep raw Evidence with pointer. |
| **metric_impact** | LoCoMo F1/B1/J overall and per question type; tool ablations (no semantic/keyword/context). |
| **refine_candidate** | **yes** — S7 RL search-over-raw-memory vs compress-first packs |

---

### 9. WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning
**arXiv:2512.02425** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S5, S7 |
| **problem** | Long video agents rely on text summaries and fixed temporal scales, losing visual evidence and missing variable-duration events. |
| **representation** | **WorldMM** multimodal multi-scale memory: **episodic** (multi-timescale event graphs), **semantic** (consolidated knowledge), **visual** (dual-mode retrieve). Adaptive multi-turn retrieval agent chooses memories/scales. Semantic consolidation merges overlapping/conflicting triplets via LLM. |
| **write / read / forget** | Write: build episodic graphs + consolidate semantic triplets + index visual. Read: adaptive multi-turn retrieve across three memories. Forget: consolidation drops outdated/conflicting triplets. |
| **conflict** | Embedding overlap then LLM decides outdated/conflicting triplets during semantic consolidation. |
| **privacy** | Paper warns continuous structured video knowledge raises privacy/security — recommends access controls (no attack eval). |
| **Kedger lessons** | (1) Long-video/session packs need **three complementary memories** (event graph / semantic / visual pointers), not text gists alone. (2) Adaptive finish of retrieve iterations beats fixed-k hydrate. (3) Avg **~8.4%** gains reported vs baselines; ablations: fixed timescale **−6.1%**, no graphs **−4.4%**, no semantic consolidation **~−7%** long-term, no dual visual **~−3%**; 5-step vs 1-step **+9.3%** on EgoLifeQA. (4) Conflict-aware triplet consolidation is a concrete SUPERSEDES path for multimodal Anchors. |
| **metric_impact** | Long-video QA (EgoLifeQA/Ego-R1/HippoVlog/LVBench/Video-MME); memory-module and step ablations; latency. |
| **refine_candidate** | **yes** — S7 multimodal multi-scale adaptive retrieve + conflict consolidate |

---

### 10. VideoARM: Agentic Reasoning over Hierarchical Memory for Long-Form Video
**arXiv:2512.12360** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Long-form video understanding either uses brittle hand pipelines or exhaustive token-heavy preprocessing before MLLM reasoning. |
| **representation** | **VideoARM**: observe–think–act–memorize loop. **HM³** hierarchical multimodal memory (sensory→… tiers). Controller schedules multimodal tools (scene snapper, clip analyzer, etc.) coarse-to-fine over dynamically built memory; discards static exhaustive preprocess. |
| **write / read / forget** | Write: continuous query-aware clues into HM³ during acting. Read: controller retrieves/inspects hierarchical memory via tools. Forget: discards exhaustive preprocess paradigm; step budget limits memory growth. |
| **conflict** | Silent. |
| **privacy** | Silent (footer only). |
| **Kedger lessons** | (1) Build video/session memory **on-the-fly during agent loop**, not offline full ingest. (2) Hierarchy sensory→semantic is L0/L2 pointer design for hydrate expand. (3) Ablations: best multimodal toolset **80.0%**; weak controllers drop to **54.9%/40.5%** — controller quality dominates memory. (4) Step-budget SLI couples token efficiency with answer quality. |
| **metric_impact** | Long-video benchmarks + ablations (model/tools/HM³/step budget/sampling); token efficiency analysis. |
| **refine_candidate** | **no** — (WorldMM/GraphReader tickets cover hierarchical video memory) |

---

### 11. MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience Retrieval
**arXiv:2512.16962** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | Agents trust retrieved 'successful' past experiences; this trust boundary enables persistent compromise beyond transient prompt injection. |
| **representation** | **MemoryGraft** two-phase attack: poison long-term experience store with malicious-but-plausible successful trajectories; later tasks retrieve them via FAISS∪BM25 and **semantic imitation** replicates attacker patterns. Demonstrated on MetaGPT DataInterpreter + GPT-4o. |
| **write / read / forget** | Attacker writes poisoned success records into ℳ; victim reads via hybrid retrieve; Verify may discard if storage medium check fails (limited defense). |
| **conflict** | Integrity attack on experience memory — not factual SUPERSEDES. |
| **privacy** | Core security paper: persistent memory injection / indirect prompt injection class; PRP up to **~47.9–50%** of retrieves poisoned in reported setting. |
| **Kedger lessons** | (1) Treat promoted experience/skill memory as an **untrusted channel** — require provenance + Verify before imitate. (2) Hybrid dense+lexical retrieve increases poison surface; add anomaly/provenance rerank. (3) Measure **poisoned retrieval proportion (PRP)** and downstream task hijack as S6 seal regression fixtures. (4) Single-shot grafts that persist across sessions break session-scoped sanitizer assumptions. |
| **metric_impact** | PRP; attack success / benign task fidelity on agent workloads; Verify ablation. |
| **refine_candidate** | **yes** — S6 experience-memory poison (MemoryGraft) seal harness |

---

### 12. MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory
**arXiv:2601.03192** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Fine-tuning for self-evolution is costly and forgets; memory methods retrieve by passive semantic match and inject noise. |
| **representation** | **MemRL**: non-parametric RL on episodic memory. Store **Intent–Experience–Utility** triplets; **Two-Phase Retrieval** semantic recall then **value-aware** selection using learned utilities from environmental feedback. Decouples stable reasoning (frozen LM) from plastic memory. |
| **write / read / forget** | Write: episodic experiences with utility updates from rewards (EMA-style). Read: two-phase semantic→utility filter. Forget: catastrophic forgetting avoided by not updating LM weights; low-utility items deprioritized (not necessarily deleted). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate should rank Anchors by **utility/Q**, not embedding alone. (2) Keep LM frozen; evolve memory utilities online (stability–plasticity). (3) Table 2: MemRL best Last/CSR across Code/OS/DB/Exploration/Knowledge (e.g. aggregate **0.772/0.798** vs MemP **0.736/0.760**). (4) Intent–Experience–Utility schema is a promote record shape for S4. |
| **metric_impact** | Last-epoch success and cumulative success rate (CSR) on BigCodeBench, Lifelong Agent Bench, ALFWorld; retrieval-size ablations. |
| **refine_candidate** | **yes** — S7 two-phase utility-aware episodic retrieve |

---

### 13. Implicit Graph, Explicit Retrieval: Towards Efficient and Interpretable Long-Horizon Agents
**arXiv:2601.03417** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Explicit structured memories get brittle under long context; latent memories are efficient but uninspectable. |
| **representation** | **LatentGraphMem**: graph builder stores **latent** graph of long doc; subgraph retriever selects task-specific explicit subgraph under budget; frozen LLM reasons over retrieved evidence. Train builder+retriever; joint refinement. |
| **write / read / forget** | Write: latent graph from document. Read: budgeted explicit subgraph retrieve → frozen reasoner. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent (footer only). |
| **Kedger lessons** | (1) Keep S5 graph **latent for storage**, materialize explicit subgraph only at hydrate — best of audit+efficiency. (2) Fixed retrieve budget is a pack-compile constraint. (3) Best avg accuracy across scales: **56.08% / 58.64% / 63.34%** (1.5B/3B/8B). (4) Frozen reasoner + trained retrieve aligns with Kedger not finetuning Anchor store into weights. |
| **metric_impact** | Long-horizon QA accuracy vs structured/latent baselines across model scales; subgraph budget ablations. |
| **refine_candidate** | **yes** — S5 latent graph + explicit subgraph hydrate |

---

### 14. TeleMem: Building Long-Term and Multimodal Memory for Agentic AI
**arXiv:2601.06037** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | RAG treats memories as independent fragments without consolidation/update/causal organization → unstable long-horizon reasoning. |
| **representation** | **TeleMem**: structured evolvable **semantic trajectories**; multimodal memory + ReAct observe–think–act loop; consolidation across dialogue/multimodal segments to cut redundancy and fix inconsistencies. |
| **write / read / forget** | Write: trajectory-structured multimodal memories with consolidation/update. Read: ReAct-style recall over trajectories. Forget: decay/forgetting discussed vs MemoryBank; consolidation reduces redundancy. |
| **conflict** | Consolidation resolves inconsistencies/contradictions across segments. |
| **privacy** | Excludes LoCoMo adversarial subset — eval choice. |
| **Kedger lessons** | (1) Store memories as **causal semantic trajectories**, not bag-of-chunks. (2) Periodic consolidate before hydrate (dedupe+inconsistency repair). (3) ZH-4O QA: TeleMem **86.33%** vs Mem0 **70.20%** / RAG **62.45%**; claims **+19%** vs Mem0, **−43%** tokens (abstract). (4) Multimodal segments must enter same trajectory schema as text for agent loops. |
| **metric_impact** | ZH-4O accuracy; token usage; comparisons to Mem0/A-Mem/MOOM/long-context LLM. |
| **refine_candidate** | **yes** — S3 trajectory consolidate + multimodal ReAct memory |

---

### 15. HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents
**arXiv:2601.06377** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S4, S7 |
| **problem** | Long-term memory systems lack adaptability/scalability/self-evolution under continuous dialogue. |
| **representation** | **HiMem**: **Episode Memory** via Topic-Aware Event–Surprise dual-channel segmentation; **Note Memory** multi-stage extraction of stable knowledge. Hybrid + best-effort retrieve (Note→Episode with LLM sufficiency check). Conflict-aware Memory Revision: ADD/UPDATE/DELETE on independent/extendable/contradictory; adaptive forgetting. |
| **write / read / forget** | Write: episodes + notes; revision ADD/UPDATE/DELETE. Read: best-effort hierarchical retrieve. Forget: adaptive forgetting regulates Note Memory; episodes preserved temporally. |
| **conflict** | Explicit conflict-aware revision when new info overlaps/extends/contradicts notes. |
| **privacy** | Ethics note on data privacy for memory systems; excludes adversarial dialogue category. |
| **Kedger lessons** | (1) Dual Episode/Note stores map cleanly to L2 episodes vs L3 notes/Anchors. (2) Best-effort Note→Episode escalate when evidence insufficient — hydrate pattern. (3) Self-evolution improves Note Memory **~+5.85%** (overall **~+0.28%**). (4) Typed ADD/UPDATE/DELETE on contradiction is SUPERSEDES-ready. |
| **metric_impact** | Long-horizon dialogue QA; hybrid vs best-effort retrieve; self-evolution ablations. |
| **refine_candidate** | **yes** — S3/S4 HiMem-style conflict-aware Note revision |

---

### 16. AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operations
**arXiv:2601.08323** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Hand-crafted static memory workflows don't generalize; need learnable memory management policy. |
| **representation** | **AtomMem**: memory as POMDP; atomic **CRUD** action space joint with env actions; hybrid retrieval; policy optimized (RL) to orchestrate Create/Read/Update/Delete for task demands. |
| **write / read / forget** | Write/Read/Update/Delete are first-class learned actions over memory state s^mem. |
| **conflict** | Discusses non-conflicting accumulation tasks vs cases needing conflict handling; CRUD Update/Delete available but not a typed ConflictSet. |
| **privacy** | Silent (footer only). |
| **Kedger lessons** | (1) Expose **atomic memory ops** to the agent policy rather than fixed cognify scripts. (2) Jointly learn when to act in env vs mutate memory. (3) Prefer learnable CRUD over fixed forgetting schedules for long-horizon agents. (4) Use POMDP formulation to test Kedger promote/hydrate as controllable actions in fixtures. |
| **metric_impact** | Long-context and multi-question benchmarks in paper experiments; ablation of CRUD action set. |
| **refine_candidate** | **yes** — S2/S3 learnable atomic CRUD memory policy |

---

### 17. Explore with Long-term Memory: A Benchmark and Multimodal LLM-based Agent for Embodied Exploration
**arXiv:2601.10744** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Embodied benchmarks score task success but ignore exploration process and long-term memory use for lifelong operation. |
| **representation** | **LMEE** task + **LMEE-Bench** (multi-goal nav + memory QA). **MemoryExplorer**: MLLM fine-tuned with RL to retrieve long-term episodic memory under context limits and explore proactively for future use. |
| **write / read / forget** | Write: episodic exploration memories from embodied trajectories. Read: memory retrieval during planning under window limits. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent (footer only). |
| **Kedger lessons** | (1) Eval hydrate with **process metrics** (exploration/memory use), not outcome-only success. (2) Train policies that retrieve episodic memory when context can't hold full history. (3) Partial-test note: ~**35%** of test set (58/166) used under resource limits — don't overclaim full-bench numbers. (4) Memory-QA coupled to nav is a good S7/S8 fixture pattern. |
| **metric_impact** | LMEE-Bench navigation success/SPL-like + memory QA; exploration ablations; real-world tests. |
| **refine_candidate** | **no** — (benchmark primary; agent similar to MemRL/WebCoach tickets) |

---

### 18. Toward Efficient Agents: Memory, Tool learning, and Planning
**arXiv:2601.14192** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Agent research optimizes effectiveness while under-studying efficiency (latency, tokens, steps) across memory, tools, and planning. |
| **representation** | Survey/roadmap clustering memory into working vs external (textual/latent/item-based), tool learning, and planning efficiency techniques; catalogs systems (COMEDY, MemAgent, MemoRAG, MemoryBank, Graphiti-like, etc.) with shared high-leverage patterns. |
| **write / read / forget** | Survey maps write/read/forget patterns across cited systems (e.g. Ebbinghaus forgetting, overwrite fixed memory, KV compress) — not a single new WRF loop. |
| **conflict** | Notes conflict-handling modules in cited schedulers (MemScheduler/MemVault) — survey-level. |
| **privacy** | Silent beyond generic. |
| **Kedger lessons** | (1) Every Kedger stage ticket should declare an **efficiency SLI** (tokens/latency/steps), not only quality. (2) Prefer catalogued patterns: activation/KV latent memory vs symbolic packs by threat model. (3) CoA-style tool routing claim **>30%** inference time cut vs Toolformer in surveyed results — measure tool-select cost. (4) Use this paper as index into efficiency-relevant memory designs when prioritizing refine tickets. |
| **metric_impact** | Comparative efficiency axes: tokens, latency, steps, memory bytes vs task success across surveyed methods. |
| **refine_candidate** | **no** — (survey; feed prioritization only) |

---

### 19. EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding
**arXiv:2602.15329** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Online/streaming video forces tradeoff between long-range context and fine detail under MLLM window limits; passive token pruning is insufficient. |
| **representation** | **EventMemAgent**: hierarchical **event-centric** memory for streams; multi-granular perception toolkit; agentic RL internalizes when to invoke tools/reason. Active perception vs passive sliding-window/token prune. |
| **write / read / forget** | Write: archive stream into structured event memories. Read: iterative multi-granular perception over hierarchy. Forget: event abstraction replaces unbounded raw frame retention; contrasts token pruning baselines. |
| **conflict** | Frames problem as conflict between infinite stream and finite window — architectural, not belief conflict. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Online hydrate should be **event-centric**, not frame-token sliding only. (2) RL the perception/tool policy jointly with memory use. (3) With 32 frames: avg **60.75%** > GPT-4o **59.54%**; gains **+4.27%** real-time perception, **+1.08%** backward, **+1.1%** forward active. (4) Cap sensory buffer by event boundaries for WorkingState pressure. |
| **metric_impact** | Online video understanding suite accuracy under frame budget; vs open/proprietary baselines. |
| **refine_candidate** | **yes** — S2/S7 event-centric online video memory agent |

---

### 20. M2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory and Skill Memory
**arXiv:2603.00503** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Long-horizon web agents bloat context with full histories and still reason poorly; training-heavy fixes are costly. |
| **representation** | **M²** training-free dual memory: **In-Mem** recursive textual abstractions of recent trajectory (discard redundant raw steps); **Ex-Mem** external skill/experience memory for decision robustness. Integrates both into web agent context. |
| **write / read / forget** | Write: step summaries into In-Mem chain; skills/experiences into Ex-Mem. Read: both memories conditioned into C_t. Forget: discard raw older observations replaced by recursive summaries (−55.4% tokens in one setting). |
| **conflict** | Silent. |
| **privacy** | Silent (footer only). |
| **Kedger lessons** | (1) Split working trajectory compress (**In-Mem**) from durable skill store (**Ex-Mem**). (2) Recursive summary chain is a PRE_COMPACT pattern for long web sessions. (3) Reported lifts e.g. **+12.5% / +5.5% / +16.2%** across backbones with In&Ex; token cuts **~53–55%**. (4) Training-free dual memory is preferable when you can't fine-tune the web actor. |
| **metric_impact** | Web navigation success vs Normal/In-only/Ex-only; tokens/steps. |
| **refine_candidate** | **yes** — S2 In-Mem + S3 Ex-Mem dual for web agents |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (honest deep-recard) | 20 |
| Cumulative FULL | **400** |
