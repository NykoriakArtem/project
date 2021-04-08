import browsermobproxy
import os
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class DriverManager(unittest.TestCase):
    bmp_url = "localhost"
    client = browsermobproxy.Client(f"{bmp_url}:9090")

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        desired_caps = chrome_options.to_capabilities()
        desired_caps["goog:loggingPrefs"] = {"performance": "ALL"}
        desired_caps["browserName"] = "chrome"

        self.driver = webdriver.Remote(
            command_executor=os.getenv("WD_URL"), desired_capabilities=desired_caps
        )

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
