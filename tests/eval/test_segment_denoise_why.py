"""SeCom segment score + ConflictRAG why conflicts + ingest denoise."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.boundary.segment import segment_continuity_score
from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.constants import SEGMENT_THETA
from kedger.redact.denoise import denoise_summary
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint


def test_segment_score_topic_shift() -> None:
    auth = [
        {
            "summary": "auth jwt middleware",
            "entity_hints": [{"entity_type": "file", "name": "auth/jwt.ts"}],
        }
        for _ in range(4)
    ]
    billing = [
        {
            "summary": "billing stripe webhook",
            "entity_hints": [{"entity_type": "file", "name": "billing/stripe.ts"}],
        }
        for _ in range(4)
    ]
    score = segment_continuity_score(auth + billing)
    assert score is not None
    assert score < SEGMENT_THETA


def test_segment_score_same_cluster_high() -> None:
    span = [
        {
            "summary": f"format only {i}",
            "entity_hints": [{"entity_type": "file", "name": "src/app.ts"}],
        }
        for i in range(8)
    ]
    score = segment_continuity_score(span)
    assert score is not None
    assert score >= SEGMENT_THETA


def test_denoise_strips_formatter_spam() -> None:
    assert denoise_summary("formatter only ran on src/app.ts") == ""
    assert denoise_summary("Reject cookie sessions for auth") != ""


def test_why_includes_conflicts_for_dual_decisions(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem1 = runner.invoke(main, ["remember", "decision", "Use Redis sessions"])
    anc1 = [ln for ln in rem1.output.splitlines() if ln.startswith("id:")][0].split(":", 1)[
        1
    ].strip()
    assert (
        runner.invoke(
            main, ["remember", "decision", "Use JWT bearer tokens"]
        ).exit_code
        == 0
    )
    why = runner.invoke(main, ["why", anc1])
    assert why.exit_code == 0, why.output
    assert "conflicts" in why.output
    assert "ESCALATE" in why.output or "contradiction" in why.output


def test_topic_shift_soft_cognify(kedger_env: Path, runner: CliRunner) -> None:
    """C4-ish: auth files then billing files → soft segment boundary episode."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    for i in range(4):
        store.ingest_observation(
            {
                "type": "file_edit",
                "session_id": "s",
                "workstream_id": ws["id"],
                "summary": f"auth change {i}",
                "entity_hints": [{"entity_type": "file", "name": "auth/session.ts"}],
            },
            principal_id=p.principal_id,
        )
    for i in range(4):
        store.ingest_observation(
            {
                "type": "file_edit",
                "session_id": "s",
                "workstream_id": ws["id"],
                "summary": f"billing change {i}",
                "entity_hints": [{"entity_type": "file", "name": "billing/invoice.ts"}],
            },
            principal_id=p.principal_id,
        )
    res = cognify_workstream(
        store, principal=p, event_type="turn_stop", force=False, reseal=False
    )
    assert not res.skipped, res.skip_reason
    assert res.boundary is not None
    assert res.boundary.reason in {"segment_score", "turn_stop"}
