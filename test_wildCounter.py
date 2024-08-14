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
