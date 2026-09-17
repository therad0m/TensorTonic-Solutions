import numpy as np


"ndarray is n-dimensional array"
def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    return 1 / (1 + np.exp(-x))