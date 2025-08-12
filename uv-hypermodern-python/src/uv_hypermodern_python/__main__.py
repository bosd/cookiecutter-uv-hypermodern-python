"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Uv Hypermodern Python."""


if __name__ == "__main__":
    main(prog_name="uv-hypermodern-python")  # pragma: no cover
