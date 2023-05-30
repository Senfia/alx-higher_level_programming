#!/usr/bin/python3
"""
Class Square definition module
"""


class Square:
    """define a square."""
    def __init__(self, size):
        """
        instantiate object
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
