"""Tests for the assertions for callables."""

from stepline.assertions._object_assert import ObjectAssert
from stepline.assertions._types._callable_assert import CallableAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on callables."""
    assert issubclass(CallableAssert, ObjectAssert)
