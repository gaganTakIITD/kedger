"""DB migration + notifications wipe-import stresses (eng handoff fidelity)."""

from __future__ import annotations

import shutil
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.handoff.compile import seal_handoff
from kedger.hooks.runner import run_hook
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint
from kedger.store.paths import project_dir


def _run_wipe_import(
    *,
    runner: CliRunner,
    tmp_path: Path,
    name: str,
    turns: list[dict],
    must_in_inject: list[str],
    must_in_transcript: list[str],
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", name]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    for i, t in enumerate(turns):
        store.ingest_observation(
            {
                **t,
                "session_id": name,
                "workstream_id": ws["id"],
                "agent_tool": "cursor",
                "ts": f"2026-08-09T12:{i:02d}:00Z",
            },
            principal_id=p.principal_id,
        )
    cog = cognify_workstream(
        store, principal=p, force=True, event_type="pre_compact", reseal=False
    )
    assert cog.episode
    promote_candidates(
        store, principal=p, workstream_id=ws["id"], mode="conservative"
    )
    path, pack = seal_handoff(store, principal=p, workstream_slug="default")
    park = tmp_path / f"{name}-pack"
    park.mkdir()
    dst = park / path.name
    shutil.copy2(path, dst)
    tmeta = pack.get("transcript_meta") or {}
    if tmeta.get("sidecar"):
        side = path.parent / tmeta["sidecar"]
        if side.exists():
            shutil.copy2(side, park / tmeta["sidecar"])

    shutil.rmtree(project_dir(repo_fingerprint()))
    hyd = runner.invoke(main, ["hydrate", "--pack", str(dst)])
    assert hyd.exit_code == 0, hyd.output

    store_b = Store.open(repo_fingerprint())
    p = load_principal()
    out = run_hook(
        store_b,
        principal=p,
        payload={"type": "SessionStart", "session_id": f"{name}_next"},
        source="cursor",
    )
    ctx = (out.get("additionalContext") or "").lower()
    for tok in must_in_inject:
        assert tok.lower() in ctx, f"missing {tok} in inject:\n{ctx[:800]}"

    dec = runner.invoke(main, ["transcript", "decompress", "--pack", str(dst)])
    assert dec.exit_code == 0, dec.output
    for tok in must_in_transcript:
        assert tok in dec.output or tok.lower() in dec.output.lower()


def test_db_migration_wipe_import(kedger_env: Path, runner: CliRunner, tmp_path: Path) -> None:
    _run_wipe_import(
        runner=runner,
        tmp_path=tmp_path,
        name="dbmig",
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "migration 0042 failed in prod. dont rerun blindly. "
                    "never drop users.email — billing needs it. take advisory lock first."
                ),
            },
            {
                "type": "agent_response",
                "summary": (
                    "Rejection: do not rerun migration 0042 blindly. "
                    "Rejection: never drop users.email. "
                    "Decision: take advisory lock then retry in smaller batches. "
                    "Next: patch 0042 then expand lock timeout."
                ),
            },
            {
                "type": "file_edit",
                "summary": "Edited migrations/0042_users.sql (+8/-1)",
                "entity_hints": [
                    {"entity_type": "file", "name": "migrations/0042_users.sql"}
                ],
                "edit_stats": {
                    "path": "migrations/0042_users.sql",
                    "edits": 2,
                    "lines_added": 8,
                    "lines_removed": 1,
                },
            },
            {
                "type": "tool_fail",
                "summary": "psql → ERROR: deadlock detected on users",
            },
        ],
        must_in_inject=["email", "0042"],
        must_in_transcript=["deadlock", "0042"],
    )


def test_notifications_wipe_import(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    _run_wipe_import(
        runner=runner,
        tmp_path=tmp_path,
        name="notif",
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "push notifs double-firing on ios. dont touch android fcm this session. "
                    "must debounce by notification_id. leave analytics alone."
                ),
            },
            {
                "type": "agent_response",
                "summary": (
                    "Rejection: do not touch android fcm. "
                    "Rejection: leave analytics alone. "
                    "Constraint: must debounce by notification_id. "
                    "Decision: fix ios APNs receipt path only. "
                    "Next: patch ApnsWorker then receipt fixture."
                ),
            },
            {
                "type": "file_edit",
                "summary": "Edited src/notify/apns_worker.py (+19/-6)",
                "entity_hints": [
                    {"entity_type": "file", "name": "src/notify/apns_worker.py"}
                ],
                "edit_stats": {
                    "path": "src/notify/apns_worker.py",
                    "edits": 3,
                    "lines_added": 19,
                    "lines_removed": 6,
                },
            },
        ],
        must_in_inject=["notification", "apns"],
        must_in_transcript=["analytics", "fcm"],
    )
