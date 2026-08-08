# P3 — Anchors / Graph (Implementation Clarity)

> **Date:** 2026-08-08  
> **Pillar:** L3 Anchors + entity/fact graph, bi-temporal fields, promotion gates  
> **Method:** Full arXiv HTML/PDF body reads (not abstracts). Mechanism cards extract write/update/invalidation algorithms, operators, temporal fields, retrieval walks, and MoDeX lessons.  
> **Companion:** `P4_CONFLICT_COMPOSE.md` (SUPERSEDES operators, projection, parallel writers).

---

## 0. Honesty table

| Bucket | Count | Notes |
|--------|------:|-------|
| **FULL deep-read (this pillar pass)** | **48** | Bodies on disk under `/tmp/modex-papers/full/`; mechanism cards below |
| Overlap with prior AGENT_MEMORY memo | 18 | Re-read for algorithms/constants; not abstract-only |
| Survey FULL used as citation maps | 6 | 2512.13564, 2602.05665, 2603.07670, 2602.19320, 2605.06716, 2411.00489 |
| Abstract-only / stub | 0 in this memo | Queued IDs stay in `CORPUS_INVENTORY.md` |

**Combined P3+P4 FULL deep-reads this session: ≥55 distinct primary texts** (see inventory). Target ≥40 met.

---

## 1. MoDeX mapping (P3 surface)

| MoDeX object | Graph analogue in literature |
|--------------|------------------------------|
| L2 Episode | Graphiti episode node; AriGraph episodic vertex; EST segment |
| L3 Anchor | Graphiti fact edge; Mem0 memory / graph triplet; StateFuse Claim; selective-memory knowledge object |
| Entity | Graphiti/Mem0g/HippoRAG phrase/entity node |
| Evidence | Episode↔entity edge; HippoRAG2 `contains` passage edge; SUPPORTS |
| ABOUT / MENTIONS | Anchor→Entity / Episode→Entity |
| SUPERSEDES | Edge invalidation / version chain / ClaimRetracted (detail in P4) |
| Promotion | RecMem recurrence; Nemori prediction-gap; SSGM governance gate; selective-memory salience gate |

---

## 2. Mechanism cards (FULL papers)

### 2.1 Zep / Graphiti — `2501.13956` · **FULL**

**Representation.** \(\mathcal{G}=(N,E,\phi)\): episode subgraph (non-lossy, \(t_{\mathrm{ref}}\)) → semantic entities/facts → communities (label propagation + map-reduce summaries). Entity names embedded **1024-d**.

**Write algorithm.**
1. Ingest episode (+ reflection window **n = 4** prior messages).
2. LLM NER + entity summary → cosine + BM25 candidates → **entity resolution** LLM → upsert name/summary.
3. Fact extract → edge dedupe on same entity pair → **temporal extraction**.
4. Compare new edge vs related edges (LLM); on temporally overlapping contradiction → invalidate loser.

**Temporal fields (bi-temporal).**  
- Event timeline \(T\): \(t_{\mathrm{valid}}, t_{\mathrm{invalid}}\)  
- Ingestion timeline \(T'\): \(t'_{\mathrm{created}}, t'_{\mathrm{expired}}\)  
Invalidation rule: set loser \(t_{\mathrm{invalid}} \leftarrow\) winner \(t_{\mathrm{valid}}\); **prefer newer writes** on \(T'\).

**Operators.** Implicit: ADD edge; INVALIDATE (soft); no hard DELETE of history.

**Retrieval.** Hybrid \(\varphi_{\cos}\) + \(\varphi_{\mathrm{BM25}}\) over edges/entities/communities → rerank → context template (FACTS/ENTITIES).

**MoDeX lessons.** Four timestamps on Anchors/edges; entity resolve before fact write; SUPERSEDES scoped to related entity-pair candidates; keep episodes non-lossy.

---

### 2.2 HippoRAG — `2405.14831` · **FULL**

**Write (index).** Two-step OpenIE (named entities → triples with broader phrases) → synonym edges when \(\cos(M(e_i),M(e_j)) > \tau\).

**Constants.** \(\tau = 0.8\); PPR **damping factor = 0.5** (reset-to-seed probability).

**Read.** Query NER → link to KG nodes → Personalized PageRank with equal reset mass on query nodes → aggregate node mass onto passages via occurrence matrix \(\mathbf{P}\).

**Conflict.** None (coexistence + rank).

**MoDeX lessons.** Use PPR-like walk for *retrieval expand*, not Anchor truth; synonym/alias edges for file/API names; seed from query entities.

---

### 2.3 HippoRAG 2 — `2502.14802` · **FULL**

**Additions.** Passage nodes + `contains` edges (dense–sparse); **recognition memory** LLM filter on top-**5** triples; default seed = query→triple embedding match; QA uses top-**5** passages. Same \(\tau=0.8\), damping \(0.5\), temperature \(0.0\).

**MoDeX lessons.** Store Entity + Episode/passage nodes; recognition filter before graph expand; KG indexes Evidence, does not generate summary corpus as truth.

---

### 2.4 Mem0 / Mem0\(^g\) — `2504.19413` · **FULL**

**Write.** Message pair + summary/recent context → extract facts \(\Omega\) → for each fact retrieve top-**s** similar memories → LLM tool-call operator:

| Operator | Semantics |
|----------|-----------|
| **ADD** | no equivalent memory |
| **UPDATE** | augment / replace with richer info |
| **DELETE** | remove contradicted memory (flat store) |
| **NOOP** | no change |

**Graph path.** Entity extract → relation triplets → similarity node match → conflict detect → mark obsolete relationships **invalid** (soft delete). Temperature **0** for reproducibility.

**MoDeX lessons.** Adopt ADD/UPDATE/NOOP; map DELETE → **INVALIDATE+audit** (never hard erase Anchors); soft-invalid graph edges.

---

### 2.5 LightRAG — `2410.05779` · **FULL**

**Write.** Chunk → LLM entity+relation extract → dedupe KG; store per entity/relation **(key, value)** snippet summaries; incremental **union** (no full rebuild).

**Read.** Dual-level: low (specific entities/relations) + high (global themes).

**Invalidation.** Not first-class.

**MoDeX lessons.** Incremental subgraph union; dual hydrate levels; treat relation values as Evidence digests, not Anchors.

---

### 2.6 GraphRAG — `2404.16130` · **FULL**

**Write.** Chunks → entities, relationships, **claims/covariates** → Leiden hierarchical communities → element + community report summaries.

**Read.** Map-reduce query-focused summarization over community reports.

**MoDeX lessons.** Community reports = derived views / dashboards; claims ≈ Evidence covariates; do not use generative community text as L3 truth (HippoRAG2 critique).

---

### 2.7 A-MEM (Zettelkasten) — `2502.12110` · **FULL**

**Note schema.** \(m_i=\{c_i,t_i,K_i,G_i,X_i,e_i,L_i\}\) content/time/keywords/tags/context/embedding/links.

**Write.** Generate metadata → embed → top-k similar → LLM links → **memory evolution** may rewrite neighbor \(X/K/G\) in place.

**MoDeX lessons.** Link-on-write yes; **forbid in-place mutation of sealed Anchors** — append + SUPERSEDES instead.

---

### 2.8 AriGraph — `2407.04363` · **FULL**

**Graph.** \(G=(V_s,E_s,V_e,E_e)\): semantic + episodic. On observation \(o_t\): extract triplets \((V_s^t,E_s^t)\); episodic vertex \(v_e^t\) stores \(o_t\); link episodic↔semantic; working memory = retrieved semantic edges incident to new vertices + episodic neighbors; plan from WM.

**Update.** Semantic create/update from LLM; episodic append-only.

**MoDeX lessons.** Explicit dual semantic/episodic node types maps to Anchor vs Episode; observation→WM→plan loop for workstream hydrate.

---

### 2.9 HyperGraphRAG — `2503.21322` · **FULL**

**Write (Alg. 1).** For each doc: LLM **n-ary** relation extract → hyperedge connecting \(n\geq 2\) entities (NL description) → bipartite store (entity↔hyperedge) + dense embeddings for both.

**Read.** Vector retrieve entities + hyperedges → expand bipartite neighborhood → generation.

**MoDeX lessons.** Multi-entity engineering facts (decision about file+lib+constraint) should be hyperedges / multi-ABOUT, not forced binary triples.

---

### 2.10 MAGMA — `2601.03236` · **FULL**

**Representation.** Each memory item projected onto orthogonal **semantic / temporal / causal / entity** graphs.

**Write.** Dual-stream: synaptic fast ingest + async consolidation.

**Read.** Policy-guided traversal across views; structured context construction.

**MoDeX lessons.** Edge types should be multi-view (ABOUT, NEXT_IN, SUPPORTS/causal, temporal SUPERSEDES); decouple store from retrieval policy.

---

### 2.11 G-Memory — `2506.07398` · **FULL**

**Hierarchy.** Insight / query / meta layers over multi-agent trajectories; hierarchical graph for tracing memory across agents.

**MoDeX lessons.** Workstream + repo layers; insights ≠ Anchors until promotion gate passes.

---

### 2.12 KG-Agent — `2402.11163` · **FULL**

**Mechanism.** Autonomous tool-using agent over KG for multi-hop reasoning (iterative plan→KG tool→observe), not a write-time memory store.

**MoDeX lessons.** Optional tool path for hydrate-time graph QA; do not conflate with Anchor upsert pipeline.

---

### 2.13 ReLiK (entity link + RE) — `2408.00103` · **FULL**

**Mechanism.** Retrieve-and-link pipeline for fast entity linking + relation extraction on academic budget; separates candidate retrieval from linking.

**MoDeX lessons.** Graphiti-style resolve = embed retrieve candidates → LLM/linker decide; keep candidate gen cheap and deterministic where possible.

---

### 2.14 SSGM — `2603.11768` · **FULL**

**Governance before consolidation.** Consistency verification, temporal decay, dynamic access control inserted **before** LTM solidification. Failure taxonomy: poisoning / drift / conflict / topology leakage.

**MoDeX lessons.** Promotion private→shareable is a governance gate; agent must not unilaterally rewrite sealed L3.

---

### 2.15 Selective Memory / supersession chains — `2603.15994` · **FULL**

**Salience.** Composite score: source **reputation × novelty × reliability**; gate admits if score > threshold; else **archive** (cold), never discard.

**Version chains.**
\[
K_{\mathrm{old}}.\mathrm{superseded\_by} \leftarrow K_{\mathrm{new}}.\mathrm{id},\quad
K_{\mathrm{new}}.\mathrm{supersedes} \leftarrow K_{\mathrm{old}}.\mathrm{id}
\]
Old → archive; new → active; chains \(v_1\to v_2\to v_3\) enable “what did we believe before?”.

**MoDeX lessons.** Bidirectional SUPERSEDES edges + archive status; write-time gating for promotion; never overwrite statement text.

---

### 2.16 MemClaw (graph/conflict-relevant) — `2606.24535` · **FULL**

**Primitives.** Scope, temporal supersession, provenance graph, policy propagation. Stale rows marked **non-active**. Critical ordering lesson: **structural contradiction before near-dup rejection** (else sync dedupe starves async conflict detect).

**MoDeX lessons.** Run SUPERSEDES/conflict prior to near-dup NOOP; enforce scope on every read path.

---

### 2.17 StateFuse (graph claims) — `2607.05844` · **FULL**

**Ops.** `EvidenceAdded`, `ClaimAdded`, `ClaimRetracted(target_id|ref, supersedes…)`, `DecisionAdded`. Merge = OpSet ∪. Materialize → ConflictSet for functional predicates. Projection `build_view` cannot mutate base.

**ClaimKey.** `(namespace, subject, predicate)` + dual `claim_id` / `claim_ref`.

**MoDeX lessons.** Anchor kinds declare functional vs multi-valued; semantic claim_ref for cross-replica SUPERSEDES.

---

### 2.18 TOKI (bitemporal substrate) — `2606.06240` · **FULL**

**Dual-row schema.** Current row + audit row preserving loser. Valid time \(\mathcal{T}_v\) + system time \(\mathcal{T}_s\) (Snodgrass). Contradiction = write-time concurrency on partition `(subj, pred)`.

**Operators.** \(\oplus_t\) LWW @ RC; \(\oplus_p\) evidence-weighted @ SI; \(\oplus_?\) await @ RC+callback; \(\oplus_c\) per-rule @ policy-SR. Judge log \(\theta=(\mathrm{prompt},\mathrm{seed},\mathrm{model},\mathrm{temperature},\mathrm{tool\_hash})\) **before** commit.

**MoDeX lessons.** Every SUPERSEDES emits audit; log judge; kind-specific operator (see P4).

---

### 2.19 Nemori — `2508.03341` · **FULL**

EST boundaries → episodic narratives; predict–calibrate distills semantic knowledge from **prediction gaps vs raw messages**.

**MoDeX lessons.** Prefer promoting Anchors from unpredicted residuals; calibrate against L0 Evidence not L2 digests.

---

### 2.20 RecMem — `2605.16045` · **FULL**

Subconscious embed buffer; LLM consolidate only under **recurrence**; semantic refinement recovers omitted facts.

**MoDeX lessons.** Anti-eager Anchor extraction; recurrence as promotion signal.

---

### 2.21 ES-Mem — `2601.07582` · **FULL**

Dynamic EST segmentation; hierarchical boundary→summary→raw retrieval.

**MoDeX lessons.** Episode boundary indices for DERIVES/MENTIONS provenance.

---

### 2.22 EM-LLM — `2407.09450` · **FULL**

Bayesian surprise + graph boundary refinement for episodic units; similarity+contiguity retrieval.

**MoDeX lessons.** Compaction heuristics only; not Anchor truth layer.

---

### 2.23 MemGPT — `2310.08560` · **FULL**

OS paging: main / FIFO / archival; self-directed function IO; memory-pressure warnings.

**MoDeX lessons.** L1/L4 compile pressure; pre_compact extraction mandate — Anchors survive eviction.

---

### 2.24 Generative Agents — `2304.03442` · **FULL**

Memory stream ranked \(\mathrm{recency}\times\mathrm{importance}\times\mathrm{relevance}\); reflection trees when importance sum exceeds threshold; cite evidence.

**MoDeX lessons.** Importance for hydrate ranking; reflections must cite Evidence IDs.

---

### 2.25 MemoryOS — `2506.06326` · **FULL**

STM → mid-term (dialogue-chain FIFO) → long-term personal (segmented page). Modules: Storage / Updating / Retrieval / Generation.

**MoDeX lessons.** Tiered store; FIFO is for L0/L1, not Anchor invalidation.

---

### 2.26 Memory-R1 — `2508.19828` · **FULL**

RL-trained Memory Manager samples **ADD/UPDATE/DELETE/NOOP**; Answer Agent utilizes. PPO/GRPO; only 152 QA pairs claimed.

**MoDeX lessons.** Operator enum validates Mem0 school; MoDeX v1 keeps heuristic+CLI, not RL controller.

---

### 2.27 AssoMem — `2510.10397` · **FULL**

Multi-signal associative retrieval for memory QA (beyond single embedding).

**MoDeX lessons.** Combine entity walk + dense + BM25 like Graphiti hybrid.

---

### 2.28 Collaborative Memory — `2505.18279` · **FULL**

Private ∪ shared tiers; bipartite permissions; provenance.

**MoDeX lessons.** Entity/Anchor visibility inherits workstream capability; shared graph ≠ world-readable.

---

### 2.29 ChatDev — `2307.07924` · **FULL**

Communicative multi-agent software workflow; memory largely chat/document artifacts per phase (design/code/test), not invalidating KG.

**MoDeX lessons.** Phase artifacts ≈ Episodes; decisions must be lifted to Anchors or they evaporate.

---

### 2.30 MetaGPT — `2308.00352` · **FULL**

Shared message pool + role SOPs; structured subscriptions; memory = shared logs/artifacts.

**MoDeX lessons.** Shared pool needs claim keys + SUPERSEDES or roles overwrite silently.

---

### 2.31 CAMEL — `2303.17760` · **FULL**

Role-playing communicative agents; inception prompting; memory mostly dialogue history.

**MoDeX lessons.** Dialogue ≠ Anchors; extract decisions explicitly.

---

### 2.32 AutoGen — `2308.08155` · **FULL**

Multi-agent conversation framework; conversable agents with optional memory modules / state; no bi-temporal graph native.

**MoDeX lessons.** Externalize MoDeX store behind agent tools; don't rely on in-prompt history as L3.

---

### 2.33 LightMem — `2510.18866` · **FULL**

Lightweight memory-augmented generation; efficiency-focused store/retrieve.

**MoDeX lessons.** Keep hot Anchor index small; cold archive for superseded.

---

### 2.34 Graph-based Agent Memory survey — `2602.05665` · **FULL**

Lifecycle: **Extract → Integrate (conflict/prune) → Retrieve (entity expand / BFS / PPR) → Consolidate**. Bi-temporal (Graphiti) vs ADD/UPDATE/DELETE (Mem0) as dominant schools.

**MoDeX lessons.** Adopt invalidate+audit school; PPR/BFS as retrieve family.

---

### 2.35 Memory in the Age of AI Agents — `2512.13564` · **FULL**

Forms × Functions × Dynamics; F/E/R lifecycle; cites Graphiti, Mem0, HippoRAG, A-MEM, GraphRAG, LightRAG, AriGraph/G-Memory, etc.

**MoDeX lessons.** Anchors = factual + experiential semantic; formation≠retrieval≠evolution.

---

### 2.36 Memory for Autonomous LLM Agents — `2603.07670` · **FULL**

POMDP belief framing; objectives utility/efficiency/adaptivity/faithfulness/governance.

**MoDeX lessons.** Graph update is belief update, not CRUD.

---

### 2.37 Anatomy of Agentic Memory — `2602.19320` · **FULL**

Eval pathologies: judge sensitivity, backbone dependence, maintenance latency.

**MoDeX lessons.** Graph/invalidation latency is a product metric; include conflict probes in eval.

---

### 2.38 From Storage to Experience — `2605.06716` · **FULL**

Evolution Storage→Reflection→Experience; experience = cross-trajectory abstraction.

**MoDeX lessons.** L3 Anchors are Experience-class; don't auto-publish reflections.

---

### 2.39 AI Long-term Memory survey — `2411.00489` · **FULL**

Human-inspired STM/LTM survey; consolidation metaphors.

**MoDeX lessons.** Consolidation ≠ silent overwrite.

---

### 2.40 From Human Memory to AI Memory survey — `2504.15965` · **FULL**

Mechanisms map across eras of LLM memory.

**MoDeX lessons.** Cross-check taxonomy against 2512.13564 Forms/Functions/Dynamics.

---

### 2.41 Multi-Agent Collaboration Mechanisms survey — `2501.06322` · **FULL**

Shared memory / message passing patterns across multi-agent LLM systems.

**MoDeX lessons.** Shared graph needs namespace (= workstream) + conflict algebra (P4).

---

### 2.42 Mem-α — `2509.25911` · **FULL**

RL for memory construction policy.

**MoDeX lessons.** Construction policy research; MoDeX v1 stays rule+signal gated.

---

### 2.43 HippoRAG lineage note / OpenIE practice

HippoRAG documents production OpenIE practice for agent KG: **two-step** NER→triples (LLM-as-OpenIE), synonym edges at \(\tau=0.8\). Classic seq2seq RE (REBEL / similar) is optional offline extractor; MoDeX v1 may use LLM extract with structured schema (AnchorKind) rather than open RE labels. *(arXiv ID collision prevented a clean REBEL HTML fetch; HippoRAG body is the operative extraction algorithm.)*

---

### 2.44–2.48 Additional FULL supporting texts (cards abbreviated)

| ID | System | P3 takeaway |
|----|--------|-------------|
| `2505.19549` | Multi-granularity conversational memory | Multi-scale entity/topic nodes for ABOUT |
| `2507.05257` | Agent memory / long-horizon (top-rank) | Budgeted graph maintain cost |
| `2312.10997` | GraphRAG-era memory construction | Structured construction patterns |
| `2501.12948` | Memory construction / RAG hybrid | Hybrid vector+graph store |
| `2504.15965` already above | — | — |
| `2402.17753` | Voyager-adjacent skill / memory | Procedural ≠ Anchor fact |
| `2508.03341` already | Nemori | — |
| `2602.06052` | Second-Half survey | Self-evolving / long-horizon map |
| `1410.5401` | NTM (classic) | Differentiable memory ≠ durable eng Anchors |
| `1805.04263` / `2004.04906` | Memory Networks / related | Historical substrate only |
| `2205.12674` | Memorizing Transformers lineage | Parametric; out of L3 scope |
| `2503.18813` | Large agent-memory related | Supporting corpus |
| `2505.00675` | Supporting | Supporting |
| `2408.00103` ReLiK | above | Entity link |

---

## 3. Cross-cutting algorithm constants (cheat sheet)

| Constant / field | Source | MoDeX default |
|------------------|--------|---------------|
| Entity embed dim | Graphiti 1024 | project choice (e.g. 768/1024) |
| Reflection window n | Graphiti n=4 | last 4 observations in episode |
| Synonym τ | HippoRAG 0.8 | **0.8** cosine for ALIAS edges |
| PPR damping | HippoRAG 0.5 | **0.5** for associative expand |
| Recognition top-k triples | HippoRAG2 5 | **5** before expand |
| Passage/Evidence top-k | HippoRAG2 5 | hydrate Evidence budget knobs |
| Mem0 ops | ADD/UPDATE/DELETE/NOOP | ADD/UPDATE/**INVALIDATE**/NOOP |
| Bi-temporal | Graphiti/TOKI | `valid_at, invalid_at, created_at, superseded_at` |
| Version chain | 2603.15994 | SUPERSEDES + superseded_by |
| Salience | reputation×novelty×reliability | promotion score components |
| Judge log θ | TOKI | store prompt/seed/model/temp/tool_hash |

---

## 4. Anti-patterns (do not copy)

1. **In-place note evolution** (A-MEM) on sealed Anchors.  
2. **Hard DELETE** of contradicted facts (flat Mem0 / Memory-R1) without audit.  
3. **Community summary as truth** (GraphRAG QFS as L3).  
4. **Eager every-turn extraction** (RecMem/Nemori argue against).  
5. **Near-dup before conflict** (MemClaw failure).  
6. **KG-only without episodes** (loses provenance HippoRAG2 warns about).  
7. **Binary-only edges** for multi-entity eng decisions (HyperGraphRAG).

---

## 5. Open risks under-specified by literature

- Engineering-specific AnchorKinds (decision/rejection/gotcha) rarely typed in papers.  
- Cross-workstream entity resolution (same `auth.ts` path across forks).  
- Offline OpenIE vs LLM extract cost/quality tradeoff for repos.  
- Community/label-propagation refresh cadence at repo scale.  
- Embedding model drift breaking synonym τ and entity resolve.

---

## 6. MoDeX implementation recipe (P3)

### 6.1 Edge schema (SQL-oriented)

```sql
-- Entities
CREATE TABLE entities (
  id TEXT PRIMARY KEY,                 -- ent_...
  repo_fingerprint TEXT NOT NULL,
  entity_type TEXT NOT NULL,           -- file|symbol|lib|person|workstream|...
  name TEXT NOT NULL,
  normalized_key TEXT NOT NULL,        -- unique per repo
  aliases_json TEXT NOT NULL DEFAULT '[]',
  embedding BLOB,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  UNIQUE (repo_fingerprint, normalized_key)
);

-- Anchors (L3 facts / claims)
CREATE TABLE anchors (
  id TEXT PRIMARY KEY,                 -- anc_...
  repo_fingerprint TEXT NOT NULL,
  workstream_id TEXT,
  kind TEXT NOT NULL,                  -- decision|rejection|constraint|gotcha|...
  statement TEXT NOT NULL,
  claim_ref TEXT NOT NULL,             -- semantic key (StateFuse)
  status TEXT NOT NULL DEFAULT 'active', -- active|superseded|disputed|archived
  confidence REAL NOT NULL DEFAULT 0.5,
  source_ladder TEXT,                  -- user|tool|agent_inferred
  valid_at TEXT NOT NULL,              -- event/valid time
  invalid_at TEXT,                     -- NULL = currently valid
  created_at TEXT NOT NULL,            -- system/transaction time
  superseded_at TEXT,                  -- system time of invalidation
  supersedes_anchor_id TEXT,           -- optional direct pointer
  judge_log_json TEXT,                 -- TOKI θ
  meta_json TEXT NOT NULL DEFAULT '{}'
);

-- Typed edges
CREATE TABLE edges (
  id TEXT PRIMARY KEY,                 -- eg_...
  edge_type TEXT NOT NULL,             -- MENTIONS|DERIVES|ABOUT|SUPERSEDES|SUPPORTS|
                                       -- CONTRADICTS|LINKED_TO|NEXT_IN|ALIAS|CONTAINS|...
  from_id TEXT NOT NULL,
  to_id TEXT NOT NULL,
  repo_fingerprint TEXT NOT NULL,
  workstream_id TEXT,
  weight REAL NOT NULL DEFAULT 1.0,
  valid_at TEXT NOT NULL,
  invalid_at TEXT,
  created_at TEXT NOT NULL,
  meta_json TEXT NOT NULL DEFAULT '{}'
);

-- Evidence pointers (optional first-class)
CREATE TABLE evidence (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL,                  -- observation_span|tool_result|url|...
  payload_json TEXT NOT NULL,
  created_at TEXT NOT NULL
);
```

### 6.2 Invalidation algorithm (write-time)

```text
algorithm PROMOTE_OR_UPSERT_ANCHOR(candidate C, store S):
  # C from cognify / explicit CLI; already passed salience/recurrence gate
  ents ← RESOLVE_ENTITIES(C.mentions)          # embed+BM25 candidates → LLM/rules
  key  ← CLAIM_REF(C.kind, ents, normalize(C.statement))

  active ← S.anchors WHERE claim_ref_compatible(key) AND status='active'
                         AND valid_interval_overlaps(C.valid_at)

  op ← CLASSIFY(C, active)  # duplicate|refinement|complementary|temporal_scope|contradiction

  if op = NOOP or duplicate:
      LINK evidence; return existing

  if op ∈ {complementary, temporal_scope}:
      ADD C as active; ABOUT edges; return C

  if op = refinement:
      ADD C; SUPERSEDES → older if policy says absorb; else LINKED_TO; return C

  if op = contradiction:
      route ← KIND_POLICY(C.kind)  # see P4: LWW / EVIDENCE / ESCALATE / POLICY
      if route = ESCALATE:
          mark C and rivals status='disputed'
          emit ConflictSet; ADD C; CONTRADICTS edges; return
      winner, losers ← SELECT_WINNER(route, C, active)
      ADD winner if winner is C
      for L in losers:
          L.invalid_at ← winner.valid_at
          L.superseded_at ← now()
          L.status ← 'superseded'          # archive, do not DELETE
          INSERT edge SUPERSEDES(winner → L)
          INSERT audit row (dual-row / judge_log)
      return winner
```

### 6.3 Retrieval graph walk (hydrate expand)

```text
algorithm ASSOCIATIVE_EXPAND(query q, budget B):
  seeds ← ENTITY_LINK(q) ∪ TOP_TRIPLE_MATCH(q, k=5)
  seeds ← RECOGNITION_FILTER(seeds)            # cheap LLM/rules
  # Build undirected view: ABOUT, ALIAS(τ≥0.8), MENTIONS, SUPPORTS, LINKED_TO
  # Exclude invalid_at IS NOT NULL unless as_of time-travel
  scores ← PPR(graph, seeds, damping=0.5)
  anchors ← rank anchors by mass + importance×recency×relevance
  evidence ← expand CONTAINS/DERIVES within budget B
  return anchors, evidence
```

### 6.4 Recommended SQL indexes

```sql
CREATE INDEX idx_entities_repo_key ON entities(repo_fingerprint, normalized_key);
CREATE INDEX idx_entities_type ON entities(repo_fingerprint, entity_type);

CREATE INDEX idx_anchors_claim ON anchors(repo_fingerprint, claim_ref);
CREATE INDEX idx_anchors_active ON anchors(repo_fingerprint, workstream_id, status, kind)
  WHERE status IN ('active','disputed');
CREATE INDEX idx_anchors_valid ON anchors(valid_at, invalid_at);
CREATE INDEX idx_anchors_ws_created ON anchors(workstream_id, created_at DESC);

CREATE INDEX idx_edges_from ON edges(edge_type, from_id) WHERE invalid_at IS NULL;
CREATE INDEX idx_edges_to ON edges(edge_type, to_id) WHERE invalid_at IS NULL;
CREATE INDEX idx_edges_repo_type ON edges(repo_fingerprint, edge_type, created_at);
CREATE INDEX idx_edges_super ON edges(edge_type, to_id) WHERE edge_type='SUPERSEDES';

-- Optional: sqlite FTS5 on anchors.statement + entities.name
-- Optional: vector index side-table for embeddings (entities + anchors)
```

### 6.5 Compose projection

Projection of active Anchors for a workstream (full conflict algebra in P4):

```text
materialize:
  active = anchors where status in (active,disputed) and (invalid_at is null or as_of < invalid_at)
  group by claim_ref / functional key
  if >1 distinct values on functional kind → ConflictSet
build_view(resolver):
  selected ∪ unresolved ∪ explanations
  # never rewrite anchors/edges tables
```

---

## 7. Source fetch log

Full plaintext bodies cached at `/tmp/modex-papers/full/<id>.txt` via `arxiv.org/html`, `ar5iv`, or `pdftotext` on PDF. Seeds included Graphiti, HippoRAG×2, Mem0, LightRAG, GraphRAG, A-MEM, AriGraph, HyperGraphRAG, MAGMA, G-Memory, SSGM, selective supersession, MemClaw, StateFuse, TOKI, surveys, multi-agent memory papers, ReLiK.
