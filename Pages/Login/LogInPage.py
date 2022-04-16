from Pages.Common.BaseClass import BaseClass
import time

class LogInClass(BaseClass):

    def __init__(self, driver):
        super(LogInClass, self).__init__(driver)
        self.defaultLogIn = self.variables.defaultLogin

    def fill_login_field(self, ):
        logInField = self.customFind.find_element(self.locators.loginPageLoginFieldLocator)
        logInField.send_keys(self.defaultLogIn)
        time.sleep(5)

    def press_continue_button(self):
        continueButton = self.customFind.find_element(self.locators.loginPageContinuePageLocator)
        continueButton.click()
