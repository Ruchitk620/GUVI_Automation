from pages.home_page import HomePage


def test_guvi_homepage_title(driver):

    home_page = HomePage(driver)

    home_page.open()

    actual_title = home_page.get_title()

    print(
        f"Actual page title: {actual_title}"
    )

    expected_title = "HCL GUVI | Learn to code in your native language"

    assert actual_title == expected_title, (
        f"Title mismatch. "
        f"Expected: '{expected_title}', "
        f"Actual: '{actual_title}'"
    )

    print(
        "GUVI homepage title is correct"
    )