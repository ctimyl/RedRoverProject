from steps.card_product_steps import CardProductSteps
from steps.catalog_steps import CatalogSteps
import time


class TestCardProcuct:
    def test_card_product_elements_should_be_displayed(self, browser, login):
        # отображение элементов формы логина
        catalog_steps = CatalogSteps(browser)
        catalog_steps.click_card_product_title()
        card_procuct_steps = CardProductSteps(browser)
        card_procuct_steps.card_product_element_should_be_displayed()

    def test_add_from_card_procuct(self, browser, login):
        # Добавление товара в корзину из карточки товара

        catalog_steps = CatalogSteps(browser)
        catalog_steps.click_card_product_title()
        card_procuct_steps = CardProductSteps(browser)
        time.sleep(1)
        assert (card_procuct_steps.url_should_be_displayed() ==
                f'https://www.saucedemo.com/inventory-item.html?id=4')
        card_procuct_steps.click_add_btn()
        time.sleep(1)
        card_procuct_steps.remove_btn_should_be_displayed()
        assert card_procuct_steps.basket_badge() == '1'

    def test_delete_from_card_procuct(self, browser, login):
        # Удаление товара из корзины через карточку товара

        catalog_steps = CatalogSteps(browser)
        catalog_steps.click_card_product_title()
        card_procuct_steps = CardProductSteps(browser)
        time.sleep(1)
        card_procuct_steps.click_add_btn()
        time.sleep(1)
        card_procuct_steps.click_remove_btn()
        card_procuct_steps.add_btn_should_be_displayed()
        assert card_procuct_steps.basket_badge() == ''
