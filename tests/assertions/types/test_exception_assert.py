"""Tests for the assertions for exceptions."""

from stepline.assertions import ExceptionAssert, ObjectAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on exceptions."""
    assert issubclass(ExceptionAssert, ObjectAssert)
