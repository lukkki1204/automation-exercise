from pages.sign_up import SignUp
import time

def test_sign_up_link(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()

    assert sign_up.header_visibility(sign_up.sign_up_text_ID).is_displayed(), "Signup page not opened"

def test_sign_up_positive(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("Lukasz", "domiosekpiateczek@domiosekpiateczek")
    
    assert sign_up.header_visibility(sign_up.gender_male_mark_ID), "Signup didn't go properly"

def test_sign_up_negative_blank_name(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("", "dominik@dominik")

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
    sign_up.new_user_sign_up("Lukasz", "monikarzadzka@monikarzadzka")
    sign_up.enter_account_information("male", "lukasz", "1", "January", "2003", 
    "lukasz", "pawel", "AA", "ABC", "ABCD", "Canada", "Poland", "Krakow", "31-234", "123456789" 
    )
    sign_up.delete_account()

    assert sign_up.header_visibility(sign_up.signed_up_info_ID).text == "ACCOUNT DELETED!"

def test_login_positive(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("Lukasz", "dominopiatas@dominopiatas")
    sign_up.enter_account_information("male", "lukasz", "1", "January", "2003", 
    "lukasz", "pawel", "AA", "ABC", "ABCD", "Canada", "Poland", "Krakow", "31-234", "123456789" 
    )
    sign_up.logout()
    sign_up.login("dominopiatas@dominopiatas", "lukasz") 

    assert sign_up.header_visibility(sign_up.login_info_ID)

    sign_up.delete_account()

def test_login_negative(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("Lukasz", "krzysiumaberdka@krzysiumaberdka")
    sign_up.enter_account_information("male", "lukasz", "1", "January", "2003", 
    "lukasz", "pawel", "AA", "ABC", "ABCD", "Canada", "Poland", "Krakow", "31-234", "123456789" 
    )
    sign_up.logout()
    sign_up.login("jasiek", "") 

    assert sign_up.header_visibility(sign_up.login_password_field_ID)
    
    sign_up.driver.refresh()
    sign_up.login("krzysiumaberdka@krzysiumaberdka", "lukasz")
    sign_up.delete_account()

def test_register_with_existing_email(driver):
    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("Lukasz", "dziadziujasiu@dziadziujasiu")
    sign_up.enter_account_information("male", "lukasz", "1", "January", "2003", 
    "lukasz", "pawel", "AA", "ABC", "ABCD", "Canada", "Poland", "Krakow", "31-234", "123456789" 
    )
    sign_up.logout()
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("Lukasz", "")

    assert sign_up.header_visibility(sign_up.login_password_field_ID), 'sth went wrong'

    sign_up.login("dziadziujasiu@dziadziujasiu", "lukasz")
    sign_up.delete_account()
