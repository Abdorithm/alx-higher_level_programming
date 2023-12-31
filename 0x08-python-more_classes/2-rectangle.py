#!/usr/bin/python3
"""
defines rectangle
"""


class Rectangle:
    """
    Represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initializes rectangle
        Args:
            width (int):
            height (int):
        Returns:
            None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of __width
        Returns:
            width of the rectangle
         """
        return self.__width

    @width.setter
    def width(self, value):
        """setter of __width
        Args:
            value (int): the width
        Returns:
            None
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """getter of __height
        Returns:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter of __height
        Args:
            value (int): the height
        Returns:
            None
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """public instance method area
        Returns:
            area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """public instance method perimeter
        Returns:
            the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
