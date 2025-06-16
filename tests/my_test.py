from pages.cart import Cart

def test_cart(driver):
    cart = Cart(driver)
    cart.add_multiple_products(2)

