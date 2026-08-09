"""Smoke: self-made complex messy payments session → capture → handoff → doctor."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream, extract_claims_from_span
from kedger.compose import compose_view
from kedger.constants import ANCHOR_STATEMENT_MAX
from kedger.handoff.compile import seal_handoff
from kedger.hydrate.rank import project_hydrate
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint

CRISP_MAX = 165

# Brand-new messy transcript (payments / rate-limit / webhooks) — unclear intent,
# agent + tool results mixed in. Built for this smoke; not copied from prior fixtures.
PAYMENTS_MESSY = [
    {
        "type": "user_prompt",
        "summary": (
            "ugh payments have been weird after the stripe bump? or maybe rate limit, "
            "not sure. some charges double on retry and webhooks feel late. "
            "also please dont flip the billing feature flag, finance will scream. "
            "poke around src/payments and the worker maybe"
        ),
    },
    {
        "type": "agent_response",
        "summary": (
            "I'll inspect charge + webhook paths and leave the billing feature flag alone. "
            "Double charges on retry often mean missing idempotency keys; webhook lag can be "
            "queue backlog or signature verify failures."
        ),
    },
    {
        "type": "tool_result",
        "summary": (
            "rg Idempotency-Key src/payments → no header on POST /v1/charges. "
            "webhook worker retries 5xx without jitter; rate limit middleware returns 429 "
            "without Retry-After. feature flag billing_v2=true in staging only."
        ),
        "entity_hints": [
            {"entity_type": "file", "name": "src/payments/charges.py"},
            {"entity_type": "file", "name": "src/payments/webhooks.py"},
            {"entity_type": "file", "name": "src/worker/webhook_jobs.py"},
        ],
    },
    {
        "type": "user_prompt",
        "summary": (
            "yeah idempotency sounds right I guess. lead said we must send Idempotency-Key "
            "on every charge create. and never auto-ack webhooks we cannot verify. "
            "rate limit — should we raise it? idk product might hate that. "
            "for now stop the double charge. oh and reject adding a second payments SDK, "
            "last time that was a mess"
        ),
    },
    {
        "type": "agent_response",
        "summary": (
            "Constraint: must send Idempotency-Key on every charge create. "
            "Rejection: never auto-ack webhooks we cannot verify. "
            "Rejection: do not add a second payments SDK — keep existing Stripe client. "
            "Rejection: do not flip billing feature flag. "
            "Open question: whether to raise rate limits (product call). "
            "Decision: for this session fix double-charge via idempotency keys first. "
            "Next: add Idempotency-Key on charge create, then verify webhook signatures, "
            "then inspect 429 Retry-After."
        ),
    },
    {
        "type": "tool_result",
        "summary": (
            "git blame src/worker/webhook_jobs.py: retry storm from missing jitter after "
            "stripe timeout; unrelated to feature flag. Safe to treat flag as out of scope."
        ),
        "entity_hints": [{"entity_type": "file", "name": "src/worker/webhook_jobs.py"}],
    },
    {
        "type": "user_prompt",
        "summary": (
            "ok leave rate limit config alone for now too. wait should webhooks share the "
            "charge idempotency store? maybe? whatever — just make double charges stop. "
            "i have to run — dont forget the verify-before-ack rule"
        ),
    },
    {
        "type": "agent_response",
        "summary": (
            "Parking shared idempotency store for webhooks as an open question. "
            "Must remember: Idempotency-Key on charge create; never auto-ack unverified "
            "webhooks; do not flip billing feature flag; do not add a second payments SDK; "
            "leave rate limit config alone this session."
        ),
    },
    {
        "type": "file_edit",
        "summary": "Edited src/payments/charges.py — attach Idempotency-Key from request id",
        "entity_hints": [{"entity_type": "file", "name": "src/payments/charges.py"}],
    },
]

REQUIRED = [
    ("idempotency", ("idempotency",)),
    ("webhook_verify", ("auto-ack", "unverified", "verify")),
    ("no_second_sdk", ("second payments", "payments sdk", "stripe client")),
    ("no_feature_flag", ("feature flag", "billing")),
    ("rate_limit_park", ("rate limit", "raise rate")),
]


def test_compose_complementary_rejections_both_kept() -> None:
    """Parallel policies (different slots) must ADD, not ESCALATE-drop."""
    a = {
        "id": "anc_a",
        "kind": "rejection",
        "statement": "Do not flip billing feature flag",
        "status": "active",
    }
    b = {
        "id": "anc_b",
        "kind": "rejection",
        "statement": "Do not add a second payments SDK",
        "status": "active",
    }
    kept, cs = compose_view([a, b])
    assert len(kept) == 2
    assert not any(c["action"] == "ESCALATE" for c in cs.conflicts)


def test_payments_messy_capture_smoke(kedger_env: Path, runner: CliRunner) -> None:
    """End-to-end smoke on a self-made unclear payments transcript."""
    assert runner.invoke(main, ["keys", "init", "--name", "smoke"]).exit_code == 0
    doc = runner.invoke(main, ["doctor"])
    assert doc.exit_code == 0
    assert "doctor: all checks passed" in doc.output

    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )

    obs = []
    for i, turn in enumerate(PAYMENTS_MESSY):
        obs.append(
            store.ingest_observation(
                {
                    **turn,
                    "session_id": "sess_payments_messy",
                    "workstream_id": ws["id"],
                    "agent_tool": "cursor",
                    "ts": f"2026-08-09T10:{i:02d}:00Z",
                },
                principal_id=p.principal_id,
            )
        )

    claims = extract_claims_from_span(obs)
    assert len(claims) >= 5
    assert all(len(c.statement) <= CRISP_MAX for c in claims)
    assert not any("ugh payments" in c.statement.lower() for c in claims)

    cog = cognify_workstream(
        store, principal=p, force=True, event_type="sessionEnd", reseal=False
    )
    assert cog.episode is not None
    assert "ugh payments" not in (cog.episode.get("summary") or "").lower()

    promoted = promote_candidates(
        store, principal=p, workstream_id=ws["id"], mode="conservative"
    )
    assert promoted

    anchors = store.list_anchors(active_only=True)
    assert 5 <= len(anchors) <= 14
    for a in anchors:
        stmt = a.get("statement") or ""
        assert len(stmt) <= ANCHOR_STATEMENT_MAX
        assert len(stmt) <= CRISP_MAX
        assert "ugh payments" not in stmt.lower()

    blob = " ".join(f"{a.get('kind')} {a.get('statement')}" for a in anchors).lower()
    blob += " " + (cog.episode.get("summary") or "").lower()
    missing = [
        name
        for name, keys in REQUIRED
        if not any(k in blob for k in keys)
    ]
    assert not missing, f"missing themes {missing}; blob={blob[:600]}"

    path, pack = seal_handoff(store, principal=p, workstream_slug="default")
    assert path.exists()
    assert len(pack.get("anchors") or []) >= 5

    proj = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        topic="payments idempotency webhook rate limit",
        purpose="engineering",
    )
    # Complementary policies should survive into next-session inject
    assert len(proj.anchors) >= 4
    conflict_n = (
        len(proj.conflicts.conflicts)
        if hasattr(proj.conflicts, "conflicts")
        else len(proj.conflicts)
    )
    assert conflict_n <= 3, f"unexpected escalate storm: {conflict_n}"

    # Doctor still green after cognify/promote/seal
    doc2 = runner.invoke(main, ["doctor"])
    assert doc2.exit_code == 0
    assert "all checks passed" in doc2.output

    # CLI hydrate smoke
    live = runner.invoke(
        main, ["hydrate", "--live", "--topic", "idempotency webhook", "--purpose", "engineering"]
    )
    assert live.exit_code == 0, live.output
    assert "Idempotency" in live.output or "idempotency" in live.output.lower()
