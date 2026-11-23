"""Assertions for numbers."""

from decimal import Decimal
from fractions import Fraction

from stepline.assertions._object_assert import ObjectAssert


class NumberAssert[N: int | float | Decimal | Fraction](ObjectAssert[N]):
    """Assertions for numbers: `int`, `float`, `Decimal` and `Fraction`, but not `bool`."""

    # TODO: Extend class-docstring with the list of checks and examples
