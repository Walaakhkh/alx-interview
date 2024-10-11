#!/usr/bin/python3
"""
0-lockboxes.py

This module contains a method that determines if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list where each element is a list representing
                               a box and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    # List to keep track of unlocked boxes, initially only box 0 is unlocked
    unlocked = [False] * len(boxes)
    unlocked[0] = True

    # Stack to manage the keys we find, starting with the keys in box 0
    keys = [0]

    # While there are keys to process
    while keys:
        current_key = keys.pop()  # Take a key from the stack
        for key in boxes[current_key]:
            # If the key opens a new box and it's a valid box number
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True  # Mark the box as unlocked
                keys.append(key)      # Add the new key to the stack

    # Check if all boxes have been unlocked
    return all(unlocked)
