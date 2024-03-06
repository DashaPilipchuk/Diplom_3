from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('open page in browser')
    def go_to_burger_site(self, url):
        return self.driver.get(url)

    @allure.step('find element by locator')
    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message=f'Element not found in {locator}')

    @allure.step('click on element')
    def find_element_located_click(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator),
                                                      message=f'Element not found in {locator}').click()

    @allure.step('fill field')
    def find_element_located_send_keys(self, locator, field_name, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}').send_keys(field_name)

    @allure.step('get text of element')
    def get_text_of_element(self, element):
        return self.find_element_located(element).text

    @allure.step('Check new url')
    def check_new_url(self, new_url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(new_url))

    @allure.step('drag and drop')
    def drag_and_drop(self, locator_1, locator_2):
        drag = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator_1))
        drop = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator_2))
        return ActionChains(self.driver).drag_and_drop(drag, drop).release().perform()

    @allure.step('get value of element')
    def get_attribute(self, locator, element):
        return self.find_element_located(locator).get_attribute(element)