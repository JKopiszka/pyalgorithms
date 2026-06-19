# sort_tests.py
#
# Unit tests for sort functions
# Jakub Kopiszka (c) 2026

import unittest
from pyalgorithms import sorting

class TestBubbleSortFunctions(unittest.TestCase):
    def setUp(self):
        self.test_list = [8, 24, 9, 41, 5, 23, 91, 44, 77, 109, 0]

    def test_bubble_sort_normal(self):
        self.assertEqual(sorting.bubble_sort(self.test_list), [0, 5, 8, 9, 23, 24, 41, 44, 77, 91, 109])

    def test_bubble_sort_single(self):
        self.assertEqual(sorting.bubble_sort([1]), [1])

    def test_bubble_sort_negative(self):
        self.assertEqual(sorting.bubble_sort([-10, -5, -20]), [-20, -10, -5])

    def test_bubble_sort_descending(self):
        self.assertEqual(sorting.bubble_sort(self.test_list, desc=True), [109, 91, 77, 44, 41, 24, 23, 9, 8, 5, 0])

    def test_bubble_sort_repeated(self):
        self.assertEqual(sorting.bubble_sort([2, 2, 2, 2]), [2, 2, 2, 2])

    def test_bubble_sort_empty(self):
        with self.assertRaises(ValueError):
            sorting.bubble_sort([])

class TestQuickSortFunctions(unittest.TestCase):
    def setUp(self):
        self.test_list = [8, 24, 9, 41, 5, 23, 91, 44, 77, 109, 0]

    def test_quick_sort_normal(self):
        self.assertEqual(sorting.quick_sort(self.test_list), [0, 5, 8, 9, 23, 24, 41, 44, 77, 91, 109])

    def test_quick_sort_single(self):
        self.assertEqual(sorting.quick_sort([1]), [1])

    def test_quick_sort_negative(self):
        self.assertEqual(sorting.quick_sort([-10, -5, -20]), [-20, -10, -5])

    def test_quick_sort_descending(self):
        self.assertEqual(sorting.quick_sort(self.test_list, desc=True), [109, 91, 77, 44, 41, 24, 23, 9, 8, 5, 0])

    def test_quick_sort_repeated(self):
        self.assertEqual(sorting.quick_sort([2, 2, 2, 2]), [2, 2, 2, 2])

    def test_quick_sort_empty(self):
        with self.assertRaises(ValueError):
            sorting.quick_sort([])

class TestSelectSortFunctions(unittest.TestCase):
    def setUp(self):
        self.test_list = [8, 24, 9, 41, 5, 23, 91, 44, 77, 109, 0]

    def test_select_sort_normal(self):
        self.assertEqual(sorting.select_sort(self.test_list), [0, 5, 8, 9, 23, 24, 41, 44, 77, 91, 109])

    def test_select_sort_single(self):
        self.assertEqual(sorting.select_sort([1]), [1])

    def test_select_sort_negative(self):
        self.assertEqual(sorting.select_sort([-10, -5, -20]), [-20, -10, -5])

    def test_select_sort_descending(self):
        self.assertEqual(sorting.select_sort(self.test_list, desc=True), [109, 91, 77, 44, 41, 24, 23, 9, 8, 5, 0])

    def test_select_sort_repeated(self):
        self.assertEqual(sorting.select_sort([2, 2, 2, 2]), [2, 2, 2, 2])

    def test_select_sort_empty(self):
        with self.assertRaises(ValueError):
            sorting.select_sort([])