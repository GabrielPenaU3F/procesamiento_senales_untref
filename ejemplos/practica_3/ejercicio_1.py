import numpy as np


def punto_a(x_t):
    return [3 * x for x in x_t]

def punto_b(x_t):
    return [- 1 - x for x in x_t]

def punto_c(x_t):
    return [np.exp(x) for x in x_t]

