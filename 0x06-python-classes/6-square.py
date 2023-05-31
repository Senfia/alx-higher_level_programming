#!/usr/bin/python3
"""Class Square definition module"""


class Square:
    """Define a square."""

    def __init__(self, size):
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

    @property
    def position(self):
        """set size of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Return area of Square object"""
        errMes = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(errMes)
        if len(value) < 2:
            raise TypeError(errMes)
        if not (type(value[0]) is int and type(value[1]) is int):
            raise TypeError(errMes)
        if (value[0] < 0 or value[1] < 0):
            raise TypeError(errMes)
        self.__position = value
    
    def area(self):
        """Return area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square using #."""
        if self.size == 0:
            print()
            return
        for l in range(self.position[1]):
            print()
        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
