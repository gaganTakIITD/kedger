"""Stress capture on more such messy prompts; lock known failure modes."""

from __future__ import annotations

from kedger.cognify.extract import extract_claims_from_span


def _blob(claims) -> str:
    return " ".join(c.statement.lower() for c in claims)


def test_messy_auth_csrf_capture() -> None:
    turns = [
        {
            "id": "1",
            "type": "user_prompt",
            "summary": (
                "bro login is broken on mobile?? cookies? jwt? idk half the team wants "
                "cookies back. dont put secrets in logs tho. also csrf keeps biting us on /api"
            ),
        },
        {
            "id": "2",
            "type": "agent_response",
            "summary": (
                "mobile cant share cookie jar easily. csrf on cookie sessions is painful for apis. "
                "i wont log bearer tokens. maybe short lived jwt + refresh?"
            ),
        },
        {
            "id": "3",
            "type": "user_prompt",
            "summary": (
                "yeah reject cookies for api auth then. must rotate refresh. "
                "old android still sends X-Session-Id dont break that til v3. next fix login first"
            ),
        },
    ]
    claims = extract_claims_from_span(turns)
    blob = _blob(claims)
    assert "cookie" in blob
    assert "log" in blob or "bearer" in blob or "secret" in blob
    assert "refresh" in blob
    assert "android" in blob or "session" in blob
    assert not any(c.statement.lower().startswith("bro ") for c in claims)
    assert not any(c.statement.lower().endswith(" tho") for c in claims)


def test_messy_db_migration_capture() -> None:
    turns = [
        {
            "id": "1",
            "type": "user_prompt",
            "summary": (
                "migration 0042 failed in prod overnight lol. staging was fine ofc. "
                "dont rerun it blindly. maybe lock issue? also never drop users email column "
                "we need it for billing"
            ),
        },
        {
            "id": "2",
            "type": "tool_result",
            "summary": (
                "0042_add_idx: lock wait timeout on users; email column still present; no down migration"
            ),
        },
        {
            "id": "3",
            "type": "agent_response",
            "summary": (
                "ok so for now: dont rerun 0042 in prod, add down migration, keep email column, "
                "take lock in smaller batches. open question whether we need online schema change tool"
            ),
        },
    ]
    claims = extract_claims_from_span(turns)
    blob = _blob(claims)
    kinds = {c.kind for c in claims}
    assert "down migration" in blob
    assert "email" in blob
    assert "rerun" in blob or "0042" in blob
    assert "open_question" in kinds
    # Must not mis-tag the open question as a constraint
    assert not any(
        c.kind == "constraint" and "online schema" in c.statement.lower() for c in claims
    )


def test_messy_notif_spam_capture() -> None:
    turns = [
        {
            "id": "1",
            "type": "user_prompt",
            "summary": (
                "users getting 5 password reset emails wtf. maybe retry queue? "
                "dont disable the whole mailer. feature flag email_v2 leave it. fix the dupes only"
            ),
        },
        {
            "id": "2",
            "type": "agent_response",
            "summary": (
                "looks like missing dedupe key on reset job. i wont touch email_v2 flag. "
                "next patch worker idempotency for reset emails"
            ),
        },
        {
            "id": "3",
            "type": "user_prompt",
            "summary": (
                "cool. and like never send reset to unverified emails?? product said that last week. "
                "park the digests redesign"
            ),
        },
    ]
    claims = extract_claims_from_span(turns)
    blob = _blob(claims)
    assert "mailer" in blob or "disable" in blob
    assert "email_v2" in blob or "flag" in blob
    assert "unverified" in blob
    assert "dedupe" in blob or "idempotency" in blob
