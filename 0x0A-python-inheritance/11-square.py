#!/usr/bin/python3
"""
This is the Square class. 
It inherits from the Rectangle class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size):
        """
        Initialize Square object
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return: area of Square object
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return: string representation of the Squre object
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
