"""
This is the docstring for ./subpkg_2/module_3.py.  This module provides one
function `baz`.  Example usage is:

>>> baz(0)
0
"""


def baz(x):
    """
    Return the input x if it is an int or float.

    Parameters
    ----------
    x : input argument

    Returns
    -------
    x : If it is of type int or float

    Examples
    --------
    >>> baz(0)
    0

    >>> baz(0.0)
    0.0

    >>> baz('a string')
    Traceback (most recent call last):
        ...
    ValueError: x must be int or float
    """
    if not isinstance(x, (int, float)):
        raise ValueError('x must be int or float')
    return x
