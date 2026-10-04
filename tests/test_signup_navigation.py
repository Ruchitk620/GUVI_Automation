from pages.home_page import HomePage
from pages.signup_page import SignupPage


def test_signup_navigation_url(driver):

    home_page = HomePage(driver)

    home_page.open()

    home_page.click_signup()

    signup_page = SignupPage(driver)

    current_url = signup_page.get_current_url()

    print(
        f"Current Sign-Up URL: {current_url}"
    )

    assert "/register/" in current_url.lower(), (
        f"Sign-Up navigation URL is incorrect. "
        f"Expected '/register/' in URL, "
        f"Actual: {current_url}"
    )

    print(
        "Sign-Up navigation URL is correct"
    )