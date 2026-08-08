# Kedger Memory Schemas v1 (Locked)

> **Status:** Design lock — implementation constitution  
> **Product:** Kedger  
> **Schema family:** `kedger.memory.v1`  
> **Date:** 2026-08-08  
> **Depends on:** `docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`

This file freezes the exact record shapes for the layered store + graph + sealed handoff.

**Rules for this version**

- Unknown fields must be rejected by writers (`additionalProperties: false` mentally)
- Timestamps are ISO-8601 UTC (`YYYY-MM-DDTHH:MM:SSZ` or with fractional seconds)
- IDs are prefixed ULID strings (sortable + debuggable)
- Canonical store is structured records, not markdown
- Anchors are compact-native; Evidence/Episodes/Raw are budgeted

---

## 0. Common primitives

### 0.1 ID prefixes

| Prefix | Record |
|--------|--------|
| `anc_` | Anchor |
| `evd_` | Evidence |
| `ep_` | Episode |
| `ent_` | Entity |
| `obs_` | Observation (L0) |
| `ws_` | Workstream |
| `wk_` | WorkingState |
| `hf_` | HandoffPack |
| `cap_` | Capability |
| `pr_` | Principal |
| `eg_` | Graph edge |

Pattern:

```text
^[a-z]{2,4}_[0-9A-HJKMNP-TV-Z]{26}$
```

(ULID alphabet after prefix)

### 0.2 Enums

```text
AnchorKind:
  decision | rejection | constraint | gotcha | goal | next_step | open_question

AnchorStatus:
  active | superseded | disputed | archived

Visibility:
  private_raw | workstream_private | repo_shared_safe | ephemeral_render

ObservationType:
  session_start | user_prompt | agent_response | file_edit | tool_call
  | tool_result | error | stop | session_end | pre_compact | note

EntityType:
  repo | workstream | person | agent_tool | file | module | service
  | api | table | library | pattern | error_class | test | pr | commit | other

EdgeType:
  MENTIONS | DERIVES | RELATES_TO | ABOUT | SUPERSEDES | SUPPORTS
  | CONTRADICTS | NEXT_IN | IN_WORKSTREAM | IN_COMMUNITY
  | COMPILED_INTO | LINKED_TO | CONTINUES | PARALLEL_WITH
  | BRANCH_OF | SAME_WORKSTREAM | MERGES_TO | DERIVES_FROM_SESSIONS

CapabilityPermission:
  read_hydrate | append | admin

PromotionSource:
  explicit | auto_signal | reflection | import
```

### 0.3 Shared objects

```json
{
  "Provenance": {
    "episode_id": "ep_...",
    "observation_ids": ["obs_..."],
    "actor_principal_id": "pr_...",
    "session_id": "string",
    "agent_tool": "cursor|claude_code|antigravity|other",
    "source": "explicit|auto_signal|reflection|import",
    "repo_fingerprint": "string",
    "branch": "string|null",
    "workstream_id": "ws_...|null"
  }
}
```

```json
{
  "EntityRef": {
    "entity_id": "ent_...",
    "entity_type": "file",
    "name": "auth/session.ts"
  }
}
```

---

## 1. Observation (L0)

Short-lived sensor record. Not durable memory by itself.

```json
{
  "schema_version": "kedger.memory.v1",
  "id": "obs_01HXYZ...",
  "type": "user_prompt",
  "ts": "2026-08-08T18:01:00Z",
  "repo_fingerprint": "rf_...",
  "workstream_id": "ws_...",
  "session_id": "sess_...",
  "actor_principal_id": "pr_...",
  "agent_tool": "cursor",
  "summary": "Reject cookie sessions; use JWT",
  "payload_ref": "raw://span/...",
  "entity_hints": [
    {"entity_type": "file", "name": "auth/session.ts"}
  ],
  "importance": 0.72,
  "redacted": true,
  "visibility": "private_raw"
}
```

### Required
`schema_version, id, type, ts, repo_fingerprint, session_id, actor_principal_id, summary, visibility`

### Constraints
- `importance` ∈ `[0,1]`
- payload bodies should live out-of-record when large (`payload_ref`)
- never placed into sealed handoff by default

---

## 2. WorkingState (L1)

One mutable document per workstream.

```json
{
  "schema_version": "kedger.memory.v1",
  "id": "wk_01HXYZ...",
  "workstream_id": "ws_01HXYZ...",
  "repo_fingerprint": "rf_...",
  "goal": "Replace cookie sessions with JWT auth",
  "last_user_ask": "Reject cookie sessions; use JWT",
  "files_in_flight": ["auth/session.ts", "auth/middleware.ts"],
  "open_questions": ["How to rotate refresh tokens?"],
  "blockers": [],
  "active_branch": "feat/auth",
  "active_anchor_ids": ["anc_...", "anc_..."],
  "updated_at": "2026-08-08T18:05:00Z",
  "updated_by_session_id": "sess_...",
  "visibility": "workstream_private"
}
```

### Required
`schema_version, id, workstream_id, repo_fingerprint, goal, updated_at, visibility`

### Constraints
- keep tiny: target serialized size ≤ 4KB
- upsert semantics (not append-only)
- `files_in_flight` max 40 repo-relative paths

---

## 3. Episode (L2)

Compressed chapter created on boundary/cognify.

```json
{
  "schema_version": "kedger.memory.v1",
  "id": "ep_01HXYZ...",
  "repo_fingerprint": "rf_...",
  "workstream_id": "ws_...",
  "session_ids": ["sess_a", "sess_b"],
  "time_start": "2026-08-08T17:40:00Z",
  "time_end": "2026-08-08T18:05:00Z",
  "branch": "feat/auth",
  "summary": "Moved auth from cookie sessions toward JWT after CSRF failures.",
  "failed_approaches": ["cookie sessions"],
  "next_steps": ["implement refresh-token rotation"],
  "files_touched": ["auth/session.ts", "auth/middleware.ts"],
  "anchor_ids": ["anc_reject_cookies", "anc_use_jwt", "anc_next_refresh"],
  "entity_ids": ["ent_file_auth_session", "ent_lib_cookies"],
  "observation_span": {
    "from_ts": "2026-08-08T17:40:00Z",
    "to_ts": "2026-08-08T18:05:00Z",
    "count": 26
  },
  "salient_evidence_ids": ["evd_..."],
  "importance": 0.81,
  "visibility": "workstream_private",
  "created_at": "2026-08-08T18:05:01Z"
}
```

### Required
`schema_version, id, repo_fingerprint, workstream_id, time_start, time_end, summary, created_at, visibility`

### Constraints
- `summary` ≤ 500 chars recommended (hard max 1200)
- `files_touched` max 40
- `failed_approaches` / `next_steps` max 20 each
- created only by cognify/boundary (or explicit import)

---

## 4. Anchor (L3) — canonical durable memory

```json
{
  "schema_version": "kedger.memory.v1",
  "id": "anc_01HXYZ...",
  "kind": "rejection",
  "statement": "Do not use cookie sessions for auth",
  "reason": "CSRF brittleness and failing integration tests",
  "status": "active",
  "about": [
    {"entity_id": "ent_...", "entity_type": "file", "name": "auth/session.ts"},
    {"entity_id": "ent_...", "entity_type": "library", "name": "cookies"}
  ],
  "repo_fingerprint": "rf_...",
  "workstream_id": "ws_...",
  "visibility": "workstream_private",
  "importance": 0.93,
  "valid_at": "2026-08-08T18:04:00Z",
  "invalid_at": null,
  "created_at": "2026-08-08T18:05:01Z",
  "updated_at": "2026-08-08T18:05:01Z",
  "supersedes": [],
  "superseded_by": null,
  "provenance": {
    "episode_id": "ep_...",
    "observation_ids": ["obs_..."],
    "actor_principal_id": "pr_...",
    "session_id": "sess_...",
    "agent_tool": "cursor",
    "source": "auto_signal",
    "repo_fingerprint": "rf_...",
    "branch": "feat/auth",
    "workstream_id": "ws_..."
  },
  "shareable": false
}
```

### Required
`schema_version, id, kind, statement, status, repo_fingerprint, visibility, importance, valid_at, created_at, updated_at, provenance, shareable`

### Constraints
- `statement` one sentence; max 240 chars
- `reason` max 480 chars
- `about` max 12 entity refs
- if `status=superseded` then `invalid_at` and `superseded_by` required
- `shareable=true` only allowed with `visibility=repo_shared_safe`
- repo-global anchors may set `workstream_id=null`

### Survival rank (for hydrate)
`constraint > rejection > decision > goal > next_step > open_question > gotcha`

---

## 5. Evidence

```json
{
  "schema_version": "kedger.memory.v1",
  "id": "evd_01HXYZ...",
  "supports_anchor_id": "anc_...",
  "snippet": "CSRF failures reproduced on cookie session path in auth tests",
  "source_ref": "obs_...",
  "weight": 0.7,
  "created_at": "2026-08-08T18:05:01Z",
  "visibility": "workstream_private"
}
```

### Required
`schema_version, id, supports_anchor_id, snippet, source_ref, weight, created_at, visibility`

### Constraints
- `snippet` max 280 chars
- droppable under budget; must not be required to understand Anchor

---

## 6. Entity

```json
{
  "schema_version": "kedger.memory.v1",
  "id": "ent_01HXYZ...",
  "entity_type": "file",
  "name": "auth/session.ts",
  "normalized_key": "file:auth/session.ts",
  "repo_fingerprint": "rf_...",
  "aliases": ["session.ts"],
  "created_at": "2026-08-08T17:41:00Z",
  "updated_at": "2026-08-08T18:05:01Z"
}
```

### Required
`schema_version, id, entity_type, name, normalized_key, repo_fingerprint, created_at, updated_at`

### Constraints
- `normalized_key` unique per repo
- file names are repo-relative POSIX paths

---

## 7. Graph Edge

```json
{
  "schema_version": "kedger.memory.v1",
  "id": "eg_01HXYZ...",
  "edge_type": "ABOUT",
  "from_id": "anc_...",
  "to_id": "ent_...",
  "repo_fingerprint": "rf_...",
  "workstream_id": "ws_...",
  "valid_at": "2026-08-08T18:04:00Z",
  "invalid_at": null,
  "created_at": "2026-08-08T18:05:01Z",
  "meta": {
    "weight": 1.0,
    "note": null
  }
}
```

### Required
`schema_version, id, edge_type, from_id, to_id, repo_fingerprint, created_at, valid_at`

### Temporal edges
`SUPERSEDES`, `ABOUT` (when judgment changes), `RELATES_TO` conflicts use `invalid_at` rather than delete.

### Allowed endpoints (v1)

| EdgeType | from → to |
|----------|-----------|
| MENTIONS | Episode → Entity |
| DERIVES | Episode → Anchor |
| ABOUT | Anchor → Entity |
| SUPERSEDES | Anchor → Anchor |
| SUPPORTS | Evidence\|Anchor → Anchor |
| CONTRADICTS | Anchor → Anchor |
| LINKED_TO | Anchor → Anchor |
| NEXT_IN | Episode → Episode |
| IN_WORKSTREAM | * → Entity(workstream) or Workstream id |
| COMPILED_INTO | Anchor\|Episode\|WorkingState → HandoffPack |
| CONTINUES / PARALLEL_WITH / BRANCH_OF | HandoffPack → HandoffPack |

---

## 8. Workstream

```json
{
  "schema_version": "kedger.memory.v1",
  "id": "ws_01HXYZ...",
  "repo_fingerprint": "rf_...",
  "name": "auth-refactor",
  "slug": "auth-refactor",
  "status": "active",
  "primary_branches": ["feat/auth"],
  "member_principal_ids": ["pr_maya", "pr_gagan"],
  "created_at": "2026-08-08T16:00:00Z",
  "updated_at": "2026-08-08T18:05:01Z",
  "visibility": "workstream_private"
}
```

### Required
`schema_version, id, repo_fingerprint, name, slug, status, member_principal_ids, created_at, updated_at, visibility`

---

## 9. Capability

```json
{
  "schema_version": "kedger.memory.v1",
  "id": "cap_01HXYZ...",
  "grantee_principal_id": "pr_gagan",
  "issuer_principal_id": "pr_maya",
  "scope": {
    "type": "workstream",
    "workstream_id": "ws_...",
    "handoff_id": null
  },
  "permissions": ["read_hydrate", "append"],
  "created_at": "2026-08-08T18:10:00Z",
  "expires_at": null,
  "revoked_at": null,
  "issuer_signature": "base64..."
}
```

### Required
`schema_version, id, grantee_principal_id, issuer_principal_id, scope, permissions, created_at, issuer_signature`

### Scope.type
`workstream | handoff | repo_shared`

---

## 10. Principal

```json
{
  "schema_version": "kedger.memory.v1",
  "id": "pr_01HXYZ...",
  "display_name": "Maya",
  "public_key": "base64...",
  "device_id": "dev_...",
  "created_at": "2026-08-01T10:00:00Z"
}
```

### Required
`schema_version, id, display_name, public_key, created_at`

---

## 11. HandoffPack payload (L4 inner structured content)

This is the **plaintext structured payload** before sealing into `.kxp`.

```json
{
  "schema_version": "kedger.memory.v1",
  "id": "hf_01HXYZ...",
  "repo_fingerprint": "rf_...",
  "workstream_id": "ws_...",
  "branch": "feat/auth",
  "session_ids": ["sess_..."],
  "from_principal_id": "pr_maya",
  "to_scope": "workstream",
  "created_at": "2026-08-08T18:05:02Z",
  "parent_handoff_id": "hf_previous",
  "related_handoff_ids": [],
  "relations": [
    {"edge_type": "CONTINUES", "to_id": "hf_previous"}
  ],
  "anchors": [
    {"$ref_inline": "Anchor objects ranked, active-first"}
  ],
  "working": {"$ref_inline": "WorkingState snapshot"},
  "episode_digests": [
    {"$ref_inline": "Episode objects (1..3)"}
  ],
  "evidence": [],
  "budget": {
    "max_bytes": 32768,
    "used_bytes": 9120,
    "dropped": ["older_episodes", "evidence"]
  },
  "content_hash": "sha256:..."
}
```

### Required
`schema_version, id, repo_fingerprint, workstream_id, from_principal_id, to_scope, created_at, anchors, working, episode_digests, budget, content_hash`

### Constraints
- `anchors` sorted by survival rank then importance/recency
- default `max_bytes = 32768` (32KB)
- `evidence` optional and first dropped after older episodes
- must be reconstructable without L0 raw

### `to_scope`
`self | workstream | recipients | any_authorized`

---

## 12. Sealed pack envelope `.kxp` (outer)

Canonical on-disk/exchange format. Not markdown.

```json
{
  "magic": "MXP1",
  "schema_version": "kedger.pack.v1",
  "handoff_id": "hf_...",
  "workstream_id": "ws_...",
  "repo_fingerprint": "rf_...",
  "created_at": "2026-08-08T18:05:02Z",
  "from_principal_id": "pr_maya",
  "recipient_key_ids": ["pr_maya", "pr_gagan"],
  "algo": {
    "encrypt": "X25519+XChaCha20Poly1305",
    "sign": "Ed25519",
    "kdf": "recipient-sealed-box",
    "hash": "sha256"
  },
  "content_hash": "sha256:...",
  "signature": "base64...",
  "ciphertext": "base64..."
}
```

### Required header fields
`magic, schema_version, handoff_id, workstream_id, repo_fingerprint, created_at, from_principal_id, recipient_key_ids, algo, content_hash, signature, ciphertext`

### Security laws
- ciphertext contains HandoffPack payload only
- no Anchor/working plaintext in header
- hydrate requires principal key in `recipient_key_ids` (or derived capability path)
- signature must verify `from_principal_id`

> Crypto suite above is the **v1 intent lock**. Implementation choice locked in `docs/SEALED_PACKS_AND_SHAREABLE_ANCHORS_V1.md`: age-shaped multi-recipient envelope + libsodium-compatible X25519 wrap / XChaCha20-Poly1305 STREAM / Ed25519 sign-then-encrypt (Kedger-native `.kxp` bytes; full age CLI wire-compat optional later).

---

## 13. Cognify output bundle (engine-internal)

Not necessarily persisted as one row; defines cognify return contract.

```json
{
  "schema_version": "kedger.memory.v1",
  "episode": {"$ref": "Episode"},
  "anchors_upserted": [{"$ref": "Anchor"}],
  "anchors_invalidated": ["anc_..."],
  "edges_upserted": [{"$ref": "GraphEdge"}],
  "working": {"$ref": "WorkingState"},
  "handoff": {"$ref": "HandoffPack"},
  "sealed_pack_path": "packs/ws_.../hf_....kxp",
  "dropped_observation_count": 26
}
```

---

## 14. Size / budget constants (v1 defaults)

| Item | Default |
|------|---------|
| WorkingState max | 4 KiB |
| Anchor statement max | 240 chars |
| Anchor reason max | 480 chars |
| Episode summary max | 1200 chars (target ≤ 500) |
| Evidence snippet max | 280 chars |
| HandoffPack `max_bytes` | 32 KiB |
| Episodes in handoff | 1..3 |
| Anchors in handoff | ranked until budget |
| L0 retention | 7 days or 50 MiB (whichever first) |

### Drop order when over budget
1. raw observations (already excluded)  
2. evidence  
3. older episodes  
4. gotchas  
5. open_questions  
6. never drop active constraints/rejections/decisions while budget remains  

---

## 15. Validation invariants

Writers/readers must enforce:

1. Every Anchor has provenance with at least `actor_principal_id` + `source`
2. `status=superseded` ⇒ `invalid_at` and `superseded_by` set
3. `shareable=true` ⇒ `visibility=repo_shared_safe`
4. HandoffPack `content_hash` matches canonical JSON of payload
5. `.kxp` signature verifies before decrypt use
6. Hydrate denied if principal not recipient/capability holder
7. Workstream WorkingState cardinality = 1 active doc per `workstream_id`
8. File entity names are repo-relative, never absolute machine paths

---

## 16. Minimal example set (auth-refactor)

```text
obs_...  user_prompt "reject cookies, use JWT"
wk_...   goal=JWT auth; files=[auth/session.ts]
ep_...   summary=moved from cookies to JWT
anc_1    rejection cookies
anc_2    decision JWT
anc_3    next_step refresh rotation
eg_...   ep DERIVES anc_1/anc_2/anc_3
eg_...   anc ABOUT file/library
hf_...   sealed pack containing anc_1..3 + wk + ep
cap_...  maya grants gagan read_hydrate on workstream
```

---

## 17. Lock checklist

- [x] Observation schema  
- [x] WorkingState schema  
- [x] Episode schema  
- [x] Anchor schema  
- [x] Evidence schema  
- [x] Entity schema  
- [x] Graph Edge schema  
- [x] Workstream / Principal / Capability schemas  
- [x] HandoffPack payload schema  
- [x] `.kxp` envelope schema + algo intent  
- [x] Budget constants + drop order  
- [x] Validation invariants  

### Still open (next docs)

- Workstream identity detection algorithm details  
- Exact promotion signal detector rules  
- Parallel compose conflict matrix  
- Hook event → ObservationType mapping table  

---

## 18. Changelog

| Date | Change |
|------|--------|
| 2026-08-08 | Initial v1 schema lock for core memory/graph/handoff/capability records. |
