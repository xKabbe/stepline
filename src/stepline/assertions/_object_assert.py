"""The base assertion class with the generic assertions that work for every value."""


class ObjectAssert[T]:
    """
    Generic assertions that work for every value, and the base of all assertion classes.

    `assert_that` returns this class for values without a type-specific assertion class,
    for example `None` or instances of your own classes. All type-specific classes, such as
    `NumberAssert` or `StringAssert`, inherit its assertions.

    Args:
        actual: The value to check.
        description: A name for the value, shown in failure messages, e.g. "status code".
    """

    # TODO: Extend class-docstring with the list of checks and examples

    def __init__(self, actual: T, description: str | None = None) -> None:
        self._actual = actual
        self._description = description
