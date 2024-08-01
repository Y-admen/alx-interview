#!/usr/bin/python3
def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    unlocked = set([0])  # First box is always unlocked
    keys = set(boxes[0])  # Keys from the first box

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked) == n
