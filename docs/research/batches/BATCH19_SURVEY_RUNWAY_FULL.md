# Batch 19 — Survey Runway FULL (Kedger) — **honest deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Body-grounded mechanism cards (Intro/Method/Results) replacing 2026-08-08 abstract-template cards.  
> **Progress:** FULL 360 → **380**.  
> **Method:** Fulltext `/tmp/kedger-papers/full/{id}.txt` + agent deep-read cards.  
> **Kedger stages:** S1–S8  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers from body only.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body deep-read; deep-recard upgrade of Batch19) | **20** | `2502.05453`, `2502.13843`, `2503.10049`, `2505.20231`, `2505.20286`, `2506.13651`, `2507.21105`, `2508.01415`, `2508.01832`, `2508.13250`, `2509.01055`, `2509.17459`, `2509.22315`, `2509.25250`, `2510.03611`, `2510.04195`, `2510.04618`, `2510.07134`, `2510.07925`, `2510.09720` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs cached |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. DAMCS: Decentralized Generative Agents with Adaptive Hierarchical Knowledge Graph
**arXiv:2502.05453** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S5', 'S7', 'S8'] |
| **problem** | CTDE MARL doesn't scale to dynamic open-world multi-agent cooperation with multimodal data and flexible strategies. |
| **representation** | DAMCS: adaptive hierarchical KG memory per agent; structured reasoning outputs; structured communication; Multi-agent Crafter testbed; decentralized planning. |
| **write / read / forget** | Write: adaptive hierarchical KG from experience. Read: query KG for cooperative planning. Forget: Silent (adaptive updates). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Per-agent hierarchical KG + structured messages ≈ S5/S8 for multi-agent Kedger. (2) Decentralized memory avoids central WorkingState bottleneck. (3) Multi-agent Crafter is a cooperation SLI candidate. (4) Structured output format beats free-form chat for agent IPC. |
| **metric_impact** | Two-agent scene 63% fewer steps to goal vs LLM basic; six-agent 74% fewer steps; single LLM-Mem 13.6% fewer steps; diamond collection 39% fewer steps vs single LLM-Mem; basic agent success drops to 60% on last three tasks. |
| **refine_candidate** | **yes — S5 adaptive hierarchical KG for multi-agent memory** |

---

### 2. AgentCF++: Memory-enhanced Agents for Popularity-aware Cross-domain Recommendations
**arXiv:2502.13843** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S2', 'S3', 'S7'] |
| **problem** | AgentCF memory mixes irrelevant cross-domain info and ignores popularity/social influence from others' interactions. |
| **representation** | AgentCF++ dual-layer memory + two-step fusion: separates domain memories and adds popularity-aware signals; inference + update phases; Amazon cross-domain Cross-1…5. |
| **write / read / forget** | Write: update dual-layer (domain + fused) memories post-interaction. Read: two-step fusion at decision time. Forget: Silent. |
| **conflict** | Silent. |
| **privacy** | Mentions privacy-preserving simulation of user behavior as motivation for agent-based rec. |
| **Kedger lessons** | (1) Cross-domain hydrate must isolate domain memories before fuse—prevent bleed. (2) Popularity/social Evidence is a separate facet from personal preference Anchors. (3) Dual-layer design maps to private vs cohort tiers. (4) Report MRR/NDCG on Cross-* as personalization SLIs. |
| **metric_impact** | MRR table vs BPR-MF/SASRec/Pop/AgentCF on Cross-1…5 (e.g., BPR-MF ~0.29–0.31, SASRec ~0.31–0.38); AgentCF++ best in paper's overall comparison (exact winning MRR cells in Table; NDCG in repo). |
| **refine_candidate** | **yes — S2 dual-layer domain isolation + popularity facet** |

---

### 3. LGC-MARL: LLM Planner + Graph-based Collaboration Policy for MAS
**arXiv:2503.10049** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S1', 'S5', 'S7'] |
| **problem** | Pure MARL struggles with complex tasks/reward design; pure LLM MAS too slow/fragile in dynamic envs. |
| **representation** | LGC-MARL: critic-equipped LLM planner → subtasks + action-dependency graph; graph-based collaboration meta-policy for MARL; LLM reward-function generator; constrained graph-format LLM outputs. |
| **write / read / forget** | Write: Silent long-term symbolic memory (graph policy params / rewards). Read: agents follow dependency graph each episode. Forget: Silent. |
| **conflict** | Silent (critic checks subtask rationality / hallucination). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) LLM should emit dependency graphs for agents, not dialogue scripts. (2) Critic-before-execute mirrors S8 gate on plans. (3) LLM-generated rewards are risky—keep human audit. (4) Graph communication is low-cost coordination Evidence. |
| **metric_impact** | Scene1 Success Rate up to 0.92 for full method vs 0.6–0.89 ablations (wo reward / wo graph etc.); also Average Time and token cost metrics. |
| **refine_candidate** | **no — MARL training stack; graph-plan pattern only** |

---

### 4. MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session Agents
**arXiv:2505.20231** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S3', 'S7'] |
| **problem** | Multi-session TOD RAG uses semantic similarity, ignoring task intent and slot coherence. |
| **representation** | MemGuide two-stage: (1) Intent-Aligned Retrieval vs stored intent descriptions → QA memory units; (2) Missing-Slot Guided Filtering with CoT slot reasoner + fine-tuned LLaMA-8B re-rank by marginal slot-completion gain; proactive confirmation responses. |
| **write / read / forget** | Write: memory bank of intent-tagged QA units from sessions. Read: intent match then slot-gain re-rank. Forget: Silent (filter excludes low-gain units from context). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S7 hydrate for TOD must key on intent+slots, not embedding similarity alone. (2) Marginal slot-completion gain is a concrete re-rank objective for pack compile. (3) Confirmation-type responses are a first-class agent act when slots incomplete. (4) Build intent-tagged memory banks at cognify time. |
| **metric_impact** | Task success +11% (88%→99%); dialogue length −47.1% (6.03→3.19); turns 2.52→1.21 (−52%); Recall@5 +7.7% avg vs semantic-only. |
| **refine_candidate** | **yes — S7 intent-aligned + slot-gain memory filter** |

---

### 5. Alita: Generalist Agent with Minimal Predefinition and Maximal Self-Evolution
**arXiv:2505.20286** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S1', 'S3', 'S7'] |
| **problem** | Generalist agents depend on large hand-built tool/workflow inventories, hurting adaptability and scale. |
| **representation** | Alita: manager agent orchestrates web agent with only basic tools; MCP brainstorming → search OSS → generate scripts/envs → CodeReAct loop with self-correct; encapsulate new tools as MCP servers for reuse (self-reinforcing). |
| **write / read / forget** | Write: new MCPs/tools into reusable box after success. Read: invoke MCP tools during solve. Forget: Silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Prefer growable MCP tool registry over giant predefined S1 tool packs. (2) Successful tool creation should promote into sealed reusable modules. (3) Web-search-for-libraries is an Evidence path for tool synthesis. (4) Track pass@k on GAIA-like suites as agent SLI. |
| **metric_impact** | GAIA: 75.15% pass@1 and 87.27% pass@3 (Claude-Sonnet-4+GPT-4o), > OpenAI Deep Research 67.36% pass@1; MathVista/PathVQA 74.00%/52.00% pass@1; ablation gains e.g. 3.85%→11.54% in a reported setting. |
| **refine_candidate** | **yes — S1/S3 MCP self-evolving tool promote** |

---

### 6. xbench: Profession-Aligned Real-World Agent Productivity Evaluations
**arXiv:2506.13651** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S7', 'S8'] |
| **problem** | Agent benches track isolated skills, not commercial productivity / Technology-Market Fit. |
| **representation** | xbench dynamic profession-aligned suite; initial Recruitment (50 headhunting tasks) and Marketing (50 advertiser reqs × 836 influencers); metrics correlated with productivity value; live leaderboard. |
| **write / read / forget** | Silent (eval suite, not memory system). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Add profession-aligned SLIs alongside Hotpot-style QA. (2) Tasks split People/People-to-Info distributions (~44/30/26%) inform fixture design. (3) Score rubrics use 50/85/95/100% coverage bands—reuse for hydrate completeness. (4) Track agent productivity over time, not one snapshot. |
| **metric_impact** | Recruitment 50 tasks; Marketing 50×836; domain CAGR context 17.6%; info-coverage scoring bands 50–100%; baselines reported on xbench.org. |
| **refine_candidate** | **no — eval suite; adopt as external SLI source** |

---

### 7. AgentMaster: Multi-Agent Framework Using A2A and MCP Protocols
**arXiv:2507.21105** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S1', 'S7', 'S8'] |
| **problem** | MAS lack standardized inter-agent communication and heterogeneous tool access; few systems combine A2A+MCP. |
| **representation** | AgentMaster: coordinator with complexity assessment; A2A between agents; MCP clients for tools; retrieval agents; LLM integration + error handling; multimodal IR/analysis case study. |
| **write / read / forget** | Write: Silent persistent (session orchestration state). Read: retrieval agents + MCP tools. Forget: Silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Standardize Kedger tool bus on MCP-like contracts and agent IPC on A2A-like messages. (2) Complexity-aware coordinator routes simple vs multi-agent hydrate. (3) Eval with BERTScore + G-Eval for multi-agent answers. (4) Dual-protocol pilot reduces ad-hoc glue. |
| **metric_impact** | BERTScore F1 96.3%; LLM-as-judge G-Eval 87.1% (complex queries also >87.1% G-Eval / ~96.3% BERTScore). |
| **refine_candidate** | **yes — S1 MCP+A2A protocol layer for multi-agent hydrate** |

---

### 8. RoboMemory: Brain-inspired Multi-memory Framework for Embodied Agents
**arXiv:2508.01415** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S2', 'S3', 'S5', 'S7', 'S8'] |
| **problem** | VLM embodied agents lack long-horizon memory; VLAs lack high-level planning over history. |
| **representation** | RoboMemory: preprocessor; comprehensive embodied memory (spatial KG + episodic + semantic + long-term); closed-loop planner with critic; low-level executor; dynamic spatial KG update algorithm. |
| **write / read / forget** | Write: update spatial KG + episodic/semantic stores from perception. Read: retrieve subgraphs for planning. Forget/repair: detect local inconsistencies and merge observations. |
| **conflict** | Spatial KG update retrieves subgraphs, detects local inconsistencies, merges observations. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Embodied memory should split spatial KG / episodic / semantic like RoboMemory modules. (2) Critic-in-the-loop is mandatory (55% vs 67% SR without critic). (3) Inconsistency detection on spatial graphs ≈ S5 ConflictSet. (4) Ablate each memory type—spatial removal hurts most (47% SR). |
| **metric_impact** | Avg SR +26.5% over strong baseline (Qwen2.5-VL-72B-Ins); full 67% vs w/o critic 55%, w/o spatial 47%, w/o episodic 62%, w/o semantic 58%, w/o long-term 57%. |
| **refine_candidate** | **yes — S5 dynamic spatial KG + critic-gated plan** |

---

### 9. MLP Memory: Retriever-pretrained Differentiable External Memory for LMs
**arXiv:2508.01832** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S2', 'S7'] |
| **problem** | RAG retrievers are non-differentiable and weakly coupled to LMs; hallucinations persist on knowledge-intensive tasks. |
| **representation** | Decouple memorization: pretrained MLP external memory imitates retriever behavior, differentiable, interpolated with LM like kNN-LM but parametric MLP; scaling-law study vs GPT-2 sizes. |
| **write / read / forget** | Write: pretrain MLP memory on corpus (imitate retrieval). Read: interpolate MLP memory distribution with LM. Forget: Silent (weights fixed at inference unless retrained). |
| **conflict** | Silent (NLI entail/contradict mentioned only as eval task type). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Differentiable external memory is an alternative to symbolic packs for parametric memorization—keep auditability tradeoff explicit. (2) Scaling exponents improve (+17.5% WikiText-103, +24.1% web mix)—memory size co-scales. (3) Stronger hallucination reductions vs kNN-LM on HaluEval-style metrics. (4) Not a drop-in for sealed Anchors—use only where provenance optional. |
| **metric_impact** | Power-law exponent improvements 17.5% (WikiText-103) and 24.1% (web); HaluEval/knowledge-task gains (e.g., avg scores ~46–48%; Llama/Mistral accuracies ~72–75%); 99% cum. prob mass with 308 tokens in analysis. |
| **refine_candidate** | **no — neural memory weights conflict with Anchor audit path** |

---

### 10. Explicit vs Implicit Memory: Multi-hop Reasoning over Personalized Information
**arXiv:2508.13250** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S3', 'S4', 'S7'] |
| **problem** | Personalization memory work focuses on preference QA; real tasks need multi-hop reasoning over large user info (MPR). |
| **representation** | Compares explicit memory (RAG variants), implicit (model adaptation), and HybridMem/BlockSFT (cluster statements → LoRA blocks); reasoning structures NR/SR/MR/DR; hop-count stress tests. |
| **write / read / forget** | Write: explicit stores statements; BlockSFT trains per-cluster LoRAs. Read: retrieve statements or activate adapters. Forget: Silent. |
| **conflict** | Silent. |
| **privacy** | Personalized user statements—privacy implied by personalization setting, no attack study. |
| **Kedger lessons** | (1) Multi-hop personalization needs explicit statement graphs/packs, not only preference embeddings. (2) Implicit-only memory can hurt long-hop reasoning—prefer hybrid. (3) Cluster count ~30–50 robust for BlockSFT. (4) Track accuracy vs hop length as SLI (60%→20% degradation pattern). |
| **metric_impact** | Overall +10–20% vs NR baselines on multi-hop structures; MR falls from >60% (2-hop) to ~20% (10-hop); DR can drop ~80% under stress; HybridMem best overall. |
| **refine_candidate** | **yes — S7 hybrid explicit+block memory for multi-hop personalization** |

---

### 11. VerlTool: Holistic Agentic RL with Tool Use (ARLT)
**arXiv:2509.01055** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S1', 'S7'] |
| **problem** | ARLT systems are fragmented, synchronous, and hard to extend across tool domains. |
| **representation** | VerlTool framework: asynchronous rollouts, modular tool-as-plugin, consistent tokenization, parallel tool server; tasks VT-Math/Search/SQL/VisualReasoner/DeepSearch/SWE. |
| **write / read / forget** | Write: Silent (RL training trajectories). Read: tool results in multi-turn rollouts. Forget: Silent. |
| **conflict** | Tokenization consistency to avoid prefix inconsistencies during rollout. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Kedger tool training/eval should use async multi-turn tool servers. (2) Tool-as-plugin matches S1 extensibility. (3) Keep token-list prefixes consistent across tool calls. (4) Multi-domain ARLT numbers become regression targets. |
| **metric_impact** | VT-Math 62.2% avg math benches; VT-Search 45.9% (+10.9 vs Search-R1); VT-VisualReasoner 82.7% V*; VT-DeepSearch 34.0% GAIA. |
| **refine_candidate** | **no — RL infra; consume metrics/tools patterns** |

---

### 12. Principles: Synthetic Strategy Memory for Proactive Dialogue Agents
**arXiv:2509.17459** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S3', 'S4', 'S7'] |
| **problem** | Proactive dialogue strategy planners suffer limited coverage, preference bias, and costly retraining. |
| **representation** | Principles: offline self-play → detect success/failure → revise strategy → backtrack re-simulate → derive reusable principle memory; at inference retrieve+reinterpret principles for strategy planning (training-free). |
| **write / read / forget** | Write: derive Principles from successful/failed simulations into strategy memory. Read: retrieve top-k principles to plan. Forget: Silent (offline corpus grows). |
| **conflict** | Silent (mitigates strategy bias, not factual conflict). |
| **privacy** | Ethical-risk note on LLM use; no PII mechanism. |
| **Kedger lessons** | (1) Strategy memory is a promote target distinct from factual Anchors. (2) Learn from both success and failure trajectories. (3) Offline self-play principles transfer without fine-tune—cheap S4 path. (4) Online construction works but drops SR (0.7385→0.6615 ESConv)—prefer offline seed. |
| **metric_impact** | Principles ESConv SR 0.7385 AT 6.36; ExTES 0.8615/5.87; P4G 0.9500/4.73; P4G+ 0.5917/7.15; ablations w/o retrieval/reinterpret drop SR; baselines often <0.56 SR; dominant-strategy bias >80% usage in PPDPP-like methods. |
| **refine_candidate** | **yes — S4 synthetic strategy-memory promote for proactive agents** |

---

### 13. PRIME: Planning and Retrieval-Integrated Memory for Dual-Process Reasoning
**arXiv:2509.22315** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S7', 'S8'] |
| **problem** | LLMs need both fast intuitive answers and slow deliberate retrieval/planning; fixed always-System-2 is costly. |
| **representation** | PRIME multi-agent: System-1 Quick Thinking; Reflection triggers System-2 pipeline (planning, hypothesis, retrieval/reading, integration, decision); dual-process medical + multi-hop reasoning. |
| **write / read / forget** | Write: Silent durable store (in-run agent scratchpads). Read: retrieval/reading agents pull evidence under System 2. Forget: Silent. |
| **conflict** | Reflection checks logical inconsistencies/uncertainty before accepting System-1. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Uncertainty-triggered System-2 mirrors FLARE-style mid-turn hydrate. (2) Separate planning/hypothesis/retrieve/decide agents clarify S8 stages. (3) Easy questions should stay System-1 (96.59%/92.68%) to save cost. (4) Ablate reading/hypothesis—each costs ~1–3 pts. |
| **metric_impact** | Full PRIME 87.2%; System-1 only 80.4%; System-2 only 86.0%; ablations 84.8/84.2/83.6; hard set System-1 85.71%→35.71% without help while System-2 recovers. |
| **refine_candidate** | **yes — S7/S8 uncertainty-triggered deliberate retrieve pipeline** |

---

### 14. Memory Management and Contextual Consistency for Long-Running Low-Code Agents
**arXiv:2509.25250** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S2', 'S3', 'S6', 'S7'] |
| **problem** | Long-running LCNC agents suffer memory inflation and contextual degradation (forget constraints, self-contradict). |
| **representation** | Hybrid episodic+semantic memory with Intelligent Decay score (recency×relevance×user utility) to prune/consolidate; smart summarization; user-centric visual memory UI for non-technical users. |
| **write / read / forget** | Write: episodic/semantic stores. Read: retrieve under decay-weighted relevance. Forget: Intelligent Decay prunes/consolidates by composite score. |
| **conflict** | Addresses agents contradicting prior decisions via consistency-oriented decay/summarization. |
| **privacy** | Silent (user-visible memory management). |
| **Kedger lessons** | (1) Decay should be user-utility-aware, not recency-only. (2) LCNC needs visual memory controls (align Memory Sandbox). (3) Measure token cost vs task completion together. (4) Contextual consistency SLI: contradiction rate under long runs. |
| **metric_impact** | Absolute +13.6% task completion vs baseline; −22% average token cost vs basic RAG while improving completion. |
| **refine_candidate** | **yes — S2/S6 Intelligent Decay + user memory UI** |

---

### 15. Can an LLM Induce a Graph? Memory Drift and Context Length
**arXiv:2510.03611** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S5', 'S7', 'S8'] |
| **problem** | Needle-in-haystack benches miss whether LLMs induce structured relational graphs from long noisy text. |
| **representation** | Eval: reconstruct graphs from natural-language descriptions under edge/degree/clique sampling; metric Memory Drift from precision/recall vs gold edges; tests GPT-4o, o1, Gemini-2, Llama-3, Mistral-7B; studies density, CoT, hallucination vs forgetting. |
| **write / read / forget** | Silent (diagnostic eval, not a memory writer). |
| **conflict** | Silent (structural mismatch measured as drift). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Graph induction under long context is a harder SLI than needle retrieval for S5. (2) Memory drift begins at shorter lengths than advertised context windows. (3) Distinguish hallucination vs forgetting failure modes in fixtures. (4) Don't assume CoT/o1 fully fixes drift—paper stresses residual limits. |
| **metric_impact** | Defines Memory Drift with examples Perfect 0.00 / Mid 0.50 / Balanced 0.75 from P/R; finds earlier sharper degradation than needle benches across five LLMs (figures in §IV). |
| **refine_candidate** | **yes — S5 graph-induction memory-drift probe** |

---

### 16. LLM-MapRepair: Coherent Spatial Memory via Graph Rectification
**arXiv:2510.04195** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S5', 'S6', 'S7'] |
| **problem** | Incremental LLM map construction accumulates topological/directional conflicts as environments grow. |
| **representation** | LLM-MapRepair: conflict detection; error localization via Minimal Conflicting Path Pair + LCA candidate edges + Edge Impact scoring; version-control graph ops; repair prioritization; cleaned MANGO-style benchmark. |
| **write / read / forget** | Write: incremental navigation graph with version control. Read: query repaired graph for paths. Forget/repair: remove/fix conflicting edges by priority. |
| **conflict** | Core contribution: detect/localize/repair structural inconsistencies (topo/directional/cascading). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S5 spatial/topology graphs need ConflictSet + LCA localization, not only triple NLI. (2) Edge Impact prioritization ≈ SUPERSEDES urgency. (3) Version control on graph Anchors enables audit/rollback. (4) Huge edge-recall lift shows repair > raw LLM mapping. |
| **metric_impact** | Node recall 94.3% (+8.6 pp) and edge recall 88.2% (+55.8 pp) vs direct LLM mapping; CF repair-rate gains up to +50 pp on cases; non-LLM referees noted for some settings. |
| **refine_candidate** | **yes — S5/S6 graph ConflictSet repair + version control** |

---

### 17. ACE: Agentic Context Engineering for Self-Improving LMs
**arXiv:2510.04618** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S2', 'S3', 'S7'] |
| **problem** | Context adaptation methods suffer brevity bias and context collapse; need evolving contexts without destroying detail. |
| **representation** | ACE: incremental delta updates to context; grow-and-refine with reflection + curator; avoids collapse via structured evolving contexts; eval on AppWorld agents + finance/medical/text-to-SQL; KV-cache cost analysis. |
| **write / read / forget** | Write: append/refine context deltas (cheatsheet-like). Read: use evolved context at inference. Forget: dedup/prune triggers at max length hyperparameters. |
| **conflict** | Discussion mentions contradiction detection to prioritize curator updates. |
| **privacy** | Related-work cites unlearning/privacy as motivation for not always fine-tuning weights. |
| **Kedger lessons** | (1) Prefer delta context updates over full rewrite to avoid collapse. (2) Reflector+Curator roles map to cognify/promote. (3) Longer contexts ≠ higher serving cost if KV reuse engineered. (4) +10.6% agent / +8.6% finance gains are refine targets for WorkingState evolution. |
| **metric_impact** | +10.6% agents and +8.6% finance avg over strong baselines; up to 10–20% higher accuracy vs MIPROv2 with ≤35× fewer …; AppWorld margins vs GEPA/ReAct ~11–12 pts; online +14.8% vs ReAct. |
| **refine_candidate** | **yes — S2/S3 incremental delta context evolve (ACE)** |

---

### 18. TrackVLA++: Reasoning and Memory for Embodied Visual Tracking
**arXiv:2510.07134** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S2', 'S7', 'S8'] |
| **problem** | Language-guided embodied tracking fails under occlusion/distractors without spatial reasoning and temporal memory. |
| **representation** | TrackVLA++: Polar-CoT spatial reasoning → polar-coordinate tokens; Target Identification Memory (TIM) with gated updates for long-horizon identity; VLA action head. |
| **write / read / forget** | Write: gated TIM updates preserving last reliable target features. Read: TIM+Polar tokens condition actions. Forget: gate blocks noisy updates (implicit). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Gated identity memory is a WorkingState pattern for tracking entities across turns. (2) Compact spatial tokens (polar) beat verbose CoT in action loops. (3) Ablate CoT (+6.0 SR) and TIM (+2.8) separately. (4) Distractor/occlusion suites needed in embodied SLIs. |
| **metric_impact** | Beats prior leaders by 5.1% and 12% SR (egocentric settings); SR 74.0% vs NavFoM 62.0%; recognition accuracy 87.5% vs 83.0%; vs TrackVLA +14/7/17% on tasks; CoT +6.0 SR, TIM +2.8. |
| **refine_candidate** | **yes — S2 gated Target Identification Memory** |

---

### 19. Persistent Memory and User Profiles for Personalized Long-term LLM Agents
**arXiv:2510.07925** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S2', 'S3', 'S4', 'S7'] |
| **problem** | RAG lacks binding of context with durable user-specific personalization across long-term agent interactions. |
| **representation** | Agentic architecture: short-term memory, summaries, long-term memory, evolving user profile; multi-agent collaboration + multi-source retrieval; self-validator refinement loop. |
| **write / read / forget** | Write: summaries → LTM; update user profile. Read: retrieve LTM+profile with context. Forget: summarization compression; validator may refine inconsistencies. |
| **conflict** | Self-validator detects gaps/inconsistencies and triggers refinement. |
| **privacy** | Personalization/user profiles—no formal privacy attack eval. |
| **Kedger lessons** | (1) Separate profile Anchors from episodic LTM in promote. (2) Self-validator before answer ≈ ConflictSet lite. (3) Pilot user studies complement synthetic LongMemEval metrics. (4) Ablations show profiles+LTM beat RAG-baseline retrieval accuracy. |
| **metric_impact** | Rater agreement 93% retrieval accuracy / 81–84% response; GVD GPT-4o agentic system retrieval ~96% vs RAG-baseline 87%; BertScore/ROUGE tables across GPT-4o & Gemini on GVD/LongMemEval. |
| **refine_candidate** | **yes — S4 evolving user-profile + LTM split with self-validator** |

---

### 20. PAMU: Preference-Aware Memory Update for Long-Term LLM Agents
**arXiv:2510.09720** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | ['S3', 'S4', 'S7'] |
| **problem** | Memory systems improve store/retrieve but lack dynamic preference-memory updates as user behavior evolves. |
| **representation** | PAMU: preference extractor; continuous + categorical preference dims; fuse sliding-window average (SW) with EMA; change-detection signal; Bayesian/Kalman motivation; plugs into ReadAgent/MemoryBank/etc. on LoCoMo. |
| **write / read / forget** | Write: update preference memory via SW+EMA fusion each window. Read: preference-guided prompting for RG. Forget: EMA/SW naturally downweight stale prefs (soft). |
| **conflict** | Silent (preference change ≠ factual conflict). |
| **privacy** | Silent in mechanism (personal prefs). |
| **Kedger lessons** | (1) Preference Anchors need explicit update operators (SW+EMA), not retrieve-only. (2) Separate continuous vs categorical preference dims. (3) Change-detection should trigger re-hydrate of persona packs. (4) Drop-in module across five memory baselines on LoCoMo is the integration pattern. |
| **metric_impact** | Improves F1/BLEU-1 across five LoCoMo scenarios and five baselines (e.g., Qwen2.5-1.5B RA 6.54→8.27 F1 single-hop; multi-hop tables similarly †-marked gains). |
| **refine_candidate** | **yes — S4 preference-memory SW+EMA update operator** |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (honest deep-recard) | 20 |
| Cumulative FULL | **380** |
