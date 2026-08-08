# P5 — Hydrate / Retrieve (Implementation Clarity)

> **Date:** 2026-08-08  
> **Pillar:** L4 pack compile + ranking + budgets + associative retrieval + hydrate inject  
> **Depends on:** `MEMORY_SCHEMAS_V1.md` §11–14, `OPEN_SOURCE_MEMORY_ARCHITECTURE.md` §9A.5, existing `AGENT_MEMORY_CORPUS_DEEP_READ.md`  
> **Method:** Full-body deep-reads of primary HTML/PDF texts (not abstracts). New papers beyond prior memos are marked ★.

---

## 1. Honesty table

| Bucket | Count | Notes |
|--------|------:|-------|
| **FULL deep-read** (this pillar pass) | **26** | Full extracted bodies; mechanism cards below |
| Substantial / re-used from prior MoDeX memos | 6 | HippoRAG×2, LightRAG, GraphRAG, GenAgents, MemGPT already in AGENT_MEMORY; re-read for hydrate algorithms |
| Abstract / stub | 0 in this memo | Wrong IDs discarded (not counted) |
| **Combined with P6 FULL this session** | **≥48** | See `CORPUS_INVENTORY.md` |

### FULL ledger (P5)

| ID | Paper | Year | ★ new vs prior memos |
|----|-------|------|----------------------|
| 2405.14831 | HippoRAG | 2024 | re-deep (impl) |
| 2502.14802 | HippoRAG 2 | 2025 | re-deep (impl) |
| 2410.05779 | LightRAG | 2024 | re-deep |
| 2404.16130 | GraphRAG | 2024 | re-deep |
| 2304.03442 | Generative Agents | 2023 | re-deep (scoring) |
| 2310.08560 | MemGPT | 2023 | re-deep (paging) |
| 2401.18059 | RAPTOR | 2024 | ★ |
| 2504.18070 | PropRAG | 2025 | ★ |
| 2403.14403 | Adaptive-RAG | 2024 | ★ |
| 2310.11511 | Self-RAG | 2023 | ★ |
| 2305.06983 | FLARE (Active RAG) | 2023 | ★ |
| 2510.10397 | AssoMem | 2025 | ★ |
| 2508.04903 | RCR-Router | 2025 | ★ |
| 2307.03172 | Lost in the Middle | 2023 | ★ |
| 2310.05736 | LLMLingua | 2023 | ★ |
| 2310.06201 | Compressing Context (Selective Context) | 2023 | ★ |
| 2310.04408 | RECOMP | 2023 | ★ |
| 2312.03414 | Compressed Context Memory | 2023 | ★ |
| 2101.06804 | What Makes Good In-Context Examples (KATE) | 2021 | ★ |
| 2402.03367 | RAG-Fusion | 2024 | ★ |
| 2406.14550 | GraphReader | 2024 | ★ |
| 2502.12110 | A-MEM | 2025 | ★ (hydrate angle) |
| 2410.10813 | LongMemEval | 2024 | ★ |
| 2507.05257 | MemoryAgentBench | 2025 | ★ |
| 2402.17753 | LoCoMo | 2024 | ★ |
| 2601.06966 | RealMem | 2026 | ★ |

---

## 2. Mechanism cards (FULL)

### 2.1 Generative Agents (2304.03442) — retrieval score

- **Write:** Memory stream of NL observations; importance ∈ [1,10] at write via LLM poignancy prompt.
- **Read:**  
  \[
  \mathrm{score}=\alpha_r\cdot\mathrm{recency}+\alpha_i\cdot\mathrm{importance}+\alpha_v\cdot\mathrm{relevance}
  \]
  with all \(\alpha=1\) after min-max to [0,1].  
  - Recency = exponential decay over hours since last retrieve, factor **0.995**.  
  - Relevance = cosine(query emb, memory emb).  
  - Top-k that fit context window.
- **Forget/reflect:** Σ importance ≥ 150 → reflection tree (observations → abstractions); reflections re-enter stream.
- **MoDeX:** Direct ancestor of hydrate scoring; Anchors already carry `importance`; add recency + relevance + **kind survival** prior.

### 2.2 MemGPT (2310.08560) — paging under budget

- **Tiers:** Main context = system + working + FIFO queue; external = archival + recall DBs.
- **Control:** LLM function calls page in/out; `request_heartbeat=true` chains multi-step retrieval; overflow alerts trigger eviction writes.
- **MoDeX:** L4 pack = compiled “main context boot”; store = archival. Do **not** give ambient self-page over private tiers without capability (shareable memo). Hydrate is OS-page-in done by MoDeX CLI, not free agent ambient authority.

### 2.3 HippoRAG (2405.14831) — associative single-step multi-hop

- **Index:** LLM OpenIE → schemaless KG (phrase nodes + passage links).
- **Retrieve:** Extract query concepts → Personalized PageRank (PPR) seeded on those nodes → rank passages by node mass. Multi-hop in one retrieval; 10–30× cheaper than iterative IRCoT.
- **MoDeX:** Entity graph + ABOUT/LINKED_TO edges are the hippocampal index. Hydrate expand = bounded PPR / BFS from query entities + hot files, not full-graph dump.

### 2.4 HippoRAG 2 (2502.14802) — passage nodes + recognition memory

- Fixes HippoRAG’s factual-memory regression vs dense RAG.
- **Online:** Embed scores passages **and** triples; LLM **recognition memory** filters irrelevant triples; PPR over phrase+passage nodes; passage reset probs × weight factor.
- Fallback: empty filter → pure dense top passages.
- **MoDeX:** Associative expand must not drown simple “what did we decide?” lookups — always keep dense/lexical path for Anchor statements; graph expand is additive with budget cap.

### 2.5 LightRAG (2410.05779) — dual-level retrieval

- Graph entity/relation extract + vectors; **low-level** (entity/edge precise) vs **high-level** (themes); hybrid mode; incremental updates without full rebuild.
- **MoDeX:** Map low-level → Anchor/entity ABOUT; high-level → episode digests / workstream theme. Pack compile uses both: Anchors first, digests second.

### 2.6 GraphRAG (2404.16130) — community map-reduce

- Index: entities/edges/claims → Leiden communities → community summaries.  
- Query: local search vs global map-reduce over community answers → final answer. Explicitly cites lost-in-the-middle as reason not to stuff raw million-token corpora.
- **MoDeX:** Global community summarization is **too expensive/noisy for v1 handoff** (HippoRAG2 lesson: summaries hurt factual QA). Use community-style only for rare repo-wide sensemaking, never default hydrate.

### 2.7 RAPTOR (2401.18059) — recursive tree

- Embed → cluster → summarize → recurse → tree; retrieve across abstraction levels.
- Strong on multi-step QA; risks summary noise (HippoRAG2).
- **MoDeX:** Episode digests already are one-level RAPTOR leaves→parent. Do not auto-build deep summary trees into L4; optional offline cognify later.

### 2.8 PropRAG (2504.18070) — proposition paths + beam ★

- Replaces lossy triples with **context-rich propositions**; LLM-free online **beam search over proposition paths** for multi-hop chains; SOTA Recall@5 / F1 on 2Wiki/Hotpot/MuSiQue without iterative LLM query rewriting.
- **MoDeX:** Anchor `statement` is already proposition-shaped. Associative retrieval can beam over SUPERSEDES/ABOUT/SUPPORTS paths (beam width 3–5, depth ≤3) instead of free-text IRCoT.

### 2.9 Adaptive-RAG (2403.14403) — complexity router ★

- Classifier over query complexity → **no retrieval / single-step / multi-hop**. Avoids always-on expensive retrieval.
- **MoDeX hydrate modes:**  
  - `boot` (SESSION_START) → always pack HEAD (no classifier).  
  - `query` mid-session → adaptive: entity hit → local expand; multi-hop question → PropRAG-style path; chitchat → skip store retrieval.

### 2.10 Self-RAG (2310.11511) — reflection tokens ★

- Trains LM to emit `Retrieve` / `ISREL` / `ISSUP` / `ISUSE` critique tokens; adaptive on-demand retrieval + passage filtering.
- **MoDeX v1:** Do not train a Self-RAG model. Steal the **control surface**: after candidate retrieve, drop items that fail cheap `ISREL`-like checks (entity overlap / lexical / embedding threshold) before packing.

### 2.11 FLARE (2305.06983) — active forward retrieval ★

- Predict next sentence; if low-confidence tokens → use prediction as query → retrieve → regenerate. Continual retrieve during long generation.
- **MoDeX:** Relevant for long agent turns after hydrate, not for initial pack compile. Optional later: mid-session `modex recall` when agent confidence dips.

### 2.12 AssoMem (2510.10397) — multi-signal fusion ★

- Associative memory graph: utterances ↔ LLM-extracted **clues**.  
- Scores: relevance, importance, temporal alignment.  
- **Fusion:** Conditional MI weights  
  \[
  w^{(d)}(q)=\frac{\exp(\mathrm{CMI}_d(q)/T)}{\sum_{d'}\exp(\mathrm{CMI}_{d'}(q)/T)},\quad
  s(u)=\sum_d w^{(d)}(q)\,s^{(d)}(u)
  \]
- Fixed weights underperform adaptive MI (~4% drop). Sweet spot ≈ **k=6** evidence utterances (more retrieval ≠ more QA).
- **MoDeX:** Adopt multi-signal idea with **fixed interpretable weights for v1** (no CMI training); keep adaptive MI as Phase F+ option. Clues ≈ entities + kind tags.

### 2.13 RCR-Router (2508.04903) — role/stage token budgets ★

- Shared memory store \(M_t\); each agent role \(R_i\) + stage \(S_t\) + budget \(B_i\).  
- Importance \(\alpha(m;R_i,S_t)\) from semantic + lexical + **recency decay**; greedy fill until token budget (knapsack; optimal if uniform item sizes).  
- Cuts tokens ~25–47% vs full-context routing.
- **MoDeX:** Pack compile **is** a router with roles: `boot_agent`, `human_handoff`, `ci_bot`. Different budgets + facet policies per role.

### 2.14 Lost in the Middle (2307.03172) — pack layout ★

- U-shaped use of context: primacy + recency strong; **middle collapses**. Explicit long-context models still fail.
- **MoDeX packing law:** Place survival-critical Anchors at **start**; WorkingState + next_step at **end**; episode digests/evidence in middle only if budget remains. Never bury active constraints mid-pack.

### 2.15 Packing / compression literature ★

| Paper | Mechanism | MoDeX steal |
|-------|-----------|-------------|
| LLMLingua (2310.05736) | Perplexity-based iterative token drop under budget | Optional compress of episode digests only — **never** compress Anchor statements |
| Selective Context (2310.06201) | Drop low self-information tokens | Same: digests/evidence only |
| RECOMP (2310.04408) | Compress retrieved docs; selective augmentation | Pre-pack: if evidence selected, compress snippet to ≤280 chars (schema) |
| Compressed Context Memory (2312.03414) | Online compress for interactive LMs | WorkingState already ≤4 KiB; keep |

### 2.16 ICL-with-memory (2101.06804 KATE) ★

- Good in-context exemplars = nearest neighbors in embedding space (not random).  
- **MoDeX:** When hydrating few-shot style reminders (e.g. prior similar decisions), retrieve by embedding to current goal/files — not FIFO.

### 2.17 RAG-Fusion (2402.03367) ★

- Multi-query generation + Reciprocal Rank Fusion.  
- **MoDeX query hydrate:** Expand user/agent question into 2–3 rewrite queries; RRF over Anchor hits before budget cut.

### 2.18 GraphReader (2406.14550) ★

- Agent explores graph with notes; fine-grained page-in.  
- Complements MemGPT: exploration policy for large graphs. MoDeX v1 uses bounded expand, not free agent walk (cost + Inv-Scope).

### 2.19 A-MEM (2502.12110) ★

- Zettelkasten-like notes with links; agentic memory evolution.  
- Supports LINKED_TO / associative recall patterns already in MoDeX edge types.

### 2.20 Eval suites (hydrate acceptance) ★

| Bench | What it stresses for MoDeX |
|-------|----------------------------|
| **LongMemEval** (2410.10813) | Multi-session recall; abstention; knowledge updates |
| **MemoryAgentBench** (2507.05257) | Accurate retrieval, test-time learning, long-range understanding, **selective forgetting** / conflict |
| **LoCoMo** (2402.17753) | Very long multi-turn; temporal + multi-hop |
| **RealMem** (2601.06966) | Real-world memory-driven interaction realism |

**Eval implication:** Hydrate quality ≠ Recall@k alone. Must score: constraint survival under 8 KiB budget, supersession freshness, no private bleed, selective forget after unshare.

---

## 3. Synthesis → MoDeX hydrate architecture

```text
candidates = store_slice(workstream) ∪ opt_in_shared_facet
candidates = InvScope_filter(principal, candidates)          # P6 — every path
candidates = temporal_resolve(active_first, supersedes)      # invalidate losers
expanded  = associative_expand(candidates, query, budget_expand)
scored    = score(expanded, query, now)                      # §4 formula
packed    = pack_under_budget(scored, role_budget)           # §5 drop order
layout    = primacy_recency_layout(packed)                   # lost-in-middle
inject    = render_ephemeral(layout) → agent context
```

---

## 4. MoDeX implementation recipe — hydrate ranking formula

### 4.1 Recommended scoring formula (v1 lock proposal)

Let each candidate item \(x\) (Anchor / WorkingState field / Episode digest / Evidence) have:

| Signal | Definition | Range |
|--------|------------|-------|
| \(K(x)\) | Kind survival prior | see table |
| \(I(x)\) | `importance` (Anchors) or derived | [0,1] |
| \(R_{\mathrm{time}}(x)\) | Recency | [0,1] |
| \(R_{\mathrm{sem}}(x)\) | Semantic relevance to query/goal | [0,1] |
| \(A(x)\) | Associative expand bonus | [0,1] |
| \(V(x)\) | Visibility/capability admissibility | {0,1} |

**Kind prior \(K\) (survival rank, schemas §4):**

| kind | \(K\) |
|------|------:|
| constraint | 1.00 |
| rejection | 0.95 |
| decision | 0.90 |
| goal | 0.70 |
| next_step | 0.65 |
| open_question | 0.40 |
| gotcha | 0.35 |
| episode_digest | 0.25 |
| evidence | 0.15 |
| working_blob | 0.80 (always include if fits) |

**Recency** (GenAgents-style, half-life friendly):

\[
R_{\mathrm{time}}(x)=\exp\big(-\lambda\cdot\Delta t_{\mathrm{hours}}(x)\big),\quad \lambda=\ln(2)/H
\]

Defaults: Anchors \(H=72\mathrm{h}\); episodes \(H=24\mathrm{h}\); evidence \(H=12\mathrm{h}\).  
(GenAgents used 0.995/game-hour ≈ slow decay; engineering handoffs need faster episode decay.)

**Relevance:**

\[
R_{\mathrm{sem}}(x)=\max\big(\cos(e_q,e_x),\;\mathrm{jaccard}(\mathrm{entities}_q,\mathrm{about}_x),\;\mathbf{1}[\mathrm{file\ overlap}]\big)
\]

Query \(q\) for `boot` hydrate = WorkingState.goal + hot files + branch name.  
For `query` hydrate = user/agent utterance (+ optional RAG-Fusion rewrites, RRF).

**Associative bonus** (HippoRAG/PropRAG/AssoMem):

\[
A(x)=\min\big(1,\;\beta\cdot\mathrm{PPR\_mass}(x)+\gamma\cdot\mathbf{1}[\mathrm{beam\_path\_hit}]\big)
\]

with expand capped: max **12** graph nodes, depth ≤ **2**, beam width **3**.

**Hard gate:**

\[
V(x)=\mathbf{1}[\mathrm{InvScope}(\mathrm{principal},x)]
\]

If \(V=0\), drop (404 semantics; never score).

**Final score:**

\[
\boxed{
S(x)=V(x)\cdot\Big(
w_K K(x)+w_I I(x)+w_t R_{\mathrm{time}}(x)+w_s R_{\mathrm{sem}}(x)+w_A A(x)
\Big)
}
\]

**v1 weights (interpretable, AssoMem-inspired but fixed):**

| Weight | Value | Rationale |
|--------|------:|-----------|
| \(w_K\) | **0.35** | Engineering continuity = kind survival first |
| \(w_I\) | **0.20** | Explicit importance / Tier signals |
| \(w_t\) | **0.15** | Recency (stronger for episodes via \(H\)) |
| \(w_s\) | **0.20** | Task relevance |
| \(w_A\) | **0.10** | Associative expand — helpful, not dominant |

Sort by \(S\) descending; stable-tiebreak: kind rank → `updated_at` → `id`.

**Active constraints/rejections/decisions** with `status=active` get \(K\) floor + **must-keep set** \(M\): they are never dropped while budget remains (schemas §14).

---

## 5. MoDeX implementation recipe — drop order + pack budgets

### 5.1 Size budgets (align schemas §14; role variants from RCR-Router)

| Role / facet | `max_bytes` | Episodes | Evidence | Shared facet |
|--------------|------------:|---------:|---------:|--------------|
| `boot_agent` (default) | **32768** | 1–3 | 0–4 | opt-in ranked ≤8 KiB |
| `human_handoff` | 49152 | 2–3 | ≤6 | opt-in |
| `ci_bot` (attenuated) | 8192 | 0–1 | 0 | shared constraints only |
| `extreme` (context pressure) | 8192 | 0 | 0 | must-keep Anchors + L1 only |

WorkingState target ≤ **4 KiB**. Anchor statement ≤240 / reason ≤480.

### 5.2 Drop order (when `used_bytes > max_bytes`)

Exact priority (lowest survival dropped first):

1. Raw L0 observations (never in pack)  
2. Evidence snippets (highest index first / lowest \(S\))  
3. Older episode digests (keep newest 1)  
4. `gotcha` Anchors  
5. `open_question` Anchors  
6. Low-\(S\) `next_step` / stale `goal` duplicates  
7. Associative-expanded Anchors not in must-keep / not ABOUT hot files  
8. Shared-facet Anchors (opt-in set shrinks before private workstream must-keep)  
9. **Never drop** active `constraint` / `rejection` / `decision` while bytes remain  
10. If still over: truncate episode summary to 500 chars; then WorkingState notes field; emit `budget.dropped[]`

Record every drop in `HandoffPack.budget.dropped`.

### 5.3 Primacy/recency layout (Lost-in-the-Middle)

```text
[HEADER meta]
[MUST-KEEP anchors: constraints → rejections → decisions]   # START
[other anchors by S]
[episode digests]                                            # MIDDLE
[evidence if any]
[WorkingState: goal, next_step, hot files]                   # END
[budget audit]
```

### 5.4 Associative expand algorithm (v1)

```text
function associative_expand(seeds, query_entities, B_expand):
  frontier = seeds ∪ anchors_about(query_entities)
  # PropRAG-style beam on edges: SUPERSEDES, ABOUT, SUPPORTS, LINKED_TO, CONTRADICTS
  paths = beam_search(frontier, width=3, depth=2, score=edge_weight * sem_sim)
  # HippoRAG-style: optional PPR on entity subgraph if |E| < 5k
  extras = top_nodes(paths ∪ ppr_mass, limit=12)
  return InvScope_filter(extras)
```

Anti-pattern: GraphRAG global community dump into every pack (cost + noise + PRISM amplification).

### 5.5 Compile pseudocode

```python
def compile_handoff(ws, principal, role="boot_agent", query=None):
    assert has_capability(principal, ws, "read_hydrate")  # or recipient seal path
    budget = ROLE_BUDGETS[role]
    q = query or working_state_query(ws)

    cands = load_active_anchors(ws) + load_working(ws) + load_recent_episodes(ws, k=5)
    cands += load_shared_facet(ws, opt_in=True)  # ranked, separate sub-budget
    cands = [x for x in cands if inv_scope(principal, x)]
    cands = resolve_supersession(cands)  # active winners only

    expanded = associative_expand(cands, entities(q), B_expand=12)
    scored = sorted(expanded, key=lambda x: S(x, q), reverse=True)

    pack = PackBuilder(max_bytes=budget.max_bytes)
    # must-keep first
    for x in must_keep(scored):
        pack.try_add(x)
    for x in scored:
        if x in pack: continue
        if not pack.try_add(x):
            pack.record_drop(x)
    pack.apply_layout_primacy_recency()
    pack.content_hash = sha256(canonical_json(pack.payload))
    return pack  # then seal → .mxp (P6)
```

---

## 6. Anti-patterns (do not copy)

| Anti-pattern | Source | Why bad for MoDeX |
|--------------|--------|-------------------|
| Always full-context to every agent | RCR-Router baselines | Token burn + leakage surface |
| Summary-only memory as sole store | RAPTOR/GraphRAG failure modes (HippoRAG2) | Factual/decision drift |
| Relevance-only retrieval | AssoMem | Fails similarity-dense engineering logs |
| Unbounded graph expand on id | Graph ACL / MAMA | Inference + hub leakage |
| Put critical Anchors in middle of prompt | Lost-in-the-Middle | Model ignores them |
| Compress Anchor statements with LLMLingua | packing papers | Corrupts judgments |
| Ambient MemGPT self-page across principals | MemGPT + shareable memo | Confused deputy |
| Train Self-RAG / CMI fusion for v1 | Self-RAG / AssoMem | Heavy; fixed weights suffice |

---

## 7. Open risks

1. Exact \(\lambda\) / half-lives need online tuning against LongMemEval + internal handoff traces.  
2. PPR cost on large monorepos — may need entity sharding per workstream.  
3. Adaptive-RAG classifier for mid-session recall not specified for engineering intents.  
4. Interaction of pack deputy (shared facet) with ranking — see P6.  
5. MemoryAgentBench selective-forgetting: hydrate cache invalidation SLA after supersession/unshare.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-08-08 | Initial P5 implementation memo from 26 FULL deep-reads + MoDeX recipes. |
