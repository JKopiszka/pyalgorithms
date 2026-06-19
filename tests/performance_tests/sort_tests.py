# sort_tests.py
#
# Sorting tests for search functions
# Jakub Kopiszka (c) 2026

import pyalgorithms, random, time

VALUES, AMOUNTS_OF_VALUES = 10000, 10000

def test_bubble_sort_performence():
    test_list = [random.randint(-VALUES, VALUES) for x in range(AMOUNTS_OF_VALUES)]

    start = time.time()
    pyalgorithms.sorting.bubble_sort(test_list)
    end = time.time()

    print("EXECUTION TIME: " + str((end - start)))

def test_quick_sort_performence():
    test_list = [random.randint(-VALUES, VALUES) for x in range(AMOUNTS_OF_VALUES)]

    start = time.time()
    pyalgorithms.sorting.quick_sort(test_list)
    end = time.time()

    print("EXECUTION TIME: " + str((end - start)))

def test_select_sort_performence():
    test_list = [random.randint(-VALUES, VALUES) for x in range(AMOUNTS_OF_VALUES)]

    start = time.time()
    pyalgorithms.sorting.select_sort(test_list)
    end = time.time()

    print("EXECUTION TIME: " + str((end - start)))

def main():
    test_bubble_sort_performence()
    test_select_sort_performence()
    test_quick_sort_performence()

if __name__ == "__main__":
    main()
