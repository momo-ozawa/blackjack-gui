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
    print("Creating a Montecarlo model with %d samples..." % sample_size)
    for i in range(sample_size):
        update_bin()
    # Print the histogram result
    print(histogram)


if __name__ == "__main__":
    n = int(input("Enter your sample size:"))
    montecarlo_simulation(n)
