"""Tests for the assertions for strings."""

from stepline.assertions._object_assert import ObjectAssert
from stepline.assertions._types._string_assert import StringAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on strings."""
    assert issubclass(StringAssert, ObjectAssert)
