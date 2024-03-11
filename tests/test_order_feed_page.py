import allure
import pytest
from pages.main_functional_page import MainFunctionalPage
from pages.order_feed_page import OrderFeedPage
from const import Urls, Constants
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeedPage:
    @allure.title('click on order')
    def test_click_on_order(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_burger_site(Urls.URL_FEED)
        order_feed.click_on_order()
        assert order_feed.find_popup_order_information()

    @pytest.mark.xfail(reason='тест падает из за бага с номером заказа при создании')
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
        order_feed.click_on_cross_popup_button()
        main_functional.click_on_order_feed_button()
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_order_history_button()
        assert order_feed.get_number()

    @pytest.mark.xfail(reason='тест падает из за бага с номером заказа при создании')
    @allure.title('check counter Completed for all time')
    def test_check_counter_completed_for_all_time(self, driver):
        order_feed = OrderFeedPage(driver)
        main_functional = MainFunctionalPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed.go_to_burger_site(Urls.URL_FEED)
        order_number_before_create = order_feed.get_order_number_create_all_time()
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_email_field()
        personal_account_page.fill_email_field(Constants.TEST_EMAIL)
        personal_account_page.click_on_password_field()
        personal_account_page.fill_password_field(Constants.TEST_PASSWORD)
        personal_account_page.click_on_login_button()
        main_functional.add_ingredient_to_order()
        main_functional.click_on_create_order_button()
        order_feed.click_on_cross_popup_button()
        main_functional.click_on_order_feed_button()
        order_number_after_create = order_feed.get_order_number_create_all_time()
        assert order_number_before_create - order_number_after_create == 1

    @pytest.mark.xfail(reason='тест падает из за бага с номером заказа при создании')
    @allure.title('check counter Completed today')
    def test_check_counter_completed_today(self, driver):
        order_feed = OrderFeedPage(driver)
        main_functional = MainFunctionalPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed.go_to_burger_site(Urls.URL_FEED)
        order_number_before_create = order_feed.get_order_number_create_today()
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_email_field()
        personal_account_page.fill_email_field(Constants.TEST_EMAIL)
        personal_account_page.click_on_password_field()
        personal_account_page.fill_password_field(Constants.TEST_PASSWORD)
        personal_account_page.click_on_login_button()
        main_functional.add_ingredient_to_order()
        main_functional.click_on_create_order_button()
        order_feed.click_on_cross_popup_button()
        main_functional.click_on_order_feed_button()
        order_number_after_create = order_feed.get_order_number_create_today()
        assert order_number_before_create - order_number_after_create == 1

    @pytest.mark.xfail(reason='тест падает из за бага с номером заказа при создании')
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
        order_number = order_feed.get_text_of_order_number()
        order_feed.click_on_cross_popup_button()
        main_functional.click_on_order_feed_button()
        order_number_in_progress = order_feed.get_order_number_in_progress()
        assert order_number == order_number_in_progress
