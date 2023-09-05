#!/usr/bin/python3

import sys

col = []
diag1 = []
diag2 = []
solutions = []
n = 0


def completeSearch(x):
    if x == n:
        print(solutions)
        return
    for y in range(n):
        if col[y] or diag1[x+y] or diag2[x-y+n]:
            continue
        col[y] = diag1[x+y] = diag2[x-y+n] = 1
        solutions.append([x, y])
        completeSearch(x+1)
        solutions.pop(len(solutions)-1)
        col[y] = diag1[x+y] = diag2[x-y+n] = 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(n):
        col.append(0)
    for i in range(n * 2):
        diag1.append(0)
        diag2.append(0)

    completeSearch(0)
