# Kedger Eval Harness

> **Date:** 2026-08-08  
> **Code:** [`tests/eval/`](../../tests/eval/) · reports → `artifacts/eval/`  
> **Rule:** Governance probes > chat-QA vanity. No MoDeX dashboards.

## 1. Fixture suites

| Suite | File | Sources |
|-------|------|---------|
| Governance | `test_governance.py` | Arch §15, SHAREABLE, PART D |
| Cognify C1–C14 (subset runnable) | `test_cognify_fixtures.py` | P2 §8 |
| Budget / survival | `test_budgets_slis.py` | schemas + P5 drop order |
| MAB projection | `test_mab_projection.py` | MemoryAgentBench AR/TTL/LRU/SF |
| Temporal / abstention | `test_temporal_abstain.py` | LoCoMo, LongMemEval, HaluMem |
| Perf SLIs | `test_perf_slis.py` | hook/cognify/seal timings |

Run:

```bash
pytest -q tests/eval
pytest -q   # full suite including unit tests
```

## 2. Performance / resource SLIs

| SLI | Soft gate (local) | Intent |
|-----|-------------------|--------|
| `hook_session_start_p95_ms` | < 2000 ms | SessionStart hydrate inject |
| `cognify_hard_p95_ms` | < 3000 ms | PreCompact path |
| `seal_open_roundtrip_ms` | < 2000 ms | Handoff UX |
| `hydrate_pack_bytes` | ≤ 32768 | `HANDOFF_MAX_BYTES` |
| `anchor_drop_violations` | = 0 | Never drop active constraint/rejection/decision while lower kinds remain |
| `store_size_growth` | L0 rotate reduces row pressure | Rotation effectiveness |

JSON lines written under `artifacts/eval/slis.jsonl` when tests run with write permission.

## 3. External bench → Kedger projection

| Bench | Projection |
|-------|------------|
| MemoryAgentBench AR | Fact survives cognify→hydrate substring match |
| MemoryAgentBench TTL | Stale playbook superseded; newest wins |
| MemoryAgentBench LRU | Old L0 pruned; Anchors untouched |
| MemoryAgentBench SF | Ordered edits → SUPERSEDES chain; forget residual |
| LoCoMo / LongMemEval | Temporal update + abstain when no Evidence |
| HaluMem | Extract candidates only from span text (no invented Anchors) |
| ConfAIde | Share/redact: secrets never in shared facet |

## 4. Merge gate

Refine PRs must not regress:

- Inv-Scope 404 paths  
- `anchor_drop_violations == 0`  
- WorkingState ≤ 4096  
- PART D sealed scenarios  
