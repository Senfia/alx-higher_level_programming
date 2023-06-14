#!/usr/bin/python3
"""
This is module 0-read_file.
It contains only one function.
"""


def read_file(filename=""):
    """
    reads and prints file
    """
    with open(filename, 'r') as f:
        print(f.read(), end="")
