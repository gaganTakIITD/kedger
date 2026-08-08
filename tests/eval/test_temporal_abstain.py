"""LoCoMo / LongMemEval / HaluMem projections — temporal update + abstention."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint


def test_locomo_temporal_update(kedger_env: Path, runner: CliRunner) -> None:
    """Temporal flip: later fact supersedes earlier via forget+remember."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(main, ["remember", "decision", "Deploy target is us-east-1"])
    anc = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(":", 1)[
        1
    ].strip()
    assert runner.invoke(main, ["forget", anc]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "decision", "Deploy target is eu-west-1"]
        ).exit_code
        == 0
    )
    hyd = runner.invoke(main, ["hydrate", "--live"])
    assert "eu-west-1" in hyd.output
    assert "us-east-1" not in hyd.output


def test_longmemeval_abstain_why_unknown(
    kedger_env: Path, runner: CliRunner
) -> None:
    """Abstain: why on unknown id must not invent Anchors."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    why = runner.invoke(main, ["why", "anc_does_not_exist_000000000001"])
    assert why.exit_code != 0
    assert "eu-west" not in why.output.lower()


def test_halumem_no_invented_candidates(kedger_env: Path, runner: CliRunner) -> None:
    """HaluMem extract: cognify must not invent statements absent from span/anchors."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    store.ingest_observation(
        {
            "type": "user_prompt",
            "session_id": "h",
            "workstream_id": ws["id"],
            "summary": "Discussed logging levels for the worker",
        },
        principal_id=p.principal_id,
    )
    res = cognify_workstream(store, principal=p, force=True, reseal=False)
    for c in res.candidates:
        stmt = (c.get("statement") or "").lower()
        # Must be grounded in the span text
        assert "logging" in stmt or "worker" in stmt
        assert "quantum" not in stmt
