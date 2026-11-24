"""Tests for the assertions for mappings."""

from stepline.assertions._object_assert import ObjectAssert
from stepline.assertions._types._mapping_assert import MappingAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on mappings."""
    assert issubclass(MappingAssert, ObjectAssert)
