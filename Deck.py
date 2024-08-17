class Deck:
    def __init__(self, name, count):
        self.name = name
        self.count = count
    
    def __eq__(self, other):
        return self.name == other.name and self.count == other.count

    def __hash__(self):
        return hash((self.name, self.count))
    
    def __str__(self):
        return f"Deck({self.name}, {self.count})"