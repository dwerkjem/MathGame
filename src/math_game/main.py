"""
Main module for the Simple Math Game.

This module contains the main function that runs the game.
"""

from rich import print
from rich.prompt import Prompt


from math_game.modules.random_problem import RandomProblem


def main():
    i = 0
    print("[bold] Welcome to [green]Simple Math Game![/bold]")
    max_number = Prompt.ask("Enter the maximum number to use in the game:", default="10")
    floats = Prompt.ask("Allow floating-point numbers? [y/n]", default="n").lower() == "y"
    number_of_problems = Prompt.ask("Enter the number of problems to solve:", default="10")

    rp = RandomProblem( max_number=int(max_number), floats=floats)
    while i < int(number_of_problems):
        question = rp.random_problem()
        print(question)
        answer = input("Answer: ")
        if rp.evaluate(question, answer):
            print("Correct!")
            i += 1
        else:
            print("Incorrect!")
            i += 1

if __name__ == "__main__":
    main()
