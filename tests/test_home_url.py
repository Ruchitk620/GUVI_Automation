from pages.home_page import HomePage


def test_guvi_homepage_url(driver):

    home_page = HomePage(driver)

    home_page.open()

    current_url = home_page.get_current_url()

    print(
        f"Current URL: {current_url}"
    )

    assert "guvi.in" in current_url.lower(), \
        "GUVI homepage did not load correctly"

    print(
        "GUVI homepage loaded successfully"
    )