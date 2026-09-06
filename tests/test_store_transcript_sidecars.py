from __future__ import annotations

import json
from pathlib import Path

import pytest
from click.testing import CliRunner

from kedger.cli.main import main
from kedger.handoff.transcript import (
    attach_transcript_for_pack,
    compress_transcript,
    decompress_transcript,
    resolve_transcript_archive,
    turns_from_observations,
)
from kedger.store import Store, repo_fingerprint
from kedger.store.encryption import RAW_PAYLOADS_XCHACHA, read_store_meta
from kedger.store.paths import project_dir
from kedger.store.transcript_sidecars import (
    TRANSCRIPT_ENC_SUFFIX,
    TRANSCRIPT_MAGIC,
    TRANSCRIPT_PLAIN_SUFFIX,
    migrate_plaintext_to_encrypted,
    read_sidecar,
    write_sidecar,
)


def _sample_archive() -> dict:
    turns = turns_from_observations(
        [
            {
                "id": "obs_1",
                "type": "user_prompt",
                "ts": "2026-01-01T00:00:00Z",
                "summary": "Use Postgres not Redis",
            }
        ]
    )
    return compress_transcript(turns)


def test_plaintext_transcript_sidecar_round_trip(tmp_path: Path) -> None:
    archive = _sample_archive()
    path = tmp_path / f"hf_test{TRANSCRIPT_PLAIN_SUFFIX}"
    write_sidecar(path, archive, store_key=None)
    assert TRANSCRIPT_MAGIC not in path.read_bytes()[:4]
    loaded = read_sidecar(path, store_key=None)
    assert decompress_transcript(loaded) == decompress_transcript(archive)


def test_encrypted_transcript_sidecar_round_trip(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert runner.invoke(main, ["init", "--hooks", "none", "--encrypt-store"]).exit_code == 0
    fp = repo_fingerprint()
    store = Store.open(fp)
    assert store._store_key is not None
    archive = _sample_archive()
    plain_path = project_dir(fp) / "packs" / "ws1" / f"hf_test{TRANSCRIPT_PLAIN_SUFFIX}"
    enc_path = write_sidecar(plain_path, archive, store_key=store._store_key)
    assert enc_path.name.endswith(TRANSCRIPT_ENC_SUFFIX)
    assert enc_path.read_bytes()[:4] == TRANSCRIPT_MAGIC
    loaded = read_sidecar(enc_path, store_key=store._store_key)
    assert decompress_transcript(loaded) == decompress_transcript(archive)


def test_resolve_transcript_archive_reads_encrypted_sidecar(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert runner.invoke(main, ["init", "--hooks", "none", "--encrypt-store"]).exit_code == 0
    fp = repo_fingerprint()
    store = Store.open(fp)
    archive = _sample_archive()
    packs_dir = project_dir(fp) / "packs" / "ws1"
    packs_dir.mkdir(parents=True)
    written = write_sidecar(
        packs_dir / f"hf_side{TRANSCRIPT_PLAIN_SUFFIX}",
        archive,
        store_key=store._store_key,
    )
    meta = {"sidecar": written.name, "inline": False, "turn_count": 1}
    resolved = resolve_transcript_archive(
        {"transcript_meta": meta},
        sidecar_root=packs_dir,
        store_key=store._store_key,
    )
    assert resolved is not None
    assert decompress_transcript(resolved) == decompress_transcript(archive)


def test_migrate_plaintext_transcript_on_store_encrypt(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert runner.invoke(main, ["init", "--hooks", "none"]).exit_code == 0
    fp = repo_fingerprint()
    archive = _sample_archive()
    packs_dir = project_dir(fp) / "packs" / "ws1"
    packs_dir.mkdir(parents=True)
    plain = packs_dir / f"hf_old{TRANSCRIPT_PLAIN_SUFFIX}"
    plain.write_text(json.dumps(archive), encoding="utf-8")

    enc = runner.invoke(main, ["store", "encrypt"])
    assert enc.exit_code == 0, enc.output
    assert not plain.exists()
    assert list(packs_dir.glob(f"*{TRANSCRIPT_ENC_SUFFIX}"))

    store = Store.open(fp)
    loaded = read_sidecar(
        packs_dir / f"hf_old{TRANSCRIPT_ENC_SUFFIX}",
        store_key=store._store_key,
    )
    assert decompress_transcript(loaded) == decompress_transcript(archive)

    meta = read_store_meta(fp)
    assert meta and meta.get("transcript_sidecars") == RAW_PAYLOADS_XCHACHA


def test_attach_transcript_sidecar_encrypted_when_store_key(
    tmp_path: Path,
) -> None:
    archive = _sample_archive()
    pack = {"id": "hf_budget", "budget": {"dropped": []}, "layers": {}}
    out = attach_transcript_for_pack(
        archive,
        pack=pack,
        max_bytes=256,
        sidecar_dir=tmp_path,
        handoff_id="hf_budget",
        store_key=b"\x01" * 32,
    )
    assert out["transcript"] is None
    sidecar_name = out["transcript_meta"]["sidecar"]
    assert sidecar_name.endswith(TRANSCRIPT_ENC_SUFFIX)
    path = tmp_path / sidecar_name
    assert path.exists()
    loaded = read_sidecar(path, store_key=b"\x01" * 32)
    assert decompress_transcript(loaded) == decompress_transcript(archive)


def test_default_plaintext_sidecar_stays_green(tmp_path: Path) -> None:
    archive = _sample_archive()
    pack = {"id": "hf_plain", "budget": {"dropped": []}, "layers": {}}
    out = attach_transcript_for_pack(
        archive,
        pack=pack,
        max_bytes=256,
        sidecar_dir=tmp_path,
        handoff_id="hf_plain",
        store_key=None,
    )
    sidecar_name = out["transcript_meta"]["sidecar"]
    assert sidecar_name.endswith(TRANSCRIPT_PLAIN_SUFFIX)
    resolved = resolve_transcript_archive(
        out,
        sidecar_root=tmp_path,
        store_key=None,
    )
    assert resolved is not None
