from LocatorsFile.AmazonLocators import *
from Common.CustumFind.FindElement import FindElement

class HomePageAmazonClass():
    def __init__(self,driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def push_cart(self):
        cart = self.findElement.find(*homePageCart)
        cart.click()


    def push_home_page(self): # todo
        homePage = self.findElement.find(*goHomePage)
        homePage.click()


    def file_search_field(self,txt):
        fileSearch = self.findElement.find(*clickFileSearch)
        fileSearch.click()
        fileSearch.send_keys(txt)

    def click_search_button(self):
        searchButton = self.findElement.find(*clickSearchButton)
        searchButton.click()
