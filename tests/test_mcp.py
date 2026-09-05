"""Minimal MCP read tools."""

from __future__ import annotations

import json
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.mcp.registry import TOOL_SPECS, call_tool
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint


def test_mcp_tools_registered() -> None:
    names = {t["name"] for t in TOOL_SPECS}
    assert names == {"hydrate", "anchors_get"}


def test_mcp_hydrate_and_anchors_get(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "mcp"]).exit_code == 0
    rem = runner.invoke(
        main, ["remember", "constraint", "Must send Idempotency-Key on charge create"]
    )
    assert rem.exit_code == 0, rem.output
    store = Store.open(repo_fingerprint())
    p = load_principal()
    anchors = store.ranked_active_anchors(
        workstream_id=store.get_workstream_by_slug("default")["id"]
    )
    assert anchors
    hyd = call_tool("hydrate", {"workstream": "default"}, store=store, principal=p)
    assert hyd.get("anchors")
    assert any("Idempotency" in a["statement"] for a in hyd["anchors"])
    got = call_tool(
        "anchors_get", {"anchor_id": anchors[0]["id"]}, store=store, principal=p
    )
    assert got["anchor"]["id"] == anchors[0]["id"]


def test_mcp_cli_call(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "mcpcli"]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "decision", "Use JWT for API auth"]
        ).exit_code
        == 0
    )
    res = runner.invoke(main, ["mcp", "call", "hydrate", "--args-json", "{}"])
    assert res.exit_code == 0, res.output
    data = json.loads(res.output)
    assert data["anchors"]


def test_mcp_anchors_get_404(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "mcp404"]).exit_code == 0
    res = runner.invoke(
        main,
        ["mcp", "call", "anchors_get", "--args-json", '{"anchor_id":"anc_missing"}'],
    )
    assert res.exit_code == 404
