#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Description: returns the perimeter of the island described in grid
    :param grid: list of list of integers
    :return: perimeter of the island
    """
    result = 0
    for top in range(len(grid)):
        for bottom in range(len(grid[top])):
            if (grid[top][bottom] == 1):
                val = 4
                if (grid[top - 1][bottom] == 1):
                    val -= 1
                if (grid[top][bottom + 1] == 1):
                    val -= 1
                if (grid[top][bottom - 1] == 1):
                    val -= 1
                if (grid[top + 1][bottom] == 1):
                    val -= 1
                result += val
    return result
