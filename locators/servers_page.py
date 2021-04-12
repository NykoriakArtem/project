from selenium.webdriver.common.by import By


class ServersPageLocators:
    SERVERS_PAGE = (By.XPATH, "//*[@class='css-15lnkij']")
    ASSESS_PROTECT_TOGGLES_SERVERS_PAGE = (By.XPATH, "//*[@class='css-wpjxul']")
    ASSESS_PROTECT_TOGGLES_SERVERS_OVERVIEW_PAGE = (By.XPATH, "//*[@class='css-14ylbqb']")
    SAMPLE_SERVER = (By.XPATH, "//*[@data-e2e='server-name-cell-Sample Server']")
    SERVER_PANEL = (By.XPATH, "//*[@class='panel panel-border']")
