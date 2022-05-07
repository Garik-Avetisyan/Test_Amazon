import time
from LocatorsFile.AmazonLocators import *
from Common.CustumFind.FindElement import FindElement

class MainPageClass():
    def __init__(self,driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def fill_login(self,login):
        emailInputField = self.findElement.find(*logInPageEmailInputField)
        emailInputField.click()
        time.sleep(1)
        emailInputField.clear()
        time.sleep(2)
        emailInputField.send_keys(login)


    def press_continue(self):
        continueButton = self.findElement.find(*logInPageContinueButton)
        continueButton.click()

    def fill_password(self,password):
        passInputField = self.findElement.find(*logInPagePassInputField)
        passInputField.click()
        time.sleep(1)
        passInputField.clear()
        time.sleep(2)
        passInputField.send_keys(password)

    def click_remember_me(self):
        rememnberMe = self.findElement.find(*logInPageRememberMe)
        rememnberMe.click()


    def press_signin_button(self):
        signInButton = self.findElement.find(By.ID, "signInSubmit")
        signInButton.click()
