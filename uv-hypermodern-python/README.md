# Uv Hypermodern Python

[![PyPI](https://img.shields.io/pypi/v/uv-hypermodern-python.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/uv-hypermodern-python.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/uv-hypermodern-python)][pypi status]
[![License](https://img.shields.io/pypi/l/uv-hypermodern-python)][license]

[![Read the documentation at https://uv-hypermodern-python.readthedocs.io/](https://img.shields.io/readthedocs/uv-hypermodern-python/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/bosd/uv-hypermodern-python/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/bosd/uv-hypermodern-python/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Ruff codestyle][ruff badge]][ruff project]

[pypi status]: https://pypi.org/project/uv-hypermodern-python/
[read the docs]: https://uv-hypermodern-python.readthedocs.io/
[tests]: https://github.com/bosd/uv-hypermodern-python/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/bosd/uv-hypermodern-python
[pre-commit]: https://github.com/pre-commit/pre-commit
[ruff badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff project]: https://github.com/charliermarsh/ruff

## Features

- TODO

## Requirements

- TODO

## Installation

You can install _Uv Hypermodern Python_ via [pip] from [PyPI]. The package is distributed as a pure Python package, but also with pre-compiled wheels for major platforms, which include performance optimizations.

```console
$ pip install uv-hypermodern-python
```

The pre-compiled wheels are built using `mypyc` and will be used automatically if your platform is supported. You can check the files on PyPI to see the list of available wheels.

## Usage

Please see the [Command-line Reference] for details.

## Development

To contribute to this project, please see the [Contributor Guide].

### Mypyc Compilation

This project can be compiled with `mypyc` to produce a high-performance version of the package. The compilation is optional and is controlled by an environment variable.

To build and install the compiled version locally, you can use the `tests_compiled` nox session:

```console
$ nox -s tests_compiled
```

This will set the `UV_HYPERMODERN_PYTHON_COMPILE_MYPYC=1` environment variable, which triggers the compilation logic in `setup.py`. The compiled package will be installed in editable mode in a new virtual environment.

You can also build the compiled wheels for distribution using the `cibuildwheel` workflow, which is configured to run on releases. If you want to build the wheels locally, you can use `cibuildwheel` directly:

```console
$ pip install cibuildwheel
$ export UV_HYPERMODERN_PYTHON_COMPILE_MYPYC=1
$ cibuildwheel --output-dir wheelhouse
```

This will create the compiled wheels in the `wheelhouse` directory.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Uv Hypermodern Python_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [uv hypermodern python cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[uv hypermodern python cookiecutter]: https://github.com/bosd/cookiecutter-uv-hypermodern-python
[file an issue]: https://github.com/bosd/uv-hypermodern-python/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/bosd/uv-hypermodern-python/blob/main/LICENSE
[contributor guide]: https://github.com/bosd/uv-hypermodern-python/blob/main/CONTRIBUTING.md
[command-line reference]: https://uv-hypermodern-python.readthedocs.io/en/latest/usage.html
