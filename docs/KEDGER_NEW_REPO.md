# Kedger — New Repository Plan

> **Status:** Naming locked; **this is the Kedger repository**  
> **Date:** 2026-08-08  
> **Product:** Kedger  
> **Hard rule:** **Kedger ≠ MoDeX.** Different name, repo, CLI, paths, packs, and product story.

Design drafts were temporarily authored under the MoDeX hackathon repo’s `docs/`; they now live here. That co-location was temporary storage of docs — **not** a merge of the two products.

---

## 1. Two products (do not conflate)

| | **Kedger** | **MoDeX** |
|--|------------|-----------|
| What | New OSS memory + sealed handoff engine | Hackathon prototype (Memory of Codex) |
| Repo | New `kedger` repository | `google-hackathon` (this repo) |
| CLI / paths | `kedger`, `~/.kedger/`, `.kxp` | MoDeX’s own surfaces / demo stack |
| Stack | hooks → CLI → Anchors → sealed packs | MCP, Fivetran, BigQuery/Sheet, ADK, dashboard |
| Brand | Kedger only | MoDeX only |

Relationship: Kedger may reuse **problem lessons** learned while building MoDeX.  
It is **not** a MoDeX rebrand, “MoDeX OSS edition,” or drop-in continuation of the hackathon stack.

---

## 2. Identity (Kedger locks)

| Field | Value |
|-------|-------|
| Name | **Kedger** |
| CLI | `kedger` |
| Schema | `kedger.memory.v1` |
| Private store | `~/.kedger/` |
| Repo policy | `<repo>/.kedger/` |
| Sealed packs | `*.kxp` |

Metaphor: *kedge* = small working anchor used to warp a ship into place → place Anchors, pull continuity forward.

---

## 3. What moves into the Kedger repo

Kedger design constitution (port as Kedger docs):

- `docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`
- `docs/MEMORY_SCHEMAS_V1.md`
- `docs/WORKSTREAM_AND_PROMOTION_V1.md`
- `docs/PARALLEL_COMPOSE_AND_HOOKS_V1.md`
- `docs/SEALED_PACKS_AND_SHAREABLE_ANCHORS_V1.md`
- `docs/IMPLEMENTATION_FROM_LITERATURE.md`
- Selected research that is clearly Kedger-implementation material (rewrite “MoDeX mapping” headers to **Kedger** only after copy — do not rewrite MoDeX product docs in place)
- This file

**Stay in the MoDeX / hackathon repo (do not absorb into Kedger brand):**

- Fivetran / BigQuery / Sheet bus
- ADK multi-agent Face 2 theater
- Hackathon dashboard / judge MCP credentials
- MoDeX MCP face, README, JUDGES.md, submission materials
- Anything marketed or named as MoDeX

---

## 4. Suggested Kedger repo layout (Phase A)

```text
kedger/
  README.md
  LICENSE                 # Apache-2.0 preferred
  pyproject.toml
  docs/                   # Kedger design locks only
  src/kedger/
    cli/
    store/
    keys/
    ingest/
    remember/
  tests/
  hooks/
```

Phase A CLI minimum:

```text
kedger keys ...
kedger ingest --from-hook
kedger remember decision|reject|constraint "..."
kedger forget <id>
kedger status
kedger doctor
```

Then Phase B sealed handoff (`handoff` / `hydrate` / `grant` / `revoke`).

---

## 5. Repo status

The **`kedger`** repository exists and is separate from MoDeX / `google-hackathon`.

---

## 6. Implementation steps

Phase A (this tree):

1. Bootstrap `kedger` package + console entrypoint  
2. Private store at `~/.kedger/projects/<repo_fingerprint>/store.sqlite`  
3. Principal key bootstrap (`kedger keys`)  
4. `remember` / `forget` / `status` against Anchor schema v1  
5. Unit tests for store invariants (SUPERSEDES; no silent overwrite)

Phase B next: sealed handoff (`handoff` / `hydrate` / `grant` / `revoke`).

Do not deploy. Do not pull MoDeX’s Fivetran/ADK/BigQuery demo core into Kedger. Do not rename MoDeX to Kedger anywhere in the hackathon product.
