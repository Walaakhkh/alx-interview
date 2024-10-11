#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    # Start with the first box (box 0) already unlocked
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    
    # Create a stack to hold keys, starting with the keys in box 0
    keys = [0]
    
    # Process the keys one by one
    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            # If the key opens a new box, unlock it and collect the keys inside
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    
    # If all boxes are unlocked, return True, otherwise return False
    return all(unlocked)
