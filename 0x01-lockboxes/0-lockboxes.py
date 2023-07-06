#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # List to track if a box is unlocked
    unlocked[0] = True  # The first box is unlocked initially

    # Iterate through each box and its keys
    for box_number, keys in enumerate(boxes):
        if unlocked[box_number]:
            # Mark all the boxes that can be opened with the current keys
            for key in keys:
                if key < n:
                    unlocked[key] = True

    # Check if all the boxes are unlocked
    return all(unlocked)
