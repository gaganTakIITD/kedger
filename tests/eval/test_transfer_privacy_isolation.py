"""Privacy + workstream isolation on pack transfer."""

from __future__ import annotations

import shutil
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.handoff.compile import seal_handoff
from kedger.handoff.transcript import compress_transcript, decompress_transcript, turns_from_observations
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint
from kedger.store.paths import project_dir


def test_transcript_redacts_secrets_before_compress() -> None:
    obs = [
        {
            "id": "1",
            "type": "user_prompt",
            "ts": "2026-08-09T01:00:00Z",
            "summary": "here is my key sk-abcdefghijklmnopqrstuvwxyz012345 and keep going",
            "session_id": "s",
        }
    ]
    turns = turns_from_observations(obs)
    assert "sk-abcdefghijklmnopqrstuvwxyz012345" not in turns[0]["summary"]
    assert "REDACTED" in turns[0]["summary"]
    archive = compress_transcript(turns)
    restored = decompress_transcript(archive)
    blob = restored[0]["summary"]
    assert "sk-abcdefghijklmnopqrstuvwxyz012345" not in blob
    assert "REDACTED" in blob


def test_import_into_named_workstream_isolated(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "iso"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="payments", principal_id=p.principal_id, signing_key=p.signing_key
    )
    store.ingest_observation(
        {
            "type": "user_prompt",
            "summary": "must send Idempotency-Key; do not flip billing_v2",
            "session_id": "iso",
            "workstream_id": ws["id"],
            "agent_tool": "cursor",
            "ts": "2026-08-09T02:00:00Z",
        },
        principal_id=p.principal_id,
    )
    store.ingest_observation(
        {
            "type": "agent_response",
            "summary": (
                "Constraint: must send Idempotency-Key. "
                "Rejection: do not flip billing_v2."
            ),
            "session_id": "iso",
            "workstream_id": ws["id"],
            "agent_tool": "cursor",
            "ts": "2026-08-09T02:01:00Z",
        },
        principal_id=p.principal_id,
    )
    cognify_workstream(
        store,
        principal=p,
        workstream_slug="payments",
        force=True,
        event_type="pre_compact",
        reseal=False,
    )
    promote_candidates(
        store, principal=p, workstream_id=ws["id"], mode="conservative"
    )
    path, _pack = seal_handoff(
        store, principal=p, workstream_slug="payments"
    )
    park = tmp_path / "iso"
    park.mkdir()
    dst = park / path.name
    shutil.copy2(path, dst)

    shutil.rmtree(project_dir(repo_fingerprint()))

    # Import into a different local slug — must not spill into default-empty
    hyd = runner.invoke(
        main, ["hydrate", "--pack", str(dst), "--workstream", "imported-payments"]
    )
    assert hyd.exit_code == 0, hyd.output

    store_b = Store.open(repo_fingerprint())
    paid = store_b.get_workstream_by_slug("imported-payments")
    default = store_b.get_workstream_by_slug("default")
    assert paid is not None
    paid_anchors = store_b.ranked_active_anchors(workstream_id=paid["id"])
    assert any("idempotency" in (a.get("statement") or "").lower() for a in paid_anchors)
    if default is not None:
        def_anchors = store_b.ranked_active_anchors(workstream_id=default["id"])
        assert def_anchors == []
