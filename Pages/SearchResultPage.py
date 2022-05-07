from LocatorsFile.AmazonLocators import *
from Common.CustumFind.FindElement import FindElement

class SearchResultClass():
    def __init__(self,driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def open_first_element(self):
        firstElement = self.findElement.find(*resultPageFirstProduct)
        firstElement.click()
