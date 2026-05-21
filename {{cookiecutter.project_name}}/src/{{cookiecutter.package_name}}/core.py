"""Core library logic.

Put your performance-sensitive, fully typed business logic in modules like this
one. They are compiled to C extensions by mypyc when the project is built with
``{{cookiecutter.package_name | upper}}_COMPILE_MYPYC=1`` (see ``setup.py``).

Keep the Click command-line interface in ``__main__`` *out* of the compiled set:
Click's decorators set attributes on the function object, which is not possible
on a mypyc-compiled function.
"""


def greet(name: str) -> str:
    """Build a greeting for the given name.

    Args:
        name: The name to greet.

    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"
