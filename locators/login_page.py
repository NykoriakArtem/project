from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.XPATH, "//*[@name='username']")
    NEXT_LOGIN_BUTTON = (By.XPATH, "//*[@class='btn btn-primary btn-lg btn-block text-center ng-binding ng-isolate-scope ladda-button']")
    PASSWORD_FIELD = (By.XPATH, "//*[@name='password']")
    DASHBOARD_LOGO = (By.XPATH, "//*[@class='logo-image hidden-sm']")