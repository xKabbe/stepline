## Summary

<!-- What does this PR change, and why? One or two sentences. -->

Closes #

## Type of change

<!--
  The PR title becomes the commit message on `main` (squash merge) and drives
  versioning and the changelog via release-please. It must follow Conventional Commits:

      <type>(<scope>): <short description in imperative mood>

  - type:   what kind of change this is (see list below)
  - scope:  optional, the part of stepline that is affected, e.g.
            assertions, steps, metadata, log, cli, render, pytest, docs, ci
  - description: lowercase, no trailing period, max. ~72 characters,
            written as a command ("add", "fix", "remove" – not "added", "fixes")

  Types and when to use them:

  feat      A new feature or new public API for users.
            → triggers a MINOR release (0.3.0 → 0.4.0) and appears under "Features".
            e.g.  feat(assertions): add is_close_to to NumericAssertion
                  feat(cli): add `stepline spec export` command

  fix       A bug fix that users can notice.
            → triggers a PATCH release (0.4.0 → 0.4.1) and appears under "Bug Fixes".
            e.g.  fix(steps): keep step order when using async steps
                  fix(render): avoid broken box characters on legacy Windows consoles

  perf      A change that makes stepline faster or lighter without changing behavior.
            → triggers a PATCH release and appears under "Performance".
            e.g.  perf(pytest): cache metadata lookup during collection

  docs      Documentation only: README, docs site, docstrings, examples.
            → no release.
            e.g.  docs(steps): add how-to for CRUD flows with blocked steps

  refactor  Code restructuring that changes neither behavior nor public API.
            → no release.
            e.g.  refactor(core): split Failure formatting into its own module

  test      Adding or improving tests only.
            → no release.
            e.g.  test(assertions): add hypothesis tests for is_multiple_of

  build     Packaging, dependencies, build configuration (pyproject.toml, uv.lock).
            → no release.
            e.g.  build: bump rich to 14.x

  ci        GitHub Actions workflows and other CI configuration.
            → no release.
            e.g.  ci: run test matrix on windows and macos

  chore     Maintenance that fits nowhere else (tooling config, repo housekeeping).
            → no release.
            e.g.  chore: configure pre-commit hooks

  revert    Reverts an earlier commit.
            e.g.  revert: feat(cli): add `stepline spec export` command

  Breaking changes:
  Add `!` after the type/scope when existing user code would stop working
  (renamed or removed API, changed default behavior). Explain the migration
  in the PR description under "BREAKING CHANGE:".
            → before 1.0: MINOR release; from 1.0 on: MAJOR release.
            e.g.  feat(steps)!: rename `on_error` to `on_failure`
-->

- [ ] `feat` – new feature or public API
- [ ] `fix` – bug fix
- [ ] `perf` – performance improvement
- [ ] `docs` – documentation only
- [ ] `refactor` – restructuring without behavior change
- [ ] `test` – tests only
- [ ] `build` / `ci` / `chore` – packaging, CI, maintenance
- [ ] Breaking change (title uses `!`, migration explained below)

## Checklist

- [ ] Tests added or updated, all green locally
- [ ] Public API has complete docstrings with an example
- [ ] Documentation updated (if user-facing)
- [ ] Type checks pass (`pyright`)
- [ ] Tried it out in a real test project (if user-facing)
