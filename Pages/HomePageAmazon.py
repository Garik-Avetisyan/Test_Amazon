import time
from LocatorsFile.AmazonLocators import *

class HomePageAmazonClass():
    def __init__(self,driver):
        self.driver = driver

    def push_cart(self):
        cart = self.driver.find_element(*homePageCart)
        cart.click()
        time.sleep(1)

    def push_home_page(self):
        homePage = self.driver.find_element(*goHomePage)
        homePage.click()
        time.sleep(1)

    def file_search_field(self,txt):
        fileSearch = self.driver.find_element(*clickFileSearch)
        fileSearch.click()
        time.sleep(1)
        fileSearch.send_keys(txt)

    def click_search_button(self):
        searchButton = self.driver.find_element(*clickSearchButton)
        searchButton.click()
        time.sleep(1)