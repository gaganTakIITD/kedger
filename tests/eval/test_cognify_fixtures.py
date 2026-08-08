"""Cognify fixtures C1–C14 (runnable subset mapped to current engine)."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

from click.testing import CliRunner

from kedger.boundary import detect_boundary
from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.constants import IDLE_BOUNDARY_MINUTES, RECURRENCE_PROMOTE_THETA
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint


def _init_store(runner: CliRunner):
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    return store, p, ws


def _ingest(store, p, ws_id, texts, session="s"):
    # Use near-now timestamps so idle boundary (25m) does not false-trigger.
    now = datetime.now(timezone.utc)
    for i, text in enumerate(texts):
        ts = (now - timedelta(seconds=len(texts) - i)).strftime("%Y-%m-%dT%H:%M:%SZ")
        store.ingest_observation(
            {
                "type": "user_prompt",
                "session_id": session,
                "workstream_id": ws_id,
                "summary": text,
                "entity_hints": [{"entity_type": "file", "name": f"f{i}.ts"}],
                "ts": ts,
            },
            principal_id=p.principal_id,
        )


def test_c1_pre_compact_hard(kedger_env: Path, runner: CliRunner) -> None:
    store, p, ws = _init_store(runner)
    _ingest(store, p, ws["id"], [f"edit file {i}" for i in range(12)])
    assert runner.invoke(main, ["remember", "reject", "No cookies"]).exit_code == 0
    res = cognify_workstream(
        store, principal=p, event_type="pre_compact", force=False, reseal=True
    )
    assert not res.skipped
    assert res.boundary and res.boundary.kind == "hard"
    store = Store.open(repo_fingerprint())
    assert store.latest_episode(ws["id"]) is not None
    assert any(
        "cookie" in (a.get("statement") or "").lower()
        for a in store.ranked_active_anchors(workstream_id=ws["id"])
    )


def test_c2_session_end_hard_small_span(kedger_env: Path, runner: CliRunner) -> None:
    store, p, ws = _init_store(runner)
    _ingest(store, p, ws["id"], ["a", "b", "c"])
    res = cognify_workstream(
        store, principal=p, event_type="session_end", reseal=True
    )
    assert not res.skipped
    assert res.boundary.kind == "hard"
    assert res.pack_path


def test_c3_idle_gap_uses_constant(kedger_env: Path) -> None:
    now = datetime(2026, 8, 8, 12, 0, tzinfo=timezone.utc)
    last = (now - timedelta(minutes=IDLE_BOUNDARY_MINUTES)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    b = detect_boundary(
        last_obs_ts=last, now=now, span_count=3, min_span=1
    )
    assert b is not None
    assert b.reason == "idle"
    # Below threshold: no idle boundary
    last2 = (now - timedelta(minutes=IDLE_BOUNDARY_MINUTES - 1)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    assert (
        detect_boundary(last_obs_ts=last2, now=now, span_count=3, min_span=1) is None
    )


def test_c5_no_split_lint_noise(kedger_env: Path, runner: CliRunner) -> None:
    store, p, ws = _init_store(runner)
    # Same file cluster — formatter spam should not trigger topic segment cut
    for i in range(15):
        store.ingest_observation(
            {
                "type": "file_edit",
                "session_id": "s",
                "workstream_id": ws["id"],
                "summary": f"format only {i}",
                "entity_hints": [{"entity_type": "file", "name": "src/app.ts"}],
            },
            principal_id=p.principal_id,
        )
    res = cognify_workstream(
        store, principal=p, event_type="note", force=False, reseal=False
    )
    assert res.skipped


def test_c7_recurrence_not_auto_share(kedger_env: Path, runner: CliRunner) -> None:
    store, p, ws = _init_store(runner)
    text = "Reject cookie sessions for auth"
    for ep in range(RECURRENCE_PROMOTE_THETA):
        _ingest(store, p, ws["id"], [text], session=f"s{ep}")
        cognify_workstream(
            Store.open(repo_fingerprint()),
            principal=p,
            event_type="cognify",
            force=True,
            reseal=False,
        )
        store = Store.open(repo_fingerprint())
    shared = runner.invoke(main, ["anchors", "--shared"])
    assert shared.output.strip() == "(none)"


def test_c9_min_span_skip(kedger_env: Path, runner: CliRunner) -> None:
    store, p, ws = _init_store(runner)
    _ingest(store, p, ws["id"], ["one", "two"])
    res = cognify_workstream(
        store,
        principal=p,
        event_type="turn_stop",
        force=False,
        reseal=False,
        min_span=5,
    )
    assert res.skipped
    assert res.skip_reason in {"min_span", "no_boundary"}


def test_c13_provenance_after_prune(kedger_env: Path, runner: CliRunner) -> None:
    store, p, ws = _init_store(runner)
    _ingest(store, p, ws["id"], ["Reject cookies", "Use JWT", "Next: rotate keys"])
    res = cognify_workstream(store, principal=p, force=True, reseal=False)
    assert res.episode
    ids = res.episode["observation_span"]["observation_ids"]
    assert ids
    store = Store.open(repo_fingerprint())
    obs = store.list_observations(workstream_id=ws["id"])
    assert any(o.get("payload_pruned") for o in obs)
    # ids still resolvable
    by_id = {o["id"]: o for o in obs}
    assert all(i in by_id for i in ids)


def test_c14_overcut_guard(kedger_env: Path, runner: CliRunner) -> None:
    store, p, ws = _init_store(runner)
    _ingest(store, p, ws["id"], [f"tool noise {i}" for i in range(8)])
    # Only one forced cognify → one episode (granularity)
    cognify_workstream(store, principal=p, force=True, reseal=False)
    store = Store.open(repo_fingerprint())
    # latest_episode exists; count episodes via list if available
    ep = store.latest_episode(ws["id"])
    assert ep is not None
    assert ep["observation_span"]["count"] == 8


def test_force_cognify_digest_from_anchors(kedger_env: Path, runner: CliRunner) -> None:
    """S3 refine: remember-only then --force yields Anchor digest, not empty stub."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "reject", "Do not use cookie sessions"]
        ).exit_code
        == 0
    )
    cog = runner.invoke(main, ["cognify", "--force"])
    assert cog.exit_code == 0
    assert "Episode (cognify)" not in cog.output or "cookie" in cog.output.lower()
    store = Store.open(repo_fingerprint())
    ws = store.get_workstream_by_slug("default")
    ep = store.latest_episode(ws["id"])
    assert ep is not None
    assert "cookie" in (ep.get("summary") or "").lower() or "Anchors:" in (
        ep.get("summary") or ""
    )
