#!/usr/bin/python3
"""Defines a class MyList"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """public instance method print_sorted"""
        print(sorted(self))
