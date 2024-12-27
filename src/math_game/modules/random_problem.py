import random
import re
from typing import List, Literal, Union


class RandomProblem:
    def __init__(
        self,
        operations: List[Literal["+", "-", "*", "/"]] = ["+", "-", "*"],
        max_number: int = 20,
        floats: bool = False,
        precision: int = 2,
    ):
        self.operations = operations
        self.max_number = max_number
        self.floats = floats
        self.precision = precision

    def number_of_zeros(self, number: int) -> int:
        length = len(str(number))
        return str(number).zfill(length).count("0")

    def random_value(self) -> Union[int, float]:
        if self.floats:
            return round(random.uniform(0, self.max_number), self.precision)
        return random.randint(0, self.max_number)

    def random_operation(self) -> str:
        return random.choice(self.operations)

    def random_problem(self) -> str:
        question: str = (
            f"{self.random_value()} {self.random_operation()} {self.random_value()}"
        )
        return question

    def evaluate(self, question: str, answer: str) -> bool:
        # Use regex to remove any whitespace from the answer
        answer = re.sub(r"\s+", "", answer)

        # Evaluate the question and compare with the provided answer
        try:
            correct_answer = str(eval(question))
            return correct_answer == answer
        except Exception:
            return False
