from random import *


class Card():
    def __init__(self, rank, suit):
        self.card=[]
        self.rank = rank
        self.suit = suit
        self.card.append((self.rank,self.suit))


    def __str__(self):
        #return print("string object")
        return print(f"{self.rank} of {self.suit}")

    def __getitem__(self,index):
        return self.card[index]



class Chips():
    def __init__(self):
        self.initialamount=100
        self.bet=0

    def placebet(self, bet_amount):
        self.bet_amount=bet_amount

        if self.bet_amount <= self.initialamount:
            return True
        else:
            print("not enough amount in account")
            return False

    def bet_win(self):
        self.initialamount = self.initialamount + self.bet_amount
        print(f'amount remaining: {self.initialamount}')

    def bet_loose(self):
        self.initialamount = self.initialamount - self.bet_amount
        print(f'amount remaining: {self.initialamount}')


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

        shuffle(self.deck)

    def popacard(self):
        return self.deck.pop()


# define global values

def can_hit_more(cards_at_hand):
    i = len(cards_at_hand)
    #print(list(range(0,i,1)))
    #print(str(i))
    valuesum=0
    for count in range(0, i, 1):
        print("cards_at_hand: "+cards_at_hand[count][0][0])
        valuesum += int(values[cards_at_hand[count][0][0]])
    if valuesum < 21:
        print("Player is eligible to hit more")
        return True
    else:
        return False


def check_if_blackjack(cards_at_hand):
    i = len(cards_at_hand)
    valuesum=0
    for count in range(0,i,1):
        print(values[cards_at_hand[count][0][0]])
        valuesum += int(values[cards_at_hand[count][0][0]])
        if valuesum == 21:
            return True
        else:
            return False

def check_if_busted(cards_at_hand):
    i = len(cards_at_hand)
    valuesum = 0
    for count in range(0, i, 1):
        valuesum += int(values[cards_at_hand[count][0][0]])
        if valuesum == 21:
            return True
        else:
            return False


def declare_winner(dealercard1,dealercard2,playercard):
    print(f"Dealer card #2 is " + dealercard2[0][0] + " of " + dealercard2[0][1])
    dealersum = int(values[dealercard1[0][0]]) + int(values[dealercard2[0][0]])
    playersum=0
    i = len(playercard)
    for count in range(0, i, 1):
        playersum += int(values[playercard[count][0][0]])
    print("playersum: "+str(playersum))
    print("dealersum: "+str(dealersum))
    if dealersum < 21 and playersum < 21:
        if playersum > dealersum:
            return "player"
        elif playersum < dealersum:
            return "dealer"
    elif dealersum > 21:
        print("Dealer busted!")
        return "player"
    elif playersum > 21:
        print("Player busted!")
        return "dealer"
    elif dealersum == 21:
        print("Dealer black-jack")
        return "dealer"

def next_hand(playercard,deck):
    if input("Want to hit ? enter 'y' or 'n'") == 'y':
        playercard.append(deck.popacard())
    return playercard


def another_hand():
    result = input("Do you want to play another hand? Enter 'y' or 'n'")
    if result[0].lower() == 'y':
        return True
    else:
        return False

def main():



        #shuffle the cards:
        deck = Deck()
        deck.shuffle()

        next_hit = True
        while next_hit:

            #Place a bet
            bet=int(input("Make a bet"))
            chips = Chips()
            chips.placebet(bet)

            #Draw cards for Dealer:
            dealercard1 = deck.popacard()

            print(f"Dealer card #1 is "+dealercard1[0][0]+ " of "+dealercard1[0][1])
            dealercard2=deck.popacard()

            #pop 2 cards for Player
            playercard = []

            playercard.append(deck.popacard())
            playercard.append(deck.popacard())

            print(f"Player card #1 is {playercard[0][0][0]} of {playercard[0][0][1]}")
            print(f"Player card #2 is {playercard[1][0][0]} of {playercard[1][0][1]}")

            if check_if_blackjack(playercard):
                print("inside check_if_blackjack")
                print("Player wins")
                if another_hand():
                    continue
                else:
                    if declare_winner(dealercard1, dealercard2, playercard) == "player":
                        print("Player wins")
                    elif declare_winner(dealercard1, dealercard2, playercard) == "dealer":
                        print("Dealer wins")
                    next_hit = False


            if check_if_busted(playercard):
                print("inside check_if_busted")
                print("Busted !! Dealer wins !!")
                if another_hand():
                    continue
                else:
                    if declare_winner(dealercard1, dealercard2, playercard) == "player":
                        print("Player wins")
                    elif declare_winner(dealercard1, dealercard2, playercard) == "dealer":
                        print("Dealer wins")
                    next_hit = False

            hit_more = True
            while hit_more:
                if can_hit_more(playercard):
                    print("inside can_hit_more")
                    if input("Want to hit ? enter 'y' or 'n'") == 'y':
                        playercard.append(deck.popacard())
                        if not check_if_blackjack(playercard):
                            if not check_if_busted(playercard):
                                hit_more=True
                            else:
                                hit_more=False
                        else:
                            hit_more=False
                    else:
                        hit_more=False
                else:
                    hit_more=False


            if declare_winner(dealercard1, dealercard2, playercard) == "player":
                print("Player wins")
            elif declare_winner(dealercard1, dealercard2, playercard) == "dealer":
                print("Dealer wins")



main()