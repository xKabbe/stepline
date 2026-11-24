"""Tests for the assertions for dates and datetimes."""

from stepline.assertions._object_assert import ObjectAssert
from stepline.assertions._types._date_assert import DateAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on dates and datetimes."""
    assert issubclass(DateAssert, ObjectAssert)
