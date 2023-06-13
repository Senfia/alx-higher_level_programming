#!/usr/bin/python3
"""
This is module inherits_from

It only defines one funtion
"""



def inherits_from(obj, a_class):
    """
    evaluates if an object is directly or indrectly from a
    subclass ofa certain class
    
    Args:
        obj: object
        a_class: class

    Return:
        True if obj is from a sub class of a_class excluding
        a_class, otherwise, False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
