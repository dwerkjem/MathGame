import matplotlib.pyplot as plt
import numpy as np

from math_game.modules import points


def test_build_spline():
    spline_func = points.score_function
    # graph the spline and save it
    x = np.linspace(0, 120, 1000)
    y = spline_func(x)
    plt.plot(x, y)
    plt.xlabel("Time (s)")
    plt.ylabel("Points")
    plt.title("Spline Interpolation for Points")
    plt.grid()
    plt.savefig("tests/test_modules/test_points.png")

    # check the spline at some points
    assert spline_func(0) == 100
    assert spline_func(15) == 50
    assert spline_func(30) == 25
