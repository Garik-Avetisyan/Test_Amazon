import unittest
from TestCases import CartPageTests


class CartSuitClass(unittest.TestSuite):
    def cart_suit_test(self):
        suite = unittest.TestSuite()
        suite.addTest(CartPageTests.CartPageTestClass('test_delate_one_product'))
        suite.addTest(CartPageTests.CartPageTestClass('test_delate_all_product'))
        return suite