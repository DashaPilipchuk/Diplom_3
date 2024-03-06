import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_functional_page_locators import MainFunctionalPageLocators


class MainFunctionalPage(BasePage):
    @allure.step('click on constructor button')
    def click_on_constructor_button(self):
        return self.find_element_located_click(MainFunctionalPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('click on order feed button')
    def click_on_order_feed_button(self):
        return self.find_element_located_click(MainFunctionalPageLocators.ORDER_FEED_BUTTON)

    @allure.step('click on ingredient')
    def click_on_ingredient(self):
        return self.find_element_located_click(MainFunctionalPageLocators.INGREDIENT)

    @allure.step('click on cross button')
    def click_on_cross_button(self):
        return self.find_element_located_click(MainFunctionalPageLocators.CROSS_BUTTON)

    @allure.step('add ingredient to order')
    def add_ingredient_to_order(self):
        return self.drag_and_drop(MainFunctionalPageLocators.INGREDIENT, MainFunctionalPageLocators.ORDER_ZONE)

    @allure.step('click on create order button')
    def click_on_create_order_button(self):
        return self.find_element_located_click(MainFunctionalPageLocators.CREATE_ORDER_BUTTON)