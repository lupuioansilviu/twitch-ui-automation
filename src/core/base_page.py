from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text: str):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    def dom_ready(self):
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def scroll_down(self, times: int = 1):
        for _ in range(times):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def dismiss_overlays(self) -> bool:
        """
        I left locator here, but of course, we can create a new Locators.page to store everything there
        """
        try:
            accept_btn = self.driver.find_element(
                By.XPATH,
                "//button[.//div[normalize-space()='Accept'] or normalize-space()='Accept']"
            )
            if accept_btn.is_displayed() and accept_btn.is_enabled():
                accept_btn.click()
                return True
        except Exception:
            pass

        return False

    def click_with_overlay_handling(self, locator, attempts: int = 3):
        last_err = None
        for _ in range(attempts):
            try:
                self.click(locator)
                return
            except (TimeoutException, StaleElementReferenceException) as e:
                last_err = e
                self.dismiss_overlays()
        raise last_err