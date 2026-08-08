"""ConfAIde-style share probes — private secrets must not appear in shared facet."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main


def test_confaide_private_token_never_shared(
    kedger_env: Path, runner: CliRunner
) -> None:
    """Tier-ish probe: remember with secret reason → share blocked; shared list empty."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main,
        [
            "remember",
            "decision",
            "Use company SSO for admin",
            "--reason",
            "token sk-abcdefghijklmnopqrstuvwxyz0123456789 leaked in chat",
        ],
    )
    assert rem.exit_code == 0, rem.output
    assert "sk-abcdefghijklmnopqrstuvwxyz0123456789" not in rem.output
    anc = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(":", 1)[
        1
    ].strip()
    sh = runner.invoke(main, ["share", anc])
    # Either blocked by redaction canary, or if statement alone is clean and reason
    # was redacted — still must not list raw secret in shared output.
    listed = runner.invoke(main, ["anchors", "--shared"])
    assert "sk-abcdefghijklmnopqrstuvwxyz0123456789" not in listed.output
    assert "sk-abcdefghijklmnopqrstuvwxyz0123456789" not in sh.output


def test_confaide_public_decision_can_share(
    kedger_env: Path, runner: CliRunner
) -> None:
    """Public eng decision without secrets remains shareable when explicit."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main,
        ["remember", "decision", "Prefer JWT access tokens over cookie sessions"],
    )
    anc = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(":", 1)[
        1
    ].strip()
    sh = runner.invoke(main, ["share", anc])
    assert sh.exit_code == 0, sh.output
    listed = runner.invoke(main, ["anchors", "--shared"])
    assert anc in listed.output
    assert "JWT" in listed.output
