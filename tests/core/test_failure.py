"""Tests for the failure object that describes a failed check."""

from dataclasses import FrozenInstanceError

import pytest

from stepline._core.failure import Failure, NotSet


def test_failure_holds_all_given_fields() -> None:
    """A failure keeps the check, the actual and expected value, and the description."""
    check = "to be equal to"
    actual, expected = 404, 200
    description = "status code"

    failure = Failure(check=check, actual=actual, expected=expected, description=description)

    assert failure.check == check
    assert failure.actual == actual
    assert failure.expected == expected
    assert failure.description == description


def test_failure_defaults_to_no_expected_value_and_no_description() -> None:
    """A failure created without expected value and description uses the defaults."""
    check = "to be positive"
    actual = -2

    failure = Failure(check=check, actual=actual)

    assert failure.check == check
    assert failure.actual == actual
    assert failure.expected is NotSet.NOT_SET
    assert failure.description is None


def test_failure_distinguishes_expected_none_from_no_expected_value() -> None:
    """An expected `None` is a real expected value and not the same as no expected value."""
    failure_with_none = Failure(check="to be none", actual="error", expected=None)
    failure_without_expected = Failure(check="to be positive", actual=-1)

    assert failure_with_none.expected is None
    assert failure_with_none.expected is not NotSet.NOT_SET
    assert failure_without_expected.expected is NotSet.NOT_SET


def test_failure_cannot_be_changed_after_creation() -> None:
    """A failure is immutable, so its fields cannot be changed after it was created."""
    check = "to be equal to"
    actual, expected = 404, 200
    description = "status code"

    failure = Failure(check=check, actual=actual, expected=expected, description=description)

    with pytest.raises(FrozenInstanceError):
        # noinspection PyDataclass
        failure.actual = 3000  # pyright: ignore[reportAttributeAccessIssue]

    assert failure.actual == actual


def test_failure_accepts_only_keyword_arguments() -> None:
    """A failure can only be created with keyword arguments, so fields cannot be mixed up."""
    check = "to be equal to"
    actual, expected = 404, 200
    description = "status code"

    with pytest.raises(TypeError, match="positional argument"):
        # noinspection PyArgumentList
        Failure(check, actual, expected, description)  # pyright: ignore[reportCallIssue]
