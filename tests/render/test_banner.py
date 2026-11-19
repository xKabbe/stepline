"""Tests for the stepline banner shown by standalone commands such as `stepline --version`."""

import io
from importlib.metadata import PackageNotFoundError, metadata

import pytest
from rich.console import Console

import stepline
from stepline._render.banner import LOGO_LINES, SLOGAN, render_banner


def test_banner_shows_logo_next_to_info_on_wide_console() -> None:
    """A wide console shows the banner with the logo and the info table side by side."""
    text = _render(width=120)
    logo_indices = _logo_indices(text=text)
    stepline_version_index = _stepline_version_index(text=text)

    assert f"by {metadata('pytest-stepline').get('author', '-')}" in text
    assert SLOGAN in text
    assert logo_indices
    assert stepline_version_index in logo_indices


def test_banner_shows_logo_above_info_on_medium_console() -> None:
    """A medium console shows the banner with the logo on top of the info table."""
    text = _render(width=60)
    logo_indices = _logo_indices(text=text)
    stepline_version_index = _stepline_version_index(text=text)

    assert f"by {metadata('pytest-stepline').get('author', '-')}" in text
    assert SLOGAN in text
    assert logo_indices
    assert stepline_version_index > max(logo_indices)


def test_banner_shows_single_line_on_narrow_console() -> None:
    """A narrow console shows only a single line with the stepline version and the command."""
    text = _render(width=40)
    assert f"stepline {stepline.__version__} · --version" == text.strip()


def test_banner_shows_pytest_as_not_installed_if_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    The banner shows pytest as "not installed" if pytest cannot be found.

    Args:
        monkeypatch: The pytest monkeypatch fixture to replace the version lookup.
    """

    def _raise_package_not_found(name: str) -> None:
        raise PackageNotFoundError(name)

    monkeypatch.setattr("stepline._render.banner.version", _raise_package_not_found)

    text = _render(width=120)
    assert "pytest not installed" in text


def _render(width: int) -> str:
    """
    Render the banner for `--version` into a console with a fixed width.

    Args:
        width: The width of the console in terminal cells.

    Returns:
        The rendered banner as plain text without colors.
    """
    output = io.StringIO()
    console = Console(file=output, width=width, color_system=None)

    render_banner(console=console, command="--version")
    return output.getvalue()


def _logo_indices(text: str) -> list[int]:
    """
    Find all lines of the rendered banner that contain a part of the logo.

    Args:
        text: The rendered banner.

    Returns:
        The indices of all lines with a part of the logo, empty if the logo is not shown.
    """
    return [i for i, line in enumerate(text.splitlines()) if any(part.strip() in line for part in LOGO_LINES)]


def _stepline_version_index(text: str) -> int:
    """
    Find the line of the rendered banner that contains the stepline version entry of the info table.

    Args:
        text: The rendered banner.

    Returns:
        The index of the line with the version entry.
    """
    return next(i for i, line in enumerate(text.splitlines()) if f"version {stepline.__version__}" in line)
