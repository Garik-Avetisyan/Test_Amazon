import unittest
from TestSuite.CartPageSuit import CartPageSuitFile

class CartRunClass():
    def run(self, suite):
        runner = unittest.TextTestRunner()
        runner.run(suite)

if __name__ == "__main__":
    runner = CartRunClass()
    suit = CartPageSuitFile.CartSuitClass()
    runner.run(suit.cart_suit_test())