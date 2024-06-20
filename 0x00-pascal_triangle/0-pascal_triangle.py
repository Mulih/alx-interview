#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns list of integers
    representing Pascal Triangle of n
    returns empty list if n <= 0
    """
    j = []
    if n <= 0:
        return j
    j = [[1]]
    for k in range(1, n):
        temp = [1]
        for t in range(len(j[k - 1]) - 1):
            curr = j[k - 1]
            temp.append(j[k - 1][t] + j[k - 1][t + 1])
        temp.append(1)
        j.append(temp)
    return j
