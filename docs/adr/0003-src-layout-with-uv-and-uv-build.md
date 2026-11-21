# 0003: src Layout With uv and uv_build

!!! success "Status: Accepted · 2026-11-10"

## Context

A Python project needs a folder structure, a tool to manage environments and dependencies,
and a build backend that turns the source into a package for PyPI.

The old library used a flat layout, where the package folder sits directly in the repository
root. In this layout, tests can import the package from the working directory instead of the
installed version, so a missing file in the package or a broken entry point can go unnoticed.

stepline also registers entry points (a pytest plugin and a command-line tool). These only
work when the package is actually installed, so tests should always run against the installed
package.

## Decision

!!! abstract "In short"

    stepline uses the **src layout** (`src/stepline/`), **uv** to manage Python versions,
    environments and dependencies, and **uv_build** as the build backend.

- All dependencies, including the development tools, are declared in `pyproject.toml` and
  locked in `uv.lock`. CI installs them with `uv sync --locked`.
- The package ships a `py.typed` marker, so type checkers use its annotations.
- uv_build is pinned to a minor version range in `[build-system]`.

## Alternatives

??? info "Flat layout"

    Simpler at first glance, but tests may import the source folder instead of the installed
    package. Packaging errors then only show up for users.

??? info "Poetry"

    A mature all-in-one tool, but with its own lock file format and dependency resolver,
    and noticeably slower than uv.

??? info "Hatch with hatchling, or setuptools"

    Both are established build backends. They need more configuration than uv_build and add
    a second tool next to uv, while uv_build works with uv without extra setup.

## Consequences

<div class="grid" markdown>

!!! success "Positive"

    - Tests always run against the installed package, including its entry points.
    - One tool for Python versions, environments, dependencies, locking and building.
    - Fast installs locally and in CI, with reproducible environments from `uv.lock`.

!!! warning "Negative"

    - After changing entry points, `uv sync` must run again before they are active.
    - uv_build is young and supports fewer options than older backends.
    - The pinned uv_build version range needs regular updates.

</div>

*[ADR]: Architecture Decision Record
*[CI]: Continuous integration
