#!/usr/bin/python3
"""Contains the class Student"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance
        or only the attrs values in the dictionary"""
        if attrs is not None and all(isinstance(elem, str) for elem in attrs):
            return {elem: self.__dict__[elem]
                    for elem in attrs if elem in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all the attributes of Student instance"""
        for elem in json:
            if elem in self.__dict__:
                self.__dict__[elem] = json[elem]
