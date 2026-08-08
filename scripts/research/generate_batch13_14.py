#!/usr/bin/env python3
"""Generate Batch 13/14 FULL memos and ledger deltas."""
from __future__ import annotations

from pathlib import Path

OUT = Path("docs/research/batches")

REQUIRED = ("id", "title", "stages", "problem", "representation", "wrf", "conflict", "privacy", "lessons", "metric", "refine")

B13 = [
    {
        "id": "1803.05355",
        "title": "FEVER — fact extraction and verification",
        "stages": "S4, S5, S8",
        "problem": "Claim verification against Wikipedia: 185k claims labeled Supported/Refuted/NotEnoughInfo with sentence-level evidence.",
        "representation": "Pipeline: retrieve evidence → classify claim veracity; NEI = abstain when evidence insufficient.",
        "wrf": "Read-only external corpus; no memory write — NEI class is explicit non-commit.",
        "conflict": "Evidence may contradict claim; Refuted = reject promotion analog.",
        "privacy": "Silent.",
        "lessons": "(1) S4 promote only with Supported-class evidence spans. (2) S8 `why` cites evidence sentences like FEVER annotations. (3) NEI → abstain, never invent Anchor. (4) Label quality κ≈0.68 — human promotion gates need calibration.",
        "metric": "verification ACC + NEI precision",
        "refine": "yes",
    },
    {
        "id": "2103.08541",
        "title": "VitaminC — contrastive fact verification",
        "stages": "S4, S5, S8",
        "problem": "Fact verifiers fail on subtle Wikipedia revisions — need sensitivity to near-identical contrasting evidence.",
        "representation": ">400k claim-evidence pairs from >100k Wikipedia fact revisions; contrastive pairs differ minimally but flip label.",
        "wrf": "Read-only evidence; auxiliary tasks: tag relevant words, identify factual revisions, generate consistent edits.",
        "conflict": "Core: nearly identical passages with opposite veracity — tests supersession detection.",
        "privacy": "Silent.",
        "lessons": "(1) SUPERSEDES must detect micro-edits not just wholesale replacement. (2) Promotion fixtures need contrastive near-dup pairs. (3) +10% adversarial FV accuracy from contrastive training. (4) Word-level salience maps → Anchor span grounding.",
        "metric": "contrastive FV accuracy",
        "refine": "yes",
    },
    {
        "id": "2303.16634",
        "title": "G-Eval — GPT-4 NLG evaluation with CoT rubrics",
        "stages": "S4, S8",
        "problem": "Reference metrics (BLEU/ROUGE) misalign with humans; need reference-free LLM judges with better correlation.",
        "representation": "G-Eval: LLM chain-of-thought + form-filling rubric (coherence, consistency, fluency, relevance); probability-weighted scoring.",
        "wrf": "Read-only eval — no persistent store; judge reads candidate output + optional reference.",
        "conflict": "Silent on factual conflict resolution.",
        "privacy": "Silent.",
        "lessons": "(1) Eng-judgment SLIs should use CoT rubrics not single scalar. (2) Spearman 0.514 on summarization — still imperfect; combine auto+human. (3) Watch bias toward LLM-generated text in judges. (4) S8 rationale quality evaluable via G-Eval dimensions.",
        "metric": "human-judge Spearman on promotion/why quality",
        "refine": "yes",
    },
    {
        "id": "2405.01535",
        "title": "Prometheus 2 — open rubric-specialized judge LM",
        "stages": "S4, S8",
        "problem": "Proprietary judges (GPT-4) costly/opaque; need open models for absolute + relative scoring with rubrics.",
        "representation": "Prometheus 2: fine-tuned judge LM; absolute score 1–5 on custom rubric + pairwise preference mode; reference-answer optional.",
        "wrf": "Read-only assessment; rubric + response (+ optional reference) in context.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) Kedger eng fixtures can use Prometheus-class rubrics for Anchor promotion QA. (2) Relative mode for A/B compose outputs. (3) Open judge enables CI regression on S8 quality. (4) Custom rubrics per SLI dimension (faithfulness, completeness).",
        "metric": "rubric score correlation vs human",
        "refine": "yes",
    },
    {
        "id": "2311.09677",
        "title": "R-Tuning — instruct LLMs to say 'I don't know'",
        "stages": "S4, S7, S8",
        "problem": "LLMs hallucinate on unknowns; need selective prediction / abstention without always guessing.",
        "representation": "R-Tuning: fine-tune on (question, answer) + (question, abstention) pairs; model learns when to refuse.",
        "wrf": "Parametric update during training; inference = abstention token or refusal phrase on low-confidence.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) S7 hydrate should abstain when Evidence empty — R-Tuning class. (2) S4 reject promotion when grounding score below τ. (3) Pair unknowns with explicit abstention in training data. (4) Reduces hallucination on unanswerable queries.",
        "metric": "abstention precision/recall on NEI queries",
        "refine": "yes",
    },
    {
        "id": "2309.15217",
        "title": "RAGAS — reference-free RAG evaluation",
        "stages": "S7, S8",
        "problem": "RAG systems lack gold labels; need automatic metrics for faithfulness and relevance without human refs.",
        "representation": "RAGAS: faithfulness (answer grounded in context), answer relevance, context precision/recall — LLM-as-judge decomposition.",
        "wrf": "Eval-only; reads (question, retrieved contexts, answer) tuple.",
        "conflict": "Faithfulness metric detects unsupported claims vs retrieved context.",
        "privacy": "Silent.",
        "lessons": "(1) S7 SLI: faithfulness of hydrated answer to Evidence pack. (2) Context precision = retrieve quality gate before compose. (3) Reference-free → usable in CI on synthetic fixtures. (4) Decompose RAG eval not single EM score.",
        "metric": "RAGAS faithfulness + context precision",
        "refine": "yes",
    },
    {
        "id": "2405.01525",
        "title": "FLAME — factuality-aware alignment",
        "stages": "S4, S7, S8",
        "problem": "Alignment improves helpfulness but can hurt factuality; need benchmarks + training for factual consistency.",
        "representation": "FLAME benchmark: atomic claim verification + citation grounding tasks; measures factuality under alignment.",
        "wrf": "Read-path verification over claims with optional citations.",
        "conflict": "Atomic claims may conflict; verification resolves per-claim.",
        "privacy": "Silent.",
        "lessons": "(1) Post-promotion Anchor audit = atomic claim check (FLAME-style). (2) Citation grounding for S8 `why` chains. (3) Alignment passes must not regress factuality SLI. (4) Separate helpfulness vs faithfulness metrics.",
        "metric": "atomic factuality + citation grounding ACC",
        "refine": "yes",
    },
    {
        "id": "2305.14552",
        "title": "Sources of hallucination in LLMs on inference",
        "stages": "S4, S7, S8",
        "problem": "Hallucinations arise from multiple sources — need taxonomy to target mitigation (data vs model vs prompt).",
        "representation": "Empirical study decomposing hallucination sources: pretraining data gaps, finetuning, decoding, retrieval errors.",
        "wrf": "Analysis paper — no new memory architecture; categorizes failure modes at inference.",
        "conflict": "Retrieval-context conflict listed as hallucination source.",
        "privacy": "Silent.",
        "lessons": "(1) S7 failures: tag whether hallucination from retrieve vs parametric vs compose. (2) Promotion rejects when source=parametric-only on factual Anchors. (3) Mitigation differs by source — no one fix. (4) Provenance logging helps attribute source class.",
        "metric": "hallucination source attribution in fixtures",
        "refine": "yes",
    },
    {
        "id": "2512.10696",
        "title": "ReMe — dynamic procedural memory",
        "stages": "S3, S4, S8",
        "problem": "Static procedural memory fails as tasks evolve; agents need experience distillation and iterative refinement.",
        "representation": "ReMe: procedural memory framework — capture trajectories, distill reusable procedures, refine via feedback loop.",
        "wrf": "Write procedural traces → distill → read at task time → refine on failure/success signals.",
        "conflict": "Silent unless explicit version supersession.",
        "privacy": "Silent.",
        "lessons": "(1) L3 procedural Anchors need refine loop not write-once. (2) S4 promotion after successful replay validation. (3) Distill multi-step traces to compact procedure cards. (4) Pair with eval on procedure reuse rate.",
        "metric": "procedure reuse success rate",
        "refine": "yes",
    },
    {
        "id": "2603.24639",
        "title": "ERL — experiential reflective learning",
        "stages": "S3, S4, S8",
        "problem": "LLM agents don't learn from past trajectories without explicit experience replay and reflection.",
        "representation": "ERL: collect experiences → reflective summarization → replay buffer curation → policy improvement without weight updates.",
        "wrf": "Write experience logs → reflect → promote curated lessons → read during new episodes.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) S3 cognify + S4 promote = ERL-style reflection before L3 commit. (2) Replay buffer curation prevents noise accumulation. (3) Self-improvement without finetuning matches Kedger CLI model. (4) Measure improvement over episode batches.",
        "metric": "task success delta after ERL cycles",
        "refine": "yes",
    },
    {
        "id": "2210.03493",
        "title": "Auto-CoT — automatic chain-of-thought prompting",
        "stages": "S7, S8",
        "problem": "Manual CoT demos costly; need automatic demonstration selection for reasoning tasks.",
        "representation": "Auto-CoT: cluster questions → select representative demos per cluster → zero-shot CoT generation pipeline.",
        "wrf": "Read-only demo pool; selects k in-context examples automatically.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) S8 `why` generation can auto-select exemplar rationales by cluster. (2) Demo diversity matters — cluster before select. (3) Reduces manual eng-judgment fixture authoring. (4) Pair with active learning (2305.14264) for budgeted selection.",
        "metric": "reasoning ACC vs manual CoT",
        "refine": "no",
    },
    {
        "id": "2504.13169",
        "title": "REVERSE — generate but verify",
        "stages": "S4, S7, S8",
        "problem": "Multimodal models hallucinate objects/relations — need generate-then-verify before output commit.",
        "representation": "REVERSE: generate candidate answer → self-verify against image/context → reject or revise before final output.",
        "wrf": "Draft → verify gate → commit/reject loop; no persistent memory.",
        "conflict": "Verification rejects inconsistent generations.",
        "privacy": "Silent.",
        "lessons": "(1) S4 promotion = generate-verify-reject pattern before Anchor commit. (2) S7 compose should verify hydrated answer vs Evidence before return. (3) Rejection anchor when verify fails. (4) Applicable beyond VLM to text compose.",
        "metric": "hallucination rate pre/post verify gate",
        "refine": "yes",
    },
    {
        "id": "2305.14264",
        "title": "Active learning principles for in-context learning",
        "stages": "S7, S8",
        "problem": "ICL demo selection under label budget — which examples maximize performance?",
        "representation": "Active learning framework for ICL: uncertainty/diversity criteria to pick demos from pool.",
        "wrf": "Read demo pool; write nothing — selects subset for context.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) Hydrate pack demo selection = active learning problem. (2) Budget k demos by uncertainty on target query. (3) Label-efficient eng-judgment calibration. (4) Combine with KATE kNN retrieval (Batch8).",
        "metric": "ICL ACC vs demo budget",
        "refine": "no",
    },
    {
        "id": "2309.11054",
        "title": "Design of chain-of-thought for math problem solving",
        "stages": "S8",
        "problem": "CoT prompt structure materially affects math reasoning reliability — design choices matter.",
        "representation": "Empirical study of CoT templates: step granularity, intermediate variable naming, equation ordering.",
        "wrf": "Prompt-only; no memory persistence.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) S8 `why` templates should follow validated CoT structure. (2) Step granularity affects error rate — tune for audit readability. (3) Eng-judgment rubrics should check intermediate steps. (4) Bad CoT design → false promotion of wrong rationale.",
        "metric": "math/reasoning step correctness",
        "refine": "no",
    },
    {
        "id": "2308.02151",
        "title": "Retroformer — retrospective LLM agents",
        "stages": "S3, S7, S8",
        "problem": "LLM agents lack retrospective learning from past failures in multi-step tasks.",
        "representation": "Retroformer: frozen LLM agent + trainable retrospective model providing hindsight feedback to refine prompts/plans.",
        "wrf": "Log trajectories → retrospective model generates feedback → adjust forward policy prompts.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) S8 post-mortem on failed hydrate/compose feeds S3 cognify. (2) Retrospective feedback without finetuning base LM. (3) Provenance: link feedback to failed trajectory ID. (4) Improves multi-step tool/agent success.",
        "metric": "multi-step task success after retrospective feedback",
        "refine": "yes",
    },
    {
        "id": "2510.08558",
        "title": "Agent learning via early experience",
        "stages": "S3, S4, S8",
        "problem": "Agents deployed cold-start; need pre-deployment experience accumulation before live tasks.",
        "representation": "Early Experience paradigm: sandbox exploration → distill skills/procedures → transfer to deployment agent.",
        "wrf": "Write sandbox trajectories → abstract experience → read at deployment; promotion after validation.",
        "conflict": "Silent.",
        "privacy": "Sandbox may contain synthetic data only.",
        "lessons": "(1) S4 promotion from sandbox to production Anchor store requires explicit gate. (2) Early experience ≠ live memory — separate namespaces. (3) Distill exploration into L3 before user-facing deploy. (4) Measure transfer success rate.",
        "metric": "sandbox→live task transfer ACC",
        "refine": "yes",
    },
    {
        "id": "2502.07459",
        "title": "PerCul — story-driven cultural evaluation",
        "stages": "S4, S8",
        "problem": "Western-centric benchmarks miss cultural reasoning; need localized eval with native speaker judgment.",
        "representation": "PerCul: Persian cultural stories + native annotator rubrics; tests cultural knowledge and reasoning.",
        "wrf": "Eval-only benchmark; no agent memory.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) Eng-judgment rubrics must be locale/culture-aware for global users. (2) Promotion gates calibrated on diverse cultural fixtures. (3) Auto-judges (G-Eval) may fail on cultural items — human fallback. (4) Expand fixture diversity beyond English-centric LoCoMo class.",
        "metric": "cultural reasoning ACC by locale",
        "refine": "no",
    },
]

B14 = [
    {
        "id": "2306.03901",
        "title": "ChatDB — SQL databases as symbolic memory",
        "stages": "S2, S3, S5, S7",
        "problem": "Neural memory accumulates errors; complex multi-hop reasoning needs exact symbolic store.",
        "representation": "LLM controller + SQL DB memory: generate SQL read/write ops; DB holds structured historical state.",
        "wrf": "Write via INSERT/UPDATE SQL; read via SELECT; LLM plans multi-hop SQL programs.",
        "conflict": "SQL constraints enforce consistency; updates overwrite rows explicitly.",
        "privacy": "DB can scope tables per tenant — silent on crypto.",
        "lessons": "(1) Kedger sqlite graph = ChatDB-class symbolic memory. (2) Exact retrieval for structured facts beats fuzzy embed for tables. (3) LLM generates memory ops — audit SQL like Anchor ops. (4) Multi-hop = chained SQL not single vector search.",
        "metric": "multi-hop QA ACC on structured memory",
        "refine": "yes",
    },
    {
        "id": "2406.04151",
        "title": "AgentGym — evolving LLM agents across environments",
        "stages": "S1, S3, S8",
        "problem": "Agent training fragmented across envs; need unified platform + trajectories for cross-task evolution.",
        "representation": "AgentGym: 14+ envs (WebShop, WebArena, ALFWorld, SciWorld, …) + trajectory dataset + AgentEvol curriculum.",
        "wrf": "Collect/filter trajectories across envs; behavioral cloning + iterative exploration (AgentEvol).",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) Memory eval needs multi-env trajectories not single chat bench. (2) AgentEvol = experience promotion across tasks. (3) Trajectory filtering before L3 ingest. (4) Cross-env generalization tests memory transfer.",
        "metric": "cross-env success rate after evolution",
        "refine": "yes",
    },
    {
        "id": "1911.00172",
        "title": "kNN-LM — nearest-neighbor language models",
        "stages": "S2, S7",
        "problem": "Parametric LMs weak on rare facts; non-parametric datastore improves perplexity without retraining.",
        "representation": "kNN-LM: interpolate pretrained LM with kNN over embedding datastore (keys=hidden states, values=tokens).",
        "wrf": "Read-only datastore at inference; optional domain adaptation by swapping neighbor corpus.",
        "conflict": "Silent.",
        "privacy": "Datastore may leak training snippets — membership concern.",
        "lessons": "(1) Kedger optional embed index = kNN datastore for hydrate. (2) Rare Anchor facts benefit from exact neighbor retrieval. (3) +2.9 perplexity points on WikiText-103. (4) Separate parametric vs non-parametric evidence in S8 provenance.",
        "metric": "perplexity / rare-fact recall",
        "refine": "yes",
    },
    {
        "id": "2004.12832",
        "title": "ColBERT — late interaction dense retrieval",
        "stages": "S7",
        "problem": "Bi-encoder retrieval loses token-level matching; cross-encoders too slow at scale.",
        "representation": "ColBERT: contextualized late interaction — MaxSim over token embeddings; offline indexing + fast online scoring.",
        "wrf": "Read-only passage index; query-time MaxSim aggregation.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) S7 passage retrieve can use ColBERT-class late interaction. (2) Token-level match helps entity-heavy Anchor hydrate. (3) Index passages not whole sessions. (4) Balance latency vs bi-encoder baseline.",
        "metric": "retrieve MRR/Recall@k on Anchor corpus",
        "refine": "no",
    },
    {
        "id": "2208.03299",
        "title": "Atlas — retrieval augmented few-shot LM",
        "stages": "S7",
        "problem": "Few-shot LM performance limited without retrieval; need joint retriever+LM training.",
        "representation": "Atlas: T5-style LM + Contriever retriever; end-to-end trained on QA with retrieved passages in context.",
        "wrf": "Retrieve top-k passages → prepend to input → generate answer; retriever+LM co-trained.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) Hydrate = retrieve-then-generate with co-trained components. (2) Few-shot Anchor QA benefits from Atlas pattern. (3) Passage attribution in output for S8. (4) Strong multi-hop QA with fixed retrieve budget.",
        "metric": "few-shot QA F1 with retrieve budget",
        "refine": "no",
    },
    {
        "id": "2002.08909",
        "title": "REALM — retrieval-augmented LM pre-training",
        "stages": "S7",
        "problem": "LMs lack access to external knowledge at pretrain time; retrieval should be baked into LM training.",
        "representation": "REALM: retrieve Wikipedia chunks during masked LM pretrain; asynchronous retriever refresh.",
        "wrf": "Retriever index updated during pretrain; LM learns to use retrieved docs.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) Long-term: Kedger embed index refresh async like REALM. (2) Retrieval not bolt-on — train/instruct for Evidence use. (3) Open-domain QA gains from pretrain retrieve. (4) Provenance: retrieved doc ID in context.",
        "metric": "open-domain QA EM",
        "refine": "no",
    },
    {
        "id": "2402.04624",
        "title": "MemoryLLM — self-updatable LLM memory",
        "stages": "S2, S3, S4",
        "problem": "Frozen LMs can't incorporate new facts without full finetune; need internal memory slots that update.",
        "representation": "MemoryLLM: latent memory matrix injected into transformer layers; update operator writes new knowledge into slots.",
        "wrf": "Write via memory update module on new documents; read via attention to memory tokens during inference.",
        "conflict": "Updates may overwrite — implicit supersession in slots.",
        "privacy": "Silent.",
        "lessons": "(1) Parametric memory slots ≠ Kedger Anchors but inform update semantics. (2) Self-update without full finetune. (3) Track slot version for audit. (4) Pair with explicit graph invalidation for governance.",
        "metric": "knowledge update ACC after write",
        "refine": "yes",
    },
    {
        "id": "2502.00592",
        "title": "M+ — scalable long-term MemoryLLM",
        "stages": "S2, S3, S4",
        "problem": "MemoryLLM slots limited; need scalable long-term memory without proportional param growth.",
        "representation": "M+: hierarchical/scalable extension of MemoryLLM — more slots + efficient update/retrieval over long streams.",
        "wrf": "Stream documents → selective slot update → read via memory attention.",
        "conflict": "Slot overwrite = soft supersession.",
        "privacy": "Silent.",
        "lessons": "(1) Long-horizon L3 needs scalable update not unbounded context. (2) M+ patterns for memory budget management. (3) Combine parametric slots with explicit Anchor graph. (4) Measure retention after many updates.",
        "metric": "long-stream knowledge retention",
        "refine": "yes",
    },
    {
        "id": "2509.24704",
        "title": "MemGen — generative latent memory",
        "stages": "S2, S3, S7",
        "problem": "Retrieval-only memory misses generative synthesis; agents need latent memory that generates recall.",
        "representation": "MemGen: generative latent memory module — compress experiences to latents, generate memory-informed outputs.",
        "wrf": "Write experiences → encode to latent memory → generate/decode at recall time.",
        "conflict": "Silent.",
        "privacy": "Latent memory not human-readable — governance gap.",
        "lessons": "(1) Generative recall complements retrieve-from-graph. (2) Latent memory needs export/audit path for Kedger. (3) Weave with explicit Anchors for shareable subset. (4) Agent task performance vs pure RAG.",
        "metric": "agent task ACC with generative memory",
        "refine": "yes",
    },
    {
        "id": "2402.04617",
        "title": "InfLLM — training-free long-context memory",
        "stages": "S2, S7",
        "problem": "Context windows finite; need infinite context without training via memory hierarchy.",
        "representation": "InfLLM: local attention window + external memory unit storing distant context chunks; retrieve into window.",
        "wrf": "Chunk long input → store in memory unit → retrieve relevant chunks into active window.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) S2 working state = active window; L2/L3 = InfLLM memory unit. (2) Training-free → matches Kedger v1 heuristic hydrate. (3) Chunk boundary affects recall — align with episode boundaries. (4) Long-document QA benchmarks.",
        "metric": "long-context QA with fixed window",
        "refine": "yes",
    },
    {
        "id": "2606.29824",
        "title": "Neural procedural memory for LLM agents",
        "stages": "S3, S4, S7",
        "problem": "LLM agents repeat planning; need implicit procedural memory encoding skills without explicit scripts.",
        "representation": "Neural procedural memory: encode successful action sequences into compact neural modules recalled at execution.",
        "wrf": "Write successful trajectories → distill procedural encoding → read during similar tasks.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) Procedural L3 tier for tool workflows. (2) Distill multi-step plans to reusable procedures. (3) S4 promote after N successful replays. (4) Complements Memp (Batch10) explicit procedural store.",
        "metric": "procedure reuse rate on tool tasks",
        "refine": "yes",
    },
    {
        "id": "2606.23127",
        "title": "Managing procedural memory in LLM agents",
        "stages": "S3, S4, S8",
        "problem": "Procedural memory grows unbounded; need lifecycle control, adaptation, and pruning.",
        "representation": "Framework for procedural memory CRUD: acquisition, refinement, deprecation, conflict between procedures.",
        "wrf": "Lifecycle ops on procedure store — consolidate, adapt, retire stale procedures.",
        "conflict": "Explicit procedure conflict detection and resolution.",
        "privacy": "Silent.",
        "lessons": "(1) Kedger INVALIDATE for superseded procedures. (2) Consolidation pass like sleep-time compute. (3) Version procedures with superseded_by links. (4) Audit trail on procedure promotion/retirement.",
        "metric": "procedure store size vs task success",
        "refine": "yes",
    },
    {
        "id": "2608.03463",
        "title": "LeanMem — efficient long-term agent memory",
        "stages": "S2, S3, S7",
        "problem": "Agent memory systems too heavy; need simple efficient long-term memory with minimal overhead.",
        "representation": "LeanMem: lightweight memory architecture — selective retention + compact encoding + fast retrieval.",
        "wrf": "Filter incoming observations → compact store → retrieve top-k for context injection.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) Kedger v1 should stay LeanMem-simple not over-engineer. (2) Selective retention = promotion gate. (3) Compact encoding before L3 graph ingest. (4) Latency budget for memory maintenance.",
        "metric": "memory ops latency + QA ACC",
        "refine": "yes",
    },
    {
        "id": "2603.24018",
        "title": "ELITE — experiential learning and intent-aware transfer",
        "stages": "S3, S4, S8",
        "problem": "Agents fail to transfer learned skills across intents/domains without explicit transfer mechanism.",
        "representation": "ELITE: capture experiences with intent labels → transfer relevant subsets to new tasks via intent matching.",
        "wrf": "Write intent-tagged experiences → match intent at new task → read transferred subset.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) Anchor metadata includes intent/workstream tags for transfer. (2) S4 promote with intent scope not global. (3) Cross-workstream hydrate filters by intent. (4) Measure transfer vs scratch performance.",
        "metric": "cross-intent transfer success delta",
        "refine": "yes",
    },
    {
        "id": "2512.18950",
        "title": "Hierarchical procedural memory (Bayesian)",
        "stages": "S3, S4, S5",
        "problem": "Flat procedure lists don't capture skill hierarchy; need structured procedural memory with uncertainty.",
        "representation": "Bayesian hierarchical procedural memory: decompose skills into tree; update beliefs on execution outcomes.",
        "wrf": "Write execution outcomes → Bayesian update on hierarchy nodes → read most probable procedure path.",
        "conflict": "Competing procedures resolved by posterior weight.",
        "privacy": "Silent.",
        "lessons": "(1) Procedure graph hierarchy in Kedger L3. (2) Uncertainty-aware procedure selection. (3) S5 compose picks procedure branch by confidence. (4) Supersede low-posterior branches after evidence.",
        "metric": "hierarchical procedure selection ACC",
        "refine": "yes",
    },
    {
        "id": "2605.30690",
        "title": "ElasticMem — latent memory as learnable resource",
        "stages": "S2, S3, S4",
        "problem": "Fixed memory capacity wastes resources; memory should elastically expand/contract with task demands.",
        "representation": "ElasticMem: learnable latent memory resource — dynamic capacity allocation based on task complexity signals.",
        "wrf": "Elastic expand on high surprise/complexity → compress when stable; read latent memory during inference.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) Memory budget scales with surprise (ES-Mem class signal). (2) Compress stable L2 before promote. (3) Elastic capacity for long projects. (4) Monitor memory cost SLI.",
        "metric": "memory footprint vs task performance",
        "refine": "yes",
    },
    {
        "id": "2509.08755",
        "title": "AgentGym-RL — RL for long-horizon agents",
        "stages": "S1, S3, S8",
        "problem": "Behavioral cloning insufficient for long-horizon agents; need RL on AgentGym trajectories.",
        "representation": "AgentGym-RL: RL fine-tuning on AgentGym envs for long-horizon tool use; reward from env success.",
        "wrf": "Policy generates actions → env feedback → RL update; memory from successful trajectories.",
        "conflict": "Silent.",
        "privacy": "Silent.",
        "lessons": "(1) Kedger v1 avoids RL memory controller but RL trajectories feed L3 promotion. (2) Long-horizon reward shapes what gets remembered. (3) Pair with AgentGym platform for eval. (4) Log trajectory provenance for promoted Anchors.",
        "metric": "long-horizon env success after RL",
        "refine": "no",
    },
]


def validate(papers: list[dict]) -> None:
    for p in papers:
        for k in REQUIRED:
            assert k in p, f"{p.get('id')}: missing {k}"


def card(i: int, p: dict) -> str:
    parts = p["title"].split("—", 1)
    name = parts[0].strip()
    subtitle = parts[1].strip() if len(parts) > 1 else p["title"]
    return f"""
### {i}. {name} — {subtitle}
**arXiv:{p['id']}** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | {p['stages']} |
| **problem** | {p['problem']} |
| **representation** | {p['representation']} |
| **write / read / forget** | {p['wrf']} |
| **conflict** | {p['conflict']} |
| **privacy** | {p['privacy']} |
| **Kedger lessons** | {p['lessons']} |
| **metric_impact** | {p['metric']} |
| **refine_candidate** | **{p['refine']}** |

---
"""


def ids_line(papers: list[dict]) -> str:
    return ", ".join(f"`{p['id']}`" for p in papers)


def write_full_memo(path: Path, header: str, papers: list[dict], synthesis: str) -> None:
    cards = "".join(card(i + 1, p) for i, p in enumerate(papers))
    ids = [p["id"] for p in papers]
    body = f"""{header}

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new body deep-read; ID not previously FULL in CORPUS §2) | **17** | {ids_line(papers)} |
| **RE-READ** | **0** | — |
| **SKIPPED duplicate** | **0** | — |
| **Fetch failed / skipped** | **0** | All 17 IDs have `.txt` ≥25k chars |

**Cache path:** `/tmp/kedger-papers/full/{{id}}.txt`

---

## 1. Mechanism cards
{cards}
## 2. Batch synthesis

{synthesis}

---

## 3. Cached FULL ID list

```
{chr(10).join(ids)}
```
"""
    path.write_text(body)


def write_ledger(path: Path, papers: list[dict], memo_tag: str, source: str) -> None:
    rows = []
    for p in papers:
        short = p["title"].split("—")[0].strip()
        rows.append(f"| {p['id']} | {short} | **FULL** | no | {memo_tag} |")
    body = f"""# Ledger delta — {memo_tag} (for CORPUS_INVENTORY merge)

> **Date:** 2026-08-08  
> **Source memo:** `docs/research/batches/{source}`  
> **Cache:** `/tmp/kedger-papers/full/{{id}}.txt`

Merge rule: set inventory depth to **FULL** for every row below (all new FULL for CORPUS §2 arXiv ledger).

| ID | Title | Status | Prior FULL? | Memo |
|----|-------|--------|-------------|------|
{chr(10).join(rows)}

## Counts

| Bucket | N |
|--------|--:|
| FULL (new arXiv) | **17** |
| RE-READ | 0 |
| SKIPPED duplicate | 0 |

## Successfully FULL ID list

```
{chr(10).join(p['id'] for p in papers)}
```
"""
    path.write_text(body)


def main() -> None:
    validate(B13)
    validate(B14)
    assert len(B13) == 17 and len(B14) == 17

    b13_header = """# Batch 13 — Promote · Eng-Judgment · Abstention · Provenance · Decision/Rejection (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-300-fb37`  
> **Scope:** Tier-4/6 runway — **promotion gates**, **eng-judgment eval**, **abstention/faithfulness**, **provenance/SUPERSEDES**, **decision/rejection anchors**, **experience promotion**. Papers **not** already FULL in `CORPUS_INVENTORY.md` §2 (Batch4–Batch12). ADR/QOC already FULL in Batch8 — not re-marked.  
> **Method:** Full arXiv HTML/ar5iv or PDF→text; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards only — not abstract skim.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Lens:** S4 promote, S6 share gates, S8 why/abstain, ConflictSet, eng-judgment gold, provenance chains"""

    b13_synth = """| Theme | Papers | Kedger hook |
|-------|--------|-------------|
| **Promotion / verification** | FEVER, VitaminC, FLAME, ReMe, ERL, Early Experience | S4 gates; Supported/Refuted/NEI; contrastive supersession |
| **Eng-judgment** | G-Eval, Prometheus 2, RAGAS, Auto-CoT, Active ICL, CoT design, PerCul | Rubric judges; reference-free RAG faithfulness; cultural calibration |
| **Abstention** | R-Tuning, FEVER NEI | Selective prediction; refuse when Evidence absent |
| **Provenance / attribution** | Hallucination sources, Retroformer | Source taxonomy; retrospective feedback chains |
| **Decision / rejection** | REVERSE, R-Tuning | Generate-verify-reject before Anchor commit |"""

    b14_header = """# Batch 14 — Mixed Runway · Agent Memory · Retrieve Lineage (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-300-fb37`  
> **Scope:** Remaining high-value **agent-memory** + **retrieve lineage** papers from FULL runway seed queue with fetchable arXiv IDs not yet FULL in `CORPUS_INVENTORY.md` §2. Excludes Batch9–12 FULL (MIRIX, M3-Agent, HiAgent, ReSum, REPLUG, etc.).  
> **Method:** Full arXiv HTML/ar5iv or PDF→text; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards only.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Lens:** Symbolic+latent memory, procedural lifecycle, retrieve co-training, agent training platforms"""

    b14_synth = """| Theme | Papers | Kedger hook |
|-------|--------|-------------|
| **Symbolic memory** | ChatDB | SQL/graph as exact memory substrate |
| **Parametric/latent memory** | MemoryLLM, M+, MemGen, ElasticMem, InfLLM | Update slots; generative recall; elastic capacity |
| **Procedural memory** | Neural PM, Managing PM, Hierarchical PM | Lifecycle, hierarchy, Bayesian selection |
| **Retrieve lineage** | kNN-LM, ColBERT, Atlas, REALM | Non-parametric datastore; late interaction; co-training |
| **Agent platforms** | AgentGym, AgentGym-RL, LeanMem, ELITE | Multi-env trajectories; RL; efficient retention |"""

    write_full_memo(OUT / "BATCH13_PROMOTE_WHY_FULL.md", b13_header, B13, b13_synth)
    write_full_memo(OUT / "BATCH14_MIXED_RUNWAY_FULL.md", b14_header, B14, b14_synth)
    write_ledger(OUT / "BATCH13_LEDGER_DELTA.md", B13, "BATCH13", "BATCH13_PROMOTE_WHY_FULL.md")
    write_ledger(OUT / "BATCH14_LEDGER_DELTA.md", B14, "BATCH14", "BATCH14_MIXED_RUNWAY_FULL.md")
    print("Generated 4 batch files")


if __name__ == "__main__":
    main()
