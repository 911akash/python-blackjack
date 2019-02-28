class Hand():
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0


    def add_card(self,card):
        self.cards.append(card)


    def adjust_for_ace(self):
        for (r,s) in self.cards[]:
            if r == 'ace':
                self.aces += 1