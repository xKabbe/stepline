"""Tests for the generic assertions that work for every value."""

from collections.abc import Callable, Collection, Mapping
from datetime import date, datetime

import pytest

from stepline.assertions import ObjectAssert
from stepline.errors import AssertionFailedError

EQUAL_VALUES = [
    pytest.param(3, 3, id="equal-ints"),
    pytest.param(1, 1.0, id="int-and-float"),
    pytest.param("text", "text", id="equal-strings"),
    pytest.param([1, 2], [1, 2], id="equal-lists"),
    pytest.param({"key": "value"}, {"key": "value"}, id="equal-dicts"),
    pytest.param(None, None, id="none"),
]
DIFFERENT_VALUES = [
    pytest.param(1, 2, id="different-ints"),
    pytest.param(6, "6", id="int-and-str"),
    pytest.param("Help", "help", id="different-case"),
    pytest.param([4, 5], [5, 4], id="different-order"),
    pytest.param(None, 0, id="none-and-zero"),
]

SAME_OBJECTS = [
    pytest.param(0, id="int"),
    pytest.param("hurra", id="string"),
    pytest.param(True, id="bool"),
    pytest.param([7, 8, 9], id="list"),
    pytest.param(None, id="none"),
    pytest.param(object(), id="object"),
]
SEPARATE_OBJECTS = [
    pytest.param([5, 2], [5, 2], id="separate-equal-lists"),
    pytest.param({"foo": "bar"}, {"foo": "bar"}, id="separate-equal-dicts"),
    pytest.param(object(), object(), id="separate-objects"),
]

NONE_VALUES = [pytest.param(None, id="none")]
OTHER_VALUES = [
    pytest.param(0, id="zero"),
    pytest.param(5, id="int"),
    pytest.param("", id="empty-string"),
    pytest.param("hello", id="string"),
    pytest.param(False, id="false"),
    pytest.param([], id="empty-list"),
    pytest.param(object(), id="object"),
]

INSTANCES_OF_THE_TYPE = [
    pytest.param({}, dict, id="dict-is-dict"),
    pytest.param({}, Mapping, id="dict-is-mapping"),
    pytest.param([1], list, id="list-is-list"),
    pytest.param([1], Collection, id="list-is-collection"),
    pytest.param(True, bool, id="bool-is-bool"),
    pytest.param(True, int, id="bool-is-int"),
    pytest.param(2.2, float, id="float-is-float"),
    pytest.param(datetime(2026, 1, 1, 1), datetime, id="datetime-is-datetime"),
    pytest.param(datetime(2026, 1, 1, 1), date, id="datetime-is-date"),
    pytest.param(ValueError("ohhh"), BaseException, id="value-error-is-base-exception"),
    pytest.param(len, Callable, id="function-is-callable"),
    pytest.param(None, object, id="none-is-object"),
]
INSTANCES_OF_OTHER_TYPES = [
    pytest.param(1, bool, id="int-is-not-bool"),
    pytest.param(1, float, id="int-is-not-float"),
    pytest.param("text", bytes, id="string-is-not-bytes"),
    pytest.param(date(2026, 1, 1), datetime, id="date-is-not-datetime"),
]


@pytest.mark.parametrize(("actual", "expected"), EQUAL_VALUES)
def test_assertion_is_equal_to_passes_for_equal_values(actual: object, expected: object) -> None:
    """
    The check passes if the value is equal to the expected value, even if it is a different object or type.

    Args:
        actual: The value to check.
        expected: A value that is equal to the checked value.
    """
    ObjectAssert(actual).is_equal_to(expected)


@pytest.mark.parametrize(("actual", "expected"), DIFFERENT_VALUES)
def test_assertion_is_equal_to_fails_for_different_values(actual: object, expected: object) -> None:
    """
    The check fails with the expected value if the value is not equal to it.

    Args:
        actual: The value to check.
        expected: A value that is not equal to the checked value.
    """
    with pytest.raises(AssertionFailedError) as error_info:
        ObjectAssert(actual).is_equal_to(expected)

    assert error_info.value.failure.check == "to be equal to"
    assert error_info.value.failure.expected == expected


@pytest.mark.parametrize(("actual", "expected"), DIFFERENT_VALUES)
def test_assertion_is_not_equal_to_passes_for_different_values(actual: object, expected: object) -> None:
    """
    The check passes if the value is not equal to the given value.

    Args:
        actual: The value to check.
        expected: A value that is not equal to the checked value.
    """
    ObjectAssert(actual).is_not_equal_to(expected)


@pytest.mark.parametrize(("actual", "expected"), EQUAL_VALUES)
def test_assertion_is_not_equal_to_fails_for_equal_values(actual: object, expected: object) -> None:
    """
    The check fails with the given value if the value is equal to it, even if it is a different object or type.

    Args:
        actual: The value to check.
        expected: A value that is equal to the checked value.
    """
    with pytest.raises(AssertionFailedError) as error_info:
        ObjectAssert(actual).is_not_equal_to(expected)

    assert error_info.value.failure.check == "not to be equal to"
    assert error_info.value.failure.expected == expected


@pytest.mark.parametrize("actual", SAME_OBJECTS)
def test_assertion_is_same_as_passes_for_the_same_object(actual: object) -> None:
    """
    The check passes if the value is the given object itself.

    Args:
        actual: The object to check, also given as the expected object.
    """
    ObjectAssert(actual).is_same_as(actual)


@pytest.mark.parametrize(("actual", "expected"), SEPARATE_OBJECTS)
def test_assertion_is_same_as_fails_for_a_different_object(actual: object, expected: object) -> None:
    """
    The check fails with the expected object if the value is a separate object, even if it is equal.

    Args:
        actual: The object to check.
        expected: A separate object, equal to the checked object or not.
    """
    with pytest.raises(AssertionFailedError) as error_info:
        ObjectAssert(actual).is_same_as(expected)

    assert error_info.value.failure.check == "to be the same object as"
    assert error_info.value.failure.expected is expected


@pytest.mark.parametrize(("actual", "expected"), SEPARATE_OBJECTS)
def test_assertion_is_not_same_as_passes_for_a_different_object(actual: object, expected: object) -> None:
    """
    The check passes if the value is a separate object, even if it is equal.

    Args:
        actual: The object to check.
        expected: A separate object, equal to the checked object or not.
    """
    ObjectAssert(actual).is_not_same_as(expected)


@pytest.mark.parametrize("actual", SAME_OBJECTS)
def test_assertion_is_not_same_as_fails_for_the_same_object(actual: object) -> None:
    """
    The check fails with the given object if the value is that object itself.

    Args:
        actual: The object to check, also given as the object it must not be.
    """
    with pytest.raises(AssertionFailedError) as error_info:
        ObjectAssert(actual).is_not_same_as(actual)

    assert error_info.value.failure.check == "not to be the same object as"
    assert error_info.value.failure.expected is actual


@pytest.mark.parametrize("actual", NONE_VALUES)
def test_assertion_is_none_passes_for_none(actual: object) -> None:
    """
    The check passes if the value is `None`.

    Args:
        actual: `None` as the value to check.
    """
    ObjectAssert(actual).is_none()


@pytest.mark.parametrize("actual", OTHER_VALUES)
def test_assertion_is_none_fails_for_any_other_value(actual: object) -> None:
    """
    The check fails with `None` as expected value for any other value, even a falsy one.

    Args:
        actual: A value other than `None`, including falsy values like `0` or `""`.
    """
    with pytest.raises(AssertionFailedError) as error_info:
        ObjectAssert(actual).is_none()

    assert error_info.value.failure.check == "to be"
    assert error_info.value.failure.expected is None


@pytest.mark.parametrize("actual", OTHER_VALUES)
def test_assertion_is_not_none_passes_for_any_other_value(actual: object) -> None:
    """
    The check passes for any value except `None`, even a falsy one.

    Args:
        actual: A value other than `None`, including falsy values like `0` or `""`.
    """
    ObjectAssert(actual).is_not_none()


@pytest.mark.parametrize("actual", NONE_VALUES)
def test_assertion_is_not_none_fails_for_none(actual: object) -> None:
    """
    The check fails with `None` as expected value if the value is `None`.

    Args:
        actual: `None` as the value to check.
    """
    with pytest.raises(AssertionFailedError) as error_info:
        ObjectAssert(actual).is_not_none()

    assert error_info.value.failure.check == "not to be"
    assert error_info.value.failure.expected is None


@pytest.mark.parametrize(("actual", "expected_type"), INSTANCES_OF_THE_TYPE)
def test_assertion_is_instance_of_passes_for_instances_of_the_type(actual: object, expected_type: type[object]) -> None:
    """
    The check passes for instances of the type, of its subclasses and of registered abstract base classes.

    Args:
        actual: The value to check.
        expected_type: A type that the checked value is an instance of.
    """
    ObjectAssert(actual).is_instance_of(expected_type)


@pytest.mark.parametrize(("actual", "expected_type"), INSTANCES_OF_OTHER_TYPES)
def test_assertion_is_instance_of_fails_for_instances_of_other_types(
    actual: object, expected_type: type[object]
) -> None:
    """
    The check fails with the expected type if the value is not an instance of it.

    Args:
        actual: The value to check.
        expected_type: A type that the checked value is not an instance of.
    """
    with pytest.raises(AssertionFailedError) as error_info:
        ObjectAssert(actual).is_instance_of(expected_type)

    assert error_info.value.failure.check == "to be an instance of"
    assert error_info.value.failure.expected is expected_type


@pytest.mark.parametrize(("actual", "expected_type"), INSTANCES_OF_OTHER_TYPES)
def test_assertion_is_not_instance_of_passes_for_instances_of_other_types(
    actual: object, expected_type: type[object]
) -> None:
    """
    The check passes if the value is not an instance of the given type.

    Args:
        actual: The value to check.
        expected_type: A type that the checked value is not an instance of.
    """
    ObjectAssert(actual).is_not_instance_of(expected_type)


@pytest.mark.parametrize(("actual", "expected_type"), INSTANCES_OF_THE_TYPE)
def test_assertion_is_not_instance_of_fails_for_instances_of_the_type(
    actual: object, expected_type: type[object]
) -> None:
    """
    The check fails with the given type if the value is an instance of it or of one of its subclasses.

    Args:
        actual: The value to check.
        expected_type: A type that the checked value is an instance of.
    """
    with pytest.raises(AssertionFailedError) as error_info:
        ObjectAssert(actual).is_not_instance_of(expected_type)

    assert error_info.value.failure.check == "not to be an instance of"
    assert error_info.value.failure.expected is expected_type


def test_assertion_returns_itself_for_chaining() -> None:
    """Every check returns the assertion itself, so that checks can be chained."""
    status_code = 404
    assertion = ObjectAssert(status_code)
    none_assertion = ObjectAssert(None)

    assert assertion.is_equal_to(status_code) is assertion
    assert assertion.is_not_equal_to(200) is assertion
    assert assertion.is_same_as(status_code) is assertion
    assert assertion.is_not_same_as(object()) is assertion
    assert none_assertion.is_none() is none_assertion
    assert assertion.is_not_none() is assertion
    assert assertion.is_instance_of(int) is assertion
    assert assertion.is_not_instance_of(str) is assertion
    assert assertion.is_not_none().is_equal_to(status_code).is_instance_of(int) is assertion


def test_assertion_failure_holds_the_actual_value_and_description() -> None:
    """A failed check passes the checked value and the description to the failure."""
    status_code = 404
    description = "status code"
    with pytest.raises(AssertionFailedError) as error_info:
        ObjectAssert(status_code, description).is_equal_to(200)

    assert error_info.value.failure.actual == status_code
    assert error_info.value.failure.description == description


def test_assertion_failure_has_no_description_by_default() -> None:
    """A failed check without a description gives `None` as description to the failure."""
    status_code = 404
    with pytest.raises(AssertionFailedError) as error_info:
        ObjectAssert(status_code).is_equal_to(200)

    assert error_info.value.failure.actual == status_code
    assert error_info.value.failure.description is None
