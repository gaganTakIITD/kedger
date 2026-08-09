# Publishing Kedger

## Current PyPI status

| Version | Notes |
|---------|--------|
| `0.1.0` | On PyPI now — thinner CLI surface |
| `0.1.1` | Launch tip (this branch/tag) — publish after merge |

Project: https://pypi.org/project/kedger/

**Do not reuse `0.1.0`.** Bump for every upload.

## Release checklist (`0.1.1`)

1. Merge tip to `main` (PR green: pytest + smoke + wheel packs)
2. Confirm versions match: `pyproject.toml`, `src/kedger/__init__.py`, `CHANGELOG.md`
3. Local gate:

   ```bash
   pip install -e ".[dev]"
   bash scripts/check_hook_packs_sync.sh
   pytest -q
   bash scripts/smoke_transfer.sh
   bash scripts/smoke_wheel_install.sh
   ```

4. Tag and push: `git tag v0.1.1 && git push origin v0.1.1`
5. Preferred: GitHub Actions **Release** workflow publishes via Trusted Publisher  
   Fallback: `python -m build && twine upload dist/*`
6. Confirm https://pypi.org/project/kedger/0.1.1/ and GitHub Release notes → CHANGELOG

## Trusted Publisher (one-time)

On PyPI → kedger → Publishing → add GitHub:

| Field | Value |
|-------|--------|
| Owner | `gaganTakIITD` |
| Repository | `kedger` |
| Workflow | `release.yml` |
| Environment | `pypi` |

Create the matching GitHub Environment named `pypi` (optional protection rules).

Workflow: `.github/workflows/release.yml` (OIDC, no long-lived token in the repo).

## Manual upload fallback

```bash
pip install -e ".[dev]"
pytest -q
rm -rf dist build *.egg-info
python -m build
twine check dist/*
TWINE_USERNAME=__token__ TWINE_PASSWORD=pypi-... twine upload dist/*
```

## After upload

1. README install stays `pip install "kedger>=0.1.1"`
2. Do not publish from a dirty tree; do not bundle MoDeX assets

## Do not

- Claim Phase F features (LLM distill / sync / MCP) as shipped
- Market Kedger as MoDeX
