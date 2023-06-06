#!/usr/bin/python3
"""
This is a Rectangle class.
This module contains 1 Rectangle class
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if self.__check_arg(value, "height"):
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if self.__check_arg(value, "width"):
            self.__width = value

    def __check_arg(self, value, attribute):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))
        return (True)

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        return ("\n".join(["{}".format(self.print_symbol) *
                           self.__width
                           for i in range(self.__height)]))

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
