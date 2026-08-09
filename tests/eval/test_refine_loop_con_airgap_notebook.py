"""Refine-loop eval: CoN evidence notes, AirGap purpose packs, notebook walk."""

from __future__ import annotations

import json
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.evidence.notes import note_evidence
from kedger.graph import notebook_walk, upsert_entity
from kedger.handoff.compile import compile_handoff_pack
from kedger.hydrate import project_hydrate
from kedger.hydrate.purpose import minimize_anchor_for_purpose
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint
from kedger.why import explain_anchor


def test_con_note_labels_support_vs_unknown() -> None:
    """Chain-of-Note 2311.09210: support vs unknown without inventing."""
    support = note_evidence(
        {"snippet": "Use JWT bearer tokens for API auth middleware"},
        anchor_statement="Use JWT bearer tokens for API auth",
    )
    unknown = note_evidence(
        {"snippet": "Unrelated weather forecast for Seattle tomorrow"},
        anchor_statement="Use JWT bearer tokens for API auth",
    )
    assert support["relevance"] == "support"
    assert unknown["relevance"] == "unknown"


def test_why_attaches_con_notes_and_abstain(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(main, ["remember", "decision", "Use JWT bearer tokens"])
    anc = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(":", 1)[
        1
    ].strip()
    store = Store.open(repo_fingerprint())
    p = load_principal()
    store.insert_evidence(
        supports_anchor_id=anc,
        snippet="JWT bearer tokens validated in auth middleware",
        source_ref="obs://support",
    )
    store.insert_evidence(
        supports_anchor_id=anc,
        snippet="Purple banana smoothie recipe with kale",
        source_ref="obs://noise",
    )
    expl = explain_anchor(store, anchor_id=anc, principal_id=p.principal_id)
    assert len(expl["evidence"]) == 2
    labels = {e["note"]["relevance"] for e in expl["evidence"]}
    assert "support" in labels
    assert "unknown" in labels
    assert expl["abstain"] is False

    # All-unknown → abstain
    rem2 = runner.invoke(main, ["remember", "gotcha", "Never commit .env files"])
    anc2 = [ln for ln in rem2.output.splitlines() if ln.startswith("id:")][0].split(
        ":", 1
    )[1].strip()
    store.insert_evidence(
        supports_anchor_id=anc2,
        snippet="Stock market closed higher on Friday afternoon",
        source_ref="obs://ood",
    )
    expl2 = explain_anchor(store, anchor_id=anc2, principal_id=p.principal_id)
    assert expl2["abstain"] is True
    assert expl2["evidence"][0]["note"]["relevance"] == "unknown"


def test_airgap_purpose_strips_reason_on_hydrate(
    kedger_env: Path, runner: CliRunner
) -> None:
    """AirGapAgent 2405.05175: third_party purpose drops reason/provenance."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main,
        [
            "remember",
            "decision",
            "Use company SSO for admin",
            "--reason",
            "internal ops preference from security review",
        ],
    )
    assert rem.exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    full = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        purpose="engineering",
    )
    mini = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        purpose="third_party",
    )
    assert any("reason" in a for a in full.anchors)
    assert all("reason" not in a for a in mini.anchors)
    assert all("provenance" not in a for a in mini.anchors)
    assert all("secret_hits" not in a for a in mini.anchors)

    cli = runner.invoke(main, ["hydrate", "--live", "--purpose", "third_party"])
    assert cli.exit_code == 0, cli.output
    assert "purpose:      third_party" in cli.output
    assert "internal ops preference" not in cli.output


def test_airgap_minimize_helper_fail_closed() -> None:
    anc = {
        "id": "anc_x",
        "kind": "decision",
        "statement": "Use Redis",
        "reason": "secret ops note",
        "status": "active",
        "provenance": {"actor_principal_id": "p1"},
        "secret_hits": ["openai_sk"],
        "shareable": False,
    }
    m = minimize_anchor_for_purpose(anc, "export")
    assert "reason" not in m
    assert "provenance" not in m
    assert "secret_hits" not in m
    assert m["statement"] == "Use Redis"


def test_notebook_walk_respects_call_budget(
    kedger_env: Path, runner: CliRunner
) -> None:
    """GraphReader: call cap separate from node budget; notebook entries recorded."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(main, ["remember", "decision", "Use JWT for auth"])
    anc = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(":", 1)[
        1
    ].strip()
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    for i in range(6):
        ent = upsert_entity(store, entity_type="file", name=f"auth/mod_{i}.ts")
        store.insert_edge(
            edge_type="ABOUT", from_id=anc, to_id=ent["id"], workstream_id=ws["id"]
        )
    nb = notebook_walk(
        store,
        [anc],
        topic_terms={"auth", "jwt"},
        max_calls=3,
        budget=20,
        max_hops=2,
    )
    assert nb.call_count <= 3
    assert len(nb.entries) <= 3
    assert nb.terminated in {"budget", "topic_satisfied", "empty"}

    proj = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        topic="auth jwt",
        walk_budget=8,
        notebook_max_calls=4,
    )
    assert proj.notebook_calls <= 4
    assert isinstance(proj.notebook, list)
    cli = runner.invoke(
        main, ["hydrate", "--live", "--topic", "auth", "--notebook-calls", "2"]
    )
    assert cli.exit_code == 0, cli.output
    assert "notebook:" in cli.output


def test_compile_pack_purpose_minimized(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert (
        runner.invoke(
            main,
            [
                "remember",
                "decision",
                "Prefer Postgres for state",
                "--reason",
                "team voted after incident postmortem",
            ],
        ).exit_code
        == 0
    )
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    pack = compile_handoff_pack(
        store, workstream=ws, principal=p, purpose="third_party"
    )
    assert pack.get("purpose") == "third_party"
    assert pack["anchors"]
    assert all("reason" not in a for a in pack["anchors"])
