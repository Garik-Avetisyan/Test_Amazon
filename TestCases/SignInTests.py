import time
import unittest
from Pages.Signin.LogInPage import LoginPageClass
from Pages.Signin.PasswordPage import PasswordPageClass
from Common.GeneralSetUp.SetUpFile import SetUpClass
from Common.PersonalVariables.PersonalVariablesFile import *


class LoginTestClass(unittest.TestCase, SetUpClass, PersonalVariablesClass):
    def setUp(self):
        self.generalSetUp()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)


    def test_login_negativ(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginPage.fill_login(PersonalVariablesClass.negativ_login(self))
        self.loginPage.press_continue()
        self.passwordPage.fill_password(PersonalVariablesClass.password(self))
        self.passwordPage.click_remember_me()
        self.passwordPage.press_signin_button()

    def test_password_negativ(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginPage.fill_login(PersonalVariablesClass.login(self))
        self.loginPage.press_continue()
        self.passwordPage.fill_password(PersonalVariablesClass.negativ_password(self))
        self.passwordPage.click_remember_me()
        self.passwordPage.press_signin_button()

    def test_login_positiv(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginPage.fill_login(PersonalVariablesClass.login(self))
        self.loginPage.press_continue()
        self.passwordPage.fill_password(PersonalVariablesClass.password(self))
        self.passwordPage.click_remember_me()
        self.passwordPage.press_signin_button()




    def tearDown(self):
        time.sleep(1)
        self.driver.close()

