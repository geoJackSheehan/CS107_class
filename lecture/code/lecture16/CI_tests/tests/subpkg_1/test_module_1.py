"""
This test suite (a module) runs tests for subpkg_1.module_1 of the
cs107_package.
"""

# Here we use `unittest` from the Python standard library
import unittest

# project code to test (requires `cs107_package` to be in PYTHONPATH)
from cs107_package.subpkg_1.module_1 import (Foo, foo)


# test classes must start with `Test` (classes are required for `unittest` tests)
class TestTypes(
    unittest.TestCase
):  # test classes must inherit from unittest.TestCase

    # test methods (functions) must be prepended with `test_`.
    def test_class_Foo(self):
        """
        This is just a trivial test to check that `Foo` is initialized
        correctly.  More tests associated to the class `Foo` could be written in
        this method.
        """
        f = Foo(1, 2)  # create instance
        self.assertEqual(f.a, 1)  # check attribute `a`
        self.assertEqual(f.b, 2)  # check attribute `b`


class TestFunctions(unittest.TestCase):

    def test_function_foo(self):
        """
        This is just a trivial test to check the return value of function `foo`.
        """
        # assert the return value of foo()
        self.assertEqual(foo(), "cs107_package.subpkg_1.module_1.foo()")


if __name__ == '__main__':
    # can use this to run the test module standalone
    unittest.main()
