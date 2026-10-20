"""Unit tests for Level 2 Python Assessment using standard unittest."""

import unittest
from assessment import (
    filter_and_sum_evens,
    count_character_frequencies,
    find_highest_scoring_student,
    categorize_temperatures,
)


class TestFilterAndSumEvens(unittest.TestCase):
    def test_standard_list(self):
        self.assertEqual(filter_and_sum_evens([1, 2, 3, 4, 5, 6]), 12)

    def test_no_evens(self):
        self.assertEqual(filter_and_sum_evens([1, 3, 5, 7]), 0)

    def test_empty_list(self):
        self.assertEqual(filter_and_sum_evens([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(filter_and_sum_evens([-4, -3, -2, 1, 0]), -6)


class TestCountCharacterFrequencies(unittest.TestCase):
    def test_standard_string(self):
        text = "Hello World!"
        expected = {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
        self.assertEqual(count_character_frequencies(text), expected)

    def test_ignores_punctuation_and_case(self):
        text = "a1, a2! A1?"
        expected = {"a": 3, "1": 2, "2": 1}
        self.assertEqual(count_character_frequencies(text), expected)

    def test_empty_string(self):
        self.assertEqual(count_character_frequencies(""), {})


class TestFindHighestScoringStudent(unittest.TestCase):
    def test_standard_scores(self):
        scores = {
            "Alice": [85.0, 90.0, 95.0],   # Avg: 90.0
            "Bob": [70.0, 80.0, 75.0],     # Avg: 75.0
            "Charlie": [95.0, 95.0, 100.0] # Avg: 96.67
        }
        self.assertEqual(find_highest_scoring_student(scores), ("Charlie", 96.67))

    def test_empty_dictionary(self):
        self.assertEqual(find_highest_scoring_student({}), ("", 0.0))


class TestCategorizeTemperatures(unittest.TestCase):
    def test_standard_temperatures(self):
        temps = [10.0, 15.0, 22.5, 25.0, 30.0, 5.5]
        expected = {
            "Cold": [10.0, 5.5],
            "Warm": [15.0, 22.5, 25.0],
            "Hot": [30.0]
        }
        self.assertEqual(categorize_temperatures(temps), expected)

    def test_empty_list(self):
        expected = {"Cold": [], "Warm": [], "Hot": []}
        self.assertEqual(categorize_temperatures([]), expected)


if __name__ == "__main__":
    unittest.main()