"""Tests for the assertions for paths."""

from stepline.assertions._object_assert import ObjectAssert
from stepline.assertions._types._path_assert import PathAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on paths."""
    assert issubclass(PathAssert, ObjectAssert)
