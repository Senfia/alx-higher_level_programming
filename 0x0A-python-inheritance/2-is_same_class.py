#!/usr/bin/python3
"""
This is module 2-is_same_class

It only defines one funtion
"""


def is_same_class(obj, a_class):
    """
    Evaluates if an object belongs to this class exactly


    Return:
        True if the object is exactly an instance of the specified class,
        otherwise False.
    """
    return type(obj) == a_class
