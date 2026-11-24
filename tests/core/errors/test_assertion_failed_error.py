"""Tests for the error that stepline raises when a single check fails."""

import pickle

import pytest

from stepline._core.errors.assertion_failed_error import AssertionFailedError
from stepline._core.failure import Failure

FAILURE = Failure(check="to be equal to", actual=404, expected=200, description="status code")


def test_error_is_an_assertion_error() -> None:
    """The error is an `AssertionError`, so pytest and other tools report it as a normal test failure."""
    error = AssertionFailedError(failure=FAILURE)

    assert isinstance(error, AssertionError)


def test_error_holds_the_failure() -> None:
    """The error keeps the given failure object itself, so tools can read the details of the failed check."""
    error = AssertionFailedError(failure=FAILURE)

    assert error.failure is FAILURE


def test_error_message_contains_check_and_values() -> None:
    """The message names the check and shows the actual and the expected value as `repr`."""
    error = AssertionFailedError(failure=FAILURE)
    error_message = str(error)

    assert FAILURE.check in error_message
    assert repr(FAILURE.actual) in error_message
    assert repr(FAILURE.expected) in error_message


def test_error_message_omits_missing_expected_value() -> None:
    """The message end with the check if the check has no expected value."""
    failure_without_expected = Failure(check="to be positive", actual=-2)
    error = AssertionFailedError(failure=failure_without_expected)
    error_message = str(error)

    assert error_message.endswith(failure_without_expected.check)


@pytest.mark.parametrize(
    "expected",
    [
        pytest.param(0, id="zero"),
        pytest.param("", id="empty-string"),
        pytest.param(None, id="none"),
        pytest.param(False, id="false"),
    ],
)
def test_error_message_keeps_falsy_expected_values(expected: object) -> None:
    """
    The message shows an expected value even if it is falsy.

    Args:
        expected: The falsy value, e.g. `0` or `None`.
    """
    failure = Failure(check="to be equal to", actual=404, expected=expected)
    error = AssertionFailedError(failure=failure)

    assert str(error).endswith(f"to be equal to {expected!r}")


def test_error_can_be_pickled() -> None:
    """The error survives pickling, which pytest-xdist needs to send failures from its workers."""
    error = AssertionFailedError(failure=FAILURE)
    restored = pickle.loads(pickle.dumps(error))

    assert isinstance(restored, AssertionFailedError)
    assert restored.failure == FAILURE
