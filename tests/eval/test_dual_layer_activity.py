"""Dual-layer capture: base Anchors (user+agent) + activity ops (edits/files/lines)."""

from __future__ import annotations

import json
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream, compile_activity
from kedger.cognify.activity import edit_stats_from_payload, summarize_file_edit
from kedger.handoff.compile import seal_handoff
from kedger.hooks.normalize import normalize_hook_event
from kedger.hooks.runner import run_hook
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint


def test_file_edit_normalize_captures_line_deltas() -> None:
    n = normalize_hook_event(
        {
            "type": "afterFileEdit",
            "file_path": "src/payments/charges.py",
            "edits": [
                {
                    "old_string": "def charge():\n    pass\n",
                    "new_string": (
                        "def charge():\n"
                        "    headers['Idempotency-Key'] = kid\n"
                        "    return client.create()\n"
                    ),
                }
            ],
        },
        source="cursor",
    )
    obs = n["observation"]
    assert obs["type"] == "file_edit"
    assert "charges.py" in obs["summary"]
    assert obs["edit_stats"]["lines_added"] >= 1
    assert any("charges.py" in f for f in (obs.get("files") or []))


def test_compile_activity_counts_agent_and_edits() -> None:
    span = [
        {"id": "1", "type": "user_prompt", "summary": "fix doubles yo"},
        {
            "id": "2",
            "type": "agent_response",
            "summary": "adding idempotency keys; wont touch billing flag",
        },
        {
            "id": "3",
            "type": "file_edit",
            "summary": "Edited src/payments/charges.py (+5/-1)",
            "entity_hints": [{"entity_type": "file", "name": "src/payments/charges.py"}],
            "edit_stats": {
                "path": "src/payments/charges.py",
                "edits": 1,
                "lines_added": 5,
                "lines_removed": 1,
            },
            "payload": {
                "file_path": "src/payments/charges.py",
                "lines_added": 5,
                "lines_removed": 1,
            },
        },
        {
            "id": "4",
            "type": "file_edit",
            "summary": "Edited src/payments/webhooks.py (+3/-0)",
            "edit_stats": {
                "path": "src/payments/webhooks.py",
                "edits": 1,
                "lines_added": 3,
                "lines_removed": 0,
            },
            "payload": {
                "path": "src/payments/webhooks.py",
                "lines_added": 3,
                "lines_removed": 0,
            },
        },
        {
            "id": "5",
            "type": "tool_result",
            "summary": "rg Idempotency-Key → 2 hits",
        },
    ]
    act = compile_activity(span)
    assert act["layer"] == "activity"
    assert act["totals"]["files"] == 2
    assert act["totals"]["edits"] >= 2
    assert act["totals"]["lines_added"] == 8
    assert act["totals"]["lines_removed"] == 1
    assert act["totals"]["agent_turns"] == 1
    assert act["totals"]["user_turns"] == 1
    assert act["totals"]["tool_results"] == 1


def test_dual_layer_handoff_and_hydrate_inject(
    kedger_env: Path, runner: CliRunner
) -> None:
    """Agent results + file edits feed activity layer; judgments feed base Anchors."""
    assert runner.invoke(main, ["keys", "init", "--name", "dual"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    ws_id = ws["id"]

    # Messy user + rich agent/tool/edit stream (hooks auto-capture shape)
    turns = [
        {
            "type": "user_prompt",
            "summary": "yo doubles on checkout again, dont touch billing flag",
        },
        {
            "type": "agent_response",
            "summary": (
                "ok so for now: add idempotency keys on charge create, "
                "dont auto ack bad signatures, leave billing flag"
            ),
        },
        {
            "type": "tool_result",
            "summary": "rg charges.py → no Idempotency-Key header",
            "entity_hints": [
                {"entity_type": "file", "name": "src/payments/charges.py"}
            ],
        },
        {
            "type": "file_edit",
            "summary": "Edited src/payments/charges.py (+12/-2)",
            "files": ["src/payments/charges.py"],
            "entity_hints": [
                {"entity_type": "file", "name": "src/payments/charges.py"}
            ],
            "edit_stats": {
                "path": "src/payments/charges.py",
                "edits": 2,
                "lines_added": 12,
                "lines_removed": 2,
            },
        },
        {
            "type": "file_edit",
            "summary": "Edited src/payments/webhooks.py (+4/-1)",
            "files": ["src/payments/webhooks.py"],
            "entity_hints": [
                {"entity_type": "file", "name": "src/payments/webhooks.py"}
            ],
            "edit_stats": {
                "path": "src/payments/webhooks.py",
                "edits": 1,
                "lines_added": 4,
                "lines_removed": 1,
            },
        },
        {
            "type": "agent_response",
            "summary": "patched charges+webhooks; next verify signatures in CI",
        },
    ]
    for i, t in enumerate(turns):
        store.ingest_observation(
            {
                **t,
                "session_id": "sess_dual",
                "workstream_id": ws_id,
                "agent_tool": "cursor",
                "ts": f"2026-08-09T14:{i:02d}:00Z",
            },
            principal_id=p.principal_id,
        )

    working = store.get_working_state(ws_id)
    assert working
    # User ask must not be overwritten by agent turns
    assert "doubles" in (working.get("last_user_ask") or "").lower()
    assert working.get("last_agent_action")
    assert (working.get("activity") or {}).get("totals", {}).get("files", 0) >= 2

    cog = cognify_workstream(
        store, principal=p, force=True, event_type="pre_compact", reseal=False
    )
    assert cog.episode
    act = cog.episode.get("activity") or {}
    assert act.get("totals", {}).get("lines_added", 0) >= 10
    assert act.get("totals", {}).get("agent_turns", 0) >= 1

    promote_candidates(store, principal=p, workstream_id=ws_id, mode="conservative")
    path, pack = seal_handoff(store, principal=p, workstream_slug="default")
    assert path.exists()
    assert pack.get("layers", {}).get("base") == "anchors"
    assert pack.get("layers", {}).get("activity") == "agent_ops"
    pack_act = pack.get("activity") or {}
    assert pack_act.get("totals", {}).get("files", 0) >= 2
    # Base layer still has judgment anchors from agent+user
    stmts = " ".join(a["statement"].lower() for a in (pack.get("anchors") or []))
    assert "idempotency" in stmts or "billing" in stmts or "ack" in stmts

    # sessionStart hydrate inject must show BOTH layers
    out = run_hook(
        store,
        principal=p,
        payload={"type": "SessionStart", "session_id": "next"},
        source="cursor",
    )
    ctx = out.get("additionalContext") or ""
    assert "Base memory" in ctx or "Anchors" in ctx or "[" in ctx
    assert "Agent activity" in ctx or "ops layer" in ctx
    assert "charges.py" in ctx or "files" in ctx.lower()
