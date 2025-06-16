from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT = 2

class SignUp:
    def __init__(self, driver):
        self.driver = driver
        self.sign_up_link_ID = (By.LINK_TEXT, "Signup / Login")
        self.name_field_ID = (By.NAME, "name")
        self.email_field_ID = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
        self.sign_up_button_ID = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')
        self.gender_male_mark_ID = (By.ID, "id_gender1")
        self.gender_female_mark_ID = (By.ID, "id_gender2")
        self.password_field_ID = (By.ID, "password")
        self.day_of_birth_field_ID = (By.ID, "days")
        self.month_of_birth_ID = (By.ID, "months")
        self.year_of_birth_ID = (By.ID, "years")
        self.first_name_field_ID = (By.ID, "first_name")
        self.last_name_field_ID = (By.ID, "last_name")
        self.company_field_ID = (By.ID, "company")
        self._address_field_ID = (By.ID, "address1")
        self.address2_field_ID = (By.ID, "address2")
        self.country_dropdown_ID = (By.ID, "country")
        self.state_field_ID = (By.ID, "state")
        self.city_field_ID = (By.ID, "city")
        self.zipcode_field_ID = (By.ID, "zipcode")
        self.mobile_number_field_ID = (By.ID, "mobile_number")
        self.create_account_button_ID = (By.CSS_SELECTOR, '.btn.btn-default')
        self.sign_up_text_ID = (By.XPATH, '//h2[text()="New User Signup!"]')
        self.signed_up_info_ID = (By.CSS_SELECTOR, ".title.text-center")
        self.continue_button_ID = (By.CSS_SELECTOR, ".btn.btn-primary")
        self.delete_account_link_ID = (By.XPATH, '//a[@href="/delete_account"]')
        self.logout_button_ID = (By.XPATH, '//a[@href="/logout"]')
        self.login_email_field_ID = (By.CSS_SELECTOR, 'input[data-qa="login-email"]')
        self.login_password_field_ID = (By.NAME, "password")
        self.login_button_ID = (By.CSS_SELECTOR, '.btn.btn-default')
        self.login_info_ID = (By.CSS_SELECTOR, ".fa.fa-user")
        self.existing_email_used_ID = (By.XPATH, 'p[text()="Email Address already exist!"]')

    def select_sign_up_link(self):
        element = WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(self.sign_up_link_ID)
        )
        element.click()
    
    def new_user_sign_up(self, name, email):
        name_field = WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(self.name_field_ID)
        )
        email_field = self.driver.find_element(*self.email_field_ID)
        sign_up_button = self.driver.find_element(*self.sign_up_button_ID)

        name_field.send_keys(name)
        email_field.send_keys(email)
        sign_up_button.click()

    def enter_account_information(self, gender, password, day, month, year, first_name, last_name, company, address,
        address2, country, state, city, zipcode, mobile_number
        ):
        if gender == "male":
            title_field = WebDriverWait(self.driver, WAIT).until(
                EC.presence_of_element_located(self.gender_male_mark_ID)
            )
            title_field.click()
        else:
            title_field = WebDriverWait(self.driver, WAIT).until(
                EC.presence_of_element_located(self.gender_female_mark_ID)
            )
            title_field.click()
        
        password_field = self.driver.find_element(*self.password_field_ID)
        password_field.send_keys(password)

        dropdown_day = Select(self.driver.find_element(*self.day_of_birth_field_ID))
        dropdown_day.select_by_visible_text(day)

        dropdown_month = Select(self.driver.find_element(*self.month_of_birth_ID))
        dropdown_month.select_by_visible_text(month)

        dropdown_year = Select(self.driver.find_element(*self.year_of_birth_ID))
        dropdown_year.select_by_visible_text(year)

        first_name_field = self.driver.find_element(*self.first_name_field_ID)
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(*self.last_name_field_ID)
        last_name_field.send_keys(last_name)

        company_field = self.driver.find_element(*self.company_field_ID)
        company_field.send_keys(company)

        address_field = self.driver.find_element(*self._address_field_ID)
        address_field.send_keys(address)

        address2_field = self.driver.find_element(*self.address2_field_ID)
        address2_field.send_keys(address2)

        dropdown_country = Select(self.driver.find_element(*self.country_dropdown_ID))
        dropdown_country.select_by_visible_text(country)

        state_field = self.driver.find_element(*self.state_field_ID)
        state_field.send_keys(state)

        city_field = self.driver.find_element(*self.city_field_ID)
        city_field.send_keys(city)

        zipcode_field = self.driver.find_element(*self.zipcode_field_ID)
        zipcode_field.send_keys(zipcode)

        mobile_number_field = self.driver.find_element(*self.mobile_number_field_ID)
        mobile_number_field.send_keys(mobile_number)
        mobile_number_field.send_keys(Keys.RETURN)

        continue_button = WebDriverWait(self.driver, WAIT).until(
            EC.element_to_be_clickable(self.continue_button_ID)
        )
        continue_button.click()

    def delete_account(self):
        delete_account_link = WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(self.delete_account_link_ID)
        )
        delete_account_link.click()

    def logout(self):
        logout_button = WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(self.logout_button_ID)
        )
        logout_button.click()

    def login(self, email, password):
        email_field = WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(self.login_email_field_ID)
        )
        password_field = self.driver.find_element(*self.login_password_field_ID)

        email_field.send_keys(email)
        password_field.send_keys(password)
        
        login_button = self.driver.find_element(*self.login_button_ID)
        login_button.click()

    def header_visibility(self, locator):
        return WebDriverWait(self.driver, WAIT).until(
            EC.visibility_of_element_located(locator)
        )
        