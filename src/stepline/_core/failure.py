"""The failure object that describes a failed check."""

from dataclasses import dataclass
from enum import Enum, auto


class NotSet(Enum):
    """Marks that a check has no expected value, as opposed to an expected `None`."""

    NOT_SET = auto()


@dataclass(frozen=True, kw_only=True, slots=True)
class Failure:
    """
    Describes a failed check: what was checked, what was found and what was expected.

    Assertions create a failure, failure messages render it, and later steps and the console output display it. The
    object only holds data and knows nothing about formatting.
    It is immutable, but the values it holds may still be mutable objects.

    Attributes:
        check: The check as a readable phrase, e.g. "to be equal to".
        actual: The value that was checked.
        expected: The expected value, or `NotSet.NOT_SET` if the check has none. `None` is a valid expected value, e.g.
            for `is_none()`.
        description: The description given to `assert_that`, or `None`.
    """

    check: str
    actual: object
    expected: object = NotSet.NOT_SET
    description: str | None = None
