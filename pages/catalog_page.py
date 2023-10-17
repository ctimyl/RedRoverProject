from selenium.webdriver.common.by import By


class CatalogPage:
    ADD_BUTTON = (By.XPATH, f'//*[@id="add-to-cart-sauce-labs-backpack"]')
    REMOVE_BUTTON = (By.XPATH, f'//*[@id="remove-sauce-labs-backpack"]')
    BASKET_BAGE = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    CARD_PRODUCT_IMG_LINK = (By.XPATH, '//*[@id="item_4_img_link"]')
    CARD_PRODUCT_TITLE_LINK = (By.XPATH, '//*[@id="item_4_title_link"]')
    FILTER_BUTTON = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    PAGE_TITLE = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    BURGER_MENU = (By.XPATH, '//*[@id="react-burger-menu-btn"]')

    CARD_PRODUCT_URL = 'https://www.saucedemo.com/inventory-item.html?id=4'