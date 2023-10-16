from pages.catalog_page import CatalogPage
from BasePage import BasePage

class CatalogSteps(BasePage):

    def catalog_page_should_be_displayed(self):
        assert (CatalogPage.CARD_PRODUCT_URL, "CARD_PRODUCT_URL не отображается")