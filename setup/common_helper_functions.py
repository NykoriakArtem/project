from simple_settings import settings
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located,
    element_to_be_clickable
)
from locators.login_page import LoginPageLocators


def log_in_with_admin_user(self, user):
    driver = self.driver
    wait = self.wait
    driver.get(settings.URL)
    driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.email)
    driver.find_element(*LoginPageLocators.NEXT_LOGIN_BUTTON).click()
    wait.until(visibility_of_element_located(LoginPageLocators.PASSWORD_FIELD))
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user.pw)

    driver.find_element(*LoginPageLocators.NEXT_LOGIN_BUTTON).click()
    wait.until(visibility_of_element_located(LoginPageLocators.DASHBOARD_LOGO))


def find_element_click(self, element):
    self.wait.until(element_to_be_clickable(element))
    self.driver.find_element(*element).click()


def find_element_send_keys(self, element, *args):
    self.wait.until(visibility_of_element_located(element))
    self.driver.find_element(*element).send_keys(args)
