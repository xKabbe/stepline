"""Tests for the generic assertions that work for every value."""

from stepline.assertions._object_assert import ObjectAssert


def test_assertion_keeps_actual_value_and_description() -> None:
    """The assertion keeps the checked value and the description for its checks."""
    actual = 404
    description = "status code"
    assert_instance = ObjectAssert(actual=actual, description=description)

    assert assert_instance._actual == actual  # pyright: ignore[reportPrivateUsage]
    assert assert_instance._description == description  # pyright: ignore[reportPrivateUsage]


def test_assertion_has_no_description_by_default() -> None:
    """The description is `None` if none is given."""
    actual = 404
    assert_instance = ObjectAssert(actual=actual)

    assert assert_instance._actual == actual  # pyright: ignore[reportPrivateUsage]
    assert assert_instance._description is None  # pyright: ignore[reportPrivateUsage]
