import allure
from pages.password_recovery_page import PasswordRecoveryPage
from const import Urls, Constants


class TestPasswordRecoveryPage:
    @allure.title('go to the password recovery page by clicking the “Recover Password” button')
    def test_go_to_password_recovery_page_by_click_recover_password_button(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.go_to_burger_site(Urls.URL_LOGIN)
        password_recovery_page.click_on_recovery_password_button()
        assert password_recovery_page.check_new_url(Urls.URL_FORGOT_PASSWORD)

    @allure.title('fill email field and click on “Recover" button')
    def test_go_to_reset_password_page(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.go_to_burger_site(Urls.URL_FORGOT_PASSWORD)
        password_recovery_page.click_on_email_field()
        password_recovery_page.fill_email_field(email=Constants.EMAIL_FOR_RECOVERY)
        password_recovery_page.click_on_recovery_button()
        assert password_recovery_page.check_new_url(Urls.URL_RESET_PASSWORD)

    @allure.title('click_on_show button')
    def test_click_on_show_button(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.go_to_burger_site(Urls.URL_FORGOT_PASSWORD)
        password_recovery_page.click_on_email_field()
        password_recovery_page.fill_email_field(email=Constants.EMAIL_FOR_RECOVERY)
        password_recovery_page.click_on_recovery_button()
        password_recovery_page.click_on_show_button()
        assert password_recovery_page.find_activ_field()
