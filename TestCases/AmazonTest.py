# amazon login --- garikavetisyantest@mail.ru
# amazon password -- Ankappass$


from selenium import webdriver
import time
import unittest
from Pages.LogInPage import MainPageClass
from Pages.HomePageAmazon import HomePageAmazonClass
from Pages.CartPage import CartPageClass


class AmazonTestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.mainPage = MainPageClass(self.driver)
        self.homePageAmazon = HomePageAmazonClass(self.driver)
        self.cartPage = CartPageClass(self.driver)

    def test_simpleTC(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&") # open youtube
        self.mainPage.fill_login("garikavetisyantest@mail.ru")
        self.mainPage.press_continue()
        self.mainPage.fill_password("Ankappass$")
        self.mainPage.click_remember_me()
        self.mainPage.press_signin_button()
        self.homePageAmazon.push_cart()
        self.cartPage.delete_all_products()

    def tearDown(self):
        time.sleep(10)
        self.driver.close()