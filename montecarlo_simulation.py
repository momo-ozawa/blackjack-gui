"""
montecarlo_simulation.py: Assignment 2.2, CIS 211
Author: Momo Ozawa

The window in your Blackjack program has room for 6 cards for each player. Is this
enough space? What is the probability of a player needing more than 6 cards?

One way to figure this out is by running a Monte Carlo simulation.
"""

import sys
from Deck import *
from Histogram import *
from Blackjack import *

# Initialize 10 bins, from 1 to 10 
# A bin represents how many cards we need to deal before the total is 22 or higher
num_cards_bin = [i for i in range(1, 11)]
histogram = Histogram(num_cards_bin)


def update_bin():
    """
    For each hand, update the bin that corresponds to the number of cards dealt
    before the total is 22 or higher. Ex. If a hand reaches 25 on the 3rd card 
    add one to the count in bin 3.
    """
    deck = Deck(BlackjackCard)
    deck.shuffle()

    hand = [ ] 
    result = 0

    while result < 22:
        hand += deck.deal(1)
        result = total(hand)

    # Add 1 to the appropriate bin
    histogram.count(len(hand))


def montecarlo_simulation(sample_size):
    print("Creating a Montecarlo model with {} samples... \n".format(sample_size))
    for i in range(sample_size):
        update_bin()
    return histogram


def percentage_by_hand(histogram, sample_size):
    key_value_list = [(k, v) for k, v in histogram.items()]
    for tup in key_value_list:
        print("{:>2.0f} cards: {:>7.4f}%".format(tup[0], (tup[1] / sample_size * 100)))


if __name__ == "__main__":
    n = int(input("Enter your sample size:"))
    results = montecarlo_simulation(n)
    print("HISTOGRAM RESULTS:")
    print(results, "\n")
    print("PERCENTAGE BY BIN:")
    percentage_by_hand(results, n)
