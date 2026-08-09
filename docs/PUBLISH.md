# Publishing Kedger

## Current PyPI status

| Version | Notes |
|---------|--------|
| `0.1.0` | First claim (2026-08-08) — thinner CLI surface |
| `0.1.1` | Launch surface: init, hooks install, dual-layer, transcript, pack import |

Project: https://pypi.org/project/kedger/

**Do not reuse `0.1.0`.** Bump for every upload.

## Release checklist (`0.1.1+`)

- [ ] `pytest -q` green on the release commit
- [ ] `./scripts/smoke_transfer.sh` green
- [ ] Version bumped in `pyproject.toml` + `src/kedger/__init__.py` + `CHANGELOG.md`
- [ ] Git tag `vX.Y.Z` pushed
- [ ] GitHub Release notes point at CHANGELOG

## Build & upload

```bash
pip install -e ".[dev]"
pytest -q
rm -rf dist build *.egg-info
python -m build
twine check dist/*
TWINE_USERNAME=__token__ TWINE_PASSWORD=pypi-... twine upload dist/*
```

Confirm: https://pypi.org/project/kedger/

## After upload

1. README default install remains `pip install "kedger>=0.1.1"`
2. Prefer Trusted Publisher (GitHub → `gaganTakIITD/kedger`) for later releases
3. Do not publish from a dirty tree; do not bundle MoDeX assets

## Do not

- Claim Phase F features (LLM distill / sync / MCP) as shipped
- Market Kedger as MoDeX
