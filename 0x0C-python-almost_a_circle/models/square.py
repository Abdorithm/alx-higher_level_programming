#!/usr/bin/python3
"""Defines the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the Rectangle instance
            Args:
                size (int):
                x (int):
                y (int):
                id (int): id form the parent class
            Return:
                None"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """update attributes from args"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for elem in kwargs:
                for attr in dir(self):
                    if elem == attr:
                        setattr(self, attr, kwargs[elem])

    @property
    def size(self):
        """getter of __size
        Returns:
            size of the square"""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int):
        Returns:
            None"""
        if type(value) is int:
            if value <= 0:
                raise ValueError("width must be > 0")
            self._Rectangle__width = value
            self._Rectangle__height = value
        else:
            raise TypeError("width must be an integer")
