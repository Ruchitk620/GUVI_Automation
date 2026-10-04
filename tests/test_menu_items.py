from pages.home_page import HomePage


def test_main_menu_items_visible_and_accessible(driver):

    home_page = HomePage(driver)

    home_page.open()

    menu_items = [
        "Courses",
        "Practice",
        "LIVE Classes"
    ]

    for menu_name in menu_items:

        assert home_page.is_menu_item_visible(
            menu_name
        ), f"{menu_name} menu is not visible"

        print(
            f"{menu_name} menu is visible and accessible"
        )