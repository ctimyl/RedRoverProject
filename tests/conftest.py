import time

import pytest
from selenium import webdriver
from steps.login_steps import LoginSteps

@pytest.fixture()
def successful_signup():
    driver = webdriver.Chrome()

    login = "standard_user"
    password = "secret_sauce"

    login_steps = LoginSteps()
    login_steps.input_login_password("standard_user","secret_sauce")
    login_steps.click_login()

    yield driver

    time.sleep(1)
    driver.quit()