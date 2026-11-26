"""Assertions for exceptions."""

from stepline.assertions._object_assert import ObjectAssert


class ExceptionAssert(ObjectAssert[BaseException]):
    """Assertions for exception instances."""

    # TODO: Extend class-docstring with the list of checks and examples
