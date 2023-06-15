#!/usr/bin/python3
"""
Student class
It contains two functions.
"""


class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Creates Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        gets a dictionary of Student.
        """
        if attr is not None:
            reslt = {o: self.__dict__[o] for o in self.__dict__.keys() & attr}
            return (reslt)
        else:
            return (self.__dict__)
