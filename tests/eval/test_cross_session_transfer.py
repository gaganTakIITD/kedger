"""Cross-session pack import dogfood — wipe store, restore from .kxp, next agent lives.

This is the product path the zlib transcript + dual-layer handoff must serve:
session A builds memory → seal → store gone → hydrate --pack imports → session B inject.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.handoff.compile import seal_handoff
from kedger.handoff.transcript import decompress_transcript, resolve_transcript_archive
from kedger.hooks.runner import run_hook
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint
from kedger.store.paths import project_dir, store_path


def _build_session_a(store: Store, principal) -> tuple[Path, dict]:
    ws = store.ensure_workstream(
        slug="default",
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    ws_id = ws["id"]
    turns = [
        {
            "type": "user_prompt",
            "summary": (
                "checkout doubles on stripe. must send Idempotency-Key. "
                "never auto-ack unverified webhooks. do not flip billing_v2."
            ),
        },
        {
            "type": "agent_response",
            "summary": (
                "Constraint: must send Idempotency-Key on every charge create. "
                "Rejection: never auto-ack unverified webhooks. "
                "Rejection: do not flip billing_v2. "
                "Decision: keep existing Stripe client. "
                "Next: patch charges.py."
            ),
        },
        {
            "type": "file_edit",
            "summary": "Edited src/payments/charges.py (+22/-4)",
            "entity_hints": [
                {"entity_type": "file", "name": "src/payments/charges.py"}
            ],
            "edit_stats": {
                "path": "src/payments/charges.py",
                "edits": 3,
                "lines_added": 22,
                "lines_removed": 4,
            },
        },
        {
            "type": "tool_fail",
            "summary": "pytest tests/test_charges.py → AssertionError missing Idempotency-Key",
        },
        {
            "type": "agent_response",
            "summary": "fixed fixture; Idempotency-Key asserted in CI now",
        },
    ]
    for i, t in enumerate(turns):
        store.ingest_observation(
            {
                **t,
                "session_id": "sess_a",
                "workstream_id": ws_id,
                "agent_tool": "cursor",
                "ts": f"2026-08-09T20:{i:02d}:00Z",
            },
            principal_id=principal.principal_id,
        )
    cog = cognify_workstream(
        store,
        principal=principal,
        workstream_slug="default",
        force=True,
        event_type="pre_compact",
        reseal=False,
    )
    assert cog.episode
    assert cog.episode.get("transcript")
    promote_candidates(
        store, principal=principal, workstream_id=ws_id, mode="conservative"
    )
    # Copy pack out of project dir before wipe
    path, pack = seal_handoff(
        store, principal=principal, workstream_slug="default"
    )
    return path, pack


def test_cross_session_pack_import_restores_next_agent(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "xfer"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    pack_src, pack = _build_session_a(store, p)

    # Park the sealed pack (+ optional sidecar) outside the wiped project tree
    park = tmp_path / "transfer"
    park.mkdir()
    pack_dst = park / pack_src.name
    shutil.copy2(pack_src, pack_dst)
    tmeta = pack.get("transcript_meta") or {}
    if tmeta.get("sidecar"):
        side_src = pack_src.parent / tmeta["sidecar"]
        if side_src.exists():
            shutil.copy2(side_src, park / tmeta["sidecar"])

    # Prove session-A inject had policy + ops before wipe
    out_a = run_hook(
        store,
        principal=p,
        payload={"type": "SessionStart", "session_id": "mid_a"},
        source="cursor",
    )
    ctx_a = (out_a.get("additionalContext") or "").lower()
    assert "idempotency" in ctx_a or "billing" in ctx_a
    assert "charges.py" in ctx_a or "agent activity" in ctx_a

    # Wipe durable store (keep keys) — simulates new machine / lost SQLite
    fp = repo_fingerprint()
    proj = project_dir(fp)
    shutil.rmtree(proj)
    assert not store_path(fp).exists()

    # Session B: open pack → durable import
    hyd = runner.invoke(
        main, ["hydrate", "--pack", str(pack_dst), "--workstream", "default"]
    )
    assert hyd.exit_code == 0, hyd.output
    assert "imported:" in hyd.output
    assert "idempotency" in hyd.output.lower() or "billing" in hyd.output.lower()

    store_b = Store.open(fp)
    p = load_principal()
    ws = store_b.get_workstream_by_slug("default")
    assert ws is not None
    anchors = store_b.ranked_active_anchors(workstream_id=ws["id"])
    blob = " ".join(a["statement"].lower() for a in anchors)
    assert "idempotency" in blob or "billing" in blob

    working = store_b.get_working_state(ws["id"])
    assert working
    assert (working.get("activity") or {}).get("totals", {}).get("files", 0) >= 1
    assert working.get("transcript_meta", {}).get("turn_count", 0) >= 1

    # Live hydrate + next-agent hook inject must work with NO original L0
    live = runner.invoke(main, ["hydrate", "--live"])
    assert live.exit_code == 0, live.output
    assert "idempotency" in live.output.lower() or "billing" in live.output.lower()
    assert "activity:" in live.output.lower() or "charges" in live.output.lower()

    out_b = run_hook(
        store_b,
        principal=p,
        payload={"type": "SessionStart", "session_id": "sess_b"},
        source="cursor",
        workstream_slug="default",
    )
    ctx_b = out_b.get("additionalContext") or ""
    assert "Base memory" in ctx_b or "[" in ctx_b
    assert "Agent activity" in ctx_b or "ops layer" in ctx_b
    assert "idempotency" in ctx_b.lower() or "billing" in ctx_b.lower()
    assert "charges.py" in ctx_b.lower() or "files" in ctx_b.lower()
    assert "Transcript archive" in ctx_b or "zlib" in ctx_b.lower()

    # CLI transcript decompress restores tool_fail phrase lost from Anchors
    dec = runner.invoke(
        main, ["transcript", "decompress", "--pack", str(pack_dst)]
    )
    assert dec.exit_code == 0, dec.output
    assert "AssertionError" in dec.output or "Idempotency-Key" in dec.output

    stats = runner.invoke(main, ["transcript", "stats", "--live"])
    assert stats.exit_code == 0, stats.output
    assert "turn_count" in stats.output


def test_hydrate_no_import_does_not_merge_anchors(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "nomerge"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    pack_src, _pack = _build_session_a(store, p)
    park = tmp_path / "p2"
    park.mkdir()
    pack_dst = park / pack_src.name
    shutil.copy2(pack_src, pack_dst)

    fp = repo_fingerprint()
    shutil.rmtree(project_dir(fp))

    hyd = runner.invoke(
        main,
        ["hydrate", "--pack", str(pack_dst), "--no-import", "--workstream", "default"],
    )
    assert hyd.exit_code == 0, hyd.output
    assert "imported:" not in hyd.output

    store_b = Store.open(fp)
    # ensure empty-ish: no default workstream anchors from import
    ws = store_b.get_workstream_by_slug("default")
    # --no-import should not have created workstream via import; may be absent
    if ws is not None:
        anchors = store_b.ranked_active_anchors(workstream_id=ws["id"])
        assert anchors == []


def test_peer_grant_import_live_continuity(
    kedger_env: Path,
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch,
) -> None:
    """Alice seals for Bob; Bob hydrates+imports and gets next-session inject."""
    from kedger.keys import init_principal

    assert runner.invoke(main, ["keys", "init", "--name", "alice"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    alice = load_principal()
    pack_src, _pack = _build_session_a(store, alice)

    bob_home = tmp_path / "bob-home"
    bob_home.mkdir()
    monkeypatch.setenv("KEDGER_HOME", str(bob_home))
    bob = init_principal(name="bob")
    recip = tmp_path / "bob.json"
    recip.write_text(
        json.dumps(
            {
                "principal_id": bob.principal_id,
                "name": "bob",
                "public_key_b64": bob.public_key_b64,
                "x25519_public_b64": bob.x25519_public_b64,
            }
        ),
        encoding="utf-8",
    )

    # Alice grants Bob and reseals
    monkeypatch.setenv("KEDGER_HOME", str(kedger_env))
    grant = runner.invoke(
        main,
        [
            "grant",
            "--to",
            bob.principal_id,
            "--recipient-file",
            str(recip),
        ],
    )
    assert grant.exit_code == 0, grant.output
    handoff = runner.invoke(main, ["handoff"])
    assert handoff.exit_code == 0, handoff.output
    pack_line = [ln for ln in handoff.output.splitlines() if ln.startswith("pack:")][0]
    pack_path = Path(pack_line.split(":", 1)[1].strip())

    park = tmp_path / "peer-pack"
    park.mkdir()
    pack_dst = park / pack_path.name
    shutil.copy2(pack_path, pack_dst)

    # Bob opens + imports on his empty home
    monkeypatch.setenv("KEDGER_HOME", str(bob_home))
    hyd = runner.invoke(main, ["hydrate", "--pack", str(pack_dst)])
    assert hyd.exit_code == 0, hyd.output
    assert "imported:" in hyd.output

    store_b = Store.open(repo_fingerprint())
    bob_p = load_principal()
    out = run_hook(
        store_b,
        principal=bob_p,
        payload={"type": "SessionStart", "session_id": "bob_next"},
        source="cursor",
    )
    ctx = (out.get("additionalContext") or "").lower()
    assert "idempotency" in ctx or "billing" in ctx
    assert "charges.py" in ctx or "agent activity" in ctx or "ops layer" in ctx
