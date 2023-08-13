#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ([0 for i in range(max(len(tuple_a), len(tuple_b)))])
    for i in range(max(len(tuple_a), len(tuple_b))):
        if i < len(tuple_a):
            tuple_c[i] += tuple_a[i]
        if i < len(tuple_b):
            tuple_c[i] += tuple_b[i]
    return tuple(tuple_c)
