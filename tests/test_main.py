"""Unit tests for the 'main.py' program.

This program contains a series of unit test designed to verify the
correct functionality of the functions in 'main.py'
Each test case is a method within the 'TestMain' class, which
inherits from 'unittest.TestCase'.
"""

import unittest
from src.main import roll_a_dice, execute_roll_a_dice, find_matches


class TestMain(unittest.TestCase):
    """A class used to perform unit tests on the functions in the
    'main' module.

    Attributes:
        None

    Methods:
        test_roll_a_dice()
        test_execute_roll_a_dice()
        test_find_matches()
    """

    def setUp(self) -> None:
        """Set up testing enviroment."""
        self.word_list = [
            ["11111", "first"],
            ["22222", "second"],
            ["33333", "third"],
        ]

        self.all_results = ["11111", "22222", "44444", "55555", "66666"]

    def test_roll_a_dice(self) -> None:
        """Tests the 'roll_a_dice()' function from the 'main' module.

        This test checks if the function is working correctly by
        asserting two conditions:

        - The lenght of the result list should be 5.
        - All number in the result list should be between 1 and 6.
        """
        result = roll_a_dice()
        self.assertEqual(len(result), 5)
        self.assertTrue(all(1 <= num <= 6 for num in result))

    def test_execute_roll_a_dice(self) -> None:
        """Tests the 'execute_roll_a_dice()' function from the 'main'
        module.

        This test checks if the function is working correctly by
        asserting two conditions:

        - The lenght of the result list should be 6.
        - All elements in the result list should be instances of the
        'str' class.
        """
        result = execute_roll_a_dice()
        self.assertEqual(len(result), 6)
        self.assertTrue(all(isinstance(num_str, str) for num_str in result))

    def test_find_matches(self) -> None:
        """Tests the 'find_matches()' function from the 'main' module.

        This test checks if the function is working correctly by
        asserting the following conditions:

        - Given a word list and a list of results, the function should
          return a string of words that match the results.
        - The word list is a list of lists where each inner list
          contains a string of numbers and its corresponding word.
        - The results list contains strings of concatenated numbers.
        """
        result = find_matches(self.word_list, self.all_results)
        self.assertEqual(result, "first second")

    def test_find_matches_empty_list(self) -> None:
        """Test 'find_matches() function with an empty list.

        Checks if the function handles an empty list correctly by
        asserting that it returns an empty string.
        """
        result = find_matches([], self.all_results)
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
