import time
from LocatorsFile.AmazonLocators import *


class ProductPageClass():
    def __init__(self,driver):
        self.driver = driver

    def add_to_cart(self):
        addToCart = self.driver.find_element(*addToCartButtn)
        addToCart.click()