# import unittest
# from selenium import webdriver
from simple_settings import settings
from setup.driver_manager import DriverManager
from setup.common_helper_functions import log_in_with_admin_user
from setup.custom_assertions import wait_and_assert_displayed
from selenium.webdriver.common.keys import Keys
from settings.base import Contrast
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located,
    element_to_be_clickable,
)
from locators.login_page import (
    USERNAME_FIELD,
    NEXT_LOGIN_BUTTON,
    PASSWORD_FIELD,
    DASHBOARD_LOGO
)

class TestLogin(DriverManager):
    def test_login(self):

        log_in_with_admin_user(self, settings.Contrast.AdminUser())

        wait_and_assert_displayed(self, DASHBOARD_LOGO)
