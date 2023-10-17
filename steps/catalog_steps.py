from BasePage import BasePage
from pages.catalog_page import CatalogPage


class CatalogSteps(BasePage):

    def catalog_page_should_be_displayed(self):
        assert (CatalogPage.CARD_PRODUCT_URL, "CARD_PRODUCT_URL не отображается")

    def catalog_element_should_be_displayed(self):
        assert (self.find_element(CatalogPage.ADD_BUTTON).is_displayed(), "ADD_BUTTON не отображается")
        assert (self.find_element(CatalogPage.CARD_PRODUCT_IMG).is_displayed(), "CARD_PRODUCT_IMG не отображается")
        assert (self.find_element(CatalogPage.CARD_PRODUCT_TITLE).is_displayed(), "CARD_PRODUCT_TITLE не отображается")
        assert (self.find_element(CatalogPage.FILTER_BUTTON).is_displayed(), "FILTER_BUTTON не отображается")
        assert (self.find_element(CatalogPage.PAGE_TITLE).is_displayed(), "PAGE_TITLE не отображается")
        assert (self.find_element(CatalogPage.BURGER_MENU).is_displayed(), "BURGER_MENU не отображается")
        assert (self.find_element(CatalogPage.BASKET_BADGE).is_displayed(), "BASKET_BADGE не отображается")
        return self

    def add_btn__should_be_displayed(self):
        assert (self.find_element(CatalogPage.ADD_BUTTON).is_displayed(), "ADD_BUTTON не отображается")

    def click_add_btn(self):
        self.find_element(CatalogPage.ADD_BUTTON).click()

    def remove_btn_should_be_displayed(self):
        assert (self.find_element(CatalogPage.REMOVE_BUTTON).is_displayed(), "REMOVE_BUTTON не отображается")

    def click_remove_btn(self):
        self.find_element(CatalogPage.REMOVE_BUTTON).click()

    def basket_badge(self):
        assert (self.find_element(CatalogPage.BASKET_BADGE).is_displayed(), "BASKET_BAGE не отображается")
        return self.find_element(CatalogPage.BASKET_BADGE).text

    def click_basket_badge(self):
        self.find_element(CatalogPage.BASKET_BADGE).click()

    def click_card_product_title(self):
        self.find_element(CatalogPage.CARD_PRODUCT_TITLE).click()

    def click_card_product_img(self):
        self.find_element(CatalogPage.CARD_PRODUCT_IMG).click()

    def url_should_be_displayed(self):
        return self.opened_url()
