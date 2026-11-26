"""The `assert_that` entry point, which picks the assertion class for the type of a value."""

from collections.abc import Callable, Collection, Mapping
from datetime import date
from decimal import Decimal
from fractions import Fraction
from functools import singledispatch
from pathlib import Path
from typing import Any, overload

from stepline.assertions._object_assert import ObjectAssert
from stepline.assertions._types._boolean_assert import BooleanAssert
from stepline.assertions._types._bytes_assert import BytesAssert
from stepline.assertions._types._callable_assert import CallableAssert
from stepline.assertions._types._collection_assert import CollectionAssert
from stepline.assertions._types._date_assert import DateAssert
from stepline.assertions._types._exception_assert import ExceptionAssert
from stepline.assertions._types._mapping_assert import MappingAssert
from stepline.assertions._types._number_assert import NumberAssert
from stepline.assertions._types._path_assert import PathAssert
from stepline.assertions._types._string_assert import StringAssert


# noinspection PyOverloads
# noinspection PyMissingOrEmptyDocstring
@overload
def assert_that(actual: bool, description: str | None = None) -> BooleanAssert: ...  # pyright: ignore[reportOverlappingOverload]


# noinspection PyOverloads
# noinspection PyMissingOrEmptyDocstring
@overload
def assert_that[N: int | float | Decimal | Fraction](actual: N, description: str | None = None) -> NumberAssert[N]: ...


# noinspection PyOverloads
# noinspection PyMissingOrEmptyDocstring
@overload
def assert_that(actual: str, description: str | None = None) -> StringAssert: ...  # pyright: ignore[reportOverlappingOverload]


# noinspection PyOverloads
# noinspection PyMissingOrEmptyDocstring
@overload
def assert_that(actual: bytes | bytearray, description: str | None = None) -> BytesAssert: ...


# noinspection PyOverloads
# noinspection PyMissingOrEmptyDocstring
@overload
def assert_that[K, V](actual: Mapping[K, V], description: str | None = None) -> MappingAssert[K, V]: ...


# noinspection PyOverloads
# noinspection PyMissingOrEmptyDocstring
@overload
def assert_that[E](actual: Collection[E], description: str | None = None) -> CollectionAssert[E]: ...


# noinspection PyOverloads
# noinspection PyMissingOrEmptyDocstring
@overload
def assert_that(actual: Path, description: str | None = None) -> PathAssert: ...


# noinspection PyOverloads
# noinspection PyMissingOrEmptyDocstring
@overload
def assert_that(actual: date, description: str | None = None) -> DateAssert: ...


# noinspection PyOverloads
# noinspection PyMissingOrEmptyDocstring
@overload
def assert_that(actual: BaseException, description: str | None = None) -> ExceptionAssert: ...


# noinspection PyOverloads
# noinspection PyMissingOrEmptyDocstring
@overload
def assert_that(actual: Callable[..., object], description: str | None = None) -> CallableAssert: ...


# noinspection PyOverloads
# noinspection PyMissingOrEmptyDocstring
@overload
def assert_that[T](actual: T, description: str | None = None) -> ObjectAssert[T]: ...


def assert_that(actual: object, description: str | None = None) -> ObjectAssert[Any]:
    """
    Start an assertion on a value.

    The returned assertion class depends on the type of the value, so only checks that fit the value are available, e.g.
    number checks for numbers and string checks for strings. Values without a type-specific class get the generic
    assertions of `ObjectAssert`.

    Examples:
        ```python
        assert_that(response.status, description="status code").is_equal_to(200)
        ```

    Args:
        actual: The value to check.
        description: A name for the value, shown in failure messages, e.g. "status code".

    Returns:
        The assertion class that matches the type of `actual`.
    """
    return _assertion_for(actual, description)


@singledispatch
def _assertion_for(actual: object, description: str | None, /) -> ObjectAssert[Any]:
    """
    Create the assertion class for the type of `actual`.

    The type-specific classes are registered below. This function is the fallback for every other type and returns
    the generic `ObjectAssert`.

    Args:
        actual: The value to check.
        description: A name for the value, shown in failure messages, e.g. "status code".

    Returns:
        The assertion class that matches the type of `actual`.
    """
    return ObjectAssert(actual=actual, description=description)


_assertion_for.register(bool, BooleanAssert)
for _number_type in [int, float, Decimal, Fraction]:
    _assertion_for.register(_number_type, NumberAssert)
_assertion_for.register(str, StringAssert)
for _bytes_type in [bytes, bytearray]:
    _assertion_for.register(_bytes_type, BytesAssert)
_assertion_for.register(Mapping, MappingAssert)
_assertion_for.register(Collection, CollectionAssert)
_assertion_for.register(Path, PathAssert)
_assertion_for.register(date, DateAssert)
_assertion_for.register(BaseException, ExceptionAssert)
_assertion_for.register(Callable, CallableAssert)  # pyright: ignore[reportArgumentType, reportCallIssue]
