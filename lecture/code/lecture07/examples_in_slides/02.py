#!/usr/bin/env python3
def Complex(r, i):
    """
    Construct a complex number
    Arguments:
        r: real part
        i: imaginary part
    """
    return (r, i)


# interface with complex numbers
def real(c):
    """Get the real part of a complex number c"""
    return c[0]


def imag(c):
    """Get the imaginary part of a complex number c"""
    return c[1]


def string(c):
    """Represent a complex number c as a string"""
    return f"{c[0]:e} + i{c[1]:e}"


z = Complex(1, 2)
print(real(z), imag(z), string(z))
