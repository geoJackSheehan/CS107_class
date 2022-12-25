# File       : test_P6.py
# Description: Test cases for testing Complex numbers addition and
#              multiplication
# Copyright 2022 Harvard University. All Rights Reserved.
import pytest

# import names to test
from P6 import Complex


class TestComplex:
    """Test class for complex types"""

    def test_init(self):
        real = 1
        imag = 2
        z = Complex(real, imag)
        assert z.real == real
        assert z.imag == imag

    def test_addition(self):
        z1 = Complex(1, 1)

        # complex addition
        z2 = Complex(2, 2)
        z3 = z1 + z2
        assert z3.real == 3
        assert z3.imag == 3

        # integer scalar
        int_scalar = int(2)
        z3 = z1 + int_scalar
        assert z3.real == 3
        assert z3.imag == 1

        # float scalar
        float_scalar = float(2)
        z3 = z1 + float_scalar
        assert z3.real == 3
        assert z3.imag == 1

        # check unsupported types throw errors
        with pytest.raises(TypeError):
            z1 + '1'
            '1' + z1

    def test_multiplication(self):
        z1 = Complex(1, 1)

        # complex addition
        z2 = Complex(2, 2)
        z3 = z1 * z2
        assert z3.real == 0
        assert z3.imag == 4

        # integer scalar
        int_scalar = int(2)
        z3 = z1 * int_scalar
        assert z3.real == 2
        assert z3.imag == 2

        # float scalar
        float_scalar = float(2)
        z3 = z1 * float_scalar
        assert z3.real == 2
        assert z3.imag == 2

        # check unsupported types throw errors
        with pytest.raises(TypeError):
            z1 * '1'
            '1' * z1

    def test_reflective_operators(self):
        z1 = Complex(1, 1)
        a = 2.0

        # addition
        z2 = a + z1
        assert z2.real == 3
        assert z2.imag == 1

        # multiplication
        z2 = a * z1
        assert z2.real == 2
        assert z2.imag == 2
