from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.find(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False
