# bubblesort.py
#
# Implemented function for bubble sort algorithm.
# Jakub Kopiszka (c) 2026


def bubble_sort(arr: list, desc: bool = False) -> list:
    """
    Sorts given array using bubble sort algorithm.

    Args:
        arr (list): List to be sorted.
        desc (bool, optional): If True, sorts in descending order. Defaults to False.

    Returns:
        list: Sorted list.
    """
    
    if len(arr) < 1:
        raise ValueError("List cannot be empty.")

    n: int = len(arr)

    for i in range(1, n):
        swapped: bool = False

        for j in range(0, n - 1):
            if (arr[j] > arr[j + 1] and not desc) or (arr[j] < arr[j + 1] and desc):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr
