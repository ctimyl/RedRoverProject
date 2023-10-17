from pages.login_page import LoginPage
from BasePage import BasePage


class LoginSteps(BasePage):

    def login_form_should_be_displayed(self):
        assert (self.find_element(LoginPage.LOGIN_INPUT).is_displayed(), "USERNAME не отображается")
        assert (self.find_element(LoginPage.PASSWORD_INPUT).is_displayed(), "PASSWORD не отображается")
        assert (self.find_element(LoginPage.LOGIN_BTN).is_displayed(), "LOGIN не отображается")
        return self

    def input_login_password(self, login, password):
        self.find_element(LoginPage.LOGIN_INPUT).send_keys(login)
        self.find_element(LoginPage.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.find_element(LoginPage.LOGIN_BTN).click()

    def get_login_error(self):
        assert (self.find_element(LoginPage.LOGIN_ERROR).is_displayed(), "LOGIN_ERROR не отображается")
        return self.find_element(LoginPage.LOGIN_ERROR).text
