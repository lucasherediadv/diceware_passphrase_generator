# Diceware Passphrase Generator

A simple passphrase generator that uses the diceware method...

This program simulate the roll of five dices, six times, to use the results for pick the words from a wordlist. The wordlist used is the provided by the [Electronic Frontier Foundation](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) designed for memorability and passphrase strength.

The workflow of this program is based on the directions given by the Electronic Frontier Foundation [here](https://www.eff.org/dice):

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