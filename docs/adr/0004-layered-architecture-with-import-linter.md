# 0004: Layered Architecture With import-linter

!!! success "Status: Accepted · 2026-11-15"

## Context

stepline will grow into several features (steps, assertions, metadata, logging and
performance) and several integrations (the pytest plugin, console output with rich and the
command-line tool with Typer). Without clear boundaries, features start to import pytest or
rich directly, integrations call into each other, and the code becomes hard to test and hard
to change.

Some parts must also work outside of pytest: typed assertions, for example, should be usable
in any Python code, and the core logic should be testable without starting a pytest session.

The old library mixed these concerns, which made its structure the hardest part to change.

## Decision

!!! abstract "In short"

    stepline is organized in layers whose dependencies only point inwards, following the
    ideas of ports and adapters. import-linter enforces the rules on every check and in CI.

From the outside to the inside:

| Layer | Packages | Role |
|-------|----------|------|
| Integrations | `_cli`, `_pytest` | Adapters to Typer and pytest |
| Rendering | `_render` | Output with rich |
| Features | `assertions`, `steps`, `metadata`, `log`, `performance` | The public API |
| Core | `_core` | Shared logic and data, free of framework dependencies |

Additional rules:

- `_core` must not import pytest, rich or Typer.
- `assertions` must not import pytest, rich or Typer, so it works in any Python code.
- Packages starting with an underscore are internal. Only the feature packages form the
  public API.

``` mermaid
flowchart TB
    I["_cli · _pytest"] --> R["_render"]
    R --> F["assertions · steps · metadata · log · performance"]
    F --> C["_core"]
```

## Alternatives

??? info "One package without rules"

    The fastest way to start, but nothing stops a feature from depending on pytest or an
    integration from reaching into internals. The structure erodes with every change.

??? info "Rules by convention only"

    Describe the layers in the documentation and rely on discipline. Violations are easy to
    miss in reviews and only show up when the code is already hard to change.

??? info "Separate distributions per layer"

    Splitting stepline into several packages enforces boundaries through the dependency
    graph, but multiplies versioning and release work for a project of this size.

## Consequences

<div class="grid" markdown>

!!! success "Positive"

    - Violations fail `poe imports` locally and the lint job in CI, before they are merged.
    - The core and the assertions can be tested and used without pytest.
    - Integrations such as the console output can change without touching the features.

!!! warning "Negative"

    - Features need to go through the core instead of calling integrations directly, which
      adds some indirection.
    - New packages must be placed in a layer and added to `.importlinter`.
    - The boundaries are an up-front decision that may need adjusting as features grow.

</div>

*[ADR]: Architecture Decision Record
*[CI]: Continuous integration
*[API]: Application programming interface
