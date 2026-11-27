"""The error raised when a single check fails."""

from stepline._core.failure import Failure, NotSet


class AssertionFailedError(AssertionError):
    """
    Raised when a check fails.

    It is an `AssertionError`, so pytest and other tools treat it as a normal test failure.
    The failure object describes what was checked, what was found and what was expected.

    Args:
        failure: The failure that describes the failed check.

    Attributes:
        failure: The failure that describes the failed check.
    """

    __module__ = "stepline.errors"

    def __init__(self, failure: Failure) -> None:
        super().__init__(failure)
        self.failure = failure

    def __str__(self) -> str:
        """
        Build the failure message from the failure.

        Returns:
            The string representation of the failure.
        """
        message = f"expected {self.failure.actual!r} {self.failure.check}"
        return message if self.failure.expected is NotSet.NOT_SET else f"{message} {self.failure.expected!r}"
