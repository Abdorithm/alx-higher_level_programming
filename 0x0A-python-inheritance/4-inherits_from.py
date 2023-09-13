#!/usr/bin/python3
"""defines inherits_from method"""


def inherits_from(obj, a_class):
    """know if obj is an instance of a class that
    is inherited (directly or not) of a_class"""
    if isinstance(obj, a_class):
        return True
    return False
