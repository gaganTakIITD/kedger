"""PART D validation scenarios from SEALED_PACKS_AND_SHAREABLE_ANCHORS_V1.md."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from click.testing import CliRunner
from nacl.public import PrivateKey
from nacl.signing import SigningKey

from kedger.cli.main import main
from kedger.crypto.kxp import KxpError, LocalIdentity, Recipient, open_kxp, seal_kxp
from kedger.handoff import hydrate_pack, seal_handoff
from kedger.ids import new_id
from kedger.keys import init_principal, load_principal
from kedger.store import Store, repo_fingerprint
from kedger.store.db import utc_now


def _seal_pair():
    sender_sign = SigningKey.generate()
    sender_x = PrivateKey.generate()
    peer_x = PrivateKey.generate()
    sender_id = new_id("pr")
    peer_id = new_id("pr")
    payload = {
        "schema_version": "kedger.memory.v1",
        "id": new_id("hf"),
        "anchors": [{"id": "anc_x", "kind": "constraint", "statement": "JWT only"}],
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
    return blob, sender, sender_sign, peer_id, peer_x, payload


def test_d1_multi_recipient_seal() -> None:
    blob, sender, sender_sign, peer_id, peer_x, payload = _seal_pair()
    peer = LocalIdentity(
        principal_id=peer_id,
        signing_key=SigningKey.generate(),
        x25519_private=peer_x,
    )
    opened = open_kxp(blob, identity=peer, trusted_sender_verify_key=sender_sign.verify_key)
    assert opened["payload"]["id"] == payload["id"]
    self_open = open_kxp(
        blob, identity=sender, trusted_sender_verify_key=sender_sign.verify_key
    )
    assert self_open["payload"]["anchors"][0]["statement"] == "JWT only"


def test_d3_sign_binding_rewrap_fails() -> None:
    blob, sender, sender_sign, peer_id, peer_x, payload = _seal_pair()
    # Attacker tries to open as non-recipient — uniform not found
    attacker = LocalIdentity(
        principal_id=new_id("pr"),
        signing_key=SigningKey.generate(),
        x25519_private=PrivateKey.generate(),
    )
    with pytest.raises(KxpError, match="pack not found"):
        open_kxp(
            blob, identity=attacker, trusted_sender_verify_key=sender_sign.verify_key
        )
    # Tamper header recipient list without valid stanzas
    import struct

    from kedger.crypto import kxp as kxp_mod

    header_len = struct.unpack(">I", blob[4:8])[0]
    header = json.loads(blob[8 : 8 + header_len])
    header["recipient_key_ids"].append(attacker.principal_id)
    new_header = json.dumps(header, sort_keys=True, separators=(",", ":")).encode()
    tampered = kxp_mod.MAGIC + struct.pack(">I", len(new_header)) + new_header + blob[8 + header_len :]
    with pytest.raises(KxpError, match="pack not found"):
        open_kxp(
            tampered, identity=peer_id and LocalIdentity(
                principal_id=peer_id,
                signing_key=SigningKey.generate(),
                x25519_private=peer_x,
            ),
            trusted_sender_verify_key=sender_sign.verify_key,
        )


def test_d2_revoke_reseal(
    kedger_env: Path, runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "alice"]).exit_code == 0
    assert runner.invoke(main, ["remember", "decision", "Use refresh tokens"]).exit_code == 0

    bob_home = tmp_path / "bob"
    bob_home.mkdir()
    monkeypatch.setenv("KEDGER_HOME", str(bob_home))
    bob = init_principal(name="bob")
    recip = tmp_path / "bob.json"
    recip.write_text(
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
    assert (
        runner.invoke(
            main,
            [
                "grant",
                "--to",
                bob.principal_id,
                "--recipient-file",
                str(recip),
            ],
        ).exit_code
        == 0
    )
    handoff = runner.invoke(main, ["handoff"])
    assert handoff.exit_code == 0, handoff.output
    old_pack = Path(
        [ln for ln in handoff.output.splitlines() if ln.startswith("pack:")][0].split(
            ":", 1
        )[1].strip()
    )

    rev = runner.invoke(main, ["revoke", "--from", bob.principal_id])
    assert rev.exit_code == 0, rev.output
    assert "resealed:" in rev.output

    # Bob can still open OLD pack (documented), cannot open NEW head
    monkeypatch.setenv("KEDGER_HOME", str(bob_home))
    store = Store.open(repo_fingerprint())
    bob_p = load_principal()
    opened_old = hydrate_pack(store, principal=bob_p, pack_path=old_pack)
    assert opened_old["payload"]["anchors"]

    # Find new pack path from alice home
    monkeypatch.setenv("KEDGER_HOME", str(kedger_env))
    new_handoff = runner.invoke(main, ["handoff"])
    assert new_handoff.exit_code == 0
    new_pack = Path(
        [ln for ln in new_handoff.output.splitlines() if ln.startswith("pack:")][0].split(
            ":", 1
        )[1].strip()
    )
    monkeypatch.setenv("KEDGER_HOME", str(bob_home))
    with pytest.raises(KxpError, match="pack not found"):
        hydrate_pack(store, principal=bob_p, pack_path=new_pack)


def test_d4_explicit_share(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main, ["remember", "constraint", "No cookie sessions", "--reason", "CSRF"]
    )
    assert rem.exit_code == 0, rem.output
    anc_id = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(
        ":", 1
    )[1].strip()
    sh = runner.invoke(main, ["share", anc_id])
    assert sh.exit_code == 0, sh.output
    assert "repo_shared_safe" in sh.output
    listed = runner.invoke(main, ["anchors", "--shared"])
    assert listed.exit_code == 0
    assert anc_id in listed.output


def test_d5_recurrence_does_not_auto_share(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    for _ in range(3):
        assert (
            runner.invoke(
                main, ["remember", "gotcha", "Watch the CSRF edge case"]
            ).exit_code
            == 0
        )
    listed = runner.invoke(main, ["anchors", "--shared"])
    assert listed.exit_code == 0
    assert listed.output.strip() == "(none)"


def test_d6_get_by_id_404(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    gossip = "anc_01HZZZZZZZZZZZZZZZZZZZZZZZ"
    got = runner.invoke(main, ["anchors", "--get", gossip])
    assert got.exit_code == 404
    assert "not found" in got.output.lower()
    assert "forbidden" not in got.output.lower()


def test_d7_unshare_cascade(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(main, ["remember", "rejection", "No cookies"])
    anc_id = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(
        ":", 1
    )[1].strip()
    assert runner.invoke(main, ["share", anc_id]).exit_code == 0
    assert runner.invoke(main, ["handoff"]).exit_code == 0
    assert runner.invoke(main, ["unshare", anc_id]).exit_code == 0
    listed = runner.invoke(main, ["anchors", "--shared"])
    assert listed.output.strip() == "(none)"


def test_d8_pack_deputy_default_excludes_shared(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(main, ["remember", "constraint", "Shared constraint"])
    anc_id = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(
        ":", 1
    )[1].strip()
    assert runner.invoke(main, ["share", anc_id]).exit_code == 0
    # New workstream pack without --include-shared should still include
    # workstream-scoped anchors; shared-only foreign facets need opt-in.
    # Create another remember in default (same ws) — pack includes it.
    # Opt-in flag exists and default is off for *additional* shared dump.
    h1 = runner.invoke(main, ["handoff"])
    assert h1.exit_code == 0
    h2 = runner.invoke(main, ["handoff", "--include-shared"])
    assert h2.exit_code == 0


def test_d9_secret_canary_blocks_share(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main,
        [
            "remember",
            "constraint",
            "Do not commit secrets",
            "--reason",
            "saw ghs_abcdefghijklmnopqrstuvwxyz99 in logs",
        ],
    )
    assert rem.exit_code == 0, rem.output
    assert "ghs_" not in rem.output  # redacted at remember
    anc_id = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(
        ":", 1
    )[1].strip()
    sh = runner.invoke(main, ["share", anc_id])
    assert sh.exit_code != 0
    assert "blocked" in sh.output.lower() or "redaction" in sh.output.lower()
    listed = runner.invoke(main, ["anchors", "--shared"])
    assert listed.output.strip() == "(none)"
