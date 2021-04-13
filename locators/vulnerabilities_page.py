from selenium.webdriver.common.by import By


class VulnPageLocators:
    VULNERABILITIES_PAGE = (By.XPATH, "//*[@class='css-15lnkij']")
    VULN_NAME_LINK = (By.XPATH, "//*[@class='css-6lko4w']")
    TAG_ICON = (By.XPATH, "//*[@alt='Tag Vulnerability']")
    TAG_INPUT_SEARCH_FIELD = \
        (By.XPATH, "//*[@class='ui-select-search input-xs ng-pristine ng-untouched ng-valid']")
    TAG_INPUT_RESULT = \
        (By.XPATH, "//*[@class='ui-select-choices ui-select-choices-content ui-select-dropdown dropdown-menu']")
    TAG_SAVE = (By.XPATH, "//*[@class='btn btn-info ng-scope']")
    TAG_CANCEL = (By.XPATH, "//*[@class='btn btn-default ng-scope']")
    VULNERABILITY_TAG = (By.XPATH, "//*[@data-testid='tag-test-id']")
    TAG_REMOVE_ICON = (By.XPATH, "//*[@class='close ui-select-match-close']")
    VULNERABILITY_FILTER_ICON = (By.XPATH, "//*[@data-e2e='column-header-title_vulnerability']")
