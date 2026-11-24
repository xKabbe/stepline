"""Tests for the assertions for collections."""

from stepline.assertions._object_assert import ObjectAssert
from stepline.assertions._types._collection_assert import CollectionAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on collections."""
    assert issubclass(CollectionAssert, ObjectAssert)
