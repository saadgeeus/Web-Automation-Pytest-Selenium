from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Locators
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    # Step 1: Start checkout from the cart page
    def start_checkout(self):
        self.click(self.CHECKOUT_BTN)

    # Step 2: Fill out information form
    def fill_information(self, first_name, last_name, postal_code):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BTN)

    # Step 3: Complete the order
    def finish_checkout(self):
        self.click(self.FINISH_BTN)

    # Step 4: Verify order completion
    def is_order_complete(self):
        return self.is_displayed(self.COMPLETE_HEADER)
