"""kedger CLI — Phase A store + keys + remember/forget/status/doctor/ingest."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click

from kedger import SCHEMA_VERSION, __version__
from kedger.keys import KeysError, init_principal, load_principal
from kedger.store import Store, kedger_home, repo_fingerprint, repo_material, store_path
from kedger.store.db import KIND_ALIASES
from kedger.store.paths import keys_dir


def _die(msg: str, code: int = 1) -> None:
    click.echo(f"error: {msg}", err=True)
    raise SystemExit(code)


def _require_principal():
    try:
        return load_principal()
    except KeysError as e:
        _die(str(e))


def _open_store() -> Store:
    fp = repo_fingerprint()
    return Store.open(fp)


@click.group()
@click.version_option(__version__, prog_name="kedger")
def main() -> None:
    """Kedger — local-first engineering memory CLI.

    Kedger is not MoDeX. Product locks: ~/.kedger/, .kxp, kedger.memory.v1.
    """


@main.group("keys")
def keys_group() -> None:
    """Manage local Ed25519 principal keys."""


@keys_group.command("init")
@click.option("--name", default="default", show_default=True, help="Principal display name")
@click.option("--force", is_flag=True, help="Rotate / overwrite existing principal")
def keys_init(name: str, force: bool) -> None:
    """Create a local Ed25519 principal under ~/.kedger/keys/."""
    try:
        principal = init_principal(name=name, force=force)
    except KeysError as e:
        _die(str(e))
    click.echo(f"principal_id: {principal.principal_id}")
    click.echo(f"name:         {principal.name}")
    click.echo(f"public_key:   {principal.public_key_b64}")
    click.echo(f"keys_dir:     {keys_dir()}")


@keys_group.command("show")
def keys_show() -> None:
    """Show principal id + public key."""
    principal = _require_principal()
    click.echo(f"principal_id: {principal.principal_id}")
    click.echo(f"name:         {principal.name}")
    click.echo(f"public_key:   {principal.public_key_b64}")
    click.echo(f"created_at:   {principal.created_at}")
    click.echo(f"keys_dir:     {keys_dir()}")


@main.command("remember")
@click.argument("kind")
@click.argument("statement")
@click.option("--reason", default=None, help="Why this Anchor exists")
@click.option("--shareable", is_flag=True, help="Explicit share (share_mode=explicit_only)")
@click.option("--workstream", default=None, help="Optional workstream id (ws_…)")
def remember_cmd(
    kind: str,
    statement: str,
    reason: str | None,
    shareable: bool,
    workstream: str | None,
) -> None:
    """Create an Anchor (decision/reject/constraint/…)."""
    principal = _require_principal()
    store = _open_store()
    try:
        record = store.remember(
            kind,
            statement,
            reason=reason,
            principal_id=principal.principal_id,
            shareable=shareable,
            workstream_id=workstream,
        )
    except ValueError as e:
        _die(str(e))
    click.echo(f"id:      {record['id']}")
    click.echo(f"kind:    {record['kind']}")
    click.echo(f"status:  {record['status']}")
    click.echo(f"statement: {record['statement']}")
    if record.get("reason"):
        click.echo(f"reason:  {record['reason']}")


@main.command("forget")
@click.argument("anchor_id")
def forget_cmd(anchor_id: str) -> None:
    """Invalidate an Anchor via SUPERSEDES — never hard-delete."""
    principal = _require_principal()
    store = _open_store()
    try:
        result = store.forget(anchor_id, principal_id=principal.principal_id)
    except KeyError as e:
        _die(str(e), code=404)
    except ValueError as e:
        _die(str(e))
    forgotten = result["forgotten"]
    tomb = result["tombstone"]
    edge = result["edge"]
    click.echo(f"forgotten:     {forgotten['id']} (status={forgotten['status']})")
    click.echo(f"superseded_by: {tomb['id']}")
    click.echo(f"edge:          {edge['id']} SUPERSEDES")


@main.command("status")
@click.option("--list", "list_anchors", is_flag=True, help="List active Anchors")
def status_cmd(list_anchors: bool) -> None:
    """Show fingerprint, store path, and counts."""
    fp = repo_fingerprint()
    material = repo_material()
    path = store_path(fp)
    home = kedger_home()
    click.echo(f"schema:            {SCHEMA_VERSION}")
    click.echo(f"kedger_home:       {home}")
    click.echo(f"repo_fingerprint:  {fp}")
    click.echo(f"repo_material:     {material}")
    click.echo(f"store:             {path}")
    if not path.exists():
        click.echo("counts:            (store not initialized)")
        return
    store = Store.open(fp)
    counts = store.counts()
    click.echo(
        "counts:            "
        f"active={counts['anchors_active']} "
        f"superseded={counts['anchors_superseded']} "
        f"total_anchors={counts['anchors_total']} "
        f"observations={counts['observations']} "
        f"supersedes_edges={counts['supersedes_edges']}"
    )
    if list_anchors:
        anchors = store.list_anchors(active_only=True)
        if not anchors:
            click.echo("anchors:           (none active)")
            return
        click.echo("anchors:")
        for a in anchors:
            reason = f" — {a['reason']}" if a.get("reason") else ""
            click.echo(f"  {a['id']}  [{a['kind']}] {a['statement']}{reason}")


@main.command("doctor")
def doctor_cmd() -> None:
    """Run health checks for the local Kedger install."""
    checks: list[tuple[str, bool, str]] = []

    home = kedger_home()
    home.mkdir(parents=True, exist_ok=True)
    checks.append(("kedger_home", home.is_dir(), str(home)))

    try:
        principal = load_principal()
        checks.append(
            ("principal", True, f"{principal.principal_id} ({principal.name})")
        )
        checks.append(("signing_key", principal.signing_key is not None, "present" if principal.signing_key else "missing"))
    except KeysError as e:
        checks.append(("principal", False, str(e)))
        principal = None

    fp = repo_fingerprint()
    path = store_path(fp)
    if path.exists():
        try:
            store = Store.open(fp)
            meta = store.meta()
            ok = meta.get("schema_version") == SCHEMA_VERSION
            checks.append(
                ("store", ok, f"{path} schema={meta.get('schema_version')}")
            )
            counts = store.counts()
            checks.append(
                (
                    "anchors",
                    True,
                    f"active={counts['anchors_active']} total={counts['anchors_total']}",
                )
            )
        except Exception as e:  # noqa: BLE001
            checks.append(("store", False, str(e)))
    else:
        checks.append(("store", True, f"not created yet ({path})"))

    kinds = ", ".join(sorted(set(KIND_ALIASES.values())))
    checks.append(("anchor_kinds", True, kinds))
    checks.append(
        (
            "identity_lock",
            True,
            "Kedger≠MoDeX; CLI=kedger; packs=.kxp; schema=kedger.memory.v1",
        )
    )

    failed = 0
    for name, ok, detail in checks:
        mark = "ok" if ok else "FAIL"
        if not ok:
            failed += 1
        click.echo(f"[{mark}] {name}: {detail}")
    if failed:
        raise SystemExit(1)
    click.echo("doctor: all checks passed")


@main.command("ingest")
@click.option("--from-hook", "from_hook", is_flag=True, required=True, help="Read observation JSON from stdin")
def ingest_cmd(from_hook: bool) -> None:
    """Ingest an L0 observation (typically from an IDE hook)."""
    if not from_hook:
        _die("--from-hook is required")
    principal = _require_principal()
    raw = sys.stdin.read()
    if not raw.strip():
        _die("empty stdin; expected JSON observation")
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as e:
        _die(f"invalid JSON: {e}")
    if not isinstance(payload, dict):
        _die("observation JSON must be an object")
    store = _open_store()
    record = store.ingest_observation(payload, principal_id=principal.principal_id)
    click.echo(f"id:      {record['id']}")
    click.echo(f"type:    {record['type']}")
    click.echo(f"summary: {record['summary']}")


if __name__ == "__main__":
    main()
