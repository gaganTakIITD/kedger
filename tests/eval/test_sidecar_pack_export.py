"""Large transcript → sidecar → pack-export → wipe → import continuity."""

from __future__ import annotations

import shutil
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.hooks.runner import run_hook
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint
from kedger.store.paths import project_dir


def test_sidecar_pack_export_wipe_import(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "sidebig"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    # Fat repetitive turns to force non-trivial zlib archive
    for i in range(60):
        kind = "user_prompt" if i % 3 == 0 else (
            "agent_response" if i % 3 == 1 else "file_edit"
        )
        turn: dict = {
            "type": kind,
            "session_id": "fat",
            "workstream_id": ws["id"],
            "agent_tool": "cursor",
            "ts": f"2026-08-09T22:{(i // 60):02d}:{i % 60:02d}Z",
            "summary": (
                "Constraint: must send Idempotency-Key on every charge create. "
                "Rejection: never auto-ack unverified webhooks. "
                f"UNIQUE_SIDECAR_TOKEN_{i} padding " + ("x" * 40)
            ),
        }
        if kind == "file_edit":
            path = f"src/payments/f{i % 5}.py"
            turn["summary"] = f"Edited {path} (+3/-1) UNIQUE_SIDECAR_TOKEN_{i}"
            turn["entity_hints"] = [{"entity_type": "file", "name": path}]
            turn["edit_stats"] = {
                "path": path,
                "edits": 1,
                "lines_added": 3,
                "lines_removed": 1,
            }
        store.ingest_observation(turn, principal_id=p.principal_id)

    cog = cognify_workstream(
        store, principal=p, force=True, event_type="pre_compact", reseal=False
    )
    assert cog.episode and cog.episode.get("transcript")
    promote_candidates(
        store, principal=p, workstream_id=ws["id"], mode="conservative"
    )

    export_dir = tmp_path / "xfer"
    exp = runner.invoke(
        main, ["pack-export", "--out-dir", str(export_dir)]
    )
    assert exp.exit_code == 0, exp.output
    packs = list(export_dir.glob("*.kxp"))
    assert len(packs) == 1

    # Wipe and restore from exported bundle
    shutil.rmtree(project_dir(repo_fingerprint()))
    hyd = runner.invoke(main, ["hydrate", "--pack", str(packs[0])])
    assert hyd.exit_code == 0, hyd.output
    assert "imported:" in hyd.output

    store_b = Store.open(repo_fingerprint())
    p = load_principal()
    out = run_hook(
        store_b,
        principal=p,
        payload={"type": "SessionStart", "session_id": "after"},
        source="cursor",
    )
    ctx = out.get("additionalContext") or ""
    assert "Transcript archive" in ctx
    assert "recent turns" in ctx.lower() or "UNIQUE_SIDECAR_TOKEN" in ctx
    assert "idempotency" in ctx.lower() or "billing" in ctx.lower() or "[" in ctx

    dec = runner.invoke(main, ["transcript", "decompress", "--pack", str(packs[0])])
    assert dec.exit_code == 0, dec.output
    assert "UNIQUE_SIDECAR_TOKEN_59" in dec.output
    assert "UNIQUE_SIDECAR_TOKEN_0" in dec.output
