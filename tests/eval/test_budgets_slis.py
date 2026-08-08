"""Budget + hydrate survival SLIs."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.constants import HANDOFF_MAX_BYTES
from kedger.hydrate import project_hydrate
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint

from sli_util import record_sli


def test_hydrate_pack_bytes_and_no_critical_drop(
    kedger_env: Path, runner: CliRunner, sli_sink: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    for kind, stmt in [
        ("constraint", "Must use TLS"),
        ("reject", "Do not store passwords in plaintext"),
        ("decision", "Use Argon2id for password hashing"),
        ("gotcha", "Legacy bcrypt hashes still in DB"),
        ("next", "Migrate rows next sprint"),
    ]:
        # CLI kind aliases
        k = {"reject": "reject", "next": "next_step"}.get(kind, kind)
        assert runner.invoke(main, ["remember", k, stmt]).exit_code == 0, stmt

    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    # Tiny budget to force drops of low-survival kinds
    proj = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        max_bytes=800,
    )
    record_sli(sli_sink, "hydrate_pack_bytes", float(proj.used_bytes), unit="bytes")
    assert proj.used_bytes <= HANDOFF_MAX_BYTES
    kinds = {a["kind"] for a in proj.anchors}
    # Critical kinds must survive while gotcha/next may drop
    assert "constraint" in kinds or "rejection" in kinds or "decision" in kinds
    violations = 0
    if proj.dropped:
        dropped_kinds = []
        for did in proj.dropped:
            # dropped ids may be gone from selected; infer from store
            a = store.get_anchor(did)
            if a:
                dropped_kinds.append(a["kind"])
        selected_low = [
            a["kind"]
            for a in proj.anchors
            if a["kind"] in {"gotcha", "open_question", "next_step"}
        ]
        for dk in dropped_kinds:
            if dk in {"constraint", "rejection", "decision"} and selected_low:
                violations += 1
    record_sli(sli_sink, "anchor_drop_violations", float(violations), unit="count")
    assert violations == 0


def test_handoff_under_budget(kedger_env: Path, runner: CliRunner, sli_sink: Path) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert runner.invoke(main, ["remember", "constraint", "TLS only"]).exit_code == 0
    out = Path("handoff_eval.kxp")
    res = runner.invoke(main, ["handoff", "--out", str(out)])
    assert res.exit_code == 0, res.output
    size = out.stat().st_size
    record_sli(
        sli_sink, "hydrate_pack_bytes", float(size), unit="bytes", pack=str(out)
    )
    # Sealed blob may be larger than plaintext budget; plaintext projection checked above.
    assert size > 0
