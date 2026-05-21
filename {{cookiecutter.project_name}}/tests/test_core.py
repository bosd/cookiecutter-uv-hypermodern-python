"""Test cases for the core module."""

from {{cookiecutter.package_name}}.core import greet


def test_greet_returns_message() -> None:
    """It returns a greeting containing the name."""
    assert greet("world") == "Hello, world!"
