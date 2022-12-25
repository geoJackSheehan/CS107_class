#!/usr/bin/env python3
# File       : newton_fd.py
# Description: Newton's method with approximate Jacobian representation
# Copyright 2021 Harvard University. All Rights Reserved.
import numpy as np

f = lambda x: x - np.exp(-2.0 * np.sin(4.0 * x) * np.sin(4.0 * x))
J = lambda x, eps: (
    f(x + eps) - f(x)
) / eps  # Finite-Difference approximation of J


def newton(f, J, x_k, tol=1.0e-8, max_it=100, eps=1.0e-8):
    root = None
    for k in range(max_it):
        dx_k = -f(x_k) / J(x_k, eps)
        if abs(dx_k) < tol:
            root = x_k + dx_k
            print(f"Found root {root:e} at iteration {k+1}")
            print(f(root))
            break
        print(f"Iteration {k+1}: Delta x = {dx_k:e}")
        x_k += dx_k
    return root


if __name__ == "__main__":
    import argparse

    def parse_args():
        # yapf: disable
        parser = argparse.ArgumentParser(description="Newton-Raphson Method")
        parser.add_argument('-g', '--initial_guess', type=float, help="Initial guess", required=True)
        parser.add_argument('-t', '--tolerance', type=float, default=1.0e-8, help="Convergence tolerance")
        parser.add_argument('-i', '--maximum_iterations', type=int, default=100, help="Maximum iterations")
        # yapf: enable
        return parser.parse_args()
        return parser.parse_args()

    args = parse_args()
    newton(f, J, args.initial_guess, args.tolerance, args.maximum_iterations)
