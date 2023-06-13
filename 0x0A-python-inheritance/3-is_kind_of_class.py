#!/usr/bin/python3
"""
This is module 2-is_same_class

It only defines one funtion
"""



def is_kind_of_class(obj, a_class):
    """
    evaluates an object and it's subclass

    Return:
        True if the object is of type class or a subclass of
        it, otherwise, False
    """
    if isinstance(obj, a_class):
        return True
    return False
