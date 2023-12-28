"""Program Docs"""
from random import randint


def roll_a_dice() -> list:
    """Generates a list of random numbers between 1 and 6
    simulating the roll of a dice.

    Returns:
        list: list of random numbers.
    """
    return [randint(1, 6) for _ in range(5)]


def execute_roll_a_dice() -> list[str]:
    """Rolls the dice 6 times and returns the results as
    a list of strings.

    Returns:
        A list of 6 strings, each of which is a concatenation
        of the digits obtained from rolling a dice.
    """
    return ["".join(map(str, roll_a_dice())) for _ in range(6)]


def find_matches() -> str:
    """Find matches between the lines in eff_wordlist.txt and the
    results of execute_roll_a_dice().

    Returns:
        A string containing the second word of each line in
        eff_wordlist.txt that contains a match with any of the
        results of execute_roll_a_dice().
    """
    with open("list/eff_wordlist.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    results = execute_roll_a_dice()

    matches = []
    for line in lines:
        split_line = line.split()
        if split_line[0] in results:
            matches.append(split_line[1])

    # Convert matches(list[str]) into a space-separated string.
    return " ".join(map(str, matches))


if __name__ == "__main__":
    print(find_matches())
