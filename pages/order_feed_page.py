import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from selenium.webdriver.common.by import By


class OrderFeedPage(BasePage):
    @allure.step('click on order')
    def click_on_order(self):
        return self.find_element_located_click(OrderFeedPageLocators.ORDER)

    @allure.step('find popup order information')
    def find_popup_order_information(self):
        return self.find_element_located(OrderFeedPageLocators.ORDER_INFORMATION_POPUP_OPEN)

    @allure.step('get text of order number')
    def get_text_of_order_number(self):
        return self.get_text_of_element(OrderFeedPageLocators.ORDER_NUMBER_CREATE)

    @allure.step('click on cross popup button')
    def click_on_cross_popup_button(self):
        return self.find_element_located_click(OrderFeedPageLocators.CROSS_BUTTON)

    @allure.step('get order number')
    def get_number(self):
        order_number = self.get_text_of_order_number()
        return self.find_element_located((By.XPATH, f'//p[text()= "#{order_number}"'))

    @allure.step('get order number  create all time')
    def get_order_number_create_all_time(self):
        return int(self.get_text_of_element(OrderFeedPageLocators.COUNT_ORDER_ALL_TIME))

    @allure.step('get order number create today')
    def get_order_number_create_today(self):
        return int(self.get_text_of_element(OrderFeedPageLocators.COUNT_ORDER_TODAY))

    @allure.step('get order number in progress')
    def get_order_number_in_progress(self):
        return self.get_text_of_element(OrderFeedPageLocators.ORDER_IN_PROGRESS)






