#!/usr/bin/python3
"""
This is the BaseGeometry class.
"""


class BaseGeometry:
    """
    Raise exception
    """

    def area(self):
        """ Not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value
        """
        if type(name) is not str:
            return
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
