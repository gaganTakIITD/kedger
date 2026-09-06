from __future__ import annotations

from pathlib import Path

import pytest
from click.testing import CliRunner

from kedger.cli.main import main
from kedger.store import Store, StoreEncryptionError, encryption_state, store_path
from kedger.store.encryption import (
    STORE_KEY_ENV,
    load_store_key,
    migrate_plaintext_to_sqlcipher,
    sqlite_header_is_plaintext,
    write_store_meta,
)
from kedger.store.fingerprint import repo_fingerprint


def _init_plain_store(kedger_env: Path, runner: CliRunner) -> str:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main,
        ["remember", "decision", "Encrypt the local store"],
    )
    assert rem.exit_code == 0, rem.output
    return repo_fingerprint()


def test_plaintext_store_default(kedger_env: Path, runner: CliRunner) -> None:
    fp = _init_plain_store(kedger_env, runner)
    path = store_path(fp)
    assert path.exists()
    assert sqlite_header_is_plaintext(path)
    state = encryption_state(fp, path)
    assert not state.enabled

    status = runner.invoke(main, ["store", "status"])
    assert status.exit_code == 0, status.output
    assert "encryption: off" in status.output


def test_encrypt_migrate_round_trip(kedger_env: Path, runner: CliRunner) -> None:
    fp = _init_plain_store(kedger_env, runner)
    path = store_path(fp)

    enc = runner.invoke(main, ["store", "encrypt"])
    assert enc.exit_code == 0, enc.output
    assert "encrypted:" in enc.output
    assert not sqlite_header_is_plaintext(path)
    assert (path.with_name(path.name + ".plaintext.bak")).exists()

    state = encryption_state(fp, path)
    assert state.enabled

    store = Store.open(fp)
    anchors = store.list_anchors(active_only=True)
    assert any("Encrypt the local store" in a["statement"] for a in anchors)

    doc = runner.invoke(main, ["doctor"])
    assert doc.exit_code == 0, doc.output
    assert "encryption=on (sqlcipher)" in doc.output


def test_init_encrypt_store_creates_encrypted_db(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    init = runner.invoke(main, ["init", "--hooks", "none", "--encrypt-store"])
    assert init.exit_code == 0, init.output
    assert "encryption:   SQLCipher" in init.output

    fp = repo_fingerprint()
    path = store_path(fp)
    assert path.exists()
    assert not sqlite_header_is_plaintext(path)
    assert encryption_state(fp, path).enabled

    rem = runner.invoke(main, ["remember", "goal", "Ship encrypted by default"])
    assert rem.exit_code == 0, rem.output
    store = Store.open(fp)
    assert store.list_anchors(active_only=True)


def test_fail_closed_missing_key(
    kedger_env: Path, runner: CliRunner, monkeypatch: pytest.MonkeyPatch
) -> None:
    fp = _init_plain_store(kedger_env, runner)
    path = store_path(fp)
    assert runner.invoke(main, ["store", "encrypt"]).exit_code == 0

    key_path = kedger_env / "keys" / "store.key"
    assert key_path.exists()
    key_path.unlink()
    monkeypatch.delenv(STORE_KEY_ENV, raising=False)

    with pytest.raises(StoreEncryptionError, match="store encryption key missing"):
        Store.open(fp)

    doc = runner.invoke(main, ["doctor"])
    assert doc.exit_code == 1
    assert "store encryption key missing" in doc.output


def test_store_encrypt_idempotent(kedger_env: Path, runner: CliRunner) -> None:
    _init_plain_store(kedger_env, runner)
    first = runner.invoke(main, ["store", "encrypt"])
    assert first.exit_code == 0, first.output
    second = runner.invoke(main, ["store", "encrypt"])
    assert second.exit_code == 0, second.output
    assert "already encrypted" in second.output


def test_env_store_key_override(
    kedger_env: Path, runner: CliRunner, monkeypatch: pytest.MonkeyPatch
) -> None:
    fp = _init_plain_store(kedger_env, runner)
    path = store_path(fp)
    key = load_store_key(create=True)
    migrate_plaintext_to_sqlcipher(path, key=key)
    write_store_meta(fp, {"encryption": "sqlcipher", "migrated_at": "test"})

    (kedger_env / "keys" / "store.key").unlink()
    monkeypatch.delenv(STORE_KEY_ENV, raising=False)

    with pytest.raises(StoreEncryptionError):
        Store.open(fp)

    import base64

    monkeypatch.setenv(STORE_KEY_ENV, base64.b64encode(key).decode("ascii"))
    store = Store.open(fp)
    assert store.list_anchors(active_only=True)
