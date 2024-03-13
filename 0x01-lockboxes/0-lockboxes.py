#!/usr/bin/python3
""" defines methods to solve lockboxes problems """

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    num_boxes = len(boxes)
    if num_boxes == 1:
        return True

    keys = set(boxes[0])
    unlocked = {0}

    while keys:
        key = keys.pop()
        if 0 <= key < num_boxes and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

    return len(unlocked) == num_boxes

if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
