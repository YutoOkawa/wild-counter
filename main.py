from wildCounter import WildCounter
from Card import Card
from Deck import Deck
import csv

if __name__ == "__main__":
    wc = WildCounter()
    # wc.start()
    with open('Standard.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            card = Card(row[0], row[1])
            deck = Deck(row[3], int(row[2]))
            wc.inputCard(card, deck)

    print("WildCounter finished")
    wc.printCardList()
    print("WildCard総数:", wc.calculateWildCard())
    for symbol in wc.symbol:
        print(symbol, ":", wc.calculateSymbolWildCard(symbol))