import pytest
from selenium import webdriver

#тесты сделаны для прохождения на Chrome
@pytest.fixture(params=['Chrome'])
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    elif request.param == 'Firefox':
        driver = webdriver.Firefox()
    yield driver
    driver.quit()








