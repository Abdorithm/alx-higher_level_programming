#!/usr/bin/python3
"""defines class BaseGeometry"""


class BaseGeometry():
    """the BaseGeometry class"""

    def area(self):
        """public instance method area()"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
