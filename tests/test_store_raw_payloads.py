from __future__ import annotations

import json
from pathlib import Path

import pytest
from click.testing import CliRunner

from kedger.cli.main import main
from kedger.store import Store, encryption_state, store_path
from kedger.store.encryption import RAW_PAYLOADS_XCHACHA, read_store_meta
from kedger.store.fingerprint import repo_fingerprint
from kedger.store.raw_payloads import (
    RAW_MAGIC,
    parse_payload_ref,
    raw_dir,
    read_payload,
    should_spill_payload,
    write_payload,
)


def _large_hook_payload(text: str) -> dict:
    return {
        "type": "user_prompt",
        "session_id": "sess_test",
        "summary": text[:200],
        "text": text,
        "message": text,
    }


def test_plaintext_raw_payload_round_trip(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    fp = repo_fingerprint()
    store = Store.open(fp)
    ws = store.ensure_workstream(slug="default", principal_id="pr_test")
    blob = "x" * 700
    record = store.ingest_observation(
        _large_hook_payload(blob),
        principal_id="pr_test",
    )
    record["workstream_id"] = ws["id"]
    ref = record.get("payload_ref")
    assert ref and ref.startswith("raw://")
    path = raw_dir(fp) / f"{parse_payload_ref(ref)}.json"
    assert path.exists()
    assert RAW_MAGIC not in path.read_bytes()[:4]

    loaded = store.observation_payload(record)
    assert loaded.get("text") == blob

    status = runner.invoke(main, ["store", "status"])
    assert status.exit_code == 0, status.output
    assert "plaintext JSON in raw/" in status.output


def test_encrypted_raw_payload_round_trip(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    enc = runner.invoke(main, ["init", "--hooks", "none", "--encrypt-store"])
    assert enc.exit_code == 0, enc.output

    fp = repo_fingerprint()
    store = Store.open(fp)
    ws = store.ensure_workstream(slug="default", principal_id="pr_test")
    blob = "secret observation body " * 40
    record = store.ingest_observation(
        _large_hook_payload(blob),
        principal_id="pr_test",
    )
    record["workstream_id"] = ws["id"]
    ref = record["payload_ref"]
    obs_id = parse_payload_ref(ref)
    assert obs_id
    enc_path = raw_dir(fp) / f"{obs_id}.enc"
    assert enc_path.exists()
    assert enc_path.read_bytes()[:4] == RAW_MAGIC

    loaded = store.observation_payload(record)
    assert loaded.get("text") == blob

    meta = read_store_meta(fp)
    assert meta and meta.get("raw_payloads") == RAW_PAYLOADS_XCHACHA

    doc = runner.invoke(main, ["doctor"])
    assert doc.exit_code == 0, doc.output
    assert "raw_payloads:" in doc.output
    assert "XChaCha20-Poly1305" in doc.output
    assert "kxp_at_rest:" in doc.output


def test_small_payload_stays_inline(kedger_env: Path) -> None:
    fp = repo_fingerprint()
    store = Store.open(fp)
    tiny = {"type": "note", "summary": "ok", "tool_name": "grep"}
    assert not should_spill_payload(tiny)
    record = store.ingest_observation(tiny, principal_id="pr_test")
    assert not record.get("payload_ref")
    assert record.get("payload", {}).get("tool_name") == "grep"


def test_migrate_plaintext_raw_on_store_encrypt(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    fp = repo_fingerprint()
    store = Store.open(fp)
    blob = "migrate me " * 80
    record = store.ingest_observation(
        _large_hook_payload(blob),
        principal_id="pr_test",
    )
    ref = record["payload_ref"]
    obs_id = parse_payload_ref(ref)
    plain_path = raw_dir(fp) / f"{obs_id}.json"
    assert plain_path.exists()

    enc = runner.invoke(main, ["store", "encrypt"])
    assert enc.exit_code == 0, enc.output
    assert not plain_path.exists()
    assert (raw_dir(fp) / f"{obs_id}.enc").exists()

    store2 = Store.open(fp)
    loaded = store2.observation_payload(record)
    assert loaded.get("text") == blob

    meta = read_store_meta(fp)
    assert meta and meta.get("raw_payloads") == RAW_PAYLOADS_XCHACHA


def test_handoff_still_opens_after_raw_encryption(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert runner.invoke(main, ["init", "--hooks", "none", "--encrypt-store"]).exit_code == 0
    assert (
        runner.invoke(
            main,
            ["remember", "decision", "Use encrypted raw payloads"],
        ).exit_code
        == 0
    )
    pack_path = tmp_path / "local.kxp"
    seal = runner.invoke(main, ["handoff", "--out", str(pack_path)])
    assert seal.exit_code == 0, seal.output
    assert pack_path.exists()
    assert pack_path.read_bytes()[:4] == b"KXP1"
    open_res = runner.invoke(main, ["peer", "open", str(pack_path)])
    assert open_res.exit_code == 0, open_res.output
    assert "opened:" in open_res.output


def test_prune_deletes_raw_file(kedger_env: Path) -> None:
    fp = repo_fingerprint()
    store = Store.open(fp)
    blob = "prune target " * 60
    record = store.ingest_observation(
        _large_hook_payload(blob),
        principal_id="pr_test",
    )
    ref = record["payload_ref"]
    obs_id = parse_payload_ref(ref)
    assert obs_id
    plain = raw_dir(fp) / f"{obs_id}.json"
    assert plain.exists()
    store.prune_observation_payloads([record["id"]])
    assert not plain.exists()
