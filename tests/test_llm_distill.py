"""Optional LLM distill — mocked HTTP only (no network in CI)."""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest
from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify.engine import cognify_workstream
from kedger.cognify.llm_distill import (
    distill_episode,
    llm_distill_requested,
    resolve_llm_config,
)
from kedger.cognify.extract import extract_claims_from_span
from kedger.store import Store, repo_fingerprint
from time_helpers import recent_ts


def test_llm_distill_off_by_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KEDGER_LLM_DISTILL", raising=False)
    assert llm_distill_requested(flag=False) is False
    assert resolve_llm_config() is None


def test_resolve_config_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KEDGER_LLM_API_KEY", "sk-test")
    monkeypatch.setenv("KEDGER_LLM_BASE_URL", "https://example.com/v1")
    monkeypatch.setenv("KEDGER_LLM_MODEL", "test-model")
    cfg = resolve_llm_config()
    assert cfg is not None
    assert cfg.api_key == "sk-test"
    assert cfg.base_url == "https://example.com/v1"
    assert cfg.model == "test-model"


def test_distill_episode_mock_http() -> None:
    llm_json = {
        "summary": "JWT auth adopted; cookie sessions rejected; refresh rotation next.",
        "claims": [
            {
                "kind": "constraint",
                "statement": "Never store refresh tokens in localStorage",
            }
        ],
    }

    def mock_post(
        url: str, headers: dict[str, str], body: bytes, timeout: float
    ) -> tuple[int, str]:
        assert url.endswith("/chat/completions")
        assert headers["Authorization"] == "Bearer sk-mock"
        payload = json.loads(body.decode("utf-8"))
        assert payload["model"] == "gpt-test"
        return (
            200,
            json.dumps(
                {
                    "choices": [
                        {"message": {"content": json.dumps(llm_json)}},
                    ]
                }
            ),
        )

    span = [
        {
            "id": "obs_1",
            "type": "user_prompt",
            "summary": "Reject cookie sessions for auth",
            "ts": recent_ts(minutes_ago=1),
        },
        {
            "id": "obs_2",
            "type": "user_prompt",
            "summary": "We decided to use JWT instead",
            "ts": recent_ts(minutes_ago=0),
        },
    ]
    heuristic = extract_claims_from_span(span)
    from kedger.cognify.llm_distill import LlmDistillConfig

    cfg = LlmDistillConfig(api_key="sk-mock", base_url="https://mock/v1", model="gpt-test")
    out = distill_episode(
        span,
        heuristic_summary="heuristic digest",
        heuristic_claims=heuristic,
        config=cfg,
        http_post=mock_post,
    )
    assert out is not None
    assert "JWT" in out.summary
    assert any("localStorage" in c.statement for c in out.supplemental_claims)


def test_distill_fails_soft_on_http_error() -> None:
    def bad_post(
        url: str, headers: dict[str, str], body: bytes, timeout: float
    ) -> tuple[int, str]:
        return 401, '{"error":"bad key"}'

    from kedger.cognify.llm_distill import LlmDistillConfig

    cfg = LlmDistillConfig(api_key="sk-bad")
    out = distill_episode(
        [{"summary": "decide redis", "type": "user_prompt"}],
        heuristic_summary="decide redis",
        heuristic_claims=[],
        config=cfg,
        http_post=bad_post,
    )
    assert out is None


def test_cognify_llm_distill_cli_mock(
    kedger_env: Path, runner: CliRunner, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("KEDGER_LLM_API_KEY", "sk-ci")
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    from kedger.keys import load_principal

    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    store.ingest_observation(
        {
            "type": "user_prompt",
            "session_id": "s1",
            "workstream_id": ws["id"],
            "summary": "Reject cookie sessions; use JWT",
            "ts": recent_ts(minutes_ago=0),
        },
        principal_id=p.principal_id,
    )

    def mock_post(
        url: str, headers: dict[str, str], body: bytes, timeout: float
    ) -> tuple[int, str]:
        content = json.dumps(
            {
                "summary": "Session: JWT over cookies for auth.",
                "claims": [],
            }
        )
        return 200, json.dumps({"choices": [{"message": {"content": content}}]})

    import kedger.cognify.llm_distill as ld

    monkeypatch.setattr(ld, "_default_http_post", mock_post)
    cog = runner.invoke(main, ["cognify", "--force", "--llm-distill", "--no-reseal"])
    assert cog.exit_code == 0, cog.output
    assert "distill:    llm" in cog.output

    store = Store.open(repo_fingerprint())
    ep = store.latest_episode(ws["id"])
    assert ep is not None
    assert ep.get("distill_v1", {}).get("mode") == "llm"
    assert "JWT" in ep["summary"]


def test_cognify_llm_flag_without_key_falls_back(
    kedger_env: Path, runner: CliRunner, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("KEDGER_LLM_API_KEY", raising=False)
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    from kedger.keys import load_principal

    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    store.ingest_observation(
        {
            "type": "user_prompt",
            "session_id": "s1",
            "workstream_id": ws["id"],
            "summary": "Reject cookie sessions for auth",
            "ts": recent_ts(minutes_ago=0),
        },
        principal_id=p.principal_id,
    )
    cog = runner.invoke(main, ["cognify", "--force", "--llm-distill", "--no-reseal"])
    assert cog.exit_code == 0, cog.output
    assert "distill:    heuristic" in cog.output
    ep = store.latest_episode(ws["id"])
    assert ep is not None
    assert ep.get("distill_v1") is None
