"""The stepline command-line tool."""

from typing import Annotated

import typer

from stepline._cli.options.version import version_option

app = typer.Typer(
    name="stepline",
    help="Step by step. Line by line.",
    no_args_is_help=True,
    add_completion=False,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
    pretty_exceptions_show_locals=False,
)


@app.callback()
def cli(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-V",
            callback=version_option,
            is_eager=True,
            help="Show the stepline banner with version information and exit.",
        ),
    ] = False,
) -> None:
    """
    Step by step. Line by line.

    Args:
        version: Handled by `version_option`, which shows the banner and exits.
        The parameter only exists for that Typer adds the option.
    """


def main() -> None:
    """Run the stepline command-line tool."""
    app()
