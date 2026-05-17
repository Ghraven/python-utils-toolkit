# Changelog

All notable changes to python-utils-toolkit are documented here.

## [Unreleased]

### Planned
- `http_utils` — thin wrapper around urllib for GET/POST with retries
- `cli_utils` — argument parsing helpers for script CLIs
- PyPI publish workflow

---

## [1.1.0] — 2026-05-11

### Added
- Tests for `rate_limiter` — covers `AsyncRateLimiter` and `RateLimiter` edge cases
- Tests for `number_utils` — formatting, tick rounding, pct_change
- Tests for `string_utils` — slugify, truncate, camel_to_snake
- Tests for `retry` — exponential backoff, jitter, exception filtering
- Tests for `cache_utils` — TTL expiry, maxsize eviction, memoize decorator
- Tests for `async_utils` — timeout, gather_safe, async_retry
- Tests for `dict_utils` — deep_merge, safe_get, flatten_dict, pick, omit
- Tests for `file_helpers` — read/write, atomic_write, ensure_dir, file_size
- Tests for `datetime_utils` — now_utc, humanize_delta, parse_date, timestamp_ms
- Tests for `list_utils` — chunk, flatten, deduplicate, batch_by, first, last
- Tests for `crypto_utils` — hmac_sha256, sha256, md5, generate_nonce
- Tests for `validation_utils` — is_valid_symbol, is_valid_email, require, require_keys, is_within_range
- Tests for `timer` — Timer context manager, @timer decorator
- Tests for `env` — Env typed loader (str, int, float, bool, list)
- Tests for `logger` — get_logger setup, colour formatter

---

## [1.0.0] — 2025-05-01

### Added
- `utils/retry.py` — `@retry` decorator with exponential backoff and jitter
- `utils/rate_limiter.py` — token-bucket rate limiter (sync + async)
- `utils/timer.py` — `@timer` decorator and `Timer` context manager
- `utils/file_helpers.py` — safe read/write, atomic saves, JSON helpers
- `utils/logger.py` — structured logging with colour output and file rotation
- `utils/env.py` — typed `.env` / environment variable loader
- `utils/string_utils.py` — slugify, truncate, camel_to_snake
- `utils/datetime_utils.py` — UTC helpers, humanize_delta, market hours check
- `utils/number_utils.py` — currency format, tick rounding, pct_change
- `utils/list_utils.py` — chunk, flatten, deduplicate, batch_by
- `utils/dict_utils.py` — deep_merge, safe_get, flatten_dict, pick, omit
- `utils/cache_utils.py` — TTLCache and `@memoize` for API response caching
- `utils/async_utils.py` — async retry, timeout wrapper, gather_safe
- `utils/crypto_utils.py` — HMAC-SHA256 signing, nonce generation
- `utils/validation_utils.py` — guard clauses, symbol/email validation
- `pyproject.toml` with full PyPI metadata
- `README.md` with usage examples for all modules
