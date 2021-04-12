from random import randint
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from simple_settings import settings
from locators.dashboard import DashboardLocators
from locators.vulnerabilities_page import VulnPageLocators
from setup.driver_manager import DriverManager
from setup.common_helper_functions import (
    log_in_with_admin_user,
    find_element_click,
    find_element_send_keys
)
from setup.custom_assertions import (
    wait_and_assert_displayed,
    wait_and_assert_text_equal
)


class TestAddNewTagFilterUI(DriverManager):
    def test_add_new_tag_filer_ui(self):
        driver = self.driver
        tag_name = f"Test tag {randint(1, 100)}"
        log_in_with_admin_user(self, settings.Contrast.AdminUser())

        find_element_click(self, DashboardLocators.VULNERABILITIES_TAB)
        wait_and_assert_displayed(self, VulnPageLocators.VULNERABILITIES_PAGE)
        # open the first vulnerability item on the list.
        li = driver.find_elements(*VulnPageLocators.VULN_NAME_LINK)
        li[0].click()
        # remove old tags if any.
        find_element_click(self, VulnPageLocators.TAG_ICON)
        try:
            if wait_and_assert_displayed(self, VulnPageLocators.VULNERABILITY_TAG):
                tags = self.driver.find_elements(*VulnPageLocators.TAG_REMOVE_ICON)
                for x in range(0, len(tags)):
                    if tags[x].is_displayed():
                        tags[x].click()
        except TimeoutException:
            find_element_click(self, VulnPageLocators.TAG_CANCEL)
            find_element_click(self, VulnPageLocators.TAG_ICON)
        # create a new unique tag.
        find_element_send_keys(self, VulnPageLocators.TAG_INPUT_SEARCH_FIELD, tag_name)
        find_element_click(self, VulnPageLocators.TAG_INPUT_RESULT)
        find_element_click(self, VulnPageLocators.TAG_SAVE)

        # return back to Vulnerabilities page and filter by your new tag.
        find_element_click(self, DashboardLocators.VULNERABILITIES_TAB)
        find_element_click(self, VulnPageLocators.VULNERABILITY_FILTER_ICON)
        # this test will fail on the line 51 b/c there is a bug described in the BR-005.
        driver.find_element(By.XPATH, f"//*[@data-e2e='filter-option-{tag_name}']").click()
        find_element_click(self, VulnPageLocators.VULNERABILITY_FILTER_ICON)
        sleep(2)
        # navigate to the filtered vulnerability and assert tag name correct.
        li = driver.find_elements(*VulnPageLocators.VULN_NAME_LINK)
        li[0].click()
        wait_and_assert_text_equal(self, VulnPageLocators.VULNERABILITY_TAG, tag_name)