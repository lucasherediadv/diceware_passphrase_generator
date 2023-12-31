"""Docs"""
import unittest
from src import main


class TestMain(unittest.TestCase):
    """Docs"""
    def test_roll_a_dice(self):
        """Docs"""
        result = main.roll_a_dice()
        self.assertEqual(len(result), 5)
        self.assertTrue(all(1 <= num <= 6 for num in result))


if __name__ == '__main__':
    unittest.main()
