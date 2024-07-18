#!/usr/bin/python3
"""Module for 2D matrix rotation"""


def rotate_2d_matrix(matrix):
    """Rotates m by n 2D matrix in place."""
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    b, t = 0, rows - 1
    for j in range(cols * rows):
        if j % rows == 0:
            matrix.append([])
        if t == -1:
            t = rows - 1
            b += 1
        matrix[-1].append(matrix[t][b])
        if b == cols - 1 and t >= -1:
            matrix.pop(t)
        t -= 1
