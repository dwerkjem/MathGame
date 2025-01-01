import matplotlib.pyplot as plt
import numpy as np

from math_game.modules import points


def test_build_spline():
    spline_func = points.build_spline()
    # graph the spline and save it
    x = np.linspace(0, 300, 1000)
    y = spline_func(x)
    plt.plot(x, y)
    plt.xlabel("Time (s)")
    plt.ylabel("Points")
    plt.title("Spline Interpolation for Points")
    plt.grid()
    plt.savefig("spline.png")
