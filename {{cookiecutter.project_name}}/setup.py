"""This file handles the mypyc compilation settings.

It is configured to conditionally compile the project's Python modules into C
extensions using mypyc, based on the presence of an environment variable.
This allows for producing both pure Python and compiled wheels.
"""

import os

from setuptools import setup

# The 'mypycify' function is not available in a stock 'setuptools' environment,
# so we only import it when we're actually going to use it. This allows the
# project to be installed in environments where 'mypy' is not present.
if os.environ.get("{{cookiecutter.package_name | upper}}_COMPILE_MYPYC") == "1":
    from mypyc.build import mypycify


def get_ext_modules():
    """Conditionally builds mypyc C extensions.

    If the `{{cookiecutter.package_name | upper}}_COMPILE_MYPYC` environment variable is set to "1",
    this function will return a list of modules to be compiled by mypyc.
    Otherwise, it returns an empty list, resulting in a pure Python build.
    """
    if os.environ.get("{{cookiecutter.package_name | upper}}_COMPILE_MYPYC") == "1":
        print("Compiling with mypyc...")
        # Add the paths to the Python modules you want to compile here.
        # For example:
        # return mypycify([
        #     "src/{{cookiecutter.package_name}}/__main__.py",
        #     "src/{{cookiecutter.package_name}}/some_other_module.py",
        # ])
        return mypycify(
            [
                "src/{{cookiecutter.package_name}}/__main__.py",
            ]
        )

    print("Skipping mypyc compilation. Building pure Python package...")
    return []


setup(
    # Most of the project metadata is configured in `pyproject.toml`.
    # This `setup.py` is primarily used for the conditional mypyc compilation.
    ext_modules=get_ext_modules(),
)
