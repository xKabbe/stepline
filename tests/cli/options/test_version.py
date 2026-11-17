"""Tests for the `stepline --version` option."""

import platform
from importlib.metadata import metadata, version

import pytest
from typer.testing import CliRunner

import stepline
from stepline._cli.app import app
from stepline._render.banner import SLOGAN

runner = CliRunner()


@pytest.mark.parametrize("option", ["--version", "-V"])
def test_version_option_shows_banner_and_exits(option: str) -> None:
    """
    The long and short version option show the stepline banner and exit successfully.

    Args:
        option: The version option given on the command line, either `--version` or `-v`.
    """
    result = runner.invoke(app, [option])
    assert result.exit_code == 0
    assert f"by {metadata('stepline').get('author', '-')}" in result.output
    assert stepline.__version__ in result.output
    assert platform.python_version() in result.output
    assert version("pytest") in result.output
    assert f"{platform.system()} {platform.release()} · {platform.machine()}" in result.output
    assert "--version" in result.output
    assert SLOGAN in result.output
