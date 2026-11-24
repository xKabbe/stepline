"""Tests for the assertions for callables."""

from stepline.assertions import CallableAssert, ObjectAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on callables."""
    assert issubclass(CallableAssert, ObjectAssert)
