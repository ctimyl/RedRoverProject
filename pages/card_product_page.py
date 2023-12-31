from selenium.webdriver.common.by import By


class CardProductPage():
    ADD_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    REMOVE_BUTTON = (By.ID, 'remove-sauce-labs-backpack')
    BASKET_BADGE = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    CARD_PRODUCT_TITLE = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    BACK_BUTTON = (By.ID, 'back-to-products')
