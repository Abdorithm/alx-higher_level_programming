#!/usr/bin/python3
"""Unittests for square.py"""
import unittest
import sys
from models.square import Square

sys.path.append('../../')


class testSquare(unittest.TestCase):
    """represents unittests for the Square class"""

    def test_area(self):
        b12 = Square(12)
        self.assertEqual(b12.area(), 144)


if __name__ == '__main__':
    unittest.main()
