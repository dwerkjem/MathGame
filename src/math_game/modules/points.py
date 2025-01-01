import math

import numpy as np


def score_function(time_elapsed):
    """
    Compute the score based on the elapsed time:
    - Starts at 100 (instant answer).
    - Is exactly 50 points at 15 seconds.
    - Smoothly decays to approach 0 as time increases but never reaches 0.

    Args:
        time_elapsed (float): The time (in seconds) taken to answer.

    Returns:
        float: The score based on the response time.
    """
    # Constants for the decay function
    initial_score = 100  # Maximum score at t=0
    half_life = 15  # Time where score is 50 (3 times slower)
    decay_rate = (
        math.log(2) / half_life
    )  # Decay constant to ensure score is 50 at 15 sec

    # Calculate the score using exponential decay
    score = initial_score * np.exp(-decay_rate * time_elapsed)

    # Ensure score never goes below a small positive value (e.g., 0.01)
    return np.maximum(score, 0.01)
