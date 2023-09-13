#!/usr/bin/python3
"""defines is_same_class method"""


def is_same_class(obj, a_class):
    """know if obj is an instance of a_class"""
    if type(obj) is a_class:
        return True
    return False
