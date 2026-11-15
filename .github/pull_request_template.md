<!--
  Build the PR title from the two lists below. It becomes the commit message on `main`
  (squash merge) and drives the version number and changelog via release-please.

      feat(cli): add spec export command
      ^    ^     ^
      |    |     |__ Subject: lowercase, imperative ("add", not "added"), no period, max. ~72 chars
      |    |________ Scope:   optional, the area of stepline (see list below)
      |_____________ Type:    what kind of change (see list below)

  Breaking change? Add `!` before the colon, e.g. `feat(steps)!: rename on_error to on_failure`,
  and describe the migration under "Breaking change" below.
-->

## Summary

<!-- What does this PR change, and why? One or two sentences. -->

Closes #

## Type

<!--
  Pick exactly one. The type decides whether a release happens:

  feat      new feature or public API          → minor release   e.g. feat(assertions): add is_close_to
  fix       bug fix users can notice           → patch release   e.g. fix(steps): keep step order with async steps
  perf      faster or lighter, same behavior   → patch release   e.g. perf(metadata): cache marker lookup
  docs      documentation only                 → no release      e.g. docs(steps): add how-to for CRUD flows
  refactor  restructuring, same behavior       → no release      e.g. refactor(console): extract failure box
  test      tests only                         → no release      e.g. test(assertions): add hypothesis tests
  build     packaging, dependencies            → no release      e.g. build: add typer dependency
  ci        GitHub Actions workflows           → no release      e.g. ci(tooling): run tests on macos
  chore     maintenance, tooling config        → no release      e.g. chore(tooling): configure pre-commit
  revert    reverts an earlier change          → depends         e.g. revert: feat(cli): add spec export command
-->

- [ ] `feat` – new feature or public API
- [ ] `fix` – bug fix
- [ ] `perf` – performance improvement
- [ ] `docs` – documentation only
- [ ] `refactor` – restructuring without behavior change
- [ ] `test` – tests only
- [ ] `build` – packaging and dependencies
- [ ] `ci` – workflows and CI configuration
- [ ] `chore` – maintenance and tooling
- [ ] `revert` – reverts an earlier change

## Scope

<!--
  Pick one, or none if the change affects the whole project.
  `deps` and `deps-dev` are reserved for automated dependency updates.
-->

- [ ] `assertions` – assert_that() and all assertion classes
- [ ] `steps` – steps, scenarios and step failure behavior
- [ ] `metadata` – metadata decorators, spec export and test reports
- [ ] `console` – console output, logging and rendering
- [ ] `cli` – the stepline command-line tool
- [ ] `tooling` – repository setup, linting, CI and release pipeline
- [ ] `docs` – documentation site, ADRs and examples
- [ ] no scope

## Breaking change

- [ ] This PR breaks existing user code (title uses `!`)

<!-- If checked: what breaks, and how do users migrate? -->

## Checklist

- [ ] Tests added or updated, all green locally (`uv run poe check`)
- [ ] Public API has complete docstrings with an example
- [ ] Documentation updated (if user-facing)
- [ ] Tried it out in a real test project (if user-facing)
