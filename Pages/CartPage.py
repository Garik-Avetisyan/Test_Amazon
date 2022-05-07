from LocatorsFile.AmazonLocators import *
from Common.CustumFind.FindElement import FindElement


class CartPageClass():
    def __init__(self,driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def delete_all_products(self):
        cartCount = self.findElement.find(*cartPageCartCount)
        numberOfProductsInCart = int(cartCount.text)
        while numberOfProductsInCart > 0:
            deleteButton = self.findElement.find(*cartPageDeleteButton)
            deleteButton.click()
            numberOfProductsInCart -= 1

    def delete_one_product(self):
        deleteButton = self.findElement.find(*cartPageDeleteButton)
        deleteButton.click()