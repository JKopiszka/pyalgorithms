# search_tests.py
#
# Unit tests for search functions
# Jakub Kopiszka (c) 2026

import unittest
from pyalgorithms import search

class TestSearchFunctions(unittest.TestCase):
    def setUp(self):
        self.test_list = [5, 10, 15, 20]

    ## MINIMUM FUNCTIONS TEST SET ##

    def test_min_normal(self):
        self.assertEqual(search.min(self.test_list), 5)

    def test_min_single_element(self):
        self.assertEqual(search.min([10]), 10)

    def test_min_negative_values(self):
        self.assertEqual(search.min([-5, -1, -10]), -10)

    def test_min_repeated_values(self):
        self.assertEqual(search.min([5, 5, 5]), 5)

    def test_min_empty_list(self):
        with self.assertRaises(ValueError):
            search.min([])

    def test_min_invalid_type(self):
        with self.assertRaises(TypeError):
            search.min(["a", "b"])

    ## MAXIMUM FUNCTIONS TEST SET ##

    def test_max_normal(self):
        self.assertEqual(search.max(self.test_list), 20)

    def test_max_single_element(self):
        self.assertEqual(search.max([10]), 10)

    def test_max_negative_values(self):
        self.assertEqual(search.max([-5, -1, -10]), -1)

    def test_max_repeated_values(self):
        self.assertEqual(search.max([5, 5, 5]), 5)

    def test_max_empty_list(self):
        with self.assertRaises(ValueError):
            search.max([])
            
    def test_max_invalid_type(self):
        with self.assertRaises(TypeError):
            search.max(["a", "b"])


if __name__ == "__main__":
    unittest.main()
