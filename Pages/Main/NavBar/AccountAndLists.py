from Pages.Common.BaseClass import BaseClass
import time


class AccountAndListsClass(BaseClass):

    def __init__(self, driver):
        super(AccountAndListsClass, self).__init__(driver)

    def recommendation_field(self):
        recommendationsButton = self.customFind.find_element(self.locators.accountAndListsRecommendations)
        self.actions.move_to_element(recommendationsButton).click().perform()
        time.sleep(5)

    def choosing_3th_item(self):
        commonXpathForEachItem = self.customFind.find_elements(self.locators.recommendationsItemsChoosing)
        i = 1
        while i < 100:
            i += 1
            try:
                commonXpathForEachItem[i].click()
                self.recommendation_add_to_cart_button()
            except:
                continue

    def recommendation_add_to_cart_button(self):
        reccAddToCart = self.customFind.find_element(self.locators.recommendationsAddToCartButton)
        reccAddToCart.click()

    def see_all_buying_options(self):
        seeAllBuyingOptions = self.customFind.find_element(self.locators.recommendationItemsSeeAllBuyingOptions)
        seeAllBuyingOptions.click()
