from Card import Card
import unittest

class CardTest(unittest.TestCase):
    def test_Card(self):
        # GIVEN
        expectedCard = Card("test_name", "test_symbol")
        
        # THEN
        assert expectedCard.name == "test_name"
        assert expectedCard.symbol == "test_symbol"