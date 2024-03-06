import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.personal_account_page_locators import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):
    @allure.step('click on personal account button')
    def click_on_personal_account_button(self):
        return self.find_element_located_click(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('click on email field')
    def click_on_email_field(self):
        return self.find_element_located_click(PersonalAccountPageLocators.EMAIL_FIELD)

    @allure.step('fill email field')
    def fill_email_field(self, email):
        return self.find_element_located_send_keys(PersonalAccountPageLocators.EMAIL_FIELD, email)

    @allure.step('click on password field')
    def click_on_password_field(self):
        return self.find_element_located_click(PersonalAccountPageLocators.PASSWORD_FIELD)

    @allure.step('fill password field')
    def fill_password_field(self, password):
        return self.find_element_located_send_keys(PersonalAccountPageLocators.PASSWORD_FIELD, password)

    @allure.step('click on login button')
    def click_on_login_button(self):
        return self.find_element_located_click(PersonalAccountPageLocators.LOGIN_BUTTON)

    @allure.step('click on order history button')
    def click_on_order_history_button(self):
        return self.find_element_located_click(PersonalAccountPageLocators.HISTORY_ORDER_BUTTON)

    @allure.step('click on logout button')
    def click_on_logout_button(self):
        return self.find_element_located_click(PersonalAccountPageLocators.LOGOUT_BUTTON)

