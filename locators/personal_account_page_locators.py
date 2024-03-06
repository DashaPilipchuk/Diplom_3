from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    HISTORY_ORDER_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    EMAIL_FIELD = (By.XPATH, '//input[@type ="text"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@type ="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')