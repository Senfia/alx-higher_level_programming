#!/usr/bin/python3
"""
It contains one function
"""


def number_of_lines(filename=""):
    """
    Returns Number of lines in a file
    """
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            count += 1
    return count
