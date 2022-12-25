#!/usr/bin/env python3
def Complex(r, i):
    """
    Construct a complex number
    Arguments:
        r: real part
        i: imaginary part
    """
    def implementation(method, z=None):
        nonlocal r, i
        if method.lower() == 'set_z':
            assert z is not None
            r, i = z
        elif method.lower() == 'real':
            return r
        elif method.lower() == 'imag':
            return i
        elif method.lower() == 'string':
            return f"{r:e} + i{i:e}"

    return implementation


z = Complex(1, 2)
z('set_z', (3, 4))
print(z('real'), z('imag'), z('string'))
