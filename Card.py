class Card:
    # TODO: カード枚数もカードクラスから隔離したい
    def __init__(self, name, symbol, count):
        self.name = name
        self.symbol = symbol
        self.count = count

    def __eq__(self, other):
        return self.name == other.name and self.symbol == other.symbol and self.count == other.count

    def __hash__(self):
        return hash((self.name, self.symbol, self.count))
    
    def __str__(self):
        return f"Card({self.name}, {self.symbol}, {self.count})"