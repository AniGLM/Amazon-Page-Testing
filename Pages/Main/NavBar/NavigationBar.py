from Pages.Common.BaseClass import BaseClass
import time
class NavigationBarClass(BaseClass):

    def __init__(self, driver):
        super(NavigationBarClass, self).__init__(driver)
        self.defaultItem = self.variables.defaultSearchItem

    def fill_search_field(self, ):
        searchField = self.customFind.find_element(self.locators.navigationBarSearchButtonLocator)
        searchField.send_keys(self.defaultItem)
        time.sleep(4)

    def press_into_search_button(self):
        enterButton = self.customFind.find_element(self.locators.navigationBarEnterButtonLocator)
        enterButton.click()

    def add_to_cart_button(self):
        addCart = self.customFind.find_element(self.locators.navigationBarAddCartLocator)
        addCart.click()

    def open_cart(self):
        checkingCart = self.customFind.find_element(self.locators.navigationBarCheckingCartLocator)
        checkingCart.click()

    def account_and_lists(self):
        accountAndListsButton = self.customFind.find_element(self.locators.navigationBarAccountAndLists)
        self.actions.move_to_element(accountAndListsButton).perform()
        time.sleep(5)
