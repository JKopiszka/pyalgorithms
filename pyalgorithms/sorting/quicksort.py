# quicksort.py
#
# Implemented function for quick sort algorithm.
# Jakub Kopiszka (c) 2026


def quick_sort(arr: list, desc: bool = False):
    n: int = len(arr)

    if n <= 1:
        return arr

    pivot = arr[(n - 1) // 2]

    right = [item for item in arr if (item > pivot and not desc) or (item < pivot and desc)]
    left = [item for item in arr if (item < pivot and not desc) or (item > pivot and desc)]
    mid = [item for item in arr if item == pivot]

    return quick_sort(left, desc) + mid + quick_sort(right, desc)