from Card import Card

class WildCounter:
    def __init__(self):
        self.cardList = {}
        self.symbol = ["DMU", "BRO", "ONE", "MOM", "MAT", "WOE", "LCI", "MKM", "OTJ", "BIG", "BLB"]

    def printStandardFormat(self):
        print("スタンダードフォーマット:", self.symbol)

    def inputCard(self, name, symbol, count, deck):
        card = Card(name, symbol, count)
        if card in self.cardList:
            self.cardList[card].append(deck)
        else:
            self.cardList[card] = [deck]

    def start(self):
        print("WildCounter started")