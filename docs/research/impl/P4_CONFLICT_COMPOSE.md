# P4 — Conflict / Compose (Implementation Clarity)

> **Date:** 2026-08-08  
> **Pillar:** Parallel writers, SUPERSEDES, ConflictSet, projection vs write, audit losers  
> **Method:** Full arXiv HTML/PDF body reads.  
> **Companion:** `P3_ANCHORS_GRAPH.md` (entity/fact graph, bi-temporal fields, PPR).  
> **Design lock cross-ref:** `docs/PARALLEL_COMPOSE_AND_HOOKS_V1.md`

---

## 0. Honesty table

| Bucket | Count | Notes |
|--------|------:|-------|
| **FULL deep-read (this pillar pass)** | **42** | Conflict/compose-relevant bodies; cards below |
| Shared with P3 FULL set | ~25 | Same session fetch; dual-use papers counted once in inventory |
| **Combined P3+P4 distinct FULL** | **≥55** | Target ≥40 met |
| Survey FULL for conflict taxonomy | 5 | 2602.05665, 2512.13564, 2603.07670, 2501.06322, 2602.19320 |

---

## 1. Architectural split (literature consensus)

```text
Layer 1 — Replicated append substrate (CRDT / OpSet / event log)
  EvidenceAdded | ClaimAdded | ClaimRetracted | DecisionAdded | AnchorWritten | EdgeWritten
  merge = set-union; never erase losers

Layer 2 — Projection / compose resolver (deterministic policy)
  build_view → Selected | Unresolved ConflictSets | Explanations
  MUST NOT rewrite Layer-1 history  (StateFuse Prop. Projection Non-Interference)
```

Sources: **StateFuse** (OpSet + ConflictSet + bounded projection), **TOKI** (typed write-time operators + dual-row audit), **CRDT multi-agent pattern** (collect then ContextMerge), **event-sourcing / CQRS**.

---

## 2. Mechanism cards (FULL papers)

### 2.1 StateFuse — `2607.05844` · **FULL**

**Ops.** `EvidenceAdded`, `ClaimAdded`, `ClaimRetracted(target_claim_id?, target_claim_ref?, reason, supersedes_*)`, `DecisionAdded`.

**Materialize.**
1. Index evidence/claims  
2. Compute `claim_ref` under predicate registry  
3. Apply retractions (exact id **or** semantic ref; unseen-target → no resurrection)  
4. Drop inactive  
5. Group by `ClaimKey=(namespace, subject, predicate)`  
6. Emit **ConflictSet** when functional predicate has >1 distinct active value  

**Projection.** `build_view(state, constraints, resolver) → (Selected, Unresolved, Explanations)`. Resolver may abstain; **cannot mutate base**. Compaction must be projection-equivalent.

**Empirical nuance.** Conflict preservation improves **safe abstention/correction**, not universal accuracy.

**MoDeX.** `disputed` status; dual `anc_id` + `claim_ref`; L4 handoff = projection.

---

### 2.2 TOKI — `2606.06240` · **FULL**

**Thesis.** Contradiction resolution = **write-time concurrency control** on partition `(subj, pred)` with bitemporal overlap.

**Dual-row.** Every operator commits **current row + audit row** (loser preserved).

**Four typed operators.**

| Op | Name | Isolation | Winner rule |
|----|------|-----------|-------------|
| \(\oplus_t\) | LWW | Read Committed | later system/valid time |
| \(\oplus_p\) | Evidence-weighted | Snapshot Isolation | higher confidence (+ evidence) |
| \(\oplus_?\) | Await-confirmation | RC + callback | human/judge callback |
| \(\oplus_c\) | Per-rule policy | Policy serializable | rule table on kind |

**Algorithm 1 (write path).** Detect contradicting incumbent → isolation precondition gate → typed operator → **judge-log write precedes commit** → dual-row persist. Judge key \(\theta=(\mathrm{prompt},\mathrm{seed},\mathrm{model\_version},\mathrm{temperature},\mathrm{tool\_output\_hash})\).

**N-ary.** Fold operators over conflict sets (not pairwise-only).

**Baselines TOKI audits.** Mem0 ADD/UPDATE/DELETE drops losers; Graphiti invalidates without fact-level `superseded_by` field / decoder-seed pin; etc.

**MoDeX.** Named operators + audit + judge log + kind policy table.

---

### 2.3 Selective Memory supersession — `2603.15994` · **FULL**

**Operators.** Gate (admit/archive by salience); on update create bidirectional version links:
- \(K_{old}.\mathrm{superseded\_by} \leftarrow K_{new}.id\)
- \(K_{new}.\mathrm{supersedes} \leftarrow K_{old}.id\)
- Move old to **archive**, new to **active**  
Never overwrite; temporal queries walk chain \(v_1\to v_2\to v_3\).

**Salience.** reputation × novelty × reliability vs threshold; below → cold archive.

**MoDeX.** SUPERSEDES edge + `status=archived/superseded`; promotion salience gate.

---

### 2.4 MemClaw — `2606.24535` · **FULL**

**Fleet failures.** Unauthorized leakage; stale propagation; contradiction persistence; provenance collapse.

**Temporal supersession.** Outdated rows marked **non-active**; provenance graph depth walks.

**Critical ordering.** Synchronous near-duplicate gate can **reject contradictory writes before async contradiction detector runs** → contradiction persistence. Fix: **structural conflict/supersession before near-dup NOOP**.

**Consistency cost paid at write time**, not only read time. Scope must be enforced on **all** read paths (GET-by-id gap remediated in study).

**MoDeX.** Pipeline order: normalize → claim_ref match → conflict classify → supersede/escalate → only then near-dup short-circuit; scope on hydrate + get.

---

### 2.5 Mem0 / Mem0\(^g\) — `2504.19413` · **FULL**

**Flat ops.** ADD / UPDATE / DELETE / NOOP via LLM tool-call after top-s retrieval.  
**Graph.** Conflict detection → mark relationships **invalid** (soft), enabling temporal reasoning.

**MoDeX mapping.** DELETE → INVALIDATE+SUPERSEDES+audit (do not physically remove Anchor rows).

---

### 2.6 Memory-R1 — `2508.19828` · **FULL**

RL Memory Manager learns ADD/UPDATE/DELETE/NOOP; Answer Agent utilizes. Outcome reward from QA.

**MoDeX.** Validates operator enum; v1 remains heuristic/policy, not PPO.

---

### 2.7 Graphiti / Zep — `2501.13956` · **FULL**

LLM compares new vs related edges; temporally overlapping contradiction →  
\(t_{\mathrm{invalid}}(\mathrm{loser}) \leftarrow t_{\mathrm{valid}}(\mathrm{winner})\); prefer newer on transaction timeline \(T'\). History retained.

**Gap vs TOKI/Selective.** No first-class `superseded_by` field / audit tuple / judge seed pin — MoDeX adds these.

---

### 2.8 SSGM — `2603.11768` · **FULL**

Consistency verification **before consolidation**; drift vs extrinsic threat taxonomy; access control.

**MoDeX.** Shareable promotion after conflict resolve + capability check.

---

### 2.9 Collaborative Memory — `2505.18279` · **FULL**

Private/shared tiers; dynamic ACL; provenance. Parallel users ⇒ permissioned compose, not global LWW.

**MoDeX.** Compose respects principal scope; shared Anchors escalate more readily.

---

### 2.10 A-MEM — `2502.12110` · **FULL**

Evolution rewrites neighbors in place — **anti-pattern** for conflict audit.

**MoDeX.** Reject silent mutation; append+SUPERSEDES.

---

### 2.11 HippoRAG / HippoRAG2 — `2405.14831` / `2502.14802` · **FULL**

No belief revision; ranking only. Contradictory triples may coexist.

**MoDeX.** Separation: retrieval graph may keep ALIAS/MENTIONS; **truth graph** must invalidate.

---

### 2.12 LightRAG / GraphRAG — `2410.05779` / `2404.16130` · **FULL**

Dedup/profile merge / claims-as-covariates; not versioned belief revision.

**MoDeX.** Dedup ≠ supersession; claims feed Evidence, not silent Anchor edits.

---

### 2.13 HyperGraphRAG — `2503.21322` · **FULL**

N-ary facts; coexistence at index time.

**MoDeX.** Conflict keys may involve **set of ABOUT entities**, not only binary subject.

---

### 2.14 AriGraph — `2407.04363` · **FULL**

Semantic update + episodic append; weak explicit contradiction algebra.

**MoDeX.** Episodic append-only; semantic updates must go through SUPERSEDES.

---

### 2.15 MAGMA — `2601.03236` · **FULL**

Multi-graph views; dual-stream ingest/consolidate — consolidation is where conflicts should be typed.

**MoDeX.** Fast path append ops; slow path runs conflict classify.

---

### 2.16 G-Memory — `2506.07398` · **FULL**

Hierarchical multi-agent memory tracing; insights across agents need namespace isolation.

**MoDeX.** Workstream namespace in ClaimKey.

---

### 2.17 MetaGPT / ChatDev / CAMEL / AutoGen — `2308.00352` / `2307.07924` / `2303.17760` / `2308.08155` · **FULL**

Shared message pools / phase docs / dialogue memory. **No** typed SUPERSEDES; last message often wins implicitly.

**MoDeX lessons.** Multi-agent frameworks need MoDeX store underneath or they hide contradictions in chat logs.

---

### 2.18 Generative Agents / MemGPT / MemoryOS — `2304.03442` / `2310.08560` / `2506.06326` · **FULL**

Importance ranking / paging / FIFO tiers — eviction ≠ logical invalidation.

**MoDeX.** Do not treat cache drop as SUPERSEDES.

---

### 2.19 Nemori / RecMem / ES-Mem — `2508.03341` / `2605.16045` / `2601.07582` · **FULL**

Promotion gating reduces conflict volume (fewer junk Anchors). Light on explicit contradiction ops.

**MoDeX.** Fewer writes ⇒ fewer ConflictSets; still need TOKI operators when they occur.

---

### 2.20 Surveys — `2602.05665`, `2512.13564`, `2603.07670`, `2501.06322`, `2602.19320`, `2605.06716`, `2411.00489` · **FULL**

Integrate step = conflict detection + pruning; shared multi-agent memory is a frontier with trustworthiness debt; eval must include conflict-bearing slices (MemoryAgentBench).

---

### 2.21 AgentLeak / MemLeak (compose/governance adjacency) — `2602.11510` / `2606.29788` · **FULL**

Leakage via memory topology / shared stores. Compose must not widen scope.

**MoDeX.** Projection filters by capability before union.

---

### 2.22–2.30 Additional FULL supporting texts

| ID | Role for P4 |
|----|-------------|
| `2505.19549` | Granularity selection can create false conflicts if keys too coarse |
| `2510.10397` AssoMem | Multi-signal retrieve of conflict candidates |
| `2508.19828` Memory-R1 | RL ops (above) |
| `2509.25911` Mem-α | Construction policy ≠ conflict policy |
| `2510.18866` LightMem | Hot/cold after supersession |
| `2408.00103` ReLiK | Entity identity errors ⇒ false conflicts |
| `2503.21760` / `2508.06433` / `2402.16288` | Supporting multi-agent / memory conflict corpus |
| `2604.22085` | Supporting |
| `2507.05257` / `2507.07957` | Top-rank agent memory systems; update semantics |
| `1410.5401` NTM | Not conflict-preserving |
| `2505.18279` | Collaborative (above) |

---

## 3. Conflict taxonomy → operators

| Type | Meaning | Default MoDeX operator |
|------|---------|------------------------|
| `duplicate` | same claim_ref / normalized statement | `DEDUPE` / `NOOP` (+ link evidence) |
| `refinement` | specializes without negating | `UPDATE` absorb or `LINKED_TO` |
| `complementary` | different facets | `ADD` both + `LINKED_TO`/`PARALLEL_WITH` |
| `temporal_scope` | non-overlapping valid intervals | keep both; set `valid_at`/`invalid_at` |
| `contradiction` | incompatible values, overlapping validity | typed resolve below |

**Comparable key v1.**
```text
claim_ref = hash(repo, kind, sorted(about.normalized_key[]), normalize(statement)?)
# for decision/rejection prefer entity signature over raw statement text
```

---

## 4. Kind-specific policy (TOKI \(\oplus_c\) locked defaults)

| Kind | Parallel contradiction |
|------|------------------------|
| `constraint` | **ESCALATE** (never silent LWW) |
| `rejection` | SUPERSEDE_BY_EVIDENCE if one tool-verified; else **ESCALATE** |
| `decision` | explicit user > agent_inferred; two users disagree → **ESCALATE** |
| `gotcha` | SUPERSEDE_BY_TIME or EVIDENCE OK |
| `goal` / `next_step` | union or escalate; never smash |
| `open_question` | `ADD` union |

---

## 5. Anti-patterns

1. Silent LWW on constraints/decisions.  
2. DELETE without audit row.  
3. Near-dup short-circuit before contradiction classify (MemClaw).  
4. Resolver rewriting Layer-1 (StateFuse violation).  
5. Pairwise-only merges (miss n-ary three-way eng debates).  
6. Projection that hides `disputed` for “cleaner” accuracy.  
7. Scope enforced on search but not get-by-id.

---

## 6. Open risks

- LLM judge nondeterminism without keyed \(\theta\) log (TOKI tightness).  
- Cross-replica id absence → need semantic `claim_ref` retractions.  
- False conflicts from bad entity resolution.  
- Latency of write-time LLM contradiction checks at high fan-in.  
- Eval gold=latest collapses the metric StateFuse warns about.

---

## 7. MoDeX implementation recipe (P4)

### 7.1 Edge / audit schema additions

```sql
-- See also P3 anchors/edges tables.

CREATE TABLE conflict_sets (
  id TEXT PRIMARY KEY,                 -- cset_...
  repo_fingerprint TEXT NOT NULL,
  workstream_id TEXT,
  claim_ref TEXT NOT NULL,
  kind TEXT NOT NULL,
  candidate_anchor_ids_json TEXT NOT NULL,  -- [...]
  distinct_values_json TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'open',      -- open|resolved|escalated
  resolution_anchor_id TEXT,
  resolver TEXT,                            -- lww|evidence|policy|human|abstain
  reason TEXT,
  created_at TEXT NOT NULL,
  resolved_at TEXT
);

CREATE TABLE audit_events (
  id TEXT PRIMARY KEY,
  event_type TEXT NOT NULL,            -- SUPERSEDE|ESCALATE|DEDUPE|RETRACT|COMPOSE_VIEW
  repo_fingerprint TEXT NOT NULL,
  workstream_id TEXT,
  winner_id TEXT,
  loser_id TEXT,
  claim_ref TEXT,
  operator TEXT NOT NULL,              -- SUPERSEDE_BY_TIME|SUPERSEDE_BY_EVIDENCE|ESCALATE|POLICY|...
  judge_log_json TEXT,                 -- TOKI θ
  as_of_valid_at TEXT,
  created_at TEXT NOT NULL,
  meta_json TEXT NOT NULL DEFAULT '{}'
);

-- SUPERSEDES is an edges.edge_type; optional denorm on anchors.supersedes_anchor_id
```

### 7.2 Exact SUPERSEDES algorithm recommended for MoDeX

```text
################################################################################
# MoDeX SUPERSEDES (recommended)
# Synthesis of: Graphiti bi-temporal invalidation + Selective Memory version
# chains + TOKI dual-row/typed ops + StateFuse ConflictSet/projection bounds
# + MemClaw pipeline ordering.
################################################################################

algorithm MODEX_SUPERSEDES_ON_WRITE(new_anchor A, store S, principal P):

  REQUIRE has_capability(P, append, A.workstream_id)

  # --- 0. Normalize & resolve (P3) ---
  A.about ← RESOLVE_ENTITIES(A.mentions)
  A.claim_ref ← MAKE_CLAIM_REF(A.repo, A.kind, A.about, A.statement)
  A.valid_at ← A.valid_at or A.event_time or now()
  A.created_at ← now()

  # --- 1. Candidate set (active, overlapping validity, same functional key) ---
  Cands ← { X ∈ S.anchors |
              X.repo = A.repo
          and X.status ∈ {'active','disputed'}
          and claim_ref_compatible(X.claim_ref, A.claim_ref)
          and intervals_overlap(X.valid_at, X.invalid_at, A.valid_at, NULL) }

  # --- 2. MemClaw ordering: classify BEFORE near-dup short-circuit ---
  class ← LLM_OR_RULES_CLASSIFY(A, Cands)
          # → duplicate | refinement | complementary | temporal_scope | contradiction

  if class = duplicate:
      LINK evidence(A → existing); AUDIT(DEDUPE); return existing   # NOOP-ish

  if class = complementary:
      INSERT A status='active'; LINKED_TO; return A                 # ADD

  if class = temporal_scope:
      INSERT A; optionally set prior.invalid_at if sequential; return A

  if class = refinement:
      INSERT A status='active'
      if policy.absorb_refinement(A.kind):
          for X in Cands: SUPERSEDE_LINK(A, X, op='POLICY_REFINE')
      else:
          LINKED_TO(A, Cands)
      return A

  # --- 3. contradiction → typed operator (TOKI) ---
  assert class = contradiction
  op ← KIND_POLICY(A.kind)   # table in §4
      # maps to SUPERSEDE_BY_TIME | SUPERSEDE_BY_EVIDENCE | ESCALATE | POLICY

  if op = ESCALATE:
      INSERT A status='disputed'
      for X in Cands: X.status ← 'disputed'; CONTRADICTS edges
      OPEN ConflictSet(claim_ref, candidates=Cands∪{A}, resolver='human')
      AUDIT(ESCALATE, judge_log=θ); return A

  # select winner
  if op = SUPERSEDE_BY_TIME:      # ⊕_t
      winner ← argmax_{X in Cands∪{A}} (X.valid_at, X.created_at)
  else if op = SUPERSEDE_BY_EVIDENCE:  # ⊕_p
      winner ← argmax (source_ladder_rank, confidence, valid_at, created_at)
  else if op = POLICY:            # ⊕_c
      winner ← APPLY_RULE_TABLE(A.kind, Cands∪{A})

  losers ← (Cands∪{A}) \ {winner}

  if winner = A and A not in S: INSERT A status='active'

  for L in losers:
      # Graphiti-style bi-temporal invalidation
      L.invalid_at     ← winner.valid_at
      L.superseded_at  ← now()              # system/transaction time
      L.status         ← 'superseded'       # Selective Memory: archive, don't DELETE
      # Selective Memory bidirectional version chain
      INSERT edge SUPERSEDES(from=winner.id, to=L.id,
                             valid_at=winner.valid_at, created_at=now())
      L.meta.superseded_by ← winner.id
      winner.meta.supersedes ← append(L.id)
      # TOKI dual-row / audit
      AUDIT(SUPERSEDE, winner=winner, loser=L, operator=op, judge_log=θ)

  CLOSE any open ConflictSet on claim_ref with resolution=winner
  return winner


algorithm INTERVALS_OVERLAP(v1, i1, v2, i2):
  # treat NULL invalid_at as +∞
  end1 ← i1 or +∞; end2 ← i2 or +∞
  return v1 < end2 and v2 < end1
```

**Invariants.**
1. Losers remain readable for audit / time-travel (`status=superseded`, `invalid_at` set).  
2. No hard DELETE of Anchor rows in v1.  
3. Judge log \(\theta\) persisted whenever LLM classification or evidence weigh used.  
4. Projection may abstain; it may not resurrect superseded without `as_of`.  
5. Near-dup runs only after contradiction classify.

### 7.3 Compose projection algorithm

```text
algorithm COMPOSE_PROJECTION(workstream W, mode, resolver, principal P, as_of=None):

  REQUIRE capability(P, read_hydrate, W)

  ops ← Layer1_ops visible to P scoped to W∪repo_shared_safe

  # Materialize (StateFuse)
  M ← MATERIALIZE(ops, as_of)
      # apply SUPERSEDES/retractions; group by claim_ref;
      # ConflictSet if functional kind has >1 active distinct value

  if mode = pin:      view ← pack_or_actor_slice(...)
  if mode = primary:  view ← latest handoff HEAD + active anchors
  if mode = lineage:  view ← HEAD ∪ selected ancestor anchors
  if mode = compose:  # default multi-writer
      Selected, Unresolved, Expl ← build_view(M, resolver, constraints)
      # WorkingState field merges:
      #   files_in_flight/open_questions/blockers = set-union
      #   goal: equal→keep; else goals_conflict[] + escalate marker
      #   last_user_ask: LWW + prior in recent_asks[]
      #   active_anchor_ids: Selected ids

  # Budgeted hydrate: drop Unresolved into explicit conflict markers, not silent omit
  return HandoffPack | WorkingState view  # L4 projection; do not write back winners
```

### 7.4 Recommended SQL indexes

```sql
CREATE INDEX idx_cset_open ON conflict_sets(workstream_id, status, claim_ref)
  WHERE status='open';
CREATE INDEX idx_cset_claim ON conflict_sets(repo_fingerprint, claim_ref);

CREATE INDEX idx_audit_ws_time ON audit_events(workstream_id, created_at DESC);
CREATE INDEX idx_audit_loser ON audit_events(loser_id);
CREATE INDEX idx_audit_claim ON audit_events(claim_ref, created_at DESC);

CREATE INDEX idx_anchors_claim_status ON anchors(repo_fingerprint, claim_ref, status);
CREATE INDEX idx_anchors_disputed ON anchors(workstream_id, status)
  WHERE status='disputed';

CREATE INDEX idx_edges_supersedes_active ON edges(from_id, to_id, created_at)
  WHERE edge_type='SUPERSEDES';
```

### 7.5 WorkingState compose (parallel agents)

| Field | Merge |
|-------|-------|
| goal | compatible→keep; else `goals_conflict[]` |
| files_in_flight | set-union |
| open_questions | set-union |
| blockers | set-union |
| last_user_ask | LWW + audit in `recent_asks[]` |
| active_branch | multi-value OK; projection picks primary |
| active_anchor_ids | post-SUPERSEDES Selected set |

---

## 8. Source fetch log

Bodies in `/tmp/modex-papers/full/`. Primary conflict sources: StateFuse, TOKI, Selective Memory `2603.15994`, MemClaw, Mem0/Mem0g, Memory-R1, Graphiti, SSGM, Collaborative Memory, multi-agent frameworks (MetaGPT/ChatDev/CAMEL/AutoGen), graph surveys `2602.05665` + `2512.13564`.
