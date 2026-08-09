"""Capture gate: messy unclear human session → crisp Anchors (not paragraph dumps)."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.constants import ANCHOR_STATEMENT_MAX
from kedger.handoff.compile import seal_handoff
from kedger.hydrate.rank import project_hydrate
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint

# Soft max used by extractor; allow tiny slack for ellipsis/capitalization.
CRISP_MAX = 165


MESSY_TURNS = [
    {
        "type": "user_prompt",
        "summary": (
            "hey so like the users endpoint has been weird since friday? "
            "or maybe its the cache idk. staging is fine prod is slow sometimes "
            "and also the worker ate a job last night but that might be unrelated. "
            "can you just look around src/api and the tests? "
            "oh and dont touch the deploy scripts i got burned last time"
        ),
    },
    {
        "type": "agent_response",
        "summary": (
            "I'll inspect src/api/users.py, src/api/cache.py, and the flaky users tests first. "
            "I will avoid deploy scripts. Prod-only slowness with fine staging often points at "
            "cache TTL / stampede; the worker job may be a separate incident."
        ),
    },
    {
        "type": "tool_result",
        "summary": (
            "rg CACHE_TTL src/api/cache.py → CACHE_TTL=60. "
            "users.py get_user has no cache key namespace; concurrent misses stampede redis. "
            "tests/test_users.py marked flaky; sleeps 2s then asserts stale user name."
        ),
        "entity_hints": [
            {"entity_type": "file", "name": "src/api/cache.py"},
            {"entity_type": "file", "name": "src/api/users.py"},
            {"entity_type": "file", "name": "tests/test_users.py"},
        ],
    },
    {
        "type": "user_prompt",
        "summary": (
            "hmm yeah the cache thing sounds right-ish but also sometimes it returns "
            "the wrong user after a rename?? weird. maybe we should bump TTL? "
            "or not? my lead said never cache PII longer than a minute though. "
            "whatever you think. also that flaky test drives me crazy — we should "
            "never retry it silently in CI"
        ),
    },
    {
        "type": "agent_response",
        "summary": (
            "Lead constraint: never cache PII longer than 60s — so do not bump TTL above 60. "
            "Wrong-user-after-rename looks like missing cache key versioning on user id+updated_at. "
            "Decision: keep CACHE_TTL=60, add namespaced keys, invalidate on rename. "
            "Rejection: do not silently retry the flaky users test in CI — fix or quarantine it. "
            "Next: patch cache keys, then fix test_users sleep assertion."
        ),
    },
    {
        "type": "tool_result",
        "summary": (
            "git log -1 src/worker/jobs.py: unrelated OOM fix from last night; "
            "no link to users endpoint. Safe to treat worker as separate."
        ),
        "entity_hints": [{"entity_type": "file", "name": "src/worker/jobs.py"}],
    },
    {
        "type": "user_prompt",
        "summary": (
            "ok cool leave the worker alone then. wait should we even be caching get_user "
            "at all? product might want live reads. i dont know. for now just make the "
            "stale rename stop happening. oh and use the existing redis client, dont "
            "add another library — last agent tried that and we rejected it"
        ),
    },
    {
        "type": "agent_response",
        "summary": (
            "Open question: whether get_user should be cached at all (product live-reads). "
            "For this session: fix stale rename via key versioning; keep existing redis client — "
            "reject adding a new cache library. Avoid deploy scripts. Will edit cache.py + users.py."
        ),
    },
    {
        "type": "file_edit",
        "summary": "Edited src/api/cache.py — namespaced user keys with updated_at version suffix",
        "entity_hints": [{"entity_type": "file", "name": "src/api/cache.py"}],
    },
    {
        "type": "user_prompt",
        "summary": (
            "looks ok-ish. can you also check if staging redis flush is why staging looks fine? "
            "actually never mind save that for later. i gotta jump — just dont forget the "
            "no silent CI retry thing and the PII TTL cap"
        ),
    },
    {
        "type": "agent_response",
        "summary": (
            "Parking staging redis flush as a later open question. "
            "Must remember: never cache PII >60s; never silently retry flaky test_users in CI; "
            "do not touch deploy scripts; worker is out of scope; reject new cache libraries."
        ),
    },
]


REQUIRED_THEMES = [
    ("pii_ttl", ("pii", "60")),
    ("no_silent_ci_retry", ("silently retry", "retry")),
    ("no_deploy_touch", ("deploy",)),
    ("no_new_cache_lib", ("library", "redis client")),
    ("worker_scope", ("worker",)),
]


def _theme_hit(blob: str, keys: tuple[str, ...]) -> bool:
    return any(k in blob for k in keys)


def test_messy_unclear_session_capture_gate(kedger_env: Path, runner: CliRunner) -> None:
    """Gate: unclear intent + agent/tool logs still yield crisp durable memory."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    for i, turn in enumerate(MESSY_TURNS):
        payload = {
            **turn,
            "session_id": "sess_messy",
            "workstream_id": ws["id"],
            "agent_tool": "cursor",
            "ts": f"2026-08-09T08:{i:02d}:00Z",
        }
        store.ingest_observation(payload, principal_id=p.principal_id)

    cog = cognify_workstream(
        store, principal=p, force=True, event_type="sessionEnd", reseal=False
    )
    assert cog.episode is not None
    # Episode digest must not be a single dumped user ramble
    summary = cog.episode.get("summary") or ""
    assert "hey so like the users endpoint" not in summary.lower()
    assert len(cog.candidates) >= 3

    promoted = promote_candidates(
        store, principal=p, workstream_id=ws["id"], mode="conservative"
    )
    assert promoted, "Tier A claims must promote"

    anchors = store.list_anchors(active_only=True)
    assert anchors

    # Crispness: no whole-paragraph Anchors
    for a in anchors:
        stmt = a.get("statement") or ""
        assert len(stmt) <= ANCHOR_STATEMENT_MAX
        assert len(stmt) <= CRISP_MAX, f"noisy paragraph Anchor: {stmt!r}"
        assert "hey so like" not in stmt.lower()
        assert "hmm yeah" not in stmt.lower()

    blob = " ".join(
        f"{a.get('kind')} {a.get('statement')}" for a in anchors
    ).lower()
    blob += " " + summary.lower()

    missing = [
        name
        for name, keys in REQUIRED_THEMES
        if not _theme_hit(blob, keys)
    ]
    assert not missing, f"handoff missing themes {missing}; blob={blob[:500]}"

    # Kinds should be meaningful — not everything as rejection
    kinds = {a.get("kind") for a in anchors}
    assert "constraint" in kinds or "rejection" in kinds
    assert len(kinds) >= 2

    path, pack = seal_handoff(store, principal=p, workstream_slug="default")
    assert path.exists()
    assert pack.get("anchors")

    proj = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        topic="cache PII flaky CI deploy redis",
        purpose="engineering",
    )
    assert proj.anchors, "next-session hydrate must inject something"
    # Live inject should not be dominated by conflict noise from paragraph dumps
    conflict_n = len(proj.conflicts.conflicts) if hasattr(proj.conflicts, "conflicts") else len(proj.conflicts)
    assert conflict_n <= 3, f"too many compose conflicts from noisy capture: {conflict_n}"
    assert len(proj.anchors) >= 4
    assert len(anchors) <= 14, f"still over-promoting: {len(anchors)} anchors"
