"""Program Docs"""
from random import randint


def roll_a_dice() -> list:
    """Generates a list of random numbers between 1 and 6,
        simulating the roll of a dice.

    Returns:
        list: list of random numbers.
    """

    # return [randint(1, 6) for _ in range(5)]
    return list(map(lambda x: randint(1, 6), range(5)))


def execute_roll_a_dice() -> list[str]:
    """Rolls the dice 6 times and returns the results as
    a list of strings.

    Returns:
        A list of 6 strings, each string representing
        the result of a dice roll.
    """

    # results = [roll_a_dice() for _ in range(6)]
    results = list(map(lambda x: roll_a_dice(), range(6)))
    # results = [''.join(map(str, result)) for result in results]
    results = list(map(lambda x: "".join(map(str, x)), results))
    return results


def find_matches() -> str:
    """Returns a space-separated string of words from
    'list/eff_large_wordlist.txt' that contain any of
    the results of 'execute_roll_a_dice()'.
    """

    with open("list/eff_large_wordlist.txt", "r", encoding="utf=8") as f:
        lines = f.readlines()

    results = execute_roll_a_dice()

    # matches = []
    # for line in lines:
    #     for result in results:
    #         if result in line:
    #             matches.append(line.split()[1])

    matches = list(
        map(
            lambda x: x.split()[1],
            filter(lambda x: any(result in x for result in results), lines),
        )
    )

    return " ".join(map(str, matches))


if __name__ == "__main__":
    print(find_matches())
