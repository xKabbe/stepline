"""Tests for the entry point that picks the assertion class for a value."""

from collections import OrderedDict
from datetime import date, datetime
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
from typing import Any, assert_type

import pytest

from stepline.assertions._assert_that import assert_that
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


@pytest.mark.parametrize(
    ("actual", "expected_type"),
    [
        pytest.param(True, BooleanAssert, id="bool"),
        pytest.param(1, NumberAssert, id="int"),
        pytest.param(1.5, NumberAssert, id="float"),
        pytest.param(Decimal("1.5"), NumberAssert, id="decimal"),
        pytest.param(Fraction(1, 2), NumberAssert, id="fraction"),
        pytest.param("hello world", StringAssert, id="str"),
        pytest.param(b"hello world", BytesAssert, id="bytes"),
        pytest.param(bytearray(b"hello world"), BytesAssert, id="bytearray"),
        pytest.param({"foo": "bar"}, MappingAssert, id="dict"),
        pytest.param([1, 2], CollectionAssert, id="list"),
        pytest.param((1, 2), CollectionAssert, id="tuple"),
        pytest.param({1, 2}, CollectionAssert, id="set"),
        pytest.param(Path("file.txt"), PathAssert, id="path"),
        pytest.param(date(2026, 1, 1), DateAssert, id="date"),
        pytest.param(ValueError("ohhh"), ExceptionAssert, id="exception"),
        pytest.param(len, CallableAssert, id="function"),
        pytest.param(int, CallableAssert, id="class"),
        pytest.param(None, ObjectAssert, id="none"),
        pytest.param(object(), ObjectAssert, id="object"),
    ],
)
def test_returns_the_assertion_for_the_value_type(actual: object, expected_type: type[ObjectAssert[Any]]) -> None:
    """
    Every value gets the assertion class that fits its type, with `ObjectAssert` as fallback.

    Args:
        actual: A value of one of the supported types, or of any other type.
        expected_type: The assertion class that fits the type of the value.
    """
    assert type(assert_that(actual)) is expected_type


@pytest.mark.parametrize(
    ("actual", "expected_type"),
    [
        pytest.param(OrderedDict([("a", 1)]), MappingAssert, id="ordered-dict"),
        pytest.param(datetime(2026, 1, 1, 12, 0), DateAssert, id="datetime"),
        pytest.param(KeyError("key"), ExceptionAssert, id="key-error"),
    ],
)
def test_returns_the_assertion_of_the_base_type_for_subclasses(
    actual: object, expected_type: type[ObjectAssert[Any]]
) -> None:
    """
    Subclasses of a known type get the assertion class of that type.

    Args:
        actual: A value whose type is a subclass of a known type.
        expected_type: The assertion class of the known base type.
    """
    assert type(assert_that(actual)) is expected_type


def test_has_the_matching_static_type() -> None:
    """The type checker sees the same assertion class that `assert_that` returns at runtime."""
    assert_type(assert_that(True), BooleanAssert)
    assert_type(assert_that(4), NumberAssert[int])
    assert_type(assert_that(4.5), NumberAssert[float])
    assert_type(assert_that("lorem ipsum"), StringAssert)
    assert_type(assert_that(b"lorem ipsum"), BytesAssert)
    assert_type(assert_that({str(1): 1}), MappingAssert[str, int])
    assert_type(assert_that([1, "2"]), CollectionAssert[int | str])
    assert_type(assert_that(Path("report.json")), PathAssert)
    assert_type(assert_that(date(2027, 1, 1)), DateAssert)
    assert_type(assert_that(ValueError("nooo")), ExceptionAssert)
    assert_type(assert_that(type), CallableAssert)
    assert_type(assert_that(None), ObjectAssert[None])


def test_passes_the_description_to_the_assertion() -> None:
    """The description given to `assert_that` reaches the assertion."""
    description = "status code"
    assertion = assert_that(4, description=description)

    assert assertion._description == description  # pyright: ignore[reportPrivateUsage]
