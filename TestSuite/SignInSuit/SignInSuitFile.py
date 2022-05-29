import unittest
from TestCases import SignInTests


class SignInSuitClass(unittest.TestSuite):
    def signin_suit_test(self):
        suite = unittest.TestSuite()
        suite.addTest(SignInTests.LoginTestClass('test_login_negativ'))
        suite.addTest(SignInTests.LoginTestClass('test_password_negativ'))
        suite.addTest(SignInTests.LoginTestClass('test_login_positiv'))
        return suite