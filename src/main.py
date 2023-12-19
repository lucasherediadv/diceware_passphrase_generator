"""Docstring"""
import random


def roll_a_dice(number_of_rolls: int = 5) -> list:
    """Generates a list of random dice rolls.
    
    Args:
        number_of_rolls (int): Number of times to roll the dice.

    Returns:
        list: List of dice roll results.
    """

    return [random.randint(1, 6) for _ in range(number_of_rolls)]


def execute_roll_a_dice() -> list:
    """Executes multiple rolls of the dice
    
    Returns:
        list: A list of lists, where each 
        sublist contains the results of rolls of a dice.
    """

    dice_rolls = [roll_a_dice() for _ in range(5)]
    return dice_rolls


def format_results() -> list:
    """Generates a list of strings representing
    the results of multiple dice rolls.
    
    Returns:
        list: A list of strings, where each string 
        represents the concatenated results of each dice roll
    """

    results = execute_roll_a_dice()
    results = ["".join(map(str, result)) for result in results]
    return results


def find_matches() -> str:
    """Docs"""
    with open("diceware_list.txt", "r", encoding="utf=8") as f:
        lines = f.readlines()

    results = format_results()

    matches = []
    for line in lines:
        for result in results:
            if result in line:
                matches.append(line.split()[1])

    return matches

    # string = " ".join(str(x) for x in matches)
    # return string


passphrase = find_matches()
print(passphrase)
