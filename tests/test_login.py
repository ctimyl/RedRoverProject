from steps.login_steps import LoginSteps
from steps.catalog_steps import CatalogSteps
from Fake_user import generate_fake_user

class TestLogin:

    def test_login_form_should_be_displayed(self, browser):
        login_steps = LoginSteps(browser)
        login_steps.login_form_should_be_displayed()

    def test_success_login(self, browser):
        login_steps = LoginSteps(browser)
        login_steps.input_login_password("standard_user", "secret_sauce")
        login_steps.click_login()
        catalog_steps = CatalogSteps(browser)
        catalog_steps.catalog_page_should_be_displayed()

    # def fake(self, browser):
    #     first_name_field = LoginSteps(browser)
    #     first_name_field.click_login()
    #     do_fake_user = generate_fake_user()
    #     name = do_fake_user.first_name
    #