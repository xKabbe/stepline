"""Tests for the assertions for `bytes` and `bytearray` values."""

from stepline.assertions._object_assert import ObjectAssert
from stepline.assertions._types._bytes_assert import BytesAssert


def test_assert_class_is_an_object_assert() -> None:
    """The assertion is an `ObjectAssert`, so all generic checks work on `bytes` and `bytearray` values."""
    assert issubclass(BytesAssert, ObjectAssert)
