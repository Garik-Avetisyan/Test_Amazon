import time
from LocatorsFile.AmazonLocators import *
from Common.CustumFind.FindElement import FindElement



class LoginPageClass():
    def __init__(self, driver):
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

#validation block
        try:
            self.findElement.find(*logInPagePassInputField)
            print("login page OK")
        except:
            error_masage = str(self.findElement.find(*errorMasage).text)
            print(error_masage)
            exit("error code = 01")
