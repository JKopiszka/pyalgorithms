# min.py
#
# Implemented function for minimals search algorithm.
# Jakub Kopiszka (c) 2026


def min(arr: list) -> int | float:
    """
    Returns the smallest value from the given list.

    Args:
        arr (list): List in which the minimum value should be searched.

    Returns:
        int | float: The smallest found value.
    """

    # Safety-point
    if len(arr) < 1:
        raise ValueError("Empty list.")
    if not all(isinstance(x, int | float) for x in arr):
        raise TypeError("Wrong type of provided array items.") 

    min_val: int | float = arr[0]

    for i in arr:
        min_val = i if i < min_val else min_val

    return min_val
