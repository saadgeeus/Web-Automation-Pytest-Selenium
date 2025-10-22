from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_search_add_to_cart(driver):
    # Step 1: Login
    LoginPage(driver).open()
    LoginPage(driver).login("standard_user", "secret_sauce")

    # Step 2: Add first product to cart
    products = ProductsPage(driver)
    products.add_first_product_to_cart()

    # Step 3: Verify cart count updated
    assert products.get_cart_count() == "1"
