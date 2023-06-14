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

    def to_json(self):
        """
        gets a dictionary of Student.
        """
        return (self.__dict__)
