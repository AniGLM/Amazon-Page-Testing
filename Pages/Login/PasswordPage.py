import time
from Pages.Common.BaseClass import BaseClass


class PasswordClass(BaseClass):

    def __init__(self, driver):
        super(PasswordClass, self).__init__(driver)
        self.defaultPass = self.variables.defaultPassword

    def fill_password_field(self, ):
        passwordField = self.customFind.find_element(self.locators.passwordPagePasswordFieldLocator)
        passwordField.send_keys(self.defaultPass)
        time.sleep(4)

    def click_into_signIn_button(self):
        signInButton = self.customFind.find_element(self.locators.passwordPageSignInButtonLocator)
        signInButton.click()
        time.sleep(4)

    def keep_me_signIn(self):
        rememberMe = self.customFind.find_element(self.locators.keepMeSignedInLocator)
        rememberMe.click()
        time.sleep(2)

    def sign_out_button(self):
        signOutButton = self.customFind.find_element(self.locators.accountAndListSignOutButton)
        self.actions.move_to_element(signOutButton).click().perform()


