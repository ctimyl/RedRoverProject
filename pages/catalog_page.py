from selenium.webdriver.common.by import By

class CatalogPage:
    ADD_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    REMOVE_BUTTON = (By.ID, 'remove-sauce-labs-backpack')
    BASKET_BADGE = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    CARD_PRODUCT_IMG = (By.ID, 'item_4_img_link')
    CARD_PRODUCT_TITLE = (By.ID, 'item_4_title_link')
    FILTER_BUTTON = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    PAGE_TITLE = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    BURGER_MENU = (By.ID, 'react-burger-menu-btn')

    CARD_PRODUCT_URL = 'https://www.saucedemo.com/inventory.html'


