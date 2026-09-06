from __future__ import annotations

import base64
from pathlib import Path
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from kedger.cli.main import main
from kedger.store import (
    Store,
    StoreEncryptionError,
    StoreKeySource,
    encryption_state,
    resolve_store_key,
    store_path,
)
from kedger.store.encryption import (
    STORE_KEY_ENV,
    STORE_KEYRING_SERVICE,
    STORE_KEYRING_USERNAME,
    load_store_key,
    migrate_plaintext_to_sqlcipher,
    write_store_meta,
)
from kedger.store.fingerprint import repo_fingerprint


def _init_plain_store(kedger_env: Path, runner: CliRunner) -> str:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main,
        ["remember", "decision", "Keyring precedence test"],
    )
    assert rem.exit_code == 0, rem.output
    return repo_fingerprint()


@pytest.fixture()
def fake_keyring(monkeypatch: pytest.MonkeyPatch) -> dict[str, str]:
    vault: dict[str, str] = {}

    def usable() -> bool:
        return True

    def backend_name() -> str:
        return "FakeKeyring"

    def load_key() -> bytes | None:
        raw = vault.get(f"{STORE_KEYRING_SERVICE}/{STORE_KEYRING_USERNAME}")
        if raw is None:
            return None
        return base64.b64decode(raw)

    def save_key(key: bytes) -> None:
        vault[f"{STORE_KEYRING_SERVICE}/{STORE_KEYRING_USERNAME}"] = base64.b64encode(
            key
        ).decode("ascii")

    monkeypatch.setattr("kedger.store.encryption._keyring_usable", usable)
    monkeypatch.setattr("kedger.store.encryption._keyring_backend_name", backend_name)
    monkeypatch.setattr("kedger.store.encryption._load_keyring_store_key", load_key)
    monkeypatch.setattr(
        "kedger.store.encryption._save_keyring_store_key", save_key
    )
    return vault


def test_resolve_precedence_env_over_keyring_and_file(
    kedger_env: Path, fake_keyring: dict[str, str], monkeypatch: pytest.MonkeyPatch
) -> None:
    file_key = b"\x01" * 32
    keyring_key = b"\x02" * 32
    env_key = b"\x03" * 32

    path = kedger_env / "keys" / "store.key"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(file_key)
    fake_keyring[f"{STORE_KEYRING_SERVICE}/{STORE_KEYRING_USERNAME}"] = base64.b64encode(
        keyring_key
    ).decode("ascii")
    monkeypatch.setenv(STORE_KEY_ENV, base64.b64encode(env_key).decode("ascii"))

    res = resolve_store_key()
    assert res.source == StoreKeySource.ENV
    assert res.key == env_key


def test_resolve_precedence_keyring_over_file(
    kedger_env: Path, fake_keyring: dict[str, str], monkeypatch: pytest.MonkeyPatch
) -> None:
    file_key = b"\x01" * 32
    keyring_key = b"\x02" * 32

    path = kedger_env / "keys" / "store.key"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(file_key)
    fake_keyring[f"{STORE_KEYRING_SERVICE}/{STORE_KEYRING_USERNAME}"] = base64.b64encode(
        keyring_key
    ).decode("ascii")
    monkeypatch.delenv(STORE_KEY_ENV, raising=False)

    res = resolve_store_key()
    assert res.source == StoreKeySource.KEYRING
    assert res.key == keyring_key


def test_resolve_file_fallback_when_no_keyring(
    kedger_env: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    file_key = b"\x04" * 32
    path = kedger_env / "keys" / "store.key"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(file_key)
    monkeypatch.delenv(STORE_KEY_ENV, raising=False)
    monkeypatch.setattr("kedger.store.encryption._keyring_usable", lambda: False)

    res = resolve_store_key()
    assert res.source == StoreKeySource.FILE
    assert res.key == file_key


def test_encrypt_stores_key_in_keyring_by_default(
    kedger_env: Path, runner: CliRunner, fake_keyring: dict[str, str]
) -> None:
    _init_plain_store(kedger_env, runner)
    enc = runner.invoke(main, ["store", "encrypt"])
    assert enc.exit_code == 0, enc.output
    assert "key: keyring" in enc.output
    assert f"{STORE_KEYRING_SERVICE}/{STORE_KEYRING_USERNAME}" in fake_keyring
    assert not (kedger_env / "keys" / "store.key").exists()


def test_encrypt_key_file_flag_writes_file_not_keyring(
    kedger_env: Path, runner: CliRunner, fake_keyring: dict[str, str]
) -> None:
    _init_plain_store(kedger_env, runner)
    enc = runner.invoke(main, ["store", "encrypt", "--key-file"])
    assert enc.exit_code == 0, enc.output
    assert "key: file" in enc.output
    assert (kedger_env / "keys" / "store.key").exists()
    assert f"{STORE_KEYRING_SERVICE}/{STORE_KEYRING_USERNAME}" not in fake_keyring


def test_open_encrypted_store_from_keyring(
    kedger_env: Path, runner: CliRunner, fake_keyring: dict[str, str]
) -> None:
    fp = _init_plain_store(kedger_env, runner)
    path = store_path(fp)
    key = load_store_key(create=True, prefer_keyring=True)
    migrate_plaintext_to_sqlcipher(path, key=key)
    write_store_meta(fp, {"encryption": "sqlcipher", "migrated_at": "test"})

    (kedger_env / "keys" / "store.key").unlink(missing_ok=True)
    fake_keyring[f"{STORE_KEYRING_SERVICE}/{STORE_KEYRING_USERNAME}"] = base64.b64encode(
        key
    ).decode("ascii")

    store = Store.open(fp)
    anchors = store.list_anchors(active_only=True)
    assert any("Keyring precedence test" in a["statement"] for a in anchors)


def test_doctor_reports_keyring_source(
    kedger_env: Path, runner: CliRunner, fake_keyring: dict[str, str]
) -> None:
    _init_plain_store(kedger_env, runner)
    assert runner.invoke(main, ["store", "encrypt"]).exit_code == 0

    doc = runner.invoke(main, ["doctor"])
    assert doc.exit_code == 0, doc.output
    assert "store_key: keyring" in doc.output


def test_fail_closed_no_key_anywhere(
    kedger_env: Path, runner: CliRunner, monkeypatch: pytest.MonkeyPatch
) -> None:
    fp = _init_plain_store(kedger_env, runner)
    assert runner.invoke(main, ["store", "encrypt", "--key-file"]).exit_code == 0

    (kedger_env / "keys" / "store.key").unlink()
    monkeypatch.delenv(STORE_KEY_ENV, raising=False)
    monkeypatch.setattr("kedger.store.encryption._keyring_usable", lambda: False)

    with pytest.raises(StoreEncryptionError, match="store encryption key missing"):
        Store.open(fp)

    doc = runner.invoke(main, ["doctor"])
    assert doc.exit_code == 1
    assert "store encryption key missing" in doc.output
