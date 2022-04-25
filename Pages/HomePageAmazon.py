from selenium.webdriver.common.by import By
import time
from LocatorsFile.AmazonLocators import *

class HomePageAmazonClass():
    def __init__(self,driver):
        self.driver = driver

    def push_cart(self):
        cart = self.driver.find_element(*homePageCart)
        cart.click()
        time.sleep(3)