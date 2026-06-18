# max.py
#
# Implemented function for maximals search algorithm.
# Jakub Kopiszka (c) 2026


def max(arr: list) -> int | float:
    """
    Returns the highest value from the given list.

    Args:
        arr (list): List in which the maximum value should be searched.

    Returns:
        int | float: The highest found value.
    """
    # Safety-point
    if len(arr) < 1:
        raise ValueError("Empty list.")
    if not all(isinstance(x, int | float) for x in arr):
        raise TypeError("Wrong type of provided array items.") 

    max_val: int | float = arr[0]

    for i in arr:
        max_val = i if i > max_val else max_val

    return max_val
