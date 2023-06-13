#!/usr/bin/python3
"""
This is the Rectangle class.

This class inherits from BaseGeometry class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle
    subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """
        instantiates width and height are positive int
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
