"""Purpose-minimized Anchor projection (AirGapAgent / Contextual Integrity).

Lit: AirGapAgent 2405.05175 — only task-needed fields in third-party context.
"""

from __future__ import annotations

from typing import Any

# Fields always allowed in any hydrate/pack projection
_CORE_FIELDS = (
    "schema_version",
    "id",
    "kind",
    "statement",
    "status",
    "visibility",
    "importance",
    "valid_at",
    "invalid_at",
    "created_at",
    "updated_at",
    "supersedes",
    "superseded_by",
    "shareable",
    "workstream_id",
    "about",
    "repo_fingerprint",
)

# Extra fields for eng-local / full purposes
_ENGINEERING_EXTRA = (
    "reason",
    "provenance",
)

# Never export these under third-party / export purposes
_SENSITIVE = frozenset({"reason", "provenance", "secret_hits", "record_json"})

PURPOSE_THIRD_PARTY = "third_party"
PURPOSE_EXPORT = "export"
PURPOSE_ENGINEERING = "engineering"
PURPOSE_INTERNAL = "internal"

MINIMIZING_PURPOSES = frozenset({PURPOSE_THIRD_PARTY, PURPOSE_EXPORT})


def minimize_anchor_for_purpose(
    anc: dict[str, Any],
    purpose: str | None,
) -> dict[str, Any]:
    """Project Anchor fields for a hydrate/pack purpose.

    ``None`` / engineering / internal → keep reason + provenance (no secret_hits).
    ``third_party`` / ``export`` → core fields only (statement plane, no reason).
    """
    if purpose is None or purpose in {PURPOSE_ENGINEERING, PURPOSE_INTERNAL, ""}:
        out = {k: anc[k] for k in (*_CORE_FIELDS, *_ENGINEERING_EXTRA) if k in anc}
        # never surface raw secret_hits list in hydrate dumps
        return out

    if purpose in MINIMIZING_PURPOSES:
        return {k: anc[k] for k in _CORE_FIELDS if k in anc}

    # Unknown purpose → minimize (fail closed)
    return {k: anc[k] for k in _CORE_FIELDS if k in anc}


def minimize_anchors(
    anchors: list[dict[str, Any]],
    purpose: str | None,
) -> list[dict[str, Any]]:
    return [minimize_anchor_for_purpose(a, purpose) for a in anchors]
