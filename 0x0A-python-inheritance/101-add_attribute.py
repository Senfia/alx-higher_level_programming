#!/usr/bin/python3
def add_attribute(obj, name, val):
    """
    adds a new attribute to an object if it’s possible
    """
    obj.__dict__[name] = val
