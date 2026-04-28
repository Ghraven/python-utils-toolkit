"""Tests for utils.number_utils."""
from utils.number_utils import (
    format_currency, round_to_tick, pct_change, clamp, safe_divide,
)


def test_format_currency():
    assert format_currency(1234567.89) == "$1,234,567.89"
    assert format_currency(100, symbol="€") == "€100.00"


def test_round_to_tick():
    assert round_to_tick(0.12345, 0.0001) == 0.1235
    assert round_to_tick(87654.321, 0.01) == 87654.32


def test_pct_change_positive():
    assert pct_change(100, 110) == 10.0


def test_pct_change_negative():
    assert pct_change(100, 90) == -10.0


def test_pct_change_zero_base():
    assert pct_change(0, 100) == 0.0


def test_clamp():
    assert clamp(15, 0, 10) == 10
    assert clamp(-5, 0, 10) == 0
    assert clamp(5, 0, 10) == 5


def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) == 0.0
    assert safe_divide(10, 0, default=-1) == -1
