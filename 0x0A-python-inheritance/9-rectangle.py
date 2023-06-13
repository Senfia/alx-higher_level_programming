#!/usr/bin/python3
"""
This is the Rectangle class.
It inherits from BaseGeometry class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle
    subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """
        instantiates a Rectangle is wodth and height are
        positive int
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """
        computes area of rectangle
        """
        return self.__width * self.__height
    def __str__(self):
        """
        Return: string representation of the Rectangle object
        """
        return "[Rectangle] {}/{}".format(self.__width,
        				  self.__height)
