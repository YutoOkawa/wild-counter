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
        # TODO: カードクラス,枚数,デッキ名を要素に持つクラスを持つようにする
        # TODO: 入力された枚数が現在ある値よりも大きい場合は値を更新する(これは更新クラスメソッドを生やして良いかも)
        cardDetail = CardDetail(card, count, deck)
        self.cardList.append(cardDetail)
        # if card in self.cardList:
        #     self.cardList[card].append(deck)
        # else:
        #     self.cardList[card] = [deck]

    def printCardList(self):
        for key in self.cardList:
            print(key, self.cardList[key])

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
            self.inputCard(card, deck)
            if self.inputString("カードを追加しました\n追加を続けますか？(y/n)") == "n":
                break
        print("WildCounter finished")
        self.printCardList()
