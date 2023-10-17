from pages.checkout_page import CheckoutPage
from BasePage import BasePage

class CheckoutSteps(BasePage):

    def catalog_element_should_be_displayed(self):
        assert (self.find_element(CheckoutPage.FIRST_NAME_FIELD).is_displayed(), "FIRST_NAME_FIELD не отображается")
        assert (self.find_element(CheckoutPage.LAST_NAME_FIELD).is_displayed(), "LAST_NAME_FIELD не отображается")
        assert (self.find_element(CheckoutPage.POSTCODE_FIELD).is_displayed(), "POSTCODE_FIELD не отображается")
        assert (self.find_element(CheckoutPage.CONTINUE_BUTTON).is_displayed(), "CONTINUE_BUTTON не отображается")
        assert (self.find_element(CheckoutPage.CANCEL_BUTTON).is_displayed(), "CANCEL_BUTTON не отображается")
        return self

    def input_name(self, first_name, last_name, postcode):
        self.find_element(CheckoutPage.FIRST_NAME_FIELD).send_keys(first_name)
        self.find_element(CheckoutPage.LAST_NAME_FIELD).send_keys(last_name)
        self.find_element(CheckoutPage.POSTCODE_FIELD).send_keys(postcode)

    def click_continue(self):
        self.find_element(CheckoutPage.CONTINUE_BUTTON).click()

    def click_finish(self):
        self.find_element(CheckoutPage.FINISH_BUTTON).click()

    def back_home_btn_should_be_displayed(self):
        assert self.find_element(CheckoutPage.BACK_HOME_BUTTON).is_displayed(), "BACK_HOME_BUTTON не отображается"

    def checkout_title_should_be_displayed(self):
        self.find_element(CheckoutPage.COMPLETE_ORDER_TITLE).is_displayed(), "COMPLETE_ORDER_TITLE не отображается"
        return self.find_element(CheckoutPage.COMPLETE_ORDER_TITLE).text

    def card_title_should_be_displayed(self):
        self.find_element(CheckoutPage.CARD_TITLE).is_displayed(), "CARD_TITLE не отображается"
        return self.find_element(CheckoutPage.CARD_TITLE).text