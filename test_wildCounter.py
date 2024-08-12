from wildCounter import WildCounter
from Card import Card
import unittest

class WildCounterTest(unittest.TestCase):
    def test_inputCard(unittest):
        # GIVEN
        wc = WildCounter()
        expectedCard = Card("test_name", "test_symbol", 4)
        expectedDeck = ["deck"]

        # WHEN
        wc.inputCard("test_name", "test_symbol", 4, "deck")

        # THEN
        assert wc.cardList[expectedCard] == expectedDeck

    def test_cardList_does_not_have_multiple_key_and_have_lists_of_decks(unittest):
        # GIVEN
        wc = WildCounter()
        card = Card("test_name", "test_symbol", 4)
        
        # WHEN
        wc.inputCard("test_name", "test_symbol", 4, "deck")
        wc.inputCard("test_name", "test_symbol", 4, "deck2")

        # THEN
        assert len(wc.cardList) == 1
        assert wc.cardList[card] == ["deck", "deck2"]