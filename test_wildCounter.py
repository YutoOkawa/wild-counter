from wildCounter import WildCounter
from Card import Card
import unittest

class WildCounterTest(unittest.TestCase):
    def testInputCard(unittest):
        # GIVEN
        wc = WildCounter()
        expectedCard = Card("test_name", "test_symbol", 4)
        expectedDeck = ["deck"]

        # WHEN
        wc.inputCard("test_name", "test_symbol", 4, "deck")

        # THEN
        assert wc.cardList[expectedCard] == expectedDeck