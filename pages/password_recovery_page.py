import allure
from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPgeLocators


class PasswordRecoveryPage(BasePage):
    @allure.step('click on recovery password button')
    def click_on_recovery_password_button(self):
        return self.find_element_located_click(PasswordRecoveryPgeLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.step('click on email field')
    def click_on_email_field(self):
        return self.find_element_located_click(PasswordRecoveryPgeLocators.EMAIL_FIELD)

    @allure.step('fill email field')
    def fill_email_field(self, email):
        return self.find_element_located_send_keys(PasswordRecoveryPgeLocators.EMAIL_FIELD, email)

    @allure.step('click on recovery button')
    def click_on_recovery_button(self):
        return self.find_element_located_click(PasswordRecoveryPgeLocators.RECOVERY_BUTTON)

    @allure.step('click on show button')
    def click_on_show_button(self):
        return self.find_element_located_click(PasswordRecoveryPgeLocators.SHOW_BUTTON)

    @allure.step('find activ field')
    def find_activ_field(self):
        return self.find_element_located(PasswordRecoveryPgeLocators.ACTIV_FIELD)
