import pytest
from selenium import webdriver
from steps.login_steps import LoginSteps
from BasePage import BasePage


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    base_url = BasePage(driver)
    driver.get(base_url.base_url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login(browser):
    login_steps = LoginSteps(browser)
    login_steps.input_login_password("standard_user", "secret_sauce")
    login_steps.click_login()
