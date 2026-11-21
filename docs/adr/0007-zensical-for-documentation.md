# 0007: Zensical for Documentation

!!! success "Status: Accepted · 2026-11-21"

## Context

stepline needs a documentation site: guides, the architecture decisions and, later, an API
reference generated from the docstrings. The old library used MkDocs with the theme Material
for MkDocs, and the plan for stepline was to do the same.

When the documentation was set up, this stack was no longer a good basis for a new project:

- Material for MkDocs is in maintenance mode, receives no new features, and reaches its end of
  life in 2027.
- MkDocs 1.x has not been developed further since 2024, and MkDocs 2.0 is an incompatible
  rewrite without a migration path for existing sites.
- The team behind Material for MkDocs builds **Zensical** as its successor. It reads the
  usual MkDocs project structure and offers the familiar Material look. Its first dependable
  release line, 0.1, started in November 2026.

## Decision

!!! abstract "In short"

    stepline builds its documentation with **Zensical**, configured in `zensical.toml`, and
    publishes it to GitHub Pages.

- Pages are written in Markdown under `docs/`.
- Every pull request builds the documentation with `--strict`, so broken links fail the build.
- Every push to `main` publishes the site.
- The API reference will use mkdocstrings, which Zensical supports.

## Alternatives

??? info "MkDocs with Material for MkDocs"

    Familiar from the old library and very mature, but at the end of its life. Starting a new
    project on it would mean a migration within the first year.

??? info "Sphinx with MyST and Furo"

    The long-standing standard for Python libraries, with the most mature API reference and
    cross-references. Its configuration and its reStructuredText conventions are more complex,
    even with Markdown through MyST, which is more than this project needs at its start.

??? info "JavaScript-based tools such as Docusaurus or VitePress"

    Modern sites, but they cannot read Python docstrings, so an API reference would need a
    separate tool.

## Consequences

<div class="grid" markdown>

!!! success "Positive"

    - Actively maintained, with the familiar Material look and Markdown authoring.
    - Admonitions, content tabs, diagrams and other features are built in.
    - Fast builds, and a strict build in CI catches broken links early.

!!! warning "Negative"

    - Zensical is young: plugin support is narrower than with MkDocs, and features may change.
    - Cross-references in the API reference are less mature than in Sphinx.
    - Fewer examples and answers exist online than for MkDocs or Sphinx.

</div>

*[ADR]: Architecture Decision Record
*[API]: Application programming interface
*[CI]: Continuous integration
