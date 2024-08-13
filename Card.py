class Card:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __eq__(self, other):
        return self.name == other.name and self.symbol == other.symbol

    def __hash__(self):
        return hash((self.name, self.symbol))
    
    def __str__(self):
        return f"Card({self.name}, {self.symbol})"