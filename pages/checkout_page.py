from selenium.webdriver.common.by import By


class CheckoutPage:
    FIRST_NAME_FIELD = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME_FIELD = (By.XPATH, '//*[@id="last-name"]')
    POSTCODE_FIELD = (By.XPATH, '//*[@id="postal-code"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="continue"]')
    CARD_TITLE = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    CANCEL_BUTTON = (By.XPATH, '//*[@id="cancel"]')
    FINISH_BUTTON = (By.XPATH, '//*[@id="finish"]')
    BACK_HOME_BUTTON = (By.XPATH, '//*[@id="back-to-products"]')
    COMPLETE_ORDER_TITLE = (By.XPATH, '//*[@id="checkout_complete_container"]/h2')
