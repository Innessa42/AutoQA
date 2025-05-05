import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from HA_6.page import LoginPage, InventoryPage


class TestInventory:

    @pytest.fixture(scope="class")
    def driver(self):
        options = Options()
        options.add_argument("--disable-features=PasswordCheck")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        driver = webdriver.Chrome(options=options)

        driver.get("https://www.saucedemo.com/")
        authorization_data = {
            "user-name": "standard_user",
            "password": "secret_sauce"
        }
        LoginPage(driver).login(credentials=authorization_data, button_id="login-button")
        yield driver
        driver.quit()

    @pytest.fixture(scope="class")
    def inventory_page(self, driver):
        return InventoryPage(driver)

    def test_add_product(self, inventory_page):
        product_ids = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for product_id in product_ids:
            assert inventory_page.add_product(locator_value=product_id, by=By.ID)

    def test_click_shopping_cart(self, inventory_page):
        result_url = inventory_page.open_page_via_element(locator_value="shopping_cart_link", by=By.CLASS_NAME)
        assert result_url == "https://www.saucedemo.com/cart.html"

    def test_click_checkout(self, inventory_page):
        result_url = inventory_page.open_page_via_element(locator_value="checkout", by=By.ID)
        assert result_url == "https://www.saucedemo.com/checkout-step-one.html"

    def test_enter_information(self, inventory_page):
        info = {
            "first-name": "Inna",
            "last-name": "Graur",
            "postal-code": "54321"
        }
        result_url = inventory_page.submit_product_form(fields=info, button_id="continue")
        assert result_url == "https://www.saucedemo.com/checkout-step-two.html"

    def test_check_total(self, inventory_page):
        total_text = inventory_page.check_total(locator_value="summary_total_label", by=By.CLASS_NAME).text
        assert "58.29" in total_text

















#import pytest
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
#from webdriver_manager.chrome import ChromeDriverManager
#import time
#
#
## Page Object Model
#class LoginPage:
#    def __init__(self, driver):
#        self.driver = driver
#        self.username_input = (By.ID, "user-name")
#        self.password_input = (By.ID, "password")
#        self.login_button = (By.ID, "login-button")
#
#    def login(self, username, password):
#        self.driver.find_element(*self.username_input).send_keys(username)
#        self.driver.find_element(*self.password_input).send_keys(password)
#        self.driver.find_element(*self.login_button).click()
#
#
#class InventoryPage:
#    def __init__(self, driver):
#        self.driver = driver
#
#    def add_to_cart(self, product_name):
#        product_button = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
#        self.driver.find_element(*product_button).click()
#
#    def go_to_cart(self):
#        cart_button = (By.CLASS_NAME, "shopping_cart_link")
#        self.driver.find_element(*cart_button).click()
#
#
#class CartPage:
#    def __init__(self, driver):
#        self.driver = driver
#
#    def proceed_to_checkout(self):
#        checkout_button = (By.ID, "checkout")
#        self.driver.find_element(*checkout_button).click()
#
#
#class CheckoutPage:
#    def __init__(self, driver):
#        self.driver = driver
#
#    def fill_checkout_info(self, first_name, last_name, postal_code):
#        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
#        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
#        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
#        self.driver.find_element(By.ID, "continue").click()
#
#    def get_total_price(self):
#        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
#        return total_element.text.split("$")[1]
#
#
#@pytest.fixture
#def driver():
#    service = Service(ChromeDriverManager().install())
#    options = webdriver.ChromeOptions()
#    options.add_argument("--headless")  # Запуск без интерфейса браузера
#    driver = webdriver.Chrome(service=service, options=options)
#    driver.implicitly_wait(10)  # Ожидание элементов
#    yield driver
#    driver.quit()
#
#
#def test_swag_labs_checkout(driver):
#    url = "https://www.saucedemo.com/"
#    driver.get(url)
#
#    login_page = LoginPage(driver)
#    login_page.login("standard_user", "secret_sauce")
#
#    inventory_page = InventoryPage(driver)
#    inventory_page.add_to_cart("Sauce Labs Backpack")
#    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
#    inventory_page.add_to_cart("Sauce Labs Onesie")
#    inventory_page.go_to_cart()
#
#    cart_page = CartPage(driver)
#    cart_page.proceed_to_checkout()
#
#    checkout_page = CheckoutPage(driver)
#    checkout_page.fill_checkout_info("John", "Doe", "12345")
#
#    total_price = checkout_page.get_total_price()
#    assert total_price == "58.29", f"Ожидалась сумма $58.29, получено: ${total_price}"
#