#!/usr/bin/python3
"""defines the write_file method"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)


nb_characters = write_file("my_first_file.txt", "Abdo\n")
print(nb_characters)
