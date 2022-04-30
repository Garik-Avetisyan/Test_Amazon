import time
from LocatorsFile.AmazonLocators import *

class MainPageClass():
    def __init__(self,driver):
        self.driver = driver

    def fill_login(self,login):
        emailInputField = self.driver.find_element(*logInPageEmailInputField)
        emailInputField.click()
        time.sleep(1)
        emailInputField.clear()
        time.sleep(3)
        emailInputField.send_keys(login)


    def press_continue(self):
        continueButton = self.driver.find_element(*logInPageContinueButton)
        continueButton.click()

    def fill_password(self,password):
        passInputField = self.driver.find_element(*logInPagePassInputField)
        passInputField.click()
        time.sleep(1)
        passInputField.clear()
        time.sleep(3)
        passInputField.send_keys(password)

    def click_remember_me(self):
        rememnberMe = self.driver.find_element(*logInPageRememberMe)
        rememnberMe.click()


    def press_signin_button(self):
        signInButton = self.driver.find_element(By.ID, "signInSubmit")
        signInButton.click()
