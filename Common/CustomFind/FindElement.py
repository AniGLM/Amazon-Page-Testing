from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class CustomFindElement():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element
        except NoSuchElementException:
            print("The locator didn't find")

    def find_elements(self, locator):
        try:
            elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
            return elements
        except NoSuchElementException:
            print("The locator didn't find")
