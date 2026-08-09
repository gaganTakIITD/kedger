# Batch 17 — Survey Runway FULL (Kedger) — **honest deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Body-grounded mechanism cards (Intro/Method/Results) replacing 2026-08-08 abstract-template cards.  
> **Progress:** FULL 320 → **340**.  
> **Method:** Fulltext `/tmp/kedger-papers/full/{id}.txt` + agent deep-read cards.  
> **Kedger stages:** S1–S8  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers from body only.


---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body deep-read; deep-recard upgrade of Batch17) | **20** | `2508.10419`, `2508.12379`, `2508.15294`, `2509.21212`, `2509.23040`, `2510.01353`, `2510.13614`, `2510.19897`, `2510.21618`, `2511.10030`, `2511.20857`, `2512.12856`, `2512.20092`, `2512.20237`, `2512.20745`, `2601.04726`, `2601.07468`, `2602.07624`, `2302.04023`, `2305.14938` |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs cached |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards

### 1. ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning
**arXiv:2508.10419** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Stateless single-step RAG fails on long novels where plot, veridical details, and evolving relations require stateful metacognitive retrieval. |
| **representation** | ComoRAG: veridical layer (raw chunks), summary nodes, episodic layer (plotline); metacognitive regulation with Dynamic Memory Workspace — probe/retrieve/integrate loop over global memory pool across steps. |
| **write / read / forget** | Write: maintain global memory pool M_pool across iterative steps with newly retrieved info. Read: adaptive probes over veridical/summary/episodic layers. Forget: Silent. |
| **conflict** | Discusses integrating contradictory narrative evidence (e.g., Snape protects/bullies Harry); soft reasoning, not typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Narrative hydrate needs veridical vs episodic layers, not one chunk index. (2) Metacognitive probe loop = mid-turn S7 re-hydrate on gaps. (3) Relative gains up to ~11% vs strongest RAG baseline; other reported lifts include +24.6% class improvements in analyses. (4) Keep memory workspace stateful across retrieval iterations. |
| **metric_impact** | Consistent relative gains up to ~11% vs strongest baseline on 200K+ token narrative benchmarks; analyses cite additional lifts (e.g., +24.6% in reported comparisons). |
| **refine_candidate** | **yes — stateful metacognitive narrative hydrate** |

---

### 2. GraphCogent: Mitigating LLMs’ Working Memory Constraints via Multi-Agent Collaboration in Complex Graph Understanding
**arXiv:2508.12379** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S5, S7, S8 |
| **problem** | LLMs fail real-world large-graph queries (e.g., 9/10 wrong web paths) because working memory cannot retain topology across long multi-step reasoning. |
| **representation** | GraphCogent: multi-agent collaboration over Graph4real-style tasks; tool-augmented graph algorithms; Graph N-back (50-edge subsets) probes topology retention; agents offset LLM working-memory limits. |
| **write / read / forget** | Write: intermediate agent/tool state for graph exploration. Read: tools/algorithms over graph subsets. Forget: topology forgetting measured as failure mode (Section 4.2). |
| **conflict** | Silent on typed SUPERSEDES (decision preference conflicts noted anecdotally). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Don’t stuff whole graphs into WorkingState — agent+tool decomposition. (2) Graph N-back-style probes for S2 topology retention SLIs. (3) Qwen2.5-1.5–8B GraphCogent: ~50% improvement over DeepSeek-R1-scale baselines; +20% accuracy vs agent baseline with −80%/−30% tokens (in/out toolset). (4) Measure topology forgetting explicitly. |
| **metric_impact** | ~50% improvement vs massive LLMs like DeepSeek-R1 (671B) in reported setting; +20% accuracy vs strong agent baseline; −80% tokens (in-toolset) / −30% (out-toolset). |
| **refine_candidate** | **yes — multi-agent graph working-memory offload** |

---

### 3. Multiple Memory Systems for Enhancing the Long-term Memory of Agent
**arXiv:2508.15294** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7 |
| **problem** | MemoryBank/A-MEM-style stores have poor memory-content quality, hurting recall and response quality on long agent histories. |
| **representation** | MMS (Multiple Memory Systems): process STM → multiple LTM fragments inspired by Tulving; build paired retrieval memory units and contextual memory units (1:1); semantic vs other memory-type separation for task-stage needs. |
| **write / read / forget** | Write: convert STM into typed LTM fragments + paired retrieval/context units. Read: retrieval units for relevance; contextual units for generation. Forget: discusses mitigating catastrophic forgetting via continuous learning framing. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent (HTML footer only). |
| **Kedger lessons** | (1) Split retrieve-keys from generate-context payloads (paired units). (2) Tulving-inspired typing (semantic/episodic) at S3. (3) Reported EM improvements on 200-question eval (e.g., EM figures in mid-20s vs weaker baselines; up to ~11-point class gains in tables). (4) Content-quality gate before promote beats dumping raw history. |
| **metric_impact** | 200-question eval; EM examples in tables include ~24.82–30.71 range across systems; MMS improves over MemoryBank/A-MEM class baselines. |
| **refine_candidate** | **yes — paired retrieval/context memory units** |

---

### 4. SGMem: Sentence Graph Memory for Long-Term Conversational Agents
**arXiv:2509.21212** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7 |
| **problem** | Coarse session/turn/summary memory segmentation fragments evidence and weakens retrieval across dialogue granularities. |
| **representation** | SGMem: sentence-level graph over sessions/rounds/turns/generated memories; construction & management plus usage (retrieve memory and sentences); membership edges link chunks to constituent sentences. |
| **write / read / forget** | Write: sentence-graph construction from dialogue + generated memories. Read: retrieve memories and supporting sentences. Forget: Silent. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent (graph 'membership' edges are structural, not privacy ACL). |
| **Kedger lessons** | (1) Default memory node granularity = sentence, not whole session. (2) Keep edges from summaries back to source sentences for S8 grounding. (3) Multi-granularity retrieve (session↔sentence) for LoCoMo/LongMemEval. (4) Generated-memory nodes must remain linked to raw turns. |
| **metric_impact** | LongMemEval/LoCoMo results in §4 (accuracy tables); case study RAG-SMFI on LongMemEval. |
| **refine_candidate** | **yes — sentence-graph memory granularity** |

---

### 5. Look Back to Reason Forward: Revisitable Memory for Long-Context LLM Agents
**arXiv:2509.23040** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7, S8 |
| **problem** | Memorize-while-reading linear scans prune latent evidence, overwrite useful memory, and cannot revisit earlier document regions for long-context QA. |
| **representation** | ReMemR1: MDP memory agent with history-augmented state; RL multi-level rewards (trajectory outcome + step action shaping); memory callback actions to revisit prior content (vs forward-only MemAgent). |
| **write / read / forget** | Write: update memory buffer while reading. Read: callback/revisit prior memory/document spans. Forget: overwriting is identified as failure of forward-only baselines; selective retention via RL. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Discusses privacy/security considerations of long-horizon store/recall systems at a high level. |
| **Kedger lessons** | (1) S7 long-doc hydrate needs revisit/callback, not only append scans. (2) Multi-level RL rewards (answer + evidence + behavior) inform pack-compile training. (3) Reported scores include 80.8%/38.3%/31.3%/50.3% class results across settings. (4) Failure modes: recall collapse & memory pollution → monitoring SLIs. |
| **metric_impact** | Reported long-context results include 80.8%, 38.3%, 31.3%, 50.3% (plus 29.9%/32%) across evaluated settings vs forward-only memorize-while-reading agents. |
| **refine_candidate** | **yes — revisitable memory callbacks for long-context** |

---

### 6. Memtrack: Evaluating Long-Term Memory and State Tracking in Multi-Platform Dynamic Agent Environments
**arXiv:2510.01353** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7, S8 |
| **problem** | Memory benchmarks are conversation-centric and miss dynamic multi-platform enterprise workflows with async events and state tracking. |
| **representation** | Memtrack benchmark: multi-platform org workflows (messages/code/docs); noisy/conflicting cross-referred info; manual+agent-synthesized instances; metrics for correctness/state tracking; forget/retain ability noted as understudied. |
| **write / read / forget** | Write: N/A (benchmark of agent memory systems). Read: agents must track state across platforms. Forget: identified as understudied capability to evaluate. |
| **conflict** | Instances include noisy, conflicting, cross-referring information — conflict-resolution stress test; no single SUPERSEDES API. |
| **privacy** | Team-membership style tool APIs in environment; not a privacy mechanism paper. |
| **Kedger lessons** | (1) Enterprise memory eval ≠ LoCoMo chat — need multi-platform state fixtures. (2) Best GPT-5 only ~60% Correctness on Memtrack — headroom SLI. (3) Conflict/noise built into tasks → ConflictSet eval. (4) Explicit forget/retain tests should be added to Kedger harness. |
| **metric_impact** | Best GPT-5 ≈ 60% Correctness on Memtrack; other models lower (e.g., reported EM-like scores including ~0.144 class failures). |
| **refine_candidate** | **yes — multi-platform state-tracking eval** |

---

### 7. MemoTime: Memory-Augmented Temporal Knowledge Graph Enhanced Large Language Model Reasoning
**arXiv:2510.13614** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | TKGQA plan-retrieve-answer pipelines fail on multi-entity temporal operators, evidence conflicts, and lack reusable temporal experience. |
| **representation** | MemoTime: temporal grounding → Tree of Time hierarchical temporal reasoning → temporal evidence retrieval/pruning → Experience Memory for reusable temporal strategies. |
| **write / read / forget** | Write: experience memory of temporal reasoning patterns; TKG facts as structured store. Read: retrieve/prune temporal evidence along Tree of Time. Forget: pruning removes irrelevant temporal evidence (not user unshare). |
| **conflict** | Notes exclusive/contradictory temporal facts causing bad chains; pruning/evidence selection mitigates — not typed SUPERSEDES. |
| **privacy** | Silent (related-work privacy cite only). |
| **Kedger lessons** | (1) Temporal questions need a Tree-of-Time plan object in S8, not flat retrieve. (2) Experience Memory for temporal operators as procedural Anchors. (3) Up to ~24.0% gains reported; other scores e.g. 77.9%/68.2%/71.4%/74.5% class results. (4) Explicit prune step before answer. |
| **metric_impact** | Up to ~24.0% improvement reported; additional temporal QA scores in mid-60s–70s% across settings. |
| **refine_candidate** | **yes — Tree-of-Time temporal hydrate** |

---

### 8. Learning from Supervision with Semantic and Episodic Memory: A Reflective Approach to Agent Adaptation
**arXiv:2510.19897** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Agents need to learn classification behaviors from labeled examples without weight updates, while remaining flexible and interpretable. |
| **representation** | Memory-augmented critiques: episodic memory stores instance-level critiques; semantic memory stores abstracted rules; combine both at inference; critique-based methods vs label-only baselines; reduces thinking tokens for reasoning models. |
| **write / read / forget** | Write: store critiques into episodic and/or semantic memory from labeled supervision. Read: retrieve critiques/rules for new inputs. Forget: Silent (contrasts with fine-tune catastrophic forgetting). |
| **conflict** | Notes models may accept false critiques that contradict knowledge — integrity risk, not SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Promote both instance critiques and abstracted semantic rules. (2) Non-parametric critique memory avoids fine-tune forgetting. (3) Critique methods outperform across most configs (e.g., 56.2%/74%/81.6% class results; +4.6 points cited). (4) Guard against poisoned critiques in S4 promote. |
| **metric_impact** | Critique-based methods beat baselines on Multi-Condition Ranking/NFCorpus settings; examples include 56.2%, 74%, 81.6%, +4.6 points; critiques cut thinking tokens vs EP_LABEL. |
| **refine_candidate** | **yes — episodic+semantic critique memory** |

---

### 9. DeepAgent: A General Reasoning Agent with Scalable Toolsets
**arXiv:2510.21618** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7, S8 |
| **problem** | Workflow-locked agents can’t globally plan with large toolsets over long horizons; interactive memory isn’t autonomously managed inside deep reasoning. |
| **representation** | DeepAgent: end-to-end deep reasoning with autonomous tool search/call; Memory Fold action compresses interaction history into structured memory; brain-inspired memory schema; ToolPO end-to-end RL. |
| **write / read / forget** | Write: Memory Fold compresses history into structured summary memory. Read: folded memory + tools inside ongoing reasoning. Forget: fold replaces verbose history (compression), not tombstone unshare. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Add explicit Memory Fold action to S2 under context pressure. (2) Tool search inside reasoning loop, not fixed MCP preload. (3) Reported scores include 89.0%/75.4%/55.0%/52.6% class results across agent benchmarks. (4) End-to-end RL (ToolPO) for tool+memory policy co-training. |
| **metric_impact** | Benchmark tables report up to ~89.0%/75.4% class scores and other mid-range results (55.0%/52.6%/64.0%/40.6%); up to ~6.0% / +5.2% gains in comparisons. |
| **refine_candidate** | **yes — Memory Fold action under context pressure** |

---

### 10. Multi-agent In-context Coordination via Decentralized Memory Retrieval (MAICC)
**arXiv:2511.10030** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7 |
| **problem** | Decentralized MARL/ICL agents misalign on credit assignment and task context, limiting cooperative adaptation at test time. |
| **representation** | MAICC: train multi-agent trajectory embedding models; decentralized memory retrieval balancing online test-time data with offline memory; hybrid utility score mixing individual and team returns for credit assignment. |
| **write / read / forget** | Write: offline multi-agent trajectory memory. Read: decentralized retrieve of coordination context at test time. Forget: Silent (balancing online vs offline implies replacement pressure). |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Multi-agent Kedger deployments need team-level utility in retrieve scoring. (2) Decentralized memory retrieve for coordination, not shared megacontext. (3) Faster adaptation on ALFWorld/SMAC vs priors. (4) Trajectory embeddings as first-class memory keys. |
| **metric_impact** | Improved adaptation speed/quality on ALFWorld and SMAC v1/v2 vs existing methods (paper figures; 95% CI reporting in plots). |
| **refine_candidate** | **no** |

---

### 11. Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory
**arXiv:2511.20857** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Memory evals focus on static conversational retrieve; they miss agents that accumulate and reuse experience across evolving task streams at test time. |
| **representation** | Evo-Memory benchmark: Search/Synthesis/Evolve loop; baselines ExpRAG (experience retrieval+aggregation) and ReMem (reason+act+memory); analyzes easy→hard sequences, feedback, and memory pruning. |
| **write / read / forget** | Write: evolve/synthesize experience memory across task stream. Read: retrieve prior experience for new tasks. Forget: memory pruning analyzed as ablation/component. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Dataset prep filters leakage/ambiguity; not a user-privacy system. |
| **Kedger lessons** | (1) Test-time evolving memory is a distinct SLI from LoCoMo QA. (2) ReMem-style reason-act-memory synergy for agents. (3) Pruning matters — unbounded experience hurts. (4) Easy→hard curriculum ordering affects memory usefulness. |
| **metric_impact** | ExpRAG/ReMem beat static baselines on evolving streams (e.g., ExpRAG Eco/Eng cells 0.70/0.85 vs Baseline 0.55/0.84 on Claude 3.7 Sonnet table). |
| **refine_candidate** | **yes — evolving experience-memory eval + prune** |

---

### 12. Forgetful but Faithful: A Cognitive Memory Architecture and Benchmark for Privacy-Aware Generative Agents
**arXiv:2512.12856** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6, S7 |
| **problem** | Generative agents must forget under budget and privacy (right-to-be-forgotten) while remaining narratively faithful — most stores lack policy-addressable retention. |
| **representation** | MaRS: typed episodic/semantic/social/task memories with provenance, retention scores, budget partitions; six forgetting policies (FIFO, LRU, Priority Decay, Reflection-Summary, Random-Drop, Hybrid) including privacy-aware policies; FiFA benchmark (coherence, goals, social recall, privacy preservation, cost). |
| **write / read / forget** | Write: typed MaRS nodes with provenance + retention score. Read: indexed retrieve under budget. Forget: first-class — six policies + privacy-aware erasure/retention control (core contribution). |
| **conflict** | Narrative coherence metric penalizes contradictions after forgetting; not typed SUPERSEDES links. |
| **privacy** | Core paper: privacy-aware forgetting policies + FiFA Privacy Preservation metric; right-to-be-forgotten framing. |
| **Kedger lessons** | (1) S6 unshare needs policy-addressable retention scores, not ad-hoc delete. (2) FiFA-style multi-metric: faithfulness under forget, not EM alone. (3) Hybrid forget policy often best tradeoff per paper analysis. (4) Provenance/audit fields mandatory for privacy erase proofs. |
| **metric_impact** | Hybrid policy best composite ≈0.911 on FiFA; Composite=0.25 NC + 0.25 GCR + 0.20 SRA + 0.15 PP + 0.15 CE. |
| **refine_candidate** | **yes — MaRS retention scores + privacy-aware forget policies** |

---

### 13. Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi-session Agents
**arXiv:2512.20092** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | As multi-session histories grow noisy, models fail to select temporally pertinent evidence for temporal QA. |
| **representation** | Memory-T1: coarse-to-fine retrieval then RL fine-grained session selection; multi-level rewards — Accuracy Ra, Evidence Grounding Rg, Temporal Consistency Rt. |
| **write / read / forget** | Write: memory pool from multi-session dialogues (assumed existing store). Read: coarse retrieve then RL select evidence sessions. Forget: Silent (noise accumulation motivated but not a forget API). |
| **conflict** | Temporal consistency reward penalizes inconsistent timelines; not typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Temporal hydrate = coarse recall + learned fine select, not top-k embed only. (2) Reward temporal consistency separately from answer EM. (3) Reported ~67.0% with gains e.g. +10.2% / +23.4% class improvements in tables. (4) Grounding reward Rg ties S8 why to selected sessions. |
| **metric_impact** | ~67.0% reported; gains vs baselines include ~+10.2% and up to ~+23.4% in evaluated settings; 716-example scale cited. |
| **refine_candidate** | **yes — RL temporal evidence selection** |

---

### 14. MemR3: Memory Retrieval via Reflective Reasoning for LLM Agents
**arXiv:2512.20237** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Deployed memory systems over-optimize compression/storage and under-specify closed-loop control of retrieval quality. |
| **representation** | MemR3: router chooses among retrieve / reflect / answer; Global Evidence-Gap Tracker makes missing evidence explicit; LangGraph nodes; compatible with existing stores; LoCoMo protocol re-alignment discussion. |
| **write / read / forget** | Write: none required (retrieval controller over existing memories). Read: iterative retrieve until gap tracker satisfied or answer. Forget: Silent (mentions catastrophic forgetting of parametric updates in related work). |
| **conflict** | Robustness tests inject noisy/contradictory memories and measure routing impact — conflict-aware eval, not SUPERSEDES types. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S7 should be a retrieve/reflect/answer router, not single-shot. (2) Evidence-gap tracker is an explicit WorkingState object for S8. (3) LoCoMo scores in ~74–81% range across backends (e.g., 74.62–81.55%). (4) Re-check LoCoMo eval protocol bugs before trusting leaderboards. |
| **metric_impact** | LoCoMo results ~74.62%/76.26%/75.54%/81.55%/76.32%/78.94%/80.88%/79.46% across configurations; ablations on n_chk / n_max / iterations. |
| **refine_candidate** | **yes — evidence-gap tracker + retrieve/reflect router** |

---

### 15. AgentMath: Empowering Mathematical Reasoning for Large Language Models via Tool-Augmented Agent
**arXiv:2512.20745** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Long-CoT LRMs are inefficient and inaccurate on problems needing precise computation; tool-integrated math agents lack scalable RL training. |
| **representation** | AgentMath: NL CoT→tool-augmented trajectory data; agentic RL interleaving language with code interpreter; training systems (async rollout, agentic partial rollout, prefix-aware load balancing) for 4–5× speedup. |
| **write / read / forget** | Write: none persistent memory — trajectory rollouts for training. Read: code interpreter tools during reasoning. Forget: Silent. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Semantic similarity filtering to prevent train/eval leakage. |
| **Kedger lessons** | (1) Math hydrate should interleave code tools, not pure CoT. (2) Partial rollout engineering matters for long tool traces. (3) AgentMath-30B-A3B attains very high AIME/HMMT scores (paper cites ~90% class on competition sets). (4) Leakage controls for eng-judgment datasets. |
| **metric_impact** | SOTA on AIME24/AIME25/HMMT25; AgentMath-30B-A3B ~90%+ class on reported competition benchmarks; 4–5× RL training speedup. |
| **refine_candidate** | **no** |

---

### 16. Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning
**arXiv:2601.04726** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | Flat similarity memory fails long-horizon agents that need event structure and logical navigation over past experiences. |
| **representation** | Event-centric hierarchical memory as a logic map; incremental hierarchical construction; Active Multi-Path Memory Search with Planner/Explorer/Responder agents collecting evidence across paths. |
| **write / read / forget** | Write: incremental hierarchical event memory construction. Read: multi-path planner/explorer search then respond. Forget: Silent. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Store events as navigable logic-map nodes, not flat embeddings. (2) Multi-path explorer search for S7 over event graphs. (3) Reported scores e.g. 47.92%/52.18%/57.96%/48.93%/52.52% class results. (4) Planner vs explorer separation clarifies S8 traces. |
| **metric_impact** | Event-centric method reaches 57.96 / 50.51 / 52.18 on reported columns vs flat Mem0/MemoryOS/HippoRAG/A-Mem baselines (table §5). |
| **refine_candidate** | **yes — event-centric logic-map memory** |

---

### 17. Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents
**arXiv:2601.07468** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Personal agent memories keyed by dialogue time mis-order real-world occurrence time and lose durative states/patterns. |
| **representation** | Build semantic timeline (occurrence time) from episodic memory; consolidate into time-aware durative memory; semantic-time guided utilization; hierarchical update ops DUPLICATE/ADD/INVALIDATE/UPDATE. |
| **write / read / forget** | Write: episodic → durative consolidation on semantic timeline. Read: retrieve under semantic-temporal constraints matching query temporal intent. Forget: INVALIDATE operation as first-class update alongside ADD/UPDATE. |
| **conflict** | Silent on typed SUPERSEDES (INVALIDATE is closest). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Distinguish dialogue time vs event occurrence time in Anchor timestamps. (2) Durative memories for persistent states, not only point facts. (3) INVALIDATE/UPDATE ops align with Kedger promote graph. (4) Gains ~74.80% with +20.30%/+22.56% class lifts reported. |
| **metric_impact** | ~74.80% / 62.60% class scores; +20.30% / +22.56% improvements; other figures 71.23%/76.69%/63.64%/68.44%/74.8%. |
| **refine_candidate** | **yes — semantic-timeline durative memory + INVALIDATE** |

---

### 18. M2A: Multimodal Memory Agent with Dual-Layer Hybrid Memory for Long-Term Personalized Interactions
**arXiv:2602.07624** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Personalized multimodal agents freeze concepts at init and can’t edit evolving aliases/preferences across weeks of multi-modal dialogue beyond context windows. |
| **representation** | M2A: dual-layer hybrid memory — Layer1 Raw Message Store + Layer2 Semantic Memory Store; tri-path hybrid retrieval; iterative write-back of evolving multimodal concepts during interaction. |
| **write / read / forget** | Write: incremental updates to raw+semantic stores (add/delete/modify guidance). Read: tri-path hybrid retrieval at generation. Forget: delete/modify supported in update policy. |
| **conflict** | Mentions conflicting new vs outdated info during updates; soft update logic, not typed SUPERSEDES. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Keep raw multimodal messages and semantic concept layer separate. (2) Write-back personalization during interaction, not static profiles. (3) Scores e.g. 44.64%/56.48%/33.27%/34.73%/36.26% across ablations/tasks. (4) Tri-path retrieve ablation justifies hybrid keys. |
| **metric_impact** | Reported accuracies/F1-like scores around 30–56% range (e.g., 44.64%, 56.48%, 33.27%); dual-layer and tri-path ablations in §5.3. |
| **refine_candidate** | **yes — editable dual-layer multimodal personal memory** |

---

### 19. A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning, Hallucination, and Interactivity
**arXiv:2302.04023** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S8 |
| **problem** | Interactive LLMs lacked broad quantitative evaluation across multitask/multilingual/multimodal reasoning, factuality/hallucination, and multi-turn interactivity. |
| **representation** | Eval framework over 23 datasets / 8 NLP task families + new multimodal set; measures reasoning categories, factuality vs intrinsic/extrinsic hallucination, and multi-turn prompt-engineering interactivity. |
| **write / read / forget** | Write: N/A (evaluation). Read: model answers under zero/few-shot and multi-turn prompts. Forget: Silent (dialogue example about forgetting user constraints is an interactivity failure case). |
| **conflict** | Hallucination taxonomy includes contradictions with source input (intrinsic). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S8 eng-judgment needs hallucination-type labels (intrinsic vs extrinsic). (2) Multi-turn constraint tracking is a WorkingState SLI (restaurant rating forget example). (3) ~63.41% avg on 10 reasoning categories — baseline for weak reasoners. (4) Multilingual/multimodal axes for fixture diversity. |
| **metric_impact** | ~63.41% average accuracy across 10 reasoning categories; summarization ~8% ROUGE-1; MT ~2% ChrF++ under multi-turn prompt engineering; 23 datasets / 8 tasks. |
| **refine_candidate** | **no** |

---

### 20. Do LLMs Understand Social Knowledge? Evaluating the Sociability of Large Language Models with SocKET
**arXiv:2305.14938** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S8 |
| **problem** | LLMs are deployed in social/conversational settings without a grounded benchmark of social language understanding. |
| **representation** | SocKET: 58 theory-grounded social NLP tasks in five categories of social knowledge; analyzes transfer via multi-task training on correlated vs weakly correlated social tasks. |
| **write / read / forget** | Silent. |
| **conflict** | Silent on typed SUPERSEDES. |
| **privacy** | Silent (task membership categories only). |
| **Kedger lessons** | (1) Persona/social Anchors need SocKET-style competency fixtures. (2) Multi-task transfer helps only for correlated social skills — don’t blindly joint-train. (3) Theory-grounded task taxonomy > ad-hoc vibe checks for S8. (4) Conversational agents should track social-knowledge failures separately from factual EM. |
| **metric_impact** | 58 tasks across five social-knowledge categories; multi-task transfer effects in §6 (correlated tasks help; weakly correlated can hurt). |
| **refine_candidate** | **no** |

---

## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (honest deep-recard) | 20 |
| Cumulative FULL | **340** |
