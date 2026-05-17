"""Tests for utils/datetime_utils.py"""
from datetime import datetime, timezone
from utils.datetime_utils import now_utc, parse_date, humanize_delta, timestamp_ms


def test_now_utc_is_aware():
    dt = now_utc()
    assert dt.tzinfo is not None
    assert dt.tzinfo == timezone.utc


def test_parse_date_returns_aware():
    dt = parse_date("2024-01-15")
    assert dt.year == 2024
    assert dt.month == 1
    assert dt.day == 15
    assert dt.tzinfo == timezone.utc


def test_humanize_delta_seconds_only():
    assert humanize_delta(45) == "45s"


def test_humanize_delta_minutes_and_seconds():
    assert humanize_delta(90) == "1m 30s"


def test_humanize_delta_hours():
    assert humanize_delta(3661) == "1h 1m 1s"


def test_humanize_delta_exact_hour():
    assert humanize_delta(3600) == "1h"


def test_humanize_delta_zero():
    assert humanize_delta(0) == "0s"


def test_timestamp_ms_is_int():
    ts = timestamp_ms()
    assert isinstance(ts, int)
    assert ts > 1_700_000_000_000  # after Nov 2023
