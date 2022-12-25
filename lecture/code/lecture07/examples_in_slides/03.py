#!/usr/bin/env python3
def Complex(r, i):
    """
    Construct a complex number
    Arguments:
        r: real part
        i: imaginary part
    """
    def implementation(method):
        if method.lower() == 'real':
            return r
        elif method.lower() == 'imag':
            return i
        elif method.lower() == 'string':
            return f"{r:e} + i{i:e}"

    return implementation


z = Complex(1, 2)
print(z('real'), z('imag'), z('string'))
