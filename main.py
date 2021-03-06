import Chips
import Deck

def can_hit_more(cards_at_hand):
    i = len(cards_at_hand)
    #print(list(range(0,i,1)))
    #print(str(i))
    valuesum=0
    for count in range(0, i, 1):
        print("cards_at_hand: "+cards_at_hand[count][0][0])
        valuesum += int(Deck.values[cards_at_hand[count][0][0]])
    if valuesum < 21:
        print("Player is eligible to hit more")
        return True
    else:
        return False


def check_if_blackjack(cards_at_hand):
    i = len(cards_at_hand)
    valuesum=0
    for count in range(0,i,1):
        #print(Deck.values[cards_at_hand[count][0][0]])
        valuesum += int(Deck.values[cards_at_hand[count][0][0]])
    if valuesum == 21:
        return True
    else:
        return False

def check_if_busted(cards_at_hand):
    i = len(cards_at_hand)
    valuesum = 0
    for count in range(0, i, 1):
        valuesum += int(Deck.values[cards_at_hand[count][0][0]])
    if valuesum == 21:
        return True
    else:
        return False


def declare_winner(dealercard1,dealercard2,playercard):
    print(f"Dealer card #2 is " + dealercard2[0][0] + " of " + dealercard2[0][1])
    dealersum = int(Deck.values[dealercard1[0][0]]) + int(Deck.values[dealercard2[0][0]])
    playersum=0
    i = len(playercard)
    for count in range(0, i, 1):
        playersum += int(Deck.values[playercard[count][0][0]])
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
    elif playersum == 21:
        print("Player black-jack")
        return "player"

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
        deck = Deck.Deck()
        deck.shuffle()

        next_hit = True
        while next_hit:

            #Place a bet
            bet=int(input("Make a bet"))
            chips = Chips.Chips()
            chips.placebet(bet)

            #Draw cards for Dealer:
            dealercard1 = deck.popacard()

            print(f"Dealer card #1 is "+dealercard1[0][0]+ " of "+dealercard1[0][1])
            dealercard2=deck.popacard()

            #pop 2 cards for Player
            playercard = []
            #playercard = [('ten','spades'),('ace','spades')]

            playercard.append(deck.popacard())
            playercard.append(deck.popacard())

            print(f"Player card #1 is {playercard[0][0][0]} of {playercard[0][0][1]}")
            print(f"Player card #2 is {playercard[1][0][0]} of {playercard[1][0][1]}")

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

            result = declare_winner(dealercard1, dealercard2, playercard)
            if result == "player":
                print("Player wins")
            elif result == "dealer":
                print("dealer")


main()