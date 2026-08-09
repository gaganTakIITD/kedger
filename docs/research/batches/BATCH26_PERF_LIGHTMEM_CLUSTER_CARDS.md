# Batch26 — Performance cluster deep-read mechanism cards

> **Date:** 2026-08-09  
> **Scope:** Body-grounded FULL deep-reads of LightMem / Reproducing LightMem / LeanMem / SLM-LightMem / All-Mem.  
> **Focus:** online/offline split · dual-path evidence+anchors · packing budgets · visible-surface memory · sleep-time merge.  
> **Cache:** `/tmp/kedger-papers/full/{id}.txt` (LeanMem was one long line; read via wrap).  
> **Do not invent:** Silent where the paper has no mechanism.

Kedger constants referenced in lessons: `L0`–`L4`, `HANDOFF_MAX_BYTES=32768`, `PPR_DAMPING=0.5`, `SURVIVAL_RANK`, `explicit_only`.

---

## 1. LightMem: Lightweight and Efficient Memory-Augmented Generation
**arXiv:2510.18866** · Fang, Deng, Xu, Jiang et al. · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **arxiv_id** | `2510.18866` |
| **title** | LightMem: Lightweight and Efficient Memory-Augmented Generation |
| **kedger_stages** | S1, S2, S3, S4, S7 |
| **problem** | Conventional agent memory summarizes/updates **every turn online**, feeding raw redundant dialogue into LLM extract/update; topic entanglement from fixed windows; update latency tightly coupled to inference. |
| **representation** | Atkinson–Shiffrin-style three stages: (1) **Light1 sensory** — LLMLingua-2 (or entropy) pre-compress retain tokens with \(P(\mathrm{retain})>\tau\) at compression rate \(r\); sensory buffer **512 tokens**; hybrid topic cut \(\mathcal{B}=\mathcal{B}_1\cap\mathcal{B}_2\) (attention local-max ∩ similarity drop). (2) **Light2 topic-aware STM** — buffer `{topic, user/model turns}` until token threshold \(th\) → LLM summarize → LTM entry `{topic, embed(sum), user, model}`. (3) **Light3 LTM sleep-time update** — online **soft insert** + build similarity update queues; offline **parallel** \(f_{\mathrm{update}}\) with \(t_j\ge t_i\) and top-\(k\) candidates. Complexity \(O(N r^x T / th)\) vs baseline \(O(N)\). |
| **write_read_forget** | **Write:** compress → topic-segment → STM flush at \(th\) → soft-insert LTM. **Read:** cosine retrieve over MiniLM embeddings of summaries (usage stage held constant across baselines). **Forget:** implicit via offline update/merge/delete ops; paper warns real-time LLM updates may incorrectly delete non-conflicting older entries — soft-add preserves semantics until sleep merge. |
| **conflict** | Timestamp-ordered update queues (later may update earlier); heavy conflict resolution deferred offline. No typed SUPERSEDES algebra. |
| **privacy** | Ethics: dialogue memory may hold sensitive data; advocates anonymization + consent. No ACL/`explicit_only` mechanism. |
| **numbers** | LongMemEval-S GPT-4o-mini best ACC **68.64%** (\(r{=}0.7,th{=}512\) online) / **67.07%** after OP-update; vs A-MEM **62.60%**, FullText **56.80%**. Qwen best online ACC **70.20%** (\(r{=}0.6,th{=}768\)). Claimed vs strongest baseline: ACC +**2.09–6.40%** (GPT) / up to **+7.67%** (Qwen); total tokens up to **38×** / **21.8×** down; API up to **30×** / **17.1×**; runtime up to **12.4×** / **6.3×**. Online-only: tokens up to **105.9×** / **117.1×**, API **159.4×** / **309.9×**. LoCoMo GPT LightMem(0.8,768) ACC **72.99%**, total **85.19k** tokens, **29.83** calls, **815.32s** vs Mem0 **61.69%** / **1693.39k** / **1602.20** calls. Topic-seg ablation: **−6.3%** GPT / **−5.4%** Qwen ACC; hybrid topic accuracy **>80%**. Compress submodule **<2GB** GPU. |
| **kedger_lessons** | (1) **L0 pre-compress before cognify** — drop boilerplate before any LLM extract; maps to S1 redact/filter before persist. (2) **Token-threshold STM (\(th\))** not turn-count — couples to L1/`WORKING_MAX_BYTES=4096` and episode flush, not only file soft/hard 12/40. (3) **Soft insert online + sleep-time merge offline** is the latency model for S3 cognify / S4 promote — never pay full SUPERSEDES in the hook path. (4) Offline parallel queues reinforce: consolidate outside hydrate; pack still bounded by `HANDOFF_MAX_BYTES=32768`. (5) Newer-wins via \(t_j\ge t_i\) ≈ temporal bias inside `SURVIVAL_RANK`/recency, but Kedger still needs typed SUPERSEDES + audit (not silent overwrite). (6) Retriever held constant in paper — do not treat ACC gains as pure architecture without S7 retrieve SLI. (7) Share stays `explicit_only` — ethics note ≠ share ladder. |
| **metric_impact** | LongMemEval-S / LoCoMo ACC; construction Summary+Update tokens/API/runtime; online vs online+offline cost split; topic-seg ablation; \(r\)/\(th\) Pareto. |
| **refine_candidate** | **yes** — S1/S2/S3 online soft-insert + offline sleep-time consolidate with token STM threshold + pre-compress gate |

---

## 2. Reproducing LightMem: Naive RAG Is Just as Good for Memory Management
**arXiv:2607.29104** · Zhou, Wang, Koopman, Zuccon · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **arxiv_id** | `2607.29104` |
| **title** | Reproducing LightMem: Naive RAG Is Just as Good for Memory Management |
| **kedger_stages** | S3, S7, S8 |
| **problem** | LightMem’s reported gains may be retriever-sensitive; constructed memory may discard answer-relevant raw evidence; end-to-end ACC conflates construction vs retrieval failures. |
| **representation** | Reproduction of LightMem sensory→STM→LTM with OP-update; configs \((r,th)\in\{(0.4,768),(0.6,768),(0.8,1024)\}\); `update_sim_threshold=0.8`, queue top-\(k{=}20\) keep \(n{=}10\); `messages_use=user_only`. Contrasts **constructed-memory RAG** vs **Naive RAG over raw user turns**; 11 sparse/dense/hybrid retrievers; matched depth and matched answering-token budgets; oracle gold turns vs constructed memories. |
| **write_read_forget** | Same LightMem construction + offline OP-update. Read varies only retriever over fixed store. Forget/loss measured via oracle gap (construction discards evidence). |
| **conflict** | Silent on typed conflict ops; knowledge-update category analyzed via retriever stability. Abstention: irrelevant retrieves can cause false answers. |
| **privacy** | Silent. |
| **numbers** | LongMemEval-S, 444 questions (exclude 56 single-session-assistant). Repro ACC: Full-context **60.8%**, Naive RAG **67.3%**, LightMem (0.4,768) **57.0%**, (0.6,768) **68.2%**, (0.8,1024) **70.7%** (original paper Qwen: 62.3 / 65.1 / 67.3). Constr. tokens ours **72.68–119.88k** vs paper **135.43–146.42k**; calls **64.69–117.62** vs **172.90–192.56**. Ans tokens top-10: LightMem **0.66–0.72k**/q vs Naive **1.03k** vs Full **18.84k**. Fixed store, vary retriever: ACC **58.1%–75.5%**, Recall@10 **0.390–0.587**; default MiniLM **70.7%** / **0.530**; Qwen3-Emb-4B **75.5%** / **0.587**; oracle-ref **77.7%**. Matched ~330 tok/q: LightMem +**5.5** ACC pts avg (8/11 retrievers); ~500 tok: +**2.2**; ~935 tok: slight disadvantage. Oracle: Naive gold **89.0%** vs LightMem constructed **77.7%** (**−11.3**); construction **119,884** tokens + **~117** LLM calls/sample; ans save ~**374** tok/q → break-even ~**321** questions. Naive SPLADE top-10 **78.8%** already exceeds LightMem oracle-ref. |
| **kedger_lessons** | (1) **Dual-path hydrate:** keep L0/Evidence raw turns as faithful bank; treat L3 summary Anchors as compact auxiliary — not a replacement (maps dual Evidence+Anchors). (2) Packing budgets matter: compact entries win only under tight ans budgets — directly informs `HANDOFF_MAX_BYTES=32768` Pareto SLIs (test ~330 / ~500 / ~1k token regimes). (3) S7 retriever choice can swing ACC by **~17 pts** on a fixed store — measure hydrate Recall separately from cognify. (4) Construction cost amortization (~321 q) must appear in eval harness, not only online latency. (5) Oracle gap = faithfulness probe for S8/why + cognify loss. (6) `PPR_DAMPING=0.5` / graph walk still need strong first-stage retrieve; fusion MiniLM+BM25 hurt here — don’t assume hybrid helps. (7) Share/`explicit_only` Silent. |
| **metric_impact** | Repro ACC ordering; Constr. tokens/calls; Ans tok/q; Recall@10; matched-depth Δ; matched-budget Δ; oracle ACC gap; break-even questions. |
| **refine_candidate** | **yes** — S7 dual-path Evidence+Anchor hydrate with matched token-budget SLI + construction-loss oracle |

---

## 3. LeanMem: Simple and Efficient Long-Term Memory for LLM Agents
**arXiv:2608.03463** · Liao, Wu, Hou, Liu, Wu, Wang · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **arxiv_id** | `2608.03463` |
| **title** | LeanMem: Simple and Efficient Long-Term Memory for LLM Agents |
| **kedger_stages** | S1, S2, S3, S4, S5, S7 |
| **problem** | Uniform summarize/retrieve pipelines either burn tokens or irreversibly lose fine-grained evidence; dialogue content differs in compressibility, temporal dynamics, and fidelity needs. |
| **representation** | Three stages: (1) **Controlled Memory Writing** — rule filter low-value turns; topic segments via similarity valley depth \(d_i\) with \(\tau=\mu_D+0.05\sigma_D\); LLM scheduler routes \(y\in\{\texttt{ignore},\texttt{profile},\texttt{event},\texttt{record}\}\) by stability / temporal dependence / fidelity (priority: temporal > stability; high fidelity overrides compress). Materialize: profile = attribute–value pairs (no extra LLM); event = \(\langle e,t,z\rangle\) topic/time/state; record = \(\langle gist, NER(GLiNER), source\ pointer\ I\rangle\) to original dialogue. (2) **Selective Memory Evolution** — only event memory buffered; offline localized merge by topic/state when buffer capacity hit. (3) **Adaptive Evidence Composition** — LLM planner \(\pi_q=\langle\mathcal{C}_q,d_q,\mathcal{M}_q,\mathbf{w}_q,\mathbf{k}_q\rangle\) picks types + per-type depths; rerank \(\mathrm{score}=w^c[\mathrm{Rel}_c+\mathrm{Match}]\); expand record pointers to raw spans only when needed. |
| **write_read_forget** | **Write:** filter→segment→route→heterogeneous materialize; profiles/records skip evolution. **Read:** query-conditioned type+budget composition (not fixed global top-\(k\)). **Forget:** `ignore` for non-persistent segments; no destructive delete of records (source-grounded). |
| **conflict** | Event evolution revises state / extends timeline via temporal anchors; silent on typed SUPERSEDES sets. |
| **privacy** | Silent (user attributes in profile memory — no share policy). |
| **numbers** | LoCoMo GPT-4.1-mini: LeanMem Recall **83.80** / Acc **84.87**, Build **69.45K**, Infer **3.04K**, Lat **2.77s** vs LightMem **82.17/79.33**, **106.67K**, **3.98K**, **4.88s**; vs A-Mem Build **1197.28K**. LongMemEval-S GPT: Acc **91.80**, Recall **97.67**, Build **117.61K**, Infer **3.62K**, Lat **2.16s** vs LightMem Acc **76.73** / A-Mem **71.40** (Build **1330.77K**). Gains vs strongest memory baseline: LoCoMo Acc **+5.54/+5.84** (GPT/Qwen); LongMemEval-S **+15.07/+2.80**. Abstract: up to **+15.1** Acc points; vs A-Mem up to **+20.40** Acc pts, build tokens up to **17.24×**↓, infer up to **8.41×**↓. LoCoMo category lifts vs strongest baseline: Multi-Hop **+12.02**, Temporal **+6.23**, Open-Domain **+2.46**, Single-Hop **+10.57**. Ablation Acc (GPT): full LoCoMo **84.87** / LME **91.80**; w/o utterance filter **75.58/82.20**; w/o topic seg **82.79/79.60**; w/o storage schedule **72.79/71.00**; w/o mem evolution **84.42/81.20**; w/o retrieval plan **77.92/81.20**. LongMemEval-S histories ~**115K** tokens, 40–50 sessions; LoCoMo ~**16K** tokens, up to 32 sessions. |
| **kedger_lessons** | (1) **Heterogeneous L2/L3 kinds** — profile≈constraint/preference Anchors, event≈timeline Anchors, record≈Evidence pointer+gist; do not uniform-summarize into one Anchor blob. (2) Record source pointers = dual-path Evidence+Anchor: pack gists under `HANDOFF_MAX_BYTES`, expand snippets (`EVIDENCE_SNIPPET_MAX`) on demand. (3) **Selective offline evolution only for temporal/event** — sleep-time merge should not rewrite stable `SURVIVAL_RANK` high kinds (constraint/rejection) every cycle. (4) Query-conditioned \(\mathbf{k}_q\) budgets = S7 hydrate packing policy beyond flat PPR; still compatible with `PPR_DAMPING=0.5` walks over ABOUT/TEMPORAL edges. (5) Topic valley \(\tau=\mu+0.05\sigma\) is a cheap S3 boundary prior alongside `SEGMENT_THETA=0.60`. (6) Biggest ablation hit = dropping storage schedule — promote path must classify fidelity before compress. (7) `explicit_only` Silent — profile attrs must not auto-share. |
| **metric_impact** | LoCoMo/LongMemEval-S Recall+Acc; Build/Infer tokens; latency; per-question-type Acc; five-way ablation. |
| **refine_candidate** | **yes** — S3/S4/S7 typed write schedule (profile/event/record) + selective event sleep-merge + query-budget evidence composition |

---

## 4. Lightweight LLM Agent Memory with Small Language Models
**arXiv:2604.07798** · Zhang, Zhang, Chen, et al. · 2026 · **FULL**  
*(Paper title/system also named “LightMem”; distinct from 2510.18866.)*

| Field | Content |
|-------|---------|
| **arxiv_id** | `2604.07798` |
| **title** | Lightweight LLM Agent Memory with Small Language Models |
| **kedger_stages** | S1, S2, S3, S5, S6, S7 |
| **problem** | Retrieval-only memory is cheap but noisy; LLM-online memory ops are accurate but accumulate latency; need bounded online compute with durable consolidation. |
| **representation** | **STM** = non-persisted context window; **MTM** = user-scoped episodic summaries (embed + time/access stats + user id), capacity \(B=10^4\); **LTM** = de-identified graph knowledge distilled offline (no user ids). Online SLMs: Controller (HQ rewrite + route/budget), Selector (2-stage retrieve), Writer (MTM append/merge). Coarse stage returns **2K** candidates (split across \(n\) HQs), Selector keeps **≤K**; default coarse top-10 NN with MiniLM-384d; LoRA-tuned Selector on 2k (Query,Subgraph,Path) samples. Offline LLM consolidates incremental MTM batches into LTM graph with merge/update/drop + confidence decay. |
| **write_read_forget** | **Write:** SLM-3 → MTM; conflicts via temporal cues + evidence strength; eviction of stale/low-utility at capacity. **Read:** metadata-constrained vector coarse → semantic re-rank to Top-K; concurrent MTM+LTM routing for update-gap. **Forget:** MTM prune; LTM confidence decay / drop of weak candidates. |
| **conflict** | Writer merges repetitive / resolves conflicts with time+evidence strength; offline merge/update/drop. No typed ConflictSet API. |
| **privacy** | **User-identifier isolation** on MTM; LTM deliberately **de-identified / user-agnostic** for cross-user trends. Closest lit signal to Kedger share separation — still not sealed packs. |
| **numbers** | Avg **~+2.5 F1** over A-MEM on LoCoMo. GPT-4o-mini: LightMem multi-hop F1 **28.85** vs A-MEM **27.02**; token length **1,150** vs A-MEM **2,520** vs LoCoMo/MemGPT ~**16.9k**. DialSim GPT-4o-mini: F1 **4.12**, SBERT **23.40** vs A-MEM **3.45 / 19.51**. Latency P50/P95 retrieval **83/167 ms**, e2e **581/1325 ms** vs A-MEM retrieval **856/1583**, e2e **914/3682**. MTM growth DialSim: at 10k entries LightMem F1 **4.12** vs vector-only **3.83** (Δ**0.29**). Error injection: full **4.12/23.40** → cascading failure **1.85/11.20**. Update-gap multi-hop F1: full **28.85**, LTM-only **19.45**, MTM-only **20.12**, MTM noise sat **23.10**. |
| **kedger_lessons** | (1) **SLM online / LLM offline** mirrors Kedger hooks+WorkingState cheap path vs async cognify — keep S1/S2 free of large-model consolidate. (2) Fixed **2K→K** retrieve budget is a concrete S7 packing pattern under `HANDOFF_MAX_BYTES`. (3) Concurrent MTM+LTM retrieval = dual-path L2 episodes + L3 Anchors during update gap (don’t hydrate only promoted Anchors). (4) User-id isolation + de-identified LTM ≈ local store vs shareable facet — reinforce `explicit_only` (never auto-promote personal MTM into shared). (5) Graph LTM + LoRA selector complements `PPR_DAMPING=0.5` walks — semantic filter after vector recall. (6) Capacity \(B=10^4\) + decay = L0/L2 retention pressure akin to `L0_MAX_ROWS` / survival ranking. (7) Measure P50/P95 memory-module latency as first-class SLI. |
| **metric_impact** | LoCoMo F1/BLEU by category + token length; DialSim F1/ROUGE/METEOR/SBERT; P50/P95 latency; MTM-growth stability; error-injection; update-gap ablation. |
| **refine_candidate** | **yes** — S7 two-stage 2K→K semantic re-rank + concurrent MTM/LTM hydrate during consolidate lag |

---

## 5. All-Mem: Agentic Lifelong Memory via Dynamic Topology Evolution
**arXiv:2603.19595** · Lv, Chang, Tao, et al. · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **arxiv_id** | `2603.19595` |
| **title** | All-Mem: Agentic Lifelong Memory via Dynamic Topology Evolution |
| **kedger_stages** | S3, S4, S5, S7, S8 |
| **problem** | Lifelong banks accumulate structural drift (conflation, redundancy, supersession) that crowds fixed retrieve budgets; online reorganization is too expensive; destructive summary/update loses immutable evidence. |
| **representation** | Topology bank \(\mathcal{M}=(\mathcal{V},\mathcal{E})\); unit \(v=\langle c_{\mathrm{immutable}}, s, \mathcal{K}, \mathbf{z}, t, a\in\{0,1\}\rangle\). **Visible surface** \(\mathcal{V}^+=\{a_i=1\}\) is the only coarse-search domain. Edges: temporal \(\mathcal{E}_\tau\), semantic \(\mathcal{E}_\sigma\) (out-degree cap), versioning \(\mathcal{E}_\nu\), sibling \(\mathcal{E}_\beta\); archived units hop-reachable within \(H_N\). **Online:** write unit + sparse Top-\(k\) surface links + id-buffer. **Offline ATC:** parallel LLM diagnose Split/Merge/Update with confidence \(p\ge\theta_{op}\); serial execute Split→Merge→Update; archive by \(a\leftarrow 0\) (non-destructive). **Retrieve:** Stage1 Top-\(k\) anchors on \(\mathcal{V}^+\); Stage2 Expand hop \(H_q\) candidate cap \(L\); Stage3 re-rank; materialize evidence \(c_i\). Defaults \(\theta=0.9\), \(d_\sigma=8\); best sweep \((K,k,L)=(16,10,40)\). |
| **write_read_forget** | **Write:** online lightweight ingest; offline topology edits. **Read:** visible-surface anchors → budgeted typed expansion → evidence attach. **Forget:** visibility archive (not delete); raw \(c_i\) retained; recovery via version/sibling links. |
| **conflict** | **Update** operator = current supersedes predecessor with \(\mathcal{E}_\nu\) link; Merge dedups redundant visible sets; Split disentangles conflation. Confidence-gated; fail-closed applicability checks. |
| **privacy** | Limitations call for privacy-aware retention/deletion as future work. No share ACL. Ethics/limitation only. |
| **numbers** | LoCoMo: All-Mem 4o-J **54.63**, F1 **52.18**, R@5 **46.63**, N@5 **41.02** vs Mem0 **48.91/43.08/38.74/32.13** (+**5.72** 4o-J, +**9.10** F1; +**7.89** R@5 vs Mem0; +**5.24** N@5 vs LightMem). LongMemEval-s: 4o-J **60.20**, F1 **45.19**, R@5/N@5 **94.68/93.27** vs Mem0 **55.80/36.10/90.17/87.14**. Best sweep F1 **45.19** at \((K{=}16,k{=}10,L{=}40)\); Mem0 comparable tok ~**1.4k–2.1k**, A-Mem ~**2.8k–3.5k**. Cost LongMemEval-s: online write **2.38s / 539 tok** per turn; query retrieve **27.54ms / 918 tok**; amortized offline **0.21s / 1237 tok** per turn; ATC event **12.79s / 74.1k tok**. ATC totals: Diagnosis **621k**, Split **12.6k**, Merge **87.9k**, Update **25.1k**, edits **125.6k**, ATC events **8.37k**. Ablation LoCoMo: Full F1 **52.18** / R@5 **46.63** / lat **23.02ms** → No-Visibility **47.63/41.84/34.58ms**; w/o Merge **49.02/43.96**; Anchors-only **49.27/43.19**; No-recovery-links **50.06**. |
| **kedger_lessons** | (1) **Visible-surface memory** = searchable Anchor facet vs full Evidence archive — hydrate Stage1 must not scan all L0/L2. (2) Non-destructive archive (\(a=0\)) + version links = SUPERSEDES with recoverability for S5/S8 why — never overwrite Evidence. (3) Online sparse link + offline ATC = sleep-time merge for graph debt; keep hook path to id-buffer only. (4) Budgets \((k,H_q,L,K)\) are the right S7 knobs alongside `HANDOFF_MAX_BYTES` and notebook/`--walk-budget`; `PPR_DAMPING=0.5` fits hop-bounded expand. (5) Prefer archiving low-`SURVIVAL_RANK` duplicates off the visible surface before pack compile. (6) Measure memory-module ms separately from generator tokens (27.54ms retrieve vs 918 tok inject). (7) `explicit_only` still required — visible≠shareable. |
| **metric_impact** | LoCoMo/LongMemEval-s 4o-J/F1/BLEU/ROUGE + R@5/N@5; F1–token Pareto; \(\theta\)/\(d_\sigma\) sensitivity; online/offline/query cost split; visibility/Merge/expansion ablations. |
| **refine_candidate** | **yes** — S5/S7 visible-surface gating + hop-budget expand from Anchors to archived Evidence + offline Split/Merge/Update consolidate |

---

## Cross-paper performance synthesis (for Kedger)

| Theme | Strongest paper signal | Kedger mapping |
|-------|------------------------|----------------|
| Online/offline split | LightMem soft-insert + OP-update; All-Mem id-buffer + ATC; SLM-LightMem SLM-online/LLM-offline | S1–S2 cheap; S3/S4/S5 async |
| Dual-path evidence+anchors | LeanMem record pointers; Repro LightMem oracle gap (−11.3 Acc); All-Mem immutable \(c_i\) | Evidence bank + Anchor facet; expand on demand |
| Packing budgets | Repro matched ~330/500/935 tok; All-Mem \((K,k,L)\); SLM 2K→K; `HANDOFF_MAX_BYTES=32768` | S7 hydrate Pareto SLIs |
| Visible-surface memory | All-Mem \(\mathcal{V}^+\); No-Visibility hurts F1 (−4.55) and latency | Searchable Anchors ≠ full archive |
| Sleep-time merge | LightMem parallel queues; LeanMem event-only evolution; All-Mem Merge-heavy ATC (87.9k merges) | Offline consolidate; preserve high `SURVIVAL_RANK` |

---

## IDs covered

```
2510.18866
2607.29104
2608.03463
2604.07798
2603.19595
```
