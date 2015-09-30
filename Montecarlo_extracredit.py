import sys
from Deck import *
from Histogram import *
from Blackjack import *


num_hands = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
h = Histogram(num_hands)


def montecarlo():
    deck = Deck(BlackjackCard)
    deck.shuffle()

    hand = [ ] 
    result = 0

    while result < 22:
        hand += deck.deal(1)
        result = total(hand)
    
    # add 1 to the appropriate bin
    h.count(len(hand))


def main():
    print("Iterating 1,000,000 hands...")
    
    for i in range(1000000):
        montecarlo()
        
    print(h) # print the histogram result in shell


main()
