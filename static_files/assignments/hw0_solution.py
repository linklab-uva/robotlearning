import torch
import numpy as np

class HW0Solution:
    def __init__(self):
        pass

    # Simulate the system Ax+b for one timestep using the given initial conditions
    # A = NxN numpy array
    # b = 1D N numpy array
    # init_cond = N x 1 x M numpy array (M different initial conditions)
    # return = N x 1 x M numpy array (M different initial conditions)
    def sim_systems(self, A, b, init_cond):
        return 0

    # Compute the partial derivatives (gradients) of a multi-dimensional function.
    # dx = Scalar value showing distance between discrete samples
    # y = N-dimentional numpy array of sample points at regular intervals.
    #   -For the 2D case, y is N x N
    # returns = gradient (as torch tensor) at every point in y.
    #   -For the 2D case, return 2 x (N-1) x (N-1).  The first 2 channels are the x and y components
    def compute_derivative(self, dx, y):
        return 0
