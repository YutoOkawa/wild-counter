from wildCounter import WildCounter
from CardDetail import CardDetail
from Card import Card
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
        expectedCardDetail = CardDetail(expectedCard, 4, "deck")

        # WHEN
        wc.inputCard(expectedCard, 4, "deck")

        # THEN
        assert wc.cardList[0] == expectedCardDetail
        assert wc.cards == {expectedCard}

    def test_calculateWildCard(unittest):
        # GIVEN
        wc = WildCounter()
        wc.cardList = [CardDetail(Card("test_name", "test_symbol"), 4, "deck"), CardDetail(Card("test_name", "test_symbol"), 2, "deck")]

        # WHEN
        count = wc.calculateWildCard()

        # THEN
        assert count == 6

    def test_inputCard_should_update_count_when_card_counter_is_upper_than_carddetails(unittest):
        # GIVEN
        wc = WildCounter()
        testCard = Card("test_name", "test_symbol")
        testCard1 = Card("test1_name", "test1_symbol")
        wc.inputCard(testCard, 2, "deck")
        wc.inputCard(testCard1, 2, "deck")

        # WHEN
        wc.inputCard(Card("test_name", "test_symbol"), 3, "deck")

        # THEN
        count = wc.calculateWildCard()
        assert count == 5

    def test_calculateSymbolWildCard(unittest):
        # GIVEN
        wc = WildCounter()
        wc.cardList = [CardDetail(Card("test_name", "DMU"), 4, "deck"), CardDetail(Card("test_name", "BRO"), 2, "deck")]

        # WHEN
        dmuCount = wc.calculateSymbolWildCard("DMU")
        broCount = wc.calculateSymbolWildCard("BRO")

        # THEN
        assert dmuCount == 4
        assert broCount == 2