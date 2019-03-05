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