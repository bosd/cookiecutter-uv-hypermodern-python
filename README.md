# cookiecutter-uv-hypermodern-python

<!-- badges-begin -->

[![Status][status badge]][status badge]
[![Python Version][python version badge]][github page]
[![CalVer][calver badge]][calver]
[![License][license badge]][license]<br>
[![Read the documentation][readthedocs badge]][readthedocs page]
[![Tests][github actions badge]][github actions page]
[![Codecov][codecov badge]][codecov page]<br>
[![pre-commit enabled][pre-commit badge]][pre-commit project]
[![Ruff codestyle][ruff badge]][ruff project]
[![Contributor Covenant][contributor covenant badge]][code of conduct]

[ruff badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff project]: https://github.com/charliermarsh/ruff
[calver badge]: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
[calver]: https://calver.org/
[code of conduct]: https://github.com/bosd/cookiecutter-uv-hypermodern-python/blob/main/CODE_OF_CONDUCT.md
[codecov badge]: https://codecov.io/gh/bosd/cookiecutter-uv-hypermodern-python-instance/branch/main/graph/badge.svg
[codecov page]: https://codecov.io/gh/bosd/cookiecutter-uv-hypermodern-python-instance
[contributor covenant badge]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
[github actions badge]: https://github.com/bosd/cookiecutter-uv-hypermodern-python/workflows/Tests/badge.svg
[github actions page]: https://github.com/bosd/cookiecutter-uv-hypermodern-python/actions?workflow=Tests
[github page]: https://github.com/bosd/cookiecutter-uv-hypermodern-python
[license badge]: https://img.shields.io/github/license/bosd/cookiecutter-uv-hypermodern-python
[license]: https://opensource.org/license/mit
[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit project]: https://pre-commit.com/
[python version badge]: https://img.shields.io/pypi/pyversions/cookiecutter-uv-hypermodern-python-instance
[readthedocs badge]: https://img.shields.io/readthedocs/cookiecutter-uv-hypermodern-python/latest.svg?label=Read%20the%20Docs
[readthedocs page]: https://cookiecutter-uv-hypermodern-python.readthedocs.io/
[status badge]: https://badgen.net/badge/status/alpha/d8624d

<!-- badges-end -->

<p align="center"><img alt="logo" src="docs/_static/logo.png" width="50%" /></p>

[Cookiecutter] template for a Python package based on the
[Hypermodern Python] article series.

✨📚✨ [Read the full documentation][readthedocs page]

[cookiecutter]: https://github.com/audreyr/cookiecutter
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769

## Usage

```console
cookiecutter gh:bosd/cookiecutter-uv-hypermodern-python --checkout=2022.6.3
```

## Features

<!-- features-begin -->

- Packaging and dependency management with [uv]
- Test automation with [Nox]
- Linting with [pre-commit] and [ruff]
- Continuous integration with [GitHub Actions]
- Documentation with [Sphinx], [MyST], and [Read the Docs] using the [furo] theme
- Automated uploads to [PyPI] and [TestPyPI]
- Automated release notes with [Release Drafter]
- Automated dependency updates with [Dependabot]
- Code formatting with [ruff] and [Prettier]
- Import sorting with [ruff]
- Testing with [pytest]
- Code coverage with [Coverage.py]
- Coverage reporting with [Codecov]
- Command-line interface with [Click]
- Static type-checking with [mypy]
- Runtime type-checking with [Typeguard]
- Check documentation examples with [xdoctest]
- Generate API documentation with [autodoc] and [napoleon]
- Generate command-line reference with [sphinx-click]
- Manage project labels with [GitHub Labeler]

The template supports Python 3.9, 3.10, 3.11, 3.12 and 3.13.

[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[click]: https://click.palletsprojects.com/
[codecov]: https://codecov.io/
[coverage.py]: https://coverage.readthedocs.io/
[dependabot]: https://github.com/dependabot/dependabot-core
[furo]: https://pradyunsg.me/furo/
[github actions]: https://github.com/features/actions
[github labeler]: https://github.com/marketplace/actions/github-labeler
[mypy]: https://mypy-lang.org/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[uv]: https://docs.astral.sh/uv/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[pypi]: https://pypi.org/
[pytest]: https://docs.pytest.org/en/latest/
[read the docs]: https://readthedocs.org/
[release drafter]: https://github.com/release-drafter/release-drafter
[ruff]: https://github.com/astral-sh/ruff
[sphinx]: https://www.sphinx-doc.org/
[sphinx-click]: https://sphinx-click.readthedocs.io/
[testpypi]: https://test.pypi.org/
[typeguard]: https://github.com/agronholm/typeguard
[xdoctest]: https://github.com/Erotemic/xdoctest

<!-- features-end -->
