# 0002: Python 3.15 as Minimum Version

!!! success "Status: Accepted · 2026-11-10"

## Context

stepline starts from scratch as the successor of an older internal library. There is no
existing user base that depends on older Python versions, and the first stable release (1.0)
is still many feature releases away.

The project relies heavily on modern typing: pyright runs in strict mode, the public API is
meant to be fully typed, and features such as typed assertions profit from the newest syntax
for generics, type parameter defaults and deferred evaluation of annotations. Every older
Python version that is supported would need to be tested in CI and would limit which language
features can be used.

The project was first planned with Python 3.14. When the repository was created, Python 3.15
was about to be released.

## Decision

!!! abstract "In short"

    stepline requires Python 3.15 or newer (`requires-python = ">=3.15"`), and CI tests
    against Python 3.15.

The minimum version is raised deliberately and only through a new ADR, not as a side effect
of a dependency update.

## Alternatives

??? info "Python 3.14"

    The originally planned version. It would have reached slightly more users at the start,
    but by the time stepline offers its core features, Python 3.15 is the current release and
    3.14 would be the version that holds the project back.

??? info "A wide range, such as Python 3.12 or newer"

    The usual choice for established libraries, as it reaches the most users. For a new
    project it means a test matrix over several versions and giving up newer language
    features, without having users that need the older versions.

## Consequences

<div class="grid" markdown>

!!! success "Positive"

    - The newest language and typing features are available everywhere in the code.
    - CI tests a single Python version on three operating systems, which keeps it fast.
    - No compatibility code for older Python versions.

!!! warning "Negative"

    - Projects that do not run on Python 3.15 yet cannot use stepline.
    - Some tools and libraries may need a while to fully support a new Python version.
    - Supporting an older version later is possible, but needs a new ADR and more CI jobs.

</div>

*[ADR]: Architecture Decision Record
*[CI]: Continuous integration
