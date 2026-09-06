"""Tarball export/import of ~/.kedger/projects/<fp>/ for multi-device transfer."""

from __future__ import annotations

import json
import shutil
import tarfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from kedger import SCHEMA_VERSION, __version__
from kedger.store.encryption import encryption_state, read_store_meta
from kedger.store.fingerprint import repo_fingerprint, repo_material
from kedger.store.paths import project_dir, store_path

SYNC_SCHEMA = "kedger.sync.v1"
BUNDLE_SUFFIX = ".kxs"

# Relative paths under project_dir included in the bundle (store root).
BUNDLE_ENTRIES = (
    "store.sqlite",
    "store.meta.json",
    "raw",
    "packs",
    "acl",
)


class SyncBundleError(RuntimeError):
    """Invalid bundle or import preconditions."""


@dataclass(frozen=True)
class ExportResult:
    path: Path
    repo_fingerprint: str
    file_count: int
    encrypted: bool
    manifest: dict[str, Any]


@dataclass(frozen=True)
class ImportResult:
    repo_fingerprint: str
    backup_path: Path | None
    file_count: int
    encrypted: bool
    manifest: dict[str, Any]


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _project_root(fp: str) -> Path:
    return project_dir(fp)


def _collect_project_files(root: Path) -> list[tuple[str, Path]]:
    """Return (arcname, source_path) pairs for bundle members."""
    items: list[tuple[str, Path]] = []
    for name in BUNDLE_ENTRIES:
        src = root / name
        if not src.exists():
            continue
        if src.is_file():
            items.append((name, src))
        elif src.is_dir():
            for path in sorted(src.rglob("*")):
                if path.is_file():
                    rel = path.relative_to(root).as_posix()
                    items.append((rel, path))
    return items


def _manifest_for(fp: str, *, files: list[str]) -> dict[str, Any]:
    sp = store_path(fp)
    enc = encryption_state(fp, sp)
    meta = read_store_meta(fp) or {}
    return {
        "schema_version": SYNC_SCHEMA,
        "memory_schema": SCHEMA_VERSION,
        "kedger_version": __version__,
        "exported_at": _utc_now(),
        "repo_fingerprint": fp,
        "repo_material": repo_material(),
        "encryption": {
            "store": meta.get("encryption") if enc.enabled else None,
            "raw_payloads": meta.get("raw_payloads"),
        },
        "files": files,
    }


def export_bundle(
    *,
    out_path: Path,
    repo_fp: str | None = None,
) -> ExportResult:
    """Write a `.kxs` tarball of the current repo project store."""
    fp = repo_fp or repo_fingerprint()
    root = _project_root(fp)
    db = store_path(fp)
    if not db.exists():
        raise SyncBundleError(
            f"no store at {db}; run `kedger init` first"
        )

    members = _collect_project_files(root)
    if not members:
        raise SyncBundleError(f"project store empty at {root}")

    arc_names = sorted({arc for arc, _ in members})
    manifest = _manifest_for(fp, files=arc_names)

    out_path = Path(out_path)
    if out_path.suffix != BUNDLE_SUFFIX:
        out_path = out_path.with_suffix(BUNDLE_SUFFIX)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with tarfile.open(out_path, mode="w:gz") as tar:
        manifest_bytes = json.dumps(manifest, indent=2, sort_keys=True).encode("utf-8")
        info = tarfile.TarInfo(name="manifest.json")
        info.size = len(manifest_bytes)
        tar.addfile(info, fileobj=_bytes_io(manifest_bytes))
        for arc, src in members:
            tar.add(src, arcname=arc)

    enc = encryption_state(fp, db)
    return ExportResult(
        path=out_path,
        repo_fingerprint=fp,
        file_count=len(members) + 1,
        encrypted=enc.enabled,
        manifest=manifest,
    )


def _bytes_io(data: bytes):
    import io

    return io.BytesIO(data)


def _read_manifest(tar: tarfile.TarFile) -> dict[str, Any]:
    try:
        member = tar.getmember("manifest.json")
    except KeyError as e:
        raise SyncBundleError("bundle missing manifest.json") from e
    raw = tar.extractfile(member)
    if raw is None:
        raise SyncBundleError("cannot read manifest.json")
    try:
        manifest = json.loads(raw.read().decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        raise SyncBundleError(f"invalid manifest.json: {e}") from e
    if not isinstance(manifest, dict):
        raise SyncBundleError("manifest.json must be a JSON object")
    if manifest.get("schema_version") != SYNC_SCHEMA:
        raise SyncBundleError(
            f"unsupported bundle schema: {manifest.get('schema_version')!r} "
            f"(expected {SYNC_SCHEMA})"
        )
    return manifest


def import_bundle(
    bundle_path: Path,
    *,
    force: bool = False,
    repo_fp: str | None = None,
) -> ImportResult:
    """Restore a `.kxs` bundle into ~/.kedger/projects/<fp>/."""
    bundle_path = Path(bundle_path)
    if not bundle_path.is_file():
        raise SyncBundleError(f"bundle not found: {bundle_path}")

    target_fp = repo_fp or repo_fingerprint()
    root = _project_root(target_fp)

    with tarfile.open(bundle_path, mode="r:gz") as tar:
        manifest = _read_manifest(tar)
        bundle_fp = manifest.get("repo_fingerprint")
        if bundle_fp != target_fp and not force:
            raise SyncBundleError(
                f"repo fingerprint mismatch: bundle={bundle_fp} "
                f"current={target_fp} (pass --force to import anyway)"
            )

        allowed = set(manifest.get("files") or [])
        backup: Path | None = None
        if root.exists() and any(root.iterdir()):
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            backup = root.with_name(root.name + f".sync-backup-{stamp}")
            root.rename(backup)
        root.mkdir(parents=True, exist_ok=True)

        extracted = 0
        for member in tar.getmembers():
            if member.name == "manifest.json":
                continue
            if member.isdir():
                continue
            if allowed and member.name not in allowed:
                continue
            if ".." in Path(member.name).parts:
                raise SyncBundleError(f"unsafe path in bundle: {member.name!r}")
            dest = root / member.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            src = tar.extractfile(member)
            if src is None:
                continue
            with dest.open("wb") as out:
                shutil.copyfileobj(src, out)
            extracted += 1

    db = store_path(target_fp)
    enc = encryption_state(target_fp, db)
    return ImportResult(
        repo_fingerprint=target_fp,
        backup_path=backup,
        file_count=extracted,
        encrypted=enc.enabled,
        manifest=manifest,
    )


def keys_guidance_lines(*, encrypted: bool) -> list[str]:
    """Operator hints printed after export/import (keys stay out of bundle)."""
    lines = [
        "keys:         NOT included in bundle (by design — transfer separately)",
        "principal:    copy ~/.kedger/keys/principal.{json,ed25519,x25519} "
        "to the new device, or run `kedger keys init` and re-grant peers",
    ]
    if encrypted:
        lines.append(
            "store key:    copy KEDGER_STORE_KEY, OS keyring entry, or "
            "~/.kedger/keys/store.key before opening the store"
        )
    else:
        lines.append(
            "encryption:   bundle contains plaintext SQLite — "
            "run `kedger store encrypt` before export for at-rest protection"
        )
    lines.append(
        "peer share:   unchanged — use `kedger peer send` / sealed `.kxp` "
        "(explicit_only; not ambient sync)"
    )
    lines.append(
        "handoff only: for a slice without full store, use "
        "`kedger pack-export` → `kedger hydrate --pack`"
    )
    return lines
