---
icon: lucide/landmark
---

# Architecture decisions

This section records the important architecture decisions behind stepline as
**Architecture Decision Records** (ADRs). Each record explains one decision: the situation
that made it necessary, what was decided, and what follows from it.

!!! info "Why ADRs?"

    Code shows *what* was built, but rarely *why*. ADRs keep the reasoning next to the
    project, so later changes can build on it instead of guessing. They are short, written
    once, and never rewritten. A changed decision gets a new ADR that supersedes the old one.

## Decisions

| ADR | Title | Status |
|-----|-------|--------|
| [0001](0001-record-architecture-decisions.md) | Record Architecture Decisions as ADRs | Accepted |
| [0002](0002-python-3-15-as-minimum-version.md) | Python 3.15 as Minimum Version | Accepted |
| [0003](0003-src-layout-with-uv-and-uv-build.md) | src Layout With uv and uv_build | Accepted |
| [0004](0004-layered-architecture-with-import-linter.md) | Layered Architecture With import-linter | Accepted |
| [0005](0005-distribution-and-import-name.md) | Distribution and Import Name | Accepted |
| [0006](0006-automated-releases.md) | Automated Releases | Accepted |
| [0007](0007-zensical-for-documentation.md) | Zensical for Documentation | Accepted |

## Lifecycle

Every ADR has a status. A new record starts as *proposed* and becomes *accepted* once the
decision is made. Accepted records are not edited afterwards: if a decision changes, a new
ADR replaces it, and the old one is marked as *superseded*.

``` mermaid
stateDiagram-v2
    direction LR
    [*] --> Proposed
    Proposed --> Accepted
    Proposed --> Rejected
    Accepted --> Superseded: replaced by a newer ADR
    Accepted --> Deprecated: no longer relevant
```

## Writing a new ADR

1. Copy the template [template](template.md) into a new file `docs/adr/NNNN-short-title.md`, with the next free
   four-digit number, for example `0008-step-semantics.md`.
2. Fill in the sections and set the status to *Proposed*.
3. Add the record to the table above and to the `nav` in `zensical.toml`.
4. Once the decision is made, set the status to *Accepted*.

*[ADR]: Architecture Decision Record
*[ADRs]: Architecture Decision Records
