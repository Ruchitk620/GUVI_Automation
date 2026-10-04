from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:

    URL = "https://www.guvi.in/register/"

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            15
        )

    def get_current_url(self):

        return self.driver.current_url

    def is_page_loaded(self):

        try:

            self.wait.until(
                EC.url_contains(
                    "/register"
                )
            )

            return True

        except Exception:

            return False