"""Tests for utils.rate_limiter."""
import time
import pytest
from utils.rate_limiter import RateLimiter


def test_allows_burst():
    limiter = RateLimiter(calls_per_second=100, burst=5)
    start = time.monotonic()
    for _ in range(5):
        limiter.acquire()
    elapsed = time.monotonic() - start
    assert elapsed < 0.1  # burst should be near-instant


def test_rate_limits():
    limiter = RateLimiter(calls_per_second=20)
    start = time.monotonic()
    for _ in range(3):
        limiter.acquire()
    elapsed = time.monotonic() - start
    # 3 calls at 20/s should take ~0.1s
    assert elapsed >= 0.05


def test_callable_interface():
    limiter = RateLimiter(calls_per_second=100)
    limiter()  # should not raise
