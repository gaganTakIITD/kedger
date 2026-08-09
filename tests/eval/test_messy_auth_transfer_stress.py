"""End-to-end stress: messy unlabeled → cognify+promote → wipe → import → inject."""

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

MESSY = [
    {
        "type": "user_prompt",
        "summary": (
            "auth still cookies on /api and mobile cant share the jar. "
            "reject cookies for api auth. must use short lived jwt + rotating refresh. "
            "never log Authorization bearers. android still sends X-Session-Id till v3 "
            "so keep compat shim. dashboard cookies out of scope."
        ),
    },
    {
        "type": "agent_response",
        "summary": (
            "rejecting cookie sessions for api. going with short-lived jwt and opaque "
            "refresh. wont log bearers. keep x-session-id shim until android v3. "
            "next mint login jwt then refresh rotation."
        ),
    },
    {
        "type": "file_edit",
        "summary": "Edited src/auth/session.py (+24/-19)",
        "entity_hints": [{"entity_type": "file", "name": "src/auth/session.py"}],
        "edit_stats": {
            "path": "src/auth/session.py",
            "edits": 3,
            "lines_added": 24,
            "lines_removed": 19,
        },
    },
    {
        "type": "file_edit",
        "summary": "Edited src/auth/jwt.py (+31/-0)",
        "entity_hints": [{"entity_type": "file", "name": "src/auth/jwt.py"}],
        "edit_stats": {
            "path": "src/auth/jwt.py",
            "edits": 2,
            "lines_added": 31,
            "lines_removed": 0,
        },
    },
    {
        "type": "tool_fail",
        "summary": "pytest tests/test_auth_api.py → 401 missing Authorization on /api/me",
    },
    {
        "type": "agent_response",
        "summary": (
            "fixed bearer extract. still open: should refresh cookies stay for dashboard "
            "only? parked. next ci fixture for rotating refresh."
        ),
    },
]


def test_messy_auth_wipe_import_next_agent(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "authstress"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    for i, t in enumerate(MESSY):
        store.ingest_observation(
            {
                **t,
                "session_id": "auth_a",
                "workstream_id": ws["id"],
                "agent_tool": "cursor",
                "ts": f"2026-08-09T21:{i:02d}:00Z",
            },
            principal_id=p.principal_id,
        )

    # Prefer the one-shot product path
    cog = cognify_workstream(
        store, principal=p, force=True, event_type="pre_compact", reseal=False
    )
    assert cog.episode
    promote_candidates(
        store, principal=p, workstream_id=ws["id"], mode="conservative"
    )
    path, pack = seal_handoff(store, principal=p, workstream_slug="default")
    assert pack.get("transcript") or pack.get("transcript_meta")

    park = tmp_path / "auth-pack"
    park.mkdir()
    dst = park / path.name
    shutil.copy2(path, dst)
    tmeta = pack.get("transcript_meta") or {}
    if tmeta.get("sidecar"):
        side = path.parent / tmeta["sidecar"]
        if side.exists():
            shutil.copy2(side, park / tmeta["sidecar"])

    # Wipe store
    shutil.rmtree(project_dir(repo_fingerprint()))

    hyd = runner.invoke(main, ["hydrate", "--pack", str(dst)])
    assert hyd.exit_code == 0, hyd.output
    assert "imported:" in hyd.output

    store_b = Store.open(repo_fingerprint())
    p = load_principal()
    live = runner.invoke(main, ["hydrate", "--live"])
    assert live.exit_code == 0, live.output
    low = live.output.lower()
    assert "cookie" in low or "jwt" in low
    assert "never log" in low or "bearer" in low
    assert "session.py" in low or "jwt.py" in low or "activity:" in low

    out = run_hook(
        store_b,
        principal=p,
        payload={"type": "SessionStart", "session_id": "auth_b"},
        source="cursor",
    )
    ctx = (out.get("additionalContext") or "").lower()
    assert "cookie" in ctx or "jwt" in ctx
    assert "never log" in ctx or "bearer" in ctx
    assert "agent activity" in ctx or "ops layer" in ctx
    assert "session.py" in ctx or "jwt.py" in ctx
    assert "transcript archive" in ctx or "zlib" in ctx
    # tool_fail gotcha should reach base Anchors after conservative promote
    assert "401" in ctx or "authorization" in ctx or "gotcha" in ctx

    dec = runner.invoke(main, ["transcript", "decompress", "--pack", str(dst)])
    assert dec.exit_code == 0, dec.output
    assert "401" in dec.output or "Authorization" in dec.output
    assert "X-Session-Id" in dec.output or "android" in dec.output.lower()
