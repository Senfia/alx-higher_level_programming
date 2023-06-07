#!/usr/bin/python3
"""
This is the "add_integer" module.
Defines an integer addition function.
"""


def add_integer(a, b):
    """
    Returns the sum of a and b.
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (a + b)
