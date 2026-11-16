"""The stepline banner shown by standalone commands such as `stepline --version`."""

import platform
from importlib.metadata import PackageNotFoundError, metadata, version

from rich import box
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

import stepline


def render_banner(console: Console, command: str) -> None:
    """
    Render the stepline banner for a specific command in the console.

    Depending on the width of the terminal this banner will be shown in one of the following formats:

    - Logo and table with information will be displayed side by side (large width)
    - Logo and table with information will be displayed on top of each other (medium width)
    - Only a short statement with the stepline version will be printed (small width)

    Args:
        console: The rich console to print to.
        command: The command that shows the banner, e.g. "--version".
    """
    min_width_side_by_side = 85
    min_width_banner = 60

    if console.width < min_width_banner:
        # Only print the information without a logo if terminal width is too small
        console.print(f"stepline {stepline.__version__} · {command}")
        return

    logo, info = _gradient_logo(), _info_table(command=command)
    if console.width >= min_width_side_by_side:
        # Panel content for a larger width to display the logo and table side by side
        grid = Table.grid(padding=(0, 4))
        grid.add_column()
        grid.add_column(vertical="middle")
        grid.add_row(logo, info)

        content = grid
    else:
        # Panel content for a smaller width to display the logo on top of the table
        content = Group(logo, Text(), info)

    unicode_ok = console.encoding.lower().startswith("utf")

    console.print(
        Panel(
            content,
            box=box.ROUNDED if unicode_ok else box.ASCII,
            border_style="grey42",
            title=f"[dim]by {metadata('stepline').get('author')}[/]",
            title_align="left",
            subtitle="[italic dim]Step by step. Line by line.[/]",
            subtitle_align="right",
            padding=(1, 2),
            expand=False,
        )
    )


def _gradient_logo() -> Text:
    """
    Build the stepline logo with a horizontal color gradient.

    Returns:
        The colored logo as rich text.
    """
    logo_lines = (
        r"         __             ___",
        r"   _____/ /____  ____  / (_)___  ___",
        r"  / ___/ __/ _ \/ __ \/ / / __ \/ _ \ ",
        r" (__  ) /_/  __/ /_/ / / / / / /  __/",
        r"/____/\__/\___/ .___/_/_/_/ /_/\___/",
        r"             /_/",
    )
    gradient_start = (34, 211, 238)
    gradient_end = (139, 92, 246)

    width = max(len(line) for line in logo_lines)
    logo = Text()

    for line in logo_lines:
        for column, char in enumerate(line):
            share = column / (width - 1)
            red, green, blue = (
                round(start + (end - start) * share) for start, end in zip(gradient_start, gradient_end, strict=True)
            )

            logo.append(char, style=f"bold rgb({red},{green},{blue})")
        logo.append("\n")
    logo.rstrip()

    return logo


def _info_table(command: str) -> Table:
    """
    Build the info table column next to the logo.

    Args:
        command: The command that shows the banner, e.g. "--version".

    Returns:
        A two-column table with labels and values.
    """
    table = Table.grid(padding=(0, 1))
    table.add_column(style="dim", justify="right")
    table.add_column()
    table.add_row("version", f"[bold cyan]{stepline.__version__}[/]")
    table.add_row("python", platform.python_version())
    table.add_row("pytest", _get_pytest_version())
    table.add_row("platform", f"{platform.system()} {platform.release()} · {platform.machine()}")
    table.add_row("command", command)
    return table


def _get_pytest_version() -> str:
    """
    Return the installed version of pytest.

    Returns:
        The version string, or "not installed"
    """
    try:
        return version("pytest")
    except PackageNotFoundError:
        return "not installed"
