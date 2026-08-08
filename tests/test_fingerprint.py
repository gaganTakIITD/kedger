from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from kedger.store.fingerprint import normalize_remote_url, repo_fingerprint


def test_fingerprint_stable_from_remote(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    subprocess.run(
        ["git", "remote", "add", "origin", "git@github.com:Acme/Demo.Git"],
        cwd=repo,
        check=True,
        capture_output=True,
    )
    monkeypatch.chdir(repo)
    fp1 = repo_fingerprint()
    fp2 = repo_fingerprint()
    assert fp1 == fp2
    assert fp1.startswith("rf_")
    assert len(fp1) == 3 + 16

    assert normalize_remote_url("git@github.com:Acme/Demo.Git") == "github.com/acme/demo"
    assert (
        normalize_remote_url("https://github.com/Acme/Demo.git")
        == "github.com/acme/demo"
    )
    assert (
        normalize_remote_url(
            "https://x-access-token:ghs_secret@github.com/Acme/Demo.git"
        )
        == "github.com/acme/demo"
    )
