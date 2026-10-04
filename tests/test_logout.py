import os

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_logout(driver):

    valid_email = os.getenv(
        "GUVI_VALID_EMAIL"
    )

    valid_password = os.getenv(
        "GUVI_VALID_PASSWORD"
    )

    assert valid_email, (
        "GUVI_VALID_EMAIL environment variable is not set"
    )

    assert valid_password, (
        "GUVI_VALID_PASSWORD environment variable is not set"
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

    login_page.wait.until(
        lambda driver:
        "/sign-in" not in driver.current_url.lower()
    )

    print(
        "Valid login successful"
    )

    dashboard_page = DashboardPage(driver)

    dashboard_page.close_cookie_banner()

    print(
        "Cookie banner handled"
    )

    dashboard_page.click_account_dropdown()

    print(
        "Account dropdown clicked"
    )

    dashboard_page.click_logout()

    print(
        "Signout clicked"
    )

    print(
        f"URL after Signout: "
        f"{driver.current_url}"
    )

    print(
        "Verifying logged-out state..."
    )

    def signout_control_disappeared(driver):

        try:

            signout_elements = driver.find_elements(
                *dashboard_page.SIGNOUT
            )

            for element in signout_elements:

                if element.is_displayed():

                    return False

            return True

        except Exception:

            return True

    login_page.wait.until(
        signout_control_disappeared
    )

    signout_elements = driver.find_elements(
        *dashboard_page.SIGNOUT
    )

    visible_signout_elements = [

        element
        for element in signout_elements
        if element.is_displayed()
    ]

    assert len(visible_signout_elements) == 0, (
        "Signout control is still visible after logout"
    )

    print(
        "Signout control is no longer visible"
    )

    print(
        "Logout successful"
    )