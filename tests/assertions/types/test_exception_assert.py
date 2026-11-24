"""Tests for the assertions for exceptions."""

from stepline.assertions._object_assert import ObjectAssert
from stepline.assertions._types._exception_assert import ExceptionAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on exceptions."""
    assert issubclass(ExceptionAssert, ObjectAssert)
