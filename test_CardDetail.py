from Card import Card
from CardDetail import CardDetail
import unittest

class CardDetailTest(unittest.TestCase):
    def test_CardDetail(unittest):
        # GIVEN
        expectedCard = Card("test_name", "test_symbol")

        # WHEN
        cardDetail = CardDetail(Card("test_name", "test_symbol"), 4, "test_deck")

        assert cardDetail.card == expectedCard
        assert cardDetail.count == 4
        assert cardDetail.deck == ("test_deck",)

    def test_CardDetail_isIncludedCard(unittest):
        # GIVEN
        expectedCard = Card("test_name", "test_symbol")
        cardDetail = CardDetail(Card("test_name", "test_symbol"), 4, "test_deck")

        # WHEN
        isIncluded = cardDetail.isIncludedCard(expectedCard)

        # THEN
        assert isIncluded == True

    def test_CardDetail_updateCount(unittest):
        # GIVEN
        cardDetail = CardDetail(Card("test_name", "test_symbol"), 2, "deck")

        # WHEN
        cardDetail.updateCount(3)

        # THEN
        assert cardDetail.count == 3

    def test_updateDeck(unittest):
        # GIVEN
        cardDetail = CardDetail(Card("test_name", "test_symbol"), 2, "deck")

        # WHEN
        cardDetail.updateDeck("new_deck")

        # THEN
        assert cardDetail.deck == ("deck", "new_deck")