#!/usr/bin/python3
"""
This is module lookup.
It contains only one function.
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    Arguments:
        obj: any object
    Returns:
        a list
    """
    return dir(obj)
