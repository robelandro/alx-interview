#!/usr/bin/python3
"""Module 14-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    lsd = [[0 for x in range(i + 1)] for i in range(n)]
    lsd[0] = [1]

    for i in range(1, n):
        lsd[i][0] = 1
        for j in range(1, i + 1):
            if j < len(lsd[i - 1]):
                lsd[i][j] = lsd[i - 1][j - 1] + lsd[i - 1][j]
            else:
                lsd[i][j] = lsd[i - 1][0]
    return lsd
