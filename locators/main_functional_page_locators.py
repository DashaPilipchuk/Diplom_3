from selenium.webdriver.common.by import By


class MainFunctionalPageLocators:
    INGREDIENT = (By.XPATH, '//p[text()="Соус Spicy-X"]')
    ORDER_ZONE = (By.XPATH, '//span[text()="Перетяните булочку сюда (верх)"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')
    CROSS_BUTTON = (By.XPATH,
                    "(//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'])[1]")
    COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']/div/p[@class='counter_counter__num__3nue1']")
    INGREDIENT_DETAILS_POPUP_OPEN = (By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]')
    INGREDIENT_DETAILS_POPUP_CLOSE = (By.XPATH, "(//section[@class='Modal_modal__P3_V5'])[1]")
    CREATE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    CREATE_ORDER_POPUP = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")