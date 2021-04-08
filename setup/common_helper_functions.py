import json
from selenium.webdriver.common.keys import Keys
from simple_settings import settings
from selenium.webdriver.common.action_chains import ActionChains
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


def log_in_with_admin_user(self, user):
    driver = self.driver
    wait = self.wait

    driver.get(settings.URL)

    driver.find_element(*USERNAME_FIELD).send_keys(user.email)
    driver.find_element(*NEXT_LOGIN_BUTTON).click()
    wait.until(visibility_of_element_located(PASSWORD_FIELD))
    driver.find_element(*PASSWORD_FIELD).send_keys(user.pw)

    driver.find_element(*NEXT_LOGIN_BUTTON).click()
    wait.until(visibility_of_element_located(DASHBOARD_LOGO))



def find_element_click(self, element):
    self.wait.until(element_to_be_clickable(element))
    self.driver.find_element(*element).click()


def find_element_send_keys(self, element, *args):
    self.wait.until(visibility_of_element_located(element))
    self.driver.find_element(*element).send_keys(args)


def move_to_element_click(self, element):
    self.wait.until(visibility_of_element_located(element))
    ActionChains(self.driver).move_to_element(self.driver.find_element(*element)).perform()
    self.driver.find_element(*element).click()


def assert_correct_api_post_request(self, environment):
    requests = []
    for log in self.driver.get_log("performance"):
        source = json.loads(log["message"])
        try:
            if (
                "Network.responseReceived" in source["message"]["method"]
                or "Network.requestWillBeSent" in source["message"]["method"]
            ):
                if source["message"]["params"]["request"]["hasPostData"]:
                    requests.append(source)
                    continue
        except KeyError:
            continue

    for request in requests:
        self.assertIn(environment, request["message"]["params"]["request"]["url"])

    return requests
