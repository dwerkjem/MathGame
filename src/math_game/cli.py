"""Console script for math_game."""
import math_game

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for math_game."""
    console.print("Replace this message by putting your code into "
               "math_game.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
