"""Turns a failure into a plain-text message of a failed check."""

import reprlib

from stepline._core.failure import Failure, NotSet

_LABEL_GAP = 2

_HEADLINE_REPR = reprlib.Repr(
    maxlevel=2,
    maxstring=40,
    maxother=40,
    maxlist=6,
    maxtuple=6,
    maxset=6,
    maxfrozenset=6,
    maxdeque=6,
    maxdict=6,
)
_TREE_REPR = reprlib.Repr(
    maxlevel=6,
    maxstring=1000,
    maxother=1000,
    maxlist=50,
    maxtuple=50,
    maxset=50,
    maxfrozenset=50,
    maxdeque=50,
    maxdict=50,
)


def format_failure(failure: Failure) -> str:
    """
    Build the message for a failed check.

    The first line describes the check and stands on its own, as pytest shows only this line in its short test summary.
    If the check has an expected value, a tree below it compares the expected value with the found one.

    Values are shown with `repr`, so strings, `None` and numbers stay distinguishable. Long values are shortened: in the
    first line strongly, so that it stays short, and in the tree only if they are very large.

    Examples:
        ```text
        status code: expected 404 to be equal to 200
        ├─ expected  200
        ╰─ actual    404
        ```

    Args:
        failure: The failure that describes the failed check.

    Returns:
        The message, with the tree only if the check has an expected value.
    """
    prefix = f"{failure.description}: " if failure.description else ""
    headline = f"{prefix}expected {_HEADLINE_REPR.repr(failure.actual)} {failure.check}"

    if failure.expected is NotSet.NOT_SET:
        return headline

    found = failure.actual if failure.found is NotSet.NOT_SET else failure.found
    expected_label = "expected not" if failure.negated else "expected"
    actual_label = "actual"
    width = max(len(expected_label), len(actual_label))
    gap = " " * _LABEL_GAP

    return (
        f"{headline} {_HEADLINE_REPR.repr(failure.expected)}\n"
        f"├─ {expected_label:<{width}}{gap}{_TREE_REPR.repr(failure.expected)}\n"
        f"╰─ {actual_label:<{width}}{gap}{_TREE_REPR.repr(found)}"
    )
