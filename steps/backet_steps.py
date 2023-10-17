from pages.basket_page import BasketPage
from BasePage import BasePage


class BasketSteps(BasePage):
    def checkout_btn_should_be_displayed(self):
        assert (self.find_element(BasketPage.CHECKOUT_BUTTON).is_displayed(), "CHECKOUT_BUTTON не отображается")

    def click_checkout_btn(self):
        self.find_element(BasketPage.CHECKOUT_BUTTON).click()

    def continue_btn_should_be_displayed(self):
        assert (self.find_element(BasketPage.CONTINUE_SHOPPING_BUTTON).is_displayed(),
        "CONTINUE_SHOPPING_BUTTON не отображается")

    def click_continue_btn(self):
        self.find_element(BasketPage.CONTINUE_SHOPPING_BUTTON).click()

    def remove_btn_should_be_displayed(self):
        assert (self.find_element(BasketPage.REMOVE_BUTTON).is_displayed(), "REMOVE_BUTTON не отображается")

    def remove_btn_not_be_displayed(self):
        assert self.is_element_not_displayed(BasketPage.REMOVE_BUTTON)

    def click_remove_btn(self):
        self.find_element(BasketPage.REMOVE_BUTTON).click()

    def basket_badge(self):
        assert (self.find_element(BasketPage.BASKET_BADGE).is_displayed(), "BASKET_BAGE не отображается")
        return self.find_element(BasketPage.BASKET_BADGE).text
