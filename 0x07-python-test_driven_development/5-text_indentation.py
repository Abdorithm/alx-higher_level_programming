#!/usr/bin/python3
"""
This is the "5-test_indentation" module.

The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """
    splits a string into lines separeted by
    "?", ":", "." followed by 2 new lines
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if a == '?' or a == '.' or a == ':':
            flag = 1
            print(a)
            print()
        else:
            if a != ' ':
                flag = 0
            if flag == 0:
                print(a, end="")
