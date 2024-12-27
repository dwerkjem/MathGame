from math_game.modules import random_problem


def test_number_of_zeros():
    rp = random_problem.RandomProblem()
    assert rp.number_of_zeros(100) == 2
    assert rp.number_of_zeros(1000) == 3
    assert rp.number_of_zeros(100402) == 3
    assert rp.number_of_zeros(100402000) == 6
