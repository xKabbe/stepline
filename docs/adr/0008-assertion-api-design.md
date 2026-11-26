# 0008: Assertion API Design

!!! note "Status: Accepted · 2026-11-26"

## Context

Typed assertions are the first feature of stepline. Their API is what users write most often,
so it needs to be decided before any code exists, and it has to work well with the tools
stepline is built with:

- pyright runs in strict mode, and editors should only suggest methods that make sense for
  the value under test.
- Following [ADR 0004](0004-layered-architecture-with-import-linter.md), assertions must not depend on pytest, rich or Typer, so they
  work in any Python code.
- Plain `assert` statements give little context when they fail. stepline's assertions should
  say what was checked, what was expected and what was found.

Established libraries such as AssertJ (Java), Truth (Java) and assertpy (Python) show a
proven shape for this: a single entry point that picks a set of checks based on the type of
the value.

## Decision

!!! abstract "In short"

    stepline provides a fluent, typed assertion API with a single entry point,
    `assert_that(actual, description=...)`, which returns an assertion class chosen by the
    type of the value. Failed assertions raise immediately, unless they run inside a
    `with soft_assertions():` block.

### Entry point

- `assert_that(actual, description=None)` is the only entry point. The optional keyword
  argument `description` names the checked value in failure messages.
- Users import it from the package root: `from stepline import assert_that`. The assertion
  classes, needed only for type hints, live in `stepline.assertions`.

### Choosing the assertion class

- `@overload` signatures of `assert_that` tell pyright which class is returned for which type.
- At runtime, `functools.singledispatch` picks the class. This also allows registering
  further types later.
- More specific types always come before more general ones: `bool` before `int`, `str`,
  `bytes` and mappings before other collections, and `datetime` before `date`.

### Classes

| Class | Types |
|-------|-------|
| `ObjectAssert[T]` | Base class with the generic assertions; fallback for every other type |
| `BooleanAssert` | `bool` |
| `NumberAssert` | `int`, `float` and other real numbers, but not `bool` |
| `StringAssert` | `str` |
| `BytesAssert` | `bytes`, `bytearray` |
| `CollectionAssert` | lists, tuples, sets and other collections |
| `MappingAssert` | dictionaries and other mappings |
| `PathAssert` | `pathlib.Path` |
| `DateAssert` | `date`, `datetime` |
| `CallableAssert` | functions and other callables |
| `ExceptionAssert` | exception instances |

All classes are created up front. The type-specific ones start empty, inheriting the generic
assertions, and get their own methods feature by feature.

Some values need a different view to be checked well. Assertion classes may offer `as_…()`
methods that convert the value and return another assertion class, for example
`assert_that(text).as_url()` for URL checks. Plain strings therefore keep string assertions.

### Methods

- Method names use three prefixes: `is_…` for states and comparisons (`is_equal_to`,
  `is_none`), `has_…` for properties (`has_length`) and `contains…` for content
  (`contains`, `contains_only`). Abbreviations such as `eq` or `gt` are not used.
- Negations are separate methods, such as `is_not_equal_to` or `is_not_none`. They exist only
  where they add meaning: `is_not_greater_than` is not needed next to
  `is_less_than_or_equal_to`.
- `is_equal_to` compares with `==`, `is_same_as` with `is`.
- Every method returns `Self`, so checks can be chained.

### Writing styles

Chains of any length, one check per line and a variable holding the assertion are equally
valid. All of them stop at the first failure:

=== "Chain"

    ``` python
    assert_that(status, description="status code").is_greater_than_or_equal_to(200).is_less_than(300)
    ```

=== "One check per line"

    ``` python
    assert_that(status).is_greater_than_or_equal_to(200)
    assert_that(status).is_less_than(300)
    ```

=== "Variable"

    ``` python
    code = assert_that(status, description="status code")
    code.is_greater_than_or_equal_to(200)
    code.is_less_than(300)
    ```

=== "Dedicated method"

    ``` python
    assert_that(status).is_between(200, 299)
    ```

### Failures

- A failed check raises `AssertionFailedError`, a subclass of `AssertionError`, so pytest and
  other tools treat it as a normal test failure. It carries the failure object from the core.
- The `with` statement is reserved for **soft assertions**: inside
  `with soft_assertions():`, all failed checks are collected and reported together at the end
  of the block. The assertion classes themselves do not support `with`. Soft assertions are
  designed in a separate ADR, together with the step semantics.

## Alternatives

??? info "Plain `assert` statements with pytest's assertion rewriting"

    No extra API to learn, and pytest already shows the compared values. But the messages only
    know the expression, not its meaning, the checks are not reusable outside pytest, and
    editors cannot suggest checks that fit the value.

??? info "A negation modifier such as `.not_`"

    `assert_that(x).not_.is_equal_to(y)` halves the number of methods, but every method then has
    to handle both directions, failure messages get harder to word, and editors no longer show
    which negations exist.

??? info "Separate entry points per type"

    Functions such as `assert_number(x)` or `assert_string(x)` need no type dispatch, but users
    have to pick the right function and learn many names instead of one.

??? info "Soft assertions as a switch, such as `assert_that(x, soft=True)`"

    The same code would then mean different things depending on a flag. A dedicated block makes
    collected failures visible where they happen.

## Consequences

<div class="grid" markdown>

!!! success "Positive"

    - One entry point to learn, and editors suggest only the checks that fit the value.
    - Every failure explains what was checked, expected and found.
    - Assertions work in any Python code, not only in pytest.
    - New types and checks can be added without changing existing code.

!!! warning "Negative"

    - Overloads and dispatch must be kept in the same order, or pyright and the runtime disagree.
    - Explicit negations mean more methods to write, test and document.
    - Eleven assertion classes exist before most of them have methods of their own.
    - Soft assertions are announced, but not available until their own ADR is implemented.

</div>

*[ADR]: Architecture Decision Record
*[API]: Application programming interface
