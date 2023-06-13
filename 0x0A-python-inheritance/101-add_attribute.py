#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
