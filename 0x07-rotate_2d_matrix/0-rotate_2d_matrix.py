#!/usr/bin/python3
"""
Rotating matrix moudule
"""


def rotate_2d_matrix(matrix):
    """
    Description: rotating the given n * n matrix to 90d

    :param: matrix list
    :return: matrix list
    """
    new_array = [[]for _ in range(len(matrix))]
    for x in reversed(matrix):
        for i in range(len(matrix)):
            new_array[i].append(x[i])
    matrix[:] = new_array
