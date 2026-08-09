"""10-case dual-layer handoff smoke — spectrum of user/agent detail.

Cases range from very-detailed user+agent contexts down to sparse/none,
so we can see how session handoff behaves for the next agent.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.handoff.compile import seal_handoff
from kedger.hooks.runner import run_hook
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint


@dataclass
class Case:
    id: str
    title: str
    user_detail: str  # high | medium | low | none
    agent_detail: str  # high | medium | low | none
    turns: list[dict[str, Any]]
    expect_themes: list[str]
    expect_files: list[str]
    expect_min_lines_added: int


# ---------------------------------------------------------------------------
# 10 self-made cases
# ---------------------------------------------------------------------------

CASES: list[Case] = [
    Case(
        id="C01",
        title="Very detailed user + very detailed agent (payments idempotency)",
        user_detail="high",
        agent_detail="high",
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "Production checkout double-charges on Stripe timeout retries. "
                    "Lead constraint: must send Idempotency-Key on every charge create. "
                    "Never auto-ack webhooks we cannot verify. Do not flip billing_v2 flag. "
                    "Do not add a second payments SDK — keep existing Stripe client. "
                    "Leave rate-limit config alone this session. Next: stop doubles only."
                ),
            },
            {
                "type": "agent_response",
                "summary": (
                    "Constraint: must send Idempotency-Key on every charge create. "
                    "Rejection: never auto-ack unverified webhooks. "
                    "Rejection: do not flip billing_v2. "
                    "Rejection: do not add a second payments SDK. "
                    "Decision: keep existing Stripe client. "
                    "Next: patch charges.py then webhook signature verify."
                ),
            },
            {
                "type": "tool_result",
                "summary": "rg Idempotency-Key src/payments → 0 hits on POST /v1/charges",
                "entity_hints": [
                    {"entity_type": "file", "name": "src/payments/charges.py"}
                ],
            },
            {
                "type": "file_edit",
                "files": ["src/payments/charges.py"],
                "entity_hints": [
                    {"entity_type": "file", "name": "src/payments/charges.py"}
                ],
                "edit_stats": {
                    "path": "src/payments/charges.py",
                    "edits": 3,
                    "lines_added": 28,
                    "lines_removed": 4,
                },
                "summary": "Edited src/payments/charges.py (+28/-4)",
            },
            {
                "type": "file_edit",
                "files": ["src/payments/webhooks.py"],
                "entity_hints": [
                    {"entity_type": "file", "name": "src/payments/webhooks.py"}
                ],
                "edit_stats": {
                    "path": "src/payments/webhooks.py",
                    "edits": 2,
                    "lines_added": 15,
                    "lines_removed": 2,
                },
                "summary": "Edited src/payments/webhooks.py (+15/-2)",
            },
            {
                "type": "agent_response",
                "summary": (
                    "Patched charges+webhooks. Open question: shared idempotency store "
                    "for webhooks? Parked. Next: CI signature verify fixture."
                ),
            },
        ],
        expect_themes=["idempotency", "billing", "webhook", "stripe"],
        expect_files=["charges.py", "webhooks.py"],
        expect_min_lines_added=40,
    ),
    Case(
        id="C02",
        title="Very detailed user + medium agent (auth cookies→JWT)",
        user_detail="high",
        agent_detail="medium",
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "API auth still cookie sessions; CSRF on /api and mobile cannot share "
                    "the jar. Reject cookies for API auth. Must use short-lived JWT access "
                    "with rotating opaque refresh. Never log Authorization bearers. "
                    "Android still sends X-Session-Id until v3 — keep compat shim. "
                    "Dashboard cookies are out of scope."
                ),
            },
            {
                "type": "agent_response",
                "summary": (
                    "Rejecting cookie sessions for API. Decision: short-lived JWT + opaque "
                    "refresh. Won't log bearers. Keep X-Session-Id shim until Android v3. "
                    "Next: mint login JWT then refresh rotation."
                ),
            },
            {
                "type": "file_edit",
                "files": ["src/auth/session.py"],
                "entity_hints": [
                    {"entity_type": "file", "name": "src/auth/session.py"}
                ],
                "edit_stats": {
                    "path": "src/auth/session.py",
                    "edits": 2,
                    "lines_added": 22,
                    "lines_removed": 18,
                },
                "summary": "Edited src/auth/session.py (+22/-18)",
            },
        ],
        expect_themes=["cookie", "jwt", "android"],
        expect_files=["session.py"],
        expect_min_lines_added=20,
    ),
    Case(
        id="C03",
        title="Medium user + very detailed agent (DB migration 0042)",
        user_detail="medium",
        agent_detail="high",
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "migration 0042 blew up in prod overnight, staging was fine. "
                    "dont rerun blindly. never drop users.email — billing needs it."
                ),
            },
            {
                "type": "agent_response",
                "summary": (
                    "Rejection: do not rerun 0042 in prod. "
                    "Constraint: never drop users email column. "
                    "Decision: add down migration. "
                    "Decision: take lock in smaller batches. "
                    "Open question: whether we need an online schema-change tool. "
                    "Next: write 0042_down.sql then batched index create."
                ),
            },
            {
                "type": "tool_result",
                "summary": "0042_add_idx: lock wait timeout; email column present; no down migration",
                "entity_hints": [
                    {"entity_type": "file", "name": "migrations/0042_add_idx.sql"}
                ],
            },
            {
                "type": "file_edit",
                "files": ["migrations/0042_down.sql"],
                "entity_hints": [
                    {"entity_type": "file", "name": "migrations/0042_down.sql"}
                ],
                "edit_stats": {
                    "path": "migrations/0042_down.sql",
                    "edits": 1,
                    "lines_added": 40,
                    "lines_removed": 0,
                },
                "summary": "Edited migrations/0042_down.sql (+40/-0)",
            },
            {
                "type": "file_edit",
                "files": ["migrations/0042_add_idx.sql"],
                "entity_hints": [
                    {"entity_type": "file", "name": "migrations/0042_add_idx.sql"}
                ],
                "edit_stats": {
                    "path": "migrations/0042_add_idx.sql",
                    "edits": 1,
                    "lines_added": 12,
                    "lines_removed": 3,
                },
                "summary": "Edited migrations/0042_add_idx.sql (+12/-3)",
            },
        ],
        expect_themes=["0042", "email", "down"],
        expect_files=["0042_down.sql", "0042_add_idx.sql"],
        expect_min_lines_added=50,
    ),
    Case(
        id="C04",
        title="Very detailed user + low agent (notif spam — agent vague)",
        user_detail="high",
        agent_detail="low",
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "Users get 5 password-reset emails. Do not disable the whole mailer. "
                    "Leave feature flag email_v2 alone. Never send reset to unverified emails. "
                    "Fix dedupe only — park digests redesign."
                ),
            },
            {
                "type": "agent_response",
                "summary": "looking into the mailer stuff, will poke around",
            },
            {
                "type": "file_edit",
                "files": ["src/worker/reset_mail.py"],
                "entity_hints": [
                    {"entity_type": "file", "name": "src/worker/reset_mail.py"}
                ],
                "edit_stats": {
                    "path": "src/worker/reset_mail.py",
                    "edits": 1,
                    "lines_added": 6,
                    "lines_removed": 1,
                },
                "summary": "Edited src/worker/reset_mail.py (+6/-1)",
            },
        ],
        expect_themes=["mailer", "unverified", "email_v2"],
        expect_files=["reset_mail.py"],
        expect_min_lines_added=5,
    ),
    Case(
        id="C05",
        title="Low user + very detailed agent (agent carries the session)",
        user_detail="low",
        agent_detail="high",
        turns=[
            {"type": "user_prompt", "summary": "cache weird??"},
            {
                "type": "agent_response",
                "summary": (
                    "Lead constraint: never cache PII longer than 60s. "
                    "Rejection: do not bump CACHE_TTL above 60. "
                    "Rejection: do not silently retry flaky test_users in CI. "
                    "Decision: keep CACHE_TTL=60, add namespaced keys, invalidate on rename. "
                    "Gotcha: wrong-user-after-rename = missing key versioning. "
                    "Next: patch cache.py then fix test_users."
                ),
            },
            {
                "type": "tool_result",
                "summary": "CACHE_TTL=60; get_user has no cache key namespace",
                "entity_hints": [
                    {"entity_type": "file", "name": "src/api/cache.py"}
                ],
            },
            {
                "type": "file_edit",
                "files": ["src/api/cache.py"],
                "entity_hints": [
                    {"entity_type": "file", "name": "src/api/cache.py"}
                ],
                "edit_stats": {
                    "path": "src/api/cache.py",
                    "edits": 2,
                    "lines_added": 18,
                    "lines_removed": 5,
                },
                "summary": "Edited src/api/cache.py (+18/-5)",
            },
            {
                "type": "file_edit",
                "files": ["tests/test_users.py"],
                "entity_hints": [
                    {"entity_type": "file", "name": "tests/test_users.py"}
                ],
                "edit_stats": {
                    "path": "tests/test_users.py",
                    "edits": 1,
                    "lines_added": 9,
                    "lines_removed": 7,
                },
                "summary": "Edited tests/test_users.py (+9/-7)",
            },
        ],
        expect_themes=["pii", "ttl", "cache"],
        expect_files=["cache.py", "test_users.py"],
        expect_min_lines_added=25,
    ),
    Case(
        id="C06",
        title="Medium user + medium agent (feature flag kill-switch)",
        user_detail="medium",
        agent_detail="medium",
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "rollout of search_v3 is flaky in EU. dont remove the kill switch. "
                    "must keep fallback to search_v2 for 14 days. next: gate EU only."
                ),
            },
            {
                "type": "agent_response",
                "summary": (
                    "Rejection: do not remove kill switch. "
                    "Constraint: keep search_v2 fallback 14 days. "
                    "Decision: gate search_v3 to EU only for now. "
                    "Next: edit flags.yaml then edge router."
                ),
            },
            {
                "type": "file_edit",
                "files": ["config/flags.yaml"],
                "entity_hints": [
                    {"entity_type": "file", "name": "config/flags.yaml"}
                ],
                "edit_stats": {
                    "path": "config/flags.yaml",
                    "edits": 1,
                    "lines_added": 8,
                    "lines_removed": 2,
                },
                "summary": "Edited config/flags.yaml (+8/-2)",
            },
        ],
        expect_themes=["kill", "fallback", "eu"],
        expect_files=["flags.yaml"],
        expect_min_lines_added=8,
    ),
    Case(
        id="C07",
        title="Low user + low agent + rich edits (ops-heavy, speech-light)",
        user_detail="low",
        agent_detail="low",
        turns=[
            {"type": "user_prompt", "summary": "fix the lint pls"},
            {"type": "agent_response", "summary": "on it"},
            {
                "type": "file_edit",
                "files": ["src/a.py"],
                "entity_hints": [{"entity_type": "file", "name": "src/a.py"}],
                "edit_stats": {
                    "path": "src/a.py",
                    "edits": 4,
                    "lines_added": 2,
                    "lines_removed": 14,
                },
                "summary": "Edited src/a.py (+2/-14)",
            },
            {
                "type": "file_edit",
                "files": ["src/b.py"],
                "entity_hints": [{"entity_type": "file", "name": "src/b.py"}],
                "edit_stats": {
                    "path": "src/b.py",
                    "edits": 3,
                    "lines_added": 1,
                    "lines_removed": 11,
                },
                "summary": "Edited src/b.py (+1/-11)",
            },
            {
                "type": "file_edit",
                "files": ["src/c.py"],
                "entity_hints": [{"entity_type": "file", "name": "src/c.py"}],
                "edit_stats": {
                    "path": "src/c.py",
                    "edits": 2,
                    "lines_added": 0,
                    "lines_removed": 9,
                },
                "summary": "Edited src/c.py (+0/-9)",
            },
            {"type": "tool_result", "summary": "ruff check → 0 errors"},
        ],
        expect_themes=[],  # speech thin — ops should still hand off
        expect_files=["a.py", "b.py", "c.py"],
        expect_min_lines_added=0,  # mostly deletions
    ),
    Case(
        id="C08",
        title="High user + none agent speech (only tools/edits after ask)",
        user_detail="high",
        agent_detail="none",
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "Must redact openai_sk and bearer tokens before any log ship. "
                    "Never commit .env. Reject adding a new secrets scanner library — "
                    "use existing redact module. Next: wire redact into ingest only."
                ),
            },
            # no agent_response — only tools/edits (hook still fires)
            {
                "type": "tool_result",
                "summary": "rg openai_sk src/ → 2 fixtures only",
                "entity_hints": [
                    {"entity_type": "file", "name": "src/kedger/redact/scanner.py"}
                ],
            },
            {
                "type": "file_edit",
                "files": ["src/kedger/ingest/pipeline.py"],
                "entity_hints": [
                    {"entity_type": "file", "name": "src/kedger/ingest/pipeline.py"}
                ],
                "edit_stats": {
                    "path": "src/kedger/ingest/pipeline.py",
                    "edits": 1,
                    "lines_added": 11,
                    "lines_removed": 0,
                },
                "summary": "Edited src/kedger/ingest/pipeline.py (+11/-0)",
            },
        ],
        expect_themes=["redact", "bearer", "secret"],
        expect_files=["pipeline.py"],
        expect_min_lines_added=10,
    ),
    Case(
        id="C09",
        title="None/minimal user + none/minimal agent (near-empty session)",
        user_detail="none",
        agent_detail="none",
        turns=[
            {"type": "user_prompt", "summary": "ok"},
            {"type": "agent_response", "summary": "ok"},
        ],
        expect_themes=[],
        expect_files=[],
        expect_min_lines_added=0,
    ),
    Case(
        id="C10",
        title="Mixed messy user + detailed agent + tool fail (partial success)",
        user_detail="medium",
        agent_detail="high",
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "yo rate limiter biting EU partners?? idk bump it or not. "
                    "dont touch billing. leave worker alone. fix 429 Retry-After maybe"
                ),
            },
            {
                "type": "agent_response",
                "summary": (
                    "Rejection: do not touch billing. "
                    "Rejection: leave worker alone / out of scope. "
                    "Open question: whether to raise EU rate limits (product). "
                    "Decision: for now add Retry-After on 429 only. "
                    "Next: patch middleware then partner fixture."
                ),
            },
            {
                "type": "tool_fail",
                "summary": "pytest tests/test_rate_limit.py → AssertionError missing Retry-After",
            },
            {
                "type": "file_edit",
                "files": ["src/api/middleware/rate_limit.py"],
                "entity_hints": [
                    {
                        "entity_type": "file",
                        "name": "src/api/middleware/rate_limit.py",
                    }
                ],
                "edit_stats": {
                    "path": "src/api/middleware/rate_limit.py",
                    "edits": 2,
                    "lines_added": 14,
                    "lines_removed": 3,
                },
                "summary": "Edited src/api/middleware/rate_limit.py (+14/-3)",
            },
            {
                "type": "agent_response",
                "summary": (
                    "Retry-After added. Tool fail was fixture lag — re-run green. "
                    "Still open: EU quota bump needs product."
                ),
            },
        ],
        expect_themes=["billing", "retry-after", "rate", "worker"],
        expect_files=["rate_limit.py"],
        expect_min_lines_added=14,
    ),
]


def _score_handoff(
    case: Case,
    *,
    anchors: list[dict[str, Any]],
    activity: dict[str, Any],
    inject: str,
    episode_summary: str,
) -> dict[str, Any]:
    """Rate how insightful the next-agent handoff is (0–5 style dimensions)."""
    blob = " ".join(a.get("statement", "").lower() for a in anchors)
    blob += " " + (episode_summary or "").lower()
    inject_l = (inject or "").lower()
    totals = (activity or {}).get("totals") or {}
    files = (activity or {}).get("files") or []

    themes_hit = sum(1 for t in case.expect_themes if t.lower() in blob)
    themes_total = max(1, len(case.expect_themes)) if case.expect_themes else 0
    theme_score = (
        5
        if not case.expect_themes
        else round(5 * themes_hit / themes_total, 2)
    )

    files_hit = sum(
        1
        for ef in case.expect_files
        if any(ef.lower() in str(f.get("path", "")).lower() for f in files)
        or ef.lower() in inject_l
    )
    files_total = max(1, len(case.expect_files)) if case.expect_files else 0
    file_score = (
        5
        if not case.expect_files
        else round(5 * files_hit / files_total, 2)
    )

    lines_ok = int(totals.get("lines_added") or 0) >= case.expect_min_lines_added
    # For deletion-heavy cases, also accept lines_removed signal
    if case.id == "C07":
        lines_ok = int(totals.get("lines_removed") or 0) >= 20 and int(
            totals.get("files") or 0
        ) >= 3
    line_score = 5.0 if lines_ok else (
        3.0 if int(totals.get("lines_added") or 0) > 0 or int(totals.get("files") or 0) > 0 else 1.0
    )

    has_base = "## base memory" in inject_l or "[constraint]" in inject_l or "[rejection]" in inject_l or "[decision]" in inject_l or bool(anchors)
    has_ops = "agent activity" in inject_l or "ops layer" in inject_l
    dual_score = 5.0 if (has_base and has_ops) else (3.0 if has_base or has_ops else 0.0)

    # Sparse sessions: dual still valuable if ops or honest empty base
    if case.user_detail == "none" and case.agent_detail == "none":
        # C09 — expect thin but non-crashing handoff
        insight = 2.0 if inject else 0.0
        dual_score = 5.0 if has_ops or has_base or inject else 0.0
        theme_score = 5.0
        file_score = 5.0
        line_score = 5.0
    else:
        insight = round(
            0.35 * theme_score + 0.25 * file_score + 0.20 * line_score + 0.20 * dual_score,
            2,
        )

    return {
        "theme_score": theme_score,
        "file_score": file_score,
        "line_delta_score": line_score,
        "dual_layer_score": dual_score,
        "insight_for_next_agent": insight,
        "themes_hit": themes_hit,
        "themes_total": len(case.expect_themes),
        "files_hit": files_hit,
        "anchor_count": len(anchors),
        "activity_totals": totals,
        "inject_has_base": has_base,
        "inject_has_ops": has_ops,
    }


def _run_case(case: Case, store: Store, principal) -> dict[str, Any]:
    ws = store.ensure_workstream(
        slug=f"ws-{case.id.lower()}",
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    ws_id = ws["id"]
    for i, turn in enumerate(case.turns):
        store.ingest_observation(
            {
                **turn,
                "session_id": f"sess_{case.id}",
                "workstream_id": ws_id,
                "agent_tool": "cursor",
                "ts": f"2026-08-09T16:{i:02d}:00Z",
            },
            principal_id=principal.principal_id,
        )

    cog = cognify_workstream(
        store,
        principal=principal,
        workstream_slug=ws["slug"],
        force=True,
        event_type="pre_compact",
        reseal=False,
    )
    promote_candidates(
        store, principal=principal, workstream_id=ws_id, mode="conservative"
    )
    _path, pack = seal_handoff(
        store, principal=principal, workstream_slug=ws["slug"]
    )
    out = run_hook(
        store,
        principal=principal,
        payload={"type": "SessionStart", "session_id": f"next_{case.id}"},
        source="cursor",
        workstream_slug=ws["slug"],
    )
    inject = out.get("additionalContext") or ""
    anchors = pack.get("anchors") or []
    activity = pack.get("activity") or (cog.episode or {}).get("activity") or {}
    scores = _score_handoff(
        case,
        anchors=anchors,
        activity=activity,
        inject=inject,
        episode_summary=(cog.episode or {}).get("summary") or "",
    )
    return {
        "id": case.id,
        "title": case.title,
        "user_detail": case.user_detail,
        "agent_detail": case.agent_detail,
        "layers": pack.get("layers"),
        "anchors": [
            {"kind": a.get("kind"), "statement": a.get("statement")} for a in anchors
        ],
        "activity_totals": (activity or {}).get("totals"),
        "activity_files": (activity or {}).get("files"),
        "episode_summary": ((cog.episode or {}).get("summary") or "")[:280],
        "inject_preview": inject[:900],
        "scores": scores,
    }


def test_ten_case_handoff_spectrum_smoke(kedger_env: Path, runner: CliRunner) -> None:
    """Run all 10 spectrum cases; require average next-agent insight >= 3.0."""
    assert runner.invoke(main, ["keys", "init", "--name", "spectrum"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()

    results = [_run_case(c, store, p) for c in CASES]
    insights = [r["scores"]["insight_for_next_agent"] for r in results]
    avg = sum(insights) / len(insights)

    # Persist artifact for humans
    out_dir = Path("artifacts/eval")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "handoff_spectrum_10.json").write_text(
            json.dumps({"average_insight": avg, "cases": results}, indent=2, default=str)
        )
    except OSError:
        pass

    # Hard gates
    assert len(results) == 10
    assert avg >= 3.0, f"average insight {avg} < 3.0: {insights}"

    # Detailed ends should be strong
    by_id = {r["id"]: r for r in results}
    assert by_id["C01"]["scores"]["insight_for_next_agent"] >= 4.0
    assert by_id["C01"]["scores"]["inject_has_base"]
    assert by_id["C01"]["scores"]["inject_has_ops"]
    assert by_id["C05"]["scores"]["insight_for_next_agent"] >= 3.5  # agent carries
    assert by_id["C07"]["activity_totals"]["files"] >= 3  # ops-heavy
    assert by_id["C09"]["scores"]["insight_for_next_agent"] >= 1.0  # thin but alive

    # Line deltas must surface for edit-heavy cases
    assert (by_id["C01"]["activity_totals"] or {}).get("lines_added", 0) >= 40
    assert (by_id["C03"]["activity_totals"] or {}).get("lines_added", 0) >= 50
