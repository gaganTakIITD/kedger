"""Phase E: hook normalize + SESSION_START inject + PRE_COMPACT cognify."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.hooks.normalize import normalize_hook_event
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint


def test_normalize_eight_events() -> None:
    for raw, expected in [
        ("SessionStart", "session_start"),
        ("user_prompt", "user_prompt"),
        ("agent_response", "agent_response"),
        ("AfterFileEdit", "file_edit"),
        ("tool_fail", "tool_fail"),
        ("stop", "stop"),
        ("PreCompact", "pre_compact"),
        ("SessionEnd", "session_end"),
    ]:
        n = normalize_hook_event({"type": raw, "summary": "x"})
        assert n["observation"]["type"] == expected


def test_normalize_ide_native_names() -> None:
    cases = [
        ("beforeSubmitPrompt", "user_prompt"),
        ("afterAgentResponse", "agent_response"),
        ("afterFileEdit", "file_edit"),
        ("postToolUseFailure", "tool_fail"),
        ("preCompact", "pre_compact"),
        ("sessionEnd", "session_end"),
        ("UserPromptSubmit", "user_prompt"),
        ("PostToolUseFailure", "tool_fail"),
    ]
    for raw, expected in cases:
        n = normalize_hook_event({"type": raw, "summary": "x"})
        assert n["observation"]["type"] == expected, raw


def test_normalize_user_prompt_includes_hydrate_inject() -> None:
    n = normalize_hook_event({"type": "beforeSubmitPrompt", "prompt": "hi"})
    assert n["observation"]["type"] == "user_prompt"
    assert n["side_effects"] == ["hydrate_inject", "ingest"]
    edit = normalize_hook_event(
        {"hook_event_name": "PostToolUse", "tool_name": "Edit", "summary": "f"}
    )
    assert edit["observation"]["type"] == "file_edit"
    other = normalize_hook_event(
        {"hook_event_name": "PostToolUse", "tool_name": "Bash", "summary": "ls"}
    )
    assert other["observation"]["type"] == "tool_result"


def test_session_start_hydrate_inject(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "constraint", "JWT only for sessions"]
        ).exit_code
        == 0
    )
    payload = {"type": "SessionStart", "session_id": "s1"}
    res = runner.invoke(
        main,
        ["hook", "--source", "cursor"],
        input=json.dumps(payload),
    )
    assert res.exit_code == 0, res.output
    data = json.loads(res.output)
    assert data["ok"] is True
    ctx = data.get("additional_context") or data.get("additionalContext")
    assert ctx
    assert "JWT only" in ctx
    assert any(s["effect"] == "hydrate_inject" for s in data["side_effects"])


def test_pre_compact_hard_cognify(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert runner.invoke(main, ["remember", "goal", "Finish auth"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    store.ingest_observation(
        {
            "type": "user_prompt",
            "workstream_id": ws["id"],
            "session_id": "s",
            "summary": "Reject cookies; use JWT",
        },
        principal_id=p.principal_id,
    )
    payload = {"type": "PreCompact", "session_id": "s", "workstream_id": ws["id"]}
    res = runner.invoke(
        main,
        ["hook", "--source", "claude_code"],
        input=json.dumps(payload),
    )
    assert res.exit_code == 0, res.output
    data = json.loads(res.output)
    assert any(s.get("effect") == "cognify_hard" for s in data["side_effects"])
    store = Store.open(repo_fingerprint())
    assert store.latest_episode(ws["id"]) is not None


def test_hook_still_capability_gated(kedger_env: Path, runner: CliRunner, tmp_path: Path, monkeypatch) -> None:
    # Alice has memory
    assert runner.invoke(main, ["keys", "init", "--name", "alice"]).exit_code == 0
    assert runner.invoke(main, ["remember", "decision", "Use refresh tokens"]).exit_code == 0

    # Bob fresh home — SESSION_START should not leak Alice anchors
    bob = tmp_path / "bob"
    bob.mkdir()
    monkeypatch.setenv("KEDGER_HOME", str(bob))
    assert runner.invoke(main, ["keys", "init", "--name", "bob"]).exit_code == 0
    res = runner.invoke(
        main,
        ["hook", "--source", "cursor"],
        input=json.dumps({"type": "SessionStart"}),
    )
    assert res.exit_code == 0, res.output
    data = json.loads(res.output)
    ctx = data.get("additionalContext") or ""
    assert "Use refresh tokens" not in ctx


def test_before_submit_prompt_hydrate_inject(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "constraint", "Idempotency-Key on charge create"]
        ).exit_code
        == 0
    )
    payload = {
        "type": "beforeSubmitPrompt",
        "session_id": "s1",
        "prompt": "patch charges.py",
    }
    res = runner.invoke(
        main,
        ["hook", "--source", "cursor"],
        input=json.dumps(payload),
    )
    assert res.exit_code == 0, res.output
    data = json.loads(res.output)
    ctx = data.get("additional_context") or data.get("additionalContext")
    assert ctx
    assert "Idempotency" in ctx
    effects = {s["effect"] for s in data["side_effects"]}
    assert "hydrate_inject" in effects
    assert "ingest" in effects


def test_user_prompt_submit_claude_hydrate(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert (
        runner.invoke(main, ["remember", "reject", "Do not flip billing_v2"]).exit_code == 0
    )
    payload = {
        "hook_event_name": "UserPromptSubmit",
        "session_id": "s2",
        "prompt": "what is our billing constraint?",
    }
    res = runner.invoke(
        main,
        ["hook", "--source", "claude_code"],
        input=json.dumps(payload),
    )
    assert res.exit_code == 0, res.output
    data = json.loads(res.output)
    hso = data.get("hookSpecificOutput") or {}
    ctx = hso.get("additionalContext") or data.get("additionalContext")
    assert ctx
    assert "billing" in ctx.lower()
    assert hso.get("hookEventName") == "UserPromptSubmit"


def test_hook_shell_fail_soft_when_kedger_missing() -> None:
    hook = Path(__file__).resolve().parents[1] / "hooks" / "cursor" / "kedger-hook.sh"
    kedger_bin = shutil.which("kedger")
    assert kedger_bin, "kedger must be installed for this test"
    kedger_dir = str(Path(kedger_bin).parent)
    path_parts = [
        p for p in os.environ.get("PATH", "").split(os.pathsep) if p and p != kedger_dir
    ]
    env = {**os.environ, "PATH": os.pathsep.join(path_parts)}
    proc = subprocess.run(
        [str(hook), "beforeSubmitPrompt"],
        input='{"prompt":"hello"}',
        text=True,
        capture_output=True,
        env=env,
        check=False,
    )
    assert proc.returncode == 0
    data = json.loads(proc.stdout)
    assert data["ok"] is True
    assert data.get("skipped") is True
