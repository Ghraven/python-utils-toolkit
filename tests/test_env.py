"""Tests for utils/env.py"""
import os
import pytest
from utils.env import Env


@pytest.fixture(autouse=True)
def clean_env():
    """Remove test keys before and after each test."""
    test_keys = ["TEST_STR", "TEST_INT", "TEST_FLOAT", "TEST_BOOL", "TEST_LIST"]
    for k in test_keys:
        os.environ.pop(k, None)
    yield
    for k in test_keys:
        os.environ.pop(k, None)


def test_str_from_env():
    os.environ["TEST_STR"] = "hello"
    env = Env(dotenv_path=".nonexistent")
    assert env.str("TEST_STR") == "hello"


def test_str_default():
    env = Env(dotenv_path=".nonexistent")
    assert env.str("TEST_STR", default="fallback") == "fallback"


def test_str_missing_raises():
    env = Env(dotenv_path=".nonexistent")
    with pytest.raises(KeyError):
        env.str("TEST_STR")


def test_int_from_env():
    os.environ["TEST_INT"] = "42"
    env = Env(dotenv_path=".nonexistent")
    assert env.int("TEST_INT") == 42


def test_int_default():
    env = Env(dotenv_path=".nonexistent")
    assert env.int("TEST_INT", default=8080) == 8080


def test_int_invalid_raises():
    os.environ["TEST_INT"] = "not_a_number"
    env = Env(dotenv_path=".nonexistent")
    with pytest.raises(ValueError):
        env.int("TEST_INT")


def test_float_from_env():
    os.environ["TEST_FLOAT"] = "3.14"
    env = Env(dotenv_path=".nonexistent")
    assert env.float("TEST_FLOAT") == pytest.approx(3.14)


def test_bool_true_values():
    env = Env(dotenv_path=".nonexistent")
    for val in ["1", "true", "True", "yes", "on"]:
        os.environ["TEST_BOOL"] = val
        assert env.bool("TEST_BOOL") is True


def test_bool_false_values():
    env = Env(dotenv_path=".nonexistent")
    for val in ["0", "false", "no", "off", ""]:
        os.environ["TEST_BOOL"] = val
        assert env.bool("TEST_BOOL") is False


def test_list_from_env():
    os.environ["TEST_LIST"] = "a,b,c"
    env = Env(dotenv_path=".nonexistent")
    assert env.list("TEST_LIST") == ["a", "b", "c"]


def test_list_missing_returns_empty():
    env = Env(dotenv_path=".nonexistent")
    assert env.list("TEST_LIST") == []


def test_loads_from_dotenv_file(tmp_path):
    dotenv = tmp_path / ".env"
    dotenv.write_text("TEST_STR=from_file\n", encoding="utf-8")
    os.environ.pop("TEST_STR", None)
    env = Env(dotenv_path=dotenv)
    assert env.str("TEST_STR") == "from_file"


def test_dotenv_does_not_override_existing(tmp_path):
    dotenv = tmp_path / ".env"
    dotenv.write_text("TEST_STR=from_file\n", encoding="utf-8")
    os.environ["TEST_STR"] = "from_env"
    env = Env(dotenv_path=dotenv)
    assert env.str("TEST_STR") == "from_env"
