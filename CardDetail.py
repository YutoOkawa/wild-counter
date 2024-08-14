from Card import Card

class CardDetail:
    def __init__(self, card, count, deck):
        self.card = card
        self.count = count
        self.deck = deck
    
    def __eq__(self, other):
        return self.card == other.card and self.count == other.count and self.deck == other.deck
    
    def __hash__(self):
        return hash((self.card, self.count, self.deck))
    
    def __str__(self):
        return f"CardDetail({self.card}, {self.count}, {self.deck})"

    def isIncludedCard(self, card):
        return self.card == card