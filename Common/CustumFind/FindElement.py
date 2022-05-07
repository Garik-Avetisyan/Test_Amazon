from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FindElement():
    def __init__(self,driver):
        self.driver = driver
    def find(self,by:By,licator:str):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((by,licator)))
        return element

