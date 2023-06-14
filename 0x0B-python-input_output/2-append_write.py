#!/usr/bin/python3
"""
append_write module.
It contains one function.
"""


def append_write(filename="", text=""):
    """
    append a string to a file
    """
    with open(filename, 'a') as f:
        return f.write(text)
