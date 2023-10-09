import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

BASE_URL = "https://www.saucedemo.com/"
driver = webdriver.Chrome()

@pytest.fixture()
def successful_signup():
    driver = webdriver.Chrome()
    # успешная авторизация

    login = "standard_user"
    password = "secret_sauce"

    driver.get(BASE_URL)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys(login)

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    yield driver

    time.sleep(1)
    driver.quit()


class TestAuth:
    def test_successful_signup(self, successful_signup):
        driver = successful_signup
        # Авторизация используя корректные данные (standard_user, secret_sauce)
        time.sleep(3)
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    def test_unsuccessful_signup(self):
        # Авторизация используя некорректные данные (user, user)
        driver.get(BASE_URL)
        username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
        username_field.send_keys("user")

        password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
        password_field.send_keys("user")

        login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
        login_button.click()

        time.sleep(2)
        error_button = driver.find_element(By.XPATH, '//button[@class="error-button"]')
        assert error_button.is_displayed()


class TestBasket:
    def test_add_to_basket(self, successful_signup):
        driver = successful_signup
        # Добавление товара в корзину через каталог

        add_basket_button = driver.find_element(By.XPATH, '//button[starts-with(@id, "add-to-cart-sauce-labs-")]')
        add_basket_button.click()

        time.sleep(2)
        remove_button = driver.find_element(By.XPATH, '//button[starts-with(@id, "remove-sauce-labs-")]')
        assert remove_button.is_displayed()

        basket_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        assert basket_badge.text == '1'

    def test_add_from_basket(self, successful_signup):
        driver = successful_signup

        add_basket_button = driver.find_element(By.XPATH, '//button[starts-with(@id, "add-to-cart-sauce-labs-")]')
        add_basket_button.click()

        basket_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        basket_button.click()

        remove_button_in_backet = driver.find_element(By.XPATH, '//button[starts-with(@id, "remove-sauce-labs-")]')
        remove_button_in_backet.click()

        time.sleep(2)
        try:
            remove_button_in_backet = driver.find_element(By.XPATH, '//button[starts-with(@id, "remove-sauce-labs-")]')
            assert not remove_button_in_backet.is_displayed()
        except NoSuchElementException:
            # Если элемент не найден, это означает, что он успешно удален
            pass

    def test_add_from_card_procuct(self, successful_signup):
        driver = successful_signup
        # Добавление товара в корзину из карточки товара

        expected_id = '4' # id нужного нам товара

        card_product = driver.find_element(By.XPATH, f'//*[@id="item_{expected_id}_title_link"]')
        card_product.click()

        time.sleep(1)

        assert driver.current_url == f'https://www.saucedemo.com/inventory-item.html?id={expected_id}'

        add_from_card_procuct = driver.find_element(By.XPATH, '//*[starts-with(@id, "add-to-cart-sauce-labs-")]')
        add_from_card_procuct.click()

        time.sleep(1)
        remove_button = driver.find_element(By.XPATH, '//*[starts-with(@id, "remove-sauce-labs-")]')
        assert remove_button.is_displayed()

        basket_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        assert basket_badge.text == '1'

    def test_delete_from_card_procuct(self, successful_signup):
        driver = successful_signup
        # Удаление товара из корзины через карточку товара
        card_product = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
        card_product.click()

        time.sleep(1)

        add_from_card_procuct = driver.find_element(By.XPATH, '//*[starts-with(@id, "add-to-cart-sauce-labs-")]')
        add_from_card_procuct.click()

        time.sleep(1)
        remove_button = driver.find_element(By.XPATH, '//*[starts-with(@id, "remove-sauce-labs-")]')
        remove_button.click()

        add_from_card_procuct = driver.find_element(By.XPATH, '//*[starts-with(@id, "add-to-cart-sauce-labs-")]')
        assert add_from_card_procuct.is_displayed()

        basket_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        assert basket_badge.text == ""

class TestCardProcuct:
    def test_move_from_img(self, successful_signup):
        driver = successful_signup

        expected_id = '4'  # id нужного нам товара
        card_product = driver.find_element(By.XPATH, f'//*[@id="item_{expected_id}_img_link"]')
        card_product.click()

        time.sleep(1)

        assert driver.current_url == f'https://www.saucedemo.com/inventory-item.html?id={expected_id}'


    def test_move_from_title(self, successful_signup):
        driver = successful_signup

        expected_id = '4'  # id нужного нам товара
        card_product = driver.find_element(By.XPATH, f'//*[@id="item_{expected_id}_title_link"]')
        card_product.click()

        time.sleep(1)

        assert driver.current_url == f'https://www.saucedemo.com/inventory-item.html?id={expected_id}'
