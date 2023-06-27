#!/usr/bin/python3
"""
returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    ''' generates pascals triangle '''
    pascal = []
    if n <= 0:
        return pascal
    prev = [1]
    for c in range(1, n + 1):
        new = [1]
        for i in range(1, len(prev)):
            new += [prev[i - 1] + prev[i]]
        if c > 1:
            new += [1]
        pascal += [new]
        prev = new
        c += 1
    return pascal
