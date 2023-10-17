from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

    def opened_url(self):
        return self.driver.current_url

    # def not_be_shown(self, locator):
    #     driver = self.driver.get(self.base_url)
    #     element = locator
    #     WebDriverWait(self.driver, 1).until_not(EC.visibility_of_element_located(element), "Can't load page")
    #     return driver

    def is_element_not_displayed(self, locator):
        try:
            WebDriverWait(self.driver, 1).until_not(EC.visibility_of_element_located(locator))
            return True
        except:
            return False