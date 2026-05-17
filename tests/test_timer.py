"""Tests for utils/timer.py"""
import time
import pytest
from utils.timer import Timer, timer


class TestTimerContextManager:
    def test_elapsed_is_positive(self):
        with Timer("test", log=False) as t:
            time.sleep(0.05)
        assert t.elapsed >= 0.04

    def test_elapsed_accessible_after_block(self):
        t = Timer(log=False)
        with t:
            pass
        assert isinstance(t.elapsed, float)

    def test_no_log_does_not_raise(self):
        with Timer("silent", log=False):
            pass


class TestTimerDecorator:
    def test_return_value_preserved(self):
        @timer
        def fn():
            return 42
        assert fn() == 42

    def test_args_passed_through(self):
        @timer
        def add(a, b):
            return a + b
        assert add(2, 3) == 5

    def test_exception_propagates(self):
        @timer
        def boom():
            raise ValueError("err")
        with pytest.raises(ValueError):
            boom()
