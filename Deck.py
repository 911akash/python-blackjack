from random import *
import Card

suits=('Hearts','Diamonds','Spades','Clubs')

ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')

values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':'10','queen':10,
        'king':10,'ace':11}


class Deck():
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        return str(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def popacard(self):
        return self.deck.pop()