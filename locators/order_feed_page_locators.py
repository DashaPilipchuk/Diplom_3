from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER = (By.XPATH, "//div[@class='OrderHistory_dataBox__1mkxK']")
    ORDER_INFORMATION_POPUP_OPEN = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    CROSS_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    ORDER_NUMBER_CREATE = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text "
                                     "text_type_digits-large mb-8']")
    COUNT_ORDER_ALL_TIME = (By.CSS_SELECTOR, '#root > div > main > div > div > div > div.undefined.mb-15 > '
                                             'p.OrderFeed_number__2MbrQ.text.text_type_digits-large')
    COUNT_ORDER_TODAY = (By.CSS_SELECTOR, '#root > div > main > div > div > div > div:nth-child(3) > '
                                          'p.OrderFeed_number__2MbrQ.text.text_type_digits-large')
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li["
                                   "@class='text text_type_digits-default mb-2']")




