from selenium import webdriver
import unittest
from Pages.LogInPage import MainPageClass
from Pages.HomePageAmazon import HomePageAmazonClass
from Pages.CartPage import CartPageClass
from Pages.SearchResultPage import SearchResultClass
from Pages.ProductPage import ProductPageClass


class AmazonTestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("..\\Common\\Driver\\chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.mainPage = MainPageClass(self.driver)
        self.homePageAmazon = HomePageAmazonClass(self.driver)
        self.cartPage = CartPageClass(self.driver)
        self.searchResult = SearchResultClass(self.driver)
        self.productPage = ProductPageClass(self.driver)

    def test_simpleTC(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.mainPage.fill_login("garikavetisyantest@mail.ru")
        self.mainPage.press_continue()
        self.mainPage.fill_password("Ankappass$")
        self.mainPage.click_remember_me()
        self.mainPage.press_signin_button()
        self.homePageAmazon.push_cart()
        self.cartPage.delete_all_products()
        self.homePageAmazon.push_home_page()
        self.homePageAmazon.file_search_field("watch for men")
        self.homePageAmazon.click_search_button()
        self.searchResult.open_first_element()
        self.productPage.add_to_cart()



    def tearDown(self):
        self.driver.close()

