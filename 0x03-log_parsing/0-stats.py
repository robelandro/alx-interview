#!/usr/bin/python3
"""
Module Log Parsing
"""
import sys
import signal


def slicer(line):
    """
    Slice the line
    """
    lines = line.split()
    result = {'Status': None, 'Size': None}
    result['Size'] = lines[-1]
    result['Status'] = lines[-2]

    return result


def countStore(sliced, result):
    """
    Count and store the statistics
    """
    status = sliced['Status']
    if status.isdigit():
        result.setdefault(status, 0)
        result[status] += 1
    result['File size'] += int(sliced['Size'])


def printStat(result):
    """
    Print the statistics
    """
    for key, value in result.items():
        if key.isdigit() or key == 'File size':
            print(f"{key}: {value}")


def handler(signal_received, frame):
    """
    Handle the signal
    """
    printStat(Result)
    sys.exit(0)


if __name__ == '__main__':
    Counter = 0
    Result = {'File size': 0}
    signal.signal(signal.SIGINT, handler)
    try:
        for line in sys.stdin:
            countStore(slicer(line), Result)
            if Counter == 10:
                printStat(Result)
                Counter = 0
            else:
                print(f'Line: {line}', end='')
            Counter += 1
    except KeyboardInterrupt:
        handler(None, None)
