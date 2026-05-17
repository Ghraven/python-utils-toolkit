# Contributing to python-utils-toolkit

Thanks for your interest! This is a small focused library — contributions that add clear value are very welcome.

## What fits

- New utility module in `utils/` (bring your own test file in `tests/`)
- Bug fix with a regression test
- Documentation improvement

## What doesn't fit

- Modules that require external dependencies (this is a zero-dep library)
- Utilities already covered by the standard library with minimal wrapping

## How to contribute

1. Fork the repo
2. Create a branch: `git checkout -b fix/my-fix` or `feat/my-module`
3. Add your code in `utils/`
4. Add tests in `tests/test_<module>.py`
5. Run tests: `pytest`
6. Open a PR with a clear description of what you changed and why

## Running tests

```bash
pip install pytest pytest-asyncio
pytest
```

## Code style

- Type hints on all public functions
- Docstring with a one-line summary and `Args` / `Returns` where helpful
- Pure Python — no external runtime dependencies
