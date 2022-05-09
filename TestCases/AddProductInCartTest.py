import time
import unittest
from Pages.Signin.LogInPage import LoginPageClass
from Pages.Signin.PasswordPage import PasswordPageClass
from Pages.MainPage.HomePageAmazon import HomePageAmazonClass
from Pages.CartPage.CartPage import CartPageClass
from Pages.SearchProduct.SearchResultPage import SearchResultClass
from Pages.SearchProduct.SelectedProductPage import ProductPageClass
from Common.GeneralSetUp.SetUpFile import SetUpClass
from Common.PersonalVariables.PersonalVariablesFile import *


class AmazonTestClass(unittest.TestCase, SetUpClass, PersonalVariablesClass):
    def setUp(self):
        self.generalSetUp()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)
        self.homePageAmazon = HomePageAmazonClass(self.driver)
        self.searchResult = SearchResultClass(self.driver)
        self.productPage = ProductPageClass(self.driver)

    def test_simpleTC(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginPage.fill_login(PersonalVariablesClass.login(self))
        self.loginPage.press_continue()
        self.passwordPage.fill_password(PersonalVariablesClass.password(self))
        self.passwordPage.click_remember_me()
        self.passwordPage.press_signin_button()
        self.homePageAmazon.file_search_field(PersonalVariablesClass.searchedProduct(self))
        self.homePageAmazon.click_search_button()
        self.searchResult.open_first_element()
        self.productPage.add_to_cart()
        self.homePageAmazon.click_home_page_button()
        self.homePageAmazon.sign_out()



    def tearDown(self):
        time.sleep(1)
        self.driver.close()

