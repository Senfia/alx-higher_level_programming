#!/usr/bin/python3
"""Class Square definition module"""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Arguments:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area."""
        return (self.__size * self.__size)
