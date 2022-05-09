from LocatorsFile.AmazonLocators import *
from Common.CustumFind.FindElement import FindElement

class ProductPageClass():
    def __init__(self,driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def add_to_cart(self):
        addToCart = self.findElement.find(*addToCartButtn)
        addToCart.click()