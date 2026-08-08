"""GraphReader walk budget + MEXTRA-style memory dump probes."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.graph import upsert_entity
from kedger.hydrate import project_hydrate
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint


def test_walk_budget_caps_expand(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(main, ["remember", "decision", "Use JWT for auth"])
    anc = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(":", 1)[
        1
    ].strip()
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    # Link a chain of entities/anchors via ABOUT edges
    for i in range(8):
        ent = upsert_entity(store, entity_type="file", name=f"auth/mod_{i}.ts")
        store.insert_edge(
            edge_type="ABOUT", from_id=anc, to_id=ent["id"], workstream_id=ws["id"]
        )
    tight = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        walk_budget=3,
        walk_hops=1,
    )
    wide = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        walk_budget=20,
        walk_hops=2,
    )
    assert tight.walk_budget == 3
    assert len(tight.walk_ids) <= 3
    assert len(wide.walk_ids) >= len(tight.walk_ids)

    cli = runner.invoke(main, ["hydrate", "--live", "--walk-budget", "2"])
    assert cli.exit_code == 0, cli.output
    assert "walk_budget:  2" in cli.output


def test_memory_dump_does_not_regurgitate_secret(
    kedger_env: Path, runner: CliRunner
) -> None:
    """MEXTRA-ish: secret material must not appear in hydrate/status dumps."""
    secret = "sk-dumpProbeKeyABCDEFGH0123456789"
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main,
        [
            "remember",
            "gotcha",
            "Do not paste API keys into chat",
            "--reason",
            f"saw {secret} in logs",
        ],
    )
    assert rem.exit_code == 0
    assert secret not in rem.output
    hyd = runner.invoke(main, ["hydrate", "--live"])
    assert hyd.exit_code == 0
    assert secret not in hyd.output
    status = runner.invoke(main, ["status", "--list"])
    assert secret not in status.output
    shared = runner.invoke(main, ["anchors", "--shared"])
    assert secret not in shared.output
