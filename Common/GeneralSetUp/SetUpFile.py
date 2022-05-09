from selenium import webdriver


class SetUpClass():
    def generalSetUp(self):
        self.driver = webdriver.Chrome("..\\Common\\Driver\\chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    #
    # def a(self):
    #     signOut = self.driver.find_element()
    #     signOut.send_keys("")


