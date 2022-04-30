from selenium.webdriver.common.by import By


# LogIn page
logInPageEmailInputField = (By.ID, "ap_email")
logInPageContinueButton = (By.ID, "continue")
logInPagePassInputField = (By.ID, "ap_password")
logInPageRememberMe = (By.NAME, "rememberMe")
logInPageSignInButton = (By.ID, "signInSubmit")


# Home page
homePageCart = (By.ID, "nav-cart-count")
goHomePage = (By.ID, "nav-logo-sprites")
clickFileSearch = (By.ID, "twotabsearchtextbox")
clickSearchButton = (By.ID, "nav-search-submit-button")

# Cart page
cartPageCartCount = (By.ID, "nav-cart-count")
cartPageDeleteButton = (By.XPATH, "(//input[@value='Delete'])[1]")


# Search result page
resultPageFirstProduct = (By.XPATH, "(//span[@class='a-size-base-plus a-color-base a-text-normal'])[1]")

#product page
addToCartButtn = (By.ID, "add-to-cart-button")