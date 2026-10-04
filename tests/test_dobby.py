import time

from pages.home_page import HomePage


def test_dobby_guvi_assistant_present(driver):

    home_page = HomePage(driver)

    home_page.open()

    print(
        "GUVI homepage opened"
    )

    time.sleep(3)

    print(
        "Waiting for assistant to load"
    )

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(5)

    print(
        "Scrolled to bottom and waited for assistant"
    )

    assert home_page.is_dobby_visible(), (
        "GUVI assistant/chat widget is not present"
    )

    print(
        "GUVI Dobby/Chat Assistant is present"
    )