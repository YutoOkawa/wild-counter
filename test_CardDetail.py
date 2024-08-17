from Card import Card
from Deck import Deck
from CardDetail import CardDetail
import unittest

class CardDetailTest(unittest.TestCase):
    def test_CardDetail(unittest):
        # GIVEN
        expectedCard = Card("test_name", "test_symbol")
        expectedDeck = Deck("test_deck", 4)

        # WHEN
        cardDetail = CardDetail(expectedCard, expectedDeck)

        assert cardDetail.card == expectedCard
        assert cardDetail.deck == (expectedDeck,)

    def test_CardDetail_isIncludedCard(unittest):
        # GIVEN
        expectedCard = Card("test_name", "test_symbol")
        expectedDeck = Deck("test_deck", 4)
        cardDetail = CardDetail(expectedCard, expectedDeck)

        # WHEN
        isIncluded = cardDetail.isIncludedCard(expectedCard)

        # THEN
        assert isIncluded == True

    def test_CardDetail_updateCount(unittest):
        # GIVEN
        cardDetail = CardDetail(Card("test_name", "test_symbol"), Deck("test_deck", 2))

        # WHEN
        cardDetail.updateCount(3)

        # THEN
        assert cardDetail.count == 3

    def test_updateDeck(unittest):
        # GIVEN
        initDeck = Deck("deck", 2)
        cardDetail = CardDetail(Card("test_name", "test_symbol"),initDeck)
        appendDeck = Deck("new_deck", 2)

        # WHEN
        cardDetail.updateDeck(appendDeck)

        # THEN
        assert cardDetail.deck == (initDeck, appendDeck)