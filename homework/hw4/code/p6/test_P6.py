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
        # TODO: Test that complex numbers are initialized correctly
        pass

    def test_addition(self):
        # TODO: Test complex addition:
        #   The implementation only supports addition for mixed operands of type
        #   int, float or Complex.  You should test all three variants.
        #
        #   You should also test that the implementation throws a TypeError when
        #   other types are used for addition.  Use for example:
        #   with pytest.raises(TypeError):
        #       z1 + '1'
        #       '1' + z1
        pass

    def test_multiplication(self):
        # TODO: Test complex multiplication:
        #   The implementation only supports multiplication for mixed operands
        #   of type int, float or Complex.  You should test all three variants.
        #
        #   You should also test that the implementation throws a TypeError when
        #   other types are used for multiplication.  Use for example:
        #   with pytest.raises(TypeError):
        #       z1 * '1'
        #       '1' * z1
        pass

    def test_reflective_operators(self):
        # TODO: Test reflective operators for the Complex type (what happens
        # when you do `1 + z` instead of `z + 1` where `z` is a complex number).
        pass
