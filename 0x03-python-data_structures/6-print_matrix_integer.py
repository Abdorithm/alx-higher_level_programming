#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix and matrix:
            for i in range(len(row)):
                str = " " if i != len(row)-1 else "\n"
                print("{:d}".format(row[i]), end=str)
