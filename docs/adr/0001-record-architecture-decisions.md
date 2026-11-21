# 0001: Record Architecture Decisions as ADRs

!!! success "Status: Accepted · 2026-11-21"

## Context

stepline is built step by step, feature by feature, and many decisions shape it long before
the code shows them: the minimum Python version, the project layout, the layers of the
architecture, the package name, the release process and the documentation tooling.

The reasons behind these decisions currently live in issues, pull requests and notes. Code
shows *what* was built, but rarely *why*, and squashed commit messages are too short to carry
the reasoning. Some decisions will also be revisited later, as the switch from MkDocs to
Zensical already showed. Judging whether a decision still holds requires knowing the
situation it was made in.

## Decision

!!! abstract "In short"

    stepline records every significant architecture decision as an Architecture Decision
    Record (ADR): one short Markdown file per decision in `docs/adr/`, published as part of
    the documentation.

A decision is significant if it affects the structure of the code, its dependencies, the
public API or the project tooling, or if it would be expensive to reverse.

- Each ADR follows the [template](template.md) and gets the next free four-digit number.
- An ADR starts as *Proposed* and becomes *Accepted* once the decision is made.
- Accepted ADRs are not rewritten. If a decision changes, a new ADR supersedes the old one,
  and the old one keeps its text and is marked as *Superseded*.
- ADRs are added and changed through pull requests, like code.

## Alternatives

??? info "No written record"

    Rely on commit messages, pull requests and issues. The information exists, but it is
    scattered across many places, hard to search and easy to lose. Squash merges reduce each
    change to a single title.

??? info "GitHub Wiki"

    A wiki lives outside the repository. Its pages are not versioned together with the code,
    not reviewed in pull requests, and not part of the published documentation.

??? info "One design document"

    A single document that describes the current architecture. It is easy to read at first,
    but it gets rewritten with every change, so the reasons for earlier decisions disappear.

??? info "A more detailed ADR format"

    Formats such as MADR add sections for decision drivers, deciders and a detailed rating
    of each option. For a project with one maintainer this is more overhead than value. The
    lightweight template keeps the essential parts: context, decision, alternatives and
    consequences.

## Consequences

<div class="grid" markdown>

!!! success "Positive"

    - The reasoning behind decisions is easy to find, next to the code and in the documentation.
    - ADRs are versioned and reviewed together with the changes they describe.
    - Revisiting a decision starts from its original context instead of from memory.
    - Future contributors can understand the project without asking.

!!! warning "Negative"

    - Every significant decision takes a few extra minutes to write down.
    - It is a judgment call which decisions are significant enough for an ADR.
    - Superseding instead of editing leads to more files over time.
    - ADRs 0001 to 0007 are written retroactively, so their context is reconstructed after
      the fact.

</div>

*[ADR]: Architecture Decision Record
*[ADRs]: Architecture Decision Records
