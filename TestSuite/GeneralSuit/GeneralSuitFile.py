import unittest
from TestCases import AddProductInCartTest
from TestCases import AmazonFullTest
from TestCases import LoginNegativTest
from TestCases import PasswordNegativTest

class GeneraleSuitClass(unittest.TestSuite):
    def suit_test(self):
        suite = unittest.TestSuite()
        suite.addTest(LoginNegativTest.LoginTestClass('test_simpleTC'))
        suite.addTest(PasswordNegativTest.LoginTestClass('test_simpleTC'))
        suite.addTest(AddProductInCartTest.AmazonTestClass('test_simpleTC'))
        suite.addTest(AmazonFullTest.AmazonTestClass('test_simpleTC'))
        return suite



