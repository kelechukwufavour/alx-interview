#!/usr/bin/python3
""" defines methods to solve lockboxes problems """

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    if not boxes:
        return False

    keys = set([0])
    visited = set()

    while keys:
        box_index = keys.pop()
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited:
                keys.add(key)

    return len(visited) == len(boxes)

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
