"""Smoke tests that verify the installed package works at a basic level."""

import stepline


def test_package_is_importable() -> None:
    """The stepline package can be imported."""
    assert stepline.__name__ == "stepline"


def test_version_is_available() -> None:
    """The package exposes its version from the installed metadata."""
    assert isinstance(stepline.__version__, str)
    assert stepline.__version__, "stepline has no version - is the package installed (uv sync)?"
