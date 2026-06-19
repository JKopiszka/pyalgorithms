# search_tests.py
#
# Performance tests for search functions
# Jakub Kopiszka (c) 2026

import pyalgorithms, random, time

def test_max_performence():
    test_list = [random.randint(-1000000, 1000000) for x in range(100000)]

    total = 0
    
    for i in range(200):
        start = time.perf_counter()
        pyalgorithms.search.max(test_list)
        end = time.perf_counter()
        total += (end - start)

    print("AVG EXECUTION TIME: " + str((total / 200)))

def test_min_performence():
    test_list = [random.randint(-1000000, 1000000) for x in range(100000)]

    total = 0

    for i in range(200):
        start = time.perf_counter()
        pyalgorithms.search.min(test_list)
        end = time.perf_counter()
        total += (end - start)

    print("AVG EXECUTION TIME: " + str((total / 200)))

def main():
    test_max_performence()
    test_min_performence()

if __name__ == "__main__":
    main()
