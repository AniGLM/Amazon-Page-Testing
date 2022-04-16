from Pages.Common.BaseClass import BaseClass
import time


class ItemSelectionClass(BaseClass):

    def __init__(self, driver):
        super(ItemSelectionClass, self).__init__(driver)

    def choose_item_field(self):
        chosenItem = self.customFind.find_element(self.locators.itemSelectionChosenItemLocator)
        chosenItem.click()

    def size_chart_field(self):
        sizeChart = self.customFind.find_element(self.locators.itemSelectionSizeChartLocator)
        sizeChart.click()
        time.sleep(4)

    def item_size_fit(self):
        sizeFit = self.customFind.find_element(self.locators.itemSelectionSizeFitLocator)
        sizeFit.click()
        time.sleep(4)
