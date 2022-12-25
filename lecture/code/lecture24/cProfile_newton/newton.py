#!/usr/bin/env python3
# File       : newton.py
# Description: Newton's method with exact and FD approximated Jacobian
# Copyright 2022 Harvard University. All Rights Reserved.
import cProfile
import numpy as np

f = lambda x: x - np.exp(-2.0 * np.sin(4.0 * x) * np.sin(4.0 * x))
J = lambda x: 1.0 + 16.0 * np.exp(-2.0 * np.sin(4.0 * x)**2) * np.sin(4.0 * x) * np.cos(4.0 * x)

def J_fd(eps):
    """Returns finite-difference function object for given discretization `eps`."""
    return lambda x: (f(x + eps) - f(x)) / eps


def newton(f, J, x_k, tol=1.0e-8, max_it=100):
    """Newton-Raphson method."""
    root = None
    for k in range(max_it):
        dx_k = -f(x_k) / J(x_k)
        if abs(dx_k) < tol:
            root = x_k + dx_k
            print(f"Found root {root:e} at iteration {k+1}")
            break
        print(f"Iteration {k+1}: Delta x = {dx_k:e}")
        x_k += dx_k
    return root


def main(J):
    """
    Main function with specific Jacobian `J`.

    Parameters
    ----------
    J : function
        Jacobian function object to be used in the Newton-Raphson method.

    """
    newton(f, J, 0.1, 1.0e-8, 100)


if __name__ == "__main__":
    # TODO: implement the three cProfile calls here:
    # 1. Profile the exact Jacobian and save it in file `exact`
    # 2. Profile the FD Jacobian with eps=1.0e-1 and save it in file `approx_coarse`
    # 3. Profile the FD Jacobian with eps=1.0e-8 and save it in file `approx_fine`
    pass
