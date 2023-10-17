from selenium.webdriver.common.by import By


class CheckoutPage:
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    POSTCODE_FIELD = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    CARD_TITLE = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    CANCEL_BUTTON = (By.ID, 'cancel')
    FINISH_BUTTON = (By.ID, 'finish')
    BACK_HOME_BUTTON = (By.ID, 'back-to-products')
    COMPLETE_ORDER_TITLE = (By.XPATH, '//*[@id="checkout_complete_container"]/h2')
