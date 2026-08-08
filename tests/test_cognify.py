"""Phase C: boundary + cognify + episode + L0 prune + reseal."""

from __future__ import annotations

import json
from pathlib import Path

from click.testing import CliRunner

from kedger.boundary import detect_boundary
from kedger.cli.main import main
from kedger.store import Store, repo_fingerprint


def test_hard_boundary_always() -> None:
    b = detect_boundary(event_type="pre_compact", span_count=0)
    assert b is not None
    assert b.kind == "hard"


def test_soft_idle_needs_span() -> None:
    assert detect_boundary(event_type="idle", span_count=0, min_span=1) is None


def test_cognify_cli_creates_episode(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    from kedger.keys import load_principal

    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    for i, text in enumerate(
        [
            "Reject cookie sessions for auth",
            "We decided to use JWT instead",
            "Next: implement refresh rotation",
        ]
    ):
        store.ingest_observation(
            {
                "type": "user_prompt",
                "session_id": "s1",
                "workstream_id": ws["id"],
                "summary": text,
                "entity_hints": [{"entity_type": "file", "name": "auth/session.ts"}],
                "ts": f"2026-08-08T18:0{i}:00Z",
            },
            principal_id=p.principal_id,
        )

    cog = runner.invoke(main, ["cognify", "--force"])
    assert cog.exit_code == 0, cog.output
    assert "episode:" in cog.output
    assert "boundary:   hard/" in cog.output
    assert "pack:" in cog.output

    store = Store.open(repo_fingerprint())
    ep = store.latest_episode(ws["id"])
    assert ep is not None
    assert ep["digest_v1"] is True
    assert "observation_ids" in ep["observation_span"]
    # payloads pruned
    obs = store.list_observations(workstream_id=ws["id"])
    assert any(o.get("payload_pruned") for o in obs)

    # recurrence ≠ share
    shared = runner.invoke(main, ["anchors", "--shared"])
    assert shared.output.strip() == "(none)"


def test_cognify_pre_compact_event(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    payload = {
        "type": "pre_compact",
        "session_id": "s",
        "summary": "About to compact context",
    }
    # attach workstream via remember first
    assert runner.invoke(main, ["remember", "goal", "Ship JWT auth"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    from kedger.keys import load_principal

    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    assert ws
    payload["workstream_id"] = ws["id"]
    assert (
        runner.invoke(main, ["ingest", "--from-hook"], input=json.dumps(payload)).exit_code
        == 0
    )
    cog = runner.invoke(main, ["cognify", "--event", "pre_compact"])
    assert cog.exit_code == 0, cog.output
    assert "episode:" in cog.output
