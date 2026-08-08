from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.store import Store, repo_fingerprint


def _init(runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0


def test_remember_and_forget_supersedes(kedger_env: Path, runner: CliRunner) -> None:
    _init(runner)

    rem = runner.invoke(
        main,
        [
            "remember",
            "reject",
            "Do not use cookie sessions",
            "--reason",
            "CSRF",
        ],
    )
    assert rem.exit_code == 0, rem.output
    assert "kind:    rejection" in rem.output
    anc_line = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0]
    anc_id = anc_line.split(":", 1)[1].strip()
    assert anc_id.startswith("anc_")

    store = Store.open(repo_fingerprint())
    counts = store.counts()
    assert counts["anchors_active"] == 1

    forgot = runner.invoke(main, ["forget", anc_id])
    assert forgot.exit_code == 0, forgot.output
    assert "SUPERSEDES" in forgot.output

    store = Store.open(repo_fingerprint())
    counts = store.counts()
    assert counts["anchors_active"] == 0
    assert counts["anchors_superseded"] == 1
    assert counts["supersedes_edges"] == 1

    # row still present — never hard-deleted
    assert store.get_anchor(anc_id) is not None
    assert store.get_anchor(anc_id)["status"] == "superseded"
    assert store.get_anchor(anc_id)["superseded_by"]
