"""
Main module for the Simple Math Game.

This module contains the main function that runs the game.
"""

from rich import print

from math_game.modules.random_problem import RandomProblem


def main():
    print("[bold] Welcome to [green]Simple Math Game![/bold]")

    rp = RandomProblem()
    while True:
        question = rp.random_problem()
        print(question)
        answer = input("Answer: ")
        if rp.evaluate(question, answer):
            print("Correct!")
        else:
            print("Incorrect!")
            break


if __name__ == "__main__":
    main()
