import selenium
from Locators.Locators import LocatorsClass
from Common.CustomFind.FindElement import CustomFindElement
from Common.Variables.Variables import VariablesClass
from selenium.webdriver import ActionChains


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class BaseClass():

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.locators = LocatorsClass()
        self.customFind = CustomFindElement(self.driver)
        self.variables = VariablesClass()

