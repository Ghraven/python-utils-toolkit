"""Tests for utils.rate_limiter."""
import time
from utils.rate_limiter import RateLimiter


def test_allows_burst():
    limiter = RateLimiter(calls_per_second=100, burst=5)
    start = time.monotonic()
    for _ in range(5):
        limiter.acquire()
    elapsed = time.monotonic() - start
    assert elapsed < 0.2


def test_callable_interface():
    limiter = RateLimiter(calls_per_second=100)
    limiter()  # should not raise


def test_single_acquire():
    limiter = RateLimiter(calls_per_second=50)
    limiter.acquire()  # should not block
