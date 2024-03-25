"""This program generates a passphrase of six words using the diceware 
method.

It simulates rolling five dice, uses the results to select a word
from a predefined list and repeat the process six times to generates
a secure and memorable passphrase."""

# TODO: Unify some functionalities in one function

import sys
from secrets import randbelow

DICE_ROLLS = 5
EXECUTIONS = 6
WORD_LIST_FILE = "wordlist/eff_large_wordlist.txt"


def load_word_list(file_path):
    """Load the word list from a file.

    Args:
        file_path (str): The path to the file containing the word list.

    Returns:
        list[list[str]]: A list of lists representing the word list.
        Each inner list is a list from the file, split into strings.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.split() for line in file]
    except IOError as e:
        print(f"Error opening file: {e}")
        sys.exit(1)


def roll_five_dice():
    """Simulates the roll of five dice, each producing a random number
    between 1 and 6.

    Returns:
        list[int]: A list of five integers,
        each between 1 and 6, inclusive
    """
    return [randbelow(6) + 1 for _ in range(DICE_ROLLS)]


def convert_dice_rolls_to_str(dice_roll):
    """Converts a list of integers into a string

    Args:
        dice_roll (list[int]): A list of integers representing the
        dice roll.

    Return:
        list[str]: A string representation of the dice roll.
    """
    return "".join(map(str, dice_roll))


def execute_multiple_dice_rolls():
    """Executes a dice roll multiple times and returns the results
    as strings.

    Returns:
        list[str]: A list of strings representing the results of each
        dice roll.
    """
    return [
        convert_dice_rolls_to_str(roll_five_dice()) for _ in range(EXECUTIONS)
    ]


def find_matches(word_list, all_results):
    """Finds matches between elements in 'WORD_LIST' and the results
    of 'execute_roll_a_dice()'.

    Returns:
        str: A string of matches found between 'WORD_LIST' and
        'all_results', separated by spaces.
    """
    matches = []

    for split_line in word_list:
        if split_line[0] in all_results:
            matches.append(split_line[1])

    return " ".join(matches)


def main():
    """Main function to tie all the steps together."""
    word_list = load_word_list(WORD_LIST_FILE)

    all_results = execute_multiple_dice_rolls()

    print(find_matches(word_list, all_results))


if __name__ == "__main__":
    main()
