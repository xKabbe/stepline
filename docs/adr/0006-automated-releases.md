# 0006: Automated Releases

!!! success "Status: Accepted · 2026-11-19"

## Context

stepline is released feature by feature, not on a fixed schedule. Every release needs a new
version number, a changelog entry, a Git tag, a GitHub release and an upload to PyPI. Doing
this by hand is error-prone: a forgotten version bump, a tag that does not match the version
in `pyproject.toml`, or a changelog that misses changes.

Uploading to PyPI traditionally requires an API token stored as a secret, which has to be
protected and renewed. An upload to PyPI is also final: a published version can never be
replaced.

## Decision

!!! abstract "In short"

    Releases are derived from Conventional Commits by **release-please** and published to
    PyPI with **Trusted Publishing**. A release happens when the maintainer merges the
    release pull request and approves the deployment.

1. Pull request titles follow Conventional Commits, checked by a workflow. Pull requests are
   squash-merged, so each title becomes one commit on `main`.
2. After every merge, release-please updates a release pull request with the next version,
   based on the commit types, and the changelog.
3. Merging the release pull request creates the tag and the GitHub release. release-please
   runs with a GitHub App token, so the release can trigger further workflows.
4. The publish workflow builds the package once and uploads it to PyPI through Trusted
   Publishing. The `pypi` environment only accepts version tags and waits for the
   maintainer's approval.
5. TestPyPI can be published to manually, to test the process without a real release.

## Alternatives

??? info "Manual releases"

    Bump the version, write the changelog, tag and upload by hand. Full control, but every
    step can be forgotten or done inconsistently.

??? info "python-semantic-release"

    Similar idea, but it typically releases directly on every relevant merge. The release
    pull request of release-please gives an explicit point to decide *when* to release.

??? info "Upload with an API token"

    Works with every CI system, but the token is a long-lived secret that must be stored,
    protected and renewed. Trusted Publishing uses short-lived credentials instead.

## Consequences

<div class="grid" markdown>

!!! success "Positive"

    - Version numbers, changelog, tags and releases are always consistent.
    - No PyPI token exists that could leak.
    - Two safeguards protect PyPI: the tag rule and the manual approval.
    - Published packages carry attestations that prove where they were built.

!!! warning "Negative"

    - Pull request titles must follow Conventional Commits.
    - Changes of type `docs`, `build` or `ci` do not trigger a release, so they only reach
      PyPI with the next feature or fix.
    - The GitHub App and its private key are one more thing to maintain.
    - Special cases, such as the first release, need a one-time override in the
      configuration.

</div>

*[ADR]: Architecture Decision Record
*[CI]: Continuous integration
*[API]: Application programming interface
