#!/usr/bin/python3
"""
This is the MyInt class. This class inherits from int class.
"""


class MyInt(int):
    """
    Creates MyInt object
    """
    def __init__(self, val):
        """
        Override == and return !=
        """
        if type(val) is super():
            self.__val = val

    def __eq__(self, other):
        """
        !=
        """
        return False

    def __ne__(self, other):
        """
        ==
        """
        return True
