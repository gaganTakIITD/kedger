# Parallel Compose & Hook Event Mapping v1

> **Status:** Design lock (deep-read, research-informed)  
> **Date:** 2026-08-08  
> **Depends on:** `OPEN_SOURCE_MEMORY_ARCHITECTURE.md`, `MEMORY_SCHEMAS_V1.md`, `WORKSTREAM_AND_PROMOTION_V1.md`  
> **Honesty note:** We cannot literally read 200+ full papers in one pass. This lock is based on **close reading** of the strongest recent primary sources + official IDE hook specifications (listed in §0), not keyword skimming alone.

---

## 0. Sources actually read / heavily extracted

### Parallel memory / conflict / compose
| Source | What we took after reading |
|--------|----------------------------|
| **StateFuse (Volkov et al., 2026)** arXiv:2607.05844 | Immutable history + **explicit Conflict objects**; resolution is **projection-time**, must not rewrite replicated base; dual correction handles (`claim_id` / semantic `claim_ref`); silent overwrite is the failure mode to avoid |
| **TOKI (Wang, 2026)** arXiv:2606.06240 | Contradiction resolution = write-time concurrency control; four typed operators: **LWW**, **evidence-weighted**, **await-confirmation**, **per-rule**; dual-row **current + audit**; keep losing fact; LLM-judge needs **keyed logging** or you get replay inconsistency / belief-drift / audit erasure |
| **Governed Shared Memory / MemClaw (Margalit et al., 2026)** arXiv:2606.24535 | Four fleet failures: unauthorized leakage, stale propagation, contradiction persistence, provenance collapse; temporal supersession + scoped retrieval + provenance as first-class; live systems fail when scope enforcement is asymmetric across read paths |
| **Selective Memory / supersession chains (2026)** arXiv:2603.15994 | Prefer supersession links over overwrite; version chains enable temporal queries; archive old, don’t destroy |
| **CRDT multi-agent guides (crdt-merge, Silk, agentcrdt)** | Two-layer pattern: (1) convergent append/collect of claims, (2) deterministic projection/resolver; contradictions can be first-class events |
| **resolver-oss / typed conflict taxonomy** | Conflict kinds: contradiction, refinement, complementary, temporal_scope, duplicate → operators ADD / UPDATE / DEDUPE / SUPERSEDE / ESCALATE |

### Hook event systems (primary docs)
| Source | What we took |
|--------|--------------|
| **Claude Code Hooks** (`code.claude.com/docs/en/hooks`) | Cadence classes: session / turn / tool; `SessionStart` inject via `additionalContext`; `PreCompact` can block; `Stop` can continue; common fields `session_id`, `transcript_path`, `cwd`; tool events carry `tool_name/input/response` |
| **Cursor Hooks** (`cursor.com/docs/hooks`) | Closely analogous events (`sessionStart`, `beforeSubmitPrompt`, `afterFileEdit`, `preCompact`, `afterAgentResponse`, `stop`); stdin JSON → command hooks; `stop` can return `followup_message`; cloud agents defer some sessionStart semantics |

---

## PART A — Parallel compose & conflict (same workstream, multiple agents/sessions)

### A1. Problem statement (from the papers)

When two agents/sessions work the **same workstream** in parallel, they can:

1. append compatible facts (complementary)
2. refine the same fact (refinement)
3. duplicate the same fact (dedupe)
4. contradict on the same key (true conflict)
5. write temporally scoped truths that look contradictory if time is ignored

Research consensus after close reading:

> **Do not silently collapse disagreement at write time.**  
> Preserve history + provenance; resolve in a typed, auditable way; expose conflicts in the hydrate projection when unresolved.

StateFuse’s key empirical nuance: preserving conflicts does not always raise raw accuracy, but it **does** enable safer abstention and correction versus collapsed overwrite surfaces.

### A2. Architectural split we adopt (StateFuse + CRDT two-layer)

```text
Layer 1 — Replicated / append substrate (immutable ops)
  - every Anchor write, supersession, evidence, episode, handoff relation
  - convergent collect (order-insensitive union of ops)
  - never erase losers

Layer 2 — Projection / compose resolver (deterministic policy)
  - builds WorkingState view + HandoffPack view for a consumer
  - may choose winner, union, or escalate/abstain
  - CANNOT rewrite Layer-1 history
```

This matches:

- StateFuse “bounded projection authority”
- event-sourcing / CQRS
- crdt-merge Layer1 collect + Layer2 ContextMerge

### A3. Conflict taxonomy (typed)

For two claims `A` and `B` on a comparable key:

| Type | Meaning | Default operator |
|------|---------|------------------|
| `duplicate` | same normalized statement/entities | `DEDUPE` (keep higher provenance/confidence; link both) |
| `refinement` | B specializes/extends A without negating | `UPDATE` / absorb into evolved Anchor + evolution note |
| `complementary` | different facets, both useful | `ADD` both; link `LINKED_TO` / `PARALLEL_WITH` |
| `temporal_scope` | both true in different valid intervals | keep both with `valid_at/invalid_at`; no false contradiction |
| `contradiction` | same key, incompatible object, overlapping validity | typed resolve (below) or `ESCALATE` |

**Comparable key (v1):**

```text
key = (repo_fingerprint, kind, normalized_statement_or_about_signature)
```

For decisions/rejections about entities, prefer:

```text
key = (repo, kind, sorted(about.normalized_key[]))
```

when statement text varies but target is the same (e.g. “don’t use Mongo” vs “reject MongoDB”).

### A4. Compose modes for parallel handoffs

When hydrating a workstream with multiple recent packs/sessions:

| Mode | Behavior | When |
|------|----------|------|
| `pin` | use one actor/pack only | user/agent explicitly pins |
| `primary` | latest handoff HEAD by `created_at` + repo-global anchors | default single-consumer continue |
| `compose` | merge Layer-1 claims via typed operators; build one projection | multi-agent same task |
| `lineage` | latest + selected ancestor anchors | audit / “how did we get here” |

**Default for multi-writer same workstream:** `compose` for Anchors; working-state uses conflict-preserving merge (below).

### A5. Typed resolve operators for Anchors (TOKI-informed)

Map TOKI’s four heuristics into our product, with **audit row always kept** (loser → `status=superseded` or `disputed`, never deleted).

#### Operator matrix

| Operator | Our name | Isolation/guard idea | Use when |
|----------|----------|----------------------|----------|
| `⊕_t` LWW | `SUPERSEDE_BY_TIME` | later `valid_at`/`created_at` wins if same key | low-stakes working notes, gotchas with clear recency |
| `⊕_p` evidence-weighted | `SUPERSEDE_BY_EVIDENCE` | higher confidence + stronger source ladder wins | tool-verified vs inferred |
| `⊕_?` await-confirm | `ESCALATE` | do not auto-pick; mark `disputed` | high-stakes constraints/decisions disagree |
| `⊕_c` per-rule | `POLICY` | kind-specific hard rules | constraints/rejections policy below |

#### Kind-specific policy (`⊕_c`) — locked defaults

| Kind | Parallel contradiction policy |
|------|-------------------------------|
| `constraint` | **ESCALATE** (never silent LWW) |
| `rejection` | evidence-weighted if one side tool-verified; else **ESCALATE** |
| `decision` | if explicit user judgment vs agent-inferred → user wins; if two explicit users disagree → **ESCALATE** |
| `gotcha` | LWW/evidence-weighted OK |
| `goal` / `next_step` | do not smash; keep both as open parallel working intents or escalate |
| `open_question` | union (ADD) |

This directly implements TOKI’s lesson that high-stakes strategy must declare its contract, and StateFuse’s lesson that early collapse is unsafe.

### A6. WorkingState compose (parallel agents)

WorkingState is **not** a single LWW blob under parallel writers.

Compose fields:

| Field | Merge |
|-------|-------|
| `goal` | if equal/compatible → keep; if conflict → `goals_conflict[]` + escalate marker |
| `files_in_flight` | set-union |
| `open_questions` | set-union |
| `blockers` | set-union |
| `last_user_ask` | LWW by timestamp **plus** keep prior in `recent_asks[]` (audit) |
| `active_branch` | multi-value if different; projection may show primary branch + others |
| `active_anchor_ids` | union of active anchors after Anchor compose |

Hydrate must surface:

```text
conflicts[]: [{key, claims[], policy, status: disputed|auto_resolved}]
```

so the next agent can abstain or ask (StateFuse abstention value).

### A7. Handoff relation graph under parallelism

When agent A and agent B both produce packs on same workstream:

```text
hf_A  --PARALLEL_WITH--  hf_B
hf_compose --COMPILED_FROM--> hf_A, hf_B
hf_compose --CONTINUES--> previous HEAD (if any)
```

Rules:

1. Do not delete `hf_A`/`hf_B` when composing  
2. New HEAD may point to `hf_compose` or remain actor-specific with a workstream compose view  
3. Capability/ACL still gates who can read each pack (Governed Shared Memory leakage lesson)

### A8. Failure modes we explicitly defend against

From MemClaw + TOKI + StateFuse:

| Failure | Defence in our design |
|---------|------------------------|
| Unauthorized leakage | workstream capability + sealed `.kxp` recipients |
| Stale propagation | temporal `invalid_at` + supersession chains |
| Contradiction persistence (hidden) | explicit `disputed` / Conflict projection |
| Provenance collapse | required provenance on Anchors; audit losers retained |
| Replay inconsistency (LLM judge) | v1 prefers deterministic operators; if LLM judge used, log keyed verdict `(conflict_id, judge_input_hash, winner_id, model, prompt_version)` |
| Audit erasure | never delete superseded Anchors |
| Asymmetric scope bugs | every read path (hydrate/inspect/why/get-by-id) must enforce ACL |

### A9. Parallel compose algorithm (v1)

```text
function compose_workstream(ws_id, pack_ids|latest_parallel):
  ops = collect Layer-1 ops from selected packs/sessions
  anchors = group_by_comparable_key(ops.anchors)
  resolved = []
  conflicts = []
  for key, claims in anchors:
      kind = conflict_type(claims)
      if kind in {duplicate, refinement, complementary, temporal_scope}:
          resolved += apply_soft_merge(kind, claims)  # ADD/UPDATE/DEDUPE/time-split
      else:  # contradiction
          op = policy_for(claims.kind)  # ESCALATE / EVIDENCE / LWW
          if op == ESCALATE:
              conflicts += ConflictSet(claims)
              # keep all claims visible as disputed/active-candidates
          else:
              winner, losers = apply(op, claims)
              mark_supersession(winner, losers)  # audit retained
              resolved += winner
  working = merge_working_states(ops.working)
  episodes = take_recent_unique(ops.episodes, n=3)
  pack = compile_handoff(resolved, working, episodes, conflicts, budget)
  seal(pack)
  return pack
```

### A10. Lock statements — parallel compose

1. Layer-1 history is append/immutable; compose is a projection.  
2. Conflicts are first-class; silent overwrite is forbidden for constraints and contested decisions.  
3. Losers remain as superseded/audit rows.  
4. WorkingState merges by field policy, not whole-doc LWW.  
5. Hydrate surfaces unresolved conflicts for abstention.  
6. All compose reads are capability-scoped.

---

## PART B — Hook event mapping (IDE → Observation / engine actions)

### B1. Design principle

Hooks are sensors + boundary triggers.  
They must map into our **normalized ObservationType** and engine actions, not leak IDE-specific names into the core store.

```text
IDE event → normalize(adapter) → Observation(+meta) → router/cognify/hydrate
```

### B2. Cadence classes (from Claude Code docs)

| Cadence | Meaning | Our use |
|---------|---------|---------|
| Session-level | start/end once | bind workstream; hydrate; final cognify |
| Turn-level | each user/agent turn | L0 prompts/responses; soft state updates |
| Tool-level | each tool call | file/tool observations; noisy, budgeted |
| Compact-level | before/after compact | **must externalize Anchors before loss** |

### B3. v1 minimum hook set (must implement)

These are the minimum events adapters must cover (name via Claude / Cursor equivalents):

| Normalized engine event | Claude Code | Cursor | Required action |
|-------------------------|-------------|--------|-----------------|
| `SESSION_START` | `SessionStart` | `sessionStart` | resolve workstream; **authorized hydrate inject** |
| `USER_PROMPT` | `UserPromptSubmit` | `beforeSubmitPrompt` | L0 obs; Tier-A judgment detect; L1 delta |
| `AGENT_RESPONSE` | (from Stop `last_assistant_message` / transcript) | `afterAgentResponse` | L0 obs (summarized); signal extract |
| `FILE_EDIT` | `PostToolUse` match Edit/Write | `afterFileEdit` | L0 file_edit; update files_in_flight |
| `TOOL_FAIL` | `PostToolUseFailure` | `postToolUseFailure` | L0 error; possible rejection candidate |
| `PRE_COMPACT` | `PreCompact` | `preCompact` | **cognify now** (Anchors first) before compact |
| `TURN_STOP` | `Stop` | `stop` | soft boundary candidate; optional cognify if importance high |
| `SESSION_END` | `SessionEnd` | `sessionEnd` | hard cognify + seal handoff HEAD |

### B4. Optional v1.1 hooks (useful, not required)

| Engine event | Claude | Cursor | Use |
|--------------|--------|--------|-----|
| `TOOL_CALL` | `PostToolUse` (non-edit) | `postToolUse` / shell/MCP after* | denser L0 (often dropped) |
| `SUBAGENT_STOP` | `SubagentStop` | `subagentStop` | treat as nested episode fragment |
| `POST_COMPACT` | `PostCompact` | — | verify Anchors survived; reinject if needed |

### B5. Normalized Observation mapping details

#### SESSION_START
Inputs commonly available: `session_id`, `cwd`, `source` (`startup|resume|clear|compact|fork`), transcript path.  
Actions:
1. compute `repo_fingerprint` from cwd  
2. resolve workstream  
3. if capability ok → hydrate compile → return IDE inject payload  
   - Claude: `hookSpecificOutput.additionalContext`  
   - Cursor: sessionStart context injection mechanism / write secure temp only if needed  

**Important (Cursor cloud caveat):** sessionStart may be deferred in some cloud environments; engine must also support explicit `kedger hydrate` fallback.

#### USER_PROMPT
Capture:
- summary text (redacted)
- full text only in private_raw payload_ref if privacy allows  
Detect Tier-A promotion language immediately.

#### FILE_EDIT
Capture:
- repo-relative path (never absolute machine path as entity name)
- coarse change count if available  
Update L1 `files_in_flight` (upsert, capped).

Skip noise:
- empty path
- 0-change edits
- generated/vendor paths (configurable denylist)

#### PRE_COMPACT
This is the **most important boundary hook** (Claude Code community + Anthropic compaction lessons).

Actions (synchronous, best-effort, fast path):
1. cognify current span  
2. upsert Anchors/Evidence  
3. seal/update handoff  
4. only then allow compact  

If cognify fails: still attempt Anchor emergency snapshot of WorkingState + last judgment candidates.

Claude: exit 2 can block compact — use only if emergency snapshot fails and policy says hard-fail.

#### TURN_STOP / SESSION_END
- TURN_STOP: maybe cognify if importance threshold hit  
- SESSION_END: always cognify + seal  

### B6. Adapter contract

Each IDE adapter implements:

```text
parse(stdin_json) -> EngineEvent
to_observation(EngineEvent) -> Observation
side_effects(EngineEvent) -> {hydrate_text?, cognify?, grant_checks}
emit_ide_output(...) -> stdout JSON for that IDE
```

Core engine never imports Cursor/Claude types.

### B7. What not to do with hooks

| Anti-pattern | Why |
|--------------|-----|
| Log every tool payload into Anchors | contamination / privacy / budget death |
| Hydrate giant markdown into SessionStart | context rot; violates sealed/private model |
| Depend on transcript_path being fully flushed | Claude docs: transcript may lag; prefer event fields like last_assistant_message |
| Silent cross-workstream write from file overlap only | breaks identity rules |
| Use Stop followup loops to “keep chatting for memory” | unstable; cognify instead |

### B8. Lock statements — hooks

1. v1 minimum event set is the 8 rows in §B3.  
2. `PRE_COMPACT` and `SESSION_END` are hard cognify boundaries.  
3. `SESSION_START` is the hydrate injection point (with CLI fallback).  
4. Store only normalized ObservationTypes; IDE names stay in adapter meta.  
5. File entities are repo-relative.  
6. Hook injects ephemeral authorized context only — not plaintext canonical memory files.

---

## PART C — Combined runtime picture

```text
Agent A (Cursor)          Agent B (Claude)     same workstream
   hooks                     hooks
     │                         │
     ▼                         ▼
 normalize adapter        normalize adapter
     │                         │
     └────────────┬────────────┘
                  ▼
            ENGINE CORE
     L0 ingest → L1 update → promotion signals
                  │
        PRE_COMPACT / SESSION_END
                  ▼
               cognify
                  │
        Layer-1 ops (immutable)
                  │
        compose projection (if parallel)
                  │
        seal .kxp (recipients only)
                  │
        next SESSION_START hydrate (authorized)
```

---

## PART D — Defaults to implement

```text
compose.default_mode = compose for multi-writer, primary for single-writer
compose.constraint_policy = ESCALATE
compose.decision_policy = user_over_agent else ESCALATE if dual-explicit
compose.rejection_policy = EVIDENCE else ESCALATE
compose.keep_audit_losers = true
hooks.min_set = SESSION_START, USER_PROMPT, AGENT_RESPONSE, FILE_EDIT,
                TOOL_FAIL, PRE_COMPACT, TURN_STOP, SESSION_END
hooks.pre_compact = hard_cognify
hooks.session_start = hydrate_inject
```

---

## PART E — Validation scenarios

1. **Parallel complementary:** A edits auth tests, B edits auth middleware → compose unions files + episodes; no false conflict.  
2. **Parallel contradiction on constraint:** A “must use Postgres”, B “must use MySQL” → disputed ConflictSet, hydrate shows both, no silent winner.  
3. **Supersession:** B later confirms Postgres with user explicit → SUPERSEDES, audit keeps MySQL claim.  
4. **PreCompact:** force compact mid-session → Anchors+handoff exist even if transcript summary is lossy.  
5. **ACL:** third principal cannot hydrate compose pack.  
6. **Hook normalization:** Cursor `afterFileEdit` and Claude `PostToolUse(Write)` produce same ObservationType `file_edit`.

---

## PART F — Still deferred

- Full CRDT wire protocol between machines (v1 can compose locally from sealed packs + shared store ops)
- LLM-as-judge conflict classifier as default (optional later; must log keyed verdicts if enabled)
- Antigravity/Windsurf adapter tables (same normalized events)
- Shareable-anchor auto policy beyond explicit `shareable=true`

---

## Changelog

| Date | Change |
|------|--------|
| 2026-08-08 | Initial deep-read lock for parallel compose/conflict operators and IDE hook→engine event mapping. |
