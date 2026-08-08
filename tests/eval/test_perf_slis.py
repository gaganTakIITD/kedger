"""Performance SLIs — soft local gates for hook / cognify / seal paths."""

from __future__ import annotations

import json
import time
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main

from sli_util import record_sli

# Soft gates (CI VMs vary); these catch pathological regressions only.
HOOK_P95_MS = 2000.0
COGNIFY_P95_MS = 3000.0
SEAL_MS = 2000.0


def _p95(samples: list[float]) -> float:
    if not samples:
        return 0.0
    xs = sorted(samples)
    idx = max(0, int(round(0.95 * (len(xs) - 1))))
    return xs[idx]


def test_hook_session_start_sli(
    kedger_env: Path, runner: CliRunner, sli_sink: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert runner.invoke(main, ["remember", "constraint", "TLS required"]).exit_code == 0
    samples: list[float] = []
    for _ in range(5):
        t0 = time.perf_counter()
        res = runner.invoke(
            main,
            ["hook", "--source", "cursor"],
            input=json.dumps({"type": "SessionStart", "session_id": "perf"}),
        )
        dt = (time.perf_counter() - t0) * 1000.0
        assert res.exit_code == 0, res.output
        samples.append(dt)
    p95 = _p95(samples)
    record_sli(sli_sink, "hook_session_start_p95_ms", p95)
    assert p95 < HOOK_P95_MS, p95


def test_cognify_hard_sli(kedger_env: Path, runner: CliRunner, sli_sink: Path) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert runner.invoke(main, ["remember", "goal", "Finish auth"]).exit_code == 0
    from kedger.keys import load_principal
    from kedger.store import Store, repo_fingerprint

    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    samples: list[float] = []
    for i in range(3):
        store = Store.open(repo_fingerprint())
        store.ingest_observation(
            {
                "type": "user_prompt",
                "session_id": "p",
                "workstream_id": ws["id"],
                "summary": f"Reject cookies pass {i}",
            },
            principal_id=p.principal_id,
        )
        t0 = time.perf_counter()
        res = runner.invoke(main, ["cognify", "--force"])
        dt = (time.perf_counter() - t0) * 1000.0
        assert res.exit_code == 0, res.output
        samples.append(dt)
    p95 = _p95(samples)
    record_sli(sli_sink, "cognify_hard_p95_ms", p95)
    assert p95 < COGNIFY_P95_MS, p95


def test_seal_open_roundtrip_sli(
    kedger_env: Path, runner: CliRunner, sli_sink: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert runner.invoke(main, ["remember", "decision", "Use JWT"]).exit_code == 0
    out = Path("seal_perf.kxp")
    t0 = time.perf_counter()
    res = runner.invoke(main, ["handoff", "--out", str(out)])
    assert res.exit_code == 0, res.output
    res2 = runner.invoke(main, ["hydrate", "--pack", str(out)])
    dt = (time.perf_counter() - t0) * 1000.0
    assert res2.exit_code == 0, res2.output
    record_sli(sli_sink, "seal_open_roundtrip_ms", dt)
    assert dt < SEAL_MS, dt
