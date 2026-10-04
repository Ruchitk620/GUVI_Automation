from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HomePage:

    URL = "https://www.guvi.in/"

    LOGIN_BUTTON = (
        By.ID,
        "login-btn"
    )

    SIGNUP_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Sign up']"
    )

    COURSES_MENU = (
        By.XPATH,
        "//*[normalize-space()='Courses']"
    )

    PRACTICE_MENU = (
        By.XPATH,
        "//*[normalize-space()='Practice']"
    )

    LIVE_CLASSES_MENU = (
        By.XPATH,
        "//*[contains(normalize-space(),'LIVE Classes')]"
    )

    DOBBY = (
        By.ID,
        "zsiq_float"
    )

    COOKIE_IFRAME = (
        By.ID,
        "ccbar_iframe"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15
        )

    def open(self):

        self.driver.get(self.URL)

        self.driver.switch_to.default_content()

    def get_title(self):

        return self.driver.title

    def get_current_url(self):

        return self.driver.current_url

    def close_cookie_banner(self):

        self.driver.switch_to.default_content()

        try:

            iframe = WebDriverWait(
                self.driver,
                3
            ).until(
                EC.presence_of_element_located(
                    self.COOKIE_IFRAME
                )
            )

            self.driver.switch_to.frame(iframe)

            consent_locators = [

                (
                    By.XPATH,
                    "//button[contains("
                    "translate(normalize-space(),"
                    "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                    "'abcdefghijklmnopqrstuvwxyz'),"
                    "'accept')]"
                ),

                (
                    By.XPATH,
                    "//button[contains("
                    "translate(normalize-space(),"
                    "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                    "'abcdefghijklmnopqrstuvwxyz'),"
                    "'agree')]"
                ),

                (
                    By.XPATH,
                    "//button[contains("
                    "translate(normalize-space(),"
                    "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                    "'abcdefghijklmnopqrstuvwxyz'),"
                    "'allow')]"
                ),

                (
                    By.XPATH,
                    "//button[contains("
                    "translate(normalize-space(),"
                    "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                    "'abcdefghijklmnopqrstuvwxyz'),"
                    "'close')]"
                ),

                (
                    By.XPATH,
                    "//button[contains("
                    "translate(normalize-space(),"
                    "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                    "'abcdefghijklmnopqrstuvwxyz'),"
                    "'got it')]"
                )
            ]

            for locator in consent_locators:

                try:

                    button = WebDriverWait(
                        self.driver,
                        1
                    ).until(
                        EC.element_to_be_clickable(
                            locator
                        )
                    )

                    button.click()

                    break

                except Exception:

                    continue

        except TimeoutException:

            pass

        finally:

            self.driver.switch_to.default_content()

    def is_login_visible(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.LOGIN_BUTTON
                )
            ).is_displayed()

        except Exception:

            return False

    def is_login_clickable(self):

        try:

            return self.wait.until(
                EC.element_to_be_clickable(
                    self.LOGIN_BUTTON
                )
            ).is_enabled()

        except Exception:

            return False

    def click_login(self):

        self.close_cookie_banner()

        login_button = self.wait.until(
            EC.presence_of_element_located(
                self.LOGIN_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            login_button
        )

        try:

            self.wait.until(
                EC.element_to_be_clickable(
                    self.LOGIN_BUTTON
                )
            ).click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                login_button
            )

    def is_signup_visible(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.SIGNUP_BUTTON
                )
            ).is_displayed()

        except Exception:

            return False

    def is_signup_clickable(self):

        try:

            return self.wait.until(
                EC.element_to_be_clickable(
                    self.SIGNUP_BUTTON
                )
            ).is_enabled()

        except Exception:

            return False

    def click_signup(self):

        self.close_cookie_banner()

        signup_button = self.wait.until(
            EC.element_to_be_clickable(
                self.SIGNUP_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            signup_button
        )

        try:

            signup_button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                signup_button
            )

    def is_menu_item_visible(self, menu_name):

        locators = {
            "Courses": self.COURSES_MENU,
            "LIVE Classes": self.LIVE_CLASSES_MENU,
            "Practice": self.PRACTICE_MENU
        }

        locator = locators[menu_name]

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    locator
                )
            ).is_displayed()

        except Exception:

            return False

    def is_dobby_visible(self):

        try:

            # The current GUVI assistant/chat widget is
            # dynamically loaded after scrolling.

            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            self.wait.until(
                EC.presence_of_element_located(
                    self.DOBBY
                )
            )

            return self.driver.find_element(
                *self.DOBBY
            ).is_displayed()

        except Exception:

            return False