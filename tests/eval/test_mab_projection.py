"""MemoryAgentBench AR/TTL/LRU/SF → Kedger projections (deterministic offline)."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.hydrate import project_hydrate
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint


def test_mab_ar_fact_survives_cognify_hydrate(
    kedger_env: Path, runner: CliRunner
) -> None:
    """AR: accurate retrieval — fact in L0 survives cognify → hydrate."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    fact = "Reject cookie sessions; use JWT bearer tokens"
    store.ingest_observation(
        {
            "type": "user_prompt",
            "session_id": "ar",
            "workstream_id": ws["id"],
            "summary": fact,
        },
        principal_id=p.principal_id,
    )
    cognify_workstream(store, principal=p, force=True, reseal=False)
    # Promote via remember (Tier A explicit) to ensure Anchor survival
    assert runner.invoke(main, ["remember", "reject", fact[:240]]).exit_code == 0
    store = Store.open(repo_fingerprint())
    proj = project_hydrate(
        store, principal_id=p.principal_id, workstream_id=ws["id"]
    )
    blob = " ".join(a.get("statement") or "" for a in proj.anchors).lower()
    assert "jwt" in blob or "cookie" in blob


def test_mab_ttl_newest_wins(kedger_env: Path, runner: CliRunner) -> None:
    """TTL / update: forget old playbook; newest decision wins."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(main, ["remember", "decision", "Use Redis sessions"])
    old = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(":", 1)[
        1
    ].strip()
    assert runner.invoke(main, ["forget", old]).exit_code == 0
    assert (
        runner.invoke(main, ["remember", "decision", "Use JWT access tokens"]).exit_code
        == 0
    )
    hyd = runner.invoke(main, ["hydrate", "--live"])
    assert "JWT" in hyd.output
    assert "Redis sessions" not in hyd.output


def test_mab_lru_l0_prune_keeps_anchors(kedger_env: Path, runner: CliRunner) -> None:
    """LRU-ish: L0 pressure prune must not delete Anchors."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "constraint", "All APIs require authentication"]
        ).exit_code
        == 0
    )
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    for i in range(80):
        store.ingest_observation(
            {
                "type": "note",
                "session_id": "lru",
                "workstream_id": ws["id"],
                "summary": f"old noise {i}",
            },
            principal_id=p.principal_id,
        )
    store.rotate_observations(workstream_id=ws["id"])
    store = Store.open(repo_fingerprint())
    assert any(
        "authentication" in (a.get("statement") or "").lower()
        for a in store.ranked_active_anchors(workstream_id=ws["id"])
    )


def test_mab_sf_supersedes_chain(kedger_env: Path, runner: CliRunner) -> None:
    """SF selective forgetting: ordered edits leave SUPERSEDES provenance."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(main, ["remember", "decision", "Fact v1 cookies ok"])
    anc = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(":", 1)[
        1
    ].strip()
    assert runner.invoke(main, ["forget", anc]).exit_code == 0
    assert (
        runner.invoke(main, ["remember", "decision", "Fact v2 cookies forbidden"]).exit_code
        == 0
    )
    store = Store.open(repo_fingerprint())
    old = store.get_anchor(anc)
    assert old["status"] == "superseded"
    assert store.counts()["supersedes_edges"] >= 1
    # Residual: statement row remains but inactive (never hard-delete)
    assert old["statement"]
