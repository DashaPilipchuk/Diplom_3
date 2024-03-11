import allure
from pages.base_page import BasePage
from locators.main_functional_page_locators import MainFunctionalPageLocators


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

    @allure.step('find popup ingredient details')
    def find_popup_ingredient_details(self):
        return self.find_element_located(MainFunctionalPageLocators.INGREDIENT_DETAILS_POPUP_OPEN)

    @allure.step('get attribute popup')
    def get_attribute_on_main_page(self, element):
        return self.get_attribute(MainFunctionalPageLocators.INGREDIENT_DETAILS_POPUP_CLOSE, element)

    @allure.step('get text of number')
    def get_text_of_number_ingredient(self):
        return self.get_text_of_element(MainFunctionalPageLocators.COUNTER)

    @allure.step('find popup create order')
    def find_popup_create_order(self):
        return self.find_element_located(MainFunctionalPageLocators.CREATE_ORDER_POPUP)
