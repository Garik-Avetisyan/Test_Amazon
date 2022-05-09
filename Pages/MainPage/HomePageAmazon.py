import time
from LocatorsFile.AmazonLocators import *
from Common.CustumFind.FindElement import FindElement
from selenium.webdriver.common.keys import Keys



class HomePageAmazonClass():
    def __init__(self,driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)


    def click_cart_button(self):
        cart = self.findElement.find(*homePageCart)
        cart.click()


    def click_home_page_button(self):
        homePage = self.findElement.find(*goHomePage)
        homePage.click()


    def file_search_field(self,txt):
        fileSearch = self.findElement.find(*clickFileSearch)
        fileSearch.click()
        fileSearch.send_keys(txt)

    def click_search_button(self):
        searchButton = self.findElement.find(*clickSearchButton)
        searchButton.click()

    def sign_out(self):
        accountBlock = self.findElement.find(*accountBlockk)
        accountBlock.send_keys(Keys.ENTER)
        signOut = self.findElement.find(*signOutButton)
        signOut.click()




