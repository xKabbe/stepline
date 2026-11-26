"""Tests for the assertions for numbers."""

from stepline.assertions import NumberAssert, ObjectAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on numbers."""
    assert issubclass(NumberAssert, ObjectAssert)
