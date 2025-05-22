from pages.sign_up import SignUp
import time

def test_sign_up_link(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()

    assert sign_up.header_visibility(sign_up.sign_up_text_ID).is_displayed(), "Signup page not opened"

def test_sign_up_positive(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("Lukasz", "damina@damian")
    
    assert sign_up.header_visibility(sign_up.name_field_ID), "Signup didn't go properly"

def test_sign_up_negative_blank_name(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("", "damina@damian")

    assert sign_up.header_visibility(sign_up.sign_up_text_ID).is_displayed()

def test_sign_up_negative_blank_email(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("Lukasz", "")

    assert sign_up.header_visibility(sign_up.sign_up_text_ID).is_displayed()

def test_sign_up_negative_blank_name_and_email(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("", "")

    assert sign_up.header_visibility(sign_up.sign_up_text_ID).is_displayed()

def test_sign_up_negative_no_at_sign(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("Lukasz", "Lukasz")

    assert sign_up.header_visibility(sign_up.sign_up_text_ID).is_displayed()

def test_register_positive(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("Lukasz", "pawel@pawel")
    sign_up.enter_account_information("male", "lukasz", "1", "January", "2003", 
    "lukasz", "pawel", "AA", "ABC", "ABCD", "Canada", "Poland", "Krakow", "31-234", "123456789" 
    )

    assert sign_up.header_visibility(sign_up.signed_up_info_ID).text == "ACCOUNT CREATED!"
