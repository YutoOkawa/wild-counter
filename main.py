from wildCounter import WildCounter
from Card import Card
import csv

if __name__ == "__main__":
    wc = WildCounter()
    # wc.start()
    with open('Standard.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            card = Card(row[0], row[1])
            wc.inputCard(card, int(row[2]), row[3])

    print("WildCounter finished")
    wc.printCardList()
    print("WildCard総数:", wc.calculateWildCard())
    for symbol in wc.symbol:
        print(symbol, ":", wc.calculateSymbolWildCard(symbol))