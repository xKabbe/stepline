"""Assertions for callables."""

from collections.abc import Callable

from stepline.assertions._object_assert import ObjectAssert


class CallableAssert(ObjectAssert[Callable[..., object]]):
    """Assertions for functions and other callables."""

    # TODO: Extend class-docstring with the list of checks and examples
