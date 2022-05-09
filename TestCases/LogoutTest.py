import time
import unittest
from Pages.Signin.LogInPage import LoginPageClass
from Pages.Signin.PasswordPage import PasswordPageClass
from Pages.MainPage.HomePageAmazon import HomePageAmazonClass
from Common.GeneralSetUp.SetUpFile import SetUpClass
from Common.PersonalVariables.PersonalVariablesFile import *



class AmazonTestClass(unittest.TestCase, SetUpClass, PersonalVariablesClass):
    def setUp(self):
        self.generalSetUp()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)
        self.homePageAmazon = HomePageAmazonClass(self.driver)


    def test_simpleTC(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginPage.fill_login(PersonalVariablesClass.login(self))
        self.loginPage.press_continue()
        self.passwordPage.fill_password(PersonalVariablesClass.password(self))
        self.passwordPage.click_remember_me()
        self.passwordPage.press_signin_button()
        self.homePageAmazon.sign_out()




    def tearDown(self):
        time.sleep(1)
        self.driver.close()

