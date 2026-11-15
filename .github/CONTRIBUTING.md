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

### Pre-commit hooks

After `uv run pre-commit install`, a set of checks runs automatically on every commit:
formatting and linting with ruff, spell checking, lock file and workflow validation,
and basic file hygiene. The first run takes a moment while the hooks are installed.

If a hook fixes something (for example, formatting), the commit stops and the fixed
files are left unstaged. Review the changes, `git add` them and commit again.

Commits directly to `main` are blocked; please work on a branch.

## Everyday commands

[poethepoet](https://poethepoet.natn.io/) is installed with the dev dependencies.
Its tasks are defined in `poe_tasks.toml`.

### With `poe` (shortcuts)

```bash
uv run poe check          # run all checks, like CI does
uv run poe fix            # auto-fix lint findings and format all code
uv run poe hooks          # run all pre-commit hooks on all files

uv run poe format-check   # check formatting
uv run poe lint           # lint
uv run poe imports        # check import rules
uv run poe typecheck      # strict type checking
uv run poe test           # run the test suite (extra arguments are passed to pytest)
uv run poe cov            # run the test suite with a coverage report
uv run poe format         # format all code

uv run poe                # list all available tasks
```

### Without `poe` (the underlying commands)

```bash
uv run ruff format --check          # check formatting
uv run ruff check                   # lint
uv run lint-imports                 # check import rules
uv run pyright                      # strict type checking
uv run pytest                       # run the test suite
uv run pytest --cov                 # run the test suite with a coverage report
uv run ruff check --fix             # auto-fix lint findings
uv run ruff format                  # format all code
uv run pre-commit run --all-files   # run all pre-commit hooks on all files
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
