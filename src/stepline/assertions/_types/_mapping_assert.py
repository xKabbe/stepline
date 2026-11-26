"""Assertions for mappings."""

from collections.abc import Mapping

from stepline.assertions._object_assert import ObjectAssert


class MappingAssert[K, V](ObjectAssert[Mapping[K, V]]):
    """Assertions for mappings such as dictionaries."""

    # TODO: Extend class-docstring with the list of checks and examples
