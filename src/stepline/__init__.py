"""Structured pytest tests with steps, typed assertions, and test documentation."""

from importlib.metadata import version

from stepline.assertions._assert_that import assert_that

__version__ = version("pytest-stepline")
__all__ = ["__version__", "assert_that"]
