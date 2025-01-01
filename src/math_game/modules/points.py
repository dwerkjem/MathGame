import math
import time

import numpy as np
from scipy.interpolate import make_interp_spline


def build_spline():
    """
    Build a cubic spline that passes through the key points:
    t=0  -> 100 points
    t=5  -> 50  points
    t=30 -> 25  points

    Returns:
        A spline function f(t) valid for 0 <= t <= 30.
    """
    # Key time points
    x = np.array([0, 5, 30], dtype=float)
    # Corresponding scores
    y = np.array([100, 50, 25], dtype=float)

    # Create a cubic spline interpolant
    spline_func = make_interp_spline(x, y, k=3)
    return spline_func


def score_function(time_elapsed, spline_func):
    """
    Compute the score for a given time_elapsed using:
      1) The spline for t <= 30.
      2) A smooth exponential decay for t > 30.

    Args:
        time_elapsed (float): The time (in seconds) taken to answer.
        spline_func (callable): The spline function for 0 <= t <= 30.

    Returns:
        float: The score based on the response time.
    """
    if time_elapsed <= 0:
        # An "instant" response
        return 100.0
    elif time_elapsed <= 30:
        # Use the spline for times up to 30 seconds
        return max(
            0, float(spline_func(time_elapsed))
        )  # Clamp to avoid negative values
    else:
        # For times > 30, exponentially approach 0
        decay_factor = 0.03  # Adjust as desired
        score_at_30 = 25.0
        return max(
            0, float(score_at_30 * math.exp(-decay_factor * (time_elapsed - 30)))
        )
