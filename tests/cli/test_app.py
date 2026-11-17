"""Tests for the stepline command-line tool."""

import pytest
from typer.testing import CliRunner

from stepline._cli.app import app

runner = CliRunner()


@pytest.mark.parametrize(
    ("option", "short_option", "help_text"),
    [("--help", "-h", "Show this message and exit."), ("--version", "-V", "Show the stepline banner")],
)
def test_app_contains_option(option: str, short_option: str, help_text: str) -> None:
    """
    The stepline `--help` output lists an option together with its short form and help text.

    Args:
        option: The long name of the option, e.g. `--version`.
        short_option: The short name of the option, e.g. `-V`.
        help_text: A part of the help text that is shown for the option.
    """
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Usage: stepline" in result.output
    assert "Options" in result.output
    assert option in result.output
    assert short_option in result.output
    assert help_text in result.output


def test_app_shows_help_without_arguments() -> None:
    """Calling the stepline command-line tool without arguments show the help output."""
    result = runner.invoke(app, [])

    assert result.exit_code == 2
    assert "Usage: stepline" in result.output
    assert "Options" in result.output
