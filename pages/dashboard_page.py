from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DashboardPage:

    HEADER = (
        By.ID,
        "header-container"
    )

    SIGNOUT = (
        By.XPATH,
        "//img[@alt='Signout']"
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

            got_it_button = (
                By.XPATH,
                "//button[contains("
                "translate(normalize-space(),"
                "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                "'abcdefghijklmnopqrstuvwxyz'),"
                "'got it')]"
            )

            try:

                button = WebDriverWait(
                    self.driver,
                    3
                ).until(
                    EC.element_to_be_clickable(
                        got_it_button
                    )
                )

                button.click()

                print(
                    "Cookie 'Got it!' clicked"
                )

            except Exception:

                print(
                    "Cookie 'Got it!' button not found"
                )

        except TimeoutException:

            print(
                "Cookie banner not present"
            )

        finally:

            self.driver.switch_to.default_content()

    def click_account_dropdown(self):

        self.driver.switch_to.default_content()

        self.wait.until(
            EC.presence_of_element_located(
                self.HEADER
            )
        )

        print(
            "GUVI header found"
        )

        def find_account_dropdown(driver):

            try:

                header = driver.find_element(
                    *self.HEADER
                )

                dropdown = driver.execute_script(
                    """
                    const header = arguments[0];

                    const svgs = header.querySelectorAll(
                        "svg.lucide-chevron-down"
                    );

                    for (const svg of svgs) {

                        const path = svg.querySelector("path");

                        if (
                            path &&
                            path.getAttribute("d") ===
                            "m6 9 6 6 6-6"
                        ) {

                            return svg;
                        }
                    }

                    return null;
                    """,
                    header
                )

                return dropdown

            except Exception:

                return False

        dropdown = self.wait.until(
            find_account_dropdown
        )

        print(
            "Account dropdown found"
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            dropdown
        )

        self.driver.execute_script(
            """
            arguments[0].dispatchEvent(
                new MouseEvent(
                    'click',
                    {
                        bubbles: true,
                        cancelable: true,
                        view: window
                    }
                )
            );
            """,
            dropdown
        )

        print(
            "Account dropdown clicked"
        )

    def click_logout(self):

        self.driver.switch_to.default_content()

        signout = self.wait.until(
            EC.presence_of_element_located(
                self.SIGNOUT
            )
        )

        print(
            "Signout icon found"
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            signout
        )

        self.driver.execute_script(
            "arguments[0].click();",
            signout
        )

        print(
            "Signout clicked"
        )

    def logout(self):

        self.close_cookie_banner()

        self.click_account_dropdown()

        self.click_logout()