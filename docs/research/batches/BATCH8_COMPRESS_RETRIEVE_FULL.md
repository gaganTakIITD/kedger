# Batch 8 — Compress · Retrieve · Active RAG · Prompt Injection · Eng-Judgment (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch8-measure-refine-fb37`  
> **Scope:** Tier-6 runway — **active/interleaved retrieval**, **context compression** (gist/KV/embedding), **hydrate robustness**, **classic prompt injection**, **embedding inversion**, **agent backdoors**, **ADR/QOC eng-judgment**. Papers **not** already FULL in `CORPUS_INVENTORY.md` §2 arXiv ledger or Batch4–Batch7.  
> **Prioritized cached queue:** FLARE, ConflictRAG, IRCoT, Gist Tokens, Text Embeddings Reveal, Chain-of-Note, Selective Context duplicate skipped, CCM, Prompt Injection apps.  
> **Method:** Full arXiv HTML (ar5iv fallback) or PDF→text when HTML thin; cache `/tmp/kedger-papers/full/{id}.{html,txt,pdf}`. Mechanism cards only — not abstract skim.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Lens:** S7 pack compile, compression budgets, query-aware retrieve, conflict-before-answer, untrusted Evidence, Inv-Scope, compact shareable rationale (ADR/QOC).

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new body deep-read; ID not previously FULL in CORPUS §2 / Batch4–7) | **16** | FLARE (2305.06983); ConflictRAG (2605.17301); IRCoT (2212.10509); Gist Tokens (2304.08467); Text Embeddings Reveal (2310.06816); Chain-of-Note (2311.09210); HouYi PI (2306.05499); CCM (2312.03414); MemoRAG (2409.05591); xRAG (2405.13792); ReadAgent (2402.09727); BadAgent (2406.03007); Automated PI AgentDojo (2606.10525); KATE (2101.06804); RAG-Fusion (2402.03367); ADR/QOC eng-judgment (`adr-qoc-design-rationale`) |
| **SKIPPED duplicate** | **1** | `2310.06201` — same Selective Context as `2304.12102` (BATCH6 FULL); HTML fetched, not re-marked |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped (no invented content)** | **0** | `2312.03414` / `2101.06804` via ar5iv; all 16 FULL IDs have `.txt` ≥25k chars (ADR card from SHAREABLE memo bodies) |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt` (all 15 arXiv FULL IDs present).

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded. Numbers are from paper text/tables.

---

## 1. Mechanism cards

### 1.1 FLARE — Forward-Looking Active REtrieval augmented generation  
**arXiv:2305.06983** · Jiang et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Single-shot retrieve-and-generate fails for long-form QA/summary/CoT — information needs emerge mid-generation. |
| **representation** | **Active RAG** framework: at step t, query qry(x, y_<t); generate chunk y_t conditioning on D_qt. **FLARE:** draft next **sentence**; if low-confidence tokens → use draft as query → retrieve → regenerate sentence. Variants: FLARE_instruct (LM emits search queries) vs FLARE_direct. |
| **write / read / forget** | Read-only external corpus; discards prior retrieved docs each step (only current D_qt in context). No memory write. |
| **conflict** | Silent on contradictory docs. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Mid-session `modex recall` should trigger on **uncertainty**, not fixed intervals. (2) Forward-looking query = next planned Anchor/evidence need, not only user utterance. (3) Do not accumulate unbounded retrieved Evidence in WorkingState — swap per step like FLARE. (4) Long `why` chains may need interleaved retrieve during generation. |
| **metric_impact** | Long-form QA utility under active vs passive retrieve; retrieve count × quality on 2Wiki/StrategyQA/ASQA/WikiAsp. |
| **refine_candidate** | **yes** — S7 confidence-triggered mid-turn hydrate |

---

### 1.2 ConflictRAG — detect/classify/resolve before generation  
**arXiv:2605.17301** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S7, S8 |
| **problem** | RAG assumes retrieved docs are mutually consistent; contradictions degrade answers. |
| **representation** | Pipeline: hybrid BM25+Contriever (K=5) → **two-stage conflict detection** (MiniLM-MLP @ τ_c=0.7 handles ~73% pairs @ 120ms; LLM fallback) → type-adaptive resolution → conflict-aware generation w/ source attribution. **Entropy-TOPSIS** MCDM for factual conflicts (authority/recency/relevance/specificity/consistency weights). **CARS** diagnostic metric (AC, detection F1, resolution, source fidelity). Parametric–contextual detector compares closed- vs open-book answers. |
| **write / read / forget** | Read-path over corpus; no persistent belief update — resolution picks sources pre-answer. |
| **conflict** | Core: inter-doc factual/temporal/opinion conflicts + parametric vs context. **88.7%** detection F1; **90.8%** binary accuracy @ **62%** API cost reduction vs LLM-only. **+5.3–6.1%** correctness vs strongest conflict-aware baseline on natural benchmarks. |
| **privacy** | Source attribution increases transparency; silent on membership. |
| **Kedger lessons** | (1) S4/S5 compose must run **ConflictSet before pack compile**, not only post-hoc `why`. (2) Cheap embedding classifier + LLM fallback mirrors Kedger tiered cognify. (3) Entropy-TOPSIS ≈ weighted Anchor provenance (authority/recency) for SUPERSEDES losers. (4) CARS-style SLI: correctness + conflict-handling, not EM alone. |
| **metric_impact** | Conflict detection F1; answer correctness under injected contradictions; resolution appropriateness. |
| **refine_candidate** | **yes** — S4/S7 ConflictRAG-style pre-hydrate conflict module |

---

### 1.3 IRCoT — interleaved retrieval with chain-of-thought  
**arXiv:2212.10509** · Trivedi et al. · 2022 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7, S8 |
| **problem** | One-shot question retrieval insufficient for multi-hop — next evidence depends on partial reasoning. |
| **representation** | Start: retrieve K paragraphs on question. Loop: **Reason** — generate next CoT sentence from Q + collected paragraphs + prior CoT; **Retrieve** — use last CoT sentence as query for K more paragraphs (cap total **15**). Terminate on “answer is” or max **8** steps. Reader: CoT or direct prompting over final paragraph set. |
| **write / read / forget** | Read-only corpus; paragraphs accumulate (dedup implicit). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Default multi-hop hydrate = **interleave graph/Anchor expand with reasoning trace**, not one-shot embedding search. (2) Persist explored path as S8 `why` (IRCoT trace). (3) Cap paragraphs/steps like HippoRAG PPR budget. (4) CoT sentence as query ≈ PropRAG beam step without training. Paper: **+11–21** recall points vs question-only; **+15** F1 QA; **~50%** fewer CoT factual errors (GPT-3). |
| **metric_impact** | Fixed-budget gold-paragraph recall; multi-hop F1 on HotpotQA/2Wiki/MuSiQue/IIRC. |
| **refine_candidate** | no (PropRAG/GraphReader tickets cover interleaved expand) |

---

### 1.4 Gist Tokens — compress prompts into cached activations  
**arXiv:2304.08467** · Mu et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Prompts occupy context window; re-encoding same instruction is wasteful. |
| **representation** | Insert k **gist tokens** after prompt; modified attention mask blocks post-gist tokens from attending to pre-gist prompt → forces compression into gist KV activations. Instruction tuning on Alpaca+ (130k examples). Meta-learn compression across tasks (HyperNetwork view). |
| **write / read / forget** | Cache gist KV per task prompt; read at inference. No symbolic forget. |
| **conflict** | Silent. |
| **privacy** | Silent — compressed activations may retain sensitive prompt text (see embedding inversion batch mate). |
| **Kedger lessons** | (1) System/instruction facets of L4 pack are gist-cache candidates; never gist-compress Anchor **statements**. (2) Up to **~26×** prompt compression, **~40%** FLOPs reduction, **~4.2%** wall-time speedup in paper. (3) Attention-mask trick cheaper than per-task soft prompts. (4) Separate neural gist from symbolic WorkingState ≤4 KiB policy. |
| **metric_impact** | Compression ratio vs win-rate vs uncompressed control on Human/Alpaca eval splits. |
| **refine_candidate** | no (symbolic pack path preferred for audit) |

---

### 1.5 Text Embeddings Reveal — embedding inversion attack  
**arXiv:2310.06816** · Morris et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S6, S7 |
| **problem** | Dense embeddings used for memory/RAG may leak source text. |
| **representation** | **Embedding inversion:** train decoder to reconstruct text from embeddings via iterative correct-and-re-embed. Eval on OpenAI + SOTA embedding models; can recover **full names** and sensitive spans from doc embeddings. |
| **write / read / forget** | Attack is read on stored embeddings; **~92%** exact recovery on **32-token** inputs in paper. |
| **conflict** | Silent. |
| **privacy** | Core privacy paper: embeddings ≠ safe compression for secrets. Inversion risk scales with embedder quality. |
| **Kedger lessons** | (1) Do not store raw embeds of `private_raw` in shared indexes without encryption/attenuation. (2) S6 unshare must **tombstone vectors** + caches (aligns GEIA/MemLeak). (3) Prefer structured Anchor fields over embedding-only Evidence for shareable tiers. (4) Red-team fixture: invert hydrated snippet embeds post-unshare. |
| **metric_impact** | Inversion exact-match rate @ token length; residual leak after tombstone. |
| **refine_candidate** | **yes** — S6/S7 embedding inversion residual probe |

---

### 1.6 Chain-of-Note (CoN) — sequential reading notes for RALMs  
**arXiv:2311.09210** · Yu et al. · EMNLP 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7, S8 |
| **problem** | Noisy/irrelevant retrieved docs mislead RALMs; models ignore parametric knowledge when retrieval wrong. |
| **representation** | For each retrieved doc d_i, generate reading note y_{d_i} assessing relevance; then final answer y. Note types: (a) direct support, (b) contextual inference, (c) **unknown** when irrelevant + OOD. Trained LLaMA-2-7B on 10k GPT-4 CoN traces; **Hybrid Training** internalizes reasoning. |
| **write / read / forget** | Read retrieved docs; notes are ephemeral unless logged. |
| **conflict** | Notes can flag conflicting docs (implicit). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S7 pack compile should attach **per-Evidence note** (ISREL-like) before injecting. (2) Explicit **abstain/unknown** path when retrieved Anchors irrelevant (Self-RAG steal). (3) **+7.9** EM under noise; **+10.5** rejection rate on RealTimeQA OOD. (4) CoN > CoT for retrieval-augmented settings per paper GPT-4 study. |
| **metric_impact** | QA EM/F1 under noisy retrieval; OOD rejection rate. |
| **refine_candidate** | **yes** — S7 per-Evidence reading-note gate |

---

### 1.7 HouYi — prompt injection against LLM-integrated applications  
**arXiv:2306.05499** · Liu et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | LLM-integrated apps merge user input + third-party content — classic **prompt injection** surface. |
| **representation** | **HouYi** black-box attack framework: compose prompts from **framework / separator / disruptor** components; infer app context; iterative refinement. Pilot categorizes injection types; evaluates on anonymized real apps (WriteSonic prompt leak, Parea abuse cases). |
| **write / read / forget** | Attack harness; may exfil system prompts or hijack app behavior. |
| **conflict** | Integrity / instruction hierarchy failure. |
| **privacy** | Prompt leak = confidentiality breach. |
| **Kedger lessons** | (1) Tool returns + web/email Evidence are **untrusted instruction channels** (extends InjecAgent). (2) S6 sealed packs must not concatenate raw external content without delimiter + sanitizer. (3) Separator/disruptor patterns → S1 denylist fixtures. (4) Black-box PI testing required for hydrate APIs exposing retrieved text to models. |
| **metric_impact** | Vulnerability detection rate on LLM-app corpus; successful prompt leak / hijack cases. |
| **refine_candidate** | no (Batch7 IPI/firewall tickets primary) |

---

### 1.8 Compressed Context Memory (CCM) — online KV compression  
**arXiv:2312.03414** · Kim et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S7 |
| **problem** | Online chat/personalization accumulates context → quadratic attention cost. |
| **representation** | **CCM:** compress each interaction chunk c(t) into ⟨COMP⟩ token KV via conditional **LoRA** (only on COMP tokens). Update Mem(t): **concat** (CCM-concat) or **merge** average (CCM-merge). Parallelized training unrolls recursion. Streaming variant with attention-sink sliding window. |
| **write / read / forget** | Write = append compressed memory; read = attend Mem(t) + current input. Merge forgets fine detail; concat retains per-step slots. |
| **conflict** | Silent. |
| **privacy** | Silent — compressed KV may retain secrets (cf. embedding inversion). |
| **Kedger lessons** | (1) WorkingState online growth needs **incremental compress**, not only PRE_COMPACT batch. (2) **~5×** smaller KV @ ~full-context accuracy on MetaICL/LaMP/DailyDialog; throughput **5.3→69.9** samples/s (A100) in paper Table 1. (3) Prefer concat when contexts are diverse (dialogue), merge when redundant (profiles). (4) Conditional LoRA pattern for cheap adapter without full finetune. |
| **metric_impact** | Accuracy/perplexity vs peak KV bytes; throughput @ batch. |
| **refine_candidate** | no (MemGPT pressure + LLMLingua cover symbolic path) |

---

### 1.9 MemoRAG — global memory + clue-based retrieve  
**arXiv:2409.05591** · Qian et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S5, S7 |
| **problem** | Standard RAG queries misaligned with implicit info needs in long contexts / non-QA tasks. |
| **representation** | Dual-system: light **memory model** Θ_mem builds global memory θ_mem of long context (KV-compressible); on query q, generate draft clues y → retrieve evidence E with clues (not q alone) → heavy generator Θ produces Y. **RLGF** rewards clues that improve answer quality. |
| **write / read / forget** | Write = compress full context to θ_mem (offloadable); read = clue-guided retrieve + generate. |
| **conflict** | Silent. |
| **privacy** | Global memory holds full doc — capability-scope before sharing θ_mem. |
| **Kedger lessons** | (1) Long repo/session hydrate: skim-to-memory then **clue-based** retrieve (human cognition fig). (2) Draft clues ≈ FLARE forward query at pack-compile time. (3) Wins on LongBench + InfiniteBench QA and **non-QA** summarization vs vanilla RAG. (4) Separate cheap memory builder from expensive answer model — maps to L2 digest vs L4 pack compiler. |
| **metric_impact** | Task accuracy on long-context suites vs RAG baselines; clue quality ablation. |
| **refine_candidate** | **yes** — S7 clue-guided hydrate for implicit queries |

---

### 1.10 xRAG — one-token retrieval modality fusion  
**arXiv:2405.13792** · Cheng et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | RAG concatenates full passages → long contexts; soft-prompt compressions need heavy activation storage. |
| **representation** | Treat dense retriever embedding E as **retrieval modality**; train small projector W to map E into LLM space as **one document token** [X]; frozen retriever + frozen LLM, train bridge only (<0.1% params). Two-stage: paraphrase pretrain + context-aware instruction tuning w/ RAG self-distillation. |
| **write / read / forget** | Reuse offline passage embeddings; no per-doc activation cache. |
| **conflict** | Silent. |
| **privacy** | Paper cites embeddings reveal almost as much as text — do not xRAG-compress private Evidence. |
| **Kedger lessons** | (1) Extreme compress trade: **>10%** avg gains on six knowledge tasks vs LLMLingua-style; **3.53×** FLOPs reduction vs full RAG in paper. (2) Only viable for **non-sensitive** public corpus chunks. (3) Plug-and-play aligns with frozen Anchor embed index + small adapter. (4) Complements Gist (prompt) vs xRAG (document). |
| **metric_impact** | Downstream QA F1 vs compression baselines; FLOPs @ equal retriever. |
| **refine_candidate** | no |

---

### 1.11 ReadAgent — gist memory over paginated long docs  
**arXiv:2402.09727** · Lee et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S7 |
| **problem** | Very long inputs exceed practical context; humans use gist + lookup. |
| **representation** | **ReadAgent:** (1) paginate context; (2) **gist** each page to episodic memory w/ page pointer; (3) **lookup** — LLM selects pages to expand in-context for task. Inspired by human verbatim vs gist memory. |
| **write / read / forget** | Write gists (lossy); read full pages on demand. |
| **conflict** | Silent. |
| **privacy** | Gists may drop secrets — or leak if too faithful; not studied. |
| **Kedger lessons** | (1) L2 episode digests = gist + provenance pointer (page/file/span). (2) S7 two-phase: always pack gists; expand raw L0 only on lookup within budget. (3) Beats full-context baselines on long-doc QA benchmarks in paper. (4) Complements GraphReader notebook walk. |
| **metric_impact** | Long-doc QA vs full-read; lookup count × accuracy. |
| **refine_candidate** | no (GraphReader + SeCom segment tickets) |

---

### 1.12 BadAgent — backdoor attacks on LLM agents  
**arXiv:2406.03007** · Gong et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S3, S6 |
| **problem** | Agent fine-tuning/backdoors can trigger harmful tool actions. |
| **representation** | **BadAgent:** poison fine-tune data with trigger T + covert op CO. **Active:** attacker inserts T in user input. **Passive:** T hidden in environment (web/product HTML). Tasks: OS, WebShop, Mind2Web. Metrics: ASR, FSR (benign task fidelity). |
| **write / read / forget** | Write = poison training set; read = trigger at inference. |
| **conflict** | Integrity backdoor, not SUPERSEDES. |
| **privacy** | Covert ops include exfil / purchase fraud. |
| **Kedger lessons** | (1) Do not run untrusted LoRA/adapters on capture/cognify paths. (2) **>85%** ASR on SOTA agents; **>90%** ASR @ 20% poison in paper — provenance-gate promoted skills. (3) Passive env triggers ⇒ web Evidence sanitization (AgentDojo class). (4) ASR/FSR pair = utility-under-attack SLI for tool agents. |
| **metric_impact** | ASR/FSR on agent tasks @ poison rate; defense fine-tune residual ASR. |
| **refine_candidate** | no (AgentPoison/MINJA memory tickets) |

---

### 1.13 Assessing Automated PI in Agentic Environments  
**arXiv:2606.10525** · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | Need automated, optimization-based PI evaluation for **stateful tool agents**, not static strings. |
| **representation** | Extends **AgentDojo** with **GCG** + **TAP** adversarial optimizers on tool-output injection slots; universal vs per-task attacks; tokenization-robust targets. Threat model: adversary controls tool/email/web content; goal = exfil or harmful tool use. |
| **write / read / forget** | Eval harness generating adaptive injections. |
| **conflict** | Instruction integrity attacks. |
| **privacy** | Exfil success criterion. |
| **Kedger lessons** | (1) S6 seal regression must include **optimized** PI, not template-only InjecAgent strings. (2) Combine AgentDojo utility metric with GCG/TAP ASR. (3) Chat-template aware attacks ⇒ normalize tool schemas before hydrate. (4) Adaptive attacks break delimiter-only defenses — need minimizer/sanitizer (IPI Firewalls). |
| **metric_impact** | AgentDojo ASR under GCG/TAP vs static PI; utility retained. |
| **refine_candidate** | **yes** — S6 optimized-PI AgentDojo extension harness |

---

### 1.14 KATE — kNN in-context example selection  
**arXiv:2101.06804** · Liu et al. · 2021 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | GPT-3 few-shot performance highly sensitive to which demos are in context. |
| **representation** | **KATE (kNN-Augmented in-context Example selection):** embed training examples + test input; retrieve nearest neighbors as ICL demos (vs random). Eval on classification/NLI tasks. |
| **write / read / forget** | Read-only demo bank. |
| **conflict** | Silent. |
| **privacy** | Nearest neighbor may leak similar private episodes — Inv-Scope filter needed. |
| **Kedger lessons** | (1) When hydrating few-shot reminders (prior decisions), retrieve by **embedding similarity to current goal**, not FIFO. (2) Demo bank = L2 case Evidence with embed index. (3) Pair with CoN/ISREL so bad neighbors aren't injected. |
| **metric_impact** | Task accuracy: KATE vs random ICL on GPT-3 suites. |
| **refine_candidate** | no |

---

### 1.15 RAG-Fusion — multi-query + reciprocal rank fusion  
**arXiv:2402.03367** · Rackauckas · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | Single-query retrieval misses facets of engineer/product questions. |
| **representation** | LLM generates **multiple query variants** → retrieve each → **RRF** fuse ranked lists → generate answer. Industrial eval (Infineon product QA): manual accuracy/relevance/comprehensiveness judges. |
| **write / read / forget** | Read-only corpus. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) S7 `query` hydrate mode: 2–3 rewrites + RRF over Anchor hits before budget cut (already in P5 spec — now FULL body). (2) Cheap lift for ambiguous eng queries. (3) Do not RRF private + shared indexes without Inv-Scope partition. |
| **metric_impact** | Judge scores vs single-query RAG on product QA set. |
| **refine_candidate** | no |

---

### 1.16 ADR / QOC / IBIS — design rationale as shareable memory (eng-judgment)  
**Source:** Nygard ADR practice; MacLean **QOC**; Gruber KSL-92-59; IBIS — deep-read via `SHAREABLE_ANCHOR_POLICY_RESEARCH.md` §D · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6, S8 |
| **problem** | Teams lose **why** behind decisions; chat logs are too noisy to share; rationale capture fails when detached from workflow. |
| **representation** | **ADR:** repo-local `docs/adr/`; lifecycle Proposed→Accepted→Deprecated/Superseded; Accepted **immutable** — change only via new ADR + SUPERSEDES link. **QOC/IBIS:** capture Question / Options / Criteria (or Issue/Position/Argument), not transcript. High-value artifact = compact decision sentence + alternatives + evidence links. |
| **write / read / forget** | Write on acceptance/promotion; read during handoff/onboarding; supersede via new ADR, never silent edit. |
| **conflict** | Explicit SUPERSEDES chain is the ADR norm — aligns with Kedger invalidation. |
| **privacy** | Public repo ADRs vs private personnel/legal notes; redact before `repo_shared_safe`. |
| **Kedger lessons** | (1) Promote **Anchor statement + reason + SUPERSEDES**, not episode digests (QOC lesson). (2) `repo_shared_safe` ≈ Accepted ADR tier; deliberation stays `workstream_private`. (3) Tie capture to PR/CAD/hook workflow or it won't happen. (4) S8 `why` should cite QOC options rejected, not replay private chat. |
| **metric_impact** | Eng-judgment pairwise: handoff pack with QOC-style Anchors vs transcript dump. |
| **refine_candidate** | no (policy locked in SHAREABLE memo) |

---

## 2. Cross-cutting map → Kedger stages

| Stage | Papers | Takeaway |
|-------|--------|----------|
| S1 hooks | HouYi PI, BadAgent, Automated PI | Untrusted channels; poisoned adapters; optimized injections |
| S2 working | Gist, CCM, ReadAgent, MemoRAG | Incremental compress; gist pointers; global memory sketch |
| S3 cognify | Text Embeddings Reveal, BadAgent | Embedding inversion risk; provenance-gate skills |
| S4 promote | ConflictRAG, ADR/QOC | Conflict before share; immutable Accepted + SUPERSEDES |
| S5 graph | IRCoT, ConflictRAG, MemoRAG | Interleaved expand; conflict detect; clue retrieve |
| S6 seal | HouYi, Text Embeddings Reveal, BadAgent, Automated PI | PI on integrated apps; vector tombstones; adaptive ASR |
| S7 hydrate | FLARE, IRCoT, CoN, xRAG, MemoRAG, KATE, RAG-Fusion, CCM | Active/clue/interleaved retrieve; reading notes; fusion |
| S8 why | FLARE, IRCoT, CoN, ADR/QOC | Traces + rationale, not raw retrieval dumps |

---

## 3. Refine tickets (≤3)

1. **ConflictRAG pre-hydrate conflict module** — MLP+LLM two-stage detect/classify on candidate Evidence; Entropy-TOPSIS source pick; metric: detection F1 + answer correctness under injected contradictions vs compose-only baseline.  
2. **S7 per-Evidence CoN reading-note gate** — Require sequential ISREL-style note per retrieved Anchor before pack; abstain path for OOD; metric: **+7.9** noisy EM class on eng QA fixture + rejection rate on stale Anchors.  
3. **Embedding inversion + optimized PI probe** — Text Embeddings Reveal fixture on shared embed index post-unshare; extend AgentDojo with GCG/TAP injections on tool outputs; metric: inversion EM @32 tokens → 0 after tombstone; ASR vs IPI firewall baseline.

---

## 4. Successfully FULL-read IDs

```
2305.06983
2605.17301
2212.10509
2304.08467
2310.06816
2311.09210
2306.05499
2312.03414
2409.05591
2405.13792
2402.09727
2406.03007
2606.10525
2101.06804
2402.03367
adr-qoc-design-rationale
```

**Skipped duplicate:** `2310.06201` (Selective Context — see `2304.12102` BATCH6).
