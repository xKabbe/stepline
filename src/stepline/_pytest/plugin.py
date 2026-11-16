"""pytest plugin that integrates stepline into every test run."""

import platform

import pytest

import stepline


def pytest_report_header(config: pytest.Config) -> str:
    """
    Add the stepline header line to the start of a test run.

    Args:
        config: The pytest configuration object.

    Returns:
        The header line shown below pytest's own session information.
    """
    return f"├─ stepline {stepline.__version__} · Python {platform.python_version()} · pytest {pytest.__version__}"
