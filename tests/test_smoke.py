"""Smoke tests that verify the package can be imported."""

import stepline


def test_package_is_importable() -> None:
    assert stepline.__name__ == "stepline"
