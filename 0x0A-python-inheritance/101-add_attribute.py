#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, name, val):
    """
    adds a new attribute to an object if it’s possible
    """
    obj.__dict__[name] = val
