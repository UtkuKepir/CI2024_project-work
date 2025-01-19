# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html


# Notez bien: No need to include f0 -- it's just an example!
def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray:
    return 1 + np.exp(-(x[0] + x[1] + x[2]))

def f3(x: np.ndarray) -> np.ndarray:
    return np.cos(np.tan(x[0])) + (1 + np.exp(-x[1])) + x[2]

def f4(x: np.ndarray) -> np.ndarray:
    return np.exp(np.cos(x[0] * x[1]))

def f5(x: np.ndarray) -> np.ndarray:
    return np.cos(x[0]) * 0.02871653301747079 / x[1]

def f6(x: np.ndarray) -> np.ndarray:
    return np.cos(np.exp(1 / (1 + np.exp(-x[0])))) + x[1]

def f7(x: np.ndarray) -> np.ndarray:
    return np.exp(x[0] * x[1])

def f8(x: np.ndarray) -> np.ndarray:
    return ((np.exp(x[5]) * (np.exp(x[0]) + x[3])) - (np.tan(1 / x[1]) + x[2])) + x[4]