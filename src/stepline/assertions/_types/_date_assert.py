"""Assertions for dates and datetimes."""

from datetime import date

from stepline.assertions._object_assert import ObjectAssert


class DateAssert(ObjectAssert[date]):
    """Assertions for `date` and `datetime` values."""

    # TODO: Extend class-docstring with the list of checks and examples
