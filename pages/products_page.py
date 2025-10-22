from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):
    FIRST_ADD_TO_CART = (By.XPATH, "(//button[text()='Add to cart'])[1]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")

    def add_first_product_to_cart(self):
        self.click(self.FIRST_ADD_TO_CART)

    def open_cart(self):
        self.click(self.CART_ICON)

    def get_cart_count(self):
        return self.find(self.CART_COUNT).text
