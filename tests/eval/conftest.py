"""Eval harness fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest

from sli_util import sli_path


@pytest.fixture()
def sli_sink(tmp_path: Path) -> Path:
    return sli_path(tmp_path)
