from pages.order import Order
from pages.sign_up import SignUp
import time


def test_order(driver):
    order = Order(driver)
    order.select_products_link()
    order.add_to_cart()
    order.continue_shopping()

    sign_up = SignUp(driver)
    sign_up.select_sign_up_link()
    sign_up.new_user_sign_up("Lukasz", "jernyl@jernyl")
    sign_up.enter_account_information("male", "lukasz", "1", "January", "2003", 
    "lukasz", "pawel", "AA", "ABC", "ABCD", "Canada", "Poland", "Krakow", "31-234", "123456789" 
    )

    order.go_to_cart()
    order.order_product()
    order.place_order("Lukasz", "1", "123", "12", "2030")

    sign_up.logout()
    sign_up.login("jernyl@jernyl", "lukasz") 

    sign_up.delete_account()

