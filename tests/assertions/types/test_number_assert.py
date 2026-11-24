"""Tests for the assertions for numbers."""

from stepline.assertions._object_assert import ObjectAssert
from stepline.assertions._types._number_assert import NumberAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on numbers."""
    assert issubclass(NumberAssert, ObjectAssert)
