from selenium.webdriver.common.by import By


class LoginPage:
    LOGIN_INPUT = (By.XPATH, '//input[@data-test="username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@data-test="password"]')
    LOGIN_BTN = (By.XPATH, '//input[@data-test="login-button"]')

    LOGIN_ERROR = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
