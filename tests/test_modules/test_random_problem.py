import numpy as np

from math_game.modules import random_problem


def test_number_of_zeros():
    rp = random_problem.RandomProblem()
    assert rp.number_of_zeros(100) == 2
    assert rp.number_of_zeros(1000) == 3
    assert rp.number_of_zeros(100402) == 3
    assert rp.number_of_zeros(100402000) == 6


def test_random_value():
    rp = random_problem.RandomProblem()
    values = [rp.random_value() for _ in range(1000)]
    assert np.mean(values) >= 0
    assert np.mean(values) <= 20
    assert np.std(values) > 0

    rp = random_problem.RandomProblem(floats=True)
    values = [rp.random_value() for _ in range(1000)]
    assert np.mean(values) >= 0
    assert np.mean(values) <= 20
    assert np.std(values) > 0
    assert any(isinstance(value, float) for value in values)

    rp = random_problem.RandomProblem(max_number=10)
    values = [rp.random_value() for _ in range(1000)]
    assert np.mean(values) >= 0
    assert np.mean(values) <= 10
    assert np.std(values) > 0

    rp = random_problem.RandomProblem(floats=True, max_number=10)
    values = [rp.random_value() for _ in range(1000)]
    assert np.mean(values) >= 0
    assert np.mean(values) <= 10
    assert np.std(values) > 0
    assert any(isinstance(value, float) for value in values)
