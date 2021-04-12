from selenium.webdriver.common.by import By


class DashboardLocators:
    APPLICATIONS_TAB = (By.XPATH, "//*[@data-e2e='header-application-link']")
    SERVERS_TAB = (By.XPATH, "//*[@data-e2e='header-server-link']")
    LIBRARIES_TAB = (By.XPATH, "//*[@data-e2e='header-libraries-link']")
    VULNERABILITIES_TAB = (By.XPATH, "//*[@data-e2e='header-vulns-link']")
    ATTACKS_TAB = (By.XPATH, "//*[@data-e2e='header-attacks-link']")