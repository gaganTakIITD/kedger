# Kedger Track 0 — FULL deep-read queue (≥500)

> **Program:** Kedger research (measure → refine).
> **Honesty rule:** `FULL` only if listed in `CORPUS_INVENTORY.md` §2 ledger.
> `seed_placeholder` entries need fetch — they are **not** FULL deep-reads.
> Historical memos may say “MoDeX”; that is labeling debt, not product identity.

## Stats

| Metric | Value |
|--------|------:|
| Unique arXiv IDs scanned | 161 |
| FULL (from inventory) | 151 |
| queued (scanned, not FULL) | 26 |
| seed_placeholder (pad) | 323 |
| **Queue size** | **500** |
| Markdown files scanned | 33 |

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
| 1 | `2310.17884` | ConfAIde / Can LLMs Keep a Secret? | queued | 1 (eval/failure) | hydrate_retrieve | yes |
| 2 | `2506.21605` | MemBench | queued | 1 (eval/failure) | hydrate_retrieve | yes |
| 3 | `2601.06966` | RealMem | queued | 1 (eval/failure) | hydrate_retrieve | yes |
| 4 | `survey-seed-006` | MemoryArena — agent memory evaluation suite | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 5 | `survey-seed-007` | MemBench — memory benchmark suite | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 6 | `survey-seed-008` | RealMem — realistic memory evaluation | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 7 | `survey-seed-015` | LongMemEval-V2 (2605.12493) — eng-colleague eval follow-on | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 8 | `survey-seed-042` | AppWorld / environment memory benchmarks | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 9 | `survey-seed-043` | AgentBench — agent evaluation harness | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 10 | `survey-seed-044` | GAIA benchmark — tool-use failure modes | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 11 | `survey-seed-045` | WebArena / BrowserGym memory carryover | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 12 | `survey-seed-046` | SWE-bench agent trajectory memory notes | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 13 | `survey-seed-047` | τ-bench / tool-agent eval memory slices | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 14 | `survey-seed-081` | Unify GraphRAG evaluation protocols | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 15 | `survey-seed-082` | RGB — retrieval-augmented generation benchmark | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 16 | `survey-seed-083` | CRAG — Corrective RAG benchmark | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 17 | `survey-seed-084` | MultiHop-RAG benchmark | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 18 | `survey-seed-085` | HotpotQA as memory multi-hop probe | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 19 | `survey-seed-086` | 2WikiMultiHopQA probe | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 20 | `survey-seed-087` | MuSiQue multi-hop probe | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 21 | `survey-seed-088` | Bamboogle / Compose multi-hop | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 22 | `survey-seed-089` | TriviaQA / Natural Questions RAG baselines | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 23 | `survey-seed-092` | ConflictQA / conflicting knowledge eval | seed_placeholder | 1 (eval/failure) | conflict_compose | yes |
| 24 | `survey-seed-093` | FreshQA temporal freshness eval | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 25 | `survey-seed-094` | RealtimeQA temporal memory | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 26 | `survey-seed-095` | SituatedQA / context-dependent answers | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 27 | `survey-seed-103` | PerLTQA personal long-term QA | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 28 | `survey-seed-104` | Long-context Needle-in-Haystack protocols | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 29 | `survey-seed-105` | RULER long-context eval suite | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 30 | `survey-seed-106` | ∞Bench long-context | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 31 | `survey-seed-107` | LongBench / LongBench-v2 | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 32 | `survey-seed-108` | L-Eval long-context eval | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 33 | `survey-seed-109` | ZeroSCROLLS long-context | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 34 | `survey-seed-110` | QuALITY long-doc reading | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 35 | `survey-seed-145` | LLM-as-extractor reliability studies | seed_placeholder | 1 (eval/failure) | anchors_graph | yes |
| 36 | `survey-seed-146` | Hallucination audits for memory write paths | seed_placeholder | 1 (eval/failure) | conflict_compose | yes |
| 37 | `survey-seed-147` | Self-RAG / CRAG corrective retrieval | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 38 | `survey-seed-148` | Corrective RAG (Yan et al.) full mechanisms | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 39 | `survey-seed-245` | Datasheets for memory datasets | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 40 | `survey-seed-247` | HELM / decoding trust eval suites | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 41 | `survey-seed-248` | BIG-bench agent-adjacent tasks | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 42 | `survey-seed-249` | MMLU as non-memory control baseline | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 43 | `survey-seed-250` | AgentBoard evaluation framework | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 44 | `survey-seed-251` | AgentEval / LLM-as-judge for agents | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 45 | `survey-seed-252` | LLM-as-judge bias studies (memory claims) | seed_placeholder | 1 (eval/failure) | hydrate_retrieve | yes |
| 46 | `1809.09600` | HotpotQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 47 | `2011.01060` | 2WikiMultiHopQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 48 | `2305.13300` | Adaptive Chameleon (knowledge conflicts) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 49 | `2307.03172` | Lost in the Middle | FULL | 1 (eval/failure) | episode_cognify,hydrate_retrieve | no |
| 50 | `2307.13854` | WebArena | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 51 | `2308.03688` | AgentBench | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 52 | `2308.14508` | LongBench | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 53 | `2309.01431` | RGB (RAG Benchmark) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 54 | `2310.03214` | FreshLLMs / FreshQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 55 | `2310.11511` | Self-RAG | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 56 | `2311.12983` | GAIA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 57 | `2401.15391` | MultiHop-RAG | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 58 | `2401.15884` | Corrective Retrieval Augmented Generation | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 59 | `2402.13718` | ∞Bench (InfiniteBench) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 60 | `2402.16288` | PerLTQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 61 | `2402.17753` | LoCoMo | FULL | 1 (eval/failure) | episode_cognify | yes |
| 62 | `2404.06654` | RULER | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 63 | `2406.04744` | CRAG (Comprehensive RAG Benchmark) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 64 | `2406.13144` | DialSim / LongDialQA | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 65 | `2407.11963` | NeedleBench | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 66 | `2410.10813` | LongMemEval | FULL | 1 (eval/failure) | episode_cognify,hydrate_retrieve | yes |
| 67 | `2412.15204` | LongBench v2 | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 68 | `2502.09597` | PrefEval | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 69 | `2507.05257` | MemoryAgentBench | FULL | 1 (eval/failure) | episode_cognify | yes |
| 70 | `2510.17281` | MemoryBench (continual feedback) | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 71 | `2602.16313` | MemoryArena | FULL | 1 (eval/failure) | hydrate_retrieve | no |
| 72 | `2605.12493` | LongMemEval-V2 | FULL | 1 (eval/failure) | hydrate_retrieve | yes |
| 73 | `survey-seed-023` | HiAgent — working-memory manager for multi-turn tasks | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 74 | `survey-seed-024` | ReSum — working-memory / resume manager | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 75 | `survey-seed-027` | Letta (MemGPT product line) docs — paging UX | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 76 | `survey-seed-028` | Claude Code memory / CLAUDE.md patterns (docs) | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 77 | `survey-seed-029` | Cursor Memories / Rules docs | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 78 | `survey-seed-041` | JARVIS / HuggingGPT tool memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 79 | `survey-seed-048` | ToolBench memory-of-tools patterns | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 80 | `survey-seed-049` | API-Bank tool trajectory memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 81 | `survey-seed-050` | RestGPT stateful API memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 82 | `survey-seed-056` | TPTU tool planning memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 83 | `survey-seed-057` | Chameleon LLM tool composer memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 84 | `survey-seed-065` | ReWOO planner memory separation | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 85 | `survey-seed-067` | RET-LLM follow-ons / SQL memory agents | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 86 | `survey-seed-127` | SCM controller variants beyond 2304.13343 | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 87 | `survey-seed-128` | Ebbinghaus forgetting implementations beyond MemoryBank | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 88 | `survey-seed-164` | Matryoshka embeddings for budgeted hydrate | seed_placeholder | 2 (capture/compaction) | hydrate_retrieve | yes |
| 89 | `survey-seed-165` | Prompt compression (LLMLingua / LongLLMLingua) | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 90 | `survey-seed-166` | Selective Context / semantic compression | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 91 | `survey-seed-167` | RECOMP retrieve-compress | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 92 | `survey-seed-168` | xRAG / representation compression | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 93 | `survey-seed-169` | Gisting / gist tokens memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 94 | `survey-seed-170` | Activation Beacon / compressed KV | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 95 | `survey-seed-171` | PyramidKV / multilevel KV eviction | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 96 | `survey-seed-172` | Quest / KV retrieval for long context | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 97 | `survey-seed-173` | LOOK-M multimodal KV memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 98 | `survey-seed-174` | Heavy-Hitter variants beyond H₂O | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 99 | `survey-seed-175` | Attention sink analyses beyond StreamingLLM | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 100 | `survey-seed-176` | Scissorhands KV eviction | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 101 | `survey-seed-177` | LESS / adaptive KV | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 102 | `survey-seed-178` | Gear / quantized KV cache | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 103 | `survey-seed-179` | KIVI KV cache quantization | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 104 | `survey-seed-180` | SmoothQuant / KV quant engineering | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 105 | `survey-seed-181` | vLLM paged attention engineering notes | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 106 | `survey-seed-182` | SGLang radix attention prefix memory | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 107 | `survey-seed-183` | Anthropic context editing API notes (beyond inventory) | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 108 | `survey-seed-184` | OpenAI Responses / compaction API notes | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 109 | `survey-seed-185` | Gemini context caching docs | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 110 | `survey-seed-186` | AWS Bedrock session memory docs | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 111 | `survey-seed-187` | Azure AI Agent Service memory docs | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 112 | `survey-seed-188` | Google ADK session/memory docs | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 113 | `survey-seed-198` | OTel GenAI semantic conventions for L0 capture | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 114 | `survey-seed-199` | LLM tracing (Langfuse/Phoenix) → Evidence mapping | seed_placeholder | 2 (capture/compaction) | capture_working | yes |
| 115 | `1410.5401` | NTM | FULL | 2 (capture/compaction) | anchors_graph | no |
| 116 | `1901.02860` | Transformer-XL | FULL | 2 (capture/compaction) | capture_working | no |
| 117 | `1911.05507` | Compressive Transformer | FULL | 2 (capture/compaction) | capture_working | no |
| 118 | `2304.11062` | RMT to 1M tokens | FULL | 2 (capture/compaction) | capture_working | no |
| 119 | `2305.01625` | Unlimiformer | FULL | 2 (capture/compaction) | capture_working | no |
| 120 | `2305.10250` | MemoryBank (Zhong forgetting curve) | FULL | 2 (capture/compaction) | capture_working,episode_cognify | no |
| 121 | `2305.14322` | RET-LLM | FULL | 2 (capture/compaction) | capture_working | no |
| 122 | `2305.14788` | AutoCompressors | FULL | 2 (capture/compaction) | capture_working | no |
| 123 | `2305.16300` | Landmark Attention | FULL | 2 (capture/compaction) | capture_working | no |
| 124 | `2306.14048` | H₂O Heavy-Hitter Oracle | FULL | 2 (capture/compaction) | capture_working | no |
| 125 | `2307.06945` | ICAE (In-context Autoencoder) | FULL | 2 (capture/compaction) | capture_working | no |
| 126 | `2309.17453` | StreamingLLM | FULL | 2 (capture/compaction) | capture_working,episode_cognify | no |
| 127 | `2310.08560` | MemGPT | FULL | 2 (capture/compaction) | episode_cognify,anchors_graph,conflict_compose | no |
| 128 | `2403.16971` | AIOS | FULL | 2 (capture/compaction) | capture_working | no |
| 129 | `2404.14469` | SnapKV | FULL | 2 (capture/compaction) | capture_working | no |
| 130 | `claude-code-hooks-compaction-context-editing-docs` | Claude Code Hooks + Compaction + Context editing docs | FULL | 2 (capture/compaction) | capture_working | yes |
| 131 | `claude-code-hooks-docs` | Claude Code hooks docs | FULL | 2 (capture/compaction) | capture_working | no |
| 132 | `claude-compaction-compact-2026-01-12` | Claude Compaction (`compact-2026-01-12`) | FULL | 2 (capture/compaction) | capture_working | yes |
| 133 | `claude-context-editing-clear-tool-uses-thinking` | Claude Context editing (`clear_tool_uses` / thinking) | FULL | 2 (capture/compaction) | capture_working | no |
| 134 | `cursor-hooks-docs` | Cursor hooks docs | FULL | 2 (capture/compaction) | capture_working | no |
| 135 | `magic-wormhole-protocols` | Magic Wormhole protocols | FULL | 2 (capture/compaction) | capture_working | no |
| 136 | `rfc-2693` | SPKI Certificate Theory | FULL | 2 (capture/compaction) | capture_working | no |
| 137 | `survey-seed-009` | FLEX — semantic gating for trajectory merge | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 138 | `survey-seed-014` | Memento 2 (2512.22716 follow-on) — stateful reflective memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 139 | `survey-seed-025` | H2R — self-evolving memory line (survey-cited) | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 140 | `survey-seed-039` | ExpeL — experiential learning memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 141 | `survey-seed-052` | XAgent long-horizon memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 142 | `survey-seed-055` | ProAgent procedural memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 143 | `survey-seed-059` | VideoAgent episodic memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 144 | `survey-seed-060` | Cradle agent memory (game/env) | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 145 | `survey-seed-061` | OdysseyAgent long-horizon memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 146 | `survey-seed-062` | LLaMA-Rider / game skill memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 147 | `survey-seed-063` | GITM — generally better Minecraft agents memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 148 | `survey-seed-096` | DialDoc / document-grounded dialogue memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 149 | `survey-seed-097` | MultiWOZ belief-state memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 150 | `survey-seed-098` | SGD Schema-Guided Dialogue memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 151 | `survey-seed-099` | Taskmaster dialogue memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 152 | `survey-seed-100` | PersonaChat / personalization memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 153 | `survey-seed-101` | MSC — Multi-Session Chat | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 154 | `survey-seed-102` | Conversation Chronicles long dialogue | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 155 | `survey-seed-111` | BookSum / chapter summarization memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 156 | `survey-seed-112` | SummScreen dialogue summarization | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 157 | `survey-seed-113` | MediaSum interview summarization | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 158 | `survey-seed-114` | QMSum query-based meeting memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 159 | `survey-seed-115` | MeetingBank meeting memory | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 160 | `survey-seed-116` | AMI / ICSI meeting corpora (memory baselines) | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 161 | `survey-seed-117` | TopicSeg classical text segmentation (Choi, etc.) | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 162 | `survey-seed-118` | TextTiling classical boundary detection | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 163 | `survey-seed-119` | C99 / TopicTiling segmentation | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 164 | `survey-seed-120` | BERT-based dialogue discourse segmentation papers | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 165 | `survey-seed-121` | SuperDialseg dialogue segmentation | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 166 | `survey-seed-122` | DialSTART family follow-ons | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 167 | `survey-seed-125` | MemTree hierarchical memory tree | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 168 | `survey-seed-126` | TiM follow-on think-in-memory variants | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 169 | `survey-seed-195` | Temporal.io durable execution vs episode boundaries | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 170 | `survey-seed-196` | Cadence/workflow engines as episode stores | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 171 | `survey-seed-197` | OpenTelemetry span→episode mapping | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 172 | `survey-seed-258` | Sleep-time compute papers (beyond Sleep-SCM) | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 173 | `survey-seed-265` | Experience replay buffers (RL) → L2 mapping | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 174 | `survey-seed-266` | Prioritized experience replay | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 175 | `survey-seed-267` | Episodic control (Neural Episodic Control) | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 176 | `survey-seed-272` | Offline RL datasets as episodic corpora | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 177 | `survey-seed-273` | Case-based reasoning classics → Memento mapping | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 178 | `survey-seed-277` | Predictive processing / surprise → EST | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 179 | `survey-seed-279` | Event Segmentation Theory psychology sources | seed_placeholder | 3 (episode/boundary) | episode_cognify | yes |
| 180 | `2304.13343` | SCM (Self-Controlled Memory) | FULL | 3 (episode/boundary) | capture_working,episode_cognify | no |
| 181 | `2305.02747` | Unsupervised Dialogue Topic Seg (DialSTART) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 182 | `2305.16291` | Voyager | FULL | 3 (episode/boundary) | episode_cognify | no |
| 183 | `2308.10464` | HyperSeg (HDC topic seg) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 184 | `2311.08719` | Think-in-Memory (TiM) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 185 | `2403.11901` | Larimar | FULL | 3 (episode/boundary) | episode_cognify | no |
| 186 | `2504.16754` | HEMA | FULL | 3 (episode/boundary) | episode_cognify | no |
| 187 | `2506.06326` | MemoryOS | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph,conflict_compose | no |
| 188 | `2506.08098` | Cognitive Weave | FULL | 3 (episode/boundary) | episode_cognify | no |
| 189 | `2508.03341` | Nemori / What Deserves Memory | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph | no |
| 190 | `2512.17083` | Granularity-Aware Dialogue Topic Seg | FULL | 3 (episode/boundary) | episode_cognify | no |
| 191 | `2601.07582` | ES-Mem | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph | no |
| 192 | `2604.20943` | Sleep-Consolidated Memory (preview) | FULL | 3 (episode/boundary) | episode_cognify | no |
| 193 | `2605.16045` | RecMem | FULL | 3 (episode/boundary) | episode_cognify,anchors_graph | no |
| 194 | `2406.14550` | GraphReader | queued | 4 (graph/conflict) | anchors_graph,conflict_compose | yes |
| 195 | `survey-seed-002` | Cognee — queryable graph embeddings memory toolkit | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 196 | `survey-seed-003` | OpenMemory — graph memory toolkit | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 197 | `survey-seed-004` | MemMachine — graph memory toolkit | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 198 | `survey-seed-005` | Memary — graph memory toolkit | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 199 | `survey-seed-010` | Classic REBEL — seq2seq relation extraction | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 200 | `survey-seed-011` | Stanford OpenIE — open information extraction | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 201 | `survey-seed-017` | AgentGit — git-like rollback/branch for agent workflows | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 202 | `survey-seed-026` | MIRIX — multi-agent memory organization (survey/toolkit) | seed_placeholder | 4 (graph/conflict) | anchors_graph,privacy_seal | yes |
| 203 | `survey-seed-030` | LangGraph long-term memory store docs | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 204 | `survey-seed-031` | LlamaIndex memory modules docs | seed_placeholder | 4 (graph/conflict) | anchors_graph,hydrate_retrieve | yes |
| 205 | `survey-seed-036` | ChatDB — database-as-memory agents | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 206 | `survey-seed-037` | DB-GPT memory / knowledge layer | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 207 | `survey-seed-053` | ChatArena multi-agent memory | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 208 | `survey-seed-054` | AgentVerse multi-agent memory | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 209 | `survey-seed-068` | ChatDB SQL memory (survey-cited) | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 210 | `survey-seed-070` | Zep Cloud product docs (beyond paper) | seed_placeholder | 4 (graph/conflict) | anchors_graph,conflict_compose | yes |
| 211 | `survey-seed-071` | Graphiti OSS README / temporal ops | seed_placeholder | 4 (graph/conflict) | anchors_graph,conflict_compose | yes |
| 212 | `survey-seed-072` | Mem0 product docs / graph mode | seed_placeholder | 4 (graph/conflict) | anchors_graph,conflict_compose | yes |
| 213 | `survey-seed-073` | HippoRAG code release / OpenIE pipeline notes | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 214 | `survey-seed-074` | Microsoft GraphRAG docs / Leiden communities | seed_placeholder | 4 (graph/conflict) | anchors_graph,hydrate_retrieve | yes |
| 215 | `survey-seed-075` | LightRAG repo docs | seed_placeholder | 4 (graph/conflict) | anchors_graph,hydrate_retrieve | yes |
| 216 | `survey-seed-076` | Nano-GraphRAG / community variants | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 217 | `survey-seed-077` | FastGraphRAG variants | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 218 | `survey-seed-078` | KG-RAG / KG-enhanced RAG surveys tails | seed_placeholder | 4 (graph/conflict) | anchors_graph,hydrate_retrieve | yes |
| 219 | `survey-seed-079` | ToG — Think-on-Graph | seed_placeholder | 4 (graph/conflict) | anchors_graph,hydrate_retrieve | yes |
| 220 | `survey-seed-080` | StructGPT structured knowledge memory | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 221 | `survey-seed-090` | FEVER fact verification vs SUPERSEDES | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 222 | `survey-seed-091` | VitaminC fact revision corpus | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 223 | `survey-seed-123` | GIMS / graph-informed memory systems (survey tails) | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 224 | `survey-seed-124` | A-MEM follow-on notes / Zettelkasten agent memory | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 225 | `survey-seed-135` | CRDT primers for parallel compose (automerge/yjs) | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 226 | `survey-seed-136` | Event sourcing primers for audit losers | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 227 | `survey-seed-137` | CQRS read-model projections vs compose | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 228 | `survey-seed-138` | Operational transform vs CRDT conflict notes | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 229 | `survey-seed-139` | Anomaly detection for stale belief edges | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 230 | `survey-seed-140` | Knowledge graph embedding entity resolve (TransE/RotatE) | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 231 | `survey-seed-141` | Entity linking surveys (EL) for Anchor resolve | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 232 | `survey-seed-142` | Coreference resolution for agent entity merge | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 233 | `survey-seed-143` | OpenIE6 / IMoJIE extraction pipelines | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 234 | `survey-seed-144` | SpaCy / GLINER IE engineering notes | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 235 | `survey-seed-243` | Provenance graphs for LLM outputs (survey) | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 236 | `survey-seed-244` | W3C PROV mapping to Evidence rows | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 237 | `survey-seed-280` | Zettelkasten method primers for A-MEM mapping | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 238 | `survey-seed-282` | Roam/Logseq/Obsidian graph UX lessons | seed_placeholder | 4 (graph/conflict) | anchors_graph | yes |
| 239 | `survey-seed-294` | Property-based testing for SUPERSEDES | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 240 | `survey-seed-295` | Jepsen-style linearizability lessons for compose | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 241 | `survey-seed-296` | CALM theorem / coordination-free compose | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 242 | `survey-seed-297` | BAC / BASE consistency for agent memory | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 243 | `survey-seed-298` | Causal consistency primers for multi-writer Anchors | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 244 | `survey-seed-299` | Vector clocks / version vectors | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 245 | `survey-seed-300` | Merkle clocks / hash chains for audit | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 246 | `survey-seed-303` | Append-only Evidence store designs | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 247 | `survey-seed-304` | Soft deletion vs hard deletion studies | seed_placeholder | 4 (graph/conflict) | conflict_compose | yes |
| 248 | `2404.16130` | GraphRAG | FULL | 4 (graph/conflict) | anchors_graph | no |
| 249 | `2405.14831` | HippoRAG | FULL | 4 (graph/conflict) | anchors_graph | no |
| 250 | `2407.04363` | AriGraph | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 251 | `2408.00103` | ReLiK (EL + RE) | FULL | 4 (graph/conflict) | anchors_graph | no |
| 252 | `2410.05779` | LightRAG | FULL | 4 (graph/conflict) | anchors_graph | no |
| 253 | `2501.13956` | Zep / Graphiti | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 254 | `2502.14802` | HippoRAG 2 | FULL | 4 (graph/conflict) | anchors_graph | no |
| 255 | `2503.21322` | HyperGraphRAG | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 256 | `2504.19413` | Mem0 / Mem0g | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 257 | `2506.07398` | G-Memory | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 258 | `2601.03236` | MAGMA | FULL | 4 (graph/conflict) | episode_cognify,anchors_graph,conflict_compose | no |
| 259 | `2602.05665` | Graph-based Agent Memory survey | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 260 | `2603.11768` | SSGM | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 261 | `2605.15701` | H-Mem (hybrid tree+graph) | FULL | 4 (graph/conflict) | anchors_graph,conflict_compose | no |
| 262 | `2606.06240` | TOKI | FULL | 4 (graph/conflict) | conflict_compose | no |
| 263 | `2607.05844` | StateFuse | FULL | 4 (graph/conflict) | conflict_compose | no |
| 264 | `2505.23643` | Fides — Securing AI Agents with IFC | queued | 5 (privacy/capability) | privacy_seal | yes |
| 265 | `2512.04668` | Topology Matters (MAMA) | queued | 5 (privacy/capability) | privacy_seal | yes |
| 266 | `survey-seed-001` | CaMeL — capability-based information flow control for LLMs | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 267 | `survey-seed-200` | Prompt logging redaction standards | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 268 | `survey-seed-201` | PII detection libraries for capture redaction | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 269 | `survey-seed-202` | Presidio / common redaction engines | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 270 | `survey-seed-203` | DLP patterns for agent transcripts | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 271 | `survey-seed-204` | Secret scanning (trufflehog/gitleaks) at capture | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 272 | `survey-seed-205` | OWASP LLM Top 10 — sensitive info disclosure | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 273 | `survey-seed-206` | OWASP Agentic AI security draft | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 274 | `survey-seed-207` | NIST AI RMF memory/governance mapping | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 275 | `survey-seed-208` | Contextual integrity (Nissenbaum) primers | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 276 | `survey-seed-209` | GDPR right-to-erasure vs invalidate+audit | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 277 | `survey-seed-210` | CCPA deletion vs belief history retention | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 278 | `survey-seed-211` | Differential privacy for shared memory aggregates | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 279 | `survey-seed-212` | Secure enclaves for sealed packs (SGX/SEV notes) | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 280 | `survey-seed-213` | TPM / hardware key custody for .kpack | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 281 | `survey-seed-214` | age / ssh-age recipient patterns beyond C2SP | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 282 | `survey-seed-215` | TUF / update frameworks for pack distribution | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 283 | `survey-seed-216` | Sigstore / keyless signing for shareable anchors | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 284 | `survey-seed-217` | Paseto / Branca token capability notes | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 285 | `survey-seed-218` | Biscuit vs Macaroon attenuation cookbook | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 286 | `survey-seed-219` | UCANs — user-controlled authorization networks | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 287 | `survey-seed-220` | Object capabilities (Miller) deep primer | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 288 | `survey-seed-221` | Spritely Goblins / OcapPub deeper docs | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 289 | `survey-seed-222` | Cap'n Proto RPC capability patterns | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 290 | `survey-seed-223` | E language capability lessons for agents | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 291 | `survey-seed-224` | Macaroons caveats engineering cookbook | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 292 | `survey-seed-225` | Google Zanzibar authorization for shared graphs | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 293 | `survey-seed-226` | OPA / Cedar policy engines for compose gates | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 294 | `survey-seed-227` | SpiceDB relationship tuples vs Anchor ACL | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 295 | `survey-seed-228` | ReBAC surveys for shareable anchors | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 296 | `survey-seed-229` | ABAC vs capability trade studies | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 297 | `survey-seed-230` | Confused deputy problem classics | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 298 | `survey-seed-231` | Ambient authority anti-patterns in agent tools | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 299 | `survey-seed-232` | Prompt injection → memory poisoning papers | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 300 | `survey-seed-233` | Indirect prompt injection memory persistence | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 301 | `survey-seed-234` | RAG poisoning / corpus poisoning papers | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 302 | `survey-seed-235` | Agent malware / tool exfil case studies | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 303 | `survey-seed-236` | MemGuard / memory firewall product notes | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 304 | `survey-seed-237` | Air-gapped memory partitions engineering | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 305 | `survey-seed-238` | Cross-tenant vector index isolation failures | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 306 | `survey-seed-239` | Embedding inversion / recovery attacks | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 307 | `survey-seed-240` | Membership inference on memory stores | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 308 | `survey-seed-241` | Model stealing via memory APIs | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 309 | `survey-seed-242` | Canary / watermark insertion for memory provenance | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 310 | `survey-seed-290` | Software provenance / SBOM analogies | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 311 | `survey-seed-291` | SLSA build provenance for pack integrity | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 312 | `survey-seed-292` | in-toto supply chain attestation | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 313 | `survey-seed-301` | Tamper-evident logs (Trillian) analogies | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 314 | `survey-seed-302` | Certificate Transparency lessons for Anchor audit | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 315 | `survey-seed-305` | GDPR Article 17 technical implementations | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 316 | `survey-seed-306` | Right to be forgotten in ML surveys | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 317 | `survey-seed-307` | Machine unlearning surveys → Anchor invalidate | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 318 | `survey-seed-308` | SISA unlearning → partition memory stores | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 319 | `survey-seed-309` | Exact unlearning vs approximate for graphs | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 320 | `survey-seed-310` | Graph unlearning papers | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 321 | `survey-seed-311` | Federated learning memory silos | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 322 | `survey-seed-312` | Split learning / vertical privacy | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 323 | `survey-seed-313` | Secure multi-party compute for shared stats | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 324 | `survey-seed-314` | Homomorphic encryption feasibility for packs | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 325 | `survey-seed-315` | Searchable encryption for private hydrate | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 326 | `survey-seed-316` | PIR private information retrieval for memory | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 327 | `survey-seed-317` | ORAM for access-pattern hiding (supporting) | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 328 | `survey-seed-318` | TEE-based RAG papers | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 329 | `survey-seed-319` | Confidential computing for LLM inference | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 330 | `survey-seed-320` | Private retrieval / anonymized shared memory | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 331 | `survey-seed-321` | k-anonymity / l-diversity for shared digests | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 332 | `survey-seed-322` | Synthetic data for shareable episode digests | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 333 | `survey-seed-323` | Differential privacy for community summaries | seed_placeholder | 5 (privacy/capability) | privacy_seal | yes |
| 334 | `2303.17760` | CAMEL | FULL | 5 (privacy/capability) | conflict_compose | no |
| 335 | `2505.18279` | Collaborative Memory | FULL | 5 (privacy/capability) | anchors_graph,conflict_compose | no |
| 336 | `2602.11510` | AgentLeak | FULL | 5 (privacy/capability) | conflict_compose | yes |
| 337 | `2605.10614` | PRISM | FULL | 5 (privacy/capability) | privacy_seal | no |
| 338 | `2606.24535` | MemClaw / Governed Shared Memory | FULL | 5 (privacy/capability) | anchors_graph,conflict_compose | no |
| 339 | `2606.29788` | MemLeak | FULL | 5 (privacy/capability) | conflict_compose | yes |
| 340 | `acl26` | MAMA topology leakage | FULL | 5 (privacy/capability) | privacy_seal | yes |
| 341 | `biscuits-design-spec` | Biscuits DESIGN+spec | FULL | 5 (privacy/capability) | privacy_seal | no |
| 342 | `c2sp-age-md` | C2SP age.md | FULL | 5 (privacy/capability) | privacy_seal | no |
| 343 | `capability-myths-demolished` | Capability Myths Demolished | FULL | 5 (privacy/capability) | privacy_seal | no |
| 344 | `libsodium-seal-box-sign` | libsodium seal/box/sign | FULL | 5 (privacy/capability) | privacy_seal | no |
| 345 | `macaroons-ndss-2014` | Macaroons NDSS 2014 | FULL | 5 (privacy/capability) | privacy_seal | no |
| 346 | `mls-rfc-9420-9750` | MLS RFC 9420 / 9750 | FULL | 5 (privacy/capability) | privacy_seal | no |
| 347 | `spritely-ocappub` | Spritely / OcapPub | FULL | 5 (privacy/capability) | privacy_seal | no |
| 348 | `vault-eknow-2025` | VAULT (eKNOW 2025) | FULL | 5 (privacy/capability) | privacy_seal | no |
| 349 | `2005.11485` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 350 | `2101.06804` | What Makes Good In-Context Examples (KATE) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 351 | `2305.06983` | FLARE (Active RAG) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 352 | `2309.04697` | Leakage-Abuse Attacks on SSE | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 353 | `2310.04408` | RECOMP | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 354 | `2310.05736` | LLMLingua | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 355 | `2310.06201` | Compressing Context (Selective Context) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 356 | `2312.03414` | Compressed Context Memory | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 357 | `2312.10997` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 358 | `2402.03367` | RAG-Fusion | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 359 | `2402.13753` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 360 | `2503.21760` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 361 | `2507.07957` | MIRIX — body cached; prior FULL in BATCH_SYSTEMS | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 362 | `2508.06433` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 363 | `2508.09736` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 364 | `2510.06719` | DP Synthetic Text for RAG | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 365 | `2511.03506` | HaluMem | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 366 | `2601.03785` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 367 | `2604.22085` | (title TBD — queued for FULL deep-read) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 368 | `2605.27825` | MRMMIA (membership inference on memory) | queued | 6 (eng-judgment) | hydrate_retrieve | no |
| 369 | `survey-seed-012` | MemU — product memory system (survey-named) | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 370 | `survey-seed-013` | Memobase — product memory system (survey-named) | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 371 | `survey-seed-016` | DNC — Differentiable Neural Computer | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 372 | `survey-seed-018` | Retroformer — parametric memory adaptation | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 373 | `survey-seed-019` | Early Experience — parametric/experiential adaptation | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 374 | `survey-seed-020` | MemoryLLM — latent parametric memory | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 375 | `survey-seed-021` | M+ memory model — latent/parametric lineage | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 376 | `survey-seed-022` | MemGen — generative parametric memory | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 377 | `survey-seed-032` | Haystack memory / agent memory docs | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 378 | `survey-seed-033` | CrewAI memory docs | seed_placeholder | 6 (eng-judgment) | anchors_graph | no |
| 379 | `survey-seed-034` | AutoGPT memory backend docs | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 380 | `survey-seed-035` | BabyAGI / task memory lineage | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 381 | `survey-seed-038` | ThinkGPT — thinking + memory patterns | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 382 | `survey-seed-040` | ClinicalAgent / MedAgents memory slices | seed_placeholder | 6 (eng-judgment) | privacy_seal | no |
| 383 | `survey-seed-051` | OpenAgents memory modules | seed_placeholder | 6 (eng-judgment) | anchors_graph | no |
| 384 | `survey-seed-058` | MMAC / multi-modal agent memory survey tails | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 385 | `survey-seed-064` | Plan-and-Solve / plan memory | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 386 | `survey-seed-066` | PEARL planning memory | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 387 | `survey-seed-069` | SQL-of-Thought / NL2SQL memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 388 | `survey-seed-129` | Human episodic memory models → agent mapping papers | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 389 | `survey-seed-130` | Complementary learning systems (CLS) → L2/L3 mapping | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 390 | `survey-seed-131` | Hopfield / modern Hopfield retrieval memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 391 | `survey-seed-132` | KAN / kernel memory analogies (supporting) | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 392 | `survey-seed-133` | Vector DB product memory patterns (Chroma/Weaviate/Qdrant) | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 393 | `survey-seed-134` | pgvector / sqlite-vss engineering memory notes | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 394 | `survey-seed-149` | Adaptive retrieval controllers beyond Adaptive-RAG | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 395 | `survey-seed-150` | FLARE active retrieval | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 396 | `survey-seed-151` | IRCoT interleaving retrieval | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 397 | `survey-seed-152` | DSP / Demonstrate-Search-Predict | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 398 | `survey-seed-153` | REPLUG retrieval-enhanced LMs | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 399 | `survey-seed-154` | Atlas few-shot retrieval memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 400 | `survey-seed-155` | REALM pretraining retrieval memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 401 | `survey-seed-156` | kNN-LM datastore memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 402 | `survey-seed-157` | SPALM / sparse memory LMs | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 403 | `survey-seed-158` | Product Quantization memory indexes | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 404 | `survey-seed-159` | HNSW engineering notes for hydrate latency | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 405 | `survey-seed-160` | BM25 + dense hybrid retrieval recipes | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 406 | `survey-seed-161` | ColBERT late interaction retrieval | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 407 | `survey-seed-162` | BGE / E5 embedding model cards for memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 408 | `survey-seed-163` | Instruction-aware embeddings for agent memory | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 409 | `survey-seed-189` | OpenAI Swarm / Agents SDK memory patterns | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 410 | `survey-seed-190` | Semantic Kernel memory store | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 411 | `survey-seed-191` | Haystack Agent memory components | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 412 | `survey-seed-192` | DSPy memory / state modules | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 413 | `survey-seed-193` | Guidance / Outlines constrained decode + memory | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 414 | `survey-seed-194` | PydanticAI deps/memory patterns | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 415 | `survey-seed-246` | Model cards for memory controllers | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 416 | `survey-seed-253` | Inter-annotator agreement for eng-judgment gold | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 417 | `survey-seed-254` | Pairwise preference protocols for compose quality | seed_placeholder | 6 (eng-judgment) | conflict_compose | no |
| 418 | `survey-seed-255` | Bradley-Terry ranking for memory ablations | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 419 | `survey-seed-256` | Cost/latency accounting for memory maintenance | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 420 | `survey-seed-257` | Token economics of reflection loops | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 421 | `survey-seed-259` | DreamBooth-style consolidation analogies (supporting) | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 422 | `survey-seed-260` | Continual learning surveys → agent memory | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 423 | `survey-seed-261` | Catastrophic forgetting in parametric memory | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 424 | `survey-seed-262` | Elastic Weight Consolidation analogies | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 425 | `survey-seed-263` | Progress & compress continual learning | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 426 | `survey-seed-264` | PackNet / progressive nets analogies | seed_placeholder | 6 (eng-judgment) | capture_working | no |
| 427 | `survey-seed-268` | Model-based RL world models as memory | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 428 | `survey-seed-269` | Dreamer / RSSM latent memory | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 429 | `survey-seed-270` | Decision Transformer trajectory memory | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 430 | `survey-seed-271` | Trajectory transformer memory | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 431 | `survey-seed-274` | Rete / production systems as procedural memory | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 432 | `survey-seed-275` | SOAR / ACT-R cognitive architectures mapping | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 433 | `survey-seed-276` | Global Workspace Theory → hydrate broadcast | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 434 | `survey-seed-278` | Free energy principle primers (supporting only) | seed_placeholder | 6 (eng-judgment) | episode_cognify | no |
| 435 | `survey-seed-281` | Personal knowledge management (PKM) systems | seed_placeholder | 6 (eng-judgment) | anchors_graph | no |
| 436 | `survey-seed-283` | Org-roam / emacs memory workflows | seed_placeholder | 6 (eng-judgment) | anchors_graph | no |
| 437 | `survey-seed-284` | Dendron hierarchical notes | seed_placeholder | 6 (eng-judgment) | anchors_graph | no |
| 438 | `survey-seed-285` | Tana / supertags as schema memory | seed_placeholder | 6 (eng-judgment) | anchors_graph | no |
| 439 | `survey-seed-286` | ADR / Architecture Decision Records practice | seed_placeholder | 6 (eng-judgment) | conflict_compose | no |
| 440 | `survey-seed-287` | QOC — Questions Options Criteria rationale | seed_placeholder | 6 (eng-judgment) | conflict_compose | no |
| 441 | `survey-seed-288` | IBIS issue-based information systems | seed_placeholder | 6 (eng-judgment) | conflict_compose | no |
| 442 | `survey-seed-289` | Design rationale capture systems | seed_placeholder | 6 (eng-judgment) | conflict_compose | no |
| 443 | `survey-seed-293` | Reproducible builds for memory fixtures | seed_placeholder | 6 (eng-judgment) | hydrate_retrieve | no |
| 444 | `1410.3916` | Memory Networks | FULL | 6 (eng-judgment) | capture_working | no |
| 445 | `1805.04263` | Memory-net / memorizing-transformer lineage | FULL | 6 (eng-judgment) | anchors_graph | no |
| 446 | `2004.04906` | Memory-net / memorizing-transformer lineage | FULL | 6 (eng-judgment) | anchors_graph | no |
| 447 | `2005.11401` | RAG (Lewis et al.) | FULL | 6 (eng-judgment) | capture_working | no |
| 448 | `2109.10862` | Recursive Summarizing Books | FULL | 6 (eng-judgment) | episode_cognify | no |
| 449 | `2112.04426` | RETRO | FULL | 6 (eng-judgment) | episode_cognify | no |
| 450 | `2203.08913` | Memorizing Transformers | FULL | 6 (eng-judgment) | capture_working | no |
| 451 | `2205.12674` | Memory-net / memorizing-transformer lineage | FULL | 6 (eng-judgment) | anchors_graph | no |
| 452 | `2207.06881` | Recurrent Memory Transformer | FULL | 6 (eng-judgment) | capture_working | no |
| 453 | `2210.03629` | ReAct | FULL | 6 (eng-judgment) | capture_working | no |
| 454 | `2302.04761` | Toolformer | FULL | 6 (eng-judgment) | capture_working | no |
| 455 | `2303.11366` | Reflexion | FULL | 6 (eng-judgment) | capture_working | no |
| 456 | `2304.03442` | Generative Agents | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 457 | `2307.07924` | ChatDev | FULL | 6 (eng-judgment) | conflict_compose | no |
| 458 | `2308.00352` | MetaGPT | FULL | 6 (eng-judgment) | conflict_compose | no |
| 459 | `2308.08155` | AutoGen | FULL | 6 (eng-judgment) | conflict_compose | no |
| 460 | `2308.08239` | MemoChat | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 461 | `2308.15022` | Recursive Summarization (dialogue memory) | FULL | 6 (eng-judgment) | capture_working,episode_cognify | no |
| 462 | `2309.07864` | Rise and Potential of LLM Agents (survey; §memory) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 463 | `2401.18059` | RAPTOR | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 464 | `2402.11163` | KG-Agent | FULL | 6 (eng-judgment) | anchors_graph | no |
| 465 | `2403.14403` | Adaptive-RAG | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 466 | `2404.13501` | Zhang memory mechanisms survey | FULL | 6 (eng-judgment) | capture_working | no |
| 467 | `2407.09450` | EM-LLM | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph | no |
| 468 | `2410.15665` | Long Term Memory: Foundation of AI Self-Evolution | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 469 | `2411.00489` | AI Long-term Memory survey | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 470 | `2501.06322` | Multi-Agent Collaboration Mechanisms survey | FULL | 6 (eng-judgment) | conflict_compose | no |
| 471 | `2501.12948` | Additional fetched fulltexts used as supporting | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 472 | `2502.12110` | A-MEM | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 473 | `2503.18813` | Additional fetched fulltexts used as supporting | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 474 | `2504.15965` | From Human Memory to AI Memory survey | FULL | 6 (eng-judgment) | anchors_graph | no |
| 475 | `2504.18070` | PropRAG | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 476 | `2505.00675` | Additional fetched fulltexts used as supporting | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 477 | `2505.19549` | Multi-granularity conversational memory (MemGAS) | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph | no |
| 478 | `2506.15841` | MEM1 (constant-size IS memory) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 479 | `2507.02259` | MemAgent | FULL | 6 (eng-judgment) | episode_cognify | no |
| 480 | `2507.03724` | MemOS | FULL | 6 (eng-judgment) | capture_working,episode_cognify | no |
| 481 | `2507.06229` | Agent KB (cross-framework experience) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 482 | `2508.04903` | RCR-Router | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 483 | `2508.16153` | Memento (case-based M-MDP memory) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 484 | `2508.19828` | Memory-R1 | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 485 | `2509.25140` | ReasoningBank + MaTTS | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 486 | `2509.25911` | Mem-α | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 487 | `2510.04851` | LEGOMem (modular procedural multi-agent) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 488 | `2510.10397` | AssoMem | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 489 | `2510.12635` | Memory as Action / MemAct | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 490 | `2510.18866` | LightMem | FULL | 6 (eng-judgment) | episode_cognify,anchors_graph,conflict_compose | no |
| 491 | `2511.06449` | FLEX | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 492 | `2511.13593` | O-Mem (omni persona/episodic/working) | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 493 | `2512.13564` | Memory in the Age of AI Agents (survey) | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 494 | `2512.22716` | Memento 2 | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 495 | `2601.05960` | Memory-as-a-Tool | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 496 | `2602.06052` | Agent Memory Second Half survey | FULL | 6 (eng-judgment) | hydrate_retrieve | no |
| 497 | `2602.19320` | Anatomy of Agentic Memory (survey) | FULL | 6 (eng-judgment) | conflict_compose | no |
| 498 | `2603.07670` | Memory for Autonomous LLM Agents (survey) | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 499 | `2603.15994` | Selective Memory / supersession chains | FULL | 6 (eng-judgment) | anchors_graph,conflict_compose | no |
| 500 | `2605.06716` | From Storage to Experience (survey) | FULL | 6 (eng-judgment) | anchors_graph | no |

## Machine-readable

- `docs/research/queue/full_queue.jsonl` — one JSON object per line.
- Rebuild: `python3 scripts/research/build_full_queue.py`
- Fetch arXiv HTML: `python3 scripts/research/fetch_paper.py <id>`

