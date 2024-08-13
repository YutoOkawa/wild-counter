from Card import Card
from CardDetail import CardDetail
import unittest

class CardDetailTest(unittest.TestCase):
    def test_CardDetail(self):
        # GIVEN
        expectedCard = Card("test_name", "test_symbol")

        # WHEN
        cardDetail = CardDetail(Card("test_name", "test_symbol"), 4, "test_deck")

        assert cardDetail.card == expectedCard
        assert cardDetail.count == 4
        assert cardDetail.deck == "test_deck"