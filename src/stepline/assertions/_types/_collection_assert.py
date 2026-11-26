"""Assertions for collections."""

from collections.abc import Collection

from stepline.assertions._object_assert import ObjectAssert


class CollectionAssert[E](ObjectAssert[Collection[E]]):
    """Assertions for collections such as lists, tuples and sets."""

    # TODO: Extend class-docstring with the list of checks and examples
