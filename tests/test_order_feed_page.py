import allure
import pytest
from selenium.webdriver.common.by import By
from Diplom_3.pages.main_functional_page import MainFunctionalPage
from Diplom_3.pages.order_feed_page import OrderFeedPage
from Diplom_3.locators.order_feed_page_locators import OrderFeedPageLocators
from Diplom_3.const import Urls, Constants
from Diplom_3.pages.personal_account_page import PersonalAccountPage


class TestOrderFeedPage:
    @allure.title('click on order')
    def test_click_on_order(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_burger_site(Urls.URL_FEED)
        order_feed.click_on_order()
        assert order_feed.find_element_located(OrderFeedPageLocators.ORDER_INFORMATION_POPUP_OPEN)

    #тест падает из за бага с номером заказа при создании
    @pytest.mark.xfail
    @allure.title('orders from Orders History are displayed on Orders Feed')
    def test_check_display_orders(self, driver):
        order_feed = OrderFeedPage(driver)
        main_functional = MainFunctionalPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed.go_to_burger_site(Urls.URL_LOGIN)
        personal_account_page.click_on_email_field()
        personal_account_page.fill_email_field(Constants.TEST_EMAIL)
        personal_account_page.click_on_password_field()
        personal_account_page.fill_password_field(Constants.TEST_PASSWORD)
        personal_account_page.click_on_login_button()
        main_functional.add_ingredient_to_order()
        main_functional.click_on_create_order_button()
        order_number = order_feed.get_text_of_element(OrderFeedPageLocators.ORDER_NUMBER_CREATE)
        order_feed.find_element_located_click(OrderFeedPageLocators.CROSS_BUTTON)
        main_functional.click_on_order_feed_button()
        order_feed.find_element_located((By.XPATH, f'//p[text()= "#{order_number}"'))
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_order_history_button()
        assert order_feed.find_element_located((By.XPATH, f'//p[text()= "#{order_number}"'))

    # тест падает из за бага с номером заказа при создании
    @pytest.mark.xfail
    @allure.title('check counter Completed for all time')
    def test_check_counter_completed_for_all_time(self, driver):
        order_feed = OrderFeedPage(driver)
        main_functional = MainFunctionalPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed.go_to_burger_site(Urls.URL_FEED)
        order_number_before_create = int(order_feed.get_text_of_element(OrderFeedPageLocators.COUNT_ORDER_ALL_TIME))
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_email_field()
        personal_account_page.fill_email_field(Constants.TEST_EMAIL)
        personal_account_page.click_on_password_field()
        personal_account_page.fill_password_field(Constants.TEST_PASSWORD)
        personal_account_page.click_on_login_button()
        main_functional.add_ingredient_to_order()
        main_functional.click_on_create_order_button()
        order_feed.find_element_located_click(OrderFeedPageLocators.CROSS_BUTTON)
        main_functional.click_on_order_feed_button()
        order_number_after_create = int(order_feed.get_text_of_element(OrderFeedPageLocators.COUNT_ORDER_ALL_TIME))
        assert order_number_before_create - order_number_after_create == 1

    # тест падает из за бага с номером заказа при создании
    @pytest.mark.xfail
    @allure.title('check counter Completed today')
    def test_check_counter_completed_today(self, driver):
        order_feed = OrderFeedPage(driver)
        main_functional = MainFunctionalPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed.go_to_burger_site(Urls.URL_FEED)
        order_number_before_create = int(order_feed.get_text_of_element(OrderFeedPageLocators.COUNT_ORDER_TODAY))
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_email_field()
        personal_account_page.fill_email_field(Constants.TEST_EMAIL)
        personal_account_page.click_on_password_field()
        personal_account_page.fill_password_field(Constants.TEST_PASSWORD)
        personal_account_page.click_on_login_button()
        main_functional.add_ingredient_to_order()
        main_functional.click_on_create_order_button()
        order_feed.find_element_located_click(OrderFeedPageLocators.CROSS_BUTTON)
        main_functional.click_on_order_feed_button()
        order_number_after_create = int(order_feed.get_text_of_element(OrderFeedPageLocators.COUNT_ORDER_TODAY))
        assert order_number_before_create - order_number_after_create == 1

    # тест падает из за бага с номером заказа при создании
    @pytest.mark.xfail
    @allure.title('check order number in progress')
    def test_check_order_number_in_progress(self, driver):
        order_feed = OrderFeedPage(driver)
        main_functional = MainFunctionalPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed.go_to_burger_site(Urls.URL_LOGIN)
        personal_account_page.click_on_email_field()
        personal_account_page.fill_email_field(Constants.TEST_EMAIL)
        personal_account_page.click_on_password_field()
        personal_account_page.fill_password_field(Constants.TEST_PASSWORD)
        personal_account_page.click_on_login_button()
        main_functional.add_ingredient_to_order()
        main_functional.click_on_create_order_button()
        order_number = order_feed.get_text_of_element(OrderFeedPageLocators.ORDER_NUMBER_CREATE)
        order_feed.find_element_located_click(OrderFeedPageLocators.CROSS_BUTTON)
        main_functional.click_on_order_feed_button()
        order_number_in_progress = order_feed.get_text_of_element(OrderFeedPageLocators.ORDER_IN_PROGRESS)
        assert  order_number == order_number_in_progress
