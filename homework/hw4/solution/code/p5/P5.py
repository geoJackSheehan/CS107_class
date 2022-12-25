#!/usr/bin/env python3
# File       : P5.py
# Description: Dual number with support for addition and multiplication
# Copyright 2022 Harvard University. All Rights Reserved.


class DualNumber:
    """Simple dual number object (lecture 12)"""

    def __init__(self, real, dual=1):
        self.real = real
        self.dual = dual

    def __add__(self, other):
        if not isinstance(other, (int, float, DualNumber)):
            raise TypeError(f"Unsupported type `{type(other)}`")
        if isinstance(other, (int, float)):
            # scalar numbers
            return DualNumber(other + self.real, self.dual)
        else:
            # dual number
            return DualNumber(self.real + other.real, self.dual + other.dual)

    def __mul__(self, other):
        if not isinstance(other, (int, float, DualNumber)):
            raise TypeError(f"Unsupported type `{type(other)}`")
        if isinstance(other, (int, float)):
            # scalar numbers
            return DualNumber(other * self.real, other * self.dual)
        else:
            # dual number
            return DualNumber(
                self.real * other.real,
                self.real * other.dual + self.dual * other.real
            )

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == "__main__":
    x1 = 0.5
    z = DualNumber(x1)
    a0 = 2.0
    a1 = 2.5
    a2 = 3.0
    f = a0 + z * a2 * z + a1 * z
    print(f.real)
    print(f.dual)
