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