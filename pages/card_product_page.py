from selenium.webdriver.common.by import By

class CardProductPage():
    ADD_BUTTON = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    REMOVE_BUTTON = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    BASKET_BADGE = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    CARD_PROSUCT_TITLE = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    BACK_BUTTON = (By.XPATH, '//*[@id="back-to-products"]')