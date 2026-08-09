"""Least-friction peer card → send → open path."""

from __future__ import annotations

import json
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.keys import init_principal, load_principal
from kedger.store import Store, repo_fingerprint


def test_peer_card_add_send_open(
    kedger_env: Path, runner: CliRunner, tmp_path: Path, monkeypatch
) -> None:
    assert runner.invoke(main, ["init", "--name", "alice", "--hooks", "none"]).exit_code == 0
    alice_home = kedger_env
    work = Path.cwd()

    # Alice remembers policy
    assert (
        runner.invoke(
            main,
            ["remember", "reject", "Do not flip billing_v2", "--reason", "finance"],
        ).exit_code
        == 0
    )

    bob_home = tmp_path / "bob-home"
    bob_home.mkdir()
    monkeypatch.setenv("KEDGER_HOME", str(bob_home))
    monkeypatch.chdir(work)
    bob = init_principal(name="bob")
    card = tmp_path / "bob.kedger.json"
    card_res = runner.invoke(main, ["peer", "card", "--out", str(card)])
    assert card_res.exit_code == 0, card_res.output
    assert card.is_file()
    body = json.loads(card.read_text(encoding="utf-8"))
    assert body["principal_id"] == bob.principal_id
    assert "private" not in json.dumps(body).lower()

    # Alice grants+sends
    monkeypatch.setenv("KEDGER_HOME", str(alice_home))
    xfer = tmp_path / "xfer"
    send = runner.invoke(
        main,
        ["peer", "send", "--to", str(card), "--out-dir", str(xfer), "--no-promote"],
    )
    assert send.exit_code == 0, send.output
    packs = list(xfer.glob("*.kxp"))
    assert packs, send.output

    # Bob opens
    monkeypatch.setenv("KEDGER_HOME", str(bob_home))
    opened = runner.invoke(main, ["peer", "open", str(packs[0])])
    assert opened.exit_code == 0, opened.output
    assert "imported:" in opened.output or "anchors:" in opened.output

    live = runner.invoke(main, ["hydrate", "--live"])
    assert live.exit_code == 0, live.output
    assert "billing" in live.output.lower()


def test_grant_infers_to_from_card(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "a"]).exit_code == 0
    # Fake peer card
    card = tmp_path / "p.kedger.json"
    # Need real key material shape — mint second principal in isolated home then restore
    from nacl.public import PrivateKey
    from nacl.signing import SigningKey
    import base64

    sk = SigningKey.generate()
    x = PrivateKey.generate()
    pid = "pr_testpeer000000000000000001"
    card.write_text(
        json.dumps(
            {
                "principal_id": pid,
                "name": "peer",
                "public_key_b64": base64.b64encode(bytes(sk.verify_key)).decode(),
                "x25519_public_b64": base64.b64encode(bytes(x.public_key)).decode(),
            }
        ),
        encoding="utf-8",
    )
    res = runner.invoke(main, ["grant", "--recipient-file", str(card)])
    assert res.exit_code == 0, res.output
    assert pid in res.output
