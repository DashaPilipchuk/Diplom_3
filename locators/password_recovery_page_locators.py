from selenium.webdriver.common.by import By


class PasswordRecoveryPgeLocators:
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, '//a[text()="Восстановить пароль"]')
    EMAIL_FIELD = (By.XPATH, '//input[@type ="text"]')
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    SHOW_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    ACTIV_FIELD = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
