# Diceware Passphrase Generator

A simple passphrase generator that uses the diceware method...

This program uses the [Electronic Frontier Foundation](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) word list, designed for memorability and passphrase strength.

The workflow of this program is based on the directions given by [EFF](https://www.eff.org/dice):

1. Roll five dice all at once.

2. Write the results of each dice.

3. Search the word next to your results in the wordlist.

4. Write down the word.

5. Repeat steps 1-4 five more times to come up with a total of six words.

## Installation

```
$ git clone https://github.com/lucasherediadv/diceware_passphrase_generator.git

$ cd diceware_passphrase_generator/

$ pip install .
```

## Usage

```
$ diceware
creamer eastbound expletive headcount slot widget

```

## License

Diceware Passphrase Generator its released under the MIT license.

Diceware is a trademark of [Arnold Reinhold](https://theworld.com/~reinhold/).

Copyright for the [EFF large list](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) by [Joseph Bonneau](https://www.eff.org/about/staff/joseph-bonneau) and [EFF](https://www.eff.org/)