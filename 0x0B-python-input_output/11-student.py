#!/usr/bin/python3
"""
Student class
It contains three functions.
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

    def to_json(self, attrs=None):
        """
        gets a dictionary of Student.
        """
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            return {o: p for o, p in self.__dict__.items() if o in attrs}
        else:
            return (self.__dict__.copy())

    def reload_from_json(self, json_data):
        """
        replaces all attributes of the Student
        """
        for key, value in json_data.items():
            self.__dict__[key] = value

