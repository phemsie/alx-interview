#!/usr/bin/python3
""" determines if all the boxes can be opened """


def canUnlockAll(boxes):
    ''' checks if all boxes can be opened '''
    keys = set(boxes[0])
    for i in range(1, len(boxes)):
        if (i in keys):
            keys = keys.union(set(boxes[i]))
    for i in range(1, len(boxes)):
        if (i in keys):
            keys = keys.union(set(boxes[i]))
    for i in range(1, len(boxes)):
        if i not in keys:
            return False
    return True
