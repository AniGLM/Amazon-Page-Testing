from Pages.Common.BaseClass import BaseClass


class CartContentClass(BaseClass):
    def __init__(self, driver):
        super(CartContentClass, self).__init__(driver)

    def delete_cart_1th_item(self):
        deleteButton = self.customFind.find_element(self.locators.navigationBarDeleteContent)
        deleteButton.click()

    def delete_all_products_from_cart(self):
        cartElementCount = self.customFind.find_element(self.locators.navigationBarGetCartItemsCount).text
        cartElementCount = int(cartElementCount)

        while cartElementCount > 0:
            self.delete_cart_1th_item()
            cartElementCount -= 1

    def check_cart_content(self):
        cartItemsCount = self.customFind.find_element(self.locators.navigationBarGetCartItemsCount)
        count = int(cartItemsCount.text)

        if count == 0:
            print("Cart is empty")
        else:
            print("There are some items")
