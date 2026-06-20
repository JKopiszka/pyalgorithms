# sort_tests.py
#
# Sorting tests for search functions
# Jakub Kopiszka (c) 2026

import pyalgorithms, random, time

VALUES, AMOUNTS_OF_VALUES = 1000, 1000

def test_bubble_sort_performence():
    test_list = [random.randint(-VALUES, VALUES) for x in range(AMOUNTS_OF_VALUES)]
    total = 0

    for i in range(200):
        start = time.perf_counter()
        pyalgorithms.sorting.bubble_sort(test_list)
        end = time.perf_counter()
        total += end - start

    print("AVG EXECUTION TIME: " + str((total / 200)))

def test_quick_sort_performence():
    test_list = [random.randint(-VALUES, VALUES) for x in range(AMOUNTS_OF_VALUES)]
    total = 0

    for i in range(200):
        start = time.perf_counter()
        pyalgorithms.sorting.quick_sort(test_list)
        end = time.perf_counter()
        total += end - start

    print("AVG EXECUTION TIME: " + str((total / 200)))

def test_select_sort_performence():
    test_list = [random.randint(-VALUES, VALUES) for x in range(AMOUNTS_OF_VALUES)]
    total = 0

    for i in range(200):
        start = time.perf_counter()
        pyalgorithms.sorting.select_sort(test_list)
        end = time.perf_counter()
        total += end - start

    print("AVG EXECUTION TIME: " + str((total / 200)))

def main():
    test_bubble_sort_performence()
    test_select_sort_performence()
    test_quick_sort_performence()

if __name__ == "__main__":
    main()
