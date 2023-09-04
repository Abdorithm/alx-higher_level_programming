#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The 2-matrix_divided module supplies one function, matrix_divided().
For example,

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """ Divide all elements of a matrix"""

    errmsg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError(errmsg)
        size.append(len(row))
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError(errmsg)
    if len(set(size)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
