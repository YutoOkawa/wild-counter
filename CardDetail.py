from Card import Card

class CardDetail:
    def __init__(self, card, deck):
        self.card = card
        self.deck = (deck,)
    
    def __eq__(self, other):
        return self.card == other.card and self.deck == other.deck
    
    def __hash__(self):
        return hash((self.card, self.count, self.deck))
    
    def __str__(self):
        return f"CardDetail({self.card}, {self.___deckstr___()})"

    def ___deckstr___(self):
        deckStr = "Deck("
        for deck in self.deck:
            deckStr += f"{deck.name}:{deck.count},"
        deckStr += ")"
        return deckStr

    def isIncludedCard(self, card):
        return self.card == card
    
    def updateCount(self, count):
        self.count = count
    
    def updateDeck(self, deck):
        self.deck += (deck,)