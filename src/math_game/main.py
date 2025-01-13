"""
Main module for the Simple Math Game.

This module contains the main function that runs the game.
"""

import time

from rich import print
from rich.prompt import Prompt


from math_game.modules.random_problem import RandomProblem
from math_game.modules.points import score_function

def main():
    i = 0
    print("[bold] Welcome to [green]Simple Math Game![/bold]")
    max_number = Prompt.ask("Enter the maximum number to use in the game:", default="10")
    floats = Prompt.ask("Allow floating-point numbers? [y/n]", default="n").lower() == "y"
    number_of_problems = Prompt.ask("Enter the number of problems to solve:", default="10")
    total_score = 0
    rp = RandomProblem( max_number=int(max_number), floats=floats)
    while i < int(number_of_problems):
        question = rp.random_problem()
        print(question)
        start_time = time.time()
        answer = input("Answer: ")
        if rp.evaluate(question, answer):
            print("Correct!")
            end_time = time.time()
            time_elapsed = end_time - start_time
            score = score_function(time_elapsed)
            print(f"Score: [bold]{score:.2f}[/bold] points")
            total_score += score
            i += 1
        else:
            print("Incorrect!")
            i += 1
    print("Game over!")
    print(f"Your final score is: [bold]{total_score:.2f}[/bold] points")
if __name__ == "__main__":
    main()
