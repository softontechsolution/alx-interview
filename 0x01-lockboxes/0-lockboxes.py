#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    for key in range(1, len(boxes) - 1):
        ha = False
        for idx in range(len(boxes)):
            ha = (key in boxes[idx] and key != idx)
            if ha:
                break
        if ha is False:
            return ha
    return True
