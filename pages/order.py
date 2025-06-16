from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

WAIT = 4

class Order:
    def __init__(self, driver):
        self.driver = driver
        self.products_link_ID = (By.XPATH, '//a[@href="/products"]')
        self.men_products_ID = (By.XPATH, '//a[@href="#Men" and text()="Men"]')
        self.women_products_ID = (By.XPATH, '//a[@href="#Woman"]')
        self.kids_products_ID = (By.XPATH, '//a[@href="#Kids"]')
        self.men_tshirts_ID = (By.XPATH, '//a[@href="/category_products/3"]')
        self.product_details_ID = (By.CSS_SELECTOR, ".fa.fa-plus-square")
        self.summer_white_top_details_ID = (By.XPATH, '//p[contains(text(), "Summer White Top")]/following::a[contains(text(), "View Product")][1]')
        self.polo_section_ID = (By.XPATH, '//a[@href="/brand_products/Polo"]')
        self.add_to_cart_ID = (By.CSS_SELECTOR, ".btn.btn-default.add-to-cart")
        self.view_cart_ID = (By.XPATH, '//a[@href="/view_cart"]')
        self.continue_shopping_ID = (By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block")
        self.proceed_to_checkout_ID = (By.CSS_SELECTOR, ".btn.btn-default.check_out")
        self.continue_on_cart_ID = (By.CSS_SELECTOR, ".btn.btn-success.close-checkout-modal.btn-block")
        self.register_login_to_checkout_ID = (By.XPATH, '//a[@href="/login"]')
        self.place_order_ID = (By.XPATH, '//a[@href="/payment"]')
        self.card_name_ID = (By.NAME, "name_on_card")
        self.card_number_ID = (By.NAME, "card_number")
        self.cvc_ID = (By.NAME, "cvc")
        self.expiration_m_ID = (By.NAME, "expiry_month")
        self.expiration_y_ID = (By.NAME, "expiry_year")
        self.pay_and_confirm_order_ID = (By.CSS_SELECTOR, ".form-control.btn.btn-primary.submit-button")
        self.continue_button_ID = (By.CSS_SELECTOR, 'a[data-qa="continue-button"]')

    def select_products_link(self):
        element = WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(self.products_link_ID)
        )
        element.click()

    def select_product_category(self, category_name, category):
        #xpath = f'//a[@href="#{category_name}" and text()="{category_name}"]'
        selector = f"a[href='#{category_name}'] span"
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        self.driver.execute_script("arguments[0].click();", element)
        
        number = 0
        if category == "Dress":
            number = "1"
        elif category == "Tops":
            number = "2"
        elif category == "Saree":
            number = "7"
        elif category == "T-shirts":
            number = "3"
        elif category == "Jeans":
            number = "6"
        elif category == "Tops&Shirts":
            number = "5"
        category_field = WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((By.XPATH, f'//a[@href="/category_products/{number}"]'))
        )
        category_field.click()

    def select_product_by_brand(self, brand):
        xpath = f'//a[@href="/brand_products/{brand}"]'
        brand_element = WebDriverWait(self.driver, WAIT).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", brand_element)
        brand_element.click()

    def add_to_cart(self):
        product = WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((By.XPATH, '(//div[@class="product-image-wrapper"])[1]'))
        )

        ActionChains(self.driver).move_to_element(product).perform()

        add_to_cart_button = WebDriverWait(self.driver, WAIT).until(
            EC.element_to_be_clickable((By.XPATH, '(//a[contains(@class, "add-to-cart")])[1]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
        add_to_cart_button.click()

    def continue_shopping(self):
        continue_button = WebDriverWait(self.driver, WAIT).until(
            EC.element_to_be_clickable(self.continue_shopping_ID)
        )
        continue_button.click()

    def go_to_cart(self):
        cart_button = WebDriverWait(self.driver,WAIT).until(
            EC.element_to_be_clickable(self.view_cart_ID)
        )
        cart_button.click()

    def order_product(self):
        proceed_to_checkout_button = WebDriverWait(self.driver, WAIT).until(
            EC.element_to_be_clickable(self.proceed_to_checkout_ID)
        )
        proceed_to_checkout_button.click()

        WebDriverWait(self.driver, WAIT).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Address Details")
        )
        place_order = WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(self.place_order_ID)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", place_order)

        WebDriverWait(self.driver, WAIT).until(
            EC.element_to_be_clickable(self.place_order_ID)
        ).click()

    def place_order(self, card_name, card_number, cvc, expiration_m, expiration_y):
        card_name_field = WebDriverWait(self.driver, WAIT).until(
            EC.element_to_be_clickable(self.card_name_ID)
        )
        card_name_field.send_keys(card_name)

        card_number_field = self.driver.find_element(*self.card_number_ID)
        card_number_field.send_keys(card_number)

        cvc_field = self.driver.find_element(*self.cvc_ID)
        cvc_field.send_keys(cvc)

        expiration_m_field = self.driver.find_element(*self.expiration_m_ID)
        expiration_m_field.send_keys(expiration_m)

        expiration_y_field = self.driver.find_element(*self.expiration_y_ID)
        expiration_y_field.send_keys(expiration_y)

        pay_and_confirm_order_button = self.driver.find_element(*self.pay_and_confirm_order_ID)
        pay_and_confirm_order_button.click()

        continue_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.continue_button_ID)
        )
        continue_button.click()


