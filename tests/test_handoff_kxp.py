"""Phase B: seal/open roundtrip + unauthorized hydrate → 404."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from click.testing import CliRunner
from nacl.public import PrivateKey
from nacl.signing import SigningKey

from kedger.cli.main import main
from kedger.crypto.kxp import KxpError, LocalIdentity, Recipient, open_kxp, seal_kxp
from kedger.handoff import hydrate_pack
from kedger.ids import new_id
from kedger.keys import init_principal, load_principal
from kedger.store import Store, repo_fingerprint
from kedger.store.db import utc_now


def test_seal_open_roundtrip_unit() -> None:
    sender_sign = SigningKey.generate()
    sender_x = PrivateKey.generate()
    peer_x = PrivateKey.generate()
    sender_id = new_id("pr")
    peer_id = new_id("pr")

    payload = {
        "schema_version": "kedger.memory.v1",
        "id": new_id("hf"),
        "anchors": [{"id": "anc_test", "kind": "rejection", "statement": "no cookies"}],
        "working": {"goal": "auth"},
        "workstream_id": new_id("ws"),
        "created_at": utc_now(),
    }
    context = {
        "handoff_id": payload["id"],
        "workstream_id": payload["workstream_id"],
        "repo_fingerprint": "rf_test",
        "created_at": payload["created_at"],
    }
    sender = LocalIdentity(
        principal_id=sender_id,
        signing_key=sender_sign,
        x25519_private=sender_x,
        verify_key=sender_sign.verify_key,
    )
    recipients = [
        Recipient(key_id=sender_id, x25519_public=bytes(sender_x.public_key)),
        Recipient(key_id=peer_id, x25519_public=bytes(peer_x.public_key)),
    ]
    blob = seal_kxp(
        payload=payload, context=context, sender=sender, recipients=recipients, epoch=1
    )
    assert blob.startswith(b"KXP1")

    peer_identity = LocalIdentity(
        principal_id=peer_id,
        signing_key=SigningKey.generate(),
        x25519_private=peer_x,
    )
    opened = open_kxp(
        blob,
        identity=peer_identity,
        trusted_sender_verify_key=sender_sign.verify_key,
    )
    assert opened["payload"]["id"] == payload["id"]
    assert opened["payload"]["anchors"][0]["statement"] == "no cookies"

    stranger = LocalIdentity(
        principal_id=new_id("pr"),
        signing_key=SigningKey.generate(),
        x25519_private=PrivateKey.generate(),
    )
    with pytest.raises(KxpError, match="pack not found"):
        open_kxp(
            blob,
            identity=stranger,
            trusted_sender_verify_key=sender_sign.verify_key,
        )


def test_handoff_hydrate_cli_roundtrip(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "alice"]).exit_code == 0
    rem = runner.invoke(
        main,
        ["remember", "reject", "Do not use cookie sessions", "--reason", "CSRF"],
    )
    assert rem.exit_code == 0, rem.output

    handoff = runner.invoke(main, ["handoff", "--workstream", "default"])
    assert handoff.exit_code == 0, handoff.output
    pack_line = [ln for ln in handoff.output.splitlines() if ln.startswith("pack:")][0]
    pack_path = Path(pack_line.split(":", 1)[1].strip())
    assert pack_path.exists()
    assert pack_path.suffix == ".kxp"

    hyd = runner.invoke(main, ["hydrate", "--pack", str(pack_path)])
    assert hyd.exit_code == 0, hyd.output
    assert "Do not use cookie sessions" in hyd.output
    assert "rejection" in hyd.output


def test_unauthorized_hydrate_is_404(
    kedger_env: Path, runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "alice"]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "constraint", "JWT only", "--reason", "policy"]
        ).exit_code
        == 0
    )
    handoff = runner.invoke(main, ["handoff"])
    assert handoff.exit_code == 0, handoff.output
    pack_line = [ln for ln in handoff.output.splitlines() if ln.startswith("pack:")][0]
    pack_path = Path(pack_line.split(":", 1)[1].strip())

    bob_home = tmp_path / "bob-home"
    bob_home.mkdir()
    monkeypatch.setenv("KEDGER_HOME", str(bob_home))
    assert runner.invoke(main, ["keys", "init", "--name", "bob"]).exit_code == 0
    denied = runner.invoke(main, ["hydrate", "--pack", str(pack_path)])
    assert denied.exit_code == 404
    assert "not found" in denied.output.lower()
    assert "forbidden" not in denied.output.lower()
    assert "unauthorized" not in denied.output.lower()


def test_grant_includes_peer_on_reseal(
    kedger_env: Path,
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "alice"]).exit_code == 0
    assert (
        runner.invoke(main, ["remember", "decision", "Use refresh tokens"]).exit_code
        == 0
    )

    bob_home = tmp_path / "bob"
    bob_home.mkdir()
    monkeypatch.setenv("KEDGER_HOME", str(bob_home))
    bob = init_principal(name="bob")
    recip_path = tmp_path / "bob-recip.json"
    recip_path.write_text(
        json.dumps(
            {
                "principal_id": bob.principal_id,
                "name": "bob",
                "public_key_b64": bob.public_key_b64,
                "x25519_public_b64": bob.x25519_public_b64,
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setenv("KEDGER_HOME", str(kedger_env))
    grant = runner.invoke(
        main,
        [
            "grant",
            "--workstream",
            "default",
            "--to",
            bob.principal_id,
            "--recipient-file",
            str(recip_path),
        ],
    )
    assert grant.exit_code == 0, grant.output

    handoff = runner.invoke(main, ["handoff"])
    assert handoff.exit_code == 0, handoff.output
    pack_line = [ln for ln in handoff.output.splitlines() if ln.startswith("pack:")][0]
    pack_path = Path(pack_line.split(":", 1)[1].strip())

    monkeypatch.setenv("KEDGER_HOME", str(bob_home))
    store = Store.open(repo_fingerprint())
    bob_loaded = load_principal()
    opened = hydrate_pack(store, principal=bob_loaded, pack_path=pack_path)
    assert any(
        a["statement"] == "Use refresh tokens" for a in opened["payload"]["anchors"]
    )
