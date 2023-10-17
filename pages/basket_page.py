from selenium.webdriver.common.by import By


class BasketPage:
    REMOVE_BUTTON = (By.ID, 'remove-sauce-labs-backpack')
    BASKET_BADGE = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')
