# Contributing to stepline

Thanks for your interest in stepline! Bug reports, ideas, documentation fixes and code
contributions are all welcome.

## Before you start

- **Bugs:** open an issue with the bug report template, including a minimal reproduction.
- **New features:** please open a feature request first, so we can agree on the API
  before you invest time in an implementation.
- **Questions:** use [GitHub Discussions](https://github.com/xKabbe/stepline/discussions).
- **Security issues:** never in public, see [SECURITY.md](SECURITY.md).

## Development setup

stepline uses [uv](https://docs.astral.sh/uv/) for everything.

```bash
  git clone git@github.com:xKabbe/stepline.git
  cd stepline
  uv sync                         # creates .venv with all dev dependencies
  uv run pre-commit install       # runs formatting and lint checks before each commit
```

## Everyday commands

```bash
  uv run pytest                   # run the test suite
  uv run ruff format              # format code
  uv run ruff check --fix         # lint and auto-fix
  uv run pyright                  # strict type checking
```

All of these also run in CI on Linux, Windows and macOS.

## Making a change

1. Create a branch from `main`, e.g. `feat/12-numeric-assertions` or `fix/14-nan-handling`.
2. Keep pull requests small and focused on one topic.
3. Open a pull request. **The PR title must follow
   [Conventional Commits](https://www.conventionalcommits.org/)**, for example
   `feat(assertions): add is_close_to`. The PR template explains all types and scopes.
4. Pull requests are squash-merged, so the PR title becomes the commit message on `main`
   and the entry in the changelog.

## What a good pull request includes

- Tests for new behavior or a fixed bug, all passing locally
- Complete Google-style docstrings with an example for every public function or method
- Type hints that pass `pyright` in strict mode
- Documentation updates for anything users will notice

## Releases

Releases are automated with release-please. You never need to bump versions or edit
`CHANGELOG.md` by hand; the maintainer merges the release PR when a milestone is complete.
