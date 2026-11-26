"""Tests for the assertions for paths."""

from stepline.assertions import ObjectAssert, PathAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on paths."""
    assert issubclass(PathAssert, ObjectAssert)
