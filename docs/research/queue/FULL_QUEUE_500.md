# Kedger Track 0 — FULL deep-read queue (≥500)

> **Program:** Kedger research (measure → refine).
> **Honesty rule:** `FULL` only if listed in `CORPUS_INVENTORY.md` §2 ledger.
> `seed_placeholder` entries need fetch — they are **not** FULL deep-reads.
> Legacy labels in older memo bodies are being migrated to Kedger terminology.

## Stats

| Metric | Value |
|--------|------:|
| Unique arXiv IDs scanned | 488 |
| FULL (from inventory) | 500 |
| queued (scanned, not FULL) | 4 |
| seed_placeholder (pad) | 0 |
| **Queue size** | **504** |
| Markdown files scanned | 73 |

## Priority tiers

| Tier | Theme |
|-----:|-------|
| 1 | eval/failure |
| 2 | capture/compaction |
| 3 | episode/boundary |
| 4 | graph/conflict |
| 5 | privacy/capability |
| 6 | eng-judgment |

## Queue

| # | ID | Title hint | Status | Tier | Kedger stages | Refine? |
|--:|----|------------|--------|-----:|---------------|---------|
| 1 | `1809.09600` | HotpotQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 2 | `2002.08909` | REALM — retrieval-augmented LM pre-training | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 3 | `2004.12832` | ColBERT — late interaction dense retrieval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 4 | `2011.01060` | 2WikiMultiHopQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 5 | `2208.03299` | Atlas — retrieval augmented few-shot LM | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 6 | `2212.10509` | IRCoT — interleaved retrieval + CoT | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 7 | `2301.12652` | REPLUG — retrieval-augmented black-box LMs | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 8 | `2302.04023` | A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Re | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 9 | `2303.16634` | G-Eval — GPT-4 NLG evaluation with CoT rubrics | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 10 | `2305.06983` | FLARE / Active Retrieval Augmented Generation | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 11 | `2305.13300` | Adaptive Chameleon (knowledge conflicts) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 12 | `2305.13711` | LLM-Eval: Unified Multi-Dimensional Automatic Evaluation for Open | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 13 | `2305.14938` | Do LLMs Understand Social Knowledge? Evaluating the Sociability o | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 14 | `2305.15852` | Self-contradictory Hallucinations of Large Language Models: Evalu | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 15 | `2307.03172` | Lost in the Middle | FULL | 1 (eval/failure) | episode_cognify,hydrate_retrieve | no |
| 16 | `2307.13854` | WebArena | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 17 | `2308.03688` | AgentBench | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 18 | `2308.04026` | AgentSims: An Open-Source Sandbox for Large Language Model Evalua | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 19 | `2308.07201` | ChatEval: Towards Better LLM-based Evaluators through Multi-Agent | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 20 | `2308.14508` | LongBench | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 21 | `2309.01431` | RGB (RAG Benchmark) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 22 | `2309.15217` | RAGAS — reference-free RAG evaluation | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 23 | `2310.00935` | Resolving Knowledge Conflicts in LLMs | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 24 | `2310.03025` | Retrieval meets Long Context Large Language Models | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 25 | `2310.03214` | FreshLLMs / FreshQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 26 | `2310.05036` | AvalonBench: Evaluating LLMs Playing the Game of Avalon | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 27 | `2310.06770` | SWE-bench — real GitHub issue resolution | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 28 | `2310.11511` | Self-RAG | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 29 | `2310.17884` | ConfAIde — contextual integrity for LLM secrecy | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 30 | `2311.12983` | GAIA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 31 | `2312.14197` | BIPIA (indirect prompt injection benchmark) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 32 | `2401.15391` | MultiHop-RAG | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 33 | `2401.15884` | Corrective Retrieval Augmented Generation | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 34 | `2402.13718` | ∞Bench (InfiniteBench) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 35 | `2402.16288` | PerLTQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 36 | `2402.17753` | LoCoMo | FULL | 1 (eval/failure) | episode_cognify | yes |
| 37 | `2403.11381` | Melting Pot — LLM-augmented agent cooperation eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 38 | `2404.06654` | RULER | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 39 | `2404.09992` | MMInA: Benchmarking Multihop Multimodal Internet Agents | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 40 | `2405.01535` | Prometheus 2 — open rubric-specialized judge LM | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 41 | `2405.07960` | AgentClinic: a multimodal agent benchmark to evaluate AI in simul | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 42 | `2405.13792` | xRAG — one-token retrieval modality fusion | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 43 | `2405.16089` | Towards Completeness-Oriented Tool Retrieval for Large Language M | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 44 | `2406.04744` | CRAG (Comprehensive RAG Benchmark) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 45 | `2406.08747` | StreamBench: Towards Benchmarking Continuous Improvement of Langu | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 46 | `2406.12045` | τ-bench — tool-agent-user interaction + pass^k | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 47 | `2406.12430` | PlanRAG: A Plan-then-Retrieval Augmented Generation for Generativ | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 48 | `2406.13144` | DialSim / LongDialQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 49 | `2406.13743` | GenAI-Bench: Evaluating and Improving Compositional Text-to-Visua | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 50 | `2407.11963` | NeedleBench | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 51 | `2408.08921` | Graph Retrieval-Augmented Generation: A Survey | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 52 | `2408.16967` | MemLong: Memory-Augmented Retrieval for Long Text Modeling | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 53 | `2409.05591` | MemoRAG — global memory-enhanced retrieval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 54 | `2409.19401` | Crafting Personalized Agents through Retrieval-Augmented Generati | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 55 | `2409.20163` | MemSim: A Bayesian Simulator for Evaluating Memory of LLM-based P | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 56 | `2410.02694` | HELMET: How to Evaluate Long-Context Language Models Effectively | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 57 | `2410.06992` | SWE-Bench+: Enhanced Coding Benchmark for LLMs | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 58 | `2410.07176` | Astute RAG — imperfect retrieval + conflicts | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 59 | `2410.10813` | LongMemEval | FULL | 1 (eval/failure) | episode_cognify,hydrate_retrieve | yes |
| 60 | `2410.20878` | AutoRAG: Automated Framework for optimization of Retrieval Augmen | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 61 | `2411.13093` | Video-RAG: Visually-aligned Retrieval-Augmented Long Video Compre | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 62 | `2412.15204` | LongBench v2 | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 63 | `2412.15540` | MRAG: A Modular Retrieval Framework for Time-Sensitive Question A | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 64 | `2501.09136` | Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 65 | `2502.03358` | Minerva: A Programmable Memory Test Benchmark for Language Models | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 66 | `2502.07459` | PerCul — story-driven cultural evaluation | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 67 | `2502.09597` | PrefEval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 68 | `2504.12516` | BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agent | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 69 | `2504.13079` | Retrieval-Augmented Generation with Conflicting Evidence | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 70 | `2505.11942` | LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 71 | `2505.20096` | MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborat | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 72 | `2506.01952` | WebChoreArena: Evaluating Web Browsing Agents on Realistic Tediou | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 73 | `2506.13356` | StoryBench: A Dynamic Benchmark for Evaluating Long-Term Memory w | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 74 | `2506.13651` | xbench: Tracking Agents Productivity Scaling with Profession-Alig | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 75 | `2506.21605` | MemBench — comprehensive memory eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 76 | `2507.05257` | MemoryAgentBench | FULL | 1 (eval/failure) | episode_cognify | yes |
| 77 | `2508.14704` | MCP-Universe: Benchmarking Large Language Models with Real-World | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 78 | `2508.15253` | Conflict-Aware Soft Prompting for Retrieval-Augmented Generation | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 79 | `2508.19855` | Youtu-GraphRAG: Vertically Unified Agents for Graph Retrieval-Aug | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 80 | `2509.21325` | PIR-RAG — private information retrieval for RAG | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 81 | `2509.22315` | PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reas | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 82 | `2510.01353` | MEMTRACK: Evaluating Long-Term Memory and State Tracking in Multi | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 83 | `2510.17281` | MemoryBench (continual feedback) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 84 | `2510.27246` | BEAM benchmark + LIGHT memory framework | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 85 | `2511.03506` | HaluMem — hallucination in agent memory eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 86 | `2511.20857` | Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-E | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 87 | `2512.12856` | Forgetful but Faithful: A Cognitive Memory Architecture and Bench | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 88 | `2512.20237` | MemR$^3$: Memory Retrieval via Reflective Reasoning for LLM Agent | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 89 | `2601.03417` | Implicit Graph, Explicit Retrieval: Towards Efficient and Interpr | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 90 | `2601.06966` | RealMem — project-oriented memory benchmark | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 91 | `2601.10744` | Explore with Long-term Memory: A Benchmark and Multimodal LLM-bas | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 92 | `2602.16313` | MemoryArena | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 93 | `2602.22769` | AMA-Bench — long-horizon agentic memory eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 94 | `2604.22085` | Memanto — typed semantic memory + info-theoretic retrieval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 95 | `2605.12493` | LongMemEval-V2 | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 96 | `2605.18421` | EvoMemBench — self-evolving memory eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 97 | `2608.00009` | AgentMemBench — strategy-agnostic dialogue memory eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 98 | `1410.5401` | NTM | FULL | 2 (capture/compaction) | anchors_graph | no |
| 99 | `1901.02860` | Transformer-XL | FULL | 2 (capture/compaction) | capture_working | no |
| 100 | `1911.00172` | kNN-LM — nearest-neighbor language models | FULL | 2 (capture/compaction) | capture_working | no |
| 101 | `1911.05507` | Compressive Transformer | FULL | 2 (capture/compaction) | capture_working | no |
| 102 | `2108.00573` | MuSiQue — multihop via single-hop composition | FULL | 2 (capture/compaction) | capture_working | no |
| 103 | `2210.03493` | Auto-CoT — automatic chain-of-thought prompting | FULL | 2 (capture/compaction) | capture_working | no |
| 104 | `2304.11062` | RMT to 1M tokens | FULL | 2 (capture/compaction) | capture_working | no |
| 105 | `2305.01625` | Unlimiformer | FULL | 2 (capture/compaction) | capture_working | no |
| 106 | `2305.10250` | MemoryBank (Zhong forgetting curve) | FULL | 2 (capture/compaction) | capture_working,episode_cognify | no |
| 107 | `2305.14322` | RET-LLM | FULL | 2 (capture/compaction) | capture_working | no |
| 108 | `2305.14323` | ChatCoT: Tool-Augmented Chain-of-Thought Reasoning on Chat-based | FULL | 2 (capture/compaction) | capture_working | no |
| 109 | `2305.14325` | Improving Factuality and Reasoning in Language Models through Mul | FULL | 2 (capture/compaction) | capture_working | no |
| 110 | `2305.14788` | AutoCompressors | FULL | 2 (capture/compaction) | capture_working | no |
| 111 | `2305.16300` | Landmark Attention | FULL | 2 (capture/compaction) | capture_working | no |
| 112 | `2305.17118` | Scissorhands (KV persistence-of-importance) | FULL | 2 (capture/compaction) | capture_working | no |
| 113 | `2305.17144` | Ghost in the Minecraft: Generally Capable Agents for Open-World E | FULL | 2 (capture/compaction) | capture_working | no |
| 114 | `2305.19118` | Encouraging Divergent Thinking in Large Language Models through M | FULL | 2 (capture/compaction) | capture_working | no |
| 115 | `2306.05499` | Prompt Injection vs LLM-integrated Applications (HouYi) | FULL | 2 (capture/compaction) | capture_working | no |
| 116 | `2306.14048` | H₂O Heavy-Hitter Oracle | FULL | 2 (capture/compaction) | capture_working | no |
| 117 | `2307.06945` | ICAE (In-context Autoencoder) | FULL | 2 (capture/compaction) | capture_working | no |
| 118 | `2308.03549` | Zhongjing: Enhancing the Chinese Medical Capabilities of Large La | FULL | 2 (capture/compaction) | capture_working | no |
| 119 | `2309.11054` | Design of chain-of-thought for math problem solving | FULL | 2 (capture/compaction) | capture_working | no |
| 120 | `2309.17453` | StreamingLLM | FULL | 2 (capture/compaction) | capture_working,episode_cognify | no |
| 121 | `2310.08560` | MemGPT | FULL | 2 (capture/compaction) | episode_cognify,anchors_graph,conflict_compose | no |
| 122 | `2312.03414` | Compressed Context Memory (CCM) — online KV compress | FULL | 2 (capture/compaction) | capture_working | no |
| 123 | `2312.03815` | LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS- | FULL | 2 (capture/compaction) | capture_working | no |
| 124 | `2401.07128` | EHRAgent: Code Empowers Large Language Models for Few-shot Comple | FULL | 2 (capture/compaction) | capture_working | no |
| 125 | `2403.16971` | AIOS | FULL | 2 (capture/compaction) | capture_working | no |
| 126 | `2404.14469` | SnapKV | FULL | 2 (capture/compaction) | capture_working | no |
| 127 | `2405.02957` | Agent Hospital: A Simulacrum of Hospital with Evolvable Medical A | FULL | 2 (capture/compaction) | capture_working | no |
| 128 | `2406.02069` | PyramidKV | FULL | 2 (capture/compaction) | capture_working | no |
| 129 | `2406.10774` | Quest (query-aware KV pages) | FULL | 2 (capture/compaction) | capture_working | no |
| 130 | `2409.03284` | iText2KG — incremental zero-shot KG construction | FULL | 2 (capture/compaction) | capture_working | no |
| 131 | `2411.11581` | OASIS: Open Agent Social Interaction Simulations with One Million | FULL | 2 (capture/compaction) | capture_working | no |
| 132 | `2501.01702` | AgentRefine: Enhancing Agent Generalization through Refinement Tu | FULL | 2 (capture/compaction) | capture_working | no |
| 133 | `2501.05366` | Search-o1: Agentic Search-Enhanced Large Reasoning Models | FULL | 2 (capture/compaction) | capture_working | no |
| 134 | `2504.13805` | LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration | FULL | 2 (capture/compaction) | capture_working | no |
| 135 | `2505.16067` | How Memory Management Impacts LLM Agents: An Empirical Study of E | FULL | 2 (capture/compaction) | capture_working | no |
| 136 | `2507.16784` | Beyond Context Limits: Subconscious Threads for Long-Horizon Reas | FULL | 2 (capture/compaction) | capture_working | no |
| 137 | `2507.21428` | MemTool: Optimizing Short-Term Memory Management for Dynamic Tool | FULL | 2 (capture/compaction) | capture_working | no |
| 138 | `2508.12379` | GraphCogent: Mitigating LLMs' Working Memory Constraints via Mult | FULL | 2 (capture/compaction) | capture_working | no |
| 139 | `2508.12630` | Semantic Anchoring in Agentic Memory: Leveraging Linguistic Struc | FULL | 2 (capture/compaction) | capture_working | no |
| 140 | `2508.13250` | Explicit v.s. Implicit Memory: Exploring Multi-hop Complex Reason | FULL | 2 (capture/compaction) | capture_working | no |
| 141 | `2509.01055` | VerlTool: Towards Holistic Agentic Reinforcement Learning with To | FULL | 2 (capture/compaction) | capture_working | no |
| 142 | `2509.08755` | AgentGym-RL — RL for long-horizon agents | FULL | 2 (capture/compaction) | capture_working | no |
| 143 | `2510.04195` | Constructing coherent spatial memory in LLM agents through graph | FULL | 2 (capture/compaction) | capture_working | no |
| 144 | `2510.07134` | TrackVLA++: Unleashing Reasoning and Memory Capabilities in VLA M | FULL | 2 (capture/compaction) | capture_working | no |
| 145 | `2511.01633` | Scaling Graph Chain-of-Thought Reasoning: A Multi-Agent Framework | FULL | 2 (capture/compaction) | capture_working | no |
| 146 | `2511.21726` | Goal-Directed Search Outperforms Goal-Agnostic Memory Compression | FULL | 2 (capture/compaction) | capture_working | no |
| 147 | `2601.01885` | Agentic Memory: Learning Unified Long-Term and Short-Term Memory | FULL | 2 (capture/compaction) | capture_working | no |
| 148 | `2601.06377` | HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents | FULL | 2 (capture/compaction) | capture_working | no |
| 149 | `2603.00503` | M$^2$: Dual-Memory Augmentation for Long-Horizon Web Agents via T | FULL | 2 (capture/compaction) | capture_working | no |
| 150 | `2607.21325` | CVA (cryptographically verifiable agent authorization) | FULL | 2 (capture/compaction) | capture_working | no |
| 151 | `claude-code-hooks-compaction-context-editing-docs` | Claude Code Hooks + Compaction + Context editing docs | FULL | 2 (capture/compaction) | capture_working | yes |
| 152 | `claude-code-hooks-docs` | Claude Code hooks docs | FULL | 2 (capture/compaction) | capture_working | no |
| 153 | `claude-compaction-compact-2026-01-12` | Claude Compaction (`compact-2026-01-12`) | FULL | 2 (capture/compaction) | capture_working | yes |
| 154 | `claude-context-editing-clear-tool-uses-thinking` | Claude Context editing (`clear_tool_uses` / thinking) | FULL | 2 (capture/compaction) | capture_working | no |
| 155 | `cursor-hooks-docs` | Cursor hooks docs | FULL | 2 (capture/compaction) | capture_working | no |
| 156 | `magic-wormhole-protocols` | Magic Wormhole protocols | FULL | 2 (capture/compaction) | capture_working | no |
| 157 | `rfc-2693` | SPKI Certificate Theory | FULL | 2 (capture/compaction) | capture_working | no |
| 158 | `2304.13343` | SCM (Self-Controlled Memory) | FULL | 3 (episode/boundary) | capture_working,episode_cognify | no |
| 159 | `2305.02747` | Unsupervised Dialogue Topic Seg (DialSTART) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 160 | `2305.16291` | Voyager | FULL | 3 (episode/boundary) | episode_cognify | no |
| 161 | `2307.11019` | Investigating the Factual Knowledge Boundary of Large Language Mo | FULL | 3 (episode/boundary) | episode_cognify | yes |
| 162 | `2308.10464` | HyperSeg (HDC topic seg) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 163 | `2309.17452` | ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem | FULL | 3 (episode/boundary) | episode_cognify | no |
| 164 | `2311.08719` | Think-in-Memory (TiM) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 165 | `2403.11901` | Larimar | FULL | 3 (episode/boundary) | episode_cognify | no |
| 166 | `2410.12480` | KcMF — knowledge-compliant schema/entity matching | FULL | 3 (episode/boundary) | episode_cognify | no |
| 167 | `2501.06590` | ChemAgent: Self-updating Library in Large Language Models Improve | FULL | 3 (episode/boundary) | episode_cognify | no |
| 168 | `2501.12254` | Memory Storyboard: Leveraging Temporal Segmentation for Streaming | FULL | 3 (episode/boundary) | episode_cognify | no |
| 169 | `2502.05589` | SeCom (segment memory + compress denoise) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 170 | `2504.16754` | HEMA | FULL | 3 (episode/boundary) | episode_cognify | no |
| 171 | `2506.06326` | MemoryOS | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph,conflict_compose | no |
| 172 | `2506.08098` | Cognitive Weave | FULL | 3 (episode/boundary) | episode_cognify | no |
| 173 | `2508.03341` | Nemori / What Deserves Memory | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph | no |
| 174 | `2508.15294` | A Multi-Memory Segment System for Generating High-Quality Long-Te | FULL | 3 (episode/boundary) | episode_cognify | no |
| 175 | `2512.17083` | Granularity-Aware Dialogue Topic Seg | FULL | 3 (episode/boundary) | episode_cognify | no |
| 176 | `2512.20745` | AgentMath: Empowering Mathematical Reasoning for Large Language M | FULL | 3 (episode/boundary) | episode_cognify | no |
| 177 | `2601.03785` | Membox — topic continuity memory boxes | FULL | 3 (episode/boundary) | episode_cognify | no |
| 178 | `2601.07582` | ES-Mem | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph | no |
| 179 | `2604.20943` | Sleep-Consolidated Memory (preview) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 180 | `2605.16045` | RecMem | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph | no |
| 181 | `2109.06157` | SituatedQA — temporal/geographic context QA | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 182 | `2306.08302` | Unifying Large Language Models and Knowledge Graphs: A Roadmap | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 183 | `2307.07697` | Think-on-Graph (ToG) | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 184 | `2401.03426` | LLM entity resolution (cost-efficient) | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 185 | `2403.06434` | BoostER — LLM-enhanced entity resolution | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 186 | `2404.16130` | GraphRAG | FULL | 4 (graph/conflict) | anchors_graph | no |
| 187 | `2405.14831` | HippoRAG | FULL | 4 (graph/conflict) | anchors_graph | no |
| 188 | `2405.19686` | Knowledge Graph Tuning: Real-time Large Language Model Personaliz | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 189 | `2406.14550` | GraphReader | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 190 | `2407.04363` | AriGraph | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 191 | `2408.00103` | ReLiK (EL + RE) | FULL | 4 (graph/conflict) | anchors_graph | no |
| 192 | `2408.05861` | Temporal Knowledge-Graph Memory in a Partially Observable Environ | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 193 | `2410.05779` | LightRAG | FULL | 4 (graph/conflict) | anchors_graph | no |
| 194 | `2410.19627` | Knowledge Graph Enhanced Language Agents for Recommendation | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 195 | `2501.00309` | GraphRAG with Graphs | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 196 | `2501.13956` | Zep / Graphiti | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 197 | `2502.14802` | HippoRAG 2 | FULL | 4 (graph/conflict) | anchors_graph | no |
| 198 | `2503.21322` | HyperGraphRAG | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 199 | `2504.19413` | Mem0 / Mem0g | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 200 | `2506.07398` | G-Memory | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 201 | `2506.18019` | Graphs Meet AI Agents: Taxonomy, Progress, and Future Opportuniti | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 202 | `2507.21407` | Graph-Augmented Large Language Model Agents: Current Progress and | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 203 | `2508.10391` | LeanRAG: Knowledge-Graph-Based Generation with Semantic Aggregati | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 204 | `2509.21212` | SGMem: Sentence Graph Memory for Long-Term Conversational Agents | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 205 | `2510.03611` | Can an LLM Induce a Graph? Investigating Memory Drift and Context | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 206 | `2510.13614` | MemoTime: Memory-Augmented Temporal Knowledge Graph Enhanced Larg | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 207 | `2511.17467` | PersonaAgent with GraphRAG: Community-Aware Knowledge Graphs for | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 208 | `2601.02744` | SYNAPSE — spreading activation episodic-semantic graph | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 209 | `2601.03236` | MAGMA | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 210 | `2601.12331` | ppRAG / CAPRISE — encrypted distance-preserving RAG | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 211 | `2602.05665` | Graph-based Agent Memory survey | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 212 | `2603.11768` | SSGM | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 213 | `2605.15701` | H-Mem (hybrid tree+graph) | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 214 | `2605.17301` | ConflictRAG — conflict-aware RAG | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | yes |
| 215 | `2605.28773` | FluxMem — connectivity-evolving memory graph | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 216 | `2606.06036` | MRAgent — active graph memory reconstruction | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 217 | `2606.06240` | TOKI | FULL | 4 (graph/conflict) | conflict_compose | no |
| 218 | `2607.05844` | StateFuse | FULL | 4 (graph/conflict) | conflict_compose | no |
| 219 | `2303.17760` | CAMEL | FULL | 5 (privacy/capability) | conflict_compose | no |
| 220 | `2401.05459` | Personal LLM Agents: Insights and Survey about the Capability, Ef | FULL | 5 (privacy/capability) | privacy_seal | no |
| 221 | `2409.00138` | PrivacyLens | FULL | 5 (privacy/capability) | privacy_seal | yes |
| 222 | `2502.13172` | MEXTRA / Unveiling Privacy Risks in LLM Agent Memory | FULL | 5 (privacy/capability) | privacy_seal | yes |
| 223 | `2503.08175` | Privacy-Enhancing Paradigms within Federated Multi-Agent Systems | FULL | 5 (privacy/capability) | privacy_seal | yes |
| 224 | `2505.18279` | Collaborative Memory | FULL | 5 (privacy/capability) | anchors_graph,conflict_compose | no |
| 225 | `2505.23643` | Fides — IFC for securing AI agents | FULL | 5 (privacy/capability) | privacy_seal | no |
| 226 | `2512.04668` | Topology Matters / MAMA | FULL | 5 (privacy/capability) | privacy_seal | no |
| 227 | `2602.11510` | AgentLeak | FULL | 5 (privacy/capability) | conflict_compose | yes |
| 228 | `2604.26525` | PRAG — end-to-end privacy-preserving RAG | FULL | 5 (privacy/capability) | privacy_seal | yes |
| 229 | `2605.10614` | PRISM | FULL | 5 (privacy/capability) | privacy_seal | no |
| 230 | `2606.24535` | MemClaw / Governed Shared Memory | FULL | 5 (privacy/capability) | anchors_graph,conflict_compose | no |
| 231 | `2606.29788` | MemLeak | FULL | 5 (privacy/capability) | conflict_compose | yes |
| 232 | `biscuits-design-spec` | Biscuits DESIGN+spec | FULL | 5 (privacy/capability) | privacy_seal | no |
| 233 | `c2sp-age-md` | C2SP age.md | FULL | 5 (privacy/capability) | privacy_seal | no |
| 234 | `capability-myths-demolished` | Capability Myths Demolished | FULL | 5 (privacy/capability) | privacy_seal | no |
| 235 | `libsodium-seal-box-sign` | libsodium seal/box/sign | FULL | 5 (privacy/capability) | privacy_seal | no |
| 236 | `macaroons-ndss-2014` | Macaroons NDSS 2014 | FULL | 5 (privacy/capability) | privacy_seal | no |
| 237 | `mls-rfc-9420-9750` | MLS RFC 9420 / 9750 | FULL | 5 (privacy/capability) | privacy_seal | no |
| 238 | `spritely-ocappub` | Spritely / OcapPub | FULL | 5 (privacy/capability) | privacy_seal | no |
| 239 | `vault-eknow-2025` | VAULT (eKNOW 2025) | FULL | 5 (privacy/capability) | privacy_seal | no |
| 240 | `2005.11485` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 241 | `2304.08485` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 242 | `2310.06201` | Same Selective Context paper as `2304.12102` (BATCH6 FULL) — body fetched, not re-marked | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 243 | `2402.13753` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 244 | `1410.3916` | Memory Networks | FULL | 6 (eng-judgment) | capture_working | no |
| 245 | `1803.05355` | FEVER — fact extraction and verification | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 246 | `1805.04263` | Memory-net / memorizing-transformer lineage | FULL | 6 (eng-judgment) | anchors_graph | no |
| 247 | `2004.04906` | Memory-net / memorizing-transformer lineage | FULL | 6 (eng-judgment) | anchors_graph | no |
| 248 | `2005.11401` | RAG (Lewis et al.) | FULL | 6 (eng-judgment) | capture_working | no |
| 249 | `2007.01282` | FiD — Fusion-in-Decoder RAG | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 250 | `2101.06804` | KATE — kNN in-context example selection | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 251 | `2103.08541` | VitaminC — contrastive fact verification | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 252 | `2107.07567` | MSC / Beyond Goldfish Memory — multi-session chat | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 253 | `2109.10862` | Recursive Summarizing Books | FULL | 6 (eng-judgment) | episode_cognify | no |
| 254 | `2112.04426` | RETRO | FULL | 6 (eng-judgment) | episode_cognify | no |
| 255 | `2203.08913` | Memorizing Transformers | FULL | 6 (eng-judgment) | capture_working | no |
| 256 | `2205.12674` | Memory-net / memorizing-transformer lineage | FULL | 6 (eng-judgment) | anchors_graph | no |
| 257 | `2207.06881` | Recurrent Memory Transformer | FULL | 6 (eng-judgment) | capture_working | no |
| 258 | `2207.13332` | RealTime QA — dynamic weekly present-time QA | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 259 | `2210.03629` | ReAct | FULL | 6 (eng-judgment) | capture_working | no |
| 260 | `2212.10496` | HyDE — hypothetical document embeddings | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 261 | `2212.14024` | DSP — Demonstrate-Search-Predict | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 262 | `2302.04761` | Toolformer | FULL | 6 (eng-judgment) | capture_working | no |
| 263 | `2303.11366` | Reflexion | FULL | 6 (eng-judgment) | capture_working | no |
| 264 | `2304.03442` | Generative Agents | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 265 | `2304.08467` | Gist Tokens — prompt compression | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 266 | `2304.12102` | Selective Context | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 267 | `2305.03010` | GEIA (generative embedding inversion) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 268 | `2305.05091` | Knowledge-enhanced Agents for Interactive Text Games | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 269 | `2305.08371` | SuperDialseg | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 270 | `2305.09645` | StructGPT — IRR over structured data | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 271 | `2305.14264` | Active learning principles for in-context learning | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 272 | `2305.14318` | CREATOR: Tool Creation for Disentangling Abstract and Concrete Re | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 273 | `2305.14552` | Sources of hallucination in LLMs on inference | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 274 | `2306.03314` | Multi-Agent Collaboration: Harnessing the Power of Intelligent LL | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 275 | `2306.03901` | ChatDB — SQL databases as symbolic memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 276 | `2307.07047` | Does Collaborative Human-LM Dialogue Generation Help Information | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 277 | `2307.07924` | ChatDev | FULL | 6 (eng-judgment) | conflict_compose | no |
| 278 | `2307.12856` | A Real-World WebAgent with Planning, Long Context Understanding, | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 279 | `2308.00352` | MetaGPT | FULL | 6 (eng-judgment) | conflict_compose | no |
| 280 | `2308.01542` | Memory Sandbox: Transparent and Interactive Memory Management for | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 281 | `2308.02151` | Retroformer — retrospective LLM agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 282 | `2308.03427` | TPTU: Large Language Model-based AI Agents for Task Planning and | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 283 | `2308.08155` | AutoGen | FULL | 6 (eng-judgment) | conflict_compose | no |
| 284 | `2308.08239` | MemoChat | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 285 | `2308.10144` | ExpeL | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 286 | `2308.10848` | AgentVerse — dynamic multi-agent collaboration | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 287 | `2308.11339` | ProAgent: Building Proactive Cooperative Agents with Large Langua | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 288 | `2308.15022` | Recursive Summarization (dialogue memory) | FULL | 6 (eng-judgment) | capture_working,episode_cognify | no |
| 289 | `2309.01918` | RoboAgent: Generalization and Efficiency in Robot Manipulation vi | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 290 | `2309.03736` | TradingGPT: Multi-Agent System with Layered Memory and Distinct C | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 291 | `2309.04175` | Knowledge-tuning Large Language Models with Structured Medical Kn | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 292 | `2309.04697` | Leakage-Abuse Attacks on SSE | FULL | 6 (eng-judgment) | hydrate_retrieve | yes |
| 293 | `2309.06794` | Cognitive Mirage: A Review of Hallucinations in Large Language Mo | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 294 | `2309.07864` | Rise and Potential of LLM Agents (survey; §memory) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 295 | `2309.07870` | Agents: An Open-source Framework for Autonomous Language Agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 296 | `2310.02172` | Lyfe Agents: Generative agents for low-cost real-time social inte | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 297 | `2310.04408` | RECOMP | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 298 | `2310.05029` | MemWalker — interactive reading memory tree | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 299 | `2310.05736` | LLMLingua | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 300 | `2310.06500` | MetaAgents: Large Language Model Based Agents for Decision-Making | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 301 | `2310.06816` | Text Embeddings Reveal (Almost) As Much As Text | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 302 | `2310.06839` | LongLLMLingua | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 303 | `2310.09233` | AgentCF: Collaborative Learning with Autonomous Language Agents f | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 304 | `2310.10436` | EconAgent: Large Language Model-Empowered Agents for Simulating M | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 305 | `2310.16340` | RCAgent: Cloud Root Cause Analysis by Autonomous Agents with Tool | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 306 | `2311.04177` | Enhancing LLM Intelligence with ARM-RAG: Auxiliary Rationale Memo | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 307 | `2311.05876` | Trends in Integration of Knowledge and Large Language Models: A S | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 308 | `2311.05997` | JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Mult | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 309 | `2311.09210` | Chain-of-Note (CoN) — robust RALM | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 310 | `2311.09677` | R-Tuning — selective prediction / abstention | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 311 | `2311.11315` | TPTU-v2: Boosting Task Planning and Tool Usage of Large Language | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 312 | `2311.17227` | War and Peace (WarAgent): Large Language Model-based Multi-Agent | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 313 | `2312.00326` | Agent-OM: Leveraging LLM Agents for Ontology Matching | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 314 | `2312.04889` | KwaiAgents: Generalized Information-seeking Agent System with Lar | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 315 | `2312.10997` | RAG for LLMs — survey | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 316 | `2401.03462` | Activation Beacon | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 317 | `2401.07339` | CodeAgent: Enhancing Code Generation with Tool-Integrated Agent S | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 318 | `2401.14215` | Commonsense-augmented Memory Construction and Management in Long- | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 319 | `2401.18059` | RAPTOR | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 320 | `2402.03367` | RAG-Fusion — multi-query RRF | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 321 | `2402.04617` | InfLLM — training-free long-context memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 322 | `2402.04624` | MemoryLLM — self-updatable LLM memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 323 | `2402.07867` | PoisonedRAG | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 324 | `2402.09727` | ReadAgent — gist memory for long contexts | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 325 | `2402.11163` | KG-Agent | FULL | 6 (eng-judgment) | anchors_graph | no |
| 326 | `2402.14034` | AgentScope: A Flexible yet Robust Multi-Agent Platform | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 327 | `2402.17840` | Spill the Beans (RAG datastore extraction) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 328 | `2402.18485` | A Multimodal Foundation Agent for Financial Trading: Tool-Augment | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 329 | `2403.01112` | Efficient Episodic Memory Utilization of Cooperative Multi-Agent | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 330 | `2403.02691` | InjecAgent | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 331 | `2403.04317` | Online Adaptation of Language Models with a Memory of Amortized C | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 332 | `2403.04957` | Automatic Universal Prompt Injection Attacks | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 333 | `2403.12968` | LLMLingua-2 | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 334 | `2403.14403` | Adaptive-RAG | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 335 | `2403.17134` | RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 336 | `2404.09982` | INMS: Memory Sharing for Large Language Model based Agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 337 | `2404.13501` | Zhang memory mechanisms survey | FULL | 6 (eng-judgment) | capture_working | no |
| 338 | `2405.01525` | FLAME — factuality-aware alignment | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 339 | `2405.05175` | AirGapAgent | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 340 | `2405.14486` | RefChecker: Reference-based Fine-grained Hallucination Checker an | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 341 | `2405.20446` | RAG membership inference | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 342 | `2406.00057` | Toward Conversational Agents with Context and Time Sensitive Long | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 343 | `2406.03007` | BadAgent — backdoor attacks on LLM agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 344 | `2406.04151` | AgentGym — evolving LLM agents across environments | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 345 | `2406.05804` | Review of LLM-Agent Paradigms (tool/RAG/planning) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 346 | `2406.05925` | Hello Again! LLM-powered Personalized Agent for Long-term Dialogu | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 347 | `2406.06124` | Enhancing Long-Term Memory using Hierarchical Aggregate Tree for | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 348 | `2406.10149` | BABILong: Testing the Limits of LLMs with Long Context Reasoning- | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 349 | `2406.10996` | Towards Lifelong Dialogue Agents via Timeline-based Memory Manage | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 350 | `2406.13352` | AgentDojo | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 351 | `2407.01178` | $\text{Memory}^3$: Language Modeling with Explicit Memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 352 | `2407.02485` | RankRAG — unified context ranking + generation | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 353 | `2407.09450` | EM-LLM | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph | no |
| 354 | `2407.12784` | AgentPoison (memory/RAG backdoor) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 355 | `2407.18901` | AppWorld — interactive coding agents in app sandbox | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 356 | `2408.03615` | Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Lon | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 357 | `2408.09559` | HiAgent — hierarchical working memory management | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 358 | `2409.07429` | Agent Workflow Memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 359 | `2410.03156` | MELODI: Exploring Memory Compression for Long Contexts | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 360 | `2410.15665` | Long Term Memory: Foundation of AI Self-Evolution | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 361 | `2410.20682` | SHARE: Shared Memory-Aware Open-Domain Long-Term Dialogue Dataset | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 362 | `2411.00489` | AI Long-term Memory survey | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 363 | `2411.01705` | RAG backdoor data extraction | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 364 | `2412.01857` | Planning from Imagination: Episodic Simulation and Episodic Memor | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 365 | `2412.15266` | On the Structural Memory of LLM Agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 366 | `2412.15274` | Memory-Augmented Agent Training for Business Document Understandi | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 367 | `2501.00358` | Embodied VideoAgent: Persistent Memory from Egocentric Videos and | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 368 | `2501.06322` | Multi-Agent Collaboration Mechanisms survey | FULL | 6 (eng-judgment) | conflict_compose | no |
| 369 | `2501.12948` | Additional fetched fulltexts used as supporting | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 370 | `2502.00306` | Stealthy MIA for RAG (Riddle Me This) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 371 | `2502.00592` | M+ — scalable long-term MemoryLLM | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 372 | `2502.05453` | LLM-Powered Decentralized Generative Agents with Adaptive Hierarc | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 373 | `2502.12110` | A-MEM | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 374 | `2502.13843` | AgentCF++: Memory-enhanced LLM-based Agents for Popularity-aware | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 375 | `2503.03704` | MINJA (query-only memory injection) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 376 | `2503.05193` | Memory-augmented Query Reconstruction for LLM-based Knowledge Gra | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 377 | `2503.07018` | Toward Multi-Session Personalized Conversation: A Large-Scale Dat | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 378 | `2503.08026` | RMM — Reflective Memory Management | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 379 | `2503.09516` | Search-R1: Training LLMs to Reason and Leverage Search Engines wi | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 380 | `2503.10049` | Enhancing Multi-Agent Systems via Reinforcement Learning with LLM | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 381 | `2503.18813` | Additional fetched fulltexts used as supporting | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 382 | `2503.21760` | MemInsight — autonomous memory augmentation | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 383 | `2504.11703` | Progent (privilege control) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 384 | `2504.12369` | WorldMem: Long-term Consistent World Simulation with Memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 385 | `2504.13169` | REVERSE — generate but verify | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 386 | `2504.13171` | Sleep-time Compute | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 387 | `2504.15965` | From Human Memory to AI Memory survey | FULL | 6 (eng-judgment) | anchors_graph | no |
| 388 | `2504.18070` | PropRAG | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 389 | `2504.20073` | RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 390 | `2504.21776` | WebThinker: Empowering Large Reasoning Models with Deep Research | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 391 | `2505.00675` | Additional fetched fulltexts used as supporting | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 392 | `2505.02099` | MemEngine — modular memory library | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 393 | `2505.15962` | Pre-training Limited Memory Language Models with Internal and Ext | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 394 | `2505.16348` | Embodied Agents Meet Personalization: Investigating Challenges an | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 395 | `2505.16421` | WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinfo | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 396 | `2505.19549` | Multi-granularity conversational memory (MemGAS) | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph | no |
| 397 | `2505.20231` | MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi- | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 398 | `2505.20286` | Alita: Generalist Agent Enabling Scalable Agentic Reasoning with | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 399 | `2505.23052` | RAGRouter — RAG-aware query routing | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 400 | `2505.23841` | SkewRoute — training-free KG-RAG LLM routing | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 401 | `2505.24478` | Cognee / KG–LLM interface optimization | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 402 | `2506.03141` | Context as Memory: Scene-Consistent Interactive Long Video Genera | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 403 | `2506.14728` | AgentDistill: Training-Free Agent Distillation with Generalizable | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 404 | `2506.15841` | MEM1 (constant-size IS memory) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 405 | `2507.02259` | MemAgent | FULL | 6 (eng-judgment) | episode_cognify | no |
| 406 | `2507.02592` | WebSailor: Navigating Super-human Reasoning for Web Agent | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 407 | `2507.03616` | EvoAgentX: An Automated Framework for Evolving Agentic Workflows | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 408 | `2507.03724` | MemOS | FULL | 6 (eng-judgment) | capture_working,episode_cognify | no |
| 409 | `2507.06229` | Agent KB (cross-framework experience) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 410 | `2507.07957` | MIRIX — multi-agent memory system | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 411 | `2507.07998` | PyVision: Agentic Vision with Dynamic Tooling | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 412 | `2507.10457` | LPCI — logic-layer prompt control injection | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 413 | `2507.21055` | Can Memory-Augmented LLM Agents Aid Journalism in Interpreting an | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 414 | `2507.21105` | AgentMaster: A Multi-Agent Conversational Framework Using A2A and | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 415 | `2507.22925` | Hierarchical Memory for High-Efficiency Long-Term Reasoning in LL | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 416 | `2508.01415` | RoboMemory: A Brain-inspired Multi-memory Agentic Framework for I | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 417 | `2508.01832` | MLP Memory: A Retriever-Pretrained Memory for Large Language Mode | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 418 | `2508.03680` | Agent Lightning: Train ANY AI Agents with Reinforcement Learning | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 419 | `2508.04700` | SEAgent: Self-Evolving Computer Use Agent with Autonomous Learnin | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 420 | `2508.04903` | RCR-Router | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 421 | `2508.06433` | Memp — agent procedural memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 422 | `2508.07010` | Narrative Memory in Machines: Multi-Agent Arc Extraction in Seria | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 423 | `2508.07407` | A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 424 | `2508.08997` | Intrinsic Memory Agents — heterogeneous MAS memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 425 | `2508.09736` | M3-Agent — multimodal long-term memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 426 | `2508.09874` | Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Lang | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 427 | `2508.10419` | ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful L | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 428 | `2508.11567` | AgentMental: An Interactive Multi-Agent Framework for Explainable | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 429 | `2508.15305` | Coarse-to-Fine Grounded Memory for LLM Agent Planning | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 430 | `2508.16153` | Memento (case-based M-MDP memory) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 431 | `2508.16629` | Learn to Memorize: Optimizing LLM-based Agents with Adaptive Memo | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 432 | `2508.19828` | Memory-R1 | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 433 | `2509.10852` | Pre-Storage Reasoning for Episodic Memory: Shifting Inference Bur | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 434 | `2509.13313` | ReSum — context summarization for search agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 435 | `2509.17459` | PRINCIPLES: Synthetic Strategy Memory for Proactive Dialogue Agen | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 436 | `2509.23040` | Look Back to Reason Forward: Revisitable Memory for Long-Context | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 437 | `2509.24704` | MemGen — generative latent memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 438 | `2509.25140` | ReasoningBank + MaTTS | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 439 | `2509.25250` | Memory Management and Contextual Consistency for Long-Running Low | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 440 | `2509.25911` | Mem-α | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 441 | `2510.04618` | Agentic Context Engineering: Evolving Contexts for Self-Improving | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 442 | `2510.04851` | LEGOMem (modular procedural multi-agent) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 443 | `2510.05244` | IPI Firewalls (Minimizer + Sanitizer) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 444 | `2510.06664` | ToolMem: Enhancing Multimodal Agents with Learnable Tool Capabili | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 445 | `2510.06719` | DP Synthetic Text for RAG | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 446 | `2510.07925` | Enabling Personalized Long-term Interactions in LLM-based Agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 447 | `2510.08558` | Agent learning via early experience | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 448 | `2510.09720` | Preference-Aware Memory Update for Long-Term LLM Agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 449 | `2510.10397` | AssoMem | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 450 | `2510.11967` | Context-Folding — branch/return context management | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 451 | `2510.12635` | Memory as Action / MemAct | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 452 | `2510.13363` | D-SMART: Enhancing LLM Dialogue Consistency via Dynamic Structure | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 453 | `2510.18866` | LightMem | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 454 | `2510.19897` | Learning from Supervision with Semantic and Episodic Memory: A Re | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 455 | `2510.21618` | DeepAgent: A General Reasoning Agent with Scalable Toolsets | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 456 | `2510.23010` | TALM: Dynamic Tree-Structured Multi-Agent Framework with Long-Ter | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 457 | `2510.24699` | AgentFold — proactive context management | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 458 | `2510.26486` | LINK-KG — coreference-resolved KG construction | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 459 | `2511.00628` | AgentGit — Git-like MAS checkpoints/branching | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 460 | `2511.01448` | LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficien | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 461 | `2511.06179` | MemoriesDB: A Temporal-Semantic-Relational Database for Long-Term | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 462 | `2511.06449` | FLEX | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 463 | `2511.07800` | From Experience to Strategy: Empowering LLM Agents with Trainable | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 464 | `2511.10030` | Multi-agent In-context Coordination via Decentralized Memory Retr | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 465 | `2511.12997` | WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guid | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 466 | `2511.13593` | O-Mem (omni persona/episodic/working) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 467 | `2511.17208` | A Simple Yet Strong Baseline for Long-Term Conversational Memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 468 | `2511.21678` | Agentic Learner with Grow-and-Refine Multimodal Semantic Memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 469 | `2512.02425` | WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 470 | `2512.10696` | ReMe — dynamic procedural memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 471 | `2512.12360` | VideoARM: Agentic Reasoning over Hierarchical Memory for Long-For | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 472 | `2512.13564` | Memory in the Age of AI Agents (survey) | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 473 | `2512.16962` | MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Exp | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 474 | `2512.18950` | Hierarchical procedural memory (Bayesian) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 475 | `2512.20092` | Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 476 | `2512.22716` | Memento 2 | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 477 | `2601.03192` | MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 478 | `2601.04726` | Memory Matters More: Event-Centric Memory as a Logic Map for Agen | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 479 | `2601.05960` | Memory-as-a-Tool | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 480 | `2601.06037` | TeleMem: Building Long-Term and Multimodal Memory for Agentic AI | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 481 | `2601.07468` | Beyond Dialogue Time: Temporal Semantic Memory for Personalized L | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 482 | `2601.08323` | AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Ope | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 483 | `2601.14192` | Toward Efficient Agents: Memory, Tool learning, and Planning | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 484 | `2602.06052` | Agent Memory Second Half survey | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 485 | `2602.07624` | M2A: Multimodal Memory Agent with Dual-Layer Hybrid Memory for Lo | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 486 | `2602.15329` | EventMemAgent: Hierarchical Event-Centric Memory for Online Video | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 487 | `2602.19320` | Anatomy of Agentic Memory (survey) | FULL | 6 (eng-judgment) | conflict_compose | no |
| 488 | `2603.01455` | From Verbatim to Gist: Distilling Pyramidal Multimodal Memory via | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 489 | `2603.02228` | Neural Paging — learned context management | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 490 | `2603.07670` | Memory for Autonomous LLM Agents (survey) | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 491 | `2603.15994` | Selective Memory / supersession chains | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 492 | `2603.24018` | ELITE — experiential learning and intent-aware transfer | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 493 | `2603.24639` | ERL — experiential reflective learning | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 494 | `2604.04853` | MemMachine — ground-truth-preserving agent memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 495 | `2604.21748` | StructMem — structured hierarchical memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 496 | `2605.06716` | From Storage to Experience (survey) | FULL | 6 (eng-judgment) | anchors_graph | no |
| 497 | `2605.27825` | MRMMIA — membership inference on chat-agent memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 498 | `2605.30690` | ElasticMem — latent memory as learnable resource | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 499 | `2606.04425` | Cross-Session Stored Prompt Injection | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 500 | `2606.10525` | Assessing Automated Prompt Injection in Agentic Environments | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 501 | `2606.23127` | Managing procedural memory in LLM agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 502 | `2606.29824` | Neural procedural memory for LLM agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 503 | `2608.03463` | LeanMem — efficient long-term agent memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 504 | `adr-qoc-ibis-design-rationale-practice` | ADR / QOC / IBIS design-rationale practice | FULL | 6 (eng-judgment) | hydrate_retrieve | no |

## Machine-readable

- `docs/research/queue/full_queue.jsonl` — one JSON object per line.
- Rebuild: `python3 scripts/research/build_full_queue.py`
- Fetch arXiv HTML: `python3 scripts/research/fetch_paper.py <id>`

