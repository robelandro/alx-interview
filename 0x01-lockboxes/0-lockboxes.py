#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened.
    """
    keys = [0]
    for key in keys:
        for key2 in boxes[key]:
            if key2 not in keys and key2 < len(boxes):
                keys.append(key2)
    if len(keys) == len(boxes):
        return True
    return False
