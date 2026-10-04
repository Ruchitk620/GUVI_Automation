from pages.home_page import HomePage
from pages.signup_page import SignupPage


def test_signup_button_visible_clickable_and_navigation(driver):

    home_page = HomePage(driver)

    home_page.open()

    assert home_page.is_signup_visible(), \
        "Sign-Up button is not visible"

    print("Sign-Up button is visible")

    assert home_page.is_signup_clickable(), \
        "Sign-Up button is not clickable"

    print("Sign-Up button is clickable")

    home_page.click_signup()

    signup_page = SignupPage(driver)

    assert signup_page.is_page_loaded(), \
        f"Sign-Up page did not load. Current URL: {signup_page.get_current_url()}"

    print(
        f"Sign-Up page opened successfully: "
        f"{signup_page.get_current_url()}"
    )