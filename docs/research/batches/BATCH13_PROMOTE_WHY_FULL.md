# Batch 13 — Promote · Eng-Judgment · Abstention · Provenance · Decision/Rejection (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch-to-300-fb37`  
> **Scope:** Tier-4/6 runway — **promotion gates**, **eng-judgment eval**, **abstention/faithfulness**, **provenance/SUPERSEDES**, **decision/rejection anchors**, **experience promotion**. Papers **not** already FULL in `CORPUS_INVENTORY.md` §2 (Batch4–Batch12). ADR/QOC already FULL in Batch8 — not re-marked.  
> **Method:** Full arXiv HTML/ar5iv or PDF→text; cache `/tmp/kedger-papers/full/{id}.txt`. Mechanism cards only — not abstract skim.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Lens:** S4 promote, S6 share gates, S8 why/abstain, ConflictSet, eng-judgment gold, provenance chains

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new body deep-read; ID not previously FULL in CORPUS §2) | **17** | `1803.05355`, `2103.08541`, `2303.16634`, `2405.01535`, `2311.09677`, `2309.15217`, `2405.01525`, `2305.14552`, `2512.10696`, `2603.24639`, `2210.03493`, `2504.13169`, `2305.14264`, `2309.11054`, `2308.02151`, `2510.08558`, `2502.07459` |
| **RE-READ** | **0** | — |
| **SKIPPED duplicate** | **0** | — |
| **Fetch failed / skipped** | **0** | All 17 IDs have `.txt` ≥25k chars |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt`

---

## 1. Mechanism cards

### 1. FEVER — fact extraction and verification
**arXiv:1803.05355** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S8 |
| **problem** | Claim verification against Wikipedia: 185k claims labeled Supported/Refuted/NotEnoughInfo with sentence-level evidence. |
| **representation** | Pipeline: retrieve evidence → classify claim veracity; NEI = abstain when evidence insufficient. |
| **write / read / forget** | Read-only external corpus; no memory write — NEI class is explicit non-commit. |
| **conflict** | Evidence may contradict claim; Refuted = reject promotion analog. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S4 promote only with Supported-class evidence spans. (2) S8 `why` cites evidence sentences like FEVER annotations. (3) NEI → abstain, never invent Anchor. (4) Label quality κ≈0.68 — human promotion gates need calibration. |
| **metric_impact** | verification ACC + NEI precision |
| **refine_candidate** | **yes** |

---

### 2. VitaminC — contrastive fact verification
**arXiv:2103.08541** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S8 |
| **problem** | Fact verifiers fail on subtle Wikipedia revisions — need sensitivity to near-identical contrasting evidence. |
| **representation** | >400k claim-evidence pairs from >100k Wikipedia fact revisions; contrastive pairs differ minimally but flip label. |
| **write / read / forget** | Read-only evidence; auxiliary tasks: tag relevant words, identify factual revisions, generate consistent edits. |
| **conflict** | Core: nearly identical passages with opposite veracity — tests supersession detection. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) SUPERSEDES must detect micro-edits not just wholesale replacement. (2) Promotion fixtures need contrastive near-dup pairs. (3) +10% adversarial FV accuracy from contrastive training. (4) Word-level salience maps → Anchor span grounding. |
| **metric_impact** | contrastive FV accuracy |
| **refine_candidate** | **yes** |

---

### 3. G-Eval — GPT-4 NLG evaluation with CoT rubrics
**arXiv:2303.16634** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S8 |
| **problem** | Reference metrics (BLEU/ROUGE) misalign with humans; need reference-free LLM judges with better correlation. |
| **representation** | G-Eval: LLM chain-of-thought + form-filling rubric (coherence, consistency, fluency, relevance); probability-weighted scoring. |
| **write / read / forget** | Read-only eval — no persistent store; judge reads candidate output + optional reference. |
| **conflict** | Silent on factual conflict resolution. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Eng-judgment SLIs should use CoT rubrics not single scalar. (2) Spearman 0.514 on summarization — still imperfect; combine auto+human. (3) Watch bias toward LLM-generated text in judges. (4) S8 rationale quality evaluable via G-Eval dimensions. |
| **metric_impact** | human-judge Spearman on promotion/why quality |
| **refine_candidate** | **yes** |

---

### 4. Prometheus 2 — open rubric-specialized judge LM
**arXiv:2405.01535** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S8 |
| **problem** | Proprietary judges (GPT-4) costly/opaque; need open models for absolute + relative scoring with rubrics. |
| **representation** | Prometheus 2: fine-tuned judge LM; absolute score 1–5 on custom rubric + pairwise preference mode; reference-answer optional. |
| **write / read / forget** | Read-only assessment; rubric + response (+ optional reference) in context. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Kedger eng fixtures can use Prometheus-class rubrics for Anchor promotion QA. (2) Relative mode for A/B compose outputs. (3) Open judge enables CI regression on S8 quality. (4) Custom rubrics per SLI dimension (faithfulness, completeness). |
| **metric_impact** | rubric score correlation vs human |
| **refine_candidate** | **yes** |

---

### 5. R-Tuning — instruct LLMs to say 'I don't know'
**arXiv:2311.09677** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S7, S8 |
| **problem** | LLMs hallucinate on unknowns; need selective prediction / abstention without always guessing. |
| **representation** | R-Tuning: fine-tune on (question, answer) + (question, abstention) pairs; model learns when to refuse. |
| **write / read / forget** | Parametric update during training; inference = abstention token or refusal phrase on low-confidence. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S7 hydrate should abstain when Evidence empty — R-Tuning class. (2) S4 reject promotion when grounding score below τ. (3) Pair unknowns with explicit abstention in training data. (4) Reduces hallucination on unanswerable queries. |
| **metric_impact** | abstention precision/recall on NEI queries |
| **refine_candidate** | **yes** |

---

### 6. RAGAS — reference-free RAG evaluation
**arXiv:2309.15217** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | RAG systems lack gold labels; need automatic metrics for faithfulness and relevance without human refs. |
| **representation** | RAGAS: faithfulness (answer grounded in context), answer relevance, context precision/recall — LLM-as-judge decomposition. |
| **write / read / forget** | Eval-only; reads (question, retrieved contexts, answer) tuple. |
| **conflict** | Faithfulness metric detects unsupported claims vs retrieved context. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S7 SLI: faithfulness of hydrated answer to Evidence pack. (2) Context precision = retrieve quality gate before compose. (3) Reference-free → usable in CI on synthetic fixtures. (4) Decompose RAG eval not single EM score. |
| **metric_impact** | RAGAS faithfulness + context precision |
| **refine_candidate** | **yes** |

---

### 7. FLAME — factuality-aware alignment
**arXiv:2405.01525** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S7, S8 |
| **problem** | Alignment improves helpfulness but can hurt factuality; need benchmarks + training for factual consistency. |
| **representation** | FLAME benchmark: atomic claim verification + citation grounding tasks; measures factuality under alignment. |
| **write / read / forget** | Read-path verification over claims with optional citations. |
| **conflict** | Atomic claims may conflict; verification resolves per-claim. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Post-promotion Anchor audit = atomic claim check (FLAME-style). (2) Citation grounding for S8 `why` chains. (3) Alignment passes must not regress factuality SLI. (4) Separate helpfulness vs faithfulness metrics. |
| **metric_impact** | atomic factuality + citation grounding ACC |
| **refine_candidate** | **yes** |

---

### 8. Sources of hallucination in LLMs on inference — Sources of hallucination in LLMs on inference
**arXiv:2305.14552** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S7, S8 |
| **problem** | Hallucinations arise from multiple sources — need taxonomy to target mitigation (data vs model vs prompt). |
| **representation** | Empirical study decomposing hallucination sources: pretraining data gaps, finetuning, decoding, retrieval errors. |
| **write / read / forget** | Analysis paper — no new memory architecture; categorizes failure modes at inference. |
| **conflict** | Retrieval-context conflict listed as hallucination source. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S7 failures: tag whether hallucination from retrieve vs parametric vs compose. (2) Promotion rejects when source=parametric-only on factual Anchors. (3) Mitigation differs by source — no one fix. (4) Provenance logging helps attribute source class. |
| **metric_impact** | hallucination source attribution in fixtures |
| **refine_candidate** | **yes** |

---

### 9. ReMe — dynamic procedural memory
**arXiv:2512.10696** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S8 |
| **problem** | Static procedural memory fails as tasks evolve; agents need experience distillation and iterative refinement. |
| **representation** | ReMe: procedural memory framework — capture trajectories, distill reusable procedures, refine via feedback loop. |
| **write / read / forget** | Write procedural traces → distill → read at task time → refine on failure/success signals. |
| **conflict** | Silent unless explicit version supersession. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) L3 procedural Anchors need refine loop not write-once. (2) S4 promotion after successful replay validation. (3) Distill multi-step traces to compact procedure cards. (4) Pair with eval on procedure reuse rate. |
| **metric_impact** | procedure reuse success rate |
| **refine_candidate** | **yes** |

---

### 10. ERL — experiential reflective learning
**arXiv:2603.24639** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S8 |
| **problem** | LLM agents don't learn from past trajectories without explicit experience replay and reflection. |
| **representation** | ERL: collect experiences → reflective summarization → replay buffer curation → policy improvement without weight updates. |
| **write / read / forget** | Write experience logs → reflect → promote curated lessons → read during new episodes. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S3 cognify + S4 promote = ERL-style reflection before L3 commit. (2) Replay buffer curation prevents noise accumulation. (3) Self-improvement without finetuning matches Kedger CLI model. (4) Measure improvement over episode batches. |
| **metric_impact** | task success delta after ERL cycles |
| **refine_candidate** | **yes** |

---

### 11. Auto-CoT — automatic chain-of-thought prompting
**arXiv:2210.03493** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Manual CoT demos costly; need automatic demonstration selection for reasoning tasks. |
| **representation** | Auto-CoT: cluster questions → select representative demos per cluster → zero-shot CoT generation pipeline. |
| **write / read / forget** | Read-only demo pool; selects k in-context examples automatically. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S8 `why` generation can auto-select exemplar rationales by cluster. (2) Demo diversity matters — cluster before select. (3) Reduces manual eng-judgment fixture authoring. (4) Pair with active learning (2305.14264) for budgeted selection. |
| **metric_impact** | reasoning ACC vs manual CoT |
| **refine_candidate** | **no** |

---

### 12. REVERSE — generate but verify
**arXiv:2504.13169** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S7, S8 |
| **problem** | Multimodal models hallucinate objects/relations — need generate-then-verify before output commit. |
| **representation** | REVERSE: generate candidate answer → self-verify against image/context → reject or revise before final output. |
| **write / read / forget** | Draft → verify gate → commit/reject loop; no persistent memory. |
| **conflict** | Verification rejects inconsistent generations. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S4 promotion = generate-verify-reject pattern before Anchor commit. (2) S7 compose should verify hydrated answer vs Evidence before return. (3) Rejection anchor when verify fails. (4) Applicable beyond VLM to text compose. |
| **metric_impact** | hallucination rate pre/post verify gate |
| **refine_candidate** | **yes** |

---

### 13. Active learning principles for in-context learning — Active learning principles for in-context learning
**arXiv:2305.14264** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | ICL demo selection under label budget — which examples maximize performance? |
| **representation** | Active learning framework for ICL: uncertainty/diversity criteria to pick demos from pool. |
| **write / read / forget** | Read demo pool; write nothing — selects subset for context. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Hydrate pack demo selection = active learning problem. (2) Budget k demos by uncertainty on target query. (3) Label-efficient eng-judgment calibration. (4) Combine with KATE kNN retrieval (Batch8). |
| **metric_impact** | ICL ACC vs demo budget |
| **refine_candidate** | **no** |

---

### 14. Design of chain-of-thought for math problem solving — Design of chain-of-thought for math problem solving
**arXiv:2309.11054** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S8 |
| **problem** | CoT prompt structure materially affects math reasoning reliability — design choices matter. |
| **representation** | Empirical study of CoT templates: step granularity, intermediate variable naming, equation ordering. |
| **write / read / forget** | Prompt-only; no memory persistence. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S8 `why` templates should follow validated CoT structure. (2) Step granularity affects error rate — tune for audit readability. (3) Eng-judgment rubrics should check intermediate steps. (4) Bad CoT design → false promotion of wrong rationale. |
| **metric_impact** | math/reasoning step correctness |
| **refine_candidate** | **no** |

---

### 15. Retroformer — retrospective LLM agents
**arXiv:2308.02151** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S7, S8 |
| **problem** | LLM agents lack retrospective learning from past failures in multi-step tasks. |
| **representation** | Retroformer: frozen LLM agent + trainable retrospective model providing hindsight feedback to refine prompts/plans. |
| **write / read / forget** | Log trajectories → retrospective model generates feedback → adjust forward policy prompts. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S8 post-mortem on failed hydrate/compose feeds S3 cognify. (2) Retrospective feedback without finetuning base LM. (3) Provenance: link feedback to failed trajectory ID. (4) Improves multi-step tool/agent success. |
| **metric_impact** | multi-step task success after retrospective feedback |
| **refine_candidate** | **yes** |

---

### 16. Agent learning via early experience — Agent learning via early experience
**arXiv:2510.08558** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S8 |
| **problem** | Agents deployed cold-start; need pre-deployment experience accumulation before live tasks. |
| **representation** | Early Experience paradigm: sandbox exploration → distill skills/procedures → transfer to deployment agent. |
| **write / read / forget** | Write sandbox trajectories → abstract experience → read at deployment; promotion after validation. |
| **conflict** | Silent. |
| **privacy** | Sandbox may contain synthetic data only. |
| **Kedger lessons** | (1) S4 promotion from sandbox to production Anchor store requires explicit gate. (2) Early experience ≠ live memory — separate namespaces. (3) Distill exploration into L3 before user-facing deploy. (4) Measure transfer success rate. |
| **metric_impact** | sandbox→live task transfer ACC |
| **refine_candidate** | **yes** |

---

### 17. PerCul — story-driven cultural evaluation
**arXiv:2502.07459** · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S8 |
| **problem** | Western-centric benchmarks miss cultural reasoning; need localized eval with native speaker judgment. |
| **representation** | PerCul: Persian cultural stories + native annotator rubrics; tests cultural knowledge and reasoning. |
| **write / read / forget** | Eval-only benchmark; no agent memory. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Eng-judgment rubrics must be locale/culture-aware for global users. (2) Promotion gates calibrated on diverse cultural fixtures. (3) Auto-judges (G-Eval) may fail on cultural items — human fallback. (4) Expand fixture diversity beyond English-centric LoCoMo class. |
| **metric_impact** | cultural reasoning ACC by locale |
| **refine_candidate** | **no** |

---

## 2. Batch synthesis

| Theme | Papers | Kedger hook |
|-------|--------|-------------|
| **Promotion / verification** | FEVER, VitaminC, FLAME, ReMe, ERL, Early Experience | S4 gates; Supported/Refuted/NEI; contrastive supersession |
| **Eng-judgment** | G-Eval, Prometheus 2, RAGAS, Auto-CoT, Active ICL, CoT design, PerCul | Rubric judges; reference-free RAG faithfulness; cultural calibration |
| **Abstention** | R-Tuning, FEVER NEI | Selective prediction; refuse when Evidence absent |
| **Provenance / attribution** | Hallucination sources, Retroformer | Source taxonomy; retrospective feedback chains |
| **Decision / rejection** | REVERSE, R-Tuning | Generate-verify-reject before Anchor commit |

---

## 3. Cached FULL ID list

```
1803.05355
2103.08541
2303.16634
2405.01535
2311.09677
2309.15217
2405.01525
2305.14552
2512.10696
2603.24639
2210.03493
2504.13169
2305.14264
2309.11054
2308.02151
2510.08558
2502.07459
```
