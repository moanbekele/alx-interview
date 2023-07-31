#!/usr/bin/python3
'''odule designed to handle or manipulate lockboxes.
'''


def canUnlockAll(boxes):
    '''
    This code defines a function that determines whether it is possible to unlock all the boxes in a list of boxes.
    Each box is represented by a list of integers that correspond to the indices of other boxes that can be unlocked with the keys inside that box.
    The function assumes that the first box is already unlocked, 
    and checks whether it is possible to unlock all the other boxes in the list using the keys found in the boxes that have already been opened.
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
