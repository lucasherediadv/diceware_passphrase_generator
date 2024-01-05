"""Unit tests for the 'main.py' program.

This program contains a series of unit test designed to verify the
correct functionality of the functions in 'main.py'
Each test case is a method within the 'TestMain' class, which
inherits from 'unittest.TestCase'.
"""

import unittest
from src.main import roll_a_dice, execute_roll_a_dice, find_matches


class TestMain(unittest.TestCase):
    """Unit tests for the functions in the 'main' module."""

    def test_roll_a_dice_returns_list_of_five_numbers_in_range(self) -> None:
        """Test if the function returns a list of 5 number between
        1 and 6."""
        result = roll_a_dice()
        self.assertEqual(len(result), 5)
        self.assertTrue(all(1 <= num <= 6 for num in result))

    def test_execute_roll_a_dice_returns_list_of_six_strings(self) -> None:
        """Test if the function returns a list of 6 strings."""
        result = execute_roll_a_dice()
        self.assertEqual(len(result), 6)
        for num_str in result:
            self.assertIsInstance(num_str, str)

    def test_find_matches_returns_matching_words(self) -> None:
        """Test if the function returns matching words from the word
        list"""
        word_list = [
            ["11111", "first"],
            ["22222", "second"],
            ["33333", "third"],
        ]

        all_results = ["11111", "22222", "44444", "55555", "66666"]

        result = find_matches(word_list, all_results)
        self.assertEqual(result, "first second")

    def test_find_matches_handles_empty_list(self) -> None:
        """Test if the function returns an empty string for an
        emtpy word list."""
        all_results = ["11111", "22222", "44444", "55555", "66666"]

        result = find_matches([], all_results)
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
