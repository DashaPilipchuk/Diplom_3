import time

import allure
from pages.main_functional_page import MainFunctionalPage
from locators.main_functional_page_locators import MainFunctionalPageLocators
from const import Urls, Constants
from pages.personal_account_page import PersonalAccountPage


class TestMainFunctionalPageLocators:
    @allure.title('click on constructor button')
    def test_click_on_constructor_button(self, driver):
        main_functional = MainFunctionalPage(driver)
        main_functional.go_to_burger_site(Urls.URL_LOGIN)
        main_functional.click_on_constructor_button()
        assert main_functional.check_new_url(Urls.URL_MAIN)

    @allure.title('click on order feed button')
    def test_click_on_order_feed_button(self, driver):
        main_functional = MainFunctionalPage(driver)
        main_functional.go_to_burger_site(Urls.URL_MAIN)
        main_functional.click_on_order_feed_button()
        assert main_functional.check_new_url(Urls.URL_FEED)

    @allure.title('click on ingredient')
    def test_click_on_ingredient(self, driver):
        main_functional = MainFunctionalPage(driver)
        main_functional.go_to_burger_site(Urls.URL_MAIN)
        main_functional.click_on_ingredient()
        assert main_functional.find_element_located(MainFunctionalPageLocators.INGREDIENT_DETAILS_POPUP_OPEN)

    @allure.title('click on cross button')
    def test_click_on_cross_button(self, driver):
        main_functional = MainFunctionalPage(driver)
        main_functional.go_to_burger_site(Urls.URL_MAIN)
        main_functional.click_on_ingredient()
        main_functional.click_on_cross_button()
        assert (main_functional.get_attribute(MainFunctionalPageLocators.INGREDIENT_DETAILS_POPUP_CLOSE, 'class')
                == Constants.CLASS_POPUP_CLOSE)

    @allure.title('add ingredient')
    def test_add_ingredient(self, driver):
        main_functional = MainFunctionalPage(driver)
        main_functional.go_to_burger_site(Urls.URL_MAIN)
        main_functional.add_ingredient_to_order()
        assert int(main_functional.get_text_of_element(MainFunctionalPageLocators.COUNTER)) == 1

    @allure.title('create order')
    def test_create_order(self, driver):
        main_functional = MainFunctionalPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.go_to_burger_site(Urls.URL_LOGIN)
        personal_account_page.click_on_email_field()
        personal_account_page.fill_email_field(Constants.TEST_EMAIL)
        personal_account_page.click_on_password_field()
        personal_account_page.fill_password_field(Constants.TEST_PASSWORD)
        personal_account_page.click_on_login_button()
        main_functional.add_ingredient_to_order()
        main_functional.click_on_create_order_button()
        assert main_functional.find_element_located(MainFunctionalPageLocators.CREATE_ORDER_POPUP)

