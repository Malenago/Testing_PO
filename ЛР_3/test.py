import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    password.send_keys(Keys.RETURN)

    time.sleep(2)
    assert "Swag Labs" in driver.title


def test_unsuccessful_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")

    username.send_keys("invalid_user")
    password.send_keys("wrong_password")
    password.send_keys(Keys.RETURN)

    time.sleep(2)
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert "Username and password do not match" in error_message.text


def test_add_to_cart(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/inventory.html")

    add_to_cart_button = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()

    cart_icon = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart_icon.click()

    time.sleep(2)

    assert "Sauce Labs Backpack" in driver.page_source


def test_complete_purchase(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/checkout-step-one.html")

    first_name = driver.find_element(By.ID, "first-name")
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")

    first_name.send_keys("Test")
    last_name.send_keys("User")
    postal_code.send_keys("12345")

    continue_button = driver.find_element(By.CSS_SELECTOR, "input.btn_primary.cart_button")
    continue_button.click()

    time.sleep(2)

    finish_button = driver.find_element(By.CSS_SELECTOR, "button.btn_action.cart_button")
    finish_button.click()

    time.sleep(2)

    assert "Thank you for your order!" in driver.page_source


