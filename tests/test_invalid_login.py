from pages.login_page import LoginPage


def test_invalid_login(driver):

    login_page = LoginPage(driver)

    login_page.open()

    print(
        f"Login page opened: "
        f"{login_page.get_current_url()}"
    )

    invalid_email = "invalid_test_user_123456@example.com"
    invalid_password = "WrongPassword123!"

    login_page.login(
        invalid_email,
        invalid_password
    )

    print(
        "Invalid login credentials submitted"
    )

    if login_page.is_error_displayed():

        error_message = login_page.get_error_message()

        print(
            f"Error message displayed: {error_message}"
        )

        assert error_message != "", \
            "Error element exists but contains no message"

        print(
            "Invalid login scenario handled successfully"
        )

    else:

        current_url = login_page.get_current_url()

        assert "/sign-in" in current_url.lower(), (
            "Invalid login did not remain on the login page "
            "and no error message was detected. "
            f"Current URL: {current_url}"
        )

        print(
            "Invalid login was rejected and user remained "
            "on the login page"
        )