import time
from LocatorsFile.AmazonLocators import *

class SearchResultClass():
    def __init__(self,driver):
        self.driver = driver

    def open_first_element(self):
        firstElement = self.driver.find_element(*resultPageFirstProduct)
        firstElement.click()
