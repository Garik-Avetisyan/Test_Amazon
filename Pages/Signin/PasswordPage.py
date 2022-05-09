import time
from LocatorsFile.AmazonLocators import *
from Common.CustumFind.FindElement import FindElement

class PasswordPageClass():
    def __init__(self,driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

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
        signInButton = self.findElement.find(*logInPageSignInButton)
        signInButton.click()

#validation block
        try:
            self.findElement.find(*goHomePage)
            print("password page OK")
            print("sign_in")
        except:
            error_masage = str(self.findElement.find(*errorMasage).text)
            print(error_masage)
            exit("error code = 02")