from Card import Card
from CardDetail import CardDetail
import pprint

class WildCounter:
    def __init__(self):
        self.cardList = []
        self.cards = set()
        self.symbol = ["DMU", "BRO", "ONE", "MOM", "MAT", "WOE", "LCI", "MKM", "OTJ", "BIG", "BLB"]

    def printStandardFormat(self):
        print("スタンダードフォーマット:", self.symbol)

    def calculateWildCard(self):
        count = 0
        for cardDetail in self.cardList:
            deckCount = 0
            for deck in cardDetail.deck:
                if deckCount < deck.count:
                    deckCount = deck.count
            count += deckCount
        return count

    def calculateSymbolWildCard(self, symbol):
        count = 0
        for cardDetail in self.cardList:
            deckCount = 0
            for deck in cardDetail.deck:
                if cardDetail.card.symbol == symbol:
                    if deckCount < deck.count:
                        deckCount = deck.count
            count += deckCount
        return count

    def calculateDeckWildCard(self, deckName):
        count = 0
        for cardDetail in self.cardList:
            deckCount = 0
            for deck in cardDetail.deck:
                if deck.name == deckName:
                    if deckCount < deck.count:
                        deckCount = deck.count
            count += deckCount
        return count
    
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

    def inputCard(self, card, deck):
        cardCount = len(self.cards)
        self.cards.add(card)
        if cardCount != len(self.cards):
            self.cardList.append(CardDetail(card, deck))
            return
        else:
            for cardDetail in self.cardList:
                if cardDetail.isIncludedCard(card):
                    self.updateCardDetail(cardDetail, deck)
                    return

    def updateCardDetail(self, cardDetail, newDeck):
        self.cardList.remove(cardDetail)
        cardDetail.updateDeck(newDeck)
        self.cardList.append(cardDetail)

    def printCardList(self):
        for cardDetail in self.cardList:
            print(cardDetail)

    def start(self):
        print("WildCounter started")
        while True:
            # TODO: validation
            name = self.inputString("カード名を入力してください: ")
            self.printStandardFormat()
            symbol = self.inputString("シンボルを入力してください: ")
            count = self.inputNumber("枚数を入力してください: ")
            card = Card(name, symbol)
            deck = self.inputString("デッキ名を入力してください: ")
            self.inputCard(card, count, deck)
            if self.inputString("カードを追加しました\n追加を続けますか？(y/n)") == "n":
                break
        print("WildCounter finished")
        self.printCardList()
        print("WildCard総数:", self.calculateWildCard())
        for symbol in self.symbol:
            print(symbol, ":", self.calculateSymbolWildCard(symbol))
