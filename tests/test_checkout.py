from fake_user import generate_fake_user
from steps.catalog_steps import CatalogSteps
from steps.checkout_steps import CheckoutSteps
from steps.backet_steps import BasketSteps
import time


class TestCheckout:
    def test_do_ordering(self, browser, login):
        # Оформление заказа используя корректные данные
        generated_user = generate_fake_user()
        catalog_steps = CatalogSteps(browser)
        catalog_steps.click_add_btn()
        catalog_steps.click_basket_badge()
        backet_steps = BasketSteps(browser)
        backet_steps.click_checkout_btn()
        checkout_steps = CheckoutSteps(browser)
        checkout_steps.input_name(
            generated_user.first_name,
            generated_user.last_name,
            generated_user.postcode
            )
        time.sleep(1)
        checkout_steps.click_continue()
        checkout_steps.click_finish()
        checkout_steps.back_home_btn_should_be_displayed()
