#!/usr/bin/python3
"""
write_file module.
It contains one function.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file 
    returns: the number of characters.
    """
    with open(filename, 'w') as f:
        return f.write(text)
