#!/usr/bin/python

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
    boxes (list of lists): Each sublist contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = boxes[0].copy()

    while stack:
        key = stack.pop()
        if 0 <= key < n and not opened[key]:
            opened[key] = True

            for new_key in boxes[key]:
                if new_key not in stack and not opened[new_key if new_key < n else 0]:
                    stack.append(new_key)

    return all(opened)

