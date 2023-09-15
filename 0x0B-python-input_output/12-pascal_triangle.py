#!/usr/bin/python3
"""defines the pascal_triangle method"""


def pascal_triangle(n):
    """that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    pascal = []
    if n <= 0:
        return pascal
    for i in range(n):
        if i == 0:
            row = [1]
        else:
            last = pascal[i-1]
            row = [1]
            for j in range(len(last)-1):
                row.append(last[j] + last[j+1])
            row.append(1)
        pascal.append(row)
    return pascal
