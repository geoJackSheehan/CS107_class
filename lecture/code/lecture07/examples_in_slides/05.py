#!/usr/bin/env python3
class Complex():
    """Complex number type"""
    def __init__(self, real, imag):
        self.real = real  # real part
        self.imag = imag  # imaginary part


z = Complex(1, 2)
print(z.__dict__)
print(vars(z))
print(Complex)
print(type(z))
print(z.real)
print(z.imag)
