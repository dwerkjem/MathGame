"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Hypermodern Simple Math Game."""


if __name__ == "__main__":
    main(prog_name="hypermodern-simple-math-game")  # pragma: no cover
