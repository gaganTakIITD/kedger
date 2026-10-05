# Eval evidence (mechanical proof, not a field study)

> **Stage 2 start** — a public pointer at what CI already measures.  
> **This page does not invent SLI numbers.** Reproduce locally; do not treat empty [`PEER_TRIALS.md`](PEER_TRIALS.md) rows as filled.  
> **Tip:** Kedger **0.2.6** · **Audience:** strangers who should not have to spelunk `tests/eval/`

Kedger’s **mechanical** proof is CI + pytest evals + smoke scripts. That is **not** a published user study and **not** five human Alice→Bob trials.

Honesty line: *Beta OSS. Mechanically tested handoff. Not yet a published user study.*

---

## What CI already runs

[`.github/workflows/ci.yml`](../.github/workflows/ci.yml) on `main` and `Cursor/**` (Python 3.11 / 3.12):

| Step | What it is |
|------|------------|
| `bash scripts/check_hook_packs_sync.sh` | Hook packs in `hooks/` match the wheel |
| `pytest -q` | Unit tests **and** the whole eval harness under `tests/eval/` |
| `smoke_transfer` / `smoke_wheel_install` / `smoke_peer_handoff` / `smoke_prompt_inject` | End-to-end mechanical paths |

Badge: [CI workflow](https://github.com/gaganTakIITD/kedger/actions/workflows/ci.yml). Green CI means those gates passed on that commit — not that anyone in the field completed a peer send.

---

## Reproduce (no harvested numbers)

From a clone:

```bash
pip install -e ".[dev]"
bash scripts/check_hook_packs_sync.sh
pytest -q
pytest -q tests/eval
```

Harness contract (suites, documented **soft gates**, merge rules): [`research/EVAL_HARNESS.md`](research/EVAL_HARNESS.md).

When the workspace is writable, eval tests append JSON lines to `artifacts/eval/slis.jsonl` (gitignored scratch — see `.gitignore`). If that path cannot be created, tests fall back to a temp file (`tests/eval/sli_util.py`). **Do not commit** `slis.jsonl`. **Do not paste unpublished timings into README / Marketing as product claims.**

To inspect a local run after `pytest -q tests/eval`:

```bash
# only if your run wrote the repo-local sink
python -c "from pathlib import Path; p=Path('artifacts/eval/slis.jsonl'); print(p.read_text() if p.exists() else 'no local slis.jsonl (gitignored; re-run pytest)')"
```

There is no checked-in dashboard of p95s. If the file is missing, that is expected on a fresh clone.

---

## What the harness measures (names and gates, not scores)

Documented in [`research/EVAL_HARNESS.md`](research/EVAL_HARNESS.md) and asserted in code. These are **gate definitions**, not measured field results.

| SLI / gate | Soft gate (local / CI VM) | Where |
|------------|---------------------------|--------|
| `hook_session_start_p95_ms` | < 2000 ms | `tests/eval/test_perf_slis.py` |
| `cognify_hard_p95_ms` | < 3000 ms | same |
| `seal_open_roundtrip_ms` | < 2000 ms | same |
| `hydrate_pack_bytes` | ≤ 32768 (`HANDOFF_MAX_BYTES`) | `tests/eval/test_budgets_slis.py` |
| `anchor_drop_violations` | = 0 (never drop active constraint/rejection/decision while lower kinds remain) | same |

**Strict handoff B01–B05** (`tests/eval/test_handoff_quality_strict.py`) — binary probes, not vibes:

| Case | Title |
|------|--------|
| B01 | Policy-heavy payments — constraints/rejections must survive |
| B02 | Messy unlabeled slang — capture still yields usable policy |
| B03 | Ops-heavy agent-only — activity must carry continuity |
| B04 | Near-empty session — must abstain from invented policy |
| B05 | Unlabeled messy speech — policy + ops without `Constraint:` labels |

Rules in that file: `kedger_dual` must beat `none` on non-empty policy/ops cases; empty sessions abstain; zlib transcript archive roundtrips across seal.

**Other suites under `tests/eval/`** (full list in the harness doc):

- Governance / Inv-Scope 404 (`test_governance.py`)
- Cognify fixtures C1–C14 subset (`test_cognify_fixtures.py`)
- MemoryAgentBench AR/TTL/LRU/SF projections (`test_mab_projection.py`)
- LoCoMo / LongMemEval / HaluMem temporal + abstention (`test_temporal_abstain.py`)
- ConfAIde share/redact probe (`test_confaide_share_probe.py`)
- Dual-layer spectrum / insight under caps (`test_handoff_spectrum_10.py`, `test_p0_memory_perf.py`)

Merge gate (harness §4): no regression on Inv-Scope 404, `anchor_drop_violations == 0`, WorkingState ≤ 4096, PART D sealed scenarios.

---

## What this is not

| Not | Where that lives instead |
|-----|--------------------------|
| Five **human** peer trials | [`PEER_TRIALS.md`](PEER_TRIALS.md) rows 1–5 — still empty; recruit with [`PEER_ASK_PACK.md`](PEER_ASK_PACK.md) |
| Mechanical M1–M5 as field proof | Those rows are CI/agent smokes only |
| Published user study / “proven in production” | Claim guardrails: [`MARKETING.md`](MARKETING.md) |
| Live timings for the README | Re-run pytest; do not freeze a VM p95 as a product number |
| Install → doctor-clean DX hardening | Still Stage 2 remaining work ([`ROADMAP.md`](ROADMAP.md)); Windows PATH warn is documented at 0.2.6 |

Stage 3 product bets wait until Stage 1 rows 1–5 are filled (pass or fail-with-issue).
