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
| –   | The first records follow soon. | – |

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

1. Copy the template below into a new file `docs/adr/NNNN-short-title.md`, with the next free
   four-digit number, for example `0004-step-semantics.md`.
2. Fill in the sections and set the status to *Proposed*.
3. Add the record to the table above and to the `nav` in `zensical.toml`.
4. Once the decision is made, set the status to *Accepted*.

??? example "ADR template"

    ``` markdown
    # NNNN: Short title of the decision

    - **Status:** Proposed
    - **Date:** YYYY-MM-DD

    ## Context

    What is the situation, and which forces or constraints make a decision necessary?

    ## Decision

    What was decided? Write it as a clear statement: "stepline uses ..."

    ## Alternatives

    Which other options were considered, and why were they not chosen?

    ## Consequences

    What becomes easier or harder because of this decision?
    ```

*[ADR]: Architecture Decision Record
*[ADRs]: Architecture Decision Records
