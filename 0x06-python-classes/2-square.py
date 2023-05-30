#!/usr/bin/python3
"""
Class Square definition module
"""


class Square:
    """define a square."""
    def __init__(self, size=0):
        """
        instantiate object
        Arguments:
        	size(int): square size
        """
        self.__size = __size
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
