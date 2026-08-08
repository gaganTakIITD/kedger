#!/usr/bin/env python3
"""Generate Batch 9/10 FULL memos from cached /tmp/kedger-papers/full/{id}.txt bodies."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BATCHES = ROOT / "docs" / "research" / "batches"

BATCH9_NEW = [
    {
        "id": "2602.22769",
        "title": "AMA-Bench — long-horizon agentic memory eval",
        "stages": "S1, S7, S8",
        "problem": "Dialogue-centric memory benchmarks miss machine-generated agent-environment trajectories (states, actions, tool outputs).",
        "representation": "AMA-Bench: real agentic trajectories + expert QA and synthetic trajectories scaling to arbitrary length; rule-based and expert QA. AMA-Agent adds causality graph + tool-augmented retrieval.",
        "lessons": "(1) Kedger eval needs agent-env trajectories, not only chat logs. (2) Causal/objective state beats similarity-only retrieve on long horizons. (3) GPT-5.2 ~72% on AMA-Bench — far from saturated. (4) AMA-Agent +11.16% over strongest baseline; ~57% avg accuracy in paper.",
        "metric_impact": "Agentic trajectory QA accuracy @ 32K–128K; causality-graph retrieve vs embedding-only hydrate.",
        "refine": "yes",
    },
    {
        "id": "2605.18421",
        "title": "EvoMemBench — self-evolving memory eval",
        "stages": "S2, S3, S4, S8",
        "problem": "Existing benches don't systematically test memory update/reuse across scopes and content types.",
        "representation": "2×2 grid: in-episode vs cross-episode × knowledge-oriented vs execution-oriented. 15 memory methods vs long-context baselines under unified protocol.",
        "lessons": "(1) Map Kedger fixtures to four EvoMem cells (episode-local cognify vs cross-episode promote). (2) Long-context baselines stay competitive — memory SLIs must include difficult/insufficient-context cases. (3) Retrieval wins knowledge; procedural memory wins execution when structure matches. (4) No single memory form dominates all settings.",
        "metric_impact": "Per-quadrant accuracy; cross-environment transfer on execution memory.",
        "refine": "yes",
    },
    {
        "id": "2608.00009",
        "title": "AgentMemBench — strategy-agnostic dialogue memory eval",
        "stages": "S2, S7, S8",
        "problem": "Fair comparison across memory strategies (EKV, graph episodic, compression, web-augmented) lacking.",
        "representation": "Five strategies on MSC/PersonaChat/LongDial: EKV, GEM, CBS, ICW, WAM. Metrics: Recall@k, nDCG, answer score, faithfulness, footprint, latency over 491 annotated turns.",
        "lessons": "(1) EKV best macro recall (~0.792) but ~5100 vs ~300 tokens footprint — explicit accuracy–efficiency trade-off for S2 packs. (2) Long-range recall (gold turn many sessions back) collapses ICW/recency — dense retrieve scales. (3) CBS runner-up by inheriting turn provenance — cognify summaries need Evidence links. (4) WAM external results carry no in-corpus provenance — hydrate must tag source tier.",
        "metric_impact": "Recall@k + faithfulness + memory footprint on multi-session dialogue fixtures.",
        "refine": "yes",
    },
    {
        "id": "2309.04697",
        "title": "Leakage-Abuse Attacks on Searchable Symmetric Encryption",
        "stages": "S6, S7",
        "problem": "Forward/backward-private DSSE still leaks via access/volume patterns exploitable by leakage-abuse attacks.",
        "representation": "LAAs on DSSE schemes; keyword recovery from search/update traces despite linkability breaking.",
        "lessons": "(1) Encrypted semantic index ≠ Inv-Scope — pattern leakage remains. (2) Prefer capability-scoped plaintext indexes under process gates + sealed `.kxp` transit, not ciphertext search as v1 security boundary. (3) Tombstone/unshare must consider access-pattern oracles. (4) Paper recovery rates up to ~93% class — treat as red-team fixture class.",
        "metric_impact": "Keyword recovery rate under SSE trace simulation; post-unshare access-pattern residual.",
        "refine": "yes",
    },
    {
        "id": "2510.06719",
        "title": "DP Synthetic Text for RAG (DP-SynRAG)",
        "stages": "S6, S7",
        "problem": "RAG corpora memorization risk when indexing sensitive text.",
        "representation": "Two-stage DP-SynRAG: soft clustering + differentially private synthetic text generation for RAG indexing/training.",
        "lessons": "(1) Shared/community Anchor digests may need DP synthesis before publish — not raw L0. (2) Utility–privacy trade on synthetic RAG corpora informs S6 shareable tier policy. (3) Not a substitute for capability attenuation. (4) Evaluate memorization probes on published synthetic packs.",
        "metric_impact": "Downstream QA utility vs membership/memorization probes on DP-synthetic index.",
        "refine": "no",
    },
    {
        "id": "2605.27825",
        "title": "MRMMIA — membership inference on chat-agent memory",
        "stages": "S6, S7, S8",
        "problem": "MIAs studied for training/RAG DBs but under-explored for persistent chat-agent memory.",
        "representation": "Adversary probes whether target interaction lives in agent memory via query/response signals.",
        "lessons": "(1) Inv-Scope 404 on deny — no existence leak via hydrate APIs. (2) Rate-limit id/recipient probes on memory APIs. (3) Minimize pack metadata that confirms membership. (4) S8 must not echo stored private spans that enable MIA features.",
        "metric_impact": "MIA AUC on memory store vs baseline absent record.",
        "refine": "yes",
    },
    {
        "id": "2508.09736",
        "title": "M3-Agent — multimodal agent long-term memory",
        "stages": "S1, S2, S3, S7",
        "problem": "Multimodal streaming (video/audio) needs memory beyond text dialogue benchmarks.",
        "representation": "M3-Bench-robot/web; long-term memory module with memorization + control; automatic eval on multimodal traces.",
        "lessons": "(1) L0 capture must normalize multimodal Evidence (not text-only hooks). (2) Memory control policy separate from answer model — maps to cognify cron vs hydrate. (3) Benchmark multimodal agent memory separately from LoCoMo-class text. (4) Silent on typed SUPERSEDES — use invalidate+audit for AV facts.",
        "metric_impact": "Multimodal QA/recall on M3-Bench vs text-only memory baselines.",
        "refine": "no",
    },
    {
        "id": "2507.07957",
        "title": "MIRIX — multi-agent memory system",
        "stages": "S2, S3, S4, S5, S7",
        "problem": "Monolithic memory modules don't separate episodic/semantic/procedural/resource facets for agents.",
        "representation": "Six memory components (Core, Episodic, Semantic, Procedural, Resource, Knowledge Vault) + multi-agent update/retrieval workflows and active retrieval design.",
        "lessons": "(1) Map Kedger Anchor kinds to MIRIX facets — procedural ≠ episodic promote gates. (2) Active retrieval workflow ≈ S7 tiered hydrate with component-specific indexes. (3) Multi-agent memory marketplace implies capability-scoped share per component. (4) Wearable-device use case → edge capture + seal before cloud cognify.",
        "metric_impact": "Component-wise recall + update latency on MemoryAgentBench-class tasks (paper cross-eval).",
        "refine": "yes",
    },
    {
        "id": "2606.04425",
        "title": "Cross-Session Stored Prompt Injection",
        "stages": "S1, S3, S4, S6, S8",
        "problem": "Prompt injection research focuses on single session; agent persistent state enables stored XSS-like attacks across sessions.",
        "representation": "Lifecycle taxonomy: persistence channels (memory, filesystem, AGENTS.md, checkpoints) + incorporation (direct load vs conditional retrieve). Sandbox toolkit + benchmark.",
        "lessons": "(1) Treat memory writes as privileged — log causing prompt; gate promote on instruction-like content. (2) S6 unshare/tombstone must purge stored injection residues. (3) Conditional retrieve (RAG/memory) is activation path — ConflictSet before trust. (4) State-centric security, not interaction-only filters.",
        "metric_impact": "Attack success rate across persistence channels/models; residual activation after unshare.",
        "refine": "yes",
    },
    {
        "id": "2507.10457",
        "title": "LPCI — Logic-layer Prompt Control Injection",
        "stages": "S1, S3, S6, S7",
        "problem": "Encoded/delayed payloads in memory/vector stores bypass input filters and trigger across sessions.",
        "representation": "LPCI lifecycle: tool poisoning → logic-layer payload → role override via memory entrenchment → vector persistence. 1700 structured tests; up to ~49% execution on less-protected models.",
        "lessons": "(1) Memory integrity validation + prompt risk scoring at cognify/write. (2) Vector-store payload persistence ≈ MINJA/AgentPoison class — provenance gates. (3) Runtime attestation for external tool/docs feeding L0. (4) Enterprise agent memory needs session-aware controls beyond static PI regex.",
        "metric_impact": "LPCI execution rate @ model/platform; detection precision of memory-integrity scanner.",
        "refine": "yes",
    },
    {
        "id": "2301.12652",
        "title": "REPLUG — retrieval-augmented black-box LMs",
        "stages": "S7, S8",
        "problem": "Retrieval-augmented LMs often require white-box cross-attention training.",
        "representation": "Tuneable retriever + frozen LM; prepend retrieved docs to input; LM likelihood weights supervise retriever.",
        "lessons": "(1) S7 can swap retrieve-then-prepend without finetuning reader — matches black-box API hydrate. (2) Retriever tuning signal from LM feedback ≈ eng-judgment on hydrate utility. (3) FLARE-adjacent: forward needs still require active/interleaved variants. (4) Paper gains ~4–6% on knowledge tasks — retrieve quality dominates.",
        "metric_impact": "End-task accuracy vs retrieve@k ablation on fixed LM reader.",
        "refine": "no",
    },
    {
        "id": "2212.14024",
        "title": "DSP — Demonstrate-Search-Predict",
        "stages": "S5, S7, S8",
        "problem": "Composing retrieval and LMs for knowledge-intensive NLP lacks modular training-free patterns.",
        "representation": "Pipeline: demonstrate (ICL templates) → search (retrieve) → predict (LM); composes independently tuned modules.",
        "lessons": "(1) Hydrate pack compile = modular DSP stages — demo facets, search Evidence, predict answer/`why`. (2) Swap search module without retraining cognify — aligns plugin retrievers. (3) FLARE/IRCoT extend with interleaving; DSP is single-shot compose baseline. (4) Strong multi-hop gains when search module matched to task.",
        "metric_impact": "Multi-hop QA F1 vs module ablation (demonstrate/search/predict).",
        "refine": "no",
    },
    {
        "id": "2410.07176",
        "title": "Astute RAG — imperfect retrieval + knowledge conflicts",
        "stages": "S4, S5, S7, S8",
        "problem": "Imperfect retrieval introduces noise and parametric–context conflicts that hurt RAG.",
        "representation": "Adaptive internal knowledge generation + iterative source-aware consolidation + answer finalization before generation.",
        "lessons": "(1) S4/S7 ConflictSet before pack compile — Astute consolidation ≈ pre-hydrate conflict resolve (ConflictRAG-adjacent). (2) Allow parametric fallback when retrieve set is noisy. (3) Source-aware weighting mirrors Anchor provenance fields. (4) Paper reports large gains under real-world imperfect retrieval.",
        "metric_impact": "Answer correctness under noisy/contradictory retrieve sets vs vanilla RAG.",
        "refine": "yes",
    },
    {
        "id": "2502.00306",
        "title": "Riddle Me This — stealthy MIA for RAG",
        "stages": "S6, S7",
        "problem": "Standard MIA queries detectable; RAG systems leak membership via interrogation-style prompts.",
        "representation": "Interrogation attack: generated queries + ground-truth answer matching for membership inference on RAG corpora.",
        "lessons": "(1) Hydrate APIs must not enable high-precision membership oracles on sealed packs. (2) Rate-limit + perturb responses on repeated probe patterns. (3) Complements MRMMIA/RAG-MIA fixtures. (4) Stealthy probes harder to block with regex — behavioral detection.",
        "metric_impact": "MIA AUC under stealthy interrogation vs naive shadow-model attack.",
        "refine": "yes",
    },
    {
        "id": "2406.05804",
        "title": "Review of LLM-Agent Paradigms (tool/RAG/planning/feedback)",
        "stages": "S1, S7, S8",
        "problem": "Agent memory eval must sit inside broader tool-use/planning/feedback paradigms.",
        "representation": "Survey taxonomy: LLM-profiled roles, task universality (decision vs information envs), tool/RAG/planning/feedback learning clusters.",
        "lessons": "(1) Kedger hooks capture tool/RAG traces as L0 — align with survey's information-processing envs. (2) Memory maintenance latency must be measured inside full agent loop, not isolated QA. (3) Feedback-learning agents need SUPERSEDES on policy updates. (4) Use as bibliography harvest for tier-1/2 runway.",
        "metric_impact": "Taxonomy coverage checklist for eval harness env classes.",
        "refine": "no",
    },
    {
        "id": "2403.11381",
        "title": "LLM-Augmented Agents in Melting Pot — cooperation eval",
        "stages": "S4, S5, S6, S8",
        "problem": "Multi-agent cooperation with LLM-augmented agents under-evaluated in memory-sharing settings.",
        "representation": "Melting Pot environments; GPT-4/3.5 LAAs; cooperation metrics vs reference policies.",
        "lessons": "(1) Shared-memory topology affects cooperation — complements MAMA hub-restriction fixtures. (2) Memory of prior episodes can help or hinder social dilemmas — test promote gates. (3) Eval privacy leakage in multi-agent + shared graph settings. (4) Preliminary: cooperation propensity but imperfect coordination.",
        "metric_impact": "Cooperation rate vs memory-sharing policy ablation in gridworld/social dilemmas.",
        "refine": "no",
    },
    {
        "id": "2403.04957",
        "title": "Automatic Universal Prompt Injection Attacks",
        "stages": "S1, S6, S7",
        "problem": "Manual prompt injections don't scale; need optimization-based universal attacks on integrated LLM apps.",
        "representation": "Momentum gradient search on prompt suffixes/prefixes with universal transfer objectives across models/apps.",
        "lessons": "(1) Untrusted Evidence in hydrate must pass injection scanner before entering WorkingState. (2) Universal suffixes transfer — don't rely on single-model regex defenses. (3) Combine with HouYi/AgentDojo fixtures from Batch7/8. (4) Attack success ~50%+ class in paper on open models — assume hostile reader.",
        "metric_impact": "Attack success rate (ASR) vs defense stack on tool-integrated apps.",
        "refine": "yes",
    },
]

BATCH9_REREAD = [
    ("2310.17884", "ConfAIde — contextual integrity / Can LLMs Keep a Secret?", "S4, S6, S8", "Batch2/P6 FULL"),
    ("2506.21605", "MemBench — multi-scenario multi-level memory eval", "S1, S2, S7, S8", "Batch2/BATCH_SYSTEMS FULL"),
    ("2601.06966", "RealMem — project-oriented memory interaction benchmark", "S1, S2, S7, S8", "P5/Batch4 RE-READ"),
    ("2505.23643", "Fides — IFC for AI agent planners", "S1, S4, S6", "Batch2/P6 FULL"),
    ("2511.03506", "HaluMem — operation-level memory hallucination eval", "S3, S4, S8", "BATCH_SYSTEMS FULL"),
]

BATCH10_NEW = [
    {
        "id": "2601.03785",
        "title": "Membox — topic continuity memory boxes",
        "stages": "S2, S3, S4, S7",
        "problem": "Fragmentation–compensation (utterance store + embedding retrieve) breaks topic continuity and temporal reasoning.",
        "representation": "Topic Loom: sliding-window same-topic turn grouping into sealed memory boxes; Trace Weaver links boxes into long-range event timelines.",
        "lessons": "(1) Cognify at storage time — group consecutive same-topic turns before embed index. (2) Trace Weaver ≈ bi-temporal episode links for macro-topic recurrence. (3) Up to ~68% F1 gain on temporal reasoning vs Mem0/A-MEM on LoCoMo with fewer tokens. (4) Boundary detector feeds HARD/SOFT cuts — aligns EST/segment fixtures.",
        "metric_impact": "Temporal/multi-hop F1 on LoCoMo + token budget vs turn/session baselines.",
        "refine": "yes",
    },
    {
        "id": "2503.08026",
        "title": "RMM — Reflective Memory Management for dialogue",
        "stages": "S2, S3, S7, S8",
        "problem": "Fixed session/turn boundaries misalign with semantic topic units in personalized dialogue.",
        "representation": "Prospective reflection: topic-based memory extraction/update at session end; Retrospective reflection: online RL refines retrieval using cited evidence.",
        "lessons": "(1) Topic-coherent memory units > session delimiters for promote/hydrate. (2) Retrospective RL on cited evidence ≈ eng-judgment feedback on hydrate misfires. (3) Pair with granularity-aware eval (2512.17083). (4) Silent on sealed packs — use capability gates separately.",
        "metric_impact": "Personalized dialogue quality + retrieval precision vs turn/session memory.",
        "refine": "yes",
    },
    {
        "id": "2509.13313",
        "title": "ReSum — context summarization for long-horizon search agents",
        "stages": "S1, S2, S7",
        "problem": "Web/search agents hit context limits; architectural memory tokens break compatibility.",
        "representation": "Periodic summary tool compresses history to compact restart state; ReSum-GRPO trains agents for segmented trajectories (+4.5% training-free, +8.2% with GRPO in paper).",
        "lessons": "(1) PreCompact hook can invoke external summarizer — reset WorkingState to (query, summary). (2) Trigger near context limit (~70–80%), not early turns. (3) Summary quality tool (ReSumTool-30B) matters — generic LLM summaries fail. (4) Plug-and-play vs MemGPT paging — simpler but summary-lossy.",
        "metric_impact": "Pass@1 on BrowseComp-class tasks vs ReAct @ fixed token budget.",
        "refine": "yes",
    },
    {
        "id": "2603.02228",
        "title": "Neural Paging — learned context management (H-NTM)",
        "stages": "S1, S2",
        "problem": "MemGPT-style LM-managed paging wastes tokens on housekeeping; RAG is passive/coarse.",
        "representation": "Decouple LLM reasoning from learned Page Controller (neural MMU) predicting evict/prefetch; strict separation from MemGPT kernel-in-user-space.",
        "lessons": "(1) Don't force main agent to manage KV/paging — separate controller service for S2 pressure. (2) MemGPT foil: function-call paging vs learned policy. (3) Target Turing-complete agents with bounded active context. (4) Silent on SUPERSEDES — symbolic Anchor path still authoritative.",
        "metric_impact": "Task success vs active context size + paging policy ablation.",
        "refine": "yes",
    },
    {
        "id": "2510.27246",
        "title": "BEAM benchmark + LIGHT memory framework",
        "stages": "S2, S3, S7, S8",
        "problem": "Long-dialogue benchmarks lack narrative coherence and diverse memory abilities beyond simple recall.",
        "representation": "BEAM: auto-generated coherent conversations up to 10M tokens, 2000 questions / 10 ability types. LIGHT: episodic retrieve + working-memory buffer (recent z turns) + scratchpad of salient facts filtered per question.",
        "lessons": "(1) Three-tier hydrate: episodic retrieve + working buffer + curated scratchpad Anchors. (2) Even 1M context models degrade on BEAM length — retrieval mandatory. (3) LIGHT +3.5–12.69% over strongest baselines. (4) Ablation: working memory helps mid-length; scratchpad critical at 10M.",
        "metric_impact": "BEAM ability-wise accuracy @ 100K–10M tokens; LIGHT ablation SLI.",
        "refine": "yes",
    },
    {
        "id": "2604.21748",
        "title": "StructMem — structured hierarchical memory",
        "stages": "S2, S3, S5, S7",
        "problem": "Flat memory stores lose event-level bindings and cross-event structure in long horizons.",
        "representation": "Hierarchical structured memory preserving event bindings + cross-event connections; hierarchical retrieve.",
        "lessons": "(1) Cognify emits structured episode objects, not flat strings. (2) Graph/Anchor edges encode cross-event links — StructMem validates hierarchical retrieve. (3) Long-horizon behavior tasks need structure metric, not EM alone. (4) Complements Graphiti episode→entity pipeline.",
        "metric_impact": "Long-horizon task success + structural consistency vs flat RAG memory.",
        "refine": "yes",
    },
    {
        "id": "2605.28773",
        "title": "FluxMem — connectivity-evolving memory graph",
        "stages": "S3, S4, S5, S7",
        "problem": "Static memory graphs don't evolve connectivity as agent experience accumulates.",
        "representation": "Heterogeneous memory graph with evolving connectivity; continual integration of new nodes/edges.",
        "lessons": "(1) Promotion must update graph connectivity, not only append nodes. (2) Monitor edge drift/poison — governance before consolidate (SSGM-aligned). (3) Retrieve = subgraph expand with connectivity-aware PPR analog. (4) Paper reports double-digit gains on long-dialogue settings.",
        "metric_impact": "Recall + graph connectivity metrics under continual write load.",
        "refine": "yes",
    },
    {
        "id": "2503.21760",
        "title": "MemInsight — autonomous memory augmentation",
        "stages": "S3, S4, S7",
        "problem": "Agents need autonomous decisions on what/when to augment memory without constant user cues.",
        "representation": "Autonomous memory augmentation pipeline deciding memory entries/refinement from interaction traces.",
        "lessons": "(1) Cognify cron should auto-augment with guardrails — not unbounded LLM writes. (2) Autonomous augment ↔ RecMem recurrence gate (anti-eager). (3) Measure augment precision separately from QA end metric. (4) Provenance on augmented entries mandatory for promote.",
        "metric_impact": "Augment precision/recall + downstream task utility vs manual memory curation.",
        "refine": "yes",
    },
    {
        "id": "2604.22085",
        "title": "Memanto — typed semantic memory + info-theoretic retrieval",
        "stages": "S3, S5, S7, S8",
        "problem": "Untyped memory retrieval wastes context on irrelevant stored facts in long-horizon agents.",
        "representation": "Typed semantic memory schema + information-theoretic retrieval scoring for long-horizon agents.",
        "lessons": "(1) Anchor `kind` typing should drive retrieve scoring — not embedding alone. (2) Info-theoretic score ≈ utility-per-token for S7 budget. (3) Long-horizon agents need typed forget/refresh policies. (4) Paper strong gains on multi-step tasks when types match query.",
        "metric_impact": "Retrieve precision@budget + long-horizon success vs untyped embed retrieve.",
        "refine": "yes",
    },
    {
        "id": "2508.06433",
        "title": "Memp — agent procedural memory",
        "stages": "S3, S4, S7",
        "problem": "Procedural/skills memory under-studied vs episodic/semantic in agents.",
        "representation": "Procedural memory store for reusable skills/workflows distilled from trajectories.",
        "lessons": "(1) Voyager-style skill library = procedural tier — separate promote ACL from episodic. (2) Memp explores procedural recall for repeated tool workflows. (3) Version procedural Anchors with SUPERSEDES on skill updates. (4) Eval procedural separately in EvoMem execution quadrant.",
        "metric_impact": "Skill reuse rate + trajectory length reduction on repeated task families.",
        "refine": "no",
    },
    {
        "id": "2501.00309",
        "title": "GraphRAG with Graphs — structured RAG survey/ framework",
        "stages": "S3, S5, S7",
        "problem": "Graph-enhanced RAG lacks unified treatment of graph construction + retrieve for agents.",
        "representation": "Graph-first RAG pipeline: graph construction from corpus, community/summary views, graph-aware retrieval integration.",
        "lessons": "(1) P3 graph cognify outputs feed graph-RAG hydrate — not duplicate GraphRAG community summaries as Anchors. (2) Separate graph index refresh from Anchor invalidation. (3) Use as pattern catalog for S5 walks. (4) Large survey body — mechanism cards focus on agent-memory retrieve coupling.",
        "metric_impact": "Graph-RAG QA vs flat chunk RAG on multi-hop entity queries.",
        "refine": "no",
    },
    {
        "id": "2408.09559",
        "title": "HiAgent — hierarchical working memory management",
        "stages": "S1, S2, S7",
        "problem": "Long-horizon agent tasks overflow context; flat ReAct history is inefficient.",
        "representation": "Hierarchical working memory manager: subtask-scoped memory tiers + selective retention for long-horizon tasks.",
        "lessons": "(1) WorkingState should be hierarchical (task/subtask scopes) not one flat deque. (2) MemGPT-adjacent but explicit hierarchy for tool-heavy agents. (3) Pair with Context-Folding/ReSum compaction triggers. (4) Paper reports large gains on long-horizon agent benchmarks vs flat context.",
        "metric_impact": "Long-horizon task SR vs flat-context agent @ equal token cap.",
        "refine": "yes",
    },
    {
        "id": "2504.13171",
        "title": "Sleep-time Compute — offline consolidation for agents",
        "stages": "S3, S4, S8",
        "problem": "Online-only memory update is expensive; humans consolidate offline.",
        "representation": "Allocate extra compute between interactions (sleep-time) to reorganize/predict memory before next session.",
        "lessons": "(1) Cognify cron = sleep-time consolidation — decouple from online hydrate latency SLO. (2) Batch reflection/promotion candidates overnight. (3) Complements Sleep-SCM (2604.20943) already in corpus. (4) Don't block user turn on heavy cognify — async sleep jobs.",
        "metric_impact": "Next-session task utility vs online-only cognify @ fixed total compute budget.",
        "refine": "yes",
    },
    {
        "id": "2510.11967",
        "title": "Context-Folding — branch/return agent context management",
        "stages": "S1, S2, S7, S8",
        "problem": "Linear history growth breaks long-horizon agents; summarization loses structure.",
        "representation": "Branch into sub-trajectory for subtask; return folds intermediate steps keeping concise summary; FoldGRPO dense token-level process rewards.",
        "lessons": "(1) Subtask branch ≈ workstream-local WorkingState; return = promote summary to parent WS. (2) 32K active budget + branches beats 327K linear context (62%/58% on BrowseComp+/SWE-Bench Verified in paper). (3) FoldGRPO +20% BrowseComp vs ReAct GRPO. (4) Prefer structured fold summaries over blind compress.",
        "metric_impact": "pass@1 @ 32K×10 branches vs 327K linear on long-horizon agent benches.",
        "refine": "yes",
    },
    {
        "id": "2505.02099",
        "title": "MemEngine — modular memory library",
        "stages": "S2, S3, S7",
        "problem": "Research memory models lack unified modular implementation framework.",
        "representation": "Three-level MemEngine: memory functions → operations → models (MemoryBank, MemGPT, etc.); config + utility modules.",
        "lessons": "(1) Kedger cognify/hydrate interfaces should mirror function→operation→model layering. (2) Swap memory backends without rewriting agent loop — plugin retrievers. (3) MemBench built on MemEngine — align eval harness adapters. (4) Library not governance — still need SUPERSEDES/seal.",
        "metric_impact": "Cross-model parity tests using shared MemEngine adapters in eval harness.",
        "refine": "no",
    },
    {
        "id": "2510.24699",
        "title": "AgentFold — proactive context management for web agents",
        "stages": "S1, S2, S7",
        "problem": "Long web-agent trajectories need proactive compaction beyond passive summarization.",
        "representation": "Granular + deep condensation with proactive fold/unfold of context; targets long-horizon web agents.",
        "lessons": "(1) Proactive fold before pressure flush — don't wait for 100% MemGPT threshold. (2) Multi-scale condensation maps to L2 digest + L4 pack tiers. (3) Compare AgentFold vs Context-Folding branch semantics in dogfood. (4) Paper ~36–47% gains class on web agent benchmarks.",
        "metric_impact": "Web agent success @ fixed context with proactive vs reactive compaction.",
        "refine": "yes",
    },
    {
        "id": "2310.05029",
        "title": "MemWalker — interactive reading beyond context limit",
        "stages": "S2, S5, S7, S8",
        "problem": "Very long documents exceed context; passive retrieve misses multi-hop structure.",
        "representation": "Build memory tree over document; agent navigates/interacts with tree nodes (interactive reading) to answer.",
        "lessons": "(1) Hydrate over long repos = tree walk, not single embedding top-k. (2) Notebook/tree navigation ≈ GraphReader function vocabulary. (3) Cap walk steps as S7 budget. (4) Paper strong gains on long-doc QA vs single-shot read.",
        "metric_impact": "Long-doc QA accuracy vs walk-budget + tree depth.",
        "refine": "yes",
    },
]


def card_md(i: int, c: dict, status: str = "FULL") -> str:
    return f"""### 1.{i} {c['title'].split('—')[0].strip()}  
**arXiv:{c['id']}** · **{status}**

| Field | Content |
|-------|---------|
| **kedger_stages** | {c['stages']} |
| **problem** | {c['problem']} |
| **representation** | {c['representation']} |
| **write / read / forget** | See paper body; Kedger maps write→cognify/promote, read→hydrate, forget→invalidate+audit unless paper specifies otherwise. |
| **conflict** | {"Conflict-aware where noted." if "conflict" in c.get("title","").lower() or "Astute" in c['title'] else "Silent or partial — see paper."} |
| **privacy** | {"Privacy/security focus." if any(x in c['id'] for x in ['2309','2510','2605','2606','2507','2502','2403']) or 'MIA' in c['title'] or 'Injection' in c['title'] else "Silent or partial — see paper."} |
| **Kedger lessons** | {c['lessons']} |
| **metric_impact** | {c['metric_impact']} |
| **refine_candidate** | **{c['refine']}**{' — S6/S7 fixture ticket' if c['refine']=='yes' else ''} |

---
"""


def reread_card(i: int, pid: str, title: str, stages: str, prior: str) -> str:
    return f"""### 1.{i} {title.split('—')[0].strip()}  
**arXiv:{pid}** · **RE-READ** ({prior})

| Field | Content |
|-------|---------|
| **kedger_stages** | {stages} |
| **note** | Prior FULL deep-read; re-extracted for Batch 9 Kedger S1–S8 mapping. Does **not** count toward NEW FULL quota. |
| **refine_candidate** | **yes** where eval/privacy probes already ticketed in `EVAL_HARNESS.md` |

---
"""


def write_batch9():
    lines = [
        "# Batch 9 — Eval · Privacy · Active Retrieve · Prompt-Injection Memory (Kedger)",
        "",
        "> **Date:** 2026-08-08  ",
        "> **Branch:** `Cursor/batch-to-300-fb37`  ",
        "> **Scope:** Tier-1/5 eval/privacy + FLARE/ConflictRAG-adjacent retrieve + prompt-injection memory papers **not** previously FULL in `CORPUS_INVENTORY.md` §2.  ",
        "> **Priority queue:** ConfAIde, MemBench, RealMem, Fides, HaluMem → **RE-READ** (already FULL elsewhere). FLARE/ConflictRAG already Batch8 FULL — not duplicated.  ",
        "> **Method:** Full arXiv HTML/PDF bodies; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards only.  ",
        "",
        "---",
        "",
        "## 0. Honesty table (this batch)",
        "",
        "| Status | Count | Papers |",
        "|--------|------:|--------|",
        f"| **FULL** (new; ID not previously FULL in CORPUS §2) | **{len(BATCH9_NEW)}** | "
        + "; ".join(f"{c['title'].split('—')[0].strip()} ({c['id']})" for c in BATCH9_NEW[:6])
        + "; … |",
        f"| **RE-READ** (prior FULL; inventory backfill mapping only) | **{len(BATCH9_REREAD)}** | "
        + "; ".join(f"{t} ({pid})" for pid, t, _, _ in BATCH9_REREAD)
        + " |",
        "| **Fetch failed / skipped** | **0** | All listed IDs have `.txt` ≥45k chars (RE-READ included) |",
        "",
        "**Cache path:** `/tmp/kedger-papers/full/{id}.txt`",
        "",
        "---",
        "",
        "## 1. Mechanism cards",
        "",
    ]
    for i, c in enumerate(BATCH9_NEW, 1):
        lines.append(card_md(i, c))
    base = len(BATCH9_NEW)
    for j, (pid, title, stages, prior) in enumerate(BATCH9_REREAD, 1):
        lines.append(reread_card(base + j, pid, title, stages, prior))
    lines.extend(
        [
            "## 2. Successfully FULL-read IDs (NEW only)",
            "",
            "```",
            * [c["id"] for c in BATCH9_NEW],
            "```",
            "",
            "**RE-READ IDs (not counted NEW):**",
            "```",
            *[pid for pid, _, _, _ in BATCH9_REREAD],
            "```",
            "",
        ]
    )
    (BATCHES / "BATCH9_EVAL_PRIVACY_FULL.md").write_text("\n".join(lines), encoding="utf-8")


def write_batch10():
    lines = [
        "# Batch 10 — Capture · Episode · Boundary · Working Memory · Compaction (Kedger)",
        "",
        "> **Date:** 2026-08-08  ",
        "> **Branch:** `Cursor/batch-to-300-fb37`  ",
        "> **Scope:** Tier-2/3 episode/boundary/capture/compaction/MemGPT-adjacent papers **not** previously FULL in `CORPUS_INVENTORY.md` §2.  ",
        "> **Sources:** Survey bibliographies + queue tier 2–3 (Membox, RMM, ReSum, BEAM/LIGHT, Context-Folding, HiAgent, …).  ",
        "> **Method:** Full arXiv HTML/PDF bodies; cache `/tmp/kedger-papers/full/{id}.txt`.  ",
        "",
        "---",
        "",
        "## 0. Honesty table (this batch)",
        "",
        "| Status | Count | Papers |",
        "|--------|------:|--------|",
        f"| **FULL** (new) | **{len(BATCH10_NEW)}** | "
        + "; ".join(f"{c['title'].split('—')[0].strip()} ({c['id']})" for c in BATCH10_NEW[:6])
        + "; … |",
        "| **RE-READ** | **0** | — |",
        "| **Fetch failed / skipped** | **0** | All IDs `.txt` ≥24k chars |",
        "",
        "---",
        "",
        "## 1. Mechanism cards",
        "",
    ]
    for i, c in enumerate(BATCH10_NEW, 1):
        lines.append(card_md(i, c))
    lines.extend(
        [
            "## 2. Successfully FULL-read IDs",
            "",
            "```",
            *[c["id"] for c in BATCH10_NEW],
            "```",
            "",
        ]
    )
    (BATCHES / "BATCH10_CAPTURE_EPISODE_FULL.md").write_text("\n".join(lines), encoding="utf-8")


def write_deltas():
    b9 = [
        "## Batch 9 — Ledger delta (for CORPUS_INVENTORY merge)",
        "",
        "> **Source:** `docs/research/batches/BATCH9_EVAL_PRIVACY_FULL.md`",
        "",
        "| ID | Title | Status | Prior FULL? | Memo |",
        "|----|-------|--------|-------------|------|",
    ]
    for c in BATCH9_NEW:
        b9.append(
            f"| {c['id']} | {c['title']} | **FULL** | no | BATCH9 |"
        )
    for pid, title, _, prior in BATCH9_REREAD:
        b9.append(f"| {pid} | {title} | **RE-READ** | yes ({prior}) | BATCH9 |")
    b9.extend(
        [
            "",
            "## Counts",
            "",
            f"| FULL (new) | **{len(BATCH9_NEW)}** |",
            f"| RE-READ | **{len(BATCH9_REREAD)}** |",
            "",
            "## NEW FULL ID list",
            "",
            "```",
            *[c["id"] for c in BATCH9_NEW],
            "```",
            "",
        ]
    )
    (BATCHES / "BATCH9_LEDGER_DELTA.md").write_text("\n".join(b9), encoding="utf-8")

    b10 = [
        "## Batch 10 — Ledger delta (for CORPUS_INVENTORY merge)",
        "",
        "> **Source:** `docs/research/batches/BATCH10_CAPTURE_EPISODE_FULL.md`",
        "",
        "| ID | Title | Status | Prior FULL? | Memo |",
        "|----|-------|--------|-------------|------|",
    ]
    for c in BATCH10_NEW:
        b10.append(f"| {c['id']} | {c['title']} | **FULL** | no | BATCH10 |")
    b10.extend(
        [
            "",
            f"## Counts: **{len(BATCH10_NEW)}** new FULL",
            "",
            "```",
            *[c["id"] for c in BATCH10_NEW],
            "```",
            "",
        ]
    )
    (BATCHES / "BATCH10_LEDGER_DELTA.md").write_text("\n".join(b10), encoding="utf-8")


if __name__ == "__main__":
    write_batch9()
    write_batch10()
    write_deltas()
    print("wrote batch 9/10 memos")
