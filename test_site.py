import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from Fake_user import FakeUserGenerator


BASE_URL = "https://www.saucedemo.com/"

def generate_fake_user():
    # Генерация пользовательских данных
    generated_user = FakeUserGenerator()
    return generated_user

@pytest.fixture()
def successful_signup():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    # успешная авторизация

    login = "standard_user"
    password = "secret_sauce"

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
        driver = webdriver.Chrome()
        driver.get(BASE_URL)
        # Авторизация используя некорректные данные (user, user)
        username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
        username_field.send_keys("user")

        password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
        password_field.send_keys("user")

        login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
        login_button.click()

        time.sleep(2)
        error_button = driver.find_element(By.XPATH, '//button[@class="error-button"]')
        assert error_button.is_displayed()
        driver.quit()


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

    def test_del_from_basket(self, successful_signup):
        # Удаление товара из корзины через корзину
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
        # Успешный переход к карточке товара после клика на картинку товара
        driver = successful_signup

        expected_id = '4'  # id нужного нам товара
        card_product = driver.find_element(By.XPATH, f'//*[@id="item_{expected_id}_img_link"]')
        card_product.click()

        time.sleep(1)

        assert driver.current_url == f'https://www.saucedemo.com/inventory-item.html?id={expected_id}'


    def test_move_from_title(self, successful_signup):
        # Успешный переход к карточке товара после клика на название товара
        driver = successful_signup

        expected_id = '4'  # id нужного нам товара
        card_product = driver.find_element(By.XPATH, f'//*[@id="item_{expected_id}_title_link"]')
        card_product.click()

        time.sleep(1)

        assert driver.current_url == f'https://www.saucedemo.com/inventory-item.html?id={expected_id}'

class TestOrder:
    def test_do_ordering(self, successful_signup):
        # Оформление заказа используя корректные данные
        driver = successful_signup
        generated_user = generate_fake_user()

        add_basket_button = driver.find_element(By.XPATH, '//button[starts-with(@id, "add-to-cart-sauce-labs-")]')
        add_basket_button.click()

        basket_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        basket_button.click()

        checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        checkout_button.click()

        first_name_field = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        first_name_field.send_keys(generated_user.first_name)

        last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        last_name_field.send_keys(generated_user.last_name)

        postcode_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        postcode_field.send_keys(generated_user.postcode)

        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()

        finish_button = driver.find_element(By.XPATH, '//*[@id="finish"]')
        finish_button.click()

        back_home_button = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')

        assert back_home_button.is_displayed()
