"""Docs"""
import unittest
from src.main import roll_a_dice, execute_roll_a_dice, find_matches


class TestMain(unittest.TestCase):

    """Docs"""

    def test_roll_a_dice(self):
        """Docs"""
        result = roll_a_dice()
        self.assertEqual(len(result), 5)
        self.assertTrue(all(1 <= num <= 6 for num in result))

    def test_execute_roll_a_dice(self):
        """Docs"""
        result = execute_roll_a_dice()
        self.assertEqual(len(result), 6)
        self.assertTrue(
            all(isinstance(num_str, str) for num_str in result)
        )

    def test_find_matches(self):
        """Docs"""
        word_list = [
            ["11111", "first"],
            ["22222", "second"],
            ["33333", "third"],
        ]

        all_results = ["11111", "22222", "44444", "55555", "66666"]
        result = find_matches(word_list, all_results)
        self.assertEqual(result, "first second")


if __name__ == "__main__":
    unittest.main()
