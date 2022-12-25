#!/usr/bin/env python3
# File       : exercise_2.py
# Description: Implementation examples of forward mode AD
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np

# a.)
class derivative:
    """Functor for function decoration adding derivatives
    """

    def __init__(self, Dpf=None):
        self.Dpf = Dpf  # save state from @decorator argument, only needed for a.)

    def __call__(self, f):
        """Outer function of closure takes wrapped function f as an argument.
        """

        def closure(x, p=None):
            # check if dimensions are good
            if p is None:
                p = np.zeros(x.shape)
            else:
                assert len(p) == len(
                    x
                ), f"Seed vector must have same dimension as input vector"

            if self.Dpf is not None:
                # a.) return function evaluation and evaluate directional
                # derivative which must be provided via the decorator (not
                # automatic)
                return np.array([f(x), self.Dpf(x, p)])
            else:
                # assumes x is a list of dual numbers, no derivative has been
                # specified!  The for-loop initializes the dual part to the seed
                # vector contents
                for z, s in zip(x, p):
                    assert isinstance(z, DualNumber)
                    z.dual = s
                # b.) evaluate function only, dual numbers take care of rest
                return f(x)

        return closure

# b.)
class DualNumber():
    """Simple dual number class"""

    def __init__(self, real, dual=0.0):
        self.real = real
        self.dual = dual  # corresponds to D_p initial value

    def __add__(self, other):
        assert isinstance(
            other, DualNumber
        ), f'The object {other} is not a DualNumber'
        return DualNumber(self.real + other.real, self.dual + other.dual)

    def __mul__(self, other):
        assert isinstance(
            other, DualNumber
        ), f'The object {other} is not a DualNumber'
        return DualNumber(
            self.real * other.real,
            self.real * other.dual + self.dual * other.real
        )

    def __repr__(self):
        return f"DualNumber(real={self.real:e}, dual={self.dual:e})"


def main():

    x = np.ones((2,))  # point of evaluation

    # a.)
    @derivative(lambda x, p: 2.0 * (x[0] * p[0] + x[1] * p[1]))
    def f(x):
        return x[0] * x[0] + x[1] * x[1]

    print(f(x, p=[1, 0]))
    print(f(x, p=[0, 1]))
    print(f(x, p=[1, 1]))

    # b.) Note: the decorator is technically not needed for part b.), it is used
    # in the solution here to stress that the derivative is not needed at all
    # (using the None keyword)!
    @derivative(None)
    def f(x):
        return x[0] * x[0] + x[1] * x[1]

    z = np.array([DualNumber(v) for v in x])
    print(f(z, p=[1, 0]))
    print(f(z, p=[0, 1]))
    print(f(z, p=[1, 1]))


if __name__ == "__main__":
    main()
