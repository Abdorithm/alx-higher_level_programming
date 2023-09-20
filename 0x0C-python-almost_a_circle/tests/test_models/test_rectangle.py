#!/usr/bin/python3
"""Unittests for rectangle.py"""
import unittest
import sys
from models.rectangle import Rectangle

sys.path.append('../../')


class testRectangle(unittest.TestCase):
    """represents unittests for the Rectangle class"""

    def test_area(self):
        b12 = Rectangle(12, 20)
        self.assertEqual(b12.area(), 240)


if __name__ == '__main__':
    unittest.main()
