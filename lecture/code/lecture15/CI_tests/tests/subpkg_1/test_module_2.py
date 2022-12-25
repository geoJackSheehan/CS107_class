"""
This test suite (a module) runs tests for subpkg_1.module_2 of the
cs107_package.
"""

# Let us use `pytest` this time
import pytest

# project code to test (requires `cs107_package` to be in PYTHONPATH)
from cs107_package.subpkg_1.module_2 import (bar)


class TestFunctions:
    """We do not inherit from unittest.TestCase for pytest's!"""

    def test_bar(self):
        """
        This is just a trivial test to check the return value of function `bar`.
        """
        # assert the return value of bar() (note that this uses Python's
        # `assert` statement directly, no need to inherit from anything!)
        assert bar() == "cs107_package.subpkg_1.module_2.bar()"


# ==============================================================================
# A test function unrelated to `cs107_package`.  It is here to demonstrate the
# feature of `pytest` used in `test_example_function` below.
def example_function():
    """If you have code that raises exceptions, pytest can verify them."""
    raise RuntimeError("This function should not be called")


def test_example_function():
    with pytest.raises(RuntimeError):
        example_function()


# ==============================================================================

if __name__ == "__main__":
    # can use this to run the test module standalone
    pytest.main()
