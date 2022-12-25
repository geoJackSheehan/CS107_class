# File       : P6.py
# Description: Untested complex number implementation
# Copyright 2022 Harvard University. All Rights Reserved.


class Complex:
    """Untested class for complex numbers"""

    _supported_types = (int, float)

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for addition"
            )
        else:  # supported scalar types
            return Complex(self.real + other, self.imag)

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(
                self.real * other.real - self.imag * other.imag,
                self.real * other.imag + other.real * self.imag
            )
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for multiplication"
            )
        else:  # supported scalar types
            return Complex(self.real * other, self.imag * other)

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)
