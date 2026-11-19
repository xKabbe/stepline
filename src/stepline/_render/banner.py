"""The stepline banner shown by standalone commands such as `stepline --version`."""

import platform
from importlib.metadata import PackageNotFoundError, metadata, version

from rich import box
from rich.console import Console, Group
from rich.measure import Measurement
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

import stepline

LOGO_LINES = (
    r"         __             ___",
    r"   _____/ /____  ____  / (_)___  ___",
    r"  / ___/ __/ _ \/ __ \/ / / __ \/ _ \ ",
    r" (__  ) /_/  __/ /_/ / / / / / /  __/",
    r"/____/\__/\___/ .___/_/_/_/ /_/\___/",
    r"             /_/",
)
SLOGAN = "Step by step. Line by line."

GRADIENT_START = (34, 211, 238)
GRADIENT_END = (139, 92, 246)

PANEL_PADDING = (1, 2)
PANEL_CHROME = 2 + 2 * PANEL_PADDING[1]
MEASURE_WIDTH = 1_000


def render_banner(console: Console, command: str) -> None:
    """
    Render the stepline banner for a specific command in the console.

    The banner uses the widest of the following layouts that fits into the console:

    - Logo and table with information displayed side by side
    - Logo and table with information displayed on top of each other
    - Only a short statement with the stepline version, if neither layout fits

    Args:
        console: The rich console to print to.
        command: The command that shows the banner, e.g. "--version".
    """
    logo, info = _gradient_logo(), _info_table(command=command)

    side_by_side = Table.grid(padding=(0, 4))
    side_by_side.add_column()
    side_by_side.add_column(vertical="middle")
    side_by_side.add_row(logo, info)

    stacked = Group(logo, Text(), info)

    measure_options = console.options.update_width(MEASURE_WIDTH)
    content = next(
        (
            layout
            for layout in (side_by_side, stacked)
            if Measurement.get(console, measure_options, layout).maximum + PANEL_CHROME <= console.width
        ),
        None,
    )

    if content is None:
        console.print(f"stepline {stepline.__version__} · {command}")
        return

    console.print(
        Panel(
            content,
            box=box.ROUNDED,
            border_style="grey42",
            title=f"[dim]by {metadata('pytest-stepline').get('author')}[/]",
            title_align="left",
            subtitle=f"[italic dim]{SLOGAN}[/]",
            subtitle_align="right",
            padding=PANEL_PADDING,
            expand=False,
        )
    )


def _gradient_logo() -> Text:
    """
    Build the stepline logo with a horizontal color gradient.

    Returns:
        The colored logo as rich text.
    """
    width = max(len(line) for line in LOGO_LINES)
    logo = Text()

    for line in LOGO_LINES:
        for column, char in enumerate(line):
            share = column / (width - 1)
            red, green, blue = (
                round(start + (end - start) * share) for start, end in zip(GRADIENT_START, GRADIENT_END, strict=True)
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
        The version string, or "not installed".
    """
    try:
        return version("pytest")
    except PackageNotFoundError:
        return "not installed"
