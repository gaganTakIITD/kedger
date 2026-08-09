# Kedger Stage Research Matrix

> **Date:** 2026-08-08  
> **Purpose:** Map literature constants → current Kedger code → deltas → experiments for stages S1–S8.  
> **Locks:** Do not redesign schema/packs; Phase F stays closed unless SLIs demand an allowed slice.

Code constants: [`src/kedger/constants.py`](../../src/kedger/constants.py).

| Stage | Surface | Lit constants (sources) | Kedger today | Delta / experiment | Refine? |
|-------|---------|-------------------------|--------------|--------------------|---------|
| **S1** Hooks/capture | `hooks/`, `ingest/`, `redact/` | PreCompact HARD; MemGPT warn 0.70 / flush ~0.85; redact; **delay-k online compaction** (2608.00902); StreamingLLM sinks≠semantics (Batch26) | 8-event normalize; L0 warn/flush; redact | **Delay-k soft-stale L0 only (P0)** — never attention-evict Anchors | **yes** — Batch26 B26-R2 |
| **S2** WorkingState | `store/db.py` L1 | Soft files 12 / hard 40; Working ≤4KiB; PrefEval: prefs always available | `WORKING_MAX_BYTES=4096`, soft 12 / hard 40 | Budget fixture under load; prefs via Anchors not only WorkingState | no (budget locked; fixture only) |
| **S3** Cognify | `boundary/`, `cognify/` | IDLE 25–45m (Nemori 30m; WORKSTREAM lock 25m); EST θ=0.60; C1–C14 fixtures | `IDLE_BOUNDARY_MINUTES=25`, `SEGMENT_THETA=0.60`; force cognify; weak digest on empty span; **multi-claim extract** (`cognify/extract.py`) before promote | Keep **25m**; claim-split + theme dedupe so messy sessions don't paragraph-promote; C1–C14 + messy capture gate | **yes** — claim extract + messy gate |
| **S4** Promote | `promote/`, `remember/` | RecMem θ_count=3; Heat τ=5; never auto-share; HaluMem update correctness | `RECURRENCE_PROMOTE_THETA=3`, `HEAT_TAU=5`, `shareable=False` on candidates | Recurrence promote fixture C7; no-relitigation after rejection | yes — fixtures |
| **S5** Graph/compose | `graph/`, `compose/` | ALIAS τ=0.8; SUPERSEDES; GraphReader notebook; **HippoRAG seed IDF**; All-Mem visible surface (Batch26) | compose ESCALATE; **`notebook_walk`**; PPR d=0.5 **uniform seeds**; seed `anchors[:5]` | **Seed IDF (P0)**; visible-surface fixtures (P1) | **yes** — Batch26 |
| **S6** Seal/share | `crypto/kxp.py`, `handoff/`, `share/`, `acl/` | Inv-Scope 404; revoke≠erase; pack-deputy; ConfAIde Tier-4 | PART D tests; `NOT_FOUND_CODE=404`; `explicit_only` | Seal roundtrip SLI; secret canary already PART D | no (extend SLI only) |
| **S7** Hydrate | `hydrate/rank.py` | Drop order; walk budget; AirGap purpose; **LeanMem dual-path budgets**; LightMem-repro tight-token win (Batch26) | `--walk-budget`; `--purpose`; `HANDOFF_MAX_BYTES=32768` | **Dual-path Evidence+Anchors quotas (P0)** | **yes** — Batch26 B26-C1 |
| **S8** Why | `why.py` | Provenance after prune; LongMemEval abstention; ConflictRAG dual-view; Chain-of-Note per Evidence | `why` + ConflictSet; **CoN reading notes** (`support`/`context`/`unknown`) + `abstain` | Optional LLM CoN remains Phase F | done (conflicts + CoN notes) |

## Batch26 perf tickets (2026-08-09)

See [`PERFORMANCE_PROGRESS_ROADMAP.md`](PERFORMANCE_PROGRESS_ROADMAP.md).

1. **P0** Seed IDF on PPR (`graph/expand.py`)  
2. **P0** Dual-path Evidence + Anchors under 32KB (`handoff/compile.py`, `hydrate/rank.py`)  
3. **P0** Delay-k soft-stale on L0 only (`store` / ingest)  
4. **P1** Visible-surface + sleep-time merge + kind quotas  

## Batch4 refine tickets (linked)

1. MemoryAgentBench AR/TTL/LRU/SF → `tests/eval/test_mab_projection.py`  
2. HaluMem + LongMemEval abstention → cognify/why faithfulness probes  
3. ConfAIde Tier-4 + MemoryArena multi-session → seal/share probes (PART D + dogfood)

## Refine loop 2026-08-09 (S3 capture gate — claim extract)

| Ticket | Change | Eval |
|--------|--------|------|
| S3 multi-claim extract | `cognify/extract.py` — split/classify/theme-dedupe L0 → crisp candidates (no whole-paragraph promote); episode digest from claims; promote attaches evidence | `test_claim_extract.py`, `test_messy_capture_gate.py` |
| S3/S5 complementary compose | `compose/ops.py` — same-kind parallel policies **ADD**; only same-slot alternatives **ESCALATE** | `test_capture_smoke_payments.py`, dual-evidence fixtures still green |
| S3 dual-layer activity | `cognify/activity.py` — ops digest (files/edits/lines/agent turns); handoff `activity` + hydrate inject; file_edit normalize line deltas | `test_dual_layer_activity.py` |

LLM distill remains **Phase F**; this is deterministic capture architecture so unclear human sessions still yield durable Anchors.

## Refine loop 2026-08-09 (S7/S8/S5)

Citations: AirGapAgent `2405.05175`; Chain-of-Note `2311.09210`; GraphReader `2406.14550`.

| Ticket | Change | Eval |
|--------|--------|------|
| S8 CoN notes | `evidence/notes.py` + `why.explain_anchor` notes/abstain; `Store.insert_evidence` | `test_refine_loop_con_airgap_notebook.py` |
| S7 purpose packs | `hydrate/purpose.py`; `--purpose` on live hydrate; pack `purpose=` | same |
| S5/S7 notebook | `graph.notebook_walk`; hydrate notebook surface + `--notebook-calls` | same |

SLI note: `artifacts/eval/refine_loop_s7_s8_before_after.md` (local scratch).

## Constant decisions locked this program pass

| Constant | Decision | Evidence |
|----------|----------|----------|
| `IDLE_BOUNDARY_MINUTES` | **25** (unchanged) | WORKSTREAM lock; lit range 25–45; fixtures parametrize on constant |
| Empty-span `--force` cognify | Digest from **active Anchors** when span empty | Dogfood: `candidates:0` / weak “Episode (cognify)” after remember-only |
| LLM distill | **Still Phase F** | Deterministic cognify remains SoT until C1–C14 plateau |
