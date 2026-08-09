"""Truly messy unlabeled prompts (typos, slang, no Constraint: labels)."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream, extract_claims_from_span
from kedger.handoff.compile import seal_handoff
from kedger.hydrate.rank import project_hydrate
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint

# Intentionally poorly written — no tidy agent labels.
RAW_MESSY = [
    {
        "type": "user_prompt",
        "summary": (
            "yo the checkout keeps double charging ppl sometimes after timeouts?? "
            "also webhooks r late or idk maybe its the queue. staging fine prod angry. "
            "dont touch billing_v2 flag pls finance will murder me. look at payments stuff i guess"
        ),
    },
    {
        "type": "agent_response",
        "summary": (
            "looking at charges and webhooks. double charge after timeout usually missing "
            "idempotency. i wont touch the billing flag. webhook delay could be retries without jitter."
        ),
    },
    {
        "type": "tool_result",
        "summary": (
            "charges.py post has no Idempotency-Key. webhook_jobs retries on 500 no backoff. "
            "429s have no Retry-After header"
        ),
        "entity_hints": [
            {"entity_type": "file", "name": "src/payments/charges.py"},
            {"entity_type": "file", "name": "src/worker/webhook_jobs.py"},
        ],
    },
    {
        "type": "user_prompt",
        "summary": (
            "ugh yeah that. lead was yelling we gotta put idempotency key on charge creates always. "
            "and like dont ack webhooks if sig verify fails?? rate limit bump?? probably not "
            "product will cry. just stop doubles. also no new stripe sdk we already rejected "
            "that mess last quarter"
        ),
    },
    {
        "type": "agent_response",
        "summary": (
            "ok so for now: add idempotency keys on charge create, dont auto ack bad signatures, "
            "leave rate limits, leave billing flag, keep current stripe client not a second sdk. "
            "next ill patch charges.py then webhook verify"
        ),
    },
    {
        "type": "user_prompt",
        "summary": (
            "cool whatever leave rate limit alone yeah. do webhooks need same store as charges??? "
            "idk park that. gotta go — remember the verify thing"
        ),
    },
]

THEMES = [
    ("idempotency", ("idempotency",)),
    ("no_billing_flag", ("billing", "flag")),
    ("no_auto_ack", ("ack", "signature")),
    ("no_second_sdk", ("sdk", "stripe")),
    ("rate_limit", ("rate",)),
]


def test_extract_raw_messy_unlabeled() -> None:
    claims = extract_claims_from_span(
        [{"id": str(i), **t} for i, t in enumerate(RAW_MESSY)]
    )
    assert len(claims) >= 5, f"too few claims from messy chat: {claims}"
    blob = " ".join(c.statement.lower() for c in claims)
    assert "idempotency" in blob
    assert "billing" in blob or "flag" in blob
    assert "ack" in blob or "signature" in blob
    assert "sdk" in blob or "stripe" in blob
    # Must not keep the opening yo-ramble as one Anchor
    assert not any(c.statement.lower().startswith("yo the checkout") for c in claims)
    assert all(len(c.statement) <= 165 for c in claims)


def test_e2e_raw_messy_handoff(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "messy"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    for i, turn in enumerate(RAW_MESSY):
        store.ingest_observation(
            {
                **turn,
                "session_id": "sess_raw_messy",
                "workstream_id": ws["id"],
                "agent_tool": "cursor",
                "ts": f"2026-08-09T12:{i:02d}:00Z",
            },
            principal_id=p.principal_id,
        )

    cog = cognify_workstream(
        store, principal=p, force=True, event_type="sessionEnd", reseal=False
    )
    assert cog.episode
    assert "yo the checkout" not in (cog.episode.get("summary") or "").lower()

    promote_candidates(store, principal=p, workstream_id=ws["id"], mode="conservative")
    path, pack = seal_handoff(store, principal=p, workstream_slug="default")
    anchors = pack.get("anchors") or []
    assert anchors
    blob = " ".join(a["statement"].lower() for a in anchors)
    blob += " " + (cog.episode.get("summary") or "").lower()
    missing = [n for n, keys in THEMES if not any(k in blob for k in keys)]
    assert not missing, f"missing {missing}; anchors={[a['statement'] for a in anchors]}"

    proj = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        topic="idempotency webhook billing sdk",
        purpose="engineering",
    )
    assert len(proj.anchors) >= 3
    doc = runner.invoke(main, ["doctor"])
    assert doc.exit_code == 0
    assert path.exists()
