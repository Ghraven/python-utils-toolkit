"""Tests for utils.retry."""
import pytest
from utils.retry import retry


def test_succeeds_on_first_attempt():
    @retry(max_attempts=3)
    def always_succeeds():
        return 42
    assert always_succeeds() == 42


def test_retries_and_succeeds():
    calls = []
    @retry(max_attempts=3, base_delay=0.01)
    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise ConnectionError("fail")
        return "ok"
    assert flaky() == "ok"
    assert len(calls) == 3


def test_raises_after_max_attempts():
    @retry(max_attempts=2, base_delay=0.01, exceptions=(ValueError,))
    def always_fails():
        raise ValueError("boom")
    with pytest.raises(ValueError, match="boom"):
        always_fails()


def test_non_matching_exception_propagates_immediately():
    calls = []
    @retry(max_attempts=5, base_delay=0.01, exceptions=(ConnectionError,))
    def wrong_error():
        calls.append(1)
        raise RuntimeError("unexpected")
    with pytest.raises(RuntimeError):
        wrong_error()
    assert len(calls) == 1  # no retries
