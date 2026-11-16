"""The `--version` option of the stepline command-line tool."""

import typer
from rich.console import Console

from stepline._render.banner import render_banner


def version_option(value: bool) -> None:
    """
    Show the stepline banner and exit when `--version` is given.

    Typer calls this function for every run, because the option is eager.
    It only acts when the `--version` option was actually given.

    Args:
        value: Whether `--version` or `-V` was given on the command line.

    Raises:
        typer.Exit: After showing the banner, to end the program.
    """
    if value:
        render_banner(console=Console(), command="--version")
        raise typer.Exit
