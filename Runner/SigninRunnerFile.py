import unittest
from TestSuite.SignInSuit import SignInSuitFile

class SigninRunClass():
    def run(self, suite):
        runner = unittest.TextTestRunner()
        runner.run(suite)

if __name__ == "__main__":
    runner = SigninRunClass()
    suit = SignInSuitFile.SignInSuitClass()
    runner.run(suit.signin_suit_test())