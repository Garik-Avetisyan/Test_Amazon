import unittest
from TestSuite.GeneralSuit import GeneralSuitFile

class RunClass():
    def run(self, suite):
        runner = unittest.TextTestRunner()
        runner.run(suite)

if __name__ == "__main__":
    runner = RunClass()
    suit = GeneralSuitFile.GeneraleSuitClass()
    runner.run(suit.suit_test())


