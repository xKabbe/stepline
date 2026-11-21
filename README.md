<p align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/xKabbe/stepline/main/docs/assets/brand/stepline-logo-tagline-800.png">
        <img src="https://raw.githubusercontent.com/xKabbe/stepline/main/docs/assets/brand/stepline-logo-tagline-on-light-800.png" alt="stepline – Step by step. Line by line.">
    </picture>
</p>

<p align="center">
    <a href="https://pypi.org/project/pytest-stepline/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/pytest-stepline?label=PyPI&color=22d3ee&logo=pypi&logoColor=FFD242"></a>
    <a href="https://pypi.org/project/pytest-stepline/"><img alt="Supported Python versions" src="https://img.shields.io/pypi/pyversions/pytest-stepline?label=Python&color=45abf1&logo=python&logoColor=FFD43B"></a>
    <a href="https://docs.pytest.org/en/stable/"><img alt="pytest plugin" src="https://img.shields.io/badge/pytest-plugin-6884f3?logo=pytest&logoColor=0A9EDC"></a>
    <a href="https://github.com/xKabbe/stepline/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/pytest-stepline?label=License&color=8b5cf6&logo=opensourceinitiative&logoColor=3DA639"></a>
</p>

<p align="center">
    <a href="https://github.com/xKabbe/stepline/actions/workflows/ci.yml"><img alt="CI status" src="https://img.shields.io/github/actions/workflow/status/xKabbe/stepline/ci.yml?branch=main&label=CI&logo=githubactions"></a>
    <a href="https://github.com/xKabbe/stepline/actions/workflows/ci.yml"><img alt="Coverage 100 %" src="https://img.shields.io/badge/coverage-100%25-brightgreen"></a>
    <a href="https://xkabbe.github.io/stepline/"><img alt="Documentation build" src="https://img.shields.io/github/actions/workflow/status/xKabbe/stepline/docs.yml?branch=main&label=docs&logo=readthedocs"></a>
    <a href="https://github.com/microsoft/pyright"><img alt="Checked with pyright (strict)" src="https://img.shields.io/badge/types-pyright%20strict-blue"></a>
    <a href="https://github.com/astral-sh/ruff"><img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>
    <a href="https://github.com/astral-sh/uv"><img alt="uv" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json"></a>
    <a href="https://zensical.org/"><img alt="Built with Zensical" src="https://img.shields.io/badge/built%20with-Zensical-0f172a?logo=zensical"></a>
    <a href="https://www.conventionalcommits.org"><img alt="Conventional Commits" src="https://img.shields.io/badge/commits-conventional-fe5196?logo=conventionalcommits"></a>
</p>

<p align="center">
    <a href="https://xkabbe.github.io/stepline/">Documentation</a> ·
    <a href="https://pypi.org/project/pytest-stepline/">PyPI</a> ·
    <a href="https://github.com/xKabbe/stepline/blob/main/CHANGELOG.md">Changelog</a> ·
    <a href="https://github.com/xKabbe/stepline/milestones">Roadmap</a> ·
    <a href="https://github.com/xKabbe/stepline/releases">Releases</a>
</p>

---

`stepline` is a [pytest](https://docs.pytest.org) companion library for structured, readable tests:
steps that show what a test does, typed assertions that say what went wrong, and test documentation that lives right next to the code.

> [!NOTE]
> **Early development:** stepline is in alpha.
> Most features are still being built, and APIs may change between releases.

## Features

|    | Feature                                                                                   |
|----|-------------------------------------------------------------------------------------------|
| 👣 | **Steps**: structure tests into named steps, as a context manager or decorator            |
| 🎯 | **Typed assertions**: fluent `assert_that(...)` with clear failure messages               |
| 🏷️ | **Test metadata**: decorators for descriptions and issue links, plus a spec export        |
| 📜 | **Console output**: modern, rich-based logging of steps and results                       |
| ⏱️  | **Performance**: measure and check how long steps and tests take                          |
| 🧩 | **pytest plugin**: works out of the box with your existing pytest setup                   |
| 💻 | **Command-line tool**: inspect your setup and export test documentation from the terminal |

## Installation

stepline requires **Python 3.15** or newer.
It is a test tool, so add it as a development dependency:

```bash
# with uv
uv add --dev pytest-stepline

# with pip
pip install pytest-stepline
```

The package is called `pytest-stepline` on PyPI.
In your code, on the command line and in pytest, it is simply `stepline`.

## Quick check

After installation, pytest picks up the plugin automatically:

```console
$ pytest
=========================== test session starts ===========================
platform linux -- Python 3.15.2, pytest-9.2.0, pluggy-1.7.0
├─ stepline 0.0.1 · Python 3.15.2 · pytest 9.2.0
...
```

The command-line tool shows the installed version and your environment:

```bash
stepline --version
```

<p align="center">
    <img src="https://raw.githubusercontent.com/xKabbe/stepline/main/docs/assets/version-command.png" alt="stepline --version" width="640">
</p>

To switch the plugin off for a single run, use `pytest -p no:stepline`.

## Contributing

stepline is currently a personal project in early development and does not accept contributions yet.
This may change once the foundation is in place.
The [contributing guide](https://github.com/xKabbe/stepline/blob/main/.github/CONTRIBUTING.md) describes the development setup.

## License

stepline is released under the [MIT License](https://github.com/xKabbe/stepline/blob/main/LICENSE).
