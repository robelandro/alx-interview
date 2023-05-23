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
    for top in range(len(grid) - 1):
        for botm in range(len(grid[top]) - 1):
            if (grid[top][botm] == 1):
                val = 4
                if (top > 0 and grid[top - 1][botm] == 1):
                    val -= 1
                if (botm < len(grid[top]) - 1 and grid[top][botm + 1] == 1):
                    val -= 1
                if (botm > 0 and grid[top][botm - 1] == 1):
                    val -= 1
                if (top < len(grid) - 1 and grid[top + 1][botm] == 1):
                    val -= 1
                result += val
    return result
