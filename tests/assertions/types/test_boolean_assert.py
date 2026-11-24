"""Tests for the assertions for `bool` values."""

from stepline.assertions._object_assert import ObjectAssert
from stepline.assertions._types._boolean_assert import BooleanAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on `bool` values."""
    assert issubclass(BooleanAssert, ObjectAssert)
