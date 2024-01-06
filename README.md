# Diceware Passphrase Generator

This is a simple passphrase generator that uses the diceware method.

## What is the diceware method?

The Diceware method is a simple and effective way to generate strong and memorable passphrases. It involves rolling dice to generate a sequence of random numbers, which are then used to look up words in a list. By combining several words from the list, you can create a passphrase that is both easy to remember and difficult to guess

## Why use the diceware method?

The Diceware method is a great way to generate strong and memorable passphrases because it relies on true randomness. Unlike passwords that are based on personal information or common words, Diceware passphrases are truly random and therefore much harder to crack.

## How to use the program

Follow these steps to use the program:

1. **Clone the respository** to your local machine:

```
# Clone the repo
$ git clone https://github.com/lucasherediadv/diceware_passphrase_generator.git

# Change working directory
$ cd diceware_passphrase_generator
```

2. **Install the program** using pip:

```
$ pip install .
```

3. **Run the program** from the command line using the diceware command:

```
$ diceware
creamer eastbound expletive headcount slot widget
```

## Word list

The word list used by this program is the [Electronic Frontier Foundation](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) word list by [Joseph Bonneau](https://www.eff.org/about/staff/joseph-bonneau). This list was designed for memorability and passphrase strength.  

For more information about the list used see [here](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases).

## License

Diceware Passphrase Generator its released under the MIT license.

Diceware is a trademark of [Arnold Reinhold](https://theworld.com/~reinhold/).

The copyright for the [EFF large list](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) belongs to [Joseph Bonneau](https://www.eff.org/about/staff/joseph-bonneau) and [EFF](https://www.eff.org/)
