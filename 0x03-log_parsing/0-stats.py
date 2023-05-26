#!/usr/bin/python3
"""
0-stats module
"""
import sys


def slicer(line):
    """
    Slice the line into status and size information.

    :param line: Line to slice
    :type line: str
    :return: Dictionary with the sliced line
    :rtype: dict
    """
    lines = line.split()
    result = {'Status': None, 'Size': None}
    result['Size'] = lines[-1]
    result['Status'] = lines[-2]

    return result


def countStore(sliced, result):
    """
    Count and store the statistics based on the sliced line.

    :param sliced: Sliced line containing status and size information
    :type sliced: dict
    :param result: Dictionary with the statistics
    :type result: dict
    :return: None
    """
    status = sliced['Status']
    if status.isdigit():
        result.setdefault(status, 0)
        result[status] += 1
    result['File size'] += int(sliced['Size'])


def printStat(result):
    """
    Print the statistics.

    :param result: Dictionary with the statistics
    :type result: dict
    :return: None
    """
    for key, value in result.items():
        if key.isdigit() or key == 'File size':
            print(f"{key}: {value}")


if __name__ == '__main__':
    Counter = 0
    Result = {'File size': 0}
    try:
        for line in sys.stdin:
            countStore(slicer(line), Result)
            if Counter == 10:
                printStat(Result)
                Counter = 0
            Counter += 1
    except KeyboardInterrupt:
        printStat(Result)
        raise
