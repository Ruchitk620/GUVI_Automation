from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_button_visible_clickable_and_navigation(driver):

    home_page = HomePage(driver)

    home_page.open()

    assert home_page.is_login_visible(), \
        "Login button is not visible"

    print("Login button is visible")

    assert home_page.is_login_clickable(), \
        "Login button is not clickable"

    print("Login button is clickable")

    home_page.click_login()

    login_page = LoginPage(driver)

    assert login_page.get_current_url().lower().startswith(
        LoginPage.URL
    ), (
        f"Login navigation failed. "
        f"Current URL: {login_page.get_current_url()}"
    )

    print(
        f"Login page opened successfully: "
        f"{login_page.get_current_url()}"
    )