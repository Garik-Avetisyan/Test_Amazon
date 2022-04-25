from selenium.webdriver.common.by import By


# LogIn page

logInPageEmailInputField = (By.ID, "ap_email")
logInPageContinueButton = (By.ID, "continue")
logInPagePassInputField = (By.ID, "ap_password")
logInPageRememberMe = (By.NAME, "rememberMe")
logInPageSignInButton = (By.ID, "signInSubmit")


# Home page

homePageCart = (By.ID, "nav-cart-count")


# Cart page

cartPageCartCount = (By.ID, "nav-cart-count")
cartPageDeleteButton = (By.XPATH, "(//input[@value='Delete'])[1]")