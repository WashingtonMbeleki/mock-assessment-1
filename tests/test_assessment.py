import unittest
from assessment import (
    check_even_odd,
    get_grade,
    sum_list_elements,
    find_first_negative,
    count_vowels
)

class TestPythonAssessmentLevel3(unittest.TestCase):

    def test_check_even_odd(self):
        self.assertEqual(check_even_odd(4), "Even")
        self.assertEqual(check_even_odd(7), "Odd")
        self.assertEqual(check_even_odd(0), "Even")
        self.assertEqual(check_even_odd(-3), "Odd")

    def test_get_grade(self):
        self.assertEqual(get_grade(95), "A")
        self.assertEqual(get_grade(90), "A")
        self.assertEqual(get_grade(82), "B")
        self.assertEqual(get_grade(70), "C")
        self.assertEqual(get_grade(65), "D")
        self.assertEqual(get_grade(45), "F")

    def test_sum_list_elements(self):
        self.assertEqual(sum_list_elements([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_list_elements([-1, 1, 0]), 0)
        self.assertEqual(sum_list_elements([]), 0)

    def test_find_first_negative(self):
        self.assertEqual(find_first_negative([5, 3, -2, 7, -8]), -2)
        self.assertEqual(find_first_negative([-1, 2, 3]), -1)
        self.assertEqual(find_first_negative([10, 20, 30]), None)
        self.assertEqual(find_first_negative([]), None)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("Python Programming"), 4)
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(count_vowels("rhythm"), 0)

if __name__ == "__main__":
    unittest.main()