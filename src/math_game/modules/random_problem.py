import ast
import math
import operator
import random
import re


class RandomProblem:
    def __init__(self, floats=False, max_number=20):
        self.floats = floats
        self.max_number = max_number
        self.operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
        }

    def safe_eval(self, expr):
        """
        Safely evaluate a simple arithmetic expression.
        """
        try:
            node = ast.parse(expr, mode="eval").body
            return self._eval_node(node)
        except Exception:
            raise ValueError("Invalid expression")

    def _eval_node(self, node):
        if isinstance(node, ast.Constant):  # number node (e.g. 1, 2, 3)
            return node.value
        elif isinstance(node, ast.BinOp):  # operator node (e.g. +, -, *, /)
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            op_type = type(node.op)
            if op_type in self.operators:
                return self.operators[op_type](left, right)
            else:
                raise ValueError("Unsupported operator")
        else:
            raise ValueError("Unsupported expression")

    def evaluate(self, question: str, answer: str) -> bool:
        answer = re.sub(r"\s+", "", answer)
        try:
            correct_answer_value = self.safe_eval(question)
            user_answer = float(answer)
            if self.floats:
                return math.isclose(user_answer, correct_answer_value, rel_tol=1e-9)
            else:
                return user_answer == correct_answer_value
        except Exception:
            return False

    def random_problem(self) -> str:
        operation = self.random_operation()
        if self.floats:
            val1 = self.random_value()
            val2 = self.random_value()
            question = f"{val1} {operation} {val2}"
        else:
            if operation == "/":
                divider = self.random_value()
                # Ensure divider is not zero
                while divider == 0:
                    divider = self.random_value()
                dividend = self.random_value()
                question = f"{divider * dividend}/{divider}"
            else:
                val1 = self.random_value()
                val2 = self.random_value()
                question = f"{val1} {operation} {val2}"
        return question

    def random_operation(self) -> str:
        return random.choice(["+", "-", "*", "/"])

    def random_value(self) -> int:
        return random.randint(0, self.max_number)

    def number_of_zeros(self, number: int) -> int:
        return len(re.findall(r"0", str(number)))

    def __str__(self):
        return f"RandomProblem(floats={self.floats}, max_number={self.max_number})"


if __name__ == "__main__":
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
