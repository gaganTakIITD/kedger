"""Reloop gates: never-log constraints, short decisions, tool_fail promote, HEAD install."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.cognify.extract import extract_claims_from_span, extract_claims_from_text
from kedger.handoff.compile import seal_handoff
from kedger.hooks.runner import run_hook
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint
from kedger.store.paths import project_dir


def test_never_log_unlabeled_is_constraint() -> None:
    for text in (
        "never log Authorization bearers",
        "never cache PII longer than 60s",
        "never log secrets in CI output",
    ):
        claims = extract_claims_from_text(text, source_type="user_prompt")
        assert claims, text
        assert claims[0].kind == "constraint", (text, claims)
        assert "never" in claims[0].statement.lower()


def test_short_tech_decisions_survive() -> None:
    for text in ("Decision: use JWT", "use JWT", "Decision: adopt Redis"):
        claims = extract_claims_from_text(text, source_type="agent_response")
        assert any(c.kind == "decision" for c in claims), (text, claims)


def test_gotta_idempotency_normalizes() -> None:
    claims = extract_claims_from_text(
        "gotta idempotency key", source_type="user_prompt"
    )
    assert claims
    assert claims[0].kind == "constraint"
    stmt = claims[0].statement.lower()
    assert "idempotency" in stmt
    assert "must" in stmt
    assert stmt != "must idempotency key"


def test_tool_fail_gotcha_promotes_on_conservative(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "gotcha"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    store.ingest_observation(
        {
            "type": "tool_fail",
            "summary": "pytest → 401 missing Authorization on /api/me",
            "session_id": "g",
            "workstream_id": ws["id"],
            "agent_tool": "cursor",
            "ts": "2026-08-09T08:00:00Z",
        },
        principal_id=p.principal_id,
    )
    store.ingest_observation(
        {
            "type": "agent_response",
            "summary": "Constraint: must use short-lived JWT. Next: fix bearer extract.",
            "session_id": "g",
            "workstream_id": ws["id"],
            "agent_tool": "cursor",
            "ts": "2026-08-09T08:01:00Z",
        },
        principal_id=p.principal_id,
    )
    cog = cognify_workstream(
        store, principal=p, force=True, event_type="pre_compact", reseal=False
    )
    assert cog.episode
    promoted = promote_candidates(
        store, principal=p, workstream_id=ws["id"], mode="conservative"
    )
    kinds = {a["kind"] for a in promoted}
    assert "gotcha" in kinds or any(
        a.get("kind") == "gotcha"
        for a in store.ranked_active_anchors(workstream_id=ws["id"])
    )
    blob = " ".join(
        a["statement"].lower()
        for a in store.ranked_active_anchors(workstream_id=ws["id"])
    )
    assert "401" in blob or "authorization" in blob


def test_import_installs_head_for_session_start_recovery(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "head"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    store.ingest_observation(
        {
            "type": "user_prompt",
            "summary": "never log Authorization bearers; must use short-lived JWT",
            "session_id": "h",
            "workstream_id": ws["id"],
            "agent_tool": "cursor",
            "ts": "2026-08-09T09:00:00Z",
        },
        principal_id=p.principal_id,
    )
    store.ingest_observation(
        {
            "type": "agent_response",
            "summary": (
                "Constraint: never log Authorization bearers. "
                "Constraint: must use short-lived JWT. "
                "Decision: use JWT."
            ),
            "session_id": "h",
            "workstream_id": ws["id"],
            "agent_tool": "cursor",
            "ts": "2026-08-09T09:01:00Z",
        },
        principal_id=p.principal_id,
    )
    cognify_workstream(
        store, principal=p, force=True, event_type="pre_compact", reseal=False
    )
    promote_candidates(
        store, principal=p, workstream_id=ws["id"], mode="conservative"
    )
    path, pack = seal_handoff(store, principal=p, workstream_slug="default")
    park = tmp_path / "headpack"
    park.mkdir()
    dst = park / path.name
    shutil.copy2(path, dst)

    # Wipe store entirely (including packs) then import from parked pack
    shutil.rmtree(project_dir(repo_fingerprint()))
    hyd = runner.invoke(main, ["hydrate", "--pack", str(dst)])
    assert hyd.exit_code == 0, hyd.output

    store_b = Store.open(repo_fingerprint())
    ws_b = store_b.get_workstream_by_slug("default")
    assert ws_b is not None
    packs_dir = project_dir(repo_fingerprint()) / "packs" / ws_b["id"]
    assert (packs_dir / "HEAD").exists()
    hid = (packs_dir / "HEAD").read_text(encoding="utf-8").strip()
    assert (packs_dir / f"{hid}.kxp").exists()

    # Clear Anchors to force sessionStart HEAD auto-import path
    with store_b.connection() as conn:
        conn.execute("UPDATE anchors SET status = 'archived'")
        # also rewrite record_json status for ranked_active filter
        rows = conn.execute("SELECT id, record_json FROM anchors").fetchall()
        for row in rows:
            rec = json.loads(row["record_json"])
            rec["status"] = "archived"
            conn.execute(
                "UPDATE anchors SET record_json = ? WHERE id = ?",
                (json.dumps(rec), row["id"]),
            )

    p = load_principal()
    out = run_hook(
        store_b,
        principal=p,
        payload={"type": "SessionStart", "session_id": "recover"},
        source="cursor",
    )
    ctx = out.get("additionalContext") or ""
    assert "jwt" in ctx.lower() or "authorization" in ctx.lower() or "bearer" in ctx.lower()


def test_empty_session_start_skips_junk_ingest_and_empty_inject(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "empty"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    out = run_hook(
        store,
        principal=p,
        payload={"type": "SessionStart", "session_id": "empty1"},
        source="cursor",
    )
    # No Anchors yet → empty inject (no skeleton spam)
    assert out.get("additionalContext") in (None, "")
    effects = out.get("side_effects") or []
    ingest = [e for e in effects if e.get("effect") == "ingest"]
    assert ingest and ingest[0].get("status") == "skipped_empty_session_start"
    obs = store.list_observations()
    assert not any(o.get("type") == "session_start" for o in obs)


def test_dont_put_secrets_in_logs_is_constraint() -> None:
    claims = extract_claims_from_text(
        "dont put secrets in logs tho", source_type="user_prompt"
    )
    assert claims
    assert claims[0].kind == "constraint"
    assert "secret" in claims[0].statement.lower() or "log" in claims[0].statement.lower()


def test_doctor_reports_head_after_pack_export(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "doc"]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "constraint", "Must use JWT access tokens"]
        ).exit_code
        == 0
    )
    assert runner.invoke(main, ["handoff"]).exit_code == 0
    doc = runner.invoke(main, ["doctor"])
    assert doc.exit_code == 0, doc.output
    assert "handoff_head" in doc.output
    assert "promotion_queue" in doc.output
    assert ".kxp" in doc.output
