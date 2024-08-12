from Card import Card

class WildCounter:
    def __init__(self):
        self.cardList = {}
        self.symbol = ["DMU", "BRO", "ONE", "MOM", "MAT", "WOE", "LCI", "MKM", "OTJ", "BIG", "BLB"]

    def printStandardFormat(self):
        print("スタンダードフォーマット:", self.symbol)
    
    def inputNumber(self):
        while True:
            try:
                number = int(input())
            except ValueError as err:
                print(err)
                print("数字を入力してください")
                continue
            break
        return number

    def inputString(self):
        return input()

    def inputCard(self, card, deck):
        if card in self.cardList:
            self.cardList[card].append(deck)
        else:
            self.cardList[card] = [deck]

    def start(self):
        print("WildCounter started")
        