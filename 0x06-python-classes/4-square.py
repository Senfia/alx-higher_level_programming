#!/usr/bin/python3
"""Class Square definition module"""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Arguments:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """set size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area."""
        return (self.__size * self.__size)
