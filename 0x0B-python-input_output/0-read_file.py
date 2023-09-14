#!/usr/bin/python3
"""defines the read_file method"""


def read_file(filename=""):
    """reads a text file (UTF-8) and prints
    it to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        [print(line, end="") for line in f.readlines()]
