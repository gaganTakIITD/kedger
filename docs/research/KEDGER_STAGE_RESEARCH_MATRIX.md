# Kedger Stage Research Matrix

> **Date:** 2026-08-08  
> **Purpose:** Map literature constants → current Kedger code → deltas → experiments for stages S1–S8.  
> **Locks:** Do not redesign schema/packs; Phase F stays closed unless SLIs demand an allowed slice.

Code constants: [`src/kedger/constants.py`](../../src/kedger/constants.py).

| Stage | Surface | Lit constants (sources) | Kedger today | Delta / experiment | Refine? |
|-------|---------|-------------------------|--------------|--------------------|---------|
| **S1** Hooks/capture | `hooks/`, `ingest/`, `redact/` | PreCompact HARD before compact (Claude/Cursor docs); MemGPT warn 0.70 / flush ~0.85; redact before persist (ConfAIde/CaMeL) | 8-event normalize; L0 warn/flush ratios match; redact-before-persist | Measure `hook_session_start_p95_ms`; generation probes on share (Batch4 ConfAIde) | yes — SLI + ConfAIde probes |
| **S2** WorkingState | `store/db.py` L1 | Soft files 12 / hard 40; Working ≤4KiB; PrefEval: prefs always available | `WORKING_MAX_BYTES=4096`, soft 12 / hard 40 | Budget fixture under load; prefs via Anchors not only WorkingState | no (budget locked; fixture only) |
| **S3** Cognify | `boundary/`, `cognify/` | IDLE 25–45m (Nemori 30m; WORKSTREAM lock 25m); EST θ=0.60; C1–C14 fixtures | `IDLE_BOUNDARY_MINUTES=25`, `SEGMENT_THETA=0.60`; force cognify; weak digest on empty span | Keep **25m** (WORKSTREAM lock); fixtures use constant; improve empty-span digest from active Anchors; C1–C14 pytest | **yes** — digest + fixtures |
| **S4** Promote | `promote/`, `remember/` | RecMem θ_count=3; Heat τ=5; never auto-share; HaluMem update correctness | `RECURRENCE_PROMOTE_THETA=3`, `HEAT_TAU=5`, `shareable=False` on candidates | Recurrence promote fixture C7; no-relitigation after rejection | yes — fixtures |
| **S5** Graph/compose | `graph/`, `compose/` | ALIAS τ=0.8; SUPERSEDES before near-dup (MemClaw); bi-temporal | `ALIAS_TAU=0.8`; SUPERSEDES on forget; compose escalate | Parallel workstream isolation fixture | yes — fixture |
| **S6** Seal/share | `crypto/kxp.py`, `handoff/`, `share/`, `acl/` | Inv-Scope 404; revoke≠erase; pack-deputy; ConfAIde Tier-4 | PART D tests; `NOT_FOUND_CODE=404`; `explicit_only` | Seal roundtrip SLI; secret canary already PART D | no (extend SLI only) |
| **S7** Hydrate | `hydrate/rank.py` | Drop order constraints→…→raw; PPR d=0.5; HippoRAG2 recognition top-k=5; MAB AR/TTL/LRU/SF | Survival rank + budget drop; `PPR_DAMPING=0.5`; associative expand | `hydrate_pack_bytes` + `anchor_drop_violations`; MAB projection adapters | yes — SLIs + adapters |
| **S8** Why | `why.py` | Provenance after prune; LongMemEval abstention; MemLeak no resurrect | `why` returns scoped chain; prune keeps observation_ids | Provenance after payload prune; abstain when no Evidence | yes — fixture |

## Batch4 refine tickets (linked)

1. MemoryAgentBench AR/TTL/LRU/SF → `tests/eval/test_mab_projection.py`  
2. HaluMem + LongMemEval abstention → cognify/why faithfulness probes  
3. ConfAIde Tier-4 + MemoryArena multi-session → seal/share probes (PART D + dogfood)

## Constant decisions locked this program pass

| Constant | Decision | Evidence |
|----------|----------|----------|
| `IDLE_BOUNDARY_MINUTES` | **25** (unchanged) | WORKSTREAM lock; lit range 25–45; fixtures parametrize on constant |
| Empty-span `--force` cognify | Digest from **active Anchors** when span empty | Dogfood: `candidates:0` / weak “Episode (cognify)” after remember-only |
| LLM distill | **Still Phase F** | Deterministic cognify remains SoT until C1–C14 plateau |
