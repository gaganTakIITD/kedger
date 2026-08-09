# Kedger — Repository Plan

> **Status:** This is the Kedger repository  
> **Date:** 2026-08-08  
> **Product:** Kedger

---

## 1. Identity (Kedger locks)

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

## 2. Core docs in this repo

- `docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`
- `docs/MEMORY_SCHEMAS_V1.md`
- `docs/WORKSTREAM_AND_PROMOTION_V1.md`
- `docs/PARALLEL_COMPOSE_AND_HOOKS_V1.md`
- `docs/SEALED_PACKS_AND_SHAREABLE_ANCHORS_V1.md`
- `docs/IMPLEMENTATION_FROM_LITERATURE.md`
- `docs/research/` — lit corpus + eval harness notes
- This file

**Out of scope for Kedger core:** external demo buses, multi-agent theater stacks, judge dashboards, or cloud sync services (see Phase F).

---

## 3. Suggested layout (Phase A)

```text
kedger/
  README.md
  LICENSE                 # Apache-2.0 preferred
  pyproject.toml
  src/kedger/
  hooks/                  # IDE packs (also bundled in wheel)
  tests/
  docs/
  scripts/
```

---

## 4. Launch checklist

1. CI green (`pytest` + smokes)
2. GitHub About: description, topics, social preview (`docs/assets/social.png`)
3. PyPI `0.1.1` via Trusted Publisher or twine
4. GitHub Release from `CHANGELOG.md`

See `docs/PUBLISH.md` and `docs/IMPLEMENTATION_STATUS.md`.
