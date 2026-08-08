# Kedger Implementation From Literature

> **Status:** Living implementation guide synthesized from **full-body deep-reads**  
> **Product:** **Kedger** (not MoDeX — different product)  
> **Date:** 2026-08-08  
> **Audience:** Engineers implementing Phase A–E against locked schemas  
> **Companion:** `docs/research/impl/P1…P6_*.md`, `docs/research/CORPUS_INVENTORY.md`  
> **Honesty:** We do **not** claim every paper in the ~780-ID survey seed was end-to-end read. This guide only encodes mechanisms from papers whose bodies were actually read (see inventory). Background agents continue expanding FULL coverage per pillar.

---

## 0. How to use this document

For each Kedger component:

1. **Do this** — concrete algorithm / schema / constant  
2. **Because** — which papers showed it and why  
3. **Do not** — anti-pattern observed in literature or production failures  

If a constant is marked `TUNE`, start with the listed default and measure on handoff continuity + no-relitigation fixtures.

---

## 1. Layer mapping (literature → Kedger)

| Kedger | Closest literature analogues (deep-read) | Implementation stance |
|-------|------------------------------------------|------------------------|
| **L0 Raw** | MemGPT FIFO queue; MemoryOS STM dialogue pages; RecMem subconscious embeds; StreamingLLM sink tokens | Append-only, rotatable, never handoff-canonical |
| **L1 Working** | MemGPT main/core; MIRIX Core (persona/human); MemoryOS in-flight STM chain meta; AIOS context | Mutable UPSERT per workstream; small; always hydrated first |
| **L2 Episodes** | Nemori/ES-Mem EST segments; MemoryOS MTM segments+pages; EM-LLM surprise boundaries; Graphiti episodes | Boundary → digest; keep provenance to L0 ids |
| **L3 Anchors** | Mem0 facts; Graphiti edges; MIRIX Semantic/Episodic distilled; GenAgents reflections; A-MEM notes | Atomic, bi-temporal, SUPERSEDES not DELETE |
| **Evidence** | Graphiti episode→entity edges; HippoRAG passages; MIRIX Resource details | Budgeted; detachable; never required for Anchor meaning |
| **L4 Handoff** | MemGPT compile to main; StateFuse projection; MIRIX Active Retrieval pack into system prompt | Ranked projection; sealed `.kxp`; cannot rewrite L3 |
| **Workstream** | StateFuse namespaces; MemClaw fleet/scope; Collaborative Memory user partitions | Primary continuity key |
| **Shareable** | Collaborative Memory shared tier; MIRIX marketplace vision (caution); ADR Accepted | Orthogonal ladder; `explicit_only` |

---

## 2. L0 Capture (hooks → observations)

### Do this
```text
on hook_event:
  redact(secrets)                         # before persist
  obs = Observation{
    type, ts, session_id, actor_principal_id,
    repo_fingerprint, workstream_id?, summary,
    payload_ref, visibility=private_raw
  }
  append L0
  if state_changing(obs): soft_patch L1   # goal/files/questions only
  emit promotion_signals(obs)             # Tier A/B/C counters; do NOT LLM every turn
  if boundary(obs): schedule cognify()
```

### Because
- **RecMem:** eager LLM extraction every turn is wasteful; subconscious/cheap store first.  
- **MemoryOS STM:** pages are `{Q,R,T}` (+ chain meta); FIFO migrate when full.  
- **MIRIX app:** capture cadence can be high (screenshots 1.5s) but **batch before heavy update** (their 20-image batch). For coding hooks: append every event; cognify on boundaries.  
- **AgentLeak:** redact before any cross-agent channel; internal channels leak more than final outputs.

### Constants (start)
| Constant | Default | Source intuition |
|----------|---------|------------------|
| `l0_max_rows_per_workstream` | 5000 | MemGPT-style FIFO pressure |
| `l0_max_age_hours` | 72 | rotate after episode cognify sooner |
| `redaction_before_persist` | true | AgentLeak / vault |
| `llm_on_every_observation` | **false** | RecMem |

### Do not
- Put full tool dumps into L4.  
- Treat L0 as searchable across principals.  
- Skip redaction until share time (too late — MemLeak residuals).

---

## 3. L1 Working state

### Do this
```sql
UPSERT working_state SET
  goal, next_step, files_in_flight[], open_questions[],
  blockers[], updated_at
WHERE workstream_id = ?
```

Field-wise merge on parallel compose (union files/questions; conflict goals → open_questions) — see parallel compose lock.

### Because
- **MemGPT / MIRIX Core:** always-visible small block; rewrite when >~90% capacity (MIRIX).  
- **MemoryOS:** STM chain meta keeps “current topic continuity” without promoting to persona.

### Constants
| Constant | Default |
|----------|---------|
| `working_max_bytes` | 4–6 KB |
| `core_rewrite_ratio` | 0.90 (MIRIX) |
| `files_in_flight_max` | 12 |

### Do not
- Store durable decisions only in working (they die on compact).  
- Auto-promote working goals to `repo_shared_safe`.

---

## 4. L2 Episode cognify (boundaries)

> Full recipe: `docs/research/impl/P2_EPISODE_COGNIFY.md` (ES-Mem, Membox, RecMem, …).

### Boundary detectors
```text
HARD (always): PRE_COMPACT | SESSION_END | kedger cognify
SOFT (if min_span): workstream_switch | idle>T_idle | F_score<θ_segment | optional Loom shift/surprise
```

### Cognify algorithm
```text
span = L0 since last boundary
if SOFT and |span|<min_span: skip
episode = {
  summary, boundary_summary,          # ES-Mem: boundaries are retrieve anchors
  topic_keywords, observation_ids[],
  heat, time_start, time_end
}
NEXT_IN(prev→ep); optional macro traces (Membox Trace Weaver)
promotion.tier_A_B_C(span, ep)        # RecMem recurrence → candidates only
compose.project → seal.kxp(epoch++)
mark L0 compacted; never delete Anchors
```

### Because
- **Membox:** fragmentation–compensation fails; seal topic-continuous boxes at storage time.  
- **ES-Mem:** MI/intent dynamic cuts + boundary text for coarse-to-fine retrieve.  
- **RecMem:** \(\theta_{sim}=0.7\), \(\theta_{count}=5\) (chat) / **3** (eng); LLM only on recurrence.  
- **MemoryOS:** Heat + segmented paging for migration/eviction ranking.

### Constants
| Constant | Default | Notes |
|----------|---------|-------|
| `θ_segment` | 0.60 | MemoryOS F_score |
| `θ_sim` / `θ_count` | 0.70 / 3 | RecMem; eng denser than LoCoMo’s 5 |
| `q_MI` | 0.35 | ES-Mem candidate quantile |
| `min_span_events` | 8 | avoid tiny chapters |
| `T_idle` | 45 min | engineering session gap |
| `boundary_summary_max_chars` | 400 | |
| `llm_topic_loom` / `llm_episode_digest` | off v1 | deterministic first |
| `hard_boundaries` | PRE_COMPACT, SESSION_END | never skip |

### Do not
- Fixed every-N-turns episodes.  
- One Observation = one L2 atom.  
- Forgetting-curve **delete** on Anchors (MemoryBank decay is ranking-only).  
- Auto-share from Heat/recurrence.

---

## 5. L3 Anchors + graph (the compact-native store)

### Anchor write (Mem0-style operators + Graphiti timestamps)
```text
candidates = extract_judgments(span)  # deterministic patterns first; LLM optional
for c in candidates:
  key = normalize_claim_key(c.kind, c.entities, c.statement)
  neighbors = retrieve_same_key_or_entity_pair(key)
  op = classify(c, neighbors)  # ADD | UPDATE | SUPERSEDE | DEDUPE | NOOP | ESCALATE

  if op == ADD:
    insert Anchor{valid_at=now, status=active, provenance, shareable=false}
  if op == SUPERSEDE:
    old.invalid_at = c.valid_at; old.status=superseded; keep row
    insert new Anchor; edge SUPERSEDES(new, old)
  if op == DEDUPE:
    link evidence; maybe bump confidence
  if op == ESCALATE:
    ConflictSet{claims...} for compose/hydrate
```

### Bi-temporal fields (Graphiti — required)
| Field | Meaning |
|-------|---------|
| `valid_at` / `invalid_at` | When fact was true in the world/task |
| `created_at` / `updated_at` | When Kedger learned/changed it |

### Entity graph
- `EntityNode(normalized_key)` unique per repo  
- Edges: `ABOUT`, `DERIVES`, `SUPERSEDES`, `RELATED`, `NEXT_IN`  
- Retrieval expand: HippoRAG-style seed entities → neighborhood / PPR (hydrate)

### Promotion into Anchorhood (orthogonal to share)
Use existing Tier A/B/C doc. Literature reinforcement:
- **Tier A explicit language** ≈ ADR / user remember  
- **Tier B recurrence** ≈ RecMem (≥3) / MemoryOS heat  
- **Never** let reflection importance alone publish (GenAgents creates candidates only)

### Because
- **Mem0:** ADD/UPDATE/DELETE/NOOP tool loop — we replace DELETE with SUPERSEDE.  
- **Graphiti:** invalidate overlapping edges; prefer newer transactionally; keep history.  
- **A-MEM:** atomic notes + links; do **not** silently rewrite sealed Anchor text in place.  
- **TOKI/StateFuse:** losers stay as audit.

### Constants
| Constant | Default |
|----------|---------|
| `recurrence_promote_n` | 3 |
| `anchor_statement_max_chars` | 280 |
| `evidence_default_on_promote` | optional pointer only |
| `ppr_damping` | 0.5 (HippoRAG-like; TUNE) |
| `entity_alias_cos_τ` | 0.8 (HippoRAG synonym; TUNE) |

### Do not
- Silent overwrite of Anchor statement.  
- Treat embedding similarity as entitlement (MemClaw).  
- Auto `shareable=true` on promote.

---

## 6. Parallel compose (P4)

### Layer split (locked + reaffirmed)
```text
Layer-1: immutable ops (append Anchor/Evidence/Episode/Relation/Conflict)
Layer-2: projection resolver for Working + Handoff (deterministic policy)
```

### Operators (implementation enum)
`DEDUPE | UPDATE | ADD | SUPERSEDE_BY_TIME | SUPERSEDE_BY_EVIDENCE | ESCALATE | POLICY`

### Defaults
```text
constraints → ESCALATE (surface both)
decisions   → user_over_agent else ESCALATE if dual-explicit
rejections  → EVIDENCE-weighted else ESCALATE
complementary → ADD both
keep_audit_losers = true
```

### Because
StateFuse (projection authority), TOKI (typed ops + audit rows), MemClaw (contradiction admits before near-dup gate).

### Do not
- Let near-duplicate 409 starve supersession (MemClaw production bug).  
- Collapse ConflictSet at write time for constraints.

---

## 7. Hydrate / L4 compile (P5)

### Scoring (start formula)
Inspired by Generative Agents `recency × importance × relevance`, MemoryOS Heat, and Kedger survival order:

```text
score(a) =
  w_kind[a.kind]                 # constraint/reject > decision > gotcha > goal > next > open_q
  * (0.35 * relevance(a, query_or_workstream))
  * (0.25 * recency(a.updated_at))
  * (0.20 * importance_or_heat(a))
  * (0.20 * provenance_trust(a))
  * scope_ok(a, principal)       # 0 if not entitled → drop (Inv-Scope)
```

### Pack composition order (budget)
1. Working state (always if entitled)  
2. Active constraints + rejections  
3. Active decisions (non-superseded)  
4. Gotchas / goals / next_steps  
5. Latest 1–3 episode digests  
6. Evidence snippets (first to drop)  
7. Optional `repo_shared_safe` facet (opt-in, ranked, capped)

### Active retrieval (MIRIX lesson)
On `SESSION_START`: derive topic from workstream goal + recent files → retrieve → inject. Do not wait for the model to “remember to search.”

### Lost-in-the-middle
Put constraints/rejects at **edges** of inject blob (start + end), not first buried mid-pack (Liu et al. 2307.03172).

### Constants
| Constant | Default |
|----------|---------|
| `handoff_target_kb` | 25–40 |
| `max_anchors` | 40 |
| `max_episodes` | 3 |
| `max_evidence` | 8 |
| `shared_facet_max` | 10 |

### Do not
- Dump entire shared index into every pack (PRISM amplification / pack deputy).  
- Hydrate without capability check.

---

## 8. Privacy, share, seal (P6)

### Inv-Scope middleware (MemClaw)
```text
def authorize(principal, action, object):
  if not capability_covers(principal, action, object):
    raise NotFound()   # 404, not 403
  return object
# apply to: list, search, get_by_id, hydrate, export, mcp
```

### Share ladder
```text
share_mode = explicit_only
before share:
  kind_allowlist → redact → detach Evidence → conflict check → set shareable+visibility
unshare:
  revoke shared facet → cascade embeddings/caches → stale packs
```

### Seal pipeline (locked)
Age-shaped multi-recipient + XChaCha20-Poly1305 STREAM + Ed25519 sign-then-encrypt; **revoke = reseal new epoch**.

### MIRIX Knowledge Vault lesson
Secrets belong in a **vault-like visibility**, never Semantic/Episodic share paths. Map to Kedger `private_raw` + never-promote.

### Do not
- Existence oracles via 403.  
- Git-commit packs.  
- Trust agent-inferred auto-share.

---

## 9. Evaluation harness (implement with Phase A+)

From MemBench / MemoryAgentBench / LoCoMo / HaluMem / ArgusFleet lessons:

| Fixture | Pass criteria |
|---------|---------------|
| No-relitigation | Rejection Anchor survives compact; hydrate answers without raw chat |
| Supersession | New decision invalidates old; audit retains loser |
| Budget | Pack ≤ ceiling; constraints retained under drop order |
| Inv-Scope | Outsider GET-by-id → not found |
| Parallel compose | Complementary union; constraint conflict escalates |
| Unshare cascade | Shared index omits after unshare |
| Hallucination/HaluMem-style | Hydrate must not invent Anchors not in store |

---

## 10. Phase A code skeleton (what to build first)

```text
kedger/
  store/sqlite.py          # L0–L3 tables + indexes
  redact.py
  keys.py                  # Ed25519 + X25519; keychain
  ingest.py                # Observation append + L1 patch
  remember.py              # explicit Anchor upsert
  cognify.py               # boundary → episode → promote
  compose.py               # Layer-2 projection
  seal.py / hydrate.py     # .kxp + ranking
  acl.py                   # Inv-Scope 404
  hooks/normalize.py       # Cursor/Claude → ObservationType
```

SQLite indexes to create on day 1:
```sql
CREATE INDEX obs_ws_ts ON observations(workstream_id, ts);
CREATE INDEX anc_ws_status_kind ON anchors(workstream_id, status, kind);
CREATE INDEX anc_valid ON anchors(valid_at, invalid_at);
CREATE UNIQUE INDEX ent_repo_key ON entities(repo_fingerprint, normalized_key);
CREATE INDEX edge_src_type ON edges(src_id, edge_type);
CREATE INDEX cap_grantee_ws ON capabilities(grantee_principal_id, workstream_id);
```

---

## 11. Literature → constant cheat sheet

| Name | Value | From |
|------|-------|------|
| Recurrence promote | 3 | RecMem / Kedger Tier B |
| Heat τ → persona/LPM | 5 | MemoryOS |
| Core rewrite | 90% | MIRIX |
| Segment score | cos+Jaccard > θ | MemoryOS |
| Recency μ | ~1e7 s | MemoryOS Heat |
| User KB FIFO | 100 | MemoryOS |
| Active retrieval | on | MIRIX |
| Deny code | 404 | MemClaw |
| Share mode | explicit_only | Collaborative Memory + Kedger policy |
| DELETE Anchors | forbidden (SUPERSEDE) | Graphiti/TOKI/StateFuse |
| Seal revoke | reseal epoch++ | MLS |

---

## 12. What still needs more FULL reads (active)

Background deep-read campaign continues for Memory-R1, Mem-α, G-Memory, LightMem details, ConfAIde/Fides, RAPTOR/PropRAG, more CRDT multi-agent, HaluMem failure taxonomies. New cards land under `docs/research/impl/`. This file should be updated when a FULL read changes a constant or algorithm.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-08-08 | Initial cross-pillar implementation synthesis from deep-read MemoryOS, MIRIX, MemOS framing, Graphiti/Mem0/RecMem/StateFuse/TOKI/MemClaw/HippoRAG/hooks/crypto locks. |
