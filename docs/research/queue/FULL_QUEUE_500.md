# Kedger Track 0 — FULL deep-read queue (≥500)

> **Program:** Kedger research (measure → refine).
> **Honesty rule:** `FULL` only if listed in `CORPUS_INVENTORY.md` §2 ledger.
> `seed_placeholder` entries need fetch — they are **not** FULL deep-reads.
> Historical memos may say “MoDeX”; that is labeling debt, not product identity.

## Stats

| Metric | Value |
|--------|------:|
| Unique arXiv IDs scanned | 261 |
| FULL (from inventory) | 258 |
| queued (scanned, not FULL) | 19 |
| seed_placeholder (pad) | 223 |
| **Queue size** | **500** |
| Markdown files scanned | 51 |

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
| 1 | `2303.16634` | G-Eval | queued | 1 (eval/failure) | hydrate_retrieve | yes |
| 2 | `survey-seed-006` | MemoryArena — agent memory evaluation suite | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 3 | `survey-seed-007` | MemBench — memory benchmark suite | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 4 | `survey-seed-008` | RealMem — realistic memory evaluation | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 5 | `survey-seed-015` | LongMemEval-V2 (2605.12493) — eng-colleague eval follow-on | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 6 | `survey-seed-042` | AppWorld / environment memory benchmarks | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 7 | `survey-seed-043` | AgentBench — agent evaluation harness | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 8 | `survey-seed-044` | GAIA benchmark — tool-use failure modes | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 9 | `survey-seed-045` | WebArena / BrowserGym memory carryover | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 10 | `survey-seed-046` | SWE-bench agent trajectory memory notes | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 11 | `survey-seed-047` | τ-bench / tool-agent eval memory slices | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 12 | `survey-seed-081` | Unify GraphRAG evaluation protocols | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 13 | `survey-seed-082` | RGB — retrieval-augmented generation benchmark | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 14 | `survey-seed-083` | CRAG — Corrective RAG benchmark | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 15 | `survey-seed-084` | MultiHop-RAG benchmark | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 16 | `survey-seed-085` | HotpotQA as memory multi-hop probe | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 17 | `survey-seed-086` | 2WikiMultiHopQA probe | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 18 | `survey-seed-087` | MuSiQue multi-hop probe | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 19 | `survey-seed-088` | Bamboogle / Compose multi-hop | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 20 | `survey-seed-089` | TriviaQA / Natural Questions RAG baselines | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 21 | `survey-seed-092` | ConflictQA / conflicting knowledge eval | seed_placeholder | 1 (eval/failure) | conflict_compose | yes |
| 22 | `survey-seed-093` | FreshQA temporal freshness eval | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 23 | `survey-seed-094` | RealtimeQA temporal memory | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 24 | `survey-seed-095` | SituatedQA / context-dependent answers | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 25 | `survey-seed-103` | PerLTQA personal long-term QA | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 26 | `survey-seed-104` | Long-context Needle-in-Haystack protocols | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 27 | `survey-seed-105` | RULER long-context eval suite | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 28 | `survey-seed-106` | ∞Bench long-context | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 29 | `survey-seed-107` | LongBench / LongBench-v2 | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 30 | `survey-seed-108` | L-Eval long-context eval | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 31 | `survey-seed-109` | ZeroSCROLLS long-context | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 32 | `survey-seed-110` | QuALITY long-doc reading | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 33 | `survey-seed-145` | LLM-as-extractor reliability studies | seed_placeholder | 1 (eval/failure) | anchors_graph | yes |
| 34 | `survey-seed-146` | Hallucination audits for memory write paths | seed_placeholder | 1 (eval/failure) | conflict_compose | yes |
| 35 | `survey-seed-147` | Self-RAG / CRAG corrective retrieval | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 36 | `survey-seed-148` | Corrective RAG (Yan et al.) full mechanisms | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 37 | `1809.09600` | HotpotQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 38 | `2011.01060` | 2WikiMultiHopQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 39 | `2212.10509` | IRCoT — interleaved retrieval + CoT | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 40 | `2301.12652` | REPLUG — retrieval-augmented black-box LMs | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 41 | `2305.06983` | FLARE / Active Retrieval Augmented Generation | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 42 | `2305.13300` | Adaptive Chameleon (knowledge conflicts) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 43 | `2307.03172` | Lost in the Middle | FULL | 1 (eval/failure) | episode_cognify,hydrate_retrieve | no |
| 44 | `2307.13854` | WebArena | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 45 | `2308.03688` | AgentBench | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 46 | `2308.14508` | LongBench | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 47 | `2309.01431` | RGB (RAG Benchmark) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 48 | `2310.00935` | Resolving Knowledge Conflicts in LLMs | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 49 | `2310.03214` | FreshLLMs / FreshQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 50 | `2310.11511` | Self-RAG | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 51 | `2310.17884` | ConfAIde — contextual integrity for LLM secrecy | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 52 | `2311.12983` | GAIA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 53 | `2312.14197` | BIPIA (indirect prompt injection benchmark) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 54 | `2401.15391` | MultiHop-RAG | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 55 | `2401.15884` | Corrective Retrieval Augmented Generation | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 56 | `2402.13718` | ∞Bench (InfiniteBench) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 57 | `2402.16288` | PerLTQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 58 | `2402.17753` | LoCoMo | FULL | 1 (eval/failure) | episode_cognify | yes |
| 59 | `2403.11381` | Melting Pot — LLM-augmented agent cooperation eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 60 | `2404.06654` | RULER | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 61 | `2405.13792` | xRAG — one-token retrieval modality fusion | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 62 | `2406.04744` | CRAG (Comprehensive RAG Benchmark) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 63 | `2406.13144` | DialSim / LongDialQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 64 | `2407.11963` | NeedleBench | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 65 | `2409.05591` | MemoRAG — global memory-enhanced retrieval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 66 | `2410.07176` | Astute RAG — imperfect retrieval + conflicts | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 67 | `2410.10813` | LongMemEval | FULL | 1 (eval/failure) | episode_cognify,hydrate_retrieve | yes |
| 68 | `2412.15204` | LongBench v2 | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 69 | `2502.09597` | PrefEval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 70 | `2506.21605` | MemBench — comprehensive memory eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 71 | `2507.05257` | MemoryAgentBench | FULL | 1 (eval/failure) | episode_cognify | yes |
| 72 | `2509.21325` | PIR-RAG — private information retrieval for RAG | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 73 | `2510.17281` | MemoryBench (continual feedback) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 74 | `2510.27246` | BEAM benchmark + LIGHT memory framework | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 75 | `2511.03506` | HaluMem — hallucination in agent memory eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 76 | `2601.06966` | RealMem — project-oriented memory benchmark | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 77 | `2602.16313` | MemoryArena | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 78 | `2602.22769` | AMA-Bench — long-horizon agentic memory eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 79 | `2604.22085` | Memanto — typed semantic memory + info-theoretic retrieval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 80 | `2605.12493` | LongMemEval-V2 | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 81 | `2605.18421` | EvoMemBench — self-evolving memory eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 82 | `2608.00009` | AgentMemBench — strategy-agnostic dialogue memory eval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 83 | `survey-seed-023` | HiAgent — working-memory manager for multi-turn tasks | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 84 | `survey-seed-024` | ReSum — working-memory / resume manager | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 85 | `survey-seed-027` | Letta (MemGPT product line) docs — paging UX | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 86 | `survey-seed-028` | Claude Code memory / CLAUDE.md patterns (docs) | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 87 | `survey-seed-029` | Cursor Memories / Rules docs | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 88 | `survey-seed-041` | JARVIS / HuggingGPT tool memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 89 | `survey-seed-048` | ToolBench memory-of-tools patterns | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 90 | `survey-seed-049` | API-Bank tool trajectory memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 91 | `survey-seed-050` | RestGPT stateful API memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 92 | `survey-seed-056` | TPTU tool planning memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 93 | `survey-seed-057` | Chameleon LLM tool composer memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 94 | `survey-seed-065` | ReWOO planner memory separation | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 95 | `survey-seed-067` | RET-LLM follow-ons / SQL memory agents | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 96 | `survey-seed-127` | SCM controller variants beyond 2304.13343 | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 97 | `survey-seed-128` | Ebbinghaus forgetting implementations beyond MemoryBank | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 98 | `survey-seed-164` | Matryoshka embeddings for budgeted hydrate | seed_placeholder | 2 (capture/compaction) | hydrate_retrieve | yes |
| 99 | `survey-seed-165` | Prompt compression (LLMLingua / LongLLMLingua) | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 100 | `survey-seed-166` | Selective Context / semantic compression | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 101 | `survey-seed-167` | RECOMP retrieve-compress | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 102 | `survey-seed-168` | xRAG / representation compression | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 103 | `survey-seed-169` | Gisting / gist tokens memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 104 | `survey-seed-170` | Activation Beacon / compressed KV | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 105 | `survey-seed-171` | PyramidKV / multilevel KV eviction | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 106 | `survey-seed-172` | Quest / KV retrieval for long context | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 107 | `survey-seed-173` | LOOK-M multimodal KV memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 108 | `survey-seed-174` | Heavy-Hitter variants beyond H₂O | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 109 | `survey-seed-175` | Attention sink analyses beyond StreamingLLM | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 110 | `survey-seed-176` | Scissorhands KV eviction | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 111 | `survey-seed-177` | LESS / adaptive KV | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 112 | `survey-seed-178` | Gear / quantized KV cache | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 113 | `survey-seed-179` | KIVI KV cache quantization | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 114 | `survey-seed-180` | SmoothQuant / KV quant engineering | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 115 | `survey-seed-181` | vLLM paged attention engineering notes | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 116 | `survey-seed-182` | SGLang radix attention prefix memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 117 | `survey-seed-183` | Anthropic context editing API notes (beyond inventory) | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 118 | `survey-seed-184` | OpenAI Responses / compaction API notes | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 119 | `survey-seed-185` | Gemini context caching docs | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 120 | `survey-seed-186` | AWS Bedrock session memory docs | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 121 | `survey-seed-187` | Azure AI Agent Service memory docs | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 122 | `survey-seed-188` | Google ADK session/memory docs | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 123 | `survey-seed-198` | OTel GenAI semantic conventions for L0 capture | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 124 | `survey-seed-199` | LLM tracing (Langfuse/Phoenix) → Evidence mapping | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 125 | `1410.5401` | NTM | FULL | 2 (capture/compaction) | anchors_graph | no |
| 126 | `1901.02860` | Transformer-XL | FULL | 2 (capture/compaction) | capture_working | no |
| 127 | `1911.05507` | Compressive Transformer | FULL | 2 (capture/compaction) | capture_working | no |
| 128 | `2304.11062` | RMT to 1M tokens | FULL | 2 (capture/compaction) | capture_working | no |
| 129 | `2305.01625` | Unlimiformer | FULL | 2 (capture/compaction) | capture_working | no |
| 130 | `2305.10250` | MemoryBank (Zhong forgetting curve) | FULL | 2 (capture/compaction) | capture_working,episode_cognify | no |
| 131 | `2305.14322` | RET-LLM | FULL | 2 (capture/compaction) | capture_working | no |
| 132 | `2305.14788` | AutoCompressors | FULL | 2 (capture/compaction) | capture_working | no |
| 133 | `2305.16300` | Landmark Attention | FULL | 2 (capture/compaction) | capture_working | no |
| 134 | `2305.17118` | Scissorhands (KV persistence-of-importance) | FULL | 2 (capture/compaction) | capture_working | no |
| 135 | `2306.05499` | Prompt Injection vs LLM-integrated Applications (HouYi) | FULL | 2 (capture/compaction) | capture_working | no |
| 136 | `2306.14048` | H₂O Heavy-Hitter Oracle | FULL | 2 (capture/compaction) | capture_working | no |
| 137 | `2307.06945` | ICAE (In-context Autoencoder) | FULL | 2 (capture/compaction) | capture_working | no |
| 138 | `2309.17453` | StreamingLLM | FULL | 2 (capture/compaction) | capture_working,episode_cognify | no |
| 139 | `2310.08560` | MemGPT | FULL | 2 (capture/compaction) | episode_cognify,anchors_graph,conflict_compose | no |
| 140 | `2312.03414` | Compressed Context Memory (CCM) — online KV compress | FULL | 2 (capture/compaction) | capture_working | no |
| 141 | `2403.16971` | AIOS | FULL | 2 (capture/compaction) | capture_working | no |
| 142 | `2404.14469` | SnapKV | FULL | 2 (capture/compaction) | capture_working | no |
| 143 | `2406.02069` | PyramidKV | FULL | 2 (capture/compaction) | capture_working | no |
| 144 | `2406.10774` | Quest (query-aware KV pages) | FULL | 2 (capture/compaction) | capture_working | no |
| 145 | `2409.03284` | iText2KG — incremental zero-shot KG construction | FULL | 2 (capture/compaction) | capture_working | no |
| 146 | `2607.21325` | CVA (cryptographically verifiable agent authorization) | FULL | 2 (capture/compaction) | capture_working | no |
| 147 | `claude-code-hooks-compaction-context-editing-docs` | Claude Code Hooks + Compaction + Context editing docs | FULL | 2 (capture/compaction) | capture_working | yes |
| 148 | `claude-code-hooks-docs` | Claude Code hooks docs | FULL | 2 (capture/compaction) | capture_working | no |
| 149 | `claude-compaction-compact-2026-01-12` | Claude Compaction (`compact-2026-01-12`) | FULL | 2 (capture/compaction) | capture_working | yes |
| 150 | `claude-context-editing-clear-tool-uses-thinking` | Claude Context editing (`clear_tool_uses` / thinking) | FULL | 2 (capture/compaction) | capture_working | no |
| 151 | `cursor-hooks-docs` | Cursor hooks docs | FULL | 2 (capture/compaction) | capture_working | no |
| 152 | `magic-wormhole-protocols` | Magic Wormhole protocols | FULL | 2 (capture/compaction) | capture_working | no |
| 153 | `rfc-2693` | SPKI Certificate Theory | FULL | 2 (capture/compaction) | capture_working | no |
| 154 | `survey-seed-009` | FLEX — semantic gating for trajectory merge | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 155 | `survey-seed-014` | Memento 2 (2512.22716 follow-on) — stateful reflective memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 156 | `survey-seed-025` | H2R — self-evolving memory line (survey-cited) | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 157 | `survey-seed-039` | ExpeL — experiential learning memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 158 | `survey-seed-052` | XAgent long-horizon memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 159 | `survey-seed-055` | ProAgent procedural memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 160 | `survey-seed-059` | VideoAgent episodic memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 161 | `survey-seed-060` | Cradle agent memory (game/env) | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 162 | `survey-seed-061` | OdysseyAgent long-horizon memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 163 | `survey-seed-062` | LLaMA-Rider / game skill memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 164 | `survey-seed-063` | GITM — generally better Minecraft agents memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 165 | `survey-seed-096` | DialDoc / document-grounded dialogue memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 166 | `survey-seed-097` | MultiWOZ belief-state memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 167 | `survey-seed-098` | SGD Schema-Guided Dialogue memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 168 | `survey-seed-099` | Taskmaster dialogue memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 169 | `survey-seed-100` | PersonaChat / personalization memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 170 | `survey-seed-101` | MSC — Multi-Session Chat | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 171 | `survey-seed-102` | Conversation Chronicles long dialogue | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 172 | `survey-seed-111` | BookSum / chapter summarization memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 173 | `survey-seed-112` | SummScreen dialogue summarization | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 174 | `survey-seed-113` | MediaSum interview summarization | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 175 | `survey-seed-114` | QMSum query-based meeting memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 176 | `survey-seed-115` | MeetingBank meeting memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 177 | `survey-seed-116` | AMI / ICSI meeting corpora (memory baselines) | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 178 | `survey-seed-117` | TopicSeg classical text segmentation (Choi, etc.) | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 179 | `survey-seed-118` | TextTiling classical boundary detection | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 180 | `survey-seed-119` | C99 / TopicTiling segmentation | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 181 | `survey-seed-120` | BERT-based dialogue discourse segmentation papers | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 182 | `survey-seed-121` | SuperDialseg dialogue segmentation | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 183 | `survey-seed-122` | DialSTART family follow-ons | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 184 | `survey-seed-125` | MemTree hierarchical memory tree | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 185 | `survey-seed-126` | TiM follow-on think-in-memory variants | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 186 | `survey-seed-195` | Temporal.io durable execution vs episode boundaries | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 187 | `survey-seed-196` | Cadence/workflow engines as episode stores | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 188 | `survey-seed-197` | OpenTelemetry span→episode mapping | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 189 | `2304.13343` | SCM (Self-Controlled Memory) | FULL | 3 (episode/boundary) | capture_working,episode_cognify | no |
| 190 | `2305.02747` | Unsupervised Dialogue Topic Seg (DialSTART) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 191 | `2305.16291` | Voyager | FULL | 3 (episode/boundary) | episode_cognify | no |
| 192 | `2308.10464` | HyperSeg (HDC topic seg) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 193 | `2311.08719` | Think-in-Memory (TiM) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 194 | `2403.11901` | Larimar | FULL | 3 (episode/boundary) | episode_cognify | no |
| 195 | `2410.12480` | KcMF — knowledge-compliant schema/entity matching | FULL | 3 (episode/boundary) | episode_cognify | no |
| 196 | `2502.05589` | SeCom (segment memory + compress denoise) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 197 | `2504.16754` | HEMA | FULL | 3 (episode/boundary) | episode_cognify | no |
| 198 | `2506.06326` | MemoryOS | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph,conflict_compose | no |
| 199 | `2506.08098` | Cognitive Weave | FULL | 3 (episode/boundary) | episode_cognify | no |
| 200 | `2508.03341` | Nemori / What Deserves Memory | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph | no |
| 201 | `2512.17083` | Granularity-Aware Dialogue Topic Seg | FULL | 3 (episode/boundary) | episode_cognify | no |
| 202 | `2601.03785` | Membox — topic continuity memory boxes | FULL | 3 (episode/boundary) | episode_cognify | no |
| 203 | `2601.07582` | ES-Mem | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph | no |
| 204 | `2604.20943` | Sleep-Consolidated Memory (preview) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 205 | `2605.16045` | RecMem | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph | no |
| 206 | `survey-seed-002` | Cognee — queryable graph embeddings memory toolkit | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 207 | `survey-seed-003` | OpenMemory — graph memory toolkit | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 208 | `survey-seed-004` | MemMachine — graph memory toolkit | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 209 | `survey-seed-005` | Memary — graph memory toolkit | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 210 | `survey-seed-010` | Classic REBEL — seq2seq relation extraction | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 211 | `survey-seed-011` | Stanford OpenIE — open information extraction | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 212 | `survey-seed-017` | AgentGit — git-like rollback/branch for agent workflows | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 213 | `survey-seed-026` | MIRIX — multi-agent memory organization (survey/toolkit) | seed_placeholder | 4 (graph/conflict) | anchors_graph,privacy_seal | yes |
| 214 | `survey-seed-030` | LangGraph long-term memory store docs | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 215 | `survey-seed-031` | LlamaIndex memory modules docs | seed_placeholder | 4 (graph/conflict) | anchors_graph,hydrate_retrieve | yes |
| 216 | `survey-seed-036` | ChatDB — database-as-memory agents | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 217 | `survey-seed-037` | DB-GPT memory / knowledge layer | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 218 | `survey-seed-053` | ChatArena multi-agent memory | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 219 | `survey-seed-054` | AgentVerse multi-agent memory | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 220 | `survey-seed-068` | ChatDB SQL memory (survey-cited) | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 221 | `survey-seed-070` | Zep Cloud product docs (beyond paper) | seed_placeholder | 4 (graph/conflict) | anchors_graph,conflict_compose | yes |
| 222 | `survey-seed-071` | Graphiti OSS README / temporal ops | seed_placeholder | 4 (graph/conflict) | anchors_graph,conflict_compose | yes |
| 223 | `survey-seed-072` | Mem0 product docs / graph mode | seed_placeholder | 4 (graph/conflict) | anchors_graph,conflict_compose | yes |
| 224 | `survey-seed-073` | HippoRAG code release / OpenIE pipeline notes | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 225 | `survey-seed-074` | Microsoft GraphRAG docs / Leiden communities | seed_placeholder | 4 (graph/conflict) | anchors_graph,hydrate_retrieve | yes |
| 226 | `survey-seed-075` | LightRAG repo docs | seed_placeholder | 4 (graph/conflict) | anchors_graph,hydrate_retrieve | yes |
| 227 | `survey-seed-076` | Nano-GraphRAG / community variants | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 228 | `survey-seed-077` | FastGraphRAG variants | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 229 | `survey-seed-078` | KG-RAG / KG-enhanced RAG surveys tails | seed_placeholder | 4 (graph/conflict) | anchors_graph,hydrate_retrieve | yes |
| 230 | `survey-seed-079` | ToG — Think-on-Graph | seed_placeholder | 4 (graph/conflict) | anchors_graph,hydrate_retrieve | yes |
| 231 | `survey-seed-080` | StructGPT structured knowledge memory | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 232 | `survey-seed-090` | FEVER fact verification vs SUPERSEDES | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 233 | `survey-seed-091` | VitaminC fact revision corpus | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 234 | `survey-seed-123` | GIMS / graph-informed memory systems (survey tails) | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 235 | `survey-seed-124` | A-MEM follow-on notes / Zettelkasten agent memory | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 236 | `survey-seed-135` | CRDT primers for parallel compose (automerge/yjs) | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 237 | `survey-seed-136` | Event sourcing primers for audit losers | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 238 | `survey-seed-137` | CQRS read-model projections vs compose | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 239 | `survey-seed-138` | Operational transform vs CRDT conflict notes | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 240 | `survey-seed-139` | Anomaly detection for stale belief edges | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 241 | `survey-seed-140` | Knowledge graph embedding entity resolve (TransE/RotatE) | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 242 | `survey-seed-141` | Entity linking surveys (EL) for Anchor resolve | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 243 | `survey-seed-142` | Coreference resolution for agent entity merge | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 244 | `survey-seed-143` | OpenIE6 / IMoJIE extraction pipelines | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 245 | `survey-seed-144` | SpaCy / GLINER IE engineering notes | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 246 | `2307.07697` | Think-on-Graph (ToG) | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 247 | `2401.03426` | LLM entity resolution (cost-efficient) | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 248 | `2403.06434` | BoostER — LLM-enhanced entity resolution | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 249 | `2404.16130` | GraphRAG | FULL | 4 (graph/conflict) | anchors_graph | no |
| 250 | `2405.14831` | HippoRAG | FULL | 4 (graph/conflict) | anchors_graph | no |
| 251 | `2406.14550` | GraphReader | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 252 | `2407.04363` | AriGraph | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 253 | `2408.00103` | ReLiK (EL + RE) | FULL | 4 (graph/conflict) | anchors_graph | no |
| 254 | `2410.05779` | LightRAG | FULL | 4 (graph/conflict) | anchors_graph | no |
| 255 | `2501.00309` | GraphRAG with Graphs | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 256 | `2501.13956` | Zep / Graphiti | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 257 | `2502.14802` | HippoRAG 2 | FULL | 4 (graph/conflict) | anchors_graph | no |
| 258 | `2503.21322` | HyperGraphRAG | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 259 | `2504.19413` | Mem0 / Mem0g | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 260 | `2506.07398` | G-Memory | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 261 | `2601.02744` | SYNAPSE — spreading activation episodic-semantic graph | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 262 | `2601.03236` | MAGMA | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 263 | `2601.12331` | ppRAG / CAPRISE — encrypted distance-preserving RAG | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 264 | `2602.05665` | Graph-based Agent Memory survey | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 265 | `2603.11768` | SSGM | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 266 | `2605.15701` | H-Mem (hybrid tree+graph) | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 267 | `2605.17301` | ConflictRAG — conflict-aware RAG | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | yes |
| 268 | `2605.28773` | FluxMem — connectivity-evolving memory graph | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 269 | `2606.06036` | MRAgent — active graph memory reconstruction | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 270 | `2606.06240` | TOKI | FULL | 4 (graph/conflict) | conflict_compose | no |
| 271 | `2607.05844` | StateFuse | FULL | 4 (graph/conflict) | conflict_compose | no |
| 272 | `survey-seed-001` | CaMeL — capability-based information flow control for LLMs | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 273 | `survey-seed-200` | Prompt logging redaction standards | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 274 | `survey-seed-201` | PII detection libraries for capture redaction | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 275 | `survey-seed-202` | Presidio / common redaction engines | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 276 | `survey-seed-203` | DLP patterns for agent transcripts | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 277 | `survey-seed-204` | Secret scanning (trufflehog/gitleaks) at capture | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 278 | `survey-seed-205` | OWASP LLM Top 10 — sensitive info disclosure | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 279 | `survey-seed-206` | OWASP Agentic AI security draft | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 280 | `survey-seed-207` | NIST AI RMF memory/governance mapping | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 281 | `survey-seed-208` | Contextual integrity (Nissenbaum) primers | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 282 | `survey-seed-209` | GDPR right-to-erasure vs invalidate+audit | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 283 | `survey-seed-210` | CCPA deletion vs belief history retention | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 284 | `survey-seed-211` | Differential privacy for shared memory aggregates | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 285 | `survey-seed-212` | Secure enclaves for sealed packs (SGX/SEV notes) | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 286 | `survey-seed-213` | TPM / hardware key custody for .kpack | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 287 | `survey-seed-214` | age / ssh-age recipient patterns beyond C2SP | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 288 | `survey-seed-215` | TUF / update frameworks for pack distribution | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 289 | `survey-seed-216` | Sigstore / keyless signing for shareable anchors | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 290 | `survey-seed-217` | Paseto / Branca token capability notes | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 291 | `survey-seed-218` | Biscuit vs Macaroon attenuation cookbook | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 292 | `survey-seed-219` | UCANs — user-controlled authorization networks | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 293 | `survey-seed-220` | Object capabilities (Miller) deep primer | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 294 | `survey-seed-221` | Spritely Goblins / OcapPub deeper docs | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 295 | `survey-seed-222` | Cap'n Proto RPC capability patterns | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 296 | `survey-seed-223` | E language capability lessons for agents | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 297 | `2303.17760` | CAMEL | FULL | 5 (privacy/capability) | conflict_compose | no |
| 298 | `2409.00138` | PrivacyLens | FULL | 5 (privacy/capability) | privacy_seal | yes |
| 299 | `2502.13172` | MEXTRA / Unveiling Privacy Risks in LLM Agent Memory | FULL | 5 (privacy/capability) | privacy_seal | yes |
| 300 | `2505.18279` | Collaborative Memory | FULL | 5 (privacy/capability) | anchors_graph,conflict_compose | no |
| 301 | `2505.23643` | Fides — IFC for securing AI agents | FULL | 5 (privacy/capability) | privacy_seal | no |
| 302 | `2512.04668` | Topology Matters / MAMA | FULL | 5 (privacy/capability) | privacy_seal | no |
| 303 | `2602.11510` | AgentLeak | FULL | 5 (privacy/capability) | conflict_compose | yes |
| 304 | `2604.26525` | PRAG — end-to-end privacy-preserving RAG | FULL | 5 (privacy/capability) | privacy_seal | yes |
| 305 | `2605.10614` | PRISM | FULL | 5 (privacy/capability) | privacy_seal | no |
| 306 | `2606.24535` | MemClaw / Governed Shared Memory | FULL | 5 (privacy/capability) | anchors_graph,conflict_compose | no |
| 307 | `2606.29788` | MemLeak | FULL | 5 (privacy/capability) | conflict_compose | yes |
| 308 | `biscuits-design-spec` | Biscuits DESIGN+spec | FULL | 5 (privacy/capability) | privacy_seal | no |
| 309 | `c2sp-age-md` | C2SP age.md | FULL | 5 (privacy/capability) | privacy_seal | no |
| 310 | `capability-myths-demolished` | Capability Myths Demolished | FULL | 5 (privacy/capability) | privacy_seal | no |
| 311 | `libsodium-seal-box-sign` | libsodium seal/box/sign | FULL | 5 (privacy/capability) | privacy_seal | no |
| 312 | `macaroons-ndss-2014` | Macaroons NDSS 2014 | FULL | 5 (privacy/capability) | privacy_seal | no |
| 313 | `mls-rfc-9420-9750` | MLS RFC 9420 / 9750 | FULL | 5 (privacy/capability) | privacy_seal | no |
| 314 | `spritely-ocappub` | Spritely / OcapPub | FULL | 5 (privacy/capability) | privacy_seal | no |
| 315 | `vault-eknow-2025` | VAULT (eKNOW 2025) | FULL | 5 (privacy/capability) | privacy_seal | no |
| 316 | `1803.05355` | FEVER | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 317 | `1911.00172` | kNN-LM | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 318 | `2002.08909` | REALM | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 319 | `2004.12832` | ColBERT | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 320 | `2005.11485` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 321 | `2103.08541` | VitaminC | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 322 | `2208.03299` | Atlas | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 323 | `2306.03901` | ChatDB | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 324 | `2308.02151` | Retroformer | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 325 | `2310.06201` | Same Selective Context paper as `2304.12102` (BATCH6 FULL) — body fetched, not re-marked | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 326 | `2402.04624` | MemoryLLM | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 327 | `2402.13753` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 328 | `2406.04151` | AgentGym | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 329 | `2502.00592` | M+ | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 330 | `2509.24704` | MemGen | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 331 | `2510.08558` | Early Experience | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 332 | `2512.10696` | ReMe | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 333 | `2603.24639` | ERL | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 334 | `survey-seed-012` | MemU — product memory system (survey-named) | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 335 | `survey-seed-013` | Memobase — product memory system (survey-named) | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 336 | `survey-seed-016` | DNC — Differentiable Neural Computer | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 337 | `survey-seed-018` | Retroformer — parametric memory adaptation | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 338 | `survey-seed-019` | Early Experience — parametric/experiential adaptation | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 339 | `survey-seed-020` | MemoryLLM — latent parametric memory | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 340 | `survey-seed-021` | M+ memory model — latent/parametric lineage | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 341 | `survey-seed-022` | MemGen — generative parametric memory | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 342 | `survey-seed-032` | Haystack memory / agent memory docs | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 343 | `survey-seed-033` | CrewAI memory docs | seed_placeholder | 6 (eng-judgment) | anchors_graph | no |
| 344 | `survey-seed-034` | AutoGPT memory backend docs | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 345 | `survey-seed-035` | BabyAGI / task memory lineage | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 346 | `survey-seed-038` | ThinkGPT — thinking + memory patterns | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 347 | `survey-seed-040` | ClinicalAgent / MedAgents memory slices | seed_placeholder | 6 (eng-judgment) | privacy_seal | no |
| 348 | `survey-seed-051` | OpenAgents memory modules | seed_placeholder | 6 (eng-judgment) | anchors_graph | no |
| 349 | `survey-seed-058` | MMAC / multi-modal agent memory survey tails | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 350 | `survey-seed-064` | Plan-and-Solve / plan memory | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 351 | `survey-seed-066` | PEARL planning memory | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 352 | `survey-seed-069` | SQL-of-Thought / NL2SQL memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 353 | `survey-seed-129` | Human episodic memory models → agent mapping papers | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 354 | `survey-seed-130` | Complementary learning systems (CLS) → L2/L3 mapping | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 355 | `survey-seed-131` | Hopfield / modern Hopfield retrieval memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 356 | `survey-seed-132` | KAN / kernel memory analogies (supporting) | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 357 | `survey-seed-133` | Vector DB product memory patterns (Chroma/Weaviate/Qdrant) | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 358 | `survey-seed-134` | pgvector / sqlite-vss engineering memory notes | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 359 | `survey-seed-149` | Adaptive retrieval controllers beyond Adaptive-RAG | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 360 | `survey-seed-150` | FLARE active retrieval | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 361 | `survey-seed-151` | IRCoT interleaving retrieval | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 362 | `survey-seed-152` | DSP / Demonstrate-Search-Predict | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 363 | `survey-seed-153` | REPLUG retrieval-enhanced LMs | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 364 | `survey-seed-154` | Atlas few-shot retrieval memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 365 | `survey-seed-155` | REALM pretraining retrieval memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 366 | `survey-seed-156` | kNN-LM datastore memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 367 | `survey-seed-157` | SPALM / sparse memory LMs | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 368 | `survey-seed-158` | Product Quantization memory indexes | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 369 | `survey-seed-159` | HNSW engineering notes for hydrate latency | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 370 | `survey-seed-160` | BM25 + dense hybrid retrieval recipes | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 371 | `survey-seed-161` | ColBERT late interaction retrieval | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 372 | `survey-seed-162` | BGE / E5 embedding model cards for memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 373 | `survey-seed-163` | Instruction-aware embeddings for agent memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 374 | `survey-seed-189` | OpenAI Swarm / Agents SDK memory patterns | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 375 | `survey-seed-190` | Semantic Kernel memory store | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 376 | `survey-seed-191` | Haystack Agent memory components | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 377 | `survey-seed-192` | DSPy memory / state modules | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 378 | `survey-seed-193` | Guidance / Outlines constrained decode + memory | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 379 | `survey-seed-194` | PydanticAI deps/memory patterns | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 380 | `1410.3916` | Memory Networks | FULL | 6 (eng-judgment) | capture_working | no |
| 381 | `1805.04263` | Memory-net / memorizing-transformer lineage | FULL | 6 (eng-judgment) | anchors_graph | no |
| 382 | `2004.04906` | Memory-net / memorizing-transformer lineage | FULL | 6 (eng-judgment) | anchors_graph | no |
| 383 | `2005.11401` | RAG (Lewis et al.) | FULL | 6 (eng-judgment) | capture_working | no |
| 384 | `2101.06804` | KATE — kNN in-context example selection | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 385 | `2109.10862` | Recursive Summarizing Books | FULL | 6 (eng-judgment) | episode_cognify | no |
| 386 | `2112.04426` | RETRO | FULL | 6 (eng-judgment) | episode_cognify | no |
| 387 | `2203.08913` | Memorizing Transformers | FULL | 6 (eng-judgment) | capture_working | no |
| 388 | `2205.12674` | Memory-net / memorizing-transformer lineage | FULL | 6 (eng-judgment) | anchors_graph | no |
| 389 | `2207.06881` | Recurrent Memory Transformer | FULL | 6 (eng-judgment) | capture_working | no |
| 390 | `2210.03629` | ReAct | FULL | 6 (eng-judgment) | capture_working | no |
| 391 | `2212.10496` | HyDE — hypothetical document embeddings | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 392 | `2212.14024` | DSP — Demonstrate-Search-Predict | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 393 | `2302.04761` | Toolformer | FULL | 6 (eng-judgment) | capture_working | no |
| 394 | `2303.11366` | Reflexion | FULL | 6 (eng-judgment) | capture_working | no |
| 395 | `2304.03442` | Generative Agents | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 396 | `2304.08467` | Gist Tokens — prompt compression | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 397 | `2304.12102` | Selective Context | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 398 | `2305.03010` | GEIA (generative embedding inversion) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 399 | `2305.08371` | SuperDialseg | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 400 | `2305.09645` | StructGPT — IRR over structured data | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 401 | `2307.07924` | ChatDev | FULL | 6 (eng-judgment) | conflict_compose | no |
| 402 | `2308.00352` | MetaGPT | FULL | 6 (eng-judgment) | conflict_compose | no |
| 403 | `2308.08155` | AutoGen | FULL | 6 (eng-judgment) | conflict_compose | no |
| 404 | `2308.08239` | MemoChat | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 405 | `2308.10144` | ExpeL | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 406 | `2308.10848` | AgentVerse — dynamic multi-agent collaboration | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 407 | `2308.15022` | Recursive Summarization (dialogue memory) | FULL | 6 (eng-judgment) | capture_working,episode_cognify | no |
| 408 | `2309.04697` | Leakage-Abuse Attacks on SSE | FULL | 6 (eng-judgment) | hydrate_retrieve | yes |
| 409 | `2309.07864` | Rise and Potential of LLM Agents (survey; §memory) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 410 | `2310.04408` | RECOMP | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 411 | `2310.05029` | MemWalker — interactive reading memory tree | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 412 | `2310.05736` | LLMLingua | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 413 | `2310.06816` | Text Embeddings Reveal (Almost) As Much As Text | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 414 | `2310.06839` | LongLLMLingua | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 415 | `2311.09210` | Chain-of-Note (CoN) — robust RALM | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 416 | `2312.10997` | RAG for LLMs — survey | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 417 | `2401.03462` | Activation Beacon | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 418 | `2401.18059` | RAPTOR | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 419 | `2402.03367` | RAG-Fusion — multi-query RRF | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 420 | `2402.07867` | PoisonedRAG | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 421 | `2402.09727` | ReadAgent — gist memory for long contexts | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 422 | `2402.11163` | KG-Agent | FULL | 6 (eng-judgment) | anchors_graph | no |
| 423 | `2402.17840` | Spill the Beans (RAG datastore extraction) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 424 | `2403.02691` | InjecAgent | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 425 | `2403.04957` | Automatic Universal Prompt Injection Attacks | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 426 | `2403.12968` | LLMLingua-2 | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 427 | `2403.14403` | Adaptive-RAG | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 428 | `2404.13501` | Zhang memory mechanisms survey | FULL | 6 (eng-judgment) | capture_working | no |
| 429 | `2405.05175` | AirGapAgent | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 430 | `2405.20446` | RAG membership inference | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 431 | `2406.03007` | BadAgent — backdoor attacks on LLM agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 432 | `2406.05804` | Review of LLM-Agent Paradigms (tool/RAG/planning) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 433 | `2406.13352` | AgentDojo | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 434 | `2407.02485` | RankRAG — unified context ranking + generation | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 435 | `2407.09450` | EM-LLM | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph | no |
| 436 | `2407.12784` | AgentPoison (memory/RAG backdoor) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 437 | `2408.09559` | HiAgent — hierarchical working memory management | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 438 | `2410.15665` | Long Term Memory: Foundation of AI Self-Evolution | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 439 | `2411.00489` | AI Long-term Memory survey | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 440 | `2411.01705` | RAG backdoor data extraction | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 441 | `2501.06322` | Multi-Agent Collaboration Mechanisms survey | FULL | 6 (eng-judgment) | conflict_compose | no |
| 442 | `2501.12948` | Additional fetched fulltexts used as supporting | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 443 | `2502.00306` | Stealthy MIA for RAG (Riddle Me This) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 444 | `2502.12110` | A-MEM | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 445 | `2503.03704` | MINJA (query-only memory injection) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 446 | `2503.08026` | RMM — Reflective Memory Management | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 447 | `2503.18813` | Additional fetched fulltexts used as supporting | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 448 | `2503.21760` | MemInsight — autonomous memory augmentation | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 449 | `2504.11703` | Progent (privilege control) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 450 | `2504.13171` | Sleep-time Compute | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 451 | `2504.15965` | From Human Memory to AI Memory survey | FULL | 6 (eng-judgment) | anchors_graph | no |
| 452 | `2504.18070` | PropRAG | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 453 | `2505.00675` | Additional fetched fulltexts used as supporting | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 454 | `2505.02099` | MemEngine — modular memory library | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 455 | `2505.19549` | Multi-granularity conversational memory (MemGAS) | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph | no |
| 456 | `2505.23052` | RAGRouter — RAG-aware query routing | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 457 | `2505.23841` | SkewRoute — training-free KG-RAG LLM routing | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 458 | `2505.24478` | Cognee / KG–LLM interface optimization | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 459 | `2506.15841` | MEM1 (constant-size IS memory) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 460 | `2507.02259` | MemAgent | FULL | 6 (eng-judgment) | episode_cognify | no |
| 461 | `2507.03724` | MemOS | FULL | 6 (eng-judgment) | capture_working,episode_cognify | no |
| 462 | `2507.06229` | Agent KB (cross-framework experience) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 463 | `2507.07957` | MIRIX — multi-agent memory system | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 464 | `2507.10457` | LPCI — logic-layer prompt control injection | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 465 | `2508.04903` | RCR-Router | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 466 | `2508.06433` | Memp — agent procedural memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 467 | `2508.08997` | Intrinsic Memory Agents — heterogeneous MAS memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 468 | `2508.09736` | M3-Agent — multimodal long-term memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 469 | `2508.16153` | Memento (case-based M-MDP memory) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 470 | `2508.19828` | Memory-R1 | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 471 | `2509.13313` | ReSum — context summarization for search agents | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 472 | `2509.25140` | ReasoningBank + MaTTS | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 473 | `2509.25911` | Mem-α | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 474 | `2510.04851` | LEGOMem (modular procedural multi-agent) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 475 | `2510.05244` | IPI Firewalls (Minimizer + Sanitizer) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 476 | `2510.06719` | DP Synthetic Text for RAG | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 477 | `2510.10397` | AssoMem | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 478 | `2510.11967` | Context-Folding — branch/return context management | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 479 | `2510.12635` | Memory as Action / MemAct | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 480 | `2510.18866` | LightMem | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 481 | `2510.24699` | AgentFold — proactive context management | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 482 | `2510.26486` | LINK-KG — coreference-resolved KG construction | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 483 | `2511.00628` | AgentGit — Git-like MAS checkpoints/branching | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 484 | `2511.06449` | FLEX | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 485 | `2511.13593` | O-Mem (omni persona/episodic/working) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 486 | `2512.13564` | Memory in the Age of AI Agents (survey) | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 487 | `2512.22716` | Memento 2 | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 488 | `2601.05960` | Memory-as-a-Tool | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 489 | `2602.06052` | Agent Memory Second Half survey | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 490 | `2602.19320` | Anatomy of Agentic Memory (survey) | FULL | 6 (eng-judgment) | conflict_compose | no |
| 491 | `2603.02228` | Neural Paging — learned context management | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 492 | `2603.07670` | Memory for Autonomous LLM Agents (survey) | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 493 | `2603.15994` | Selective Memory / supersession chains | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 494 | `2604.04853` | MemMachine — ground-truth-preserving agent memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 495 | `2604.21748` | StructMem — structured hierarchical memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 496 | `2605.06716` | From Storage to Experience (survey) | FULL | 6 (eng-judgment) | anchors_graph | no |
| 497 | `2605.27825` | MRMMIA — membership inference on chat-agent memory | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 498 | `2606.04425` | Cross-Session Stored Prompt Injection | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 499 | `2606.10525` | Assessing Automated Prompt Injection in Agentic Environments | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 500 | `adr-qoc-ibis-design-rationale-practice` | ADR / QOC / IBIS design-rationale practice | FULL | 6 (eng-judgment) | hydrate_retrieve | no |

## Machine-readable

- `docs/research/queue/full_queue.jsonl` — one JSON object per line.
- Rebuild: `python3 scripts/research/build_full_queue.py`
- Fetch arXiv HTML: `python3 scripts/research/fetch_paper.py <id>`

