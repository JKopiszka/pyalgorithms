# selectsort.py
#
# Implemented function for selection sort algorithm.
# Jakub Kopiszka (c) 2026

def select_sort(arr: list, desc: bool = False):
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