# selectsort.py
#
# Implemented function for selection sort algorithm.
# Jakub Kopiszka (c) 2026

def select_sort(arr: list, desc: bool = False):
    """
    Sorts given array using select sort algorithm.

    Args:
        arr (list): List to be sorted.
        desc (bool, optional): If True, sorts in descending order. Defaults to False.

    Returns:
        list: Sorted list.
    """
    
    if len(arr) < 1:
        raise ValueError("List cannot be empty.")

    N: int = len(arr)

    for i in range(N - 1):
        swap_index: int = i

        for j in range(i + 1, N):
            if ((arr[j] < arr[swap_index]) and not desc) or (
                (arr[j] > arr[swap_index]) and desc
            ):
                swap_index = j

        arr[i], arr[swap_index] = arr[swap_index], arr[i]

    return arr