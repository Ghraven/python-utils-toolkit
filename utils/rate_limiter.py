"""Token-bucket rate limiter — sync and async variants.

Usage
-----
Sync:
>>> limiter = RateLimiter(calls_per_second=5)
>>> limiter.acquire()   # blocks if bucket is empty

Async:
>>> limiter = AsyncRateLimiter(calls_per_second=10)
>>> await limiter.acquire()
"""

from __future__ import annotations

import asyncio
import threading
import time


class RateLimiter:
    """Thread-safe token-bucket rate limiter.

    Parameters
    ----------
    calls_per_second:
        Maximum sustained call rate.
    burst:
        Maximum number of tokens that can accumulate (default = calls_per_second).
    """

    def __init__(self, calls_per_second: float, burst: int | None = None) -> None:
        self._rate = calls_per_second
        self._capacity = float(burst or calls_per_second)
        self._tokens = self._capacity
        self._last_refill = time.monotonic()
        self._lock = threading.Lock()

    def _refill(self) -> None:
        now = time.monotonic()
        elapsed = now - self._last_refill
        self._tokens = min(self._capacity, self._tokens + elapsed * self._rate)
        self._last_refill = now

    def acquire(self, tokens: float = 1.0) -> None:
        """Block until *tokens* tokens are available."""
        while True:
            with self._lock:
                self._refill()
                if self._tokens >= tokens:
                    self._tokens -= tokens
                    return
                wait = (tokens - self._tokens) / self._rate
            time.sleep(wait)

    def __call__(self, tokens: float = 1.0) -> None:
        """Alias for :meth:`acquire` — makes the limiter callable."""
        self.acquire(tokens)


class AsyncRateLimiter:
    """Asyncio-compatible token-bucket rate limiter.

    Parameters
    ----------
    calls_per_second:
        Maximum sustained call rate.
    burst:
        Maximum number of tokens that can accumulate.
    """

    def __init__(self, calls_per_second: float, burst: int | None = None) -> None:
        self._rate = calls_per_second
        self._capacity = float(burst or calls_per_second)
        self._tokens = self._capacity
        self._last_refill = time.monotonic()
        self._lock = asyncio.Lock()

    def _refill(self) -> None:
        now = time.monotonic()
        elapsed = now - self._last_refill
        self._tokens = min(self._capacity, self._tokens + elapsed * self._rate)
        self._last_refill = now

    async def acquire(self, tokens: float = 1.0) -> None:
        """Await until *tokens* tokens are available."""
        while True:
            async with self._lock:
                self._refill()
                if self._tokens >= tokens:
                    self._tokens -= tokens
                    return
                wait = (tokens - self._tokens) / self._rate
            await asyncio.sleep(wait)
