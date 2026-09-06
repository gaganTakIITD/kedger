"""Same-person device transfer via kedger sync export/import."""

from __future__ import annotations

import json
import shutil
import tarfile
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.store import Store, repo_fingerprint, store_path
from kedger.store.encryption import sqlite_header_is_plaintext
from kedger.sync.bundle import BUNDLE_SUFFIX, SYNC_SCHEMA, export_bundle


def _seed_store(runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "sync"]).exit_code == 0
    assert runner.invoke(main, ["init", "--hooks", "none"]).exit_code == 0
    rem = runner.invoke(
        main,
        ["remember", "constraint", "Must sync idempotency keys across devices"],
    )
    assert rem.exit_code == 0, rem.output


def test_sync_export_import_round_trip(
    kedger_env: Path, runner: CliRunner, tmp_path: Path, monkeypatch
) -> None:
    _seed_store(runner)
    fp = repo_fingerprint()
    bundle = tmp_path / f"{fp}{BUNDLE_SUFFIX}"

    exp = runner.invoke(main, ["sync", "export", "--out", str(bundle)])
    assert exp.exit_code == 0, exp.output
    assert bundle.is_file()
    assert "keys:         NOT included" in exp.output
    assert "peer share:" in exp.output

    with tarfile.open(bundle, "r:gz") as tar:
        manifest = json.loads(tar.extractfile("manifest.json").read().decode())
    assert manifest["schema_version"] == SYNC_SCHEMA
    assert manifest["repo_fingerprint"] == fp
    assert "store.sqlite" in manifest["files"]

    # Simulate new device: wipe project store, keep keys
    shutil.rmtree(kedger_env / "projects" / fp)
    assert not store_path(fp).exists()

    imp = runner.invoke(main, ["sync", "import", str(bundle)])
    assert imp.exit_code == 0, imp.output
    assert store_path(fp).exists()

    store = Store.open(fp)
    anchors = store.list_anchors(active_only=True)
    assert any("idempotency" in a["statement"].lower() for a in anchors)

    live = runner.invoke(main, ["hydrate", "--live"])
    assert live.exit_code == 0, live.output
    assert "idempotency" in live.output.lower()


def test_sync_import_fingerprint_mismatch(
    kedger_env: Path, runner: CliRunner, tmp_path: Path, monkeypatch
) -> None:
    _seed_store(runner)
    fp = repo_fingerprint()
    bundle = tmp_path / "other.kxs"
    export_bundle(out_path=bundle, repo_fp=fp)

    other_work = tmp_path / "other-repo"
    other_work.mkdir()
    monkeypatch.chdir(other_work)
    other_fp = repo_fingerprint()
    assert other_fp != fp

    bad = runner.invoke(main, ["sync", "import", str(bundle)])
    assert bad.exit_code != 0
    assert "fingerprint mismatch" in bad.output.lower()

    ok = runner.invoke(main, ["sync", "import", str(bundle), "--force"])
    assert ok.exit_code == 0, ok.output
    assert store_path(other_fp).exists()


def test_sync_export_encrypted_store(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    _seed_store(runner)
    enc = runner.invoke(main, ["store", "encrypt"])
    assert enc.exit_code == 0, enc.output

    fp = repo_fingerprint()
    bundle = tmp_path / f"{fp}{BUNDLE_SUFFIX}"
    exp = runner.invoke(main, ["sync", "export", "--out", str(bundle)])
    assert exp.exit_code == 0, exp.output
    assert "on (SQLCipher in bundle)" in exp.output
    assert "store key:" in exp.output

    with tarfile.open(bundle, "r:gz") as tar:
        manifest = json.loads(tar.extractfile("manifest.json").read().decode())
    assert manifest["encryption"]["store"] == "sqlcipher"
    assert not sqlite_header_is_plaintext(store_path(fp))


def test_sync_import_backs_up_existing(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    _seed_store(runner)
    fp = repo_fingerprint()
    bundle = tmp_path / f"{fp}{BUNDLE_SUFFIX}"
    assert runner.invoke(main, ["sync", "export", "--out", str(bundle)]).exit_code == 0

    runner.invoke(
        main,
        ["remember", "goal", "New anchor after first export"],
    )

    imp = runner.invoke(main, ["sync", "import", str(bundle)])
    assert imp.exit_code == 0, imp.output
    assert "backup:" in imp.output

    store = Store.open(fp)
    anchors = store.list_anchors(active_only=True)
    assert not any("New anchor after first export" in a["statement"] for a in anchors)
    assert any("idempotency" in a["statement"].lower() for a in anchors)
