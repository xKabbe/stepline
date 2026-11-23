"""Assertions for paths."""

from pathlib import Path

from stepline.assertions._object_assert import ObjectAssert


class PathAssert(ObjectAssert[Path]):
    """Assertions for `Path` values."""

    # TODO: Extend class-docstring with the list of checks and examples
