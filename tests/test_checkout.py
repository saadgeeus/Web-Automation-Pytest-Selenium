from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage


def test_checkout(driver):
    # Step 1: Login
    LoginPage(driver).open()
    LoginPage(driver).login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    products = ProductsPage(driver)
    products.add_first_product_to_cart()
    products.open_cart()

    # Step 3: Start checkout
    checkout = CheckoutPage(driver)
    checkout.start_checkout()

    # Step 4: Fill and finish checkout
    checkout.fill_information("Saad", "Khan", "12345")
    checkout.finish_checkout()

    # Step 5: Verify completion
    assert checkout.is_order_complete()
