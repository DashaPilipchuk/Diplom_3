import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    @allure.step('click on order')
    def click_on_order(self):
        return self.find_element_located_click(OrderFeedPageLocators.ORDER)
