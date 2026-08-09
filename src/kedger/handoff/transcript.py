"""Lossless transcript archive — zip-style byte compression for session transfer.

Semantic handoff (Anchors + activity) is lossy-on-purpose for compact inject.
This module is the *other* transfer path: keep the redacted turn tape, shrink it
like zip (zlib), seal it with the pack (or a sidecar), unpack in a later session.

Analogy: a large chat dump → compressed blob that still restores the same turns.
"""

from __future__ import annotations

import base64
import json
import zlib
from pathlib import Path
from typing import Any

TRANSCRIPT_SCHEMA = "kedger.transcript_archive.v1"
DEFAULT_LEVEL = 9


def turns_from_observations(observations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Project L0 observations into a transferable turn tape (already redacted)."""
    turns: list[dict[str, Any]] = []
    for o in observations:
        turn: dict[str, Any] = {
            "id": o.get("id"),
            "type": o.get("type"),
            "ts": o.get("ts"),
            "summary": o.get("summary") or "",
            "session_id": o.get("session_id"),
        }
        if o.get("entity_hints"):
            turn["entity_hints"] = o["entity_hints"]
        if o.get("edit_stats"):
            turn["edit_stats"] = o["edit_stats"]
        elif o.get("lines_added") is not None or o.get("lines_removed") is not None:
            turn["edit_stats"] = {
                "lines_added": o.get("lines_added"),
                "lines_removed": o.get("lines_removed"),
            }
        turns.append(turn)
    return turns


def compress_transcript(
    turns: list[dict[str, Any]],
    *,
    level: int = DEFAULT_LEVEL,
) -> dict[str, Any]:
    """zlib-compress a turn tape. Lossless w.r.t. the JSON turn list."""
    raw = json.dumps(turns, sort_keys=True, separators=(",", ":")).encode("utf-8")
    blob = zlib.compress(raw, level=level)
    ratio = (len(blob) / len(raw)) if raw else 1.0
    return {
        "schema": TRANSCRIPT_SCHEMA,
        "codec": "zlib",
        "level": level,
        "turn_count": len(turns),
        "raw_bytes": len(raw),
        "compressed_bytes": len(blob),
        "ratio": round(ratio, 4),
        "blob_b64": base64.b64encode(blob).decode("ascii"),
    }


def decompress_transcript(archive: dict[str, Any]) -> list[dict[str, Any]]:
    """Inverse of compress_transcript — must roundtrip exactly."""
    if not archive or archive.get("schema") != TRANSCRIPT_SCHEMA:
        raise ValueError("unsupported transcript archive schema")
    if archive.get("codec") != "zlib":
        raise ValueError(f"unsupported codec: {archive.get('codec')}")
    blob = base64.b64decode(archive["blob_b64"])
    raw = zlib.decompress(blob)
    turns = json.loads(raw.decode("utf-8"))
    if not isinstance(turns, list):
        raise ValueError("archive payload is not a turn list")
    return turns


def archive_meta(archive: dict[str, Any] | None) -> dict[str, Any] | None:
    """Stats + schema without the blob — safe for inject / budget headers."""
    if not archive:
        return None
    return {
        "schema": archive.get("schema"),
        "codec": archive.get("codec"),
        "turn_count": archive.get("turn_count"),
        "raw_bytes": archive.get("raw_bytes"),
        "compressed_bytes": archive.get("compressed_bytes"),
        "ratio": archive.get("ratio"),
        "sidecar": archive.get("sidecar"),
        "inline": bool(archive.get("blob_b64")),
    }


def archive_fits(archive: dict[str, Any], *, max_bytes: int) -> bool:
    """Whether the archive JSON can sit inside a remaining pack budget."""
    if max_bytes <= 0:
        return False
    raw = json.dumps(archive, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return len(raw) <= max_bytes


def compression_stats(archive: dict[str, Any]) -> dict[str, Any]:
    return {
        "turn_count": archive.get("turn_count"),
        "raw_bytes": archive.get("raw_bytes"),
        "compressed_bytes": archive.get("compressed_bytes"),
        "ratio": archive.get("ratio"),
        "codec": archive.get("codec"),
        "schema": archive.get("schema"),
    }


def write_transcript_sidecar(path: Path, archive: dict[str, Any]) -> Path:
    """Persist full archive next to a pack when inline budget is exhausted."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(archive, sort_keys=True, separators=(",", ":")),
        encoding="utf-8",
    )
    return path


def read_transcript_sidecar(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("sidecar is not an archive object")
    return data


def resolve_transcript_archive(
    pack_or_episode: dict[str, Any],
    *,
    sidecar_root: Path | None = None,
) -> dict[str, Any] | None:
    """Load inline transcript or follow sidecar pointer for cross-session transfer."""
    archive = pack_or_episode.get("transcript")
    if isinstance(archive, dict) and archive.get("blob_b64"):
        return archive
    meta = pack_or_episode.get("transcript_meta") or archive_meta(archive)
    if not isinstance(meta, dict):
        return archive if isinstance(archive, dict) else None
    side = meta.get("sidecar") or (archive or {}).get("sidecar")
    if side and sidecar_root is not None:
        path = Path(side)
        if not path.is_absolute():
            path = sidecar_root / path
        if path.exists():
            return read_transcript_sidecar(path)
    return archive if isinstance(archive, dict) and archive.get("blob_b64") else None


def attach_transcript_for_pack(
    archive: dict[str, Any] | None,
    *,
    pack: dict[str, Any],
    max_bytes: int,
    sidecar_dir: Path | None = None,
    handoff_id: str | None = None,
) -> dict[str, Any]:
    """Prefer inline blob; else write sidecar and keep meta only.

    Drop priority for budget: transcript blob first (lossy semantic layers stay).
    """
    out = dict(pack)
    if not archive:
        out["transcript"] = None
        out["transcript_meta"] = None
        layers = dict(out.get("layers") or {})
        layers["transcript"] = "none"
        out["layers"] = layers
        return out

    trial = dict(out)
    trial["transcript"] = archive
    trial["transcript_meta"] = archive_meta(archive)
    raw = json.dumps(trial, sort_keys=True, separators=(",", ":")).encode("utf-8")
    if len(raw) <= max_bytes:
        out["transcript"] = archive
        out["transcript_meta"] = archive_meta(archive)
        layers = dict(out.get("layers") or {})
        layers["transcript"] = "inline_zlib"
        out["layers"] = layers
        return out

    # Over budget — externalize blob
    meta = archive_meta(archive) or {}
    sidecar_name = f"{handoff_id or out.get('id') or 'hf'}.transcript.json"
    if sidecar_dir is not None:
        write_transcript_sidecar(sidecar_dir / sidecar_name, archive)
        meta["sidecar"] = sidecar_name
    meta["inline"] = False
    out["transcript"] = None
    out["transcript_meta"] = meta
    dropped = list((out.get("budget") or {}).get("dropped") or [])
    dropped.append("transcript_blob")
    budget = dict(out.get("budget") or {})
    budget["dropped"] = dropped
    out["budget"] = budget
    layers = dict(out.get("layers") or {})
    layers["transcript"] = "sidecar_zlib" if sidecar_dir is not None else "meta_only"
    out["layers"] = layers
    return out


def transcript_inject_lines(
    meta_or_archive: dict[str, Any] | None,
    *,
    turns: list[dict[str, Any]] | None = None,
    tail: int = 4,
) -> list[str]:
    """Render transfer-layer hint (+ optional recent turn tail) for hydrate inject."""
    if not meta_or_archive and not turns:
        return []
    meta = archive_meta(meta_or_archive) if meta_or_archive else {}
    if not meta and meta_or_archive:
        meta = dict(meta_or_archive)
    turns_n = meta.get("turn_count") or (len(turns) if turns else 0)
    raw_b = meta.get("raw_bytes") or 0
    comp_b = meta.get("compressed_bytes") or 0
    ratio = meta.get("ratio")
    where = "inline" if meta.get("inline") else (
        f"sidecar:{meta.get('sidecar')}" if meta.get("sidecar") else "meta"
    )
    lines = [
        "",
        "# Transcript archive (lossless zlib transfer)",
        (
            f"- turns={turns_n} raw={raw_b}B compressed={comp_b}B "
            f"ratio={ratio} via={where}"
        ),
        "- use `kedger transcript decompress --live` for full redacted turn tape",
    ]
    if turns:
        lines.append("- recent turns (lossy preview; full tape in archive):")
        for t in turns[-tail:]:
            summary = (t.get("summary") or "")[:140]
            lines.append(f"  - [{t.get('type')}] {summary}")
    return lines
