# 0005: Distribution and Import Name

!!! success "Status: Accepted · 2026-11-19"

## Context

The project, its package and its command-line tool are all called `stepline`. When the first
release was prepared, the name `stepline` had just been registered on PyPI by an unrelated
project, a debugger for AI agents. An active project's name cannot be taken over on PyPI.

The name `stepline` is already used for the brand, the repository, the documentation, the
logo and the tagline. pytest plugins on PyPI conventionally use the prefix `pytest-`, and
pytest lists all packages with this prefix in its plugin list.

## Decision

!!! abstract "In short"

    The distribution on PyPI is called **`pytest-stepline`**. Everything else stays
    **`stepline`**: the import name, the command-line tool, the pytest plugin name and the
    brand.

- `pyproject.toml` uses `name = "pytest-stepline"`, and the build backend is told to package
  the module `stepline` (`[tool.uv.build-backend] module-name = "stepline"`, see
  [ADR 0003](0003-src-layout-with-uv-and-uv-build.md)).
- Code that reads package metadata uses the distribution name, for example
  `importlib.metadata.version("pytest-stepline")`.
- The documentation and the README explain the two names.

## Alternatives

??? info "A completely new name"

    A new name would allow one name everywhere. Many candidates were considered, from Latin
    words such as *probare* or *testor* to *inoculum*. Most common words were already taken on
    PyPI, and none of the free ones fit as well as `stepline`.

??? info "`pytest-stepline` as the import name, too"

    Consistent, but `from pytest_stepline import step` is long and hides the brand. The short
    import name is what users type most often.

??? info "Another suffix or variant, such as `stepline-pytest`"

    Possible, but it breaks the convention that pytest uses to find and list plugins.

## Consequences

<div class="grid" markdown>

!!! success "Positive"

    - The brand, logo and documentation stay unchanged.
    - stepline appears in pytest's list of plugins.
    - Users write `import stepline` and run `stepline`, as before.

!!! warning "Negative"

    - Users need to know two names: `pip install pytest-stepline`, but `import stepline`.
    - The other `stepline` package also installs a module and a command called `stepline`.
      Installing both in the same environment makes one overwrite the other.
    - Searching for "stepline" on PyPI first finds the other project.

</div>

*[ADR]: Architecture Decision Record
*[AI]: Artificial intelligence
