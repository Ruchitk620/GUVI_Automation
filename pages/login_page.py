from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    URL = "https://www.guvi.in/sign-in/"

    EMAIL = (
        By.XPATH,
        "//input[@type='email']"
    )

    PASSWORD = (
        By.XPATH,
        "//input[@type='password']"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//*[self::button or self::input or self::a]"
        "[contains("
        "translate(normalize-space(.),"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
        "'abcdefghijklmnopqrstuvwxyz'),"
        "'login') "
        "or "
        "contains("
        "translate(@value,"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
        "'abcdefghijklmnopqrstuvwxyz'),"
        "'login')]"
    )

    COOKIE_IFRAME = (
        By.ID,
        "ccbar_iframe"
    )

    ERROR_MESSAGE = (
        By.XPATH,
        "//*[normalize-space()='Incorrect Email or Password']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15
        )

    def open(self):

        self.driver.get(
            self.URL
        )

        self.driver.switch_to.default_content()

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

            self.driver.switch_to.frame(
                iframe
            )

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
                    "'got it')]"
                ),

                (
                    By.XPATH,
                    "//button[contains("
                    "translate(normalize-space(),"
                    "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                    "'abcdefghijklmnopqrstuvwxyz'),"
                    "'deny')]"
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

    def enter_email(self, email):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        )

        field.clear()

        field.send_keys(
            email
        )

    def enter_password(self, password):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        )

        field.clear()

        field.send_keys(
            password
        )

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

    def login(self, email, password):

        self.enter_email(
            email
        )

        self.enter_password(
            password
        )

        self.click_login()

    def get_current_url(self):

        return self.driver.current_url

    def is_login_page_displayed(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.EMAIL
                )
            ).is_displayed()

        except Exception:

            return False

    def is_error_displayed(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.ERROR_MESSAGE
                )
            ).is_displayed()

        except Exception:

            return False

    def get_error_message(self):

        try:

            message = self.wait.until(
                EC.visibility_of_element_located(
                    self.ERROR_MESSAGE
                )
            )

            return message.text.strip()

        except Exception:

            return ""