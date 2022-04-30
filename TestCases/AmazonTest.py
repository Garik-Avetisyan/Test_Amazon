from selenium import webdriver
import time
import unittest
from Pages.LogInPage import MainPageClass
from Pages.HomePageAmazon import HomePageAmazonClass
from Pages.CartPage import CartPageClass
from Pages.SearchResultPage import SearchResultClass
from Pages.ProductPage import ProductPageClass


class AmazonTestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.mainPage = MainPageClass(self.driver)
        self.homePageAmazon = HomePageAmazonClass(self.driver)
        self.cartPage = CartPageClass(self.driver)
        self.searchResult = SearchResultClass(self.driver)
        self.productPage = ProductPageClass(self.driver)

    def test_simpleTC(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&") # open youtube
        time.sleep(2)
        self.mainPage.fill_login("garikavetisyantest@mail.ru")
        time.sleep(2)
        self.mainPage.press_continue()
        time.sleep(2)
        self.mainPage.fill_password("Ankappass$")
        time.sleep(2)
        self.mainPage.click_remember_me()
        time.sleep(2)
        self.mainPage.press_signin_button()
        time.sleep(2)
        self.homePageAmazon.push_cart()
        time.sleep(2)
        self.cartPage.delete_all_products()
        time.sleep(2)
        self.homePageAmazon.push_home_page()
        time.sleep(2)
        self.homePageAmazon.file_search_field("watch for men")
        time.sleep(2)
        self.homePageAmazon.click_search_button()
        time.sleep(2)
        self.searchResult.open_first_element()
        time.sleep(2)
        self.productPage.add_to_cart()

    def tearDown(self):
        time.sleep(10)
        self.driver.close()