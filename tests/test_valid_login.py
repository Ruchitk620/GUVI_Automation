import os

from pages.login_page import LoginPage


def test_valid_login(driver):

    valid_email = os.getenv(
        "GUVI_VALID_EMAIL"
    )

    valid_password = os.getenv(
        "GUVI_VALID_PASSWORD"
    )

    assert valid_email, (
        "GUVI_VALID_EMAIL environment variable "
        "is not set"
    )

    assert valid_password, (
        "GUVI_VALID_PASSWORD environment variable "
        "is not set"
    )

    login_page = LoginPage(driver)

    login_page.open()

    print(
        f"Login page opened: "
        f"{login_page.get_current_url()}"
    )

    login_page.login(
        valid_email,
        valid_password
    )

    print(
        "Valid login credentials submitted"
    )

    login_page.wait.until(
        lambda driver:
        "/sign-in" not in driver.current_url.lower()
    )

    current_url = login_page.get_current_url()

    print(
        f"URL after valid login: {current_url}"
    )

    assert "/sign-in" not in current_url.lower(), (
        "Valid login did not navigate away from "
        f"the login page. Current URL: {current_url}"
    )

    print(
        "Valid login successful"
    )