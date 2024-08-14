from Card import Card
from CardDetail import CardDetail
import pprint

class WildCounter:
    def __init__(self):
        self.cardList = []
        self.symbol = ["DMU", "BRO", "ONE", "MOM", "MAT", "WOE", "LCI", "MKM", "OTJ", "BIG", "BLB"]

    def printStandardFormat(self):
        print("スタンダードフォーマット:", self.symbol)
    
    def inputNumber(self, prompt):
        while True:
            print(prompt, end="")
            try:
                number = int(input())
            except ValueError as err:
                print(err)
                print("数字を入力してください")
                continue
            break
        return number

    def inputString(self, prompt):
        print(prompt, end="")
        return input()

    def inputCard(self, card, count, deck):
        cardDetail = CardDetail(card, count, deck)
        self.cardList.append(cardDetail)

    def printCardList(self):
        for cardDetail in self.cardList:
            print(cardDetail)

    def start(self):
        print("WildCounter started")
        while True:
            # TODO: validation
            name = self.inputString("カード名を入力してください: ")
            symbol = self.inputString("シンボルを入力してください: ")
            self.printStandardFormat()
            count = self.inputNumber("枚数を入力してください: ")
            card = Card(name, symbol)
            deck = self.inputString("デッキ名を入力してください: ")
            self.inputCard(card, count, deck)
            if self.inputString("カードを追加しました\n追加を続けますか？(y/n)") == "n":
                break
        print("WildCounter finished")
        self.printCardList()
