from BasePage import BasePage
from pages.card_product_page import CardProductPage

class CardProductSteps(BasePage):
    def card_product_element_should_be_displayed(self):
        assert (self.find_element(CardProductPage.ADD_BUTTON).is_displayed(), "ADD_BUTTON не отображается")
        assert (self.find_element(CardProductPage.CARD_PRODUCT_TITLE).is_displayed(), "CARD_PRODUCT_TITLE не отображается")
        assert (self.find_element(CardProductPage.BASKET_BADGE).is_displayed(), "BASKET_BADGE не отображается")
        assert (self.find_element(CardProductPage.BACK_BUTTON).is_displayed(), "BACK_BUTTON не отображается")
        return self

    def basket_badge(self):
        assert (self.find_element(CardProductPage.BASKET_BADGE).is_displayed(), "BASKET_BAGE не отображается")
        return self.find_element(CardProductPage.BASKET_BADGE).text

    def add_btn_should_be_displayed(self):
        assert (self.find_element(CardProductPage.ADD_BUTTON).is_displayed(), "ADD_BUTTON не отображается")

    def click_add_btn(self):
        self.find_element(CardProductPage.ADD_BUTTON).click()

    def remove_btn_should_be_displayed(self):
        assert (self.find_element(CardProductPage.REMOVE_BUTTON).is_displayed(), "REMOVE_BUTTON не отображается")

    def click_remove_btn(self):
        self.find_element(CardProductPage.REMOVE_BUTTON).click()

    def url_should_be_displayed(self):
        return self.opened_url()
