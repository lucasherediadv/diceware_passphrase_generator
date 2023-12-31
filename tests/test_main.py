"""Basic Unit test for the main program 'main.py'"""
import unittest
from src.main import roll_a_dice, execute_roll_a_dice, find_matches


class TestMain(unittest.TestCase):
    """This class contains unit test for the functions in the main
    module.

    The class intherits from the 'unittest.TestCase' class, which
    provides the framework for creating and running tests.

    The class contains three methods, each of which tests a specific
    function in the 'main' module.

    To run the tests, an instance of the 'TestMain' class is created
    and the 'unittest.main()' function is called.
    """

    def test_roll_a_dice(self):
        """Test Case for the function 'roll_a_dice()'

        This test checks if the function is working correctly by
        asserting two conditions:

        - The lenght of the result list should be 5.
        - All number in the result list should be between 1 and 6.
        """
        result = roll_a_dice()
        self.assertEqual(len(result), 5)
        self.assertTrue(all(1 <= num <= 6 for num in result))

    def test_execute_roll_a_dice(self):
        """Test Case for the function 'execute_roll_a_dice()'

        This test checks if the function is working correctly by
        asserting two conditions:

        - The lenght of the result list should be 6.
        - All elements in the result list should be instances of the
        'str' class.
        """
        result = execute_roll_a_dice()
        self.assertEqual(len(result), 6)
        self.assertTrue(
            all(isinstance(num_str, str) for num_str in result)
        )

    def test_find_matches(self):
        """Test Case for the function 'execute_roll_a_dice()'

        This test checks if the function is working correctly by
        asserting the following conditions:

        - Given a word list and a list of results, the function should
          return a string of words that match the results.
        - The word list is a list of lists where each inner list
          contains a string of numbers and its corresponding word.
        - The results list contains strings of concatenated numbers.
        """
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
