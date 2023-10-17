from steps.backet_steps import BasketSteps
from steps.catalog_steps import CatalogSteps
import time

class TestBacket():
    def test_del_from_basket(self, browser, login):
        # Удаление товара из корзины через корзину
        catalog_steps = CatalogSteps(browser)
        catalog_steps.click_add_btn()
        catalog_steps.click_basket_badge()
        basket_steps = BasketSteps(browser)
        basket_steps.click_remove_btn()

        basket_steps.remove_btn_not_be_displayed() # неверно, надо определиться как правильно

