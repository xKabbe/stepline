"""The base assertion class with the generic assertions that work for every value."""

from typing import NoReturn, Self

from stepline._core.failure import Failure, NotSet
from stepline.errors import AssertionFailedError


class ObjectAssert[T]:
    """
    Generic assertions that work for every value, and the base of all assertion classes.

    `assert_that` returns this class for values without a type-specific assertion class,
    for example `None` or instances of your own classes. All type-specific classes, such as
    `NumberAssert` or `StringAssert`, inherit its assertions.

    The generic checks, each with its negation:

    - Equality: `is_equal_to`, `is_not_equal_to`
    - Identity: `is_same_as`, `is_not_same_as`
    - `None`: `is_none`, `is_not_none`
    - Type: `is_instance_of`, `is_not_instance_of`

    Every check returns the assertion itself, so checks can be chained. A failed check raises `AssertionFailedError`.

    Examples:
        ```python
        assert_that(user, "current user").is_not_none().is_instance_of(User)
        assert_that(cache.get("config")).is_same_as(config)
        ```

    Args:
        actual: The value to check.
        description: A name for the value, shown in failure messages, e.g. "status code".
    """

    def __init__(self, actual: T, description: str | None = None) -> None:
        self._actual = actual
        self._description = description

    def is_equal_to(self, expected: object) -> Self:
        """
        Check that the value is equal to the expected value, using `==`.

        Examples:
            ```python
            assert_that(response.status_code).is_equal_to(200)
            assert_that([1, 2]).is_equal_to([1, 2])
            ```

        Args:
            expected: The value that the checked value must be equal to.

        Returns:
            This assertion, so that further checks can be chained.

        Raises:
            AssertionFailedError: If the value is not equal to the expected value.
        """
        __tracebackhide__ = True

        if self._actual != expected:
            self._fail(check="to be equal to", expected=expected)
        return self

    def is_not_equal_to(self, expected: object) -> Self:
        """
        Check that the value is not equal to the given value, using `!=`.

        Examples:
            ```python
            assert_that(new_password).is_not_equal_to(old_password)
            ```

        Args:
            expected: The value that the checked value must not be equal to.

        Returns:
            This assertion, so that further checks can be chained.

        Raises:
            AssertionFailedError: If the value is equal to the given value.
        """
        __tracebackhide__ = True

        if self._actual == expected:
            self._fail(check="not to be equal to", expected=expected)
        return self

    def is_same_as(self, expected: object) -> Self:
        """
        Check that the value is the same object as the expected one, using `is`.

        Examples:
            ```python
            assert_that(get_config()).is_same_as(get_config())
            ```

        Args:
            expected: The object that the checked value must be.

        Returns:
            This assertion, so that further checks can be chained.

        Raises:
            AssertionFailedError: If the value is a different object.
        """
        __tracebackhide__ = True

        if self._actual is not expected:
            self._fail(check="to be the same object as", expected=expected)
        return self

    def is_not_same_as(self, expected: object) -> Self:
        """
        Check that the value is a different object than the given one, using `is not`.

        Examples:
            ```python
            copy = original.copy()
            assert_that(copy).is_not_same_as(original)
            ```

        Args:
            expected: The object that the checked value must not be.

        Returns:
            This assertion, so that further checks can be chained.

        Raises:
            AssertionFailedError: If the value is the same object.
        """
        __tracebackhide__ = True

        if self._actual is expected:
            self._fail(check="not to be the same object as", expected=expected)
        return self

    def is_none(self) -> Self:
        """
        Check that the value is `None`.

        Examples:
            ```python
            assert_that(user.deleted_at).is_none()
            ```

        Returns:
            This assertion, so that further checks can be chained.

        Raises:
            AssertionFailedError: If the value is not `None`.
        """
        __tracebackhide__ = True

        if self._actual is not None:
            self._fail(check="to be", expected=None)
        return self

    def is_not_none(self) -> Self:
        """
        Check that the value is not `None`.

        Examples:
            ```python
            assert_that(user.id).is_not_none()
            ```

        Returns:
            This assertion, so that further checks can be chained.

        Raises:
            AssertionFailedError: If the value is `None`.
        """
        __tracebackhide__ = True

        if self._actual is None:
            self._fail(check="not to be", expected=None)
        return self

    def is_instance_of(self, expected_type: type[object]) -> Self:
        """
        Check that the value is an instance of the expected type or of one of its subclasses.

        Examples:
            ```python
            assert_that(response.json()).is_instance_of(dict)
            assert_that(True).is_instance_of(int)
            ```

        Args:
            expected_type: The type that the checked value must be an instance of.

        Returns:
            This assertion, so that further checks can be chained.

        Raises:
            AssertionFailedError: If the value is not an instance of the expected type.
        """
        __tracebackhide__ = True

        if not isinstance(self._actual, expected_type):
            self._fail(check="to be an instance of", expected=expected_type)
        return self

    def is_not_instance_of(self, expected_type: type[object]) -> Self:
        """
        Check that the value is not an instance of the given type or of one of its subclasses.

        Examples:
            ```python
            assert_that(result).is_not_instance_of(Exception)
            ```

        Args:
            expected_type: The type that the checked value must not be an instance of.

        Returns:
            This assertion, so that further checks can be chained.

        Raises:
            AssertionFailedError: If the value is an instance of the given type.
        """
        __tracebackhide__ = True

        if isinstance(self._actual, expected_type):
            self._fail(check="not to be an instance of", expected=expected_type)
        return self

    def _fail(self, check: str, expected: object = NotSet.NOT_SET) -> NoReturn:
        """
        Raise an `AssertionFailedError` with a failure for this assertion's value and description.

        Args:
            check: The check as a readable phrase, e.g. "to be equal to".
            expected: The expected value, or `NotSet.NOT_SET` if the check has none. `None` is a valid expected
                value, e.g. for `is_none()`.

        Raises:
            AssertionFailedError: Always, with the failure that describes the failed check.
        """
        __tracebackhide__ = True

        raise AssertionFailedError(
            failure=Failure(check=check, actual=self._actual, expected=expected, description=self._description)
        )
