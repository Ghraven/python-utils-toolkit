"""Tests for utils/dict_utils.py"""
import pytest
from utils.dict_utils import deep_merge, safe_get, flatten_dict, pick, omit


class TestDeepMerge:
    def test_simple_merge(self):
        result = deep_merge({"a": 1}, {"b": 2})
        assert result == {"a": 1, "b": 2}

    def test_nested_merge(self):
        base = {"a": {"x": 1}}
        override = {"a": {"y": 2}}
        assert deep_merge(base, override) == {"a": {"x": 1, "y": 2}}

    def test_override_wins_for_non_dict(self):
        assert deep_merge({"a": 1}, {"a": 99}) == {"a": 99}

    def test_does_not_mutate_base(self):
        base = {"a": {"x": 1}}
        deep_merge(base, {"a": {"y": 2}})
        assert base == {"a": {"x": 1}}


class TestSafeGet:
    def test_nested_key(self):
        assert safe_get({"a": {"b": 42}}, "a", "b") == 42

    def test_missing_key_returns_default(self):
        assert safe_get({}, "a", "b", default=0) == 0

    def test_non_dict_intermediate(self):
        assert safe_get({"a": "not_a_dict"}, "a", "b") is None

    def test_none_default(self):
        assert safe_get({"a": 1}, "z") is None


class TestFlattenDict:
    def test_nested(self):
        assert flatten_dict({"a": {"b": 1, "c": 2}}) == {"a.b": 1, "a.c": 2}

    def test_flat_dict_unchanged(self):
        assert flatten_dict({"a": 1, "b": 2}) == {"a": 1, "b": 2}

    def test_custom_separator(self):
        result = flatten_dict({"a": {"b": 1}}, separator="/")
        assert result == {"a/b": 1}

    def test_deeply_nested(self):
        result = flatten_dict({"a": {"b": {"c": 3}}})
        assert result == {"a.b.c": 3}


class TestPick:
    def test_pick_existing_keys(self):
        assert pick({"a": 1, "b": 2, "c": 3}, "a", "c") == {"a": 1, "c": 3}

    def test_pick_missing_keys_ignored(self):
        assert pick({"a": 1}, "a", "z") == {"a": 1}

    def test_pick_empty(self):
        assert pick({"a": 1}, "z") == {}


class TestOmit:
    def test_omit_key(self):
        assert omit({"a": 1, "b": 2, "c": 3}, "b") == {"a": 1, "c": 3}

    def test_omit_missing_key_no_error(self):
        assert omit({"a": 1}, "z") == {"a": 1}

    def test_omit_multiple(self):
        assert omit({"a": 1, "b": 2, "c": 3}, "a", "c") == {"b": 2}
