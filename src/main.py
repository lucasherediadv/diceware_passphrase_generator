"""This program generates a passphrase of six words using the diceware 
method.

It simulates rolling five dice, uses the results to select a word
from a predefined list and repeat the process six times to generates
a secure and memorable passphrase.
"""

from secrets import randbelow

# Represent the number of dice to be rolled simultaneously.
# It is set to 5, corresponding to the 5-digit representation of words
# in the word list.
DICE_ROLLS = 5

# Represents the number of words in the passphrase.
# Defines the number of times 'roll_a_dice()' will be executed.
EXECUTIONS = 6

# Path to the word list used to generate the passphrase.
WORD_LIST_FILE = "wordlist/eff_large_wordlist.txt"


def load_word_list(file_path: str) -> list[list[str]]:
    """Load the word list from a file.

    Each line in the file is split into a list of strings. The results
    is a list of lists, where each inner list represents a line in
    the file.

    Args:
        file_path (str): The path to the file containing the word list.

    Returns:
        list[list[str]]: A list of lists representing the word list.
        Each inner list is a list from the file, split into strings.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.split() for line in file]


def roll_a_dice() -> list[int]:
    """Simulates the roll of five dice, each producing a random number
    between 1 and 6.

    Generates a list of five integers, each representing the result of
    a dice roll. Each roll is independent and the results are stored in
    the list in the order they were rolled.

    Returns:
        list[int]: A list of five integers,
        each between 1 and 6, inclusive
    """
    return [randbelow(6) + 1 for _ in range(DICE_ROLLS)]


def execute_roll_a_dice() -> list[str]:
    """Executes 'roll_a_dice() in range 'EXECUTIONS' and returns
    the results as a list of strings.

    Concatenates the digits generated by 'roll_a_dice()' into a string
    and appends it to the result list.

    Returns:
        list[str]: A list of strings. Each string is a concatenation of
        the digits obtained from a single execution of 'roll_a_dice'.
    """
    results = []

    for _ in range(EXECUTIONS):
        roll_result = roll_a_dice()
        str_result = "".join(map(str, roll_result))
        results.append(str_result)

    return results


def find_matches(word_list: list[list[str]], all_results: list[str]) -> str:
    """Finds matches between elements in 'WORD_LIST' and the results
    of 'execute_roll_a_dice()'.

    - Checks if the first element (index[0]) of each sublist in
    'WORD_LIST' is present in the results of 'execute_roll_a_dice()'.
    - If True, apppends the second element (index[1]) of the sublist
    from 'WORD_LIST' to 'matches'.
    - Join the elements in 'matches' into a single string.

    Returns:
        str: A string of matches found between 'WORD_LIST' and
        'all_results', separated by spaces.
    """
    matches = []

    for split_line in word_list:
        if split_line[0] in all_results:
            matches.append(split_line[1])

    return " ".join(matches)


def main() -> None:
    """Main function to tie all the steps together.

    This function performs three main steps:
    - Loads a list of words from a file.
    - Execute a dice roll simulation.
    - Finds and prints matches between the word list and the dice roll
    results.

    Returns:
        None.
    """
    word_list = load_word_list(WORD_LIST_FILE)

    all_results = execute_roll_a_dice()

    print(find_matches(word_list, all_results))


if __name__ == "__main__":
    main()
