"""Turns a failure into a plain-text message of a failed check."""

from stepline._core.failure import Failure, NotSet

_LABEL_GAP = 2


def format_failure(failure: Failure) -> str:
    """
    Build the message for a failed check.

    The first line describes the check and stands on its own, as pytest shows only this line in its short test summary.
    If the check has an expected value, a tree below it compares the expected value with the found one.

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
    headline = f"{prefix}expected {failure.actual!r} {failure.check}"

    if failure.expected is NotSet.NOT_SET:
        return headline

    found = failure.actual if failure.found is NotSet.NOT_SET else failure.found
    expected_label = "expected not" if failure.negated else "expected"
    actual_label = "actual"
    width = max(len(expected_label), len(actual_label)) + _LABEL_GAP

    return (
        f"{headline} {failure.expected!r}\n"
        f"├─ {expected_label:<{width}} {failure.expected!r}\n"
        f"╰─ {actual_label:<{width}} {found!r}"
    )
