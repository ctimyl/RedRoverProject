from steps.catalog_steps import CatalogSteps
import time


class TestCatalog:

    def test_catalog_element_should_be_displayed(self, browser, login):
        # отображение элементов каталога

        catalog_steps = CatalogSteps(browser)
        catalog_steps.catalog_element_should_be_displayed()

    def test_add_to_basket(self, browser, login):
        # Добавление товара в корзину через каталог

        catalog_steps = CatalogSteps(browser)
        catalog_steps.click_add_btn()
        time.sleep(1)
        catalog_steps.remove_btn_should_be_displayed()
        assert catalog_steps.basket_badge() == '1'

    def remove_from_basket(self, browser, login):
        # Добавление товара в корзину через каталог

        catalog_steps = CatalogSteps(browser)
        catalog_steps.click_add_btn()
        time.sleep(1)
        catalog_steps.remove_btn_should_be_displayed()
        assert catalog_steps.basket_badge() == '1'
        catalog_steps.click_remove_btn()
        assert catalog_steps.basket_badge() == '0'

    def test_move_from_img(self, browser, login):
        # Успешный переход к карточке товара после клика на картинку товара

        catalog_steps = CatalogSteps(browser)
        catalog_steps.click_card_product_img()
        time.sleep(1)
        assert catalog_steps.url_should_be_displayed() == f'https://www.saucedemo.com/inventory-item.html?id=4'

    def test_move_from_title(self, browser, login):
        # Успешный переход к карточке товара после клика на название товара

        catalog_steps = CatalogSteps(browser)
        catalog_steps.click_card_product_title()
        time.sleep(1)
        assert catalog_steps.url_should_be_displayed() == f'https://www.saucedemo.com/inventory-item.html?id=4'
