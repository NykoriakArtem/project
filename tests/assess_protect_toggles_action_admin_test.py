from time import sleep
from simple_settings import settings
from locators.dashboard import DashboardLocators
from locators.servers_page import ServersPageLocators
from setup.driver_manager import DriverManager
from setup.common_helper_functions import (
    log_in_with_admin_user,
    find_element_click
)
from setup.custom_assertions import wait_and_assert_displayed


class TestAssessProtectTogglesActionAdmin(DriverManager):
    def test_assess_protect_toggles_action_admin(self):
        driver = self.driver

        log_in_with_admin_user(self, settings.Contrast.AdminUser())

        find_element_click(self, DashboardLocators.SERVERS_TAB)
        wait_and_assert_displayed(self, ServersPageLocators.SERVERS_PAGE)
        # click toggles on the servers page.
        toggles = driver.find_elements(*ServersPageLocators.ASSESS_PROTECT_TOGGLES_SERVERS_PAGE)
        for x in range(0,len(toggles)):
            if toggles[x].is_displayed():
                toggles[x].click()

        sleep(2)
        # navigate to the sample server and click on toggles there.
        find_element_click(self, ServersPageLocators.SAMPLE_SERVER)
        wait_and_assert_displayed(self, ServersPageLocators.SERVER_PANEL)
        toggles_1 = driver.find_elements(*ServersPageLocators.ASSESS_PROTECT_TOGGLES_SERVERS_OVERVIEW_PAGE)
        # test will fail here b/c of a bug described in BR-003.
        for x in range(0,len(toggles_1)):
            if toggles_1[x].is_enabled():
                toggles_1[x].click()
        print ("Assess and Protect toggles are actionable on the server overview page")