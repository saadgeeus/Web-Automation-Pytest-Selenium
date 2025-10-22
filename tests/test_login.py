from pages.login_page import LoginPage


def test_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")

    # Verify successful login by checking page URL
    assert "inventory" in driver.current_url
