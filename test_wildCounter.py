from wildCounter import WildCounter
from CardDetail import CardDetail
from Card import Card
from Deck import Deck
import unittest
import sys
import io

class WildCounterTest(unittest.TestCase):
    def stub_stdin(testcase_inst, inputs):
        stdin = sys.stdin

        def cleanup():
            sys.stdin = stdin

        testcase_inst.addCleanup(cleanup)
        sys.stdin = io.StringIO(inputs)


    def stub_stdouts(testcase_inst):
        stdout = sys.stdout

        def cleanup():
            sys.stdout = stdout

        testcase_inst.addCleanup(cleanup)
        sys.stdout = io.StringIO()

    def test_inputNumber(unittest):
        # GIVEN
        wc = WildCounter()
        expectedNumber = 4
        WildCounterTest.stub_stdin(unittest, "4\n")
        WildCounterTest.stub_stdouts(unittest)

        # WHEN
        number = wc.inputNumber("test prompt")

        # THEN
        assert number == expectedNumber

    def test_inputString(unittest):
        # GIVEN
        wc = WildCounter()
        expectedString = "test"
        WildCounterTest.stub_stdin(unittest, "test\n")
        WildCounterTest.stub_stdouts(unittest)

        # WHEN
        string = wc.inputString("test prompt")

        # THEN
        assert string == expectedString

    def test_inputCard(unittest):
        # GIVEN
        wc = WildCounter()
        expectedCard = Card("test_name", "test_symbol")
        expectedDeck = Deck("deck", 4)
        expectedCardDetail = CardDetail(expectedCard, expectedDeck)

        # WHEN
        wc.inputCard(expectedCard, expectedDeck)

        # THEN
        assert wc.cardList[0] == expectedCardDetail
        assert wc.cards == {expectedCard}

    def test_calculateWildCard(unittest):
        # GIVEN
        wc = WildCounter()
        wc.cardList = [CardDetail(Card("test_name", "test_symbol"), Deck("deck", 4)), CardDetail(Card("test_name", "test_symbol"), Deck("deck", 2))]

        # WHEN
        count = wc.calculateWildCard()

        # THEN
        assert count == 6

    def test_calculateSymbolWildCard(unittest):
        # GIVEN
        wc = WildCounter()
        wc.cardList = [CardDetail(Card("test_name", "DMU"), Deck("deck", 4)), CardDetail(Card("test_name", "BRO"), Deck("deck", 2))]

        # WHEN
        dmuCount = wc.calculateSymbolWildCard("DMU")
        broCount = wc.calculateSymbolWildCard("BRO")

        # THEN
        assert dmuCount == 4
        assert broCount == 2

    def test_calculateDeckWildCard(unittest):
        # GIVEN
        wc = WildCounter()
        wc.cardList = [CardDetail(Card("test_name", "DMU"), Deck("deck", 4)), CardDetail(Card("test_name", "BRO"), Deck("deck", 2))]

        # WHEN
        deckCount = wc.calculateDeckWildCard("deck")

        # THEN
        assert deckCount == 6
    
    def test_updateCardDetail(unittest):
        # GIVEN
        wc = WildCounter()
        wc.inputCard(Card("test_name", "test_symbol"), Deck("deck", 2))
        testCardDetail = CardDetail(Card("test_name", "test_symbol"), Deck("deck", 2))
        testNewDeck = Deck("new_deck", 2)

        # WHEN
        wc.updateCardDetail(testCardDetail, testNewDeck)

        # THEN
        assert wc.cardList[0].deck == (Deck("deck", 2), Deck("new_deck", 2))