#!/usr/bin/python3
"""defines is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """know if obj is an instance of,
    or if the object is an instance of
    a class that inherited from a_class"""

    if isinstance(obj, a_class):
        return True
    return False
