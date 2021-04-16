from simple_settings import settings
from setup.driver_manager import DriverManager
from setup.common_helper_functions import log_in_with_admin_user
from setup.custom_assertions import wait_and_assert_displayed
from locators.login_page import LoginPageLocators


class TestLogin(DriverManager):
    def test_login(self):

        log_in_with_admin_user(self, settings.Contrast.AdminUser())

        wait_and_assert_displayed(self, LoginPageLocators.DASHBOARD_LOGO)
