from steps.login_steps import LoginSteps
from steps.catalog_steps import CatalogSteps


class TestLogin:

    def test_login_form_should_be_displayed(self, browser):
        # отображение элементов формы логина
        login_steps = LoginSteps(browser)
        login_steps.login_form_should_be_displayed()

    def test_success_login(self, browser, login):
        catalog_steps = CatalogSteps(browser)
        catalog_steps.catalog_page_should_be_displayed()

    def test_unsuccessful_login(self, browser):
        login_steps = LoginSteps(browser)
        login_steps.input_login_password("user", "user")
        login_steps.click_login()
        login_steps.get_login_error()
        assert login_steps.get_login_error() == 'Epic sadface: Username and password do not match any user in this service'
