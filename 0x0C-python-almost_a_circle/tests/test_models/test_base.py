#!/usr/bin/python3
"""Unittests for base.py"""
import unittest
import sys
from models.base import Base

sys.path.append('../../')


class testBase(unittest.TestCase):
    """represents unittests for the Base class"""

    def test_increasingId(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id - b1.id, 1)

    def test_uniqueId(self):
        b12 = Base(12)
        self.assertEqual(b12.id, 12)


if __name__ == '__main__':
    unittest.main()
