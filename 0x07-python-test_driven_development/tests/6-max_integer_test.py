#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        self.assertEqual(max_integer([1, 13, 4]), 13)
        self.assertEqual(max_integer("ngszlakg"), 'z')
        self.assertEqual(max_integer([-14, -235, -33]), -14)

    def test_invalid(self):
        self.assertRaises(TypeError, max_integer, 13)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)
