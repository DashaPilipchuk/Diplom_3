import allure
from pages.personal_account_page import PersonalAccountPage
from const import Urls, Constants


class TestPersonalAccountPage:
    @allure.title('go to personal account page')
    def test_click_on_personal_account_button(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.go_to_burger_site(Urls.URL_MAIN)
        personal_account_page.click_on_personal_account_button()
        assert personal_account_page.check_new_url(Urls.URL_LOGIN)

    @allure.title('go to order history')
    def test_click_on_order_history_button(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.go_to_burger_site(Urls.URL_LOGIN)
        personal_account_page.click_on_email_field()
        personal_account_page.fill_email_field(Constants.TEST_EMAIL)
        personal_account_page.click_on_password_field()
        personal_account_page.fill_password_field(Constants.TEST_PASSWORD)
        personal_account_page.click_on_login_button()
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_order_history_button()
        assert personal_account_page.check_new_url(Urls.URL_ORDER_HISTORY)

    @allure.title('logout')
    def test_logout(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.go_to_burger_site(Urls.URL_LOGIN)
        personal_account_page.click_on_email_field()
        personal_account_page.fill_email_field(Constants.TEST_EMAIL)
        personal_account_page.click_on_password_field()
        personal_account_page.fill_password_field(Constants.TEST_PASSWORD)
        personal_account_page.click_on_login_button()
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_logout_button()
        assert personal_account_page.check_new_url(Urls.URL_LOGIN)



