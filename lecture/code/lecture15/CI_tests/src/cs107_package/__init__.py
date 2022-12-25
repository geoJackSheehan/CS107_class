"""Docstring for cs107_package test package

Some Python features were discussed using this package related to packaging and
distribution of Python packages in lecture 9.

"""

from .subpkg_1 import (foo, bar)
from .subpkg_2 import baz
from .example import foo as numpy_example

__all__ = ['foo', 'bar', 'baz', 'numpy_example']
