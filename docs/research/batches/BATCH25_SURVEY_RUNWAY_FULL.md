# Batch 25 — Survey Runway FULL (Kedger) — **honest deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Body-grounded mechanism cards (Intro/Method/Results) replacing 2026-08-08 abstract-template cards.  
> **Progress:** FULL 480 → **500**.  
> **Method:** Fulltext `/tmp/kedger-papers/full/{id}.txt` + agent deep-read cards.  
> **Kedger stages:** S1–S8  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers from body only.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body deep-read; deep-recard upgrade of Batch25) | **20** | `2505.16421`, `2506.01952`, `2506.14728`, `2506.18019`, `2507.02592`, `2507.03616`, `2507.07998`, `2507.16784`, `2507.21055`, `2507.21407`, `2508.03680`, `2508.04700`, `2508.07010`, `2508.07407`, `2508.09874`, `2508.11567`, `2508.14704`, `2508.15253`, `2508.15305`, `2508.16629` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs cached |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. WebAgent-R1 — End-to-End Multi-Turn RL for Web Agents
**arXiv:2505.16421** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Web agents need multi-turn RL on dynamic UIs; prior RL mostly single-turn math. |
| **representation** | M-GRPO multi-turn RL from online parallel trajectories; binary success reward; thinking prompts; variants R1-Zero (no BC) vs R1-CoT; WebArena-Lite. |
| **write / read / forget** | Read: online web observations. Write: policy via RL (+ optional BC warm-start). Forget: silent (warns destructive CMS deletes in prod). |
| **conflict** | Silent. |
| **privacy** | Silent — warns irreversible data deletes in CMS envs. |
| **Kedger lessons** | (1) Behavior-cloning warm-start before multi-turn RL (Zero fails from 6.1%). (2) Binary task-success reward sufficient for web SR gains. (3) Test-time more interactions scales SR. (4) Long-CoT SFT 24.5% vs 20% standard BC — why traces help before RL. |
| **metric_impact** | Qwen-2.5-3B 6.1%→33.9%; Llama-3.1-8B 8.5%→44.8%; o3 only 39.4% |
| **refine_candidate** | **yes — S1/S7 multi-turn web RL with BC warm-start** |

---

### 2. WebChoreArena — Memory-Intensive Web Browsing Benchmark
**arXiv:2506.01952** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7, S8 |
| **problem** | WebArena under-stresses memory/calc chores; agents look strong without massive/long-term memory skills. |
| **representation** | Extension of WebArena sims: Massive Memory, Calculation, Long-Term Memory, Other chore tasks; exact_match/must_include protocols; reproducible four sites. |
| **write / read / forget** | Eval-only; agents must store/retrieve large obs and cross-page memory. Forget: prune/resume plan actions in AgentOccam-style baselines. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S2 WorkingState SLIs must include Massive Memory chores, not only QA. (2) GPT-4o 42.8% WebArena → ≤6.8% WebChoreArena — don't trust easy browse scores. (3) Gemini 2.5 Pro still 44.9% — headroom. (4) Long-term cross-page memory fixtures for hydrate. |
| **metric_impact** | GPT-4o ≤6.8% vs 42.8% WebArena; Gemini 2.5 Pro 44.9% |
| **refine_candidate** | **yes — S2/S7 WebChoreArena memory-chore fixtures** |

---

### 3. AgentDistill — Training-Free Distillation via MCP Boxes
**arXiv:2506.14728** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Agent distillation via trajectory replay fails to transfer dynamic planning; need reusable structured modules. |
| **representation** | Teacher generates self-contained Model-Context-Protocols (MCPs); abstract/cluster/consolidate into MCP-Box; student reuses MCPs training-free; PathVQA/SLAKE/Game-of-24. |
| **write / read / forget** | Write: teacher MCP generation → MCP-Box consolidation. Read: student invokes MCP modules. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Promote reusable MCP/tool cards, not raw teacher trajectories. (2) Training-free student hydrate via MCP-Box. (3) Game-of-24 GPT-3.5 34.3%→82.7% shows protocol scaffolding value. (4) Cluster/consolidate before S4 to avoid MCP sprawl. |
| **metric_impact** | PathVQA students ~52.7% match teacher; Game-of-24 +48.4 pts (GPT-3.5); SLAKE up to +10% |
| **refine_candidate** | **yes — S4 MCP-Box promote from teacher runs** |

---

### 4. Graphs Meet AI Agents — Survey Taxonomy (Plan/Exec/Memory/Coord)
**arXiv:2506.18019** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Agents face messy info/ops/interactions; need systematic view of how graphs structurize agent capabilities. |
| **representation** | Survey taxonomy: graphs for planning, execution, memory, multi-agent coordination; also agents helping graph learning; privacy/security section on private message sharing. |
| **write / read / forget** | Survey — catalogs write/read graph memories and prune/mask methods (AgentPrune, AGP) from literature. |
| **conflict** | Silent as survey focus; coordination graphs may encode disagreements indirectly. |
| **privacy** | Section IX-C: data privacy for private-domain message passing; patient privacy when agents share. |
| **Kedger lessons** | (1) Map Kedger S5 graph ops onto survey axes (plan/exec/memory/coord). (2) AgentPrune-style low-rank edge mask for coordination budget. (3) Privacy-preserving edge share for multi-agent seal. (4) Use survey as pointer index — no invent mechanisms beyond cited leaves. |
| **metric_impact** | Survey — no single score; taxonomy coverage of graph×agent functions |
| **refine_candidate** | **no (survey; cite leaves for tickets)** |

---

### 5. WebSailor — Post-Training for Superhuman Web Information-Seeking
**arXiv:2507.02592** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Open-source agents lack proprietary DeepResearch-style uncertainty reduction on BrowseComp-hard search. |
| **representation** | SailorFog-QA high-uncertainty graph-synthesized tasks; reconstruct concise action-oriented thoughts from expert LRM traces; RFT cold start; DUPO (Duplicating Sampling Policy Optimization) agentic RL. |
| **write / read / forget** | Read: browse tools in ReAct-like loop. Write: RFT+RL policy. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Modest RFT cold start required before web RL (don't skip SFT entirely). (2) Reconstruct clean thoughts — don't clone verbose expert style into S8. (3) Synthesize high-uncertainty tasks for train. (4) Match proprietary BrowseComp-level with open DUPO pipeline. |
| **metric_impact** | Closes gap to proprietary on BrowseComp-en/zh; beats open ReAct+R1 browse baselines |
| **refine_candidate** | **yes — S7 RFT cold-start + DUPO for hard browse** |

---

### 6. EvoAgentX — Evolving Multi-Agent Workflows (TextGrad/AFlow/MIPRO)
**arXiv:2507.03616** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S4, S8 |
| **problem** | MAS frameworks need manual workflows; lack unified evolution of prompts/tools/topology. |
| **representation** | Five layers (components/agent/workflow/evolving/eval); evolving layer runs TextGrad, AFlow, MIPRO to refine prompts, tools, topologies; HotPotQA/MBPP/MATH/GAIA. |
| **write / read / forget** | Write: evolved prompts/workflows. Read: execute workflows. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Evolve workflow topology + prompts as first-class promote targets. (2) TextGrad helps multi-hop F1; AFlow code pass@1 — pick optimiser by task. (3) +7.44 F1 HotPotQA; +10 pass@1 MBPP; +10 MATH; up to +20 GAIA. (4) Unified eval layer before accepting evolved graph. |
| **metric_impact** | +7.44% HotPotQA F1; +10% MBPP pass@1; +10% MATH; ≤+20% GAIA |
| **refine_candidate** | **yes — S4 evolving workflow optimiser loop** |

---

### 7. PyVision — Agentic Vision with Dynamic Python Tool Generation
**arXiv:2507.07998** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Visual agents stuck with static toolsets/predefined workflows; can't invent task-specific tools. |
| **representation** | Multi-turn MLLM framework: generate/execute/refine Python tools on the fly; tooling taxonomy; V*/VLMsAreBlind etc. |
| **write / read / forget** | Write: ephemeral Python tools in session. Read: execute tools on images. Forget: tools are session-scoped (not persisted as paper focus). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Allow S1 dynamic tool synthesis under sandbox, not only fixed tool ACL. (2) Persist successful tools as L3 only after refine+eval. (3) +7.8% GPT-4.1 on V*; +31.1% Claude-4 Sonnet on VLMsAreBlind-mini. (4) Taxonomy of generated tools → audit fixtures. |
| **metric_impact** | +7.8% V* (GPT-4.1); +31.1% VLMsAreBlind-mini (Claude-4.0-Sonnet) |
| **refine_candidate** | **no (vision tooling; sandbox-tool lesson only)** |

---

### 8. TIM / TIMRUN — Thread Inference + Subtask Pruning Beyond Context Limits
**arXiv:2507.16784** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7, S8 |
| **problem** | Linear context limits bottleneck long-horizon reasoning accuracy/efficiency. |
| **representation** | TIM: recursive reasoning trees (task/thought/subtask/conclusion); TIMRUN runtime keeps working-memory KV of relevant tokens via rule-based subtask pruning; multi-hop tools in one inference; up to 90% KV manipulated. |
| **write / read / forget** | Write: structured tree nodes during generation. Read: working memory KV subset. Forget: prune completed/irrelevant subtask KV — can reduce hallucination. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Model why as tree depth×length, not flat CoT buffer. (2) Subtask pruning = WorkingState eviction without accuracy loss. (3) Maintain only relevant KV — S2 pressure valve. (4) Throughput holds while manipulating ≤90% KV. |
| **metric_impact** | Pruning preserves/improves accuracy; sustains throughput with ≤90% KV ops |
| **refine_candidate** | **yes — S2 subtask-pruned working KV / why trees** |

---

### 9. MADES — Memory-Augmented Agents for Journalism Audience Framing
**arXiv:2507.21055** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S8 |
| **problem** | Comprehensive news spans domains; audiences lack cross-domain context — need adaptive framing aids. |
| **representation** | MADES: diverse occupation/age agents with memory discuss news; monitor confusion; generate supplementary materials; human quiz + rating eval. |
| **write / read / forget** | Write: agent memories of discussion. Read: recall during simulated talk. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent on PII; journalism audience simulation. |
| **Kedger lessons** | (1) Multi-persona memory agents surface comprehension gaps before S8 explain. (2) Supplement materials grounded in discussion confusion points. (3) Human quiz: MADES supplement 85.7% vs control 64.5% vs vanilla LLM 69.2%. (4) Cosine comprehension metric as eng-judgment SLI. |
| **metric_impact** | Quiz accuracy 85.7% (MADES) vs 64.5% control vs 69.2% vanilla LLM |
| **refine_candidate** | **no (journalism UX; quiz metric idea only)** |

---

### 10. Graph-Augmented LLM Agents — Survey of Progress & Prospects
**arXiv:2507.21407** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | LLM agents weak at reliable planning, long-term memory, tool management, multi-agent coord — graphs proposed as structure. |
| **representation** | Survey of graph-augmented agent methods across planning/memory/tools/coordination; GitHub resource collection. |
| **write / read / forget** | Survey of literature write/read graph memories — no new system. |
| **conflict** | Silent beyond citing conflict-aware RAG leaves. |
| **privacy** | Silent in abstract; follow cited leaves. |
| **Kedger lessons** | (1) Prefer graph-structured memory for long-horizon plan/tool graphs. (2) Use survey to avoid reinventing S5 patterns. (3) Multi-agent coordination graphs for sealed multi-party hydrate. (4) No invented metrics — track cited benchmarks when porting. |
| **metric_impact** | Survey — qualitative coverage of graph-augmented agent tasks |
| **refine_candidate** | **no (survey)** |

---

### 11. Agent Lightning — Decoupled RL Training for Any AI Agent
**arXiv:2508.03680** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S4 |
| **problem** | RL training tightly couples to agent impl or uses brittle sequence masking — hard to train arbitrary agents. |
| **representation** | Unified data interface (state/call/reward/dataset); MDP formulation; complete decoupling of agent execution from RL training loop; works across agent frameworks. |
| **write / read / forget** | Write: training transitions via unified interface. Read: agent emits states/calls. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Decouple agent runtime from trainer — Kedger can emit transition logs without embedding RL. (2) Unified state/call/reward schema for promote datasets. (3) Avoid concat+mask hacks for multi-call agents. (4) Apply RL to existing tool agents without rewrite. |
| **metric_impact** | Framework paper — enables RL on arbitrary agents; see expts in paper body |
| **refine_candidate** | **yes — S1 transition-log interface for offline RL** |

---

### 12. SEAgent — Self-Evolving Computer-Use Agent from Experience
**arXiv:2508.04700** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | CUAs fail on novel specialized software lacking human annotations. |
| **representation** | Agentic self-evolution: autonomous learn from experience on computer-use tasks without human labels; LVLM CUA loop; experience-driven improvement. |
| **write / read / forget** | Write: experience from autonomous trials. Read: reuse for later software tasks. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Self-evolve CUAs via experience when demos missing. (2) Gate promote of computer-use skills after success validation. (3) Separate novel-software namespace until proven. (4) Measure transfer to unseen apps as SLI. |
| **metric_impact** | Paper reports gains on specialized software vs non-evolving CUAs (see tables) |
| **refine_candidate** | **yes — S3/S4 self-evolve from computer-use experience** |

---

### 13. Narrative Memory MAS — Multi-Agent Arc Extraction in Serialized TV
**arXiv:2508.07010** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S5, S8 |
| **problem** | Serialized TV narratives need sophisticated info management across temporally distributed arcs. |
| **representation** | MAS with episodic/semantic/working memory roles; agents for season arcs, anthology arcs, character networks; precision on arc types. |
| **write / read / forget** | Write: arc/character memory stores. Read: memory-informed extraction workflow. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Specialize agents by memory type (episodic/semantic/working). (2) Character entity graph as S5. (3) Arc extraction precision 89.3% anthology (25/28); 62 entities / 61 correct. (4) Evaluate memory components jointly, not only end accuracy. |
| **metric_impact** | Anthology arc precision 89.3%; 61/62 character entities correct |
| **refine_candidate** | **no (TV narrative domain)** |

---

### 14. Survey — Self-Evolving AI Agents (MASE Framework)
**arXiv:2508.07407** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S6 |
| **problem** | Most agents static post-deploy; need lifelong self-evolution from interaction feedback. |
| **representation** | Unified MASE conceptual framework: System inputs, Agent System, Environment, Optimisers; reviews evolution of models/prompts/memory/tools/workflows/communication; domain-specific + safety/ethics. |
| **write / read / forget** | Survey of write/read/optimise loops across literature; memory evolution as a component class. |
| **conflict** | Silent as taxonomy; safety section covers risks. |
| **privacy** | Dedicated safety/ethics discussion for evolving agents. |
| **Kedger lessons** | (1) Treat memory/tools/workflows as evolvable under optimiser, with promote gates. (2) Feedback loop abstraction matches Kedger cognify→promote. (3) Safety constraints on self-evolution (Asimov-inspired discussion). (4) Use as map — open tickets only from concrete cited methods. |
| **metric_impact** | Survey framework — task-specific metrics (acc/F1/SR) per cited system |
| **refine_candidate** | **no (survey)** |

---

### 15. Memory Decoder — Pretrained Plug-and-Play Domain Memory
**arXiv:2508.09874** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | DAPT costly + catastrophic forgetting; RAG kNN search slow for domain adaptation. |
| **representation** | Small transformer decoder pretrained as plug-and-play memory; interpolates with base LM; no base param change; cross-model/vocab adaptation; beats In-Context RAG & kNN-LM on overhead. |
| **write / read / forget** | Write: pretrain Memory Decoder on domain. Read: plug at inference (α interpolate). Forget: avoids catastrophic forgetting by not updating base. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) External neural memory adapter vs finetune base — preserves general skills. (2) 1.28× overhead << kNN-LM 2.17× / IC-RAG 1.51×. (3) Cross-vocab adapt with 10% train budget. (4) Still not symbolic Anchors — use when auditability secondary. |
| **metric_impact** | 1.28× overhead; 124M decoder on GPT2-medium beats DAPT; best avg on 9 downstream tasks |
| **refine_candidate** | **no (neural plug-in; symbolic pack preferred for audit)** |

---

### 16. AgentMental — Multi-Agent Explainable Mental Health Assessment
**arXiv:2508.11567** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S8 |
| **problem** | Automated psych assessment lacks interactive clinician-like dialogue, adequacy checks, structured memory. |
| **representation** | Agents for questioning, adequacy eval, scoring, updating; adaptive follow-ups; tree memory (root demographics, children symptom topics/statements); DAIC-WOZ. |
| **write / read / forget** | Write: tree memory updates each turn. Read: track topics to reduce redundant questions. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Highly sensitive mental-health dialogue — needs strict Inv-Scope (paper clinical setting). |
| **Kedger lessons** | (1) Tree-structured session memory by symptom topic. (2) Adequacy agent before next question — abstain/follow-up. (3) S8 explainability via scored structured nodes. (4) Treat mental-health content as private_raw — never share packs. |
| **metric_impact** | DAIC-WOZ effectiveness shown (see paper tables for exact scores) |
| **refine_candidate** | **no (clinical domain; privacy lesson only)** |

---

### 17. MCP-Universe — Real-World MCP Server Agent Benchmark
**arXiv:2508.14704** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Existing MCP/tool benches too simple; miss long-horizon + large unfamiliar tool spaces. |
| **representation** | 6 domains / 11 real MCP servers (nav, repos, finance, 3D, browser, web search); execution-based format/static/dynamic evaluators; long-context growth with steps. |
| **write / read / forget** | Eval read/execute against real MCP APIs. Write: none. Forget: silent. |
| **conflict** | Silent. |
| **privacy** | Auth to real servers — credential hygiene implied. |
| **Kedger lessons** | (1) Fixture suite against real MCP servers, not mocks only. (2) Execution-based graders > LLM judges. (3) GPT-5 43.72% / Grok-4 33.33% / Claude-4 Sonnet 29.44% — tool hydrate unsolved. (4) Track token growth vs steps as S2 pressure SLI. |
| **metric_impact** | Success: GPT-5 43.72%; Grok-4 33.33%; Claude-4.0-Sonnet 29.44% |
| **refine_candidate** | **yes — S7 MCP-Universe real-server fixtures** |

---

### 18. CARE — Conflict-Aware Soft Prompting for RAG
**arXiv:2508.15253** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S7, S8 |
| **problem** | Context–memory conflict: incorrect retrieved context overrides correct parametric knowledge. |
| **representation** | CARE: context assessor (from base LLM) encodes context → soft memory embeddings; reconstruction pretrain then conflict-aware finetune with grounded/adversarial soft prompts; guides which knowledge source to trust. |
| **write / read / forget** | Read: assessor encodes retrieved context to soft prompts. Write: train assessor params. Forget: silent. |
| **conflict** | Core: context–memory conflict; avg +5.0% on QA/fact-checking when mitigated. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Explicit context assessor before hydrate compose. (2) Adversarial soft prompts teach distrust of bad Evidence. (3) Soft context embeddings ≠ raw doc dump into WorkingState. (4) +5% avg — ConflictSet should include parametric-vs-context axis. |
| **metric_impact** | +5.0% average on QA and fact-checking benchmarks |
| **refine_candidate** | **yes — S7 CARE-style context–memory conflict assessor** |

---

### 19. CFGM — Coarse-to-Fine Grounded Memory for Agent Planning
**arXiv:2508.15305** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7, S8 |
| **problem** | Single-granularity memory from env interaction limits diversity/flexibility; costly to train agents. |
| **representation** | CFGM: ground env → coarse focus points for experience collection; ground hybrid-grained tips from experiences; retrieve tips+experiences at infer; on anomalies ground fine key info → self-QA reflect/correct. |
| **write / read / forget** | Write: focus points, tips, experiences. Read: retrieve task-relevant tips/experiences. Forget: silent. |
| **conflict** | Silent on SUPERSEDES; reflection corrects plans under anomalies. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Multi-granularity memory (coarse focus → tips → fine keys). (2) Anomaly → fine grounded self-QA before continue. (3) AlfWorld SR 91.00% vs ExpeL+QuBE 85.07%. (4) Tips from success+failure trajectories — promote both. |
| **metric_impact** | AlfWorld SR 91.00%; WebShop reward 85.0; ScienceWorld 57%; stronger than ExpeL/AutoGuide/QuBE |
| **refine_candidate** | **yes — S3/S7 coarse-to-fine grounded memory** |

---

### 20. Learn to Memorize — Adaptive Memory Cycles with MoE Gate
**arXiv:2508.16629** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Hand-designed agent memories ignore memory-cycle effects; labor-heavy and suboptimal per env. |
| **representation** | Model memory cycles: MoE gate for retrieve; learnable aggregation for utilization; task-specific reflection for storage; off-policy + on-policy optimization; EM reward. |
| **write / read / forget** | Write: reflection-adapted storage from success/fail. Read: MoE-gated retrieve + learned aggregate. Forget: implicit via learned storage policy / filtering successes by reward threshold β_r. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Learn retrieve/aggregate/store policies per env — not fixed MemoryBank. (2) Memory-cycle effect as first-class training signal. (3) On-policy optimize often best. (4) Reflect separately on success vs fail before storage promote. |
| **metric_impact** | On-policy variant outperforms baselines on most settings; EM as trajectory reward |
| **refine_candidate** | **yes — S3 learned MoE memory-cycle policies** |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (honest deep-recard) | 20 |
| Cumulative FULL | **500** |
