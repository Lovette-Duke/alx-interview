#!/usr/bin/python3
"""N queens challenge """
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)


def queens(n, row=0, columns=[], major_diagonals=[], minor_diagonals=[]):
    """function to find queen positions"""
    if row == n:
        yield columns
    for col in range(n):
        if col not in columns and row + col not in major_diagonals and row - col not in minor_diagonals:
            yield from queens(n, row + 1, columns + [col], major_diagonals +
                              [row + col], minor_diagonals + [row - col])


def solve(n):
    """solving the N queens problem"""
    for solution in queens(n):
        print([[i, solution[i]] for i in range(n)])


solve(n)
