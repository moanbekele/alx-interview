# 0x01-lockboxes
## `0-lockboxes.py`

-   In `0-lockboxes.py` the code defines a function called `canUnlockAll` that takes a list of `"boxes"` as input. Each box is a list that contains integer values which represent the indices of other boxes that can be unlocked with the keys inside the current box.

-   The `canUnlockAll` function checks whether all the boxes in the list can be unlocked or not, given that the first box is unlocked by default. The function uses a set of `"seen_boxes"` to keep track of the boxes that have already been opened, and a set of `"unseen_boxes"` to keep track of the boxes that are yet to be opened.

-   The function then enters a loop in which it pops an index from the `"unseen_boxes"` set, checks whether it is valid (i.e., not out of range), and adds it to the `"seen_boxes"` set if it has not been seen before. If the index is valid and has not been seen before, the keys inside that box are added to the `"unseen_boxes"` set. This process continues until there are no more unseen boxes left.At last the function returns a boolean value that indicates whether all the boxes have been opened or not. If the number of boxes that have been seen is equal to the total number of boxes, the function returns `True`, otherwise it returns `False`.