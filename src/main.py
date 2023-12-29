# TODO: Add Program Docs
"""Program Docs"""
from random import randint

# Represent the number of dices that will be rolled at
# the same time.
# Its value will always be 5 because the words in the word list
# are represented with a 5-digit number.
DICE_ROLLS = 5

# Defines the number of words that the passphrase will have.
# Six words are recommended by the EFF.
EXECUTIONS = 6

with open('list/eff_wordlist.txt', 'r', encoding='utf-8') as file:
    # For each line in the file, split the line into a list of strings.
    # The result is a list of lists, where each inner list represents
    # a line in the file.
    WORD_LIST = [line.split() for line in file]


def roll_a_dice() -> list[int]:
    # TODO: Update docs
    """Generates a list of random numbers between 1 and 6
    simulating the roll of five dices all at once and 
    storing the results in a list.

    Returns:
        list[int]: list of random numbers.
    """
    return [randint(1, 6) for _ in range(DICE_ROLLS)]


def execute_roll_a_dice() -> list[str]:
    # TODO: Update docs
    """Rolls the dice 6 times and returns the results as
    a list of strings.

    Returns:
        list[str]: A list of 6 strings, each of which is a
        concatenation of the digits obtained from rolling
        a dice.
    """
    results = []

    for _ in range(EXECUTIONS):
        roll_result = roll_a_dice()
        str_result = ''.join(map(str, roll_result))
        results.append(str_result)

    return results


def find_matches() -> str:
    # TODO: Update docs
    """Finds matches between 'WORD_LIST' and the results of dice rolls.
    
    - Checks if the value in the index [0] of each list in 
    'WORD_LIST' is in 'all_results'.
    - If True, apppends the value in index [1] of 'WORD_LIST'
    to 'matches'.
    - Values in matches are then joined into a single string.

    Returns:
        str: A string of matches found between 'WORD_LIST' and
        'all_results'
    """
    all_results = execute_roll_a_dice()

    matches = []

    for split_line in WORD_LIST:
        if split_line[0] in all_results:
            matches.append(split_line[1])

    return ' '.join(matches)


if __name__ == '__main__':
    print(find_matches())
