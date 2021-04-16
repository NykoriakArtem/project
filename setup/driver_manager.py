import os
import unittest

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()


class DriverManager(unittest.TestCase):
    def setUp(self):
        os.environ["SIMPLE_SETTINGS"] = "settings.base"
        chrome_options = webdriver.ChromeOptions()
        desired_caps = chrome_options.to_capabilities()
        desired_caps["browserName"] = "chrome"

        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub", desired_capabilities=desired_caps
        )

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()
