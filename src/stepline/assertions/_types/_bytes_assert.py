"""Assertions for bytes."""

from stepline.assertions._object_assert import ObjectAssert


class BytesAssert(ObjectAssert[bytes | bytearray]):
    """Assertions for `bytes` and `bytearray` values."""

    # TODO: Extend class-docstring with the list of checks and examples
