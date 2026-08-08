# Workstream Identity & Promotion Signals v1

> **Status:** Design lock (research-informed)  
> **Date:** 2026-08-08  
> **Depends on:** `OPEN_SOURCE_MEMORY_ARCHITECTURE.md`, `MEMORY_SCHEMAS_V1.md`  
> **Scope:** Exactly the two next locks after schemas — (1) how a workstream is identified, (2) when memory gets promoted to Anchors.

---

## 0. Research basis (what we synthesized)

We cannot literally read 1000+ papers in one pass. This lock synthesizes the **convergent findings** from the strongest relevant lines:

| Line | Key papers / systems | Takeaway we adopt |
|------|----------------------|-------------------|
| Event Segmentation Theory | Zacks et al.; ES-Mem; CompassMem; EM-LLM; Nemori | Boundaries form when goals/state/topic shift — not on arbitrary timers |
| Episode formation | Nemori Two-Step Alignment; SEEM | Top-down coherent episodes beat fixed chunk sizes |
| Surprise / prediction error | EM-LLM; Nemori Predict-Calibrate; “What Deserves Memory” | High surprise / prediction gap is a promotion/boundary signal |
| Recurrence consolidation | RecMem | Promote patterns seen repeatedly (θ_count ≈ 3–5) |
| Importance-triggered reflection | Generative Agents | Accumulate importance; reflect/consolidate when threshold crossed |
| Write-time organization | A-MEM | Link + evolve on write; don’t wait only for retrieval |
| Governed writes | SSGM; episodic→semantic without identity drift | Validate before semantic commit; provenance; no silent overwrite |
| Task threads / isolation | Colony task threads; Nimbalyst workstreams; worktree task isolation; Lalia rooms | Shared objective ≠ session; key by repo+intent(+branch/worktree); isolate parallel tasks |

**Engineering translation:**  
Workstream = durable shared objective identity.  
Promotion = governed graduation from observations/episodes → Anchors.

---

## 1. Workstream identity — what problem it solves

Without workstream identity:

- parallel agents contaminate each other
- branch switches look like “new worlds” or get wrongly merged
- handoffs become a single blob
- privacy/ACL has nothing to attach to

**Lock:** every Observation, WorkingState, Episode, and HandoffPack must resolve to exactly one `workstream_id` (or explicitly `unassigned` pending resolution).

---

## 2. Workstream identity model

### 2.1 Definition

A **Workstream** is a durable logical task thread inside a repo:

```text
Workstream =
  shared objective
  + membership (principals)
  + memory lineage (episodes/handoffs/anchors scoped to it)
  + optional branch/worktree facets
```

It is **not**:
- a chat session
- a git branch alone
- an agent process
- a person

Sessions/agents/branches join a workstream; they do not replace it.

### 2.2 Identity key (resolution order)

When a session starts or an event arrives, resolve workstream by first match:

```text
1) Explicit
   - user/agent sets --workstream / kedger use <slug>
   - pack hydrate declares workstream_id

2) Active local binding
   - this machine+repo has an active workstream for current tty/agent session

3) Structural fingerprint match (same objective lane)
   score candidates by:
     a) current git branch ∈ workstream.primary_branches
     b) overlap(files_in_focus, workstream recent files_touched)
     c) recent handoff HEAD exists for candidate
     d) slug/name lexical match to user goal text (optional)

4) Create new workstream
   - if best score < CREATE_THRESHOLD
   - or signals say objective changed hard
```

### 2.3 Fingerprint features (v1)

```text
WorkstreamFingerprint
- repo_fingerprint
- slug
- primary_branches[]
- seed_goal_text
- seed_entities[]          # files/modules/libs
- recent_files_window[]    # from last 1–3 episodes
- member_principal_ids[]
```

### 2.4 Scoring function (deterministic v1)

```text
score(candidate) =
  3.0 * branch_match
+ 2.0 * file_overlap_ratio          # Jaccard on path set
+ 1.5 * has_recent_handoff_head
+ 1.0 * goal_similarity             # embedding or token overlap
+ 0.5 * same_actor_recently_active

JOIN_THRESHOLD   = 3.0
CREATE_THRESHOLD = 2.0   # if below, create new
AMBIGUOUS_GAP    = 0.7   # if top1-top2 < gap → ask/explicit
```

If ambiguous: do **not** silently merge. Prompt or attach to `unassigned` until explicit.

### 2.5 Hard isolation rules

| Situation | Rule |
|-----------|------|
| Two agents, different goals | separate workstreams |
| Two agents, same goal/branch | same workstream, parallel sessions (`PARALLEL_WITH` handoffs) |
| Same agent switches goal hard | close/pause old workstream working-state; create/switch |
| Branch switch, same objective | stay on same workstream; update `primary_branches` / facet |
| Branch switch, new objective | new workstream |
| File overlap only, goals differ | do **not** auto-join (prevent contamination) |

### 2.6 Lifecycle

```text
active → paused → archived
```

- `active`: can receive ingest + handoff HEAD updates  
- `paused`: hydrate allowed; no silent auto-join unless explicit  
- `archived`: read-only memory lineage  

Commands:

```text
kedger workstream new <slug> --goal "..."
kedger workstream use <slug>
kedger workstream switch <slug>
kedger workstream pause|archive <slug>
kedger workstream status
```

### 2.7 Auto-create heuristic (when no explicit slug)

Create when all are true:

1. no candidate ≥ `JOIN_THRESHOLD`
2. session has a clear goal statement OR ≥ N file edits in a coherent path cluster
3. not inside an active authorized hydrate that already bound a workstream

Slug derivation:

```text
normalize(goal keywords | branch tail | top directory cluster)
e.g. feat/auth-jwt → auth-jwt
     "fix billing tax rounding" → billing-tax-rounding
```

### 2.8 Relation to episodes vs workstreams

Research distinction we keep:

- **Episode boundary** = chapter inside a workstream (topic/state shift)  
- **Workstream identity** = which objective lane the chapter belongs to  

```text
Workstream (objective lane)
  └── Episode e1
  └── Episode e2   ← boundary inside same workstream
  └── Handoff lineage
```

Do not create a new workstream on every episode boundary.

---

## 3. Episode boundary signals (inside a workstream)

Adopted from EST / Nemori / ES-Mem / EM-LLM, adapted for coding agents.

### 3.1 Hard boundaries (always close episode + cognify)

1. `session_end` / `stop` with session terminating  
2. `pre_compact` / context-pressure compact  
3. explicit `kedger handoff` / `kedger cognify`  
4. workstream switch  
5. idle gap ≥ `IDLE_BOUNDARY_MIN` (default 20–30 min)

### 3.2 Soft boundaries (may close episode if confidence high)

1. **Goal shift**: user intent materially changes inside same session  
2. **Surprise / prediction gap**: current events contradict active Anchors or WorkingState expectations (Nemori/EM-LLM style)  
3. **File-cluster shift**: dominant edited path cluster changes (e.g. `auth/*` → `billing/*`) while goal text also shifts  
4. **Cumulative importance**: sum(importance since last episode) ≥ `EPISODE_IMPORTANCE_THRESHOLD`

### 3.3 Non-boundaries (do not split)

- trivial file touch in same cluster  
- routine tool noise  
- short clarifications that continue same goal  
- formatter/lint-only edits

### 3.4 Defaults

```text
IDLE_BOUNDARY_MIN = 25 minutes
EPISODE_IMPORTANCE_THRESHOLD = 3.5   # with importance in [0,1]
FILE_CLUSTER_SHIFT_JACCARD < 0.2 + goal_shift = soft boundary
```

---

## 4. Promotion signals — when something becomes an Anchor

### 4.1 Constitutional rule

> Observations and episodes are cheap.  
> Anchors are expensive, governed, and compact-native.

Promotion is **not** “store every prompt.”  
It is graduation into L3 with provenance + validity.

### 4.2 Confidence ladder (source ranking)

From governed-memory / production practice:

```text
explicit_user_command     > 1.00
explicit_user_judgment_language > 0.90
repeated_pattern_across_episodes > 0.75
tool_verified_outcome          > 0.70
agent_inferred_alone           > 0.40   # insufficient alone for auto-commit
```

### 4.3 Auto-commit vs candidate

| Mode (`promotion`) | Behavior |
|--------------------|----------|
| `conservative` (default recommended) | only explicit commands + explicit judgment language auto-commit; others become candidates |
| `normal` | also auto-commit high-confidence recurrence / tool-verified judgments |

Candidates live in a probation buffer (hot), not as active Anchors, until accepted.

### 4.4 Signal catalog (v1)

#### Tier A — immediate Anchor commit (either mode)

**A1. Explicit remember**
```text
kedger remember decision|reject|constraint|gotcha "..."
```

**A2. Explicit judgment language from user**
Patterns (examples, closed detector list in impl):

- `we decided` / `decide to` / `going with`
- `reject` / `don't use` / `do not use` / `never use`
- `must` / `constraint` / `hard requirement`
- `gotcha` / `don't forget` / `lesson:`

Extract:
- kind
- statement
- reason (if present)
- about entities from nearby files/libs

**A3. Supersession language**
- `instead of X use Y`
- `revert decision`
- `no longer using`

⇒ create/invalidate with `SUPERSEDES` edge.

#### Tier B — candidate promotion (auto-commit only if `promotion=normal` and checks pass)

**B1. Recurrence (RecMem-style)**
```text
same normalized judgment seen in ≥ θ_count independent episodes
θ_count default = 3 (task-oriented coding)
similarity ≥ 0.7 on normalized statement/entities
```

**B2. Tool-verified outcome**
- tests fail repeatedly under approach X → candidate rejection(X)
- migration/command succeeds and user affirms → candidate decision

**B3. Prediction error / surprise (Nemori-style)**
- active Anchor or WorkingState predicted approach X
- reality contradicts X with high importance
- create candidate invalidation/new judgment

**B4. Reflection threshold (Generative Agents-style)**
```text
importance_sum since last reflection ≥ REFLECT_THRESHOLD (default 4.0)
AND episode_count_since ≥ 2
⇒ reflection pass may propose Anchor candidates (not silent commit in conservative mode)
```

#### Tier C — never auto-promote

- raw speculative agent brainstorming without user uptake  
- one-off exploratory prompts  
- secrets, credentials, private personal data  
- transient “try this?” without confirmation  
- file-edit churn without judgment

### 4.5 Pre-commit validation gate (SSGM-inspired)

Before an Anchor becomes `active`:

```text
1) schema validate (MEMORY_SCHEMAS_V1)
2) redact check
3) contradiction check against active Anchors
   - if contradicts: require supersession path (invalid_at + SUPERSEDES)
4) provenance present (actor + source + episode/obs when available)
5) statement normalized/deduped
6) visibility/shareable policy respected
```

If gate fails → remain candidate or reject with reason.

### 4.6 Kind-specific promotion policy

| Kind | Auto-commit allowed? | Notes |
|------|----------------------|-------|
| `constraint` | only Tier A (or repeated Tier B with high confidence) | highest trust bar |
| `rejection` | Tier A; Tier B recurrence/tool-fail | critical for no-relitigation |
| `decision` | Tier A; Tier B recurrence/affirmation | must support supersession |
| `gotcha` | Tier A; Tier B recurrence ≥ 2 costly failures | keep short |
| `goal` / `next_step` | usually WorkingState; promote Anchor only if durable across sessions | often workstream-scoped |
| `open_question` | optional; expire when resolved | not repo-global by default |

### 4.7 Probation buffer (dual-buffer consolidation)

From survey guidance (hot buffer → long-term):

```text
candidate_anchor
  status: probation
  created_at
  evidence_ids[]
  expires_at (default +7d if not accepted)
```

Promotion out of probation:

- explicit accept, or
- recurrence threshold hit, or
- user affirms in later turn

Else expire/discard from active consideration (history may remain for audit).

---

## 5. How workstream identity + promotion interact

```text
event
  → resolve workstream (identity algorithm)
  → append L0 under that workstream
  → update L1 if state delta
  → emit promotion signals scoped to that workstream
  → on episode boundary: cognify within workstream
  → Anchors get workstream_id (or null if repo-global shareable constraint)
  → sealed handoff updates that workstream HEAD only
```

Critical privacy implication:

- promotion never leaks into another workstream’s pack  
- repo-global Anchors require explicit `shareable=true` path  

---

## 6. Recommended defaults (lock)

```text
workstream.join_threshold = 3.0
workstream.create_threshold = 2.0
workstream.ambiguous_gap = 0.7
episode.idle_boundary_min = 25m
episode.importance_threshold = 3.5
promotion.mode = conservative
promotion.recurrence_count = 3
promotion.recurrence_similarity = 0.7
promotion.reflect_threshold = 4.0
promotion.probation_days = 7
```

---

## 7. Concrete examples

### Example A — same task, new session
- branch `feat/auth`, files `auth/*`, prior handoff exists  
- score high → join `ws_auth-refactor`  
- hydrate that workstream pack  

### Example B — parallel different task
- agent B on `billing/*`  
- low overlap with auth workstream → create/join `ws_billing-tax`  
- no auth Anchors mixed into working state  

### Example C — rejection promotion
- user: “Don’t use Mongo here, ops cost”  
- Tier A2 → Anchor(rejection) immediate  
- about entities from nearby discussion  

### Example D — recurrence promotion
- three episodes independently conclude “avoid `.cmd` wrappers on Windows”  
- Tier B1 candidate → in `normal` mode auto-commit gotcha/constraint  
- in `conservative`, surface candidate for accept  

### Example E — supersession
- old Anchor: decision cookie sessions  
- new user judgment: use JWT instead  
- commit new decision + invalidate old via SUPERSEDES  

---

## 8. Implementation checklist

### Workstream module
- [ ] resolver with scored candidates  
- [ ] ambiguous handling (no silent merge)  
- [ ] auto-create slugger  
- [ ] active binding per agent session  
- [ ] pause/archive lifecycle  

### Promotion module
- [ ] Tier A detectors (explicit + judgment language)  
- [ ] Tier B recurrence index  
- [ ] validation gate + supersession  
- [ ] probation buffer  
- [ ] conservative/normal modes  

### Telemetry (for later tuning)
- [ ] join vs create rates  
- [ ] ambiguous resolution count  
- [ ] auto-promote precision (manual overrides/rejects)  
- [ ] contamination incidents (cross-workstream bleed)

---

## 9. Non-goals for v1

- Perfect NLP topic segmentation model as hard dependency  
- Token-level surprise from model logits (EM-LLM) as required sensor  
- Fully autonomous semantic dreaming without provenance  
- Auto repo-global promotion of constraints without explicit shareable path  

Those can be optional enhancers later. Deterministic + light detectors first.

---

## 10. Lock statements

1. **Workstream is the objective-lane identity; sessions/branches/agents only join it.**  
2. **Resolve by explicit → binding → scored fingerprint → create; never silent ambiguous merge.**  
3. **Episode boundaries ≠ workstream changes.**  
4. **Promotion is governed graduation to Anchors, ranked by source confidence.**  
5. **Conservative default: explicit judgments commit; recurrence/surprise create candidates.**  
6. **All promotion/validation is workstream-scoped unless explicitly shareable.**  

---

## 11. Changelog

| Date | Change |
|------|--------|
| 2026-08-08 | Initial research-informed lock for workstream identity algorithm and Anchor promotion signals. |
