"""Tests for the stepline command-line tool."""

import sys

import click
import pytest
from typer.testing import CliRunner

from stepline._cli.app import app, main

runner = CliRunner()


def test_main_rund_the_app(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    """
    The entry point of the `stepline` command runs the command-line tool with the given arguments.

    Args:
        monkeypatch: The pytest monkeypatch fixture to set the command-line arguments.
        capsys: The pytest capsys fixture to capture the terminal output.
    """
    monkeypatch.setattr(sys, "argv", ["stepline", "--help"])

    with pytest.raises(SystemExit) as error_info:
        main()
    output = click.unstyle(capsys.readouterr().out)

    assert error_info.value.code == 0
    assert "Usage:" in output
    assert app.info.help is not None
    assert app.info.help in output


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
    output = click.unstyle(result.output)

    assert result.exit_code == 0
    assert "Usage:" in output
    assert app.info.help is not None
    assert app.info.help in output
    assert "Options" in output
    assert option in output
    assert short_option in output
    assert help_text in output


def test_app_shows_help_without_arguments() -> None:
    """Calling the stepline command-line tool without arguments show the help output."""
    result = runner.invoke(app, [])
    output = click.unstyle(result.output)

    assert result.exit_code == 2
    assert "Usage:" in output
    assert app.info.help is not None
    assert app.info.help in output
    assert "Options" in output
