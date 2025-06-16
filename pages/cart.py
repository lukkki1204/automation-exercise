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

WAIT = 2

class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.continue_button_ID = (By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block")

    
    def add_multiple_products(self, produts_amount):
        for product in range(1, produts_amount + 1):
            selector = f'a[data-product-id="{product}"]'
            button = WebDriverWait(self.driver, WAIT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            ActionChains(self.driver).move_to_element(button).perform()

            WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            ).click()

            continue_button = WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(self.continue_button_ID)
            )