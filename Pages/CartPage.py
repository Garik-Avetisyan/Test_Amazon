from selenium.webdriver.common.by import By
import time
from LocatorsFile.AmazonLocators import *


class CartPageClass():
    def __init__(self,driver):
        self.driver = driver

    def delete_all_products(self):
        cartCount = self.driver.find_element(*cartPageCartCount)
        numberOfProductsInCart = int(cartCount.text)
        while numberOfProductsInCart > 0:
            deleteButton = self.driver.find_element(*cartPageDeleteButton)
            deleteButton.click()
            numberOfProductsInCart -= 1
            time.sleep(3)

    def delete_one_product(self):
        deleteButton = self.driver.find_element(*cartPageDeleteButton)
        deleteButton.click()