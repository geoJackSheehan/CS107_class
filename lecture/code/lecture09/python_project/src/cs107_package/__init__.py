import importlib.metadata
from .subpkg_1 import (foo, bar)
from .subpkg_2 import baz

# The following will get the version of your project from the `setup.cfg`
# configuration:
__version__ = importlib.metadata.version('Fall2022_CS107')

__all__ = ['foo', 'bar', 'baz']
