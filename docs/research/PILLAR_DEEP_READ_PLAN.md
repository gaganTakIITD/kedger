# Pillar Deep-Read Plan → Implementation Clarity

> **Goal:** For each MoDeX architecture pillar, deep-read the dense relevant literature and extract **implementation-level** algorithms, data structures, thresholds, and failure modes — not keyword abstracts.  
> **Date:** 2026-08-08  
> **Corpus seed:** ~783 unique arXiv IDs extracted from previously fetched survey bodies.

## Architecture → research pillars

| Pillar | MoDeX surface | Implementation questions literature must answer |
|--------|---------------|--------------------------------------------------|
| **P1 Capture & Working** | Hooks → L0 → L1 | What events to observe; when to patch working state; redaction; buffer rotation |
| **P2 Episode / Cognify** | L0→L2 boundaries | Segmentation signals; chapter digests; prune rules; surprise/EST/recurrence |
| **P3 Anchors / Graph** | L3 + entity graph | Atomic fact shape; bi-temporal invalidation; entity resolve; promotion gates |
| **P4 Conflict / Compose** | Parallel writers | Conflict taxonomy; projection vs write; audit losers; CRDT/event-sourcing |
| **P5 Hydrate / Retrieve** | L4 compile + inject | Ranking; budget drop order; associative expand; pack composition |
| **P6 Privacy / Seal** | Capabilities + `.mxp` | Scope on every path; share promotion; seal/reseal; key UX |

## Output contract per pillar

Each pillar memo MUST contain:
1. Honesty table (FULL / substantial / abstract-only counts)
2. Mechanism cards for every FULL paper (write/read/forget/conflict/privacy)
3. **Implementation recipe** for MoDeX: tables, indexes, algorithms, pseudocode, constants
4. Anti-patterns found in papers that we must not copy
5. Open risks still under-specified by literature

## Files

- `docs/research/impl/P1_CAPTURE_WORKING.md`
- `docs/research/impl/P2_EPISODE_COGNIFY.md`
- `docs/research/impl/P3_ANCHORS_GRAPH.md`
- `docs/research/impl/P4_CONFLICT_COMPOSE.md`
- `docs/research/impl/P5_HYDRATE_RETRIEVE.md`
- `docs/research/impl/P6_PRIVACY_SEAL.md`
- `docs/IMPLEMENTATION_FROM_LITERATURE.md` (cross-pillar synthesis for builders)
