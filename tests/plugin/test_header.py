"""Tests for the stepline header line in a pytest run."""

import pytest


def test_header_line_is_shown(pytester: pytest.Pytester) -> None:
    """
    A test run shows the stepline header line with versions.

    Args:
        pytester: The pytest pytester object to run pytest in isolation/temp directory.
    """
    pytester.makepyfile("def test_foo() -> None:\n  pass\n")

    result = pytester.runpytest()
    result.stdout.fnmatch_lines(["├─ stepline * · Python * · pytest *"])
    result.assert_outcomes(passed=1)


def test_plugin_can_be_disabled(pytester: pytest.Pytester) -> None:
    """
    The plugin can be switched off with `-p no:stepline`.

    Args:
        pytester: The pytest pytester object to run pytest in isolation/temp directory.
    """
    pytester.makepyfile("def test_foo() -> None:\n  pass\n")

    result = pytester.runpytest("-p", "no:stepline")
    result.stdout.no_fnmatch_line("├─ stepline *")
    result.assert_outcomes(passed=1)
