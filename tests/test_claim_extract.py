"""Unit tests for deterministic multi-claim extraction."""

from __future__ import annotations

from kedger.cognify.extract import (
    CLAIM_SOFT_MAX,
    extract_claims_from_span,
    extract_claims_from_text,
)


def test_labeled_agent_paragraph_splits_into_crisp_claims() -> None:
    text = (
        "Lead constraint: never cache PII longer than 60s — so do not bump TTL above 60. "
        "Wrong-user-after-rename looks like missing cache key versioning. "
        "Decision: keep CACHE_TTL=60, add namespaced keys, invalidate on rename. "
        "Rejection: do not silently retry the flaky users test in CI — fix or quarantine it. "
        "Next: patch cache keys, then fix test_users sleep assertion."
    )
    claims = extract_claims_from_text(text, source_type="agent_response")
    kinds = {c.kind for c in claims}
    assert "constraint" in kinds
    assert "rejection" in kinds
    assert "decision" in kinds
    assert "next_step" in kinds
    assert all(len(c.statement) <= CLAIM_SOFT_MAX + 5 for c in claims)
    # Must not keep the whole paragraph as one claim
    assert all(len(c.statement) < len(text) - 40 for c in claims)
    blob = " ".join(c.statement.lower() for c in claims)
    assert "pii" in blob
    assert "silently retry" in blob or "flaky" in blob


def test_messy_user_ramble_does_not_become_one_anchor() -> None:
    text = (
        "hey so like the users endpoint has been weird since friday? "
        "or maybe its the cache idk. staging is fine prod is slow sometimes "
        "and also the worker ate a job last night but that might be unrelated. "
        "can you just look around src/api and the tests? "
        "oh and dont touch the deploy scripts i got burned last time"
    )
    claims = extract_claims_from_text(text, source_type="user_prompt")
    assert claims, "should extract at least the deploy rejection"
    assert any(c.kind == "rejection" for c in claims)
    assert all(len(c.statement) <= CLAIM_SOFT_MAX + 5 for c in claims)
    assert not any("hey so like" in c.statement.lower() for c in claims)


def test_span_dedupes_overlapping_agent_and_user_claims() -> None:
    span = [
        {
            "id": "obs_1",
            "type": "user_prompt",
            "summary": (
                "my lead said never cache PII longer than a minute though. "
                "we should never retry it silently in CI"
            ),
        },
        {
            "id": "obs_2",
            "type": "agent_response",
            "summary": (
                "Lead constraint: never cache PII longer than 60s. "
                "Rejection: do not silently retry the flaky users test in CI."
            ),
        },
    ]
    claims = extract_claims_from_span(span)
    pii = [c for c in claims if "pii" in c.statement.lower()]
    assert len(pii) <= 2
    assert any(c.kind == "constraint" for c in pii)


def test_tool_fail_feeds_gotcha_claims() -> None:
    from kedger.cognify.extract import extract_claims_from_span

    claims = extract_claims_from_span(
        [
            {
                "id": "1",
                "type": "tool_fail",
                "summary": "pytest → AssertionError missing Idempotency-Key",
            },
            {
                "id": "2",
                "type": "tool_fail",
                "summary": "psql → ERROR: deadlock detected on users",
            },
        ]
    )
    kinds = {c.kind for c in claims}
    assert "gotcha" in kinds
    blob = " ".join(c.statement.lower() for c in claims)
    assert "idempotency" in blob or "assertion" in blob
    assert "deadlock" in blob


def test_promote_skips_near_duplicate_idempotency(kedger_env, runner) -> None:
    from click.testing import CliRunner
    from kedger.cli.main import main
    from kedger.keys import load_principal
    from kedger.promote import promote_candidates
    from kedger.store import Store, repo_fingerprint

    assert runner.invoke(main, ["keys", "init", "--name", "dedupe"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    store.remember(
        "constraint",
        "Must send Idempotency-Key on charge create",
        principal_id=p.principal_id,
        workstream_id=ws["id"],
    )
    store.insert_promotion_candidate(
        {
            "schema_version": "kedger.memory.v1",
            "id": "anc_dup_test",
            "tier": "A",
            "kind": "constraint",
            "statement": "Must send Idempotency-Key",
            "status": "candidate",
            "heat": 3.0,
            "recurrence": 1,
            "workstream_id": ws["id"],
            "created_at": "2026-08-09T00:00:00Z",
            "shareable": False,
        }
    )
    out = promote_candidates(
        store, principal=p, workstream_id=ws["id"], mode="conservative"
    )
    assert out == []
    anchors = store.ranked_active_anchors(workstream_id=ws["id"])
    stmts = [a["statement"] for a in anchors if a["kind"] == "constraint"]
    assert len(stmts) == 1
