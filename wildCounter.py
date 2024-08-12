from Card import Card

class WildCounter:
    cardList = {}
    def __init__(self):
        self.symbol = ["DMU", "BRO", "ONE", "MOM", "MAT", "WOE", "LCI", "MKM", "OTJ", "BIG", "BLB"]

    def printStandardFormat(self):
        print("スタンダードフォーマット:", self.symbol)

    def inputCard(self, name, symbol, count, deck):
        card = Card(name, symbol, count)
        self.cardList[card] = [deck]

    def start(self):
        print("WildCounter started")