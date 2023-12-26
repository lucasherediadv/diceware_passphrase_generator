"""Used to generate a random integer based on the given range"""
from random import randint


def roll_a_dice():
    """Generates a list of random numbers according according
        to the given range, simulating the roll of a dice.

    Returns:
        list: list of random numbers.
    """

    # return [randint(1, 6) for _ in range(5)]
    return list(map(lambda x: randint(1, 6), range(5)))


def execute_roll_a_dice():
    """Docs"""

    # results = [roll_a_dice() for _ in range(6)]
    results = list(map(lambda x: roll_a_dice(), range(6)))
    # results = [''.join(map(str, result)) for result in results]
    results = list(map(lambda x: ''.join(map(str, x)), results))
    return results


def find_matches():
    """Docs"""

    with open('list/eff_large_wordlist.txt', 'r', encoding='utf=8') as f:
        lines = f.readlines()

    results = execute_roll_a_dice()

    # matches = []
    # for line in lines:
    #     for result in results:
    #         if result in line:
    #             matches.append(line.split()[1])

    matches = list(map(lambda x: x.split()[1],
                       filter(lambda x: any(result in x for result in results), lines)))

    return ' '.join(map(str, matches))


if __name__ == '__main__':
    print(find_matches())
