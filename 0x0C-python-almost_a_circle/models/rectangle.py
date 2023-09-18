#!/usr/bin/python3
"""Defines the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represents the Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the Rectangle instance
            Args:
                width (int):
                height (int):
                x (int):
                y (int):
                id (int): id form the parent class
            Return:
                None"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """update attributes from args"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for elem in kwargs:
                for attr in dir(self):
                    if elem == attr:
                        setattr(self, attr, kwargs[elem])

    def __str__(self):
        """overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle with # characters"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(self.__x * " ", end="")
            print(self.__width * "#")

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
            None"""
        if type(value) is int:
            if value <= 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """getter of __height
        Returns:
            height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of __height
        Args:
            value (int): the height
        Returns:
            None"""
        if type(value) is int:
            if value <= 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """getter of __x
        Returns:
            value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of __x
        Args:
            value (int): x
        Returns:
            None"""
        if type(value) is int:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """getter of __y
        Returns:
            value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of __y
        Args:
            value (int): y
        Returns:
            None"""
        if type(value) is int:
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")
