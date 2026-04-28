"""Tests for utils.string_utils."""
from utils.string_utils import (
    slugify, truncate, camel_to_snake,
    snake_to_camel, indent, remove_prefix, remove_suffix,
)


def test_slugify_basic():
    assert slugify("Hello World!") == "hello-world"


def test_slugify_unicode():
    result = slugify("Ångström")
    assert result == "angstrom"


def test_slugify_custom_separator():
    assert slugify("Hello World", separator="_") == "hello_world"


def test_truncate_short():
    assert truncate("Hi", 10) == "Hi"


def test_truncate_long():
    assert truncate("Hello World", 8) == "Hello..."


def test_camel_to_snake():
    assert camel_to_snake("camelCase") == "camel_case"
    assert camel_to_snake("HTTPSRequest") == "https_request"


def test_snake_to_camel():
    assert snake_to_camel("hello_world") == "helloWorld"


def test_indent():
    result = indent("line1\nline2", spaces=2)
    assert result == "  line1\n  line2"


def test_remove_prefix():
    assert remove_prefix("foobar", "foo") == "bar"
    assert remove_prefix("foobar", "baz") == "foobar"


def test_remove_suffix():
    assert remove_suffix("foobar", "bar") == "foo"
    assert remove_suffix("foobar", "baz") == "foobar"
